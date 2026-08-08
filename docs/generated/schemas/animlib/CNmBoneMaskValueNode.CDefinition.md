---
layout: default
title: "CNmBoneMaskValueNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmBoneMaskValueNode::CDefinition

# CNmBoneMaskValueNode::CDefinition

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 255 · **Module:** animlib

**Inherits from:** [CNmValueNode::CDefinition](../animlib/CNmValueNode.CDefinition.md)

**Derived by:** [CNmBoneMaskBlendNode::CDefinition](../animlib/CNmBoneMaskBlendNode.CDefinition.md), [CNmBoneMaskNode::CDefinition](../animlib/CNmBoneMaskNode.CDefinition.md), [CNmBoneMaskSelectorNode::CDefinition](../animlib/CNmBoneMaskSelectorNode.CDefinition.md), [CNmBoneMaskSwitchNode::CDefinition](../animlib/CNmBoneMaskSwitchNode.CDefinition.md), [CNmFixedWeightBoneMaskNode::CDefinition](../animlib/CNmFixedWeightBoneMaskNode.CDefinition.md), [CNmVirtualParameterBoneMaskNode::CDefinition](../animlib/CNmVirtualParameterBoneMaskNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmValueNode::CDefinition" <|-- "CNmBoneMaskValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskBlendNode::CDefinition"
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskNode::CDefinition"
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskSelectorNode::CDefinition"
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskSwitchNode::CDefinition"
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmFixedWeightBoneMaskNode::CDefinition"
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmVirtualParameterBoneMaskNode::CDefinition"
```

## Memory layout

1 fields (0 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
