---
title: CCSPlayer_CameraServices (client)
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / CCSPlayer_CameraServices

# CCSPlayer_CameraServices

> Source: **Build 26281801** · 2026-10-28 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 848 bytes (`0x350`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [CCSPlayer_CameraServices (server)](../server/CCSPlayer_CameraServices.md)

**Inherits from:** [CCSPlayerBase_CameraServices](../client/CCSPlayerBase_CameraServices.md)

**Relationships:**

```mermaid
classDiagram
    CCSPlayerBase_CameraServices <|-- CCSPlayer_CameraServices
    CPlayer_CameraServices <|-- CCSPlayerBase_CameraServices
    CPlayerPawnComponent <|-- CPlayer_CameraServices
    CCSPlayer_CameraServices --> C_PointDeathcamBounds
```

## Memory layout

32 fields (4 declared here, 28 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) | `MNotSaved` |
| `0x30` | `m_pComponentGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) |  |
| `0x48` | `m_vecCsViewPunchAngle` | QAngle | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x54` | `m_nCsViewPunchAngleTick` | [GameTick_t](../entity2/GameTick_t.md) | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x58` | `m_flCsViewPunchAngleTickRatio` | float32 | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x60` | `m_PlayerFog` | [C_fogplayerparams_t](../client/C_fogplayerparams_t.md) | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0xa0` | `m_hColorCorrectionCtrl` | CHandle< [C_ColorCorrection](../client/C_ColorCorrection.md) > | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0xa4` | `m_hViewEntity` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0xa8` | `m_hTonemapController` | CHandle< [C_TonemapController2](../client/C_TonemapController2.md) > | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0xb0` | `m_audio` | audioparams_t | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x128` | `m_PostProcessingVolumes` | C_NetworkUtlVectorBase< CHandle< [C_PostProcessingVolume](../client/C_PostProcessingVolume.md) > > | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x140` | `m_flOldPlayerZ` | float32 | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x144` | `m_flOldPlayerViewOffsetZ` | float32 | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x148` | `m_CurrentFog` | fogparams_t | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x1b0` | `m_hOldFogController` | CHandle< [C_FogController](../client/C_FogController.md) > | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x1b4` | `m_bOverrideFogColor` | bool[5] | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x1bc` | `m_OverrideFogColor` | Color[5] | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x1d0` | `m_bOverrideFogStartEnd` | bool[5] | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x1d8` | `m_fOverrideFogStart` | float32[5] | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x1ec` | `m_fOverrideFogEnd` | float32[5] | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x200` | `m_hActivePostProcessingVolume` | CHandle< [C_PostProcessingVolume](../client/C_PostProcessingVolume.md) > | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x208` | `m_angDemoViewAngles` | QAngle | [CPlayer_CameraServices](../client/CPlayer_CameraServices.md) |  |
| `0x298` | `m_iFOV` | uint32 | [CCSPlayerBase_CameraServices](../client/CCSPlayerBase_CameraServices.md) |  |
| `0x29c` | `m_iFOVStart` | uint32 | [CCSPlayerBase_CameraServices](../client/CCSPlayerBase_CameraServices.md) |  |
| `0x2a0` | `m_flFOVTime` | [GameTime_t](../entity2/GameTime_t.md) | [CCSPlayerBase_CameraServices](../client/CCSPlayerBase_CameraServices.md) |  |
| `0x2a4` | `m_flFOVRate` | float32 | [CCSPlayerBase_CameraServices](../client/CCSPlayerBase_CameraServices.md) |  |
| `0x2a8` | `m_hZoomOwner` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > | [CCSPlayerBase_CameraServices](../client/CCSPlayerBase_CameraServices.md) |  |
| `0x2ac` | `m_flLastShotFOV` | float32 | [CCSPlayerBase_CameraServices](../client/CCSPlayerBase_CameraServices.md) |  |
| `0x2b0` | `m_flDeathCamTilt` | float32 |  |  |
| `0x2b4` | `m_hDeathCamBounds` | CHandle< [C_PointDeathcamBounds](../client/C_PointDeathcamBounds.md) > |  |  |
| `0x2b8` | `m_bDeathCamBoundsSearched` | bool |  |  |
| `0x2c0` | `m_vClientScopeInaccuracy` | Vector |  |  |
