---
layout: default
title: CNmBoneWeightList
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmBoneWeightList

# CNmBoneWeightList

**Kind:** class · **Size:** 272 bytes (`0x110`) · **Align:** 8 · **Module:** animlib

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_skeletonName` | CResourceName |  |  |
| `0xe0` | `m_boneIDs` | CUtlVector< CGlobalSymbol > |  |  |
| `0xf8` | `m_weights` | CUtlVector< float32 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_skeletonName&quot;: &quot;&quot;,
	&quot;m_boneIDs&quot;:
	[
	],
	&quot;m_weights&quot;:
	[
	]
}</pre>
</details>
