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
    CompositeMaterial_t *-- GeneratedTextureHandle_t
    CompositeMaterialMatchFilter_t *-- CompositeMaterialMatchFilterType_t
    CCompositeMaterialEditorDoc *-- CompositeMaterialEditorPoint_t
    CompMatPropertyMutator_t *-- CompMatPropertyMutatorType_t
    CompMatPropertyMutator_t *-- CompositeMaterialInputLooseVariable_t
    CompMatPropertyMutator_t *-- CompMatMutatorCondition_t
    CompMatMutatorCondition_t *-- CompMatPropertyMutatorConditionType_t
    CompositeMaterialEditorPoint_t *-- CompositeMaterialAssemblyProcedure_t
    CompositeMaterialEditorPoint_t *-- CompositeMaterial_t
    CompositeMaterialInputLooseVariable_t *-- CompositeMaterialInputLooseVariableType_t
    CompositeMaterialInputLooseVariable_t *-- CompositeMaterialVarSystemVar_t
    CompositeMaterialInputLooseVariable_t *-- CompositeMaterialInputTextureType_t
    CompositeMaterialAssemblyProcedure_t *-- CompositeMaterialMatchFilter_t
    CompositeMaterialAssemblyProcedure_t *-- CompositeMaterialInputContainer_t
    CompositeMaterialAssemblyProcedure_t *-- CompMatPropertyMutator_t
    CompositeMaterialInputContainer_t *-- CompositeMaterialInputContainerSourceType_t
    CompositeMaterialInputContainer_t *-- CompositeMaterialInputLooseVariable_t
```
