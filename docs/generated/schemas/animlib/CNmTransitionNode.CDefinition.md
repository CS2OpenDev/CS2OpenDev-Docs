---
layout: default
title: "CNmTransitionNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmTransitionNode::CDefinition

# CNmTransitionNode::CDefinition

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmPoseNode::CDefinition](../animlib/CNmPoseNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmTransitionNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmTransitionNode::CDefinition" *-- NmPercent_t
    "CNmTransitionNode::CDefinition" *-- CNmBitFlags
    "CNmTransitionNode::CDefinition" *-- NmEasingOperation_t
    "CNmTransitionNode::CDefinition" *-- NmRootMotionBlendMode_t
```

## Memory layout

12 fields (11 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nTargetStateNodeIdx` | int16 |  |  |
| `0x12` | `m_nDurationOverrideNodeIdx` | int16 |  |  |
| `0x14` | `m_timeOffsetOverrideNodeIdx` | int16 |  |  |
| `0x16` | `m_startBoneMaskNodeIdx` | int16 |  |  |
| `0x18` | `m_flDuration` | float32 |  |  |
| `0x1c` | `m_boneMaskBlendInTimePercentage` | [NmPercent_t](../animlib/NmPercent_t.md) |  |  |
| `0x20` | `m_flTimeOffset` | float32 |  |  |
| `0x24` | `m_transitionOptions` | [CNmBitFlags](../animlib/CNmBitFlags.md) |  |  |
| `0x28` | `m_targetSyncIDNodeIdx` | int16 |  |  |
| `0x2a` | `m_blendWeightEasing` | [NmEasingOperation_t](../animlib/NmEasingOperation_t.md) |  |  |
| `0x2b` | `m_rootMotionBlend` | [NmRootMotionBlendMode_t](../animlib/NmRootMotionBlendMode_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmTransitionNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nTargetStateNodeIdx&quot;: -1,
	&quot;m_nDurationOverrideNodeIdx&quot;: -1,
	&quot;m_timeOffsetOverrideNodeIdx&quot;: -1,
	&quot;m_startBoneMaskNodeIdx&quot;: -1,
	&quot;m_flDuration&quot;: 0.000000,
	&quot;m_boneMaskBlendInTimePercentage&quot;:
	{
		&quot;m_flValue&quot;: 0.330000
	},
	&quot;m_flTimeOffset&quot;: 0.000000,
	&quot;m_transitionOptions&quot;:
	{
		&quot;m_flags&quot;: 1
	},
	&quot;m_targetSyncIDNodeIdx&quot;: -1,
	&quot;m_blendWeightEasing&quot;: &quot;Linear&quot;,
	&quot;m_rootMotionBlend&quot;: &quot;Blend&quot;
}</pre>
</details>
