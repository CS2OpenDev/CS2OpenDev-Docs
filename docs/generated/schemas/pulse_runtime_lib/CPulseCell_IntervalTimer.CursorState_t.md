---
layout: default
title: "CPulseCell_IntervalTimer::CursorState_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / CPulseCell_IntervalTimer::CursorState_t

# CPulseCell_IntervalTimer::CursorState_t

**Kind:** class · **Size:** 20 bytes (`0x14`) · **Align:** 4 · **Module:** pulse_runtime_lib

**Relationships:**

```mermaid
classDiagram
    "CPulseCell_IntervalTimer::CursorState_t" *-- GameTime_t
```

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_StartTime` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x4` | `m_EndTime` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x8` | `m_flWaitInterval` | float32 |  |  |
| `0xc` | `m_flWaitIntervalHigh` | float32 |  |  |
| `0x10` | `m_bCompleteOnNextWake` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_StartTime&quot;: null,
	&quot;m_EndTime&quot;: null,
	&quot;m_flWaitInterval&quot;: 0.000000,
	&quot;m_flWaitIntervalHigh&quot;: 0.000000,
	&quot;m_bCompleteOnNextWake&quot;: false
}</pre>
</details>
