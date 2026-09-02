---
title: C_OP_RemapNamedModelElementOnceTimed
module: particles
kind: class
---

[Schemas](../../schemas.md) / [particles](../particles.md) / C_OP_RemapNamedModelElementOnceTimed

# C_OP_RemapNamedModelElementOnceTimed

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 568 bytes (`0x238`) · **Align:** n/a (unspecified) · **Module:** particles

**Inherits from:** [CParticleFunctionOperator](../particles/CParticleFunctionOperator.md)

**Derived by:** [C_OP_RemapNamedModelBodyPartOnceTimed](../particles/C_OP_RemapNamedModelBodyPartOnceTimed.md), [C_OP_RemapNamedModelMeshGroupOnceTimed](../particles/C_OP_RemapNamedModelMeshGroupOnceTimed.md), [C_OP_RemapNamedModelSequenceOnceTimed](../particles/C_OP_RemapNamedModelSequenceOnceTimed.md)

**Relationships:**

```mermaid
classDiagram
    CParticleFunctionOperator <|-- C_OP_RemapNamedModelElementOnceTimed
    CParticleFunction <|-- CParticleFunctionOperator
    C_OP_RemapNamedModelElementOnceTimed <|-- C_OP_RemapNamedModelBodyPartOnceTimed
    C_OP_RemapNamedModelElementOnceTimed <|-- C_OP_RemapNamedModelMeshGroupOnceTimed
    C_OP_RemapNamedModelElementOnceTimed <|-- C_OP_RemapNamedModelSequenceOnceTimed
    C_OP_RemapNamedModelElementOnceTimed *-- InfoForResourceTypeCModel
    C_OP_RemapNamedModelElementOnceTimed *-- ParticleAttributeIndex_t
```

## Memory layout

26 fields (9 declared here, 17 inherited). Offsets are absolute from the object base.

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
| `0x1d8` | `m_hModel` | CStrongHandle< [InfoForResourceTypeCModel](../resourcesystem/InfoForResourceTypeCModel.md) > |  |  |
| `0x1e0` | `m_inNames` | CUtlVector< CUtlString > |  | `MPropertyFriendlyName input names` |
| `0x1f8` | `m_outNames` | CUtlVector< CUtlString > |  | `MPropertyFriendlyName output names` |
| `0x210` | `m_fallbackNames` | CUtlVector< CUtlString > |  | `MPropertyFriendlyName fallback names when the input doesn't match` |
| `0x228` | `m_bModelFromRenderer` | bool |  | `MPropertyFriendlyName model from renderer` |
| `0x229` | `m_bProportional` | bool |  | `MPropertyFriendlyName remap time proportional` |
| `0x22c` | `m_nFieldInput` | [ParticleAttributeIndex_t](../particles/ParticleAttributeIndex_t.md) |  | `MPropertyAttributeChoiceName particlefield_scalar` `MPropertyFriendlyName input field` |
| `0x230` | `m_nFieldOutput` | [ParticleAttributeIndex_t](../particles/ParticleAttributeIndex_t.md) |  | `MPropertyAttributeChoiceName particlefield_scalar` `MPropertyFriendlyName output field` |
| `0x234` | `m_flRemapTime` | float32 |  | `MPropertyFriendlyName remap time` |
