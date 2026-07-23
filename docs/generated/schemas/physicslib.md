---
layout: default
title: physicslib
parent: Schemas
nav_exclude: true
---

# Module: physicslib

[📊 View UML Diagram](../diagrams/physicslib.md)

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [CFeIndexedJiggleBone](#cfeindexedjigglebone) | class |  | 3 |
| [CFeJiggleBone](#cfejigglebone) | class |  | 35 |
| [CFeMorphLayer](#cfemorphlayer) | class |  | 7 |
| [CFeNamedJiggleBone](#cfenamedjigglebone) | class |  | 4 |
| [CFeVertexMapBuildArray](#cfevertexmapbuildarray) | class |  | 1 |
| [CGenericShapeProxy](#cgenericshapeproxy) | class |  | 1 |
| [CRegionSVM](#cregionsvm) | class |  | 2 |
| [CollisionDetailLayerInfo_t](#collisiondetaillayerinfo_t) | class |  | 6 |
| [CollisionDetailLayerInfo_t::Name_t](#collisiondetaillayerinfo_tname_t) | class |  | 2 |
| [CovMatrix3](#covmatrix3) | class |  | 4 |
| [Dop26_t](#dop26_t) | class |  | 1 |
| [FeAnimStrayRadius_t](#feanimstrayradius_t) | class |  | 3 |
| [FeAntiTunnelGroupBuild_t](#feantitunnelgroupbuild_t) | class |  | 2 |
| [FeAntiTunnelProbeBuild_t](#feantitunnelprobebuild_t) | class |  | 7 |
| [FeAntiTunnelProbe_t](#feantitunnelprobe_t) | class |  | 8 |
| [FeAxialEdgeBend_t](#feaxialedgebend_t) | class |  | 5 |
| [FeBandBendLimit_t](#febandbendlimit_t) | class |  | 3 |
| [FeBoneMergeLink_t](#febonemergelink_t) | class |  | 2 |
| [FeBoxRigid_t](#feboxrigid_t) | class |  | 6 |
| [FeBuildBoxRigid_t](#febuildboxrigid_t) | class | FeBoxRigid_t | 3 |
| [FeBuildSDFRigid_t](#febuildsdfrigid_t) | class | FeSDFRigid_t | 3 |
| [FeBuildSphereRigid_t](#febuildsphererigid_t) | class | FeSphereRigid_t | 3 |
| [FeBuildTaperedCapsuleRigid_t](#febuildtaperedcapsulerigid_t) | class | FeTaperedCapsuleRigid_t | 3 |
| [FeCollisionPlane_t](#fecollisionplane_t) | class |  | 4 |
| [FeCtrlOffset_t](#fectrloffset_t) | class |  | 3 |
| [FeCtrlOsOffset_t](#fectrlosoffset_t) | class |  | 2 |
| [FeCtrlSoftOffset_t](#fectrlsoftoffset_t) | class |  | 4 |
| [FeDynKinLink_t](#fedynkinlink_t) | class |  | 2 |
| [FeEdgeDesc_t](#feedgedesc_t) | class |  | 3 |
| [FeEffectDesc_t](#feeffectdesc_t) | class |  | 4 |
| [FeFitInfluence_t](#fefitinfluence_t) | class |  | 3 |
| [FeFitMatrix_t](#fefitmatrix_t) | class |  | 5 |
| [FeFitWeight_t](#fefitweight_t) | class |  | 3 |
| [FeFollowNode_t](#fefollownode_t) | class |  | 3 |
| [FeHingeLimitBuild_t](#fehingelimitbuild_t) | class |  | 4 |
| [FeHingeLimit_t](#fehingelimit_t) | class |  | 6 |
| [FeKelagerBend2_t](#fekelagerbend2_t) | class |  | 4 |
| [FeModelSelfCollisionLayer_t](#femodelselfcollisionlayer_t) | class |  | 5 |
| [FeMorphLayerDepr_t](#femorphlayerdepr_t) | class |  | 8 |
| [FeNodeBase_t](#fenodebase_t) | class |  | 7 |
| [FeNodeIntegrator_t](#fenodeintegrator_t) | class |  | 4 |
| [FeNodeReverseOffset_t](#fenodereverseoffset_t) | class |  | 3 |
| [FeNodeStrayBox_t](#fenodestraybox_t) | class |  | 4 |
| [FeNodeWindBase_t](#fenodewindbase_t) | class |  | 4 |
| [FeProxyVertexMap_t](#feproxyvertexmap_t) | class |  | 2 |
| [FeQuad_t](#fequad_t) | class |  | 3 |
| [FeRigidColliderIndices_t](#ferigidcolliderindices_t) | class |  | 5 |
| [FeRodConstraint_t](#ferodconstraint_t) | class |  | 5 |
| [FeSDFRigid_t](#fesdfrigid_t) | class |  | 11 |
| [FeSimdAnimStrayRadius_t](#fesimdanimstrayradius_t) | class |  | 3 |
| [FeSimdNodeBase_t](#fesimdnodebase_t) | class |  | 7 |
| [FeSimdQuad_t](#fesimdquad_t) | class |  | 4 |
| [FeSimdRodConstraintAnim_t](#fesimdrodconstraintanim_t) | class |  | 3 |
| [FeSimdRodConstraint_t](#fesimdrodconstraint_t) | class |  | 5 |
| [FeSimdSpringIntegrator_t](#fesimdspringintegrator_t) | class |  | 5 |
| [FeSimdTri_t](#fesimdtri_t) | class |  | 5 |
| [FeSoftParent_t](#fesoftparent_t) | class |  | 2 |
| [FeSourceEdge_t](#fesourceedge_t) | class |  | 1 |
| [FeSphereRigid_t](#fesphererigid_t) | class |  | 5 |
| [FeSpringIntegrator_t](#fespringintegrator_t) | class |  | 5 |
| [FeStiffHingeBuild_t](#festiffhingebuild_t) | class |  | 4 |
| [FeTaperedCapsuleRigid_t](#fetaperedcapsulerigid_t) | class |  | 5 |
| [FeTaperedCapsuleStretch_t](#fetaperedcapsulestretch_t) | class |  | 4 |
| [FeTreeChildren_t](#fetreechildren_t) | class |  | 1 |
| [FeTri_t](#fetri_t) | class |  | 5 |
| [FeTwistConstraint_t](#fetwistconstraint_t) | class |  | 4 |
| [FeVertexMapBuild_t](#fevertexmapbuild_t) | class |  | 6 |
| [FeVertexMapDesc_t](#fevertexmapdesc_t) | class |  | 12 |
| [FeWeightedNode_t](#feweightednode_t) | class |  | 2 |
| [FeWorldCollisionParams_t](#feworldcollisionparams_t) | class |  | 4 |
| [FourCovMatrices3](#fourcovmatrices3) | class |  | 4 |
| [FourVectors2D](#fourvectors2d) | class |  | 2 |
| [OldFeEdge_t](#oldfeedge_t) | class |  | 12 |
| [PhysFeModelDesc_t](#physfemodeldesc_t) | class |  | 111 |
| [PhysicsParticleId_t](#physicsparticleid_t) | class |  | 1 |
| [RnBlendVertex_t](#rnblendvertex_t) | class |  | 8 |
| [RnBodyDesc_t](#rnbodydesc_t) | class |  | 36 |
| [RnCapsuleDesc_t](#rncapsuledesc_t) | class | RnShapeDesc_t | 1 |
| [RnCapsule_t](#rncapsule_t) | class |  | 2 |
| [RnCompoundDesc_t](#rncompounddesc_t) | class | RnShapeDesc_t | 1 |
| [RnCompound_t](#rncompound_t) | class |  | 8 |
| [RnFace_t](#rnface_t) | class |  | 1 |
| [RnHalfEdge_t](#rnhalfedge_t) | class |  | 4 |
| [RnHullDesc_t](#rnhulldesc_t) | class | RnShapeDesc_t | 1 |
| [RnHull_t](#rnhull_t) | class |  | 14 |
| [RnMeshDesc_t](#rnmeshdesc_t) | class | RnShapeDesc_t | 1 |
| [RnMesh_t](#rnmesh_t) | class |  | 11 |
| [RnNode_t](#rnnode_t) | class |  | 4 |
| [RnPlane_t](#rnplane_t) | class |  | 2 |
| [RnShapeDesc_t](#rnshapedesc_t) | class |  | 6 |
| [RnSoftbodyCapsule_t](#rnsoftbodycapsule_t) | class |  | 3 |
| [RnSoftbodyParticle_t](#rnsoftbodyparticle_t) | class |  | 1 |
| [RnSoftbodySpring_t](#rnsoftbodyspring_t) | class |  | 2 |
| [RnSphereDesc_t](#rnspheredesc_t) | class | RnShapeDesc_t | 1 |
| [RnTriangle_t](#rntriangle_t) | class |  | 1 |
| [RnVertex_t](#rnvertex_t) | class |  | 1 |
| [RnWing_t](#rnwing_t) | class |  | 1 |
| [VertexPositionColor_t](#vertexpositioncolor_t) | class |  | 1 |
| [VertexPositionNormal_t](#vertexpositionnormal_t) | class |  | 2 |

---

### CFeIndexedJiggleBone

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CFeIndexedJiggleBone *-- CFeJiggleBone
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nNode` | uint32 |  |
| `m_nJiggleParent` | uint32 |  |
| `m_jiggleBone` | [CFeJiggleBone](../schemas/physicslib.md#cfejigglebone) |  |

### CFeJiggleBone

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nFlags` | uint32 |  |
| `m_flLength` | float32 |  |
| `m_flTipMass` | float32 |  |
| `m_flYawStiffness` | float32 |  |
| `m_flYawDamping` | float32 |  |
| `m_flPitchStiffness` | float32 |  |
| `m_flPitchDamping` | float32 |  |
| `m_flAlongStiffness` | float32 |  |
| `m_flAlongDamping` | float32 |  |
| `m_flAngleLimit` | float32 |  |
| `m_flMinYaw` | float32 |  |
| `m_flMaxYaw` | float32 |  |
| `m_flYawFriction` | float32 |  |
| `m_flYawBounce` | float32 |  |
| `m_flMinPitch` | float32 |  |
| `m_flMaxPitch` | float32 |  |
| `m_flPitchFriction` | float32 |  |
| `m_flPitchBounce` | float32 |  |
| `m_flBaseMass` | float32 |  |
| `m_flBaseStiffness` | float32 |  |
| `m_flBaseDamping` | float32 |  |
| `m_flBaseMinLeft` | float32 |  |
| `m_flBaseMaxLeft` | float32 |  |
| `m_flBaseLeftFriction` | float32 |  |
| `m_flBaseMinUp` | float32 |  |
| `m_flBaseMaxUp` | float32 |  |
| `m_flBaseUpFriction` | float32 |  |
| `m_flBaseMinForward` | float32 |  |
| `m_flBaseMaxForward` | float32 |  |
| `m_flBaseForwardFriction` | float32 |  |
| `m_flRadius0` | float32 |  |
| `m_flRadius1` | float32 |  |
| `m_vPoint0` | Vector |  |
| `m_vPoint1` | Vector |  |
| `m_nCollisionMask` | uint16 |  |

### CFeMorphLayer

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Name` | CUtlString |  |
| `m_nNameHash` | uint32 |  |
| `m_Nodes` | CUtlVector< uint16 > |  |
| `m_InitPos` | CUtlVector< Vector > |  |
| `m_Gravity` | CUtlVector< float32 > |  |
| `m_GoalStrength` | CUtlVector< float32 > |  |
| `m_GoalDamping` | CUtlVector< float32 > |  |

### CFeNamedJiggleBone

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CFeNamedJiggleBone *-- CFeJiggleBone
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_strParentBone` | CUtlString |  |
| `m_transform` | CTransform |  |
| `m_nJiggleParent` | uint32 |  |
| `m_jiggleBone` | [CFeJiggleBone](../schemas/physicslib.md#cfejigglebone) |  |

### CFeVertexMapBuildArray

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CFeVertexMapBuildArray --> FeVertexMapBuild_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Array` | CUtlVector< [FeVertexMapBuild_t](../schemas/physicslib.md#fevertexmapbuild_t)* > |  |

### CGenericShapeProxy

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_verts` | CUtlLeanVectorFixedGrowable< Vector, 8 > |  |

### CRegionSVM

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CRegionSVM *-- RnPlane_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Planes` | CUtlVector< [RnPlane_t](../schemas/physicslib.md#rnplane_t) > |  |
| `m_Nodes` | CUtlVector< uint32 > |  |

### CollisionDetailLayerInfo_t

**Metadata:** `MGetKV3ClassDefaults`, `MVDataOutlinerLeafNameFn`, `MVDataRoot`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_sDescription` | CUtlString | `MPropertyDescription How the detail layer is meant to be used` `MPropertyFriendlyName Description` |
| `m_sFriendlyName` | CUtlString | `MPropertyDescription How name is displayed in tools` `MPropertyFriendlyName Friendly Name` |
| `m_bIsQueryOnly` | bool | `MPropertyDescription Only query can use this layer, not collision` |
| `m_sParentDetailLayer` | CUtlString | `MPropertyDescription Parent detail layers automatically include the child layer` |
| `m_vecSubtreeDetailLayers` | CUtlVector< [CollisionDetailLayerInfo_t](../schemas/physicslib.md#collisiondetaillayerinfo_t)::Name_t > | `MPropertySuppressField` |
| `m_bNotPickable` | bool | `MPropertySuppressField` |

### CollisionDetailLayerInfo_t::Name_t

**Metadata:** `MGetKV3ClassDefaults`, `MVDataRoot`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nNameToken` | CUtlStringToken |  |
| `m_sNameString` | CUtlString |  |

### CovMatrix3

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vDiag` | Vector |  |
| `m_flXY` | float32 |  |
| `m_flXZ` | float32 |  |
| `m_flYZ` | float32 |  |

### Dop26_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flSupport` | float32[26] |  |

### FeAnimStrayRadius_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[2] |  |
| `flMaxDist` | float32 |  |
| `flRelaxationFactor` | float32 |  |

### FeAntiTunnelGroupBuild_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nVertexMapHash` | uint32 |  |
| `m_nCollisionMask` | uint32 |  |

### FeAntiTunnelProbeBuild_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `flWeight` | float32 |  |
| `flActivationDistance` | float32 |  |
| `flBias` | float32 |  |
| `flCurvature` | float32 |  |
| `nFlags` | uint32 |  |
| `nProbeNode` | uint16 |  |
| `targetNodes` | CUtlVector< uint16 > |  |

### FeAntiTunnelProbe_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `flWeight` | float32 |  |
| `nFlags` | uint32 |  |
| `nProbeNode` | uint16 |  |
| `nCount` | uint16 |  |
| `nBegin` | uint32 |  |
| `flActivationDistance` | float32 |  |
| `flCurvatureRadius` | float32 |  |
| `flBias` | float32 |  |

### FeAxialEdgeBend_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `te` | float32 |  |
| `tv` | float32 |  |
| `flDist` | float32 |  |
| `flWeight` | float32[4] |  |
| `nNode` | uint16[6] |  |

### FeBandBendLimit_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `flDistMin` | float32 |  |
| `flDistMax` | float32 |  |
| `nNode` | uint16[6] |  |

### FeBoneMergeLink_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nParentHash` | uint32 |  |
| `m_nChildNode` | uint16 |  |

### FeBoxRigid_t

**Derived by:** [FeBuildBoxRigid_t](physicslib.md#febuildboxrigid_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    FeBoxRigid_t <|-- FeBuildBoxRigid_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `tmFrame2` | CTransform |  |
| `nNode` | uint16 |  |
| `nCollisionMask` | uint16 |  |
| `vSize` | Vector |  |
| `nVertexMapIndex` | uint16 |  |
| `nFlags` | uint16 |  |

### FeBuildBoxRigid_t

**Inherits from:** [FeBoxRigid_t](physicslib.md#feboxrigid_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    FeBoxRigid_t <|-- FeBuildBoxRigid_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nPriority` | int32 |  |
| `m_nVertexMapHash` | uint32 |  |
| `m_nAntitunnelGroupBits` | uint32 |  |

### FeBuildSDFRigid_t

**Inherits from:** [FeSDFRigid_t](physicslib.md#fesdfrigid_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    FeSDFRigid_t <|-- FeBuildSDFRigid_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nPriority` | int32 |  |
| `m_nVertexMapHash` | uint32 |  |
| `m_nAntitunnelGroupBits` | uint32 |  |

### FeBuildSphereRigid_t

**Inherits from:** [FeSphereRigid_t](physicslib.md#fesphererigid_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    FeSphereRigid_t <|-- FeBuildSphereRigid_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nPriority` | int32 |  |
| `m_nVertexMapHash` | uint32 |  |
| `m_nAntitunnelGroupBits` | uint32 |  |

### FeBuildTaperedCapsuleRigid_t

**Inherits from:** [FeTaperedCapsuleRigid_t](physicslib.md#fetaperedcapsulerigid_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    FeTaperedCapsuleRigid_t <|-- FeBuildTaperedCapsuleRigid_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nPriority` | int32 |  |
| `m_nVertexMapHash` | uint32 |  |
| `m_nAntitunnelGroupBits` | uint32 |  |

### FeCollisionPlane_t

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    FeCollisionPlane_t *-- RnPlane_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nCtrlParent` | uint16 |  |
| `nChildNode` | uint16 |  |
| `m_Plane` | [RnPlane_t](../schemas/physicslib.md#rnplane_t) |  |
| `flStrength` | float32 |  |

### FeCtrlOffset_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `vOffset` | Vector |  |
| `nCtrlParent` | uint16 |  |
| `nCtrlChild` | uint16 |  |

### FeCtrlOsOffset_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nCtrlParent` | uint16 |  |
| `nCtrlChild` | uint16 |  |

### FeCtrlSoftOffset_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nCtrlParent` | uint16 |  |
| `nCtrlChild` | uint16 |  |
| `vOffset` | Vector |  |
| `flAlpha` | float32 |  |

### FeDynKinLink_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nParent` | uint16 |  |
| `m_nChild` | uint16 |  |

### FeEdgeDesc_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nEdge` | uint16[2] |  |
| `nSide` | uint16[2][2] |  |
| `nVirtElem` | uint16[2] |  |

### FeEffectDesc_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `sName` | CUtlString |  |
| `nNameHash` | uint32 |  |
| `nType` | int32 |  |
| `m_Params` | KeyValues3 |  |

### FeFitInfluence_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nVertexNode` | uint32 |  |
| `flWeight` | float32 |  |
| `nMatrixNode` | uint32 |  |

### FeFitMatrix_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `bone` | CTransform |  |
| `vCenter` | Vector |  |
| `nEnd` | uint16 |  |
| `nNode` | uint16 |  |
| `nBeginDynamic` | uint16 |  |

### FeFitWeight_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `flWeight` | float32 |  |
| `nNode` | uint16 |  |
| `nDummy` | uint16 |  |

### FeFollowNode_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nParentNode` | uint16 |  |
| `nChildNode` | uint16 |  |
| `flWeight` | float32 |  |

### FeHingeLimitBuild_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[6] |  |
| `nFlags` | uint32 |  |
| `flLimitCW` | float32 |  |
| `flLimitCCW` | float32 |  |

### FeHingeLimit_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[6] |  |
| `nFlags` | uint32 |  |
| `flWeight4` | float32 |  |
| `flWeight5` | float32 |  |
| `flAngleCenter` | float32 |  |
| `flAngleExtents` | float32 |  |

### FeKelagerBend2_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `flWeight` | float32[3] |  |
| `flHeight0` | float32 |  |
| `nNode` | uint16[3] |  |
| `nReserved` | uint16 |  |

### FeModelSelfCollisionLayer_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Name` | CUtlString |  |
| `m_Nodes` | CUtlVector< uint16 > |  |
| `m_flParentReaction` | float32 |  |
| `m_nFlags` | uint32 |  |
| `m_nEndIdx` | uint32[4] |  |

### FeMorphLayerDepr_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Name` | CUtlString |  |
| `m_nNameHash` | uint32 |  |
| `m_Nodes` | CUtlVector< uint16 > |  |
| `m_InitPos` | CUtlVector< Vector > |  |
| `m_Gravity` | CUtlVector< float32 > |  |
| `m_GoalStrength` | CUtlVector< float32 > |  |
| `m_GoalDamping` | CUtlVector< float32 > |  |
| `m_nFlags` | uint32 |  |

### FeNodeBase_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16 |  |
| `nDummy` | uint16[3] |  |
| `nNodeX0` | uint16 |  |
| `nNodeX1` | uint16 |  |
| `nNodeY0` | uint16 |  |
| `nNodeY1` | uint16 |  |
| `qAdjust` | QuaternionStorage |  |

### FeNodeIntegrator_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `flPointDamping` | float32 |  |
| `flAnimationForceAttraction` | float32 |  |
| `flAnimationVertexAttraction` | float32 |  |
| `flGravity` | float32 |  |

### FeNodeReverseOffset_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `vOffset` | Vector |  |
| `nBoneCtrl` | uint16 |  |
| `nTargetNode` | uint16 |  |

### FeNodeStrayBox_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `vMin` | Vector |  |
| `nFlags` | uint32 |  |
| `vMax` | Vector |  |
| `nNode` | uint16[2] |  |

### FeNodeWindBase_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNodeX0` | uint16 |  |
| `nNodeX1` | uint16 |  |
| `nNodeY0` | uint16 |  |
| `nNodeY1` | uint16 |  |

### FeProxyVertexMap_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Name` | CUtlString |  |
| `m_flWeight` | float32 |  |

### FeQuad_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[4] |  |
| `flSlack` | float32 |  |
| `vShape` | Vector4D[4] |  |

### FeRigidColliderIndices_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nTaperedCapsuleRigidIndex` | uint16 |  |
| `m_nSphereRigidIndex` | uint16 |  |
| `m_nBoxRigidIndex` | uint16 |  |
| `m_nSDFRigidIndex` | uint16 |  |
| `m_nCollisionPlaneIndex` | uint16 |  |

### FeRodConstraint_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[2] |  |
| `flMaxDist` | float32 |  |
| `flMinDist` | float32 |  |
| `flWeight0` | float32 |  |
| `flRelaxationFactor` | float32 |  |

### FeSDFRigid_t

**Derived by:** [FeBuildSDFRigid_t](physicslib.md#febuildsdfrigid_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    FeSDFRigid_t <|-- FeBuildSDFRigid_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `vLocalMin` | Vector |  |
| `vLocalMax` | Vector |  |
| `flBounciness` | float32 |  |
| `nNode` | uint16 |  |
| `nCollisionMask` | uint16 |  |
| `nVertexMapIndex` | uint16 |  |
| `nFlags` | uint16 |  |
| `m_Distances` | CUtlVector< float32 > |  |
| `m_nWidth` | int32 |  |
| `m_nHeight` | int32 |  |
| `m_nDepth` | int32 |  |

### FeSimdAnimStrayRadius_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[4][2] |  |
| `flMaxDist` | fltx4 |  |
| `flRelaxationFactor` | fltx4 |  |

### FeSimdNodeBase_t

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    FeSimdNodeBase_t *-- FourQuaternions
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[4] |  |
| `nNodeX0` | uint16[4] |  |
| `nNodeX1` | uint16[4] |  |
| `nNodeY0` | uint16[4] |  |
| `nNodeY1` | uint16[4] |  |
| `nDummy` | uint16[4] |  |
| `qAdjust` | [FourQuaternions](../schemas/mathlib_extended.md#fourquaternions) |  |

### FeSimdQuad_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[4][4] |  |
| `f4Slack` | fltx4 |  |
| `vShape` | FourVectors[4] |  |
| `f4Weights` | fltx4[4] |  |

### FeSimdRodConstraintAnim_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[4][2] |  |
| `f4Weight0` | fltx4 |  |
| `f4RelaxationFactor` | fltx4 |  |

### FeSimdRodConstraint_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[4][2] |  |
| `f4MaxDist` | fltx4 |  |
| `f4MinDist` | fltx4 |  |
| `f4Weight0` | fltx4 |  |
| `f4RelaxationFactor` | fltx4 |  |

### FeSimdSpringIntegrator_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[4][2] |  |
| `flSpringRestLength` | fltx4 |  |
| `flSpringConstant` | fltx4 |  |
| `flSpringDamping` | fltx4 |  |
| `flNodeWeight0` | fltx4 |  |

### FeSimdTri_t

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    FeSimdTri_t *-- FourVectors2D
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint32[4][3] |  |
| `w1` | fltx4 |  |
| `w2` | fltx4 |  |
| `v1x` | fltx4 |  |
| `v2` | [FourVectors2D](../schemas/physicslib.md#fourvectors2d) |  |

### FeSoftParent_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nParent` | int32 |  |
| `flAlpha` | float32 |  |

### FeSourceEdge_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[2] |  |

### FeSphereRigid_t

**Derived by:** [FeBuildSphereRigid_t](physicslib.md#febuildsphererigid_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    FeSphereRigid_t <|-- FeBuildSphereRigid_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `vSphere` | fltx4 |  |
| `nNode` | uint16 |  |
| `nCollisionMask` | uint16 |  |
| `nVertexMapIndex` | uint16 |  |
| `nFlags` | uint16 |  |

### FeSpringIntegrator_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[2] |  |
| `flSpringRestLength` | float32 |  |
| `flSpringConstant` | float32 |  |
| `flSpringDamping` | float32 |  |
| `flNodeWeight0` | float32 |  |

### FeStiffHingeBuild_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `flMaxAngle` | float32 |  |
| `flStrength` | float32 |  |
| `flMotionBias` | float32[3] |  |
| `nNode` | uint16[3] |  |

### FeTaperedCapsuleRigid_t

**Derived by:** [FeBuildTaperedCapsuleRigid_t](physicslib.md#febuildtaperedcapsulerigid_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    FeTaperedCapsuleRigid_t <|-- FeBuildTaperedCapsuleRigid_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `vSphere` | fltx4[2] |  |
| `nNode` | uint16 |  |
| `nCollisionMask` | uint16 |  |
| `nVertexMapIndex` | uint16 |  |
| `nFlags` | uint16 |  |

### FeTaperedCapsuleStretch_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[2] |  |
| `nCollisionMask` | uint16 |  |
| `nDummy` | uint16 | `MPropertySuppressField` |
| `flRadius` | float32[2] |  |

### FeTreeChildren_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nChild` | uint16[2] |  |

### FeTri_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16[3] |  |
| `w1` | float32 |  |
| `w2` | float32 |  |
| `v1x` | float32 |  |
| `v2` | Vector2D |  |

### FeTwistConstraint_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNodeOrient` | uint16 |  |
| `nNodeEnd` | uint16 |  |
| `flTwistRelax` | float32 |  |
| `flSwingRelax` | float32 |  |

### FeVertexMapBuild_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_VertexMapName` | CUtlString |  |
| `m_nNameHash` | uint32 |  |
| `m_Color` | Color |  |
| `m_flVolumetricSolveStrength` | float32 |  |
| `m_nScaleSourceNode` | int32 |  |
| `m_Weights` | CUtlVector< float32 > |  |

### FeVertexMapDesc_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `sName` | CUtlString |  |
| `nNameHash` | uint32 |  |
| `nColor` | uint32 |  |
| `nFlags` | uint32 |  |
| `nVertexBase` | uint16 |  |
| `nVertexCount` | uint16 |  |
| `nMapOffset` | uint32 |  |
| `nNodeListOffset` | uint32 |  |
| `vCenterOfMass` | Vector |  |
| `flVolumetricSolveStrength` | float32 |  |
| `nScaleSourceNode` | int16 |  |
| `nNodeListCount` | uint16 |  |

### FeWeightedNode_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nNode` | uint16 |  |
| `nWeight` | uint16 |  |

### FeWorldCollisionParams_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `flWorldFriction` | float32 |  |
| `flGroundFriction` | float32 |  |
| `nListBegin` | uint16 |  |
| `nListEnd` | uint16 |  |

### FourCovMatrices3

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vDiag` | FourVectors |  |
| `m_flXY` | fltx4 |  |
| `m_flXZ` | fltx4 |  |
| `m_flYZ` | fltx4 |  |

### FourVectors2D

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `x` | fltx4 |  |
| `y` | fltx4 |  |

### OldFeEdge_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flK` | float32[3] |  |
| `invA` | float32 |  |
| `t` | float32 |  |
| `flThetaRelaxed` | float32 |  |
| `flThetaFactor` | float32 |  |
| `c01` | float32 |  |
| `c02` | float32 |  |
| `c03` | float32 |  |
| `c04` | float32 |  |
| `flAxialModelDist` | float32 |  |
| `flAxialModelWeights` | float32[4] |  |
| `m_nNode` | uint16[4] |  |

### PhysFeModelDesc_t

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
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
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_CtrlHash` | CUtlVector< uint32 > |  |
| `m_CtrlName` | CUtlVector< CUtlString > |  |
| `m_nStaticNodeFlags` | uint32 |  |
| `m_nDynamicNodeFlags` | uint32 |  |
| `m_flLocalForce` | float32 |  |
| `m_flLocalRotation` | float32 |  |
| `m_nNodeCount` | uint16 |  |
| `m_nStaticNodes` | uint16 |  |
| `m_nRotLockStaticNodes` | uint16 |  |
| `m_nFirstPositionDrivenNode` | uint16 |  |
| `m_nSimdTriCount1` | uint16 |  |
| `m_nSimdTriCount2` | uint16 |  |
| `m_nSimdQuadCount1` | uint16 |  |
| `m_nSimdQuadCount2` | uint16 |  |
| `m_nQuadCount1` | uint16 |  |
| `m_nQuadCount2` | uint16 |  |
| `m_nTreeDepth` | uint16 |  |
| `m_nNodeBaseJiggleboneDependsCount` | uint16 |  |
| `m_nRopeCount` | uint16 |  |
| `m_Ropes` | CUtlVector< uint16 > |  |
| `m_NodeBases` | CUtlVector< [FeNodeBase_t](../schemas/physicslib.md#fenodebase_t) > |  |
| `m_SimdNodeBases` | CUtlVector< [FeSimdNodeBase_t](../schemas/physicslib.md#fesimdnodebase_t) > |  |
| `m_Quads` | CUtlVector< [FeQuad_t](../schemas/physicslib.md#fequad_t) > |  |
| `m_SimdQuads` | CUtlVector< [FeSimdQuad_t](../schemas/physicslib.md#fesimdquad_t) > |  |
| `m_SimdTris` | CUtlVector< [FeSimdTri_t](../schemas/physicslib.md#fesimdtri_t) > |  |
| `m_SimdRods` | CUtlVector< [FeSimdRodConstraint_t](../schemas/physicslib.md#fesimdrodconstraint_t) > |  |
| `m_SimdRodsAnim` | CUtlVector< [FeSimdRodConstraintAnim_t](../schemas/physicslib.md#fesimdrodconstraintanim_t) > |  |
| `m_InitPose` | CUtlVector< CTransform > |  |
| `m_Rods` | CUtlVector< [FeRodConstraint_t](../schemas/physicslib.md#ferodconstraint_t) > |  |
| `m_Twists` | CUtlVector< [FeTwistConstraint_t](../schemas/physicslib.md#fetwistconstraint_t) > |  |
| `m_HingeLimits` | CUtlVector< [FeHingeLimit_t](../schemas/physicslib.md#fehingelimit_t) > |  |
| `m_AntiTunnelBytecode` | CUtlVector< uint32 > |  |
| `m_DynKinLinks` | CUtlVector< [FeDynKinLink_t](../schemas/physicslib.md#fedynkinlink_t) > |  |
| `m_BoneMergeLinks` | CUtlVector< [FeBoneMergeLink_t](../schemas/physicslib.md#febonemergelink_t) > |  |
| `m_AntiTunnelProbes` | CUtlVector< [FeAntiTunnelProbe_t](../schemas/physicslib.md#feantitunnelprobe_t) > |  |
| `m_AntiTunnelTargetNodes` | CUtlVector< uint16 > |  |
| `m_NodeStrayBoxes` | CUtlVector< [FeNodeStrayBox_t](../schemas/physicslib.md#fenodestraybox_t) > |  |
| `m_AxialEdges` | CUtlVector< [FeAxialEdgeBend_t](../schemas/physicslib.md#feaxialedgebend_t) > |  |
| `m_NodeInvMasses` | CUtlVector< float32 > |  |
| `m_CtrlOffsets` | CUtlVector< [FeCtrlOffset_t](../schemas/physicslib.md#fectrloffset_t) > |  |
| `m_CtrlOsOffsets` | CUtlVector< [FeCtrlOsOffset_t](../schemas/physicslib.md#fectrlosoffset_t) > |  |
| `m_FollowNodes` | CUtlVector< [FeFollowNode_t](../schemas/physicslib.md#fefollownode_t) > |  |
| `m_CollisionPlanes` | CUtlVector< [FeCollisionPlane_t](../schemas/physicslib.md#fecollisionplane_t) > |  |
| `m_NodeIntegrator` | CUtlVector< [FeNodeIntegrator_t](../schemas/physicslib.md#fenodeintegrator_t) > |  |
| `m_SpringIntegrator` | CUtlVector< [FeSpringIntegrator_t](../schemas/physicslib.md#fespringintegrator_t) > |  |
| `m_SimdSpringIntegrator` | CUtlVector< [FeSimdSpringIntegrator_t](../schemas/physicslib.md#fesimdspringintegrator_t) > |  |
| `m_WorldCollisionParams` | CUtlVector< [FeWorldCollisionParams_t](../schemas/physicslib.md#feworldcollisionparams_t) > |  |
| `m_LegacyStretchForce` | CUtlVector< float32 > |  |
| `m_NodeCollisionRadii` | CUtlVector< float32 > |  |
| `m_DynNodeFriction` | CUtlVector< float32 > |  |
| `m_LocalRotation` | CUtlVector< float32 > |  |
| `m_LocalForce` | CUtlVector< float32 > |  |
| `m_TaperedCapsuleStretches` | CUtlVector< [FeTaperedCapsuleStretch_t](../schemas/physicslib.md#fetaperedcapsulestretch_t) > |  |
| `m_TaperedCapsuleRigids` | CUtlVector< [FeTaperedCapsuleRigid_t](../schemas/physicslib.md#fetaperedcapsulerigid_t) > |  |
| `m_SphereRigids` | CUtlVector< [FeSphereRigid_t](../schemas/physicslib.md#fesphererigid_t) > |  |
| `m_WorldCollisionNodes` | CUtlVector< uint16 > |  |
| `m_TreeParents` | CUtlVector< uint16 > |  |
| `m_TreeCollisionMasks` | CUtlVector< uint16 > |  |
| `m_TreeChildren` | CUtlVector< [FeTreeChildren_t](../schemas/physicslib.md#fetreechildren_t) > |  |
| `m_FreeNodes` | CUtlVector< uint16 > |  |
| `m_FitMatrices` | CUtlVector< [FeFitMatrix_t](../schemas/physicslib.md#fefitmatrix_t) > |  |
| `m_FitWeights` | CUtlVector< [FeFitWeight_t](../schemas/physicslib.md#fefitweight_t) > |  |
| `m_ReverseOffsets` | CUtlVector< [FeNodeReverseOffset_t](../schemas/physicslib.md#fenodereverseoffset_t) > |  |
| `m_AnimStrayRadii` | CUtlVector< [FeAnimStrayRadius_t](../schemas/physicslib.md#feanimstrayradius_t) > |  |
| `m_SimdAnimStrayRadii` | CUtlVector< [FeSimdAnimStrayRadius_t](../schemas/physicslib.md#fesimdanimstrayradius_t) > |  |
| `m_KelagerBends` | CUtlVector< [FeKelagerBend2_t](../schemas/physicslib.md#fekelagerbend2_t) > |  |
| `m_CtrlSoftOffsets` | CUtlVector< [FeCtrlSoftOffset_t](../schemas/physicslib.md#fectrlsoftoffset_t) > |  |
| `m_JiggleBones` | CUtlVector< [CFeIndexedJiggleBone](../schemas/physicslib.md#cfeindexedjigglebone) > |  |
| `m_SourceElems` | CUtlVector< uint16 > |  |
| `m_GoalDampedSpringIntegrators` | CUtlVector< uint32 > |  |
| `m_Tris` | CUtlVector< [FeTri_t](../schemas/physicslib.md#fetri_t) > |  |
| `m_nTriCount1` | uint16 |  |
| `m_nTriCount2` | uint16 |  |
| `m_nReservedUint8` | uint8 |  |
| `m_nExtraPressureIterations` | uint8 |  |
| `m_nExtraGoalIterations` | uint8 |  |
| `m_nExtraIterations` | uint8 |  |
| `m_SDFRigids` | CUtlVector< [FeSDFRigid_t](../schemas/physicslib.md#fesdfrigid_t) > |  |
| `m_BoxRigids` | CUtlVector< [FeBoxRigid_t](../schemas/physicslib.md#feboxrigid_t) > |  |
| `m_DynNodeVertexSet` | CUtlVector< uint8 > |  |
| `m_VertexSetNames` | CUtlVector< uint32 > |  |
| `m_RigidColliderPriorities` | CUtlVector< [FeRigidColliderIndices_t](../schemas/physicslib.md#ferigidcolliderindices_t) > |  |
| `m_MorphLayers` | CUtlVector< [FeMorphLayerDepr_t](../schemas/physicslib.md#femorphlayerdepr_t) > |  |
| `m_MorphSetData` | CUtlVector< uint8 > |  |
| `m_VertexMaps` | CUtlVector< [FeVertexMapDesc_t](../schemas/physicslib.md#fevertexmapdesc_t) > |  |
| `m_VertexMapValues` | CUtlVector< uint8 > |  |
| `m_Effects` | CUtlVector< [FeEffectDesc_t](../schemas/physicslib.md#feeffectdesc_t) > |  |
| `m_LockToParent` | CUtlVector< [FeCtrlOffset_t](../schemas/physicslib.md#fectrloffset_t) > |  |
| `m_LockToGoal` | CUtlVector< uint16 > |  |
| `m_SkelParents` | CUtlVector< int16 > |  |
| `m_DynNodeWindBases` | CUtlVector< [FeNodeWindBase_t](../schemas/physicslib.md#fenodewindbase_t) > |  |
| `m_SelfCollisionLayers` | CUtlVector< [FeModelSelfCollisionLayer_t](../schemas/physicslib.md#femodelselfcollisionlayer_t) > |  |
| `m_flInternalPressure` | float32 |  |
| `m_flDefaultTimeDilation` | float32 |  |
| `m_flWindage` | float32 |  |
| `m_flWindDrag` | float32 |  |
| `m_flDefaultSurfaceStretch` | float32 |  |
| `m_flDefaultThreadStretch` | float32 |  |
| `m_flDefaultGravityScale` | float32 |  |
| `m_flDefaultVelAirDrag` | float32 |  |
| `m_flDefaultExpAirDrag` | float32 |  |
| `m_flDefaultVelQuadAirDrag` | float32 |  |
| `m_flDefaultExpQuadAirDrag` | float32 |  |
| `m_flRodVelocitySmoothRate` | float32 |  |
| `m_flQuadVelocitySmoothRate` | float32 |  |
| `m_flAddWorldCollisionRadius` | float32 |  |
| `m_flDefaultVolumetricSolveAmount` | float32 |  |
| `m_flMotionSmoothCDT` | float32 |  |
| `m_flLocalDrag1` | float32 |  |
| `m_nRodVelocitySmoothIterations` | uint16 |  |
| `m_nQuadVelocitySmoothIterations` | uint16 |  |

### PhysicsParticleId_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | uint32 |  |

### RnBlendVertex_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nWeight0` | uint16 |  |
| `m_nIndex0` | uint16 |  |
| `m_nWeight1` | uint16 |  |
| `m_nIndex1` | uint16 |  |
| `m_nWeight2` | uint16 |  |
| `m_nIndex2` | uint16 |  |
| `m_nFlags` | uint16 |  |
| `m_nTargetIndex` | uint16 |  |

### RnBodyDesc_t

**Derived by:** [vphysics_save_cphysicsbody_t](vphysics2.md#vphysics_save_cphysicsbody_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    RnBodyDesc_t <|-- vphysics_save_cphysicsbody_t
    RnBodyDesc_t *-- DynamicContinuousContactBehavior_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_sDebugName` | CUtlString |  |
| `m_vPosition` | VectorWS |  |
| `m_qOrientation` | QuaternionStorage |  |
| `m_vLinearVelocity` | Vector |  |
| `m_vAngularVelocity` | Vector |  |
| `m_vLocalMassCenter` | Vector |  |
| `m_LocalInertiaInv` | Vector[3] |  |
| `m_flMassInv` | float32 |  |
| `m_flGameMass` | float32 |  |
| `m_flMassScaleInv` | float32 |  |
| `m_flInertiaScaleInv` | float32 |  |
| `m_flLinearDamping` | float32 |  |
| `m_flAngularDamping` | float32 |  |
| `m_flLinearDragScale` | float32 |  |
| `m_flAngularDragScale` | float32 |  |
| `m_flLinearFluidDragScale` | float32 |  |
| `m_flAngularFluidDragScale` | float32 |  |
| `m_vLastAwakeForceAccum` | Vector |  |
| `m_vLastAwakeTorqueAccum` | Vector |  |
| `m_flBuoyancyScale` | float32 |  |
| `m_flGravityScale` | float32 |  |
| `m_flTimeScale` | float32 |  |
| `m_nBodyType` | int32 |  |
| `m_nGameIndex` | uint32 |  |
| `m_nGameFlags` | uint32 |  |
| `m_nMinVelocityIterations` | int8 |  |
| `m_nMinPositionIterations` | int8 |  |
| `m_nMassPriority` | int8 |  |
| `m_bEnabled` | bool |  |
| `m_bSleeping` | bool |  |
| `m_bIsContinuousEnabled` | bool |  |
| `m_bDragEnabled` | bool |  |
| `m_vGravity` | Vector |  |
| `m_bSpeculativeEnabled` | bool |  |
| `m_bHasShadowController` | bool |  |
| `m_nDynamicContinuousContactBehavior` | [DynamicContinuousContactBehavior_t](../schemas/!GlobalTypes.md#dynamiccontinuouscontactbehavior_t) |  |

### RnCapsuleDesc_t

**Inherits from:** [RnShapeDesc_t](physicslib.md#rnshapedesc_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    RnShapeDesc_t <|-- RnCapsuleDesc_t
    RnCapsuleDesc_t *-- RnCapsule_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Capsule` | [RnCapsule_t](../schemas/physicslib.md#rncapsule_t) |  |

### RnCapsule_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vCenter` | Vector[2] |  |
| `m_flRadius` | float32 |  |

### RnCompoundDesc_t

**Inherits from:** [RnShapeDesc_t](physicslib.md#rnshapedesc_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    RnShapeDesc_t <|-- RnCompoundDesc_t
    RnCompoundDesc_t *-- RnCompound_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Compound` | [RnCompound_t](../schemas/physicslib.md#rncompound_t) |  |

### RnCompound_t

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    RnCompound_t *-- RnCapsule_t
    RnCompound_t *-- RnHull_t
    RnCompound_t *-- RnMesh_t
    RnCompound_t *-- AABB_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Spheres` | CUtlVector< RnSphere_t > |  |
| `m_Capsules` | CUtlVector< [RnCapsule_t](../schemas/physicslib.md#rncapsule_t) > |  |
| `m_Hulls` | CUtlVector< [RnHull_t](../schemas/physicslib.md#rnhull_t) > |  |
| `m_Meshes` | CUtlVector< [RnMesh_t](../schemas/physicslib.md#rnmesh_t) > |  |
| `m_Bounds` | [AABB_t](../schemas/mathlib_extended.md#aabb_t) |  |
| `m_vOrthographicAreas` | Vector |  |
| `m_flSurfaceArea` | float32 |  |
| `m_flVolume` | float32 |  |

### RnFace_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nEdge` | uint8 |  |

### RnHalfEdge_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nNext` | uint8 |  |
| `m_nTwin` | uint8 |  |
| `m_nOrigin` | uint8 |  |
| `m_nFace` | uint8 |  |

### RnHullDesc_t

**Inherits from:** [RnShapeDesc_t](physicslib.md#rnshapedesc_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    RnShapeDesc_t <|-- RnHullDesc_t
    RnHullDesc_t *-- RnHull_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Hull` | [RnHull_t](../schemas/physicslib.md#rnhull_t) |  |

### RnHull_t

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    RnHull_t *-- AABB_t
    RnHull_t *-- RnPlane_t
    RnHull_t --> CRegionSVM
    RnHull_t *-- RnVertex_t
    RnHull_t *-- RnHalfEdge_t
    RnHull_t *-- RnFace_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vCentroid` | Vector |  |
| `m_flMaxAngularRadius` | float32 |  |
| `m_Bounds` | [AABB_t](../schemas/mathlib_extended.md#aabb_t) |  |
| `m_vOrthographicAreas` | Vector |  |
| `m_MassProperties` | matrix3x4_t |  |
| `m_flVolume` | float32 |  |
| `m_flSurfaceArea` | float32 |  |
| `m_VertexPositions` | CUtlVector< Vector > |  |
| `m_FacePlanes` | CUtlVector< [RnPlane_t](../schemas/physicslib.md#rnplane_t) > |  |
| `m_nFlags` | uint32 |  |
| `m_pRegionSVM` | [CRegionSVM](../schemas/physicslib.md#cregionsvm)* |  |
| `m_Vertices` | CUtlVector< [RnVertex_t](../schemas/physicslib.md#rnvertex_t) > |  |
| `m_Edges` | CUtlVector< [RnHalfEdge_t](../schemas/physicslib.md#rnhalfedge_t) > |  |
| `m_Faces` | CUtlVector< [RnFace_t](../schemas/physicslib.md#rnface_t) > |  |

### RnMeshDesc_t

**Inherits from:** [RnShapeDesc_t](physicslib.md#rnshapedesc_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    RnShapeDesc_t <|-- RnMeshDesc_t
    RnMeshDesc_t *-- RnMesh_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Mesh` | [RnMesh_t](../schemas/physicslib.md#rnmesh_t) |  |

### RnMesh_t

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    RnMesh_t *-- RnNode_t
    RnMesh_t *-- RnTriangle_t
    RnMesh_t *-- RnWing_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vMin` | Vector |  |
| `m_vMax` | Vector |  |
| `m_Nodes` | CUtlVector< [RnNode_t](../schemas/physicslib.md#rnnode_t) > |  |
| `m_Vertices` | CUtlVectorSIMDPaddedVector |  |
| `m_Triangles` | CUtlVector< [RnTriangle_t](../schemas/physicslib.md#rntriangle_t) > |  |
| `m_Wings` | CUtlVector< [RnWing_t](../schemas/physicslib.md#rnwing_t) > |  |
| `m_TriangleEdgeFlags` | CUtlVector< uint8 > |  |
| `m_Materials` | CUtlVector< uint8 > |  |
| `m_vOrthographicAreas` | Vector |  |
| `m_nFlags` | uint32 |  |
| `m_nDebugFlags` | uint32 |  |

### RnNode_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vMin` | Vector |  |
| `m_nChildren` | uint32 |  |
| `m_vMax` | Vector |  |
| `m_nTriangleOffset` | uint32 |  |

### RnPlane_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vNormal` | Vector |  |
| `m_flOffset` | float32 |  |

### RnShapeDesc_t

**Derived by:** [RnCapsuleDesc_t](physicslib.md#rncapsuledesc_t), [RnCompoundDesc_t](physicslib.md#rncompounddesc_t), [RnHullDesc_t](physicslib.md#rnhulldesc_t), [RnMeshDesc_t](physicslib.md#rnmeshdesc_t), [RnSphereDesc_t](physicslib.md#rnspheredesc_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    RnShapeDesc_t <|-- RnCapsuleDesc_t
    RnShapeDesc_t <|-- RnCompoundDesc_t
    RnShapeDesc_t <|-- RnHullDesc_t
    RnShapeDesc_t <|-- RnMeshDesc_t
    RnShapeDesc_t <|-- RnSphereDesc_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nCollisionAttributeIndex` | uint32 |  |
| `m_nSurfacePropertyIndex` | uint32 |  |
| `m_UserFriendlyName` | CUtlString |  |
| `m_bUserFriendlyNameSealed` | bool |  |
| `m_bUserFriendlyNameLong` | bool |  |
| `m_nToolMaterialHash` | uint32 |  |

### RnSoftbodyCapsule_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vCenter` | Vector[2] |  |
| `m_flRadius` | float32 |  |
| `m_nParticle` | uint16[2] |  |

### RnSoftbodyParticle_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flMassInv` | float32 |  |

### RnSoftbodySpring_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nParticle` | uint16[2] |  |
| `m_flLength` | float32 |  |

### RnSphereDesc_t

**Inherits from:** [RnShapeDesc_t](physicslib.md#rnshapedesc_t)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    RnShapeDesc_t <|-- RnSphereDesc_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Sphere` | RnSphere_t |  |

### RnTriangle_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nIndex` | int32[3] |  |

### RnVertex_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nEdge` | uint8 |  |

### RnWing_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nIndex` | int32[3] |  |

### VertexPositionColor_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vPosition` | Vector |  |

### VertexPositionNormal_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vPosition` | Vector |  |
| `m_vNormal` | Vector |  |
