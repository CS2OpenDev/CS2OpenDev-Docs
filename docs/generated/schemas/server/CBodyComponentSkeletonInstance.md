---
layout: default
title: CBodyComponentSkeletonInstance
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CBodyComponentSkeletonInstance

# CBodyComponentSkeletonInstance

**Kind:** class · **Size:** 1248 bytes (`0x4e0`) · **Align:** 255 · **Module:** server

**Inherits from:** [CBodyComponent](../server/CBodyComponent.md)

**Derived by:** [CBodyComponentBaseAnimGraph](../server/CBodyComponentBaseAnimGraph.md), [CBodyComponentBaseModelEntity](../server/CBodyComponentBaseModelEntity.md)

**Relationships:**

```mermaid
classDiagram
    CBodyComponent <|-- CBodyComponentSkeletonInstance
    CEntityComponent <|-- CBodyComponent
    CBodyComponentSkeletonInstance <|-- CBodyComponentBaseAnimGraph
    CBodyComponentSkeletonInstance <|-- CBodyComponentBaseModelEntity
    CBodyComponentSkeletonInstance *-- CSkeletonInstance
```

## Memory layout

3 fields (1 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_pSceneNode` | [CGameSceneNode](../server/CGameSceneNode.md)* | [CBodyComponent](../server/CBodyComponent.md) | `MNotSaved` |
| `0x48` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CBodyComponent](../server/CBodyComponent.md) | `MNotSaved` |
| `0x80` | `m_skeletonInstance` | [CSkeletonInstance](../server/CSkeletonInstance.md) |  |  |
