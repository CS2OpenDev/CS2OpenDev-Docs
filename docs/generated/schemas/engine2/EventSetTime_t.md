---
layout: default
title: EventSetTime_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [engine2](../engine2.md) / EventSetTime_t

# EventSetTime_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** n/a (unspecified) · **Module:** engine2

**Relationships:**

```mermaid
classDiagram
    EventSetTime_t *-- EngineLoopState_t
```

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_LoopState` | [EngineLoopState_t](../engine2/EngineLoopState_t.md) |  |  |
| `0x28` | `m_nClientOutputFrames` | int32 |  |  |
| `0x30` | `m_flRealTime` | float64 |  |  |
| `0x38` | `m_flRenderTime` | float64 |  |  |
| `0x40` | `m_flRenderFrameTime` | float64 |  |  |
| `0x48` | `m_flRenderFrameTimeUnbounded` | float64 |  |  |
| `0x50` | `m_flRenderFrameTimeUnscaled` | float64 |  |  |
| `0x58` | `m_flTickRemainder` | float64 |  |  |
