---
layout: default
title: EventClientSimulate_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [engine2](../engine2.md) / EventClientSimulate_t

# EventClientSimulate_t

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 255 · **Module:** engine2

**Inherits from:** [EventSimulate_t](../engine2/EventSimulate_t.md)

**Relationships:**

```mermaid
classDiagram
    EventSimulate_t <|-- EventClientSimulate_t
```

## Memory layout

3 fields (0 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_LoopState` | [EngineLoopState_t](../engine2/EngineLoopState_t.md) | [EventSimulate_t](../engine2/EventSimulate_t.md) |  |
| `0x28` | `m_bFirstTick` | bool | [EventSimulate_t](../engine2/EventSimulate_t.md) |  |
| `0x29` | `m_bLastTick` | bool | [EventSimulate_t](../engine2/EventSimulate_t.md) |  |
