---
layout: default
title: CDamageRecord (server)
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CDamageRecord

# CDamageRecord

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 120 bytes (`0x78`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [CDamageRecord (client)](../client/CDamageRecord.md)

**Relationships:**

```mermaid
classDiagram
    CDamageRecord --> CCSPlayerPawn
    CDamageRecord --> CCSPlayerController
    CDamageRecord *-- EKillTypes_t
```

## Memory layout

15 fields (15 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x30` | `m_PlayerDamager` | CHandle< [CCSPlayerPawn](../server/CCSPlayerPawn.md) > |  |  |
| `0x34` | `m_PlayerRecipient` | CHandle< [CCSPlayerPawn](../server/CCSPlayerPawn.md) > |  |  |
| `0x38` | `m_hPlayerControllerDamager` | CHandle< [CCSPlayerController](../server/CCSPlayerController.md) > |  |  |
| `0x3c` | `m_hPlayerControllerRecipient` | CHandle< [CCSPlayerController](../server/CCSPlayerController.md) > |  |  |
| `0x40` | `m_szPlayerDamagerName` | CUtlString |  |  |
| `0x48` | `m_szPlayerRecipientName` | CUtlString |  |  |
| `0x50` | `m_DamagerXuid` | uint64 |  |  |
| `0x58` | `m_RecipientXuid` | uint64 |  |  |
| `0x60` | `m_flBulletsDamage` | float32 |  |  |
| `0x64` | `m_flDamage` | float32 |  |  |
| `0x68` | `m_flActualHealthRemoved` | float32 |  |  |
| `0x6c` | `m_iNumHits` | int32 |  |  |
| `0x70` | `m_iLastBulletUpdate` | int32 |  |  |
| `0x74` | `m_bIsOtherEnemy` | bool |  |  |
| `0x75` | `m_killType` | [EKillTypes_t](../server/EKillTypes_t.md) |  |  |
