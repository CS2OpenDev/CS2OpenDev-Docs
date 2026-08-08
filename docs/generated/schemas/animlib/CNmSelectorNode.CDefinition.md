---
layout: default
title: "CNmSelectorNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmSelectorNode::CDefinition

# CNmSelectorNode::CDefinition

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmPoseNode::CDefinition](../animlib/CNmPoseNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmSelectorNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
```

## Memory layout

3 fields (2 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_optionNodeIndices` | CUtlLeanVectorFixedGrowable< int16, 8 > |  |  |
| `0x28` | `m_conditionNodeIndices` | CUtlLeanVectorFixedGrowable< int16, 8 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmSelectorNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_optionNodeIndices&quot;:
	[
	],
	&quot;m_conditionNodeIndices&quot;:
	[
	]
}</pre>
</details>
