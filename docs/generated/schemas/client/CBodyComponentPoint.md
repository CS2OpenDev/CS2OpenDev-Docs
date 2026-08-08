---
layout: default
title: CBodyComponentPoint
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CBodyComponentPoint

# CBodyComponentPoint

**Kind:** class · **Size:** 432 bytes (`0x1b0`) · **Align:** 255 · **Module:** client

**Inherits from:** [CBodyComponent](../client/CBodyComponent.md)

**Relationships:**

```mermaid
classDiagram
    CBodyComponent <|-- CBodyComponentPoint
    CEntityComponent <|-- CBodyComponent
    CBodyComponentPoint *-- CGameSceneNode
```

## Memory layout

3 fields (1 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_pSceneNode` | [CGameSceneNode](../client/CGameSceneNode.md)* | [CBodyComponent](../client/CBodyComponent.md) | `MNotSaved` |
| `0x48` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CBodyComponent](../client/CBodyComponent.md) | `MNotSaved` |
| `0x80` | `m_sceneNode` | [CGameSceneNode](../client/CGameSceneNode.md) |  |  |
