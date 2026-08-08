---
layout: default
title: CCSGameModeRules
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CCSGameModeRules

# CCSGameModeRules

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** client

**Derived by:** [CCSGameModeRules_ArmsRace](../client/CCSGameModeRules_ArmsRace.md), [CCSGameModeRules_Deathmatch](../client/CCSGameModeRules_Deathmatch.md), [CCSGameModeRules_Noop](../client/CCSGameModeRules_Noop.md)

**Relationships:**

```mermaid
classDiagram
    CCSGameModeRules <|-- CCSGameModeRules_ArmsRace
    CCSGameModeRules <|-- CCSGameModeRules_Deathmatch
    CCSGameModeRules <|-- CCSGameModeRules_Noop
    CCSGameModeRules *-- CNetworkVarChainer
```

## Memory layout

1 fields (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) |  | `MNotSaved` |
