---
layout: default
title: "UML: modellib"
parent: Schemas
nav_exclude: true
---

# UML: modellib

Class relationships (inheritance and composition) for the `modellib` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CBaseConstraint <|-- CAimConstraint
    CCycleBase <|-- CAnimCycle
    CBoneConstraintBase <|-- CBaseConstraint
    CBoneConstraintBase <|-- CBoneConstraintDotToMorph
    CBaseConstraint <|-- CBoneConstraintPoseSpaceBone
    CBoneConstraintBase <|-- CBoneConstraintPoseSpaceMorph
    CBoneConstraintBase <|-- CBoneConstraintRbf
    CCycleBase <|-- CFootCycle
    CModelConfigElement <|-- CModelConfigElement_AttachedModel
    CModelConfigElement <|-- CModelConfigElement_Command
    CModelConfigElement <|-- CModelConfigElement_RandomColor
    CModelConfigElement <|-- CModelConfigElement_RandomPick
    CModelConfigElement <|-- CModelConfigElement_SetBodygroup
    CModelConfigElement <|-- CModelConfigElement_SetBodygroupOnAttachedModels
    CModelConfigElement <|-- CModelConfigElement_SetMaterialGroup
    CModelConfigElement <|-- CModelConfigElement_SetMaterialGroupOnAttachedModels
    CModelConfigElement <|-- CModelConfigElement_SetRenderColor
    CModelConfigElement <|-- CModelConfigElement_UserPick
    CBaseConstraint <|-- CMorphConstraint
    CBaseConstraint <|-- COrientConstraint
    CBaseConstraint <|-- CParentConstraint
    CBaseConstraint <|-- CPointConstraint
    CBaseConstraint <|-- CTiltTwistConstraint
    CBaseConstraint <|-- CTwistConstraint
    CAnimSkeleton *-- CAnimFoot
    CBaseConstraint *-- CConstraintSlave
    CBaseConstraint *-- CConstraintTarget
    CBoneConstraintPoseSpaceBone *-- `CBoneConstraintPoseSpaceBone::Input_t`
    CBoneConstraintPoseSpaceMorph *-- `CBoneConstraintPoseSpaceMorph::Input_t`
    CFlexOp *-- FlexOpCode_t
    CFlexRule *-- CFlexOp
    CFootCycleDefinition *-- CAnimCycle
    CFootCycleDefinition *-- CFootCycle
    CFootMotion *-- CFootStride
    CFootStride *-- CFootCycleDefinition
    CFootStride *-- CFootTrajectories
    CFootTrajectories *-- CFootTrajectory
    CHitBoxSet *-- CHitBox
    CHitBoxSetList *-- CHitBoxSet
    CMaterialDrawDescriptor *-- `CMaterialDrawDescriptor::RigidMeshPart_t`
    CMaterialDrawDescriptor *-- RenderPrimitiveType_t
    CMaterialDrawDescriptor *-- CRenderBufferBinding
    CMeshletDescriptor *-- CDrawCullingData
    CModelConfig --> CModelConfigElement
    CModelConfigElement_AttachedModel *-- ModelConfigAttachmentType_t
    CModelConfigList --> CModelConfig
    CMorphData *-- CMorphRectData
    CMorphRectData *-- CMorphBundleData
    CMorphSetData *-- MorphBundleType_t
    CMorphSetData *-- CMorphData
    CMorphSetData *-- CFlexDesc
    CMorphSetData *-- CFlexController
    CMorphSetData *-- CFlexRule
    CNPCPhysicsHull *-- NPCPhysicsHullType_t
    CPhysSurfaceProperties *-- CPhysSurfacePropertiesPhysics
    CPhysSurfaceProperties *-- CPhysSurfacePropertiesVehicle
    CPhysSurfaceProperties *-- CPhysSurfacePropertiesSoundNames
    CPhysSurfaceProperties *-- CPhysSurfacePropertiesAudio
    CRenderGroom *-- RenderHairStrandInfo_t
    CRenderMesh *-- CSceneObjectData
    CRenderMesh --> CBaseConstraint
    CRenderMesh *-- CRenderSkeleton
    CRenderMesh *-- DynamicMeshDeformParams_t
    CRenderMesh --> CRenderGroom
    CRenderSkeleton *-- RenderSkeletonBone_t
    CSceneObjectData *-- CMaterialDrawDescriptor
    CSceneObjectData *-- CMeshletDescriptor
    CSceneObjectData *-- `CSceneObjectData::RTProxyDrawDescriptor_t`
    `CSceneObjectData::RTProxyDrawDescriptor_t` *-- CMaterialDrawDescriptor
    `CSceneObjectData::RTProxyDrawDescriptor_t` *-- VertexAlbedoFormat_t
    CVPhysXSurfacePropertiesList --> CPhysSurfaceProperties
    ModelBoneFlexDriverControl_t *-- ModelBoneFlexComponent_t
    ModelBoneFlexDriver_t *-- ModelBoneFlexDriverControl_t
    ModelEmbeddedMesh_t *-- ModelMeshBufferData_t
    ModelMeshBufferData_t *-- RenderInputLayoutField_t
    PermModelData_t *-- PermModelInfo_t
    PermModelData_t *-- PermModelExtPart_t
    PermModelData_t *-- MaterialGroup_t
    PermModelData_t *-- ModelSkeletonData_t
    PermModelData_t *-- ModelBoneFlexDriver_t
    PermModelData_t --> CModelConfigList
    PermModelData_t *-- PermModelDataAnimatedMaterialAttribute_t
    PermModelData_t *-- ModelAnimGraph2Ref_t
    RenderInputLayoutField_t *-- RenderSlotType_t
    RenderSkeletonBone_t *-- SkeletonBoneBounds_t
    SkeletonAnimCapture_t *-- `SkeletonAnimCapture_t::Bone_t`
    SkeletonAnimCapture_t *-- `SkeletonAnimCapture_t::Frame_t`
    `SkeletonAnimCapture_t::Frame_t` *-- `SkeletonAnimCapture_t::FrameStamp_t`
    SkeletonDemoDb_t --> SkeletonAnimCapture_t
    SkeletonDemoDb_t *-- `SkeletonAnimCapture_t::Camera_t`
    VPhysXAggregateData_t *-- VPhysXBodyPart_t
    VPhysXAggregateData_t *-- PhysShapeMarkup_t
    VPhysXAggregateData_t *-- VPhysXConstraint2_t
    VPhysXAggregateData_t *-- VPhysXJoint_t
    VPhysXAggregateData_t *-- VPhysXCollisionAttributes_t
    VPhysXBodyPart_t *-- VPhysics2ShapeDef_t
    VPhysXConstraint2_t *-- VPhysXConstraintParams_t
    VPhysXJoint_t *-- VPhysXRange_t
    VsInputSignature_t *-- VsInputSignatureElement_t
```
