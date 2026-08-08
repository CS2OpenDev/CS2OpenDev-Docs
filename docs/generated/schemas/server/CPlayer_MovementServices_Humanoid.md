---
layout: default
title: CPlayer_MovementServices_Humanoid
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CPlayer_MovementServices_Humanoid

# CPlayer_MovementServices_Humanoid

**Kind:** class · **Size:** 656 bytes (`0x290`) · **Align:** 255 · **Module:** server

**Inherits from:** [CPlayer_MovementServices](../server/CPlayer_MovementServices.md)

**Derived by:** [CCSPlayer_MovementServices](../server/CCSPlayer_MovementServices.md)

**Relationships:**

```mermaid
classDiagram
    CPlayer_MovementServices <|-- CPlayer_MovementServices_Humanoid
    CPlayerPawnComponent <|-- CPlayer_MovementServices
    CPlayer_MovementServices_Humanoid <|-- CCSPlayer_MovementServices
```

## Memory layout

27 fields (7 declared here, 20 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) | `MNotSaved` |
| `0x30` | `m_pComponentGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) |  |
| `0x48` | `m_nImpulse` | int32 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x50` | `m_nButtons` | [CInButtonState](../server/CInButtonState.md) | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) | `MNotSaved` |
| `0x70` | `m_nQueuedButtonDownMask` | uint64 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x78` | `m_nQueuedButtonChangeMask` | uint64 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x80` | `m_nButtonDoublePressed` | uint64 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x88` | `m_pButtonPressedCmdNumber` | uint32[64] | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) | `MNotSaved` |
| `0x188` | `m_nLastCommandNumberProcessed` | uint32 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) | `MNotSaved` |
| `0x190` | `m_nToggleButtonDownMask` | uint64 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x1a0` | `m_flCmdForwardMove` | float32 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x1a4` | `m_flCmdLeftMove` | float32 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x1a8` | `m_flCmdUpMove` | float32 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x1ac` | `m_flMaxspeed` | float32 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x1b0` | `m_arrForceSubtickMoveWhen` | float32[4] | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x1c0` | `m_flForwardMove` | float32 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x1c4` | `m_flLeftMove` | float32 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x1c8` | `m_flUpMove` | float32 | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x1cc` | `m_vecLastMovementImpulses` | Vector | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x240` | `m_vecOldViewAngles` | QAngle | [CPlayer_MovementServices](../server/CPlayer_MovementServices.md) |  |
| `0x258` | `m_flStepSoundTime` | float32 |  |  |
| `0x25c` | `m_flFallVelocity` | float32 |  |  |
| `0x260` | `m_groundNormal` | Vector |  | `MNotSaved` |
| `0x26c` | `m_flSurfaceFriction` | float32 |  |  |
| `0x270` | `m_surfaceProps` | CUtlStringToken |  | `MNotSaved` |
| `0x280` | `m_nStepside` | int32 |  |  |
| `0x284` | `m_vecSmoothedVelocity` | Vector |  |  |
