---
title: CCSPlayer_HostageServices (client)
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / CCSPlayer_HostageServices

# CCSPlayer_HostageServices

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Component tracking whether this player is currently carrying a hostage.

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [CCSPlayer_HostageServices (server)](../server/CCSPlayer_HostageServices.md)

**Inherits from:** [CPlayerPawnComponent](../server/CPlayerPawnComponent.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CCSPlayer_HostageServices
    CCSPlayer_HostageServices --> C_BaseEntity
```

## Memory layout

4 fields (2 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) | `MNotSaved` |
| `0x30` | `m_pComponentGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) |  |
| `0x48` | `m_hCarriedHostage` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > |  | CHandle to the CHostage entity currently being carried by this player (INVALID_EHANDLE if none). |
| `0x4c` | `m_hCarriedHostageProp` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > |  | CHandle to the ragdoll/prop entity representing the carried hostage visually. |
