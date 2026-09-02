---
layout: default
title: CSimpleSimTimer
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CSimpleSimTimer

# CSimpleSimTimer

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 8 bytes (`0x8`) · **Align:** n/a (unspecified) · **Module:** server

**Derived by:** [CRandSimTimer](../server/CRandSimTimer.md), [CSimTimer](../server/CSimTimer.md), [CStopwatchBase](../server/CStopwatchBase.md)

**Relationships:**

```mermaid
classDiagram
    CSimpleSimTimer <|-- CRandSimTimer
    CSimpleSimTimer <|-- CSimTimer
    CSimpleSimTimer <|-- CStopwatchBase
    CSimpleSimTimer *-- GameTime_t
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flNext` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x4` | `m_nWorldGroupId` | WorldGroupId_t |  |  |
