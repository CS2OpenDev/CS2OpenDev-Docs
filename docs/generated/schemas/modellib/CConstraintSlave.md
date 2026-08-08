---
layout: default
title: CConstraintSlave
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CConstraintSlave

# CConstraintSlave

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 16 · **Module:** modellib

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_qBaseOrientation` | Quaternion |  |  |
| `0x10` | `m_vBasePosition` | Vector |  |  |
| `0x1c` | `m_nBoneHash` | uint32 |  |  |
| `0x20` | `m_flWeight` | float32 |  |  |
| `0x28` | `m_sName` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_qBaseOrientation&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		1.000000
	],
	&quot;m_vBasePosition&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_nBoneHash&quot;: 0,
	&quot;m_flWeight&quot;: 0.000000,
	&quot;m_sName&quot;: &quot;&quot;
}</pre>
</details>
