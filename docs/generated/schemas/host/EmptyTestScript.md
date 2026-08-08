---
layout: default
title: EmptyTestScript
nav_exclude: true
---

[Schemas](../../schemas.md) / [host](../host.md) / EmptyTestScript

# EmptyTestScript

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 255 · **Module:** host

**Inherits from:** [CAnimScriptBase](../host/CAnimScriptBase.md)

**Relationships:**

```mermaid
classDiagram
    CAnimScriptBase <|-- EmptyTestScript
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_bIsValid` | bool | [CAnimScriptBase](../host/CAnimScriptBase.md) |  |
| `0x10` | `m_hTest` | CAnimScriptParam< float32 > |  |  |
