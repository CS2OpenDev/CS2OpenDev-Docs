---
title: "CNmVelocityBlendNode::CDefinition"
module: animlib
kind: class
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmVelocityBlendNode::CDefinition

# CNmVelocityBlendNode::CDefinition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmParameterizedBlendNode::CDefinition](../animlib/CNmParameterizedBlendNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    `CNmParameterizedBlendNode::CDefinition` <|-- `CNmVelocityBlendNode::CDefinition`
    `CNmPoseNode::CDefinition` <|-- `CNmParameterizedBlendNode::CDefinition`
    `CNmGraphNode::CDefinition` <|-- `CNmPoseNode::CDefinition`
```

## Memory layout

4 fields (0 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_sourceNodeIndices` | CUtlLeanVectorFixedGrowable< int16, 5 > | [CNmParameterizedBlendNode::CDefinition](../animlib/CNmParameterizedBlendNode.CDefinition.md) |  |
| `0x28` | `m_nInputParameterValueNodeIdx` | int16 | [CNmParameterizedBlendNode::CDefinition](../animlib/CNmParameterizedBlendNode.CDefinition.md) |  |
| `0x2a` | `m_bAllowLooping` | bool | [CNmParameterizedBlendNode::CDefinition](../animlib/CNmParameterizedBlendNode.CDefinition.md) |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmVelocityBlendNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_sourceNodeIndices&quot;:
	[
	],
	&quot;m_nInputParameterValueNodeIdx&quot;: -1,
	&quot;m_bAllowLooping&quot;: true
}</pre>
</details>
