---
layout: default
title: CAimCameraUpdateNode
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CAimCameraUpdateNode

# CAimCameraUpdateNode

**Kind:** class · **Size:** 184 bytes (`0xb8`) · **Align:** 8 · **Module:** animgraphlib

**Inherits from:** [CUnaryUpdateNode](../animgraphlib/CUnaryUpdateNode.md)

**Relationships:**

```mermaid
classDiagram
    CUnaryUpdateNode <|-- CAimCameraUpdateNode
    CAnimUpdateNodeBase <|-- CUnaryUpdateNode
    CAimCameraUpdateNode *-- CAnimParamHandle
    CAimCameraUpdateNode *-- AimCameraOpFixedSettings_t
```

## Memory layout

12 fields (8 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_nodePath` | [CAnimNodePath](../animgraphlib/CAnimNodePath.md) | [CAnimUpdateNodeBase](../animgraphlib/CAnimUpdateNodeBase.md) |  |
| `0x48` | `m_networkMode` | [AnimNodeNetworkMode](../animgraphlib/AnimNodeNetworkMode.md) | [CAnimUpdateNodeBase](../animgraphlib/CAnimUpdateNodeBase.md) |  |
| `0x50` | `m_name` | CUtlString | [CAnimUpdateNodeBase](../animgraphlib/CAnimUpdateNodeBase.md) |  |
| `0x60` | `m_pChildNode` | [CAnimUpdateNodeRef](../animgraphlib/CAnimUpdateNodeRef.md) | [CUnaryUpdateNode](../animgraphlib/CUnaryUpdateNode.md) |  |
| `0x70` | `m_hParameterPosition` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x72` | `m_hParameterOrientation` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x74` | `m_hParameterPelvisOffset` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x76` | `m_hParameterCameraOnly` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x78` | `m_hParameterWeaponDepenetrationDistance` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x7a` | `m_hParameterWeaponDepenetrationDelta` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x7c` | `m_hParameterCameraClearanceDistance` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x80` | `m_opFixedSettings` | [AimCameraOpFixedSettings_t](../animgraphlib/AimCameraOpFixedSettings_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAimCameraUpdateNode&quot;,
	&quot;m_nodePath&quot;:
	{
		&quot;m_path&quot;:
		[
			{
				&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
			},
			{
				&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
			},
			{
				&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
			},
			{
				&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
			},
			{
				&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
			},
			{
				&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
			},
			{
				&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
			},
			{
				&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
			},
			{
				&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
			},
			{
				&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
			},
			{
				&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
			}
		],
		&quot;m_nCount&quot;: 0
	},
	&quot;m_networkMode&quot;: &quot;ServerAuthoritative&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_pChildNode&quot;:
	{
		&quot;m_nodeIndex&quot;: -1
	},
	&quot;m_hParameterPosition&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hParameterOrientation&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hParameterPelvisOffset&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hParameterCameraOnly&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hParameterWeaponDepenetrationDistance&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hParameterWeaponDepenetrationDelta&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hParameterCameraClearanceDistance&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_opFixedSettings&quot;:
	{
		&quot;m_nChainIndex&quot;: -1,
		&quot;m_nCameraJointIndex&quot;: -1,
		&quot;m_nPelvisJointIndex&quot;: -1,
		&quot;m_nClavicleLeftJointIndex&quot;: -1,
		&quot;m_nClavicleRightJointIndex&quot;: -1,
		&quot;m_nDepenetrationJointIndex&quot;: -1,
		&quot;m_propJoints&quot;:
		[
		]
	}
}</pre>
</details>
