---
layout: default
title: EventServerPostSimulate_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [engine2](../engine2.md) / EventServerPostSimulate_t

# EventServerPostSimulate_t

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 255 · **Module:** engine2

**Inherits from:** [EventSimulate_t](../engine2/EventSimulate_t.md)

**Relationships:**

```mermaid
classDiagram
    EventSimulate_t <|-- EventServerPostSimulate_t
```

## Memory layout

4 fields (1 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_LoopState` | [EngineLoopState_t](../engine2/EngineLoopState_t.md) | [EventSimulate_t](../engine2/EventSimulate_t.md) |  |
| `0x28` | `m_bFirstTick` | bool | [EventSimulate_t](../engine2/EventSimulate_t.md) |  |
| `0x29` | `m_bLastTick` | bool | [EventSimulate_t](../engine2/EventSimulate_t.md) |  |
| `0x30` | `m_bLastTickBeforeClientUpdate` | bool |  |  |
