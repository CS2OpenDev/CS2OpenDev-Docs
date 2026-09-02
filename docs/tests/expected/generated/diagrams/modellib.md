---
layout: default
title: "UML: modellib"
parent: Schemas
nav_exclude: true
---

# UML: modellib

Class relationships (inheritance and composition) for the `modellib` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CBoneConstraintBase <|-- CBaseConstraint
    CBaseConstraint <|-- CBoneConstraintPoseSpaceBone
    CBoneConstraintPoseSpaceBone *-- `CBoneConstraintPoseSpaceBone::Input_t`
```
