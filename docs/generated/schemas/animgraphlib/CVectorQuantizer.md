---
layout: default
title: CVectorQuantizer
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CVectorQuantizer

# CVectorQuantizer

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animgraphlib

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_centroidVectors` | CUtlVector< float32 > |  |  |
| `0x18` | `m_nCentroids` | int32 |  |  |
| `0x1c` | `m_nDimensions` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_centroidVectors&quot;:
	[
	],
	&quot;m_nCentroids&quot;: 0,
	&quot;m_nDimensions&quot;: 0
}</pre>
</details>
