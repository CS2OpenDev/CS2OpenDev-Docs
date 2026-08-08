---
layout: default
title: CTeamplayRules
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CTeamplayRules

# CTeamplayRules

**Kind:** class · **Size:** 208 bytes (`0xd0`) · **Align:** 255 · **Module:** server

**Inherits from:** [CMultiplayRules](../server/CMultiplayRules.md)

**Derived by:** [CCSGameRules](../server/CCSGameRules.md)

**Relationships:**

```mermaid
classDiagram
    CMultiplayRules <|-- CTeamplayRules
    CGameRules <|-- CMultiplayRules
    CTeamplayRules <|-- CCSGameRules
```

## Memory layout

8 fields (0 declared here, 8 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CGameRules](../server/CGameRules.md) | `MNotSaved` |
| `0x30` | `m_szQuestName` | char[128] | [CGameRules](../server/CGameRules.md) |  |
| `0xb0` | `m_nQuestPhase` | int32 | [CGameRules](../server/CGameRules.md) |  |
| `0xb4` | `m_nLastMatchTime` | uint32 | [CGameRules](../server/CGameRules.md) |  |
| `0xb8` | `m_nLastMatchTime_MatchID64` | uint64 | [CGameRules](../server/CGameRules.md) |  |
| `0xc0` | `m_nTotalPausedTicks` | int32 | [CGameRules](../server/CGameRules.md) |  |
| `0xc4` | `m_nPauseStartTick` | int32 | [CGameRules](../server/CGameRules.md) |  |
| `0xc8` | `m_bGamePaused` | bool | [CGameRules](../server/CGameRules.md) |  |
