---
title: CAnimationLayer
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CAnimationLayer

# CAnimationLayer

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 76 bytes (`0x4c`) · **Align:** 4 · **Module:** animgraphlib

## Memory layout

11 fields (11 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_hSequence` | CAnimNetVar< int32 > |  |  |
| `0xc` | `m_flPrevCycle` | float32 |  |  |
| `0x10` | `m_flCycle` | CAnimNetVar< float32 > |  |  |
| `0x1c` | `m_flWeight` | CAnimNetVar< float32 > |  |  |
| `0x28` | `m_nOrder` | CAnimNetVar< int32 > |  |  |
| `0x34` | `m_bLooping` | bool |  |  |
| `0x38` | `m_nFlags` | int32 |  |  |
| `0x3c` | `m_bSequenceFinished` | bool |  |  |
| `0x40` | `m_flKillRate` | float32 |  |  |
| `0x44` | `m_flKillDelay` | float32 |  |  |
| `0x48` | `m_nPriority` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_hSequence&quot;: 0,
	&quot;m_flPrevCycle&quot;: 0.000000,
	&quot;m_flCycle&quot;: 0.000000,
	&quot;m_flWeight&quot;: 0.000000,
	&quot;m_nOrder&quot;: 12,
	&quot;m_bLooping&quot;: false,
	&quot;m_nFlags&quot;: 0,
	&quot;m_bSequenceFinished&quot;: false,
	&quot;m_flKillRate&quot;: 100.000000,
	&quot;m_flKillDelay&quot;: 0.000000,
	&quot;m_nPriority&quot;: 0
}</pre>
</details>
