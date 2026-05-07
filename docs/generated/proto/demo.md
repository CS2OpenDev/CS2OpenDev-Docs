---
layout: default
title: demo.proto
parent: Protobufs
nav_exclude: true
---

# `demo.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class CDemoFileHeader {
    +string demo_file_stamp
    +int32 patch_version
    +string server_name
    +string client_name
    +string map_name
    +string game_directory
    +int32 fullpackets_version
    +bool allow_clientside_entities
    +bool allow_clientside_particles
    +string addons
    +string demo_version_name
    +string demo_version_guid
    +int32 build_num
    +string game
    +int32 server_start_tick
  }

  class CGameInfo {
    +CGameInfo.CDotaGameInfo dota
    +CGameInfo.CCSGameInfo cs
  }

  class CDotaGameInfo {
    +uint64 match_id
    +int32 game_mode
    +int32 game_winner
    +List~CGameInfo.CDotaGameInfo.CPlayerInfo~ player_info
    +uint32 leagueid
    +List~CGameInfo.CDotaGameInfo.CHeroSelectEvent~ picks_bans
    +uint32 radiant_team_id
    +uint32 dire_team_id
    +string radiant_team_tag
    +string dire_team_tag
    +uint32 end_time
  }

  class CPlayerInfo {
    +string hero_name
    +string player_name
    +bool is_fake_client
    +uint64 steamid
    +int32 game_team
  }

  class CHeroSelectEvent {
    +bool is_pick
    +uint32 team
    +int32 hero_id
  }

  class CCSGameInfo {
    +List~int32~ round_start_ticks
  }

  class CDemoFileInfo {
    +float playback_time
    +int32 playback_ticks
    +int32 playback_frames
    +CGameInfo game_info
  }

  class CDemoPacket {
    +bytes data
  }

  class CDemoFullPacket {
    +CDemoStringTables string_table
    +CDemoPacket packet
  }

  class CDemoSaveGame {
    +bytes data
    +fixed64 steam_id
    +fixed64 signature
    +int32 version
  }

  class CDemoSyncTick {
  }

  class CDemoConsoleCmd {
    +string cmdstring
  }

  class CDemoSendTables {
    +bytes data
  }

  class CDemoClassInfo {
    +List~CDemoClassInfo.class_t~ classes
  }

  class class_t {
    +int32 class_id
    +string network_name
    +string table_name
  }

  class CDemoCustomData {
    +int32 callback_index
    +bytes data
  }

  class CDemoCustomDataCallbacks {
    +List~string~ save_id
  }

  class CDemoAnimationHeader {
    +sint32 entity_id
    +int32 tick
    +bytes data
  }

  class CDemoAnimationData {
    +sint32 entity_id
    +int32 start_tick
    +int32 end_tick
    +bytes data
    +int64 data_checksum
  }

  class CDemoStringTables {
    +List~CDemoStringTables.table_t~ tables
  }

  class items_t {
    +string str
    +bytes data
  }

  class table_t {
    +string table_name
    +List~CDemoStringTables.items_t~ items
    +List~CDemoStringTables.items_t~ items_clientside
    +int32 table_flags
  }

  class CDemoStop {
  }

  class CDemoUserCmd {
    +int32 cmd_number
    +bytes data
  }

  class CDemoSpawnGroups {
    +List~bytes~ msgs
  }

  class CDemoSpawnGroupsHLTVBroadcast {
    +bytes data
  }

  class CDemoRecovery {
    +CDemoRecovery.DemoInitialSpawnGroupEntry initial_spawn_group
    +bytes spawn_group_message
  }

  class DemoInitialSpawnGroupEntry {
    +uint32 spawngrouphandle
    +bool was_created
  }

  CGameInfo --> CDotaGameInfo : dota
  CGameInfo --> CCSGameInfo : cs
  CDotaGameInfo --> CPlayerInfo : player_info[]
  CDotaGameInfo --> CHeroSelectEvent : picks_bans[]
  CDemoFileInfo --> CGameInfo : game_info
  CDemoFullPacket --> CDemoStringTables : string_table
  CDemoFullPacket --> CDemoPacket : packet
  CDemoClassInfo --> class_t : classes[]
  CDemoStringTables --> table_t : tables[]
  table_t --> items_t : items[]
  CDemoRecovery --> DemoInitialSpawnGroupEntry : initial_spawn_group

  class EDemoCommands{
    <<enumeration>>
    DEM_Error
    DEM_Stop
    DEM_FileHeader
    DEM_FileInfo
    DEM_SyncTick
    DEM_SendTables
    DEM_ClassInfo
    DEM_StringTables
    DEM_Packet
    DEM_SignonPacket
    DEM_ConsoleCmd
    DEM_CustomData
    DEM_CustomDataCallbacks
    DEM_UserCmd
    DEM_FullPacket
    DEM_SaveGame
    DEM_SpawnGroups
    DEM_AnimationData
    DEM_AnimationHeader
    DEM_Recovery
    DEM_Max
    DEM_IsCompressed
  }

```

## Enums

### `EDemoCommands`

| Name | Value |
|------|-------|
| `DEM_Error` | -1 |
| `DEM_Stop` | 0 |
| `DEM_FileHeader` | 1 |
| `DEM_FileInfo` | 2 |
| `DEM_SyncTick` | 3 |
| `DEM_SendTables` | 4 |
| `DEM_ClassInfo` | 5 |
| `DEM_StringTables` | 6 |
| `DEM_Packet` | 7 |
| `DEM_SignonPacket` | 8 |
| `DEM_ConsoleCmd` | 9 |
| `DEM_CustomData` | 10 |
| `DEM_CustomDataCallbacks` | 11 |
| `DEM_UserCmd` | 12 |
| `DEM_FullPacket` | 13 |
| `DEM_SaveGame` | 14 |
| `DEM_SpawnGroups` | 15 |
| `DEM_AnimationData` | 16 |
| `DEM_AnimationHeader` | 17 |
| `DEM_Recovery` | 18 |
| `DEM_Max` | 19 |
| `DEM_IsCompressed` | 64 |

## Messages

### `CDemoFileHeader`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `demo_file_stamp` | 1 | string | required |  |
| `patch_version` | 2 | int32 | optional |  |
| `server_name` | 3 | string | optional |  |
| `client_name` | 4 | string | optional |  |
| `map_name` | 5 | string | optional |  |
| `game_directory` | 6 | string | optional |  |
| `fullpackets_version` | 7 | int32 | optional |  |
| `allow_clientside_entities` | 8 | bool | optional |  |
| `allow_clientside_particles` | 9 | bool | optional |  |
| `addons` | 10 | string | optional |  |
| `demo_version_name` | 11 | string | optional |  |
| `demo_version_guid` | 12 | string | optional |  |
| `build_num` | 13 | int32 | optional |  |
| `game` | 14 | string | optional |  |
| `server_start_tick` | 15 | int32 | optional |  |

### `CGameInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `dota` | 4 | CGameInfo.CDotaGameInfo | optional |  |
| `cs` | 5 | CGameInfo.CCSGameInfo | optional |  |

### `CDemoFileInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `playback_time` | 1 | float | optional |  |
| `playback_ticks` | 2 | int32 | optional |  |
| `playback_frames` | 3 | int32 | optional |  |
| `game_info` | 4 | [CGameInfo](#cgameinfo) | optional |  |

### `CDemoPacket`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `data` | 3 | bytes | optional |  |

### `CDemoFullPacket`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `string_table` | 1 | [CDemoStringTables](#cdemostringtables) | optional |  |
| `packet` | 2 | [CDemoPacket](#cdemopacket) | optional |  |

### `CDemoSaveGame`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `data` | 1 | bytes | optional |  |
| `steam_id` | 2 | fixed64 | optional |  |
| `signature` | 3 | fixed64 | optional |  |
| `version` | 4 | int32 | optional |  |

### `CDemoSyncTick`

### `CDemoConsoleCmd`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `cmdstring` | 1 | string | optional |  |

### `CDemoSendTables`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `data` | 1 | bytes | optional |  |

### `CDemoClassInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `classes` | 1 | CDemoClassInfo.class_t | repeated |  |

### `CDemoCustomData`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `callback_index` | 1 | int32 | optional |  |
| `data` | 2 | bytes | optional |  |

### `CDemoCustomDataCallbacks`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `save_id` | 1 | string | repeated |  |

### `CDemoAnimationHeader`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `entity_id` | 1 | sint32 | optional |  |
| `tick` | 2 | int32 | optional |  |
| `data` | 3 | bytes | optional |  |

### `CDemoAnimationData`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `entity_id` | 1 | sint32 | optional |  |
| `start_tick` | 2 | int32 | optional |  |
| `end_tick` | 3 | int32 | optional |  |
| `data` | 4 | bytes | optional |  |
| `data_checksum` | 5 | int64 | optional |  |

### `CDemoStringTables`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `tables` | 1 | CDemoStringTables.table_t | repeated |  |

### `CDemoStop`

### `CDemoUserCmd`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `cmd_number` | 1 | int32 | optional |  |
| `data` | 2 | bytes | optional |  |

### `CDemoSpawnGroups`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `msgs` | 3 | bytes | repeated |  |

### `CDemoSpawnGroupsHLTVBroadcast`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `data` | 1 | bytes | optional |  |

### `CDemoRecovery`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `initial_spawn_group` | 1 | CDemoRecovery.DemoInitialSpawnGroupEntry | optional |  |
| `spawn_group_message` | 2 | bytes | optional |  |
