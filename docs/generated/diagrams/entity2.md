---
layout: default
title: "UML: entity2"
parent: Schemas
nav_exclude: true
---

# UML: entity2

Class relationships (inheritance and composition) for the `entity2` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CEntityComponent <|-- CScriptComponent
    CEntityInstance --> CEntityIdentity
    CEntityInstance --> CScriptComponent
```
