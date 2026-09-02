---
title: CSeqBoneMaskList
module: animationsystem
kind: class
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / CSeqBoneMaskList

# CSeqBoneMaskList

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 8 · **Module:** animationsystem

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sName` | CBufferString |  |  |
| `0x10` | `m_nLocalBoneArray` | CUtlVector< int16 > |  |  |
| `0x28` | `m_flBoneWeightArray` | CUtlVector< float32 > |  |  |
| `0x40` | `m_flDefaultMorphCtrlWeight` | float32 |  |  |
| `0x48` | `m_morphCtrlWeightArray` | CUtlVector< std::pair< CBufferString, float32 > > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sName&quot;: &quot;&quot;,
	&quot;m_nLocalBoneArray&quot;:
	[
	],
	&quot;m_flBoneWeightArray&quot;:
	[
	],
	&quot;m_flDefaultMorphCtrlWeight&quot;: 1.000000,
	&quot;m_morphCtrlWeightArray&quot;:
	[
	]
}</pre>
</details>
