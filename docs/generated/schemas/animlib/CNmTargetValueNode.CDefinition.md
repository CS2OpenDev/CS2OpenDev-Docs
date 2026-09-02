---
title: "CNmTargetValueNode::CDefinition"
module: animlib
kind: class
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmTargetValueNode::CDefinition

# CNmTargetValueNode::CDefinition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** n/a (unspecified) · **Module:** animlib

**Inherits from:** [CNmValueNode::CDefinition](../animlib/CNmValueNode.CDefinition.md)

**Derived by:** [CNmCachedTargetNode::CDefinition](../animlib/CNmCachedTargetNode.CDefinition.md), [CNmConstTargetNode::CDefinition](../animlib/CNmConstTargetNode.CDefinition.md), [CNmControlParameterTargetNode::CDefinition](../animlib/CNmControlParameterTargetNode.CDefinition.md), [CNmTargetOffsetNode::CDefinition](../animlib/CNmTargetOffsetNode.CDefinition.md), [CNmVirtualParameterTargetNode::CDefinition](../animlib/CNmVirtualParameterTargetNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    `CNmValueNode::CDefinition` <|-- `CNmTargetValueNode::CDefinition`
    `CNmGraphNode::CDefinition` <|-- `CNmValueNode::CDefinition`
    `CNmTargetValueNode::CDefinition` <|-- `CNmCachedTargetNode::CDefinition`
    `CNmTargetValueNode::CDefinition` <|-- `CNmConstTargetNode::CDefinition`
    `CNmTargetValueNode::CDefinition` <|-- `CNmControlParameterTargetNode::CDefinition`
    `CNmTargetValueNode::CDefinition` <|-- `CNmTargetOffsetNode::CDefinition`
    `CNmTargetValueNode::CDefinition` <|-- `CNmVirtualParameterTargetNode::CDefinition`
```

## Memory layout

1 field (0 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
