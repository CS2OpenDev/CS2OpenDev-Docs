---
layout: default
title: "CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t (server)"
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t

# CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t (client)](../client/CCSPlayerController_InventoryServices.NetworkedLoadoutSlot_t.md)

**Relationships:**

```mermaid
classDiagram
    `CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t` --> CEconItemView
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `pItem` | [CEconItemView](../server/CEconItemView.md)* |  |  |
| `0x8` | `team` | uint16 |  |  |
| `0xa` | `slot` | uint16 |  |  |
