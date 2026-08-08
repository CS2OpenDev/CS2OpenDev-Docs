---
layout: default
title: "CNmGraphNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmGraphNode::CDefinition

# CNmGraphNode::CDefinition

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 255 · **Module:** animlib

**Derived by:** [CNmPoseNode::CDefinition](../animlib/CNmPoseNode.CDefinition.md), [CNmValueNode::CDefinition](../animlib/CNmValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

## Memory layout

1 fields (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 |  |  |
