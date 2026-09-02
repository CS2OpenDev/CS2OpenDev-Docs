---
title: CCSPlayer_BulletServices (client)
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / CCSPlayer_BulletServices

# CCSPlayer_BulletServices

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Component tracking bullet-hit statistics registered on the server side.

**Kind:** class · **Size:** 168 bytes (`0xa8`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [CCSPlayer_BulletServices (server)](../server/CCSPlayer_BulletServices.md)

**Inherits from:** [CPlayerPawnComponent](../server/CPlayerPawnComponent.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CCSPlayer_BulletServices
```

## Memory layout

3 fields (1 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) | `MNotSaved` |
| `0x30` | `m_pComponentGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) |  |
| `0x48` | `m_totalHitsOnServer` | int32 |  | Cumulative number of bullet hits this player has registered on the server this round. |
