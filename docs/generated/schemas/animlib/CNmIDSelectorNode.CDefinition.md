---
layout: default
title: "CNmIDSelectorNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmIDSelectorNode::CDefinition

# CNmIDSelectorNode::CDefinition

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmIDValueNode::CDefinition](../animlib/CNmIDValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmIDValueNode::CDefinition" <|-- "CNmIDSelectorNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_conditionNodeIndices` | CUtlLeanVectorFixedGrowable< int16, 5 > |  |  |
| `0x28` | `m_values` | CUtlLeanVectorFixedGrowable< CGlobalSymbol, 5 > |  |  |
| `0x58` | `m_defaultValue` | CGlobalSymbol |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmIDSelectorNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_conditionNodeIndices&quot;:
	[
	],
	&quot;m_values&quot;:
	[
	],
	&quot;m_defaultValue&quot;: &quot;&quot;
}</pre>
</details>
