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
Counter-Strike 2, extracted from two upstream sources and updated
automatically every 4 hours:

- [`SteamDatabase/GameTracking-CS2`](https://github.com/SteamDatabase/GameTracking-CS2)
  — Protobufs, `.gameevents`, ConVars, commands.
- [`ValveResourceFormat/SchemaExplorer`](https://github.com/ValveResourceFormat/SchemaExplorer)
  — DumpSource2's structured `cs2.json.gz` (entity classes/structs/enums with
  fields, **memory offsets**, **type sizes**, parent chains, and metadata).

The documentation covers:

| Section | Contents | Browse URL |
|---------|----------|------------|
| **Schema entities** | All C++ entity classes, structs, and enums from CS2's DumpSource2 dump (~3 970 types across 46 engine modules), each with field offsets and class sizes | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas |
| **Protobufs** | All `.proto` message definitions — game events, network messages, GC messages, demo format (42 files, ~777 messages).  Compiled via `protoc` and walked as `FileDescriptorProto`s, so source-info comments and default values are preserved verbatim. | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/protobufs |
| **ConVars** | Every console variable with default value, flags, and description (~3 800 entries) | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/convars |
| **Commands** | Every console command with flags and description (~1 130 entries) | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/commands |
| **UML diagrams** | Mermaid class-hierarchy diagrams for every schema module | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/diagrams/server_hierarchy |
| **Entity schema** | `downstream-codegen-schemas/cs2_schema.json` — community-enriched mirror of upstream `cs2.json.gz` from DumpSource2.  Mirrors upstream's exact shape (top-level `generator` / `revision` / `version_date` / `version_time` / `classes` / `enums`) so any tooling that targets the DumpSource2 dump works unchanged.  Optional `annotations` blocks layer in community-curated descriptions, notes, and warnings.  See the [format reference](#cs2_schemajson-format) below. | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/downstream-codegen-schemas/cs2_schema.json |
| **Game events schema** | `downstream-codegen-schemas/gameevents_schema.json` — community-enriched mirror of the parsed `.gameevents` KV1 registry.  Top-level `events` list; each event preserves its `name` / `comment` / `source` / `properties` / `fields` from the upstream KV1 source.  Same `annotations` enrichment pattern as `cs2_schema.json`. | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/downstream-codegen-schemas/gameevents_schema.json |
| **ConVars schema** | `downstream-codegen-schemas/convars_schema.json` — structured projection of `DumpSource2/convars.txt`.  Top-level `convars` list, each `{ name, default, flags, description }`. | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/downstream-codegen-schemas/convars_schema.json |
| **Commands schema** | `downstream-codegen-schemas/commands_schema.json` — structured projection of `DumpSource2/commands.txt`.  Top-level `commands` list, each `{ name, flags, description }`. | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/downstream-codegen-schemas/commands_schema.json |
| **Well-known constants** | `downstream-codegen-schemas/well_known_constants.json` — integer / enum values downstream tooling needs but that DumpSource2 doesn't expose as named enum types (team numbers, `m_gamePhase`, `CSWeaponState_t`, …).  Source of truth is `docs/overlays/well_known_constants.yml`. | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/downstream-codegen-schemas/well_known_constants.json |

### `cs2_schema.json` format

The file is a community-enriched mirror of upstream SchemaExplorer's `schemas/cs2.json.gz`.
It is **not** JSON Schema — that approach was tried and abandoned because
standard codegens (quicktype, NJsonSchema, json-schema-to-typescript, …)
couldn't handle the layered `allOf`/`$ref` inheritance and synthetic
defs needed to model native CS2 types.  Mirroring upstream's structured
shape lets each consumer apply its own type-mapping policy.

**Top-level**

```json
{
  "schema_format_version": "1.1",
  "generator": "https://github.com/ValveResourceFormat/DumpSource2",
  "revision": 10627055,
  "version_date": "Apr 30 2026",
  "version_time": "15:09:15",
  "classes": [...],
  "enums":   [...]
}
```

`generator` / `revision` / `version_date` / `version_time` come straight
from upstream's header and identify the CS2 build the schema describes.
`schema_format_version` describes the JSON shape itself — major bumps on
field removal / rename, minor bumps on field addition.  Additive
`annotations` blocks do not require a bump.  All four codegen schemas
(`cs2_schema.json`, `gameevents_schema.json`, `convars_schema.json`,
`commands_schema.json`, `well_known_constants.json`) carry the same
`schema_format_version` value.

**Per-class entry** (one per `(module, name)` — cross-module twins like
`CCSPlayerController` emit one record each):

| Key | What it carries |
|---|---|
| `name` | C++ class / struct name. |
| `module` | The CS2 engine module the entity lives in (`client`, `server`, `animationsystem`, …). |
| `size` | Class instance size in bytes (the C++ `sizeof`). |
| `parents` | Inheritance list as `[{module, name}]`.  Empty when the class has no base. |
| `fields` | List of field records (see below). |
| `metadata` | Class-level metadata as `[{name, value?}]`.  Preserves runtime reflection tags like `MGetKV3ClassDefaults`, `MNetworkVarNames`, etc.  Pass through to codegen consumers as needed. |
| `annotations` *(optional)* | Community enrichment: `{description?, notes?, warning?}`.  Only present when an overlay matches the entity. |

**Per-field entry** (under a class's `fields` list):

| Key | What it carries |
|---|---|
| `name` | Field identifier (e.g. `m_hPawn`). |
| `offset` | Byte offset within the containing class. |
| `type` | Structured type record (see below). |
| `metadata` | Field-level metadata as `[{name, value?}]` — `MNetworkVarTypeOverride`, `MPropertyFriendlyName`, `MPropertyDescription`, etc.  ~4700 fields carry value-bearing metadata. |
| `annotations` *(optional)* | Community enrichment: `{description?, notes?, warning?}`.  Only present when an overlay matches the field. |

**Field `type` shapes** (`category` discriminates the variant):

| `category` | Other keys | Example |
|---|---|---|
| `builtin` | `name` | `{"category": "builtin", "name": "int32"}` |
| `declared_class` | `name`, `module` | `{"category": "declared_class", "module": "server", "name": "CCSPlayerPawn"}` |
| `declared_enum` | `name`, `module` | `{"category": "declared_enum", "module": "client", "name": "AmmoIndex_t"}` |
| `atomic` | `name`, `inner` (sometimes `inner2`, `inner3`) | `{"category": "atomic", "name": "CHandle", "inner": {...}}` |
| `ptr` | `inner` | `{"category": "ptr", "inner": {...}}` |
| `fixed_array` | `inner`, `count` | `{"category": "fixed_array", "count": 16, "inner": {...}}` |
| `bitfield` | `count` (bits) | `{"category": "bitfield", "count": 3}` |

`inner` is itself a type record — recurse to resolve `CHandle<CCSPlayerPawn>*[16]` and friends.  When the innermost type is a `declared_class` or `declared_enum`, its `module` field disambiguates which class lives where.

**Per-enum entry**:

| Key | What it carries |
|---|---|
| `name` | Enum name. |
| `module` | Engine module. |
| `alignment` | Underlying integer type (`uint32_t`, `int8_t`, …). |
| `members` | List of `{name, value, metadata}` member records.  ~1017 members across all enums carry metadata (`MPropertyFriendlyName`, `MPropertyDescription`). |
| `metadata` | Enum-level metadata. |
| `annotations` *(optional)* | Community enrichment, same shape as on classes. |

**Per-enum-member entry**:

| Key | What it carries |
|---|---|
| `name` | Member identifier. |
| `value` | Numeric value. |
| `metadata` | Member-level metadata as `[{name, value?}]`. |
| `annotations` *(optional)* | Community enrichment when the overlay supplies a per-member description. |

A consumer that has never heard of `annotations` ignores the key and gets exactly upstream's shape.  A consumer that reads `annotations` gets the curated descriptions / notes / warnings on top.

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

**Fields that older dumps carried but the current dump does not.**
The mirror passes through exactly what upstream `cs2.json.gz` emits.
Several fields that were present in older SchemaExplorer revisions
(`abstract` on classes, `flags` on enums, `handle_kind` on `CHandle` /
`CStrongHandle` / `CWeakHandle` atomics, `storage_size` on enums) are
not present in the current upstream output and so are absent from this
mirror as well.  File requests upstream at
`ValveResourceFormat/SchemaExplorer` if you need them restored.

#### Deriving handle kind from atomic name

Until upstream restores the `handle_kind` discriminator, downstream
codegen can recover it from the atomic `name` directly — every handle
atomic name in the current schema derives from `CBaseHandle` and the
name carries the distinction.  Observed in the current build (counts
are field occurrences across all classes):

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
`ehandle`.  See the [generated reference page](https://cs2opendev.github.io/CS2OpenDev-Docs/generated/gameevents)
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
Full reference: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/server#cbaseentity

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
Full reference: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/server#ccsplayercontroller

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
Full reference: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/server#ccsplayerpawn

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
Full reference: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/server#ccsgamerules

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
Full reference: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/server#ccsweaponbase

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

Full weapon list: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/server

---

### `CPlantedC4`
*The planted bomb entity.*
Full reference: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/server#cplantedc4

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
Reference: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/proto/cs_gameevents

CS2-specific game event messages (e.g. bomb plant/defuse, kill, round end).
Sent as `CMsgSource1LegacyGameEvent` on the network.

### CS2 user messages (`cstrike15_usermessages.proto`)
Reference: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/proto/cstrike15_usermessages

73 messages sent from server to individual clients: HUD hints, radar updates,
kill cam data, round end summary, item purchases, etc.

Key messages: `CCSUsrMsg_RoundEnd`, `CCSUsrMsg_SendAudio`,
`CCSUsrMsg_RadioText`, `CCSUsrMsg_HudMsg`, `CCSUsrMsg_KillCam`,
`CCSUsrMsg_MatchEndData`

### CS2 GC messages (`cstrike15_gcmessages.proto`)
Reference: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/proto/cstrike15_gcmessages

156 messages between the game client/server and Valve's Game Coordinator:
matchmaking, lobbies, item inventory, competitive ranks, GOTV relay, etc.

Key messages: `CMsgGCCStrike15_v2_MatchmakingClient2GCHello`,
`CMsgGCCStrike15_v2_ClientRequestPlayersProfile`,
`CMsgGCCStrike15_v2_MatchList`

### Core net messages (`netmessages.proto`)
Reference: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/proto/netmessages

63 engine-level network messages: snapshot packets, string tables, data
tables (SendTables), sound events, entity creation/deletion.

Key messages: `CNETMsg_Tick`, `CSVCMsg_PacketEntities`,
`CSVCMsg_CreateStringTable`, `CSVCMsg_GameEvent`, `CSVCMsg_UserMessage`

### Demo file format (`demo.proto`)
Reference: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/proto/demo

Messages defining the `.dem` file format: `CDemoHeader`, `CDemoFileHeader`,
`CDemoPacket`, `CDemoFullPacket`, `CDemoStringTables`, `CDemoClassInfo`.
CS2 demos are written in the Source 2 "PBDEMS2" binary format.

### User commands (`cs_usercmd.proto`)
Reference: https://cs2opendev.github.io/CS2OpenDev-Docs/generated/proto/cs_usercmd

`CCSUsrCmd` — the per-tick command sent from client to server: move direction,
view angles, attack buttons, subtick data.

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

| Module | Entities | Description | URL |
|--------|----------|-------------|-----|
| `server` | ~574 | Server-side entity classes (weapons, players, game rules, …) | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/server |
| `client` | ~714 | Client-side entity mirrors and UI components | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/client |
| `particles` | ~502 | Particle system types | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/particles |
| `animgraphlib` | ~265 | Animation graph nodes and types | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/animgraphlib |
| `animlib` | ~210 | Core animation types | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/animlib |
| `animationsystem` | ~55 | Top-level animation system | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/animationsystem |
| `physicslib` | ~98 | Physics types | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/physicslib |
| `vphysics2` | ~5 | Havok physics integration | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/vphysics2 |
| `modellib` | ~140 | Model/mesh types | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/modellib |
| `soundsystem` | ~23 | Sound system types | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/soundsystem |
| `materialsystem2` | ~19 | Material types | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/materialsystem2 |
| `entity2` | ~17 | Base entity framework types (`CEntityInstance`, `GameTime_t`, …) | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/entity2 |
| `navlib` | ~11 | Navigation mesh types | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/navlib |
| `resourcesystem` | ~48 | Resource/asset system types | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/resourcesystem |
| `scenesystem` | ~12 | Scene graph types | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/scenesystem |
| `pulse_system` | ~30 | Pulse scripting system | https://cs2opendev.github.io/CS2OpenDev-Docs/generated/schemas/pulse_system |

---

## Raw GitHub URLs for deep fetching

If your AI tool supports fetching raw documents, use these URLs to load full
content for a specific section:

| Content | Raw URL |
|---------|---------|
| Server schema (full, ~large) | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/schemas/server.md` |
| Client schema (full, ~large) | `https://raw.githubusercontent.com/CS2OpenDev/CS2OpenDev-Docs/main/docs/generated/schemas/client.md` |
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
| Decode player commands | `cs_usercmd.proto` → `CCSUsrCmd` |
| Find all convars for a system | ConVars reference, filter by flag or prefix |
| Build a server plugin (Metamod/CS2) | `server` schema for entity offsets, `netmessages.proto` for hooking |
| Work with item/skin data | `cstrike15_gcmessages.proto`, `CCSPlayerController_InventoryServices` |
| Understand rank/matchmaking | `cstrike15_gcmessages.proto` GC message types |
