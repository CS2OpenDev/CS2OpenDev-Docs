---
layout: default
title: CAnimGraphDoc_FollowTargetNode
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_FollowTargetNode

# CAnimGraphDoc_FollowTargetNode

**Kind:** class · **Size:** 128 bytes (`0x80`) · **Align:** 8 · **Module:** animgraphdoclib

**Inherits from:** [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md)

**Metadata:** `MPropertyFriendlyName Follow Target`

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_Node <|-- CAnimGraphDoc_FollowTargetNode
    CAnimGraphDoc_FollowTargetNode *-- CAnimGraphDoc_NodeConnection
    CAnimGraphDoc_FollowTargetNode *-- IKTargetSettings_t
```

## Memory layout

9 fields (4 declared here, 5 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x20` | `m_sName` | CUtlString | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Name` `MPropertySortPriority 100` |
| `0x28` | `m_vecPosition` | Vector2D | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x30` | `m_nNodeID` | [AnimNodeID](../modellib/AnimNodeID.md) | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x34` | `m_bDebugThisNode` | bool | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Debug This Node` `MPropertyGroupName Debug` `MPropertySortPriority -100` |
| `0x38` | `m_networkMode` | [AnimNodeNetworkMode](../!GlobalTypes/AnimNodeNetworkMode.md) | [CAnimGraphDoc_Node](../animgraphdoclib/CAnimGraphDoc_Node.md) | `MPropertyFriendlyName Network Mode` `MPropertySortPriority -110` |
| `0x40` | `m_inputConnection` | [CAnimGraphDoc_NodeConnection](../animgraphdoclib/CAnimGraphDoc_NodeConnection.md) |  | `MPropertySuppressField` |
| `0x48` | `m_boneName` | CUtlString |  | `MPropertyAttributeChoiceName Bone` `MPropertyFriendlyName Bone` |
| `0x50` | `m_TargetSettings` | [IKTargetSettings_t](../animgraphlib/IKTargetSettings_t.md) |  | `MPropertyAutoExpandSelf` `MPropertyFriendlyName Target Settings` |
| `0x78` | `m_bMatchTargetOrientation` | bool |  | `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName Match Target Orientation` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimGraphDoc_FollowTargetNode&quot;,
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
	&quot;m_boneName&quot;: &quot;&quot;,
	&quot;m_TargetSettings&quot;:
	{
		&quot;m_TargetSource&quot;: &quot;Bone&quot;,
		&quot;m_Bone&quot;:
		{
			&quot;m_Name&quot;: &quot;&quot;
		},
		&quot;m_AnimgraphParameterNamePosition&quot;:
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		&quot;m_AnimgraphParameterNameOrientation&quot;:
		{
			&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
		},
		&quot;m_TargetCoordSystem&quot;: &quot;World Space&quot;
	},
	&quot;m_bMatchTargetOrientation&quot;: false
}</pre>
</details>
