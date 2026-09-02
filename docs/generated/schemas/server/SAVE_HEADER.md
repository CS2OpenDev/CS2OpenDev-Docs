---
layout: default
title: SAVE_HEADER
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / SAVE_HEADER

# SAVE_HEADER

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 16 · **Module:** server

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_saveId` | int32 |  |  |
| `0x4` | `m_version` | int32 |  |  |
| `0x8` | `m_nConnectionCount` | int32 |  |  |
| `0xc` | `m_nMapVersion` | int32 |  |  |
| `0x10` | `m_sSpawnGroupName` | CUtlString |  |  |
| `0x20` | `m_vecWorldOffset` | matrix3x4a_t |  |  |
| `0x50` | `m_flSaveTime` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_saveId&quot;: 0,
	&quot;m_version&quot;: 0,
	&quot;m_nConnectionCount&quot;: 0,
	&quot;m_nMapVersion&quot;: 0,
	&quot;m_sSpawnGroupName&quot;: &quot;&quot;,
	&quot;m_vecWorldOffset&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_flSaveTime&quot;: 0.000000
}</pre>
</details>
