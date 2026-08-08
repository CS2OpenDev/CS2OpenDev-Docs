---
layout: default
title: animgraphlib
parent: Schemas
nav_exclude: true
---

# Module: animgraphlib

[📊 View UML Diagram](../diagrams/animgraphlib.md)

243 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [AimCameraOpFixedSettings_t](animgraphlib/AimCameraOpFixedSettings_t.md) | class | 48 | 7 |  |
| [AimMatrixOpFixedSettings_t](animgraphlib/AimMatrixOpFixedSettings_t.md) | class | 240 | 13 |  |
| [BlendItem_t](animgraphlib/BlendItem_t.md) | class | 64 | 6 |  |
| [BoneDemoCaptureSettings_t](animgraphlib/BoneDemoCaptureSettings_t.md) | class | 32 | 7 |  |
| [CActionComponentUpdater](animgraphlib/CActionComponentUpdater.md) | class | 72 | 1 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CAddUpdateNode](animgraphlib/CAddUpdateNode.md) | class | 160 | 5 | [CBinaryUpdateNode](animgraphlib/CBinaryUpdateNode.md) |
| [CAimCameraUpdateNode](animgraphlib/CAimCameraUpdateNode.md) | class | 184 | 8 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CAimMatrixUpdateNode](animgraphlib/CAimMatrixUpdateNode.md) | class | 384 | 6 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CAnimActionUpdater](animgraphlib/CAnimActionUpdater.md) | class | 24 | 0 |  |
| [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) | class | 48 | 4 |  |
| [CAnimDemoCaptureSettings](animgraphlib/CAnimDemoCaptureSettings.md) | class | 128 | 15 |  |
| [CAnimGraphDebugReplay](animgraphlib/CAnimGraphDebugReplay.md) | class | 112 | 5 |  |
| [CAnimGraphModelBinding](animgraphlib/CAnimGraphModelBinding.md) | class | 40 | 2 |  |
| [CAnimGraphNetworkSettings](animgraphlib/CAnimGraphNetworkSettings.md) | class | 40 | 1 | [CAnimGraphSettingsGroup](animgraphlib/CAnimGraphSettingsGroup.md) |
| [CAnimGraphSettingsGroup](animgraphlib/CAnimGraphSettingsGroup.md) | class | 32 | 0 |  |
| [CAnimGraphSettingsManager](animgraphlib/CAnimGraphSettingsManager.md) | class | 48 | 1 |  |
| [CAnimInputDamping](animgraphlib/CAnimInputDamping.md) | class | 24 | 3 |  |
| [CAnimMotorUpdaterBase](animgraphlib/CAnimMotorUpdaterBase.md) | class | 32 | 2 |  |
| [CAnimNodePath](animgraphlib/CAnimNodePath.md) | class | 48 | 2 |  |
| [CAnimParamHandle](animgraphlib/CAnimParamHandle.md) | class | 2 | 2 |  |
| [CAnimParamHandleMap](animgraphlib/CAnimParamHandleMap.md) | class | 32 | 1 |  |
| [CAnimParameterBase](animgraphlib/CAnimParameterBase.md) | class | 112 | 7 |  |
| [CAnimParameterManagerUpdater](animgraphlib/CAnimParameterManagerUpdater.md) | class | 256 | 6 |  |
| [CAnimReplayFrame](animgraphlib/CAnimReplayFrame.md) | class | 144 | 5 |  |
| [CAnimScriptComponentUpdater](animgraphlib/CAnimScriptComponentUpdater.md) | class | 56 | 1 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CAnimScriptManager](animgraphlib/CAnimScriptManager.md) | class | 416 | 1 |  |
| [CAnimStateMachineUpdater](animgraphlib/CAnimStateMachineUpdater.md) | class | 88 | 3 |  |
| [CAnimTagBase](animgraphlib/CAnimTagBase.md) | class | 80 | 5 |  |
| [CAnimTagManagerUpdater](animgraphlib/CAnimTagManagerUpdater.md) | class | 120 | 1 |  |
| [CAnimUpdateNodeBase](animgraphlib/CAnimUpdateNodeBase.md) | class | 88 | 3 |  |
| [CAnimUpdateNodeRef](animgraphlib/CAnimUpdateNodeRef.md) | class | 16 | 1 |  |
| [CAnimUpdateSharedData](animgraphlib/CAnimUpdateSharedData.md) | class | 256 | 10 |  |
| [CAnimationGraphInstance](animgraphlib/CAnimationGraphInstance.md) | class | 832 | 1 |  |
| [CAnimationGraphVisualizerAxis](animgraphlib/CAnimationGraphVisualizerAxis.md) | class | 112 | 2 | [CAnimationGraphVisualizerPrimitiveBase](animgraphlib/CAnimationGraphVisualizerPrimitiveBase.md) |
| [CAnimationGraphVisualizerLine](animgraphlib/CAnimationGraphVisualizerLine.md) | class | 112 | 3 | [CAnimationGraphVisualizerPrimitiveBase](animgraphlib/CAnimationGraphVisualizerPrimitiveBase.md) |
| [CAnimationGraphVisualizerPie](animgraphlib/CAnimationGraphVisualizerPie.md) | class | 128 | 4 | [CAnimationGraphVisualizerPrimitiveBase](animgraphlib/CAnimationGraphVisualizerPrimitiveBase.md) |
| [CAnimationGraphVisualizerPrimitiveBase](animgraphlib/CAnimationGraphVisualizerPrimitiveBase.md) | class | 64 | 3 |  |
| [CAnimationGraphVisualizerSphere](animgraphlib/CAnimationGraphVisualizerSphere.md) | class | 96 | 3 | [CAnimationGraphVisualizerPrimitiveBase](animgraphlib/CAnimationGraphVisualizerPrimitiveBase.md) |
| [CAnimationGraphVisualizerText](animgraphlib/CAnimationGraphVisualizerText.md) | class | 96 | 3 | [CAnimationGraphVisualizerPrimitiveBase](animgraphlib/CAnimationGraphVisualizerPrimitiveBase.md) |
| [CAnimationLayer](animgraphlib/CAnimationLayer.md) | class | 76 | 11 |  |
| [CAudioAnimTag](animgraphlib/CAudioAnimTag.md) | class | 112 | 7 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CBinaryUpdateNode](animgraphlib/CBinaryUpdateNode.md) | class | 144 | 6 | [CAnimUpdateNodeBase](animgraphlib/CAnimUpdateNodeBase.md) |
| [CBindPoseUpdateNode](animgraphlib/CBindPoseUpdateNode.md) | class | 96 | 0 | [CLeafUpdateNode](animgraphlib/CLeafUpdateNode.md) |
| [CBlend2DInstanceData](animgraphlib/CBlend2DInstanceData.md) | class | 160 | 3 |  |
| [CBlend2DUpdateNode](animgraphlib/CBlend2DUpdateNode.md) | class | 248 | 15 | [CAnimUpdateNodeBase](animgraphlib/CAnimUpdateNodeBase.md) |
| [CBlendCurve](animgraphlib/CBlendCurve.md) | class | 8 | 2 |  |
| [CBlendNodeInstanceData](animgraphlib/CBlendNodeInstanceData.md) | class | 48 | 7 |  |
| [CBlendUpdateNode](animgraphlib/CBlendUpdateNode.md) | class | 224 | 13 | [CAnimUpdateNodeBase](animgraphlib/CAnimUpdateNodeBase.md) |
| [CBlockSelectionMetricEvaluator](animgraphlib/CBlockSelectionMetricEvaluator.md) | class | 80 | 0 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CBodyGroupAnimTag](animgraphlib/CBodyGroupAnimTag.md) | class | 120 | 2 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CBodyGroupSetting](animgraphlib/CBodyGroupSetting.md) | class | 16 | 2 |  |
| [CBoneMaskUpdateNode](animgraphlib/CBoneMaskUpdateNode.md) | class | 176 | 7 | [CBinaryUpdateNode](animgraphlib/CBinaryUpdateNode.md) |
| [CBonePositionMetricEvaluator](animgraphlib/CBonePositionMetricEvaluator.md) | class | 88 | 1 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CBoneVelocityMetricEvaluator](animgraphlib/CBoneVelocityMetricEvaluator.md) | class | 88 | 1 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CBoolAnimParameter](animgraphlib/CBoolAnimParameter.md) | class | 136 | 1 | [CConcreteAnimParameter](animgraphlib/CConcreteAnimParameter.md) |
| [CCPPScriptComponentUpdater](animgraphlib/CCPPScriptComponentUpdater.md) | class | 96 | 1 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CCachedPose](animgraphlib/CCachedPose.md) | class | 64 | 4 |  |
| [CChoiceInstanceData](animgraphlib/CChoiceInstanceData.md) | class | 52 | 4 |  |
| [CChoiceUpdateNode](animgraphlib/CChoiceUpdateNode.md) | class | 192 | 10 | [CAnimUpdateNodeBase](animgraphlib/CAnimUpdateNodeBase.md) |
| [CChoreoInstanceData](animgraphlib/CChoreoInstanceData.md) | class | 920 | 1 |  |
| [CChoreoUpdateNode](animgraphlib/CChoreoUpdateNode.md) | class | 120 | 0 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CClothSettingsAnimTag](animgraphlib/CClothSettingsAnimTag.md) | class | 112 | 4 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CConcreteAnimParameter](animgraphlib/CConcreteAnimParameter.md) | class | 128 | 6 | [CAnimParameterBase](animgraphlib/CAnimParameterBase.md) |
| [CCurrentRotationVelocityMetricEvaluator](animgraphlib/CCurrentRotationVelocityMetricEvaluator.md) | class | 80 | 0 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CCurrentVelocityMetricEvaluator](animgraphlib/CCurrentVelocityMetricEvaluator.md) | class | 80 | 0 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CCycleClipInstanceData](animgraphlib/CCycleClipInstanceData.md) | class | 28 | 2 |  |
| [CCycleControlClipUpdateNode](animgraphlib/CCycleControlClipUpdateNode.md) | class | 144 | 6 | [CLeafUpdateNode](animgraphlib/CLeafUpdateNode.md) |
| [CCycleControlUpdateNode](animgraphlib/CCycleControlUpdateNode.md) | class | 120 | 3 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CDampedPathAnimMotorUpdater](animgraphlib/CDampedPathAnimMotorUpdater.md) | class | 72 | 7 | [CPathAnimMotorUpdaterBase](animgraphlib/CPathAnimMotorUpdaterBase.md) |
| [CDampedValueComponentUpdater](animgraphlib/CDampedValueComponentUpdater.md) | class | 72 | 1 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CDampedValueUpdateItem](animgraphlib/CDampedValueUpdateItem.md) | class | 40 | 3 |  |
| [CDemoSettingsComponentUpdater](animgraphlib/CDemoSettingsComponentUpdater.md) | class | 176 | 1 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CDirectPlaybackInstanceData](animgraphlib/CDirectPlaybackInstanceData.md) | class | 328 | 12 |  |
| [CDirectPlaybackTagData](animgraphlib/CDirectPlaybackTagData.md) | class | 32 | 2 |  |
| [CDirectPlaybackUpdateNode](animgraphlib/CDirectPlaybackUpdateNode.md) | class | 144 | 3 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CDirectionalBlendInstanceData](animgraphlib/CDirectionalBlendInstanceData.md) | class | 80 | 7 |  |
| [CDirectionalBlendUpdateNode](animgraphlib/CDirectionalBlendUpdateNode.md) | class | 176 | 8 | [CLeafUpdateNode](animgraphlib/CLeafUpdateNode.md) |
| [CDistanceRemainingMetricEvaluator](animgraphlib/CDistanceRemainingMetricEvaluator.md) | class | 104 | 7 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CEditableMotionGraph](animgraphlib/CEditableMotionGraph.md) | class | 88 | 0 | [CMotionGraph](animgraphlib/CMotionGraph.md) |
| [CEmitTagActionUpdater](animgraphlib/CEmitTagActionUpdater.md) | class | 32 | 2 | [CAnimActionUpdater](animgraphlib/CAnimActionUpdater.md) |
| [CEnumAnimParameter](animgraphlib/CEnumAnimParameter.md) | class | 216 | 3 | [CConcreteAnimParameter](animgraphlib/CConcreteAnimParameter.md) |
| [CExpressionActionUpdater](animgraphlib/CExpressionActionUpdater.md) | class | 32 | 3 | [CAnimActionUpdater](animgraphlib/CAnimActionUpdater.md) |
| [CFloatAnimParameter](animgraphlib/CFloatAnimParameter.md) | class | 144 | 4 | [CConcreteAnimParameter](animgraphlib/CConcreteAnimParameter.md) |
| [CFollowAttachmentUpdateNode](animgraphlib/CFollowAttachmentUpdateNode.md) | class | 272 | 1 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CFollowPathInstanceData](animgraphlib/CFollowPathInstanceData.md) | class | 36 | 5 |  |
| [CFollowPathUpdateNode](animgraphlib/CFollowPathUpdateNode.md) | class | 184 | 13 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CFollowTargetUpdateNode](animgraphlib/CFollowTargetUpdateNode.md) | class | 144 | 3 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CFootAdjustmentInstanceData](animgraphlib/CFootAdjustmentInstanceData.md) | class | 72 | 3 |  |
| [CFootAdjustmentUpdateNode](animgraphlib/CFootAdjustmentUpdateNode.md) | class | 176 | 9 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CFootCycleMetricEvaluator](animgraphlib/CFootCycleMetricEvaluator.md) | class | 104 | 1 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CFootFallAnimTag](animgraphlib/CFootFallAnimTag.md) | class | 96 | 1 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CFootLockUpdateNode](animgraphlib/CFootLockUpdateNode.md) | class | 344 | 20 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CFootPinningUpdateNode](animgraphlib/CFootPinningUpdateNode.md) | class | 208 | 4 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CFootPositionMetricEvaluator](animgraphlib/CFootPositionMetricEvaluator.md) | class | 112 | 2 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CFootStepTriggerUpdateNode](animgraphlib/CFootStepTriggerUpdateNode.md) | class | 144 | 2 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CFootstepLandedAnimTag](animgraphlib/CFootstepLandedAnimTag.md) | class | 128 | 5 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CFutureFacingMetricEvaluator](animgraphlib/CFutureFacingMetricEvaluator.md) | class | 88 | 2 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CFutureVelocityMetricEvaluator](animgraphlib/CFutureVelocityMetricEvaluator.md) | class | 96 | 4 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CHandshakeAnimTagBase](animgraphlib/CHandshakeAnimTagBase.md) | class | 88 | 1 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CHitReactUpdateNode](animgraphlib/CHitReactUpdateNode.md) | class | 208 | 8 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CInputStreamUpdateNode](animgraphlib/CInputStreamUpdateNode.md) | class | 96 | 0 | [CLeafUpdateNode](animgraphlib/CLeafUpdateNode.md) |
| [CIntAnimParameter](animgraphlib/CIntAnimParameter.md) | class | 144 | 3 | [CConcreteAnimParameter](animgraphlib/CConcreteAnimParameter.md) |
| [CJiggleBoneUpdateNode](animgraphlib/CJiggleBoneUpdateNode.md) | class | 144 | 1 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CJumpHelperUpdateNode](animgraphlib/CJumpHelperUpdateNode.md) | class | 216 | 8 | [CSequenceUpdateNode](animgraphlib/CSequenceUpdateNode.md) |
| [CLODComponentUpdater](animgraphlib/CLODComponentUpdater.md) | class | 56 | 1 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CLeafUpdateNode](animgraphlib/CLeafUpdateNode.md) | class | 88 | 0 | [CAnimUpdateNodeBase](animgraphlib/CAnimUpdateNodeBase.md) |
| [CLeanMatrixInstanceData](animgraphlib/CLeanMatrixInstanceData.md) | class | 12 | 2 |  |
| [CLeanMatrixUpdateNode](animgraphlib/CLeanMatrixUpdateNode.md) | class | 240 | 10 | [CLeafUpdateNode](animgraphlib/CLeafUpdateNode.md) |
| [CLookAtUpdateNode](animgraphlib/CLookAtUpdateNode.md) | class | 352 | 6 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CLookComponentUpdater](animgraphlib/CLookComponentUpdater.md) | class | 72 | 9 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CMaterialAttributeAnimTag](animgraphlib/CMaterialAttributeAnimTag.md) | class | 112 | 4 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CMotionDataSet](animgraphlib/CMotionDataSet.md) | class | 32 | 2 |  |
| [CMotionGraph](animgraphlib/CMotionGraph.md) | class | 88 | 7 |  |
| [CMotionGraphConfig](animgraphlib/CMotionGraphConfig.md) | class | 32 | 5 |  |
| [CMotionGraphGroup](animgraphlib/CMotionGraphGroup.md) | class | 264 | 5 |  |
| [CMotionGraphUpdateNode](animgraphlib/CMotionGraphUpdateNode.md) | class | 104 | 1 | [CLeafUpdateNode](animgraphlib/CLeafUpdateNode.md) |
| [CMotionMatchingUpdateNode](animgraphlib/CMotionMatchingUpdateNode.md) | class | 328 | 23 | [CLeafUpdateNode](animgraphlib/CLeafUpdateNode.md) |
| [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) | class | 80 | 4 |  |
| [CMotionNode](animgraphlib/CMotionNode.md) | class | 40 | 2 |  |
| [CMotionNodeBlend1D](animgraphlib/CMotionNodeBlend1D.md) | class | 72 | 2 | [CMotionNode](animgraphlib/CMotionNode.md) |
| [CMotionNodeSequence](animgraphlib/CMotionNodeSequence.md) | class | 72 | 3 | [CMotionNode](animgraphlib/CMotionNode.md) |
| [CMotionSearchDB](animgraphlib/CMotionSearchDB.md) | class | 184 | 3 |  |
| [CMotionSearchNode](animgraphlib/CMotionSearchNode.md) | class | 128 | 5 |  |
| [CMovementComponentUpdater](animgraphlib/CMovementComponentUpdater.md) | class | 184 | 8 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CMovementHandshakeAnimTag](animgraphlib/CMovementHandshakeAnimTag.md) | class | 88 | 0 | [CHandshakeAnimTagBase](animgraphlib/CHandshakeAnimTagBase.md) |
| [CMoverInstanceData](animgraphlib/CMoverInstanceData.md) | class | 44 | 4 |  |
| [CMoverUpdateNode](animgraphlib/CMoverUpdateNode.md) | class | 176 | 12 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CNetworkedCycle](animgraphlib/CNetworkedCycle.md) | class | 52 | 5 |  |
| [COrientationWarpUpdateNode](animgraphlib/COrientationWarpUpdateNode.md) | class | 192 | 13 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CPairedSequenceComponentUpdater](animgraphlib/CPairedSequenceComponentUpdater.md) | class | 56 | 0 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CPairedSequenceUpdateNode](animgraphlib/CPairedSequenceUpdateNode.md) | class | 136 | 1 | [CSequenceUpdateNodeBase](animgraphlib/CSequenceUpdateNodeBase.md) |
| [CParamSpanUpdater](animgraphlib/CParamSpanUpdater.md) | class | 24 | 1 |  |
| [CParticleAnimTag](animgraphlib/CParticleAnimTag.md) | class | 152 | 11 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CPathAnimMotorUpdater](animgraphlib/CPathAnimMotorUpdater.md) | class | 40 | 0 | [CPathAnimMotorUpdaterBase](animgraphlib/CPathAnimMotorUpdaterBase.md) |
| [CPathAnimMotorUpdaterBase](animgraphlib/CPathAnimMotorUpdaterBase.md) | class | 40 | 1 | [CAnimMotorUpdaterBase](animgraphlib/CAnimMotorUpdaterBase.md) |
| [CPathHelperUpdateNode](animgraphlib/CPathHelperUpdateNode.md) | class | 120 | 2 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CPathMetricEvaluator](animgraphlib/CPathMetricEvaluator.md) | class | 120 | 4 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CPlayerInputAnimMotorUpdater](animgraphlib/CPlayerInputAnimMotorUpdater.md) | class | 80 | 6 | [CAnimMotorUpdaterBase](animgraphlib/CAnimMotorUpdaterBase.md) |
| [CPoseHandle](animgraphlib/CPoseHandle.md) | class | 4 | 2 |  |
| [CProductQuantizer](animgraphlib/CProductQuantizer.md) | class | 32 | 2 |  |
| [CQuaternionAnimParameter](animgraphlib/CQuaternionAnimParameter.md) | class | 160 | 2 | [CConcreteAnimParameter](animgraphlib/CConcreteAnimParameter.md) |
| [CRagdollAnimTag](animgraphlib/CRagdollAnimTag.md) | class | 96 | 1 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CRagdollComponentUpdater](animgraphlib/CRagdollComponentUpdater.md) | class | 216 | 10 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CRagdollUpdateNode](animgraphlib/CRagdollUpdateNode.md) | class | 120 | 2 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CRemapValueComponentUpdater](animgraphlib/CRemapValueComponentUpdater.md) | class | 72 | 1 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CRemapValueUpdateItem](animgraphlib/CRemapValueUpdateItem.md) | class | 20 | 6 |  |
| [CRootMotion](animgraphlib/CRootMotion.md) | class | 40 | 3 |  |
| [CRootUpdateNode](animgraphlib/CRootUpdateNode.md) | class | 112 | 0 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CSelectorUpdateNode](animgraphlib/CSelectorUpdateNode.md) | class | 184 | 10 | [CAnimUpdateNodeBase](animgraphlib/CAnimUpdateNodeBase.md) |
| [CSequenceFinishedAnimTag](animgraphlib/CSequenceFinishedAnimTag.md) | class | 96 | 1 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CSequenceTagSpans](animgraphlib/CSequenceTagSpans.md) | class | 32 | 2 |  |
| [CSequenceUpdateNode](animgraphlib/CSequenceUpdateNode.md) | class | 176 | 4 | [CSequenceUpdateNodeBase](animgraphlib/CSequenceUpdateNodeBase.md) |
| [CSequenceUpdateNodeBase](animgraphlib/CSequenceUpdateNodeBase.md) | class | 120 | 2 | [CLeafUpdateNode](animgraphlib/CLeafUpdateNode.md) |
| [CSetParameterActionUpdater](animgraphlib/CSetParameterActionUpdater.md) | class | 48 | 2 | [CAnimActionUpdater](animgraphlib/CAnimActionUpdater.md) |
| [CSingleFrameUpdateNode](animgraphlib/CSingleFrameUpdateNode.md) | class | 128 | 4 | [CLeafUpdateNode](animgraphlib/CLeafUpdateNode.md) |
| [CSlopeComponentUpdater](animgraphlib/CSlopeComponentUpdater.md) | class | 72 | 7 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CSlowDownOnSlopesUpdateNode](animgraphlib/CSlowDownOnSlopesUpdateNode.md) | class | 120 | 1 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CSolveIKChainUpdateNode](animgraphlib/CSolveIKChainUpdateNode.md) | class | 168 | 2 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CSolveIKTargetHandle_t](animgraphlib/CSolveIKTargetHandle_t.md) | class | 4 | 2 |  |
| [CSpeedScaleUpdateNode](animgraphlib/CSpeedScaleUpdateNode.md) | class | 120 | 1 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CStanceOverrideUpdateNode](animgraphlib/CStanceOverrideUpdateNode.md) | class | 160 | 4 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CStanceScaleUpdateNode](animgraphlib/CStanceScaleUpdateNode.md) | class | 120 | 1 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CStateActionUpdater](animgraphlib/CStateActionUpdater.md) | class | 16 | 2 |  |
| [CStateMachineComponentUpdater](animgraphlib/CStateMachineComponentUpdater.md) | class | 136 | 1 | [CAnimComponentUpdater](animgraphlib/CAnimComponentUpdater.md) |
| [CStateMachineInstanceData](animgraphlib/CStateMachineInstanceData.md) | class | 28 | 4 |  |
| [CStateMachineUpdateNode](animgraphlib/CStateMachineUpdateNode.md) | class | 256 | 6 | [CAnimUpdateNodeBase](animgraphlib/CAnimUpdateNodeBase.md) |
| [CStateNodeInstanceData](animgraphlib/CStateNodeInstanceData.md) | class | 76 | 4 |  |
| [CStateNodeStateData](animgraphlib/CStateNodeStateData.md) | class | 24 | 3 |  |
| [CStateNodeTransitionData](animgraphlib/CStateNodeTransitionData.md) | class | 28 | 5 |  |
| [CStateUpdateData](animgraphlib/CStateUpdateData.md) | class | 72 | 10 |  |
| [CStaticPoseCache](animgraphlib/CStaticPoseCache.md) | class | 48 | 3 |  |
| [CStaticPoseCacheBuilder](animgraphlib/CStaticPoseCacheBuilder.md) | class | 56 | 0 | [CStaticPoseCache](animgraphlib/CStaticPoseCache.md) |
| [CStepsRemainingMetricEvaluator](animgraphlib/CStepsRemainingMetricEvaluator.md) | class | 112 | 2 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CStopAtGoalUpdateNode](animgraphlib/CStopAtGoalUpdateNode.md) | class | 160 | 5 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CStringAnimTag](animgraphlib/CStringAnimTag.md) | class | 80 | 0 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CSubtractUpdateNode](animgraphlib/CSubtractUpdateNode.md) | class | 160 | 4 | [CBinaryUpdateNode](animgraphlib/CBinaryUpdateNode.md) |
| [CSymbolAnimParameter](animgraphlib/CSymbolAnimParameter.md) | class | 136 | 1 | [CConcreteAnimParameter](animgraphlib/CConcreteAnimParameter.md) |
| [CTargetSelectorUpdateNode](animgraphlib/CTargetSelectorUpdateNode.md) | class | 160 | 10 | [CAnimUpdateNodeBase](animgraphlib/CAnimUpdateNodeBase.md) |
| [CTargetWarpUpdateNode](animgraphlib/CTargetWarpUpdateNode.md) | class | 152 | 14 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CTaskHandshakeAnimTag](animgraphlib/CTaskHandshakeAnimTag.md) | class | 88 | 0 | [CHandshakeAnimTagBase](animgraphlib/CHandshakeAnimTagBase.md) |
| [CTaskStatusAnimTag](animgraphlib/CTaskStatusAnimTag.md) | class | 88 | 0 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CTimeRemainingMetricEvaluator](animgraphlib/CTimeRemainingMetricEvaluator.md) | class | 96 | 4 | [CMotionMetricEvaluator](animgraphlib/CMotionMetricEvaluator.md) |
| [CToggleComponentActionUpdater](animgraphlib/CToggleComponentActionUpdater.md) | class | 32 | 2 | [CAnimActionUpdater](animgraphlib/CAnimActionUpdater.md) |
| [CTransitionUpdateData](animgraphlib/CTransitionUpdateData.md) | class | 3 | 4 |  |
| [CTurnHelperInstanceData](animgraphlib/CTurnHelperInstanceData.md) | class | 12 | 3 |  |
| [CTurnHelperUpdateNode](animgraphlib/CTurnHelperUpdateNode.md) | class | 144 | 6 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CTwoBoneIKUpdateNode](animgraphlib/CTwoBoneIKUpdateNode.md) | class | 480 | 1 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) | class | 112 | 1 | [CAnimUpdateNodeBase](animgraphlib/CAnimUpdateNodeBase.md) |
| [CVectorAnimParameter](animgraphlib/CVectorAnimParameter.md) | class | 152 | 3 | [CConcreteAnimParameter](animgraphlib/CConcreteAnimParameter.md) |
| [CVectorQuantizer](animgraphlib/CVectorQuantizer.md) | class | 32 | 3 |  |
| [CVirtualAnimParameter](animgraphlib/CVirtualAnimParameter.md) | class | 128 | 2 | [CAnimParameterBase](animgraphlib/CAnimParameterBase.md) |
| [CWarpSectionAnimTag](animgraphlib/CWarpSectionAnimTag.md) | class | 88 | 2 | [CWarpSectionAnimTagBase](animgraphlib/CWarpSectionAnimTagBase.md) |
| [CWarpSectionAnimTagBase](animgraphlib/CWarpSectionAnimTagBase.md) | class | 80 | 0 | [CAnimTagBase](animgraphlib/CAnimTagBase.md) |
| [CWayPointHelperInstanceData](animgraphlib/CWayPointHelperInstanceData.md) | class | 40 | 4 |  |
| [CWayPointHelperUpdateNode](animgraphlib/CWayPointHelperUpdateNode.md) | class | 128 | 5 | [CUnaryUpdateNode](animgraphlib/CUnaryUpdateNode.md) |
| [CZeroPoseUpdateNode](animgraphlib/CZeroPoseUpdateNode.md) | class | 96 | 0 | [CLeafUpdateNode](animgraphlib/CLeafUpdateNode.md) |
| [ChainToSolveData_t](animgraphlib/ChainToSolveData_t.md) | class | 80 | 6 |  |
| [ConfigIndex](animgraphlib/ConfigIndex.md) | class | 4 | 2 |  |
| [DampedPathMotorInstanceData_t](animgraphlib/DampedPathMotorInstanceData_t.md) | class | 40 | 3 |  |
| [FollowAttachmentSettings_t](animgraphlib/FollowAttachmentSettings_t.md) | class | 144 | 5 |  |
| [FollowTargetOpFixedSettings_t](animgraphlib/FollowTargetOpFixedSettings_t.md) | class | 16 | 5 |  |
| [FootFixedData_t](animgraphlib/FootFixedData_t.md) | class | 80 | 11 |  |
| [FootFixedSettings](animgraphlib/FootFixedSettings.md) | class | 64 | 10 |  |
| [FootLockPoseOpFixedSettings](animgraphlib/FootLockPoseOpFixedSettings.md) | class | 104 | 18 |  |
| [FootPinningPoseOpFixedData_t](animgraphlib/FootPinningPoseOpFixedData_t.md) | class | 48 | 7 |  |
| [FootStepTrigger](animgraphlib/FootStepTrigger.md) | class | 32 | 3 |  |
| [HitReactFixedSettings_t](animgraphlib/HitReactFixedSettings_t.md) | class | 68 | 17 |  |
| [IAnimationGraphInstance](animgraphlib/IAnimationGraphInstance.md) | class | 24 | 0 |  |
| [IKBoneNameAndIndex_t](animgraphlib/IKBoneNameAndIndex_t.md) | class | 16 | 1 |  |
| [IKDemoCaptureSettings_t](animgraphlib/IKDemoCaptureSettings_t.md) | class | 40 | 5 |  |
| [IKSolverSettings_t](animgraphlib/IKSolverSettings_t.md) | class | 12 | 3 |  |
| [IKTargetSettings_t](animgraphlib/IKTargetSettings_t.md) | class | 40 | 5 |  |
| [JiggleBoneSettingsList_t](animgraphlib/JiggleBoneSettingsList_t.md) | class | 24 | 1 |  |
| [JiggleBoneSettings_t](animgraphlib/JiggleBoneSettings_t.md) | class | 44 | 7 |  |
| [LookAtBone_t](animgraphlib/LookAtBone_t.md) | class | 8 | 2 |  |
| [LookAtOpFixedSettings_t](animgraphlib/LookAtOpFixedSettings_t.md) | class | 208 | 11 |  |
| [LookData](animgraphlib/LookData.md) | class | 24 | 1 |  |
| [MotionBlendItem](animgraphlib/MotionBlendItem.md) | class | 16 | 2 |  |
| [MotionDBIndex](animgraphlib/MotionDBIndex.md) | class | 4 | 1 |  |
| [MotionIndex](animgraphlib/MotionIndex.md) | class | 4 | 2 |  |
| [MotionMatchingInstanceData](animgraphlib/MotionMatchingInstanceData.md) | class | 288 | 2 |  |
| [MotionSelection](animgraphlib/MotionSelection.md) | class | 88 | 5 |  |
| [MovementData](animgraphlib/MovementData.md) | class | 232 | 18 |  |
| [NetVarConfigIndex](animgraphlib/NetVarConfigIndex.md) | class | 12 | 1 |  |
| [PairedSequenceData](animgraphlib/PairedSequenceData.md) | class | 256 | 1 |  |
| [PairedSequence_t](animgraphlib/PairedSequence_t.md) | class | 32 | 3 |  |
| [ParamSpanSample_t](animgraphlib/ParamSpanSample_t.md) | class | 24 | 2 |  |
| [ParamSpan_t](animgraphlib/ParamSpan_t.md) | class | 40 | 5 |  |
| [PerTickSettings_t](animgraphlib/PerTickSettings_t.md) | class | 1728 | 12 |  |
| [PlayerInputMotorInstanceData_t](animgraphlib/PlayerInputMotorInstanceData_t.md) | class | 40 | 3 |  |
| [SampleCode](animgraphlib/SampleCode.md) | class | 8 | 1 |  |
| [ScriptInfo_t](animgraphlib/ScriptInfo_t.md) | class | 88 | 5 |  |
| [SelectorInstanceData_t](animgraphlib/SelectorInstanceData_t.md) | class | 44 | 4 |  |
| [SequenceData](animgraphlib/SequenceData.md) | class | 56 | 2 |  |
| [SlopeData](animgraphlib/SlopeData.md) | class | 12 | 1 |  |
| [SolveIKChainPoseOpFixedSettings_t](animgraphlib/SolveIKChainPoseOpFixedSettings_t.md) | class | 24 | 1 |  |
| [StanceInfo_t](animgraphlib/StanceInfo_t.md) | class | 16 | 2 |  |
| [TagSpan_t](animgraphlib/TagSpan_t.md) | class | 12 | 3 |  |
| [TagStatus](animgraphlib/TagStatus.md) | class | 8 | 2 |  |
| [TargetSelectorInstanceData_t](animgraphlib/TargetSelectorInstanceData_t.md) | class | 48 | 2 |  |
| [TraceSettings_t](animgraphlib/TraceSettings_t.md) | class | 8 | 2 |  |
| [TwoBoneIKSettings_t](animgraphlib/TwoBoneIKSettings_t.md) | class | 352 | 15 |  |
| [WeightList](animgraphlib/WeightList.md) | class | 32 | 2 |  |
