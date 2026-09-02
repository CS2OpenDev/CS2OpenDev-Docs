---
layout: default
title: CNmRootMotionData
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmRootMotionData

# CNmRootMotionData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 16 · **Module:** animlib

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_transforms` | CUtlVector< CTransform > |  |  |
| `0x18` | `m_nNumFrames` | int32 |  |  |
| `0x1c` | `m_flAverageLinearVelocity` | float32 |  |  |
| `0x20` | `m_flAverageAngularVelocityRadians` | float32 |  |  |
| `0x30` | `m_totalDelta` | CTransform |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_transforms&quot;:
	[
	],
	&quot;m_nNumFrames&quot;: 0,
	&quot;m_flAverageLinearVelocity&quot;: 0.000000,
	&quot;m_flAverageAngularVelocityRadians&quot;: 0.000000,
	&quot;m_totalDelta&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000
	]
}</pre>
</details>
