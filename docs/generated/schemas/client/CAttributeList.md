---
title: CAttributeList (client)
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / CAttributeList

# CAttributeList

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 120 bytes (`0x78`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [CAttributeList (server)](../server/CAttributeList.md)

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
