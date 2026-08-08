---
layout: default
title: CCSPlayerController_InGameMoneyServices
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSPlayerController_InGameMoneyServices

# CCSPlayerController_InGameMoneyServices

**Kind:** class · **Size:** 88 bytes (`0x58`) · **Align:** 255 · **Module:** server

**Inherits from:** [CPlayerControllerComponent](../server/CPlayerControllerComponent.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerControllerComponent <|-- CCSPlayerController_InGameMoneyServices
```

## Memory layout

7 fields (6 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerControllerComponent](../server/CPlayerControllerComponent.md) | `MNotSaved` |
| `0x40` | `m_bReceivesMoneyNextRound` | bool |  |  |
| `0x44` | `m_iMoneyEarnedForNextRound` | int32 |  |  |
| `0x48` | `m_iAccount` | int32 |  |  |
| `0x4c` | `m_iStartAccount` | int32 |  |  |
| `0x50` | `m_iTotalCashSpent` | int32 |  |  |
| `0x54` | `m_iCashSpentThisRound` | int32 |  |  |
