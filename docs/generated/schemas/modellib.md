---
title: modellib
module: modellib
---

# Module: modellib

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

[📊 View UML Diagram](../diagrams/modellib.md)

140 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [AnimComponentID](modellib/AnimComponentID.md) | class | 4 | 1 |  |
| [AnimNodeID](modellib/AnimNodeID.md) | class | 4 | 1 |  |
| [AnimNodeOutputID](modellib/AnimNodeOutputID.md) | class | 4 | 1 |  |
| [AnimParamID](modellib/AnimParamID.md) | class | 4 | 1 |  |
| [AnimScriptHandle](modellib/AnimScriptHandle.md) | class | 4 | 1 |  |
| [AnimStateID](modellib/AnimStateID.md) | class | 4 | 1 |  |
| [AnimTagID](modellib/AnimTagID.md) | class | 4 | 1 |  |
| [AttachmentHandle_t](modellib/AttachmentHandle_t.md) | class | 1 | 1 |  |
| [CAimConstraint](modellib/CAimConstraint.md) | class | 128 | 2 | [CBaseConstraint](modellib/CBaseConstraint.md) |
| [CAnimAttachment](modellib/CAnimAttachment.md) | class | 128 | 5 |  |
| [CAnimCycle](modellib/CAnimCycle.md) | class | 4 | 0 | [CCycleBase](modellib/CCycleBase.md) |
| [CAnimFoot](modellib/CAnimFoot.md) | class | 40 | 5 |  |
| [CAnimSkeleton](modellib/CAnimSkeleton.md) | class | 208 | 8 |  |
| [CAttachment](modellib/CAttachment.md) | class | 144 | 8 |  |
| [CBaseConstraint](modellib/CBaseConstraint.md) | class | 96 | 4 | [CBoneConstraintBase](modellib/CBoneConstraintBase.md) |
| [CBoneConstraintBase](modellib/CBoneConstraintBase.md) | class | 32 | 0 |  |
| [CBoneConstraintDotToMorph](modellib/CBoneConstraintDotToMorph.md) | class | 88 | 4 | [CBoneConstraintBase](modellib/CBoneConstraintBase.md) |
| [CBoneConstraintPoseSpaceBone](modellib/CBoneConstraintPoseSpaceBone.md) | class | 136 | 1 | [CBaseConstraint](modellib/CBaseConstraint.md) |
| [CBoneConstraintPoseSpaceBone::Input_t](modellib/CBoneConstraintPoseSpaceBone.Input_t.md) | class | 40 | 2 |  |
| [CBoneConstraintPoseSpaceMorph](modellib/CBoneConstraintPoseSpaceMorph.md) | class | 160 | 5 | [CBoneConstraintBase](modellib/CBoneConstraintBase.md) |
| [CBoneConstraintPoseSpaceMorph::Input_t](modellib/CBoneConstraintPoseSpaceMorph.Input_t.md) | class | 40 | 2 |  |
| [CBoneConstraintRbf](modellib/CBoneConstraintRbf.md) | class | 200 | 2 | [CBoneConstraintBase](modellib/CBoneConstraintBase.md) |
| [CConstraintSlave](modellib/CConstraintSlave.md) | class | 80 | 5 |  |
| [CConstraintTarget](modellib/CConstraintTarget.md) | class | 96 | 6 |  |
| [CCycleBase](modellib/CCycleBase.md) | class | 4 | 1 |  |
| [CDrawCullingData](modellib/CDrawCullingData.md) | class | 4 | 2 |  |
| [CFlexController](modellib/CFlexController.md) | class | 24 | 4 |  |
| [CFlexDesc](modellib/CFlexDesc.md) | class | 8 | 1 |  |
| [CFlexOp](modellib/CFlexOp.md) | class | 8 | 2 |  |
| [CFlexRule](modellib/CFlexRule.md) | class | 32 | 2 |  |
| [CFootCycle](modellib/CFootCycle.md) | class | 4 | 0 | [CCycleBase](modellib/CCycleBase.md) |
| [CFootCycleDefinition](modellib/CFootCycleDefinition.md) | class | 60 | 9 |  |
| [CFootDefinition](modellib/CFootDefinition.md) | class | 64 | 9 |  |
| [CFootMotion](modellib/CFootMotion.md) | class | 40 | 3 |  |
| [CFootStride](modellib/CFootStride.md) | class | 88 | 2 |  |
| [CFootTrajectories](modellib/CFootTrajectories.md) | class | 24 | 1 |  |
| [CFootTrajectory](modellib/CFootTrajectory.md) | class | 32 | 3 |  |
| [CHitBox](modellib/CHitBox.md) | class | 112 | 13 |  |
| [CHitBoxSet](modellib/CHitBoxSet.md) | class | 48 | 4 |  |
| [CHitBoxSetList](modellib/CHitBoxSetList.md) | class | 24 | 1 |  |
| [CMaterialDrawDescriptor](modellib/CMaterialDrawDescriptor.md) | class | 280 | 18 |  |
| [CMaterialDrawDescriptor::RigidMeshPart_t](modellib/CMaterialDrawDescriptor.RigidMeshPart_t.md) | class | 12 | 4 |  |
| [CMeshletDescriptor](modellib/CMeshletDescriptor.md) | class | 24 | 6 |  |
| [CModelConfig](modellib/CModelConfig.md) | class | 40 | 4 |  |
| [CModelConfigElement](modellib/CModelConfigElement.md) | class | 72 | 2 |  |
| [CModelConfigElement_AttachedModel](modellib/CModelConfigElement_AttachedModel.md) | class | 232 | 13 | [CModelConfigElement](modellib/CModelConfigElement.md) |
| [CModelConfigElement_Command](modellib/CModelConfigElement_Command.md) | class | 96 | 2 | [CModelConfigElement](modellib/CModelConfigElement.md) |
| [CModelConfigElement_RandomColor](modellib/CModelConfigElement_RandomColor.md) | class | 96 | 1 | [CModelConfigElement](modellib/CModelConfigElement.md) |
| [CModelConfigElement_RandomPick](modellib/CModelConfigElement_RandomPick.md) | class | 128 | 2 | [CModelConfigElement](modellib/CModelConfigElement.md) |
| [CModelConfigElement_SetBodygroup](modellib/CModelConfigElement_SetBodygroup.md) | class | 88 | 2 | [CModelConfigElement](modellib/CModelConfigElement.md) |
| [CModelConfigElement_SetBodygroupOnAttachedModels](modellib/CModelConfigElement_SetBodygroupOnAttachedModels.md) | class | 88 | 2 | [CModelConfigElement](modellib/CModelConfigElement.md) |
| [CModelConfigElement_SetMaterialGroup](modellib/CModelConfigElement_SetMaterialGroup.md) | class | 80 | 1 | [CModelConfigElement](modellib/CModelConfigElement.md) |
| [CModelConfigElement_SetMaterialGroupOnAttachedModels](modellib/CModelConfigElement_SetMaterialGroupOnAttachedModels.md) | class | 80 | 1 | [CModelConfigElement](modellib/CModelConfigElement.md) |
| [CModelConfigElement_SetRenderColor](modellib/CModelConfigElement_SetRenderColor.md) | class | 80 | 1 | [CModelConfigElement](modellib/CModelConfigElement.md) |
| [CModelConfigElement_UserPick](modellib/CModelConfigElement_UserPick.md) | class | 96 | 1 | [CModelConfigElement](modellib/CModelConfigElement.md) |
| [CModelConfigList](modellib/CModelConfigList.md) | class | 32 | 3 |  |
| [CMorphBundleData](modellib/CMorphBundleData.md) | class | 56 | 4 |  |
| [CMorphConstraint](modellib/CMorphConstraint.md) | class | 128 | 4 | [CBaseConstraint](modellib/CBaseConstraint.md) |
| [CMorphData](modellib/CMorphData.md) | class | 32 | 2 |  |
| [CMorphRectData](modellib/CMorphRectData.md) | class | 40 | 5 |  |
| [CMorphSetData](modellib/CMorphSetData.md) | class | 152 | 8 |  |
| [CNPCPhysicsHull](modellib/CNPCPhysicsHull.md) | class | 64 | 8 |  |
| [COrientConstraint](modellib/COrientConstraint.md) | class | 96 | 0 | [CBaseConstraint](modellib/CBaseConstraint.md) |
| [CParentConstraint](modellib/CParentConstraint.md) | class | 96 | 0 | [CBaseConstraint](modellib/CBaseConstraint.md) |
| [CPhysSurfaceProperties](modellib/CPhysSurfaceProperties.md) | class | 200 | 9 |  |
| [CPhysSurfacePropertiesAudio](modellib/CPhysSurfacePropertiesAudio.md) | class | 32 | 8 |  |
| [CPhysSurfacePropertiesPhysics](modellib/CPhysSurfacePropertiesPhysics.md) | class | 24 | 6 |  |
| [CPhysSurfacePropertiesSoundNames](modellib/CPhysSurfacePropertiesSoundNames.md) | class | 96 | 12 |  |
| [CPhysSurfacePropertiesVehicle](modellib/CPhysSurfacePropertiesVehicle.md) | class | 8 | 2 |  |
| [CPointConstraint](modellib/CPointConstraint.md) | class | 96 | 0 | [CBaseConstraint](modellib/CBaseConstraint.md) |
| [CRenderBufferBinding](modellib/CRenderBufferBinding.md) | class | 32 | 2 |  |
| [CRenderGroom](modellib/CRenderGroom.md) | class | 176 | 14 |  |
| [CRenderMesh](modellib/CRenderMesh.md) | class | 552 | 7 |  |
| [CRenderSkeleton](modellib/CRenderSkeleton.md) | class | 80 | 3 |  |
| [CSceneObjectData](modellib/CSceneObjectData.md) | class | 184 | 7 |  |
| [CSceneObjectData::RTProxyDrawDescriptor_t](modellib/CSceneObjectData.RTProxyDrawDescriptor_t.md) | class | 352 | 13 |  |
| [CTiltTwistConstraint](modellib/CTiltTwistConstraint.md) | class | 144 | 2 | [CBaseConstraint](modellib/CBaseConstraint.md) |
| [CTwistConstraint](modellib/CTwistConstraint.md) | class | 144 | 3 | [CBaseConstraint](modellib/CBaseConstraint.md) |
| [CVPhysXSurfacePropertiesList](modellib/CVPhysXSurfacePropertiesList.md) | class | 24 | 1 |  |
| [DynamicMeshDeformParams_t](modellib/DynamicMeshDeformParams_t.md) | class | 12 | 6 |  |
| [MaterialGroup_t](modellib/MaterialGroup_t.md) | class | 32 | 2 |  |
| [ModelAnimGraph2Ref_t](modellib/ModelAnimGraph2Ref_t.md) | class | 16 | 2 |  |
| [ModelBoneFlexDriverControl_t](modellib/ModelBoneFlexDriverControl_t.md) | class | 32 | 5 |  |
| [ModelBoneFlexDriver_t](modellib/ModelBoneFlexDriver_t.md) | class | 40 | 3 |  |
| [ModelEmbeddedMesh_t](modellib/ModelEmbeddedMesh_t.md) | class | 112 | 9 |  |
| [ModelMeshBufferData_t](modellib/ModelMeshBufferData_t.md) | class | 48 | 13 |  |
| [ModelSkeletonData_t](modellib/ModelSkeletonData_t.md) | class | 168 | 7 |  |
| [PermModelDataAnimatedMaterialAttribute_t](modellib/PermModelDataAnimatedMaterialAttribute_t.md) | class | 16 | 2 |  |
| [PermModelData_t](modellib/PermModelData_t.md) | class | 760 | 25 |  |
| [PermModelExtPart_t](modellib/PermModelExtPart_t.md) | class | 64 | 4 |  |
| [PermModelInfo_t](modellib/PermModelInfo_t.md) | class | 88 | 10 |  |
| [PhysShapeMarkup_t](modellib/PhysShapeMarkup_t.md) | class | 16 | 3 |  |
| [PhysSoftbodyDesc_t](modellib/PhysSoftbodyDesc_t.md) | class | 144 | 6 |  |
| [RenderHairStrandInfo_t](modellib/RenderHairStrandInfo_t.md) | class | 40 | 7 |  |
| [RenderInputLayoutField_t](modellib/RenderInputLayoutField_t.md) | class | 76 | 6 |  |
| [RenderSkeletonBone_t](modellib/RenderSkeletonBone_t.md) | class | 96 | 5 |  |
| [SheetSequenceIntegerId_t](modellib/SheetSequenceIntegerId_t.md) | class | 4 | 1 |  |
| [SkeletonAnimCapture_t](modellib/SkeletonAnimCapture_t.md) | class | 192 | 10 |  |
| [SkeletonAnimCapture_t::Bone_t](modellib/SkeletonAnimCapture_t.Bone_t.md) | class | 64 | 3 |  |
| [SkeletonAnimCapture_t::Camera_t](modellib/SkeletonAnimCapture_t.Camera_t.md) | class | 48 | 2 |  |
| [SkeletonAnimCapture_t::FrameStamp_t](modellib/SkeletonAnimCapture_t.FrameStamp_t.md) | class | 28 | 8 |  |
| [SkeletonAnimCapture_t::Frame_t](modellib/SkeletonAnimCapture_t.Frame_t.md) | class | 192 | 9 |  |
| [SkeletonBoneBounds_t](modellib/SkeletonBoneBounds_t.md) | class | 24 | 2 |  |
| [SkeletonDemoDb_t](modellib/SkeletonDemoDb_t.md) | class | 56 | 3 |  |
| [VPhysXAggregateData_t](modellib/VPhysXAggregateData_t.md) | class | 336 | 17 |  |
| [VPhysXBodyPart_t](modellib/VPhysXBodyPart_t.md) | class | 168 | 12 |  |
| [VPhysXCollisionAttributes_t](modellib/VPhysXCollisionAttributes_t.md) | class | 208 | 11 |  |
| [VPhysXConstraint2_t](modellib/VPhysXConstraint2_t.md) | class | 256 | 4 |  |
| [VPhysXConstraintParams_t](modellib/VPhysXConstraintParams_t.md) | class | 248 | 46 |  |
| [VPhysXJoint_t](modellib/VPhysXJoint_t.md) | class | 208 | 30 |  |
| [VPhysXRange_t](modellib/VPhysXRange_t.md) | class | 8 | 2 |  |
| [VPhysics2ShapeDef_t](modellib/VPhysics2ShapeDef_t.md) | class | 120 | 5 |  |
| [VsInputSignatureElement_t](modellib/VsInputSignatureElement_t.md) | class | 196 | 4 |  |
| [VsInputSignature_t](modellib/VsInputSignature_t.md) | class | 48 | 2 |  |
| [FlexOpCode_t](modellib/FlexOpCode_t.md) | enum | — | 26 |  |
| [InputLayoutVariation_t](modellib/InputLayoutVariation_t.md) | enum | — | 4 |  |
| [MeshDrawPrimitiveFlags_t](modellib/MeshDrawPrimitiveFlags_t.md) | enum | — | 8 |  |
| [ModelBoneFlexComponent_t](modellib/ModelBoneFlexComponent_t.md) | enum | — | 4 |  |
| [ModelConfigAttachmentType_t](modellib/ModelConfigAttachmentType_t.md) | enum | — | 5 |  |
| [ModelMeshBufferUsage_t](modellib/ModelMeshBufferUsage_t.md) | enum | — | 8 |  |
| [ModelSkeletonData_t::BoneFlags_t](modellib/ModelSkeletonData_t.BoneFlags_t.md) | enum | — | 22 |  |
| [MorphBundleType_t](modellib/MorphBundleType_t.md) | enum | — | 4 |  |
| [MorphFlexControllerRemapType_t](modellib/MorphFlexControllerRemapType_t.md) | enum | — | 4 |  |
| [MovementCapability_t](modellib/MovementCapability_t.md) | enum | — | 10 |  |
| [NPCPhysicsHullType_t](modellib/NPCPhysicsHullType_t.md) | enum | — | 7 |  |
| [PermModelInfo_t::FlagEnum](modellib/PermModelInfo_t.FlagEnum.md) | enum | — | 15 |  |
| [RenderBufferFlags_t](modellib/RenderBufferFlags_t.md) | enum | — | 14 |  |
| [RenderMeshSlotType_t](modellib/RenderMeshSlotType_t.md) | enum | — | 3 |  |
| [RenderMultisampleType_t](modellib/RenderMultisampleType_t.md) | enum | — | 8 |  |
| [RenderPrimitiveType_t](modellib/RenderPrimitiveType_t.md) | enum | — | 14 |  |
| [RenderSlotType_t](modellib/RenderSlotType_t.md) | enum | — | 3 |  |
| [ScriptedHeldWeaponBehavior_t](modellib/ScriptedHeldWeaponBehavior_t.md) | enum | — | 4 |  |
| [ScriptedMoveTo_t](modellib/ScriptedMoveTo_t.md) | enum | — | 6 |  |
| [SharedMovementGait_t](modellib/SharedMovementGait_t.md) | enum | — | 6 |  |
| [UpscalerType_t](modellib/UpscalerType_t.md) | enum | — | 6 |  |
| [VPhysXAggregateData_t::VPhysXFlagEnum_t](modellib/VPhysXAggregateData_t.VPhysXFlagEnum_t.md) | enum | — | 3 |  |
| [VPhysXBodyPart_t::VPhysXFlagEnum_t](modellib/VPhysXBodyPart_t.VPhysXFlagEnum_t.md) | enum | — | 6 |  |
| [VPhysXConstraintParams_t::EnumFlags0_t](modellib/VPhysXConstraintParams_t.EnumFlags0_t.md) | enum | — | 4 |  |
| [VPhysXJoint_t::Flags_t](modellib/VPhysXJoint_t.Flags_t.md) | enum | — | 3 |  |
| [VertexAlbedoFormat_t](modellib/VertexAlbedoFormat_t.md) | enum | — | 3 |  |
