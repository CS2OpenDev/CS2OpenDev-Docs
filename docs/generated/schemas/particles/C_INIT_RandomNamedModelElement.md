---
title: C_INIT_RandomNamedModelElement
module: particles
kind: class
---

[Schemas](../../schemas.md) / [particles](../particles.md) / C_INIT_RandomNamedModelElement

# C_INIT_RandomNamedModelElement

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 528 bytes (`0x210`) · **Align:** n/a (unspecified) · **Module:** particles

**Inherits from:** [CParticleFunctionInitializer](../particles/CParticleFunctionInitializer.md)

**Derived by:** [C_INIT_RandomNamedModelBodyPart](../particles/C_INIT_RandomNamedModelBodyPart.md), [C_INIT_RandomNamedModelMeshGroup](../particles/C_INIT_RandomNamedModelMeshGroup.md), [C_INIT_RandomNamedModelSequence](../particles/C_INIT_RandomNamedModelSequence.md)

**Relationships:**

```mermaid
classDiagram
    CParticleFunctionInitializer <|-- C_INIT_RandomNamedModelElement
    CParticleFunction <|-- CParticleFunctionInitializer
    C_INIT_RandomNamedModelElement <|-- C_INIT_RandomNamedModelBodyPart
    C_INIT_RandomNamedModelElement <|-- C_INIT_RandomNamedModelMeshGroup
    C_INIT_RandomNamedModelElement <|-- C_INIT_RandomNamedModelSequence
    C_INIT_RandomNamedModelElement *-- InfoForResourceTypeCModel
    C_INIT_RandomNamedModelElement *-- ParticleAttributeIndex_t
```

## Memory layout

24 fields (6 declared here, 18 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_flOpStrength` | [CParticleCollectionFloatInput](../particleslib/CParticleCollectionFloatInput.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator strength` `MPropertySortPriority -100` |
| `0x180` | `m_nOpEndCapState` | [ParticleEndcapMode_t](../particles/ParticleEndcapMode_t.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator end cap state` `MPropertySortPriority -100` |
| `0x184` | `m_nToolsState` | [ParticleToolsState_t](../particles/ParticleToolsState_t.md) | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyFriendlyName operator enabled in tools or game only` `MPropertySortPriority -100` |
| `0x188` | `m_flOpStartFadeInTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator start fadein` `MPropertySortPriority -100` `MPropertyStartGroup Operator Fade` |
| `0x18c` | `m_flOpEndFadeInTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator end fadein` `MPropertySortPriority -100` |
| `0x190` | `m_flOpStartFadeOutTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator start fadeout` `MPropertySortPriority -100` |
| `0x194` | `m_flOpEndFadeOutTime` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator end fadeout` `MPropertySortPriority -100` |
| `0x198` | `m_flOpFadeOscillatePeriod` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade oscillate` `MPropertySortPriority -100` |
| `0x19c` | `m_bNormalizeToStopTime` | bool | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName normalize fade times to endcap` `MPropertySortPriority -100` |
| `0x1a0` | `m_flOpTimeOffsetMin` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time offset min` `MPropertySortPriority -100` `MPropertyStartGroup Operator Fade Time Offset` |
| `0x1a4` | `m_flOpTimeOffsetMax` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time offset max` `MPropertySortPriority -100` |
| `0x1a8` | `m_nOpTimeOffsetSeed` | int32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time offset seed` `MPropertySortPriority -100` |
| `0x1ac` | `m_nOpTimeScaleSeed` | int32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time scale seed` `MPropertySortPriority -100` `MPropertyStartGroup Operator Fade Timescale Modifiers` |
| `0x1b0` | `m_flOpTimeScaleMin` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time scale min` `MPropertySortPriority -100` |
| `0x1b4` | `m_flOpTimeScaleMax` | float32 | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleAdvancedField` `MPropertyFriendlyName operator fade time scale max` `MPropertySortPriority -100` |
| `0x1ba` | `m_bDisableOperator` | bool | [CParticleFunction](../particles/CParticleFunction.md) | `MPropertyStartGroup` `MPropertySuppressField` |
| `0x1c0` | `m_Notes` | CUtlString | [CParticleFunction](../particles/CParticleFunction.md) | `MParticleHelpField` `MPropertyAttributeEditor TextBlock()` `MPropertyFriendlyName operator help and notes` `MPropertySortPriority -100` |
| `0x1e0` | `m_nAssociatedEmitterIndex` | int32 | [CParticleFunctionInitializer](../particles/CParticleFunctionInitializer.md) | `MPropertyFriendlyName Associated emitter Index` |
| `0x1e8` | `m_hModel` | CStrongHandle< [InfoForResourceTypeCModel](../resourcesystem/InfoForResourceTypeCModel.md) > |  |  |
| `0x1f0` | `m_names` | CUtlVector< CUtlString > |  | `MPropertyFriendlyName names` |
| `0x208` | `m_bShuffle` | bool |  | `MPropertyFriendlyName shuffle` |
| `0x209` | `m_bLinear` | bool |  | `MPropertyFriendlyName linear` |
| `0x20a` | `m_bModelFromRenderer` | bool |  | `MPropertyFriendlyName model from renderer` |
| `0x20c` | `m_nFieldOutput` | [ParticleAttributeIndex_t](../particleslib/ParticleAttributeIndex_t.md) |  | `MPropertyAttributeChoiceName particlefield_scalar` `MPropertyFriendlyName output field` |
