---
layout: default
title: "CNmIDSwitchNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmIDSwitchNode::CDefinition

# CNmIDSwitchNode::CDefinition

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmIDValueNode::CDefinition](../animlib/CNmIDValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmIDValueNode::CDefinition" <|-- "CNmIDSwitchNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmIDValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

## Memory layout

6 fields (5 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nSwitchValueNodeIdx` | int16 |  |  |
| `0x12` | `m_nTrueValueNodeIdx` | int16 |  |  |
| `0x14` | `m_nFalseValueNodeIdx` | int16 |  |  |
| `0x18` | `m_falseValue` | CGlobalSymbol |  |  |
| `0x20` | `m_trueValue` | CGlobalSymbol |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmIDSwitchNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nSwitchValueNodeIdx&quot;: -1,
	&quot;m_nTrueValueNodeIdx&quot;: -1,
	&quot;m_nFalseValueNodeIdx&quot;: -1,
	&quot;m_falseValue&quot;: &quot;&quot;,
	&quot;m_trueValue&quot;: &quot;&quot;
}</pre>
</details>
