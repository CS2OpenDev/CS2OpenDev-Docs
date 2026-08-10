---
layout: default
title: "CNmFollowBoneNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmFollowBoneNode::CDefinition

# CNmFollowBoneNode::CDefinition

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmPassthroughNode::CDefinition](../animlib/CNmPassthroughNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmPassthroughNode::CDefinition" <|-- "CNmFollowBoneNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmFollowBoneNode::CDefinition" *-- NmFollowBoneMode_t
```

## Memory layout

6 fields (4 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nChildNodeIdx` | int16 | [CNmPassthroughNode::CDefinition](../animlib/CNmPassthroughNode.CDefinition.md) |  |
| `0x18` | `m_bone` | CGlobalSymbol |  |  |
| `0x20` | `m_followTargetBone` | CGlobalSymbol |  |  |
| `0x28` | `m_nEnabledNodeIdx` | int16 |  |  |
| `0x2a` | `m_mode` | [NmFollowBoneMode_t](../animlib/NmFollowBoneMode_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmFollowBoneNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nChildNodeIdx&quot;: -1,
	&quot;m_bone&quot;: &quot;&quot;,
	&quot;m_followTargetBone&quot;: &quot;&quot;,
	&quot;m_nEnabledNodeIdx&quot;: -1,
	&quot;m_mode&quot;: &quot;RotationAndTranslation&quot;
}</pre>
</details>
