---
layout: default
title: CParticleFunctionOperator
nav_exclude: true
---

[Schemas](../../schemas.md) / [particles](../particles.md) / CParticleFunctionOperator

# CParticleFunctionOperator

**Kind:** class · **Size:** 472 bytes (`0x1d8`) · **Align:** 255 · **Module:** particles

**Inherits from:** [CParticleFunction](../particles/CParticleFunction.md)

**Derived by:** [CGeneralSpin](../particles/CGeneralSpin.md), [CParticleFunctionPreEmission](../particles/CParticleFunctionPreEmission.md), [CSpinUpdateBase](../particles/CSpinUpdateBase.md), [C_OP_AlphaDecay](../particles/C_OP_AlphaDecay.md), [C_OP_BasicMovement](../particles/C_OP_BasicMovement.md), [C_OP_CPOffsetToPercentageBetweenCPs](../particles/C_OP_CPOffsetToPercentageBetweenCPs.md), [C_OP_CalculateVectorAttribute](../particles/C_OP_CalculateVectorAttribute.md), [C_OP_ChladniWave](../particles/C_OP_ChladniWave.md), [C_OP_ClampScalar](../particles/C_OP_ClampScalar.md), [C_OP_ClampVector](../particles/C_OP_ClampVector.md), [C_OP_ColorAdjustHSL](../particles/C_OP_ColorAdjustHSL.md), [C_OP_ColorInterpolate](../particles/C_OP_ColorInterpolate.md), [C_OP_ColorInterpolateRandom](../particles/C_OP_ColorInterpolateRandom.md), [C_OP_ConnectParentParticleToNearest](../particles/C_OP_ConnectParentParticleToNearest.md), [C_OP_ControlpointLight](../particles/C_OP_ControlpointLight.md), [C_OP_Cull](../particles/C_OP_Cull.md), [C_OP_CycleScalar](../particles/C_OP_CycleScalar.md), [C_OP_CylindricalDistanceToTransform](../particles/C_OP_CylindricalDistanceToTransform.md), [C_OP_DampenToCP](../particles/C_OP_DampenToCP.md), [C_OP_Decay](../particles/C_OP_Decay.md), [C_OP_DecayClampCount](../particles/C_OP_DecayClampCount.md), [C_OP_DecayMaintainCount](../particles/C_OP_DecayMaintainCount.md), [C_OP_DecayOffscreen](../particles/C_OP_DecayOffscreen.md), [C_OP_DifferencePreviousParticle](../particles/C_OP_DifferencePreviousParticle.md), [C_OP_Diffusion](../particles/C_OP_Diffusion.md), [C_OP_DirectionBetweenVecsToVec](../particles/C_OP_DirectionBetweenVecsToVec.md), [C_OP_DistanceBetweenTransforms](../particles/C_OP_DistanceBetweenTransforms.md), [C_OP_DistanceBetweenVecs](../particles/C_OP_DistanceBetweenVecs.md), [C_OP_DistanceCull](../particles/C_OP_DistanceCull.md), [C_OP_DistanceToTransform](../particles/C_OP_DistanceToTransform.md), [C_OP_DragRelativeToPlane](../particles/C_OP_DragRelativeToPlane.md), [C_OP_EndCapDecay](../particles/C_OP_EndCapDecay.md), [C_OP_EndCapTimedDecay](../particles/C_OP_EndCapTimedDecay.md), [C_OP_EndCapTimedFreeze](../particles/C_OP_EndCapTimedFreeze.md), [C_OP_FadeAndKill](../particles/C_OP_FadeAndKill.md), [C_OP_FadeAndKillForTracers](../particles/C_OP_FadeAndKillForTracers.md), [C_OP_FadeIn](../particles/C_OP_FadeIn.md), [C_OP_FadeInSimple](../particles/C_OP_FadeInSimple.md), [C_OP_FadeOut](../particles/C_OP_FadeOut.md), [C_OP_FadeOutSimple](../particles/C_OP_FadeOutSimple.md), [C_OP_GlobalLight](../particles/C_OP_GlobalLight.md), [C_OP_InheritFromParentParticles](../particles/C_OP_InheritFromParentParticles.md), [C_OP_InheritFromParentParticlesV2](../particles/C_OP_InheritFromParentParticlesV2.md), [C_OP_InheritFromPeerSystem](../particles/C_OP_InheritFromPeerSystem.md), [C_OP_InterpolateRadius](../particles/C_OP_InterpolateRadius.md), [C_OP_LagCompensation](../particles/C_OP_LagCompensation.md), [C_OP_LazyCullCompareFloat](../particles/C_OP_LazyCullCompareFloat.md), [C_OP_LerpEndCapScalar](../particles/C_OP_LerpEndCapScalar.md), [C_OP_LerpEndCapVector](../particles/C_OP_LerpEndCapVector.md), [C_OP_LerpScalar](../particles/C_OP_LerpScalar.md), [C_OP_LerpToInitialPosition](../particles/C_OP_LerpToInitialPosition.md), [C_OP_LerpToOtherAttribute](../particles/C_OP_LerpToOtherAttribute.md), [C_OP_LerpVector](../particles/C_OP_LerpVector.md), [C_OP_LockPoints](../particles/C_OP_LockPoints.md), [C_OP_LockToBone](../particles/C_OP_LockToBone.md), [C_OP_LockToPointList](../particles/C_OP_LockToPointList.md), [C_OP_LockToSavedSequentialPath](../particles/C_OP_LockToSavedSequentialPath.md), [C_OP_LockToSavedSequentialPathV2](../particles/C_OP_LockToSavedSequentialPathV2.md), [C_OP_MaintainSequentialPath](../particles/C_OP_MaintainSequentialPath.md), [C_OP_MaxVelocity](../particles/C_OP_MaxVelocity.md), [C_OP_ModelCull](../particles/C_OP_ModelCull.md), [C_OP_ModelDampenMovement](../particles/C_OP_ModelDampenMovement.md), [C_OP_MoveToHitbox](../particles/C_OP_MoveToHitbox.md), [C_OP_MovementLoopInsideSphere](../particles/C_OP_MovementLoopInsideSphere.md), [C_OP_MovementMaintainOffset](../particles/C_OP_MovementMaintainOffset.md), [C_OP_MovementMoveAlongSkinnedCPSnapshot](../particles/C_OP_MovementMoveAlongSkinnedCPSnapshot.md), [C_OP_MovementPlaceOnGround](../particles/C_OP_MovementPlaceOnGround.md), [C_OP_MovementRigidAttachToCP](../particles/C_OP_MovementRigidAttachToCP.md), [C_OP_MovementRotateParticleAroundAxis](../particles/C_OP_MovementRotateParticleAroundAxis.md), [C_OP_MovementSkinnedPositionFromCPSnapshot](../particles/C_OP_MovementSkinnedPositionFromCPSnapshot.md), [C_OP_Noise](../particles/C_OP_Noise.md), [C_OP_NormalLock](../particles/C_OP_NormalLock.md), [C_OP_NormalizeVector](../particles/C_OP_NormalizeVector.md), [C_OP_Orient2DRelToCP](../particles/C_OP_Orient2DRelToCP.md), [C_OP_OrientTo2dDirection](../particles/C_OP_OrientTo2dDirection.md), [C_OP_OscillateScalar](../particles/C_OP_OscillateScalar.md), [C_OP_OscillateScalarSimple](../particles/C_OP_OscillateScalarSimple.md), [C_OP_OscillateVector](../particles/C_OP_OscillateVector.md), [C_OP_OscillateVectorSimple](../particles/C_OP_OscillateVectorSimple.md), [C_OP_PercentageBetweenTransformLerpCPs](../particles/C_OP_PercentageBetweenTransformLerpCPs.md), [C_OP_PercentageBetweenTransforms](../particles/C_OP_PercentageBetweenTransforms.md), [C_OP_PercentageBetweenTransformsVector](../particles/C_OP_PercentageBetweenTransformsVector.md), [C_OP_PinParticleToCP](../particles/C_OP_PinParticleToCP.md), [C_OP_PinRopeSegmentParticleToParent](../particles/C_OP_PinRopeSegmentParticleToParent.md), [C_OP_PlaneCull](../particles/C_OP_PlaneCull.md), [C_OP_PointVectorAtNextParticle](../particles/C_OP_PointVectorAtNextParticle.md), [C_OP_PositionLock](../particles/C_OP_PositionLock.md), [C_OP_QuantizeFloat](../particles/C_OP_QuantizeFloat.md), [C_OP_RadiusDecay](../particles/C_OP_RadiusDecay.md), [C_OP_RampScalarLinear](../particles/C_OP_RampScalarLinear.md), [C_OP_RampScalarLinearSimple](../particles/C_OP_RampScalarLinearSimple.md), [C_OP_RampScalarSpline](../particles/C_OP_RampScalarSpline.md), [C_OP_RampScalarSplineSimple](../particles/C_OP_RampScalarSplineSimple.md), [C_OP_ReadFromNeighboringParticle](../particles/C_OP_ReadFromNeighboringParticle.md), [C_OP_ReinitializeScalarEndCap](../particles/C_OP_ReinitializeScalarEndCap.md), [C_OP_RemapCPVelocityToVector](../particles/C_OP_RemapCPVelocityToVector.md), [C_OP_RemapCPtoScalar](../particles/C_OP_RemapCPtoScalar.md), [C_OP_RemapCPtoVector](../particles/C_OP_RemapCPtoVector.md), [C_OP_RemapControlPointDirectionToVector](../particles/C_OP_RemapControlPointDirectionToVector.md), [C_OP_RemapControlPointOrientationToRotation](../particles/C_OP_RemapControlPointOrientationToRotation.md), [C_OP_RemapCrossProductOfTwoVectorsToVector](../particles/C_OP_RemapCrossProductOfTwoVectorsToVector.md), [C_OP_RemapDensityGradientToVectorAttribute](../particles/C_OP_RemapDensityGradientToVectorAttribute.md), [C_OP_RemapDensityToVector](../particles/C_OP_RemapDensityToVector.md), [C_OP_RemapDirectionToCPToVector](../particles/C_OP_RemapDirectionToCPToVector.md), [C_OP_RemapDistanceToLineSegmentBase](../particles/C_OP_RemapDistanceToLineSegmentBase.md), [C_OP_RemapDotProductToScalar](../particles/C_OP_RemapDotProductToScalar.md), [C_OP_RemapGravityToVector](../particles/C_OP_RemapGravityToVector.md), [C_OP_RemapNamedModelElementEndCap](../particles/C_OP_RemapNamedModelElementEndCap.md), [C_OP_RemapNamedModelElementOnceTimed](../particles/C_OP_RemapNamedModelElementOnceTimed.md), [C_OP_RemapParticleCountOnScalarEndCap](../particles/C_OP_RemapParticleCountOnScalarEndCap.md), [C_OP_RemapParticleCountToScalar](../particles/C_OP_RemapParticleCountToScalar.md), [C_OP_RemapScalar](../particles/C_OP_RemapScalar.md), [C_OP_RemapScalarEndCap](../particles/C_OP_RemapScalarEndCap.md), [C_OP_RemapScalarOnceTimed](../particles/C_OP_RemapScalarOnceTimed.md), [C_OP_RemapSpeed](../particles/C_OP_RemapSpeed.md), [C_OP_RemapTransformOrientationToRotations](../particles/C_OP_RemapTransformOrientationToRotations.md), [C_OP_RemapTransformOrientationToYaw](../particles/C_OP_RemapTransformOrientationToYaw.md), [C_OP_RemapTransformToVelocity](../particles/C_OP_RemapTransformToVelocity.md), [C_OP_RemapTransformVisibilityToScalar](../particles/C_OP_RemapTransformVisibilityToScalar.md), [C_OP_RemapTransformVisibilityToVector](../particles/C_OP_RemapTransformVisibilityToVector.md), [C_OP_RemapVectorComponentToScalar](../particles/C_OP_RemapVectorComponentToScalar.md), [C_OP_RemapVectorToRotations](../particles/C_OP_RemapVectorToRotations.md), [C_OP_RemapVectortoCP](../particles/C_OP_RemapVectortoCP.md), [C_OP_RemapVelocityToVector](../particles/C_OP_RemapVelocityToVector.md), [C_OP_RemapVisibilityScalar](../particles/C_OP_RemapVisibilityScalar.md), [C_OP_RestartAfterDuration](../particles/C_OP_RestartAfterDuration.md), [C_OP_RotateVector](../particles/C_OP_RotateVector.md), [C_OP_RtEnvCull](../particles/C_OP_RtEnvCull.md), [C_OP_ScreenSpaceDistanceToEdge](../particles/C_OP_ScreenSpaceDistanceToEdge.md), [C_OP_ScreenSpacePositionOfTarget](../particles/C_OP_ScreenSpacePositionOfTarget.md), [C_OP_ScreenSpaceRotateTowardTarget](../particles/C_OP_ScreenSpaceRotateTowardTarget.md), [C_OP_SequenceFromModel](../particles/C_OP_SequenceFromModel.md), [C_OP_SetAttributeToScalarExpression](../particles/C_OP_SetAttributeToScalarExpression.md), [C_OP_SetCPOrientationToDirection](../particles/C_OP_SetCPOrientationToDirection.md), [C_OP_SetCPOrientationToGroundNormal](../particles/C_OP_SetCPOrientationToGroundNormal.md), [C_OP_SetCPtoVector](../particles/C_OP_SetCPtoVector.md), [C_OP_SetChildControlPoints](../particles/C_OP_SetChildControlPoints.md), [C_OP_SetControlPointsToModelParticles](../particles/C_OP_SetControlPointsToModelParticles.md), [C_OP_SetControlPointsToParticle](../particles/C_OP_SetControlPointsToParticle.md), [C_OP_SetFloat](../particles/C_OP_SetFloat.md), [C_OP_SetFloatAttributeToVectorExpression](../particles/C_OP_SetFloatAttributeToVectorExpression.md), [C_OP_SetFloatCollection](../particles/C_OP_SetFloatCollection.md), [C_OP_SetFromCPSnapshot](../particles/C_OP_SetFromCPSnapshot.md), [C_OP_SetPerChildControlPoint](../particles/C_OP_SetPerChildControlPoint.md), [C_OP_SetPerChildControlPointFromAttribute](../particles/C_OP_SetPerChildControlPointFromAttribute.md), [C_OP_SetToCP](../particles/C_OP_SetToCP.md), [C_OP_SetUserEvent](../particles/C_OP_SetUserEvent.md), [C_OP_SetVec](../particles/C_OP_SetVec.md), [C_OP_SetVectorAttributeToVectorExpression](../particles/C_OP_SetVectorAttributeToVectorExpression.md), [C_OP_SnapshotRigidSkinToBones](../particles/C_OP_SnapshotRigidSkinToBones.md), [C_OP_SnapshotSkinToBones](../particles/C_OP_SnapshotSkinToBones.md), [C_OP_TeleportBeam](../particles/C_OP_TeleportBeam.md), [C_OP_UpdateLightSource](../particles/C_OP_UpdateLightSource.md), [C_OP_VectorFieldSnapshot](../particles/C_OP_VectorFieldSnapshot.md), [C_OP_VectorNoise](../particles/C_OP_VectorNoise.md), [C_OP_VelocityDecay](../particles/C_OP_VelocityDecay.md), [C_OP_VelocityMatchingForce](../particles/C_OP_VelocityMatchingForce.md)

**Relationships:**

```mermaid
classDiagram
    CParticleFunction <|-- CParticleFunctionOperator
    CParticleFunctionOperator <|-- CGeneralSpin
    CParticleFunctionOperator <|-- CParticleFunctionPreEmission
    CParticleFunctionOperator <|-- CSpinUpdateBase
    CParticleFunctionOperator <|-- C_OP_AlphaDecay
    CParticleFunctionOperator <|-- C_OP_BasicMovement
    CParticleFunctionOperator <|-- C_OP_CPOffsetToPercentageBetweenCPs
    CParticleFunctionOperator <|-- C_OP_CalculateVectorAttribute
    CParticleFunctionOperator <|-- C_OP_ChladniWave
    CParticleFunctionOperator <|-- C_OP_ClampScalar
    CParticleFunctionOperator <|-- C_OP_ClampVector
    CParticleFunctionOperator <|-- C_OP_ColorAdjustHSL
    CParticleFunctionOperator <|-- C_OP_ColorInterpolate
    CParticleFunctionOperator <|-- C_OP_ColorInterpolateRandom
    CParticleFunctionOperator <|-- C_OP_ConnectParentParticleToNearest
    CParticleFunctionOperator <|-- C_OP_ControlpointLight
    CParticleFunctionOperator <|-- C_OP_Cull
    CParticleFunctionOperator <|-- C_OP_CycleScalar
    CParticleFunctionOperator <|-- C_OP_CylindricalDistanceToTransform
    CParticleFunctionOperator <|-- C_OP_DampenToCP
    CParticleFunctionOperator <|-- C_OP_Decay
    CParticleFunctionOperator <|-- C_OP_DecayClampCount
    CParticleFunctionOperator <|-- C_OP_DecayMaintainCount
    CParticleFunctionOperator <|-- C_OP_DecayOffscreen
    CParticleFunctionOperator <|-- C_OP_DifferencePreviousParticle
    CParticleFunctionOperator <|-- C_OP_Diffusion
    CParticleFunctionOperator <|-- C_OP_DirectionBetweenVecsToVec
    CParticleFunctionOperator <|-- C_OP_DistanceBetweenTransforms
    CParticleFunctionOperator <|-- C_OP_DistanceBetweenVecs
    CParticleFunctionOperator <|-- C_OP_DistanceCull
    CParticleFunctionOperator <|-- C_OP_DistanceToTransform
    CParticleFunctionOperator <|-- C_OP_DragRelativeToPlane
    CParticleFunctionOperator <|-- C_OP_EndCapDecay
    CParticleFunctionOperator <|-- C_OP_EndCapTimedDecay
    CParticleFunctionOperator <|-- C_OP_EndCapTimedFreeze
    CParticleFunctionOperator <|-- C_OP_FadeAndKill
    CParticleFunctionOperator <|-- C_OP_FadeAndKillForTracers
    CParticleFunctionOperator <|-- C_OP_FadeIn
    CParticleFunctionOperator <|-- C_OP_FadeInSimple
    CParticleFunctionOperator <|-- C_OP_FadeOut
    CParticleFunctionOperator <|-- C_OP_FadeOutSimple
    CParticleFunctionOperator <|-- C_OP_GlobalLight
    CParticleFunctionOperator <|-- C_OP_InheritFromParentParticles
    CParticleFunctionOperator <|-- C_OP_InheritFromParentParticlesV2
    CParticleFunctionOperator <|-- C_OP_InheritFromPeerSystem
    CParticleFunctionOperator <|-- C_OP_InterpolateRadius
    CParticleFunctionOperator <|-- C_OP_LagCompensation
    CParticleFunctionOperator <|-- C_OP_LazyCullCompareFloat
    CParticleFunctionOperator <|-- C_OP_LerpEndCapScalar
    CParticleFunctionOperator <|-- C_OP_LerpEndCapVector
    CParticleFunctionOperator <|-- C_OP_LerpScalar
    CParticleFunctionOperator <|-- C_OP_LerpToInitialPosition
    CParticleFunctionOperator <|-- C_OP_LerpToOtherAttribute
    CParticleFunctionOperator <|-- C_OP_LerpVector
    CParticleFunctionOperator <|-- C_OP_LockPoints
    CParticleFunctionOperator <|-- C_OP_LockToBone
    CParticleFunctionOperator <|-- C_OP_LockToPointList
    CParticleFunctionOperator <|-- C_OP_LockToSavedSequentialPath
    CParticleFunctionOperator <|-- C_OP_LockToSavedSequentialPathV2
    CParticleFunctionOperator <|-- C_OP_MaintainSequentialPath
    CParticleFunctionOperator <|-- C_OP_MaxVelocity
    CParticleFunctionOperator <|-- C_OP_ModelCull
    CParticleFunctionOperator <|-- C_OP_ModelDampenMovement
    CParticleFunctionOperator <|-- C_OP_MoveToHitbox
    CParticleFunctionOperator <|-- C_OP_MovementLoopInsideSphere
    CParticleFunctionOperator <|-- C_OP_MovementMaintainOffset
    CParticleFunctionOperator <|-- C_OP_MovementMoveAlongSkinnedCPSnapshot
    CParticleFunctionOperator <|-- C_OP_MovementPlaceOnGround
    CParticleFunctionOperator <|-- C_OP_MovementRigidAttachToCP
    CParticleFunctionOperator <|-- C_OP_MovementRotateParticleAroundAxis
    CParticleFunctionOperator <|-- C_OP_MovementSkinnedPositionFromCPSnapshot
    CParticleFunctionOperator <|-- C_OP_Noise
    CParticleFunctionOperator <|-- C_OP_NormalLock
    CParticleFunctionOperator <|-- C_OP_NormalizeVector
    CParticleFunctionOperator <|-- C_OP_Orient2DRelToCP
    CParticleFunctionOperator <|-- C_OP_OrientTo2dDirection
    CParticleFunctionOperator <|-- C_OP_OscillateScalar
    CParticleFunctionOperator <|-- C_OP_OscillateScalarSimple
    CParticleFunctionOperator <|-- C_OP_OscillateVector
    CParticleFunctionOperator <|-- C_OP_OscillateVectorSimple
    CParticleFunctionOperator <|-- C_OP_PercentageBetweenTransformLerpCPs
    CParticleFunctionOperator <|-- C_OP_PercentageBetweenTransforms
    CParticleFunctionOperator <|-- C_OP_PercentageBetweenTransformsVector
    CParticleFunctionOperator <|-- C_OP_PinParticleToCP
    CParticleFunctionOperator <|-- C_OP_PinRopeSegmentParticleToParent
    CParticleFunctionOperator <|-- C_OP_PlaneCull
    CParticleFunctionOperator <|-- C_OP_PointVectorAtNextParticle
    CParticleFunctionOperator <|-- C_OP_PositionLock
    CParticleFunctionOperator <|-- C_OP_QuantizeFloat
    CParticleFunctionOperator <|-- C_OP_RadiusDecay
    CParticleFunctionOperator <|-- C_OP_RampScalarLinear
    CParticleFunctionOperator <|-- C_OP_RampScalarLinearSimple
    CParticleFunctionOperator <|-- C_OP_RampScalarSpline
    CParticleFunctionOperator <|-- C_OP_RampScalarSplineSimple
    CParticleFunctionOperator <|-- C_OP_ReadFromNeighboringParticle
    CParticleFunctionOperator <|-- C_OP_ReinitializeScalarEndCap
    CParticleFunctionOperator <|-- C_OP_RemapCPVelocityToVector
    CParticleFunctionOperator <|-- C_OP_RemapCPtoScalar
    CParticleFunctionOperator <|-- C_OP_RemapCPtoVector
    CParticleFunctionOperator <|-- C_OP_RemapControlPointDirectionToVector
    CParticleFunctionOperator <|-- C_OP_RemapControlPointOrientationToRotation
    CParticleFunctionOperator <|-- C_OP_RemapCrossProductOfTwoVectorsToVector
    CParticleFunctionOperator <|-- C_OP_RemapDensityGradientToVectorAttribute
    CParticleFunctionOperator <|-- C_OP_RemapDensityToVector
    CParticleFunctionOperator <|-- C_OP_RemapDirectionToCPToVector
    CParticleFunctionOperator <|-- C_OP_RemapDistanceToLineSegmentBase
    CParticleFunctionOperator <|-- C_OP_RemapDotProductToScalar
    CParticleFunctionOperator <|-- C_OP_RemapGravityToVector
    CParticleFunctionOperator <|-- C_OP_RemapNamedModelElementEndCap
    CParticleFunctionOperator <|-- C_OP_RemapNamedModelElementOnceTimed
    CParticleFunctionOperator <|-- C_OP_RemapParticleCountOnScalarEndCap
    CParticleFunctionOperator <|-- C_OP_RemapParticleCountToScalar
    CParticleFunctionOperator <|-- C_OP_RemapScalar
    CParticleFunctionOperator <|-- C_OP_RemapScalarEndCap
    CParticleFunctionOperator <|-- C_OP_RemapScalarOnceTimed
    CParticleFunctionOperator <|-- C_OP_RemapSpeed
    CParticleFunctionOperator <|-- C_OP_RemapTransformOrientationToRotations
    CParticleFunctionOperator <|-- C_OP_RemapTransformOrientationToYaw
    CParticleFunctionOperator <|-- C_OP_RemapTransformToVelocity
    CParticleFunctionOperator <|-- C_OP_RemapTransformVisibilityToScalar
    CParticleFunctionOperator <|-- C_OP_RemapTransformVisibilityToVector
    CParticleFunctionOperator <|-- C_OP_RemapVectorComponentToScalar
    CParticleFunctionOperator <|-- C_OP_RemapVectorToRotations
    CParticleFunctionOperator <|-- C_OP_RemapVectortoCP
    CParticleFunctionOperator <|-- C_OP_RemapVelocityToVector
    CParticleFunctionOperator <|-- C_OP_RemapVisibilityScalar
    CParticleFunctionOperator <|-- C_OP_RestartAfterDuration
    CParticleFunctionOperator <|-- C_OP_RotateVector
    CParticleFunctionOperator <|-- C_OP_RtEnvCull
    CParticleFunctionOperator <|-- C_OP_ScreenSpaceDistanceToEdge
    CParticleFunctionOperator <|-- C_OP_ScreenSpacePositionOfTarget
    CParticleFunctionOperator <|-- C_OP_ScreenSpaceRotateTowardTarget
    CParticleFunctionOperator <|-- C_OP_SequenceFromModel
    CParticleFunctionOperator <|-- C_OP_SetAttributeToScalarExpression
    CParticleFunctionOperator <|-- C_OP_SetCPOrientationToDirection
    CParticleFunctionOperator <|-- C_OP_SetCPOrientationToGroundNormal
    CParticleFunctionOperator <|-- C_OP_SetCPtoVector
    CParticleFunctionOperator <|-- C_OP_SetChildControlPoints
    CParticleFunctionOperator <|-- C_OP_SetControlPointsToModelParticles
    CParticleFunctionOperator <|-- C_OP_SetControlPointsToParticle
    CParticleFunctionOperator <|-- C_OP_SetFloat
    CParticleFunctionOperator <|-- C_OP_SetFloatAttributeToVectorExpression
    CParticleFunctionOperator <|-- C_OP_SetFloatCollection
    CParticleFunctionOperator <|-- C_OP_SetFromCPSnapshot
    CParticleFunctionOperator <|-- C_OP_SetPerChildControlPoint
    CParticleFunctionOperator <|-- C_OP_SetPerChildControlPointFromAttribute
    CParticleFunctionOperator <|-- C_OP_SetToCP
    CParticleFunctionOperator <|-- C_OP_SetUserEvent
    CParticleFunctionOperator <|-- C_OP_SetVec
    CParticleFunctionOperator <|-- C_OP_SetVectorAttributeToVectorExpression
    CParticleFunctionOperator <|-- C_OP_SnapshotRigidSkinToBones
    CParticleFunctionOperator <|-- C_OP_SnapshotSkinToBones
    CParticleFunctionOperator <|-- C_OP_TeleportBeam
    CParticleFunctionOperator <|-- C_OP_UpdateLightSource
    CParticleFunctionOperator <|-- C_OP_VectorFieldSnapshot
    CParticleFunctionOperator <|-- C_OP_VectorNoise
    CParticleFunctionOperator <|-- C_OP_VelocityDecay
    CParticleFunctionOperator <|-- C_OP_VelocityMatchingForce
```

## Memory layout

17 fields (0 declared here, 17 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_flOpStrength` | [CParticleCollectionFloatInput](../particleslib/CParticleCollectionFloatInput.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator strength` `MPropertySortPriority -100` |
| `0x178` | `m_nOpEndCapState` | [ParticleEndcapMode_t](../!GlobalTypes/ParticleEndcapMode_t.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator end cap state` `MPropertySortPriority -100` |
| `0x17c` | `m_nToolsState` | [ParticleToolsState_t](../!GlobalTypes/ParticleToolsState_t.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator enabled in tools or game only` `MPropertySortPriority -100` |
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
