# CS2 Developer Reference — AI Agent Context

This file is designed to be loaded as context into any AI coding assistant
(GitHub Copilot, Claude Code, Cursor, ChatGPT, Gemini, etc.) by external
developers working on **Counter-Strike 2 tooling, plugins, demo parsers,
game servers, or any other CS2-related project**.

You do **not** need to clone this repository. Paste this file's raw URL into
your AI tool's context, or copy-paste the content directly into a system
prompt / custom instructions field:

```
https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/AGENTS.md
```

---

## What this documentation covers

This repository contains auto-generated, structured documentation for
Counter-Strike 2, extracted from a single upstream source and updated
automatically every 4 hours:

- [`CS2OpenDev/CS2OpenDev-SchemaTracker`](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker)
  — a deterministic, provenance-tracked extraction that walks the shipped
  CS2 **runtime binaries** in-process and emits, per game build, one
  internally consistent set of JSON + protobuf artifacts: entity
  classes/structs/enums (with **memory offsets**, **type sizes**, parent
  chains, binary module, and metadata), the build's protobuf descriptors,
  network/demo message tables, ConVars, commands, game events, and the
  game-content tables (items, game modes, surfaces, props, maps).

Because SchemaTracker reads only the game binaries, coverage is
**binary-derived**: the schema is whatever the shipped binaries register,
never reconstructed from source. On `windows-x86_64` that includes both the
shipped runtime modules (`client`, `server`, `entity2`, …) and the
Windows-only tool binaries Valve ships alongside the game (`hammer.dll`,
`resourcecompiler.dll`, `worldrenderer.dll`, `modeldoc_editor.dll`, and
others), so the Source 2 editor / tooling schema is present, not absent. As
of build 25000182 (2026-08-28 Steam date; see `docs/generated/data/meta.json`
for current numbers) the schema spans **47 modules**, 3,590 distinct
top-level classes, 611 enums, and 18,549 fields.

The site base is `https://cs2opendev.github.io/CS2OpenDev-Docs`. Entity
pages live at `/schemas/<module>/<TypeName>/` (case preserved, `::`
written as `.`, see [URL scheme](#url-scheme) below); the JSON schema
files below keep their old path, `/generated/downstream-codegen-schemas/<file>`.
Old `/generated/schemas/...`-style URLs from the previous Jekyll site
redirect to the new paths.

The documentation covers:

| Section | Contents | Browse URL |
|---------|----------|------------|
| **Schema entities** | All C++ entity classes, structs, and enums the CS2 runtime + tool binaries register (3,590 classes, 611 enums across 47 modules on build 25000182), each with field offsets, class sizes, flags, and the binary module it lives in | `/schemas/` |
| **Protobufs** | The build's `.proto` message definitions: game events, network messages, GC messages, demo format (40 files, 775 messages counting nested types), read from SchemaTracker's prebuilt `FileDescriptorSet`.  These are reconstructed from the binaries, so they carry **no source comments** (see the network-message table below for the ID↔type mapping). | `/protobufs/` |
| **Network & demo messages** | Wire-protocol table: integer message ID → protobuf message type, per channel, cross-linked to the protobuf pages | `/network-messages/` |
| **ConVars** | Every console variable with default value, flags, value type, min/max, and description (3,955 entries) | `/convars/` |
| **Commands** | Every console command with flags and description (1,132 entries) | `/commands/` |
| **Game events** | The parsed `.gameevents` registry, one entry per event, anchored so a duplicate name across source files (`round_end` in all three `.gameevents` files, for example) still gets a unique link | `/game-events/` |
| **Items & economy** | Items, prefabs, paint kits (skins), sticker kits, music kits, rarities, qualities | `/items/`, `/items/paint-kits/`, `/items/sticker-kits/`, `/items/music-kits/` |
| **Maps / game modes / surfaces / props** | Radar overviews and bomb-site coordinates, game types & modes, surface physics, breakable-prop data: each its own page now | `/maps/`, `/game-modes/`, `/surfaces/`, `/props/` |
| **Binaries / modules** | Every binary in the build, with SHA-256 and, where the binary matches a schema module, the `projectName` it registers | `/modules/` |
| **Changelog** | Per-build diff (added / removed / changed) against the previous build | `/changelog/` |
| **UML diagrams** | Mermaid class-hierarchy diagrams; every module has its own at `/schemas/<module>/hierarchy/`, and `/schemas/hierarchy/` is the combined server + client tree that replaced the old single `server_hierarchy` diagram | `/schemas/hierarchy/` |
| **Codegen schema formats** | Overview of the five downstream JSON schema files below: shape, versioning, migration notes | `/codegen-schemas/` |
| **Entity schema** | `downstream-codegen-schemas/cs2_schema.json`: the entity schema in SchemaTracker's **native** shape (top-level `generator` / `build_id` / `platform` / `revision` / `version_date` / `version_time` / `classes` / `enums`), enriched with optional community `annotations`.  See the [format reference](#cs2_schemajson-format) below. | `/generated/downstream-codegen-schemas/cs2_schema.json` |
| **Game events schema** | `downstream-codegen-schemas/gameevents_schema.json`: the game-event registry.  Top-level `events` list; each event has `name` / `comment` / `source` / `properties` / `fields`.  Same `annotations` enrichment pattern as `cs2_schema.json`. | `/generated/downstream-codegen-schemas/gameevents_schema.json` |
| **ConVars schema** | `downstream-codegen-schemas/convars_schema.json`: top-level `convars` list, each `{ name, default, flags, description }`. | `/generated/downstream-codegen-schemas/convars_schema.json` |
| **Commands schema** | `downstream-codegen-schemas/commands_schema.json`: top-level `commands` list, each `{ name, flags, description }`. | `/generated/downstream-codegen-schemas/commands_schema.json` |
| **Well-known constants** | `downstream-codegen-schemas/well_known_constants.json`: integer / enum values downstream tooling needs but that the schema doesn't expose as named enum types (team numbers, `m_gamePhase`, `CSWeaponState_t`, …).  Source of truth is `docs/overlays/well_known_constants.yml`. | `/generated/downstream-codegen-schemas/well_known_constants.json` |
| **Schema history** | Field-precise build-to-build evolution of the entity schema, rendered from SchemaTracker's cumulative, facts-only `schema_evolution.json` (Layer A).  Documents the artifact's neutral rename/move **evidence surfaces**: the frozen `pairedEvidence` 1:1 pairs plus the unselected candidate lists added in artifact rev 0.6.0 (`pairCandidates`, `classPairCandidates`, `fieldMoveCandidates`), the 0.7.0 calendar axis (`fromManifestCreatedUtc` / `toManifestCreatedUtc`) and attribute coverage, and the 0.8.0 per-key `metaOps`.  No rename or safety verdict is ever asserted; promotion happens via `docs/overlays/schema-lens.yml`. | `/schema-history/` |
| **Field history schema** | `downstream-codegen-schemas/field_history.json`: whole-history record per `(class, field)`: `firstSeenBuild` / `lastSeenBuild` / `typeHistory`, plus a community-verified `confirmedRename` block where one exists.  **`[firstSeenBuild, lastSeenBuild]` is a presence *hull*, not continuous presence**. Reconstruct exact presence from `schema_evolution.json`'s transitions.  Windows is the canonical platform and a strict superset in class coverage (historical Windows-only tool binaries such as `hammer.dll` / `sfm.dll` have no Linux counterparts). | `/generated/downstream-codegen-schemas/field_history.json` |

### URL scheme

Prefix every path in this document with the site base to get a full URL,
e.g. `https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/server/CBaseEntity/`.

- Entity page: `/schemas/<module>/<TypeName>/`. Module is the schema's
  `projectName` (`server`, `client`, `entity2`, …), case is preserved, and
  `::` in a nested type name is written as `.` (`CBoneConstraintPoseSpaceBone::Input_t`
  becomes `/schemas/modellib/CBoneConstraintPoseSpaceBone.Input_t/`).
- Module index: `/schemas/<module>/`. Module inheritance tree:
  `/schemas/<module>/hierarchy/`. Combined server + client tree:
  `/schemas/hierarchy/`.
- Proto file page: `/protobufs/<stem>/`, with one anchor per message or
  enum: `#<QualifiedName>` for a top-level type, `#Parent.Nested` for a
  nested one.
- ConVars, commands, and game events are single pages with one entry per
  anchor: `/convars/#<name>`, `/commands/#<name>`, `/game-events/#<anchor>`.
  A game event name that repeats across `.gameevents` source files gets a
  source suffix on the anchor instead of colliding, e.g. `player_death-mod`.
- The five `downstream-codegen-schemas/*.json` files and `field_history.json`
  are the one exception to the new scheme: they keep serving at
  `/generated/downstream-codegen-schemas/<file>`, matching their path in
  the git repository.

### Twin entities and `projectName`

A class compiled into both the client and server binaries (`CCSPlayerController`
in `server`, `C_CSPlayerController` and `CCSPlayerController` in `client`) is
not one record: SchemaTracker emits one independent record per
`(projectName, name)` pair, each with its own offsets, because client and
server layouts can and do diverge. `module` on a record names the actual
binary (`server.dll`, `client.dll`, …); `projectName` is the grouping axis
the site and `docs/overlays/` key on. A generator fix on this branch means
a server-module twin page no longer silently inherits its offsets from the
client record that happens to share its name; each twin's page, and its
page title, now names the module it was built from.

### The `docs/generated/data/` bundle

Alongside the `downstream-codegen-schemas/` JSON above, `docs/site_data.py`
writes a second, larger JSON bundle to `docs/generated/data/` that backs
the Astro site's non-entity pages. It is **not served at a site URL**:
only `downstream-codegen-schemas/` is copied into the site's build output,
so reach it via the raw GitHub path,
`https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/data/<file>`.
Full field-level documentation is in
[`docs/generated/data/README.md`](docs/generated/data/README.md); one line
each:

- `meta.json`: build identity, per-family counts, and the 47-module list this document's counts are drawn from.
- `protobufs.json`: every proto file, flattened messages/enums (nested types included), type resolution, and the wire-id join that backs `network.json`.
- `convars.json` / `commands.json`: the ConVars and commands tables, with the shared `flags` legend from `docs/overlays/convar_flags.yml`.
- `gameevents.json`: the game-event registry with anchors and the wire `key_t` type-code legend.
- `items.json` / `paint_kits.json` / `sticker_kits.json` / `music_kits.json`: items and their prefab-resolved display fields, skins, stickers, music kits.
- `maps.json` / `game_modes.json` / `props.json` / `surfaces.json`: map radar data, game modes, breakable-prop collision groups, surface materials.
- `modules.json`: every binary in the build with its SHA-256 and, where it matches one, the schema module it registers.
- `network.json`: the union of RTTI-recovered and enum-derived message-id tables, by channel.
- `changelog.json` / `schema-history.json`: the latest build-pair diff and the full cross-build schema evolution record.

### `cs2_schema.json` format

The file is the entity schema in **CS2OpenDev-SchemaTracker's native shape**
(proto3-canonical JSON), with optional community `annotations` layered on.
It is **not** JSON Schema.  Two mechanical conventions matter to consumers:
integer `offset` / `size` / `count` values are **string-encoded**
(`"offset": "8"`), and type `category` values are **UPPERCASE**
(`BUILTIN`, `ATOMIC`, `DECLARED_CLASS`, `DECLARED_ENUM`, `PTR`,
`FIXED_ARRAY`, `BITFIELD`).

**Top-level**

```json
{
  "schema_format_version": "2.2",
  "generator": "https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker",
  "build_id": 25000182,
  "platform": "windows-x86_64",
  "revision": "hl2sdk-cs2/…",
  "version_date": "2026-08-28",
  "version_time": "2026-08-28T20:16:08Z",
  "classes": [...],
  "enums":   [...]
}
```

`build_id` is the **Steam CS2 game build** the schema describes — numeric,
monotonic, and the correct key to stamp into a package version or
`AssemblyMetadata`.  `platform` names the OS artifact set the schema projects
(`windows-x86_64`, the superset that also carries the tool-side modules).
`revision` identifies the **walker** (the hl2sdk pin), not the game build —
two different CS2 builds read by the same pinned hl2sdk share a `revision`
but not a `build_id`, so both keys are kept; they answer different questions.
`generator` / `version_date` / `version_time` round out the provenance (date
is ISO-8601).
`schema_format_version` describes the JSON shape itself — major bumps on
field removal / rename, minor bumps on field addition.  Additive
`annotations` blocks do not require a bump.  All five codegen schemas
(`cs2_schema.json`, `gameevents_schema.json`, `convars_schema.json`,
`commands_schema.json`, `well_known_constants.json`) carry the same
`schema_format_version` value.  **`2.0` is a breaking change from the
DumpSource2-mirror `1.x`** — the source moved to SchemaTracker and the
class/enum shape is native (camelCase keys, string ints, UPPERCASE
categories, a `module`/`projectName` split).

**Per-class entry** (one per `(projectName, name)` — cross-project twins like
`CCSPlayerController` in both `client` and `server` emit one record each;
multiple binary registrations under a single `projectName`, common for
`pulse_runtime_lib` cell classes, collapse to one):

| Key | What it carries |
|---|---|
| `name` | C++ class / struct name. |
| `module` | The **binary** the class is registered in (`client.dll` / `server.dll` / `engine2.dll` / `animationsystem.dll` / `!GlobalTypes`; `.so` names on Linux). |
| `projectName` | The source module / project (`client`, `server`, `entity2`, `pulse_runtime_lib`, `particleslib`, `animgraphlib`) — the axis the doc pages group by. |
| `cppName` | The class's C++ symbol name. |
| `size` | Class instance size in bytes (the C++ `sizeof`), **string-encoded**. |
| `alignment` | Byte alignment (`1`/`2`/`4`/`8`/`16`). |
| `flags`, `flags2` | Raw schema class-flag bitmasks. |
| `singleInheritanceDepth`, `multipleInheritanceDepth` | Inheritance-chain depths. |
| `parents` | Inheritance list as `[{module, name, offset}]`.  Empty when the class has no base. |
| `fields` | List of field records (see below). |
| `staticFields` | Static field records (often empty). |
| `metadata` | Class-level metadata as `[{name, value?, valueParsed?}]`.  Preserves runtime reflection tags like `MGetKV3ClassDefaults`, `MNetworkVarNames`, etc. |
| `annotations` *(optional)* | Community enrichment: `{description?, notes?, warning?}`.  Only present when an overlay matches the entity. |
| `diagram_url` *(optional)* | Absolute URL of the class's module UML inheritance diagram.  Present for classes whose `projectName` has a generated diagram page. |

**Per-field entry** (under a class's `fields` list):

| Key | What it carries |
|---|---|
| `name` | Field identifier (e.g. `m_hPawn`). |
| `offset` | Byte offset within the containing class, **string-encoded**. |
| `type` | Structured type record (see below). |
| `typeModule` | Binary module of the referenced declared type, or `""`. |
| `metadata` | Field-level metadata as `[{name, value?, valueParsed?}]` — `MNetworkVar`, `MNetworkChangeCallback`, `MPropertyFriendlyName`, `MPropertyDescription`, etc. |
| `annotations` *(optional)* | Community enrichment: `{description?, notes?, warning?}`.  Only present when an overlay matches the field. |

**Field `type` shapes.**  `category` (UPPERCASE) discriminates the variant,
and — importantly — `name` already carries the **fully-rendered** C++ type
string for every category, so the simplest consumers can read `name`
directly and ignore `inner`.  `count` is string-encoded.

| `category` | Other keys | Example `name` |
|---|---|---|
| `BUILTIN` | `name` | `"int32"` |
| `DECLARED_CLASS` | `name`, `module` | `"CCSPlayerPawn"` |
| `DECLARED_ENUM` | `name`, `module` | `"AmmoIndex_t"` |
| `ATOMIC` | `name`, `atomicCategory`, `inner` (sometimes `inner2`, `inner3`), `count` (see below) | `"CHandle< CCSPlayerPawn >"` |
| `PTR` | `name`, `inner` | `"CPulse_Chunk*"` |
| `FIXED_ARRAY` | `name`, `inner`, `count` | `"char[128]"` |
| `BITFIELD` | `name`, `count` (bits) | `"bitfield:1"` |

**ATOMIC sub-taxonomy** (`schema_format_version` 2.1+, SchemaTracker 0.9.0
walkers / v1.3.0 corpus): ATOMIC nodes carry `atomicCategory` — the engine's
own `SchemaAtomicCategory_t` discriminator, previously only inferable from
which `inner` keys were present:

| `atomicCategory` | Meaning | `count` |
|---|---|---|
| `ATOMIC_PLAIN` | No template args (`CUtlString`, `Vector`, …) | `"0"` |
| `ATOMIC_T` | One type arg (`CHandle< T >`, `CUtlVector< T >`, …) — `inner` is `T` | `"0"` |
| `ATOMIC_COLLECTION_OF_T` | Collection of `T` — `inner` is `T` | Fixed-buffer capacity `N` for the `CUtlVectorFixedGrowable< T, N >` / `CUtlLeanVectorFixedGrowable< T, N >` family (read from the binary's `m_nFixedBufferCount`, never parsed from the name); `"0"` for unbounded collections |
| `ATOMIC_TT` | Two type args (`CUtlOrderedMap< K, V >`, …) — `inner` + `inner2` | `"0"` |
| `ATOMIC_I` | Integer template arg (`CBitVec< 10 >`, `CTypedBitVec< 64 >`) | The integer arg |

A non-zero `count` on an ATOMIC node therefore no longer implies
`ATOMIC_I` — switch on `atomicCategory` instead
([SchemaTracker#8](https://github.com/CS2OpenDev/CS2OpenDev-SchemaTracker/issues/8)).
Artifacts produced by pre-0.9.0 walkers lack `atomicCategory`; treat its
absence as "infer from `inner` keys as before".

`inner` is itself a type record — recurse when you need the element type of
a template / pointer / array.  When the innermost type is a
`DECLARED_CLASS` or `DECLARED_ENUM`, its `module` field disambiguates which
class lives where.

**Per-enum entry**:

| Key | What it carries |
|---|---|
| `name` | Enum name. |
| `module` | The binary the enum is registered in. |
| `alignment` | Underlying integer type name (`uint32_t`, `int8_t`, …). |
| `size` | Underlying byte width. |
| `flags` | Raw enum-flag bitmask. |
| `members` | List of `{name, value, metadata}` member records; `value` is **string-encoded** and may be negative.  Many members carry `MPropertyFriendlyName` / `MPropertyDescription`. |
| `annotations` *(optional)* | Community enrichment, same shape as on classes. |

**Per-enum-member entry**:

| Key | What it carries |
|---|---|
| `name` | Member identifier. |
| `value` | Numeric value. |
| `metadata` | Member-level metadata as `[{name, value?}]`. |
| `annotations` *(optional)* | Community enrichment when the overlay supplies a per-member description. |

A consumer that has never heard of `annotations` ignores the key and gets SchemaTracker's native record unchanged.  A consumer that reads `annotations` gets the curated descriptions / notes / warnings on top.

**Parsed KV3 defaults.**  Class- and field-level `metadata` entries
named `MGetKV3ClassDefaults` carry the entity's KV3-encoded default
values as an escaped string.  When that string parses cleanly as JSON
(with tolerant handling of trailing commas and `<HIDDEN FOR DIFF>`
sentinels), the generator adds a sibling `value_parsed` key alongside
the raw `value` so consumers can read the structured form directly.
The raw `value` is always preserved unchanged; `value_parsed` is
absent when the string fails to parse (about 5% of entries, including
the upstream "Could not parse KV3 Defaults" sentinel).

**Classes with `size > 0` and no fields.**  ~165 classes (e.g.
`CNmGraphInstance`, `CBasePulseGraphInstance`, `CNavVolume`, `CBtNode`)
report a non-zero `size` but expose zero fields.  These are internal
Source 2 runtime classes that the schema reflection system knows the
binary size of but never registers field-level reflection for.
Downstream consumers can emit them as empty (sized) classes; field
layout is not recoverable from the dump.

#### Deriving handle kind from atomic name

There is no dedicated `handle_kind` discriminator — recover it from the
atomic `name` directly.  Every handle atomic name derives from
`CBaseHandle` and the name carries the distinction (the counts below are
field occurrences and may drift build to build):

| Atomic name | Kind | Notes |
|---|---|---|
| `CHandle` | entity | Weak reference to a `CBaseEntity`-derived target.  408 fields. |
| `CEntityHandle` | entity | Non-templated entity handle; same lifetime semantics as `CHandle` but no compile-time type tag.  28 fields. |
| `CStrongHandle` | strong | Resource handle that keeps its target alive (refcount).  Used for KV3/resource references.  187 fields. |
| `CStrongHandleCopyable` | strong | `CStrongHandle` variant with copy-constructor semantics.  5 fields. |
| `CStrongHandleVoid` | strong | Type-erased `CStrongHandle<void>` for opaque resource targets.  2 fields. |
| `CWeakHandle` | weak | Non-owning resource handle that doesn't keep the target alive.  42 fields. |

Suggested derivation, in priority order: exact-name table lookup
first, then prefix match (`CStrongHandle*` → `strong`,
`CWeakHandle*` → `weak`, anything else containing `Handle` and
derived from `CBaseHandle` → `entity`).  The exact-name table is
authoritative for the current schema; the prefix rule is the
forward-compatible fallback if upstream adds new variants.

### `gameevents_schema.json` format

Same enrichment pattern as `cs2_schema.json`, applied to the parsed
`.gameevents` registry.  Top-level is a single `events` list:

```json
{
  "events": [
    {
      "name": "player_death",
      "comment": "a game event, name may be 32 charaters long",
      "source": "game.gameevents",
      "properties": {},
      "fields": [
        {"name": "userid",   "type": "player_controller_and_pawn", "comment": "user ID"},
        {"name": "attacker", "type": "player_controller_and_pawn", "comment": "attacker"},
        {"name": "weapon",   "type": "string", "comment": "weapon name killer used"}
      ],
      "annotations": {"description": "Fired when a player is killed."}
    }
  ]
}
```

| Key | What it carries |
|---|---|
| `name` | Event name (no spaces, ≤32 chars by upstream convention). |
| `comment` | Trailing `//` comment from the source `.gameevents` line. |
| `source` | Basename of the originating file (`core.gameevents`, `game.gameevents`, `mod.gameevents`, …). |
| `properties` | Event-level metadata from the KV1 source (`local`, `reliable` flags). |
| `fields` | List of `{name, type, comment, annotations?}` records. |
| `annotations` *(optional)* | Community enrichment from `docs/overlays/gameevents.yml`. |

Field `type` values are the raw .gameevents type tags — `none`,
`string`, `bool`, `byte`, `short`, `long`, `float`, `uint64`, `local`,
`player_controller`, `player_controller_and_pawn`, `player_pawn`,
`ehandle`.  See the [generated reference page](https://cs2opendev.github.io/CS2OpenDev-Docs/game-events/)
for human-readable type meanings.

---

## CS2 Architecture overview

CS2 is built on Source 2. Its entity system uses a
**controller / pawn split**:

- A **controller** (`CBasePlayerController` → `CCSPlayerController`) is a
  lightweight, persistent entity that represents a connected client for the
  lifetime of the connection. It survives round resets.
- A **pawn** (`CBasePlayerPawn` → `CCSPlayerPawn`) is the physical, in-world
  representation of the player. It is recreated each round. The controller
  points to the current pawn via `m_hPlayerPawn`.

All server-side entities ultimately derive from `CEntityInstance` →
`CBaseEntity`. Client-side mirrors are `C_BaseEntity`-rooted (prefix `C_`).

---

## Key server-side entities

### `CBaseEntity`
*Root entity. Every server entity derives from this.*
Full reference: https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/server/CBaseEntity/

Key fields:

| Field | Type | Notes |
|-------|------|-------|
| `m_iHealth` | `int32` | Current health points |
| `m_iTeamNum` | `uint8` | 0 = unassigned, 1 = spectator, 2 = T, 3 = CT |
| `m_vecAbsOrigin` | `Vector` | World-space position |
| `m_angAbsRotation` | `QAngle` | World-space rotation |
| `m_iName` | `CUtlSymbolLarge` | Targetname / entity name |
| `m_bTakesDamage` | `bool` | Whether entity can receive damage |
| `m_nNextThinkTick` | `GameTick_t` | Next simulation tick |

---

### `CCSPlayerController`
*One per connected client, persists across rounds.*
Full reference: https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/server/CCSPlayerController/

Inheritance: `CEntityInstance` → `CBaseEntity` → `CBasePlayerController` → `CCSPlayerController`

Key fields:

| Field | Type | Notes |
|-------|------|-------|
| `m_hPlayerPawn` | `CHandle<CCSPlayerPawn>` | Handle to the active pawn (may change each round) |
| `m_iTeamNum` | `uint8` | Team: 2 = T, 3 = CT |
| `m_iszPlayerName` | `CUtlSymbolLarge` | Display name |
| `m_steamID` | `uint64` | Steam account ID |
| `m_iScore` | `int32` | Match score |
| `m_iPing` | `uint32` | Network RTT in milliseconds |
| `m_szClan` | `CUtlSymbolLarge` | Clan/team tag shown in scoreboard |
| `m_szCrosshairCodes` | `CUtlSymbolLarge` | Encoded crosshair share-code |
| `m_iPendingTeamNum` | `uint8` | Pending team change |
| `m_iCoachingTeam` | `int32` | Non-zero if player is coaching |
| `m_nPlayerDominated` | `uint64` | Bitmask of players this controller is dominating |
| `m_pInGameMoneyServices` | `CCSPlayerController_InGameMoneyServices*` | Money/economy component |
| `m_pInventoryServices` | `CCSPlayerController_InventoryServices*` | Item/skin component |
| `m_pActionTrackingServices` | `CCSPlayerController_ActionTrackingServices*` | Stat-tracking component |
| `m_pDamageServices` | `CCSPlayerController_DamageServices*` | Damage-log component |

---

### `CCSPlayerPawn`
*The in-world player body; recreated each round.*
Full reference: https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/server/CCSPlayerPawn/

Inheritance: `CBaseEntity` → `CBaseModelEntity` → `CBaseFlex` → `CBaseAnimGraph` → `CBaseCombatCharacter` → `CBasePlayerPawn` → `CCSPlayerPawnBase` → `CCSPlayerPawn`

Key fields:

| Field | Type | Notes |
|-------|------|-------|
| `m_vecVelocity` | `Vector` | Current velocity |
| `m_flFallVelocity` | `float32` | Vertical fall speed |
| `m_flStamina` | `float32` | Stamina (affects accuracy) |
| `m_flVelocityModifier` | `float32` | Speed multiplier |
| `m_iShotsFired` | `int32` | Shots fired this burst (recoil tracking) |
| `m_flFlashDuration` | `float32` | Remaining flashbang blind time (seconds) |
| `m_flFlashMaxAlpha` | `float32` | Peak flash intensity (0–255) |
| `m_bIsScoped` | `bool` | Currently scoped in |
| `m_bIsWalking` | `bool` | Currently walking (shifted) |
| `m_bResumeZoom` | `bool` | Will re-scope after shooting |
| `m_iPlayerState` | `int32` | Death-state flags |
| `m_hActiveWeapon` | `CHandle<CBasePlayerWeapon>` | Currently held weapon |
| `m_hObserverTarget` | `CHandle<CBaseEntity>` | Entity being spectated |

---

### `CCSGameRules`
*Singleton holding all match-level state.*
Full reference: https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/server/CCSGameRules/

Accessed via the `CCSGameRulesProxy` entity on the client. Inheritance:
`CGameRules` → `CMultiplayRules` → `CTeamplayRules` → `CCSGameRules`

Key fields:

| Field | Type | Notes |
|-------|------|-------|
| `m_bFreezePeriod` | `bool` | Buy phase (players frozen) |
| `m_bWarmupPeriod` | `bool` | Pre-match warmup active |
| `m_gamePhase` | `int32` | 1=First Half, 2=Second Half, 3=Pre-OT, 4=OT, 5=Game Over |
| `m_totalRoundsPlayed` | `int32` | Total rounds completed |
| `m_nRoundsPlayedThisPhase` | `int32` | Rounds in current half/OT period |
| `m_nOvertimePlaying` | `int32` | Overtime period count (0 = regulation) |
| `m_fRoundStartTime` | `GameTime_t` | When freeze time ended |
| `m_iRoundTime` | `int32` | Round time limit (seconds) |
| `m_iFreezeTime` | `int32` | Freeze-time duration (seconds) |
| `m_bMapHasBombTarget` | `bool` | Map has bomb sites |
| `m_bMapHasRescueZone` | `bool` | Map has hostage rescue zones |
| `m_iNumCT` | `int32` | Players on CT side |
| `m_iNumTerrorist` | `int32` | Players on T side |
| `m_bBombDropped` | `bool` | Bomb currently dropped on ground |
| `m_bBombPlanted` | `bool` | Bomb currently planted |
| `m_nEndMatchMapGroupVoteTypes` | `int32[10]` | Map vote options |
| `m_eMatchDevice` | `int32` | Device type (PC, console) |

---

### `CCSWeaponBase` / `CCSWeaponBaseGun`
*Base weapon classes.*
Full reference: https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/server/CCSWeaponBase/

Inheritance: `CBaseEntity` → `CBaseModelEntity` → `CBasePlayerWeapon` → `CCSWeaponBase` → `CCSWeaponBaseGun`

Key `CCSWeaponBase` fields:

| Field | Type | Notes |
|-------|------|-------|
| `m_iClip1` | `int32` | Rounds remaining in magazine |
| `m_iPrimaryAmmoCount` | `int32` | Ammo in reserve |
| `m_fLastShotTime` | `GameTime_t` | GameTime of most recent shot |
| `m_bInReload` | `bool` | Reload animation in progress |
| `m_bBurstMode` | `bool` | Burst-fire mode active (Glock, FAMAS) |
| `m_flNextPrimaryAttack` | `GameTime_t` | Earliest next fire time |
| `m_zoomLevel` | `int32` | Scope zoom level (0 = unscoped) |
| `m_iSilencerOn` | `bool` | Silencer attached (M4A1-S, USP-S) |
| `m_weaponMode` | `CSWeaponMode` | Fire mode enum |

All individual weapons (`CAWP`, `CAK47`, `CDEAGLE`, etc.) inherit from
`CCSWeaponBaseGun` and typically carry 0 additional fields (all data is in
`CCSWeaponBaseVData` and the base classes).

Full weapon list: https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/server/

---

### `CPlantedC4`
*The planted bomb entity.*
Full reference: https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/server/CPlantedC4/

| Field | Type | Notes |
|-------|------|-------|
| `m_flC4Blow` | `GameTime_t` | GameTime when bomb detonates |
| `m_bBombTicking` | `bool` | Bomb is counting down |
| `m_bBombDefused` | `bool` | Bomb was successfully defused |
| `m_hBombDefuser` | `CHandle<CCSPlayerPawn>` | Pawn currently defusing |
| `m_flDefuseLength` | `float32` | Total defuse duration (with/without kit) |
| `m_flDefuseCountDown` | `GameTime_t` | Time when defuse completes |
| `m_nBombSite` | `int32` | Bombsite index (0 = A, 1 = B) |

---

## Key Protobuf message groups

### Game events (`cs_gameevents.proto`)
Reference: `/protobufs/cs_gameevents/`

CS2-specific game event messages (e.g. bomb plant/defuse, kill, round end).
Sent as `CMsgSource1LegacyGameEvent` on the network.

### CS2 user messages (`cstrike15_usermessages.proto`)
Reference: `/protobufs/cstrike15_usermessages/`

74 top-level messages sent from server to individual clients: HUD hints,
radar updates, kill cam data, round-end and match-end summaries, item
purchases, etc.

Key messages: `CCSUsrMsg_RoundEndReportData`, `CCSUsrMsg_SendAudio`,
`CCSUsrMsg_RadioText`, `CCSUsrMsg_HudMsg`, `CCSUsrMsg_KillCam`,
`CCSUsrMsg_EndOfMatchAllPlayersData`

### CS2 GC messages (`cstrike15_gcmessages.proto`)
Reference: `/protobufs/cstrike15_gcmessages/`

17 top-level messages (25 counting nested types) exchanged with Valve's
Game Coordinator that are specific to CS2: tournament data, competitive
ranking, XP progress, deep player stats, item preview blocks. The shared
Game Coordinator envelope, session, and matchmaking-hello messages live in
sibling files also under `/protobufs/`: `base_gcmessages.proto`,
`gcsdk_gcmessages.proto`, `econ_gcmessages.proto`, `gcsystemmsgs.proto`,
which together carry most of the remaining GC-related message volume.

Key messages: `PlayerRankingInfo`, `XpProgressData`, `CEconItemPreviewDataBlock`

### Core net messages (`netmessages.proto`)
Reference: `/protobufs/netmessages/`

63 top-level engine-level network messages: snapshot packets, string
tables, data tables (SendTables), server info, voice data. (`CNETMsg_Tick`
and `CSVCMsg_GameEvent` are real CS2 wire messages but are declared in
`networkbasetypes.proto`, not here: check `/protobufs/networkbasetypes/`
for those.)

Key messages: `CSVCMsg_PacketEntities`, `CSVCMsg_SendTable`,
`CSVCMsg_CreateStringTable`, `CSVCMsg_GameEventList`, `CSVCMsg_UserMessage`

### Demo file format (`demo.proto`)
Reference: `/protobufs/demo/`

Messages defining the `.dem` file format: `CDemoFileHeader`,
`CDemoPacket`, `CDemoFullPacket`, `CDemoStringTables`, `CDemoClassInfo`.
CS2 demos are written in the Source 2 "PBDEMS2" binary format. (There is
no `CDemoHeader` message in this build; the file header message is
`CDemoFileHeader`.)

### User commands (`cs_usercmd.proto`)
Reference: `/protobufs/cs_usercmd/`

`CSGOUserCmdPB` is the per-tick command sent from client to server: move
direction, view angles, attack buttons, subtick data. (There is no
`CCSUsrCmd` message in this build.)

---

## Important enums

### Team numbers
| Value | Meaning |
|-------|---------|
| `0` | Unassigned |
| `1` | Spectator |
| `2` | Terrorist (T) |
| `3` | Counter-Terrorist (CT) |

### `m_gamePhase` values (`CCSGameRules`)
| Value | Meaning |
|-------|---------|
| `1` | First Half |
| `2` | Second Half |
| `3` | Pre-overtime (halftime of OT) |
| `4` | Overtime |
| `5` | Game Over |

### `CSWeaponState_t` (weapon state)
| Value | Meaning |
|-------|---------|
| `WEAPON_NOT_CARRIED` | On the ground |
| `WEAPON_IS_CARRIED_BY_PLAYER` | In a player's inventory |
| `WEAPON_IS_ACTIVE` | Currently held / active |

---

## Schema modules quick-reference

All 47 modules on build 25000182, sorted alphabetically. `Classes`/`Enums`
are this module's counts from `meta.json`'s `modules[]` list, which
include client/server twin records, so summing this column across all 47
rows comes out higher than the top-level distinct-name totals above
(3,590 classes, 611 enums). `Description` is left blank where this
document has no specific, sourced claim to make about a module beyond its
name; `hammer`, `resourcecompiler`, `worldrenderer`, and `modeldoc_editor`
are four of the Windows-only tool binaries called out in the coverage note
above.

| Module | Classes | Enums | Description | URL |
|--------|---------|-------|--------------|-----|
| `animationsystem` | 47 | 7 | Top-level animation system | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/animationsystem/ |
| `animdoclib` | 197 | 12 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/animdoclib/ |
| `animgraphdoclib` | 158 | 14 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/animgraphdoclib/ |
| `animgraphlib` | 243 | 57 | Animation graph nodes and types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/animgraphlib/ |
| `animlib` | 180 | 37 | Core animation types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/animlib/ |
| `client` | 487 | 3 | Client-side entity mirrors and UI components | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/client/ |
| `compositematerialslib` | 10 | 7 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/compositematerialslib/ |
| `engine2` | 42 | 0 | Core engine2 types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/engine2/ |
| `entity2` | 16 | 2 | Base entity framework types (`CEntityInstance`, `GameTime_t`, …) | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/entity2/ |
| `hammer` | 7 | 3 | Hammer level editor types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/hammer/ |
| `host` | 2 | 0 | Host application types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/host/ |
| `mapdoclib` | 3 | 0 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/mapdoclib/ |
| `materialsystem2` | 15 | 5 | Material types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/materialsystem2/ |
| `mathlib_extended` | 11 | 2 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/mathlib_extended/ |
| `met` | 3 | 0 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/met/ |
| `modeldoc_editor` | 3 | 1 | Model doc editor types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/modeldoc_editor/ |
| `modellib` | 114 | 26 | Model/mesh types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/modellib/ |
| `modtools` | 2 | 0 | Mod tools types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/modtools/ |
| `navlib` | 14 | 3 | Navigation mesh types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/navlib/ |
| `networksystem` | 1 | 0 | Networking system types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/networksystem/ |
| `panorama_content` | 0 | 2 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/panorama_content/ |
| `particles` | 434 | 73 | Particle system types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/particles/ |
| `particleslib` | 21 | 18 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/particleslib/ |
| `physicslib` | 99 | 4 | Physics types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/physicslib/ |
| `pulse_runtime_lib` | 98 | 11 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/pulse_runtime_lib/ |
| `pulse_system` | 38 | 4 | Pulse scripting system | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/pulse_system/ |
| `pulsedoc_lib` | 3 | 1 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/pulsedoc_lib/ |
| `qcontrols` | 0 | 15 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/qcontrols/ |
| `rendersystemdx11` | 4 | 3 | DirectX 11 render backend types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/rendersystemdx11/ |
| `resourcecompiler` | 17 | 2 | Resource compiler pipeline types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/resourcecompiler/ |
| `resourcefile` | 6 | 0 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/resourcefile/ |
| `resourcesystem` | 48 | 0 | Resource/asset system types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/resourcesystem/ |
| `scenesystem` | 9 | 6 | Scene graph types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/scenesystem/ |
| `schemasystem` | 1 | 2 | Schema reflection system types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/schemasystem/ |
| `server` | 910 | 231 | Server-side entity classes (weapons, players, game rules, …) | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/server/ |
| `smartprops` | 149 | 18 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/smartprops/ |
| `sounddoc_lib` | 139 | 2 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/sounddoc_lib/ |
| `soundsystem` | 35 | 13 | Sound system types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/soundsystem/ |
| `soundsystem_lowlevel` | 73 | 7 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/soundsystem_lowlevel/ |
| `soundsystem_voicecontainers` | 42 | 7 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/soundsystem_voicecontainers/ |
| `steamaudio` | 17 | 0 | Steam Audio integration types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/steamaudio/ |
| `texturelib` | 4 | 6 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/texturelib/ |
| `tier2` | 2 | 0 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/tier2/ |
| `toolscene` | 11 | 1 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/toolscene/ |
| `toolutils2` | 21 | 2 |  | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/toolutils2/ |
| `vphysics2` | 14 | 1 | Havok physics integration | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/vphysics2/ |
| `worldrenderer` | 29 | 3 | World renderer types | https://cs2opendev.github.io/CS2OpenDev-Docs/schemas/worldrenderer/ |

---

## Raw GitHub URLs for deep fetching

If your AI tool supports fetching raw documents, use these URLs to load full
content for a specific section:

| Content | Raw URL |
|---------|---------|
| Server module index (lists every type → per-type pages) | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/schemas/server.md` |
| Client module index | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/schemas/client.md` |
| A single type's full memory layout (offsets + inherited fields) | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/schemas/<module>/<TypeName>.md` (e.g. `.../schemas/server/CBaseEntity.md`) |
| Entire schema, machine-readable (all types, ~large) | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/downstream-codegen-schemas/cs2_schema.json` |
| ConVars | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/convars.md` |
| Commands | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/commands.md` |
| cs_gameevents proto | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/proto/cs_gameevents.md` |
| cstrike15_usermessages proto | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/proto/cstrike15_usermessages.md` |
| cstrike15_gcmessages proto | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/proto/cstrike15_gcmessages.md` |
| netmessages proto | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/proto/netmessages.md` |
| demo proto | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/proto/demo.md` |
| cs_usercmd proto | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/proto/cs_usercmd.md` |
| Entity hierarchy diagram | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/diagrams/server_hierarchy.md` |
| This file (AGENTS.md) | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/AGENTS.md` |

---

## Common tasks and where to look

| Task | Where to look |
|------|--------------|
| Parse a CS2 demo file | `demo.proto`, `netmessages.proto`, `CCSGameRules` fields |
| Track player positions / health | `CCSPlayerPawn` fields in `server` schema |
| Track player money / economy | `CCSPlayerController_InGameMoneyServices` in `server` schema |
| Identify round state (freeze, live, over) | `CCSGameRules.m_bFreezePeriod`, `m_gamePhase`, `m_bWarmupPeriod` |
| Decode kill/damage events | `cs_gameevents.proto` → `CMsgSource1LegacyGameEvent` |
| Understand weapon properties | `CCSWeaponBase`, `CCSWeaponBaseGun`, `CCSWeaponBaseVData` in `server` schema |
| Work with bomb events | `CPlantedC4` in `server` schema, `cs_gameevents.proto` |
| Decode player commands | `cs_usercmd.proto` → `CSGOUserCmdPB` |
| Find all convars for a system | ConVars reference, filter by flag or prefix |
| Build a server plugin (Metamod/CS2) | `server` schema for entity offsets, `netmessages.proto` for hooking |
| Work with item/skin data | `cstrike15_gcmessages.proto`, `CCSPlayerController_InventoryServices` |
| Understand rank/matchmaking | `cstrike15_gcmessages.proto` GC message types |
