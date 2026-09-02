---
title: CAimMatrixUpdateNode
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CAimMatrixUpdateNode

# CAimMatrixUpdateNode

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 384 bytes (`0x180`) · **Align:** 16 · **Module:** animgraphlib

**Inherits from:** [CUnaryUpdateNode](../animgraphlib/CUnaryUpdateNode.md)

**Relationships:**

```mermaid
classDiagram
    CUnaryUpdateNode <|-- CAimMatrixUpdateNode
    CAnimUpdateNodeBase <|-- CUnaryUpdateNode
    CAimMatrixUpdateNode *-- AimMatrixOpFixedSettings_t
    CAimMatrixUpdateNode *-- AnimVectorSource
    CAimMatrixUpdateNode *-- CAnimParamHandle
    CAimMatrixUpdateNode *-- HSequence
```

## Memory layout

10 fields (6 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_nodePath` | [CAnimNodePath](../animgraphlib/CAnimNodePath.md) | [CAnimUpdateNodeBase](../animgraphlib/CAnimUpdateNodeBase.md) |  |
| `0x48` | `m_networkMode` | [AnimNodeNetworkMode](../animgraphlib/AnimNodeNetworkMode.md) | [CAnimUpdateNodeBase](../animgraphlib/CAnimUpdateNodeBase.md) |  |
| `0x50` | `m_name` | CUtlString | [CAnimUpdateNodeBase](../animgraphlib/CAnimUpdateNodeBase.md) |  |
| `0x60` | `m_pChildNode` | [CAnimUpdateNodeRef](../animgraphlib/CAnimUpdateNodeRef.md) | [CUnaryUpdateNode](../animgraphlib/CUnaryUpdateNode.md) |  |
| `0x70` | `m_opFixedSettings` | [AimMatrixOpFixedSettings_t](../animgraphlib/AimMatrixOpFixedSettings_t.md) |  |  |
| `0x168` | `m_target` | [AnimVectorSource](../animgraphlib/AnimVectorSource.md) |  |  |
| `0x16c` | `m_paramIndex` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x170` | `m_hSequence` | [HSequence](../animationsystem/HSequence.md) |  |  |
| `0x174` | `m_bResetChild` | bool |  |  |
| `0x175` | `m_bLockWhenWaning` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAimMatrixUpdateNode&quot;,
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
	&quot;m_opFixedSettings&quot;:
	{
		&quot;m_attachment&quot;:
		{
			&quot;m_influenceRotations&quot;:
			[
				[
					0.000000,
					0.000000,
					0.000000,
					0.000000
				],
				[
					0.000000,
					0.000000,
					0.000000,
					0.000000
				],
				[
					0.000000,
					0.000000,
					0.000000,
					0.000000
				]
			],
			&quot;m_influenceOffsets&quot;:
			[
				[
					0.000000,
					0.000000,
					0.000000
				],
				[
					0.000000,
					0.000000,
					0.000000
				],
				[
					0.000000,
					0.000000,
					0.000000
				]
			],
			&quot;m_influenceIndices&quot;:
			[
				0,
				0,
				0
			],
			&quot;m_influenceWeights&quot;:
			[
				0.000000,
				0.000000,
				0.000000
			],
			&quot;m_numInfluences&quot;: 0
		},
		&quot;m_damping&quot;:
		{
			&quot;_class&quot;: &quot;CAnimInputDamping&quot;,
			&quot;m_speedFunction&quot;: &quot;NoDamping&quot;,
			&quot;m_fSpeedScale&quot;: 1.000000,
			&quot;m_fFallingSpeedScale&quot;: 1.000000
		},
		&quot;m_poseCacheHandles&quot;:
		[
			{
				&quot;m_nIndex&quot;: 65535,
				&quot;m_eType&quot;: &quot;POSETYPE_INVALID&quot;
			},
			{
				&quot;m_nIndex&quot;: 65535,
				&quot;m_eType&quot;: &quot;POSETYPE_INVALID&quot;
			},
			{
				&quot;m_nIndex&quot;: 65535,
				&quot;m_eType&quot;: &quot;POSETYPE_INVALID&quot;
			},
			{
				&quot;m_nIndex&quot;: 65535,
				&quot;m_eType&quot;: &quot;POSETYPE_INVALID&quot;
			},
			{
				&quot;m_nIndex&quot;: 65535,
				&quot;m_eType&quot;: &quot;POSETYPE_INVALID&quot;
			},
			{
				&quot;m_nIndex&quot;: 65535,
				&quot;m_eType&quot;: &quot;POSETYPE_INVALID&quot;
			},
			{
				&quot;m_nIndex&quot;: 65535,
				&quot;m_eType&quot;: &quot;POSETYPE_INVALID&quot;
			},
			{
				&quot;m_nIndex&quot;: 65535,
				&quot;m_eType&quot;: &quot;POSETYPE_INVALID&quot;
			},
			{
				&quot;m_nIndex&quot;: 65535,
				&quot;m_eType&quot;: &quot;POSETYPE_INVALID&quot;
			},
			{
				&quot;m_nIndex&quot;: 65535,
				&quot;m_eType&quot;: &quot;POSETYPE_INVALID&quot;
			}
		],
		&quot;m_eBlendMode&quot;: &quot;AimMatrixBlendMode_None&quot;,
		&quot;m_flMaxYawAngle&quot;: 45.000000,
		&quot;m_flMaxPitchAngle&quot;: 45.000000,
		&quot;m_nSequenceMaxFrame&quot;: 0,
		&quot;m_nBoneMaskIndex&quot;: -1,
		&quot;m_bTargetIsPosition&quot;: true,
		&quot;m_bUseBiasAndClamp&quot;: false,
		&quot;m_flBiasAndClampYawOffset&quot;: 1.000000,
		&quot;m_flBiasAndClampPitchOffset&quot;: 1.000000,
		&quot;m_biasAndClampBlendCurve&quot;:
		{
			&quot;m_flControlPoint1&quot;: 0.000000,
			&quot;m_flControlPoint2&quot;: 1.000000
		}
	},
	&quot;m_target&quot;: &quot;MoveDirection&quot;,
	&quot;m_paramIndex&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hSequence&quot;: -1,
	&quot;m_bResetChild&quot;: false,
	&quot;m_bLockWhenWaning&quot;: false
}</pre>
</details>
