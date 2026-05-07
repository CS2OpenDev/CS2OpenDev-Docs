---
layout: default
title: "UML: materialsystem2"
parent: Schemas
nav_exclude: true
---

# UML: materialsystem2

Class relationships (inheritance and composition) for the `materialsystem2` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    MaterialParam_t <|-- MaterialParamTexture_t
    MaterialParam_t <|-- MaterialParamFloat_t
    MaterialParam_t <|-- MaterialParamBuffer_t
    MaterialParam_t <|-- MaterialParamInt_t
    MaterialParam_t <|-- MaterialParamString_t
    MaterialParam_t <|-- MaterialParamVector_t
    PostProcessingBloomParameters_t *-- BloomBlendMode_t
    MaterialResourceData_t *-- MaterialParamInt_t
    MaterialResourceData_t *-- MaterialParamFloat_t
    MaterialResourceData_t *-- MaterialParamVector_t
    MaterialResourceData_t *-- MaterialParamTexture_t
    MaterialResourceData_t *-- MaterialParamBuffer_t
    MaterialResourceData_t *-- MaterialParamString_t
    PostProcessingResource_t *-- PostProcessingTonemapParameters_t
    PostProcessingResource_t *-- PostProcessingBloomParameters_t
    PostProcessingResource_t *-- PostProcessingVignetteParameters_t
    PostProcessingResource_t *-- PostProcessingLocalContrastParameters_t
    PostProcessingResource_t *-- PostProcessingFogScatteringParameters_t
```
