---
layout: default
title: ModelSkeletonData_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / ModelSkeletonData_t

# ModelSkeletonData_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 168 bytes (`0xa8`) · **Align:** 8 · **Module:** modellib

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_boneName` | CUtlVector< CUtlString > |  |  |
| `0x18` | `m_nParent` | CUtlVector< int16 > |  |  |
| `0x30` | `m_boneSphere` | CUtlVector< float32 > |  |  |
| `0x48` | `m_nFlag` | CUtlVector< uint32 > |  |  |
| `0x60` | `m_bonePosParent` | CUtlVector< Vector > |  |  |
| `0x78` | `m_boneRotParent` | CUtlVector< QuaternionStorage > |  |  |
| `0x90` | `m_boneScaleParent` | CUtlVector< float32 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_boneName&quot;:
	[
	],
	&quot;m_nParent&quot;:
	[
	],
	&quot;m_boneSphere&quot;:
	[
	],
	&quot;m_nFlag&quot;:
	[
	],
	&quot;m_bonePosParent&quot;:
	[
	],
	&quot;m_boneRotParent&quot;:
	[
	],
	&quot;m_boneScaleParent&quot;:
	[
	]
}</pre>
</details>
