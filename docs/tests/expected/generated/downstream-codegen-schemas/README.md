# Downstream codegen schemas

Machine-readable schemas for CS2 entity classes, structs, enums, and game
events — projected straight from
[CS2OpenDev-SchemaTracker](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker)'s
per-build artifacts so consumers get one deterministic, provenance-tracked
source instead of a chain of third-party dumps.

## Platform & provenance

Every file here projects **one** `(build, platform)` artifact set:
`windows-x86_64` (CS2 build `9000001`).  The `build_id` (the Steam CS2 game build,
numeric and monotonic) and `platform` are stamped into each schema's header
alongside the walker `revision` and the build timestamps — read them there
rather than assuming.

Windows is the canonical render because it is the superset: it carries the
tool-side modules (`hammer`, `sfm`, `modeldoc_editor`, …) that have no Linux
binaries.  A consumer that assumes Linux would get a silently wrong answer
about which classes exist, so the platform is named explicitly in every
header.  If both platforms are ever published, select by the header's
`platform` field.

## How duplicate class registrations are collapsed

`cs2_schema.json` emits **one record per `(projectName, name)`**, not one per
upstream `(binary-module, name)`.  `projectName` is SchemaTracker's
coarse-grained project axis (`client`, `server`, `entity2`,
`pulse_runtime_lib`, `particleslib`, `animgraphlib`); the finer `module` /
`cppName` from upstream are preserved verbatim on each record.

- A class registered in several binaries that all roll up to the **same**
  `projectName` collapses to a single record.  This dominates the
  `pulse_runtime_lib` cell classes (e.g. `CBasePulseGraphInstance`), which are
  statically linked into many tool binaries but describe one type.
- A name that legitimately appears under **different** `projectName`s — the
  cross-project case such as `CCSPlayerController` in both `client` and
  `server` — keeps one record per project.  So a name appearing more than once
  is expected, and the discriminator is the record's `projectName`.

## Files

- **`cs2_schema.json`** — the entity schema in SchemaTracker's **native**
  shape (`schema_format_version` `2.2`).  Top-level: `generator`, `build_id`,
  `platform`, `revision`, `version_date`, `version_time`, `classes`, `enums`.
  Each class carries `name`, `module` (the binary it lives in), `projectName`,
  `cppName`, `size`, `alignment`, `flags` / `flags2`, `parents[]`, `fields[]`
  (`name`, `offset`, `type`, `typeModule`, `metadata`), and inheritance
  depths; each enum carries `alignment` (underlying integer type) and
  `members[]`.  Integer offsets / sizes are **string-encoded** and type
  `category` values are **UPPERCASE** (`BUILTIN`, `ATOMIC`, `DECLARED_CLASS`,
  `PTR`, `FIXED_ARRAY`, `BITFIELD`, …).  As of `2.1` (SchemaTracker 0.9.0
  walkers, the v1.3.0 corpus), ATOMIC type nodes also carry
  `atomicCategory` — the explicit `SchemaAtomicCategory` discriminator
  (`ATOMIC_PLAIN` / `ATOMIC_T` / `ATOMIC_COLLECTION_OF_T` / `ATOMIC_TT` /
  `ATOMIC_I`) that previously had to be inferred from which `inner` keys
  were present — and `ATOMIC_COLLECTION_OF_T` nodes populate `count` with
  the fixed-buffer capacity `N` of the `CUtlVectorFixedGrowable< T, N >`
  family, read from the binary's own record (never parsed from the type
  name).  A non-zero `count` on an ATOMIC node therefore no longer implies
  `ATOMIC_I` — switch on `atomicCategory` instead
  ([SchemaTracker#8](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker/issues/8)).
  Optional `annotations` blocks layer
  in community-curated descriptions / notes / warnings, and an optional
  `diagram_url` on a class points at its module's UML inheritance diagram.
  Records are keyed by `(projectName, name)` — see [How duplicate class
  registrations are collapsed](#how-duplicate-class-registrations-are-collapsed)
  below.

- **`gameevents_schema.json`** — the game-event registry.  Top-level:
  `events` list; each record has `name` / `comment` / `source` /
  `properties` / `fields`.  Same `annotations` enrichment pattern.

- **`convars_schema.json`** — the console-variable table.  Top-level:
  `convars` list; each entry has `name` / `default` / `flags` /
  `description` / `value_type` (upstream's declared type, e.g. `Float32`,
  `Int32`, `Bool`, `String`; omitted when the artifact records none) /
  `min` / `max` (JSON numbers: an integer when the bound is integral, else
  a float; `null` on a side upstream leaves unbounded).  Codegen-friendly
  counterpart to the ConVars page.

- **`commands_schema.json`** — the console-command table.  Top-level:
  `commands` list; each entry has `name` / `flags` / `description` /
  `has_completion_callback` (boolean: the command registers an argument
  autocomplete callback).

- **`well_known_constants.json`** — community-curated reference tables
  for integer / enum values downstream tooling needs but that the schema
  doesn't expose as named enum types (team numbers, `m_gamePhase`,
  `CSWeaponState_t`, …).  Top-level: `constants` list; each entry has
  `name` / `comment` / `members[]` with the same `annotations` pattern.

- **`proto/*.proto`** — the build's protobuf definitions as text, copied from
  SchemaTracker (including the vendored `google/protobuf/*` well-knowns) and
  normalised with a single shared
  `option csharp_namespace = "CS2OpenDev.Protobuf";` so C# codegen doesn't
  drop every message into the global namespace (a CS0433 collision hazard).
  Unresolvable (dangling) imports are dropped.  No `package` statement is
  added — the decompiled protos use hundreds of root-qualified (`.Type`)
  cross-references that assume the empty package, so packaging them would break
  resolution.  This is a **per-file reference, not a set that compiles as a
  unit** — see [below](#proto--a-per-file-reference-not-a-compilable-set).
  Most consumers should prefer SchemaTracker's prebuilt `protos.descriptorset`
  (`protoc --descriptor_set_in`, which skips text parsing and import
  resolution entirely); these files are for compiling the protos from source.

- **`field_history.json`** — whole-history evolution of every
  `(class, field)`, projected from SchemaTracker's cumulative
  `schema_evolution.json` (Layer A).  Top-level: `baseline_build`,
  `latest_build`, `transition_count`, `fields` list (each `class` /
  `field` / `firstSeenBuild` / `lastSeenBuild` / `typeHistory`, plus an
  overlay-supplied `confirmedRename` where the community has verified one),
  and `enums`.  **`[firstSeenBuild, lastSeenBuild]` is a presence *hull*,
  not continuous presence**: a field can be absent for intermediate builds
  with no trace in this file (e.g. the 775 classes that vanished at
  `22876476 → 22877907` and returned one build later).  Reconstruct exact
  presence from `schema_evolution.json`'s per-transition add/remove ops.
  The evolution artifact's neutral rename/move *evidence surfaces*
  (`pairedEvidence` plus the unselected `pairCandidates` /
  `classPairCandidates` / `fieldMoveCandidates` lists) are **not**
  projected into this file — read them from the artifact itself; the
  [Schema History](../schema-history.md) page documents them and serves
  as the human-readable break radar.  Serves alias resolution /
  forward-back schema migration for demo parsers and SDKs.

All six files share a single top-level `schema_format_version` string
that is bumped as a family.  Bump the major when a field is removed or
renamed in any of them; bump the minor when a field is added.
Additive `annotations` blocks do not require a bump.

## Coverage — runtime only

SchemaTracker walks the **shipped CS2 runtime binaries** in-process, so
`cs2_schema.json` covers exactly the schema those binaries register
(`client`, `server`, `entity2`, `pulse_runtime_lib`, `particleslib`,
`animgraphlib`).  The Source 2 editor / tooling schema (hammer, modeldoc,
resourcecompiler, worldrenderer, …) is intentionally **not** present — it
never ships in the game.

## Class records with `size > 0` and no fields

1 classes in `cs2_schema.json` report a non-zero `size` but
expose zero fields.  These are internal Source 2 runtime classes that the
schema system knows the binary size of but never registers field-level
reflection for.  Downstream codegen consumers can safely emit them as
empty classes; field-level layout is not recoverable from the binary.

## Format reference

Full per-key documentation lives in
[`AGENTS.md`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/AGENTS.md#cs2_schemajson-format)
at the repository root.

## `proto/` — a per-file reference, not a compilable set

The `.proto/` directory mirrors SchemaTracker's decompiled protobuf
sources (the vendored `google/protobuf/*` well-knowns are included so
imports resolve).  Because the decompiled files share the **empty**
package, a few global symbols are defined in more than one file, so
`protoc *.proto` over the whole directory fails on a redefinition.
Each collision below is between exactly **two** files; compile any
subset that does not include both files of a listed pair and it
resolves cleanly (the demo/engine closure used by CS2 demo parsers
is one such subset).

**Dropped unresolved imports** (dangling in the decompile; each is marked with a comment in the file):

- `networkbasetypes.proto: google/protobuf/descriptor.proto`
- `networkbasetypes.proto: network_connection.proto`
- `networkbasetypes.proto: valveextensions.proto`

## Auto-generated — do not hand-edit

These files are regenerated every 4 hours from the latest
CS2OpenDev-SchemaTracker build by
[`.github/workflows/generate-docs.yml`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/.github/workflows/generate-docs.yml).
To change the generated output, edit the generator
(`docs/generate_docs.py`) or the community overlays under
`docs/overlays/` instead.

## Type vocabulary observed in this build

Auto-derived from the actual content of `cs2_schema.json` so
the documented vocabulary tracks upstream additions.

### Field `type.category` values

`ATOMIC`, `BITFIELD`, `BUILTIN`, `DECLARED_CLASS`, `DECLARED_ENUM`, `FIXED_ARRAY`, `PTR`

### `builtin` type names

`bool`, `char`, `float32`, `int16`, `int32`, `uint16`, `uint32`, `uint8`

### `atomic` type names

`BASEPTR`, `CEntityHandle`, `CEntityIndex`, `CEntityOutputTemplate< CBaseModelEntity::OnDamageLevelChangedArgs_t >`, `CEntityOutputTemplate< float32 >`, `CGlobalSymbol`, `CHandle< CBaseEntity >`, `CHandle< CBaseFilter >`, `CHandle< CBasePlayerController >`, `CHandle< CCSPlayerController >`, `CHandle< CEconWearable >`, `CHandle< C_BaseEntity >`, `CHandle< C_CS2HudModelArms >`, `CHandle< C_EconWearable >`, `CNetworkUtlVectorBase< CHandle< CEconWearable > >`, `CTransform`, `CTransformWS`, `CTypedBitVec< 64 >`, `CUtlLeanVector< CConstraintSlave >`, `CUtlOrderedMap< CGlobalSymbol, int32 >`, `CUtlString`, `CUtlStringToken`, `CUtlSymbolLarge`, `CUtlVector< CBoneConstraintPoseSpaceBone::Input_t >`, `CUtlVector< CConstraintTarget >`, `CUtlVector< CEntityHandle >`, `CUtlVector< CHandle< CBaseEntity > >`, `CUtlVector< CTransform >`, `CUtlVector< C_BulletHitModel* >`, `CUtlVector< RelationshipOverride_t >`, `CUtlVector< ResponseContext_t >`, `CUtlVector< sndopvarlatchdata_t >`, `CUtlVector< thinkfunc_t >`, `CUtlVectorEmbeddedNetworkVar< EntityRenderAttribute_t >`, `CUtlVectorEmbeddedNetworkVar< ViewAngleServerChange_t >`, `C_NetworkUtlVectorBase< CHandle< C_EconWearable > >`, `C_UtlVectorEmbeddedNetworkVar< EntityRenderAttribute_t >`, `C_UtlVectorEmbeddedNetworkVar< ViewAngleServerChange_t >`, `Color`, `ENTITYFUNCPTR`, `QAngle`, `USEPTR`, `Vector`, `VectorWS`

### ATOMIC `type.atomicCategory` values (schema_format_version 2.1+)

`ATOMIC_COLLECTION_OF_T`, `ATOMIC_I`, `ATOMIC_PLAIN`, `ATOMIC_T`, `ATOMIC_TT`, `ATOMIC_UNSPECIFIED`

### Metadata keys (class / field / enum / member)

- `MGetKV3ClassDefaults`
- `MKV3TransferSaveOpsForField`
- `MNotSaved`
- `MPhysPtr`
- `MSaveBehavior`


_Last regenerated against CS2 build `hl2sdk-cs2/5f891c9026230cce0fc0a3fc4b5fef1c467a1385/v1/3d1200e346019c59` (2026-08-28)._
