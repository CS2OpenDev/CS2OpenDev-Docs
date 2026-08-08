---
layout: default
title: CBlendNodeInstanceData
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CBlendNodeInstanceData

# CBlendNodeInstanceData

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 4 · **Module:** animgraphlib

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_dampedValue` | float32 |  |  |
| `0x4` | `m_flCycle` | float32 |  |  |
| `0x8` | `m_flCycleZeroTime` | float32 |  |  |
| `0xc` | `m_flPlaybackRate` | float32 |  |  |
| `0x10` | `m_flBlendValue` | CAnimNetVar< float32 > |  |  |
| `0x1c` | `m_flDuration` | float32 |  |  |
| `0x20` | `m_resetCount` | CAnimNetVar< uint8 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_dampedValue&quot;: 0.000000,
	&quot;m_flCycle&quot;: 0.000000,
	&quot;m_flCycleZeroTime&quot;: 0.000000,
	&quot;m_flPlaybackRate&quot;: 1.000000,
	&quot;m_flBlendValue&quot;: 0.000000,
	&quot;m_flDuration&quot;: 1.000000,
	&quot;m_resetCount&quot;: 0
}</pre>
</details>
