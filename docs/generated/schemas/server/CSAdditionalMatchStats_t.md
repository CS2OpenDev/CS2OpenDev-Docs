---
title: CSAdditionalMatchStats_t
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CSAdditionalMatchStats_t

# CSAdditionalMatchStats_t

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 320 bytes (`0x140`) · **Align:** n/a (unspecified) · **Module:** server

**Inherits from:** [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md)

**Relationships:**

```mermaid
classDiagram
    CSAdditionalPerRoundStats_t <|-- CSAdditionalMatchStats_t
```

## Memory layout

24 fields (12 declared here, 12 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_numChickensKilled` | int32 | [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md) |  |
| `0x4` | `m_killsWhileBlind` | int32 | [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md) |  |
| `0x8` | `m_bombCarrierkills` | int32 | [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md) |  |
| `0xc` | `m_flBurnDamageInflicted` | float32 | [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md) |  |
| `0x10` | `m_flBlastDamageInflicted` | float32 | [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md) |  |
| `0x14` | `m_iDinks` | int32 | [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md) |  |
| `0x18` | `m_bFreshStartThisRound` | bool | [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md) |  |
| `0x19` | `m_bBombPlantedAndAlive` | bool | [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md) |  |
| `0x1c` | `m_nDefuseStarts` | int32 | [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md) |  |
| `0x20` | `m_nHostagePickUps` | int32 | [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md) |  |
| `0x24` | `m_numTeammatesFlashed` | int32 | [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md) |  |
| `0x28` | `m_strAnnotationsWorkshopId` | CUtlString | [CSAdditionalPerRoundStats_t](../server/CSAdditionalPerRoundStats_t.md) |  |
| `0x110` | `m_numRoundsSurvivedStreak` | int32 |  |  |
| `0x114` | `m_maxNumRoundsSurvivedStreak` | int32 |  |  |
| `0x118` | `m_numRoundsSurvivedTotal` | int32 |  |  |
| `0x11c` | `m_iRoundsWonWithoutPurchase` | int32 |  |  |
| `0x120` | `m_iRoundsWonWithoutPurchaseTotal` | int32 |  |  |
| `0x124` | `m_numFirstKills` | int32 |  |  |
| `0x128` | `m_numClutchKills` | int32 |  |  |
| `0x12c` | `m_numPistolKills` | int32 |  |  |
| `0x130` | `m_numSniperKills` | int32 |  |  |
| `0x134` | `m_iNumSuicides` | int32 |  |  |
| `0x138` | `m_iNumTeamKills` | int32 |  |  |
| `0x13c` | `m_flTeamDamage` | float32 |  |  |
