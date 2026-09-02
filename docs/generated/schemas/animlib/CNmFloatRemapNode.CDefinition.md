---
layout: default
title: "CNmFloatRemapNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmFloatRemapNode::CDefinition

# CNmFloatRemapNode::CDefinition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmFloatValueNode::CDefinition](../animlib/CNmFloatValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    `CNmFloatValueNode::CDefinition` <|-- `CNmFloatRemapNode::CDefinition`
    `CNmValueNode::CDefinition` <|-- `CNmFloatValueNode::CDefinition`
    `CNmGraphNode::CDefinition` <|-- `CNmValueNode::CDefinition`
    `CNmFloatRemapNode::CDefinition` *-- `CNmFloatRemapNode::RemapRange_t`
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nInputValueNodeIdx` | int16 |  |  |
| `0x14` | `m_inputRange` | [CNmFloatRemapNode::RemapRange_t](../animlib/CNmFloatRemapNode.RemapRange_t.md) |  |  |
| `0x1c` | `m_outputRange` | [CNmFloatRemapNode::RemapRange_t](../animlib/CNmFloatRemapNode.RemapRange_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmFloatRemapNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nInputValueNodeIdx&quot;: -1,
	&quot;m_inputRange&quot;:
	{
		&quot;m_flBegin&quot;: 0.000000,
		&quot;m_flEnd&quot;: 0.000000
	},
	&quot;m_outputRange&quot;:
	{
		&quot;m_flBegin&quot;: 0.000000,
		&quot;m_flEnd&quot;: 0.000000
	}
}</pre>
</details>
