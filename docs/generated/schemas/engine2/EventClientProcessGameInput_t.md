---
layout: default
title: EventClientProcessGameInput_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [engine2](../engine2.md) / EventClientProcessGameInput_t

# EventClientProcessGameInput_t

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 255 · **Module:** engine2

**Relationships:**

```mermaid
classDiagram
    EventClientProcessGameInput_t *-- EngineLoopState_t
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_LoopState` | [EngineLoopState_t](../engine2/EngineLoopState_t.md) |  |  |
| `0x28` | `m_flRealTime` | float32 |  |  |
| `0x2c` | `m_flFrameTime` | float32 |  |  |
