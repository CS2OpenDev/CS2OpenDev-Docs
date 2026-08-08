---
layout: default
title: "CNmBoolValueNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmBoolValueNode::CDefinition

# CNmBoolValueNode::CDefinition

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 255 · **Module:** animlib

**Inherits from:** [CNmValueNode::CDefinition](../animlib/CNmValueNode.CDefinition.md)

**Derived by:** [CNmAndNode::CDefinition](../animlib/CNmAndNode.CDefinition.md), [CNmCachedBoolNode::CDefinition](../animlib/CNmCachedBoolNode.CDefinition.md), [CNmConstBoolNode::CDefinition](../animlib/CNmConstBoolNode.CDefinition.md), [CNmControlParameterBoolNode::CDefinition](../animlib/CNmControlParameterBoolNode.CDefinition.md), [CNmFloatComparisonNode::CDefinition](../animlib/CNmFloatComparisonNode.CDefinition.md), [CNmFloatRangeComparisonNode::CDefinition](../animlib/CNmFloatRangeComparisonNode.CDefinition.md), [CNmFootEventConditionNode::CDefinition](../animlib/CNmFootEventConditionNode.CDefinition.md), [CNmGraphEventConditionNode::CDefinition](../animlib/CNmGraphEventConditionNode.CDefinition.md), [CNmIDComparisonNode::CDefinition](../animlib/CNmIDComparisonNode.CDefinition.md), [CNmIDEventConditionNode::CDefinition](../animlib/CNmIDEventConditionNode.CDefinition.md), [CNmIDEventPercentageThroughNode::CDefinition](../animlib/CNmIDEventPercentageThroughNode.CDefinition.md), [CNmIsExternalGraphSlotFilledNode::CDefinition](../animlib/CNmIsExternalGraphSlotFilledNode.CDefinition.md), [CNmIsExternalPoseSetNode::CDefinition](../animlib/CNmIsExternalPoseSetNode.CDefinition.md), [CNmIsInactiveBranchConditionNode::CDefinition](../animlib/CNmIsInactiveBranchConditionNode.CDefinition.md), [CNmIsTargetSetNode::CDefinition](../animlib/CNmIsTargetSetNode.CDefinition.md), [CNmNotNode::CDefinition](../animlib/CNmNotNode.CDefinition.md), [CNmOrNode::CDefinition](../animlib/CNmOrNode.CDefinition.md), [CNmStateCompletedConditionNode::CDefinition](../animlib/CNmStateCompletedConditionNode.CDefinition.md), [CNmSyncEventIndexConditionNode::CDefinition](../animlib/CNmSyncEventIndexConditionNode.CDefinition.md), [CNmTimeConditionNode::CDefinition](../animlib/CNmTimeConditionNode.CDefinition.md), [CNmTransitionEventConditionNode::CDefinition](../animlib/CNmTransitionEventConditionNode.CDefinition.md), [CNmVirtualParameterBoolNode::CDefinition](../animlib/CNmVirtualParameterBoolNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmAndNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmCachedBoolNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmConstBoolNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmControlParameterBoolNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmFloatComparisonNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmFloatRangeComparisonNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmFootEventConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmGraphEventConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIDComparisonNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIDEventConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIDEventPercentageThroughNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIsExternalGraphSlotFilledNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIsExternalPoseSetNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIsInactiveBranchConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIsTargetSetNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmNotNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmOrNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmStateCompletedConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmSyncEventIndexConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmTimeConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmTransitionEventConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmVirtualParameterBoolNode::CDefinition"
```

## Memory layout

1 fields (0 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
