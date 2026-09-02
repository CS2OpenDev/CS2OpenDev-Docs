---
layout: default
title: CHitBox
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CHitBox

# CHitBox

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 112 bytes (`0x70`) · **Align:** 16 · **Module:** modellib

## Memory layout

13 fields (13 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString |  |  |
| `0x8` | `m_sSurfaceProperty` | CUtlString |  |  |
| `0x10` | `m_sBoneName` | CUtlString |  |  |
| `0x18` | `m_vMinBounds` | Vector |  |  |
| `0x24` | `m_vMaxBounds` | Vector |  |  |
| `0x30` | `m_flShapeRadius` | float32 |  |  |
| `0x34` | `m_nBoneNameHash` | uint32 |  |  |
| `0x38` | `m_nGroupId` | int32 |  |  |
| `0x3c` | `m_nShapeType` | uint8 |  |  |
| `0x3d` | `m_bTranslationOnly` | bool |  |  |
| `0x40` | `m_CRC` | uint32 |  |  |
| `0x44` | `m_cRenderColor` | Color |  |  |
| `0x48` | `m_nHitBoxIndex` | uint16 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_sSurfaceProperty&quot;: &quot;&quot;,
	&quot;m_sBoneName&quot;: &quot;&quot;,
	&quot;m_vMinBounds&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vMaxBounds&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_flShapeRadius&quot;: 0.000000,
	&quot;m_nBoneNameHash&quot;: 0,
	&quot;m_nGroupId&quot;: 0,
	&quot;m_nShapeType&quot;: 0,
	&quot;m_bTranslationOnly&quot;: false,
	&quot;m_CRC&quot;: 0,
	&quot;m_cRenderColor&quot;:
	[
		255,
		255,
		255
	],
	&quot;m_nHitBoxIndex&quot;: 0
}</pre>
</details>
