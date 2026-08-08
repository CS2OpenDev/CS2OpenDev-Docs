---
layout: default
title: CPlayer_ItemServices
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CPlayer_ItemServices

# CPlayer_ItemServices

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 255 · **Module:** server

**Inherits from:** [CPlayerPawnComponent](../server/CPlayerPawnComponent.md)

**Derived by:** [CCSPlayer_ItemServices](../server/CCSPlayer_ItemServices.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_ItemServices
    CPlayer_ItemServices <|-- CCSPlayer_ItemServices
```

## Memory layout

2 fields (0 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) | `MNotSaved` |
| `0x30` | `m_pComponentGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) |  |
