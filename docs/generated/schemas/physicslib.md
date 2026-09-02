---
layout: default
title: physicslib
parent: Schemas
nav_exclude: true
---

# Module: physicslib

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

[📊 View UML Diagram](../diagrams/physicslib.md)

103 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CFeIndexedJiggleBone](physicslib/CFeIndexedJiggleBone.md) | class | 164 | 3 |  |
| [CFeJiggleBone](physicslib/CFeJiggleBone.md) | class | 156 | 35 |  |
| [CFeMorphLayer](physicslib/CFeMorphLayer.md) | class | 136 | 7 |  |
| [CFeNamedJiggleBone](physicslib/CFeNamedJiggleBone.md) | class | 208 | 4 |  |
| [CFeVertexMapBuildArray](physicslib/CFeVertexMapBuildArray.md) | class | 24 | 1 |  |
| [CGenericShapeProxy](physicslib/CGenericShapeProxy.md) | class | 152 | 1 |  |
| [CRegionSVM](physicslib/CRegionSVM.md) | class | 48 | 2 |  |
| [CollisionDetailLayerInfo_t](physicslib/CollisionDetailLayerInfo_t.md) | class | 64 | 6 |  |
| [CollisionDetailLayerInfo_t::Name_t](physicslib/CollisionDetailLayerInfo_t.Name_t.md) | class | 16 | 2 |  |
| [CovMatrix3](physicslib/CovMatrix3.md) | class | 24 | 4 |  |
| [Dop26_t](physicslib/Dop26_t.md) | class | 104 | 1 |  |
| [FeAnimStrayRadius_t](physicslib/FeAnimStrayRadius_t.md) | class | 12 | 3 |  |
| [FeAntiTunnelGroupBuild_t](physicslib/FeAntiTunnelGroupBuild_t.md) | class | 8 | 2 |  |
| [FeAntiTunnelProbeBuild_t](physicslib/FeAntiTunnelProbeBuild_t.md) | class | 48 | 7 |  |
| [FeAntiTunnelProbe_t](physicslib/FeAntiTunnelProbe_t.md) | class | 28 | 8 |  |
| [FeAxialEdgeBend_t](physicslib/FeAxialEdgeBend_t.md) | class | 40 | 5 |  |
| [FeBandBendLimit_t](physicslib/FeBandBendLimit_t.md) | class | 20 | 3 |  |
| [FeBoneMergeLink_t](physicslib/FeBoneMergeLink_t.md) | class | 8 | 2 |  |
| [FeBoxRigid_t](physicslib/FeBoxRigid_t.md) | class | 64 | 6 |  |
| [FeBuildBoxRigid_t](physicslib/FeBuildBoxRigid_t.md) | class | 80 | 3 | [FeBoxRigid_t](physicslib/FeBoxRigid_t.md) |
| [FeBuildSDFRigid_t](physicslib/FeBuildSDFRigid_t.md) | class | 96 | 3 | [FeSDFRigid_t](physicslib/FeSDFRigid_t.md) |
| [FeBuildSphereRigid_t](physicslib/FeBuildSphereRigid_t.md) | class | 48 | 3 | [FeSphereRigid_t](physicslib/FeSphereRigid_t.md) |
| [FeBuildTaperedCapsuleRigid_t](physicslib/FeBuildTaperedCapsuleRigid_t.md) | class | 64 | 3 | [FeTaperedCapsuleRigid_t](physicslib/FeTaperedCapsuleRigid_t.md) |
| [FeCollisionPlane_t](physicslib/FeCollisionPlane_t.md) | class | 24 | 4 |  |
| [FeCtrlOffset_t](physicslib/FeCtrlOffset_t.md) | class | 16 | 3 |  |
| [FeCtrlOsOffset_t](physicslib/FeCtrlOsOffset_t.md) | class | 4 | 2 |  |
| [FeCtrlSoftOffset_t](physicslib/FeCtrlSoftOffset_t.md) | class | 20 | 4 |  |
| [FeDynKinLink_t](physicslib/FeDynKinLink_t.md) | class | 4 | 2 |  |
| [FeEdgeDesc_t](physicslib/FeEdgeDesc_t.md) | class | 16 | 3 |  |
| [FeEffectDesc_t](physicslib/FeEffectDesc_t.md) | class | 32 | 4 |  |
| [FeFitInfluence_t](physicslib/FeFitInfluence_t.md) | class | 12 | 3 |  |
| [FeFitMatrix_t](physicslib/FeFitMatrix_t.md) | class | 64 | 5 |  |
| [FeFitWeight_t](physicslib/FeFitWeight_t.md) | class | 8 | 3 |  |
| [FeFollowNode_t](physicslib/FeFollowNode_t.md) | class | 8 | 3 |  |
| [FeHingeLimitBuild_t](physicslib/FeHingeLimitBuild_t.md) | class | 24 | 4 |  |
| [FeHingeLimit_t](physicslib/FeHingeLimit_t.md) | class | 32 | 6 |  |
| [FeKelagerBend2_t](physicslib/FeKelagerBend2_t.md) | class | 24 | 4 |  |
| [FeModelSelfCollisionLayer_t](physicslib/FeModelSelfCollisionLayer_t.md) | class | 56 | 5 |  |
| [FeMorphLayerDepr_t](physicslib/FeMorphLayerDepr_t.md) | class | 144 | 8 |  |
| [FeNodeBase_t](physicslib/FeNodeBase_t.md) | class | 32 | 7 |  |
| [FeNodeIntegrator_t](physicslib/FeNodeIntegrator_t.md) | class | 16 | 4 |  |
| [FeNodeReverseOffset_t](physicslib/FeNodeReverseOffset_t.md) | class | 16 | 3 |  |
| [FeNodeStrayBox_t](physicslib/FeNodeStrayBox_t.md) | class | 32 | 4 |  |
| [FeNodeWindBase_t](physicslib/FeNodeWindBase_t.md) | class | 8 | 4 |  |
| [FeProxyVertexMap_t](physicslib/FeProxyVertexMap_t.md) | class | 16 | 2 |  |
| [FeQuad_t](physicslib/FeQuad_t.md) | class | 76 | 3 |  |
| [FeRigidColliderIndices_t](physicslib/FeRigidColliderIndices_t.md) | class | 10 | 5 |  |
| [FeRodConstraint_t](physicslib/FeRodConstraint_t.md) | class | 20 | 5 |  |
| [FeSDFRigid_t](physicslib/FeSDFRigid_t.md) | class | 80 | 11 |  |
| [FeSimdAnimStrayRadius_t](physicslib/FeSimdAnimStrayRadius_t.md) | class | 48 | 3 |  |
| [FeSimdNodeBase_t](physicslib/FeSimdNodeBase_t.md) | class | 112 | 7 |  |
| [FeSimdQuad_t](physicslib/FeSimdQuad_t.md) | class | 304 | 4 |  |
| [FeSimdRodConstraintAnim_t](physicslib/FeSimdRodConstraintAnim_t.md) | class | 48 | 3 |  |
| [FeSimdRodConstraint_t](physicslib/FeSimdRodConstraint_t.md) | class | 80 | 5 |  |
| [FeSimdSpringIntegrator_t](physicslib/FeSimdSpringIntegrator_t.md) | class | 80 | 5 |  |
| [FeSimdTri_t](physicslib/FeSimdTri_t.md) | class | 128 | 5 |  |
| [FeSoftParent_t](physicslib/FeSoftParent_t.md) | class | 8 | 2 |  |
| [FeSourceEdge_t](physicslib/FeSourceEdge_t.md) | class | 4 | 1 |  |
| [FeSphereRigid_t](physicslib/FeSphereRigid_t.md) | class | 32 | 5 |  |
| [FeSpringIntegrator_t](physicslib/FeSpringIntegrator_t.md) | class | 20 | 5 |  |
| [FeStiffHingeBuild_t](physicslib/FeStiffHingeBuild_t.md) | class | 28 | 4 |  |
| [FeTaperedCapsuleRigid_t](physicslib/FeTaperedCapsuleRigid_t.md) | class | 48 | 5 |  |
| [FeTaperedCapsuleStretch_t](physicslib/FeTaperedCapsuleStretch_t.md) | class | 16 | 4 |  |
| [FeTreeChildren_t](physicslib/FeTreeChildren_t.md) | class | 4 | 1 |  |
| [FeTri_t](physicslib/FeTri_t.md) | class | 28 | 5 |  |
| [FeTwistConstraint_t](physicslib/FeTwistConstraint_t.md) | class | 12 | 4 |  |
| [FeVertexMapBuild_t](physicslib/FeVertexMapBuild_t.md) | class | 48 | 6 |  |
| [FeVertexMapDesc_t](physicslib/FeVertexMapDesc_t.md) | class | 56 | 12 |  |
| [FeWeightedNode_t](physicslib/FeWeightedNode_t.md) | class | 4 | 2 |  |
| [FeWorldCollisionParams_t](physicslib/FeWorldCollisionParams_t.md) | class | 12 | 4 |  |
| [FourCovMatrices3](physicslib/FourCovMatrices3.md) | class | 96 | 4 |  |
| [FourVectors2D](physicslib/FourVectors2D.md) | class | 32 | 2 |  |
| [OldFeEdge_t](physicslib/OldFeEdge_t.md) | class | 72 | 12 |  |
| [PhysFeModelDesc_t](physicslib/PhysFeModelDesc_t.md) | class | 1784 | 111 |  |
| [PhysicsParticleId_t](physicslib/PhysicsParticleId_t.md) | class | 4 | 1 |  |
| [RnBlendVertex_t](physicslib/RnBlendVertex_t.md) | class | 16 | 8 |  |
| [RnBodyDesc_t](physicslib/RnBodyDesc_t.md) | class | 224 | 36 |  |
| [RnCapsuleDesc_t](physicslib/RnCapsuleDesc_t.md) | class | 56 | 1 | [RnShapeDesc_t](physicslib/RnShapeDesc_t.md) |
| [RnCapsule_t](physicslib/RnCapsule_t.md) | class | 28 | 2 |  |
| [RnCompoundDesc_t](physicslib/RnCompoundDesc_t.md) | class | 168 | 1 | [RnShapeDesc_t](physicslib/RnShapeDesc_t.md) |
| [RnCompound_t](physicslib/RnCompound_t.md) | class | 144 | 8 |  |
| [RnFace_t](physicslib/RnFace_t.md) | class | 1 | 1 |  |
| [RnHalfEdge_t](physicslib/RnHalfEdge_t.md) | class | 4 | 4 |  |
| [RnHullDesc_t](physicslib/RnHullDesc_t.md) | class | 272 | 1 | [RnShapeDesc_t](physicslib/RnShapeDesc_t.md) |
| [RnHull_t](physicslib/RnHull_t.md) | class | 248 | 14 |  |
| [RnMeshDesc_t](physicslib/RnMeshDesc_t.md) | class | 216 | 1 | [RnShapeDesc_t](physicslib/RnShapeDesc_t.md) |
| [RnMesh_t](physicslib/RnMesh_t.md) | class | 192 | 11 |  |
| [RnNode_t](physicslib/RnNode_t.md) | class | 32 | 4 |  |
| [RnPlane_t](physicslib/RnPlane_t.md) | class | 16 | 2 |  |
| [RnShapeDesc_t](physicslib/RnShapeDesc_t.md) | class | 24 | 6 |  |
| [RnSoftbodyCapsule_t](physicslib/RnSoftbodyCapsule_t.md) | class | 32 | 3 |  |
| [RnSoftbodyParticle_t](physicslib/RnSoftbodyParticle_t.md) | class | 4 | 1 |  |
| [RnSoftbodySpring_t](physicslib/RnSoftbodySpring_t.md) | class | 8 | 2 |  |
| [RnSphereDesc_t](physicslib/RnSphereDesc_t.md) | class | 40 | 1 | [RnShapeDesc_t](physicslib/RnShapeDesc_t.md) |
| [RnTriangle_t](physicslib/RnTriangle_t.md) | class | 12 | 1 |  |
| [RnVertex_t](physicslib/RnVertex_t.md) | class | 1 | 1 |  |
| [RnWing_t](physicslib/RnWing_t.md) | class | 12 | 1 |  |
| [VertexPositionColor_t](physicslib/VertexPositionColor_t.md) | class | 16 | 1 |  |
| [VertexPositionNormal_t](physicslib/VertexPositionNormal_t.md) | class | 24 | 2 |  |
| [DynamicContinuousContactBehavior_t](physicslib/DynamicContinuousContactBehavior_t.md) | enum | — | 3 |  |
| [JointAxis_t](physicslib/JointAxis_t.md) | enum | — | 4 |  |
| [JointMotion_t](physicslib/JointMotion_t.md) | enum | — | 3 |  |
| [PhysGenericShapeType_t](physicslib/PhysGenericShapeType_t.md) | enum | — | 5 |  |
