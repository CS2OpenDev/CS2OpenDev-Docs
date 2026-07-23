# Request: close the last coverage gaps vs SchemaExplorer / GameTracking-CS2

This is a Docs → SchemaTracker request, the mirror of `SCHEMA_LENS_RESPONSE.md`. It reports what
still differs between the SchemaTracker artifact set and the two upstreams the Docs site is trying to
drop — `ValveResourceFormat/SchemaExplorer` (the DumpSource2 schema dump) and
`SteamDatabase/GameTracking-CS2` (protos, game-event registries, console dumps).

**Headline:** the C++ schema layer is done — byte-for-byte parity plus a strictly richer envelope.
The console layer (convars/commands) is done. **The wire layer is not**, and two schema-adjacent
payloads (engine game events, typed metadata values) are partial. Until the wire gap closes, Docs
cannot drop `upstream/data` without losing every net/user-message definition.

Everything below is stated as provable facts + the reproduction, in the same facts-only spirit as
your response. Where we can only *infer* the producing binary (no source-attribution field in the
artifacts), we say so.

---

## Comparison basis

| Side | Source | Build / revision | Date |
|---|---|---|---|
| Upstream schema | SchemaExplorer `schemas/cs2.json.gz` (DumpSource2) | SourceRevision `10830129` | Jul 16 2026 |
| Upstream wire/events | GameTracking-CS2 `Protobufs/`, `game/**/resource/*.gameevents`, `DumpSource2/*.txt` | same game version | Jul 16 2026 |
| SchemaTracker | `artifacts/24304127/windows-x86_64/*` (newest, both platforms committed) | steamBuildId `24304127` | ~Jul 22 2026 |

The two build-ID axes are not numerically comparable (SchemaTracker `buildId` == Steam `steamBuildId`;
DumpSource2 `SourceRevision` is a Perforce CL). Matched by CS2 game version / recency. `sourceRevision`
is an empty string in every artifact, so exact matching isn't possible — a ~4-day version drift is
expected and accounts for the single class-size difference noted below.

---

## Status at a glance

| Layer | Upstream | SchemaTracker | Verdict |
|---|--:|--:|---|
| Classes (unique names) | 3,584 | 3,584 | ✅ exact parity |
| Enums (unique names) | 610 | 610 | ✅ exact parity |
| Fields (name **+ offset**) | 17,872 | 17,872 | ✅ **zero** differences |
| Enum members (name + value) | 4,575 | 4,575 | ✅ exact parity |
| Class sizes | — | — | ✅ 1 diff (`C_PlantedC4`), version drift only |
| Metadata attribute **names** | 13,314 | 14,078 | ✅ superset |
| Metadata attribute **values** | 13,314 pop. | ~9,000 pop. | ⚠️ **~4,390 typed values dropped** (§3) |
| ConVars | 3,868 | 3,954 | ✅ superset (0 missing, +86) |
| Commands | 1,122 | 1,132 | ⚠️ 6 missing (all `schema_*`), +16 |
| Game events — `game`/`mod` | 195 | 195 | ✅ exact parity |
| Game events — `core` (engine) | 94 | 15 | ⚠️ **79 missing** (§2) |
| Proto files | 43 | 32 | ⚠️ **11 missing** (§1) |
| `network_messages` join resolves | — | 3 / 192 | ⚠️ **189 dangling** (§1) |

---

## §1 — Wire layer: 11 protos missing, 189/192 network-message entries dangling (highest priority)

**Facts.**
- `protos.descriptorset` ships **32 files / 497 messages**. GameTracking-CS2 ships **43**.
- Missing files:
  ```
  netmessages.proto            usermessages.proto        cstrike15_usermessages.proto
  clientmessages.proto         gameevents.proto          cs_gameevents.proto
  networkbasetypes.proto       te.proto                  prediction_events.proto
  fatdemo.proto                steammessages_gc.proto
  ```
- **`network_messages.json` is a table of dangling references.** Of its 192 `protoMessageType`
  entries, **only 3 resolve** against the shipped descriptorset. The 189 unresolved break down as:

  | Channel | Unresolved | Lives in (upstream file) |
  |---|--:|---|
  | UserMessages | 89 | `usermessages.proto`, `cstrike15_usermessages.proto` |
  | SvcMessages | 29 | `netmessages.proto` |
  | TempEntities | 23 | `te.proto` |
  | ClcMessages | 15 | `netmessages.proto` |
  | NetMessages | 12 | `netmessages.proto`, `networkbasetypes.proto` |
  | Sounds / Decals / Bidirectional / ClientMessages / GameEvents / Source1Legacy | 21 | `clientmessages.proto`, `gameevents.proto`, `te.proto` |

  So the "which wire ID is which message" join — the single thing GameTracking-CS2 cannot give and
  SchemaTracker was meant to — points at message types that aren't in the bundle. (`demo_messages.json`
  is the counter-example and proves the mechanism works: **19/19 resolve**, because `demo.proto` ships.)

**Ask.** Emit the descriptors for the 11 missing files into `protos.descriptorset` so every
`network_messages.json` / `demo_messages.json` `protoMessageType` resolves inside the same build. These
are the core engine/user/temp-entity/game-event message families; they are what a demo or netchan
consumer actually decodes. Acceptance test: `#unresolved == 0` in the snippet below.

**Confirmed, accept as cost:** **0 of 32 files carry `source_code_info`** — reconstructed descriptors
have no comments. The Docs plan already accepts this (the wire ID→type tables more than compensate);
flagging only so it isn't mistaken for a regression to chase.

---

## §2 — Engine game events: 79 of 94 `core.gameevents` entries absent

**Facts.** `gameevents.json` has 195 events; every record's `source` is `game.gameevents` (50) or
`mod.gameevents` (145). Per-file coverage:

| Registry (GameTracking `game/**/resource/`) | Declared | In ST | Missing |
|---|--:|--:|--:|
| `game.gameevents` | 50 | 50 | 0 |
| `mod.gameevents` | 145 | 145 | 0 |
| `core.gameevents` (engine) | 94 | 15 | **79** |

The engine registry is not being walked. Missing events include ones any demo parser needs:
`player_connect`, `player_connect_full`, `player_disconnect`, `player_full_update`, `player_spawn`,
`player_info`, `round_start`, `round_freeze_end`, `round_start_pre_entity`, `server_cvar`,
`server_spawn`, `team_info`, `team_score`, `spec_target_updated`, `bot_takeover`, `entity_killed`,
`local_player_team`, all `vote_*`, all `hltv_*`.

**Ask.** Extend the game-event walk to the engine's `core.gameevents` registry (same subsystem theme
as the old convar gap — an engine binary that wasn't being enumerated). Emit with `source:
"core.gameevents"` so the origin stays visible.

---

## §3 — Metadata: attribute names present, ~4,390 typed values dropped

**Facts.** Attribute *name* coverage is a superset — name-level diff is **0 missing / 0 extra**. But
for a specific class of attributes the name is emitted with an **empty `value`** where upstream carries
the payload. This is not a few stragglers; for these attributes it is **100% of occurrences**:

| Attribute | Upstream populated | ST dropped | Value type |
|---|--:|--:|---|
| `MGetKV3ClassDefaults` | 2,897 | **3,187 (all)** | KV3 block (per-class default values) |
| `MPropertySuppressExpr` | 337 | 345 (all) | expression string |
| `MPropertySortPriority` | 246 | 246 (all) | int |
| `MPulseEditorHeaderIcon` | 123 | 176 (all) | resource path |
| `MPulseEditorCanvasItemSpecKV3` | 73 | 106 (all) | KV3 block |
| `MVDataClassGroup` | 66 | 72 (all) | quoted string |
| `MResourceTypeForInfoType` | 49 | 49 (all) | 4-char token |
| `MCustomFGDMetadata` | 38 | 43 (all) | string |
| `MPropertyReadonlyExpr` | 30 | 32 (all) | expression |
| `MVectorIsSometimesCoordinate` | 30 | 30 (all) | flag/int |
| `MPropertyProvidesEditContextString`, `MKV3TransferSaveOpsForField`, `MVDataPromoteField`, `MParticleMin/MaxVersion`, `MVData*`, `MFgdHelper`, … | ~90 | ~90 (all) | mixed |

~30 value-carrying attributes, **~4,390 dropped payloads**. Plain string/friendly-name attributes are
unaffected — `MPropertyFriendlyName` (4,954) and `MPropertyDescription` (1,305) are populated. The
failures cluster on **KV3-blob, expression, and resource-token** value types.

`MGetKV3ClassDefaults` is the one that matters most: it is the **entire per-class default-value layer**
(3,187 classes). The Docs schema contract (`CLAUDE.md`, plan Phase 1) explicitly reserves a
"KV3-defaults slot" for it, and `entity_schema.proto`'s `Metadata` already has a `valueParsed` field to
hold the parsed form.

Sample of what's lost (`CPulseCell_IntervalTimer` → `MGetKV3ClassDefaults`): upstream carries the full
default KV3 object (`_class`, `m_nEditorNodeID`, all outflow slots); ST emits `{"name":
"MGetKV3ClassDefaults", "value": ""}`.

**Ask.** In the metadata extractor, serialize these non-plain-string attribute values (KV3 blocks →
the same text form upstream emits, into `value`, and/or the structured form into `valueParsed`;
expressions and tokens → their string). Enum-member metadata does **not** have this problem — it's a
class/field-metadata extractor issue specific to the richer value types.

---

## §4 — Minor / informational

- **`C_PlantedC4` size**: upstream 5904, ST 5936. The only class-size difference across 3,584 classes;
  consistent with the ~4-day version drift, not an extraction fault. No action.
- **6 missing commands**: `schema_all_list_bindings`, `schema_detailed_class_layout`,
  `schema_dump_binding`, `schema_list_bindings`, `schema_meta_stats`, `schema_stats` — schemasystem
  self-introspection commands. Low value; note only.
- **`string_pools.json`**: still `pools: []` (empty) in current builds. If it's meant to carry data,
  it isn't yet; if intentionally build-on-demand, a one-line note in the artifact docs would help
  consumers gate on it.
- **`localization.json`**: not present in any build. Item/mode name-tokens (`#CSGO_...`) therefore
  can't resolve to human strings. The Docs plan already gates a loc page on presence — no blocker,
  just confirming it's still absent.
- **`registry_audit.json` symbol attribution**: convar/command entries carry `module: ""` (only schema
  symbols get a real module). This is why Docs still can't attribute a convar to its producing binary
  from the artifacts alone. If the walker knows the registering module for a convar/command, surfacing
  it here (or a `module` field on `convars.json`/`commands.json`) would let Docs render source-binary
  badges and retire the naming-convention inference in `SCHEMA_COVERAGE_GAP.md`. Nice-to-have.
- **Wins to note** (not gaps): `engine_constants.json` is now populated (4,735 constants; was empty);
  45 `projectName` modules now cover the editor/tooling surface (`hammer`, `modeldoc_editor`,
  `resourcecompiler`, `mapdoclib`, `sounddoc_lib`, …). The old "runtime-only, ~6 modules" framing is
  obsolete — SchemaTracker now matches DumpSource2's full module breadth. Docs' `AGENTS.md` and plan
  narrative will be updated to drop the runtime-only caveat.

---

## §5 — Two fixes to `SCHEMA_LENS_RESPONSE.md` / the evolution artifact

Reviewing the Layer A response against `artifacts/schema_evolution/windows-x86_64.json` (44 MB) and
`linux-x86_64.json`: every structural claim verified — fixed path, 378 builds / 377 transitions on both
platforms, the five `FieldOp` kinds (105,643 ops: OFFSET_CHANGE 86,852 · META_CHANGE 12,540 · ADD 3,244
· REMOVE 2,187 · TYPE_CHANGE 820), `ClassDelta`/`EnumDelta`, structured `SchemaType`, `field_history`
(26,308 win / 21,139 linux) and `enum_history` (723). No `confidence`/`rename`/SAFE-LOSSY/`alias_chain`
— all genuinely absent, as designed. Two corrections:

1. **Dangling reference.** The doc names `SCHEMA_EVOLUTION_SPEC.md` as an authoritative reference, but
   that file was deleted in `4710a030` ("Drop planning/spec docs before merge; fix their references") —
   the cleanup missed this citation. Only `schemas/schema_evolution.proto` survives. Update or drop the
   reference.

2. **`pairedEvidence` is thinner than documented.** §1 advertises `signals ⊆ {offsetExact,
   offsetAdjacent, sizeMatch, typeMatch}` with the consumer choosing the confirmation bar. In the actual
   artifact there are **198 pairings across all 377 transitions, and every one carries exactly
   `["offsetExact","typeMatch"]`** — `offsetAdjacent` and `sizeMatch` are never emitted. Against 2,187
   REMOVEs / 3,244 ADDs, the producer has already applied the strictest bar and discarded everything
   below it. So "machine reports signals, human decides" isn't quite what shipped: the pairing policy
   *is* `offsetExact ∧ typeMatch`, decided upstream. A rename where the field shifted a slot or changed
   width leaves no evidence. Either **emit the weaker signals** (so downstream can loosen the bar), or
   **state the rule plainly** in the response/proto so consumers know the pairing set is pre-filtered,
   not raw.

Neither blocks consumption; both are accuracy fixes so the doc matches the bytes.

---

## Priority order

1. **§1 wire protos** — blocks dropping `upstream/data`; makes `network_messages.json` usable.
2. **§2 engine game events** — 79 events every demo consumer needs.
3. **§3 metadata values** — recovers the per-class KV3 defaults layer (~4,390 payloads).
4. §5 doc fixes — cheap accuracy.
5. §4 items — informational / nice-to-have.

Items 1–3 are the difference between "Docs still needs both upstreams" and "Docs runs on SchemaTracker
alone." After them, the clean cut the migration plan calls for is achievable with no coverage loss.

---

## Reproduction

Run against a SchemaTracker checkout + the two upstream submodules. `B` = newest committed build.

```python
import json, gzip, glob, os, collections
from google.protobuf import descriptor_pb2

ST  = 'artifacts/24304127/windows-x86_64/'          # SchemaTracker
SEX = 'upstream/schema-explorer/schemas/cs2.json.gz'  # SchemaExplorer
GT  = 'upstream/data/'                                # GameTracking-CS2

es = json.load(open(ST+'entity_schema.json', encoding='utf-8'))
up = json.load(gzip.open(SEX, 'rt', encoding='utf-8'))

# schema parity (expect 0 / 0)
stf = {(c['name'], f['name'], int(f['offset'])) for c in es['classes'] for f in c.get('fields',[])}
upf = {(c['name'], f['name'], int(f['offset'])) for c in up['classes'] for f in c.get('fields',[])}
print('fields missing in ST:', len(upf - stf), 'ST-only:', len(stf - upf))

# §1 wire — expect unresolved == 0 once the 11 protos ship
fds = descriptor_pb2.FileDescriptorSet.FromString(open(ST+'protos.descriptorset','rb').read())
known = set()
def walk(ms):
    for m in ms: known.add(m.name); walk(m.nested_type)
for f in fds.file: walk(f.message_type)
nm = json.load(open(ST+'network_messages.json', encoding='utf-8'))
ids = [m['protoMessageType'] for ch in nm['channels'] for m in ch['messages'] if m.get('protoMessageType')]
print('network_messages unresolved:', sum(t not in known for t in ids), '/', len(ids))

# §2 engine events — expect 0 once core.gameevents is walked
st_ev = {e['name'] for e in json.load(open(ST+'gameevents.json', encoding='utf-8'))['events']}
import re
core = open(GT+'game/core/pak01_dir/resource/core.gameevents', encoding='utf-8', errors='replace').read()
core_ev = set(re.findall(r'^\t[\"]?([a-zA-Z0-9_]+)[\"]?', core, re.M))
print('core.gameevents missing in ST:', len(core_ev - st_ev))

# §3 metadata values — expect ~0 dropped once typed values serialize
def empties(cs):
    t = collections.Counter(); e = collections.Counter()
    for c in cs:
        for m in c.get('metadata',[]) + [x for f in c.get('fields',[]) for x in f.get('metadata',[])]:
            t[m['name']] += 1
            if not (m.get('value') or '').strip(): e[m['name']] += 1
    return t, e
ut, ue = empties(up['classes']); st, se = empties(es['classes'])
dropped = sum(max(0, se[n]-ue.get(n,0)) for n in ut if (ut[n]-ue.get(n,0)) > 0)
print('metadata values dropped by ST:', dropped)
```

Expected at parity: `0 / 0`, `0 / 192`, `0`, `~0`.
