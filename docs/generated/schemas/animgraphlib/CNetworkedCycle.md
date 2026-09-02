---
title: CNetworkedCycle
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CNetworkedCycle

# CNetworkedCycle

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 52 bytes (`0x34`) · **Align:** 4 · **Module:** animgraphlib

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flCycleUnclamped` | float32 |  |  |
| `0x4` | `m_flPrevCycleUnclamped` | float32 |  |  |
| `0x10` | `m_flCyclesPerSecond` | CAnimNetVar< float32 > |  |  |
| `0x1c` | `m_flCycleZeroTime` | CAnimNetVar< float32 > |  |  |
| `0x28` | `m_resetCount` | CAnimNetVar< uint8 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_flCycleUnclamped&quot;: 0.000000,
	&quot;m_flPrevCycleUnclamped&quot;: 0.000000,
	&quot;m_flCyclesPerSecond&quot;: 1.000000,
	&quot;m_flCycleZeroTime&quot;: 0.000000,
	&quot;m_resetCount&quot;: 0
}</pre>
</details>
