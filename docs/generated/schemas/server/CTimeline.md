---
title: CTimeline (server)
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CTimeline

# CTimeline

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 552 bytes (`0x228`) · **Align:** 8 · **Module:** server

**Twin:** [CTimeline (client)](../client/CTimeline.md)

**Inherits from:** [IntervalTimer](../server/IntervalTimer.md)

**Relationships:**

```mermaid
classDiagram
    IntervalTimer <|-- CTimeline
    CTimeline *-- TimelineCompression_t
```

## Memory layout

9 fields (7 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_timestamp` | [GameTime_t](../entity2/GameTime_t.md) | [IntervalTimer](../server/IntervalTimer.md) |  |
| `0xc` | `m_nWorldGroupId` | WorldGroupId_t | [IntervalTimer](../server/IntervalTimer.md) |  |
| `0x10` | `m_flValues` | float32[64] |  |  |
| `0x110` | `m_nValueCounts` | int32[64] |  |  |
| `0x210` | `m_nBucketCount` | int32 |  |  |
| `0x214` | `m_flInterval` | float32 |  |  |
| `0x218` | `m_flFinalValue` | float32 |  |  |
| `0x21c` | `m_nCompressionType` | [TimelineCompression_t](../server/TimelineCompression_t.md) |  |  |
| `0x220` | `m_bStopped` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>null</pre>
</details>
