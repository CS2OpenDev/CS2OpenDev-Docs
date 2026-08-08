---
layout: default
title: CCSGameModeRules_ArmsRace
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSGameModeRules_ArmsRace

# CCSGameModeRules_ArmsRace

**Kind:** class · **Size:** 136 bytes (`0x88`) · **Align:** 8 · **Module:** server

**Inherits from:** [CCSGameModeRules](../server/CCSGameModeRules.md)

**Relationships:**

```mermaid
classDiagram
    CCSGameModeRules <|-- CCSGameModeRules_ArmsRace
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CCSGameModeRules](../server/CCSGameModeRules.md) | `MNotSaved` |
| `0x30` | `m_WeaponSequence` | CNetworkUtlVectorBase< CUtlString > |  |  |
