---
layout: default
title: CCSPlayerController_DamageServices
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CCSPlayerController_DamageServices

# CCSPlayerController_DamageServices

Damage-log component of CCSPlayerController, backing the end-of-round 'damage given / taken' report.


**Kind:** class · **Size:** 176 bytes (`0xb0`) · **Align:** 255 · **Module:** client

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
| `0x48` | `m_DamageList` | C_UtlVectorEmbeddedNetworkVar< [CDamageRecord](../client/CDamageRecord.md) > |  | Per-opponent damage records shown on the round-end damage report. |
