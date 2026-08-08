---
layout: default
title: "CNmTargetValueNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmTargetValueNode::CDefinition

# CNmTargetValueNode::CDefinition

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 255 · **Module:** animlib

**Inherits from:** [CNmValueNode::CDefinition](../animlib/CNmValueNode.CDefinition.md)

**Derived by:** [CNmCachedTargetNode::CDefinition](../animlib/CNmCachedTargetNode.CDefinition.md), [CNmConstTargetNode::CDefinition](../animlib/CNmConstTargetNode.CDefinition.md), [CNmControlParameterTargetNode::CDefinition](../animlib/CNmControlParameterTargetNode.CDefinition.md), [CNmTargetOffsetNode::CDefinition](../animlib/CNmTargetOffsetNode.CDefinition.md), [CNmVirtualParameterTargetNode::CDefinition](../animlib/CNmVirtualParameterTargetNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmValueNode::CDefinition" <|-- "CNmTargetValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmTargetValueNode::CDefinition" <|-- "CNmCachedTargetNode::CDefinition"
    "CNmTargetValueNode::CDefinition" <|-- "CNmConstTargetNode::CDefinition"
    "CNmTargetValueNode::CDefinition" <|-- "CNmControlParameterTargetNode::CDefinition"
    "CNmTargetValueNode::CDefinition" <|-- "CNmTargetOffsetNode::CDefinition"
    "CNmTargetValueNode::CDefinition" <|-- "CNmVirtualParameterTargetNode::CDefinition"
```

## Memory layout

1 fields (0 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
