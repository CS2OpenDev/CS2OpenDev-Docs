---
layout: default
title: CSeqScaleSet
nav_exclude: true
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / CSeqScaleSet

# CSeqScaleSet

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 8 · **Module:** animationsystem

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sName` | CBufferString |  |  |
| `0x10` | `m_bRootOffset` | bool |  |  |
| `0x14` | `m_vRootOffset` | Vector |  |  |
| `0x20` | `m_nLocalBoneArray` | CUtlVector< int16 > |  |  |
| `0x38` | `m_flBoneScaleArray` | CUtlVector< float32 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sName&quot;: &quot;&quot;,
	&quot;m_bRootOffset&quot;: false,
	&quot;m_vRootOffset&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_nLocalBoneArray&quot;:
	[
	],
	&quot;m_flBoneScaleArray&quot;:
	[
	]
}</pre>
</details>
