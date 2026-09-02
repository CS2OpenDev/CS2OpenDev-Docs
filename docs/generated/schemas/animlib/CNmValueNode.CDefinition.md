---
layout: default
title: "CNmValueNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmValueNode::CDefinition

# CNmValueNode::CDefinition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** n/a (unspecified) · **Module:** animlib

**Inherits from:** [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md)

**Derived by:** [CNmBoneMaskValueNode::CDefinition](../animlib/CNmBoneMaskValueNode.CDefinition.md), [CNmBoolValueNode::CDefinition](../animlib/CNmBoolValueNode.CDefinition.md), [CNmFloatValueNode::CDefinition](../animlib/CNmFloatValueNode.CDefinition.md), [CNmIDValueNode::CDefinition](../animlib/CNmIDValueNode.CDefinition.md), [CNmTargetValueNode::CDefinition](../animlib/CNmTargetValueNode.CDefinition.md), [CNmVectorValueNode::CDefinition](../animlib/CNmVectorValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    `CNmGraphNode::CDefinition` <|-- `CNmValueNode::CDefinition`
    `CNmValueNode::CDefinition` <|-- `CNmBoneMaskValueNode::CDefinition`
    `CNmValueNode::CDefinition` <|-- `CNmBoolValueNode::CDefinition`
    `CNmValueNode::CDefinition` <|-- `CNmFloatValueNode::CDefinition`
    `CNmValueNode::CDefinition` <|-- `CNmIDValueNode::CDefinition`
    `CNmValueNode::CDefinition` <|-- `CNmTargetValueNode::CDefinition`
    `CNmValueNode::CDefinition` <|-- `CNmVectorValueNode::CDefinition`
```

## Memory layout

1 field (0 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
