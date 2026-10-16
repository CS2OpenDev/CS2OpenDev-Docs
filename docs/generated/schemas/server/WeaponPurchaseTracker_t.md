---
title: WeaponPurchaseTracker_t (server)
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / WeaponPurchaseTracker_t

# WeaponPurchaseTracker_t

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 112 bytes (`0x70`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [WeaponPurchaseTracker_t (client)](../client/WeaponPurchaseTracker_t.md)

**Relationships:**

```mermaid
classDiagram
    WeaponPurchaseTracker_t *-- WeaponPurchaseCount_t
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_weaponPurchases` | CUtlVectorEmbeddedNetworkVar< [WeaponPurchaseCount_t](../server/WeaponPurchaseCount_t.md) > |  |  |
