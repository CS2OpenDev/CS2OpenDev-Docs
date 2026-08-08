---
layout: default
title: IPhysAggregateInstance
nav_exclude: true
---

[Schemas](../../schemas.md) / [vphysics2](../vphysics2.md) / IPhysAggregateInstance

# IPhysAggregateInstance

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 255 · **Module:** vphysics2

**Inherits from:** [IPhysicsBodyList](../vphysics2/IPhysicsBodyList.md)

**Relationships:**

```mermaid
classDiagram
    IPhysicsBodyList <|-- IPhysAggregateInstance
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_pSkeleton` | void* |  |  |
| `0x10` | `m_bIsAxisAligned` | bool |  |  |
