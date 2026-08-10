---
layout: default
title: "CNmFloatSelectorNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmFloatSelectorNode::CDefinition

# CNmFloatSelectorNode::CDefinition

**Kind:** class · **Size:** 88 bytes (`0x58`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmFloatValueNode::CDefinition](../animlib/CNmFloatValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatSelectorNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmFloatSelectorNode::CDefinition" *-- NmEasingOperation_t
```

## Memory layout

6 fields (5 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_conditionNodeIndices` | CUtlLeanVectorFixedGrowable< int16, 5 > |  |  |
| `0x28` | `m_values` | CUtlLeanVectorFixedGrowable< float32, 5 > |  |  |
| `0x48` | `m_flDefaultValue` | float32 |  |  |
| `0x4c` | `m_flEaseTime` | float32 |  |  |
| `0x50` | `m_easingOp` | [NmEasingOperation_t](../animlib/NmEasingOperation_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmFloatSelectorNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_conditionNodeIndices&quot;:
	[
	],
	&quot;m_values&quot;:
	[
	],
	&quot;m_flDefaultValue&quot;: 0.000000,
	&quot;m_flEaseTime&quot;: 0.200000,
	&quot;m_easingOp&quot;: &quot;Linear&quot;
}</pre>
</details>
