---
layout: default
title: "CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t

# CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t

**Kind:** class · **Size:** 200 bytes (`0xc8`) · **Align:** 255 · **Module:** client

**Relationships:**

```mermaid
classDiagram
    "CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t" --> C_EconItemView
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `pItem` | [C_EconItemView](../client/C_EconItemView.md)* |  |  |
| `0x8` | `team` | uint16 |  |  |
| `0xa` | `slot` | uint16 |  |  |
