---
layout: default
title: CCSGameModeRules_Deathmatch
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSGameModeRules_Deathmatch

# CCSGameModeRules_Deathmatch

**Kind:** class · **Size:** 136 bytes (`0x88`) · **Align:** 8 · **Module:** server

**Inherits from:** [CCSGameModeRules](../server/CCSGameModeRules.md)

**Relationships:**

```mermaid
classDiagram
    CCSGameModeRules <|-- CCSGameModeRules_Deathmatch
    CCSGameModeRules_Deathmatch *-- GameTime_t
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CCSGameModeRules](../server/CCSGameModeRules.md) | `MNotSaved` |
| `0x30` | `m_flDMBonusStartTime` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x34` | `m_flDMBonusTimeLength` | float32 |  |  |
| `0x38` | `m_sDMBonusWeapon` | CUtlString |  |  |
