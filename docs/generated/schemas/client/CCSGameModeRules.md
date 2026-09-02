---
layout: default
title: CCSGameModeRules (client)
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CCSGameModeRules

# CCSGameModeRules

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** client

**Twin:** [CCSGameModeRules (server)](../server/CCSGameModeRules.md)

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

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) |  | `MNotSaved` |
