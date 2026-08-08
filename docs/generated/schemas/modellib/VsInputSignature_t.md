---
layout: default
title: VsInputSignature_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / VsInputSignature_t

# VsInputSignature_t

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 255 · **Module:** modellib

**Relationships:**

```mermaid
classDiagram
    VsInputSignature_t *-- VsInputSignatureElement_t
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_elems` | CUtlVector< [VsInputSignatureElement_t](../modellib/VsInputSignatureElement_t.md) > |  |  |
| `0x18` | `m_depth_elems` | CUtlVector< [VsInputSignatureElement_t](../modellib/VsInputSignatureElement_t.md) > |  |  |
