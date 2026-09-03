---
title: CBodyComponentBaseModelEntity (server)
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CBodyComponentBaseModelEntity

# CBodyComponentBaseModelEntity

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 1248 bytes (`0x4e0`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [CBodyComponentBaseModelEntity (client)](../client/CBodyComponentBaseModelEntity.md)

**Inherits from:** [CBodyComponentSkeletonInstance](../server/CBodyComponentSkeletonInstance.md)

**Relationships:**

```mermaid
classDiagram
    CBodyComponentSkeletonInstance <|-- CBodyComponentBaseModelEntity
    CBodyComponent <|-- CBodyComponentSkeletonInstance
    CEntityComponent <|-- CBodyComponent
```

## Memory layout

3 fields (0 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_pSceneNode` | [CGameSceneNode](../server/CGameSceneNode.md)* | [CBodyComponent](../server/CBodyComponent.md) | `MNotSaved` |
| `0x48` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CBodyComponent](../server/CBodyComponent.md) | `MNotSaved` |
| `0x80` | `m_skeletonInstance` | [CSkeletonInstance](../server/CSkeletonInstance.md) | [CBodyComponentSkeletonInstance](../server/CBodyComponentSkeletonInstance.md) |  |
