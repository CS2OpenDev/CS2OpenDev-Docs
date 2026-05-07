---
layout: default
title: "UML: rendersystemvulkan"
parent: Schemas
nav_exclude: true
---

# UML: rendersystemvulkan

Class relationships (inheritance and composition) for the `rendersystemvulkan` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    RsDepthStencilStateDesc_t *-- RsComparison_t
    RsDepthStencilStateDesc_t *-- RsStencilStateDesc_t
    RsRasterizerStateDesc_t *-- RsFillMode_t
    RsRasterizerStateDesc_t *-- RsCullMode_t
```
