---
layout: default
title: "UML: particleslib"
parent: Schemas
nav_exclude: true
---

# UML: particleslib

Class relationships (inheritance and composition) for the `particleslib` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    IParticleEffect <|-- CNewParticleEffect
    CParticleFloatInput <|-- CParticleCollectionFloatInput
    CParticleCollectionFloatInput <|-- CParticleCollectionRendererFloatInput
    CParticleCollectionVecInput <|-- CParticleCollectionRendererVecInput
    CParticleVecInput <|-- CParticleCollectionVecInput
    CParticleInput <|-- CParticleFloatInput
    CParticleInput <|-- CParticleModelInput
    CParticleFloatInput <|-- CParticleRemapFloatInput
    CParticleInput <|-- CParticleTransformInput
    CParticleInput <|-- CParticleVecInput
    CParticleFloatInput <|-- CPerParticleFloatInput
    CParticleVecInput <|-- CPerParticleVecInput
    CParticleCollectionBindingInstance <|-- CParticleBindingRealPulse
    CBasePulseGraphInstance <|-- CParticleCollectionBindingInstance
    CNewParticleEffect --> PARTICLE_EHANDLE__
    CNewParticleEffect --> CParticleProperty
    CParticleFloatInput *-- ParticleFloatType_t
    CParticleFloatInput *-- ParticleFloatMapType_t
    CParticleFloatInput *-- ParticleFloatRandomMode_t
    CParticleFloatInput *-- PFNoiseTurbulence_t
    CParticleFloatInput *-- PFNoiseType_t
    CParticleFloatInput *-- PFNoiseModifier_t
    CParticleFloatInput *-- ParticleFloatInputMode_t
    CParticleFloatInput *-- ParticleFloatRoundType_t
    CParticleFloatInput *-- ParticleFloatBiasType_t
    CParticleModelInput *-- ParticleModelType_t
    CParticleTransformInput *-- ParticleTransformType_t
    CParticleVecInput *-- ParticleVecType_t
    CParticleVecInput *-- CParticleFloatInput
    ParticleNamedValueSource_t *-- ParticleNamedValueConfiguration_t
```
