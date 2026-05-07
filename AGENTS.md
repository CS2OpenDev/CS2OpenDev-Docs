# CS2 Developer Reference — AI Agent Context

This file is designed to be loaded as context into any AI coding assistant
(GitHub Copilot, Claude Code, Cursor, ChatGPT, Gemini, etc.) by external
developers working on **Counter-Strike 2 tooling, plugins, demo parsers,
game servers, or any other CS2-related project**.

You do **not** need to clone this repository. Paste this file's raw URL into
your AI tool's context, or copy-paste the content directly into a system
prompt / custom instructions field:

```
https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/AGENTS.md
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
| **Schema entities** | All C++ entity classes, structs, and enums from CS2's DumpSource2 dump (~3 970 types across 46 engine modules), each with field offsets and class sizes | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas |
| **Protobufs** | All `.proto` message definitions — game events, network messages, GC messages, demo format (42 files, ~777 messages).  Compiled via `protoc` and walked as `FileDescriptorProto`s, so source-info comments and default values are preserved verbatim. | https://sid2934.github.io/CS2-OpenDevDocs/generated/protobufs |
| **ConVars** | Every console variable with default value, flags, and description (~3 800 entries) | https://sid2934.github.io/CS2-OpenDevDocs/generated/convars |
| **Commands** | Every console command with flags and description (~1 130 entries) | https://sid2934.github.io/CS2-OpenDevDocs/generated/commands |
| **UML diagrams** | Mermaid class-hierarchy diagrams for every schema module | https://sid2934.github.io/CS2-OpenDevDocs/generated/diagrams/server_hierarchy |
| **JSON Schemas** | `cs2_schema.json` and `gameevents_schema.json`, JSON Schema 2020-12.  Carries `x-cs2-source` provenance (DumpSource2 build revision + version date).  See the [`x-cs2-*` extension legend](#x-cs2--json-schema-extensions) below. | https://sid2934.github.io/CS2-OpenDevDocs/generated/cs2_schema.json |

### `x-cs2-*` JSON Schema extensions

`cs2_schema.json` is JSON Schema 2020-12 with `x-cs2-*` extensions that
preserve everything DumpSource2 captures from CS2's runtime reflection.
A consumer that ignores all `x-cs2-*` keys still gets a valid schema; a
consumer that reads them gets full memory layout, source provenance,
and cross-module disambiguation.

**Schema-level**

| Key | What it carries |
|---|---|
| `x-cs2-source` | `{generator, revision, version_date, version_time}` — the cs2.json header.  Use `revision` to know which CS2 build the schema describes. |

**On every `$defs[*]` entry**

| Key | What it carries |
|---|---|
| `x-cs2-kind` | `"class"` / `"struct"` / `"enum"`. |
| `x-cs2-module` | The CS2 engine module the entity lives in.  **String** when single-module, **array of strings** when the same name lives in multiple modules (e.g. `CCSPlayerController` is `["client", "server"]`). |
| `x-cs2-size` | Class instance size in bytes (the C++ `sizeof`). |
| `x-cs2-variants` | Present only when cross-module twins disagree on size or field count.  Each entry: `{module, size, field-count}`.  The bare-name `$def` describes one variant; the others can be retrieved from the per-module Markdown. |
| `x-cs2-base-modules` | Parallel to `allOf`'s `$ref` order, telling you which module each base lives in (matters for the 142 cross-module inheritance edges). |
| `x-cs2-base-external` | Names of bases that aren't defined in the schema (forward declarations etc.). |
| `x-cs2-metadata` | Class-level metadata as `[{name, value?}]`.  E.g. `{"name": "MGetKV3ClassDefaults", "value": "{...}"}` — the structured form so codegen consumers don't have to re-parse a stringified blob. |
| `x-cs2-enum-underlying` | Underlying integer type for enums (`uint32_t`, `int8_t`, …). |
| `x-cs2-enum-values` | `{name: numeric_value}` map for enum members. |
| `x-cs2-enum-value-descriptions` | Human-readable per-member description, derived from overlay → `MPropertyFriendlyName`/`MPropertyDescription` metadata. |
| `x-cs2-enum-value-metadata` | Raw structured metadata per member: `{member_name: [{name, value?}]}` — preserves all 1017 enum-member metadata entries DumpSource2 captures. |

**On every property (field)**

| Key | What it carries |
|---|---|
| `x-cs2-type` | Original C++ type string (e.g. `CHandle<CCSPlayerPawn>`, `Vector*`, `bitfield:3`). |
| `x-cs2-offset` | Byte offset of the field within its containing class. |
| `x-cs2-type-module` | Module of the *innermost* declared class/enum referenced by this field's type — recurses through `*`, `[]`, `CHandle<>`, `CUtlVector<>` etc.  Disambiguates which $def to follow when the target name lives in multiple modules. |
| `x-cs2-metadata` | Field-level metadata as `[{name, value?}]` (e.g. `{"name": "MNetworkVarTypeOverride", "value": "..."}`).  ~4700 fields carry value-bearing metadata. |
| `x-cs2-handle` / `x-cs2-handle-target` | Set on `CHandle<T>` style fields — flags the target type and that the value is a typed handle, not the target itself. |
| `x-cs2-pointer` | Set when the original C++ type was a raw pointer.  The schema marks the value nullable. |
| `x-cs2-bitfield-bits` | Bit width for `bitfield:N` fields. |
| `x-cs2-unresolved` | Marker that a referenced type wasn't found in the schema (rare; usually a forward-decl or platform-only type). |

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
Full reference: https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/server#cbaseentity

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
Full reference: https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/server#ccsplayercontroller

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
Full reference: https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/server#ccsplayerpawn

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
Full reference: https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/server#ccsgamerules

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
Full reference: https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/server#ccsweaponbase

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

Full weapon list: https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/server

---

### `CPlantedC4`
*The planted bomb entity.*
Full reference: https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/server#cplantedc4

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
Reference: https://sid2934.github.io/CS2-OpenDevDocs/generated/proto/cs_gameevents

CS2-specific game event messages (e.g. bomb plant/defuse, kill, round end).
Sent as `CMsgSource1LegacyGameEvent` on the network.

### CS2 user messages (`cstrike15_usermessages.proto`)
Reference: https://sid2934.github.io/CS2-OpenDevDocs/generated/proto/cstrike15_usermessages

73 messages sent from server to individual clients: HUD hints, radar updates,
kill cam data, round end summary, item purchases, etc.

Key messages: `CCSUsrMsg_RoundEnd`, `CCSUsrMsg_SendAudio`,
`CCSUsrMsg_RadioText`, `CCSUsrMsg_HudMsg`, `CCSUsrMsg_KillCam`,
`CCSUsrMsg_MatchEndData`

### CS2 GC messages (`cstrike15_gcmessages.proto`)
Reference: https://sid2934.github.io/CS2-OpenDevDocs/generated/proto/cstrike15_gcmessages

156 messages between the game client/server and Valve's Game Coordinator:
matchmaking, lobbies, item inventory, competitive ranks, GOTV relay, etc.

Key messages: `CMsgGCCStrike15_v2_MatchmakingClient2GCHello`,
`CMsgGCCStrike15_v2_ClientRequestPlayersProfile`,
`CMsgGCCStrike15_v2_MatchList`

### Core net messages (`netmessages.proto`)
Reference: https://sid2934.github.io/CS2-OpenDevDocs/generated/proto/netmessages

63 engine-level network messages: snapshot packets, string tables, data
tables (SendTables), sound events, entity creation/deletion.

Key messages: `CNETMsg_Tick`, `CSVCMsg_PacketEntities`,
`CSVCMsg_CreateStringTable`, `CSVCMsg_GameEvent`, `CSVCMsg_UserMessage`

### Demo file format (`demo.proto`)
Reference: https://sid2934.github.io/CS2-OpenDevDocs/generated/proto/demo

Messages defining the `.dem` file format: `CDemoHeader`, `CDemoFileHeader`,
`CDemoPacket`, `CDemoFullPacket`, `CDemoStringTables`, `CDemoClassInfo`.
CS2 demos are written in the Source 2 "PBDEMS2" binary format.

### User commands (`cs_usercmd.proto`)
Reference: https://sid2934.github.io/CS2-OpenDevDocs/generated/proto/cs_usercmd

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
| `server` | ~574 | Server-side entity classes (weapons, players, game rules, …) | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/server |
| `client` | ~714 | Client-side entity mirrors and UI components | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/client |
| `particles` | ~502 | Particle system types | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/particles |
| `animgraphlib` | ~265 | Animation graph nodes and types | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/animgraphlib |
| `animlib` | ~210 | Core animation types | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/animlib |
| `animationsystem` | ~55 | Top-level animation system | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/animationsystem |
| `physicslib` | ~98 | Physics types | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/physicslib |
| `vphysics2` | ~5 | Havok physics integration | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/vphysics2 |
| `modellib` | ~140 | Model/mesh types | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/modellib |
| `soundsystem` | ~23 | Sound system types | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/soundsystem |
| `materialsystem2` | ~19 | Material types | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/materialsystem2 |
| `entity2` | ~17 | Base entity framework types (`CEntityInstance`, `GameTime_t`, …) | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/entity2 |
| `navlib` | ~11 | Navigation mesh types | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/navlib |
| `resourcesystem` | ~48 | Resource/asset system types | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/resourcesystem |
| `scenesystem` | ~12 | Scene graph types | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/scenesystem |
| `pulse_system` | ~30 | Pulse scripting system | https://sid2934.github.io/CS2-OpenDevDocs/generated/schemas/pulse_system |

---

## Raw GitHub URLs for deep fetching

If your AI tool supports fetching raw documents, use these URLs to load full
content for a specific section:

| Content | Raw URL |
|---------|---------|
| Server schema (full, ~large) | `https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/docs/generated/schemas/server.md` |
| Client schema (full, ~large) | `https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/docs/generated/schemas/client.md` |
| ConVars | `https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/docs/generated/convars.md` |
| Commands | `https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/docs/generated/commands.md` |
| cs_gameevents proto | `https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/docs/generated/proto/cs_gameevents.md` |
| cstrike15_usermessages proto | `https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/docs/generated/proto/cstrike15_usermessages.md` |
| cstrike15_gcmessages proto | `https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/docs/generated/proto/cstrike15_gcmessages.md` |
| netmessages proto | `https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/docs/generated/proto/netmessages.md` |
| demo proto | `https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/docs/generated/proto/demo.md` |
| cs_usercmd proto | `https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/docs/generated/proto/cs_usercmd.md` |
| Entity hierarchy diagram | `https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/docs/generated/diagrams/server_hierarchy.md` |
| This file (AGENTS.md) | `https://raw.githubusercontent.com/sid2934/CS2-OpenDevDocs/main/AGENTS.md` |

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
