---
layout: default
title: CCSPlayerController_ActionTrackingServices
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSPlayerController_ActionTrackingServices

# CCSPlayerController_ActionTrackingServices

**Kind:** class · **Size:** 1072 bytes (`0x430`) · **Align:** 255 · **Module:** server

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
| `0x40` | `m_perRoundStats` | CUtlVectorEmbeddedNetworkVar< [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) > |  |  |
| `0xc8` | `m_matchStats` | [CSMatchStats_t](../server/CSMatchStats_t.md) |  |  |
| `0x188` | `m_iNumRoundKills` | int32 |  |  |
| `0x18c` | `m_iNumRoundKillsHeadshots` | int32 |  |  |
| `0x190` | `m_flTotalRoundDamageDealt` | float32 |  |  |
