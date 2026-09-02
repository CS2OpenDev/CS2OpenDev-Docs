---
layout: default
title: DynamicMeshDeformParams_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / DynamicMeshDeformParams_t

# DynamicMeshDeformParams_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 12 bytes (`0xc`) · **Align:** 4 · **Module:** modellib

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flTensionCompressScale` | float32 |  |  |
| `0x4` | `m_flTensionStretchScale` | float32 |  |  |
| `0x8` | `m_bRecomputeSmoothNormalsAfterAnimation` | bool |  |  |
| `0x9` | `m_bComputeDynamicMeshTensionAfterAnimation` | bool |  |  |
| `0xa` | `m_bSmoothNormalsAcrossUvSeams` | bool |  |  |
| `0xb` | `m_bEnableEyeBulgeDeformation` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_flTensionCompressScale&quot;: 0.000000,
	&quot;m_flTensionStretchScale&quot;: 0.000000,
	&quot;m_bRecomputeSmoothNormalsAfterAnimation&quot;: false,
	&quot;m_bComputeDynamicMeshTensionAfterAnimation&quot;: false,
	&quot;m_bSmoothNormalsAcrossUvSeams&quot;: false,
	&quot;m_bEnableEyeBulgeDeformation&quot;: false
}</pre>
</details>
