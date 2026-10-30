---
title: CMotionNode
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CMotionNode

# CMotionNode

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** n/a (unspecified) · **Module:** animgraphlib

**Derived by:** [CMotionNodeBlend1D](../animgraphlib/CMotionNodeBlend1D.md), [CMotionNodeSequence](../animgraphlib/CMotionNodeSequence.md)

**Relationships:**

```mermaid
classDiagram
    CMotionNode <|-- CMotionNodeBlend1D
    CMotionNode <|-- CMotionNodeSequence
    CMotionNode *-- AnimNodeID
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_name` | CUtlString |  |  |
| `0x20` | `m_id` | [AnimNodeID](../modellib/AnimNodeID.md) |  |  |
