---
layout: default
title: RenderHairStrandInfo_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / RenderHairStrandInfo_t

# RenderHairStrandInfo_t

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** 4 · **Module:** modellib

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nGuideHairIndices_nSurfaceTriIndex` | uint32[2] |  |  |
| `0x8` | `m_vGuideBary_vBaseBary` | uint16[4] |  |  |
| `0x10` | `m_vRootOffset_flLengthScale` | uint16[4] |  |  |
| `0x18` | `m_nPackedBaseUv` | uint16[2] |  |  |
| `0x1c` | `m_nPackedSurfaceNormalOs` | uint32 |  |  |
| `0x20` | `m_nPackedSurfaceTangentOs` | uint32 |  |  |
| `0x24` | `m_nDataOffset_Segments` | uint32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nGuideHairIndices_nSurfaceTriIndex&quot;:
	[
		0,
		0
	],
	&quot;m_vGuideBary_vBaseBary&quot;:
	[
		0,
		0,
		0,
		0
	],
	&quot;m_vRootOffset_flLengthScale&quot;:
	[
		0,
		0,
		0,
		0
	],
	&quot;m_nPackedBaseUv&quot;:
	[
		0,
		0
	],
	&quot;m_nPackedSurfaceNormalOs&quot;: 0,
	&quot;m_nPackedSurfaceTangentOs&quot;: 0,
	&quot;m_nDataOffset_Segments&quot;: 0
}</pre>
</details>
