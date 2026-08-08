---
layout: default
title: CNmBlendSpace2D
nav_exclude: true
---

[Schemas](../../schemas.md) / [animdoclib](../animdoclib.md) / CNmBlendSpace2D

# CNmBlendSpace2D

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 8 · **Module:** animdoclib

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_pointNames` | CUtlVector< CUtlString > |  | `MPropertyAutoExpandSelf` `MPropertyResizable` |
| `0x18` | `m_points` | CUtlVector< Vector2D > |  | `MPropertyAutoExpandSelf` `MPropertyResizable` |
| `0x30` | `m_indices` | CUtlVector< uint8 > |  | `MPropertySuppressField` |
| `0x48` | `m_hullIndices` | CUtlVector< uint8 > |  | `MPropertySuppressField` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_pointNames&quot;:
	[
	],
	&quot;m_points&quot;:
	[
	],
	&quot;m_indices&quot;:
	[
	],
	&quot;m_hullIndices&quot;:
	[
	]
}</pre>
</details>
