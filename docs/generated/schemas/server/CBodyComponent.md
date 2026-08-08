---
layout: default
title: CBodyComponent
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CBodyComponent

# CBodyComponent

**Kind:** class · **Size:** 120 bytes (`0x78`) · **Align:** 255 · **Module:** server

**Inherits from:** [CEntityComponent](../entity2/CEntityComponent.md)

**Derived by:** [CBodyComponentPoint](../server/CBodyComponentPoint.md), [CBodyComponentSkeletonInstance](../server/CBodyComponentSkeletonInstance.md)

**Relationships:**

```mermaid
classDiagram
    CEntityComponent <|-- CBodyComponent
    CBodyComponent <|-- CBodyComponentPoint
    CBodyComponent <|-- CBodyComponentSkeletonInstance
    CBodyComponent --> CGameSceneNode
    CBodyComponent *-- CNetworkVarChainer
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_pSceneNode` | [CGameSceneNode](../server/CGameSceneNode.md)* |  | `MNotSaved` |
| `0x48` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) |  | `MNotSaved` |

<details><summary>KV3 class defaults</summary>

<pre>{
}</pre>
</details>
