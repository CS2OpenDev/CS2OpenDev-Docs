---
layout: default
title: "CNmVectorCreateNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmVectorCreateNode::CDefinition

# CNmVectorCreateNode::CDefinition

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmVectorValueNode::CDefinition](../animlib/CNmVectorValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmVectorValueNode::CDefinition" <|-- "CNmVectorCreateNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

## Memory layout

5 fields (4 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_inputVectorValueNodeIdx` | int16 |  |  |
| `0x12` | `m_inputValueXNodeIdx` | int16 |  |  |
| `0x14` | `m_inputValueYNodeIdx` | int16 |  |  |
| `0x16` | `m_inputValueZNodeIdx` | int16 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmVectorCreateNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_inputVectorValueNodeIdx&quot;: -1,
	&quot;m_inputValueXNodeIdx&quot;: -1,
	&quot;m_inputValueYNodeIdx&quot;: -1,
	&quot;m_inputValueZNodeIdx&quot;: -1
}</pre>
</details>
