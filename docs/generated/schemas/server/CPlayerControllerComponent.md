---
layout: default
title: CPlayerControllerComponent
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CPlayerControllerComponent

# CPlayerControllerComponent

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 255 · **Module:** server

**Derived by:** [CCSPlayerController_ActionTrackingServices](../server/CCSPlayerController_ActionTrackingServices.md), [CCSPlayerController_DamageServices](../server/CCSPlayerController_DamageServices.md), [CCSPlayerController_InGameMoneyServices](../server/CCSPlayerController_InGameMoneyServices.md), [CCSPlayerController_InventoryServices](../server/CCSPlayerController_InventoryServices.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerControllerComponent <|-- CCSPlayerController_ActionTrackingServices
    CPlayerControllerComponent <|-- CCSPlayerController_DamageServices
    CPlayerControllerComponent <|-- CCSPlayerController_InGameMoneyServices
    CPlayerControllerComponent <|-- CCSPlayerController_InventoryServices
    CPlayerControllerComponent *-- CNetworkVarChainer
```

## Memory layout

1 fields (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) |  | `MNotSaved` |
