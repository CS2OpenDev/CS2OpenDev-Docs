---
layout: default
title: CSMatchStats_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CSMatchStats_t

# CSMatchStats_t

**Kind:** class · **Size:** 192 bytes (`0xc0`) · **Align:** 255 · **Module:** server

**Inherits from:** [CSPerRoundStats_t](../server/CSPerRoundStats_t.md)

**Relationships:**

```mermaid
classDiagram
    CSPerRoundStats_t <|-- CSMatchStats_t
```

## Memory layout

34 fields (21 declared here, 13 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x30` | `m_iKills` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x34` | `m_iDeaths` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x38` | `m_iAssists` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x3c` | `m_iDamage` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x40` | `m_iEquipmentValue` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x44` | `m_iMoneySaved` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x48` | `m_iKillReward` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x4c` | `m_iLiveTime` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x50` | `m_iHeadShotKills` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x54` | `m_iObjective` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x58` | `m_iCashEarned` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x5c` | `m_iUtilityDamage` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x60` | `m_iEnemiesFlashed` | int32 | [CSPerRoundStats_t](../server/CSPerRoundStats_t.md) |  |
| `0x68` | `m_iEnemy5Ks` | int32 |  |  |
| `0x6c` | `m_iEnemy4Ks` | int32 |  |  |
| `0x70` | `m_iEnemy3Ks` | int32 |  |  |
| `0x74` | `m_iEnemyKnifeKills` | int32 |  |  |
| `0x78` | `m_iEnemyTaserKills` | int32 |  |  |
| `0x7c` | `m_iEnemy2Ks` | int32 |  |  |
| `0x80` | `m_iUtility_Count` | int32 |  |  |
| `0x84` | `m_iUtility_Successes` | int32 |  |  |
| `0x88` | `m_iUtility_Enemies` | int32 |  |  |
| `0x8c` | `m_iFlash_Count` | int32 |  |  |
| `0x90` | `m_iFlash_Successes` | int32 |  |  |
| `0x94` | `m_flHealthPointsRemovedTotal` | float32 |  |  |
| `0x98` | `m_flHealthPointsDealtTotal` | float32 |  |  |
| `0x9c` | `m_nShotsFiredTotal` | int32 |  |  |
| `0xa0` | `m_nShotsOnTargetTotal` | int32 |  |  |
| `0xa4` | `m_i1v1Count` | int32 |  |  |
| `0xa8` | `m_i1v1Wins` | int32 |  |  |
| `0xac` | `m_i1v2Count` | int32 |  |  |
| `0xb0` | `m_i1v2Wins` | int32 |  |  |
| `0xb4` | `m_iEntryCount` | int32 |  |  |
| `0xb8` | `m_iEntryWins` | int32 |  |  |
