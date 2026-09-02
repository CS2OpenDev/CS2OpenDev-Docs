---
layout: default
title: CModelState (client)
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CModelState

# CModelState

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 688 bytes (`0x2b0`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [CModelState (server)](../server/CModelState.md)

**Relationships:**

```mermaid
classDiagram
    CModelState *-- InfoForResourceTypeCModel
    CModelState --> IPhysAggregateInstance
```

## Memory layout

14 fields (14 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0xa0` | `m_hModel` | CStrongHandle< [InfoForResourceTypeCModel](../resourcesystem/InfoForResourceTypeCModel.md) > |  |  |
| `0xa8` | `m_ModelName` | CUtlSymbolLarge |  |  |
| `0xe0` | `m_pVPhysicsAggregate` | [IPhysAggregateInstance](../vphysics2/IPhysAggregateInstance.md)* |  | `MPhysPtr` |
| `0xe8` | `m_flRootBoneOffset_x` | float32 |  |  |
| `0xec` | `m_flRootBoneOffset_y` | float32 |  |  |
| `0xf0` | `m_flRootBoneOffset_z` | float32 |  |  |
| `0xf4` | `m_nRootBoneOffsetResetSerialNumber` | uint8 |  |  |
| `0x110` | `m_bClientClothCreationSuppressed` | bool |  |  |
| `0x200` | `m_nAnimStateNoInterpSerialNumber` | uint8 |  |  |
| `0x208` | `m_MeshGroupMask` | uint64 |  |  |
| `0x258` | `m_nBodyGroupChoices` | C_NetworkUtlVectorBase< int32 > |  |  |
| `0x2a2` | `m_nIdealMotionType` | int8 |  |  |
| `0x2a3` | `m_nForceLOD` | int8 |  |  |
| `0x2a4` | `m_nClothUpdateFlags` | int8 |  |  |
