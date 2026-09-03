---
title: CStopwatch
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CStopwatch

# CStopwatch

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** n/a (unspecified) · **Module:** server

**Inherits from:** [CStopwatchBase](../server/CStopwatchBase.md)

**Relationships:**

```mermaid
classDiagram
    CStopwatchBase <|-- CStopwatch
    CSimpleSimTimer <|-- CStopwatchBase
```

## Memory layout

4 fields (1 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flNext` | [GameTime_t](../entity2/GameTime_t.md) | [CSimpleSimTimer](../server/CSimpleSimTimer.md) |  |
| `0x4` | `m_nWorldGroupId` | WorldGroupId_t | [CSimpleSimTimer](../server/CSimpleSimTimer.md) |  |
| `0x8` | `m_bIsRunning` | bool | [CStopwatchBase](../server/CStopwatchBase.md) |  |
| `0xc` | `m_flInterval` | float32 |  |  |
