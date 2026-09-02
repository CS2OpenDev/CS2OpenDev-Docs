---
layout: default
title: CCSPlayerController_ActionTrackingServices (server)
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSPlayerController_ActionTrackingServices

# CCSPlayerController_ActionTrackingServices

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Scoreboard / stat-tracking component of CCSPlayerController: per-round and per-match kill and damage statistics.

**Kind:** class · **Size:** 1072 bytes (`0x430`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [CCSPlayerController_ActionTrackingServices (client)](../client/CCSPlayerController_ActionTrackingServices.md)

**Inherits from:** [CPlayerControllerComponent](../server/CPlayerControllerComponent.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerControllerComponent <|-- CCSPlayerController_ActionTrackingServices
    CCSPlayerController_ActionTrackingServices *-- CSPerRoundStats_t
    CCSPlayerController_ActionTrackingServices *-- CSMatchStats_t
```

## Memory layout

6 fields (5 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerControllerComponent](../server/CPlayerControllerComponent.md) | `MNotSaved` |
| `0x40` | `m_perRoundStats` | CUtlVectorEmbeddedNetworkVar< [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) > |  | List of per-round statistics accumulated over the match. |
| `0xc8` | `m_matchStats` | [CSMatchStats_t](../server/CSMatchStats_t.md) |  | Aggregated per-match statistics for this player. |
| `0x188` | `m_iNumRoundKills` | int32 |  | Kills this player has scored in the current round. |
| `0x18c` | `m_iNumRoundKillsHeadshots` | int32 |  | Headshot kills this player has scored in the current round. |
| `0x190` | `m_flTotalRoundDamageDealt` | float32 |  | Total damage this player has dealt in the current round. |
