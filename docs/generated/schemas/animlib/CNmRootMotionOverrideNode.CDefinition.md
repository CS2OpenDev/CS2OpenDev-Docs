---
layout: default
title: "CNmRootMotionOverrideNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmRootMotionOverrideNode::CDefinition

# CNmRootMotionOverrideNode::CDefinition

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmPassthroughNode::CDefinition](../animlib/CNmPassthroughNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmPassthroughNode::CDefinition" <|-- "CNmRootMotionOverrideNode::CDefinition"
    "CNmPoseNode::CDefinition" <|-- "CNmPassthroughNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmRootMotionOverrideNode::CDefinition" *-- CNmBitFlags
```

## Memory layout

10 fields (8 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nChildNodeIdx` | int16 | [CNmPassthroughNode::CDefinition](../animlib/CNmPassthroughNode.CDefinition.md) |  |
| `0x18` | `m_desiredMovingVelocityNodeIdx` | int16 |  |  |
| `0x1a` | `m_desiredFacingDirectionNodeIdx` | int16 |  |  |
| `0x1c` | `m_linearVelocityLimitNodeIdx` | int16 |  |  |
| `0x1e` | `m_angularVelocityLimitNodeIdx` | int16 |  |  |
| `0x20` | `m_enabledNodeIdx` | int16 |  |  |
| `0x24` | `m_maxLinearVelocity` | float32 |  |  |
| `0x28` | `m_maxAngularVelocityRadians` | float32 |  |  |
| `0x2c` | `m_overrideFlags` | [CNmBitFlags](../animlib/CNmBitFlags.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmRootMotionOverrideNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nChildNodeIdx&quot;: -1,
	&quot;m_desiredMovingVelocityNodeIdx&quot;: -1,
	&quot;m_desiredFacingDirectionNodeIdx&quot;: -1,
	&quot;m_linearVelocityLimitNodeIdx&quot;: -1,
	&quot;m_angularVelocityLimitNodeIdx&quot;: -1,
	&quot;m_enabledNodeIdx&quot;: -1,
	&quot;m_maxLinearVelocity&quot;: -1.000000,
	&quot;m_maxAngularVelocityRadians&quot;: -1.000000,
	&quot;m_overrideFlags&quot;:
	{
		&quot;m_flags&quot;: 1
	}
}</pre>
</details>
