---
layout: default
title: animdoclib
parent: Schemas
nav_exclude: true
---

# Module: animdoclib

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

[📊 View UML Diagram](../diagrams/animdoclib.md)

209 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CNmAnimDocument](animdoclib/CNmAnimDocument.md) | class | 112 | 1 |  |
| [CNmBlendSpace1D](animdoclib/CNmBlendSpace1D.md) | class | 24 | 1 |  |
| [CNmBlendSpace1D::Point_t](animdoclib/CNmBlendSpace1D.Point_t.md) | class | 32 | 3 |  |
| [CNmBlendSpace2D](animdoclib/CNmBlendSpace2D.md) | class | 96 | 4 |  |
| [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) | class | 16 | 2 |  |
| [CNmClipDocEventTrack](animdoclib/CNmClipDocEventTrack.md) | class | 40 | 5 |  |
| [CNmClipDocEvent_BodyGroup](animdoclib/CNmClipDocEvent_BodyGroup.md) | class | 40 | 3 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_EntityAttribute](animdoclib/CNmClipDocEvent_EntityAttribute.md) | class | 104 | 5 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_FloatCurve](animdoclib/CNmClipDocEvent_FloatCurve.md) | class | 88 | 2 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_Foot](animdoclib/CNmClipDocEvent_Foot.md) | class | 24 | 1 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_FrameSnap](animdoclib/CNmClipDocEvent_FrameSnap.md) | class | 24 | 1 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_ID](animdoclib/CNmClipDocEvent_ID.md) | class | 32 | 2 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_Legacy](animdoclib/CNmClipDocEvent_Legacy.md) | class | 40 | 2 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_MaterialAttribute](animdoclib/CNmClipDocEvent_MaterialAttribute.md) | class | 288 | 6 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_OrientationWarp](animdoclib/CNmClipDocEvent_OrientationWarp.md) | class | 16 | 0 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_Particle](animdoclib/CNmClipDocEvent_Particle.md) | class | 104 | 14 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_RootMotion](animdoclib/CNmClipDocEvent_RootMotion.md) | class | 24 | 1 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_Sound](animdoclib/CNmClipDocEvent_Sound.md) | class | 64 | 7 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_TargetWarp](animdoclib/CNmClipDocEvent_TargetWarp.md) | class | 24 | 2 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocEvent_Transition](animdoclib/CNmClipDocEvent_Transition.md) | class | 32 | 2 | [CNmClipDocEvent](animdoclib/CNmClipDocEvent.md) |
| [CNmClipDocument](animdoclib/CNmClipDocument.md) | class | 248 | 13 | [CNmAnimDocument](animdoclib/CNmAnimDocument.md) |
| [CNmGraphDocAndNode](animdoclib/CNmGraphDocAndNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocAnimationPoseNode](animdoclib/CNmGraphDocAnimationPoseNode.md) | class | 528 | 3 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocAnimationPoseNode::CData](animdoclib/CNmGraphDocAnimationPoseNode.CData.md) | class | 24 | 2 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocBlend1DNode](animdoclib/CNmGraphDocBlend1DNode.md) | class | 288 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocBlend2DNode](animdoclib/CNmGraphDocBlend2DNode.md) | class | 360 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocBoneMaskBlendNode](animdoclib/CNmGraphDocBoneMaskBlendNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocBoneMaskNode](animdoclib/CNmGraphDocBoneMaskNode.md) | class | 528 | 2 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocBoneMaskNode::CData](animdoclib/CNmGraphDocBoneMaskNode.CData.md) | class | 16 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocBoneMaskParameterReferenceNode](animdoclib/CNmGraphDocBoneMaskParameterReferenceNode.md) | class | 304 | 0 | [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) |
| [CNmGraphDocBoneMaskResultNode](animdoclib/CNmGraphDocBoneMaskResultNode.md) | class | 264 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocBoneMaskSelectorNode](animdoclib/CNmGraphDocBoneMaskSelectorNode.md) | class | 296 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocBoneMaskSwitchNode](animdoclib/CNmGraphDocBoneMaskSwitchNode.md) | class | 264 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocBoneMaskVirtualParameterNode](animdoclib/CNmGraphDocBoneMaskVirtualParameterNode.md) | class | 264 | 0 | [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) |
| [CNmGraphDocBoolControlParameterNode](animdoclib/CNmGraphDocBoolControlParameterNode.md) | class | 288 | 1 | [CNmGraphDocControlParameterNode](animdoclib/CNmGraphDocControlParameterNode.md) |
| [CNmGraphDocBoolParameterReferenceNode](animdoclib/CNmGraphDocBoolParameterReferenceNode.md) | class | 304 | 0 | [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) |
| [CNmGraphDocBoolResultNode](animdoclib/CNmGraphDocBoolResultNode.md) | class | 264 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocBoolVirtualParameterNode](animdoclib/CNmGraphDocBoolVirtualParameterNode.md) | class | 264 | 0 | [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) |
| [CNmGraphDocCachedBoolNode](animdoclib/CNmGraphDocCachedBoolNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocCachedFloatNode](animdoclib/CNmGraphDocCachedFloatNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocCachedIDNode](animdoclib/CNmGraphDocCachedIDNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocCachedTargetNode](animdoclib/CNmGraphDocCachedTargetNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocCachedVectorNode](animdoclib/CNmGraphDocCachedVectorNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocClipNode](animdoclib/CNmGraphDocClipNode.md) | class | 544 | 3 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocClipNode::CData](animdoclib/CNmGraphDocClipNode.CData.md) | class | 24 | 3 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocClipSelectorNode](animdoclib/CNmGraphDocClipSelectorNode.md) | class | 280 | 0 | [CNmGraphDocSelectorBaseNode](animdoclib/CNmGraphDocSelectorBaseNode.md) |
| [CNmGraphDocCommentNode](animdoclib/CNmGraphDocCommentNode.md) | class | 104 | 3 | [CNmGraphDocNode](animdoclib/CNmGraphDocNode.md) |
| [CNmGraphDocControlParameterNode](animdoclib/CNmGraphDocControlParameterNode.md) | class | 280 | 1 | [CNmGraphDocParameterBaseNode](animdoclib/CNmGraphDocParameterBaseNode.md) |
| [CNmGraphDocCurrentSyncEventIDNode](animdoclib/CNmGraphDocCurrentSyncEventIDNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocCurrentSyncEventNode](animdoclib/CNmGraphDocCurrentSyncEventNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocDataDictionary](animdoclib/CNmGraphDocDataDictionary.md) | class | 48 | 2 |  |
| [CNmGraphDocDataDictionary::IDSet_t](animdoclib/CNmGraphDocDataDictionary.IDSet_t.md) | class | 48 | 3 |  |
| [CNmGraphDocDataDictionary::ParameterSet_t](animdoclib/CNmGraphDocDataDictionary.ParameterSet_t.md) | class | 32 | 2 |  |
| [CNmGraphDocDataDictionary::Parameter_t](animdoclib/CNmGraphDocDataDictionary.Parameter_t.md) | class | 64 | 5 |  |
| [CNmGraphDocEntryOverrideNode](animdoclib/CNmGraphDocEntryOverrideNode.md) | class | 280 | 1 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocEntryStateOverrideConditionsNode](animdoclib/CNmGraphDocEntryStateOverrideConditionsNode.md) | class | 288 | 1 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocEntryStateOverrideConduitNode](animdoclib/CNmGraphDocEntryStateOverrideConduitNode.md) | class | 80 | 0 | [CNmGraphDocStateMachineGraphNode](animdoclib/CNmGraphDocStateMachineGraphNode.md) |
| [CNmGraphDocExternalGraphNode](animdoclib/CNmGraphDocExternalGraphNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocExternalPoseNode](animdoclib/CNmGraphDocExternalPoseNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFixedWeightBoneMaskNode](animdoclib/CNmGraphDocFixedWeightBoneMaskNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatAngleMathNode](animdoclib/CNmGraphDocFloatAngleMathNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatClampNode](animdoclib/CNmGraphDocFloatClampNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatComparisonNode](animdoclib/CNmGraphDocFloatComparisonNode.md) | class | 272 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatControlParameterNode](animdoclib/CNmGraphDocFloatControlParameterNode.md) | class | 296 | 3 | [CNmGraphDocControlParameterNode](animdoclib/CNmGraphDocControlParameterNode.md) |
| [CNmGraphDocFloatCurveEventNode](animdoclib/CNmGraphDocFloatCurveEventNode.md) | class | 272 | 5 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatCurveNode](animdoclib/CNmGraphDocFloatCurveNode.md) | class | 320 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatEaseNode](animdoclib/CNmGraphDocFloatEaseNode.md) | class | 272 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatMathNode](animdoclib/CNmGraphDocFloatMathNode.md) | class | 264 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatParameterReferenceNode](animdoclib/CNmGraphDocFloatParameterReferenceNode.md) | class | 304 | 0 | [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) |
| [CNmGraphDocFloatRangeComparisonNode](animdoclib/CNmGraphDocFloatRangeComparisonNode.md) | class | 272 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatRemapNode](animdoclib/CNmGraphDocFloatRemapNode.md) | class | 272 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatRemapNode::RemapRange_t](animdoclib/CNmGraphDocFloatRemapNode.RemapRange_t.md) | class | 8 | 2 |  |
| [CNmGraphDocFloatResultNode](animdoclib/CNmGraphDocFloatResultNode.md) | class | 264 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocFloatSelectorNode](animdoclib/CNmGraphDocFloatSelectorNode.md) | class | 296 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatSelectorNode::Option_t](animdoclib/CNmGraphDocFloatSelectorNode.Option_t.md) | class | 16 | 2 |  |
| [CNmGraphDocFloatSpringNode](animdoclib/CNmGraphDocFloatSpringNode.md) | class | 272 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatSwitchNode](animdoclib/CNmGraphDocFloatSwitchNode.md) | class | 264 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFloatVirtualParameterNode](animdoclib/CNmGraphDocFloatVirtualParameterNode.md) | class | 264 | 0 | [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) |
| [CNmGraphDocFlowGraph](animdoclib/CNmGraphDocFlowGraph.md) | class | 104 | 1 | [CNmGraphDocGraph](animdoclib/CNmGraphDocGraph.md) |
| [CNmGraphDocFlowGraph::Connection_t](animdoclib/CNmGraphDocFlowGraph.Connection_t.md) | class | 80 | 5 |  |
| [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) | class | 256 | 2 | [CNmGraphDocNode](animdoclib/CNmGraphDocNode.md) |
| [CNmGraphDocFootEventConditionNode](animdoclib/CNmGraphDocFootEventConditionNode.md) | class | 264 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFootstepEventIDNode](animdoclib/CNmGraphDocFootstepEventIDNode.md) | class | 264 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocFootstepEventPercentageThroughNode](animdoclib/CNmGraphDocFootstepEventPercentageThroughNode.md) | class | 264 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocGlobalTransitionConduitNode](animdoclib/CNmGraphDocGlobalTransitionConduitNode.md) | class | 80 | 0 | [CNmGraphDocStateMachineGraphNode](animdoclib/CNmGraphDocStateMachineGraphNode.md) |
| [CNmGraphDocGlobalTransitionNode](animdoclib/CNmGraphDocGlobalTransitionNode.md) | class | 304 | 1 | [CNmGraphDocTransitionNode](animdoclib/CNmGraphDocTransitionNode.md) |
| [CNmGraphDocGraph](animdoclib/CNmGraphDocGraph.md) | class | 80 | 5 |  |
| [CNmGraphDocGraphEventConditionNode](animdoclib/CNmGraphDocGraphEventConditionNode.md) | class | 288 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocGraphEventConditionNode::Condition_t](animdoclib/CNmGraphDocGraphEventConditionNode.Condition_t.md) | class | 16 | 2 |  |
| [CNmGraphDocIDBasedClipSelectorNode](animdoclib/CNmGraphDocIDBasedClipSelectorNode.md) | class | 288 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDBasedSelectorNode](animdoclib/CNmGraphDocIDBasedSelectorNode.md) | class | 288 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDComparisonNode](animdoclib/CNmGraphDocIDComparisonNode.md) | class | 288 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDControlParameterNode](animdoclib/CNmGraphDocIDControlParameterNode.md) | class | 336 | 2 | [CNmGraphDocControlParameterNode](animdoclib/CNmGraphDocControlParameterNode.md) |
| [CNmGraphDocIDEventConditionNode](animdoclib/CNmGraphDocIDEventConditionNode.md) | class | 288 | 5 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDEventNode](animdoclib/CNmGraphDocIDEventNode.md) | class | 272 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDEventPercentageThroughNode](animdoclib/CNmGraphDocIDEventPercentageThroughNode.md) | class | 272 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDParameterReferenceNode](animdoclib/CNmGraphDocIDParameterReferenceNode.md) | class | 304 | 0 | [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) |
| [CNmGraphDocIDResultNode](animdoclib/CNmGraphDocIDResultNode.md) | class | 264 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocIDSelectorNode](animdoclib/CNmGraphDocIDSelectorNode.md) | class | 288 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDSwitchNode](animdoclib/CNmGraphDocIDSwitchNode.md) | class | 272 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDToFloatNode](animdoclib/CNmGraphDocIDToFloatNode.md) | class | 288 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIDToFloatNode::Mapping_t](animdoclib/CNmGraphDocIDToFloatNode.Mapping_t.md) | class | 16 | 2 |  |
| [CNmGraphDocIDVirtualParameterNode](animdoclib/CNmGraphDocIDVirtualParameterNode.md) | class | 264 | 0 | [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) |
| [CNmGraphDocIsExternalGraphSlotFilledNode](animdoclib/CNmGraphDocIsExternalGraphSlotFilledNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIsExternalPoseSetNode](animdoclib/CNmGraphDocIsExternalPoseSetNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIsInactiveBranchConditionNode](animdoclib/CNmGraphDocIsInactiveBranchConditionNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocIsTargetSetNode](animdoclib/CNmGraphDocIsTargetSetNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocLayerBaseNode](animdoclib/CNmGraphDocLayerBaseNode.md) | class | 264 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocLayerBlendNode](animdoclib/CNmGraphDocLayerBlendNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocLocalLayerNode](animdoclib/CNmGraphDocLocalLayerNode.md) | class | 264 | 0 | [CNmGraphDocLayerBaseNode](animdoclib/CNmGraphDocLayerBaseNode.md) |
| [CNmGraphDocNode](animdoclib/CNmGraphDocNode.md) | class | 80 | 6 |  |
| [CNmGraphDocNotNode](animdoclib/CNmGraphDocNotNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocOrNode](animdoclib/CNmGraphDocOrNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocOrientationWarpNode](animdoclib/CNmGraphDocOrientationWarpNode.md) | class | 264 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocParameterBaseNode](animdoclib/CNmGraphDocParameterBaseNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) | class | 304 | 4 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocParameterizedClipSelectorNode](animdoclib/CNmGraphDocParameterizedClipSelectorNode.md) | class | 544 | 2 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocParameterizedClipSelectorNode::CData](animdoclib/CNmGraphDocParameterizedClipSelectorNode.CData.md) | class | 32 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocParameterizedSelectorNode](animdoclib/CNmGraphDocParameterizedSelectorNode.md) | class | 544 | 2 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocParameterizedSelectorNode::CData](animdoclib/CNmGraphDocParameterizedSelectorNode.CData.md) | class | 32 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocPoseResultNode](animdoclib/CNmGraphDocPoseResultNode.md) | class | 264 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocReferencePoseNode](animdoclib/CNmGraphDocReferencePoseNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocReferencedGraphNode](animdoclib/CNmGraphDocReferencedGraphNode.md) | class | 512 | 0 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocReferencedGraphNode::CData](animdoclib/CNmGraphDocReferencedGraphNode.CData.md) | class | 16 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocRootMotionOverrideNode](animdoclib/CNmGraphDocRootMotionOverrideNode.md) | class | 272 | 7 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocScaleNode](animdoclib/CNmGraphDocScaleNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocSelectorBaseNode](animdoclib/CNmGraphDocSelectorBaseNode.md) | class | 280 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocSelectorConditionNode](animdoclib/CNmGraphDocSelectorConditionNode.md) | class | 264 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocSelectorNode](animdoclib/CNmGraphDocSelectorNode.md) | class | 280 | 0 | [CNmGraphDocSelectorBaseNode](animdoclib/CNmGraphDocSelectorBaseNode.md) |
| [CNmGraphDocStateCompletedConditionNode](animdoclib/CNmGraphDocStateCompletedConditionNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocStateLayerDataNode](animdoclib/CNmGraphDocStateLayerDataNode.md) | class | 264 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocStateMachineGraph](animdoclib/CNmGraphDocStateMachineGraph.md) | class | 96 | 1 | [CNmGraphDocGraph](animdoclib/CNmGraphDocGraph.md) |
| [CNmGraphDocStateMachineGraphNode](animdoclib/CNmGraphDocStateMachineGraphNode.md) | class | 80 | 0 | [CNmGraphDocNode](animdoclib/CNmGraphDocNode.md) |
| [CNmGraphDocStateMachineLayerNode](animdoclib/CNmGraphDocStateMachineLayerNode.md) | class | 264 | 0 | [CNmGraphDocLayerBaseNode](animdoclib/CNmGraphDocLayerBaseNode.md) |
| [CNmGraphDocStateMachineNode](animdoclib/CNmGraphDocStateMachineNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocStateNode](animdoclib/CNmGraphDocStateNode.md) | class | 304 | 11 | [CNmGraphDocStateMachineGraphNode](animdoclib/CNmGraphDocStateMachineGraphNode.md) |
| [CNmGraphDocStateNode::StateEvent_t](animdoclib/CNmGraphDocStateNode.StateEvent_t.md) | class | 16 | 4 |  |
| [CNmGraphDocStateNode::TimedStateEvent_t](animdoclib/CNmGraphDocStateNode.TimedStateEvent_t.md) | class | 24 | 4 |  |
| [CNmGraphDocSyncEventIndexConditionNode](animdoclib/CNmGraphDocSyncEventIndexConditionNode.md) | class | 264 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTargetControlParameterNode](animdoclib/CNmGraphDocTargetControlParameterNode.md) | class | 320 | 5 | [CNmGraphDocControlParameterNode](animdoclib/CNmGraphDocControlParameterNode.md) |
| [CNmGraphDocTargetInfoNode](animdoclib/CNmGraphDocTargetInfoNode.md) | class | 264 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTargetOffsetNode](animdoclib/CNmGraphDocTargetOffsetNode.md) | class | 288 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTargetParameterReferenceNode](animdoclib/CNmGraphDocTargetParameterReferenceNode.md) | class | 304 | 0 | [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) |
| [CNmGraphDocTargetPointNode](animdoclib/CNmGraphDocTargetPointNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTargetResultNode](animdoclib/CNmGraphDocTargetResultNode.md) | class | 264 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocTargetSelectorNode](animdoclib/CNmGraphDocTargetSelectorNode.md) | class | 296 | 5 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTargetVirtualParameterNode](animdoclib/CNmGraphDocTargetVirtualParameterNode.md) | class | 264 | 0 | [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) |
| [CNmGraphDocTargetWarpNode](animdoclib/CNmGraphDocTargetWarpNode.md) | class | 536 | 9 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocTargetWarpNode::CData](animdoclib/CNmGraphDocTargetWarpNode.CData.md) | class | 16 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocTimeConditionNode](animdoclib/CNmGraphDocTimeConditionNode.md) | class | 264 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTransitionConduitNode](animdoclib/CNmGraphDocTransitionConduitNode.md) | class | 112 | 2 | [CNmGraphDocStateMachineGraphNode](animdoclib/CNmGraphDocStateMachineGraphNode.md) |
| [CNmGraphDocTransitionEventConditionNode](animdoclib/CNmGraphDocTransitionEventConditionNode.md) | class | 280 | 5 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocTransitionNode](animdoclib/CNmGraphDocTransitionNode.md) | class | 288 | 8 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) | class | 512 | 3 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) | class | 8 | 0 |  |
| [CNmGraphDocVariationDataNode::OverrideValue_t](animdoclib/CNmGraphDocVariationDataNode.OverrideValue_t.md) | class | 16 | 2 |  |
| [CNmGraphDocVariationIDComparisonNode](animdoclib/CNmGraphDocVariationIDComparisonNode.md) | class | 520 | 1 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CNmGraphDocVariationIDComparisonNode::CData](animdoclib/CNmGraphDocVariationIDComparisonNode.CData.md) | class | 32 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CNmGraphDocVectorControlParameterNode](animdoclib/CNmGraphDocVectorControlParameterNode.md) | class | 296 | 1 | [CNmGraphDocControlParameterNode](animdoclib/CNmGraphDocControlParameterNode.md) |
| [CNmGraphDocVectorCreateNode](animdoclib/CNmGraphDocVectorCreateNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocVectorInfoNode](animdoclib/CNmGraphDocVectorInfoNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocVectorNegateNode](animdoclib/CNmGraphDocVectorNegateNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocVectorParameterReferenceNode](animdoclib/CNmGraphDocVectorParameterReferenceNode.md) | class | 304 | 0 | [CNmGraphDocParameterReferenceNode](animdoclib/CNmGraphDocParameterReferenceNode.md) |
| [CNmGraphDocVectorResultNode](animdoclib/CNmGraphDocVectorResultNode.md) | class | 264 | 0 | [CNmGraphDocResultNode](animdoclib/CNmGraphDocResultNode.md) |
| [CNmGraphDocVectorVirtualParameterNode](animdoclib/CNmGraphDocVectorVirtualParameterNode.md) | class | 264 | 0 | [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) |
| [CNmGraphDocVelocityBlendNode](animdoclib/CNmGraphDocVelocityBlendNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocVirtualParameterNode](animdoclib/CNmGraphDocVirtualParameterNode.md) | class | 264 | 0 | [CNmGraphDocParameterBaseNode](animdoclib/CNmGraphDocParameterBaseNode.md) |
| [CNmGraphDocZeroPoseNode](animdoclib/CNmGraphDocZeroPoseNode.md) | class | 256 | 0 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CNmGraphDocument](animdoclib/CNmGraphDocument.md) | class | 184 | 4 | [CNmAnimDocument](animdoclib/CNmAnimDocument.md) |
| [CNmGraphDocument::DebugParameterSet_t](animdoclib/CNmGraphDocument.DebugParameterSet_t.md) | class | 88 | 6 |  |
| [CNmPreviewArchetype](animdoclib/CNmPreviewArchetype.md) | class | 64 | 4 |  |
| [CNmPreviewArchetype::SecondarySkeleton_t](animdoclib/CNmPreviewArchetype.SecondarySkeleton_t.md) | class | 32 | 4 |  |
| [CNmSkeletonDocument](animdoclib/CNmSkeletonDocument.md) | class | 288 | 11 | [CNmAnimDocument](animdoclib/CNmAnimDocument.md) |
| [CNmSkeletonDocument::SecondarySkeleton_t](animdoclib/CNmSkeletonDocument.SecondarySkeleton_t.md) | class | 16 | 2 |  |
| [CNmVariationHierarchy](animdoclib/CNmVariationHierarchy.md) | class | 24 | 1 |  |
| [CnmGraphDocChainLookatNode](animdoclib/CnmGraphDocChainLookatNode.md) | class | 520 | 1 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CnmGraphDocChainLookatNode::CData](animdoclib/CnmGraphDocChainLookatNode.CData.md) | class | 72 | 6 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CnmGraphDocConstBoneTargetNode](animdoclib/CnmGraphDocConstBoneTargetNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocConstBoolNode](animdoclib/CnmGraphDocConstBoolNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocConstFloatNode](animdoclib/CnmGraphDocConstFloatNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocConstIDNode](animdoclib/CnmGraphDocConstIDNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocConstTargetNode](animdoclib/CnmGraphDocConstTargetNode.md) | class | 280 | 2 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocConstVectorNode](animdoclib/CnmGraphDocConstVectorNode.md) | class | 272 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocDurationScaleNode](animdoclib/CnmGraphDocDurationScaleNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocFollowBoneNode](animdoclib/CnmGraphDocFollowBoneNode.md) | class | 520 | 1 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CnmGraphDocFollowBoneNode::CData](animdoclib/CnmGraphDocFollowBoneNode.CData.md) | class | 24 | 2 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CnmGraphDocFootIKNode](animdoclib/CnmGraphDocFootIKNode.md) | class | 520 | 2 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CnmGraphDocFootIKNode::CData](animdoclib/CnmGraphDocFootIKNode.CData.md) | class | 32 | 3 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CnmGraphDocSpeedScaleNode](animdoclib/CnmGraphDocSpeedScaleNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
| [CnmGraphDocTwoBoneIKNode](animdoclib/CnmGraphDocTwoBoneIKNode.md) | class | 520 | 3 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CnmGraphDocTwoBoneIKNode::CData](animdoclib/CnmGraphDocTwoBoneIKNode.CData.md) | class | 24 | 2 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CnmGraphDocVariationConstFloatNode](animdoclib/CnmGraphDocVariationConstFloatNode.md) | class | 512 | 0 | [CNmGraphDocVariationDataNode](animdoclib/CNmGraphDocVariationDataNode.md) |
| [CnmGraphDocVariationConstFloatNode::CData](animdoclib/CnmGraphDocVariationConstFloatNode.CData.md) | class | 16 | 1 | [CNmGraphDocVariationDataNode::CData](animdoclib/CNmGraphDocVariationDataNode.CData.md) |
| [CnmGraphDocVelocityBasedSpeedScaleNode](animdoclib/CnmGraphDocVelocityBasedSpeedScaleNode.md) | class | 264 | 1 | [CNmGraphDocFlowNode](animdoclib/CNmGraphDocFlowNode.md) |
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
| [NmEventConditionOperator_t](animdoclib/NmEventConditionOperator_t.md) | enum | — | 2 |  |
| [NmEventPriorityRule_t](animdoclib/NmEventPriorityRule_t.md) | enum | — | 2 |  |
| [NmGraphDocGraphType_t](animdoclib/NmGraphDocGraphType_t.md) | enum | — | 8 |  |
