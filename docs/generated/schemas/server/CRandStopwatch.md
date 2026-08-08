---
layout: default
title: CRandStopwatch
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CRandStopwatch

# CRandStopwatch

**Kind:** class · **Size:** 20 bytes (`0x14`) · **Align:** 255 · **Module:** server

**Inherits from:** [CStopwatchBase](../server/CStopwatchBase.md)

**Relationships:**

```mermaid
classDiagram
    CStopwatchBase <|-- CRandStopwatch
    CSimpleSimTimer <|-- CStopwatchBase
```

## Memory layout

5 fields (2 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flNext` | [GameTime_t](../entity2/GameTime_t.md) | [CSimpleSimTimer](../server/CSimpleSimTimer.md) |  |
| `0x4` | `m_nWorldGroupId` | WorldGroupId_t | [CSimpleSimTimer](../server/CSimpleSimTimer.md) |  |
| `0x8` | `m_bIsRunning` | bool | [CStopwatchBase](../server/CStopwatchBase.md) |  |
| `0xc` | `m_flMinInterval` | float32 |  |  |
| `0x10` | `m_flMaxInterval` | float32 |  |  |
