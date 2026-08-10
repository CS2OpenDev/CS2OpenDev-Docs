---
layout: default
title: CParticleFunctionRenderer
nav_exclude: true
---

[Schemas](../../schemas.md) / [particles](../particles.md) / CParticleFunctionRenderer

# CParticleFunctionRenderer

**Kind:** class · **Size:** 552 bytes (`0x228`) · **Align:** 255 · **Module:** particles

**Inherits from:** [CParticleFunction](../particles/CParticleFunction.md)

**Derived by:** [CBaseRendererSource2](../particles/CBaseRendererSource2.md), [C_OP_Callback](../particles/C_OP_Callback.md), [C_OP_ClientPhysics](../particles/C_OP_ClientPhysics.md), [C_OP_CreateParticleSystemRenderer](../particles/C_OP_CreateParticleSystemRenderer.md), [C_OP_GameDecalRenderer](../particles/C_OP_GameDecalRenderer.md), [C_OP_GameLiquidSpill](../particles/C_OP_GameLiquidSpill.md), [C_OP_RenderAsModels](../particles/C_OP_RenderAsModels.md), [C_OP_RenderBlobs](../particles/C_OP_RenderBlobs.md), [C_OP_RenderCables](../particles/C_OP_RenderCables.md), [C_OP_RenderClientPhysicsImpulse](../particles/C_OP_RenderClientPhysicsImpulse.md), [C_OP_RenderClothForce](../particles/C_OP_RenderClothForce.md), [C_OP_RenderDeferredLight](../particles/C_OP_RenderDeferredLight.md), [C_OP_RenderFlattenGrass](../particles/C_OP_RenderFlattenGrass.md), [C_OP_RenderGpuImplicit](../particles/C_OP_RenderGpuImplicit.md), [C_OP_RenderLightBeam](../particles/C_OP_RenderLightBeam.md), [C_OP_RenderMaterialProxy](../particles/C_OP_RenderMaterialProxy.md), [C_OP_RenderModels](../particles/C_OP_RenderModels.md), [C_OP_RenderOmni2Light](../particles/C_OP_RenderOmni2Light.md), [C_OP_RenderPoints](../particles/C_OP_RenderPoints.md), [C_OP_RenderPostProcessing](../particles/C_OP_RenderPostProcessing.md), [C_OP_RenderProjected](../particles/C_OP_RenderProjected.md), [C_OP_RenderScreenShake](../particles/C_OP_RenderScreenShake.md), [C_OP_RenderScreenVelocityRotate](../particles/C_OP_RenderScreenVelocityRotate.md), [C_OP_RenderSimpleModelCollection](../particles/C_OP_RenderSimpleModelCollection.md), [C_OP_RenderSound](../particles/C_OP_RenderSound.md), [C_OP_RenderStandardLight](../particles/C_OP_RenderStandardLight.md), [C_OP_RenderStatusEffect](../particles/C_OP_RenderStatusEffect.md), [C_OP_RenderStatusEffectCitadel](../particles/C_OP_RenderStatusEffectCitadel.md), [C_OP_RenderText](../particles/C_OP_RenderText.md), [C_OP_RenderTreeShake](../particles/C_OP_RenderTreeShake.md), [C_OP_RenderVRHapticEvent](../particles/C_OP_RenderVRHapticEvent.md), [C_OP_RenderVolumetricEmitter](../particles/C_OP_RenderVolumetricEmitter.md), [C_OP_WaterImpulseRenderer](../particles/C_OP_WaterImpulseRenderer.md)

**Relationships:**

```mermaid
classDiagram
    CParticleFunction <|-- CParticleFunctionRenderer
    CParticleFunctionRenderer <|-- CBaseRendererSource2
    CParticleFunctionRenderer <|-- C_OP_Callback
    CParticleFunctionRenderer <|-- C_OP_ClientPhysics
    CParticleFunctionRenderer <|-- C_OP_CreateParticleSystemRenderer
    CParticleFunctionRenderer <|-- C_OP_GameDecalRenderer
    CParticleFunctionRenderer <|-- C_OP_GameLiquidSpill
    CParticleFunctionRenderer <|-- C_OP_RenderAsModels
    CParticleFunctionRenderer <|-- C_OP_RenderBlobs
    CParticleFunctionRenderer <|-- C_OP_RenderCables
    CParticleFunctionRenderer <|-- C_OP_RenderClientPhysicsImpulse
    CParticleFunctionRenderer <|-- C_OP_RenderClothForce
    CParticleFunctionRenderer <|-- C_OP_RenderDeferredLight
    CParticleFunctionRenderer <|-- C_OP_RenderFlattenGrass
    CParticleFunctionRenderer <|-- C_OP_RenderGpuImplicit
    CParticleFunctionRenderer <|-- C_OP_RenderLightBeam
    CParticleFunctionRenderer <|-- C_OP_RenderMaterialProxy
    CParticleFunctionRenderer <|-- C_OP_RenderModels
    CParticleFunctionRenderer <|-- C_OP_RenderOmni2Light
    CParticleFunctionRenderer <|-- C_OP_RenderPoints
    CParticleFunctionRenderer <|-- C_OP_RenderPostProcessing
    CParticleFunctionRenderer <|-- C_OP_RenderProjected
    CParticleFunctionRenderer <|-- C_OP_RenderScreenShake
    CParticleFunctionRenderer <|-- C_OP_RenderScreenVelocityRotate
    CParticleFunctionRenderer <|-- C_OP_RenderSimpleModelCollection
    CParticleFunctionRenderer <|-- C_OP_RenderSound
    CParticleFunctionRenderer <|-- C_OP_RenderStandardLight
    CParticleFunctionRenderer <|-- C_OP_RenderStatusEffect
    CParticleFunctionRenderer <|-- C_OP_RenderStatusEffectCitadel
    CParticleFunctionRenderer <|-- C_OP_RenderText
    CParticleFunctionRenderer <|-- C_OP_RenderTreeShake
    CParticleFunctionRenderer <|-- C_OP_RenderVRHapticEvent
    CParticleFunctionRenderer <|-- C_OP_RenderVolumetricEmitter
    CParticleFunctionRenderer <|-- C_OP_WaterImpulseRenderer
    CParticleFunctionRenderer *-- CParticleVisibilityInputs
```

## Memory layout

20 fields (3 declared here, 17 inherited). Offsets are absolute from the object base.

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
| `0x1d8` | `VisibilityInputs` | [CParticleVisibilityInputs](../particles/CParticleVisibilityInputs.md) |  | `MPropertySortPriority -1` |
| `0x220` | `m_bCannotBeRefracted` | bool |  | `MPropertyFriendlyName I cannot be refracted through refracting objects like water` `MPropertySortPriority -1` `MPropertyStartGroup Rendering filter` |
| `0x221` | `m_bSkipRenderingOnMobile` | bool |  | `MPropertyFriendlyName Skip rendering on mobile` `MPropertySortPriority -1` |
