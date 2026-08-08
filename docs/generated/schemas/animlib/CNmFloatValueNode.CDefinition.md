---
layout: default
title: "CNmFloatValueNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmFloatValueNode::CDefinition

# CNmFloatValueNode::CDefinition

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 255 · **Module:** animlib

**Inherits from:** [CNmValueNode::CDefinition](../animlib/CNmValueNode.CDefinition.md)

**Derived by:** [CNmCachedFloatNode::CDefinition](../animlib/CNmCachedFloatNode.CDefinition.md), [CNmConstFloatNode::CDefinition](../animlib/CNmConstFloatNode.CDefinition.md), [CNmControlParameterFloatNode::CDefinition](../animlib/CNmControlParameterFloatNode.CDefinition.md), [CNmCurrentSyncEventNode::CDefinition](../animlib/CNmCurrentSyncEventNode.CDefinition.md), [CNmFloatAngleMathNode::CDefinition](../animlib/CNmFloatAngleMathNode.CDefinition.md), [CNmFloatClampNode::CDefinition](../animlib/CNmFloatClampNode.CDefinition.md), [CNmFloatCurveEventNode::CDefinition](../animlib/CNmFloatCurveEventNode.CDefinition.md), [CNmFloatCurveNode::CDefinition](../animlib/CNmFloatCurveNode.CDefinition.md), [CNmFloatEaseNode::CDefinition](../animlib/CNmFloatEaseNode.CDefinition.md), [CNmFloatMathNode::CDefinition](../animlib/CNmFloatMathNode.CDefinition.md), [CNmFloatRemapNode::CDefinition](../animlib/CNmFloatRemapNode.CDefinition.md), [CNmFloatSelectorNode::CDefinition](../animlib/CNmFloatSelectorNode.CDefinition.md), [CNmFloatSpringNode::CDefinition](../animlib/CNmFloatSpringNode.CDefinition.md), [CNmFloatSwitchNode::CDefinition](../animlib/CNmFloatSwitchNode.CDefinition.md), [CNmFootstepEventPercentageThroughNode::CDefinition](../animlib/CNmFootstepEventPercentageThroughNode.CDefinition.md), [CNmIDToFloatNode::CDefinition](../animlib/CNmIDToFloatNode.CDefinition.md), [CNmTargetInfoNode::CDefinition](../animlib/CNmTargetInfoNode.CDefinition.md), [CNmVectorInfoNode::CDefinition](../animlib/CNmVectorInfoNode.CDefinition.md), [CNmVirtualParameterFloatNode::CDefinition](../animlib/CNmVirtualParameterFloatNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmCachedFloatNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmConstFloatNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmControlParameterFloatNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmCurrentSyncEventNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatAngleMathNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatClampNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatCurveEventNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatCurveNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatEaseNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatMathNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatRemapNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatSelectorNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatSpringNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatSwitchNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFootstepEventPercentageThroughNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmIDToFloatNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmTargetInfoNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmVectorInfoNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmVirtualParameterFloatNode::CDefinition"
```

## Memory layout

1 fields (0 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
