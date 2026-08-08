---
layout: default
title: "CNmSpeedScaleBaseNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmSpeedScaleBaseNode::CDefinition

# CNmSpeedScaleBaseNode::CDefinition

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmPassthroughNode::CDefinition](../animlib/CNmPassthroughNode.CDefinition.md)

**Derived by:** [CNmDurationScaleNode::CDefinition](../animlib/CNmDurationScaleNode.CDefinition.md), [CNmSpeedScaleNode::CDefinition](../animlib/CNmSpeedScaleNode.CDefinition.md), [CNmVelocityBasedSpeedScaleNode::CDefinition](../animlib/CNmVelocityBasedSpeedScaleNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmPassthroughNode::CDefinition" <|-- "CNmSpeedScaleBaseNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmSpeedScaleBaseNode::CDefinition" <|-- "CNmDurationScaleNode::CDefinition"
    "CNmSpeedScaleBaseNode::CDefinition" <|-- "CNmSpeedScaleNode::CDefinition"
    "CNmSpeedScaleBaseNode::CDefinition" <|-- "CNmVelocityBasedSpeedScaleNode::CDefinition"
```

## Memory layout

4 fields (2 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nChildNodeIdx` | int16 | [CNmPassthroughNode::CDefinition](../animlib/CNmPassthroughNode.CDefinition.md) |  |
| `0x18` | `m_nInputValueNodeIdx` | int16 |  |  |
| `0x1c` | `m_flDefaultInputValue` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmSpeedScaleBaseNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nChildNodeIdx&quot;: -1,
	&quot;m_nInputValueNodeIdx&quot;: -1,
	&quot;m_flDefaultInputValue&quot;: 0.000000
}</pre>
</details>
