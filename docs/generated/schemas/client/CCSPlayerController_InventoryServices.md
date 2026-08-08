---
layout: default
title: CCSPlayerController_InventoryServices
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CCSPlayerController_InventoryServices

# CCSPlayerController_InventoryServices

Loadout and persona component of CCSPlayerController: equipped items, music kit, rank, and public-profile data.


**Kind:** class · **Size:** 240 bytes (`0xf0`) · **Align:** 255 · **Module:** client

**Inherits from:** [CPlayerControllerComponent](../server/CPlayerControllerComponent.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerControllerComponent <|-- CCSPlayerController_InventoryServices
    CCSPlayerController_InventoryServices *-- MedalRank_t
    CCSPlayerController_InventoryServices *-- ServerAuthoritativeWeaponSlot_t
```

## Memory layout

10 fields (9 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerControllerComponent](../server/CPlayerControllerComponent.md) | `MNotSaved` |
| `0x40` | `m_vecNetworkableLoadout` | CUtlVector< [CCSPlayerController_InventoryServices](../client/CCSPlayerController_InventoryServices.md)::NetworkedLoadoutSlot_t > |  | Networked loadout — the item/skin occupying each equipped weapon slot. |
| `0x58` | `m_unMusicID` | uint16 |  | Item id of the equipped music kit. |
| `0x5c` | `m_rank` | [MedalRank_t](../!GlobalTypes/MedalRank_t.md)[6] |  | Competitive rank / medal ids, indexed per game mode. |
| `0x74` | `m_nPersonaDataPublicLevel` | int32 |  | Public profile (Steam persona) level. |
| `0x78` | `m_nPersonaDataPublicCommendsLeader` | int32 |  |  |
| `0x7c` | `m_nPersonaDataPublicCommendsTeacher` | int32 |  |  |
| `0x80` | `m_nPersonaDataPublicCommendsFriendly` | int32 |  |  |
| `0x84` | `m_nPersonaDataXpTrailLevel` | int32 |  |  |
| `0x88` | `m_vecServerAuthoritativeWeaponSlots` | C_UtlVectorEmbeddedNetworkVar< [ServerAuthoritativeWeaponSlot_t](../client/ServerAuthoritativeWeaponSlot_t.md) > |  |  |
