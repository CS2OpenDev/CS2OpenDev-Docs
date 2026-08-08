---
layout: default
title: CAnimMotorUpdaterBase
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CAnimMotorUpdaterBase

# CAnimMotorUpdaterBase

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 255 · **Module:** animgraphlib

**Derived by:** [CPathAnimMotorUpdaterBase](../animgraphlib/CPathAnimMotorUpdaterBase.md), [CPlayerInputAnimMotorUpdater](../animgraphlib/CPlayerInputAnimMotorUpdater.md)

**Relationships:**

```mermaid
classDiagram
    CAnimMotorUpdaterBase <|-- CPathAnimMotorUpdaterBase
    CAnimMotorUpdaterBase <|-- CPlayerInputAnimMotorUpdater
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x10` | `m_name` | CUtlString |  |  |
| `0x18` | `m_bDefault` | bool |  |  |
