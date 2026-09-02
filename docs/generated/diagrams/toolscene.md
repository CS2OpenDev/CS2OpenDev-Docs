---
title: "UML: toolscene"
---

# UML: toolscene

Class relationships (inheritance and composition) for the `toolscene` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CLightRigLight <|-- CLightRigPointLight
    CLightRigLight <|-- CLightRigSpotLight
    CLightRigLight <|-- CLightRigSunLight
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
