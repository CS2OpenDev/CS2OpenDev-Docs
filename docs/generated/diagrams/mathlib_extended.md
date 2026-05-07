---
layout: default
title: "UML: mathlib_extended"
parent: Schemas
nav_exclude: true
---

# UML: mathlib_extended

Class relationships (inheritance and composition) for the `mathlib_extended` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    FunctionInfo_t *-- FuseFunctionIndex_t
    CFuseProgram *-- FuseVariableIndex_t
    VariableInfo_t *-- FuseVariableIndex_t
    VariableInfo_t *-- FuseVariableType_t
    VariableInfo_t *-- FuseVariableAccess_t
    CFuseSymbolTable *-- ConstantInfo_t
    CFuseSymbolTable *-- VariableInfo_t
    CFuseSymbolTable *-- FunctionInfo_t
```
