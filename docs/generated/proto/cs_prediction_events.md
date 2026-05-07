---
layout: default
title: cs_prediction_events.proto
parent: Protobufs
nav_exclude: true
---

# `cs_prediction_events.proto`

**Imports:** `networkbasetypes.proto`, `prediction_events.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class CCSPredictionEvent_DamageTag {
    +float flinch_mod_small
    +float flinch_mod_large
    +float friendly_fire_damage_reduction_ratio
  }

  class ECSPredictionEvents{
    <<enumeration>>
    CSPE_DamageTag
  }

```

## Enums

### `ECSPredictionEvents`

| Name | Value |
|------|-------|
| `CSPE_DamageTag` | 1 |

## Messages

### `CCSPredictionEvent_DamageTag`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `flinch_mod_small` | 1 | float | optional |  |
| `flinch_mod_large` | 2 | float | optional |  |
| `friendly_fire_damage_reduction_ratio` | 3 | float | optional |  |
