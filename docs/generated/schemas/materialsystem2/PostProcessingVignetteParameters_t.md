---
layout: default
title: PostProcessingVignetteParameters_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [materialsystem2](../materialsystem2.md) / PostProcessingVignetteParameters_t

# PostProcessingVignetteParameters_t

**Kind:** class · **Size:** 36 bytes (`0x24`) · **Align:** 4 · **Module:** materialsystem2

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flVignetteStrength` | float32 |  |  |
| `0x4` | `m_vCenter` | Vector2D |  |  |
| `0xc` | `m_flRadius` | float32 |  |  |
| `0x10` | `m_flRoundness` | float32 |  |  |
| `0x14` | `m_flFeather` | float32 |  |  |
| `0x18` | `m_vColorTint` | Vector |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_flVignetteStrength&quot;: 0.000000,
	&quot;m_vCenter&quot;:
	[
		0.000000,
		0.000000
	],
	&quot;m_flRadius&quot;: 0.500000,
	&quot;m_flRoundness&quot;: 1.000000,
	&quot;m_flFeather&quot;: 0.500000,
	&quot;m_vColorTint&quot;:
	[
		1.000000,
		1.000000,
		1.000000
	]
}</pre>
</details>
