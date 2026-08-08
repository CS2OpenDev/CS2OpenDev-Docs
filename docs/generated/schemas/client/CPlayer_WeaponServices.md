---
layout: default
title: CPlayer_WeaponServices
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CPlayer_WeaponServices

# CPlayer_WeaponServices

**Kind:** class · **Size:** 168 bytes (`0xa8`) · **Align:** 255 · **Module:** client

**Inherits from:** [CPlayerPawnComponent](../server/CPlayerPawnComponent.md)

**Derived by:** [CCSPlayer_WeaponServices](../client/CCSPlayer_WeaponServices.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_WeaponServices
    CPlayer_WeaponServices <|-- CCSPlayer_WeaponServices
    CPlayer_WeaponServices --> C_BasePlayerWeapon
```

## Memory layout

6 fields (4 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) | `MNotSaved` |
| `0x30` | `m_pComponentGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) |  |
| `0x48` | `m_hMyWeapons` | C_NetworkUtlVectorBase< CHandle< [C_BasePlayerWeapon](../client/C_BasePlayerWeapon.md) > > |  |  |
| `0x60` | `m_hActiveWeapon` | CHandle< [C_BasePlayerWeapon](../client/C_BasePlayerWeapon.md) > |  |  |
| `0x64` | `m_hLastWeapon` | CHandle< [C_BasePlayerWeapon](../client/C_BasePlayerWeapon.md) > |  |  |
| `0x68` | `m_iAmmo` | uint16[32] |  |  |
