---
layout: default
title: CSPerRoundStats_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CSPerRoundStats_t

# CSPerRoundStats_t

**Kind:** class · **Size:** 104 bytes (`0x68`) · **Align:** 255 · **Module:** client

**Derived by:** [CSMatchStats_t](../client/CSMatchStats_t.md)

**Relationships:**

```mermaid
classDiagram
    CSPerRoundStats_t <|-- CSMatchStats_t
```

## Memory layout

13 fields (13 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x30` | `m_iKills` | int32 |  |  |
| `0x34` | `m_iDeaths` | int32 |  |  |
| `0x38` | `m_iAssists` | int32 |  |  |
| `0x3c` | `m_iDamage` | int32 |  |  |
| `0x40` | `m_iEquipmentValue` | int32 |  |  |
| `0x44` | `m_iMoneySaved` | int32 |  |  |
| `0x48` | `m_iKillReward` | int32 |  |  |
| `0x4c` | `m_iLiveTime` | int32 |  |  |
| `0x50` | `m_iHeadShotKills` | int32 |  |  |
| `0x54` | `m_iObjective` | int32 |  |  |
| `0x58` | `m_iCashEarned` | int32 |  |  |
| `0x5c` | `m_iUtilityDamage` | int32 |  |  |
| `0x60` | `m_iEnemiesFlashed` | int32 |  |  |
