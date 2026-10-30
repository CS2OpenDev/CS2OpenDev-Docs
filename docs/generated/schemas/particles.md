---
title: particles
module: particles
---

# Module: particles

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

[📊 View UML Diagram](../diagrams/particles.md)

508 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CBaseRendererSource2](particles/CBaseRendererSource2.md) | class | 11992 | 65 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [CBaseTrailRenderer](particles/CBaseTrailRenderer.md) | class | 13144 | 8 | [CBaseRendererSource2](particles/CBaseRendererSource2.md) |
| [CGeneralRandomRotation](particles/CGeneralRandomRotation.md) | class | 520 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [CGeneralSpin](particles/CGeneralSpin.md) | class | 504 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [CPAssignment_t](particles/CPAssignment_t.md) | class | 1768 | 3 |  |
| [CParticleFunction](particles/CParticleFunction.md) | class | 480 | 17 |  |
| [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) | class | 480 | 0 | [CParticleFunction](particles/CParticleFunction.md) |
| [CParticleFunctionEmitter](particles/CParticleFunctionEmitter.md) | class | 488 | 1 | [CParticleFunction](particles/CParticleFunction.md) |
| [CParticleFunctionForce](particles/CParticleFunctionForce.md) | class | 496 | 0 | [CParticleFunction](particles/CParticleFunction.md) |
| [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) | class | 488 | 1 | [CParticleFunction](particles/CParticleFunction.md) |
| [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) | class | 480 | 0 | [CParticleFunction](particles/CParticleFunction.md) |
| [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) | class | 488 | 1 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) | class | 560 | 2 | [CParticleFunction](particles/CParticleFunction.md) |
| [CParticleMassCalculationParameters](particles/CParticleMassCalculationParameters.md) | class | 1136 | 4 |  |
| [CParticleSystemDefinition](particles/CParticleSystemDefinition.md) | class | 1424 | 66 | [IParticleSystemDefinition](particles/IParticleSystemDefinition.md) |
| [CParticleVisibilityInputs](particles/CParticleVisibilityInputs.md) | class | 72 | 19 |  |
| [CPathParameters](particles/CPathParameters.md) | class | 64 | 9 |  |
| [CRandomNumberGeneratorParameters](particles/CRandomNumberGeneratorParameters.md) | class | 8 | 2 |  |
| [CSpinUpdateBase](particles/CSpinUpdateBase.md) | class | 480 | 0 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_INIT_AddVectorToVector](particles/C_INIT_AddVectorToVector.md) | class | 544 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_AgeNoise](particles/C_INIT_AgeNoise.md) | class | 528 | 8 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_ChaoticAttractor](particles/C_INIT_ChaoticAttractor.md) | class | 528 | 9 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CheckParticleForWater](particles/C_INIT_CheckParticleForWater.md) | class | 1256 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_ColorLitPerParticle](particles/C_INIT_ColorLitPerParticle.md) | class | 544 | 7 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateAlongPath](particles/C_INIT_CreateAlongPath.md) | class | 1344 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateFromCPs](particles/C_INIT_CreateFromCPs.md) | class | 880 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateFromParentParticles](particles/C_INIT_CreateFromParentParticles.md) | class | 512 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateFromPlaneCache](particles/C_INIT_CreateFromPlaneCache.md) | class | 520 | 3 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateInEpitrochoid](particles/C_INIT_CreateInEpitrochoid.md) | class | 2112 | 10 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateOnGrid](particles/C_INIT_CreateOnGrid.md) | class | 2752 | 10 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateOnModel](particles/C_INIT_CreateOnModel.md) | class | 5104 | 16 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateOnModelAtHeight](particles/C_INIT_CreateOnModelAtHeight.md) | class | 5272 | 14 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateParticleImpulse](particles/C_INIT_CreateParticleImpulse.md) | class | 1632 | 5 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreatePhyllotaxis](particles/C_INIT_CreatePhyllotaxis.md) | class | 536 | 14 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateSequentialPath](particles/C_INIT_CreateSequentialPath.md) | class | 576 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateSequentialPathV2](particles/C_INIT_CreateSequentialPathV2.md) | class | 1328 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateSpiralSphere](particles/C_INIT_CreateSpiralSphere.md) | class | 2104 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateWithinBox](particles/C_INIT_CreateWithinBox.md) | class | 4016 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateWithinCapsuleTransform](particles/C_INIT_CreateWithinCapsuleTransform.md) | class | 5992 | 11 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateWithinCone](particles/C_INIT_CreateWithinCone.md) | class | 2112 | 7 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreateWithinSphereTransform](particles/C_INIT_CreateWithinSphereTransform.md) | class | 7384 | 13 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_CreationNoise](particles/C_INIT_CreationNoise.md) | class | 536 | 10 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_DistanceCull](particles/C_INIT_DistanceCull.md) | class | 880 | 3 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_DistanceToCPInit](particles/C_INIT_DistanceToCPInit.md) | class | 2552 | 15 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_DistanceToNeighborCull](particles/C_INIT_DistanceToNeighborCull.md) | class | 1640 | 7 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_GlobalScale](particles/C_INIT_GlobalScale.md) | class | 504 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InheritFromParentParticles](particles/C_INIT_InheritFromParentParticles.md) | class | 512 | 5 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InheritVelocity](particles/C_INIT_InheritVelocity.md) | class | 496 | 2 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InitFloat](particles/C_INIT_InitFloat.md) | class | 1256 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InitFloatCollection](particles/C_INIT_InitFloatCollection.md) | class | 872 | 2 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InitFromCPSnapshot](particles/C_INIT_InitFromCPSnapshot.md) | class | 1280 | 11 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InitFromParentKilled](particles/C_INIT_InitFromParentKilled.md) | class | 624 | 2 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InitFromVectorFieldSnapshot](particles/C_INIT_InitFromVectorFieldSnapshot.md) | class | 2256 | 5 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InitSkinnedPositionFromCPSnapshot](particles/C_INIT_InitSkinnedPositionFromCPSnapshot.md) | class | 920 | 19 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InitVec](particles/C_INIT_InitVec.md) | class | 2256 | 5 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InitVecCollection](particles/C_INIT_InitVecCollection.md) | class | 2248 | 2 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InitialRepulsionVelocity](particles/C_INIT_InitialRepulsionVelocity.md) | class | 672 | 13 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InitialSequenceFromModel](particles/C_INIT_InitialSequenceFromModel.md) | class | 520 | 8 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InitialVelocityFromHitbox](particles/C_INIT_InitialVelocityFromHitbox.md) | class | 632 | 5 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_InitialVelocityNoise](particles/C_INIT_InitialVelocityNoise.md) | class | 7008 | 10 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_LifespanFromVelocity](particles/C_INIT_LifespanFromVelocity.md) | class | 672 | 8 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_ModelCull](particles/C_INIT_ModelCull.md) | class | 624 | 5 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_MoveBetweenPoints](particles/C_INIT_MoveBetweenPoints.md) | class | 2376 | 7 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_NormalAlignToCP](particles/C_INIT_NormalAlignToCP.md) | class | 600 | 2 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_NormalOffset](particles/C_INIT_NormalOffset.md) | class | 520 | 5 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_OffsetVectorToVector](particles/C_INIT_OffsetVectorToVector.md) | class | 528 | 5 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_Orient2DRelToCP](particles/C_INIT_Orient2DRelToCP.md) | class | 504 | 3 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_PlaneCull](particles/C_INIT_PlaneCull.md) | class | 880 | 3 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_PointList](particles/C_INIT_PointList.md) | class | 528 | 5 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_PositionOffset](particles/C_INIT_PositionOffset.md) | class | 4112 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_PositionOffsetToCP](particles/C_INIT_PositionOffsetToCP.md) | class | 504 | 3 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_PositionPlaceOnGround](particles/C_INIT_PositionPlaceOnGround.md) | class | 3176 | 15 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_PositionWarp](particles/C_INIT_PositionWarp.md) | class | 4024 | 10 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_PositionWarpScalar](particles/C_INIT_PositionWarpScalar.md) | class | 904 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_QuantizeFloat](particles/C_INIT_QuantizeFloat.md) | class | 872 | 2 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RadiusFromCPObject](particles/C_INIT_RadiusFromCPObject.md) | class | 496 | 1 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomAlpha](particles/C_INIT_RandomAlpha.md) | class | 512 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomAlphaWindowThreshold](particles/C_INIT_RandomAlphaWindowThreshold.md) | class | 504 | 3 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomColor](particles/C_INIT_RandomColor.md) | class | 560 | 10 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomLifeTime](particles/C_INIT_RandomLifeTime.md) | class | 504 | 3 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomModelSequence](particles/C_INIT_RandomModelSequence.md) | class | 1008 | 3 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomNamedModelBodyPart](particles/C_INIT_RandomNamedModelBodyPart.md) | class | 528 | 0 | [C_INIT_RandomNamedModelElement](particles/C_INIT_RandomNamedModelElement.md) |
| [C_INIT_RandomNamedModelElement](particles/C_INIT_RandomNamedModelElement.md) | class | 528 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomNamedModelMeshGroup](particles/C_INIT_RandomNamedModelMeshGroup.md) | class | 528 | 0 | [C_INIT_RandomNamedModelElement](particles/C_INIT_RandomNamedModelElement.md) |
| [C_INIT_RandomNamedModelSequence](particles/C_INIT_RandomNamedModelSequence.md) | class | 528 | 0 | [C_INIT_RandomNamedModelElement](particles/C_INIT_RandomNamedModelElement.md) |
| [C_INIT_RandomRadius](particles/C_INIT_RandomRadius.md) | class | 504 | 3 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomRotation](particles/C_INIT_RandomRotation.md) | class | 520 | 0 | [CGeneralRandomRotation](particles/CGeneralRandomRotation.md) |
| [C_INIT_RandomRotationSpeed](particles/C_INIT_RandomRotationSpeed.md) | class | 520 | 0 | [CGeneralRandomRotation](particles/CGeneralRandomRotation.md) |
| [C_INIT_RandomScalar](particles/C_INIT_RandomScalar.md) | class | 504 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomSecondSequence](particles/C_INIT_RandomSecondSequence.md) | class | 496 | 2 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomSequence](particles/C_INIT_RandomSequence.md) | class | 560 | 5 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomTrailLength](particles/C_INIT_RandomTrailLength.md) | class | 504 | 3 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomVector](particles/C_INIT_RandomVector.md) | class | 528 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomVectorComponent](particles/C_INIT_RandomVectorComponent.md) | class | 504 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RandomYaw](particles/C_INIT_RandomYaw.md) | class | 520 | 0 | [CGeneralRandomRotation](particles/CGeneralRandomRotation.md) |
| [C_INIT_RandomYawFlip](particles/C_INIT_RandomYawFlip.md) | class | 496 | 1 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RemapInitialDirectionToTransformToVector](particles/C_INIT_RemapInitialDirectionToTransformToVector.md) | class | 624 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RemapInitialTransformDirectionToRotation](particles/C_INIT_RemapInitialTransformDirectionToRotation.md) | class | 608 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RemapInitialVisibilityScalar](particles/C_INIT_RemapInitialVisibilityScalar.md) | class | 512 | 5 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RemapNamedModelBodyPartToScalar](particles/C_INIT_RemapNamedModelBodyPartToScalar.md) | class | 560 | 0 | [C_INIT_RemapNamedModelElementToScalar](particles/C_INIT_RemapNamedModelElementToScalar.md) |
| [C_INIT_RemapNamedModelElementToScalar](particles/C_INIT_RemapNamedModelElementToScalar.md) | class | 560 | 7 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RemapNamedModelMeshGroupToScalar](particles/C_INIT_RemapNamedModelMeshGroupToScalar.md) | class | 560 | 0 | [C_INIT_RemapNamedModelElementToScalar](particles/C_INIT_RemapNamedModelElementToScalar.md) |
| [C_INIT_RemapNamedModelSequenceToScalar](particles/C_INIT_RemapNamedModelSequenceToScalar.md) | class | 560 | 0 | [C_INIT_RemapNamedModelElementToScalar](particles/C_INIT_RemapNamedModelElementToScalar.md) |
| [C_INIT_RemapParticleCountToNamedModelBodyPartScalar](particles/C_INIT_RemapParticleCountToNamedModelBodyPartScalar.md) | class | 568 | 0 | [C_INIT_RemapParticleCountToNamedModelElementScalar](particles/C_INIT_RemapParticleCountToNamedModelElementScalar.md) |
| [C_INIT_RemapParticleCountToNamedModelElementScalar](particles/C_INIT_RemapParticleCountToNamedModelElementScalar.md) | class | 568 | 4 | [C_INIT_RemapParticleCountToScalar](particles/C_INIT_RemapParticleCountToScalar.md) |
| [C_INIT_RemapParticleCountToNamedModelMeshGroupScalar](particles/C_INIT_RemapParticleCountToNamedModelMeshGroupScalar.md) | class | 568 | 0 | [C_INIT_RemapParticleCountToNamedModelElementScalar](particles/C_INIT_RemapParticleCountToNamedModelElementScalar.md) |
| [C_INIT_RemapParticleCountToNamedModelSequenceScalar](particles/C_INIT_RemapParticleCountToNamedModelSequenceScalar.md) | class | 568 | 0 | [C_INIT_RemapParticleCountToNamedModelElementScalar](particles/C_INIT_RemapParticleCountToNamedModelElementScalar.md) |
| [C_INIT_RemapParticleCountToScalar](particles/C_INIT_RemapParticleCountToScalar.md) | class | 536 | 12 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RemapQAnglesToRotation](particles/C_INIT_RemapQAnglesToRotation.md) | class | 592 | 1 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RemapScalarToVector](particles/C_INIT_RemapScalarToVector.md) | class | 560 | 12 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RemapTransformOrientationToRotations](particles/C_INIT_RemapTransformOrientationToRotations.md) | class | 608 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RemapTransformToVector](particles/C_INIT_RemapTransformToVector.md) | class | 776 | 13 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RingWave](particles/C_INIT_RingWave.md) | class | 3608 | 11 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_RtEnvCull](particles/C_INIT_RtEnvCull.md) | class | 656 | 8 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_ScaleVelocity](particles/C_INIT_ScaleVelocity.md) | class | 2240 | 1 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_ScreenSpacePositionOfTarget](particles/C_INIT_ScreenSpacePositionOfTarget.md) | class | 2624 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_SequenceFromCP](particles/C_INIT_SequenceFromCP.md) | class | 512 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_SequenceLifeTime](particles/C_INIT_SequenceLifeTime.md) | class | 496 | 1 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_SetAttributeToScalarExpression](particles/C_INIT_SetAttributeToScalarExpression.md) | class | 1664 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_SetFloatAttributeToVectorExpression](particles/C_INIT_SetFloatAttributeToVectorExpression.md) | class | 4384 | 6 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_SetHitboxToClosest](particles/C_INIT_SetHitboxToClosest.md) | class | 2768 | 9 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_SetHitboxToModel](particles/C_INIT_SetHitboxToModel.md) | class | 2776 | 10 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_SetRigidAttachment](particles/C_INIT_SetRigidAttachment.md) | class | 504 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_SetVectorAttributeToVectorExpression](particles/C_INIT_SetVectorAttributeToVectorExpression.md) | class | 4496 | 7 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_SkyVisCull](particles/C_INIT_SkyVisCull.md) | class | 2248 | 3 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_StatusEffect](particles/C_INIT_StatusEffect.md) | class | 584 | 18 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_StatusEffectCitadel](particles/C_INIT_StatusEffectCitadel.md) | class | 568 | 19 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_StatusEffectTf](particles/C_INIT_StatusEffectTf.md) | class | 568 | 20 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_VelocityFromCP](particles/C_INIT_VelocityFromCP.md) | class | 2352 | 4 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_VelocityFromNormal](particles/C_INIT_VelocityFromNormal.md) | class | 504 | 3 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_VelocityRadialRandom](particles/C_INIT_VelocityRadialRandom.md) | class | 4768 | 8 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_INIT_VelocityRandom](particles/C_INIT_VelocityRandom.md) | class | 4768 | 7 | [CParticleFunctionInitializer](particles/CParticleFunctionInitializer.md) |
| [C_OP_AlphaDecay](particles/C_OP_AlphaDecay.md) | class | 488 | 1 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_AttractToControlPoint](particles/C_OP_AttractToControlPoint.md) | class | 1760 | 7 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_BasicMovement](particles/C_OP_BasicMovement.md) | class | 3752 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_BoxConstraint](particles/C_OP_BoxConstraint.md) | class | 3992 | 5 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [C_OP_CPOffsetToPercentageBetweenCPs](particles/C_OP_CPOffsetToPercentageBetweenCPs.md) | class | 528 | 11 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_CPVelocityForce](particles/C_OP_CPVelocityForce.md) | class | 880 | 2 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_CalculateVectorAttribute](particles/C_OP_CalculateVectorAttribute.md) | class | 576 | 11 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_Callback](particles/C_OP_Callback.md) | class | 560 | 0 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_ChladniWave](particles/C_OP_ChladniWave.md) | class | 5512 | 10 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ChooseRandomChildrenInGroup](particles/C_OP_ChooseRandomChildrenInGroup.md) | class | 872 | 2 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_ClampScalar](particles/C_OP_ClampScalar.md) | class | 1240 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ClampVector](particles/C_OP_ClampVector.md) | class | 3992 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ClientPhysics](particles/C_OP_ClientPhysics.md) | class | 1368 | 15 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_CollideWithParentParticles](particles/C_OP_CollideWithParentParticles.md) | class | 1232 | 2 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [C_OP_CollideWithSelf](particles/C_OP_CollideWithSelf.md) | class | 1232 | 2 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [C_OP_ColorAdjustHSL](particles/C_OP_ColorAdjustHSL.md) | class | 1608 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ColorInterpolate](particles/C_OP_ColorInterpolate.md) | class | 512 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ColorInterpolateRandom](particles/C_OP_ColorInterpolateRandom.md) | class | 544 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ConnectParentParticleToNearest](particles/C_OP_ConnectParentParticleToNearest.md) | class | 1248 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ConstrainDistance](particles/C_OP_ConstrainDistance.md) | class | 3096 | 5 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [C_OP_ConstrainDistanceToPath](particles/C_OP_ConstrainDistanceToPath.md) | class | 576 | 8 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [C_OP_ConstrainDistanceToUserSpecifiedPath](particles/C_OP_ConstrainDistanceToUserSpecifiedPath.md) | class | 520 | 5 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [C_OP_ConstrainLineLength](particles/C_OP_ConstrainLineLength.md) | class | 488 | 2 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [C_OP_ContinuousEmitter](particles/C_OP_ContinuousEmitter.md) | class | 1664 | 12 | [CParticleFunctionEmitter](particles/CParticleFunctionEmitter.md) |
| [C_OP_ControlPointToRadialScreenSpace](particles/C_OP_ControlPointToRadialScreenSpace.md) | class | 520 | 5 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_ControlpointLight](particles/C_OP_ControlpointLight.md) | class | 1776 | 33 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_CreateParticleSystemRenderer](particles/C_OP_CreateParticleSystemRenderer.md) | class | 2352 | 5 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_Cull](particles/C_OP_Cull.md) | class | 496 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_CurlNoiseForce](particles/C_OP_CurlNoiseForce.md) | class | 8264 | 7 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_CycleScalar](particles/C_OP_CycleScalar.md) | class | 520 | 10 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_CylindricalDistanceToTransform](particles/C_OP_CylindricalDistanceToTransform.md) | class | 2208 | 11 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_DampenToCP](particles/C_OP_DampenToCP.md) | class | 496 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_Decay](particles/C_OP_Decay.md) | class | 488 | 2 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_DecayClampCount](particles/C_OP_DecayClampCount.md) | class | 856 | 1 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_DecayMaintainCount](particles/C_OP_DecayMaintainCount.md) | class | 896 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_DecayOffscreen](particles/C_OP_DecayOffscreen.md) | class | 856 | 1 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_DensityForce](particles/C_OP_DensityForce.md) | class | 512 | 3 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_DifferencePreviousParticle](particles/C_OP_DifferencePreviousParticle.md) | class | 512 | 9 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_Diffusion](particles/C_OP_Diffusion.md) | class | 496 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_DirectionBetweenVecsToVec](particles/C_OP_DirectionBetweenVecsToVec.md) | class | 3992 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_DistanceBetweenCPsToCP](particles/C_OP_DistanceBetweenCPsToCP.md) | class | 672 | 15 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_DistanceBetweenTransforms](particles/C_OP_DistanceBetweenTransforms.md) | class | 2352 | 13 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_DistanceBetweenVecs](particles/C_OP_DistanceBetweenVecs.md) | class | 5504 | 9 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_DistanceCull](particles/C_OP_DistanceCull.md) | class | 880 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_DistanceToTransform](particles/C_OP_DistanceToTransform.md) | class | 4000 | 15 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_DragRelativeToPlane](particles/C_OP_DragRelativeToPlane.md) | class | 3000 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_DriveCPFromGlobalSoundFloat](particles/C_OP_DriveCPFromGlobalSoundFloat.md) | class | 544 | 9 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_EnableChildrenFromParentParticleCount](particles/C_OP_EnableChildrenFromParentParticleCount.md) | class | 880 | 6 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_EndCapDecay](particles/C_OP_EndCapDecay.md) | class | 480 | 0 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_EndCapTimedDecay](particles/C_OP_EndCapTimedDecay.md) | class | 856 | 1 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_EndCapTimedFreeze](particles/C_OP_EndCapTimedFreeze.md) | class | 856 | 1 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ExternalGameImpulseForce](particles/C_OP_ExternalGameImpulseForce.md) | class | 880 | 5 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_ExternalWindForce](particles/C_OP_ExternalWindForce.md) | class | 8272 | 11 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_FadeAndKill](particles/C_OP_FadeAndKill.md) | class | 512 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_FadeAndKillForTracers](particles/C_OP_FadeAndKillForTracers.md) | class | 504 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_FadeIn](particles/C_OP_FadeIn.md) | class | 496 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_FadeInSimple](particles/C_OP_FadeInSimple.md) | class | 488 | 2 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_FadeOut](particles/C_OP_FadeOut.md) | class | 560 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_FadeOutSimple](particles/C_OP_FadeOutSimple.md) | class | 488 | 2 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ForceBasedOnDistanceToPlane](particles/C_OP_ForceBasedOnDistanceToPlane.md) | class | 552 | 7 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_ForceControlPointStub](particles/C_OP_ForceControlPointStub.md) | class | 496 | 1 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_GameDecalRenderer](particles/C_OP_GameDecalRenderer.md) | class | 7360 | 16 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_GameLiquidSpill](particles/C_OP_GameLiquidSpill.md) | class | 1696 | 5 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_GlobalLight](particles/C_OP_GlobalLight.md) | class | 488 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_HSVShiftToCP](particles/C_OP_HSVShiftToCP.md) | class | 520 | 4 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_InheritFromParentParticles](particles/C_OP_InheritFromParentParticles.md) | class | 496 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_InheritFromParentParticlesV2](particles/C_OP_InheritFromParentParticlesV2.md) | class | 1624 | 8 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_InheritFromPeerSystem](particles/C_OP_InheritFromPeerSystem.md) | class | 496 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_InstantaneousEmitter](particles/C_OP_InstantaneousEmitter.md) | class | 1640 | 8 | [CParticleFunctionEmitter](particles/CParticleFunctionEmitter.md) |
| [C_OP_InterpolateRadius](particles/C_OP_InterpolateRadius.md) | class | 560 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_IntraParticleForce](particles/C_OP_IntraParticleForce.md) | class | 528 | 7 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_LagCompensation](particles/C_OP_LagCompensation.md) | class | 496 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_LazyCullCompareFloat](particles/C_OP_LazyCullCompareFloat.md) | class | 1608 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_LerpEndCapScalar](particles/C_OP_LerpEndCapScalar.md) | class | 496 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_LerpEndCapVector](particles/C_OP_LerpEndCapVector.md) | class | 504 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_LerpScalar](particles/C_OP_LerpScalar.md) | class | 872 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_LerpToInitialPosition](particles/C_OP_LerpToInitialPosition.md) | class | 3000 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_LerpToOtherAttribute](particles/C_OP_LerpToOtherAttribute.md) | class | 912 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_LerpVector](particles/C_OP_LerpVector.md) | class | 512 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_LightningSnapshotGenerator](particles/C_OP_LightningSnapshotGenerator.md) | class | 5792 | 20 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_LocalAccelerationForce](particles/C_OP_LocalAccelerationForce.md) | class | 2256 | 3 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_LockPoints](particles/C_OP_LockPoints.md) | class | 504 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_LockToBone](particles/C_OP_LockToBone.md) | class | 2976 | 15 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_LockToPointList](particles/C_OP_LockToPointList.md) | class | 520 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_LockToSavedSequentialPath](particles/C_OP_LockToSavedSequentialPath.md) | class | 560 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_LockToSavedSequentialPathV2](particles/C_OP_LockToSavedSequentialPathV2.md) | class | 560 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_MaintainEmitter](particles/C_OP_MaintainEmitter.md) | class | 1648 | 9 | [CParticleFunctionEmitter](particles/CParticleFunctionEmitter.md) |
| [C_OP_MaintainSequentialPath](particles/C_OP_MaintainSequentialPath.md) | class | 1680 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_MaxVelocity](particles/C_OP_MaxVelocity.md) | class | 1232 | 2 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ModelCull](particles/C_OP_ModelCull.md) | class | 616 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ModelDampenMovement](particles/C_OP_ModelDampenMovement.md) | class | 2376 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ModelSurfaceSnapshotGenerator](particles/C_OP_ModelSurfaceSnapshotGenerator.md) | class | 2104 | 10 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_MoveToHitbox](particles/C_OP_MoveToHitbox.md) | class | 1208 | 9 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_MovementLoopInsideSphere](particles/C_OP_MovementLoopInsideSphere.md) | class | 2624 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_MovementMaintainOffset](particles/C_OP_MovementMaintainOffset.md) | class | 504 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_MovementMoveAlongSkinnedCPSnapshot](particles/C_OP_MovementMoveAlongSkinnedCPSnapshot.md) | class | 1248 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_MovementPlaceOnGround](particles/C_OP_MovementPlaceOnGround.md) | class | 2800 | 18 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_MovementRigidAttachToCP](particles/C_OP_MovementRigidAttachToCP.md) | class | 504 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_MovementRotateParticleAroundAxis](particles/C_OP_MovementRotateParticleAroundAxis.md) | class | 2720 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_MovementSkinnedPositionFromCPSnapshot](particles/C_OP_MovementSkinnedPositionFromCPSnapshot.md) | class | 2384 | 12 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_MultiSegmentDisplaySnapshotGenerator](particles/C_OP_MultiSegmentDisplaySnapshotGenerator.md) | class | 6680 | 15 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_Noise](particles/C_OP_Noise.md) | class | 504 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_NoiseEmitter](particles/C_OP_NoiseEmitter.md) | class | 552 | 15 | [CParticleFunctionEmitter](particles/CParticleFunctionEmitter.md) |
| [C_OP_NormalLock](particles/C_OP_NormalLock.md) | class | 488 | 1 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_NormalizeVector](particles/C_OP_NormalizeVector.md) | class | 488 | 2 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_Orient2DRelToCP](particles/C_OP_Orient2DRelToCP.md) | class | 496 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_OrientTo2dDirection](particles/C_OP_OrientTo2dDirection.md) | class | 2248 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_OscillateScalar](particles/C_OP_OscillateScalar.md) | class | 528 | 13 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_OscillateScalarSimple](particles/C_OP_OscillateScalarSimple.md) | class | 544 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_OscillateVector](particles/C_OP_OscillateVector.md) | class | 1680 | 15 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_OscillateVectorSimple](particles/C_OP_OscillateVectorSimple.md) | class | 520 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ParentVortices](particles/C_OP_ParentVortices.md) | class | 520 | 3 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_PerParticleForce](particles/C_OP_PerParticleForce.md) | class | 2632 | 3 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_PercentageBetweenTransformLerpCPs](particles/C_OP_PercentageBetweenTransformLerpCPs.md) | class | 728 | 12 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_PercentageBetweenTransforms](particles/C_OP_PercentageBetweenTransforms.md) | class | 720 | 10 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_PercentageBetweenTransformsVector](particles/C_OP_PercentageBetweenTransformsVector.md) | class | 736 | 10 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_PinParticleToCP](particles/C_OP_PinParticleToCP.md) | class | 4528 | 14 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_PinRopeSegmentParticleToParent](particles/C_OP_PinRopeSegmentParticleToParent.md) | class | 1240 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_PlanarConstraint](particles/C_OP_PlanarConstraint.md) | class | 1272 | 8 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [C_OP_PlaneCull](particles/C_OP_PlaneCull.md) | class | 2248 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_PlayEndCapWhenFinished](particles/C_OP_PlayEndCapWhenFinished.md) | class | 496 | 2 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_PointVectorAtNextParticle](particles/C_OP_PointVectorAtNextParticle.md) | class | 872 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_PositionLock](particles/C_OP_PositionLock.md) | class | 2768 | 15 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_QuantizeCPComponent](particles/C_OP_QuantizeCPComponent.md) | class | 1248 | 4 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_QuantizeFloat](particles/C_OP_QuantizeFloat.md) | class | 896 | 2 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RadiusDecay](particles/C_OP_RadiusDecay.md) | class | 488 | 1 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RampCPLinearRandom](particles/C_OP_RampCPLinearRandom.md) | class | 520 | 3 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_RampScalarLinear](particles/C_OP_RampScalarLinear.md) | class | 560 | 8 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RampScalarLinearSimple](particles/C_OP_RampScalarLinearSimple.md) | class | 544 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RampScalarSpline](particles/C_OP_RampScalarSpline.md) | class | 560 | 10 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RampScalarSplineSimple](particles/C_OP_RampScalarSplineSimple.md) | class | 544 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RandomForce](particles/C_OP_RandomForce.md) | class | 520 | 2 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_ReadFromNeighboringParticle](particles/C_OP_ReadFromNeighboringParticle.md) | class | 1248 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ReinitializeScalarEndCap](particles/C_OP_ReinitializeScalarEndCap.md) | class | 496 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapAverageHitboxSpeedtoCP](particles/C_OP_RemapAverageHitboxSpeedtoCP.md) | class | 3896 | 11 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_RemapAverageScalarValuetoCP](particles/C_OP_RemapAverageScalarValuetoCP.md) | class | 1264 | 6 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_RemapBoundingVolumetoCP](particles/C_OP_RemapBoundingVolumetoCP.md) | class | 512 | 5 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_RemapCPVelocityToVector](particles/C_OP_RemapCPVelocityToVector.md) | class | 496 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapCPtoCP](particles/C_OP_RemapCPtoCP.md) | class | 528 | 10 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_RemapCPtoScalar](particles/C_OP_RemapCPtoScalar.md) | class | 528 | 11 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapCPtoVector](particles/C_OP_RemapCPtoVector.md) | class | 560 | 13 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapControlPointDirectionToVector](particles/C_OP_RemapControlPointDirectionToVector.md) | class | 496 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapControlPointOrientationToRotation](particles/C_OP_RemapControlPointOrientationToRotation.md) | class | 496 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapCrossProductOfTwoVectorsToVector](particles/C_OP_RemapCrossProductOfTwoVectorsToVector.md) | class | 3992 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapDensityGradientToVectorAttribute](particles/C_OP_RemapDensityGradientToVectorAttribute.md) | class | 488 | 2 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapDensityToVector](particles/C_OP_RemapDensityToVector.md) | class | 528 | 8 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapDirectionToCPToVector](particles/C_OP_RemapDirectionToCPToVector.md) | class | 520 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapDistanceToLineSegmentBase](particles/C_OP_RemapDistanceToLineSegmentBase.md) | class | 504 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapDistanceToLineSegmentToScalar](particles/C_OP_RemapDistanceToLineSegmentToScalar.md) | class | 520 | 3 | [C_OP_RemapDistanceToLineSegmentBase](particles/C_OP_RemapDistanceToLineSegmentBase.md) |
| [C_OP_RemapDistanceToLineSegmentToVector](particles/C_OP_RemapDistanceToLineSegmentToVector.md) | class | 536 | 3 | [C_OP_RemapDistanceToLineSegmentBase](particles/C_OP_RemapDistanceToLineSegmentBase.md) |
| [C_OP_RemapDotProductToCP](particles/C_OP_RemapDotProductToCP.md) | class | 2008 | 8 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_RemapDotProductToScalar](particles/C_OP_RemapDotProductToScalar.md) | class | 520 | 11 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapExternalWindToCP](particles/C_OP_RemapExternalWindToCP.md) | class | 2256 | 5 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_RemapGravityToVector](particles/C_OP_RemapGravityToVector.md) | class | 2352 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapModelVolumetoCP](particles/C_OP_RemapModelVolumetoCP.md) | class | 528 | 11 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_RemapNamedModelBodyPartEndCap](particles/C_OP_RemapNamedModelBodyPartEndCap.md) | class | 576 | 0 | [C_OP_RemapNamedModelElementEndCap](particles/C_OP_RemapNamedModelElementEndCap.md) |
| [C_OP_RemapNamedModelBodyPartOnceTimed](particles/C_OP_RemapNamedModelBodyPartOnceTimed.md) | class | 576 | 0 | [C_OP_RemapNamedModelElementOnceTimed](particles/C_OP_RemapNamedModelElementOnceTimed.md) |
| [C_OP_RemapNamedModelElementEndCap](particles/C_OP_RemapNamedModelElementEndCap.md) | class | 576 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapNamedModelElementOnceTimed](particles/C_OP_RemapNamedModelElementOnceTimed.md) | class | 576 | 9 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapNamedModelMeshGroupEndCap](particles/C_OP_RemapNamedModelMeshGroupEndCap.md) | class | 576 | 0 | [C_OP_RemapNamedModelElementEndCap](particles/C_OP_RemapNamedModelElementEndCap.md) |
| [C_OP_RemapNamedModelMeshGroupOnceTimed](particles/C_OP_RemapNamedModelMeshGroupOnceTimed.md) | class | 576 | 0 | [C_OP_RemapNamedModelElementOnceTimed](particles/C_OP_RemapNamedModelElementOnceTimed.md) |
| [C_OP_RemapNamedModelSequenceEndCap](particles/C_OP_RemapNamedModelSequenceEndCap.md) | class | 576 | 0 | [C_OP_RemapNamedModelElementEndCap](particles/C_OP_RemapNamedModelElementEndCap.md) |
| [C_OP_RemapNamedModelSequenceOnceTimed](particles/C_OP_RemapNamedModelSequenceOnceTimed.md) | class | 576 | 0 | [C_OP_RemapNamedModelElementOnceTimed](particles/C_OP_RemapNamedModelElementOnceTimed.md) |
| [C_OP_RemapParticleCountOnScalarEndCap](particles/C_OP_RemapParticleCountOnScalarEndCap.md) | class | 512 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapParticleCountToScalar](particles/C_OP_RemapParticleCountToScalar.md) | class | 2000 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapScalar](particles/C_OP_RemapScalar.md) | class | 512 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapScalarEndCap](particles/C_OP_RemapScalarEndCap.md) | class | 504 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapScalarOnceTimed](particles/C_OP_RemapScalarOnceTimed.md) | class | 512 | 8 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapSpeed](particles/C_OP_RemapSpeed.md) | class | 512 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapSpeedtoCP](particles/C_OP_RemapSpeedtoCP.md) | class | 520 | 8 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_RemapTransformOrientationToRotations](particles/C_OP_RemapTransformOrientationToRotations.md) | class | 600 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapTransformOrientationToYaw](particles/C_OP_RemapTransformOrientationToYaw.md) | class | 600 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapTransformToVelocity](particles/C_OP_RemapTransformToVelocity.md) | class | 584 | 1 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapTransformVisibilityToScalar](particles/C_OP_RemapTransformVisibilityToScalar.md) | class | 616 | 8 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapTransformVisibilityToVector](particles/C_OP_RemapTransformVisibilityToVector.md) | class | 632 | 8 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapVectorComponentToScalar](particles/C_OP_RemapVectorComponentToScalar.md) | class | 496 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapVectorToRotations](particles/C_OP_RemapVectorToRotations.md) | class | 3984 | 2 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapVectortoCP](particles/C_OP_RemapVectortoCP.md) | class | 496 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapVelocityToVector](particles/C_OP_RemapVelocityToVector.md) | class | 496 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RemapVisibilityScalar](particles/C_OP_RemapVisibilityScalar.md) | class | 512 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RenderAsModels](particles/C_OP_RenderAsModels.md) | class | 616 | 8 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderBlobs](particles/C_OP_RenderBlobs.md) | class | 1760 | 8 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderCables](particles/C_OP_RenderCables.md) | class | 5544 | 24 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderClientPhysicsImpulse](particles/C_OP_RenderClientPhysicsImpulse.md) | class | 1320 | 3 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderClothForce](particles/C_OP_RenderClothForce.md) | class | 560 | 0 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderDeferredLight](particles/C_OP_RenderDeferredLight.md) | class | 2376 | 16 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderFlattenGrass](particles/C_OP_RenderFlattenGrass.md) | class | 576 | 3 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderGpuImplicit](particles/C_OP_RenderGpuImplicit.md) | class | 1720 | 8 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderLightBeam](particles/C_OP_RenderLightBeam.md) | class | 8248 | 20 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderLights](particles/C_OP_RenderLights.md) | class | 600 | 7 | [C_OP_RenderPoints](particles/C_OP_RenderPoints.md) |
| [C_OP_RenderMaterialProxy](particles/C_OP_RenderMaterialProxy.md) | class | 3136 | 8 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderModels](particles/C_OP_RenderModels.md) | class | 12008 | 58 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderOmni2Light](particles/C_OP_RenderOmni2Light.md) | class | 11912 | 30 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderPoints](particles/C_OP_RenderPoints.md) | class | 568 | 1 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderPostProcessing](particles/C_OP_RenderPostProcessing.md) | class | 952 | 3 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderProjected](particles/C_OP_RenderProjected.md) | class | 3928 | 18 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderRopes](particles/C_OP_RenderRopes.md) | class | 13608 | 33 | [CBaseRendererSource2](particles/CBaseRendererSource2.md) |
| [C_OP_RenderScreenShake](particles/C_OP_RenderScreenShake.md) | class | 600 | 9 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderScreenVelocityRotate](particles/C_OP_RenderScreenVelocityRotate.md) | class | 568 | 2 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderSimpleModelCollection](particles/C_OP_RenderSimpleModelCollection.md) | class | 1456 | 9 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderSound](particles/C_OP_RenderSound.md) | class | 864 | 12 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderSprites](particles/C_OP_RenderSprites.md) | class | 16840 | 29 | [CBaseRendererSource2](particles/CBaseRendererSource2.md) |
| [C_OP_RenderStandardLight](particles/C_OP_RenderStandardLight.md) | class | 6184 | 34 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderStatusEffect](particles/C_OP_RenderStatusEffect.md) | class | 616 | 7 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderStatusEffectCitadel](particles/C_OP_RenderStatusEffectCitadel.md) | class | 608 | 6 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderStatusEffectTf](particles/C_OP_RenderStatusEffectTf.md) | class | 616 | 7 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderText](particles/C_OP_RenderText.md) | class | 576 | 2 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderTrails](particles/C_OP_RenderTrails.md) | class | 18208 | 20 | [CBaseTrailRenderer](particles/CBaseTrailRenderer.md) |
| [C_OP_RenderTreeShake](particles/C_OP_RenderTreeShake.md) | class | 600 | 10 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderVRHapticEvent](particles/C_OP_RenderVRHapticEvent.md) | class | 952 | 4 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RenderVolumetricEmitter](particles/C_OP_RenderVolumetricEmitter.md) | class | 8848 | 15 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_RepeatedTriggerChildGroup](particles/C_OP_RepeatedTriggerChildGroup.md) | class | 1632 | 5 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_RestartAfterDuration](particles/C_OP_RestartAfterDuration.md) | class | 504 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RopeSpringConstraint](particles/C_OP_RopeSpringConstraint.md) | class | 1992 | 5 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [C_OP_RotateVector](particles/C_OP_RotateVector.md) | class | 896 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_RtEnvCull](particles/C_OP_RtEnvCull.md) | class | 648 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ScreenSpaceDistanceToEdge](particles/C_OP_ScreenSpaceDistanceToEdge.md) | class | 1280 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ScreenSpacePositionOfTarget](particles/C_OP_ScreenSpacePositionOfTarget.md) | class | 2624 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ScreenSpaceRotateTowardTarget](particles/C_OP_ScreenSpaceRotateTowardTarget.md) | class | 2992 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SelectivelyEnableChildren](particles/C_OP_SelectivelyEnableChildren.md) | class | 1624 | 5 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SequenceFromModel](particles/C_OP_SequenceFromModel.md) | class | 512 | 8 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetAttributeToScalarExpression](particles/C_OP_SetAttributeToScalarExpression.md) | class | 1664 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetCPOrientationToDirection](particles/C_OP_SetCPOrientationToDirection.md) | class | 488 | 2 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetCPOrientationToGroundNormal](particles/C_OP_SetCPOrientationToGroundNormal.md) | class | 656 | 9 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetCPOrientationToPointAtCP](particles/C_OP_SetCPOrientationToPointAtCP.md) | class | 880 | 6 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetCPtoVector](particles/C_OP_SetCPtoVector.md) | class | 488 | 2 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetChildControlPoints](particles/C_OP_SetChildControlPoints.md) | class | 880 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetControlPointFieldFromVectorExpression](particles/C_OP_SetControlPointFieldFromVectorExpression.md) | class | 4760 | 7 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointFieldToScalarExpression](particles/C_OP_SetControlPointFieldToScalarExpression.md) | class | 2008 | 7 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointFieldToWater](particles/C_OP_SetControlPointFieldToWater.md) | class | 504 | 3 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointFromObjectScale](particles/C_OP_SetControlPointFromObjectScale.md) | class | 496 | 2 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointOrientation](particles/C_OP_SetControlPointOrientation.md) | class | 904 | 8 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointOrientationToCPVelocity](particles/C_OP_SetControlPointOrientationToCPVelocity.md) | class | 496 | 2 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointPositionToRandomActiveCP](particles/C_OP_SetControlPointPositionToRandomActiveCP.md) | class | 880 | 4 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointPositionToTimeOfDayValue](particles/C_OP_SetControlPointPositionToTimeOfDayValue.md) | class | 640 | 3 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointPositions](particles/C_OP_SetControlPointPositions.md) | class | 560 | 12 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointRotation](particles/C_OP_SetControlPointRotation.md) | class | 2624 | 4 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointToCPVelocity](particles/C_OP_SetControlPointToCPVelocity.md) | class | 2264 | 6 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointToCenter](particles/C_OP_SetControlPointToCenter.md) | class | 512 | 4 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointToHMD](particles/C_OP_SetControlPointToHMD.md) | class | 512 | 3 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointToHand](particles/C_OP_SetControlPointToHand.md) | class | 512 | 4 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointToImpactPoint](particles/C_OP_SetControlPointToImpactPoint.md) | class | 1040 | 12 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointToPlayer](particles/C_OP_SetControlPointToPlayer.md) | class | 520 | 6 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointToVectorExpression](particles/C_OP_SetControlPointToVectorExpression.md) | class | 4384 | 6 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointToWaterSurface](particles/C_OP_SetControlPointToWaterSurface.md) | class | 896 | 7 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetControlPointsToModelParticles](particles/C_OP_SetControlPointsToModelParticles.md) | class | 752 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetControlPointsToParticle](particles/C_OP_SetControlPointsToParticle.md) | class | 512 | 8 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetFloat](particles/C_OP_SetFloat.md) | class | 1296 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetFloatAttributeToVectorExpression](particles/C_OP_SetFloatAttributeToVectorExpression.md) | class | 4376 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetFloatCollection](particles/C_OP_SetFloatCollection.md) | class | 1280 | 4 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetFromCPSnapshot](particles/C_OP_SetFromCPSnapshot.md) | class | 1656 | 13 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetGravityToCP](particles/C_OP_SetGravityToCP.md) | class | 880 | 6 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetParentControlPointsToChildCP](particles/C_OP_SetParentControlPointsToChildCP.md) | class | 512 | 5 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetPerChildControlPoint](particles/C_OP_SetPerChildControlPoint.md) | class | 1264 | 8 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetPerChildControlPointFromAttribute](particles/C_OP_SetPerChildControlPointFromAttribute.md) | class | 512 | 8 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetRandomControlPointPosition](particles/C_OP_SetRandomControlPointPosition.md) | class | 1280 | 8 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetSimulationRate](particles/C_OP_SetSimulationRate.md) | class | 864 | 1 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetSingleControlPointPosition](particles/C_OP_SetSingleControlPointPosition.md) | class | 2352 | 4 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetToCP](particles/C_OP_SetToCP.md) | class | 504 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetUserEvent](particles/C_OP_SetUserEvent.md) | class | 1624 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetVariable](particles/C_OP_SetVariable.md) | class | 2824 | 6 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_SetVec](particles/C_OP_SetVec.md) | class | 2624 | 5 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SetVectorAttributeToVectorExpression](particles/C_OP_SetVectorAttributeToVectorExpression.md) | class | 4480 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_ShapeMatchingConstraint](particles/C_OP_ShapeMatchingConstraint.md) | class | 488 | 1 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [C_OP_SnapshotRigidSkinToBones](particles/C_OP_SnapshotRigidSkinToBones.md) | class | 488 | 3 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_SnapshotSkinToBones](particles/C_OP_SnapshotSkinToBones.md) | class | 504 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_Spin](particles/C_OP_Spin.md) | class | 504 | 0 | [CGeneralSpin](particles/CGeneralSpin.md) |
| [C_OP_SpinUpdate](particles/C_OP_SpinUpdate.md) | class | 480 | 0 | [CSpinUpdateBase](particles/CSpinUpdateBase.md) |
| [C_OP_SpinYaw](particles/C_OP_SpinYaw.md) | class | 504 | 0 | [CGeneralSpin](particles/CGeneralSpin.md) |
| [C_OP_SpringToVectorConstraint](particles/C_OP_SpringToVectorConstraint.md) | class | 3736 | 5 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [C_OP_StopAfterCPDuration](particles/C_OP_StopAfterCPDuration.md) | class | 872 | 3 | [CParticleFunctionPreEmission](particles/CParticleFunctionPreEmission.md) |
| [C_OP_TeleportBeam](particles/C_OP_TeleportBeam.md) | class | 536 | 11 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_TimeVaryingForce](particles/C_OP_TimeVaryingForce.md) | class | 528 | 4 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_TurbulenceForce](particles/C_OP_TurbulenceForce.md) | class | 560 | 8 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_TwistAroundAxis](particles/C_OP_TwistAroundAxis.md) | class | 520 | 4 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_UpdateLightSource](particles/C_OP_UpdateLightSource.md) | class | 504 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_VectorFieldSnapshot](particles/C_OP_VectorFieldSnapshot.md) | class | 2640 | 9 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_VectorNoise](particles/C_OP_VectorNoise.md) | class | 520 | 7 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_VelocityDecay](particles/C_OP_VelocityDecay.md) | class | 488 | 1 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_VelocityMatchingForce](particles/C_OP_VelocityMatchingForce.md) | class | 504 | 6 | [CParticleFunctionOperator](particles/CParticleFunctionOperator.md) |
| [C_OP_WaterImpulseRenderer](particles/C_OP_WaterImpulseRenderer.md) | class | 4200 | 8 | [CParticleFunctionRenderer](particles/CParticleFunctionRenderer.md) |
| [C_OP_WindForce](particles/C_OP_WindForce.md) | class | 512 | 1 | [CParticleFunctionForce](particles/CParticleFunctionForce.md) |
| [C_OP_WorldCollideConstraint](particles/C_OP_WorldCollideConstraint.md) | class | 480 | 0 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [C_OP_WorldTraceConstraint](particles/C_OP_WorldTraceConstraint.md) | class | 2568 | 28 | [CParticleFunctionConstraint](particles/CParticleFunctionConstraint.md) |
| [CollisionGroupContext_t](particles/CollisionGroupContext_t.md) | class | 4 | 1 |  |
| [ControlPointReference_t](particles/ControlPointReference_t.md) | class | 20 | 3 |  |
| [FloatInputMaterialVariable_t](particles/FloatInputMaterialVariable_t.md) | class | 384 | 2 |  |
| [IParticleCollection](particles/IParticleCollection.md) | class | 16 | 0 |  |
| [IParticleSystemDefinition](particles/IParticleSystemDefinition.md) | class | 8 | 0 |  |
| [MaterialVariable_t](particles/MaterialVariable_t.md) | class | 16 | 3 |  |
| [ModelReference_t](particles/ModelReference_t.md) | class | 16 | 2 |  |
| [ParticleChildrenInfo_t](particles/ParticleChildrenInfo_t.md) | class | 32 | 5 |  |
| [ParticleControlPointConfiguration_t](particles/ParticleControlPointConfiguration_t.md) | class | 144 | 3 |  |
| [ParticleControlPointDriver_t](particles/ParticleControlPointDriver_t.md) | class | 64 | 6 |  |
| [ParticlePreviewBodyGroup_t](particles/ParticlePreviewBodyGroup_t.md) | class | 16 | 2 |  |
| [ParticlePreviewState_t](particles/ParticlePreviewState_t.md) | class | 112 | 18 |  |
| [PointDefinitionWithTimeValues_t](particles/PointDefinitionWithTimeValues_t.md) | class | 24 | 1 | [PointDefinition_t](particles/PointDefinition_t.md) |
| [PointDefinition_t](particles/PointDefinition_t.md) | class | 20 | 3 |  |
| [RenderProjectedMaterial_t](particles/RenderProjectedMaterial_t.md) | class | 8 | 1 |  |
| [SequenceWeightedList_t](particles/SequenceWeightedList_t.md) | class | 8 | 2 |  |
| [TextureControls_t](particles/TextureControls_t.md) | class | 2664 | 16 |  |
| [TextureGroup_t](particles/TextureGroup_t.md) | class | 3096 | 9 |  |
| [VecInputMaterialVariable_t](particles/VecInputMaterialVariable_t.md) | class | 1760 | 2 |  |
| [BBoxVolumeType_t](particles/BBoxVolumeType_t.md) | enum | — | 5 |  |
| [BlurFilterType_t](particles/BlurFilterType_t.md) | enum | — | 2 |  |
| [ClosestPointTestType_t](particles/ClosestPointTestType_t.md) | enum | — | 3 |  |
| [Detail2Combo_t](particles/Detail2Combo_t.md) | enum | — | 7 |  |
| [DetailCombo_t](particles/DetailCombo_t.md) | enum | — | 4 |  |
| [EventTypeSelection_t](particles/EventTypeSelection_t.md) | enum | — | 13 |  |
| [HitboxLerpType_t](particles/HitboxLerpType_t.md) | enum | — | 2 |  |
| [InheritableBoolType_t](particles/InheritableBoolType_t.md) | enum | — | 3 |  |
| [MaterialProxyType_t](particles/MaterialProxyType_t.md) | enum | — | 2 |  |
| [MissingParentInheritBehavior_t](particles/MissingParentInheritBehavior_t.md) | enum | — | 4 |  |
| [ModelHitboxType_t](particles/ModelHitboxType_t.md) | enum | — | 4 |  |
| [PFuncVisualizationType_t](particles/PFuncVisualizationType_t.md) | enum | — | 7 |  |
| [ParticleAlphaReferenceType_t](particles/ParticleAlphaReferenceType_t.md) | enum | — | 4 |  |
| [ParticleAttrBoxFlags_t](particles/ParticleAttrBoxFlags_t.md) | enum | — | 11 |  |
| [ParticleCollisionGroup_t](particles/ParticleCollisionGroup_t.md) | enum | — | 7 |  |
| [ParticleCollisionMask_t](particles/ParticleCollisionMask_t.md) | enum | — | 10 |  |
| [ParticleCollisionMode_t](particles/ParticleCollisionMode_t.md) | enum | — | 5 |  |
| [ParticleControlPointAxis_t](particles/ParticleControlPointAxis_t.md) | enum | — | 6 |  |
| [ParticleDepthFeatheringMode_t](particles/ParticleDepthFeatheringMode_t.md) | enum | — | 3 |  |
| [ParticleDetailLevel_t](particles/ParticleDetailLevel_t.md) | enum | — | 4 |  |
| [ParticleEndcapMode_t](particles/ParticleEndcapMode_t.md) | enum | — | 3 |  |
| [ParticleEntityPos_t](particles/ParticleEntityPos_t.md) | enum | — | 4 |  |
| [ParticleFalloffFunction_t](particles/ParticleFalloffFunction_t.md) | enum | — | 3 |  |
| [ParticleFanType_t](particles/ParticleFanType_t.md) | enum | — | 3 |  |
| [ParticleFogType_t](particles/ParticleFogType_t.md) | enum | — | 3 |  |
| [ParticleHitboxBiasType_t](particles/ParticleHitboxBiasType_t.md) | enum | — | 2 |  |
| [ParticleHitboxDataSelection_t](particles/ParticleHitboxDataSelection_t.md) | enum | — | 2 |  |
| [ParticleImpulseType_t](particles/ParticleImpulseType_t.md) | enum | — | 6 |  |
| [ParticleLightBehaviorChoiceList_t](particles/ParticleLightBehaviorChoiceList_t.md) | enum | — | 3 |  |
| [ParticleLightFogLightingMode_t](particles/ParticleLightFogLightingMode_t.md) | enum | — | 3 |  |
| [ParticleLightTypeChoiceList_t](particles/ParticleLightTypeChoiceList_t.md) | enum | — | 4 |  |
| [ParticleLightUnitChoiceList_t](particles/ParticleLightUnitChoiceList_t.md) | enum | — | 2 |  |
| [ParticleLightingQuality_t](particles/ParticleLightingQuality_t.md) | enum | — | 6 |  |
| [ParticleLightnintBranchBehavior_t](particles/ParticleLightnintBranchBehavior_t.md) | enum | — | 2 |  |
| [ParticleLiquidContents_t](particles/ParticleLiquidContents_t.md) | enum | — | 3 |  |
| [ParticleMassMode_t](particles/ParticleMassMode_t.md) | enum | — | 2 |  |
| [ParticleMultiSegmentCountSelection_t](particles/ParticleMultiSegmentCountSelection_t.md) | enum | — | 3 |  |
| [ParticleMultiSegmentInputSelection_t](particles/ParticleMultiSegmentInputSelection_t.md) | enum | — | 2 |  |
| [ParticleMultiSegmentSpecialCharacter_t](particles/ParticleMultiSegmentSpecialCharacter_t.md) | enum | — | 4 |  |
| [ParticleOmni2LighOrientationChoiceList_t](particles/ParticleOmni2LighOrientationChoiceList_t.md) | enum | — | 5 |  |
| [ParticleOmni2LightTypeChoiceList_t](particles/ParticleOmni2LightTypeChoiceList_t.md) | enum | — | 3 |  |
| [ParticleOrientationChoiceList_t](particles/ParticleOrientationChoiceList_t.md) | enum | — | 6 |  |
| [ParticleOrientationSetMode_t](particles/ParticleOrientationSetMode_t.md) | enum | — | 4 |  |
| [ParticleOrientationType_t](particles/ParticleOrientationType_t.md) | enum | — | 4 |  |
| [ParticleOutputBlendMode_t](particles/ParticleOutputBlendMode_t.md) | enum | — | 7 |  |
| [ParticleParentSetMode_t](particles/ParticleParentSetMode_t.md) | enum | — | 3 |  |
| [ParticlePinDistance_t](particles/ParticlePinDistance_t.md) | enum | — | 12 |  |
| [ParticlePostProcessPriorityGroup_t](particles/ParticlePostProcessPriorityGroup_t.md) | enum | — | 6 |  |
| [ParticleRotationLockType_t](particles/ParticleRotationLockType_t.md) | enum | — | 3 |  |
| [ParticleSelection_t](particles/ParticleSelection_t.md) | enum | — | 3 |  |
| [ParticleSequenceCropOverride_t](particles/ParticleSequenceCropOverride_t.md) | enum | — | 3 |  |
| [ParticleSortingChoiceList_t](particles/ParticleSortingChoiceList_t.md) | enum | — | 2 |  |
| [ParticleTextureLayerBlendType_t](particles/ParticleTextureLayerBlendType_t.md) | enum | — | 7 |  |
| [ParticleToolsState_t](particles/ParticleToolsState_t.md) | enum | — | 3 |  |
| [ParticleTopology_t](particles/ParticleTopology_t.md) | enum | — | 5 |  |
| [ParticleTraceMissBehavior_t](particles/ParticleTraceMissBehavior_t.md) | enum | — | 3 |  |
| [ParticleTraceSet_t](particles/ParticleTraceSet_t.md) | enum | — | 4 |  |
| [ParticleVRHandChoiceList_t](particles/ParticleVRHandChoiceList_t.md) | enum | — | 4 |  |
| [ParticleVolumetricSmokeCreationType_t](particles/ParticleVolumetricSmokeCreationType_t.md) | enum | — | 2 |  |
| [ParticleVolumetricSmokeType_t](particles/ParticleVolumetricSmokeType_t.md) | enum | — | 4 |  |
| [PetGroundType_t](particles/PetGroundType_t.md) | enum | — | 3 |  |
| [RenderModelSubModelFieldType_t](particles/RenderModelSubModelFieldType_t.md) | enum | — | 4 |  |
| [ScalarExpressionType_t](particles/ScalarExpressionType_t.md) | enum | — | 12 |  |
| [SetStatisticExpressionType_t](particles/SetStatisticExpressionType_t.md) | enum | — | 8 |  |
| [SnapshotIndexType_t](particles/SnapshotIndexType_t.md) | enum | — | 2 |  |
| [SpriteCardPerParticleScale_t](particles/SpriteCardPerParticleScale_t.md) | enum | — | 14 |  |
| [SpriteCardShaderType_t](particles/SpriteCardShaderType_t.md) | enum | — | 2 |  |
| [SpriteCardTextureChannel_t](particles/SpriteCardTextureChannel_t.md) | enum | — | 15 |  |
| [SpriteCardTextureType_t](particles/SpriteCardTextureType_t.md) | enum | — | 12 |  |
| [StandardLightingAttenuationStyle_t](particles/StandardLightingAttenuationStyle_t.md) | enum | — | 2 |  |
| [TextureRepetitionMode_t](particles/TextureRepetitionMode_t.md) | enum | — | 2 |  |
| [VectorExpressionType_t](particles/VectorExpressionType_t.md) | enum | — | 10 |  |
| [VectorFloatExpressionType_t](particles/VectorFloatExpressionType_t.md) | enum | — | 7 |  |
