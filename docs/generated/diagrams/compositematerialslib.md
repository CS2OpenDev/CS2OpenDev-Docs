---
layout: default
title: "UML: compositematerialslib"
parent: Schemas
nav_exclude: true
---

# UML: compositematerialslib

Class relationships (inheritance and composition) for the `compositematerialslib` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CCompositeMaterialEditorDoc *-- CompositeMaterialEditorPoint_t
    CompMatPropertyMutator_t *-- CompositeMaterialInputLooseVariable_t
    CompMatPropertyMutator_t *-- CompMatMutatorCondition_t
    CompositeMaterialAssemblyProcedure_t *-- CompositeMaterialMatchFilter_t
    CompositeMaterialAssemblyProcedure_t *-- CompositeMaterialInputContainer_t
    CompositeMaterialAssemblyProcedure_t *-- CompMatPropertyMutator_t
    CompositeMaterialEditorPoint_t *-- CompositeMaterialAssemblyProcedure_t
    CompositeMaterialEditorPoint_t *-- CompositeMaterial_t
    CompositeMaterialInputContainer_t *-- CompositeMaterialInputLooseVariable_t
    CompositeMaterial_t *-- GeneratedTextureHandle_t
```
