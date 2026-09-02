---
title: CCSGameModeRules_ArmsRace (client)
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / CCSGameModeRules_ArmsRace

# CCSGameModeRules_ArmsRace

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** client

**Twin:** [CCSGameModeRules_ArmsRace (server)](../server/CCSGameModeRules_ArmsRace.md)

**Inherits from:** [CCSGameModeRules](../client/CCSGameModeRules.md)

**Relationships:**

```mermaid
classDiagram
    CCSGameModeRules <|-- CCSGameModeRules_ArmsRace
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CCSGameModeRules](../client/CCSGameModeRules.md) | `MNotSaved` |
| `0x30` | `m_WeaponSequence` | C_NetworkUtlVectorBase< CUtlString > |  |  |
