---
layout: default
title: "UML: resourcecompiler"
parent: Schemas
nav_exclude: true
---

# UML: resourcecompiler

Class relationships (inheritance and composition) for the `resourcecompiler` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CBloomLayer
    CColorCorrectionLayer <|-- CFogScatteringLayer
    CColorCorrectionLayer <|-- CColorBalanceColorCorrectionLayer
    CColorCorrectionLayer <|-- CVignetteLayer
    CColorCorrectionLayer <|-- CHueSaturationColorCorrectionLayer
    CColorCorrectionLayer <|-- CColorTintColorCorrectionLayer
    CColorCorrectionLayer <|-- CLevelsColorCorrectionLayer
    CColorCorrectionLayer <|-- CToneMappingLayer
    CColorCorrectionLayer <|-- CColorLookupColorCorrectionLayer
    CColorCorrectionLayer <|-- CCurvesColorCorrectionLayer
    CColorCorrectionLayer <|-- CBrightnessContrastColorCorrectionLayer
    CColorCorrectionLayer <|-- CLocalContrastLayer
    CColorCorrectionLayer <|-- CVibranceColorCorrectionLayer
    CPostProcessData --> CColorCorrectionLayer
    CColorCorrectionLayer --> CLayerMask
```
