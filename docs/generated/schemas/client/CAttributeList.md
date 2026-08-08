---
layout: default
title: CAttributeList
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CAttributeList

# CAttributeList

**Kind:** class · **Size:** 120 bytes (`0x78`) · **Align:** 255 · **Module:** client

**Relationships:**

```mermaid
classDiagram
    CAttributeList *-- CEconItemAttribute
    CAttributeList --> CAttributeManager
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_Attributes` | C_UtlVectorEmbeddedNetworkVar< [CEconItemAttribute](../client/CEconItemAttribute.md) > |  |  |
| `0x70` | `m_pManager` | [CAttributeManager](../client/CAttributeManager.md)* |  |  |
