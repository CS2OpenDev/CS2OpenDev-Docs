---
layout: default
title: "UML: navlib"
parent: Schemas
nav_exclude: true
---

# UML: navlib

Class relationships (inheritance and composition) for the `navlib` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CNavFlags <|-- CNavAttribute
    INavPathCost <|-- CNavPathCost
    CNavVolumeVector <|-- CNavVolumeAll
    CNavVolume <|-- CNavVolumeSphere
    CNavVolumeSphere <|-- CNavVolumeSphericalShell
    CNavVolume <|-- CNavVolumeVector
    INavPathCost *-- NavHull_t
```
