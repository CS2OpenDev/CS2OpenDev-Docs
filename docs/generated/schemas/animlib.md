---
layout: default
title: animlib
parent: Schemas
nav_exclude: true
---

# Module: animlib

[📊 View UML Diagram](../diagrams/animlib.md)

180 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CNmAdditiveBlendTask](animlib/CNmAdditiveBlendTask.md) | class | 256 | 0 | [CNmBlendTaskBase](animlib/CNmBlendTaskBase.md) |
| [CNmAndNode::CDefinition](animlib/CNmAndNode.CDefinition.md) | class | 32 | 1 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmAnimationPoseNode::CDefinition](animlib/CNmAnimationPoseNode.CDefinition.md) | class | 40 | 5 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmBitFlags](animlib/CNmBitFlags.md) | class | 4 | 1 |  |
| [CNmBlend1DNode::CDefinition](animlib/CNmBlend1DNode.CDefinition.md) | class | 128 | 1 | [CNmParameterizedBlendNode::CDefinition](animlib/CNmParameterizedBlendNode.CDefinition.md) |
| [CNmBlend2DNode::CDefinition](animlib/CNmBlend2DNode.CDefinition.md) | class | 200 | 7 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmBlendTask](animlib/CNmBlendTask.md) | class | 256 | 0 | [CNmBlendTaskBase](animlib/CNmBlendTaskBase.md) |
| [CNmBlendTaskBase](animlib/CNmBlendTaskBase.md) | class | 256 | 0 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [CNmBodyGroupEvent](animlib/CNmBodyGroupEvent.md) | class | 48 | 3 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmBoneMaskBlendNode::CDefinition](animlib/CNmBoneMaskBlendNode.CDefinition.md) | class | 24 | 3 | [CNmBoneMaskValueNode::CDefinition](animlib/CNmBoneMaskValueNode.CDefinition.md) |
| [CNmBoneMaskNode::CDefinition](animlib/CNmBoneMaskNode.CDefinition.md) | class | 24 | 1 | [CNmBoneMaskValueNode::CDefinition](animlib/CNmBoneMaskValueNode.CDefinition.md) |
| [CNmBoneMaskSelectorNode::CDefinition](animlib/CNmBoneMaskSelectorNode.CDefinition.md) | class | 120 | 6 | [CNmBoneMaskValueNode::CDefinition](animlib/CNmBoneMaskValueNode.CDefinition.md) |
| [CNmBoneMaskSwitchNode::CDefinition](animlib/CNmBoneMaskSwitchNode.CDefinition.md) | class | 32 | 5 | [CNmBoneMaskValueNode::CDefinition](animlib/CNmBoneMaskValueNode.CDefinition.md) |
| [CNmBoneMaskValueNode::CDefinition](animlib/CNmBoneMaskValueNode.CDefinition.md) | class | 16 | 0 | [CNmValueNode::CDefinition](animlib/CNmValueNode.CDefinition.md) |
| [CNmBoneWeightList](animlib/CNmBoneWeightList.md) | class | 272 | 3 |  |
| [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) | class | 16 | 0 | [CNmValueNode::CDefinition](animlib/CNmValueNode.CDefinition.md) |
| [CNmCachedBoolNode::CDefinition](animlib/CNmCachedBoolNode.CDefinition.md) | class | 24 | 2 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmCachedFloatNode::CDefinition](animlib/CNmCachedFloatNode.CDefinition.md) | class | 24 | 2 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmCachedIDNode::CDefinition](animlib/CNmCachedIDNode.CDefinition.md) | class | 24 | 2 | [CNmIDValueNode::CDefinition](animlib/CNmIDValueNode.CDefinition.md) |
| [CNmCachedPoseReadTask](animlib/CNmCachedPoseReadTask.md) | class | 128 | 0 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [CNmCachedPoseWriteTask](animlib/CNmCachedPoseWriteTask.md) | class | 128 | 0 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [CNmCachedTargetNode::CDefinition](animlib/CNmCachedTargetNode.CDefinition.md) | class | 24 | 2 | [CNmTargetValueNode::CDefinition](animlib/CNmTargetValueNode.CDefinition.md) |
| [CNmCachedVectorNode::CDefinition](animlib/CNmCachedVectorNode.CDefinition.md) | class | 24 | 2 | [CNmVectorValueNode::CDefinition](animlib/CNmVectorValueNode.CDefinition.md) |
| [CNmChainLookatNode::CDefinition](animlib/CNmChainLookatNode.CDefinition.md) | class | 120 | 9 | [CNmPassthroughNode::CDefinition](animlib/CNmPassthroughNode.CDefinition.md) |
| [CNmChainLookatTask](animlib/CNmChainLookatTask.md) | class | 288 | 0 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [CNmClip](animlib/CNmClip.md) | class | 512 | 13 |  |
| [CNmClip::ModelSpaceSamplingChainLink_t](animlib/CNmClip.ModelSpaceSamplingChainLink_t.md) | class | 12 | 3 |  |
| [CNmClipNode::CDefinition](animlib/CNmClipNode.CDefinition.md) | class | 72 | 8 | [CNmClipReferenceNode::CDefinition](animlib/CNmClipReferenceNode.CDefinition.md) |
| [CNmClipReferenceNode::CDefinition](animlib/CNmClipReferenceNode.CDefinition.md) | class | 16 | 0 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmClipSelectorNode::CDefinition](animlib/CNmClipSelectorNode.CDefinition.md) | class | 64 | 2 | [CNmClipReferenceNode::CDefinition](animlib/CNmClipReferenceNode.CDefinition.md) |
| [CNmConstBoolNode::CDefinition](animlib/CNmConstBoolNode.CDefinition.md) | class | 24 | 1 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmConstFloatNode::CDefinition](animlib/CNmConstFloatNode.CDefinition.md) | class | 24 | 1 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmConstIDNode::CDefinition](animlib/CNmConstIDNode.CDefinition.md) | class | 24 | 1 | [CNmIDValueNode::CDefinition](animlib/CNmIDValueNode.CDefinition.md) |
| [CNmConstTargetNode::CDefinition](animlib/CNmConstTargetNode.CDefinition.md) | class | 64 | 1 | [CNmTargetValueNode::CDefinition](animlib/CNmTargetValueNode.CDefinition.md) |
| [CNmConstVectorNode::CDefinition](animlib/CNmConstVectorNode.CDefinition.md) | class | 32 | 1 | [CNmVectorValueNode::CDefinition](animlib/CNmVectorValueNode.CDefinition.md) |
| [CNmControlParameterBoolNode::CDefinition](animlib/CNmControlParameterBoolNode.CDefinition.md) | class | 16 | 0 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmControlParameterFloatNode::CDefinition](animlib/CNmControlParameterFloatNode.CDefinition.md) | class | 16 | 0 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmControlParameterIDNode::CDefinition](animlib/CNmControlParameterIDNode.CDefinition.md) | class | 16 | 0 | [CNmIDValueNode::CDefinition](animlib/CNmIDValueNode.CDefinition.md) |
| [CNmControlParameterTargetNode::CDefinition](animlib/CNmControlParameterTargetNode.CDefinition.md) | class | 16 | 0 | [CNmTargetValueNode::CDefinition](animlib/CNmTargetValueNode.CDefinition.md) |
| [CNmControlParameterVectorNode::CDefinition](animlib/CNmControlParameterVectorNode.CDefinition.md) | class | 16 | 0 | [CNmVectorValueNode::CDefinition](animlib/CNmVectorValueNode.CDefinition.md) |
| [CNmCurrentSyncEventIDNode::CDefinition](animlib/CNmCurrentSyncEventIDNode.CDefinition.md) | class | 24 | 1 | [CNmIDValueNode::CDefinition](animlib/CNmIDValueNode.CDefinition.md) |
| [CNmCurrentSyncEventNode::CDefinition](animlib/CNmCurrentSyncEventNode.CDefinition.md) | class | 24 | 2 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmDurationScaleNode::CDefinition](animlib/CNmDurationScaleNode.CDefinition.md) | class | 32 | 0 | [CNmSpeedScaleBaseNode::CDefinition](animlib/CNmSpeedScaleBaseNode.CDefinition.md) |
| [CNmEntityAttributeEventBase](animlib/CNmEntityAttributeEventBase.md) | class | 56 | 2 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmEntityAttributeFloatEvent](animlib/CNmEntityAttributeFloatEvent.md) | class | 120 | 1 | [CNmEntityAttributeEventBase](animlib/CNmEntityAttributeEventBase.md) |
| [CNmEntityAttributeIntEvent](animlib/CNmEntityAttributeIntEvent.md) | class | 64 | 1 | [CNmEntityAttributeEventBase](animlib/CNmEntityAttributeEventBase.md) |
| [CNmEvent](animlib/CNmEvent.md) | class | 24 | 3 |  |
| [CNmExternalPoseNode::CDefinition](animlib/CNmExternalPoseNode.CDefinition.md) | class | 24 | 1 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmFixedWeightBoneMaskNode::CDefinition](animlib/CNmFixedWeightBoneMaskNode.CDefinition.md) | class | 24 | 1 | [CNmBoneMaskValueNode::CDefinition](animlib/CNmBoneMaskValueNode.CDefinition.md) |
| [CNmFloatAngleMathNode::CDefinition](animlib/CNmFloatAngleMathNode.CDefinition.md) | class | 24 | 2 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmFloatChannelData](animlib/CNmFloatChannelData.md) | class | 88 | 5 |  |
| [CNmFloatChannelData::ChannelSettings_t](animlib/CNmFloatChannelData.ChannelSettings_t.md) | class | 12 | 2 |  |
| [CNmFloatChannelSet_t](animlib/CNmFloatChannelSet_t.md) | class | 24 | 2 |  |
| [CNmFloatClampNode::CDefinition](animlib/CNmFloatClampNode.CDefinition.md) | class | 32 | 2 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmFloatComparisonNode::CDefinition](animlib/CNmFloatComparisonNode.CDefinition.md) | class | 32 | 5 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmFloatCurveEvent](animlib/CNmFloatCurveEvent.md) | class | 96 | 2 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmFloatCurveEventNode::CDefinition](animlib/CNmFloatCurveEventNode.CDefinition.md) | class | 40 | 4 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmFloatCurveNode::CDefinition](animlib/CNmFloatCurveNode.CDefinition.md) | class | 88 | 2 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmFloatEaseNode::CDefinition](animlib/CNmFloatEaseNode.CDefinition.md) | class | 32 | 5 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmFloatMathNode::CDefinition](animlib/CNmFloatMathNode.CDefinition.md) | class | 32 | 6 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmFloatRangeComparisonNode::CDefinition](animlib/CNmFloatRangeComparisonNode.CDefinition.md) | class | 32 | 3 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmFloatRemapNode::CDefinition](animlib/CNmFloatRemapNode.CDefinition.md) | class | 40 | 3 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmFloatRemapNode::RemapRange_t](animlib/CNmFloatRemapNode.RemapRange_t.md) | class | 8 | 2 |  |
| [CNmFloatSelectorNode::CDefinition](animlib/CNmFloatSelectorNode.CDefinition.md) | class | 88 | 5 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmFloatSpringNode::CDefinition](animlib/CNmFloatSpringNode.CDefinition.md) | class | 32 | 5 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmFloatSwitchNode::CDefinition](animlib/CNmFloatSwitchNode.CDefinition.md) | class | 32 | 5 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) | class | 16 | 0 | [CNmValueNode::CDefinition](animlib/CNmValueNode.CDefinition.md) |
| [CNmFollowBoneNode::CDefinition](animlib/CNmFollowBoneNode.CDefinition.md) | class | 48 | 4 | [CNmPassthroughNode::CDefinition](animlib/CNmPassthroughNode.CDefinition.md) |
| [CNmFollowBoneTask](animlib/CNmFollowBoneTask.md) | class | 144 | 0 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [CNmFootEvent](animlib/CNmFootEvent.md) | class | 32 | 1 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmFootEventConditionNode::CDefinition](animlib/CNmFootEventConditionNode.CDefinition.md) | class | 24 | 3 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmFootIKNode::CDefinition](animlib/CNmFootIKNode.CDefinition.md) | class | 56 | 8 | [CNmPassthroughNode::CDefinition](animlib/CNmPassthroughNode.CDefinition.md) |
| [CNmFootIKTask](animlib/CNmFootIKTask.md) | class | 320 | 12 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [CNmFootstepEventIDNode::CDefinition](animlib/CNmFootstepEventIDNode.CDefinition.md) | class | 24 | 2 | [CNmIDValueNode::CDefinition](animlib/CNmIDValueNode.CDefinition.md) |
| [CNmFootstepEventPercentageThroughNode::CDefinition](animlib/CNmFootstepEventPercentageThroughNode.CDefinition.md) | class | 24 | 3 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmFrameSnapEvent](animlib/CNmFrameSnapEvent.md) | class | 32 | 1 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmGraphDefinition](animlib/CNmGraphDefinition.md) | class | 440 | 14 |  |
| [CNmGraphDefinition::ExternalGraphSlot_t](animlib/CNmGraphDefinition.ExternalGraphSlot_t.md) | class | 16 | 2 |  |
| [CNmGraphDefinition::ExternalPoseSlot_t](animlib/CNmGraphDefinition.ExternalPoseSlot_t.md) | class | 16 | 2 |  |
| [CNmGraphDefinition::ReferencedGraphSlot_t](animlib/CNmGraphDefinition.ReferencedGraphSlot_t.md) | class | 4 | 2 |  |
| [CNmGraphEventConditionNode::CDefinition](animlib/CNmGraphEventConditionNode.CDefinition.md) | class | 128 | 3 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmGraphEventConditionNode::Condition_t](animlib/CNmGraphEventConditionNode.Condition_t.md) | class | 16 | 2 |  |
| [CNmGraphInstance](animlib/CNmGraphInstance.md) | class | 976 | 0 |  |
| [CNmGraphNode::CDefinition](animlib/CNmGraphNode.CDefinition.md) | class | 16 | 1 |  |
| [CNmGraphVariationUserData](animlib/CNmGraphVariationUserData.md) | class | 8 | 0 |  |
| [CNmIDBasedClipSelectorNode::CDefinition](animlib/CNmIDBasedClipSelectorNode.CDefinition.md) | class | 96 | 5 | [CNmClipReferenceNode::CDefinition](animlib/CNmClipReferenceNode.CDefinition.md) |
| [CNmIDBasedSelectorNode::CDefinition](animlib/CNmIDBasedSelectorNode.CDefinition.md) | class | 96 | 5 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmIDComparisonNode::CDefinition](animlib/CNmIDComparisonNode.CDefinition.md) | class | 64 | 3 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmIDEvent](animlib/CNmIDEvent.md) | class | 40 | 2 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmIDEventConditionNode::CDefinition](animlib/CNmIDEventConditionNode.CDefinition.md) | class | 88 | 3 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmIDEventNode::CDefinition](animlib/CNmIDEventNode.CDefinition.md) | class | 32 | 3 | [CNmIDValueNode::CDefinition](animlib/CNmIDValueNode.CDefinition.md) |
| [CNmIDEventPercentageThroughNode::CDefinition](animlib/CNmIDEventPercentageThroughNode.CDefinition.md) | class | 32 | 3 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmIDSelectorNode::CDefinition](animlib/CNmIDSelectorNode.CDefinition.md) | class | 96 | 3 | [CNmIDValueNode::CDefinition](animlib/CNmIDValueNode.CDefinition.md) |
| [CNmIDSwitchNode::CDefinition](animlib/CNmIDSwitchNode.CDefinition.md) | class | 40 | 5 | [CNmIDValueNode::CDefinition](animlib/CNmIDValueNode.CDefinition.md) |
| [CNmIDToFloatNode::CDefinition](animlib/CNmIDToFloatNode.CDefinition.md) | class | 104 | 4 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmIDValueNode::CDefinition](animlib/CNmIDValueNode.CDefinition.md) | class | 16 | 0 | [CNmValueNode::CDefinition](animlib/CNmValueNode.CDefinition.md) |
| [CNmIsExternalGraphSlotFilledNode::CDefinition](animlib/CNmIsExternalGraphSlotFilledNode.CDefinition.md) | class | 24 | 1 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmIsExternalPoseSetNode::CDefinition](animlib/CNmIsExternalPoseSetNode.CDefinition.md) | class | 24 | 1 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmIsInactiveBranchConditionNode::CDefinition](animlib/CNmIsInactiveBranchConditionNode.CDefinition.md) | class | 16 | 0 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmIsTargetSetNode::CDefinition](animlib/CNmIsTargetSetNode.CDefinition.md) | class | 24 | 1 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmLayerBlendNode::CDefinition](animlib/CNmLayerBlendNode.CDefinition.md) | class | 72 | 3 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmLayerBlendNode::LayerDefinition_t](animlib/CNmLayerBlendNode.LayerDefinition_t.md) | class | 12 | 8 |  |
| [CNmLegacyEvent](animlib/CNmLegacyEvent.md) | class | 80 | 2 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmMaterialAttributeEvent](animlib/CNmMaterialAttributeEvent.md) | class | 304 | 7 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmModelSpaceBlendTask](animlib/CNmModelSpaceBlendTask.md) | class | 256 | 0 | [CNmBlendTaskBase](animlib/CNmBlendTaskBase.md) |
| [CNmNotNode::CDefinition](animlib/CNmNotNode.CDefinition.md) | class | 24 | 1 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmOrNode::CDefinition](animlib/CNmOrNode.CDefinition.md) | class | 32 | 1 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmOrientationWarpEvent](animlib/CNmOrientationWarpEvent.md) | class | 24 | 0 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmOrientationWarpNode::CDefinition](animlib/CNmOrientationWarpNode.CDefinition.md) | class | 24 | 6 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmOverlayBlendTask](animlib/CNmOverlayBlendTask.md) | class | 256 | 0 | [CNmBlendTaskBase](animlib/CNmBlendTaskBase.md) |
| [CNmParameterizedBlendNode::BlendRange_t](animlib/CNmParameterizedBlendNode.BlendRange_t.md) | class | 12 | 3 |  |
| [CNmParameterizedBlendNode::CDefinition](animlib/CNmParameterizedBlendNode.CDefinition.md) | class | 48 | 3 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmParameterizedBlendNode::Parameterization_t](animlib/CNmParameterizedBlendNode.Parameterization_t.md) | class | 80 | 2 |  |
| [CNmParameterizedClipSelectorNode::CDefinition](animlib/CNmParameterizedClipSelectorNode.CDefinition.md) | class | 64 | 5 | [CNmClipReferenceNode::CDefinition](animlib/CNmClipReferenceNode.CDefinition.md) |
| [CNmParameterizedSelectorNode::CDefinition](animlib/CNmParameterizedSelectorNode.CDefinition.md) | class | 64 | 5 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmParticleEvent](animlib/CNmParticleEvent.md) | class | 112 | 14 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmPassthroughNode::CDefinition](animlib/CNmPassthroughNode.CDefinition.md) | class | 24 | 1 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) | class | 16 | 0 | [CNmGraphNode::CDefinition](animlib/CNmGraphNode.CDefinition.md) |
| [CNmPoseTask](animlib/CNmPoseTask.md) | class | 112 | 0 |  |
| [CNmReferencePoseNode::CDefinition](animlib/CNmReferencePoseNode.CDefinition.md) | class | 16 | 0 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmReferencePoseTask](animlib/CNmReferencePoseTask.md) | class | 112 | 0 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [CNmReferencedGraphNode::CDefinition](animlib/CNmReferencedGraphNode.CDefinition.md) | class | 24 | 2 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmRootMotionData](animlib/CNmRootMotionData.md) | class | 80 | 5 |  |
| [CNmRootMotionEvent](animlib/CNmRootMotionEvent.md) | class | 32 | 1 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmRootMotionOverrideNode::CDefinition](animlib/CNmRootMotionOverrideNode.CDefinition.md) | class | 48 | 8 | [CNmPassthroughNode::CDefinition](animlib/CNmPassthroughNode.CDefinition.md) |
| [CNmSampleTask](animlib/CNmSampleTask.md) | class | 128 | 0 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [CNmScaleNode::CDefinition](animlib/CNmScaleNode.CDefinition.md) | class | 32 | 2 | [CNmPassthroughNode::CDefinition](animlib/CNmPassthroughNode.CDefinition.md) |
| [CNmScaleTask](animlib/CNmScaleTask.md) | class | 208 | 0 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [CNmSelectorNode::CDefinition](animlib/CNmSelectorNode.CDefinition.md) | class | 64 | 2 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmSkeleton](animlib/CNmSkeleton.md) | class | 208 | 10 |  |
| [CNmSkeleton::SecondarySkeleton_t](animlib/CNmSkeleton.SecondarySkeleton_t.md) | class | 16 | 2 |  |
| [CNmSoundEvent](animlib/CNmSoundEvent.md) | class | 72 | 7 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmSpeedScaleBaseNode::CDefinition](animlib/CNmSpeedScaleBaseNode.CDefinition.md) | class | 32 | 2 | [CNmPassthroughNode::CDefinition](animlib/CNmPassthroughNode.CDefinition.md) |
| [CNmSpeedScaleNode::CDefinition](animlib/CNmSpeedScaleNode.CDefinition.md) | class | 32 | 0 | [CNmSpeedScaleBaseNode::CDefinition](animlib/CNmSpeedScaleBaseNode.CDefinition.md) |
| [CNmStateCompletedConditionNode::CDefinition](animlib/CNmStateCompletedConditionNode.CDefinition.md) | class | 24 | 3 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmStateMachineNode::CDefinition](animlib/CNmStateMachineNode.CDefinition.md) | class | 312 | 2 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmStateMachineNode::StateDefinition_t](animlib/CNmStateMachineNode.StateDefinition_t.md) | class | 56 | 3 |  |
| [CNmStateMachineNode::TransitionDefinition_t](animlib/CNmStateMachineNode.TransitionDefinition_t.md) | class | 8 | 4 |  |
| [CNmStateNode::CDefinition](animlib/CNmStateNode.CDefinition.md) | class | 176 | 11 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmStateNode::TimedEvent_t](animlib/CNmStateNode.TimedEvent_t.md) | class | 16 | 3 |  |
| [CNmSyncEventIndexConditionNode::CDefinition](animlib/CNmSyncEventIndexConditionNode.CDefinition.md) | class | 24 | 3 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmSyncTrack](animlib/CNmSyncTrack.md) | class | 176 | 2 |  |
| [CNmSyncTrack::EventMarker_t](animlib/CNmSyncTrack.EventMarker_t.md) | class | 16 | 2 |  |
| [CNmSyncTrack::Event_t](animlib/CNmSyncTrack.Event_t.md) | class | 16 | 3 |  |
| [CNmTarget](animlib/CNmTarget.md) | class | 48 | 6 |  |
| [CNmTargetInfoNode::CDefinition](animlib/CNmTargetInfoNode.CDefinition.md) | class | 32 | 3 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmTargetOffsetNode::CDefinition](animlib/CNmTargetOffsetNode.CDefinition.md) | class | 64 | 4 | [CNmTargetValueNode::CDefinition](animlib/CNmTargetValueNode.CDefinition.md) |
| [CNmTargetPointNode::CDefinition](animlib/CNmTargetPointNode.CDefinition.md) | class | 24 | 2 | [CNmVectorValueNode::CDefinition](animlib/CNmVectorValueNode.CDefinition.md) |
| [CNmTargetSelectorNode::CDefinition](animlib/CNmTargetSelectorNode.CDefinition.md) | class | 56 | 6 | [CNmClipReferenceNode::CDefinition](animlib/CNmClipReferenceNode.CDefinition.md) |
| [CNmTargetValueNode::CDefinition](animlib/CNmTargetValueNode.CDefinition.md) | class | 16 | 0 | [CNmValueNode::CDefinition](animlib/CNmValueNode.CDefinition.md) |
| [CNmTargetWarpEvent](animlib/CNmTargetWarpEvent.md) | class | 32 | 2 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmTargetWarpNode::CDefinition](animlib/CNmTargetWarpNode.CDefinition.md) | class | 56 | 11 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmTimeConditionNode::CDefinition](animlib/CNmTimeConditionNode.CDefinition.md) | class | 32 | 5 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmTransitionEvent](animlib/CNmTransitionEvent.md) | class | 40 | 2 | [CNmEvent](animlib/CNmEvent.md) |
| [CNmTransitionEventConditionNode::CDefinition](animlib/CNmTransitionEventConditionNode.CDefinition.md) | class | 32 | 4 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmTransitionNode::CDefinition](animlib/CNmTransitionNode.CDefinition.md) | class | 48 | 11 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmTwoBoneIKNode::CDefinition](animlib/CNmTwoBoneIKNode.CDefinition.md) | class | 48 | 7 | [CNmPassthroughNode::CDefinition](animlib/CNmPassthroughNode.CDefinition.md) |
| [CNmTwoBoneIKTask](animlib/CNmTwoBoneIKTask.md) | class | 240 | 10 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [CNmValueNode::CDefinition](animlib/CNmValueNode.CDefinition.md) | class | 16 | 0 | [CNmGraphNode::CDefinition](animlib/CNmGraphNode.CDefinition.md) |
| [CNmVectorCreateNode::CDefinition](animlib/CNmVectorCreateNode.CDefinition.md) | class | 24 | 4 | [CNmVectorValueNode::CDefinition](animlib/CNmVectorValueNode.CDefinition.md) |
| [CNmVectorInfoNode::CDefinition](animlib/CNmVectorInfoNode.CDefinition.md) | class | 24 | 2 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmVectorNegateNode::CDefinition](animlib/CNmVectorNegateNode.CDefinition.md) | class | 24 | 1 | [CNmVectorValueNode::CDefinition](animlib/CNmVectorValueNode.CDefinition.md) |
| [CNmVectorValueNode::CDefinition](animlib/CNmVectorValueNode.CDefinition.md) | class | 16 | 0 | [CNmValueNode::CDefinition](animlib/CNmValueNode.CDefinition.md) |
| [CNmVelocityBasedSpeedScaleNode::CDefinition](animlib/CNmVelocityBasedSpeedScaleNode.CDefinition.md) | class | 32 | 0 | [CNmSpeedScaleBaseNode::CDefinition](animlib/CNmSpeedScaleBaseNode.CDefinition.md) |
| [CNmVelocityBlendNode::CDefinition](animlib/CNmVelocityBlendNode.CDefinition.md) | class | 48 | 0 | [CNmParameterizedBlendNode::CDefinition](animlib/CNmParameterizedBlendNode.CDefinition.md) |
| [CNmVirtualParameterBoneMaskNode::CDefinition](animlib/CNmVirtualParameterBoneMaskNode.CDefinition.md) | class | 24 | 1 | [CNmBoneMaskValueNode::CDefinition](animlib/CNmBoneMaskValueNode.CDefinition.md) |
| [CNmVirtualParameterBoolNode::CDefinition](animlib/CNmVirtualParameterBoolNode.CDefinition.md) | class | 24 | 1 | [CNmBoolValueNode::CDefinition](animlib/CNmBoolValueNode.CDefinition.md) |
| [CNmVirtualParameterFloatNode::CDefinition](animlib/CNmVirtualParameterFloatNode.CDefinition.md) | class | 24 | 1 | [CNmFloatValueNode::CDefinition](animlib/CNmFloatValueNode.CDefinition.md) |
| [CNmVirtualParameterIDNode::CDefinition](animlib/CNmVirtualParameterIDNode.CDefinition.md) | class | 24 | 1 | [CNmIDValueNode::CDefinition](animlib/CNmIDValueNode.CDefinition.md) |
| [CNmVirtualParameterTargetNode::CDefinition](animlib/CNmVirtualParameterTargetNode.CDefinition.md) | class | 24 | 1 | [CNmTargetValueNode::CDefinition](animlib/CNmTargetValueNode.CDefinition.md) |
| [CNmVirtualParameterVectorNode::CDefinition](animlib/CNmVirtualParameterVectorNode.CDefinition.md) | class | 24 | 1 | [CNmVectorValueNode::CDefinition](animlib/CNmVectorValueNode.CDefinition.md) |
| [CNmZeroPoseNode::CDefinition](animlib/CNmZeroPoseNode.CDefinition.md) | class | 16 | 0 | [CNmPoseNode::CDefinition](animlib/CNmPoseNode.CDefinition.md) |
| [CNmZeroPoseTask](animlib/CNmZeroPoseTask.md) | class | 112 | 0 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [NmBoneMaskSetDefinition_t](animlib/NmBoneMaskSetDefinition_t.md) | class | 296 | 3 |  |
| [NmCompressionSettings_t](animlib/NmCompressionSettings_t.md) | class | 80 | 9 |  |
| [NmCompressionSettings_t::QuantizationRange_t](animlib/NmCompressionSettings_t.QuantizationRange_t.md) | class | 8 | 2 |  |
| [NmFloatCurveCompressionSettings_t](animlib/NmFloatCurveCompressionSettings_t.md) | class | 12 | 2 |  |
| [NmPercent_t](animlib/NmPercent_t.md) | class | 4 | 1 |  |
| [NmSyncTrackTimeRange_t](animlib/NmSyncTrackTimeRange_t.md) | class | 16 | 2 |  |
| [NmSyncTrackTime_t](animlib/NmSyncTrackTime_t.md) | class | 8 | 2 |  |
