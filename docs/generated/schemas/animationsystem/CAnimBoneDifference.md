---
layout: default
title: CAnimBoneDifference
nav_exclude: true
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / CAnimBoneDifference

# CAnimBoneDifference

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** animationsystem

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CBufferString |  |  |
| `0x10` | `m_parent` | CBufferString |  |  |
| `0x20` | `m_posError` | Vector |  |  |
| `0x2c` | `m_bHasRotation` | bool |  |  |
| `0x2d` | `m_bHasMovement` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_parent&quot;: &quot;&quot;,
	&quot;m_posError&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_bHasRotation&quot;: false,
	&quot;m_bHasMovement&quot;: false
}</pre>
</details>
