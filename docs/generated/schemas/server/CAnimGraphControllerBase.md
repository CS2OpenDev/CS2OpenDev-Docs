---
title: CAnimGraphControllerBase
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CAnimGraphControllerBase

# CAnimGraphControllerBase

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 136 bytes (`0x88`) · **Align:** n/a (unspecified) · **Module:** server

**Derived by:** [CBaseAnimGraphDestructibleParts_GraphController](../server/CBaseAnimGraphDestructibleParts_GraphController.md), [CCS2ChickenGraphController](../server/CCS2ChickenGraphController.md), [CCS2UIPawnGraphController](../client/CCS2UIPawnGraphController.md), [CCS2WeaponGraphController](../server/CCS2WeaponGraphController.md), [CCS2WeaponGraphController](../server/CCS2WeaponGraphController.md), [CChoreo_GraphController](../server/CChoreo_GraphController.md), [CEmptyGraphController](../server/CEmptyGraphController.md)

**Relationships:**

```mermaid
classDiagram
    CAnimGraphControllerBase <|-- CBaseAnimGraphDestructibleParts_GraphController
    CAnimGraphControllerBase <|-- CCS2ChickenGraphController
    CAnimGraphControllerBase <|-- CCS2UIPawnGraphController
    CAnimGraphControllerBase <|-- CChoreo_GraphController
    CAnimGraphControllerBase <|-- CEmptyGraphController
    CAnimGraphControllerBase <|-- CCS2WeaponGraphController
    CAnimGraphControllerBase *-- ExternalAnimGraphHandle_t
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x10` | `m_hExternalGraph` | [ExternalAnimGraphHandle_t](../server/ExternalAnimGraphHandle_t.md) |  |  |
