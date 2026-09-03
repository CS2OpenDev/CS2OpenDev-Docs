---
title: "CNmFloatEaseNode::CDefinition"
module: animlib
kind: class
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmFloatEaseNode::CDefinition

# CNmFloatEaseNode::CDefinition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmFloatValueNode::CDefinition](../animlib/CNmFloatValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    `CNmFloatValueNode::CDefinition` <|-- `CNmFloatEaseNode::CDefinition`
    `CNmValueNode::CDefinition` <|-- `CNmFloatValueNode::CDefinition`
    `CNmGraphNode::CDefinition` <|-- `CNmValueNode::CDefinition`
    `CNmFloatEaseNode::CDefinition` *-- NmEasingOperation_t
```

## Memory layout

6 fields (5 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_flEaseTime` | float32 |  |  |
| `0x14` | `m_flStartValue` | float32 |  |  |
| `0x18` | `m_nInputValueNodeIdx` | int16 |  |  |
| `0x1a` | `m_easingOp` | [NmEasingOperation_t](../animlib/NmEasingOperation_t.md) |  |  |
| `0x1b` | `m_bUseStartValue` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmFloatEaseNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_flEaseTime&quot;: 1.000000,
	&quot;m_flStartValue&quot;: 0.000000,
	&quot;m_nInputValueNodeIdx&quot;: -1,
	&quot;m_easingOp&quot;: &quot;Linear&quot;,
	&quot;m_bUseStartValue&quot;: false
}</pre>
</details>
