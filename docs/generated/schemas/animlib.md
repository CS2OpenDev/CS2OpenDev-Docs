---
layout: default
title: animlib
parent: Schemas
nav_exclude: true
---

# Module: animlib

[📊 View UML Diagram](../diagrams/animlib.md)

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [CNmAdditiveBlendTask](#cnmadditiveblendtask) | class | CNmBlendTaskBase | 0 |
| [CNmAndNode::CDefinition](#cnmandnodecdefinition) | class | CNmBoolValueNode::CDefinition | 1 |
| [CNmAnimationPoseNode::CDefinition](#cnmanimationposenodecdefinition) | class | CNmPoseNode::CDefinition | 5 |
| [CNmBitFlags](#cnmbitflags) | class |  | 1 |
| [CNmBlend1DNode::CDefinition](#cnmblend1dnodecdefinition) | class | CNmParameterizedBlendNode::CDefinition | 1 |
| [CNmBlend2DNode::CDefinition](#cnmblend2dnodecdefinition) | class | CNmPoseNode::CDefinition | 7 |
| [CNmBlendTask](#cnmblendtask) | class | CNmBlendTaskBase | 0 |
| [CNmBlendTaskBase](#cnmblendtaskbase) | class | CNmPoseTask | 0 |
| [CNmBodyGroupEvent](#cnmbodygroupevent) | class | CNmEvent | 3 |
| [CNmBoneMaskBlendNode::CDefinition](#cnmbonemaskblendnodecdefinition) | class | CNmBoneMaskValueNode::CDefinition | 3 |
| [CNmBoneMaskNode::CDefinition](#cnmbonemasknodecdefinition) | class | CNmBoneMaskValueNode::CDefinition | 1 |
| [CNmBoneMaskSelectorNode::CDefinition](#cnmbonemaskselectornodecdefinition) | class | CNmBoneMaskValueNode::CDefinition | 6 |
| [CNmBoneMaskSwitchNode::CDefinition](#cnmbonemaskswitchnodecdefinition) | class | CNmBoneMaskValueNode::CDefinition | 5 |
| [CNmBoneMaskValueNode::CDefinition](#cnmbonemaskvaluenodecdefinition) | class | CNmValueNode::CDefinition | 0 |
| [CNmBoneWeightList](#cnmboneweightlist) | class |  | 3 |
| [CNmBoolValueNode::CDefinition](#cnmboolvaluenodecdefinition) | class | CNmValueNode::CDefinition | 0 |
| [CNmCachedBoolNode::CDefinition](#cnmcachedboolnodecdefinition) | class | CNmBoolValueNode::CDefinition | 2 |
| [CNmCachedFloatNode::CDefinition](#cnmcachedfloatnodecdefinition) | class | CNmFloatValueNode::CDefinition | 2 |
| [CNmCachedIDNode::CDefinition](#cnmcachedidnodecdefinition) | class | CNmIDValueNode::CDefinition | 2 |
| [CNmCachedPoseReadTask](#cnmcachedposereadtask) | class | CNmPoseTask | 0 |
| [CNmCachedPoseWriteTask](#cnmcachedposewritetask) | class | CNmPoseTask | 0 |
| [CNmCachedTargetNode::CDefinition](#cnmcachedtargetnodecdefinition) | class | CNmTargetValueNode::CDefinition | 2 |
| [CNmCachedVectorNode::CDefinition](#cnmcachedvectornodecdefinition) | class | CNmVectorValueNode::CDefinition | 2 |
| [CNmChainLookatNode::CDefinition](#cnmchainlookatnodecdefinition) | class | CNmPassthroughNode::CDefinition | 7 |
| [CNmChainLookatTask](#cnmchainlookattask) | class | CNmPoseTask | 11 |
| [CNmClip](#cnmclip) | class |  | 16 |
| [CNmClip::ModelSpaceSamplingChainLink_t](#cnmclipmodelspacesamplingchainlink_t) | class |  | 3 |
| [CNmClipNode::CDefinition](#cnmclipnodecdefinition) | class | CNmClipReferenceNode::CDefinition | 8 |
| [CNmClipReferenceNode::CDefinition](#cnmclipreferencenodecdefinition) | class | CNmPoseNode::CDefinition | 0 |
| [CNmClipSelectorNode::CDefinition](#cnmclipselectornodecdefinition) | class | CNmClipReferenceNode::CDefinition | 2 |
| [CNmConstBoolNode::CDefinition](#cnmconstboolnodecdefinition) | class | CNmBoolValueNode::CDefinition | 1 |
| [CNmConstFloatNode::CDefinition](#cnmconstfloatnodecdefinition) | class | CNmFloatValueNode::CDefinition | 1 |
| [CNmConstIDNode::CDefinition](#cnmconstidnodecdefinition) | class | CNmIDValueNode::CDefinition | 1 |
| [CNmConstTargetNode::CDefinition](#cnmconsttargetnodecdefinition) | class | CNmTargetValueNode::CDefinition | 1 |
| [CNmConstVectorNode::CDefinition](#cnmconstvectornodecdefinition) | class | CNmVectorValueNode::CDefinition | 1 |
| [CNmControlParameterBoolNode::CDefinition](#cnmcontrolparameterboolnodecdefinition) | class | CNmBoolValueNode::CDefinition | 0 |
| [CNmControlParameterFloatNode::CDefinition](#cnmcontrolparameterfloatnodecdefinition) | class | CNmFloatValueNode::CDefinition | 0 |
| [CNmControlParameterIDNode::CDefinition](#cnmcontrolparameteridnodecdefinition) | class | CNmIDValueNode::CDefinition | 0 |
| [CNmControlParameterTargetNode::CDefinition](#cnmcontrolparametertargetnodecdefinition) | class | CNmTargetValueNode::CDefinition | 0 |
| [CNmControlParameterVectorNode::CDefinition](#cnmcontrolparametervectornodecdefinition) | class | CNmVectorValueNode::CDefinition | 0 |
| [CNmCurrentSyncEventIDNode::CDefinition](#cnmcurrentsynceventidnodecdefinition) | class | CNmIDValueNode::CDefinition | 1 |
| [CNmCurrentSyncEventNode::CDefinition](#cnmcurrentsynceventnodecdefinition) | class | CNmFloatValueNode::CDefinition | 2 |
| [CNmCurrentSyncEventNode::InfoType_t](#cnmcurrentsynceventnodeinfotype_t) | enum |  | 3 |
| [CNmDurationScaleNode::CDefinition](#cnmdurationscalenodecdefinition) | class | CNmSpeedScaleBaseNode::CDefinition | 0 |
| [CNmEntityAttributeEventBase](#cnmentityattributeeventbase) | class | CNmEvent | 2 |
| [CNmEntityAttributeFloatEvent](#cnmentityattributefloatevent) | class | CNmEntityAttributeEventBase | 1 |
| [CNmEntityAttributeIntEvent](#cnmentityattributeintevent) | class | CNmEntityAttributeEventBase | 1 |
| [CNmEvent](#cnmevent) | class |  | 3 |
| [CNmEventRelevance_t](#cnmeventrelevance_t) | enum |  | 3 |
| [CNmEventTargetEntity_t](#cnmeventtargetentity_t) | enum |  | 4 |
| [CNmExternalPoseNode::CDefinition](#cnmexternalposenodecdefinition) | class | CNmPoseNode::CDefinition | 1 |
| [CNmFixedWeightBoneMaskNode::CDefinition](#cnmfixedweightbonemasknodecdefinition) | class | CNmBoneMaskValueNode::CDefinition | 1 |
| [CNmFloatAngleMathNode::CDefinition](#cnmfloatanglemathnodecdefinition) | class | CNmFloatValueNode::CDefinition | 2 |
| [CNmFloatAngleMathNode::Operation_t](#cnmfloatanglemathnodeoperation_t) | enum |  | 4 |
| [CNmFloatClampNode::CDefinition](#cnmfloatclampnodecdefinition) | class | CNmFloatValueNode::CDefinition | 2 |
| [CNmFloatComparisonNode::CDefinition](#cnmfloatcomparisonnodecdefinition) | class | CNmBoolValueNode::CDefinition | 5 |
| [CNmFloatComparisonNode::Comparison_t](#cnmfloatcomparisonnodecomparison_t) | enum |  | 5 |
| [CNmFloatCurveEvent](#cnmfloatcurveevent) | class | CNmEvent | 2 |
| [CNmFloatCurveEventNode::CDefinition](#cnmfloatcurveeventnodecdefinition) | class | CNmFloatValueNode::CDefinition | 4 |
| [CNmFloatCurveNode::CDefinition](#cnmfloatcurvenodecdefinition) | class | CNmFloatValueNode::CDefinition | 2 |
| [CNmFloatEaseNode::CDefinition](#cnmfloateasenodecdefinition) | class | CNmFloatValueNode::CDefinition | 5 |
| [CNmFloatMathNode::CDefinition](#cnmfloatmathnodecdefinition) | class | CNmFloatValueNode::CDefinition | 6 |
| [CNmFloatMathNode::Operator_t](#cnmfloatmathnodeoperator_t) | enum |  | 12 |
| [CNmFloatRangeComparisonNode::CDefinition](#cnmfloatrangecomparisonnodecdefinition) | class | CNmBoolValueNode::CDefinition | 3 |
| [CNmFloatRemapNode::CDefinition](#cnmfloatremapnodecdefinition) | class | CNmFloatValueNode::CDefinition | 3 |
| [CNmFloatRemapNode::RemapRange_t](#cnmfloatremapnoderemaprange_t) | class |  | 2 |
| [CNmFloatSelectorNode::CDefinition](#cnmfloatselectornodecdefinition) | class | CNmFloatValueNode::CDefinition | 5 |
| [CNmFloatSpringNode::CDefinition](#cnmfloatspringnodecdefinition) | class | CNmFloatValueNode::CDefinition | 5 |
| [CNmFloatSwitchNode::CDefinition](#cnmfloatswitchnodecdefinition) | class | CNmFloatValueNode::CDefinition | 5 |
| [CNmFloatValueNode::CDefinition](#cnmfloatvaluenodecdefinition) | class | CNmValueNode::CDefinition | 0 |
| [CNmFollowBoneNode::CDefinition](#cnmfollowbonenodecdefinition) | class | CNmPassthroughNode::CDefinition | 4 |
| [CNmFollowBoneTask](#cnmfollowbonetask) | class | CNmPoseTask | 0 |
| [CNmFootEvent](#cnmfootevent) | class | CNmEvent | 1 |
| [CNmFootEventConditionNode::CDefinition](#cnmfooteventconditionnodecdefinition) | class | CNmBoolValueNode::CDefinition | 3 |
| [CNmFootIKNode::CDefinition](#cnmfootiknodecdefinition) | class | CNmPassthroughNode::CDefinition | 8 |
| [CNmFootIKTask](#cnmfootiktask) | class | CNmPoseTask | 12 |
| [CNmFootstepEventIDNode::CDefinition](#cnmfootstepeventidnodecdefinition) | class | CNmIDValueNode::CDefinition | 2 |
| [CNmFootstepEventPercentageThroughNode::CDefinition](#cnmfootstepeventpercentagethroughnodecdefinition) | class | CNmFloatValueNode::CDefinition | 3 |
| [CNmFrameSnapEvent](#cnmframesnapevent) | class | CNmEvent | 1 |
| [CNmGraphDefinition](#cnmgraphdefinition) | class |  | 14 |
| [CNmGraphDefinition::ExternalGraphSlot_t](#cnmgraphdefinitionexternalgraphslot_t) | class |  | 2 |
| [CNmGraphDefinition::ExternalPoseSlot_t](#cnmgraphdefinitionexternalposeslot_t) | class |  | 2 |
| [CNmGraphDefinition::ReferencedGraphSlot_t](#cnmgraphdefinitionreferencedgraphslot_t) | class |  | 2 |
| [CNmGraphEventConditionNode::CDefinition](#cnmgrapheventconditionnodecdefinition) | class | CNmBoolValueNode::CDefinition | 3 |
| [CNmGraphEventConditionNode::Condition_t](#cnmgrapheventconditionnodecondition_t) | class |  | 2 |
| [CNmGraphInstance](#cnmgraphinstance) | class |  | 0 |
| [CNmGraphNode::CDefinition](#cnmgraphnodecdefinition) | class |  | 1 |
| [CNmGraphVariationUserData](#cnmgraphvariationuserdata) | class |  | 0 |
| [CNmIDBasedClipSelectorNode::CDefinition](#cnmidbasedclipselectornodecdefinition) | class | CNmClipReferenceNode::CDefinition | 5 |
| [CNmIDBasedSelectorNode::CDefinition](#cnmidbasedselectornodecdefinition) | class | CNmPoseNode::CDefinition | 5 |
| [CNmIDComparisonNode::CDefinition](#cnmidcomparisonnodecdefinition) | class | CNmBoolValueNode::CDefinition | 3 |
| [CNmIDComparisonNode::Comparison_t](#cnmidcomparisonnodecomparison_t) | enum |  | 2 |
| [CNmIDEvent](#cnmidevent) | class | CNmEvent | 2 |
| [CNmIDEventConditionNode::CDefinition](#cnmideventconditionnodecdefinition) | class | CNmBoolValueNode::CDefinition | 3 |
| [CNmIDEventNode::CDefinition](#cnmideventnodecdefinition) | class | CNmIDValueNode::CDefinition | 3 |
| [CNmIDEventPercentageThroughNode::CDefinition](#cnmideventpercentagethroughnodecdefinition) | class | CNmBoolValueNode::CDefinition | 3 |
| [CNmIDSelectorNode::CDefinition](#cnmidselectornodecdefinition) | class | CNmIDValueNode::CDefinition | 3 |
| [CNmIDSwitchNode::CDefinition](#cnmidswitchnodecdefinition) | class | CNmIDValueNode::CDefinition | 5 |
| [CNmIDToFloatNode::CDefinition](#cnmidtofloatnodecdefinition) | class | CNmFloatValueNode::CDefinition | 4 |
| [CNmIDValueNode::CDefinition](#cnmidvaluenodecdefinition) | class | CNmValueNode::CDefinition | 0 |
| [CNmIsExternalGraphSlotFilledNode::CDefinition](#cnmisexternalgraphslotfillednodecdefinition) | class | CNmBoolValueNode::CDefinition | 1 |
| [CNmIsExternalPoseSetNode::CDefinition](#cnmisexternalposesetnodecdefinition) | class | CNmBoolValueNode::CDefinition | 1 |
| [CNmIsInactiveBranchConditionNode::CDefinition](#cnmisinactivebranchconditionnodecdefinition) | class | CNmBoolValueNode::CDefinition | 0 |
| [CNmIsTargetSetNode::CDefinition](#cnmistargetsetnodecdefinition) | class | CNmBoolValueNode::CDefinition | 1 |
| [CNmLayerBlendNode::CDefinition](#cnmlayerblendnodecdefinition) | class | CNmPoseNode::CDefinition | 3 |
| [CNmLayerBlendNode::LayerDefinition_t](#cnmlayerblendnodelayerdefinition_t) | class |  | 8 |
| [CNmLegacyEvent](#cnmlegacyevent) | class | CNmEvent | 2 |
| [CNmMaterialAttributeEvent](#cnmmaterialattributeevent) | class | CNmEvent | 7 |
| [CNmModelSpaceBlendTask](#cnmmodelspaceblendtask) | class | CNmBlendTaskBase | 0 |
| [CNmNotNode::CDefinition](#cnmnotnodecdefinition) | class | CNmBoolValueNode::CDefinition | 1 |
| [CNmOrNode::CDefinition](#cnmornodecdefinition) | class | CNmBoolValueNode::CDefinition | 1 |
| [CNmOrientationWarpEvent](#cnmorientationwarpevent) | class | CNmEvent | 0 |
| [CNmOrientationWarpNode::CDefinition](#cnmorientationwarpnodecdefinition) | class | CNmPoseNode::CDefinition | 6 |
| [CNmOverlayBlendTask](#cnmoverlayblendtask) | class | CNmBlendTaskBase | 0 |
| [CNmParameterizedBlendNode::BlendRange_t](#cnmparameterizedblendnodeblendrange_t) | class |  | 3 |
| [CNmParameterizedBlendNode::CDefinition](#cnmparameterizedblendnodecdefinition) | class | CNmPoseNode::CDefinition | 3 |
| [CNmParameterizedBlendNode::Parameterization_t](#cnmparameterizedblendnodeparameterization_t) | class |  | 2 |
| [CNmParameterizedClipSelectorNode::CDefinition](#cnmparameterizedclipselectornodecdefinition) | class | CNmClipReferenceNode::CDefinition | 5 |
| [CNmParameterizedSelectorNode::CDefinition](#cnmparameterizedselectornodecdefinition) | class | CNmPoseNode::CDefinition | 5 |
| [CNmParticleEvent](#cnmparticleevent) | class | CNmEvent | 14 |
| [CNmParticleEvent::Type_t](#cnmparticleeventtype_t) | enum |  | 2 |
| [CNmPassthroughNode::CDefinition](#cnmpassthroughnodecdefinition) | class | CNmPoseNode::CDefinition | 1 |
| [CNmPoseNode::CDefinition](#cnmposenodecdefinition) | class | CNmGraphNode::CDefinition | 0 |
| [CNmPoseTask](#cnmposetask) | class |  | 0 |
| [CNmReferencePoseNode::CDefinition](#cnmreferenceposenodecdefinition) | class | CNmPoseNode::CDefinition | 0 |
| [CNmReferencePoseTask](#cnmreferenceposetask) | class | CNmPoseTask | 0 |
| [CNmReferencedGraphNode::CDefinition](#cnmreferencedgraphnodecdefinition) | class | CNmPoseNode::CDefinition | 2 |
| [CNmRootMotionData](#cnmrootmotiondata) | class |  | 5 |
| [CNmRootMotionData::SamplingMode_t](#cnmrootmotiondatasamplingmode_t) | enum |  | 2 |
| [CNmRootMotionEvent](#cnmrootmotionevent) | class | CNmEvent | 1 |
| [CNmRootMotionOverrideNode::CDefinition](#cnmrootmotionoverridenodecdefinition) | class | CNmPassthroughNode::CDefinition | 7 |
| [CNmRootMotionOverrideNode::OverrideFlags_t](#cnmrootmotionoverridenodeoverrideflags_t) | enum |  | 5 |
| [CNmSampleTask](#cnmsampletask) | class | CNmPoseTask | 0 |
| [CNmScaleNode::CDefinition](#cnmscalenodecdefinition) | class | CNmPassthroughNode::CDefinition | 2 |
| [CNmScaleTask](#cnmscaletask) | class | CNmPoseTask | 0 |
| [CNmSelectorNode::CDefinition](#cnmselectornodecdefinition) | class | CNmPoseNode::CDefinition | 2 |
| [CNmSkeleton](#cnmskeleton) | class |  | 9 |
| [CNmSkeleton::SecondarySkeleton_t](#cnmskeletonsecondaryskeleton_t) | class |  | 2 |
| [CNmSoundEvent](#cnmsoundevent) | class | CNmEvent | 7 |
| [CNmSoundEvent::Position_t](#cnmsoundeventposition_t) | enum |  | 5 |
| [CNmSpeedScaleBaseNode::CDefinition](#cnmspeedscalebasenodecdefinition) | class | CNmPassthroughNode::CDefinition | 2 |
| [CNmSpeedScaleNode::CDefinition](#cnmspeedscalenodecdefinition) | class | CNmSpeedScaleBaseNode::CDefinition | 0 |
| [CNmStateCompletedConditionNode::CDefinition](#cnmstatecompletedconditionnodecdefinition) | class | CNmBoolValueNode::CDefinition | 3 |
| [CNmStateMachineNode::CDefinition](#cnmstatemachinenodecdefinition) | class | CNmPoseNode::CDefinition | 2 |
| [CNmStateMachineNode::StateDefinition_t](#cnmstatemachinenodestatedefinition_t) | class |  | 3 |
| [CNmStateMachineNode::TransitionDefinition_t](#cnmstatemachinenodetransitiondefinition_t) | class |  | 4 |
| [CNmStateNode::CDefinition](#cnmstatenodecdefinition) | class | CNmPoseNode::CDefinition | 11 |
| [CNmStateNode::TimedEvent_t](#cnmstatenodetimedevent_t) | class |  | 3 |
| [CNmStateNode::TimedEvent_t::Comparison_t](#cnmstatenodetimedevent_tcomparison_t) | enum |  | 2 |
| [CNmSyncEventIndexConditionNode::CDefinition](#cnmsynceventindexconditionnodecdefinition) | class | CNmBoolValueNode::CDefinition | 3 |
| [CNmSyncEventIndexConditionNode::TriggerMode_t](#cnmsynceventindexconditionnodetriggermode_t) | enum |  | 2 |
| [CNmSyncTrack](#cnmsynctrack) | class |  | 2 |
| [CNmSyncTrack::EventMarker_t](#cnmsynctrackeventmarker_t) | class |  | 2 |
| [CNmSyncTrack::Event_t](#cnmsynctrackevent_t) | class |  | 3 |
| [CNmTarget](#cnmtarget) | class |  | 6 |
| [CNmTargetInfoNode::CDefinition](#cnmtargetinfonodecdefinition) | class | CNmFloatValueNode::CDefinition | 3 |
| [CNmTargetInfoNode::Info_t](#cnmtargetinfonodeinfo_t) | enum |  | 8 |
| [CNmTargetOffsetNode::CDefinition](#cnmtargetoffsetnodecdefinition) | class | CNmTargetValueNode::CDefinition | 4 |
| [CNmTargetPointNode::CDefinition](#cnmtargetpointnodecdefinition) | class | CNmVectorValueNode::CDefinition | 2 |
| [CNmTargetSelectorNode::CDefinition](#cnmtargetselectornodecdefinition) | class | CNmClipReferenceNode::CDefinition | 6 |
| [CNmTargetValueNode::CDefinition](#cnmtargetvaluenodecdefinition) | class | CNmValueNode::CDefinition | 0 |
| [CNmTargetWarpEvent](#cnmtargetwarpevent) | class | CNmEvent | 2 |
| [CNmTargetWarpNode::CDefinition](#cnmtargetwarpnodecdefinition) | class | CNmPoseNode::CDefinition | 11 |
| [CNmTargetWarpNode::TargetUpdateRule_t](#cnmtargetwarpnodetargetupdaterule_t) | enum |  | 4 |
| [CNmTimeConditionNode::CDefinition](#cnmtimeconditionnodecdefinition) | class | CNmBoolValueNode::CDefinition | 5 |
| [CNmTimeConditionNode::ComparisonType_t](#cnmtimeconditionnodecomparisontype_t) | enum |  | 3 |
| [CNmTimeConditionNode::Operator_t](#cnmtimeconditionnodeoperator_t) | enum |  | 4 |
| [CNmTransitionEvent](#cnmtransitionevent) | class | CNmEvent | 2 |
| [CNmTransitionEventConditionNode::CDefinition](#cnmtransitioneventconditionnodecdefinition) | class | CNmBoolValueNode::CDefinition | 4 |
| [CNmTransitionNode::CDefinition](#cnmtransitionnodecdefinition) | class | CNmPoseNode::CDefinition | 11 |
| [CNmTransitionNode::TransitionOptions_t](#cnmtransitionnodetransitionoptions_t) | enum |  | 10 |
| [CNmTwoBoneIKNode::CDefinition](#cnmtwoboneiknodecdefinition) | class | CNmPassthroughNode::CDefinition | 7 |
| [CNmTwoBoneIKTask](#cnmtwoboneiktask) | class | CNmPoseTask | 10 |
| [CNmValueNode::CDefinition](#cnmvaluenodecdefinition) | class | CNmGraphNode::CDefinition | 0 |
| [CNmVectorCreateNode::CDefinition](#cnmvectorcreatenodecdefinition) | class | CNmVectorValueNode::CDefinition | 4 |
| [CNmVectorInfoNode::CDefinition](#cnmvectorinfonodecdefinition) | class | CNmFloatValueNode::CDefinition | 2 |
| [CNmVectorInfoNode::Info_t](#cnmvectorinfonodeinfo_t) | enum |  | 6 |
| [CNmVectorNegateNode::CDefinition](#cnmvectornegatenodecdefinition) | class | CNmVectorValueNode::CDefinition | 1 |
| [CNmVectorValueNode::CDefinition](#cnmvectorvaluenodecdefinition) | class | CNmValueNode::CDefinition | 0 |
| [CNmVelocityBasedSpeedScaleNode::CDefinition](#cnmvelocitybasedspeedscalenodecdefinition) | class | CNmSpeedScaleBaseNode::CDefinition | 0 |
| [CNmVelocityBlendNode::CDefinition](#cnmvelocityblendnodecdefinition) | class | CNmParameterizedBlendNode::CDefinition | 0 |
| [CNmVirtualParameterBoneMaskNode::CDefinition](#cnmvirtualparameterbonemasknodecdefinition) | class | CNmBoneMaskValueNode::CDefinition | 1 |
| [CNmVirtualParameterBoolNode::CDefinition](#cnmvirtualparameterboolnodecdefinition) | class | CNmBoolValueNode::CDefinition | 1 |
| [CNmVirtualParameterFloatNode::CDefinition](#cnmvirtualparameterfloatnodecdefinition) | class | CNmFloatValueNode::CDefinition | 1 |
| [CNmVirtualParameterIDNode::CDefinition](#cnmvirtualparameteridnodecdefinition) | class | CNmIDValueNode::CDefinition | 1 |
| [CNmVirtualParameterTargetNode::CDefinition](#cnmvirtualparametertargetnodecdefinition) | class | CNmTargetValueNode::CDefinition | 1 |
| [CNmVirtualParameterVectorNode::CDefinition](#cnmvirtualparametervectornodecdefinition) | class | CNmVectorValueNode::CDefinition | 1 |
| [CNmZeroPoseNode::CDefinition](#cnmzeroposenodecdefinition) | class | CNmPoseNode::CDefinition | 0 |
| [CNmZeroPoseTask](#cnmzeroposetask) | class | CNmPoseTask | 0 |
| [NmBoneMaskSetDefinition_t](#nmbonemasksetdefinition_t) | class |  | 3 |
| [NmCachedValueMode_t](#nmcachedvaluemode_t) | enum |  | 2 |
| [NmCompressionSettings_t](#nmcompressionsettings_t) | class |  | 9 |
| [NmCompressionSettings_t::QuantizationRange_t](#nmcompressionsettings_tquantizationrange_t) | class |  | 2 |
| [NmEasingFunction_t](#nmeasingfunction_t) | enum |  | 9 |
| [NmEasingOperation_t](#nmeasingoperation_t) | enum |  | 23 |
| [NmEventConditionRules_t](#nmeventconditionrules_t) | enum |  | 9 |
| [NmFloatCurveCompressionSettings_t](#nmfloatcurvecompressionsettings_t) | class |  | 2 |
| [NmFollowBoneMode_t](#nmfollowbonemode_t) | enum |  | 3 |
| [NmFootPhaseCondition_t](#nmfootphasecondition_t) | enum |  | 7 |
| [NmFootPhase_t](#nmfootphase_t) | enum |  | 5 |
| [NmFrameSnapEventMode_t](#nmframesnapeventmode_t) | enum |  | 2 |
| [NmGraphDebugMode_t](#nmgraphdebugmode_t) | enum |  | 2 |
| [NmGraphEventTypeCondition_t](#nmgrapheventtypecondition_t) | enum |  | 6 |
| [NmGraphValueType_t](#nmgraphvaluetype_t) | enum |  | 9 |
| [NmIKBlendMode_t](#nmikblendmode_t) | enum |  | 2 |
| [NmPercent_t](#nmpercent_t) | class |  | 1 |
| [NmPoseBlendMode_t](#nmposeblendmode_t) | enum |  | 3 |
| [NmRootMotionBlendMode_t](#nmrootmotionblendmode_t) | enum |  | 4 |
| [NmSyncTrackTimeRange_t](#nmsynctracktimerange_t) | class |  | 2 |
| [NmSyncTrackTime_t](#nmsynctracktime_t) | class |  | 2 |
| [NmTargetWarpAlgorithm_t](#nmtargetwarpalgorithm_t) | enum |  | 4 |
| [NmTargetWarpRule_t](#nmtargetwarprule_t) | enum |  | 5 |
| [NmTransitionRuleCondition_t](#nmtransitionrulecondition_t) | enum |  | 4 |
| [NmTransitionRule_t](#nmtransitionrule_t) | enum |  | 3 |

---

### CNmAdditiveBlendTask

**Inherits from:** [CNmBlendTaskBase](animlib.md#cnmblendtaskbase)

**Relationships:**

```mermaid
classDiagram
    CNmBlendTaskBase <|-- CNmAdditiveBlendTask
    CNmPoseTask <|-- CNmBlendTaskBase
```

### CNmAndNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmAndNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_conditionNodeIndices":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmAndNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_conditionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |

### CNmAnimationPoseNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmAnimationPoseNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nPoseTimeValueNodeIdx": -1,
	"m_nDataSlotIdx": -1,
	"m_inputTimeRemapRange":
	{
		"m_flMin": 0.000000,
		"m_flMax": 1.000000
	},
	"m_flUserSpecifiedTime": 0.000000,
	"m_bUseFramesAsInput": false
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmAnimationPoseNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nPoseTimeValueNodeIdx` | int16 |  |
| `m_nDataSlotIdx` | int16 |  |
| `m_inputTimeRemapRange` | Range_t |  |
| `m_flUserSpecifiedTime` | float32 |  |
| `m_bUseFramesAsInput` | bool |  |

### CNmBitFlags

**Metadata:** `MGetKV3ClassDefaults {
	"m_flags": 0
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flags` | uint32 |  |

### CNmBlend1DNode::CDefinition

**Inherits from:** [CNmParameterizedBlendNode::CDefinition](animlib.md#cnmparameterizedblendnodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmBlend1DNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_sourceNodeIndices":
	[
	],
	"m_nInputParameterValueNodeIdx": -1,
	"m_bAllowLooping": true,
	"m_parameterization":
	{
		"m_blendRanges":
		[
		],
		"m_parameterRange":
		{
			"m_flMin": 340282346638528859811704183484516925440.000000,
			"m_flMax": -340282346638528859811704183484516925440.000000
		}
	}
}`

**Relationships:**

```mermaid
classDiagram
    "CNmParameterizedBlendNode::CDefinition" <|-- "CNmBlend1DNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmParameterizedBlendNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_parameterization` | CNmParameterizedBlendNode::Parameterization_t |  |

### CNmBlend2DNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmBlend2DNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_sourceNodeIndices":
	[
	],
	"m_values":
	[
	],
	"m_indices":
	[
	],
	"m_hullIndices":
	[
	],
	"m_nInputParameterNodeIdx0": -1,
	"m_nInputParameterNodeIdx1": -1,
	"m_bAllowLooping": true
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmBlend2DNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_sourceNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |
| `m_values` | CUtlLeanVectorFixedGrowable<Vector2D> |  |
| `m_indices` | CUtlLeanVectorFixedGrowable<uint8> |  |
| `m_hullIndices` | CUtlLeanVectorFixedGrowable<uint8> |  |
| `m_nInputParameterNodeIdx0` | int16 |  |
| `m_nInputParameterNodeIdx1` | int16 |  |
| `m_bAllowLooping` | bool |  |

### CNmBlendTask

**Inherits from:** [CNmBlendTaskBase](animlib.md#cnmblendtaskbase)

**Relationships:**

```mermaid
classDiagram
    CNmBlendTaskBase <|-- CNmBlendTask
    CNmPoseTask <|-- CNmBlendTaskBase
```

### CNmBlendTaskBase

**Inherits from:** [CNmPoseTask](animlib.md#cnmposetask)

**Derived by:** [CNmAdditiveBlendTask](animlib.md#cnmadditiveblendtask), [CNmBlendTask](animlib.md#cnmblendtask), [CNmModelSpaceBlendTask](animlib.md#cnmmodelspaceblendtask), [CNmOverlayBlendTask](animlib.md#cnmoverlayblendtask)

**Relationships:**

```mermaid
classDiagram
    CNmPoseTask <|-- CNmBlendTaskBase
    CNmBlendTaskBase <|-- CNmAdditiveBlendTask
    CNmBlendTaskBase <|-- CNmModelSpaceBlendTask
    CNmBlendTaskBase <|-- CNmOverlayBlendTask
    CNmBlendTaskBase <|-- CNmBlendTask
```

### CNmBodyGroupEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmBodyGroupEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_target": "Self",
	"m_groupName": "",
	"m_nGroupValue": 0
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmBodyGroupEvent
    CNmBodyGroupEvent *-- CNmEventTargetEntity_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_target` | [CNmEventTargetEntity_t](../schemas/animlib.md#cnmeventtargetentity_t) |  |
| `m_groupName` | CUtlString |  |
| `m_nGroupValue` | int32 |  |

### CNmBoneMaskBlendNode::CDefinition

**Inherits from:** [CNmBoneMaskValueNode::CDefinition](animlib.md#cnmbonemaskvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmBoneMaskBlendNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSourceMaskNodeIdx": -1,
	"m_nTargetMaskNodeIdx": -1,
	"m_nBlendWeightValueNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskBlendNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoneMaskValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSourceMaskNodeIdx` | int16 |  |
| `m_nTargetMaskNodeIdx` | int16 |  |
| `m_nBlendWeightValueNodeIdx` | int16 |  |

### CNmBoneMaskNode::CDefinition

**Inherits from:** [CNmBoneMaskValueNode::CDefinition](animlib.md#cnmbonemaskvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmBoneMaskNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_boneMaskID": ""
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoneMaskValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_boneMaskID` | CGlobalSymbol |  |

### CNmBoneMaskSelectorNode::CDefinition

**Inherits from:** [CNmBoneMaskValueNode::CDefinition](animlib.md#cnmbonemaskvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmBoneMaskSelectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_defaultMaskNodeIdx": -1,
	"m_parameterValueNodeIdx": -1,
	"m_bSwitchDynamically": false,
	"m_maskNodeIndices":
	[
	],
	"m_parameterValues":
	[
	],
	"m_flBlendTimeSeconds": 0.100000
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskSelectorNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoneMaskValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_defaultMaskNodeIdx` | int16 |  |
| `m_parameterValueNodeIdx` | int16 |  |
| `m_bSwitchDynamically` | bool |  |
| `m_maskNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |
| `m_parameterValues` | CUtlLeanVectorFixedGrowable<CGlobalSymbol> |  |
| `m_flBlendTimeSeconds` | float32 |  |

### CNmBoneMaskSwitchNode::CDefinition

**Inherits from:** [CNmBoneMaskValueNode::CDefinition](animlib.md#cnmbonemaskvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmBoneMaskSwitchNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSwitchValueNodeIdx": -1,
	"m_nTrueValueNodeIdx": -1,
	"m_nFalseValueNodeIdx": -1,
	"m_flBlendTimeSeconds": 0.100000,
	"m_bSwitchDynamically": false
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskSwitchNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoneMaskValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSwitchValueNodeIdx` | int16 |  |
| `m_nTrueValueNodeIdx` | int16 |  |
| `m_nFalseValueNodeIdx` | int16 |  |
| `m_flBlendTimeSeconds` | float32 |  |
| `m_bSwitchDynamically` | bool |  |

### CNmBoneMaskValueNode::CDefinition

**Inherits from:** [CNmValueNode::CDefinition](animlib.md#cnmvaluenodecdefinition)

**Derived by:** [CNmBoneMaskBlendNode::CDefinition](animlib.md#cnmbonemaskblendnodecdefinition), [CNmBoneMaskNode::CDefinition](animlib.md#cnmbonemasknodecdefinition), [CNmBoneMaskSelectorNode::CDefinition](animlib.md#cnmbonemaskselectornodecdefinition), [CNmBoneMaskSwitchNode::CDefinition](animlib.md#cnmbonemaskswitchnodecdefinition), [CNmFixedWeightBoneMaskNode::CDefinition](animlib.md#cnmfixedweightbonemasknodecdefinition), [CNmVirtualParameterBoneMaskNode::CDefinition](animlib.md#cnmvirtualparameterbonemasknodecdefinition)

**Relationships:**

```mermaid
classDiagram
    "CNmValueNode::CDefinition" <|-- "CNmBoneMaskValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskNode::CDefinition"
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmFixedWeightBoneMaskNode::CDefinition"
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskSelectorNode::CDefinition"
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmVirtualParameterBoneMaskNode::CDefinition"
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskSwitchNode::CDefinition"
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskBlendNode::CDefinition"
```

### CNmBoneWeightList

**Metadata:** `MGetKV3ClassDefaults {
	"m_skeletonName": "",
	"m_boneIDs":
	[
	],
	"m_weights":
	[
	]
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_skeletonName` | CResourceName |  |
| `m_boneIDs` | CUtlVector<CGlobalSymbol> |  |
| `m_weights` | CUtlVector<float32> |  |

### CNmBoolValueNode::CDefinition

**Inherits from:** [CNmValueNode::CDefinition](animlib.md#cnmvaluenodecdefinition)

**Derived by:** [CNmAndNode::CDefinition](animlib.md#cnmandnodecdefinition), [CNmCachedBoolNode::CDefinition](animlib.md#cnmcachedboolnodecdefinition), [CNmConstBoolNode::CDefinition](animlib.md#cnmconstboolnodecdefinition), [CNmControlParameterBoolNode::CDefinition](animlib.md#cnmcontrolparameterboolnodecdefinition), [CNmFloatComparisonNode::CDefinition](animlib.md#cnmfloatcomparisonnodecdefinition), [CNmFloatRangeComparisonNode::CDefinition](animlib.md#cnmfloatrangecomparisonnodecdefinition), [CNmFootEventConditionNode::CDefinition](animlib.md#cnmfooteventconditionnodecdefinition), [CNmGraphEventConditionNode::CDefinition](animlib.md#cnmgrapheventconditionnodecdefinition), [CNmIDComparisonNode::CDefinition](animlib.md#cnmidcomparisonnodecdefinition), [CNmIDEventConditionNode::CDefinition](animlib.md#cnmideventconditionnodecdefinition), [CNmIDEventPercentageThroughNode::CDefinition](animlib.md#cnmideventpercentagethroughnodecdefinition), [CNmIsExternalGraphSlotFilledNode::CDefinition](animlib.md#cnmisexternalgraphslotfillednodecdefinition), [CNmIsExternalPoseSetNode::CDefinition](animlib.md#cnmisexternalposesetnodecdefinition), [CNmIsInactiveBranchConditionNode::CDefinition](animlib.md#cnmisinactivebranchconditionnodecdefinition), [CNmIsTargetSetNode::CDefinition](animlib.md#cnmistargetsetnodecdefinition), [CNmNotNode::CDefinition](animlib.md#cnmnotnodecdefinition), [CNmOrNode::CDefinition](animlib.md#cnmornodecdefinition), [CNmStateCompletedConditionNode::CDefinition](animlib.md#cnmstatecompletedconditionnodecdefinition), [CNmSyncEventIndexConditionNode::CDefinition](animlib.md#cnmsynceventindexconditionnodecdefinition), [CNmTimeConditionNode::CDefinition](animlib.md#cnmtimeconditionnodecdefinition), [CNmTransitionEventConditionNode::CDefinition](animlib.md#cnmtransitioneventconditionnodecdefinition), [CNmVirtualParameterBoolNode::CDefinition](animlib.md#cnmvirtualparameterboolnodecdefinition)

**Relationships:**

```mermaid
classDiagram
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmVirtualParameterBoolNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmFootEventConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIDComparisonNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmOrNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmFloatComparisonNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmFloatRangeComparisonNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmAndNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmNotNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmConstBoolNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmGraphEventConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIsTargetSetNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmControlParameterBoolNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmSyncEventIndexConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmTimeConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmStateCompletedConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIsInactiveBranchConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIsExternalGraphSlotFilledNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmCachedBoolNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIDEventPercentageThroughNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIDEventConditionNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmIsExternalPoseSetNode::CDefinition"
    "CNmBoolValueNode::CDefinition" <|-- "CNmTransitionEventConditionNode::CDefinition"
```

### CNmCachedBoolNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmCachedBoolNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_mode": "OnEntry"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmCachedBoolNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmCachedBoolNode::CDefinition" *-- NmCachedValueMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_mode` | [NmCachedValueMode_t](../schemas/animlib.md#nmcachedvaluemode_t) |  |

### CNmCachedFloatNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmCachedFloatNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_mode": "OnEntry"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmCachedFloatNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmCachedFloatNode::CDefinition" *-- NmCachedValueMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_mode` | [NmCachedValueMode_t](../schemas/animlib.md#nmcachedvaluemode_t) |  |

### CNmCachedIDNode::CDefinition

**Inherits from:** [CNmIDValueNode::CDefinition](animlib.md#cnmidvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmCachedIDNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_mode": "OnEntry"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmIDValueNode::CDefinition" <|-- "CNmCachedIDNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmCachedIDNode::CDefinition" *-- NmCachedValueMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_mode` | [NmCachedValueMode_t](../schemas/animlib.md#nmcachedvaluemode_t) |  |

### CNmCachedPoseReadTask

**Inherits from:** [CNmPoseTask](animlib.md#cnmposetask)

**Relationships:**

```mermaid
classDiagram
    CNmPoseTask <|-- CNmCachedPoseReadTask
```

### CNmCachedPoseWriteTask

**Inherits from:** [CNmPoseTask](animlib.md#cnmposetask)

**Relationships:**

```mermaid
classDiagram
    CNmPoseTask <|-- CNmCachedPoseWriteTask
```

### CNmCachedTargetNode::CDefinition

**Inherits from:** [CNmTargetValueNode::CDefinition](animlib.md#cnmtargetvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmCachedTargetNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_mode": "OnEntry"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmTargetValueNode::CDefinition" <|-- "CNmCachedTargetNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmTargetValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmCachedTargetNode::CDefinition" *-- NmCachedValueMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_mode` | [NmCachedValueMode_t](../schemas/animlib.md#nmcachedvaluemode_t) |  |

### CNmCachedVectorNode::CDefinition

**Inherits from:** [CNmVectorValueNode::CDefinition](animlib.md#cnmvectorvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmCachedVectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_mode": "OnEntry"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmVectorValueNode::CDefinition" <|-- "CNmCachedVectorNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmCachedVectorNode::CDefinition" *-- NmCachedValueMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_mode` | [NmCachedValueMode_t](../schemas/animlib.md#nmcachedvaluemode_t) |  |

### CNmChainLookatNode::CDefinition

**Inherits from:** [CNmPassthroughNode::CDefinition](animlib.md#cnmpassthroughnodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmChainLookatNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1,
	"m_chainEndBoneID": "",
	"m_nLookatTargetNodeIdx": -1,
	"m_nEnabledNodeIdx": -1,
	"m_flBlendTimeSeconds": 0.000000,
	"m_nChainLength": 2,
	"m_bIsTargetInWorldSpace": false,
	"m_chainForwardDir":
	[
		1.000000,
		0.000000,
		0.000000
	]
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPassthroughNode::CDefinition" <|-- "CNmChainLookatNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_chainEndBoneID` | CGlobalSymbol |  |
| `m_nLookatTargetNodeIdx` | int16 |  |
| `m_nEnabledNodeIdx` | int16 |  |
| `m_flBlendTimeSeconds` | float32 |  |
| `m_nChainLength` | uint8 |  |
| `m_bIsTargetInWorldSpace` | bool |  |
| `m_chainForwardDir` | Vector |  |

### CNmChainLookatTask

**Inherits from:** [CNmPoseTask](animlib.md#cnmposetask)

**Relationships:**

```mermaid
classDiagram
    CNmPoseTask <|-- CNmChainLookatTask
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nChainEndBoneIdx` | int32 |  |
| `m_nNumBonesInChain` | int32 |  |
| `m_chainForwardDir` | Vector |  |
| `m_flBlendWeight` | float32 |  |
| `m_flHorizontalAngleLimitDegrees` | float32 |  |
| `m_flVerticalAngleLimitDegrees` | float32 |  |
| `m_lookatTarget` | Vector |  |
| `m_bIsTargetInWorldSpace` | bool |  |
| `m_bIsRunningFromDeserializedData` | bool |  |
| `m_flHorizontalAngleDegrees` | float32 |  |
| `m_flVerticalAngleDegrees` | float32 |  |

### CNmClip

**Metadata:** `MGetKV3ClassDefaults {
	"m_skeleton": "",
	"m_nNumFrames": 0,
	"m_flDuration": 0.000000,
	"m_compressedPoseData": "[BINARY BLOB]",
	"m_trackCompressionSettings":
	[
	],
	"m_compressedPoseOffsets":
	[
	],
	"m_floatCurveIDs":
	[
	],
	"m_floatCurveDefs":
	[
	],
	"m_compressedFloatCurveData":
	[
	],
	"m_compressedFloatCurveOffsets":
	[
	],
	"m_secondaryAnimations":
	[
	],
	"m_syncTrack":
	{
		"m_syncEvents":
		[
			{
				"m_ID": <HIDDEN FOR DIFF>,
				"m_startTime":
				{
					"m_flValue": 0.000000
				},
				"m_duration":
				{
					"m_flValue": 1.000000
				}
			}
		],
		"m_nStartEventOffset": 0
	},
	"m_rootMotion":
	{
		"m_transforms":
		[
		],
		"m_nNumFrames": 0,
		"m_flAverageLinearVelocity": 0.000000,
		"m_flAverageAngularVelocityRadians": 0.000000,
		"m_totalDelta":
		[
			0.000000,
			0.000000,
			0.000000,
			0.000000,
			0.000000,
			0.000000,
			0.000000,
			0.000000
		]
	},
	"m_bIsAdditive": false,
	"m_modelSpaceSamplingChain":
	[
	],
	"m_modelSpaceBoneSamplingIndices":
	[
	],
	"m_events":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    CNmClip *-- InfoForResourceTypeCNmSkeleton
    CNmClip *-- NmCompressionSettings_t
    CNmClip *-- NmFloatCurveCompressionSettings_t
    CNmClip *-- CNmSyncTrack
    CNmClip *-- CNmRootMotionData
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_skeleton` | CStrongHandle<[InfoForResourceTypeCNmSkeleton](../schemas/resourcesystem.md#infoforresourcetypecnmskeleton)> |  |
| `m_nNumFrames` | uint32 |  |
| `m_flDuration` | float32 |  |
| `m_compressedPoseData` | CUtlBinaryBlock |  |
| `m_trackCompressionSettings` | CUtlVector<[NmCompressionSettings_t](../schemas/animlib.md#nmcompressionsettings_t)> |  |
| `m_compressedPoseOffsets` | CUtlVector<uint32> |  |
| `m_floatCurveIDs` | CUtlVector<CGlobalSymbol> |  |
| `m_floatCurveDefs` | CUtlVector<[NmFloatCurveCompressionSettings_t](../schemas/animlib.md#nmfloatcurvecompressionsettings_t)> |  |
| `m_compressedFloatCurveData` | CUtlVector<uint16> |  |
| `m_compressedFloatCurveOffsets` | CUtlVector<uint32> |  |
| `m_secondaryAnimations` | CUtlVectorFixedGrowable<[CNmClip](../schemas/animlib.md#cnmclip)*> |  |
| `m_syncTrack` | [CNmSyncTrack](../schemas/animlib.md#cnmsynctrack) |  |
| `m_rootMotion` | [CNmRootMotionData](../schemas/animlib.md#cnmrootmotiondata) |  |
| `m_bIsAdditive` | bool |  |
| `m_modelSpaceSamplingChain` | CUtlVector<[CNmClip](../schemas/animlib.md#cnmclip)::ModelSpaceSamplingChainLink_t> |  |
| `m_modelSpaceBoneSamplingIndices` | CUtlVector<int32> |  |

### CNmClip::ModelSpaceSamplingChainLink_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_nBoneIdx": -1,
	"m_nParentBoneIdx": -1,
	"m_nParentChainLinkIdx": -1
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nBoneIdx` | int32 |  |
| `m_nParentBoneIdx` | int32 |  |
| `m_nParentChainLinkIdx` | int32 |  |

### CNmClipNode::CDefinition

**Inherits from:** [CNmClipReferenceNode::CDefinition](animlib.md#cnmclipreferencenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmClipNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nPlayInReverseValueNodeIdx": -1,
	"m_nResetTimeValueNodeIdx": -1,
	"m_bSampleRootMotion": true,
	"m_bAllowLooping": false,
	"m_nDataSlotIdx": -1,
	"m_graphEvents":
	[
	],
	"m_flSpeedMultiplier": 1.000000,
	"m_nStartSyncEventOffset": 0
}`

**Relationships:**

```mermaid
classDiagram
    "CNmClipReferenceNode::CDefinition" <|-- "CNmClipNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmClipReferenceNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nPlayInReverseValueNodeIdx` | int16 |  |
| `m_nResetTimeValueNodeIdx` | int16 |  |
| `m_bSampleRootMotion` | bool |  |
| `m_bAllowLooping` | bool |  |
| `m_nDataSlotIdx` | int16 |  |
| `m_graphEvents` | CUtlVectorFixedGrowable<CGlobalSymbol> |  |
| `m_flSpeedMultiplier` | float32 |  |
| `m_nStartSyncEventOffset` | int32 |  |

### CNmClipReferenceNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Derived by:** [CNmClipNode::CDefinition](animlib.md#cnmclipnodecdefinition), [CNmClipSelectorNode::CDefinition](animlib.md#cnmclipselectornodecdefinition), [CNmIDBasedClipSelectorNode::CDefinition](animlib.md#cnmidbasedclipselectornodecdefinition), [CNmParameterizedClipSelectorNode::CDefinition](animlib.md#cnmparameterizedclipselectornodecdefinition), [CNmTargetSelectorNode::CDefinition](animlib.md#cnmtargetselectornodecdefinition)

**Metadata:** `MGetKV3ClassDefaults Could not parse KV3 Defaults`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmClipReferenceNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmClipReferenceNode::CDefinition" <|-- "CNmTargetSelectorNode::CDefinition"
    "CNmClipReferenceNode::CDefinition" <|-- "CNmParameterizedClipSelectorNode::CDefinition"
    "CNmClipReferenceNode::CDefinition" <|-- "CNmIDBasedClipSelectorNode::CDefinition"
    "CNmClipReferenceNode::CDefinition" <|-- "CNmClipNode::CDefinition"
    "CNmClipReferenceNode::CDefinition" <|-- "CNmClipSelectorNode::CDefinition"
```

### CNmClipSelectorNode::CDefinition

**Inherits from:** [CNmClipReferenceNode::CDefinition](animlib.md#cnmclipreferencenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmClipSelectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_optionNodeIndices":
	[
	],
	"m_conditionNodeIndices":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    "CNmClipReferenceNode::CDefinition" <|-- "CNmClipSelectorNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmClipReferenceNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_optionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |
| `m_conditionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |

### CNmConstBoolNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmConstBoolNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_bValue": false
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmConstBoolNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bValue` | bool |  |

### CNmConstFloatNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmConstFloatNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_flValue": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmConstFloatNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flValue` | float32 |  |

### CNmConstIDNode::CDefinition

**Inherits from:** [CNmIDValueNode::CDefinition](animlib.md#cnmidvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmConstIDNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_value": ""
}`

**Relationships:**

```mermaid
classDiagram
    "CNmIDValueNode::CDefinition" <|-- "CNmConstIDNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_value` | CGlobalSymbol |  |

### CNmConstTargetNode::CDefinition

**Inherits from:** [CNmTargetValueNode::CDefinition](animlib.md#cnmtargetvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmConstTargetNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_value":
	{
		"m_transform":
		[
			0.000000,
			0.000000,
			0.000000,
			1.000000,
			0.000000,
			0.000000,
			0.000000,
			1.000000
		],
		"m_boneID": "",
		"m_bIsBoneTarget": false,
		"m_bIsUsingBoneSpaceOffsets": true,
		"m_bHasOffsets": false,
		"m_bIsSet": false
	}
}`

**Relationships:**

```mermaid
classDiagram
    "CNmTargetValueNode::CDefinition" <|-- "CNmConstTargetNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmTargetValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmConstTargetNode::CDefinition" *-- CNmTarget
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_value` | [CNmTarget](../schemas/animlib.md#cnmtarget) |  |

### CNmConstVectorNode::CDefinition

**Inherits from:** [CNmVectorValueNode::CDefinition](animlib.md#cnmvectorvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmConstVectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_value":
	[
		0.000000,
		0.000000,
		0.000000
	]
}`

**Relationships:**

```mermaid
classDiagram
    "CNmVectorValueNode::CDefinition" <|-- "CNmConstVectorNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_value` | Vector |  |

### CNmControlParameterBoolNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmControlParameterBoolNode::CDefinition",
	"m_nNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmControlParameterBoolNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

### CNmControlParameterFloatNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmControlParameterFloatNode::CDefinition",
	"m_nNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmControlParameterFloatNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

### CNmControlParameterIDNode::CDefinition

**Inherits from:** [CNmIDValueNode::CDefinition](animlib.md#cnmidvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmControlParameterIDNode::CDefinition",
	"m_nNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmIDValueNode::CDefinition" <|-- "CNmControlParameterIDNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

### CNmControlParameterTargetNode::CDefinition

**Inherits from:** [CNmTargetValueNode::CDefinition](animlib.md#cnmtargetvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmControlParameterTargetNode::CDefinition",
	"m_nNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmTargetValueNode::CDefinition" <|-- "CNmControlParameterTargetNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmTargetValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

### CNmControlParameterVectorNode::CDefinition

**Inherits from:** [CNmVectorValueNode::CDefinition](animlib.md#cnmvectorvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmControlParameterVectorNode::CDefinition",
	"m_nNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmVectorValueNode::CDefinition" <|-- "CNmControlParameterVectorNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

### CNmCurrentSyncEventIDNode::CDefinition

**Inherits from:** [CNmIDValueNode::CDefinition](animlib.md#cnmidvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmCurrentSyncEventIDNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSourceStateNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmIDValueNode::CDefinition" <|-- "CNmCurrentSyncEventIDNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSourceStateNodeIdx` | int16 |  |

### CNmCurrentSyncEventNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmCurrentSyncEventNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSourceStateNodeIdx": -1,
	"m_infoType": "IndexAndPercentage"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmCurrentSyncEventNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSourceStateNodeIdx` | int16 |  |
| `m_infoType` | CNmCurrentSyncEventNode::InfoType_t |  |

### CNmCurrentSyncEventNode::InfoType_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `IndexAndPercentage` | 0 |  |
| `IndexOnly` | 1 |  |
| `PercentageOnly` | 2 |  |

### CNmDurationScaleNode::CDefinition

**Inherits from:** [CNmSpeedScaleBaseNode::CDefinition](animlib.md#cnmspeedscalebasenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmDurationScaleNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_flDefaultInputValue": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    "CNmSpeedScaleBaseNode::CDefinition" <|-- "CNmDurationScaleNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmSpeedScaleBaseNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

### CNmEntityAttributeEventBase

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Derived by:** [CNmEntityAttributeFloatEvent](animlib.md#cnmentityattributefloatevent), [CNmEntityAttributeIntEvent](animlib.md#cnmentityattributeintevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmEntityAttributeEventBase",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_target": "Self",
	"m_attributeName": ""
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmEntityAttributeEventBase
    CNmEntityAttributeEventBase <|-- CNmEntityAttributeFloatEvent
    CNmEntityAttributeEventBase <|-- CNmEntityAttributeIntEvent
    CNmEntityAttributeEventBase *-- CNmEventTargetEntity_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_target` | [CNmEventTargetEntity_t](../schemas/animlib.md#cnmeventtargetentity_t) |  |
| `m_attributeName` | CUtlString |  |

### CNmEntityAttributeFloatEvent

**Inherits from:** [CNmEntityAttributeEventBase](animlib.md#cnmentityattributeeventbase)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmEntityAttributeFloatEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_target": "Self",
	"m_attributeName": "",
	"m_FloatValue":
	{
		"m_spline":
		[
		],
		"m_tangents":
		[
		],
		"m_vDomainMins":
		[
			0.000000,
			0.000000
		],
		"m_vDomainMaxs":
		[
			0.000000,
			0.000000
		]
	}
}`

**Relationships:**

```mermaid
classDiagram
    CNmEntityAttributeEventBase <|-- CNmEntityAttributeFloatEvent
    CNmEvent <|-- CNmEntityAttributeEventBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_FloatValue` | CPiecewiseCurve |  |

### CNmEntityAttributeIntEvent

**Inherits from:** [CNmEntityAttributeEventBase](animlib.md#cnmentityattributeeventbase)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmEntityAttributeIntEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_target": "Self",
	"m_attributeName": "",
	"m_nIntValue": 0
}`

**Relationships:**

```mermaid
classDiagram
    CNmEntityAttributeEventBase <|-- CNmEntityAttributeIntEvent
    CNmEvent <|-- CNmEntityAttributeEventBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nIntValue` | int32 |  |

### CNmEvent

**Derived by:** [CNmBodyGroupEvent](animlib.md#cnmbodygroupevent), [CNmEntityAttributeEventBase](animlib.md#cnmentityattributeeventbase), [CNmFloatCurveEvent](animlib.md#cnmfloatcurveevent), [CNmFootEvent](animlib.md#cnmfootevent), [CNmFrameSnapEvent](animlib.md#cnmframesnapevent), [CNmIDEvent](animlib.md#cnmidevent), [CNmLegacyEvent](animlib.md#cnmlegacyevent), [CNmMaterialAttributeEvent](animlib.md#cnmmaterialattributeevent), [CNmOrientationWarpEvent](animlib.md#cnmorientationwarpevent), [CNmParticleEvent](animlib.md#cnmparticleevent), [CNmRootMotionEvent](animlib.md#cnmrootmotionevent), [CNmSoundEvent](animlib.md#cnmsoundevent), [CNmTargetWarpEvent](animlib.md#cnmtargetwarpevent), [CNmTransitionEvent](animlib.md#cnmtransitionevent)

**Metadata:** `MGetKV3ClassDefaults Could not parse KV3 Defaults`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmBodyGroupEvent
    CNmEvent <|-- CNmFootEvent
    CNmEvent <|-- CNmSoundEvent
    CNmEvent <|-- CNmIDEvent
    CNmEvent <|-- CNmLegacyEvent
    CNmEvent <|-- CNmFloatCurveEvent
    CNmEvent <|-- CNmTransitionEvent
    CNmEvent <|-- CNmParticleEvent
    CNmEvent <|-- CNmOrientationWarpEvent
    CNmEvent <|-- CNmRootMotionEvent
    CNmEvent <|-- CNmTargetWarpEvent
    CNmEvent <|-- CNmMaterialAttributeEvent
    CNmEvent <|-- CNmEntityAttributeEventBase
    CNmEvent <|-- CNmFrameSnapEvent
    CNmEvent *-- NmPercent_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flStartTime` | [NmPercent_t](../schemas/animlib.md#nmpercent_t) |  |
| `m_flDuration` | [NmPercent_t](../schemas/animlib.md#nmpercent_t) |  |
| `m_syncID` | CGlobalSymbol |  |

### CNmEventRelevance_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `ClientOnly` | 0 |  |
| `ServerOnly` | 1 |  |
| `ClientAndServer` | 2 |  |

### CNmEventTargetEntity_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Self` | 0 |  |
| `Weapon` | 1 |  |
| `HeldItem` | 2 |  |
| `Custom` | 3 |  |

### CNmExternalPoseNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmExternalPoseNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_bShouldSampleRootMotion": false
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmExternalPoseNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bShouldSampleRootMotion` | bool |  |

### CNmFixedWeightBoneMaskNode::CDefinition

**Inherits from:** [CNmBoneMaskValueNode::CDefinition](animlib.md#cnmbonemaskvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFixedWeightBoneMaskNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_flBoneWeight": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmFixedWeightBoneMaskNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoneMaskValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flBoneWeight` | float32 |  |

### CNmFloatAngleMathNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatAngleMathNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_operation": "ClampTo180"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatAngleMathNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_operation` | CNmFloatAngleMathNode::Operation_t |  |

### CNmFloatAngleMathNode::Operation_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `ClampTo180` | 0 |  |
| `ClampTo360` | 1 |  |
| `FlipHemisphere` | 2 |  |
| `FlipHemisphereNegate` | 3 |  |

### CNmFloatClampNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatClampNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_clampRange":
	{
		"m_flMin": 0.000000,
		"m_flMax": 0.000000
	}
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatClampNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_clampRange` | Range_t |  |

### CNmFloatComparisonNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatComparisonNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_nComparandValueNodeIdx": -1,
	"m_comparison": "GreaterThanEqual",
	"m_flEpsilon": 0.000000,
	"m_flComparisonValue": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmFloatComparisonNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmFloatComparisonNode::CDefinition" *-- Comparison_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_nComparandValueNodeIdx` | int16 |  |
| `m_comparison` | CNmFloatComparisonNode::[Comparison_t](../schemas/animgraphdoclib.md#comparison_t) |  |
| `m_flEpsilon` | float32 |  |
| `m_flComparisonValue` | float32 |  |

### CNmFloatComparisonNode::Comparison_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `GreaterThanEqual` | 0 |  |
| `LessThanEqual` | 1 |  |
| `NearEqual` | 2 |  |
| `GreaterThan` | 3 |  |
| `LessThan` | 4 |  |

### CNmFloatCurveEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatCurveEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_ID": <HIDDEN FOR DIFF>,
	"m_curve":
	{
		"m_spline":
		[
		],
		"m_tangents":
		[
		],
		"m_vDomainMins":
		[
			0.000000,
			0.000000
		],
		"m_vDomainMaxs":
		[
			0.000000,
			0.000000
		]
	}
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmFloatCurveEvent
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_ID` | CGlobalSymbol |  |
| `m_curve` | CPiecewiseCurve |  |

### CNmFloatCurveEventNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatCurveEventNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_eventID": "",
	"m_nDefaultNodeIdx": -1,
	"m_flDefaultValue": 0.000000,
	"m_eventConditionRules":
	{
		"m_flags": 0
	}
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatCurveEventNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmFloatCurveEventNode::CDefinition" *-- CNmBitFlags
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_eventID` | CGlobalSymbol |  |
| `m_nDefaultNodeIdx` | int16 |  |
| `m_flDefaultValue` | float32 |  |
| `m_eventConditionRules` | [CNmBitFlags](../schemas/animlib.md#cnmbitflags) |  |

### CNmFloatCurveNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatCurveNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_curve":
	{
		"m_spline":
		[
		],
		"m_tangents":
		[
		],
		"m_vDomainMins":
		[
			0.000000,
			0.000000
		],
		"m_vDomainMaxs":
		[
			0.000000,
			0.000000
		]
	}
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatCurveNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_curve` | CPiecewiseCurve |  |

### CNmFloatEaseNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatEaseNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_flEaseTime": 1.000000,
	"m_flStartValue": 0.000000,
	"m_nInputValueNodeIdx": -1,
	"m_easingOp": "Linear",
	"m_bUseStartValue": false
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatEaseNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmFloatEaseNode::CDefinition" *-- NmEasingOperation_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flEaseTime` | float32 |  |
| `m_flStartValue` | float32 |  |
| `m_nInputValueNodeIdx` | int16 |  |
| `m_easingOp` | [NmEasingOperation_t](../schemas/animlib.md#nmeasingoperation_t) |  |
| `m_bUseStartValue` | bool |  |

### CNmFloatMathNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatMathNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdxA": -1,
	"m_nInputValueNodeIdxB": -1,
	"m_bReturnAbsoluteResult": false,
	"m_bReturnNegatedResult": false,
	"m_operator": "Add",
	"m_flValueB": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatMathNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdxA` | int16 |  |
| `m_nInputValueNodeIdxB` | int16 |  |
| `m_bReturnAbsoluteResult` | bool |  |
| `m_bReturnNegatedResult` | bool |  |
| `m_operator` | CNmFloatMathNode::Operator_t |  |
| `m_flValueB` | float32 |  |

### CNmFloatMathNode::Operator_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Add` | 0 |  |
| `Sub` | 1 |  |
| `Mul` | 2 |  |
| `Div` | 3 |  |
| `Mod` | 4 |  |
| `Abs` | 5 |  |
| `Negate` | 6 |  |
| `Floor` | 7 |  |
| `Ceiling` | 8 |  |
| `IntegerPart` | 9 |  |
| `FractionalPart` | 10 |  |
| `InverseFractionalPart` | 11 |  |

### CNmFloatRangeComparisonNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatRangeComparisonNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_range":
	{
		"m_flMin": 340282346638528859811704183484516925440.000000,
		"m_flMax": -340282346638528859811704183484516925440.000000
	},
	"m_nInputValueNodeIdx": -1,
	"m_bIsInclusiveCheck": true
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmFloatRangeComparisonNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_range` | Range_t |  |
| `m_nInputValueNodeIdx` | int16 |  |
| `m_bIsInclusiveCheck` | bool |  |

### CNmFloatRemapNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatRemapNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_inputRange":
	{
		"m_flBegin": 0.000000,
		"m_flEnd": 0.000000
	},
	"m_outputRange":
	{
		"m_flBegin": 0.000000,
		"m_flEnd": 0.000000
	}
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatRemapNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_inputRange` | CNmFloatRemapNode::RemapRange_t |  |
| `m_outputRange` | CNmFloatRemapNode::RemapRange_t |  |

### CNmFloatRemapNode::RemapRange_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_flBegin": 0.000000,
	"m_flEnd": 0.000000
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flBegin` | float32 |  |
| `m_flEnd` | float32 |  |

### CNmFloatSelectorNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatSelectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_conditionNodeIndices":
	[
	],
	"m_values":
	[
	],
	"m_flDefaultValue": 0.000000,
	"m_flEaseTime": 0.200000,
	"m_easingOp": "Linear"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatSelectorNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmFloatSelectorNode::CDefinition" *-- NmEasingOperation_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_conditionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |
| `m_values` | CUtlLeanVectorFixedGrowable<float32> |  |
| `m_flDefaultValue` | float32 |  |
| `m_flEaseTime` | float32 |  |
| `m_easingOp` | [NmEasingOperation_t](../schemas/animlib.md#nmeasingoperation_t) |  |

### CNmFloatSpringNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatSpringNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_flStartValue": 0.000000,
	"m_flHertz": 4.000000,
	"m_flDampingRatio": 0.700000,
	"m_nInputValueNodeIdx": -1,
	"m_bUseStartValue": false
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatSpringNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flStartValue` | float32 |  |
| `m_flHertz` | float32 |  |
| `m_flDampingRatio` | float32 |  |
| `m_nInputValueNodeIdx` | int16 |  |
| `m_bUseStartValue` | bool |  |

### CNmFloatSwitchNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFloatSwitchNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSwitchValueNodeIdx": -1,
	"m_nTrueValueNodeIdx": -1,
	"m_nFalseValueNodeIdx": -1,
	"m_flFalseValue": 0.000000,
	"m_flTrueValue": 1.000000
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatSwitchNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSwitchValueNodeIdx` | int16 |  |
| `m_nTrueValueNodeIdx` | int16 |  |
| `m_nFalseValueNodeIdx` | int16 |  |
| `m_flFalseValue` | float32 |  |
| `m_flTrueValue` | float32 |  |

### CNmFloatValueNode::CDefinition

**Inherits from:** [CNmValueNode::CDefinition](animlib.md#cnmvaluenodecdefinition)

**Derived by:** [CNmCachedFloatNode::CDefinition](animlib.md#cnmcachedfloatnodecdefinition), [CNmConstFloatNode::CDefinition](animlib.md#cnmconstfloatnodecdefinition), [CNmControlParameterFloatNode::CDefinition](animlib.md#cnmcontrolparameterfloatnodecdefinition), [CNmCurrentSyncEventNode::CDefinition](animlib.md#cnmcurrentsynceventnodecdefinition), [CNmFloatAngleMathNode::CDefinition](animlib.md#cnmfloatanglemathnodecdefinition), [CNmFloatClampNode::CDefinition](animlib.md#cnmfloatclampnodecdefinition), [CNmFloatCurveEventNode::CDefinition](animlib.md#cnmfloatcurveeventnodecdefinition), [CNmFloatCurveNode::CDefinition](animlib.md#cnmfloatcurvenodecdefinition), [CNmFloatEaseNode::CDefinition](animlib.md#cnmfloateasenodecdefinition), [CNmFloatMathNode::CDefinition](animlib.md#cnmfloatmathnodecdefinition), [CNmFloatRemapNode::CDefinition](animlib.md#cnmfloatremapnodecdefinition), [CNmFloatSelectorNode::CDefinition](animlib.md#cnmfloatselectornodecdefinition), [CNmFloatSpringNode::CDefinition](animlib.md#cnmfloatspringnodecdefinition), [CNmFloatSwitchNode::CDefinition](animlib.md#cnmfloatswitchnodecdefinition), [CNmFootstepEventPercentageThroughNode::CDefinition](animlib.md#cnmfootstepeventpercentagethroughnodecdefinition), [CNmIDToFloatNode::CDefinition](animlib.md#cnmidtofloatnodecdefinition), [CNmTargetInfoNode::CDefinition](animlib.md#cnmtargetinfonodecdefinition), [CNmVectorInfoNode::CDefinition](animlib.md#cnmvectorinfonodecdefinition), [CNmVirtualParameterFloatNode::CDefinition](animlib.md#cnmvirtualparameterfloatnodecdefinition)

**Relationships:**

```mermaid
classDiagram
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmCurrentSyncEventNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmConstFloatNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatRemapNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatClampNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatSpringNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatCurveNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFootstepEventPercentageThroughNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmIDToFloatNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatSelectorNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatCurveEventNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmControlParameterFloatNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmTargetInfoNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatMathNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatSwitchNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmCachedFloatNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmVirtualParameterFloatNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatAngleMathNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatEaseNode::CDefinition"
    "CNmFloatValueNode::CDefinition" <|-- "CNmVectorInfoNode::CDefinition"
```

### CNmFollowBoneNode::CDefinition

**Inherits from:** [CNmPassthroughNode::CDefinition](animlib.md#cnmpassthroughnodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFollowBoneNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1,
	"m_bone": "",
	"m_followTargetBone": "",
	"m_nEnabledNodeIdx": -1,
	"m_mode": "RotationAndTranslation"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPassthroughNode::CDefinition" <|-- "CNmFollowBoneNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmFollowBoneNode::CDefinition" *-- NmFollowBoneMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bone` | CGlobalSymbol |  |
| `m_followTargetBone` | CGlobalSymbol |  |
| `m_nEnabledNodeIdx` | int16 |  |
| `m_mode` | [NmFollowBoneMode_t](../schemas/animlib.md#nmfollowbonemode_t) |  |

### CNmFollowBoneTask

**Inherits from:** [CNmPoseTask](animlib.md#cnmposetask)

**Relationships:**

```mermaid
classDiagram
    CNmPoseTask <|-- CNmFollowBoneTask
```

### CNmFootEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFootEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_phase": "LeftFootDown"
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmFootEvent
    CNmFootEvent *-- NmFootPhase_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_phase` | [NmFootPhase_t](../schemas/animlib.md#nmfootphase_t) |  |

### CNmFootEventConditionNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFootEventConditionNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSourceStateNodeIdx": -1,
	"m_phaseCondition": "LeftFootDown",
	"m_eventConditionRules":
	{
		"m_flags": 0
	}
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmFootEventConditionNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmFootEventConditionNode::CDefinition" *-- NmFootPhaseCondition_t
    "CNmFootEventConditionNode::CDefinition" *-- CNmBitFlags
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSourceStateNodeIdx` | int16 |  |
| `m_phaseCondition` | [NmFootPhaseCondition_t](../schemas/animlib.md#nmfootphasecondition_t) |  |
| `m_eventConditionRules` | [CNmBitFlags](../schemas/animlib.md#cnmbitflags) |  |

### CNmFootIKNode::CDefinition

**Inherits from:** [CNmPassthroughNode::CDefinition](animlib.md#cnmpassthroughnodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFootIKNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1,
	"m_leftEffectorBoneID": "",
	"m_rightEffectorBoneID": "",
	"m_nLeftTargetNodeIdx": -1,
	"m_nRightTargetNodeIdx": -1,
	"m_nEnabledNodeIdx": -1,
	"m_flBlendTimeSeconds": 0.000000,
	"m_blendMode": "Effector",
	"m_bIsTargetInWorldSpace": false
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPassthroughNode::CDefinition" <|-- "CNmFootIKNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmFootIKNode::CDefinition" *-- NmIKBlendMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_leftEffectorBoneID` | CGlobalSymbol |  |
| `m_rightEffectorBoneID` | CGlobalSymbol |  |
| `m_nLeftTargetNodeIdx` | int16 |  |
| `m_nRightTargetNodeIdx` | int16 |  |
| `m_nEnabledNodeIdx` | int16 |  |
| `m_flBlendTimeSeconds` | float32 |  |
| `m_blendMode` | [NmIKBlendMode_t](../schemas/animlib.md#nmikblendmode_t) |  |
| `m_bIsTargetInWorldSpace` | bool |  |

### CNmFootIKTask

**Inherits from:** [CNmPoseTask](animlib.md#cnmposetask)

**Relationships:**

```mermaid
classDiagram
    CNmPoseTask <|-- CNmFootIKTask
    CNmFootIKTask *-- CNmTarget
    CNmFootIKTask *-- NmIKBlendMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nLeftEffectorBoneIdx` | int32 |  |
| `m_nRightEffectorBoneIdx` | int32 |  |
| `m_leftTargetTransform` | CTransform |  |
| `m_rightTargetTransform` | CTransform |  |
| `m_nLeftTargetBoneIdx` | int32 |  |
| `m_nRightTargetBoneIdx` | int32 |  |
| `m_leftTarget` | [CNmTarget](../schemas/animlib.md#cnmtarget) |  |
| `m_rightTarget` | [CNmTarget](../schemas/animlib.md#cnmtarget) |  |
| `m_blendMode` | [NmIKBlendMode_t](../schemas/animlib.md#nmikblendmode_t) |  |
| `m_flBlendWeight` | float32 |  |
| `m_bIsTargetInWorldSpace` | bool |  |
| `m_bIsRunningFromDeserializedData` | bool |  |

### CNmFootstepEventIDNode::CDefinition

**Inherits from:** [CNmIDValueNode::CDefinition](animlib.md#cnmidvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFootstepEventIDNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSourceStateNodeIdx": -1,
	"m_eventConditionRules":
	{
		"m_flags": 0
	}
}`

**Relationships:**

```mermaid
classDiagram
    "CNmIDValueNode::CDefinition" <|-- "CNmFootstepEventIDNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmFootstepEventIDNode::CDefinition" *-- CNmBitFlags
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSourceStateNodeIdx` | int16 |  |
| `m_eventConditionRules` | [CNmBitFlags](../schemas/animlib.md#cnmbitflags) |  |

### CNmFootstepEventPercentageThroughNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFootstepEventPercentageThroughNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSourceStateNodeIdx": -1,
	"m_phaseCondition": "LeftFootDown",
	"m_eventConditionRules":
	{
		"m_flags": 0
	}
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFootstepEventPercentageThroughNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmFootstepEventPercentageThroughNode::CDefinition" *-- NmFootPhaseCondition_t
    "CNmFootstepEventPercentageThroughNode::CDefinition" *-- CNmBitFlags
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSourceStateNodeIdx` | int16 |  |
| `m_phaseCondition` | [NmFootPhaseCondition_t](../schemas/animlib.md#nmfootphasecondition_t) |  |
| `m_eventConditionRules` | [CNmBitFlags](../schemas/animlib.md#cnmbitflags) |  |

### CNmFrameSnapEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmFrameSnapEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_frameSnapMode": "Floor"
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmFrameSnapEvent
    CNmFrameSnapEvent *-- NmFrameSnapEventMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_frameSnapMode` | [NmFrameSnapEventMode_t](../schemas/animlib.md#nmframesnapeventmode_t) |  |

### CNmGraphDefinition

**Metadata:** `MGetKV3ClassDefaults {
	"m_variationID": "",
	"m_skeleton": "",
	"m_supportedSecondarySkeletons":
	[
	],
	"m_pUserData": null,
	"m_persistentNodeIndices":
	[
	],
	"m_nRootNodeIdx": -1,
	"m_controlParameterIDs":
	[
	],
	"m_virtualParameterIDs":
	[
	],
	"m_virtualParameterNodeIndices":
	[
	],
	"m_referencedGraphSlots":
	[
	],
	"m_externalGraphSlots":
	[
	],
	"m_externalPoseSlots":
	[
	],
	"m_nodePaths":
	[
	],
	"m_resources":
	[
	],
	"m_nodes":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    CNmGraphDefinition *-- InfoForResourceTypeCNmSkeleton
    CNmGraphDefinition --> CNmGraphVariationUserData
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_variationID` | CGlobalSymbol |  |
| `m_skeleton` | CStrongHandle<[InfoForResourceTypeCNmSkeleton](../schemas/resourcesystem.md#infoforresourcetypecnmskeleton)> |  |
| `m_supportedSecondarySkeletons` | CUtlVector<CStrongHandle<[InfoForResourceTypeCNmSkeleton](../schemas/resourcesystem.md#infoforresourcetypecnmskeleton)>> |  |
| `m_pUserData` | [CNmGraphVariationUserData](../schemas/animlib.md#cnmgraphvariationuserdata)* |  |
| `m_persistentNodeIndices` | CUtlVector<int16> |  |
| `m_nRootNodeIdx` | int16 |  |
| `m_controlParameterIDs` | CUtlVector<CGlobalSymbol> |  |
| `m_virtualParameterIDs` | CUtlVector<CGlobalSymbol> |  |
| `m_virtualParameterNodeIndices` | CUtlVector<int16> |  |
| `m_referencedGraphSlots` | CUtlVector<[CNmGraphDefinition](../schemas/animlib.md#cnmgraphdefinition)::ReferencedGraphSlot_t> |  |
| `m_externalGraphSlots` | CUtlVector<[CNmGraphDefinition](../schemas/animlib.md#cnmgraphdefinition)::ExternalGraphSlot_t> |  |
| `m_externalPoseSlots` | CUtlVector<[CNmGraphDefinition](../schemas/animlib.md#cnmgraphdefinition)::ExternalPoseSlot_t> |  |
| `m_nodePaths` | CUtlVector<CUtlString> |  |
| `m_resources` | CUtlVector<CStrongHandleVoid> |  |

### CNmGraphDefinition::ExternalGraphSlot_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_nNodeIdx": -1,
	"m_slotID": ""
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nNodeIdx` | int16 |  |
| `m_slotID` | CGlobalSymbol |  |

### CNmGraphDefinition::ExternalPoseSlot_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_nNodeIdx": -1,
	"m_slotID": ""
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nNodeIdx` | int16 |  |
| `m_slotID` | CGlobalSymbol |  |

### CNmGraphDefinition::ReferencedGraphSlot_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_nNodeIdx": -1,
	"m_dataSlotIdx": -1
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nNodeIdx` | int16 |  |
| `m_dataSlotIdx` | int16 |  |

### CNmGraphEventConditionNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmGraphEventConditionNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSourceStateNodeIdx": -1,
	"m_eventConditionRules":
	{
		"m_flags": 0
	},
	"m_conditions":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmGraphEventConditionNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmGraphEventConditionNode::CDefinition" *-- CNmBitFlags
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSourceStateNodeIdx` | int16 |  |
| `m_eventConditionRules` | [CNmBitFlags](../schemas/animlib.md#cnmbitflags) |  |
| `m_conditions` | CUtlVectorFixedGrowable<CNmGraphEventConditionNode::Condition_t> |  |

### CNmGraphEventConditionNode::Condition_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_eventID": "",
	"m_eventTypeCondition": "Entry"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmGraphEventConditionNode::Condition_t" *-- NmGraphEventTypeCondition_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_eventID` | CGlobalSymbol |  |
| `m_eventTypeCondition` | [NmGraphEventTypeCondition_t](../schemas/animlib.md#nmgrapheventtypecondition_t) |  |

### CNmGraphInstance

### CNmGraphNode::CDefinition

**Derived by:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition), [CNmValueNode::CDefinition](animlib.md#cnmvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults Could not parse KV3 Defaults`

**Relationships:**

```mermaid
classDiagram
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nNodeIdx` | int16 |  |

### CNmGraphVariationUserData

**Derived by:** [CBaseAnimGraphVariationUserData](client.md#cbaseanimgraphvariationuserdata)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmGraphVariationUserData"
}`

**Relationships:**

```mermaid
classDiagram
    CNmGraphVariationUserData <|-- CBaseAnimGraphVariationUserData
```

### CNmIDBasedClipSelectorNode::CDefinition

**Inherits from:** [CNmClipReferenceNode::CDefinition](animlib.md#cnmclipreferencenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIDBasedClipSelectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_optionNodeIndices":
	[
	],
	"m_optionIDs":
	[
	],
	"m_nParameterNodeIdx": -1,
	"m_nFallbackNodeIdx": -1,
	"m_bIgnoreInvalidOptions": false
}`

**Relationships:**

```mermaid
classDiagram
    "CNmClipReferenceNode::CDefinition" <|-- "CNmIDBasedClipSelectorNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmClipReferenceNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_optionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |
| `m_optionIDs` | CUtlLeanVectorFixedGrowable<CGlobalSymbol> |  |
| `m_nParameterNodeIdx` | int16 |  |
| `m_nFallbackNodeIdx` | int16 |  |
| `m_bIgnoreInvalidOptions` | bool |  |

### CNmIDBasedSelectorNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIDBasedSelectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_optionNodeIndices":
	[
	],
	"m_optionIDs":
	[
	],
	"m_nParameterNodeIdx": -1,
	"m_nFallbackNodeIdx": -1,
	"m_bIgnoreInvalidOptions": false
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmIDBasedSelectorNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_optionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |
| `m_optionIDs` | CUtlLeanVectorFixedGrowable<CGlobalSymbol> |  |
| `m_nParameterNodeIdx` | int16 |  |
| `m_nFallbackNodeIdx` | int16 |  |
| `m_bIgnoreInvalidOptions` | bool |  |

### CNmIDComparisonNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIDComparisonNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_comparison": "Matches",
	"m_comparisionIDs":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmIDComparisonNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmIDComparisonNode::CDefinition" *-- Comparison_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_comparison` | CNmIDComparisonNode::[Comparison_t](../schemas/animgraphdoclib.md#comparison_t) |  |
| `m_comparisionIDs` | CUtlLeanVectorFixedGrowable<CGlobalSymbol> |  |

### CNmIDComparisonNode::Comparison_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Matches` | 0 |  |
| `DoesntMatch` | 1 |  |

### CNmIDEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIDEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_ID": <HIDDEN FOR DIFF>,
	"m_secondaryID": ""
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmIDEvent
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_ID` | CGlobalSymbol |  |
| `m_secondaryID` | CGlobalSymbol |  |

### CNmIDEventConditionNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIDEventConditionNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSourceStateNodeIdx": -1,
	"m_eventConditionRules":
	{
		"m_flags": 0
	},
	"m_eventIDs":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmIDEventConditionNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmIDEventConditionNode::CDefinition" *-- CNmBitFlags
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSourceStateNodeIdx` | int16 |  |
| `m_eventConditionRules` | [CNmBitFlags](../schemas/animlib.md#cnmbitflags) |  |
| `m_eventIDs` | CUtlVectorFixedGrowable<CGlobalSymbol> |  |

### CNmIDEventNode::CDefinition

**Inherits from:** [CNmIDValueNode::CDefinition](animlib.md#cnmidvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIDEventNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSourceStateNodeIdx": -1,
	"m_eventConditionRules":
	{
		"m_flags": 0
	},
	"m_defaultValue": ""
}`

**Relationships:**

```mermaid
classDiagram
    "CNmIDValueNode::CDefinition" <|-- "CNmIDEventNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmIDEventNode::CDefinition" *-- CNmBitFlags
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSourceStateNodeIdx` | int16 |  |
| `m_eventConditionRules` | [CNmBitFlags](../schemas/animlib.md#cnmbitflags) |  |
| `m_defaultValue` | CGlobalSymbol |  |

### CNmIDEventPercentageThroughNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIDEventPercentageThroughNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSourceStateNodeIdx": -1,
	"m_eventConditionRules":
	{
		"m_flags": 0
	},
	"m_eventID": ""
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmIDEventPercentageThroughNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmIDEventPercentageThroughNode::CDefinition" *-- CNmBitFlags
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSourceStateNodeIdx` | int16 |  |
| `m_eventConditionRules` | [CNmBitFlags](../schemas/animlib.md#cnmbitflags) |  |
| `m_eventID` | CGlobalSymbol |  |

### CNmIDSelectorNode::CDefinition

**Inherits from:** [CNmIDValueNode::CDefinition](animlib.md#cnmidvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIDSelectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_conditionNodeIndices":
	[
	],
	"m_values":
	[
	],
	"m_defaultValue": ""
}`

**Relationships:**

```mermaid
classDiagram
    "CNmIDValueNode::CDefinition" <|-- "CNmIDSelectorNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_conditionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |
| `m_values` | CUtlLeanVectorFixedGrowable<CGlobalSymbol> |  |
| `m_defaultValue` | CGlobalSymbol |  |

### CNmIDSwitchNode::CDefinition

**Inherits from:** [CNmIDValueNode::CDefinition](animlib.md#cnmidvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIDSwitchNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSwitchValueNodeIdx": -1,
	"m_nTrueValueNodeIdx": -1,
	"m_nFalseValueNodeIdx": -1,
	"m_falseValue": "",
	"m_trueValue": ""
}`

**Relationships:**

```mermaid
classDiagram
    "CNmIDValueNode::CDefinition" <|-- "CNmIDSwitchNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSwitchValueNodeIdx` | int16 |  |
| `m_nTrueValueNodeIdx` | int16 |  |
| `m_nFalseValueNodeIdx` | int16 |  |
| `m_falseValue` | CGlobalSymbol |  |
| `m_trueValue` | CGlobalSymbol |  |

### CNmIDToFloatNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIDToFloatNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_defaultValue": 0.000000,
	"m_IDs":
	[
	],
	"m_values":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmIDToFloatNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_defaultValue` | float32 |  |
| `m_IDs` | CUtlLeanVectorFixedGrowable<CGlobalSymbol> |  |
| `m_values` | CUtlLeanVectorFixedGrowable<float32> |  |

### CNmIDValueNode::CDefinition

**Inherits from:** [CNmValueNode::CDefinition](animlib.md#cnmvaluenodecdefinition)

**Derived by:** [CNmCachedIDNode::CDefinition](animlib.md#cnmcachedidnodecdefinition), [CNmConstIDNode::CDefinition](animlib.md#cnmconstidnodecdefinition), [CNmControlParameterIDNode::CDefinition](animlib.md#cnmcontrolparameteridnodecdefinition), [CNmCurrentSyncEventIDNode::CDefinition](animlib.md#cnmcurrentsynceventidnodecdefinition), [CNmFootstepEventIDNode::CDefinition](animlib.md#cnmfootstepeventidnodecdefinition), [CNmIDEventNode::CDefinition](animlib.md#cnmideventnodecdefinition), [CNmIDSelectorNode::CDefinition](animlib.md#cnmidselectornodecdefinition), [CNmIDSwitchNode::CDefinition](animlib.md#cnmidswitchnodecdefinition), [CNmVirtualParameterIDNode::CDefinition](animlib.md#cnmvirtualparameteridnodecdefinition)

**Relationships:**

```mermaid
classDiagram
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmControlParameterIDNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmVirtualParameterIDNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmIDSelectorNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmFootstepEventIDNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmIDSwitchNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmCurrentSyncEventIDNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmCachedIDNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmConstIDNode::CDefinition"
    "CNmIDValueNode::CDefinition" <|-- "CNmIDEventNode::CDefinition"
```

### CNmIsExternalGraphSlotFilledNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIsExternalGraphSlotFilledNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nExternalGraphNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmIsExternalGraphSlotFilledNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nExternalGraphNodeIdx` | int16 |  |

### CNmIsExternalPoseSetNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIsExternalPoseSetNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nExternalPoseNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmIsExternalPoseSetNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nExternalPoseNodeIdx` | int16 |  |

### CNmIsInactiveBranchConditionNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIsInactiveBranchConditionNode::CDefinition",
	"m_nNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmIsInactiveBranchConditionNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

### CNmIsTargetSetNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmIsTargetSetNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmIsTargetSetNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |

### CNmLayerBlendNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmLayerBlendNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nBaseNodeIdx": -1,
	"m_bOnlySampleBaseRootMotion": true,
	"m_layerDefinition":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmLayerBlendNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nBaseNodeIdx` | int16 |  |
| `m_bOnlySampleBaseRootMotion` | bool |  |
| `m_layerDefinition` | CUtlLeanVectorFixedGrowable<CNmLayerBlendNode::LayerDefinition_t> |  |

### CNmLayerBlendNode::LayerDefinition_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_nInputNodeIdx": -1,
	"m_nWeightValueNodeIdx": -1,
	"m_nBoneMaskValueNodeIdx": -1,
	"m_nRootMotionWeightValueNodeIdx": -1,
	"m_bIsSynchronized": false,
	"m_bIgnoreEvents": false,
	"m_bIsStateMachineLayer": false,
	"m_blendMode": "Overlay"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmLayerBlendNode::LayerDefinition_t" *-- NmPoseBlendMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputNodeIdx` | int16 |  |
| `m_nWeightValueNodeIdx` | int16 |  |
| `m_nBoneMaskValueNodeIdx` | int16 |  |
| `m_nRootMotionWeightValueNodeIdx` | int16 |  |
| `m_bIsSynchronized` | bool |  |
| `m_bIgnoreEvents` | bool |  |
| `m_bIsStateMachineLayer` | bool |  |
| `m_blendMode` | [NmPoseBlendMode_t](../schemas/animlib.md#nmposeblendmode_t) |  |

### CNmLegacyEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmLegacyEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_animEventClassName": "",
	"m_KV": null
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmLegacyEvent
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_animEventClassName` | CUtlString |  |
| `m_KV` | KeyValues3 |  |

### CNmMaterialAttributeEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmMaterialAttributeEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_target": "Self",
	"m_attributeName": "",
	"m_attributeNameToken": "",
	"m_x":
	{
		"m_spline":
		[
		],
		"m_tangents":
		[
		],
		"m_vDomainMins":
		[
			0.000000,
			0.000000
		],
		"m_vDomainMaxs":
		[
			0.000000,
			0.000000
		]
	},
	"m_y":
	{
		"m_spline":
		[
		],
		"m_tangents":
		[
		],
		"m_vDomainMins":
		[
			0.000000,
			0.000000
		],
		"m_vDomainMaxs":
		[
			0.000000,
			0.000000
		]
	},
	"m_z":
	{
		"m_spline":
		[
		],
		"m_tangents":
		[
		],
		"m_vDomainMins":
		[
			0.000000,
			0.000000
		],
		"m_vDomainMaxs":
		[
			0.000000,
			0.000000
		]
	},
	"m_w":
	{
		"m_spline":
		[
		],
		"m_tangents":
		[
		],
		"m_vDomainMins":
		[
			0.000000,
			0.000000
		],
		"m_vDomainMaxs":
		[
			0.000000,
			0.000000
		]
	}
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmMaterialAttributeEvent
    CNmMaterialAttributeEvent *-- CNmEventTargetEntity_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_target` | [CNmEventTargetEntity_t](../schemas/animlib.md#cnmeventtargetentity_t) |  |
| `m_attributeName` | CUtlString |  |
| `m_attributeNameToken` | CUtlStringToken |  |
| `m_x` | CPiecewiseCurve |  |
| `m_y` | CPiecewiseCurve |  |
| `m_z` | CPiecewiseCurve |  |
| `m_w` | CPiecewiseCurve |  |

### CNmModelSpaceBlendTask

**Inherits from:** [CNmBlendTaskBase](animlib.md#cnmblendtaskbase)

**Relationships:**

```mermaid
classDiagram
    CNmBlendTaskBase <|-- CNmModelSpaceBlendTask
    CNmPoseTask <|-- CNmBlendTaskBase
```

### CNmNotNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmNotNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmNotNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |

### CNmOrNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmOrNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_conditionNodeIndices":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmOrNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_conditionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |

### CNmOrientationWarpEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmOrientationWarpEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": ""
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmOrientationWarpEvent
```

### CNmOrientationWarpNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmOrientationWarpNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nClipReferenceNodeIdx": -1,
	"m_nTargetValueNodeIdx": -1,
	"m_bIsOffsetNode": false,
	"m_bIsOffsetRelativeToCharacter": true,
	"m_bWarpTranslation": false,
	"m_samplingMode": "WorldSpace"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmOrientationWarpNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmOrientationWarpNode::CDefinition" *-- CNmRootMotionData
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nClipReferenceNodeIdx` | int16 |  |
| `m_nTargetValueNodeIdx` | int16 |  |
| `m_bIsOffsetNode` | bool |  |
| `m_bIsOffsetRelativeToCharacter` | bool |  |
| `m_bWarpTranslation` | bool |  |
| `m_samplingMode` | [CNmRootMotionData](../schemas/animlib.md#cnmrootmotiondata)::SamplingMode_t |  |

### CNmOverlayBlendTask

**Inherits from:** [CNmBlendTaskBase](animlib.md#cnmblendtaskbase)

**Relationships:**

```mermaid
classDiagram
    CNmBlendTaskBase <|-- CNmOverlayBlendTask
    CNmPoseTask <|-- CNmBlendTaskBase
```

### CNmParameterizedBlendNode::BlendRange_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_nInputIdx0": -1,
	"m_nInputIdx1": -1,
	"m_parameterValueRange":
	{
		"m_flMin": 0.000000,
		"m_flMax": 0.000000
	}
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputIdx0` | int16 |  |
| `m_nInputIdx1` | int16 |  |
| `m_parameterValueRange` | Range_t |  |

### CNmParameterizedBlendNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Derived by:** [CNmBlend1DNode::CDefinition](animlib.md#cnmblend1dnodecdefinition), [CNmVelocityBlendNode::CDefinition](animlib.md#cnmvelocityblendnodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmParameterizedBlendNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_sourceNodeIndices":
	[
	],
	"m_nInputParameterValueNodeIdx": -1,
	"m_bAllowLooping": true
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmParameterizedBlendNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmParameterizedBlendNode::CDefinition" <|-- "CNmBlend1DNode::CDefinition"
    "CNmParameterizedBlendNode::CDefinition" <|-- "CNmVelocityBlendNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_sourceNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |
| `m_nInputParameterValueNodeIdx` | int16 |  |
| `m_bAllowLooping` | bool |  |

### CNmParameterizedBlendNode::Parameterization_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_blendRanges":
	[
	],
	"m_parameterRange":
	{
		"m_flMin": 340282346638528859811704183484516925440.000000,
		"m_flMax": -340282346638528859811704183484516925440.000000
	}
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_blendRanges` | CUtlLeanVectorFixedGrowable<CNmParameterizedBlendNode::BlendRange_t> |  |
| `m_parameterRange` | Range_t |  |

### CNmParameterizedClipSelectorNode::CDefinition

**Inherits from:** [CNmClipReferenceNode::CDefinition](animlib.md#cnmclipreferencenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmParameterizedClipSelectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_optionNodeIndices":
	[
	],
	"m_optionWeights":
	[
	],
	"m_parameterNodeIdx": -1,
	"m_bIgnoreInvalidOptions": false,
	"m_bHasWeightsSet": false
}`

**Relationships:**

```mermaid
classDiagram
    "CNmClipReferenceNode::CDefinition" <|-- "CNmParameterizedClipSelectorNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmClipReferenceNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_optionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |
| `m_optionWeights` | CUtlLeanVectorFixedGrowable<uint8> |  |
| `m_parameterNodeIdx` | int16 |  |
| `m_bIgnoreInvalidOptions` | bool |  |
| `m_bHasWeightsSet` | bool |  |

### CNmParameterizedSelectorNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmParameterizedSelectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_optionNodeIndices":
	[
	],
	"m_optionWeights":
	[
	],
	"m_parameterNodeIdx": -1,
	"m_bIgnoreInvalidOptions": false,
	"m_bHasWeightsSet": false
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmParameterizedSelectorNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_optionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |
| `m_optionWeights` | CUtlLeanVectorFixedGrowable<uint8> |  |
| `m_parameterNodeIdx` | int16 |  |
| `m_bIgnoreInvalidOptions` | bool |  |
| `m_bHasWeightsSet` | bool |  |

### CNmParticleEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmParticleEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_relevance": "ClientAndServer",
	"m_type": "Create",
	"m_target": "Self",
	"m_hParticleSystem": "",
	"m_tags": "",
	"m_bStopImmediately": false,
	"m_bDetachFromOwner": false,
	"m_bPlayEndCap": false,
	"m_attachmentPoint0": "",
	"m_attachmentType0": "PATTACH_ABSORIGIN",
	"m_attachmentPoint1": "",
	"m_attachmentType1": "PATTACH_ABSORIGIN",
	"m_config": "preview",
	"m_effectForConfig": ""
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmParticleEvent
    CNmParticleEvent *-- CNmEventRelevance_t
    CNmParticleEvent *-- CNmEventTargetEntity_t
    CNmParticleEvent *-- InfoForResourceTypeIParticleSystemDefinition
    CNmParticleEvent *-- ParticleAttachment_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_relevance` | [CNmEventRelevance_t](../schemas/animlib.md#cnmeventrelevance_t) |  |
| `m_type` | [CNmParticleEvent](../schemas/animlib.md#cnmparticleevent)::Type_t |  |
| `m_target` | [CNmEventTargetEntity_t](../schemas/animlib.md#cnmeventtargetentity_t) |  |
| `m_hParticleSystem` | CStrongHandle<[InfoForResourceTypeIParticleSystemDefinition](../schemas/resourcesystem.md#infoforresourcetypeiparticlesystemdefinition)> |  |
| `m_tags` | CUtlString |  |
| `m_bStopImmediately` | bool |  |
| `m_bDetachFromOwner` | bool |  |
| `m_bPlayEndCap` | bool |  |
| `m_attachmentPoint0` | CUtlString |  |
| `m_attachmentType0` | [ParticleAttachment_t](../schemas/animationsystem.md#particleattachment_t) |  |
| `m_attachmentPoint1` | CUtlString |  |
| `m_attachmentType1` | [ParticleAttachment_t](../schemas/animationsystem.md#particleattachment_t) |  |
| `m_config` | CUtlString |  |
| `m_effectForConfig` | CUtlString |  |

### CNmParticleEvent::Type_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Create` | 0 |  |
| `Create_CFG` | 1 |  |

### CNmPassthroughNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Derived by:** [CNmAimCSNode::CDefinition](client.md#cnmaimcsnodecdefinition), [CNmChainLookatNode::CDefinition](animlib.md#cnmchainlookatnodecdefinition), [CNmFollowBoneNode::CDefinition](animlib.md#cnmfollowbonenodecdefinition), [CNmFootIKNode::CDefinition](animlib.md#cnmfootiknodecdefinition), [CNmRootMotionOverrideNode::CDefinition](animlib.md#cnmrootmotionoverridenodecdefinition), [CNmScaleNode::CDefinition](animlib.md#cnmscalenodecdefinition), [CNmSnapWeaponNode::CDefinition](client.md#cnmsnapweaponnodecdefinition), [CNmSpeedScaleBaseNode::CDefinition](animlib.md#cnmspeedscalebasenodecdefinition), [CNmTwoBoneIKNode::CDefinition](animlib.md#cnmtwoboneiknodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmPassthroughNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmSnapWeaponNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmFootIKNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmRootMotionOverrideNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmAimCSNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmTwoBoneIKNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmSpeedScaleBaseNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmScaleNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmFollowBoneNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmChainLookatNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nChildNodeIdx` | int16 |  |

### CNmPoseNode::CDefinition

**Inherits from:** [CNmGraphNode::CDefinition](animlib.md#cnmgraphnodecdefinition)

**Derived by:** [CNmAnimationPoseNode::CDefinition](animlib.md#cnmanimationposenodecdefinition), [CNmBlend2DNode::CDefinition](animlib.md#cnmblend2dnodecdefinition), [CNmClipReferenceNode::CDefinition](animlib.md#cnmclipreferencenodecdefinition), [CNmExternalPoseNode::CDefinition](animlib.md#cnmexternalposenodecdefinition), [CNmIDBasedSelectorNode::CDefinition](animlib.md#cnmidbasedselectornodecdefinition), [CNmLayerBlendNode::CDefinition](animlib.md#cnmlayerblendnodecdefinition), [CNmOrientationWarpNode::CDefinition](animlib.md#cnmorientationwarpnodecdefinition), [CNmParameterizedBlendNode::CDefinition](animlib.md#cnmparameterizedblendnodecdefinition), [CNmParameterizedSelectorNode::CDefinition](animlib.md#cnmparameterizedselectornodecdefinition), [CNmPassthroughNode::CDefinition](animlib.md#cnmpassthroughnodecdefinition), [CNmReferencePoseNode::CDefinition](animlib.md#cnmreferenceposenodecdefinition), [CNmReferencedGraphNode::CDefinition](animlib.md#cnmreferencedgraphnodecdefinition), [CNmSelectorNode::CDefinition](animlib.md#cnmselectornodecdefinition), [CNmStateMachineNode::CDefinition](animlib.md#cnmstatemachinenodecdefinition), [CNmStateNode::CDefinition](animlib.md#cnmstatenodecdefinition), [CNmTargetWarpNode::CDefinition](animlib.md#cnmtargetwarpnodecdefinition), [CNmTransitionNode::CDefinition](animlib.md#cnmtransitionnodecdefinition), [CNmZeroPoseNode::CDefinition](animlib.md#cnmzeroposenodecdefinition)

**Relationships:**

```mermaid
classDiagram
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmAnimationPoseNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmOrientationWarpNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmZeroPoseNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmStateMachineNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmLayerBlendNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmTargetWarpNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmExternalPoseNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmReferencePoseNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmBlend2DNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmIDBasedSelectorNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmParameterizedSelectorNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmStateNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmSelectorNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmReferencedGraphNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmTransitionNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmClipReferenceNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmParameterizedBlendNode::CDefinition"
```

### CNmPoseTask

**Derived by:** [CNmAimCSTask](client.md#cnmaimcstask), [CNmBlendTaskBase](animlib.md#cnmblendtaskbase), [CNmCachedPoseReadTask](animlib.md#cnmcachedposereadtask), [CNmCachedPoseWriteTask](animlib.md#cnmcachedposewritetask), [CNmChainLookatTask](animlib.md#cnmchainlookattask), [CNmFollowBoneTask](animlib.md#cnmfollowbonetask), [CNmFootIKTask](animlib.md#cnmfootiktask), [CNmReferencePoseTask](animlib.md#cnmreferenceposetask), [CNmSampleTask](animlib.md#cnmsampletask), [CNmScaleTask](animlib.md#cnmscaletask), [CNmSnapWeaponTask](client.md#cnmsnapweapontask), [CNmTwoBoneIKTask](animlib.md#cnmtwoboneiktask), [CNmZeroPoseTask](animlib.md#cnmzeroposetask)

**Relationships:**

```mermaid
classDiagram
    CNmPoseTask <|-- CNmCachedPoseWriteTask
    CNmPoseTask <|-- CNmAimCSTask
    CNmPoseTask <|-- CNmFollowBoneTask
    CNmPoseTask <|-- CNmTwoBoneIKTask
    CNmPoseTask <|-- CNmSampleTask
    CNmPoseTask <|-- CNmChainLookatTask
    CNmPoseTask <|-- CNmReferencePoseTask
    CNmPoseTask <|-- CNmBlendTaskBase
    CNmPoseTask <|-- CNmZeroPoseTask
    CNmPoseTask <|-- CNmCachedPoseReadTask
    CNmPoseTask <|-- CNmSnapWeaponTask
    CNmPoseTask <|-- CNmScaleTask
    CNmPoseTask <|-- CNmFootIKTask
```

### CNmReferencePoseNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmReferencePoseNode::CDefinition",
	"m_nNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmReferencePoseNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

### CNmReferencePoseTask

**Inherits from:** [CNmPoseTask](animlib.md#cnmposetask)

**Relationships:**

```mermaid
classDiagram
    CNmPoseTask <|-- CNmReferencePoseTask
```

### CNmReferencedGraphNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmReferencedGraphNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nReferencedGraphIdx": -1,
	"m_nFallbackNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmReferencedGraphNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nReferencedGraphIdx` | int16 |  |
| `m_nFallbackNodeIdx` | int16 |  |

### CNmRootMotionData

**Metadata:** `MGetKV3ClassDefaults {
	"m_transforms":
	[
	],
	"m_nNumFrames": 0,
	"m_flAverageLinearVelocity": 0.000000,
	"m_flAverageAngularVelocityRadians": 0.000000,
	"m_totalDelta":
	[
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000
	]
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_transforms` | CUtlVector<CTransform> |  |
| `m_nNumFrames` | int32 |  |
| `m_flAverageLinearVelocity` | float32 |  |
| `m_flAverageAngularVelocityRadians` | float32 |  |
| `m_totalDelta` | CTransform |  |

### CNmRootMotionData::SamplingMode_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Delta` | 0 |  |
| `WorldSpace` | 1 |  |

### CNmRootMotionEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmRootMotionEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_flBlendTimeSeconds": 0.100000
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmRootMotionEvent
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flBlendTimeSeconds` | float32 |  |

### CNmRootMotionOverrideNode::CDefinition

**Inherits from:** [CNmPassthroughNode::CDefinition](animlib.md#cnmpassthroughnodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmRootMotionOverrideNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1,
	"m_desiredMovingVelocityNodeIdx": -1,
	"m_desiredFacingDirectionNodeIdx": -1,
	"m_linearVelocityLimitNodeIdx": -1,
	"m_angularVelocityLimitNodeIdx": -1,
	"m_maxLinearVelocity": -1.000000,
	"m_maxAngularVelocityRadians": -1.000000,
	"m_overrideFlags":
	{
		"m_flags": 1
	}
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPassthroughNode::CDefinition" <|-- "CNmRootMotionOverrideNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmRootMotionOverrideNode::CDefinition" *-- CNmBitFlags
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_desiredMovingVelocityNodeIdx` | int16 |  |
| `m_desiredFacingDirectionNodeIdx` | int16 |  |
| `m_linearVelocityLimitNodeIdx` | int16 |  |
| `m_angularVelocityLimitNodeIdx` | int16 |  |
| `m_maxLinearVelocity` | float32 |  |
| `m_maxAngularVelocityRadians` | float32 |  |
| `m_overrideFlags` | [CNmBitFlags](../schemas/animlib.md#cnmbitflags) |  |

### CNmRootMotionOverrideNode::OverrideFlags_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `AllowMoveX` | 0 |  |
| `AllowMoveY` | 1 |  |
| `AllowMoveZ` | 2 |  |
| `AllowFacingPitch` | 3 |  |
| `ListenForEvents` | 4 |  |

### CNmSampleTask

**Inherits from:** [CNmPoseTask](animlib.md#cnmposetask)

**Relationships:**

```mermaid
classDiagram
    CNmPoseTask <|-- CNmSampleTask
```

### CNmScaleNode::CDefinition

**Inherits from:** [CNmPassthroughNode::CDefinition](animlib.md#cnmpassthroughnodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmScaleNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1,
	"m_nMaskNodeIdx": -1,
	"m_nEnableNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPassthroughNode::CDefinition" <|-- "CNmScaleNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nMaskNodeIdx` | int16 |  |
| `m_nEnableNodeIdx` | int16 |  |

### CNmScaleTask

**Inherits from:** [CNmPoseTask](animlib.md#cnmposetask)

**Relationships:**

```mermaid
classDiagram
    CNmPoseTask <|-- CNmScaleTask
```

### CNmSelectorNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmSelectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_optionNodeIndices":
	[
	],
	"m_conditionNodeIndices":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmSelectorNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_optionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |
| `m_conditionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |

### CNmSkeleton

**Metadata:** `MGetKV3ClassDefaults {
	"m_ID": <HIDDEN FOR DIFF>,
	"m_boneIDs":
	[
	],
	"m_parentIndices":
	[
	],
	"m_parentSpaceReferencePose":
	[
	],
	"m_modelSpaceReferencePose":
	[
	],
	"m_numBonesToSampleAtLowLOD": 0,
	"m_maskDefinitions":
	[
	],
	"m_secondarySkeletons":
	[
	],
	"m_bIsPropSkeleton": false
}`

**Relationships:**

```mermaid
classDiagram
    CNmSkeleton *-- NmBoneMaskSetDefinition_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_ID` | CGlobalSymbol |  |
| `m_boneIDs` | CUtlLeanVector<CGlobalSymbol> |  |
| `m_parentIndices` | CUtlVector<int32> |  |
| `m_parentSpaceReferencePose` | CUtlVector<CTransform> |  |
| `m_modelSpaceReferencePose` | CUtlVector<CTransform> |  |
| `m_numBonesToSampleAtLowLOD` | int32 |  |
| `m_maskDefinitions` | CUtlLeanVector<[NmBoneMaskSetDefinition_t](../schemas/animlib.md#nmbonemasksetdefinition_t)> |  |
| `m_secondarySkeletons` | CUtlLeanVector<[CNmSkeleton](../schemas/animlib.md#cnmskeleton)::SecondarySkeleton_t> |  |
| `m_bIsPropSkeleton` | bool |  |

### CNmSkeleton::SecondarySkeleton_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_attachToBoneID": "",
	"m_skeleton": ""
}`

**Relationships:**

```mermaid
classDiagram
    "CNmSkeleton::SecondarySkeleton_t" *-- InfoForResourceTypeCNmSkeleton
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_attachToBoneID` | CGlobalSymbol |  |
| `m_skeleton` | CStrongHandle<[InfoForResourceTypeCNmSkeleton](../schemas/resourcesystem.md#infoforresourcetypecnmskeleton)> |  |

### CNmSoundEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmSoundEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_relevance": "ClientAndServer",
	"m_name": "",
	"m_position": "None",
	"m_attachmentName": "",
	"m_tags": "",
	"m_bContinuePlayingSoundAtDurationEnd": false,
	"m_flDurationInterruptionThreshold": 0.900000
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmSoundEvent
    CNmSoundEvent *-- CNmEventRelevance_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_relevance` | [CNmEventRelevance_t](../schemas/animlib.md#cnmeventrelevance_t) |  |
| `m_name` | CUtlString |  |
| `m_position` | [CNmSoundEvent](../schemas/animlib.md#cnmsoundevent)::Position_t |  |
| `m_attachmentName` | CUtlString |  |
| `m_tags` | CUtlString |  |
| `m_bContinuePlayingSoundAtDurationEnd` | bool |  |
| `m_flDurationInterruptionThreshold` | float32 |  |

### CNmSoundEvent::Position_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 |  |
| `World` | 1 |  |
| `EntityPos` | 2 |  |
| `EntityEyePos` | 3 |  |
| `EntityAttachment` | 4 |  |

### CNmSpeedScaleBaseNode::CDefinition

**Inherits from:** [CNmPassthroughNode::CDefinition](animlib.md#cnmpassthroughnodecdefinition)

**Derived by:** [CNmDurationScaleNode::CDefinition](animlib.md#cnmdurationscalenodecdefinition), [CNmSpeedScaleNode::CDefinition](animlib.md#cnmspeedscalenodecdefinition), [CNmVelocityBasedSpeedScaleNode::CDefinition](animlib.md#cnmvelocitybasedspeedscalenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmSpeedScaleBaseNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_flDefaultInputValue": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPassthroughNode::CDefinition" <|-- "CNmSpeedScaleBaseNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmSpeedScaleBaseNode::CDefinition" <|-- "CNmSpeedScaleNode::CDefinition"
    "CNmSpeedScaleBaseNode::CDefinition" <|-- "CNmDurationScaleNode::CDefinition"
    "CNmSpeedScaleBaseNode::CDefinition" <|-- "CNmVelocityBasedSpeedScaleNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_flDefaultInputValue` | float32 |  |

### CNmSpeedScaleNode::CDefinition

**Inherits from:** [CNmSpeedScaleBaseNode::CDefinition](animlib.md#cnmspeedscalebasenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmSpeedScaleNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_flDefaultInputValue": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    "CNmSpeedScaleBaseNode::CDefinition" <|-- "CNmSpeedScaleNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmSpeedScaleBaseNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

### CNmStateCompletedConditionNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmStateCompletedConditionNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSourceStateNodeIdx": -1,
	"m_nTransitionDurationOverrideNodeIdx": -1,
	"m_flTransitionDurationSeconds": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmStateCompletedConditionNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSourceStateNodeIdx` | int16 |  |
| `m_nTransitionDurationOverrideNodeIdx` | int16 |  |
| `m_flTransitionDurationSeconds` | float32 |  |

### CNmStateMachineNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmStateMachineNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_stateDefinitions":
	[
	],
	"m_nDefaultStateIndex": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmStateMachineNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_stateDefinitions` | CUtlLeanVectorFixedGrowable<CNmStateMachineNode::StateDefinition_t> |  |
| `m_nDefaultStateIndex` | int16 |  |

### CNmStateMachineNode::StateDefinition_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_nStateNodeIdx": -1,
	"m_nEntryConditionNodeIdx": -1,
	"m_transitionDefinitions":
	[
	]
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nStateNodeIdx` | int16 |  |
| `m_nEntryConditionNodeIdx` | int16 |  |
| `m_transitionDefinitions` | CUtlLeanVectorFixedGrowable<CNmStateMachineNode::TransitionDefinition_t> |  |

### CNmStateMachineNode::TransitionDefinition_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_nTargetStateIdx": -1,
	"m_nConditionNodeIdx": -1,
	"m_nTransitionNodeIdx": -1,
	"m_bCanBeForced": false
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nTargetStateIdx` | int16 |  |
| `m_nConditionNodeIdx` | int16 |  |
| `m_nTransitionNodeIdx` | int16 |  |
| `m_bCanBeForced` | bool |  |

### CNmStateNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmStateNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1,
	"m_entryEvents":
	[
	],
	"m_executeEvents":
	[
	],
	"m_exitEvents":
	[
	],
	"m_timedRemainingEvents":
	[
	],
	"m_timedElapsedEvents":
	[
	],
	"m_nLayerWeightNodeIdx": -1,
	"m_nLayerRootMotionWeightNodeIdx": -1,
	"m_nLayerBoneMaskNodeIdx": -1,
	"m_bIsOffState": false,
	"m_bUseActualElapsedTimeInStateForTimedEvents": false
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmStateNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nChildNodeIdx` | int16 |  |
| `m_entryEvents` | CUtlLeanVectorFixedGrowable<CGlobalSymbol> |  |
| `m_executeEvents` | CUtlLeanVectorFixedGrowable<CGlobalSymbol> |  |
| `m_exitEvents` | CUtlLeanVectorFixedGrowable<CGlobalSymbol> |  |
| `m_timedRemainingEvents` | CUtlLeanVectorFixedGrowable<CNmStateNode::TimedEvent_t> |  |
| `m_timedElapsedEvents` | CUtlLeanVectorFixedGrowable<CNmStateNode::TimedEvent_t> |  |
| `m_nLayerWeightNodeIdx` | int16 |  |
| `m_nLayerRootMotionWeightNodeIdx` | int16 |  |
| `m_nLayerBoneMaskNodeIdx` | int16 |  |
| `m_bIsOffState` | bool |  |
| `m_bUseActualElapsedTimeInStateForTimedEvents` | bool |  |

### CNmStateNode::TimedEvent_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_ID": <HIDDEN FOR DIFF>,
	"m_flTimeValueSeconds": 0.000000,
	"m_comparisionOperator": "LessThanEqual"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmStateNode::TimedEvent_t" *-- Comparison_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_ID` | CGlobalSymbol |  |
| `m_flTimeValueSeconds` | float32 |  |
| `m_comparisionOperator` | CNmStateNode::TimedEvent_t::[Comparison_t](../schemas/animgraphdoclib.md#comparison_t) |  |

### CNmStateNode::TimedEvent_t::Comparison_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `LessThanEqual` | 0 |  |
| `GreaterThanEqual` | 1 |  |

### CNmSyncEventIndexConditionNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmSyncEventIndexConditionNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nSourceStateNodeIdx": -1,
	"m_triggerMode": "ExactlyAtEventIndex",
	"m_syncEventIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmSyncEventIndexConditionNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSourceStateNodeIdx` | int16 |  |
| `m_triggerMode` | CNmSyncEventIndexConditionNode::TriggerMode_t |  |
| `m_syncEventIdx` | int32 |  |

### CNmSyncEventIndexConditionNode::TriggerMode_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `ExactlyAtEventIndex` | 0 |  |
| `GreaterThanEqualToEventIndex` | 1 |  |

### CNmSyncTrack

**Metadata:** `MGetKV3ClassDefaults {
	"m_syncEvents":
	[
		{
			"m_ID": <HIDDEN FOR DIFF>,
			"m_startTime":
			{
				"m_flValue": 0.000000
			},
			"m_duration":
			{
				"m_flValue": 1.000000
			}
		}
	],
	"m_nStartEventOffset": 0
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_syncEvents` | CUtlLeanVectorFixedGrowable<[CNmSyncTrack](../schemas/animlib.md#cnmsynctrack)::Event_t> |  |
| `m_nStartEventOffset` | int32 |  |

### CNmSyncTrack::EventMarker_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_startTime":
	{
		"m_flValue": 0.000000
	},
	"m_ID": ""
}`

**Relationships:**

```mermaid
classDiagram
    "CNmSyncTrack::EventMarker_t" *-- NmPercent_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_startTime` | [NmPercent_t](../schemas/animlib.md#nmpercent_t) |  |
| `m_ID` | CGlobalSymbol |  |

### CNmSyncTrack::Event_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_ID": <HIDDEN FOR DIFF>,
	"m_startTime":
	{
		"m_flValue": 0.000000
	},
	"m_duration":
	{
		"m_flValue": 1.000000
	}
}`

**Relationships:**

```mermaid
classDiagram
    "CNmSyncTrack::Event_t" *-- NmPercent_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_ID` | CGlobalSymbol |  |
| `m_startTime` | [NmPercent_t](../schemas/animlib.md#nmpercent_t) |  |
| `m_duration` | [NmPercent_t](../schemas/animlib.md#nmpercent_t) |  |

### CNmTarget

**Metadata:** `MGetKV3ClassDefaults {
	"m_transform":
	[
		0.000000,
		0.000000,
		0.000000,
		1.000000,
		0.000000,
		0.000000,
		0.000000,
		1.000000
	],
	"m_boneID": "",
	"m_bIsBoneTarget": false,
	"m_bIsUsingBoneSpaceOffsets": true,
	"m_bHasOffsets": false,
	"m_bIsSet": false
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_transform` | CTransform |  |
| `m_boneID` | CGlobalSymbol |  |
| `m_bIsBoneTarget` | bool |  |
| `m_bIsUsingBoneSpaceOffsets` | bool |  |
| `m_bHasOffsets` | bool |  |
| `m_bIsSet` | bool |  |

### CNmTargetInfoNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmTargetInfoNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_infoType": "Distance",
	"m_bIsWorldSpaceTarget": true
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmTargetInfoNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_infoType` | CNmTargetInfoNode::Info_t |  |
| `m_bIsWorldSpaceTarget` | bool |  |

### CNmTargetInfoNode::Info_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `AngleHorizontal` | 0 |  |
| `AngleVertical` | 1 |  |
| `Distance` | 2 |  |
| `DistanceHorizontalOnly` | 3 |  |
| `DistanceVerticalOnly` | 4 |  |
| `DeltaOrientationX` | 5 |  |
| `DeltaOrientationY` | 6 |  |
| `DeltaOrientationZ` | 7 |  |

### CNmTargetOffsetNode::CDefinition

**Inherits from:** [CNmTargetValueNode::CDefinition](animlib.md#cnmtargetvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmTargetOffsetNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_bIsBoneSpaceOffset": true,
	"m_rotationOffset":
	[
		0.000000,
		0.000000,
		0.000000,
		1.000000
	],
	"m_translationOffset":
	[
		0.000000,
		0.000000,
		0.000000
	]
}`

**Relationships:**

```mermaid
classDiagram
    "CNmTargetValueNode::CDefinition" <|-- "CNmTargetOffsetNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmTargetValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_bIsBoneSpaceOffset` | bool |  |
| `m_rotationOffset` | Quaternion |  |
| `m_translationOffset` | Vector |  |

### CNmTargetPointNode::CDefinition

**Inherits from:** [CNmVectorValueNode::CDefinition](animlib.md#cnmvectorvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmTargetPointNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_bIsWorldSpaceTarget": true
}`

**Relationships:**

```mermaid
classDiagram
    "CNmVectorValueNode::CDefinition" <|-- "CNmTargetPointNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_bIsWorldSpaceTarget` | bool |  |

### CNmTargetSelectorNode::CDefinition

**Inherits from:** [CNmClipReferenceNode::CDefinition](animlib.md#cnmclipreferencenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmTargetSelectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_optionNodeIndices":
	[
	],
	"m_flOrientationScoreWeight": 1.000000,
	"m_flPositionScoreWeight": 1.000000,
	"m_parameterNodeIdx": -1,
	"m_bIgnoreInvalidOptions": false,
	"m_bIsWorldSpaceTarget": true
}`

**Relationships:**

```mermaid
classDiagram
    "CNmClipReferenceNode::CDefinition" <|-- "CNmTargetSelectorNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmClipReferenceNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_optionNodeIndices` | CUtlLeanVectorFixedGrowable<int16> |  |
| `m_flOrientationScoreWeight` | float32 |  |
| `m_flPositionScoreWeight` | float32 |  |
| `m_parameterNodeIdx` | int16 |  |
| `m_bIgnoreInvalidOptions` | bool |  |
| `m_bIsWorldSpaceTarget` | bool |  |

### CNmTargetValueNode::CDefinition

**Inherits from:** [CNmValueNode::CDefinition](animlib.md#cnmvaluenodecdefinition)

**Derived by:** [CNmCachedTargetNode::CDefinition](animlib.md#cnmcachedtargetnodecdefinition), [CNmConstTargetNode::CDefinition](animlib.md#cnmconsttargetnodecdefinition), [CNmControlParameterTargetNode::CDefinition](animlib.md#cnmcontrolparametertargetnodecdefinition), [CNmTargetOffsetNode::CDefinition](animlib.md#cnmtargetoffsetnodecdefinition), [CNmVirtualParameterTargetNode::CDefinition](animlib.md#cnmvirtualparametertargetnodecdefinition)

**Relationships:**

```mermaid
classDiagram
    "CNmValueNode::CDefinition" <|-- "CNmTargetValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmTargetValueNode::CDefinition" <|-- "CNmControlParameterTargetNode::CDefinition"
    "CNmTargetValueNode::CDefinition" <|-- "CNmCachedTargetNode::CDefinition"
    "CNmTargetValueNode::CDefinition" <|-- "CNmConstTargetNode::CDefinition"
    "CNmTargetValueNode::CDefinition" <|-- "CNmTargetOffsetNode::CDefinition"
    "CNmTargetValueNode::CDefinition" <|-- "CNmVirtualParameterTargetNode::CDefinition"
```

### CNmTargetWarpEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmTargetWarpEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_rule": "WarpXYZ",
	"m_algorithm": "Bezier"
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmTargetWarpEvent
    CNmTargetWarpEvent *-- NmTargetWarpRule_t
    CNmTargetWarpEvent *-- NmTargetWarpAlgorithm_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_rule` | [NmTargetWarpRule_t](../schemas/animlib.md#nmtargetwarprule_t) |  |
| `m_algorithm` | [NmTargetWarpAlgorithm_t](../schemas/animlib.md#nmtargetwarpalgorithm_t) |  |

### CNmTargetWarpNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmTargetWarpNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nClipReferenceNodeIdx": -1,
	"m_nTargetValueNodeIdx": -1,
	"m_samplingMode": "Delta",
	"m_targetUpdateRule": "None",
	"m_bAlignWithTargetAtLastWarpEvent": false,
	"m_flSamplingPositionErrorThresholdSq": 0.000000,
	"m_flMaxTangentLength": 1.250000,
	"m_flLerpFallbackDistanceThreshold": 0.100000,
	"m_flTargetUpdateDistanceThreshold": 0.100000,
	"m_flTargetUpdateAngleThresholdRadians": 0.087266,
	"m_alignmentBoneID": ""
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmTargetWarpNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmTargetWarpNode::CDefinition" *-- CNmRootMotionData
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nClipReferenceNodeIdx` | int16 |  |
| `m_nTargetValueNodeIdx` | int16 |  |
| `m_samplingMode` | [CNmRootMotionData](../schemas/animlib.md#cnmrootmotiondata)::SamplingMode_t |  |
| `m_targetUpdateRule` | CNmTargetWarpNode::TargetUpdateRule_t |  |
| `m_bAlignWithTargetAtLastWarpEvent` | bool |  |
| `m_flSamplingPositionErrorThresholdSq` | float32 |  |
| `m_flMaxTangentLength` | float32 |  |
| `m_flLerpFallbackDistanceThreshold` | float32 |  |
| `m_flTargetUpdateDistanceThreshold` | float32 |  |
| `m_flTargetUpdateAngleThresholdRadians` | float32 |  |
| `m_alignmentBoneID` | CGlobalSymbol |  |

### CNmTargetWarpNode::TargetUpdateRule_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 |  |
| `Recalculate` | 1 | Recalculate Warped Root Motion |
| `Offset` | 2 | Offset Warped Root Motion |
| `RecalculateOrOffset` | 3 | Recalculate Or Offset Warped Root Motion — Will offset the warped root motion if we are pass warp events |

### CNmTimeConditionNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmTimeConditionNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_sourceStateNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_flComparand": 0.000000,
	"m_type": "ElapsedTime",
	"m_operator": "LessThan"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmTimeConditionNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_sourceStateNodeIdx` | int16 |  |
| `m_nInputValueNodeIdx` | int16 |  |
| `m_flComparand` | float32 |  |
| `m_type` | CNmTimeConditionNode::ComparisonType_t |  |
| `m_operator` | CNmTimeConditionNode::Operator_t |  |

### CNmTimeConditionNode::ComparisonType_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `PercentageThroughState` | 0 |  |
| `PercentageThroughSyncEvent` | 1 |  |
| `ElapsedTime` | 2 |  |

### CNmTimeConditionNode::Operator_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `LessThan` | 0 |  |
| `LessThanEqual` | 1 |  |
| `GreaterThan` | 2 |  |
| `GreaterThanEqual` | 3 |  |

### CNmTransitionEvent

**Inherits from:** [CNmEvent](animlib.md#cnmevent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmTransitionEvent",
	"m_flStartTime":
	{
		"m_flValue": 0.000000
	},
	"m_flDuration":
	{
		"m_flValue": 0.000000
	},
	"m_syncID": "",
	"m_rule": "BlockTransition",
	"m_ID": ""
}`

**Relationships:**

```mermaid
classDiagram
    CNmEvent <|-- CNmTransitionEvent
    CNmTransitionEvent *-- NmTransitionRule_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_rule` | [NmTransitionRule_t](../schemas/animlib.md#nmtransitionrule_t) |  |
| `m_ID` | CGlobalSymbol |  |

### CNmTransitionEventConditionNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmTransitionEventConditionNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_requireRuleID": "",
	"m_eventConditionRules":
	{
		"m_flags": 0
	},
	"m_nSourceStateNodeIdx": -1,
	"m_ruleCondition": "AnyAllowed"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmTransitionEventConditionNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmTransitionEventConditionNode::CDefinition" *-- CNmBitFlags
    "CNmTransitionEventConditionNode::CDefinition" *-- NmTransitionRuleCondition_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_requireRuleID` | CGlobalSymbol |  |
| `m_eventConditionRules` | [CNmBitFlags](../schemas/animlib.md#cnmbitflags) |  |
| `m_nSourceStateNodeIdx` | int16 |  |
| `m_ruleCondition` | [NmTransitionRuleCondition_t](../schemas/animlib.md#nmtransitionrulecondition_t) |  |

### CNmTransitionNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmTransitionNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nTargetStateNodeIdx": -1,
	"m_nDurationOverrideNodeIdx": -1,
	"m_timeOffsetOverrideNodeIdx": -1,
	"m_startBoneMaskNodeIdx": -1,
	"m_flDuration": 0.000000,
	"m_boneMaskBlendInTimePercentage":
	{
		"m_flValue": 0.330000
	},
	"m_flTimeOffset": 0.000000,
	"m_transitionOptions":
	{
		"m_flags": 1
	},
	"m_targetSyncIDNodeIdx": -1,
	"m_blendWeightEasing": "Linear",
	"m_rootMotionBlend": "Blend"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmTransitionNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmTransitionNode::CDefinition" *-- NmPercent_t
    "CNmTransitionNode::CDefinition" *-- CNmBitFlags
    "CNmTransitionNode::CDefinition" *-- NmEasingOperation_t
    "CNmTransitionNode::CDefinition" *-- NmRootMotionBlendMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nTargetStateNodeIdx` | int16 |  |
| `m_nDurationOverrideNodeIdx` | int16 |  |
| `m_timeOffsetOverrideNodeIdx` | int16 |  |
| `m_startBoneMaskNodeIdx` | int16 |  |
| `m_flDuration` | float32 |  |
| `m_boneMaskBlendInTimePercentage` | [NmPercent_t](../schemas/animlib.md#nmpercent_t) |  |
| `m_flTimeOffset` | float32 |  |
| `m_transitionOptions` | [CNmBitFlags](../schemas/animlib.md#cnmbitflags) |  |
| `m_targetSyncIDNodeIdx` | int16 |  |
| `m_blendWeightEasing` | [NmEasingOperation_t](../schemas/animlib.md#nmeasingoperation_t) |  |
| `m_rootMotionBlend` | [NmRootMotionBlendMode_t](../schemas/animlib.md#nmrootmotionblendmode_t) |  |

### CNmTransitionNode::TransitionOptions_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 |  |
| `ClampDuration` | 1 |  |
| `Synchronized` | 2 |  |
| `MatchSourceTime` | 3 |  |
| `MatchSyncEventIndex` | 4 |  |
| `MatchSyncEventID` | 5 |  |
| `MatchSyncEventPercentage` | 6 |  |
| `PreferClosestSyncEventID` | 7 |  |
| `MatchTimeInSeconds` | 8 |  |
| `OffsetTimeInSeconds` | 9 |  |

### CNmTwoBoneIKNode::CDefinition

**Inherits from:** [CNmPassthroughNode::CDefinition](animlib.md#cnmpassthroughnodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmTwoBoneIKNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1,
	"m_effectorBoneID": "",
	"m_nEffectorTargetNodeIdx": -1,
	"m_nEnabledNodeIdx": -1,
	"m_flBlendTimeSeconds": 0.000000,
	"m_blendMode": "Effector",
	"m_bIsTargetInWorldSpace": false,
	"m_flChainRotationWeight": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPassthroughNode::CDefinition" <|-- "CNmTwoBoneIKNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmTwoBoneIKNode::CDefinition" *-- NmIKBlendMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_effectorBoneID` | CGlobalSymbol |  |
| `m_nEffectorTargetNodeIdx` | int16 |  |
| `m_nEnabledNodeIdx` | int16 |  |
| `m_flBlendTimeSeconds` | float32 |  |
| `m_blendMode` | [NmIKBlendMode_t](../schemas/animlib.md#nmikblendmode_t) |  |
| `m_bIsTargetInWorldSpace` | bool |  |
| `m_flChainRotationWeight` | float32 |  |

### CNmTwoBoneIKTask

**Inherits from:** [CNmPoseTask](animlib.md#cnmposetask)

**Relationships:**

```mermaid
classDiagram
    CNmPoseTask <|-- CNmTwoBoneIKTask
    CNmTwoBoneIKTask *-- CNmTarget
    CNmTwoBoneIKTask *-- NmIKBlendMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nEffectorBoneIdx` | int32 |  |
| `m_nEffectorTargetBoneIdx` | int32 |  |
| `m_targetTransform` | CTransform |  |
| `m_effectorTarget` | [CNmTarget](../schemas/animlib.md#cnmtarget) |  |
| `m_blendMode` | [NmIKBlendMode_t](../schemas/animlib.md#nmikblendmode_t) |  |
| `m_flBlendWeight` | float32 |  |
| `m_bIsTargetInWorldSpace` | bool |  |
| `m_bIsRunningFromDeserializedData` | bool |  |
| `m_flChainRotationWeight` | float32 |  |
| `m_debugEffectorBoneID` | CGlobalSymbol |  |

### CNmValueNode::CDefinition

**Inherits from:** [CNmGraphNode::CDefinition](animlib.md#cnmgraphnodecdefinition)

**Derived by:** [CNmBoneMaskValueNode::CDefinition](animlib.md#cnmbonemaskvaluenodecdefinition), [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition), [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition), [CNmIDValueNode::CDefinition](animlib.md#cnmidvaluenodecdefinition), [CNmTargetValueNode::CDefinition](animlib.md#cnmtargetvaluenodecdefinition), [CNmVectorValueNode::CDefinition](animlib.md#cnmvectorvaluenodecdefinition)

**Relationships:**

```mermaid
classDiagram
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmTargetValueNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoneMaskValueNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
```

### CNmVectorCreateNode::CDefinition

**Inherits from:** [CNmVectorValueNode::CDefinition](animlib.md#cnmvectorvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmVectorCreateNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_inputVectorValueNodeIdx": -1,
	"m_inputValueXNodeIdx": -1,
	"m_inputValueYNodeIdx": -1,
	"m_inputValueZNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmVectorValueNode::CDefinition" <|-- "CNmVectorCreateNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_inputVectorValueNodeIdx` | int16 |  |
| `m_inputValueXNodeIdx` | int16 |  |
| `m_inputValueYNodeIdx` | int16 |  |
| `m_inputValueZNodeIdx` | int16 |  |

### CNmVectorInfoNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmVectorInfoNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_desiredInfo": "X"
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmVectorInfoNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |
| `m_desiredInfo` | CNmVectorInfoNode::Info_t |  |

### CNmVectorInfoNode::Info_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `X` | 0 |  |
| `Y` | 1 |  |
| `Z` | 2 |  |
| `Length` | 3 |  |
| `AngleHorizontal` | 4 |  |
| `AngleVertical` | 5 |  |

### CNmVectorNegateNode::CDefinition

**Inherits from:** [CNmVectorValueNode::CDefinition](animlib.md#cnmvectorvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmVectorNegateNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nInputValueNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmVectorValueNode::CDefinition" <|-- "CNmVectorNegateNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputValueNodeIdx` | int16 |  |

### CNmVectorValueNode::CDefinition

**Inherits from:** [CNmValueNode::CDefinition](animlib.md#cnmvaluenodecdefinition)

**Derived by:** [CNmCachedVectorNode::CDefinition](animlib.md#cnmcachedvectornodecdefinition), [CNmConstVectorNode::CDefinition](animlib.md#cnmconstvectornodecdefinition), [CNmControlParameterVectorNode::CDefinition](animlib.md#cnmcontrolparametervectornodecdefinition), [CNmTargetPointNode::CDefinition](animlib.md#cnmtargetpointnodecdefinition), [CNmVectorCreateNode::CDefinition](animlib.md#cnmvectorcreatenodecdefinition), [CNmVectorNegateNode::CDefinition](animlib.md#cnmvectornegatenodecdefinition), [CNmVirtualParameterVectorNode::CDefinition](animlib.md#cnmvirtualparametervectornodecdefinition)

**Relationships:**

```mermaid
classDiagram
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmVectorNegateNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmTargetPointNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmCachedVectorNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmConstVectorNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmVirtualParameterVectorNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmVectorCreateNode::CDefinition"
    "CNmVectorValueNode::CDefinition" <|-- "CNmControlParameterVectorNode::CDefinition"
```

### CNmVelocityBasedSpeedScaleNode::CDefinition

**Inherits from:** [CNmSpeedScaleBaseNode::CDefinition](animlib.md#cnmspeedscalebasenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmVelocityBasedSpeedScaleNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1,
	"m_nInputValueNodeIdx": -1,
	"m_flDefaultInputValue": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    "CNmSpeedScaleBaseNode::CDefinition" <|-- "CNmVelocityBasedSpeedScaleNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmSpeedScaleBaseNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

### CNmVelocityBlendNode::CDefinition

**Inherits from:** [CNmParameterizedBlendNode::CDefinition](animlib.md#cnmparameterizedblendnodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmVelocityBlendNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_sourceNodeIndices":
	[
	],
	"m_nInputParameterValueNodeIdx": -1,
	"m_bAllowLooping": true
}`

**Relationships:**

```mermaid
classDiagram
    "CNmParameterizedBlendNode::CDefinition" <|-- "CNmVelocityBlendNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmParameterizedBlendNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

### CNmVirtualParameterBoneMaskNode::CDefinition

**Inherits from:** [CNmBoneMaskValueNode::CDefinition](animlib.md#cnmbonemaskvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmVirtualParameterBoneMaskNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmVirtualParameterBoneMaskNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoneMaskValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nChildNodeIdx` | int16 |  |

### CNmVirtualParameterBoolNode::CDefinition

**Inherits from:** [CNmBoolValueNode::CDefinition](animlib.md#cnmboolvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmVirtualParameterBoolNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmVirtualParameterBoolNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nChildNodeIdx` | int16 |  |

### CNmVirtualParameterFloatNode::CDefinition

**Inherits from:** [CNmFloatValueNode::CDefinition](animlib.md#cnmfloatvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmVirtualParameterFloatNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmVirtualParameterFloatNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nChildNodeIdx` | int16 |  |

### CNmVirtualParameterIDNode::CDefinition

**Inherits from:** [CNmIDValueNode::CDefinition](animlib.md#cnmidvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmVirtualParameterIDNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmIDValueNode::CDefinition" <|-- "CNmVirtualParameterIDNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nChildNodeIdx` | int16 |  |

### CNmVirtualParameterTargetNode::CDefinition

**Inherits from:** [CNmTargetValueNode::CDefinition](animlib.md#cnmtargetvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmVirtualParameterTargetNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmTargetValueNode::CDefinition" <|-- "CNmVirtualParameterTargetNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmTargetValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nChildNodeIdx` | int16 |  |

### CNmVirtualParameterVectorNode::CDefinition

**Inherits from:** [CNmVectorValueNode::CDefinition](animlib.md#cnmvectorvaluenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmVirtualParameterVectorNode::CDefinition",
	"m_nNodeIdx": -1,
	"m_nChildNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmVectorValueNode::CDefinition" <|-- "CNmVirtualParameterVectorNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nChildNodeIdx` | int16 |  |

### CNmZeroPoseNode::CDefinition

**Inherits from:** [CNmPoseNode::CDefinition](animlib.md#cnmposenodecdefinition)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNmZeroPoseNode::CDefinition",
	"m_nNodeIdx": -1
}`

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmZeroPoseNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

### CNmZeroPoseTask

**Inherits from:** [CNmPoseTask](animlib.md#cnmposetask)

**Relationships:**

```mermaid
classDiagram
    CNmPoseTask <|-- CNmZeroPoseTask
```

### NmBoneMaskSetDefinition_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_ID": <HIDDEN FOR DIFF>,
	"m_primaryWeightList":
	{
		"m_skeletonName": "",
		"m_boneIDs":
		[
		],
		"m_weights":
		[
		]
	},
	"m_secondaryWeightLists":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    NmBoneMaskSetDefinition_t *-- CNmBoneWeightList
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_ID` | CGlobalSymbol |  |
| `m_primaryWeightList` | [CNmBoneWeightList](../schemas/animlib.md#cnmboneweightlist) |  |
| `m_secondaryWeightLists` | CUtlLeanVector<[CNmBoneWeightList](../schemas/animlib.md#cnmboneweightlist)> |  |

### NmCachedValueMode_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `OnEntry` | 0 |  |
| `OnExit` | 1 |  |

### NmCompressionSettings_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_translationRangeX":
	{
		"m_flRangeStart": 0.000000,
		"m_flRangeLength": -1.000000
	},
	"m_translationRangeY":
	{
		"m_flRangeStart": 0.000000,
		"m_flRangeLength": -1.000000
	},
	"m_translationRangeZ":
	{
		"m_flRangeStart": 0.000000,
		"m_flRangeLength": -1.000000
	},
	"m_scaleRange":
	{
		"m_flRangeStart": 0.000000,
		"m_flRangeLength": -1.000000
	},
	"m_nTrackReadOffset": 0,
	"m_constantRotation":
	[
		0.000000,
		0.000000,
		0.000000,
		0.000000
	],
	"m_bIsRotationStatic": false,
	"m_bIsTranslationStatic": false,
	"m_bIsScaleStatic": false
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_translationRangeX` | [NmCompressionSettings_t](../schemas/animlib.md#nmcompressionsettings_t)::QuantizationRange_t |  |
| `m_translationRangeY` | [NmCompressionSettings_t](../schemas/animlib.md#nmcompressionsettings_t)::QuantizationRange_t |  |
| `m_translationRangeZ` | [NmCompressionSettings_t](../schemas/animlib.md#nmcompressionsettings_t)::QuantizationRange_t |  |
| `m_scaleRange` | [NmCompressionSettings_t](../schemas/animlib.md#nmcompressionsettings_t)::QuantizationRange_t |  |
| `m_nTrackReadOffset` | int32 |  |
| `m_constantRotation` | Quaternion |  |
| `m_bIsRotationStatic` | bool |  |
| `m_bIsTranslationStatic` | bool |  |
| `m_bIsScaleStatic` | bool |  |

### NmCompressionSettings_t::QuantizationRange_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_flRangeStart": 0.000000,
	"m_flRangeLength": -1.000000
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flRangeStart` | float32 |  |
| `m_flRangeLength` | float32 |  |

### NmEasingFunction_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Linear` | 0 |  |
| `Quad` | 1 |  |
| `Cubic` | 2 |  |
| `Quart` | 3 |  |
| `Quint` | 4 |  |
| `Sine` | 5 |  |
| `Expo` | 6 |  |
| `Circ` | 7 |  |
| `Back` | 8 |  |

### NmEasingOperation_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Linear` | 0 |  |
| `InQuad` | 1 |  |
| `OutQuad` | 2 |  |
| `InOutQuad` | 3 |  |
| `InCubic` | 4 |  |
| `OutCubic` | 5 |  |
| `InOutCubic` | 6 |  |
| `InQuart` | 7 |  |
| `OutQuart` | 8 |  |
| `InOutQuart` | 9 |  |
| `InQuint` | 10 |  |
| `OutQuint` | 11 |  |
| `InOutQuint` | 12 |  |
| `InSine` | 13 |  |
| `OutSine` | 14 |  |
| `InOutSine` | 15 |  |
| `InExpo` | 16 |  |
| `OutExpo` | 17 |  |
| `InOutExpo` | 18 |  |
| `InCirc` | 19 |  |
| `OutCirc` | 20 |  |
| `InOutCirc` | 21 |  |
| `None` | 22 |  |

### NmEventConditionRules_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `LimitSearchToSourceState` | 0 |  |
| `IgnoreInactiveEvents` | 1 |  |
| `PreferHighestWeight` | 2 |  |
| `PreferHighestProgress` | 3 |  |
| `OperatorOr` | 4 |  |
| `OperatorAnd` | 5 |  |
| `SearchOnlyGraphEvents` | 6 |  |
| `SearchOnlyAnimEvents` | 7 |  |
| `SearchBothGraphAndAnimEvents` | 8 |  |

### NmFloatCurveCompressionSettings_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_range":
	{
		"m_flRangeStart": 0.000000,
		"m_flRangeLength": -1.000000
	},
	"m_bIsStatic": false
}`

**Relationships:**

```mermaid
classDiagram
    NmFloatCurveCompressionSettings_t *-- NmCompressionSettings_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_range` | [NmCompressionSettings_t](../schemas/animlib.md#nmcompressionsettings_t)::QuantizationRange_t |  |
| `m_bIsStatic` | bool |  |

### NmFollowBoneMode_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `RotationAndTranslation` | 0 |  |
| `RotationOnly` | 1 |  |
| `TranslationOnly` | 2 |  |

### NmFootPhaseCondition_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `LeftFootDown` | 0 |  |
| `LeftFootPassing` | 1 |  |
| `LeftPhase` | 4 |  |
| `RightFootDown` | 2 |  |
| `RightFootPassing` | 3 |  |
| `RightPhase` | 5 |  |
| `None` | 6 |  |

### NmFootPhase_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `LeftFootDown` | 0 |  |
| `RightFootPassing` | 1 |  |
| `RightFootDown` | 2 |  |
| `LeftFootPassing` | 3 |  |
| `None` | 4 |  |

### NmFrameSnapEventMode_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Floor` | 0 |  |
| `Round` | 1 |  |

### NmGraphDebugMode_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Off` | 0 |  |
| `On` | 1 |  |

### NmGraphEventTypeCondition_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Entry` | 0 |  |
| `FullyInState` | 1 |  |
| `Exit` | 2 |  |
| `Timed` | 3 |  |
| `Generic` | 4 |  |
| `Any` | 5 |  |

### NmGraphValueType_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 |  |
| `Bool` | 1 |  |
| `ID` | 2 |  |
| `Float` | 3 |  |
| `Vector` | 4 |  |
| `Target` | 5 |  |
| `BoneMask` | 6 |  |
| `Pose` | 7 |  |
| `Special` | 8 |  |

### NmIKBlendMode_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Effector` | 0 |  |
| `Pose` | 1 |  |

### NmPercent_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_flValue": 0.000000
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flValue` | float32 |  |

### NmPoseBlendMode_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Overlay` | 0 |  |
| `Additive` | 1 |  |
| `ModelSpace` | 2 |  |

### NmRootMotionBlendMode_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Blend` | 0 |  |
| `Additive` | 1 |  |
| `IgnoreSource` | 2 |  |
| `IgnoreTarget` | 3 |  |

### NmSyncTrackTimeRange_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_startTime":
	{
		"m_nEventIdx": 0,
		"m_percentageThrough":
		{
			"m_flValue": 0.000000
		}
	},
	"m_endTime":
	{
		"m_nEventIdx": 0,
		"m_percentageThrough":
		{
			"m_flValue": 0.000000
		}
	}
}`

**Relationships:**

```mermaid
classDiagram
    NmSyncTrackTimeRange_t *-- NmSyncTrackTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_startTime` | [NmSyncTrackTime_t](../schemas/animlib.md#nmsynctracktime_t) |  |
| `m_endTime` | [NmSyncTrackTime_t](../schemas/animlib.md#nmsynctracktime_t) |  |

### NmSyncTrackTime_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_nEventIdx": 0,
	"m_percentageThrough":
	{
		"m_flValue": 0.000000
	}
}`

**Relationships:**

```mermaid
classDiagram
    NmSyncTrackTime_t *-- NmPercent_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nEventIdx` | int32 |  |
| `m_percentageThrough` | [NmPercent_t](../schemas/animlib.md#nmpercent_t) |  |

### NmTargetWarpAlgorithm_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `Lerp` | 0 |  |
| `Hermite` | 1 |  |
| `HermiteFeaturePreserving` | 2 |  |
| `Bezier` | 3 |  |

### NmTargetWarpRule_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `WarpXY` | 0 |  |
| `WarpZ` | 1 |  |
| `WarpXYZ` | 2 |  |
| `RotationOnly` | 3 |  |
| `FixedSection` | 4 |  |

### NmTransitionRuleCondition_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `AnyAllowed` | 0 | Any Allowed |
| `FullyAllowed` | 1 | Fully Allowed |
| `ConditionallyAllowed` | 2 | Conditionally Allowed |
| `Blocked` | 3 | Blocked |

### NmTransitionRule_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `AllowTransition` | 0 | Fully Allowed |
| `ConditionallyAllowTransition` | 1 | Conditionally Allowed |
| `BlockTransition` | 2 | Blocked |
