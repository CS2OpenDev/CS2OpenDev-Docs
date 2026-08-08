---
layout: default
title: PermModelInfo_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / PermModelInfo_t

# PermModelInfo_t

**Kind:** class · **Size:** 88 bytes (`0x58`) · **Align:** 8 · **Module:** modellib

## Memory layout

10 fields (10 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nFlags` | uint32 |  |  |
| `0x4` | `m_vHullMin` | Vector |  |  |
| `0x10` | `m_vHullMax` | Vector |  |  |
| `0x1c` | `m_vViewMin` | Vector |  |  |
| `0x28` | `m_vViewMax` | Vector |  |  |
| `0x34` | `m_flMass` | float32 |  |  |
| `0x38` | `m_vEyePosition` | Vector |  |  |
| `0x44` | `m_flMaxEyeDeflection` | float32 |  |  |
| `0x48` | `m_sSurfaceProperty` | CUtlString |  |  |
| `0x50` | `m_keyValueText` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nFlags&quot;: 0,
	&quot;m_vHullMin&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vHullMax&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vViewMin&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vViewMax&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_flMass&quot;: 0.000000,
	&quot;m_vEyePosition&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_flMaxEyeDeflection&quot;: 0.000000,
	&quot;m_sSurfaceProperty&quot;: &quot;&quot;,
	&quot;m_keyValueText&quot;: &quot;&quot;
}</pre>
</details>
