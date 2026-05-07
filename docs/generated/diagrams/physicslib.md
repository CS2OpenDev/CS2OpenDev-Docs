---
layout: default
title: "UML: physicslib"
parent: Schemas
nav_exclude: true
---

# UML: physicslib

Class relationships (inheritance and composition) for the `physicslib` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    FeTaperedCapsuleRigid_t <|-- FeBuildTaperedCapsuleRigid_t
    RnShapeDesc_t <|-- RnCapsuleDesc_t
    RnShapeDesc_t <|-- RnHullDesc_t
    RnShapeDesc_t <|-- RnSphereDesc_t
    RnShapeDesc_t <|-- RnMeshDesc_t
    FeSDFRigid_t <|-- FeBuildSDFRigid_t
    FeSphereRigid_t <|-- FeBuildSphereRigid_t
    FeBoxRigid_t <|-- FeBuildBoxRigid_t
    FeSimdTri_t *-- FourVectors2D
    RnCapsuleDesc_t *-- RnCapsule_t
    RnHullDesc_t *-- RnHull_t
    RnHull_t *-- RnVertex_t
    RnHull_t *-- RnHalfEdge_t
    RnHull_t *-- RnFace_t
    RnHull_t *-- RnPlane_t
    RnHull_t --> CRegionSVM
    CFeVertexMapBuildArray --> FeVertexMapBuild_t
    PhysFeModelDesc_t *-- FeNodeBase_t
    PhysFeModelDesc_t *-- FeSimdNodeBase_t
    PhysFeModelDesc_t *-- FeQuad_t
    PhysFeModelDesc_t *-- FeSimdQuad_t
    PhysFeModelDesc_t *-- FeSimdTri_t
    PhysFeModelDesc_t *-- FeSimdRodConstraint_t
    PhysFeModelDesc_t *-- FeSimdRodConstraintAnim_t
    PhysFeModelDesc_t *-- FeRodConstraint_t
    PhysFeModelDesc_t *-- FeTwistConstraint_t
    PhysFeModelDesc_t *-- FeHingeLimit_t
    PhysFeModelDesc_t *-- FeDynKinLink_t
    PhysFeModelDesc_t *-- FeAntiTunnelProbe_t
    PhysFeModelDesc_t *-- FeNodeStrayBox_t
    PhysFeModelDesc_t *-- FeAxialEdgeBend_t
    PhysFeModelDesc_t *-- FeCtrlOffset_t
    PhysFeModelDesc_t *-- FeCtrlOsOffset_t
    PhysFeModelDesc_t *-- FeFollowNode_t
    PhysFeModelDesc_t *-- FeCollisionPlane_t
    PhysFeModelDesc_t *-- FeNodeIntegrator_t
    PhysFeModelDesc_t *-- FeSpringIntegrator_t
    PhysFeModelDesc_t *-- FeSimdSpringIntegrator_t
    PhysFeModelDesc_t *-- FeWorldCollisionParams_t
    PhysFeModelDesc_t *-- FeTaperedCapsuleStretch_t
    PhysFeModelDesc_t *-- FeTaperedCapsuleRigid_t
    PhysFeModelDesc_t *-- FeSphereRigid_t
    PhysFeModelDesc_t *-- FeTreeChildren_t
    PhysFeModelDesc_t *-- FeFitMatrix_t
    PhysFeModelDesc_t *-- FeFitWeight_t
    PhysFeModelDesc_t *-- FeNodeReverseOffset_t
    PhysFeModelDesc_t *-- FeAnimStrayRadius_t
    PhysFeModelDesc_t *-- FeSimdAnimStrayRadius_t
    PhysFeModelDesc_t *-- FeKelagerBend2_t
    PhysFeModelDesc_t *-- FeCtrlSoftOffset_t
    PhysFeModelDesc_t *-- CFeIndexedJiggleBone
    PhysFeModelDesc_t *-- FeTri_t
    PhysFeModelDesc_t *-- FeSDFRigid_t
    PhysFeModelDesc_t *-- FeBoxRigid_t
    PhysFeModelDesc_t *-- FeRigidColliderIndices_t
    PhysFeModelDesc_t *-- FeMorphLayerDepr_t
    PhysFeModelDesc_t *-- FeVertexMapDesc_t
    PhysFeModelDesc_t *-- FeEffectDesc_t
    PhysFeModelDesc_t *-- FeNodeWindBase_t
    PhysFeModelDesc_t *-- FeModelSelfCollisionLayer_t
    FeCollisionPlane_t *-- RnPlane_t
    CastSphereSATParams_t --> RnHull_t
    CRegionSVM *-- RnPlane_t
    RnMeshDesc_t *-- RnMesh_t
    RnMesh_t *-- RnNode_t
    RnMesh_t *-- RnTriangle_t
    RnMesh_t *-- RnWing_t
    RnBodyDesc_t *-- DynamicContinuousContactBehavior_t
    CFeNamedJiggleBone *-- CFeJiggleBone
    CFeIndexedJiggleBone *-- CFeJiggleBone
```
