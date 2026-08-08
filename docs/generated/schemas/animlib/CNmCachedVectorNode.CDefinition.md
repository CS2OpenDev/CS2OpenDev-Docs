---
layout: default
title: "CNmCachedVectorNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmCachedVectorNode::CDefinition

# CNmCachedVectorNode::CDefinition

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmVectorValueNode::CDefinition](../animlib/CNmVectorValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmVectorValueNode::CDefinition" <|-- "CNmCachedVectorNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
    "CNmCachedVectorNode::CDefinition" *-- NmCachedValueMode_t
```

## Memory layout

3 fields (2 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nInputValueNodeIdx` | int16 |  |  |
| `0x14` | `m_mode` | [NmCachedValueMode_t](../!GlobalTypes/NmCachedValueMode_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmCachedVectorNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nInputValueNodeIdx&quot;: -1,
	&quot;m_mode&quot;: &quot;OnEntry&quot;
}</pre>
</details>
