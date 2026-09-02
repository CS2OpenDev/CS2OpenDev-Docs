---
layout: default
title: SimpleConstraintSoundProfile
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / SimpleConstraintSoundProfile

# SimpleConstraintSoundProfile

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** server

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_flKeyPointMinSoundThreshold` | float32 |  |  |
| `0xc` | `m_flKeyPointMaxSoundThreshold` | float32 |  |  |
| `0x10` | `m_reversalSoundThresholdSmall` | float32 |  |  |
| `0x14` | `m_reversalSoundThresholdMedium` | float32 |  |  |
| `0x18` | `m_reversalSoundThresholdLarge` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;SimpleConstraintSoundProfile&quot;,
	&quot;m_flKeyPointMinSoundThreshold&quot;: 0.000000,
	&quot;m_flKeyPointMaxSoundThreshold&quot;: 0.000000,
	&quot;m_reversalSoundThresholdSmall&quot;: 0.000000,
	&quot;m_reversalSoundThresholdMedium&quot;: 0.000000,
	&quot;m_reversalSoundThresholdLarge&quot;: 0.000000
}</pre>
</details>
