---
layout: default
title: "CNmControlParameterVectorNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmControlParameterVectorNode::CDefinition

# CNmControlParameterVectorNode::CDefinition

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmVectorValueNode::CDefinition](../animlib/CNmVectorValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmVectorValueNode::CDefinition" <|-- "CNmControlParameterVectorNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmVectorValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

## Memory layout

1 fields (0 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmControlParameterVectorNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1
}</pre>
</details>
