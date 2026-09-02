---
layout: default
title: CBtActionCombatPositioning
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CBtActionCombatPositioning

# CBtActionCombatPositioning

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 176 bytes (`0xb0`) · **Align:** n/a (unspecified) · **Module:** server

**Inherits from:** [CBtNode](../server/CBtNode.md)

**Relationships:**

```mermaid
classDiagram
    CBtNode <|-- CBtActionCombatPositioning
    CBtActionCombatPositioning *-- CountdownTimer
```

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x68` | `m_szSensorInputKey` | CUtlString |  |  |
| `0x80` | `m_szIsAttackingKey` | CUtlString |  |  |
| `0x88` | `m_ActionTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0xa0` | `m_bCrouching` | bool |  |  |
