---
layout: default
title: "UML: rendersystemdx11"
parent: Schemas
nav_exclude: true
---

# UML: rendersystemdx11

Class relationships (inheritance and composition) for the `rendersystemdx11` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    RsRasterizerStateDesc_t *-- RsFillMode_t
    RsRasterizerStateDesc_t *-- RsCullMode_t
    RsDepthStencilStateDesc_t *-- RsComparison_t
    RsDepthStencilStateDesc_t *-- RsStencilStateDesc_t
```
