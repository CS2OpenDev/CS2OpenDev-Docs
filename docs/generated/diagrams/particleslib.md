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
    CParticleCollectionBindingInstance <|-- CParticleBindingRealPulse
    CBasePulseGraphInstance <|-- CParticleCollectionBindingInstance
```
