# SchemaTracker coverage gap — remaining gaps vs. the DumpSource2 dump

**Scope of this document.** SchemaTracker's walker refactor/expansion has **closed the entire
schema coverage gap**. Classes, enums, and the type universe are now at full parity with the
DumpSource2 / SchemaExplorer dump. The *only* remaining deltas are in **convars and commands**,
and they trace to a specific, enumerable set of **binaries the convar/command walker does not yet
read**. This document identifies those binaries so they can be picked up.

> This supersedes the previous version of this file, which reported SchemaTracker as runtime-only
> (~1,064 classes / 15 enums, missing 2,952 entities). That analysis is **obsolete**: SchemaTracker
> re-walked and re-committed *every historical build* with the expanded walker, so the exact build
> that previously reported 1,064 classes (`24134959`) now reports 4,967. The schema gap it described
> no longer exists.

## Comparison basis

| Side | Source | Build / revision | Date |
|---|---|---|---|
| **Upstream** | SchemaExplorer `schemas/cs2.json.gz` (DumpSource2 output) | `SourceRevision 10830129` | Jul 16 2026 |
| **SchemaTracker** | `artifacts/24248951/windows-x86_64/*` (latest committed) | Steam `buildId 24248951` | ~Jul 20 2026 |

The two identifier axes differ (Valve `SourceRevision` vs. Steam `buildId`) and are not comparable
numerically; builds are matched by recency of the CS2 game version. The ~4-day offset is a minor
confound noted where relevant. Class/enum/convar/command matching is by **name**.

## Status at a glance

| Category | Upstream | SchemaTracker | Missing from ST | ST-only additions | Verdict |
|---|--:|--:|--:|--:|---|
| **Classes** (unique names) | 3,584 | 3,584 | **0** | **0** | ✅ parity |
| **Enums** (unique names) | 610 | 610 | **0** | **0** | ✅ parity |
| **Convars** | 3,868 | 3,354 | 570 | 56 | ⚠️ walker scope |
| **Commands** | 1,122 | 841 | 288 | 7 | ⚠️ walker scope |

---

## 1. Schema — parity reached

The set of unique **class names** is byte-for-byte identical on both sides (3,584 each, zero in
either direction). The same holds for **enum names** (610 each). Raw *entry* counts differ
(upstream 4,572 class rows vs. ST 4,967; enums 654 vs. 674) only because SchemaTracker records each
type under more binary modules; after deduping by name the universes coincide exactly. SchemaTracker's
`projectName` axis now spans all 45 modules including the editor/tooling ones the old runtime-only
walker dropped (`hammer`, `modeldoc_editor`, `mapdoclib`, `resourcecompiler`, `sounddoc_lib`, …).

**No action required for classes or enums.**

---

## 2. Remaining gaps — convars & commands

### 2.1 The gap is bidirectional

- **SchemaTracker adds** 56 convars + 7 commands the DumpSource2 dump lacks — **100% particle/
  rendering** (`r_particle_*`, `cl_particle_*`, `particle_profile`, `dumpparticlelist`). SchemaTracker
  walks `particles.dll` more thoroughly than the upstream cvarlist did. This is a genuine SchemaTracker
  *win*, not a regression.
- **SchemaTracker misses** 570 convars + 288 commands. These are **not random** — they cluster by the
  binary that registers them.

### 2.2 Coverage collapses exactly at un-walked binaries

Convar coverage stays near-complete for binaries the walker processes deeply, and drops toward zero
for binaries it does not read at all (`schemaReg` = the binary's `schemaRegistrationCount` in
`modules.json`; note the correlation):

| Subsystem (name prefix) | Upstream | In ST | Coverage | Registering binary | `schemaReg` |
|---|--:|--:|--:|---|--:|
| `fs_` / `filesystem_` | 12 | 0 | **0%** | `filesystem_stdio.dll` | 0 |
| `mm_` | 36 | 1 | **3%** | `matchmaking.dll` | 0 |
| `engine_` | 25 | 2 | **8%** | `engine2.dll` | 4 |
| `host_` | 5 | 1 | **20%** | `host.dll` / `engine2.dll` | 0 |
| `tv_` (GOTV) | 86 | 18 | **21%** | `engine2.dll` | 4 |
| `panorama_` | 101 | 23 | **23%** | `panorama.dll` / `panoramauiclient.dll` | 0 |
| `voice_` | 27 | 15 | 56% | `engine2.dll` / `soundsystem.dll` | 0 |
| `mat_` | 44 | 28 | 64% | `materialsystem2.dll` | 0 |
| `joy_` / `input_` | 53 | 39 | ~73% | `inputsystem.dll` | 0 |
| — *for contrast* — | | | | | |
| `cl_` | 513 | 461 | 90% | `client.dll` | 537 |
| `sv_` | 435 | 349 | 80% | `server.dll` | 798 |
| `snd_` | 182 | 179 | 98% | `soundsystem*` / `client.dll` | walked |
| `r_` | 400 | 316 | 79% | `client.dll` / `particles.dll` | walked |

Commands show the same shape — whole prefixes at **0%**: `demo_*`, `vprof_*`, `r_*` (engine-side),
`vis_*`, `instant_*`, `resource_*`, `crash*`, `schema_*`, `gameui_*`, plus `mat_*` (4%) and `tv_*` (9%).

The takeaway: the walker already captures convars/commands from the **runtime/game binaries it walks
for schema** (`client.dll`, `server.dll`, `particles.dll`, `soundsystem*`), but does **not** enumerate
the ConVar/ConCommand static registrations in **engine, UI, matchmaking, filesystem, material, and
input** binaries — all of which are present in the build but carry `schemaRegistrationCount ≈ 0`.

---

## 3. Binaries to add to the convar/command walker

These binaries are **present in every build's `modules.json`** but contribute **no convars/commands**
to the output. Adding their ConVar/ConCommand registration parsing to the walker closes the
attributable gap. Ordered by impact:

| # | Binary (win64 basename) | Convars recoverable | Commands recoverable | What lives here |
|---|---|--:|--:|---|
| 1 | **`engine2.dll`** | ~116 | ~74 | Engine console + **GOTV** (`tv_*`), **demo** (`demo_*`), `host_*`, and core commands (`bind`, `connect`, `changelevel`, `echo`, `exec`, `alias`, `status`, `record`) |
| 2 | **`panorama.dll`** + **`panoramauiclient.dll`** | ~78 | ~5 | Panorama UI (`panorama_*`) |
| 3 | **`matchmaking.dll`** | ~35 | ~2 | Matchmaking / dedicated (`mm_*`) |
| 4 | **`materialsystem2.dll`** | ~16 | ~22 | Material/shader (`mat_*`) |
| 5 | **`inputsystem.dll`** | ~14 | ~1 | Input/joystick (`joy_*`, `input_*`) |
| 6 | **`filesystem_stdio.dll`** | ~12 | ~2 | Filesystem (`fs_*`, `filesystem_*`) |
| 7 | **`tier0.dll` / `engine2.dll` tooling** | ~2 | ~24 | Profiler (`vprof_*`) + resource/schema tooling (`resource_*`, `schema_*`) |
| | **Subtotal (binary-attributable)** | **~273** | **~130** | |

Linux equivalents: `libengine2.so`, `libpanorama.so`, `libmatchmaking.so`, `libmaterialsystem2.so`,
`libinputsystem.so`, `libfilesystem_stdio.so`, `libtier0.so`.

> **Attribution caveat.** `convars.json` / `commands.json` carry no source-binary field, so the
> binary mapping above is inferred from Source2 registration naming convention plus the
> `schemaRegistrationCount ≈ 0` correlation — not from the walker source. The *counts* and *names*
> are exact; the *binary each is registered in* is a strong inference. If the walker reads ConVars
> from a per-binary static registration table (the Source2 pattern), "walk binary X" is the correct
> framing; if it instead reads a single global registry, the fix is to include these modules in that
> enumeration. Either way the missing names above are the target set.

---

## 4. What is *not* a walker-binary gap

The remaining **~297 convars + ~158 commands** carry `cl_`/`sv_`/misc prefixes from binaries that
*are* walked, so they are not explained by an un-walked binary. They break down as:

- **Dev/defensive/hidden entries (the majority).** Of the 570 missing convars, **406 (72%)** are
  flagged `developmentonly`, `defensive`, `cheat`, or `hidden`; of the 288 missing commands, **167 are
  `developmentonly` and 139 `defensive`**. DumpSource2 dumps the union of everything registered in a
  fully-initialized game+tools instance; a static walker may legitimately exclude registrations gated
  behind dev/defensive flags. Only **164** missing convars carry none of those flags.
- **Client-networking convars possibly in `networksystem.dll`.** A cluster of genuinely user-facing
  misses (`cl_clock_*`, `cl_tickpacket_*`, `cl_async_usercmd_*`, `cl_buffer_incoming_net_messages`)
  are networking convars that may register in `networksystem.dll` (`schemaReg 0`) rather than
  `client.dll`. **Secondary candidate binary to check.**
- **~4-day version drift.** Upstream is Jul 16, the ST build ~Jul 20. A small residual across
  otherwise-well-covered prefixes (`cl_` 90%, `sv_` 80%, `r_` 79%) is expected churn, not a defect.

---

## 5. SchemaTracker-only additions (keep these)

SchemaTracker already surfaces convars/commands the upstream dump misses — all particle/rendering:

- **Convars (56):** `r_particle_*` (gpu_implicit, cables, debug, fastpath, …), `cl_particle_*`,
  `sc_particle_debug_visualizer`, `r_physics_particle_op_spawn_scale`.
- **Commands (7):** `dumpparticlelist`, `particle_profile`, `particle_profile_spike`,
  `particle_reset_assertions`, `particle_stop_all`, `particle_stop_specified`, `particle_stop_unspecified`.

---

## 6. Reproducing this comparison

```bash
# upstream (name sets)
python - <<'PY'
import gzip, json
d=json.load(gzip.open('upstream/schema-explorer/schemas/cs2.json.gz','rt',encoding='utf-8'))
print('rev', d['revision'], d['version_date'])
print('classes', len({c['name'] for c in d['classes']}), 'enums', len({e['name'] for e in d['enums']}))
PY

# convars/commands: parse DumpSource2 text dumps (a name is a non-indented, non-blank line)
#   upstream/data/DumpSource2/convars.txt   upstream/data/DumpSource2/commands.txt
# vs SchemaTracker:
#   artifacts/24248951/windows-x86_64/{entity_schema,convars,commands}.json
# Coverage-by-prefix + binary attribution: bucket (upstream − ST) missing names by name prefix,
# map prefix → registering binary, cross-check against modules.json schemaRegistrationCount.
```

**Bottom line:** schema is at parity; the convar/command walker needs to additionally read
ConVar/ConCommand registrations from **`engine2.dll`, `panorama*.dll`, `matchmaking.dll`,
`materialsystem2.dll`, `inputsystem.dll`, `filesystem_stdio.dll`** (and check `networksystem.dll`),
which recovers ~273 convars + ~130 commands. The rest is dev/defensive-gated registrations and minor
version drift.
