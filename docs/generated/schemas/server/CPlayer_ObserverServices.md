---
title: CPlayer_ObserverServices (server)
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CPlayer_ObserverServices

# CPlayer_ObserverServices

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 88 bytes (`0x58`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [CPlayer_ObserverServices (client)](../client/CPlayer_ObserverServices.md)

**Inherits from:** [CPlayerPawnComponent](../server/CPlayerPawnComponent.md)

**Derived by:** [CCSObserver_ObserverServices](../server/CCSObserver_ObserverServices.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_ObserverServices
    CPlayer_ObserverServices <|-- CCSObserver_ObserverServices
    CPlayer_ObserverServices --> CBaseEntity
    CPlayer_ObserverServices *-- ObserverMode_t
```

## Memory layout

6 fields (4 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) | `MNotSaved` |
| `0x30` | `m_pComponentGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) |  |
| `0x48` | `m_iObserverMode` | uint8 |  |  |
| `0x4c` | `m_hObserverTarget` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x50` | `m_iObserverLastMode` | [ObserverMode_t](../server/ObserverMode_t.md) |  |  |
| `0x54` | `m_bForcedObserverMode` | bool |  |  |
