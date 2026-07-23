# Response: Schema Lens Layer A — what SchemaTracker shipped

This answers `SCHEMA_LENS_LANDSCAPE.md`. Layer A is **built and live** in CS2OpenDev-SchemaTracker
as a cumulative, machine-derived artifact — `schema_evolution.json` — computed by diffing every
consecutive committed `entity_schema.json` snapshot across the whole in-scope history.

We adopted the landscape's core architecture (Layer A upstream, objective substrate, per-transition
chain + whole-history roll-up). We **tightened one thing**: the artifact is strictly *facts only*.
Where your spec had the machine emit *inferences* — rename candidates with a confidence score,
SAFE/LOSSY safety verdicts, assembled alias chains — we emit only what is provable from the two
snapshots and hand you the raw signals to build those inferences downstream, where the policy
belongs. This is SchemaTracker's governing rule: **if we cannot prove the source of a claim, we
don't make it.**

The authoritative references are `schemas/schema_evolution.proto` (the shape) and
`SCHEMA_EVOLUTION_SPEC.md` (the design). This document is the orientation.

---

## What we adopted

| Landscape ask | Status |
|---|---|
| **Layer A is a SchemaTracker feature** (§6.2) | ✅ Built. Deterministic producer upstream; Docs stays a thin consumer. |
| **Cumulative whole-history artifact** the consumer reads in one file (§6.1) | ✅ `schema_evolution.json` — one file per platform, the entire chain + roll-ups. |
| **Per-transition delta chain, build-ascending** (§3) | ✅ `transitions[]`, one per consecutive committed pair. |
| **Field-level ops** (add / remove / retype / offset-move / meta) (§4) | ✅ `FieldOp{kind, field, from/to_type, from/to_offset, …}`. |
| **Class-level ops** (add/remove/reparent/resize/realign/flags) (§4) | ✅ `class_added/removed`, `ClassDelta{reparent, resize, realign, flags}`. |
| **Enum churn** (add/remove enum, member add/remove, value change) (§4) | ✅ `enum_*`, `EnumDelta`, `EnumMemberOp`. |
| **`field_history` roll-up** (first/last seen, type history) (§7.1) | ✅ `field_history[]` + `enum_history[]`. |
| **Structured types, not stringified** (§11.3) | ✅ `SchemaType` reused directly from `entity_schema.proto`. |
| **Determinism / fail-loud / atomic write** (§11.0) | ✅ Ordinal-sorted, culture-invariant, byte-identical re-runs; incremental refresh ≡ full backfill. |
| **A presence gate** mirroring the changelog predecessor gate (§11.7.6) | ✅ `verify-artifacts` requires the artifact and validates it. |

Coverage today: **378 builds / 377 transitions**, both platforms, from baseline `10832117` through
the current live build.

---

## What we changed or passed on (and why)

### 1. No rename assertions — neutral `PairedEvidence` instead of `renameCandidate{confidence}`
Your §4.1 proposed `renameCandidate{from, to, confidence, evidence[]}`. A rename is **provably
indistinguishable** from `remove(A) + add(B)` at the schema level — Valve may have removed A and added
an unrelated B at the same offset. A confidence number would be a fabricated claim. So:

- We **always** emit the raw facts: an `ADD` `FieldOp` and a `REMOVE` `FieldOp`.
- We **additionally** emit `PairedEvidence{from, to, signals[]}` where `signals ⊆ {offsetExact,
  offsetAdjacent, sizeMatch, typeMatch}` — the *provable relations only*. **No `confidence`, no
  probability, no `rename`.**
- **You** promote a pairing to a confirmed rename in your overlays. Machine reports signals; human
  decides. (This is the two-tier `field_history` seam you named in §6.2 — we emit the mechanical
  side, you own the authoritative side.)

### 2. No safety verdict — raw structural facts + a provable width instead of SAFE/LOSSY
Your §8 / §11.5 had the machine set `SAFE`/`LOSSY`. But safety is **consumer-impact policy, not a
schema fact**: an `OFFSET_CHANGE` is harmless for a name-keyed decoder and fatal for an offset-keyed
one; a byte-narrowing `TYPE_CHANGE` is lossy only if the field was carrying the high bits. We can't
know your decode model, so we don't classify. Instead we give you everything needed to classify:

- `FieldOp` carries `from_type`/`to_type` (structured) and `from_offset`/`to_offset`.
- When a type is a known primitive, `from_width`/`to_width` (`BuiltinWidth{bytes}`) is a **provable
  number from a fixed name→bytes table** — enough to detect narrowing yourself, without us asserting
  that narrowing *is* a problem.
- `BREAKING` (semantic redefinition, unit change, field split) was never in scope for the machine —
  it's overlay territory in Docs, exactly as your §11.5 reserved it.

### 3. `field_history` carries no alias chain
Your §11.3 `FieldHistory` had `alias_chain[]`. Assembling an alias chain means linking removes to adds
across history — an inference built on the rename guess we deliberately don't make. So `field_history`
carries `first_seen_build`, `last_seen_build`, and `type_history[]` (facts) only. Build the alias
chain downstream by walking `paired_evidence` + your confirmed renames.

### 4. `changelog.json` was **not** enriched (your §11.2 "Rendering A")
We chose not to add field-level rows to the existing `changelog.json`. Its `classes` family stays the
coarse index it always was (`field_count`, `parent`). **All** field-level detail lives in
`schema_evolution.json` — one place, one shape, no duplicated diff logic to drift. If you were counting
on the enriched changelog, read the evolution artifact instead; it's a strict superset.

### 5. Artifact lives at a **fixed path**, not under the latest build
Your §11.3 put the file under `artifacts/<latest_build>/<platform>/`. We use a **fixed** path:

```
artifacts/schema_evolution/<platform>.json
```

Same benefit (one file, whole history), but nothing to move or `git rm` build-to-build, and git
delta-compresses the near-identical successive versions. *(Note: the proto header comment still
describes the old under-latest-build location — the fixed path above is the real one.)*

### 6. Out of scope, as agreed
- **Layer B (wire encoding)** — effective wire width, sub-service flattening, networked-or-not,
  quantization (your G1/G2/G4). Not derivable from the C++ schema; needs a demo's `FlattenedSerializer`
  or a future wire dump. Untouched.
- **Layer C (consumer mapping policy)** — `targetProperty`, `transform`, `fallbackDefault`, slot
  assignment. Stays in DVN/SDK.
- **Overlays** (rename confirmation, breaking-change guards, semantic notes) — stays in Docs.

---

## How to work with it

### Where it is
`artifacts/schema_evolution/<platform>.json`, one per `windows-x86_64` / `linux-x86_64`. It is
canonical proto3-JSON of the `SchemaEvolution` message (`schemas/schema_evolution.proto`). Parse it
with the generated proto type, or as plain JSON — every optional is carried by message-presence or an
`""` string, never by a 0-vs-absent ambiguity.

### Shape at a glance
```
SchemaEvolution
├─ schema_version, platform, baseline_build, latest_build
├─ transitions[]        one per consecutive pair (from_build → to_build)
│   ├─ class_added[] / class_removed[]           "<module>/<name>"
│   ├─ class_changed[] ClassDelta
│   │   ├─ field_ops[] FieldOp{kind, field, from/to_type, from/to_offset, from/to_width, from/to_meta}
│   │   ├─ reparent / resize / realign / flags
│   │   └─ paired_evidence[] {from, to, signals[]}   ← rename SIGNALS, not a rename
│   └─ enum_added/removed[], enum_changed[] EnumDelta{member_ops[], resize, realign, flags}
├─ field_history[]      per (class_name, field): first_seen_build, last_seen_build, type_history[]
└─ enum_history[]       per enum_name: first_seen_build, last_seen_build
```

### The four value cases from your §7 — how each is served now

1. **Field-history / alias resolution (§7.1, DVN G3).** `field_history[]` gives you first/last-seen and
   the full `type_history` per `(class, field)` directly. For the alias linkage (what a field
   *superseded*): walk each transition's `paired_evidence` for the class, keep the pairings whose
   `signals` meet your bar, and stitch them into a chain. That chain is *yours* — we hand you the
   provable edges; you decide which to trust and record the confirmed ones in your overlay.

2. **Offset-keyed demo migration (§7.2).** Filter `field_ops` for `kind == OFFSET_CHANGE`;
   `from_offset` → `to_offset` per field is the reshuffle map for reinterpreting an old
   offset-keyed instance under a new layout. `resize`/`realign` on the `ClassDelta` bound the block.

3. **Type-shift awareness (§7.3).** `kind == TYPE_CHANGE` flags exactly where a decode assumption
   moves; `from_type`/`to_type` are the structured before/after, and `from_width`/`to_width` (when
   present) let you detect a byte-narrowing without us labeling it "lossy."

4. **Break radar (§7.4).** A single `transitions[]` entry is a field-precise "what structurally
   changed this build" — everything the old `field_count`-only changelog couldn't tell you.

### Doing renames and safety downstream (the deliberate split)
- **Renames:** `paired_evidence.signals` is your evidence set. Your confirmation policy (e.g.
  "`typeMatch ∧ offsetExact` ⇒ confirmed") lives in your overlay; promote there, and derive the
  authoritative alias chain from confirmed renames. We never assert one.
- **Safety:** classify `FieldOp`s against *your* decode model. Name-keyed decoder → `OFFSET_CHANGE`
  is safe, `REMOVE`/`TYPE_CHANGE` matter. Offset-keyed decoder → `OFFSET_CHANGE` is the load-bearing
  one. Use `BuiltinWidth` to spot narrowing. `BREAKING` is your overlay's call.

### Regenerating / consuming fresh
- Produced by the host **`evolution --platform <p> [--artifacts <root>] [--full]`** subcommand
  (`--full` = from-scratch backfill; otherwise an incremental append of the newest transition,
  byte-identical to a full run). It is **not** written inline by `extract` — a re-walk pass must be
  followed by `evolution` to refresh it.
- `verify-artifacts` requires the artifact to be present and consistent with the committed chain.
- Deterministic: re-running over the same committed tree is byte-identical, so you can trust a
  content hash and diff two versions meaningfully.

### Re-baselining is free
Because every full snapshot is committed, a delta between *any* two builds is just
`diff(snapshot_X, snapshot_Y)` — you never squash a run of increments. The published chain is the
convenience layer; if you can hold two `entity_schema.json` snapshots you can compute any pairwise
delta with the same engine.

---

## One-line summary for your changelog
> SchemaTracker publishes **Layer A** as a per-platform `schema_evolution.json` (facts-only:
> structural field/class/enum deltas + `field_history`, plus neutral rename *signals* and provable
> type widths). Rename confirmation, safety classification, wire facts, and consumer mapping stay
> downstream — we give you the objective substrate and the raw signals to build them.
