---
layout: default
title: CountdownTimer
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CountdownTimer

# CountdownTimer

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** client

**Relationships:**

```mermaid
classDiagram
    CountdownTimer *-- GameTime_t
```

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_duration` | float32 |  |  |
| `0xc` | `m_timestamp` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x10` | `m_timescale` | float32 |  |  |
| `0x14` | `m_nWorldGroupId` | WorldGroupId_t |  |  |

<details><summary>KV3 class defaults</summary>

<pre>null</pre>
</details>
