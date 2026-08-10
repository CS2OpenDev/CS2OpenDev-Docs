---
layout: default
title: IKSolverSettings_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / IKSolverSettings_t

# IKSolverSettings_t

**Kind:** class · **Size:** 12 bytes (`0xc`) · **Align:** 255 · **Module:** animgraphlib

**Relationships:**

```mermaid
classDiagram
    IKSolverSettings_t *-- IKSolverType
    IKSolverSettings_t *-- EIKEndEffectorRotationFixUpMode
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_SolverType` | [IKSolverType](../animgraphlib/IKSolverType.md) |  | `MPropertyAutoRebuildOnChange` `MPropertyFriendlyName Solver Type` |
| `0x4` | `m_nNumIterations` | int32 |  | `MPropertyAttrStateCallback` `MPropertyFriendlyName Num Iterations ` |
| `0x8` | `m_EndEffectorRotationFixUpMode` | [EIKEndEffectorRotationFixUpMode](../animgraphlib/EIKEndEffectorRotationFixUpMode.md) |  | `MPropertyFriendlyName End Effector Rotation Behaviour` |
