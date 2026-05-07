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
    CModelConfigElement <|-- CModelConfigElement_AttachedModel
    CModelConfigElement <|-- CModelConfigElement_SetRenderColor
    CBaseConstraint <|-- COrientConstraint
    CBaseConstraint <|-- CPointConstraint
    CBoneConstraintBase <|-- CBoneConstraintDotToMorph
    CBoneConstraintBase <|-- CBoneConstraintPoseSpaceMorph
    CBaseConstraint <|-- CBoneConstraintPoseSpaceBone
    CBaseConstraint <|-- CTiltTwistConstraint
    CBoneConstraintBase <|-- CBoneConstraintRbf
    CBaseConstraint <|-- CTwistConstraint
    CBaseConstraint <|-- CMorphConstraint
    CModelConfigElement <|-- CModelConfigElement_SetMaterialGroup
    CModelConfigElement <|-- CModelConfigElement_SetBodygroupOnAttachedModels
    CModelConfigElement <|-- CModelConfigElement_Command
    CBaseConstraint <|-- CParentConstraint
    CModelConfigElement <|-- CModelConfigElement_RandomColor
    CModelConfigElement <|-- CModelConfigElement_SetBodygroup
    CModelConfigElement <|-- CModelConfigElement_RandomPick
    CBoneConstraintBase <|-- CBaseConstraint
    CBaseConstraint <|-- CAimConstraint
    CModelConfigElement <|-- CModelConfigElement_UserPick
    CModelConfigElement <|-- CModelConfigElement_SetMaterialGroupOnAttachedModels
    CCycleBase <|-- CAnimCycle
    CCycleBase <|-- CFootCycle
    CModelConfigElement_AttachedModel *-- ModelConfigAttachmentType_t
    ModelEmbeddedMesh_t *-- ModelMeshBufferData_t
    RenderInputLayoutField_t *-- RenderSlotType_t
    VPhysXBodyPart_t *-- VPhysics2ShapeDef_t
    CFootTrajectories *-- CFootTrajectory
    VsInputSignature_t *-- VsInputSignatureElement_t
    CRenderSkeleton *-- RenderSkeletonBone_t
    CVPhysXSurfacePropertiesList --> CPhysSurfaceProperties
    CRenderGroom *-- RenderHairStrandInfo_t
    CFlexRule *-- CFlexOp
    RenderSkeletonBone_t *-- SkeletonBoneBounds_t
    ModelBoneFlexDriverControl_t *-- ModelBoneFlexComponent_t
    CAnimSkeleton *-- CAnimFoot
    CRenderMesh *-- CSceneObjectData
    CRenderMesh --> CBaseConstraint
    CRenderMesh *-- CRenderSkeleton
    CRenderMesh *-- DynamicMeshDeformParams_t
    CRenderMesh --> CRenderGroom
    SkeletonDemoDb_t --> SkeletonAnimCapture_t
    CMorphSetData *-- MorphBundleType_t
    CMorphSetData *-- CMorphData
    CMorphSetData *-- CFlexDesc
    CMorphSetData *-- CFlexController
    CMorphSetData *-- CFlexRule
    CMeshletDescriptor *-- CDrawCullingData
    CFootCycleDefinition *-- CAnimCycle
    CFootCycleDefinition *-- CFootCycle
    CHitBoxSet *-- CHitBox
    "CSceneObjectData::RTProxyDrawDescriptor_t" *-- CMaterialDrawDescriptor
    "CSceneObjectData::RTProxyDrawDescriptor_t" *-- VertexAlbedoFormat_t
    CFootStride *-- CFootCycleDefinition
    CFootStride *-- CFootTrajectories
    CFlexOp *-- FlexOpCode_t
    "SkeletonAnimCapture_t::Frame_t" *-- SkeletonAnimCapture_t
    ModelMeshBufferData_t *-- RenderInputLayoutField_t
    PermModelData_t *-- PermModelInfo_t
    PermModelData_t *-- PermModelExtPart_t
    PermModelData_t *-- MaterialGroup_t
    PermModelData_t *-- ModelSkeletonData_t
    PermModelData_t *-- ModelBoneFlexDriver_t
    PermModelData_t --> CModelConfigList
    PermModelData_t *-- PermModelDataAnimatedMaterialAttribute_t
    PermModelData_t *-- ModelAnimGraph2Ref_t
    CMorphRectData *-- CMorphBundleData
    CFootMotion *-- CFootStride
    CPhysSurfaceProperties *-- CPhysSurfacePropertiesPhysics
    CPhysSurfaceProperties *-- CPhysSurfacePropertiesVehicle
    CPhysSurfaceProperties *-- CPhysSurfacePropertiesSoundNames
    CPhysSurfaceProperties *-- CPhysSurfacePropertiesAudio
    CHitBoxSetList *-- CHitBoxSet
    CNPCPhysicsHull *-- NPCPhysicsHullType_t
    VPhysXConstraint2_t *-- VPhysXConstraintParams_t
    CBaseConstraint *-- CConstraintSlave
    CBaseConstraint *-- CConstraintTarget
    CMaterialDrawDescriptor *-- RenderPrimitiveType_t
    CMaterialDrawDescriptor *-- CRenderBufferBinding
    VPhysXAggregateData_t *-- VPhysXBodyPart_t
    VPhysXAggregateData_t *-- PhysShapeMarkup_t
    VPhysXAggregateData_t *-- VPhysXConstraint2_t
    VPhysXAggregateData_t *-- VPhysXJoint_t
    VPhysXAggregateData_t *-- VPhysXCollisionAttributes_t
    CModelConfig --> CModelConfigElement
    VPhysXJoint_t *-- VPhysXRange_t
    CMorphData *-- CMorphRectData
    ModelBoneFlexDriver_t *-- ModelBoneFlexDriverControl_t
    CModelConfigList --> CModelConfig
    CSceneObjectData *-- CMaterialDrawDescriptor
    CSceneObjectData *-- CMeshletDescriptor
```
