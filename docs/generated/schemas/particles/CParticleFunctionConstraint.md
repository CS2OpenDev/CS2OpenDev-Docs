---
layout: default
title: CParticleFunctionConstraint
nav_exclude: true
---

[Schemas](../../schemas.md) / [particles](../particles.md) / CParticleFunctionConstraint

# CParticleFunctionConstraint

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 472 bytes (`0x1d8`) · **Align:** n/a (unspecified) · **Module:** particles

**Inherits from:** [CParticleFunction](../particles/CParticleFunction.md)

**Derived by:** [C_OP_BoxConstraint](../particles/C_OP_BoxConstraint.md), [C_OP_CollideWithParentParticles](../particles/C_OP_CollideWithParentParticles.md), [C_OP_CollideWithSelf](../particles/C_OP_CollideWithSelf.md), [C_OP_ConstrainDistance](../particles/C_OP_ConstrainDistance.md), [C_OP_ConstrainDistanceToPath](../particles/C_OP_ConstrainDistanceToPath.md), [C_OP_ConstrainDistanceToUserSpecifiedPath](../particles/C_OP_ConstrainDistanceToUserSpecifiedPath.md), [C_OP_ConstrainLineLength](../particles/C_OP_ConstrainLineLength.md), [C_OP_PlanarConstraint](../particles/C_OP_PlanarConstraint.md), [C_OP_RopeSpringConstraint](../particles/C_OP_RopeSpringConstraint.md), [C_OP_ShapeMatchingConstraint](../particles/C_OP_ShapeMatchingConstraint.md), [C_OP_SpringToVectorConstraint](../particles/C_OP_SpringToVectorConstraint.md), [C_OP_WorldCollideConstraint](../particles/C_OP_WorldCollideConstraint.md), [C_OP_WorldTraceConstraint](../particles/C_OP_WorldTraceConstraint.md)

**Relationships:**

```mermaid
classDiagram
    CParticleFunction <|-- CParticleFunctionConstraint
    CParticleFunctionConstraint <|-- C_OP_BoxConstraint
    CParticleFunctionConstraint <|-- C_OP_CollideWithParentParticles
    CParticleFunctionConstraint <|-- C_OP_CollideWithSelf
    CParticleFunctionConstraint <|-- C_OP_ConstrainDistance
    CParticleFunctionConstraint <|-- C_OP_ConstrainDistanceToPath
    CParticleFunctionConstraint <|-- C_OP_ConstrainDistanceToUserSpecifiedPath
    CParticleFunctionConstraint <|-- C_OP_ConstrainLineLength
    CParticleFunctionConstraint <|-- C_OP_PlanarConstraint
    CParticleFunctionConstraint <|-- C_OP_RopeSpringConstraint
    CParticleFunctionConstraint <|-- C_OP_ShapeMatchingConstraint
    CParticleFunctionConstraint <|-- C_OP_SpringToVectorConstraint
    CParticleFunctionConstraint <|-- C_OP_WorldCollideConstraint
    CParticleFunctionConstraint <|-- C_OP_WorldTraceConstraint
```

## Memory layout

17 fields (0 declared here, 17 inherited). Offsets are absolute from the object base.

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
