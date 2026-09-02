---
title: CBtNodeConditionInactive
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CBtNodeConditionInactive

# CBtNodeConditionInactive

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 152 bytes (`0x98`) · **Align:** n/a (unspecified) · **Module:** server

**Inherits from:** [CBtNodeCondition](../server/CBtNodeCondition.md)

**Relationships:**

```mermaid
classDiagram
    CBtNodeCondition <|-- CBtNodeConditionInactive
    CBtNodeDecorator <|-- CBtNodeCondition
    CBtNode <|-- CBtNodeDecorator
    CBtNodeConditionInactive *-- CountdownTimer
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x58` | `m_bNegated` | bool | [CBtNodeCondition](../server/CBtNodeCondition.md) |  |
| `0x78` | `m_flRoundStartThresholdSeconds` | float32 |  |  |
| `0x7c` | `m_flSensorInactivityThresholdSeconds` | float32 |  |  |
| `0x80` | `m_SensorInactivityTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
