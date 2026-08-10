---
layout: default
title: CAnimGraphDoc_AimMatrixNode
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_AimMatrixNode

# CAnimGraphDoc_AimMatrixNode

**Kind:** class · **Size:** 192 bytes (`0xc0`) · **Align:** 8 · **Module:** animgraphdoclib

**Inherits from:** [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md)

**Metadata:** `MPropertyFriendlyName Aim Matrix`

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_Node <|-- CAnimGraphDoc_AimMatrixNode
    CAnimGraphDoc_AimMatrixNode *-- CAnimGraphDoc_NodeConnection
    CAnimGraphDoc_AimMatrixNode *-- AnimVectorSource
    CAnimGraphDoc_AimMatrixNode *-- AnimParamID
    CAnimGraphDoc_AimMatrixNode *-- AimMatrixBlendMode
    CAnimGraphDoc_AimMatrixNode *-- CBlendCurve
    CAnimGraphDoc_AimMatrixNode *-- CAnimInputDamping
```

## Memory layout

23 fields (18 declared here, 5 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x20` | `m_sName` | CUtlString | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Name` `MPropertySortPriority 100` |
| `0x28` | `m_vecPosition` | Vector2D | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x30` | `m_nNodeID` | [AnimNodeID](../modellib/AnimNodeID.md) | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x34` | `m_bDebugThisNode` | bool | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Debug This Node` `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x38` | `m_networkMode` | [AnimNodeNetworkMode](../animgraphlib/AnimNodeNetworkMode.md) | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Network Mode` `MPropertySortPriority -110` |
| `0x48` | `m_inputConnection` | [CAnimGraphDoc_NodeConnection](../animgraphdoclib/CAnimGraphDoc_NodeConnection.md) |  | `MPropertySuppressField` |
| `0x50` | `m_sequenceName` | CUtlString |  | `MPropertyAttributeChoiceName Sequence` `MPropertyFriendlyName Sequence` |
| `0x58` | `m_flMaxYawAngle` | float32 |  | `MPropertyFriendlyName Max Yaw Angle` |
| `0x5c` | `m_flMaxPitchAngle` | float32 |  | `MPropertyFriendlyName Max Pitch Angle` |
| `0x60` | `m_target` | [AnimVectorSource](../animgraphlib/AnimVectorSource.md) |  | `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName Target` |
| `0x68` | `m_paramName` | CUtlString |  | `MPropertySuppressField` |
| `0x70` | `m_param` | [AnimParamID](../modellib/AnimParamID.md) |  | `MPropertyAttrStateCallback` `MPropertyAttributeChoiceName VectorParameter` `MPropertyFriendlyName Parameter` |
| `0x74` | `m_bIsPosition` | bool |  | `MPropertyAttrStateCallback` `MPropertyFriendlyName Parameter is a Position` |
| `0x78` | `m_attachmentName` | CUtlString |  | `MPropertyAttributeChoiceName Attachment` `MPropertyFriendlyName Aim Attachment` |
| `0x80` | `m_blendMode` | [AimMatrixBlendMode](../animgraphlib/AimMatrixBlendMode.md) |  | `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName Blend Mode` |
| `0x88` | `m_boneMaskName` | CUtlString |  | `MPropertyAttrStateCallback` `MPropertyAttributeChoiceName BoneMask` `MPropertyFriendlyName Bone Mask` |
| `0x90` | `m_bResetBase` | bool |  | `MPropertyFriendlyName Reset Child` |
| `0x91` | `m_bLockWhenWaning` | bool |  | `MPropertyFriendlyName Lock Blend When Waning` |
| `0x92` | `m_bUseBiasAndClamp` | bool |  | `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName Use Bias + Clamp` |
| `0x94` | `m_flBiasAndClampYawOffset` | float32 |  | `MPropertyAttrStateCallback` `MPropertyFriendlyName Yaw Offset Angle` |
| `0x98` | `m_flBiasAndClampPitchOffset` | float32 |  | `MPropertyAttrStateCallback` `MPropertyFriendlyName Pitch Offset Angle` |
| `0x9c` | `m_biasAndClampBlendCurve` | [CBlendCurve](../animgraphlib/CBlendCurve.md) |  | `MPropertyAttrStateCallback` `MPropertyAttributeEditor AnimGraphBlendCurve()` `MPropertyFriendlyName Clamp Blend Curve` |
| `0xa8` | `m_damping` | [CAnimInputDamping](../animgraphlib/CAnimInputDamping.md) |  | `MPropertyFriendlyName Damping` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimGraphDoc_AimMatrixNode&quot;,
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
	&quot;m_sequenceName&quot;: &quot;&quot;,
	&quot;m_flMaxYawAngle&quot;: 45.000000,
	&quot;m_flMaxPitchAngle&quot;: 45.000000,
	&quot;m_target&quot;: &quot;LookTarget&quot;,
	&quot;m_paramName&quot;: &quot;&quot;,
	&quot;m_param&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_bIsPosition&quot;: false,
	&quot;m_attachmentName&quot;: &quot;&quot;,
	&quot;m_blendMode&quot;: &quot;AimMatrixBlendMode_Additive&quot;,
	&quot;m_boneMaskName&quot;: &quot;&quot;,
	&quot;m_bResetBase&quot;: true,
	&quot;m_bLockWhenWaning&quot;: true,
	&quot;m_bUseBiasAndClamp&quot;: false,
	&quot;m_flBiasAndClampYawOffset&quot;: 1.000000,
	&quot;m_flBiasAndClampPitchOffset&quot;: 1.000000,
	&quot;m_biasAndClampBlendCurve&quot;:
	{
		&quot;m_flControlPoint1&quot;: 0.000000,
		&quot;m_flControlPoint2&quot;: 1.000000
	},
	&quot;m_damping&quot;:
	{
		&quot;_class&quot;: &quot;CAnimInputDamping&quot;,
		&quot;m_speedFunction&quot;: &quot;NoDamping&quot;,
		&quot;m_fSpeedScale&quot;: 1.000000,
		&quot;m_fFallingSpeedScale&quot;: 1.000000
	}
}</pre>
</details>
