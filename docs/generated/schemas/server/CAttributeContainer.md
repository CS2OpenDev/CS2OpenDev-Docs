---
layout: default
title: CAttributeContainer
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CAttributeContainer

# CAttributeContainer

**Kind:** class · **Size:** 760 bytes (`0x2f8`) · **Align:** 255 · **Module:** server

**Inherits from:** [CAttributeManager](../server/CAttributeManager.md)

**Relationships:**

```mermaid
classDiagram
    CAttributeManager <|-- CAttributeContainer
    CAttributeContainer *-- CEconItemView
```

## Memory layout

7 fields (1 declared here, 6 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_Providers` | CUtlVector< CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > > | [CAttributeManager](../server/CAttributeManager.md) |  |
| `0x20` | `m_iReapplyProvisionParity` | int32 | [CAttributeManager](../server/CAttributeManager.md) |  |
| `0x24` | `m_hOuter` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > | [CAttributeManager](../server/CAttributeManager.md) |  |
| `0x28` | `m_bPreventLoopback` | bool | [CAttributeManager](../server/CAttributeManager.md) |  |
| `0x2c` | `m_ProviderType` | attributeprovidertypes_t | [CAttributeManager](../server/CAttributeManager.md) |  |
| `0x30` | `m_CachedResults` | CUtlVector< [CAttributeManager](../server/CAttributeManager.md)::cached_attribute_float_t > | [CAttributeManager](../server/CAttributeManager.md) |  |
| `0x50` | `m_Item` | [CEconItemView](../server/CEconItemView.md) |  |  |
