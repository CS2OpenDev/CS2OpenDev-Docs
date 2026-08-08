---
layout: default
title: "CNmVectorValueNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmVectorValueNode::CDefinition

# CNmVectorValueNode::CDefinition

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 255 · **Module:** animlib

**Inherits from:** [CNmValueNode::CDefinition](../animlib/CNmValueNode.CDefinition.md)

**Derived by:** [CNmCachedVectorNode::CDefinition](../animlib/CNmCachedVectorNode.CDefinition.md), [CNmConstVectorNode::CDefinition](../animlib/CNmConstVectorNode.CDefinition.md), [CNmControlParameterVectorNode::CDefinition](../animlib/CNmControlParameterVectorNode.CDefinition.md), [CNmTargetPointNode::CDefinition](../animlib/CNmTargetPointNode.CDefinition.md), [CNmVectorCreateNode::CDefinition](../animlib/CNmVectorCreateNode.CDefinition.md), [CNmVectorNegateNode::CDefinition](../animlib/CNmVectorNegateNode.CDefinition.md), [CNmVirtualParameterVectorNode::CDefinition](../animlib/CNmVirtualParameterVectorNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmCachedVectorNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmConstVectorNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmControlParameterVectorNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmTargetPointNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmVectorCreateNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmVectorNegateNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmVirtualParameterVectorNode::CDefinition"
```

## Memory layout

1 fields (0 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
