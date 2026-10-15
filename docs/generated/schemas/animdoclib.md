---
title: animdoclib
module: animdoclib
---

# Module: animdoclib

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

[📊 View UML Diagram](../diagrams/animdoclib.md)

225 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CNmAnimDocument](animdoclib/CNmAnimDocument.md) | class | 112 | 1 |  |
| [CNmBlendSpace1D](animdoclib/CNmBlendSpace1D.md) | class | 24 | 1 |  |
| [CNmBlendSpace1D::Point_t](animdoclib/CNmBlendSpace1D.Point_t.md) | class | 32 | 3 |  |
| [CNmBlendSpace2D](animdoclib/CNmBlendSpace2D.md) | class | 96 | 4 |  |
| [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) | class | 24 | 2 |  |
| [CNmClipDocEventTrack](animdoclib/CNmClipDocEventTrack.md) | class | 40 | 5 |  |
| [CNmClipDocEvent_BodyGroup](animdoclib/CNmClipDocEvent_BodyGroup.md) | class | 48 | 3 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_CameraDOF](animdoclib/CNmClipDocEvent_CameraDOF.md) | class | 88 | 1 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_CameraFOV](animdoclib/CNmClipDocEvent_CameraFOV.md) | class | 88 | 1 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_Cloth](animdoclib/CNmClipDocEvent_Cloth.md) | class | 64 | 7 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_Contact](animdoclib/CNmClipDocEvent_Contact.md) | class | 80 | 5 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_EntityAttribute](animdoclib/CNmClipDocEvent_EntityAttribute.md) | class | 112 | 5 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_FloatCurve](animdoclib/CNmClipDocEvent_FloatCurve.md) | class | 96 | 2 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_Foot](animdoclib/CNmClipDocEvent_Foot.md) | class | 32 | 1 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_FrameSnap](animdoclib/CNmClipDocEvent_FrameSnap.md) | class | 32 | 1 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_ID](animdoclib/CNmClipDocEvent_ID.md) | class | 40 | 2 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_Legacy](animdoclib/CNmClipDocEvent_Legacy.md) | class | 48 | 2 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_MaterialAttribute](animdoclib/CNmClipDocEvent_MaterialAttribute.md) | class | 296 | 6 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_OrientationWarp](animdoclib/CNmClipDocEvent_OrientationWarp.md) | class | 24 | 0 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_Particle](animdoclib/CNmClipDocEvent_Particle.md) | class | 112 | 14 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_RootMotion](animdoclib/CNmClipDocEvent_RootMotion.md) | class | 32 | 1 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_Sound](animdoclib/CNmClipDocEvent_Sound.md) | class | 72 | 7 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_TargetWarp](animdoclib/CNmClipDocEvent_TargetWarp.md) | class | 32 | 2 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_Transition](animdoclib/CNmClipDocEvent_Transition.md) | class | 40 | 2 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocument](animdoclib/CNmClipDocument.md) | class | 248 | 13 | [CNmAnimDocument](animdoclib/CNmAnimDocument.md) |
| [CNmDocTool](animdoclib/CNmDocTool.md) | class | 8 | 0 |  |
| [CNmGraphDocAndNode](animdoclib/CNmGraphDocAndNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocAnimationPoseNode](animdoclib/CNmGraphDocAnimationPoseNode.md) | class | 536 | 3 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocAnimationPoseNode::CData](animdoclib/CNmGraphDocAnimationPoseNode.CData.md) | class | 24 | 2 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocBlend1DNode](animdoclib/CNmGraphDocBlend1DNode.md) | class | 296 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocBlend2DNode](animdoclib/CNmGraphDocBlend2DNode.md) | class | 368 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocBodyGroupNode](animdoclib/CNmGraphDocBodyGroupNode.md) | class | 520 | 0 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocBodyGroupNode::CData](animdoclib/CNmGraphDocBodyGroupNode.CData.md) | class | 24 | 2 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocBoneMaskBlendNode](animdoclib/CNmGraphDocBoneMaskBlendNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocBoneMaskNode](animdoclib/CNmGraphDocBoneMaskNode.md) | class | 536 | 2 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocBoneMaskNode::CData](animdoclib/CNmGraphDocBoneMaskNode.CData.md) | class | 16 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocBoneMaskParameterReferenceNode](animdoclib/CNmGraphDocBoneMaskParameterReferenceNode.md) | class | 312 | 0 | [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) |
| [CNmGraphDocBoneMaskResultNode](animdoclib/CNmGraphDocBoneMaskResultNode.md) | class | 272 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocBoneMaskSelectorNode](animdoclib/CNmGraphDocBoneMaskSelectorNode.md) | class | 304 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocBoneMaskSwitchNode](animdoclib/CNmGraphDocBoneMaskSwitchNode.md) | class | 272 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocBoneMaskVirtualParameterNode](animdoclib/CNmGraphDocBoneMaskVirtualParameterNode.md) | class | 272 | 0 | [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) |
| [CNmGraphDocBoolControlParameterNode](animdoclib/CNmGraphDocBoolControlParameterNode.md) | class | 296 | 1 | [CNmGraphDocControlParameterNode](animdoclib/CNmGraphDocControlParameterNode.md) |
| [CNmGraphDocBoolParameterReferenceNode](animdoclib/CNmGraphDocBoolParameterReferenceNode.md) | class | 312 | 0 | [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) |
| [CNmGraphDocBoolResultNode](animdoclib/CNmGraphDocBoolResultNode.md) | class | 272 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocBoolVirtualParameterNode](animdoclib/CNmGraphDocBoolVirtualParameterNode.md) | class | 272 | 0 | [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) |
| [CNmGraphDocCachedBoolNode](animdoclib/CNmGraphDocCachedBoolNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocCachedFloatNode](animdoclib/CNmGraphDocCachedFloatNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocCachedIDNode](animdoclib/CNmGraphDocCachedIDNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocCachedTargetNode](animdoclib/CNmGraphDocCachedTargetNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocCachedVectorNode](animdoclib/CNmGraphDocCachedVectorNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocClipNode](animdoclib/CNmGraphDocClipNode.md) | class | 552 | 3 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocClipNode::CData](animdoclib/CNmGraphDocClipNode.CData.md) | class | 24 | 3 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocClipSelectorNode](animdoclib/CNmGraphDocClipSelectorNode.md) | class | 288 | 0 | [CNmGraphDocSelectorBaseNode](animdoclib/CNmGraphDocSelectorBaseNode.md) |
| [CNmGraphDocCommentNode](animdoclib/CNmGraphDocCommentNode.md) | class | 112 | 3 | [CNmGraphDocNode](animdoclib/CNmGraphDocNode.md) |
| [CNmGraphDocControlParameterNode](animdoclib/CNmGraphDocControlParameterNode.md) | class | 288 | 1 | [CNmGraphDocParameterBaseNode](animdoclib/CNmGraphDocParameterBaseNode.md) |
| [CNmGraphDocCurrentSyncEventIDNode](animdoclib/CNmGraphDocCurrentSyncEventIDNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocCurrentSyncEventNode](animdoclib/CNmGraphDocCurrentSyncEventNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocDataDictionary](animdoclib/CNmGraphDocDataDictionary.md) | class | 48 | 2 |  |
| [CNmGraphDocDataDictionary::IDSet_t](animdoclib/CNmGraphDocDataDictionary.IDSet_t.md) | class | 48 | 3 |  |
| [CNmGraphDocDataDictionary::ParameterSet_t](animdoclib/CNmGraphDocDataDictionary.ParameterSet_t.md) | class | 32 | 2 |  |
| [CNmGraphDocDataDictionary::Parameter_t](animdoclib/CNmGraphDocDataDictionary.Parameter_t.md) | class | 64 | 5 |  |
| [CNmGraphDocEntryOverrideNode](animdoclib/CNmGraphDocEntryOverrideNode.md) | class | 288 | 1 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocEntryStateOverrideConditionsNode](animdoclib/CNmGraphDocEntryStateOverrideConditionsNode.md) | class | 296 | 1 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocEntryStateOverrideConduitNode](animdoclib/CNmGraphDocEntryStateOverrideConduitNode.md) | class | 88 | 0 | [CNmGraphDocStateMachineGraphNode](animdoclib/CNmGraphDocStateMachineGraphNode.md) |
| [CNmGraphDocExternalGraphNode](animdoclib/CNmGraphDocExternalGraphNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocExternalPoseNode](animdoclib/CNmGraphDocExternalPoseNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFixedWeightBoneMaskNode](animdoclib/CNmGraphDocFixedWeightBoneMaskNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatAngleMathNode](animdoclib/CNmGraphDocFloatAngleMathNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatClampNode](animdoclib/CNmGraphDocFloatClampNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatComparisonNode](animdoclib/CNmGraphDocFloatComparisonNode.md) | class | 280 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatControlParameterNode](animdoclib/CNmGraphDocFloatControlParameterNode.md) | class | 304 | 3 | [CNmGraphDocControlParameterNode](animdoclib/CNmGraphDocControlParameterNode.md) |
| [CNmGraphDocFloatCurveEventNode](animdoclib/CNmGraphDocFloatCurveEventNode.md) | class | 280 | 5 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatCurveNode](animdoclib/CNmGraphDocFloatCurveNode.md) | class | 328 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatEaseNode](animdoclib/CNmGraphDocFloatEaseNode.md) | class | 280 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatMathNode](animdoclib/CNmGraphDocFloatMathNode.md) | class | 272 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatParameterReferenceNode](animdoclib/CNmGraphDocFloatParameterReferenceNode.md) | class | 312 | 0 | [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) |
| [CNmGraphDocFloatRangeComparisonNode](animdoclib/CNmGraphDocFloatRangeComparisonNode.md) | class | 280 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatRemapNode](animdoclib/CNmGraphDocFloatRemapNode.md) | class | 280 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatRemapNode::RemapRange_t](animdoclib/CNmGraphDocFloatRemapNode.RemapRange_t.md) | class | 8 | 2 |  |
| [CNmGraphDocFloatResultNode](animdoclib/CNmGraphDocFloatResultNode.md) | class | 272 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocFloatSelectorNode](animdoclib/CNmGraphDocFloatSelectorNode.md) | class | 304 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatSelectorNode::Option_t](animdoclib/CNmGraphDocFloatSelectorNode.Option_t.md) | class | 16 | 2 |  |
| [CNmGraphDocFloatSpringNode](animdoclib/CNmGraphDocFloatSpringNode.md) | class | 280 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatSwitchNode](animdoclib/CNmGraphDocFloatSwitchNode.md) | class | 272 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatVirtualParameterNode](animdoclib/CNmGraphDocFloatVirtualParameterNode.md) | class | 272 | 0 | [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) |
| [CNmGraphDocFlowGraph](animdoclib/CNmGraphDocFlowGraph.md) | class | 112 | 1 | [CNmGraphDocGraph](animdoclib/CNmGraphDocGraph.md) |
| [CNmGraphDocFlowGraph::Connection_t](animdoclib/CNmGraphDocFlowGraph.Connection_t.md) | class | 80 | 5 |  |
| [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) | class | 264 | 2 | [CNmGraphDocNode](animdoclib/CNmGraphDocNode.md) |
| [CNmGraphDocFootEventConditionNode](animdoclib/CNmGraphDocFootEventConditionNode.md) | class | 272 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFootstepEventIDNode](animdoclib/CNmGraphDocFootstepEventIDNode.md) | class | 272 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFootstepEventPercentageThroughNode](animdoclib/CNmGraphDocFootstepEventPercentageThroughNode.md) | class | 272 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocGlobalTransitionConduitNode](animdoclib/CNmGraphDocGlobalTransitionConduitNode.md) | class | 88 | 0 | [CNmGraphDocStateMachineGraphNode](animdoclib/CNmGraphDocStateMachineGraphNode.md) |
| [CNmGraphDocGlobalTransitionNode](animdoclib/CNmGraphDocGlobalTransitionNode.md) | class | 312 | 1 | [CNmGraphDocTransitionNode](animdoclib/CNmGraphDocTransitionNode.md) |
| [CNmGraphDocGraph](animdoclib/CNmGraphDocGraph.md) | class | 88 | 5 |  |
| [CNmGraphDocGraphEventConditionNode](animdoclib/CNmGraphDocGraphEventConditionNode.md) | class | 296 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocGraphEventConditionNode::Condition_t](animdoclib/CNmGraphDocGraphEventConditionNode.Condition_t.md) | class | 16 | 2 |  |
| [CNmGraphDocIDBasedClipSelectorNode](animdoclib/CNmGraphDocIDBasedClipSelectorNode.md) | class | 296 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDBasedSelectorNode](animdoclib/CNmGraphDocIDBasedSelectorNode.md) | class | 296 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDComparisonNode](animdoclib/CNmGraphDocIDComparisonNode.md) | class | 296 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDControlParameterNode](animdoclib/CNmGraphDocIDControlParameterNode.md) | class | 344 | 2 | [CNmGraphDocControlParameterNode](animdoclib/CNmGraphDocControlParameterNode.md) |
| [CNmGraphDocIDEventConditionNode](animdoclib/CNmGraphDocIDEventConditionNode.md) | class | 296 | 5 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDEventNode](animdoclib/CNmGraphDocIDEventNode.md) | class | 280 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDEventPercentageThroughNode](animdoclib/CNmGraphDocIDEventPercentageThroughNode.md) | class | 280 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDParameterReferenceNode](animdoclib/CNmGraphDocIDParameterReferenceNode.md) | class | 312 | 0 | [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) |
| [CNmGraphDocIDResultNode](animdoclib/CNmGraphDocIDResultNode.md) | class | 272 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocIDSelectorNode](animdoclib/CNmGraphDocIDSelectorNode.md) | class | 296 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDSwitchNode](animdoclib/CNmGraphDocIDSwitchNode.md) | class | 280 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDToFloatNode](animdoclib/CNmGraphDocIDToFloatNode.md) | class | 296 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDToFloatNode::Mapping_t](animdoclib/CNmGraphDocIDToFloatNode.Mapping_t.md) | class | 16 | 2 |  |
| [CNmGraphDocIDVirtualParameterNode](animdoclib/CNmGraphDocIDVirtualParameterNode.md) | class | 272 | 0 | [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) |
| [CNmGraphDocIsExternalGraphSlotFilledNode](animdoclib/CNmGraphDocIsExternalGraphSlotFilledNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIsExternalPoseSetNode](animdoclib/CNmGraphDocIsExternalPoseSetNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIsInactiveBranchConditionNode](animdoclib/CNmGraphDocIsInactiveBranchConditionNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIsTargetSetNode](animdoclib/CNmGraphDocIsTargetSetNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocLayerBaseNode](animdoclib/CNmGraphDocLayerBaseNode.md) | class | 272 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocLayerBlendNode](animdoclib/CNmGraphDocLayerBlendNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocLocalLayerNode](animdoclib/CNmGraphDocLocalLayerNode.md) | class | 272 | 0 | [CNmGraphDocLayerBaseNode](animdoclib/CNmGraphDocLayerBaseNode.md) |
| [CNmGraphDocNode](animdoclib/CNmGraphDocNode.md) | class | 88 | 6 |  |
| [CNmGraphDocNotNode](animdoclib/CNmGraphDocNotNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocOrNode](animdoclib/CNmGraphDocOrNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocOrientationWarpNode](animdoclib/CNmGraphDocOrientationWarpNode.md) | class | 272 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocParameterBaseNode](animdoclib/CNmGraphDocParameterBaseNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) | class | 312 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocParameterizedClipSelectorNode](animdoclib/CNmGraphDocParameterizedClipSelectorNode.md) | class | 552 | 2 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocParameterizedClipSelectorNode::CData](animdoclib/CNmGraphDocParameterizedClipSelectorNode.CData.md) | class | 32 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocParameterizedSelectorNode](animdoclib/CNmGraphDocParameterizedSelectorNode.md) | class | 552 | 2 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocParameterizedSelectorNode::CData](animdoclib/CNmGraphDocParameterizedSelectorNode.CData.md) | class | 32 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocPoseResultNode](animdoclib/CNmGraphDocPoseResultNode.md) | class | 272 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocReferencePoseNode](animdoclib/CNmGraphDocReferencePoseNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocReferencedGraphNode](animdoclib/CNmGraphDocReferencedGraphNode.md) | class | 520 | 0 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocReferencedGraphNode::CData](animdoclib/CNmGraphDocReferencedGraphNode.CData.md) | class | 16 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocRootMotionOverrideNode](animdoclib/CNmGraphDocRootMotionOverrideNode.md) | class | 280 | 7 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocScaleNode](animdoclib/CNmGraphDocScaleNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocSelectorBaseNode](animdoclib/CNmGraphDocSelectorBaseNode.md) | class | 288 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocSelectorConditionNode](animdoclib/CNmGraphDocSelectorConditionNode.md) | class | 272 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocSelectorNode](animdoclib/CNmGraphDocSelectorNode.md) | class | 288 | 0 | [CNmGraphDocSelectorBaseNode](animdoclib/CNmGraphDocSelectorBaseNode.md) |
| [CNmGraphDocStateCompletedConditionNode](animdoclib/CNmGraphDocStateCompletedConditionNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocStateLayerDataNode](animdoclib/CNmGraphDocStateLayerDataNode.md) | class | 272 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocStateMachineGraph](animdoclib/CNmGraphDocStateMachineGraph.md) | class | 104 | 1 | [CNmGraphDocGraph](animdoclib/CNmGraphDocGraph.md) |
| [CNmGraphDocStateMachineGraphNode](animdoclib/CNmGraphDocStateMachineGraphNode.md) | class | 88 | 0 | [CNmGraphDocNode](animdoclib/CNmGraphDocNode.md) |
| [CNmGraphDocStateMachineLayerNode](animdoclib/CNmGraphDocStateMachineLayerNode.md) | class | 272 | 0 | [CNmGraphDocLayerBaseNode](animdoclib/CNmGraphDocLayerBaseNode.md) |
| [CNmGraphDocStateMachineNode](animdoclib/CNmGraphDocStateMachineNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocStateNode](animdoclib/CNmGraphDocStateNode.md) | class | 328 | 12 | [CNmGraphDocStateMachineGraphNode](animdoclib/CNmGraphDocStateMachineGraphNode.md) |
| [CNmGraphDocStateNode::StateEvent_t](animdoclib/CNmGraphDocStateNode.StateEvent_t.md) | class | 16 | 4 |  |
| [CNmGraphDocStateNode::TimedStateEvent_t](animdoclib/CNmGraphDocStateNode.TimedStateEvent_t.md) | class | 24 | 4 |  |
| [CNmGraphDocSyncEventIndexConditionNode](animdoclib/CNmGraphDocSyncEventIndexConditionNode.md) | class | 272 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTargetControlParameterNode](animdoclib/CNmGraphDocTargetControlParameterNode.md) | class | 328 | 5 | [CNmGraphDocControlParameterNode](animdoclib/CNmGraphDocControlParameterNode.md) |
| [CNmGraphDocTargetInfoNode](animdoclib/CNmGraphDocTargetInfoNode.md) | class | 272 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTargetOffsetNode](animdoclib/CNmGraphDocTargetOffsetNode.md) | class | 296 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTargetParameterReferenceNode](animdoclib/CNmGraphDocTargetParameterReferenceNode.md) | class | 312 | 0 | [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) |
| [CNmGraphDocTargetPointNode](animdoclib/CNmGraphDocTargetPointNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTargetResultNode](animdoclib/CNmGraphDocTargetResultNode.md) | class | 272 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocTargetSelectorNode](animdoclib/CNmGraphDocTargetSelectorNode.md) | class | 560 | 5 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocTargetSelectorNode::CData](animdoclib/CNmGraphDocTargetSelectorNode.CData.md) | class | 16 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocTargetVirtualParameterNode](animdoclib/CNmGraphDocTargetVirtualParameterNode.md) | class | 272 | 0 | [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) |
| [CNmGraphDocTargetWarpNode](animdoclib/CNmGraphDocTargetWarpNode.md) | class | 544 | 9 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocTargetWarpNode::CData](animdoclib/CNmGraphDocTargetWarpNode.CData.md) | class | 16 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocTimeConditionNode](animdoclib/CNmGraphDocTimeConditionNode.md) | class | 272 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTimeControlledClipNode](animdoclib/CNmGraphDocTimeControlledClipNode.md) | class | 552 | 2 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocTimeControlledClipNode::CData](animdoclib/CNmGraphDocTimeControlledClipNode.CData.md) | class | 16 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocTransitionConduitNode](animdoclib/CNmGraphDocTransitionConduitNode.md) | class | 120 | 2 | [CNmGraphDocStateMachineGraphNode](animdoclib/CNmGraphDocStateMachineGraphNode.md) |
| [CNmGraphDocTransitionEventConditionNode](animdoclib/CNmGraphDocTransitionEventConditionNode.md) | class | 288 | 5 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTransitionNode](animdoclib/CNmGraphDocTransitionNode.md) | class | 296 | 8 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocVariationConstBoneTargetNode](animdoclib/CNmGraphDocVariationConstBoneTargetNode.md) | class | 520 | 0 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocVariationConstBoneTargetNode::CData](animdoclib/CNmGraphDocVariationConstBoneTargetNode.CData.md) | class | 16 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) | class | 520 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) | class | 8 | 0 |  |
| [CNmGraphDocVariationDataNode::OverrideValue_t](animdoclib/CNmGraphDocVariationDataNode.OverrideValue_t.md) | class | 16 | 2 |  |
| [CNmGraphDocVariationIDComparisonNode](animdoclib/CNmGraphDocVariationIDComparisonNode.md) | class | 528 | 1 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocVariationIDComparisonNode::CData](animdoclib/CNmGraphDocVariationIDComparisonNode.CData.md) | class | 32 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocVectorControlParameterNode](animdoclib/CNmGraphDocVectorControlParameterNode.md) | class | 304 | 1 | [CNmGraphDocControlParameterNode](animdoclib/CNmGraphDocControlParameterNode.md) |
| [CNmGraphDocVectorCreateNode](animdoclib/CNmGraphDocVectorCreateNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocVectorInfoNode](animdoclib/CNmGraphDocVectorInfoNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocVectorNegateNode](animdoclib/CNmGraphDocVectorNegateNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocVectorParameterReferenceNode](animdoclib/CNmGraphDocVectorParameterReferenceNode.md) | class | 312 | 0 | [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) |
| [CNmGraphDocVectorResultNode](animdoclib/CNmGraphDocVectorResultNode.md) | class | 272 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocVectorVirtualParameterNode](animdoclib/CNmGraphDocVectorVirtualParameterNode.md) | class | 272 | 0 | [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) |
| [CNmGraphDocVelocityBlendNode](animdoclib/CNmGraphDocVelocityBlendNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) | class | 272 | 0 | [CNmGraphDocParameterBaseNode](animdoclib/CNmGraphDocParameterBaseNode.md) |
| [CNmGraphDocZeroPoseNode](animdoclib/CNmGraphDocZeroPoseNode.md) | class | 264 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocument](animdoclib/CNmGraphDocument.md) | class | 200 | 5 | [CNmAnimDocument](animdoclib/CNmAnimDocument.md) |
| [CNmGraphDocument::DebugBoneFilterSet_t](animdoclib/CNmGraphDocument.DebugBoneFilterSet_t.md) | class | 32 | 2 |  |
| [CNmGraphDocument::DebugParameterSet_t](animdoclib/CNmGraphDocument.DebugParameterSet_t.md) | class | 88 | 6 |  |
| [CNmPreviewArchetype](animdoclib/CNmPreviewArchetype.md) | class | 64 | 4 |  |
| [CNmPreviewArchetype::SecondarySkeleton_t](animdoclib/CNmPreviewArchetype.SecondarySkeleton_t.md) | class | 32 | 4 |  |
| [CNmSkeletonDocument](animdoclib/CNmSkeletonDocument.md) | class | 312 | 12 | [CNmAnimDocument](animdoclib/CNmAnimDocument.md) |
| [CNmSkeletonDocument::ContactConfig_t](animdoclib/CNmSkeletonDocument.ContactConfig_t.md) | class | 56 | 5 |  |
| [CNmSkeletonDocument::SecondarySkeleton_t](animdoclib/CNmSkeletonDocument.SecondarySkeleton_t.md) | class | 16 | 2 |  |
| [CNmVariationHierarchy](animdoclib/CNmVariationHierarchy.md) | class | 24 | 1 |  |
| [CnmGraphDocChainLookatNode](animdoclib/CnmGraphDocChainLookatNode.md) | class | 528 | 1 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CnmGraphDocChainLookatNode::CData](animdoclib/CnmGraphDocChainLookatNode.CData.md) | class | 72 | 6 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CnmGraphDocConstBoneTargetNode](animdoclib/CnmGraphDocConstBoneTargetNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocConstBoolNode](animdoclib/CnmGraphDocConstBoolNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocConstFloatNode](animdoclib/CnmGraphDocConstFloatNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocConstIDNode](animdoclib/CnmGraphDocConstIDNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocConstTargetNode](animdoclib/CnmGraphDocConstTargetNode.md) | class | 288 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocConstVectorNode](animdoclib/CnmGraphDocConstVectorNode.md) | class | 280 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocDurationScaleNode](animdoclib/CnmGraphDocDurationScaleNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocFollowBoneNode](animdoclib/CnmGraphDocFollowBoneNode.md) | class | 528 | 1 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CnmGraphDocFollowBoneNode::CData](animdoclib/CnmGraphDocFollowBoneNode.CData.md) | class | 24 | 2 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CnmGraphDocFootIKNode](animdoclib/CnmGraphDocFootIKNode.md) | class | 528 | 2 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CnmGraphDocFootIKNode::CData](animdoclib/CnmGraphDocFootIKNode.CData.md) | class | 32 | 3 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CnmGraphDocSpeedScaleNode](animdoclib/CnmGraphDocSpeedScaleNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocTwoBoneIKNode](animdoclib/CnmGraphDocTwoBoneIKNode.md) | class | 528 | 3 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CnmGraphDocTwoBoneIKNode::CData](animdoclib/CnmGraphDocTwoBoneIKNode.CData.md) | class | 24 | 2 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CnmGraphDocVariationConstFloatNode](animdoclib/CnmGraphDocVariationConstFloatNode.md) | class | 520 | 0 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CnmGraphDocVariationConstFloatNode::CData](animdoclib/CnmGraphDocVariationConstFloatNode.CData.md) | class | 16 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CnmGraphDocVelocityBasedSpeedScaleNode](animdoclib/CnmGraphDocVelocityBasedSpeedScaleNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [NmGraphDocPin_t](animdoclib/NmGraphDocPin_t.md) | class | 32 | 5 |  |
| [NmVariation_t](animdoclib/NmVariation_t.md) | class | 248 | 4 |  |
| [CNmClipDocEventTrack::Type_t](animdoclib/CNmClipDocEventTrack.Type_t.md) | enum | — | 3 |  |
| [CNmClipDocEvent_EntityAttribute_Type_t](animdoclib/CNmClipDocEvent_EntityAttribute_Type_t.md) | enum | — | 2 |  |
| [CNmClipDocument::AdditiveBaseFrame_t](animdoclib/CNmClipDocument.AdditiveBaseFrame_t.md) | enum | — | 3 |  |
| [CNmClipDocument::AdditiveType_t](animdoclib/CNmClipDocument.AdditiveType_t.md) | enum | — | 5 |  |
| [CNmGraphDocIDEventConditionNode::SearchRule_t](animdoclib/CNmGraphDocIDEventConditionNode.SearchRule_t.md) | enum | — | 3 |  |
| [CNmGraphDocOrientationWarpNode::OffsetType_t](animdoclib/CNmGraphDocOrientationWarpNode.OffsetType_t.md) | enum | — | 2 |  |
| [CNmGraphDocStateNode::StateType_t](animdoclib/CNmGraphDocStateNode.StateType_t.md) | enum | — | 4 |  |
| [CNmGraphDocStateNode::TimedStateEventType_t](animdoclib/CNmGraphDocStateNode.TimedStateEventType_t.md) | enum | — | 2 |  |
| [CNmGraphDocTransitionNode::TimeMatchMode_t](animdoclib/CNmGraphDocTransitionNode.TimeMatchMode_t.md) | enum | — | 11 |  |
| [NmDocToolFlag_t](animdoclib/NmDocToolFlag_t.md) | enum | — | 5 |  |
| [NmDocToolType_t](animdoclib/NmDocToolType_t.md) | enum | — | 3 |  |
| [NmEventConditionOperator_t](animdoclib/NmEventConditionOperator_t.md) | enum | — | 2 |  |
| [NmEventPriorityRule_t](animdoclib/NmEventPriorityRule_t.md) | enum | — | 2 |  |
| [NmGraphDocGraphType_t](animdoclib/NmGraphDocGraphType_t.md) | enum | — | 8 |  |
