---
layout: default
title: "CNmFootIKNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmFootIKNode::CDefinition

# CNmFootIKNode::CDefinition

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmPassthroughNode::CDefinition](../animlib/CNmPassthroughNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmPassthroughNode::CDefinition" <|-- "CNmFootIKNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmFootIKNode::CDefinition" *-- NmIKBlendMode_t
```

## Memory layout

10 fields (8 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nChildNodeIdx` | int16 | [CNmPassthroughNode::CDefinition](../animlib/CNmPassthroughNode.CDefinition.md) |  |
| `0x18` | `m_leftEffectorBoneID` | CGlobalSymbol |  |  |
| `0x20` | `m_rightEffectorBoneID` | CGlobalSymbol |  |  |
| `0x28` | `m_nLeftTargetNodeIdx` | int16 |  |  |
| `0x2a` | `m_nRightTargetNodeIdx` | int16 |  |  |
| `0x2c` | `m_nEnabledNodeIdx` | int16 |  |  |
| `0x30` | `m_flBlendTimeSeconds` | float32 |  |  |
| `0x34` | `m_blendMode` | [NmIKBlendMode_t](../animlib/NmIKBlendMode_t.md) |  |  |
| `0x35` | `m_bIsTargetInWorldSpace` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmFootIKNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nChildNodeIdx&quot;: -1,
	&quot;m_leftEffectorBoneID&quot;: &quot;&quot;,
	&quot;m_rightEffectorBoneID&quot;: &quot;&quot;,
	&quot;m_nLeftTargetNodeIdx&quot;: -1,
	&quot;m_nRightTargetNodeIdx&quot;: -1,
	&quot;m_nEnabledNodeIdx&quot;: -1,
	&quot;m_flBlendTimeSeconds&quot;: 0.000000,
	&quot;m_blendMode&quot;: &quot;Effector&quot;,
	&quot;m_bIsTargetInWorldSpace&quot;: false
}</pre>
</details>
