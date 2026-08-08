---
layout: default
title: "CNmFloatRangeComparisonNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmFloatRangeComparisonNode::CDefinition

# CNmFloatRangeComparisonNode::CDefinition

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmBoolValueNode::CDefinition](../animlib/CNmBoolValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmBoolValueNode::CDefinition" <|-- "CNmFloatRangeComparisonNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoolValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_range` | Range_t |  |  |
| `0x18` | `m_nInputValueNodeIdx` | int16 |  |  |
| `0x1a` | `m_bIsInclusiveCheck` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmFloatRangeComparisonNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_range&quot;:
	{
		&quot;m_flMin&quot;: 340282346638528859811704183484516925440.000000,
		&quot;m_flMax&quot;: -340282346638528859811704183484516925440.000000
	},
	&quot;m_nInputValueNodeIdx&quot;: -1,
	&quot;m_bIsInclusiveCheck&quot;: true
}</pre>
</details>
