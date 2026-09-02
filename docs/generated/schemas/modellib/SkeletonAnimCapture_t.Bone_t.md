---
layout: default
title: "SkeletonAnimCapture_t::Bone_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / SkeletonAnimCapture_t::Bone_t

# SkeletonAnimCapture_t::Bone_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 16 · **Module:** modellib

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_Name` | CUtlString |  |  |
| `0x10` | `m_BindPose` | CTransform |  |  |
| `0x30` | `m_nParent` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_Name&quot;: &quot;&quot;,
	&quot;m_BindPose&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_nParent&quot;: -1
}</pre>
</details>
