---
layout: default
title: CGameSceneNode (server)
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CGameSceneNode

# CGameSceneNode

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 272 bytes (`0x110`) · **Align:** 16 · **Module:** server

**Twin:** [CGameSceneNode (client)](../client/CGameSceneNode.md)

**Derived by:** [CSkeletonInstance](../server/CSkeletonInstance.md)

**Relationships:**

```mermaid
classDiagram
    CGameSceneNode <|-- CSkeletonInstance
    CGameSceneNode --> CEntityInstance
    CGameSceneNode *-- CGameSceneNodeHandle
    CGameSceneNode *-- CNetworkOriginCellCoordQuantizedVector
```

## Memory layout

31 fields (31 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` bit 0 | `m_bBoneMergeFlex` | bitfield:1 |  | `MNotSaved` |
| `0x0` bit 1 | `m_bDirtyBoneMergeBoneToRoot` | bitfield:1 |  | `MNotSaved` |
| `0x0` bit 2 | `m_bDirtyBoneMergeInfo` | bitfield:1 |  | `MNotSaved` |
| `0x0` bit 3 | `m_bDirtyHierarchy` | bitfield:1 |  | `MNotSaved` |
| `0x0` bit 4 | `m_bNetworkedAnglesChanged` | bitfield:1 |  | `MNotSaved` |
| `0x0` bit 5 | `m_bNetworkedPositionChanged` | bitfield:1 |  | `MNotSaved` |
| `0x0` bit 6 | `m_bNetworkedScaleChanged` | bitfield:1 |  | `MNotSaved` |
| `0x0` bit 7 | `m_bWillBeCallingPostDataUpdate` | bitfield:1 |  | `MNotSaved` |
| `0x0` bits 8..9 | `m_nLatchAbsOrigin` | bitfield:2 |  | `MNotSaved` |
| `0x10` | `m_nodeToWorld` | CTransformWS |  | `MNotSaved` |
| `0x30` | `m_pOwner` | [CEntityInstance](../entity2/CEntityInstance.md)* |  | `MNotSaved` |
| `0x38` | `m_pParent` | [CGameSceneNode](../server/CGameSceneNode.md)* |  | `MNotSaved` |
| `0x40` | `m_pChild` | [CGameSceneNode](../server/CGameSceneNode.md)* |  | `MNotSaved` |
| `0x48` | `m_pNextSibling` | [CGameSceneNode](../server/CGameSceneNode.md)* |  | `MNotSaved` |
| `0x70` | `m_hParent` | [CGameSceneNodeHandle](../server/CGameSceneNodeHandle.md) |  |  |
| `0x80` | `m_vecOrigin` | [CNetworkOriginCellCoordQuantizedVector](../server/CNetworkOriginCellCoordQuantizedVector.md) |  |  |
| `0xb8` | `m_angRotation` | QAngle |  |  |
| `0xc4` | `m_flScale` | float32 |  |  |
| `0xc8` | `m_vecAbsOrigin` | VectorWS |  |  |
| `0xd4` | `m_angAbsRotation` | QAngle |  |  |
| `0xe0` | `m_flAbsScale` | float32 |  |  |
| `0xe4` | `m_nParentAttachmentOrBone` | int16 |  | `MNotSaved` |
| `0xe6` | `m_bDebugAbsOriginChanges` | bool |  | `MNotSaved` |
| `0xe7` | `m_bDormant` | bool |  |  |
| `0xe8` | `m_bForceParentToBeNetworked` | bool |  |  |
| `0xeb` | `m_nHierarchicalDepth` | uint8 |  | `MNotSaved` |
| `0xec` | `m_nHierarchyType` | uint8 |  | `MNotSaved` |
| `0xed` | `m_nDoNotSetAnimTimeInInvalidatePhysicsCount` | uint8 |  | `MNotSaved` |
| `0xf0` | `m_name` | CUtlStringToken |  |  |
| `0x104` | `m_hierarchyAttachName` | CUtlStringToken |  |  |
| `0x108` | `m_flClientLocalScale` | float32 |  |  |
