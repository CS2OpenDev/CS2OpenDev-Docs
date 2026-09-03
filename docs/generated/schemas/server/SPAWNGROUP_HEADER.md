---
title: SPAWNGROUP_HEADER
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / SPAWNGROUP_HEADER

# SPAWNGROUP_HEADER

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 16 · **Module:** server

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sGroupName` | CUtlString |  |  |
| `0x8` | `m_sEntityLumpName` | CUtlString |  |  |
| `0x10` | `m_vecWorldOffset` | matrix3x4a_t |  |  |
| `0x40` | `m_bClientSpawnGroup` | bool |  |  |
| `0x41` | `m_bSuppressAllEntities` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sGroupName&quot;: &quot;&quot;,
	&quot;m_sEntityLumpName&quot;: &quot;&quot;,
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
	&quot;m_bClientSpawnGroup&quot;: false,
	&quot;m_bSuppressAllEntities&quot;: false
}</pre>
</details>
