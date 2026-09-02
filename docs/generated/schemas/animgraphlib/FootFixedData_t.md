---
layout: default
title: FootFixedData_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / FootFixedData_t

# FootFixedData_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 16 · **Module:** animgraphlib

## Memory layout

11 fields (11 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_vToeOffset` | VectorAligned |  |  |
| `0x10` | `m_vHeelOffset` | VectorAligned |  |  |
| `0x20` | `m_nTargetBoneIndex` | int32 |  |  |
| `0x24` | `m_nAnkleBoneIndex` | int32 |  |  |
| `0x28` | `m_nIKAnchorBoneIndex` | int32 |  |  |
| `0x2c` | `m_ikChainIndex` | int32 |  |  |
| `0x30` | `m_flMaxIKLength` | float32 |  |  |
| `0x34` | `m_nFootIndex` | int32 |  |  |
| `0x38` | `m_nTagIndex` | int32 |  |  |
| `0x3c` | `m_flMaxRotationLeft` | float32 |  |  |
| `0x40` | `m_flMaxRotationRight` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_vToeOffset&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vHeelOffset&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_nTargetBoneIndex&quot;: -1,
	&quot;m_nAnkleBoneIndex&quot;: -1,
	&quot;m_nIKAnchorBoneIndex&quot;: -1,
	&quot;m_ikChainIndex&quot;: -1,
	&quot;m_flMaxIKLength&quot;: -1.000000,
	&quot;m_nFootIndex&quot;: -1,
	&quot;m_nTagIndex&quot;: -1,
	&quot;m_flMaxRotationLeft&quot;: 90.000000,
	&quot;m_flMaxRotationRight&quot;: 90.000000
}</pre>
</details>
