---
layout: default
title: CAnimGraphDoc_TargetSelectorNode
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_TargetSelectorNode

# CAnimGraphDoc_TargetSelectorNode

**Kind:** class · **Size:** 128 bytes (`0x80`) · **Align:** 8 · **Module:** animgraphdoclib

**Inherits from:** [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md)

**Metadata:** `MPropertyFriendlyName Target Selector`

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_Node <|-- CAnimGraphDoc_TargetSelectorNode
    CAnimGraphDoc_TargetSelectorNode *-- CTargetSelectorChild
    CAnimGraphDoc_TargetSelectorNode *-- TargetWarpLinearRootMotionMode
    CAnimGraphDoc_TargetSelectorNode *-- TargetSelectorAngleMode_t
    CAnimGraphDoc_TargetSelectorNode *-- AnimParamID
```

## Memory layout

16 fields (11 declared here, 5 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x20` | `m_sName` | CUtlString | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Name` `MPropertySortPriority 100` |
| `0x28` | `m_vecPosition` | Vector2D | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x30` | `m_nNodeID` | [AnimNodeID](../modellib/AnimNodeID.md) | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x34` | `m_bDebugThisNode` | bool | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Debug This Node` `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x38` | `m_networkMode` | [AnimNodeNetworkMode](../!GlobalTypes/AnimNodeNetworkMode.md) | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Network Mode` `MPropertySortPriority -110` |
| `0x40` | `m_children` | CUtlVector< [CTargetSelectorChild](../animgraphdoclib/CTargetSelectorChild.md) > |  |  |
| `0x58` | `m_eLinearRootMotionMode` | [TargetWarpLinearRootMotionMode](../!GlobalTypes/TargetWarpLinearRootMotionMode.md) |  | `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName Linear Root Motion Mode` |
| `0x5c` | `m_eAngleMode` | [TargetSelectorAngleMode_t](../!GlobalTypes/TargetSelectorAngleMode_t.md) |  | `MPropertyFriendlyName Angle Mode` |
| `0x60` | `m_moveHeadingParamID` | [AnimParamID](../modellib/AnimParamID.md) |  | `MPropertyAttributeChoiceName FloatParameter` `MPropertyFriendlyName Move Heading` |
| `0x64` | `m_desiredMoveHeadingParamID` | [AnimParamID](../modellib/AnimParamID.md) |  | `MPropertyAttributeChoiceName FloatParameter` `MPropertyFriendlyName Desired Move Heading` |
| `0x68` | `m_targetPositionParamID` | [AnimParamID](../modellib/AnimParamID.md) |  | `MPropertyAttrStateCallback` `MPropertyAttributeChoiceName VectorParameter` `MPropertyFriendlyName Target Position` |
| `0x6c` | `m_bTargetPositionIsWorldSpace` | bool |  | `MPropertyAttrStateCallback` `MPropertyFriendlyName Target Position Is World Space` |
| `0x70` | `m_targetFacePositionParamID` | [AnimParamID](../modellib/AnimParamID.md) |  | `MPropertyAttributeChoiceName VectorParameter` `MPropertyFriendlyName Target Face Position` |
| `0x74` | `m_bTargetFacePositionIsWorldSpace` | bool |  | `MPropertyFriendlyName Target Face Position Is World Space` |
| `0x75` | `m_bEnablePhaseMatching` | bool |  |  |
| `0x78` | `m_flPhaseMatchingMaxRootMotionSkip` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimGraphDoc_TargetSelectorNode&quot;,
	&quot;m_sName&quot;: &quot;Unnamed&quot;,
	&quot;m_vecPosition&quot;:
	[
		0.000000,
		0.000000
	],
	&quot;m_nNodeID&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_bDebugThisNode&quot;: false,
	&quot;m_networkMode&quot;: &quot;ServerAuthoritative&quot;,
	&quot;m_children&quot;:
	[
	],
	&quot;m_eLinearRootMotionMode&quot;: &quot;TargetWarpLinearRootMotionMode_Default&quot;,
	&quot;m_eAngleMode&quot;: &quot;eFacingHeading&quot;,
	&quot;m_moveHeadingParamID&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_desiredMoveHeadingParamID&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_targetPositionParamID&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_bTargetPositionIsWorldSpace&quot;: false,
	&quot;m_targetFacePositionParamID&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_bTargetFacePositionIsWorldSpace&quot;: false,
	&quot;m_bEnablePhaseMatching&quot;: false,
	&quot;m_flPhaseMatchingMaxRootMotionSkip&quot;: 0.400000
}</pre>
</details>
