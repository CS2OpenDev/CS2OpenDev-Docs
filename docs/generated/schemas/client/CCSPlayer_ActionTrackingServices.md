---
title: CCSPlayer_ActionTrackingServices (client)
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / CCSPlayer_ActionTrackingServices

# CCSPlayer_ActionTrackingServices

> Source: **Build 26144732** · 2026-10-22 · `windows-x86_64` · schema `0.12.0`

Component tracking scoring-relevant actions: weapon purchases and hostage rescue status.

**Kind:** class · **Size:** 416 bytes (`0x1a0`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [CCSPlayer_ActionTrackingServices (server)](../server/CCSPlayer_ActionTrackingServices.md)

**Inherits from:** [CPlayerPawnComponent](../server/CPlayerPawnComponent.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CCSPlayer_ActionTrackingServices
    CCSPlayer_ActionTrackingServices --> C_BasePlayerWeapon
    CCSPlayer_ActionTrackingServices *-- WeaponPurchaseTracker_t
```

## Memory layout

7 fields (5 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) | `MNotSaved` |
| `0x30` | `m_pComponentGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) |  |
| `0x48` | `m_hLastWeaponBeforeC4AutoSwitch` | CHandle< [C_BasePlayerWeapon](../client/C_BasePlayerWeapon.md) > |  |  |
| `0x4c` | `m_bIsRescuing` | bool |  | True while the player is escorting a hostage to the rescue zone. |
| `0x50` | `m_weaponPurchasesThisMatch` | [WeaponPurchaseTracker_t](../client/WeaponPurchaseTracker_t.md) |  | WeaponPurchaseTracker_t recording which weapons were bought during the match (used for match-stats). |
| `0xc0` | `m_weaponPurchasesThisRound` | [WeaponPurchaseTracker_t](../client/WeaponPurchaseTracker_t.md) |  | WeaponPurchaseTracker_t recording which weapons were bought this round (used for in-round stats and economy tracking). |
| `0x130` | `m_weaponCarryOverIntoThisRound` | [WeaponPurchaseTracker_t](../client/WeaponPurchaseTracker_t.md) |  |  |
