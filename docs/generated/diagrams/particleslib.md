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
    CBasePulseGraphInstance <|-- CParticleCollectionBindingInstance
    CParticleCollectionBindingInstance <|-- CParticleBindingRealPulse
    CParticleCollectionVecInput <|-- CParticleCollectionRendererVecInput
    CParticleInput <|-- CParticleFloatInput
    CParticleFloatInput <|-- CParticleCollectionFloatInput
    CParticleCollectionFloatInput <|-- CParticleCollectionRendererFloatInput
    CParticleFloatInput <|-- CPerParticleFloatInput
    CParticleInput <|-- CParticleTransformInput
    CParticleFloatInput <|-- CParticleRemapFloatInput
    CParticleVecInput <|-- CParticleCollectionVecInput
    IParticleEffect <|-- CNewParticleEffect
    CParticleInput <|-- CParticleVecInput
    CParticleVecInput <|-- CPerParticleVecInput
    CParticleInput <|-- CParticleModelInput
    CParticleFloatInput *-- ParticleFloatType_t
    CParticleFloatInput *-- ParticleFloatMapType_t
    CParticleFloatInput *-- ParticleFloatRandomMode_t
    CParticleFloatInput *-- PFNoiseTurbulence_t
    CParticleFloatInput *-- PFNoiseType_t
    CParticleFloatInput *-- PFNoiseModifier_t
    CParticleFloatInput *-- ParticleFloatInputMode_t
    CParticleFloatInput *-- ParticleFloatRoundType_t
    CParticleFloatInput *-- ParticleFloatBiasType_t
    CParticleTransformInput *-- ParticleTransformType_t
    ParticleNamedValueSource_t *-- ParticleNamedValueConfiguration_t
    CNewParticleEffect --> PARTICLE_EHANDLE__
    CNewParticleEffect --> CParticleProperty
    CParticleVecInput *-- ParticleVecType_t
    CParticleVecInput *-- CParticleFloatInput
    CParticleModelInput *-- ParticleModelType_t
```
