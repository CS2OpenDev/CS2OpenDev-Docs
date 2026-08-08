---
layout: default
title: WeaponPurchaseTracker_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / WeaponPurchaseTracker_t

# WeaponPurchaseTracker_t

**Kind:** class · **Size:** 112 bytes (`0x70`) · **Align:** 255 · **Module:** server

**Relationships:**

```mermaid
classDiagram
    WeaponPurchaseTracker_t *-- WeaponPurchaseCount_t
```

## Memory layout

1 fields (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_weaponPurchases` | CUtlVectorEmbeddedNetworkVar< [WeaponPurchaseCount_t](../server/WeaponPurchaseCount_t.md) > |  |  |
