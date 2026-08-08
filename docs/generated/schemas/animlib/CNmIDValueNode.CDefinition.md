---
layout: default
title: "CNmIDValueNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmIDValueNode::CDefinition

# CNmIDValueNode::CDefinition

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 255 · **Module:** animlib

**Inherits from:** [CNmValueNode::CDefinition](../animlib/CNmValueNode.CDefinition.md)

**Derived by:** [CNmCachedIDNode::CDefinition](../animlib/CNmCachedIDNode.CDefinition.md), [CNmConstIDNode::CDefinition](../animlib/CNmConstIDNode.CDefinition.md), [CNmControlParameterIDNode::CDefinition](../animlib/CNmControlParameterIDNode.CDefinition.md), [CNmCurrentSyncEventIDNode::CDefinition](../animlib/CNmCurrentSyncEventIDNode.CDefinition.md), [CNmFootstepEventIDNode::CDefinition](../animlib/CNmFootstepEventIDNode.CDefinition.md), [CNmIDEventNode::CDefinition](../animlib/CNmIDEventNode.CDefinition.md), [CNmIDSelectorNode::CDefinition](../animlib/CNmIDSelectorNode.CDefinition.md), [CNmIDSwitchNode::CDefinition](../animlib/CNmIDSwitchNode.CDefinition.md), [CNmVirtualParameterIDNode::CDefinition](../animlib/CNmVirtualParameterIDNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmCachedIDNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmConstIDNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmControlParameterIDNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmCurrentSyncEventIDNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmFootstepEventIDNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmIDEventNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmIDSelectorNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmIDSwitchNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmVirtualParameterIDNode::CDefinition"
```

## Memory layout

1 fields (0 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
