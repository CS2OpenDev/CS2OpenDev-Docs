---
layout: default
title: CFootDefinition
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CFootDefinition

# CFootDefinition

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** modellib

## Memory layout

9 fields (9 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString |  |  |
| `0x8` | `m_ankleBoneName` | CUtlString |  |  |
| `0x10` | `m_toeBoneName` | CUtlString |  |  |
| `0x18` | `m_vBallOffset` | Vector |  |  |
| `0x24` | `m_vHeelOffset` | Vector |  |  |
| `0x30` | `m_flFootLength` | float32 |  |  |
| `0x34` | `m_flBindPoseDirectionMS` | float32 |  |  |
| `0x38` | `m_flTraceHeight` | float32 |  |  |
| `0x3c` | `m_flTraceRadius` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_ankleBoneName&quot;: &quot;&quot;,
	&quot;m_toeBoneName&quot;: &quot;&quot;,
	&quot;m_vBallOffset&quot;:
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
	&quot;m_flFootLength&quot;: -1.000000,
	&quot;m_flBindPoseDirectionMS&quot;: 0.000000,
	&quot;m_flTraceHeight&quot;: -1.000000,
	&quot;m_flTraceRadius&quot;: -1.000000
}</pre>
</details>
