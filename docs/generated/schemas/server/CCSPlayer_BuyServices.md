---
layout: default
title: CCSPlayer_BuyServices (server)
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSPlayer_BuyServices

# CCSPlayer_BuyServices

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Component that records the player's sellback-eligible purchases for the current round.

**Kind:** class · **Size:** 344 bytes (`0x158`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [CCSPlayer_BuyServices (client)](../client/CCSPlayer_BuyServices.md)

**Inherits from:** [CPlayerPawnComponent](../server/CPlayerPawnComponent.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CCSPlayer_BuyServices
    CCSPlayer_BuyServices *-- SellbackPurchaseEntry_t
```

## Memory layout

3 fields (1 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) | `MNotSaved` |
| `0x30` | `m_pComponentGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) |  |
| `0xd0` | `m_vecSellbackPurchaseEntries` | CUtlVectorEmbeddedNetworkVar< [SellbackPurchaseEntry_t](../server/SellbackPurchaseEntry_t.md) > |  | Vector of SellbackPurchaseEntry_t structs; each entry represents a weapon or equipment purchase that can still be sold back before freeze time expires. |
