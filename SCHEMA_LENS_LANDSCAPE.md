# Schema Lens — Landscape & Encoding Exploration

**Status:** exploration / decision-gathering. No generator or artifact changes made yet.
**Question on the table:** should CS2OpenDev-Docs publish a "Schema Lens" — a chainable,
build-to-build definition of how CS2 entity schemas evolve — and if so, how should it be
encoded as an output artifact?

This document explores that landscape. It reads the prior DemoViewer.NET (DVN)
investigation (`C:\dev\DemoViewer.NET\docs\schema-lens\*`) but is **not bound to it**; the
goal is a robust, consistent artifact this repo can publish so downstream users
(CS2OpenDev-SDK, DVN, any demo/analytics tool) can implement forward/backward
schema compatibility more easily.

---

## 1. The reframe: what changed since the prior investigation

The DVN docs designed Schema Lens as a **downstream, hand-authored** product. Every
migration file — the genesis baseline and each per-patch delta — was to be written by a
human (or "a dedicated agent"), because DVN's only input was a *single current schema
dump* from the old `cs2-opendocs` mirror. It had no history to diff against.

That constraint is gone. This repo now sits on **CS2OpenDev-SchemaTracker**, which commits
a full `entity_schema.json` for **every historical CS2 build** — 376 builds from the
in-scope baseline `10832117` to the current `24134959`, i.e. **375 consecutive
transitions**. The complete schema-evolution history is therefore *machine-derivable*:
`delta(build_i, build_i+1) = diff(snapshot_i, snapshot_i+1)`.

This is the single most important fact for the design. It splits Schema Lens into two
layers that the prior investigation had fused together:

| Layer | Content | Objective? | Right home |
|---|---|---|---|
| **A. Schema-evolution delta** | field added/removed/retyped/moved; class added/removed/re-parented/resized; enum member churn | **Yes** — derivable by diffing committed snapshots | **This repo** (publish it) |
| **B. Wire-encoding facts** | effective wire width, sub-service flattening, networked-or-not, quantization | Partly — *not* in the schema dump; needs a demo's `FlattenedSerializer` or a future wire dump | Out of scope today (note as a separate axis) |
| **C. Consumer mapping policy** | canonical → `targetProperty` name, `transform` (BoolFromInt…), `fallbackDefault`, curated class set, slot assignment | **No** — per-tool policy | Stays downstream (DVN/SDK) |

The DVN "Schema Lens migration file" bundles A + B + C into one hand-authored artifact.
**What this repo should publish is Layer A alone** — the objective substrate every Lens is
built on. Layers B and C are tool-specific and stay downstream; publishing A *enables*
them without over-reaching into policy this repo has no authority over.

To avoid conflating vocabulary: DVN's `LensState` is a *resolved downstream product*. What
we publish is better called the **Schema Evolution Graph** (or "delta chain"). It is
exactly the user's "structured definition for how a theoretical translation layer would
need to modify the old version to work with the next build" — nothing more, nothing less.

---

## 2. What the data can and cannot tell us

### 2.1 What `entity_schema.json` carries (per build, per class)

`alignment, cppName, fields[], flags, flags2, metadata[], module, name, parents[],
projectName, singleInheritanceDepth, multipleInheritanceDepth, size, staticFields[]`

Per field: `name, offset (string int), type {category,name,module,count,inner…},
typeModule, metadata[]`. Enums carry `members[]{name,value}`, underlying size/alignment.

That is the **C++ compile-time class layout** walked from the shipped binary. It is rich
enough to compute, for any build pair, every structural change at field granularity.

### 2.2 What the existing `changelog.json` carries (and why it is not enough)

SchemaTracker already emits a per-build `changelog.json` (`fromBuild`→`toBuild`, families:
classes/enums/convars/commands/…). But for `classes` its `changed` entries are **coarse**:
across all 375 transitions the only field-level keys ever emitted are `field_count`
(849×) and `parent` (116×). It never says *which* field changed, was added, renamed,
retyped, or moved. Totals across all history: **+714 / ~955 changed / −290 classes**,
**+28 / −1 enums**.

So the changelog is a good *index* ("this build touched these classes") but a poor
*migration source*. The real substrate is the pairwise snapshot diff. (See §6 for the
open question of *where* that richer diff should be computed — here, or upstream in
SchemaTracker where both snapshots are already in hand.)

### 2.3 The hard boundary: schema ≠ wire

SchemaTracker walks the **C++ schema**, not the **network serialization**. It does not know
a field's effective wire width, whether it is networked, how sub-services are flattened,
or how values are quantized. These are exactly DVN's documented gaps:

- **G1 shadow-renamed sub-services** — `m_pWeaponServices.m_hActiveWeapon` flattening is a
  wire artifact, invisible to the schema header.
- **G2 type promotion** — `m_bHasHelmet` is `bool` in the schema but `int32` on the wire.
- **G4 declared-int-but-uint64-on-wire** — `m_steamID`, `m_nButtons`.

**Implication:** the delta chain robustly answers *"how did the C++ schema change"*
(offsets, renames, type shifts, struct reshuffles, member churn). It cannot by itself
answer *"how did the networked representation change."* We should scope and label the
artifact as **schema-level** and note wire-level as a distinct future axis. Crucially,
several real downstream needs are served by schema-level deltas alone — see §7.

---

## 3. The chain model (baseline + increments)

Matches the user's stated design, with one simplification the snapshot history unlocks.

- **Baseline anchor:** oldest in-scope build `10832117`. The baseline is not a synthetic
  "genesis migration" — it *is* that build's `entity_schema.json`. No hand authoring.
- **Increments:** one delta doc per consecutive transition `B_i → B_i+1` (375 of them).
  To bring an instance captured under build *X* forward to build *Y*, apply the deltas for
  every transition in `[X, Y)` in order.
- **Backward:** each op is defined to be **invertible** (add↔remove, rename forward↔back,
  typeShift carries both endpoints), so the same chain walks backward for the (currently
  unneeded, but designed-for) "new schema in an old tool" case. Ops that are *not* cleanly
  invertible (lossy type-narrowing, a field split) are flagged `invertible: false`.

**The simplification:** because SchemaTracker keeps *every full snapshot*, a delta between
**any** two builds is just `diff(snapshot_X, snapshot_Y)` — you never have to squash a run
of increments to re-baseline. Re-baselining is free:

- Publish the **adjacent-transition chain** (small deltas, the canonical incremental form).
- Additionally publish **periodic baselines** (full snapshots already exist) plus
  **squashed deltas** from each baseline, so a consumer whose input build is near a recent
  baseline takes few hops instead of hundreds.
- Both come from the *same diff engine*; the chain-vs-squash choice is purely a
  materialization decision, not two separate pipelines.

The incremental chain matters mainly for the *downstream* consumer who wants to ship a
compact artifact rather than 376 full snapshots. If they can afford two full snapshots,
they can compute any delta themselves; the published chain is the convenience layer.

---

## 4. Op vocabulary — grounded in what is actually diffable

Diff keyed on `(module, className)` then field `name`. Every op below is computable from
two `entity_schema.json` snapshots with no wire data.

**Class-level**
- `addClass` / `removeClass`
- `reparentClass` (`parents[]` changed — 116 real occurrences)
- `resizeClass` / `realignClass` (`size` / `alignment` shifted)
- `changeClassFlags`

**Field-level (within a matched class)**
- `addField` / `removeField`
- `changeFieldType` (`type.category`/`name` changed — the "primitive mutation" case)
- `changeFieldOffset` (offset moved — the "structural reshuffle" case; load-bearing for
  offset-keyed demo baseline decoding)
- `changeFieldMetadata`

**Enum-level**
- `addEnum` / `removeEnum`, `addMember` / `removeMember`, `changeMemberValue`

### 4.1 The rename problem (why we emit *candidates*, not assertions)

A rename appears in a naive diff as `removeField(old) + addField(new)`. Promoting that to
`rename(old→new)` is a **heuristic**: same class, matching type, same/adjacent offset →
high-confidence candidate. But the schema dump **cannot prove** a rename — Valve may have
removed A and added an unrelated B at the same offset. So:

- Always emit the objective facts (`removeField` + `addField`).
- *Additionally* emit `renameCandidate {from, to, confidence, evidence:[offsetMatch,
  typeMatch,sizeMatch]}` as an annotation.
- A human (or downstream) promotes a candidate to a confirmed `rename` via an **overlay**
  (§5). This is the honest split: machine proposes, human confirms.

This is also where DVN's **G3 (removed-then-restored fields / full alias history)** is
answered directly — the alias chain falls out of confirmed renames across the history,
which is exactly the `field-history.json` DVN asked upstream to provide.

---

## 5. Human overlays on top of the derived deltas

This repo already has an overlay mechanism (`docs/overlays/`, `(module,name)`-keyed,
community-annotated, merged by the generator). It is the natural home for the judgment the
machine cannot supply:

- **Confirmed renames** (promoting a `renameCandidate`).
- **Breaking-change guards & suggestions** (§8).
- **Semantic notes** (unit changes, meaning redefinitions, field splits).
- Optionally, *suggested* `transform` / naming hints — but flagged clearly as suggestions,
  since Layer C is downstream policy (§1).

Pipeline: **derived deltas (machine) + `docs/overlays/schema-lens/*.yml` (human) →
published delta artifact.** Same shape as the existing schema/overlay flow.

---

## 6. Where the diff engine should live (genuine fork)

The current generator only materializes the **latest** build (partial + sparse submodule).
Diffing across history needs ≥2 builds present. Two architectures:

**Option A — compute the delta chain in this repo (Docs).**
A separate, occasionally-run job does a wider/full checkout of SchemaTracker, computes the
whole chain once, and commits the artifacts. The normal 4-hourly job then only appends the
newest transition (needs the two latest builds sparse-checked-out). Keeps SchemaTracker
purely a data source; all presentation + overlays live here.

**Option B — compute field-level deltas upstream in SchemaTracker, publish here.**
SchemaTracker already emits `changelog.json` at build time, when *both* snapshots are
cheaply in hand — it is the natural place to produce the *rich* field-level diff too
(today's changelog is just coarse). Docs then consumes the upstream delta, adds human
overlays + prose + the combined `field_history.json`, and publishes. Cleaner separation
(diff logic next to the data that produces it), at the cost of an upstream change to
SchemaTracker (which is mid-refactor anyway — possibly the right moment).

This is the biggest decision and it is architectural, not cosmetic.

### 6.1 Resolution (recommended): Option B with a hybrid boundary

The deciding factor is that this repo's data acquisition is deliberately **partial +
sparse — only ever fetch the latest build**. Option A breaks that: diffing across history
forces Docs into a wide/full checkout (hundreds of builds, multi-GB), regressing the
architecture just built, for output whose source of truth is really the tracker.

Option B keeps the diff next to the data. The refinement that removes B's only downside:
have SchemaTracker emit, **at the latest build**, a *cumulative* evolution artifact (the
full chain + derived `field_history`), recomputed each build from the snapshots it already
holds locally. Then **Docs sparse-checkouts only the latest build — exactly as today — and
reads one artifact.** No history fetch; no design regression. The heavy "hold all
snapshots" work stays in SchemaTracker, which holds them anyway.

Ownership split (mirrors the objective/subjective split of §1):

| Concern | Owner |
|---|---|
| Objective field-level delta + `field_history` (Layer A facts) | **SchemaTracker** (deterministic producer) |
| Rename *confirmation*, breaking-change guards, semantic notes (overlays) | **Docs** |
| Presentation: pages, portable combined JSON, cross-links | **Docs** |

Prerequisite: SchemaTracker's in-flight refactor owns emitting the cumulative
schema-evolution artifact (its `changelog.json` mechanism is ~90% there — it needs to go
field-level and add a cumulative roll-up). Mid-refactor is the cheapest moment to fold in.

Pick Option A only if Schema Lens must ship without touching SchemaTracker at all, accepting
a periodic full-history checkout job as the cost.

### 6.2 Resolved direction: Layer A is a SchemaTracker feature

On reflection the boundary is sharper than "Option B." **Almost all of Layer A production
belongs upstream**, for two reasons:

1. The per-transition delta is literally an *enrichment of the existing `changelog.json`* —
   the same build-time diff over the same two snapshots SchemaTracker already holds, writing
   field-level ops (§4) instead of `field_count`/`parent`. An improvement to existing logic.
2. The cumulative `field_history` roll-up **cannot** live in Docs — it needs every snapshot,
   which only SchemaTracker holds. This is the non-trivial part of Layer A, and it is *forced*
   upstream. The part that isn't formatting is exactly the part Docs can't do.

**Docs' role thins to two things it is genuinely the right home for:**

- **Human overlay layer** — rename *confirmation* (promoting a `renameCandidate`),
  breaking-change guards (§8), semantic notes. This deliberately does **not** go upstream:
  SchemaTracker's identity is deterministic machine-only extraction, and curated human data
  would blur it. The tracker emits candidates (mechanical, with evidence); Docs confirms.
- **Presentation** — the Jekyll page + portable, cross-linked rendering.

**The one seam this creates:** `field_history` becomes two-tier. SchemaTracker emits the
**mechanical** history (candidate-based alias chains, type history). Docs produces the
**authoritative** history by folding in overlay-confirmed renames. Consistent with the
objective/subjective split — named here so it is not a surprise at build time.

**Consequence to accept:** this makes Schema Lens *primarily a SchemaTracker deliverable*.
The CS2OpenDev-Docs generator work is small (consume one artifact, merge overlays, render).
The design spec (op vocabulary §4, artifact shape §9, safety model §8) should be authored
against SchemaTracker's in-flight refactor as the cheapest moment to fold it in.

---

## 7. Concrete downstream value this unlocks *today* (schema-level only)

Even scoped to Layer A (no wire data), the delta chain delivers real wins:

1. **Field-history / alias resolution** — replaces DVN's hand-authored genesis and answers
   G3. "When did `m_iHealthValue` first appear, what did it supersede, what is its full
   alias chain" becomes a lookup, derived from real historical dumps rather than public
   memory.
2. **Offset-keyed demo migration** — for tools that store entity instances by C++ offset
   (baselines in demos), `changeFieldOffset` across builds is precisely the reshuffle map
   needed to reinterpret an old instance under a new layout.
3. **Type-shift awareness** — `changeFieldType` flags exactly where a consumer's decode
   assumptions break, per build.
4. **Break radar** — a per-build "what structurally changed" that is *field-precise*,
   unlike today's `field_count`-only changelog. Useful as a docs page in its own right.

Wire-dependent needs (G1/G2/G4, DVN's lane routing) still require a wire source and stay
downstream — but the schema substrate they layer on is now published and consistent.

---

## 8. Breaking changes & guarding

Per the user's ask, classify each op by migration safety and, for the unsafe ones, carry a
**suggested guard** so downstream tooling degrades instead of breaking.

| Class | Examples | Forward-migration effect |
|---|---|---|
| **Safe / lossless** | `addField`, `addClass`, metadata change, confirmed `rename`, `changeFieldOffset` | Older instance simply lacks new field → `fallbackDefault`; re-decodable |
| **Lossy** | `removeField`, type *narrowing* (int64→int32) | Data may be dropped/truncated on forward migration; acceptable, flagged |
| **True breaking** | semantic redefinition at same name+offset, field split, unit change (rad↔deg), re-parent that changes inherited layout | **Not detectable from schema alone** — must be overlay-annotated |

Each op carries `safety: safe|lossy|breaking` (machine sets safe/lossy; overlays raise to
breaking). Each breaking op carries a `guard` suggestion — one of:
`dropField` (route to fallback), `defaultFill`, `freezeLastKnown`, `exposeRaw` (surface the
uninterpreted value and let the consumer decide) — plus a free-text `note`. The goal the
user stated: *guard the tooling so it keeps working as much as possible* rather than
silently mistranslating a redefined field.

---

## 9. Proposed artifact shape (sketch, for discussion)

Per-transition `docs/generated/schema-lens/<fromBuild>-<toBuild>.json`:

```jsonc
{
  "fromBuild": "11081546", "toBuild": "11408339", "platform": "windows-x86_64",
  "schemaVersion": "…", "generatedFrom": "diff(entity_schema)",
  "classes": {
    "added":   ["client.dll/CFuncWater"],
    "removed": ["server.dll/CFuncWaterAnalog"],
    "changed": [{
      "name": "client.dll/CAnimGraphNetworkedVariables",
      "fields": {
        "added":   [{ "name": "m_foo", "type": {…}, "offset": "84" }],
        "removed": [{ "name": "m_bar", "type": {…}, "offset": "80" }],
        "typeChanged":   [{ "name": "m_x", "from": {…}, "to": {…} }],
        "offsetChanged": [{ "name": "m_y", "from": "40", "to": "48" }]
      },
      "reparent": { "from": [...], "to": [...] },
      "resize":   { "from": "96", "to": "104" },
      "renameCandidates": [
        { "from": "m_bar", "to": "m_foo", "confidence": 0.9,
          "evidence": ["typeMatch","offsetAdjacent"] }
      ]
    }]
  },
  "enums": { "added": [...], "removed": [...], "changed": [...] },
  "safety": { "lossy": [...], "breaking": [...] }   // breaking populated by overlays
}
```

Plus two combined, consumer-friendly views (portable, like `cs2_schema.json`):

- `docs/generated/schema-lens/field_history.json` — per `(class, field)`: `firstSeen`,
  `lastSeen`, confirmed alias chain, type history. Directly serves §7.1 / DVN G3.
- `docs/generated/schema-lens/index.json` — the list of transitions + available baselines.

And a human page `docs/generated/schema-lens.md` documenting the chain and how to replay
it. Overlays: `docs/overlays/schema-lens/*.yml`.

---

## 10. Decisions

1. **Published scope** — ✅ **Layer A only** (objective schema-evolution graph; no Layer C
   property-name/transform policy). §1.
2. **Rename handling** — ✅ **Candidates + overlay confirmation** (machine proposes
   `renameCandidate`, human confirms via overlay). §4.1.
3. **Diff engine home** — ✅ **SchemaTracker owns Layer A.** The per-transition delta is an
   enrichment of the existing `changelog.json` (same build-time diff, field-level instead of
   `field_count`/`parent`); the cumulative `field_history` roll-up *can only* live upstream
   since it needs every snapshot, which only SchemaTracker holds. Docs is a thin consumer:
   overlay-confirm renames + breaking-change guards, and render. See §6.1 + §6.2.
4. **Materialization** — open: adjacent-transition chain only, or also periodic baselines +
   squashed deltas for fewer hops. §3. *(Deferred; the cumulative artifact of §6.1 makes
   any-pair squashing free, so this is a packaging detail, not a blocker.)*

Nothing is built yet; this is the map before we pick a route. The concrete upstream work is
specified in §11.

---

## 11. Upstream emitter spec (SchemaTracker)

*This section specifies the SchemaTracker-side work (Layer A production). It lives in this
repo for now and moves to `CS2OpenDev-SchemaTracker` when the refactor is ready to take it.
It is written against the real code as of reading:
`host/src/Cs2SchemaTracker.Host/Changelog/BuildChangelogEmitter.cs`,
`schemas/build_changelog.proto`, `Cli/DiffCommand.cs`, `Changelog/ChangelogPredecessor.cs`.*

### 11.0 What already exists (and the idiom to respect)

SchemaTracker already has a deterministic, fail-loud, proto-defined build-to-build diff:

- **`diff --from <b> --to <b> [--platform] [--artifacts]`** (`DiffCommand`) — and the same
  emitter runs *inline* during `extract` against the immediate predecessor. Both write
  `artifacts/<to_build>/<platform>/changelog.json`.
- **`BuildChangelog`** proto: `families[]` of `FamilyDelta{family, added[], removed[],
  changed[EntryChange{name, fields[FieldChange{field, old_value, new_value}]}]}`.
- **Predecessor rule** is single-source in `ChangelogPredecessor.Resolve` (greatest numeric
  build id strictly less, with the platform dir present). Two call sites share it so they
  cannot disagree — *the pattern to imitate for any new chain logic.*
- **Invariants:** Ordinal-sorted everywhere, culture-invariant scalar rendering, byte-identical
  re-runs, fail-loud on missing/omitted sets, atomic `.tmp`→rename write.

Two idioms matter for this spec:

1. **Structure is encoded in existing string fields rather than growing the proto** — classes
   and enums key on a qualified `"<module>/<name>"` string; the **enum family already emits
   field-level rows** as `FieldChange{field:"member:<name>", old_value, new_value}`.
2. **Class diff is the shallow one** — `DiffClasses` emits only `field_count` and `parent`.
   It is the exact spot that must go field-level.

### 11.1 One diff core, two renderings

Extract the structural class/enum diff into a shared **`SchemaStructuralDiff`** core (mirroring
how `ChangelogPredecessor` is shared), then render it two ways so they can never diverge:

- **Rendering A — enriched `changelog.json`** (per-transition, existing artifact, **proto
  unchanged**): the `classes` family gains field-level `FieldChange` rows in the enum idiom.
- **Rendering B — new cumulative `schema_evolution.json`** (whole-history, **new proto**):
  structured ops + rename candidates + `field_history`, committed under the latest build.

Rendering A is the cheap "improvement around `changelog.json`." Rendering B is the load-bearing
Schema Lens artifact. Both consume the same `SchemaStructuralDiff` output.

### 11.2 Rendering A — enrich `DiffClasses` (proto-stable)

Extend `DiffClasses` so a changed class's `fields[]` also carries, in Ordinal `field` order:

| `field` key | `old_value` → `new_value` | Meaning |
|---|---|---|
| `field_count` | `20` → `22` | (existing) |
| `parent` | joined names | (existing) |
| `size` | `96` → `104` | class size shifted |
| `alignment` | `8` → `16` | class alignment shifted |
| `field+:<name>` | `""` → `<renderedType>@<offset>` | field added |
| `field-:<name>` | `<renderedType>@<offset>` → `""` | field removed |
| `fieldType:<name>` | `<renderedType>` → `<renderedType>` | declared type changed |
| `fieldOffset:<name>` | `40` → `48` | offset moved |
| `fieldMeta:<name>` | joined | metadata changed |

`<renderedType>` is a stable, culture-invariant flattening of the `SchemaType` graph — a
grammar the spec must pin exactly, e.g. `BUILTIN:int32`, `PTR->DECLARED_CLASS:CFoo`,
`FIXED_ARRAY[8]->float32`, `DECLARED_ENUM:SomeEnum_t` — the same "render a structured thing to
one deterministic string" move `parent`/`flags` already use. This rendering is lossy-by-design
(no rename linkage, stringified type); that is acceptable for the per-transition human/index
artifact. The structured truth lives in Rendering B.

No proto change. Existing consumers keep indexing `families[0]`; they simply see more rows.

### 11.3 Rendering B — new `schema_evolution.json` (+ `schema_evolution.proto`)

Because rename candidates (confidence + multi-signal evidence), per-op safety, and the
whole-history `field_history` roll-up need real structure the flat `FieldChange` model cannot
carry, add a **purpose-built artifact** rather than overloading the changelog.

- **New subcommand `evolution --platform [--artifacts]`** — walks *all* committed builds for
  the platform (generalize `ChangelogPredecessor`'s numeric ordering into the full chain),
  runs `SchemaStructuralDiff` on each consecutive pair, accumulates the transition chain +
  `field_history`, and writes **one** cumulative artifact under the **latest** build:
  `artifacts/<latest>/<platform>/schema_evolution.json`. Same invariants (deterministic,
  fail-loud, atomic).
- **Why under the latest build:** Docs sparse-checkouts *only* the latest build. Committing
  the cumulative artifact there hands Docs the entire history in one file with no wide
  checkout — the design point that keeps Docs' partial+sparse model intact (§6.1).
- **Cadence:** one-time backfill runs `evolution` over the full committed history to seed it;
  thereafter each `extract` refreshes it (append newest transition + update `field_history`).
  The prior build's copy is simply superseded (only the latest is authoritative).

Proto sketch (`schemas/schema_evolution.proto`, proto3, canonical-JSON like the rest):

```proto
message SchemaEvolution {
  string schema_version = 1; string platform = 2;
  string baseline_build = 3; string latest_build = 4;
  repeated Transition transitions = 5;      // consecutive pairs, build-ascending
  repeated FieldHistory field_history = 6;  // per (module/class, field), whole-history
  repeated EnumHistory  enum_history  = 7;
}
message Transition {
  string from_build = 1; string to_build = 2;
  repeated string class_added = 3;          // "<module>/<name>"
  repeated string class_removed = 4;
  repeated ClassDelta class_changed = 5;
}
message ClassDelta {
  string name = 1;                          // "<module>/<name>"
  repeated FieldOp field_ops = 2;
  Reparent reparent = 3; SizeChange resize = 4;
  repeated RenameCandidate rename_candidates = 5;
}
message FieldOp {
  enum Kind { ADD=0; REMOVE=1; TYPE_CHANGE=2; OFFSET_CHANGE=3; META_CHANGE=4; }
  Kind kind = 1; string field = 2;
  SchemaType from_type = 3; SchemaType to_type = 4;  // structured, not stringified
  string from_offset = 5; string to_offset = 6;
  Safety safety = 7;                        // machine sets SAFE|LOSSY only (see 11.5)
}
message RenameCandidate {
  string from = 1; string to = 2;
  Confidence confidence = 3;                // HIGH|MEDIUM|LOW — discrete, no float nondeterminism
  repeated string evidence = 4;             // "typeMatch","offsetExact","offsetAdjacent","sizeMatch"
}
message FieldHistory {
  string class = 1; string field = 2;
  string first_seen_build = 3; string last_seen_build = 4;
  repeated SchemaType type_history = 5;
  repeated string alias_chain = 6;          // MECHANICAL (candidate-derived); Docs produces the authoritative one
}
enum Safety { SAFE=0; LOSSY=1; BREAKING=2; }   // upstream never emits BREAKING (see 11.5)
```

`SchemaType` reuses the existing `entity_schema` type message so the structured form is shared,
not re-modelled.

### 11.4 Rename-candidate heuristic (must be deterministic)

Within a matched class, over the removed set R and added set A:

1. Score each `(r, a)` pair by signals: `typeMatch` (rendered types equal), `offsetExact`
   (same offset), `offsetAdjacent` (offset within the shifted block), `sizeMatch`.
2. Emit a candidate only when `typeMatch ∧ (offsetExact ∨ offsetAdjacent)`.
3. Map fired signals to a discrete `Confidence` (e.g. `typeMatch+offsetExact ⇒ HIGH`; else
   `MEDIUM`; single weak-signal survivors `LOW`) — **no float scores** (nondeterminism risk).
4. Enforce **1:1** matching (each `r`/`a` used at most once) via a greedy pass ordered by
   (confidence desc, Ordinal name) so the result is a pure function of the two snapshots.
5. **Always also emit the raw ADD + REMOVE `FieldOp`s.** A candidate never replaces the facts;
   it annotates them. Confirmation → promotion happens only in Docs overlays.

### 11.5 Safety classification (machine tier only)

The machine sets `SAFE` / `LOSSY`; it **never** emits `BREAKING` (that requires human judgment
and is raised in Docs overlays — keeps SchemaTracker deterministic):

- **SAFE:** `ADD` field/class/enum/member, metadata-only, `OFFSET_CHANGE`.
- **LOSSY:** `REMOVE` field/class/member; `TYPE_CHANGE` that *narrows* per a fixed
  width/category table (e.g. int64→int32, DECLARED_CLASS→PTR); `reparent`.
- **BREAKING:** never upstream. Reserved slot for Docs' overlay-raised semantic breaks
  (redefinition at same name+offset, unit change, field split) with a `guard` suggestion (§8).

### 11.6 Two-tier `field_history` (the §6.2 seam, concretely)

SchemaTracker emits the **mechanical** `field_history.alias_chain` (built only from
rename *candidates*). Docs, at generation time, folds in overlay-**confirmed** renames to
produce the **authoritative** alias chain it publishes. Upstream never reads overlays; Docs
never re-diffs snapshots. Clean split, no shared mutable state.

### 11.7 Deliverable checklist (for the upstream PR, when it moves)

1. `SchemaStructuralDiff` core (shared class/enum structural diff; the single source).
2. `DiffClasses` enrichment → Rendering A (proto unchanged; new `ChangelogContractTest` cases).
3. `schemas/schema_evolution.proto` + generated message.
4. `evolution` subcommand → Rendering B; one-time backfill + inline refresh on `extract`.
5. `<renderedType>` grammar pinned + unit-tested; rename heuristic + safety tables unit-tested.
6. `verify-artifacts` gate for `schema_evolution.json` presence at the latest build (mirroring
   the existing changelog predecessor gate).
7. Determinism test: re-run `evolution` over the same tree ⇒ byte-identical (as the changelog
   already asserts).
