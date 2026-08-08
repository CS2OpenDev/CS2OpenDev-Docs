---
layout: default
title: SkeletonAnimCapture_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / SkeletonAnimCapture_t

# SkeletonAnimCapture_t

**Kind:** class · **Size:** 192 bytes (`0xc0`) · **Align:** 8 · **Module:** modellib

## Memory layout

10 fields (10 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nEntIndex` | CEntityIndex |  |  |
| `0x4` | `m_nEntParent` | CEntityIndex |  |  |
| `0x8` | `m_ImportedCollision` | CUtlVector< CEntityIndex > |  |  |
| `0x20` | `m_ModelName` | CUtlString |  |  |
| `0x28` | `m_CaptureName` | CUtlString |  |  |
| `0x30` | `m_ModelBindPose` | CUtlVector< [SkeletonAnimCapture_t](../modellib/SkeletonAnimCapture_t.md)::Bone_t > |  |  |
| `0x48` | `m_FeModelInitPose` | CUtlVector< [SkeletonAnimCapture_t](../modellib/SkeletonAnimCapture_t.md)::Bone_t > |  |  |
| `0x60` | `m_nFlexControllers` | int32 |  |  |
| `0x64` | `m_bPredicted` | bool |  |  |
| `0xa8` | `m_Frames` | CUtlVector< [SkeletonAnimCapture_t](../modellib/SkeletonAnimCapture_t.md)::Frame_t > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nEntIndex&quot;: -1,
	&quot;m_nEntParent&quot;: -1,
	&quot;m_ImportedCollision&quot;:
	[
	],
	&quot;m_ModelName&quot;: &quot;&quot;,
	&quot;m_CaptureName&quot;: &quot;&quot;,
	&quot;m_ModelBindPose&quot;:
	[
	],
	&quot;m_FeModelInitPose&quot;:
	[
	],
	&quot;m_nFlexControllers&quot;: 0,
	&quot;m_bPredicted&quot;: false,
	&quot;m_Frames&quot;:
	[
	]
}</pre>
</details>
