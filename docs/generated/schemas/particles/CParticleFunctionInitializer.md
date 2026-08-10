---
layout: default
title: CParticleFunctionInitializer
nav_exclude: true
---

[Schemas](../../schemas.md) / [particles](../particles.md) / CParticleFunctionInitializer

# CParticleFunctionInitializer

**Kind:** class · **Size:** 480 bytes (`0x1e0`) · **Align:** 255 · **Module:** particles

**Inherits from:** [CParticleFunction](../particles/CParticleFunction.md)

**Derived by:** [CGeneralRandomRotation](../particles/CGeneralRandomRotation.md), [C_INIT_AddVectorToVector](../particles/C_INIT_AddVectorToVector.md), [C_INIT_AgeNoise](../particles/C_INIT_AgeNoise.md), [C_INIT_ChaoticAttractor](../particles/C_INIT_ChaoticAttractor.md), [C_INIT_CheckParticleForWater](../particles/C_INIT_CheckParticleForWater.md), [C_INIT_ColorLitPerParticle](../particles/C_INIT_ColorLitPerParticle.md), [C_INIT_CreateAlongPath](../particles/C_INIT_CreateAlongPath.md), [C_INIT_CreateFromCPs](../particles/C_INIT_CreateFromCPs.md), [C_INIT_CreateFromParentParticles](../particles/C_INIT_CreateFromParentParticles.md), [C_INIT_CreateFromPlaneCache](../particles/C_INIT_CreateFromPlaneCache.md), [C_INIT_CreateInEpitrochoid](../particles/C_INIT_CreateInEpitrochoid.md), [C_INIT_CreateOnGrid](../particles/C_INIT_CreateOnGrid.md), [C_INIT_CreateOnModel](../particles/C_INIT_CreateOnModel.md), [C_INIT_CreateOnModelAtHeight](../particles/C_INIT_CreateOnModelAtHeight.md), [C_INIT_CreateParticleImpulse](../particles/C_INIT_CreateParticleImpulse.md), [C_INIT_CreatePhyllotaxis](../particles/C_INIT_CreatePhyllotaxis.md), [C_INIT_CreateSequentialPath](../particles/C_INIT_CreateSequentialPath.md), [C_INIT_CreateSequentialPathV2](../particles/C_INIT_CreateSequentialPathV2.md), [C_INIT_CreateSpiralSphere](../particles/C_INIT_CreateSpiralSphere.md), [C_INIT_CreateWithinBox](../particles/C_INIT_CreateWithinBox.md), [C_INIT_CreateWithinCapsuleTransform](../particles/C_INIT_CreateWithinCapsuleTransform.md), [C_INIT_CreateWithinSphereTransform](../particles/C_INIT_CreateWithinSphereTransform.md), [C_INIT_CreationNoise](../particles/C_INIT_CreationNoise.md), [C_INIT_DistanceCull](../particles/C_INIT_DistanceCull.md), [C_INIT_DistanceToCPInit](../particles/C_INIT_DistanceToCPInit.md), [C_INIT_DistanceToNeighborCull](../particles/C_INIT_DistanceToNeighborCull.md), [C_INIT_GlobalScale](../particles/C_INIT_GlobalScale.md), [C_INIT_InheritFromParentParticles](../particles/C_INIT_InheritFromParentParticles.md), [C_INIT_InheritVelocity](../particles/C_INIT_InheritVelocity.md), [C_INIT_InitFloat](../particles/C_INIT_InitFloat.md), [C_INIT_InitFloatCollection](../particles/C_INIT_InitFloatCollection.md), [C_INIT_InitFromCPSnapshot](../particles/C_INIT_InitFromCPSnapshot.md), [C_INIT_InitFromParentKilled](../particles/C_INIT_InitFromParentKilled.md), [C_INIT_InitFromVectorFieldSnapshot](../particles/C_INIT_InitFromVectorFieldSnapshot.md), [C_INIT_InitSkinnedPositionFromCPSnapshot](../particles/C_INIT_InitSkinnedPositionFromCPSnapshot.md), [C_INIT_InitVec](../particles/C_INIT_InitVec.md), [C_INIT_InitVecCollection](../particles/C_INIT_InitVecCollection.md), [C_INIT_InitialRepulsionVelocity](../particles/C_INIT_InitialRepulsionVelocity.md), [C_INIT_InitialSequenceFromModel](../particles/C_INIT_InitialSequenceFromModel.md), [C_INIT_InitialVelocityFromHitbox](../particles/C_INIT_InitialVelocityFromHitbox.md), [C_INIT_InitialVelocityNoise](../particles/C_INIT_InitialVelocityNoise.md), [C_INIT_LifespanFromVelocity](../particles/C_INIT_LifespanFromVelocity.md), [C_INIT_ModelCull](../particles/C_INIT_ModelCull.md), [C_INIT_MoveBetweenPoints](../particles/C_INIT_MoveBetweenPoints.md), [C_INIT_NormalAlignToCP](../particles/C_INIT_NormalAlignToCP.md), [C_INIT_NormalOffset](../particles/C_INIT_NormalOffset.md), [C_INIT_OffsetVectorToVector](../particles/C_INIT_OffsetVectorToVector.md), [C_INIT_Orient2DRelToCP](../particles/C_INIT_Orient2DRelToCP.md), [C_INIT_PlaneCull](../particles/C_INIT_PlaneCull.md), [C_INIT_PointList](../particles/C_INIT_PointList.md), [C_INIT_PositionOffset](../particles/C_INIT_PositionOffset.md), [C_INIT_PositionOffsetToCP](../particles/C_INIT_PositionOffsetToCP.md), [C_INIT_PositionPlaceOnGround](../particles/C_INIT_PositionPlaceOnGround.md), [C_INIT_PositionWarp](../particles/C_INIT_PositionWarp.md), [C_INIT_PositionWarpScalar](../particles/C_INIT_PositionWarpScalar.md), [C_INIT_QuantizeFloat](../particles/C_INIT_QuantizeFloat.md), [C_INIT_RadiusFromCPObject](../particles/C_INIT_RadiusFromCPObject.md), [C_INIT_RandomAlpha](../particles/C_INIT_RandomAlpha.md), [C_INIT_RandomAlphaWindowThreshold](../particles/C_INIT_RandomAlphaWindowThreshold.md), [C_INIT_RandomColor](../particles/C_INIT_RandomColor.md), [C_INIT_RandomLifeTime](../particles/C_INIT_RandomLifeTime.md), [C_INIT_RandomModelSequence](../particles/C_INIT_RandomModelSequence.md), [C_INIT_RandomNamedModelElement](../particles/C_INIT_RandomNamedModelElement.md), [C_INIT_RandomRadius](../particles/C_INIT_RandomRadius.md), [C_INIT_RandomScalar](../particles/C_INIT_RandomScalar.md), [C_INIT_RandomSecondSequence](../particles/C_INIT_RandomSecondSequence.md), [C_INIT_RandomSequence](../particles/C_INIT_RandomSequence.md), [C_INIT_RandomTrailLength](../particles/C_INIT_RandomTrailLength.md), [C_INIT_RandomVector](../particles/C_INIT_RandomVector.md), [C_INIT_RandomVectorComponent](../particles/C_INIT_RandomVectorComponent.md), [C_INIT_RandomYawFlip](../particles/C_INIT_RandomYawFlip.md), [C_INIT_RemapInitialDirectionToTransformToVector](../particles/C_INIT_RemapInitialDirectionToTransformToVector.md), [C_INIT_RemapInitialTransformDirectionToRotation](../particles/C_INIT_RemapInitialTransformDirectionToRotation.md), [C_INIT_RemapInitialVisibilityScalar](../particles/C_INIT_RemapInitialVisibilityScalar.md), [C_INIT_RemapNamedModelElementToScalar](../particles/C_INIT_RemapNamedModelElementToScalar.md), [C_INIT_RemapParticleCountToScalar](../particles/C_INIT_RemapParticleCountToScalar.md), [C_INIT_RemapQAnglesToRotation](../particles/C_INIT_RemapQAnglesToRotation.md), [C_INIT_RemapScalarToVector](../particles/C_INIT_RemapScalarToVector.md), [C_INIT_RemapTransformOrientationToRotations](../particles/C_INIT_RemapTransformOrientationToRotations.md), [C_INIT_RemapTransformToVector](../particles/C_INIT_RemapTransformToVector.md), [C_INIT_RingWave](../particles/C_INIT_RingWave.md), [C_INIT_RtEnvCull](../particles/C_INIT_RtEnvCull.md), [C_INIT_ScaleVelocity](../particles/C_INIT_ScaleVelocity.md), [C_INIT_ScreenSpacePositionOfTarget](../particles/C_INIT_ScreenSpacePositionOfTarget.md), [C_INIT_SequenceFromCP](../particles/C_INIT_SequenceFromCP.md), [C_INIT_SequenceLifeTime](../particles/C_INIT_SequenceLifeTime.md), [C_INIT_SetAttributeToScalarExpression](../particles/C_INIT_SetAttributeToScalarExpression.md), [C_INIT_SetFloatAttributeToVectorExpression](../particles/C_INIT_SetFloatAttributeToVectorExpression.md), [C_INIT_SetHitboxToClosest](../particles/C_INIT_SetHitboxToClosest.md), [C_INIT_SetHitboxToModel](../particles/C_INIT_SetHitboxToModel.md), [C_INIT_SetRigidAttachment](../particles/C_INIT_SetRigidAttachment.md), [C_INIT_SetVectorAttributeToVectorExpression](../particles/C_INIT_SetVectorAttributeToVectorExpression.md), [C_INIT_SkyVisCull](../particles/C_INIT_SkyVisCull.md), [C_INIT_StatusEffect](../particles/C_INIT_StatusEffect.md), [C_INIT_StatusEffectCitadel](../particles/C_INIT_StatusEffectCitadel.md), [C_INIT_VelocityFromCP](../particles/C_INIT_VelocityFromCP.md), [C_INIT_VelocityFromNormal](../particles/C_INIT_VelocityFromNormal.md), [C_INIT_VelocityRadialRandom](../particles/C_INIT_VelocityRadialRandom.md), [C_INIT_VelocityRandom](../particles/C_INIT_VelocityRandom.md)

**Relationships:**

```mermaid
classDiagram
    CParticleFunction <|-- CParticleFunctionInitializer
    CParticleFunctionInitializer <|-- CGeneralRandomRotation
    CParticleFunctionInitializer <|-- C_INIT_AddVectorToVector
    CParticleFunctionInitializer <|-- C_INIT_AgeNoise
    CParticleFunctionInitializer <|-- C_INIT_ChaoticAttractor
    CParticleFunctionInitializer <|-- C_INIT_CheckParticleForWater
    CParticleFunctionInitializer <|-- C_INIT_ColorLitPerParticle
    CParticleFunctionInitializer <|-- C_INIT_CreateAlongPath
    CParticleFunctionInitializer <|-- C_INIT_CreateFromCPs
    CParticleFunctionInitializer <|-- C_INIT_CreateFromParentParticles
    CParticleFunctionInitializer <|-- C_INIT_CreateFromPlaneCache
    CParticleFunctionInitializer <|-- C_INIT_CreateInEpitrochoid
    CParticleFunctionInitializer <|-- C_INIT_CreateOnGrid
    CParticleFunctionInitializer <|-- C_INIT_CreateOnModel
    CParticleFunctionInitializer <|-- C_INIT_CreateOnModelAtHeight
    CParticleFunctionInitializer <|-- C_INIT_CreateParticleImpulse
    CParticleFunctionInitializer <|-- C_INIT_CreatePhyllotaxis
    CParticleFunctionInitializer <|-- C_INIT_CreateSequentialPath
    CParticleFunctionInitializer <|-- C_INIT_CreateSequentialPathV2
    CParticleFunctionInitializer <|-- C_INIT_CreateSpiralSphere
    CParticleFunctionInitializer <|-- C_INIT_CreateWithinBox
    CParticleFunctionInitializer <|-- C_INIT_CreateWithinCapsuleTransform
    CParticleFunctionInitializer <|-- C_INIT_CreateWithinSphereTransform
    CParticleFunctionInitializer <|-- C_INIT_CreationNoise
    CParticleFunctionInitializer <|-- C_INIT_DistanceCull
    CParticleFunctionInitializer <|-- C_INIT_DistanceToCPInit
    CParticleFunctionInitializer <|-- C_INIT_DistanceToNeighborCull
    CParticleFunctionInitializer <|-- C_INIT_GlobalScale
    CParticleFunctionInitializer <|-- C_INIT_InheritFromParentParticles
    CParticleFunctionInitializer <|-- C_INIT_InheritVelocity
    CParticleFunctionInitializer <|-- C_INIT_InitFloat
    CParticleFunctionInitializer <|-- C_INIT_InitFloatCollection
    CParticleFunctionInitializer <|-- C_INIT_InitFromCPSnapshot
    CParticleFunctionInitializer <|-- C_INIT_InitFromParentKilled
    CParticleFunctionInitializer <|-- C_INIT_InitFromVectorFieldSnapshot
    CParticleFunctionInitializer <|-- C_INIT_InitSkinnedPositionFromCPSnapshot
    CParticleFunctionInitializer <|-- C_INIT_InitVec
    CParticleFunctionInitializer <|-- C_INIT_InitVecCollection
    CParticleFunctionInitializer <|-- C_INIT_InitialRepulsionVelocity
    CParticleFunctionInitializer <|-- C_INIT_InitialSequenceFromModel
    CParticleFunctionInitializer <|-- C_INIT_InitialVelocityFromHitbox
    CParticleFunctionInitializer <|-- C_INIT_InitialVelocityNoise
    CParticleFunctionInitializer <|-- C_INIT_LifespanFromVelocity
    CParticleFunctionInitializer <|-- C_INIT_ModelCull
    CParticleFunctionInitializer <|-- C_INIT_MoveBetweenPoints
    CParticleFunctionInitializer <|-- C_INIT_NormalAlignToCP
    CParticleFunctionInitializer <|-- C_INIT_NormalOffset
    CParticleFunctionInitializer <|-- C_INIT_OffsetVectorToVector
    CParticleFunctionInitializer <|-- C_INIT_Orient2DRelToCP
    CParticleFunctionInitializer <|-- C_INIT_PlaneCull
    CParticleFunctionInitializer <|-- C_INIT_PointList
    CParticleFunctionInitializer <|-- C_INIT_PositionOffset
    CParticleFunctionInitializer <|-- C_INIT_PositionOffsetToCP
    CParticleFunctionInitializer <|-- C_INIT_PositionPlaceOnGround
    CParticleFunctionInitializer <|-- C_INIT_PositionWarp
    CParticleFunctionInitializer <|-- C_INIT_PositionWarpScalar
    CParticleFunctionInitializer <|-- C_INIT_QuantizeFloat
    CParticleFunctionInitializer <|-- C_INIT_RadiusFromCPObject
    CParticleFunctionInitializer <|-- C_INIT_RandomAlpha
    CParticleFunctionInitializer <|-- C_INIT_RandomAlphaWindowThreshold
    CParticleFunctionInitializer <|-- C_INIT_RandomColor
    CParticleFunctionInitializer <|-- C_INIT_RandomLifeTime
    CParticleFunctionInitializer <|-- C_INIT_RandomModelSequence
    CParticleFunctionInitializer <|-- C_INIT_RandomNamedModelElement
    CParticleFunctionInitializer <|-- C_INIT_RandomRadius
    CParticleFunctionInitializer <|-- C_INIT_RandomScalar
    CParticleFunctionInitializer <|-- C_INIT_RandomSecondSequence
    CParticleFunctionInitializer <|-- C_INIT_RandomSequence
    CParticleFunctionInitializer <|-- C_INIT_RandomTrailLength
    CParticleFunctionInitializer <|-- C_INIT_RandomVector
    CParticleFunctionInitializer <|-- C_INIT_RandomVectorComponent
    CParticleFunctionInitializer <|-- C_INIT_RandomYawFlip
    CParticleFunctionInitializer <|-- C_INIT_RemapInitialDirectionToTransformToVector
    CParticleFunctionInitializer <|-- C_INIT_RemapInitialTransformDirectionToRotation
    CParticleFunctionInitializer <|-- C_INIT_RemapInitialVisibilityScalar
    CParticleFunctionInitializer <|-- C_INIT_RemapNamedModelElementToScalar
    CParticleFunctionInitializer <|-- C_INIT_RemapParticleCountToScalar
    CParticleFunctionInitializer <|-- C_INIT_RemapQAnglesToRotation
    CParticleFunctionInitializer <|-- C_INIT_RemapScalarToVector
    CParticleFunctionInitializer <|-- C_INIT_RemapTransformOrientationToRotations
    CParticleFunctionInitializer <|-- C_INIT_RemapTransformToVector
    CParticleFunctionInitializer <|-- C_INIT_RingWave
    CParticleFunctionInitializer <|-- C_INIT_RtEnvCull
    CParticleFunctionInitializer <|-- C_INIT_ScaleVelocity
    CParticleFunctionInitializer <|-- C_INIT_ScreenSpacePositionOfTarget
    CParticleFunctionInitializer <|-- C_INIT_SequenceFromCP
    CParticleFunctionInitializer <|-- C_INIT_SequenceLifeTime
    CParticleFunctionInitializer <|-- C_INIT_SetAttributeToScalarExpression
    CParticleFunctionInitializer <|-- C_INIT_SetFloatAttributeToVectorExpression
    CParticleFunctionInitializer <|-- C_INIT_SetHitboxToClosest
    CParticleFunctionInitializer <|-- C_INIT_SetHitboxToModel
    CParticleFunctionInitializer <|-- C_INIT_SetRigidAttachment
    CParticleFunctionInitializer <|-- C_INIT_SetVectorAttributeToVectorExpression
    CParticleFunctionInitializer <|-- C_INIT_SkyVisCull
    CParticleFunctionInitializer <|-- C_INIT_StatusEffect
    CParticleFunctionInitializer <|-- C_INIT_StatusEffectCitadel
    CParticleFunctionInitializer <|-- C_INIT_VelocityFromCP
    CParticleFunctionInitializer <|-- C_INIT_VelocityFromNormal
    CParticleFunctionInitializer <|-- C_INIT_VelocityRadialRandom
    CParticleFunctionInitializer <|-- C_INIT_VelocityRandom
```

## Memory layout

18 fields (1 declared here, 17 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_flOpStrength` | [CParticleCollectionFloatInput](../particleslib/CParticleCollectionFloatInput.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator strength` `MPropertySortPriority -100` |
| `0x178` | `m_nOpEndCapState` | [ParticleEndcapMode_t](../particles/ParticleEndcapMode_t.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator end cap state` `MPropertySortPriority -100` |
| `0x17c` | `m_nToolsState` | [ParticleToolsState_t](../particles/ParticleToolsState_t.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator enabled in tools or game only` `MPropertySortPriority -100` |
| `0x180` | `m_flOpStartFadeInTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator start fadein` `MPropertySortPriority -100` `MPropertyStartGroup Operator Fade` |
| `0x184` | `m_flOpEndFadeInTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator end fadein` `MPropertySortPriority -100` |
| `0x188` | `m_flOpStartFadeOutTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator start fadeout` `MPropertySortPriority -100` |
| `0x18c` | `m_flOpEndFadeOutTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator end fadeout` `MPropertySortPriority -100` |
| `0x190` | `m_flOpFadeOscillatePeriod` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade oscillate` `MPropertySortPriority -100` |
| `0x194` | `m_bNormalizeToStopTime` | bool | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName normalize fade times to endcap` `MPropertySortPriority -100` |
| `0x198` | `m_flOpTimeOffsetMin` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time offset min` `MPropertySortPriority -100` `MPropertyStartGroup Operator Fade Time Offset` |
| `0x19c` | `m_flOpTimeOffsetMax` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time offset max` `MPropertySortPriority -100` |
| `0x1a0` | `m_nOpTimeOffsetSeed` | int32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time offset seed` `MPropertySortPriority -100` |
| `0x1a4` | `m_nOpTimeScaleSeed` | int32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time scale seed` `MPropertySortPriority -100` `MPropertyStartGroup Operator Fade Timescale Modifiers` |
| `0x1a8` | `m_flOpTimeScaleMin` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time scale min` `MPropertySortPriority -100` |
| `0x1ac` | `m_flOpTimeScaleMax` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time scale max` `MPropertySortPriority -100` |
| `0x1b2` | `m_bDisableOperator` | bool | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyStartGroup` `MPropertySuppressField` |
| `0x1b8` | `m_Notes` | CUtlString | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleHelpField` `MPropertyFriendlyName operator help and notes` `MPropertySortPriority -100` |
| `0x1d8` | `m_nAssociatedEmitterIndex` | int32 |  | `MPropertyFriendlyName Associated emitter Index` |
