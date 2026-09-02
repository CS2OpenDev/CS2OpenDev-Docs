---
layout: default
title: CPlayer_CameraServices (client)
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / CPlayer_CameraServices

# CPlayer_CameraServices

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 656 bytes (`0x290`) · **Align:** n/a (unspecified) · **Module:** client

**Twin:** [CPlayer_CameraServices (server)](../server/CPlayer_CameraServices.md)

**Inherits from:** [CPlayerPawnComponent](../server/CPlayerPawnComponent.md)

**Derived by:** [CCSPlayerBase_CameraServices](../client/CCSPlayerBase_CameraServices.md)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_CameraServices
    CPlayer_CameraServices <|-- CCSPlayerBase_CameraServices
    CPlayer_CameraServices *-- GameTick_t
    CPlayer_CameraServices *-- C_fogplayerparams_t
    CPlayer_CameraServices --> C_ColorCorrection
    CPlayer_CameraServices --> C_BaseEntity
    CPlayer_CameraServices --> C_TonemapController2
    CPlayer_CameraServices --> C_PostProcessingVolume
    CPlayer_CameraServices --> C_FogController
```

## Memory layout

22 fields (20 declared here, 2 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `__m_pChainEntity` | [CNetworkVarChainer](../entity2/CNetworkVarChainer.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) | `MNotSaved` |
| `0x30` | `m_pComponentGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CPlayerPawnComponent](../server/CPlayerPawnComponent.md) |  |
| `0x48` | `m_vecCsViewPunchAngle` | QAngle |  |  |
| `0x54` | `m_nCsViewPunchAngleTick` | [GameTick_t](../entity2/GameTick_t.md) |  |  |
| `0x58` | `m_flCsViewPunchAngleTickRatio` | float32 |  |  |
| `0x60` | `m_PlayerFog` | [C_fogplayerparams_t](../client/C_fogplayerparams_t.md) |  |  |
| `0xa0` | `m_hColorCorrectionCtrl` | CHandle< [C_ColorCorrection](../client/C_ColorCorrection.md) > |  |  |
| `0xa4` | `m_hViewEntity` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > |  |  |
| `0xa8` | `m_hTonemapController` | CHandle< [C_TonemapController2](../client/C_TonemapController2.md) > |  |  |
| `0xb0` | `m_audio` | audioparams_t |  |  |
| `0x128` | `m_PostProcessingVolumes` | C_NetworkUtlVectorBase< CHandle< [C_PostProcessingVolume](../client/C_PostProcessingVolume.md) > > |  |  |
| `0x140` | `m_flOldPlayerZ` | float32 |  |  |
| `0x144` | `m_flOldPlayerViewOffsetZ` | float32 |  |  |
| `0x148` | `m_CurrentFog` | fogparams_t |  |  |
| `0x1b0` | `m_hOldFogController` | CHandle< [C_FogController](../client/C_FogController.md) > |  |  |
| `0x1b4` | `m_bOverrideFogColor` | bool[5] |  |  |
| `0x1b9` | `m_OverrideFogColor` | Color[5] |  |  |
| `0x1cd` | `m_bOverrideFogStartEnd` | bool[5] |  |  |
| `0x1d4` | `m_fOverrideFogStart` | float32[5] |  |  |
| `0x1e8` | `m_fOverrideFogEnd` | float32[5] |  |  |
| `0x1fc` | `m_hActivePostProcessingVolume` | CHandle< [C_PostProcessingVolume](../client/C_PostProcessingVolume.md) > |  |  |
| `0x200` | `m_angDemoViewAngles` | QAngle |  |  |
