# Schema coverage gap — evaluation, root cause, and closure plan

Companion to [SCHEMA_COVERAGE_GAP.md](SCHEMA_COVERAGE_GAP.md) / `schema_coverage_gap.json`.
Evaluated 2026-07-18 against CS2OpenDev-SchemaTracker's committed artifact for build
`24134959` (`windows-x86_64`, era `cs2-2026-07-09`) and the depot binaries for that build.

> **STATUS UPDATE (2026-07-18, same day): IMPLEMENTED.** The closure plan below has been
> landed in CS2OpenDev-SchemaTracker as schema family **0.5.0** (walker loader
> allow-list +18 modules, global-scope walk, unconditional per-module registration,
> declared-ref module-index fallback on all eras, 2023 layout-validation pinned to the
> probe scopes, era class-count bands recalibrated). Verified per era against each era's
> latest committed build — all 13 eras walk cleanly:
>
> | Era (latest build) | 0.4.0 rows | 0.5.0 rows |
> |---|---:|---:|
> | cs2-2023-03-22 (12147839) | 1,062 | 2,704 |
> | cs2-2023-09-13 (13240071) | 1,017 | 2,664 |
> | cs2-2024-02-07 (13829089) | ~1,050 | 2,762 |
> | cs2-2024-04-03 (14446408) | ~1,050 | 2,760 |
> | cs2-2024-06-04 (17680670) | ~1,090 | 3,178 |
> | cs2-2025-03-12 (17732524) | ~1,090 | 3,178 |
> | cs2-2025-03-20 (19251152) | ~1,060 | 3,151 |
> | cs2-2025-07-31 (20007038) | ~1,370 | 3,785 |
> | cs2-2025-09-17 (20278147) | ~1,350 | 3,787 |
> | cs2-2025-10-16 (21529689) | ~1,350 | 3,794 |
> | cs2-2026-01-22 (22627914) | ~1,365 | 3,884 |
> | cs2-2026-04-21 (24074625) | ~1,455 | 4,019 |
> | cs2-2026-07-09 (24134959) | 1,457 | 4,192 |
>
> (Rows, not unique names; 24134959 = 3,566 unique classes / 591 unique enums.) The
> 2023 eras emit 0 enums on both versions — a pre-existing, documented 2023 enum-pool
> limitation, unchanged by this work. Historical backfill re-dumps remain to be run.

## Verdict

**The reported gap is real, and ~97.4% of it is closable within the project's constraint**
(per-build artifacts derived only from the build's depot binaries/content). This was not
estimated — it was **measured**, with a temporary environment-gated proof-of-concept walker
run offline against the build's own depot binaries:

| | Committed dump | PoC walk (same binaries, offline) | Old DumpSource2 dump |
|---|---:|---:|---:|
| Unique classes | 1,064 | **3,566** | 3,429 |
| Unique enums | 15 | **591** | 545 |

- **2,377 / 2,419** missing classes recovered (98.3%)
- **499 / 533** missing enums recovered (93.6%)
- The PoC's enum coverage *exceeds* the old dump's (591 vs 545).
- The 76 unrecovered names are classified exhaustively below; roughly half are
  **out of scope by design** (tools-only DLLs that do not ship in the CS2 depot).

## Validation of the report itself

- **Name lists: 100% accurate.** Every one of the 2,419 `missing_classes` and 533
  `missing_enums` is genuinely absent from the current committed
  `artifacts/24134959/windows-x86_64/entity_schema.json` (0 false positives).
- **Headline counts: correct on a unique-name basis.** The committed artifact holds 1,457
  class *rows*, but rows are duplicated per registering module (e.g. the 66
  `pulse_runtime_lib` classes appear under each of server/client/particles/animationsystem
  scopes); unique names = 1,064, matching the report. Same for enums (27 rows, 15 unique).
- **`added_classes` (54) / `added_enums` (3): genuine, keep them.** They are real
  registrations in the 2026 build our tracker walks (predominantly the `*_API`
  Pulse-domain classes in `server`/`client`, e.g. `CCSPlayerPawn_API`, plus recent
  additions like `CFuncMover::PathRebuildStrategy_t`). The old DumpSource2 mirror is
  simply from an older build — build skew, not an attribution error.

## Why the gap exists — three mechanisms in the walker

All three are in `walker/src/` of CS2OpenDev-SchemaTracker; none are Steam/depot
limitations.

### 1. The global `!GlobalTypes` scope is deliberately excluded (the dominant cause)

`CollectTypeScopes` (`walker/src/schema_walk.cpp`) enumerates only **per-module** type
scopes and explicitly skips the global scope — a byte-stability compatibility decision
("including it would pull in the wrong (global) class set"). But in the live schema
system, the **bulk of the registered universe lives in the global scope**: the lib
projects (`particles` 506, `animlib`, `animgraphlib`, `smartprops` 173, `modellib`,
`physicslib` 99, `sounddoc_lib`, the `soundsystem_*` trio, `worldrenderer`,
`materialsystem2`, `resourcesystem`, …) and **nearly all enums** (hence 15 vs 545 — the
starkest symptom). The per-module scopes hold only small module-local sets (e.g. the
`particles.dll` scope contains just 2 `particleslib` + 66 `pulse_runtime_lib` classes —
not the 506 `particles`-project classes).

### 2. The loader allow-list omits schema-bearing modules

`kSchemaModulesInLoadOrder` (`walker/src/loader.cpp`) loads 16 modules. Schema
descriptors are static data inside a module's image — a never-loaded module's types
cannot register. Not loaded today: `pulse_system`, `worldrenderer`, `materialsystem2`,
`meshsystem`, `navsystem`, `steamaudio`, `rendersystemdx11`, and notably
**`resourcecompiler.dll`, which ships in the depot and carries the doc-lib projects**
(`animdoclib` 197, `animgraphdoclib` 158, `sounddoc_lib`, `texturelib`, `toolutils2`,
`pulsedoc_lib`, `CMixDynamics`-class `soundsystem_lowlevel` types, …). The allow-list
comment assumes these "fail to load headless / carry no relevant schema" — **measured
false on both counts**: in the PoC, all 18 additional modules loaded cleanly headless,
and they carry the majority of the missing projects.

### 3. Full registration is never forced for partially-populated scopes

`TriggerLazySubsystemRegistration` calls `LoadSchemaDataForModules` only for 5 subsystem
modules and **only when a scope has zero bindings**. `client.dll`/`server.dll` register a
subset eagerly at static-init (462/714 classes), so their scopes are never empty and the
full binding set is never installed — which is why even *loaded* modules are partially
missing (335 `client` + 98 `server` classes, e.g. `CTakeDamageInfo`, which is verifiably
present in both DLLs' schema descriptors). Forcing `LoadSchemaDataForModules`
unconditionally for every loaded module (idempotent) closes this.

## Proof-of-concept measurement (method + exact deltas)

Temporary `CS2_WALKER_POC`-gated edits (since reverted byte-identically; nothing
committed): (a) append 18 modules to the load set, skip-on-load-failure; (b) include the
global scope in the walk; (c) force `LoadSchemaDataForModules` for every loaded module.
Run offline against `S:\Counter-Strike 2\cs2-binaries\24134959\windows-x86_64` — the
exact bytes the tracker's acquire step fetches. Baseline run of the same binary (env
unset) reproduces the committed 1,064/15 exactly (control).

Extra modules, all loading cleanly headless: `pulse_system`, `worldrenderer`,
`materialsystem2`, `meshsystem`, `navsystem`, `steamaudio`, `resourcecompiler`,
`rendersystemdx11`, `toolframework2`, `assetpreview`, `propertyeditor`,
`physicsbuilder`, `visbuilder`, `helpsystem`, `panorama`, `localize`, `vscript`,
`scenefilecache`.

### The 76 unrecovered names, exhaustively classified

**Not dumpable from build artifacts — out of scope by the project's own constraint
(≈18 classes + 19 enums).** Their owning DLLs are Workshop-Tools-only and do not ship in
the CS2 depot (verified: names absent from every file in the depot slice):
`hammer` (7 cls + 3 en), `modeldoc_editor` (3 + 1), `mapdoclib` (3), `met` (3),
`modtools` (2), `qcontrols` (15 enums). Recommend documenting these as permanent,
by-design exclusions.

**Registered only under live-game / tools code paths (≈24 classes + 15 enums).**
Present in shipped DLLs' strings but not installed by any headless registration path we
found: `client` (13 cls + 7 en — AI debug-snapshot types, `CAnimEventListener*`,
`CPulseAnimFuncs`, …), `server` (6 + 1), `soundsystem` (6 enums), plus singletons in
`pulse_runtime_lib`/`animationsystem`/`soundsystem_voicecontainers`/`physicslib`.
Marginal (0.8% of the universe); a deeper registration-forcing pass may recover some,
but accept as a known residual rather than chase.

## Recommended follow-up actions (CS2OpenDev-SchemaTracker)

1. **Walker — land the three PoC mechanisms as real features** (this is the whole gap):
   - Extend the loader allow-list with the measured 18-module set (decide
     required/optional per module; all 18 proved headless-safe on `cs2-2026-07-09`, but
     older eras need per-era verification — keep them OPTIONAL so absence in older
     layouts is tolerated, preserving the fail-loud rule for present-but-broken).
   - Force `LoadSchemaDataForModules` for every loaded module, unconditionally.
   - Include the global `!GlobalTypes` scope in `CollectTypeScopes`.
2. **Attribution policy for global-scope types.** Emitted `module` for global-scope
   classes reads `"!GlobalTypes"`; the host's emitter requires meaningful module
   attribution. Attribute by the binding's own identity (the walker already emits
   `project_name` per class — e.g. `animlib`, `smartprops`), not by the scope it was
   found in. This also matches how DumpSource2 grouped its output.
3. **Schema/versioning discipline.** This is a large, strictly-additive data expansion:
   bump the artifact `schema_version` (shape may be unchanged, but consumers must be able
   to distinguish pre/post-coverage dumps), and expect the walker layout-signature
   machinery to be unaffected (scope enumeration uses the same era-stable vtable
   surface — verify with the determinism sweep + ctest before landing).
4. **Rollout: forward-first, then per-era backfill.** Land for the current era, run the
   determinism sweep (two identical back-to-back walks — note new modules' static-init
   may introduce nondeterministic defaults exactly like the historical `cl_color`
   RandomInt case; the fixed-seed hook already exists), verify era parity
   (windows/linux), then re-dump historical eras one era at a time. The 2023-era SEH
   paths deserve extra caution: the global scope on old layouts contains far more
   records to guard.
5. **Regenerate the gap report after implementation** — expected residual: ~42 classes +
   ~34 enums, of which ~18/~19 are permanent tools-only exclusions.

## Scope note

Everything above stays within "dump only what the build's own artifacts contain": every
recovered type comes from schema descriptors physically inside depot-shipped DLLs, walked
headless and offline. No live game, no Workshop Tools install, no external source.
