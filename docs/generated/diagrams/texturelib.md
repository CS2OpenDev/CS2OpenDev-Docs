---
layout: default
title: "UML: texturelib"
parent: Schemas
nav_exclude: true
---

# UML: texturelib

Class relationships (inheritance and composition) for the `texturelib` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CTextureSheetDoc --> CTextureSheetDoc_Sequence
    CTextureSheetDoc_Sequence *-- CTextureSheetDoc_SequenceDecalParams
    CTextureSheetDoc_Sequence *-- CTextureSheetDoc_Frame
```
