---
layout: default
title: "CNmFloatClampNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmFloatClampNode::CDefinition

# CNmFloatClampNode::CDefinition

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmFloatValueNode::CDefinition](../animlib/CNmFloatValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmFloatValueNode::CDefinition" <|-- "CNmFloatClampNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmFloatValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

## Memory layout

3 fields (2 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nInputValueNodeIdx` | int16 |  |  |
| `0x14` | `m_clampRange` | Range_t |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmFloatClampNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nInputValueNodeIdx&quot;: -1,
	&quot;m_clampRange&quot;:
	{
		&quot;m_flMin&quot;: 0.000000,
		&quot;m_flMax&quot;: 0.000000
	}
}</pre>
</details>
