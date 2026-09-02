---
layout: default
title: WeaponPurchaseTracker_t (client)
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / WeaponPurchaseTracker_t

# WeaponPurchaseTracker_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 112 bytes (`0x70`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [WeaponPurchaseTracker_t (server)](../server/WeaponPurchaseTracker_t.md)

**Relationships:**

```mermaid
classDiagram
    WeaponPurchaseTracker_t *-- WeaponPurchaseCount_t
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_weaponPurchases` | C_UtlVectorEmbeddedNetworkVar< [WeaponPurchaseCount_t](../client/WeaponPurchaseCount_t.md) > |  |  |
