---
layout: default
title: CConstraintTarget
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CConstraintTarget

# CConstraintTarget

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 16 · **Module:** modellib

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x20` | `m_qOffset` | Quaternion |  |  |
| `0x30` | `m_vOffset` | Vector |  |  |
| `0x3c` | `m_nBoneHash` | uint32 |  |  |
| `0x40` | `m_sName` | CUtlString |  |  |
| `0x48` | `m_flWeight` | float32 |  |  |
| `0x59` | `m_bIsAttachment` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_qOffset&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		1.000000
	],
	&quot;m_vOffset&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_nBoneHash&quot;: 0,
	&quot;m_sName&quot;: &quot;&quot;,
	&quot;m_flWeight&quot;: 0.000000,
	&quot;m_bIsAttachment&quot;: false
}</pre>
</details>
