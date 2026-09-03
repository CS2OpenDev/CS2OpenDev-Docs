---
title: CAnimGraphDoc_MoverNode
module: animgraphdoclib
kind: class
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_MoverNode

# CAnimGraphDoc_MoverNode

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 168 bytes (`0xa8`) · **Align:** 8 · **Module:** animgraphdoclib

**Inherits from:** [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md)

**Metadata:** `MPropertyFriendlyName Mover`

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_Node <|-- CAnimGraphDoc_MoverNode
    CAnimGraphDoc_MoverNode *-- CAnimGraphDoc_NodeConnection
    CAnimGraphDoc_MoverNode *-- AnimParamID
    CAnimGraphDoc_MoverNode *-- AnimValueSource
    CAnimGraphDoc_MoverNode *-- CAnimInputDamping
```

## Memory layout

21 fields (16 declared here, 5 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x20` | `m_sName` | CUtlString | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Name` `MPropertySortPriority 100` |
| `0x28` | `m_vecPosition` | Vector2D | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x30` | `m_nNodeID` | [AnimNodeID](../modellib/AnimNodeID.md) | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x34` | `m_bDebugThisNode` | bool | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Debug This Node` `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x38` | `m_networkMode` | [AnimNodeNetworkMode](../animgraphlib/AnimNodeNetworkMode.md) | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Network Mode` `MPropertySortPriority -110` |
| `0x40` | `m_inputConnection` | [CAnimGraphDoc_NodeConnection](../animgraphdoclib/CAnimGraphDoc_NodeConnection.md) |  | `MPropertySuppressField` |
| `0x48` | `m_bApplyMovement` | bool |  | `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName Generate Movement` `MPropertyGroupName Generate Movement` |
| `0x50` | `m_moveVectorParamName` | CUtlString |  | `MPropertySuppressField` |
| `0x58` | `m_moveVectorParam` | [AnimParamID](../modellib/AnimParamID.md) |  | `MPropertyAttrStateCallback` `MPropertyAttributeChoiceName VectorParameter` `MPropertyFriendlyName Movement Velocity Parameter` `MPropertyGroupName Generate Movement` |
| `0x5c` | `m_bOrientMovement` | bool |  | `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName Orient Movement` `MPropertyGroupName Orient Movement` |
| `0x60` | `m_moveHeadingParamName` | CUtlString |  | `MPropertySuppressField` |
| `0x68` | `m_moveHeadingParam` | [AnimParamID](../modellib/AnimParamID.md) |  | `MPropertyAttrStateCallback` `MPropertyAttributeChoiceName FloatParameter` `MPropertyFriendlyName Movement Heading Parameter` `MPropertyGroupName Orient Movement` |
| `0x6c` | `m_bAdditive` | bool |  | `MPropertyFriendlyName Additive` |
| `0x6d` | `m_bTurnToFace` | bool |  | `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName Turn to Face` `MPropertyGroupName Turn to Face` |
| `0x70` | `m_facingTarget` | [AnimValueSource](../animgraphlib/AnimValueSource.md) |  | `MPropertyAttrStateCallback` `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName Face Direction` `MPropertyGroupName Turn to Face` |
| `0x78` | `m_paramName` | CUtlString |  | `MPropertySuppressField` |
| `0x80` | `m_param` | [AnimParamID](../modellib/AnimParamID.md) |  | `MPropertyAttrStateCallback` `MPropertyAttributeChoiceName FloatParameter` `MPropertyFriendlyName Facing Parameter` `MPropertyGroupName Turn to Face` |
| `0x84` | `m_bLimitOnly` | bool |  | `MPropertyAttrStateCallback` `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName Turn Limit Only` `MPropertyGroupName Turn to Face` |
| `0x88` | `m_flTurnToFaceOffset` | float32 |  | `MPropertyAttrStateCallback` `MPropertyAttributeRange -180 180` `MPropertyFriendlyName Turn to Face Offset` `MPropertyGroupName Turn to Face` |
| `0x8c` | `m_flTurnToFaceLimit` | float32 |  | `MPropertyAttrStateCallback` `MPropertyAttributeRange 0 180` `MPropertyFriendlyName Turn to Face Limit` `MPropertyGroupName Turn to Face` |
| `0x90` | `m_damping` | [CAnimInputDamping](../animgraphlib/CAnimInputDamping.md) |  | `MPropertyAttrStateCallback` `MPropertyFriendlyName Damping` `MPropertyGroupName Turn to Face` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimGraphDoc_MoverNode&quot;,
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
	&quot;m_inputConnection&quot;:
	{
		&quot;m_nodeID&quot;:
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		&quot;m_outputID&quot;:
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		}
	},
	&quot;m_bApplyMovement&quot;: true,
	&quot;m_moveVectorParamName&quot;: &quot;&quot;,
	&quot;m_moveVectorParam&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_bOrientMovement&quot;: false,
	&quot;m_moveHeadingParamName&quot;: &quot;&quot;,
	&quot;m_moveHeadingParam&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_bAdditive&quot;: false,
	&quot;m_bTurnToFace&quot;: false,
	&quot;m_facingTarget&quot;: &quot;Parameter&quot;,
	&quot;m_paramName&quot;: &quot;&quot;,
	&quot;m_param&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_bLimitOnly&quot;: false,
	&quot;m_flTurnToFaceOffset&quot;: 0.000000,
	&quot;m_flTurnToFaceLimit&quot;: 180.000000,
	&quot;m_damping&quot;:
	{
		&quot;_class&quot;: &quot;CAnimInputDamping&quot;,
		&quot;m_speedFunction&quot;: &quot;NoDamping&quot;,
		&quot;m_fSpeedScale&quot;: 1.000000,
		&quot;m_fFallingSpeedScale&quot;: 1.000000
	}
}</pre>
</details>
