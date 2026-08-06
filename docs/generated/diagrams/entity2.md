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
    CEntityComponentHelper --> EntComponentInfo_t
    EntComponentInfo_t --> CEntityComponentHelper
    EntityIOQueuePrioritizedEvent_t *-- GameTime_t
    EntityIOQueuePrioritizedEvent_t *-- CVariantDefaultAllocator
    CEntityIdentity --> CEntityAttributeTable
    CEntityInstance --> CEntityIdentity
    CEntityInstance --> CScriptComponent
```
