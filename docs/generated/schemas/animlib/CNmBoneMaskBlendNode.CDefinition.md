---
layout: default
title: "CNmBoneMaskBlendNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmBoneMaskBlendNode::CDefinition

# CNmBoneMaskBlendNode::CDefinition

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmBoneMaskValueNode::CDefinition](../animlib/CNmBoneMaskValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskBlendNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoneMaskValueNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmValueNode::CDefinition"
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nSourceMaskNodeIdx` | int16 |  |  |
| `0x12` | `m_nTargetMaskNodeIdx` | int16 |  |  |
| `0x14` | `m_nBlendWeightValueNodeIdx` | int16 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmBoneMaskBlendNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nSourceMaskNodeIdx&quot;: -1,
	&quot;m_nTargetMaskNodeIdx&quot;: -1,
	&quot;m_nBlendWeightValueNodeIdx&quot;: -1
}</pre>
</details>
