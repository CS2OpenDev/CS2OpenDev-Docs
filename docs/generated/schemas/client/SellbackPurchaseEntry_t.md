---
title: SellbackPurchaseEntry_t (client)
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / SellbackPurchaseEntry_t

# SellbackPurchaseEntry_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [SellbackPurchaseEntry_t (server)](../server/SellbackPurchaseEntry_t.md)

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x30` | `m_unDefIdx` | uint16 |  |  |
| `0x34` | `m_nCost` | int32 |  |  |
| `0x38` | `m_nPrevArmor` | int32 |  |  |
| `0x3c` | `m_bPrevHelmet` | bool |  |  |
| `0x40` | `m_hItem` | CEntityHandle |  |  |
