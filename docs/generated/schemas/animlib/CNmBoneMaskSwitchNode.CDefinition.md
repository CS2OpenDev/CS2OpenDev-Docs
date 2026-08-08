---
layout: default
title: "CNmBoneMaskSwitchNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmBoneMaskSwitchNode::CDefinition

# CNmBoneMaskSwitchNode::CDefinition

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmBoneMaskValueNode::CDefinition](../animlib/CNmBoneMaskValueNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmBoneMaskValueNode::CDefinition" <|-- "CNmBoneMaskSwitchNode::CDefinition"
    "CNmValueNode::CDefinition" <|-- "CNmBoneMaskValueNode::CDefinition"
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
| `0x18` | `m_flBlendTimeSeconds` | float32 |  |  |
| `0x1c` | `m_bSwitchDynamically` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmBoneMaskSwitchNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nSwitchValueNodeIdx&quot;: -1,
	&quot;m_nTrueValueNodeIdx&quot;: -1,
	&quot;m_nFalseValueNodeIdx&quot;: -1,
	&quot;m_flBlendTimeSeconds&quot;: 0.100000,
	&quot;m_bSwitchDynamically&quot;: false
}</pre>
</details>
