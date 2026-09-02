---
title: CHitReactUpdateNode
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CHitReactUpdateNode

# CHitReactUpdateNode

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 208 bytes (`0xd0`) · **Align:** 8 · **Module:** animgraphlib

**Inherits from:** [CUnaryUpdateNode](../animgraphlib/CUnaryUpdateNode.md)

**Relationships:**

```mermaid
classDiagram
    CUnaryUpdateNode <|-- CHitReactUpdateNode
    CAnimUpdateNodeBase <|-- CUnaryUpdateNode
    CHitReactUpdateNode *-- HitReactFixedSettings_t
    CHitReactUpdateNode *-- CAnimParamHandle
```

## Memory layout

12 fields (8 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_nodePath` | [CAnimNodePath](../animgraphlib/CAnimNodePath.md) | [CAnimUpdateNodeBase](../animgraphlib/CAnimUpdateNodeBase.md) |  |
| `0x48` | `m_networkMode` | [AnimNodeNetworkMode](../animgraphlib/AnimNodeNetworkMode.md) | [CAnimUpdateNodeBase](../animgraphlib/CAnimUpdateNodeBase.md) |  |
| `0x50` | `m_name` | CUtlString | [CAnimUpdateNodeBase](../animgraphlib/CAnimUpdateNodeBase.md) |  |
| `0x60` | `m_pChildNode` | [CAnimUpdateNodeRef](../animgraphlib/CAnimUpdateNodeRef.md) | [CUnaryUpdateNode](../animgraphlib/CUnaryUpdateNode.md) |  |
| `0x70` | `m_opFixedSettings` | [HitReactFixedSettings_t](../animgraphlib/HitReactFixedSettings_t.md) |  |  |
| `0xbc` | `m_triggerParam` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0xbe` | `m_hitBoneParam` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0xc0` | `m_hitOffsetParam` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0xc2` | `m_hitDirectionParam` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0xc4` | `m_hitStrengthParam` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0xc8` | `m_flMinDelayBetweenHits` | float32 |  |  |
| `0xcc` | `m_bResetChild` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CHitReactUpdateNode&quot;,
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
		&quot;m_nWeightListIndex&quot;: 0,
		&quot;m_nEffectedBoneCount&quot;: 0,
		&quot;m_flMaxImpactForce&quot;: 0.000000,
		&quot;m_flMinImpactForce&quot;: 0.000000,
		&quot;m_flWhipImpactScale&quot;: 0.000000,
		&quot;m_flCounterRotationScale&quot;: 0.000000,
		&quot;m_flDistanceFadeScale&quot;: 0.000000,
		&quot;m_flPropagationScale&quot;: 0.000000,
		&quot;m_flWhipDelay&quot;: 0.000000,
		&quot;m_flSpringStrength&quot;: 0.000000,
		&quot;m_flWhipSpringStrength&quot;: 0.000000,
		&quot;m_flMaxAngleRadians&quot;: 0.000000,
		&quot;m_nHipBoneIndex&quot;: 0,
		&quot;m_flHipBoneTranslationScale&quot;: 0.000000,
		&quot;m_flHipDipSpringStrength&quot;: 0.000000,
		&quot;m_flHipDipImpactScale&quot;: 0.000000,
		&quot;m_flHipDipDelay&quot;: 0.000000
	},
	&quot;m_triggerParam&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hitBoneParam&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hitOffsetParam&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hitDirectionParam&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hitStrengthParam&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_flMinDelayBetweenHits&quot;: 0.000000,
	&quot;m_bResetChild&quot;: false
}</pre>
</details>
