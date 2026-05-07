---
layout: default
title: "UML: toolscene"
parent: Schemas
nav_exclude: true
---

# UML: toolscene

Class relationships (inheritance and composition) for the `toolscene` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CLightRigLight <|-- CLightRigPointLight
    CLightRigLight <|-- CLightRigSunLight
    CLightRigLight <|-- CLightRigSpotLight
    CToolSceneLightRig *-- LightRigType_t
    CToolSceneLightRig *-- CLightRigSunLight
    CToolSceneLightRig *-- CLightRigPointLight
    CToolSceneLightRig *-- CLightRigSpotLight
    CToolSceneLightRig *-- CLightRigBackground
    CToolSceneLightRig *-- CLightRigGrid
    CToolSceneLightRig *-- CLightRigExposure
    CToolSceneLightRig *-- CLightRigPostProcessing
    CToolSceneLightRig *-- CLightRigSky
    CToolSceneLightRig *-- CLightRigVMap
```
