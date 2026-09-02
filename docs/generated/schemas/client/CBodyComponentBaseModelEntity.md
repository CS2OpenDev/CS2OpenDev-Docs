---
layout: default
title: CBodyComponentBaseModelEntity (client)
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CBodyComponentBaseModelEntity

# CBodyComponentBaseModelEntity

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 1296 bytes (`0x510`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [CBodyComponentBaseModelEntity (server)](../server/CBodyComponentBaseModelEntity.md)

**Inherits from:** [CBodyComponentSkeletonInstance](../client/CBodyComponentSkeletonInstance.md)

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
| `0x8` | `m_pSceneNode` | [CGameSceneNode](../client/CGameSceneNode.md)* | [CBodyComponent](../client/CBodyComponent.md) | `MNotSaved` |
| `0x48` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CBodyComponent](../client/CBodyComponent.md) | `MNotSaved` |
| `0x80` | `m_skeletonInstance` | [CSkeletonInstance](../client/CSkeletonInstance.md) | [CBodyComponentSkeletonInstance](../client/CBodyComponentSkeletonInstance.md) |  |
