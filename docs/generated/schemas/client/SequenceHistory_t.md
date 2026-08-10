---
layout: default
title: SequenceHistory_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / SequenceHistory_t

# SequenceHistory_t

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 255 · **Module:** client

**Relationships:**

```mermaid
classDiagram
    SequenceHistory_t *-- HSequence
    SequenceHistory_t *-- GameTime_t
    SequenceHistory_t *-- AnimLoopMode_t
```

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_hSequence` | [HSequence](../animationsystem/HSequence.md) |  |  |
| `0x4` | `m_flSeqStartTime` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x8` | `m_flSeqFixedCycle` | float32 |  |  |
| `0xc` | `m_nSeqLoopMode` | [AnimLoopMode_t](../server/AnimLoopMode_t.md) |  |  |
| `0x10` | `m_flPlaybackRate` | float32 |  |  |
| `0x14` | `m_flCyclesPerSecond` | float32 |  |  |
