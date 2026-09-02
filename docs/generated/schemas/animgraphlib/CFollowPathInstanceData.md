---
layout: default
title: CFollowPathInstanceData
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CFollowPathInstanceData

# CFollowPathInstanceData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 36 bytes (`0x24`) · **Align:** 4 · **Module:** animgraphlib

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_xLastPredictedTransformsDeltas` | CRelativeArray< CMotionTransform > |  |  |
| `0x8` | `m_dampedTurnValue` | float32 |  |  |
| `0xc` | `m_flTurnAmount` | float32 |  |  |
| `0x10` | `m_flPredictionScale` | CAnimNetVar< float32 > |  |  |
| `0x1c` | `m_flLastPathTime` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_xLastPredictedTransformsDeltas&quot;:
	[
	],
	&quot;m_dampedTurnValue&quot;: 0.000000,
	&quot;m_flTurnAmount&quot;: 0.000000,
	&quot;m_flPredictionScale&quot;: 1.000000,
	&quot;m_flLastPathTime&quot;: 0.000000
}</pre>
</details>
