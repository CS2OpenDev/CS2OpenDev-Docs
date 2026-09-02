---
layout: default
title: CAnimBone
nav_exclude: true
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / CAnimBone

# CAnimBone

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** animationsystem

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CBufferString |  |  |
| `0x10` | `m_parent` | int32 |  |  |
| `0x14` | `m_pos` | Vector |  |  |
| `0x20` | `m_quat` | QuaternionStorage |  |  |
| `0x30` | `m_scale` | float32 |  |  |
| `0x34` | `m_qAlignment` | QuaternionStorage |  |  |
| `0x44` | `m_flags` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_parent&quot;: 0,
	&quot;m_pos&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_quat&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		1.000000
	],
	&quot;m_scale&quot;: 1.000000,
	&quot;m_qAlignment&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		1.000000
	],
	&quot;m_flags&quot;: 0
}</pre>
</details>
