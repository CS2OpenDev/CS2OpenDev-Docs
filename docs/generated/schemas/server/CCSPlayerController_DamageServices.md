---
title: CCSPlayerController_DamageServices (server)
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSPlayerController_DamageServices

# CCSPlayerController_DamageServices

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Damage-log component of CCSPlayerController, backing the end-of-round 'damage given / taken' report.

**Kind:** class · **Size:** 208 bytes (`0xd0`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [CCSPlayerController_DamageServices (client)](../client/CCSPlayerController_DamageServices.md)

**Inherits from:** [CPlayerControllerComponent](../server/CPlayerControllerComponent.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerControllerComponent <|-- CCSPlayerController_DamageServices
    CCSPlayerController_DamageServices *-- CDamageRecord
```

## Memory layout

3 fields (2 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerControllerComponent](../server/CPlayerControllerComponent.md) | `MNotSaved` |
| `0x40` | `m_nSendUpdate` | int32 |  |  |
| `0x48` | `m_DamageList` | CUtlVectorEmbeddedNetworkVar< [CDamageRecord](../server/CDamageRecord.md) > |  | Per-opponent damage records shown on the round-end damage report. |
