---
layout: default
title: cs_usercmd.proto
parent: Protobufs
nav_exclude: true
---

# `cs_usercmd.proto`

**Imports:** `networkbasetypes.proto`, `usercmd.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class CSGOInterpolationInfoPB {
    +int32 src_tick
    +int32 dst_tick
    +float frac
  }

  class CSGOInterpolationInfoPB_CL {
    +float frac
  }

  class CSGOInputHistoryEntryPB {
    +CMsgQAngle view_angles
    +int32 render_tick_count
    +float render_tick_fraction
    +int32 player_tick_count
    +float player_tick_fraction
    +CSGOInterpolationInfoPB_CL cl_interp
    +CSGOInterpolationInfoPB sv_interp0
    +CSGOInterpolationInfoPB sv_interp1
    +CSGOInterpolationInfoPB player_interp
    +int32 frame_number
    +int32 target_ent_index
    +CMsgVector shoot_position
    +CMsgVector target_head_pos_check
    +CMsgVector target_abs_pos_check
    +CMsgQAngle target_abs_ang_check
  }

  class CSGOUserCmdPB {
    +CBaseUserCmdPB base
    +List~CSGOInputHistoryEntryPB~ input_history
    +int32 attack1_start_history_index
    +int32 attack2_start_history_index
    +bool left_hand_desired
    +bool is_predicting_body_shot_fx
    +bool is_predicting_head_shot_fx
    +bool is_predicting_kill_ragdolls
  }

  CSGOInputHistoryEntryPB --> CSGOInterpolationInfoPB_CL : cl_interp
  CSGOInputHistoryEntryPB --> CSGOInterpolationInfoPB : sv_interp0
  CSGOUserCmdPB --> CSGOInputHistoryEntryPB : input_history[]

```

## Messages

### `CSGOInterpolationInfoPB`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `src_tick` | 1 | int32 | optional | *(default: `-1`)* |
| `dst_tick` | 2 | int32 | optional | *(default: `-1`)* |
| `frac` | 3 | float | optional | *(default: `0`)* |

### `CSGOInterpolationInfoPB_CL`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `frac` | 3 | float | optional | *(default: `0`)* |

### `CSGOInputHistoryEntryPB`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `view_angles` | 2 | CMsgQAngle | optional |  |
| `render_tick_count` | 4 | int32 | optional |  |
| `render_tick_fraction` | 5 | float | optional |  |
| `player_tick_count` | 6 | int32 | optional |  |
| `player_tick_fraction` | 7 | float | optional |  |
| `cl_interp` | 12 | [CSGOInterpolationInfoPB_CL](#csgointerpolationinfopb_cl) | optional |  |
| `sv_interp0` | 13 | [CSGOInterpolationInfoPB](#csgointerpolationinfopb) | optional |  |
| `sv_interp1` | 14 | [CSGOInterpolationInfoPB](#csgointerpolationinfopb) | optional |  |
| `player_interp` | 15 | [CSGOInterpolationInfoPB](#csgointerpolationinfopb) | optional |  |
| `frame_number` | 64 | int32 | optional |  |
| `target_ent_index` | 65 | int32 | optional | *(default: `-1`)* |
| `shoot_position` | 66 | CMsgVector | optional |  |
| `target_head_pos_check` | 67 | CMsgVector | optional |  |
| `target_abs_pos_check` | 68 | CMsgVector | optional |  |
| `target_abs_ang_check` | 69 | CMsgQAngle | optional |  |

### `CSGOUserCmdPB`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `base` | 1 | CBaseUserCmdPB | optional |  |
| `input_history` | 2 | [CSGOInputHistoryEntryPB](#csgoinputhistoryentrypb) | repeated |  |
| `attack1_start_history_index` | 6 | int32 | optional | *(default: `-1`)* |
| `attack2_start_history_index` | 7 | int32 | optional | *(default: `-1`)* |
| `left_hand_desired` | 9 | bool | optional | *(default: `false`)* |
| `is_predicting_body_shot_fx` | 11 | bool | optional | *(default: `false`)* |
| `is_predicting_head_shot_fx` | 12 | bool | optional | *(default: `false`)* |
| `is_predicting_kill_ragdolls` | 13 | bool | optional | *(default: `false`)* |
