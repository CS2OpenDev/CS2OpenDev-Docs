---
title: CBodyComponentPoint (server)
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CBodyComponentPoint

# CBodyComponentPoint

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 400 bytes (`0x190`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [CBodyComponentPoint (client)](../client/CBodyComponentPoint.md)

**Inherits from:** [CBodyComponent](../server/CBodyComponent.md)

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
| `0x8` | `m_pSceneNode` | [CGameSceneNode](../server/CGameSceneNode.md)* | [CBodyComponent](../server/CBodyComponent.md) | `MNotSaved` |
| `0x48` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CBodyComponent](../server/CBodyComponent.md) | `MNotSaved` |
| `0x80` | `m_sceneNode` | [CGameSceneNode](../server/CGameSceneNode.md) |  |  |
