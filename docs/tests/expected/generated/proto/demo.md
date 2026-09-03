---
title: demo.proto
proto: demo.proto
---

# `demo.proto`

Demo-file container messages.

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

  class CGameInfo_CDotaGameInfo["CGameInfo.CDotaGameInfo"] {
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

  class CGameInfo_CDotaGameInfo_CPlayerInfo["CGameInfo.CDotaGameInfo.CPlayerInfo"] {
    +string hero_name
    +string player_name
    +bool is_fake_client
    +uint64 steamid
    +int32 game_team
  }

  class CGameInfo_CDotaGameInfo_CHeroSelectEvent["CGameInfo.CDotaGameInfo.CHeroSelectEvent"] {
    +bool is_pick
    +uint32 team
    +int32 hero_id
  }

  class CGameInfo_CCSGameInfo["CGameInfo.CCSGameInfo"] {
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

  class CDemoClassInfo_class_t["CDemoClassInfo.class_t"] {
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

  class CDemoStringTables_items_t["CDemoStringTables.items_t"] {
    +string str
    +bytes data
  }

  class CDemoStringTables_table_t["CDemoStringTables.table_t"] {
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

  class CDemoRecovery_DemoInitialSpawnGroupEntry["CDemoRecovery.DemoInitialSpawnGroupEntry"] {
    +uint32 spawngrouphandle
    +bool was_created
  }

  CGameInfo --> CGameInfo_CDotaGameInfo : dota
  CGameInfo --> CGameInfo_CCSGameInfo : cs
  CGameInfo_CDotaGameInfo --> CGameInfo_CDotaGameInfo_CPlayerInfo : player_info[]
  CGameInfo_CDotaGameInfo --> CGameInfo_CDotaGameInfo_CHeroSelectEvent : picks_bans[]
  CDemoFileInfo --> CGameInfo : game_info
  CDemoFullPacket --> CDemoStringTables : string_table
  CDemoFullPacket --> CDemoPacket : packet
  CDemoClassInfo --> CDemoClassInfo_class_t : classes[]
  CDemoStringTables --> CDemoStringTables_table_t : tables[]
  CDemoStringTables_table_t --> CDemoStringTables_items_t : items[]
  CDemoRecovery --> CDemoRecovery_DemoInitialSpawnGroupEntry : initial_spawn_group

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

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
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

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `dota` | 4 | [CGameInfo.CDotaGameInfo](#cgameinfocdotagameinfo) | optional |  |
| `cs` | 5 | [CGameInfo.CCSGameInfo](#cgameinfoccsgameinfo) | optional |  |

#### `CGameInfo.CDotaGameInfo`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `match_id` | 1 | uint64 | optional |  |
| `game_mode` | 2 | int32 | optional |  |
| `game_winner` | 3 | int32 | optional |  |
| `player_info` | 4 | [CGameInfo.CDotaGameInfo.CPlayerInfo](#cgameinfocdotagameinfocplayerinfo) | repeated |  |
| `leagueid` | 5 | uint32 | optional |  |
| `picks_bans` | 6 | [CGameInfo.CDotaGameInfo.CHeroSelectEvent](#cgameinfocdotagameinfocheroselectevent) | repeated |  |
| `radiant_team_id` | 7 | uint32 | optional |  |
| `dire_team_id` | 8 | uint32 | optional |  |
| `radiant_team_tag` | 9 | string | optional |  |
| `dire_team_tag` | 10 | string | optional |  |
| `end_time` | 11 | uint32 | optional |  |

##### `CGameInfo.CDotaGameInfo.CPlayerInfo`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `hero_name` | 1 | string | optional |  |
| `player_name` | 2 | string | optional |  |
| `is_fake_client` | 3 | bool | optional |  |
| `steamid` | 4 | uint64 | optional |  |
| `game_team` | 5 | int32 | optional |  |

##### `CGameInfo.CDotaGameInfo.CHeroSelectEvent`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `is_pick` | 1 | bool | optional |  |
| `team` | 2 | uint32 | optional |  |
| `hero_id` | 3 | int32 | optional |  |

#### `CGameInfo.CCSGameInfo`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `round_start_ticks` | 1 | int32 | repeated |  |

### `CDemoFileInfo`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `playback_time` | 1 | float | optional |  |
| `playback_ticks` | 2 | int32 | optional |  |
| `playback_frames` | 3 | int32 | optional |  |
| `game_info` | 4 | [CGameInfo](#cgameinfo) | optional |  |

### `CDemoPacket`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `data` | 3 | bytes | optional |  |

### `CDemoFullPacket`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `string_table` | 1 | [CDemoStringTables](#cdemostringtables) | optional |  |
| `packet` | 2 | [CDemoPacket](#cdemopacket) | optional |  |

### `CDemoSaveGame`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `data` | 1 | bytes | optional |  |
| `steam_id` | 2 | fixed64 | optional |  |
| `signature` | 3 | fixed64 | optional |  |
| `version` | 4 | int32 | optional |  |

### `CDemoSyncTick`

*(no fields)*

### `CDemoConsoleCmd`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `cmdstring` | 1 | string | optional |  |

### `CDemoSendTables`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `data` | 1 | bytes | optional |  |

### `CDemoClassInfo`

Class id to network-class-name table.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `classes` | 1 | [CDemoClassInfo.class_t](#cdemoclassinfoclass_t) | repeated | One entry per network class. |

#### `CDemoClassInfo.class_t`

One class id to network-class-name row.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `class_id` | 1 | int32 | optional |  |
| `network_name` | 2 | string | optional | The network class name the id maps to. |
| `table_name` | 3 | string | optional |  |

### `CDemoCustomData`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `callback_index` | 1 | int32 | optional |  |
| `data` | 2 | bytes | optional |  |

### `CDemoCustomDataCallbacks`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `save_id` | 1 | string | repeated |  |

### `CDemoAnimationHeader`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `entity_id` | 1 | sint32 | optional |  |
| `tick` | 2 | int32 | optional |  |
| `data` | 3 | bytes | optional |  |

### `CDemoAnimationData`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `entity_id` | 1 | sint32 | optional |  |
| `start_tick` | 2 | int32 | optional |  |
| `end_tick` | 3 | int32 | optional |  |
| `data` | 4 | bytes | optional |  |
| `data_checksum` | 5 | int64 | optional |  |

### `CDemoStringTables`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `tables` | 1 | [CDemoStringTables.table_t](#cdemostringtablestable_t) | repeated |  |

#### `CDemoStringTables.items_t`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `str` | 1 | string | optional |  |
| `data` | 2 | bytes | optional |  |

#### `CDemoStringTables.table_t`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `table_name` | 1 | string | optional |  |
| `items` | 2 | [CDemoStringTables.items_t](#cdemostringtablesitems_t) | repeated |  |
| `items_clientside` | 3 | [CDemoStringTables.items_t](#cdemostringtablesitems_t) | repeated |  |
| `table_flags` | 4 | int32 | optional |  |

### `CDemoStop`

*(no fields)*

### `CDemoUserCmd`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `cmd_number` | 1 | int32 | optional |  |
| `data` | 2 | bytes | optional |  |

### `CDemoSpawnGroups`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `msgs` | 3 | bytes | repeated |  |

### `CDemoSpawnGroupsHLTVBroadcast`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `data` | 1 | bytes | optional |  |

### `CDemoRecovery`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `initial_spawn_group` | 1 | [CDemoRecovery.DemoInitialSpawnGroupEntry](#cdemorecoverydemoinitialspawngroupentry) | optional |  |
| `spawn_group_message` | 2 | bytes | optional |  |

#### `CDemoRecovery.DemoInitialSpawnGroupEntry`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `spawngrouphandle` | 1 | uint32 | optional |  |
| `was_created` | 2 | bool | optional |  |
