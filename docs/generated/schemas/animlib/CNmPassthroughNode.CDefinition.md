---
layout: default
title: "CNmPassthroughNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmPassthroughNode::CDefinition

# CNmPassthroughNode::CDefinition

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmPoseNode::CDefinition](../animlib/CNmPoseNode.CDefinition.md)

**Derived by:** [CNmAimCSNode::CDefinition](../server/CNmAimCSNode.CDefinition.md), [CNmChainLookatNode::CDefinition](../animlib/CNmChainLookatNode.CDefinition.md), [CNmFollowBoneNode::CDefinition](../animlib/CNmFollowBoneNode.CDefinition.md), [CNmFootIKNode::CDefinition](../animlib/CNmFootIKNode.CDefinition.md), [CNmRootMotionOverrideNode::CDefinition](../animlib/CNmRootMotionOverrideNode.CDefinition.md), [CNmScaleNode::CDefinition](../animlib/CNmScaleNode.CDefinition.md), [CNmSnapWeaponNode::CDefinition](../server/CNmSnapWeaponNode.CDefinition.md), [CNmSpeedScaleBaseNode::CDefinition](../animlib/CNmSpeedScaleBaseNode.CDefinition.md), [CNmTwoBoneIKNode::CDefinition](../animlib/CNmTwoBoneIKNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmAimCSNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmChainLookatNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmFollowBoneNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmFootIKNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmRootMotionOverrideNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmScaleNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmSnapWeaponNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmSpeedScaleBaseNode::CDefinition"
    "CNmPassthroughNode::CDefinition" <|-- "CNmTwoBoneIKNode::CDefinition"
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nChildNodeIdx` | int16 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmPassthroughNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nChildNodeIdx&quot;: -1
}</pre>
</details>
