---
title: cs_prediction_events.proto
proto: cs_prediction_events.proto
---

# `cs_prediction_events.proto`

**Imports:** [`networkbasetypes.proto`](networkbasetypes.md), `prediction_events.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class CCSPredictionEvent_DamageTag {
    +float flinch_mod_small
    +float flinch_mod_large
    +float friendly_fire_damage_reduction_ratio
  }

  class CCSPredictionEvent_PlayerTeleport {
    +bool relative
    +CMsgVector origin
    +CMsgQAngle angles
    +CMsgVector velocity
  }

  class ECSPredictionEvents{
    <<enumeration>>
    CSPE_DamageTag
    CSPE_PlayerTeleport
  }

```

## Enums

### `ECSPredictionEvents`

| Name | Value |
|------|-------|
| `CSPE_DamageTag` | 1 |
| `CSPE_PlayerTeleport` | 3 |

## Messages

### `CCSPredictionEvent_DamageTag`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `flinch_mod_small` | 1 | float | optional |  |
| `flinch_mod_large` | 2 | float | optional |  |
| `friendly_fire_damage_reduction_ratio` | 3 | float | optional |  |

### `CCSPredictionEvent_PlayerTeleport`

| Field | Number | Type | Label | Description |
|-------|--------|------|-------|-------------|
| `relative` | 1 | bool | optional |  |
| `origin` | 2 | [CMsgVector](networkbasetypes.md#cmsgvector) | optional |  |
| `angles` | 3 | [CMsgQAngle](networkbasetypes.md#cmsgqangle) | optional |  |
| `velocity` | 4 | [CMsgVector](networkbasetypes.md#cmsgvector) | optional |  |
