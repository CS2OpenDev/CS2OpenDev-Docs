---
title: CPlayer_MovementServices (client)
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / CPlayer_MovementServices

# CPlayer_MovementServices

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Base movement/input component: decoded button input and per-command move intent shared by all player pawns.

**Kind:** class · **Size:** 600 bytes (`0x258`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [CPlayer_MovementServices (server)](../server/CPlayer_MovementServices.md)

**Inherits from:** [CPlayerPawnComponent](../server/CPlayerPawnComponent.md)

**Derived by:** [CCSObserver_MovementServices](../client/CCSObserver_MovementServices.md), [CPlayer_MovementServices_Humanoid](../client/CPlayer_MovementServices_Humanoid.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_MovementServices
    CPlayer_MovementServices <|-- CCSObserver_MovementServices
    CPlayer_MovementServices <|-- CPlayer_MovementServices_Humanoid
    CPlayer_MovementServices *-- CInButtonState
```

## Memory layout

20 fields (18 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) | `MNotSaved` |
| `0x30` | `m_pComponentGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) |  |
| `0x48` | `m_nImpulse` | int32 |  | Pending impulse command number (e.g. `impulse 100` flashlight). |
| `0x50` | `m_nButtons` | [CInButtonState](../server/CInButtonState.md) |  | Bitmask of currently-pressed input buttons (IN_ATTACK, IN_JUMP, IN_DUCK, …). `MNotSaved` |
| `0x70` | `m_nQueuedButtonDownMask` | uint64 |  |  |
| `0x78` | `m_nQueuedButtonChangeMask` | uint64 |  |  |
| `0x80` | `m_nButtonDoublePressed` | uint64 |  |  |
| `0x88` | `m_pButtonPressedCmdNumber` | uint32[64] |  | `MNotSaved` |
| `0x188` | `m_nLastCommandNumberProcessed` | uint32 |  | `MNotSaved` |
| `0x190` | `m_nToggleButtonDownMask` | uint64 |  |  |
| `0x1a0` | `m_flCmdForwardMove` | float32 |  |  |
| `0x1a4` | `m_flCmdLeftMove` | float32 |  |  |
| `0x1a8` | `m_flCmdUpMove` | float32 |  |  |
| `0x1ac` | `m_flMaxspeed` | float32 |  | Current maximum ground movement speed (units/second). |
| `0x1b0` | `m_arrForceSubtickMoveWhen` | float32[4] |  |  |
| `0x1c0` | `m_flForwardMove` | float32 |  | Decoded forward/back movement axis for the current user command. |
| `0x1c4` | `m_flLeftMove` | float32 |  | Decoded strafe (left/right) movement axis for the current user command. |
| `0x1c8` | `m_flUpMove` | float32 |  | Decoded vertical movement axis (swim / ladder) for the current user command. |
| `0x1cc` | `m_vecLastMovementImpulses` | Vector |  |  |
| `0x240` | `m_vecOldViewAngles` | QAngle |  |  |
