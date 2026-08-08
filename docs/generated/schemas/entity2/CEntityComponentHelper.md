---
layout: default
title: CEntityComponentHelper
nav_exclude: true
---

[Schemas](../../schemas.md) / [entity2](../entity2.md) / CEntityComponentHelper

# CEntityComponentHelper

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** 255 · **Module:** entity2

**Relationships:**

```mermaid
classDiagram
    CEntityComponentHelper --> EntComponentInfo_t
```

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_flags` | uint32 |  |  |
| `0x10` | `m_pInfo` | [EntComponentInfo_t](../entity2/EntComponentInfo_t.md)* |  |  |
| `0x18` | `m_nPriority` | int32 |  |  |
| `0x20` | `m_pNext` | [CEntityComponentHelper](../entity2/CEntityComponentHelper.md)* |  |  |
