---
layout: default
title: CNmGraphDocFlowNode
nav_exclude: true
---

[Schemas](../../schemas.md) / [animdoclib](../animdoclib.md) / CNmGraphDocFlowNode

# CNmGraphDocFlowNode

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 256 bytes (`0x100`) · **Align:** n/a (unspecified) · **Module:** animdoclib

**Inherits from:** [CNmGraphDocNode](../animdoclib/CNmGraphDocNode.md)

**Derived by:** [CNmGraphDocAimCSNode](../modtools/CNmGraphDocAimCSNode.md), [CNmGraphDocAndNode](../animdoclib/CNmGraphDocAndNode.md), [CNmGraphDocBlend1DNode](../animdoclib/CNmGraphDocBlend1DNode.md), [CNmGraphDocBlend2DNode](../animdoclib/CNmGraphDocBlend2DNode.md), [CNmGraphDocBoneMaskBlendNode](../animdoclib/CNmGraphDocBoneMaskBlendNode.md), [CNmGraphDocBoneMaskSelectorNode](../animdoclib/CNmGraphDocBoneMaskSelectorNode.md), [CNmGraphDocBoneMaskSwitchNode](../animdoclib/CNmGraphDocBoneMaskSwitchNode.md), [CNmGraphDocCachedBoolNode](../animdoclib/CNmGraphDocCachedBoolNode.md), [CNmGraphDocCachedFloatNode](../animdoclib/CNmGraphDocCachedFloatNode.md), [CNmGraphDocCachedIDNode](../animdoclib/CNmGraphDocCachedIDNode.md), [CNmGraphDocCachedTargetNode](../animdoclib/CNmGraphDocCachedTargetNode.md), [CNmGraphDocCachedVectorNode](../animdoclib/CNmGraphDocCachedVectorNode.md), [CNmGraphDocCurrentSyncEventIDNode](../animdoclib/CNmGraphDocCurrentSyncEventIDNode.md), [CNmGraphDocCurrentSyncEventNode](../animdoclib/CNmGraphDocCurrentSyncEventNode.md), [CNmGraphDocExternalGraphNode](../animdoclib/CNmGraphDocExternalGraphNode.md), [CNmGraphDocExternalPoseNode](../animdoclib/CNmGraphDocExternalPoseNode.md), [CNmGraphDocFixedWeightBoneMaskNode](../animdoclib/CNmGraphDocFixedWeightBoneMaskNode.md), [CNmGraphDocFloatAngleMathNode](../animdoclib/CNmGraphDocFloatAngleMathNode.md), [CNmGraphDocFloatClampNode](../animdoclib/CNmGraphDocFloatClampNode.md), [CNmGraphDocFloatComparisonNode](../animdoclib/CNmGraphDocFloatComparisonNode.md), [CNmGraphDocFloatCurveEventNode](../animdoclib/CNmGraphDocFloatCurveEventNode.md), [CNmGraphDocFloatCurveNode](../animdoclib/CNmGraphDocFloatCurveNode.md), [CNmGraphDocFloatEaseNode](../animdoclib/CNmGraphDocFloatEaseNode.md), [CNmGraphDocFloatMathNode](../animdoclib/CNmGraphDocFloatMathNode.md), [CNmGraphDocFloatRangeComparisonNode](../animdoclib/CNmGraphDocFloatRangeComparisonNode.md), [CNmGraphDocFloatRemapNode](../animdoclib/CNmGraphDocFloatRemapNode.md), [CNmGraphDocFloatSelectorNode](../animdoclib/CNmGraphDocFloatSelectorNode.md), [CNmGraphDocFloatSpringNode](../animdoclib/CNmGraphDocFloatSpringNode.md), [CNmGraphDocFloatSwitchNode](../animdoclib/CNmGraphDocFloatSwitchNode.md), [CNmGraphDocFootEventConditionNode](../animdoclib/CNmGraphDocFootEventConditionNode.md), [CNmGraphDocFootstepEventIDNode](../animdoclib/CNmGraphDocFootstepEventIDNode.md), [CNmGraphDocFootstepEventPercentageThroughNode](../animdoclib/CNmGraphDocFootstepEventPercentageThroughNode.md), [CNmGraphDocGraphEventConditionNode](../animdoclib/CNmGraphDocGraphEventConditionNode.md), [CNmGraphDocIDBasedClipSelectorNode](../animdoclib/CNmGraphDocIDBasedClipSelectorNode.md), [CNmGraphDocIDBasedSelectorNode](../animdoclib/CNmGraphDocIDBasedSelectorNode.md), [CNmGraphDocIDComparisonNode](../animdoclib/CNmGraphDocIDComparisonNode.md), [CNmGraphDocIDEventConditionNode](../animdoclib/CNmGraphDocIDEventConditionNode.md), [CNmGraphDocIDEventNode](../animdoclib/CNmGraphDocIDEventNode.md), [CNmGraphDocIDEventPercentageThroughNode](../animdoclib/CNmGraphDocIDEventPercentageThroughNode.md), [CNmGraphDocIDSelectorNode](../animdoclib/CNmGraphDocIDSelectorNode.md), [CNmGraphDocIDSwitchNode](../animdoclib/CNmGraphDocIDSwitchNode.md), [CNmGraphDocIDToFloatNode](../animdoclib/CNmGraphDocIDToFloatNode.md), [CNmGraphDocIsExternalGraphSlotFilledNode](../animdoclib/CNmGraphDocIsExternalGraphSlotFilledNode.md), [CNmGraphDocIsExternalPoseSetNode](../animdoclib/CNmGraphDocIsExternalPoseSetNode.md), [CNmGraphDocIsInactiveBranchConditionNode](../animdoclib/CNmGraphDocIsInactiveBranchConditionNode.md), [CNmGraphDocIsTargetSetNode](../animdoclib/CNmGraphDocIsTargetSetNode.md), [CNmGraphDocLayerBaseNode](../animdoclib/CNmGraphDocLayerBaseNode.md), [CNmGraphDocLayerBlendNode](../animdoclib/CNmGraphDocLayerBlendNode.md), [CNmGraphDocNotNode](../animdoclib/CNmGraphDocNotNode.md), [CNmGraphDocOrNode](../animdoclib/CNmGraphDocOrNode.md), [CNmGraphDocOrientationWarpNode](../animdoclib/CNmGraphDocOrientationWarpNode.md), [CNmGraphDocParameterBaseNode](../animdoclib/CNmGraphDocParameterBaseNode.md), [CNmGraphDocParameterReferenceNode](../animdoclib/CNmGraphDocParameterReferenceNode.md), [CNmGraphDocReferencePoseNode](../animdoclib/CNmGraphDocReferencePoseNode.md), [CNmGraphDocResultNode](../animdoclib/CNmGraphDocResultNode.md), [CNmGraphDocRootMotionOverrideNode](../animdoclib/CNmGraphDocRootMotionOverrideNode.md), [CNmGraphDocScaleNode](../animdoclib/CNmGraphDocScaleNode.md), [CNmGraphDocSelectorBaseNode](../animdoclib/CNmGraphDocSelectorBaseNode.md), [CNmGraphDocStateCompletedConditionNode](../animdoclib/CNmGraphDocStateCompletedConditionNode.md), [CNmGraphDocStateMachineNode](../animdoclib/CNmGraphDocStateMachineNode.md), [CNmGraphDocSyncEventIndexConditionNode](../animdoclib/CNmGraphDocSyncEventIndexConditionNode.md), [CNmGraphDocTargetInfoNode](../animdoclib/CNmGraphDocTargetInfoNode.md), [CNmGraphDocTargetOffsetNode](../animdoclib/CNmGraphDocTargetOffsetNode.md), [CNmGraphDocTargetPointNode](../animdoclib/CNmGraphDocTargetPointNode.md), [CNmGraphDocTargetSelectorNode](../animdoclib/CNmGraphDocTargetSelectorNode.md), [CNmGraphDocTimeConditionNode](../animdoclib/CNmGraphDocTimeConditionNode.md), [CNmGraphDocTransitionEventConditionNode](../animdoclib/CNmGraphDocTransitionEventConditionNode.md), [CNmGraphDocVariationDataNode](../animdoclib/CNmGraphDocVariationDataNode.md), [CNmGraphDocVectorCreateNode](../animdoclib/CNmGraphDocVectorCreateNode.md), [CNmGraphDocVectorInfoNode](../animdoclib/CNmGraphDocVectorInfoNode.md), [CNmGraphDocVectorNegateNode](../animdoclib/CNmGraphDocVectorNegateNode.md), [CNmGraphDocVelocityBlendNode](../animdoclib/CNmGraphDocVelocityBlendNode.md), [CNmGraphDocZeroPoseNode](../animdoclib/CNmGraphDocZeroPoseNode.md), [CnmGraphDocConstBoneTargetNode](../animdoclib/CnmGraphDocConstBoneTargetNode.md), [CnmGraphDocConstBoolNode](../animdoclib/CnmGraphDocConstBoolNode.md), [CnmGraphDocConstFloatNode](../animdoclib/CnmGraphDocConstFloatNode.md), [CnmGraphDocConstIDNode](../animdoclib/CnmGraphDocConstIDNode.md), [CnmGraphDocConstTargetNode](../animdoclib/CnmGraphDocConstTargetNode.md), [CnmGraphDocConstVectorNode](../animdoclib/CnmGraphDocConstVectorNode.md), [CnmGraphDocDurationScaleNode](../animdoclib/CnmGraphDocDurationScaleNode.md), [CnmGraphDocSnapWeaponNode](../modtools/CnmGraphDocSnapWeaponNode.md), [CnmGraphDocSpeedScaleNode](../animdoclib/CnmGraphDocSpeedScaleNode.md), [CnmGraphDocVelocityBasedSpeedScaleNode](../animdoclib/CnmGraphDocVelocityBasedSpeedScaleNode.md)

**Relationships:**

```mermaid
classDiagram
    CNmGraphDocNode <|-- CNmGraphDocFlowNode
    CNmGraphDocFlowNode <|-- CNmGraphDocAimCSNode
    CNmGraphDocFlowNode <|-- CNmGraphDocAndNode
    CNmGraphDocFlowNode <|-- CNmGraphDocBlend1DNode
    CNmGraphDocFlowNode <|-- CNmGraphDocBlend2DNode
    CNmGraphDocFlowNode <|-- CNmGraphDocBoneMaskBlendNode
    CNmGraphDocFlowNode <|-- CNmGraphDocBoneMaskSelectorNode
    CNmGraphDocFlowNode <|-- CNmGraphDocBoneMaskSwitchNode
    CNmGraphDocFlowNode <|-- CNmGraphDocCachedBoolNode
    CNmGraphDocFlowNode <|-- CNmGraphDocCachedFloatNode
    CNmGraphDocFlowNode <|-- CNmGraphDocCachedIDNode
    CNmGraphDocFlowNode <|-- CNmGraphDocCachedTargetNode
    CNmGraphDocFlowNode <|-- CNmGraphDocCachedVectorNode
    CNmGraphDocFlowNode <|-- CNmGraphDocCurrentSyncEventIDNode
    CNmGraphDocFlowNode <|-- CNmGraphDocCurrentSyncEventNode
    CNmGraphDocFlowNode <|-- CNmGraphDocExternalGraphNode
    CNmGraphDocFlowNode <|-- CNmGraphDocExternalPoseNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFixedWeightBoneMaskNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFloatAngleMathNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFloatClampNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFloatComparisonNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFloatCurveEventNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFloatCurveNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFloatEaseNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFloatMathNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFloatRangeComparisonNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFloatRemapNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFloatSelectorNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFloatSpringNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFloatSwitchNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFootEventConditionNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFootstepEventIDNode
    CNmGraphDocFlowNode <|-- CNmGraphDocFootstepEventPercentageThroughNode
    CNmGraphDocFlowNode <|-- CNmGraphDocGraphEventConditionNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIDBasedClipSelectorNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIDBasedSelectorNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIDComparisonNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIDEventConditionNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIDEventNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIDEventPercentageThroughNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIDSelectorNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIDSwitchNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIDToFloatNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIsExternalGraphSlotFilledNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIsExternalPoseSetNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIsInactiveBranchConditionNode
    CNmGraphDocFlowNode <|-- CNmGraphDocIsTargetSetNode
    CNmGraphDocFlowNode <|-- CNmGraphDocLayerBaseNode
    CNmGraphDocFlowNode <|-- CNmGraphDocLayerBlendNode
    CNmGraphDocFlowNode <|-- CNmGraphDocNotNode
    CNmGraphDocFlowNode <|-- CNmGraphDocOrNode
    CNmGraphDocFlowNode <|-- CNmGraphDocOrientationWarpNode
    CNmGraphDocFlowNode <|-- CNmGraphDocParameterBaseNode
    CNmGraphDocFlowNode <|-- CNmGraphDocParameterReferenceNode
    CNmGraphDocFlowNode <|-- CNmGraphDocReferencePoseNode
    CNmGraphDocFlowNode <|-- CNmGraphDocResultNode
    CNmGraphDocFlowNode <|-- CNmGraphDocRootMotionOverrideNode
    CNmGraphDocFlowNode <|-- CNmGraphDocScaleNode
    CNmGraphDocFlowNode <|-- CNmGraphDocSelectorBaseNode
    CNmGraphDocFlowNode <|-- CNmGraphDocStateCompletedConditionNode
    CNmGraphDocFlowNode <|-- CNmGraphDocStateMachineNode
    CNmGraphDocFlowNode <|-- CNmGraphDocSyncEventIndexConditionNode
    CNmGraphDocFlowNode <|-- CNmGraphDocTargetInfoNode
    CNmGraphDocFlowNode <|-- CNmGraphDocTargetOffsetNode
    CNmGraphDocFlowNode <|-- CNmGraphDocTargetPointNode
    CNmGraphDocFlowNode <|-- CNmGraphDocTargetSelectorNode
    CNmGraphDocFlowNode <|-- CNmGraphDocTimeConditionNode
    CNmGraphDocFlowNode <|-- CNmGraphDocTransitionEventConditionNode
    CNmGraphDocFlowNode <|-- CNmGraphDocVariationDataNode
    CNmGraphDocFlowNode <|-- CNmGraphDocVectorCreateNode
    CNmGraphDocFlowNode <|-- CNmGraphDocVectorInfoNode
    CNmGraphDocFlowNode <|-- CNmGraphDocVectorNegateNode
    CNmGraphDocFlowNode <|-- CNmGraphDocVelocityBlendNode
    CNmGraphDocFlowNode <|-- CNmGraphDocZeroPoseNode
    CNmGraphDocFlowNode <|-- CnmGraphDocConstBoneTargetNode
    CNmGraphDocFlowNode <|-- CnmGraphDocConstBoolNode
    CNmGraphDocFlowNode <|-- CnmGraphDocConstFloatNode
    CNmGraphDocFlowNode <|-- CnmGraphDocConstIDNode
    CNmGraphDocFlowNode <|-- CnmGraphDocConstTargetNode
    CNmGraphDocFlowNode <|-- CnmGraphDocConstVectorNode
    CNmGraphDocFlowNode <|-- CnmGraphDocDurationScaleNode
    CNmGraphDocFlowNode <|-- CnmGraphDocSnapWeaponNode
    CNmGraphDocFlowNode <|-- CnmGraphDocSpeedScaleNode
    CNmGraphDocFlowNode <|-- CnmGraphDocVelocityBasedSpeedScaleNode
    CNmGraphDocFlowNode *-- NmGraphDocPin_t
```

## Memory layout

8 fields (2 declared here, 6 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_ID` | V_uuid_t | [CNmGraphDocNode](../animdoclib/CNmGraphDocNode.md) | `MPropertySuppressField` |
| `0x18` | `m_name` | CUtlString | [CNmGraphDocNode](../animdoclib/CNmGraphDocNode.md) | `MPropertyHideField` |
| `0x20` | `m_floatingComment` | CUtlString | [CNmGraphDocNode](../animdoclib/CNmGraphDocNode.md) | `MPropertyAttributeEditor TextBlock()` |
| `0x28` | `m_position` | Vector2D | [CNmGraphDocNode](../animdoclib/CNmGraphDocNode.md) | `MPropertySuppressField` |
| `0x40` | `m_pChildGraph` | [CNmGraphDocGraph](../animdoclib/CNmGraphDocGraph.md)* | [CNmGraphDocNode](../animdoclib/CNmGraphDocNode.md) | `MPropertySuppressField` |
| `0x48` | `m_pSecondaryGraph` | [CNmGraphDocGraph](../animdoclib/CNmGraphDocGraph.md)* | [CNmGraphDocNode](../animdoclib/CNmGraphDocNode.md) | `MPropertySuppressField` |
| `0x50` | `m_inputPins` | CUtlLeanVectorFixedGrowable< [NmGraphDocPin_t](../animdoclib/NmGraphDocPin_t.md), 4 > |  |  |
| `0xd8` | `m_outputPins` | CUtlLeanVectorFixedGrowable< [NmGraphDocPin_t](../animdoclib/NmGraphDocPin_t.md), 1 > |  |  |
