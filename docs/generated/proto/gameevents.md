---
title: gameevents.proto
proto: gameevents.proto
---

# `gameevents.proto`

**Imports:** [`networkbasetypes.proto`](networkbasetypes.md)

Source 2 base game-event protobuf messages.  Provides the Source 1-legacy game-event bridge (CMsgSource1LegacyGameEvent), sound-system events (SoS), and surface-decal events.  Identified by the EBaseGameEvents enum (200–212).

## Diagram

```mermaid
classDiagram
direction LR

  class CMsgVDebugGameSessionIDEvent {
    +int32 clientid
    +string gamesessionid
  }

  class CMsgPlaceDecalEvent {
    +CMsgVector position
    +CMsgVector normal
    +CMsgVector saxis
    +int32 boneindex
    +int32 triangleindex
    +uint32 flags
    +fixed32 color
    +int32 random_seed
    +uint32 decal_group_name
    +float size_override
    +uint32 entityhandle
    +uint64 material_id
    +uint32 sequence_name
    +CMsgVector position_objectspace
    +CMsgVector normal_objectspace
  }

  class CMsgClearWorldDecalsEvent {
    +uint32 flagstoclear
  }

  class CMsgClearEntityDecalsEvent {
    +uint32 flagstoclear
  }

  class CMsgClearDecalsForEntityEvent {
    +uint32 flagstoclear
    +uint32 entityhandle
  }

  class CMsgSource1LegacyGameEventList {
    +List~CMsgSource1LegacyGameEventList.descriptor_t~ descriptors
  }

  class CMsgSource1LegacyGameEventList_key_t["CMsgSource1LegacyGameEventList.key_t"] {
    +int32 type
    +string name
  }

  class CMsgSource1LegacyGameEventList_descriptor_t["CMsgSource1LegacyGameEventList.descriptor_t"] {
    +int32 eventid
    +string name
    +List~CMsgSource1LegacyGameEventList.key_t~ keys
  }

  class CMsgSource1LegacyListenEvents {
    +int32 playerslot
    +List~uint32~ eventarraybits
  }

  class CMsgSource1LegacyGameEvent {
    +string event_name
    +int32 eventid
    +List~CMsgSource1LegacyGameEvent.key_t~ keys
    +int32 server_tick
    +int32 passthrough
  }

  class CMsgSource1LegacyGameEvent_key_t["CMsgSource1LegacyGameEvent.key_t"] {
    +int32 type
    +string val_string
    +float val_float
    +int32 val_long
    +int32 val_short
    +int32 val_byte
    +bool val_bool
    +uint64 val_uint64
  }

  class CMsgSosStartSoundEvent {
    +int32 soundevent_guid
    +fixed32 soundevent_hash
    +int32 source_entity_index
    +int32 seed
    +bytes packed_params
    +float start_time
  }

  class CMsgSosStopSoundEvent {
    +int32 soundevent_guid
  }

  class CMsgSosStopSoundEventHash {
    +fixed32 soundevent_hash
    +int32 source_entity_index
  }

  class CMsgSosSetSoundEventParams {
    +int32 soundevent_guid
    +bytes packed_params
  }

  class CMsgSosSetLibraryStackFields {
    +fixed32 stack_hash
    +bytes packed_fields
  }

  class CMsgClothStiffenAnimEvent {
    +int32 source_entity_index
    +int32 vertex_set_hash
    +float intensity
    +float length
    +float speed_in
    +float speed_out
  }

  class CMsgClothEffectAnimEvent {
    +int32 source_entity_index
    +int32 effect_name_hash
    +int32 operation
    +int32 flags
    +string tags
    +CMsgVector pte
  }

  CMsgSource1LegacyGameEventList --> CMsgSource1LegacyGameEventList_descriptor_t : descriptors[]
  CMsgSource1LegacyGameEventList_descriptor_t --> CMsgSource1LegacyGameEventList_key_t : keys[]
  CMsgSource1LegacyGameEvent --> CMsgSource1LegacyGameEvent_key_t : keys[]

  class EBaseGameEvents{
    <<enumeration>>
    GE_VDebugGameSessionIDEvent
    GE_PlaceDecalEvent
    GE_ClearWorldDecalsEvent
    GE_ClearEntityDecalsEvent
    GE_ClearDecalsForEntityEvent
    GE_Source1LegacyGameEventList
    GE_Source1LegacyListenEvents
    GE_Source1LegacyGameEvent
    GE_SosStartSoundEvent
    GE_SosStopSoundEvent
    GE_SosSetSoundEventParams
    GE_SosSetLibraryStackFields
    GE_SosStopSoundEventHash
    GE_ClothStiffenAnimEvent
    GE_ClothEffectAnimEvent
  }

```

## Enums

### `EBaseGameEvents`

| Name | Value |
|------|-------|
| `GE_VDebugGameSessionIDEvent` | 200 |
| `GE_PlaceDecalEvent` | 201 |
| `GE_ClearWorldDecalsEvent` | 202 |
| `GE_ClearEntityDecalsEvent` | 203 |
| `GE_ClearDecalsForEntityEvent` | 204 |
| `GE_Source1LegacyGameEventList` | 205 |
| `GE_Source1LegacyListenEvents` | 206 |
| `GE_Source1LegacyGameEvent` | 207 |
| `GE_SosStartSoundEvent` | 208 |
| `GE_SosStopSoundEvent` | 209 |
| `GE_SosSetSoundEventParams` | 210 |
| `GE_SosSetLibraryStackFields` | 211 |
| `GE_SosStopSoundEventHash` | 212 |
| `GE_ClothStiffenAnimEvent` | 213 |
| `GE_ClothEffectAnimEvent` | 214 |

## Messages

### `CMsgVDebugGameSessionIDEvent`

Debug event that reports the current game-session ID string to a specific client.  Used during development to trace session continuity.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `clientid` | 1 | int32 | optional | Slot index of the client receiving the session-ID debug information. |
| `gamesessionid` | 2 | string | optional | Unique string identifier for the current game session. |

### `CMsgPlaceDecalEvent`

Instructs clients to paint a decal (bullet hole, blood splatter, spray) onto a surface or entity in the world.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `position` | 1 | [CMsgVector](networkbasetypes.md#cmsgvector) | optional | World-space hit position where the decal should be placed. |
| `normal` | 2 | [CMsgVector](networkbasetypes.md#cmsgvector) | optional | Surface normal at the hit position; orients the decal correctly. |
| `saxis` | 3 | [CMsgVector](networkbasetypes.md#cmsgvector) | optional | Secondary axis vector for texture alignment. |
| `boneindex` | 4 | int32 | optional | Bone index when the decal is attached to an animated model (-1 for world surfaces). |
| `flags` | 5 | uint32 | optional | Decal flags bitmask (temporary, permanent, etc.). |
| `color` | 6 | fixed32 | optional | RGBA colour tint applied to the decal texture. |
| `random_seed` | 7 | int32 | optional | Random seed used to select from a decal group variant. |
| `decal_group_name` | 8 | uint32 | optional | Hash of the decal group name (e.g. 'BulletImpactConcrete'). |
| `size_override` | 9 | float | optional | Override size in world units (0 = use default decal size). |
| `entityhandle` | 10 | uint32 | optional | Entity handle to attach the decal to (0xFFFFFF = world). *(default: `16777215`)* |
| `material_id` | 11 | uint64 | optional | Material ID of the surface at the hit point. |
| `sequence_name` | 12 | uint32 | optional | Hash of the decal sequence name for animated decals. |
| `triangleindex` | 13 | int32 | optional | Mesh triangle index for precise placement on complex geometry. |
| `position_objectspace` | 14 | [CMsgVector](networkbasetypes.md#cmsgvector) | optional |  |
| `normal_objectspace` | 15 | [CMsgVector](networkbasetypes.md#cmsgvector) | optional |  |

### `CMsgClearWorldDecalsEvent`

Removes all world-surface decals matching the given flags (e.g. clears bullet holes at round start).

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `flagstoclear` | 1 | uint32 | optional | Bitmask of decal flags; decals with any matching flag will be removed. |

### `CMsgClearEntityDecalsEvent`

Removes all decals painted on entity surfaces that match the given flags.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `flagstoclear` | 1 | uint32 | optional | Bitmask of decal flags to clear from all entity surfaces. |

### `CMsgClearDecalsForEntityEvent`

Removes all decals on a specific entity that match the given flags.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `flagstoclear` | 1 | uint32 | optional | Bitmask of decal flags to clear. |
| `entityhandle` | 2 | uint32 | optional | Handle of the specific entity whose decals should be cleared. *(default: `16777215`)* |

### `CMsgSource1LegacyGameEventList`

Sent once at the start of a connection to register all Source 1 game-event schemas with the client.  The client uses this list to decode subsequent CMsgSource1LegacyGameEvent messages by ID.

> 📝 This is the Source 2 equivalent of the Source 1 'svc_GameEventList' message. All classic CS:GO game events (player_death, bomb_planted, etc.) are transmitted through this bridge.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `descriptors` | 1 | [CMsgSource1LegacyGameEventList.descriptor_t](#cmsgsource1legacygameeventlistdescriptor_t) | repeated |  |

#### `CMsgSource1LegacyGameEventList.key_t`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `type` | 1 | int32 | optional |  |
| `name` | 2 | string | optional |  |

#### `CMsgSource1LegacyGameEventList.descriptor_t`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `eventid` | 1 | int32 | optional |  |
| `name` | 2 | string | optional |  |
| `keys` | 3 | [CMsgSource1LegacyGameEventList.key_t](#cmsgsource1legacygameeventlistkey_t) | repeated |  |

### `CMsgSource1LegacyListenEvents`

Registers which Source 1 game-events a specific client wishes to receive. Used by plugins and spectators to opt in to event streams.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `playerslot` | 1 | int32 | optional | Player slot that is registering these event listeners. |
| `eventarraybits` | 2 | uint32 | repeated | Packed bitmask array; bit N set means listen for game-event with ID N. |

### `CMsgSource1LegacyGameEvent`

Carries a single Source 1 game-event (player_death, weapon_fire, bomb_planted, etc.) over the Source 2 network layer.  The event-type name and all key–value pairs are encoded inside the keys list.

> 📝 CS2 game events (player_death, round_start, bomb_exploded, etc.) are all transmitted as CMsgSource1LegacyGameEvent messages.  Use the event_name field to identify them and CMsgSource1LegacyGameEventList to decode keys.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `event_name` | 1 | string | optional | String name of the game event (e.g. 'player_death', 'bomb_planted'). |
| `eventid` | 2 | int32 | optional | Numeric event ID assigned during registration via CMsgSource1LegacyGameEventList. |
| `keys` | 3 | [CMsgSource1LegacyGameEvent.key_t](#cmsgsource1legacygameeventkey_t) | repeated | Typed key–value pairs carrying event-specific data (integers, floats, strings, booleans). |
| `server_tick` | 4 | int32 | optional | Server tick on which the event was fired. |
| `passthrough` | 5 | int32 | optional | Passthrough flag used internally by the event system. |

#### `CMsgSource1LegacyGameEvent.key_t`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `type` | 1 | int32 | optional |  |
| `val_string` | 2 | string | optional |  |
| `val_float` | 3 | float | optional |  |
| `val_long` | 4 | int32 | optional |  |
| `val_short` | 5 | int32 | optional |  |
| `val_byte` | 6 | int32 | optional |  |
| `val_bool` | 7 | bool | optional |  |
| `val_uint64` | 8 | uint64 | optional |  |

### `CMsgSosStartSoundEvent`

Starts a named sound event through the SoS (Sound Operating System) layer, associated with an optional source entity.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `soundevent_guid` | 1 | int32 | optional | Unique integer handle for this sound instance (used to stop or modify it later). |
| `soundevent_hash` | 2 | fixed32 | optional | CRC32 hash of the sound event name string. |
| `source_entity_index` | 3 | int32 | optional | Entity index of the sound source (-1 = world/positional). *(default: `-1`)* |
| `seed` | 4 | int32 | optional | Random seed for sound variation selection. |
| `packed_params` | 5 | bytes | optional | Packed binary parameters for the sound event (volume, pitch, position, etc.). |
| `start_time` | 6 | float | optional | Game time at which the sound should start playing (allows latency compensation). |

### `CMsgSosStopSoundEvent`

Stops a specific sound instance identified by its GUID.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `soundevent_guid` | 1 | int32 | optional | GUID of the sound instance to stop (matches soundevent_guid from CMsgSosStartSoundEvent). |

### `CMsgSosStopSoundEventHash`

Stops all sound instances matching the given sound-event hash on the specified source entity.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `soundevent_hash` | 1 | fixed32 | optional | CRC32 hash of the sound event name to stop. |
| `source_entity_index` | 2 | int32 | optional | Entity index to restrict the stop to (-1 = stop all matching sounds). *(default: `-1`)* |

### `CMsgSosSetSoundEventParams`

Updates runtime parameters of an active sound event without restarting it (e.g. volume fade, pitch shift on a looping ambient sound).

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `soundevent_guid` | 1 | int32 | optional | GUID of the active sound instance to modify. |
| `packed_params` | 5 | bytes | optional | New packed parameter values to apply to the running sound. |

### `CMsgSosSetLibraryStackFields`

Modifies fields in a named sound library stack (a group of sound layers), allowing global sound-mix changes from the server.

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `stack_hash` | 1 | fixed32 | optional | CRC32 hash of the sound library stack name to modify. |
| `packed_fields` | 5 | bytes | optional | Packed binary field values to apply to the stack. |

### `CMsgClothStiffenAnimEvent`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `source_entity_index` | 1 | int32 | optional | *(default: `-1`)* |
| `vertex_set_hash` | 2 | int32 | optional |  |
| `intensity` | 3 | float | optional |  |
| `length` | 4 | float | optional |  |
| `speed_in` | 5 | float | optional |  |
| `speed_out` | 6 | float | optional |  |

### `CMsgClothEffectAnimEvent`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `source_entity_index` | 1 | int32 | optional | *(default: `-1`)* |
| `effect_name_hash` | 2 | int32 | optional |  |
| `operation` | 3 | int32 | optional |  |
| `flags` | 4 | int32 | optional |  |
| `tags` | 5 | string | optional |  |
| `pte` | 6 | [CMsgVector](networkbasetypes.md#cmsgvector) | optional |  |
