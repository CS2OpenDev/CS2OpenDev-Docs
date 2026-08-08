---
layout: default
title: CSimTimer
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CSimTimer

# CSimTimer

**Kind:** class · **Size:** 12 bytes (`0xc`) · **Align:** 255 · **Module:** server

**Inherits from:** [CSimpleSimTimer](../server/CSimpleSimTimer.md)

**Relationships:**

```mermaid
classDiagram
    CSimpleSimTimer <|-- CSimTimer
```

## Memory layout

3 fields (1 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flNext` | [GameTime_t](../entity2/GameTime_t.md) | [CSimpleSimTimer](../server/CSimpleSimTimer.md) |  |
| `0x4` | `m_nWorldGroupId` | WorldGroupId_t | [CSimpleSimTimer](../server/CSimpleSimTimer.md) |  |
| `0x8` | `m_flInterval` | float32 |  |  |
