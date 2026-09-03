---
title: CCSPlayer_WeaponServices (server)
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSPlayer_WeaponServices

# CCSPlayer_WeaponServices

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Component attached to CCSPlayerPawn that manages the active weapon and weapon-switch timing for a CS2 player.

**Kind:** class · **Size:** 6272 bytes (`0x1880`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [CCSPlayer_WeaponServices (client)](../client/CCSPlayer_WeaponServices.md)

**Inherits from:** [CPlayer_WeaponServices](../server/CPlayer_WeaponServices.md)

**Relationships:**

```mermaid
classDiagram
    CPlayer_WeaponServices <|-- CCSPlayer_WeaponServices
    CPlayerPawnComponent <|-- CPlayer_WeaponServices
    CCSPlayer_WeaponServices *-- GameTime_t
    CCSPlayer_WeaponServices --> CBasePlayerWeapon
```

## Memory layout

20 fields (13 declared here, 7 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) | `MNotSaved` |
| `0x30` | `m_pComponentGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) |  |
| `0x48` | `m_hMyWeapons` | CNetworkUtlVectorBase< CHandle< [CBasePlayerWeapon](../server/CBasePlayerWeapon.md) > > | [CPlayer_WeaponServices](../server/CPlayer_WeaponServices.md) |  |
| `0x60` | `m_hActiveWeapon` | CHandle< [CBasePlayerWeapon](../server/CBasePlayerWeapon.md) > | [CPlayer_WeaponServices](../server/CPlayer_WeaponServices.md) |  |
| `0x64` | `m_hLastWeapon` | CHandle< [CBasePlayerWeapon](../server/CBasePlayerWeapon.md) > | [CPlayer_WeaponServices](../server/CPlayer_WeaponServices.md) |  |
| `0x68` | `m_iAmmo` | uint16[32] | [CPlayer_WeaponServices](../server/CPlayer_WeaponServices.md) |  |
| `0xa8` | `m_bPreventWeaponPickup` | bool | [CPlayer_WeaponServices](../server/CPlayer_WeaponServices.md) |  |
| `0xc0` | `m_flNextAttack` | [GameTime_t](../entity2/GameTime_t.md) |  | GameTime before which no weapon switch is permitted (e.g. after throwing a grenade). *Only sent to the owning player (LocalPlayerExclusive).* |
| `0xc4` | `m_hSavedWeapon` | CHandle< [CBasePlayerWeapon](../server/CBasePlayerWeapon.md) > |  |  |
| `0xc8` | `m_nTimeToMelee` | int32 |  |  |
| `0xcc` | `m_nTimeToSecondary` | int32 |  |  |
| `0xd0` | `m_nTimeToPrimary` | int32 |  |  |
| `0xd4` | `m_nTimeToSniperRifle` | int32 |  |  |
| `0xd8` | `m_bIsBeingGivenItem` | bool |  |  |
| `0xd9` | `m_bIsPickingUpItemWithUse` | bool |  |  |
| `0xda` | `m_bPickedUpWeapon` | bool |  |  |
| `0xdb` | `m_bDisableAutoDeploy` | bool |  |  |
| `0xdc` | `m_bIsPickingUpGroundWeapon` | bool |  |  |
| `0x1860` | `m_networkAnimTiming` | CNetworkUtlVectorBase< uint8 > |  | Byte array encoding animation transition timing for the active weapon, used to synchronise viewmodel animations across client and server. |
| `0x1878` | `m_bBlockInspectUntilNextGraphUpdate` | bool |  | True when the inspect animation is suppressed until the animation graph ticks again (prevents stutter). |
