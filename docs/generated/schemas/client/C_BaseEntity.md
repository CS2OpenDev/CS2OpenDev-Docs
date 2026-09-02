---
layout: default
title: C_BaseEntity
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / C_BaseEntity

# C_BaseEntity

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 1536 bytes (`0x600`) · **Align:** 8 · **Module:** client

**Inherits from:** [CEntityInstance](../entity2/CEntityInstance.md)

**Derived by:** [CBasePlayerController](../client/CBasePlayerController.md), [CCSCustomHudLayout](../client/CCSCustomHudLayout.md), [CCSPlayerCamera](../client/CCSPlayerCamera.md), [CCS_PortraitWorldCallbackHandler](../client/CCS_PortraitWorldCallbackHandler.md), [CCitadelSoundOpvarSetOBB](../client/CCitadelSoundOpvarSetOBB.md), [CEnvSoundscape](../client/CEnvSoundscape.md), [CInfoWorldLayer](../client/CInfoWorldLayer.md), [CLogicalEntity](../client/CLogicalEntity.md), [CPathSimple](../client/CPathSimple.md), [CPointOrient](../client/CPointOrient.md), [CPulseGameBlackboard](../client/CPulseGameBlackboard.md), [CRagdollManager](../client/CRagdollManager.md), [CSkyboxReference](../client/CSkyboxReference.md), [C_BaseModelEntity](../client/C_BaseModelEntity.md), [C_CSGO_EndOfMatchLineupEndpoint](../client/C_CSGO_EndOfMatchLineupEndpoint.md), [C_CSGO_MapPreviewCameraPath](../client/C_CSGO_MapPreviewCameraPath.md), [C_CSGO_MapPreviewCameraPathNode](../client/C_CSGO_MapPreviewCameraPathNode.md), [C_CSGO_TeamPreviewCharacterPosition](../client/C_CSGO_TeamPreviewCharacterPosition.md), [C_CSMinimapBoundary](../client/C_CSMinimapBoundary.md), [C_CSPetPlacement](../client/C_CSPetPlacement.md), [C_CSPlayerResource](../client/C_CSPlayerResource.md), [C_ColorCorrection](../client/C_ColorCorrection.md), [C_CsmFovOverride](../client/C_CsmFovOverride.md), [C_EntityFlame](../client/C_EntityFlame.md), [C_EnvCombinedLightProbeVolume](../client/C_EnvCombinedLightProbeVolume.md), [C_EnvCubemap](../client/C_EnvCubemap.md), [C_EnvCubemapFog](../client/C_EnvCubemapFog.md), [C_EnvDetailController](../client/C_EnvDetailController.md), [C_EnvLightProbeVolume](../client/C_EnvLightProbeVolume.md), [C_EnvVolumetricFogController](../client/C_EnvVolumetricFogController.md), [C_EnvVolumetricFogVolume](../client/C_EnvVolumetricFogVolume.md), [C_EnvWind](../client/C_EnvWind.md), [C_EnvWindClientside](../client/C_EnvWindClientside.md), [C_EnvWindController](../client/C_EnvWindController.md), [C_EnvWindVolume](../client/C_EnvWindVolume.md), [C_FogController](../client/C_FogController.md), [C_GameRulesProxy](../client/C_GameRulesProxy.md), [C_GlobalLight](../client/C_GlobalLight.md), [C_GradientFog](../client/C_GradientFog.md), [C_HandleTest](../client/C_HandleTest.md), [C_InfoLadderDismount](../client/C_InfoLadderDismount.md), [C_InfoVisibilityBox](../client/C_InfoVisibilityBox.md), [C_MapVetoPickController](../client/C_MapVetoPickController.md), [C_PathParticleRope](../client/C_PathParticleRope.md), [C_PlayerPing](../client/C_PlayerPing.md), [C_PlayerVisibility](../client/C_PlayerVisibility.md), [C_PointCamera](../client/C_PointCamera.md), [C_PointEntity](../client/C_PointEntity.md), [C_PointValueRemapper](../client/C_PointValueRemapper.md), [C_PortraitWorldCallbackHandler](../client/C_PortraitWorldCallbackHandler.md), [C_SkyCamera](../client/C_SkyCamera.md), [C_SoundAreaEntityBase](../client/C_SoundAreaEntityBase.md), [C_SoundEventEntity](../client/C_SoundEventEntity.md), [C_SoundOpvarSetPointBase](../client/C_SoundOpvarSetPointBase.md), [C_Team](../client/C_Team.md), [C_TintController](../client/C_TintController.md), [C_TonemapController2](../client/C_TonemapController2.md), [C_VoteController](../client/C_VoteController.md)

**Relationships:**

```mermaid
classDiagram
    CEntityInstance <|-- C_BaseEntity
    C_BaseEntity <|-- CBasePlayerController
    C_BaseEntity <|-- CCSCustomHudLayout
    C_BaseEntity <|-- CCSPlayerCamera
    C_BaseEntity <|-- CCS_PortraitWorldCallbackHandler
    C_BaseEntity <|-- CCitadelSoundOpvarSetOBB
    C_BaseEntity <|-- CEnvSoundscape
    C_BaseEntity <|-- CInfoWorldLayer
    C_BaseEntity <|-- CLogicalEntity
    C_BaseEntity <|-- CPathSimple
    C_BaseEntity <|-- CPointOrient
    C_BaseEntity <|-- CPulseGameBlackboard
    C_BaseEntity <|-- CRagdollManager
    C_BaseEntity <|-- CSkyboxReference
    C_BaseEntity <|-- C_BaseModelEntity
    C_BaseEntity <|-- C_CSGO_EndOfMatchLineupEndpoint
    C_BaseEntity <|-- C_CSGO_MapPreviewCameraPath
    C_BaseEntity <|-- C_CSGO_MapPreviewCameraPathNode
    C_BaseEntity <|-- C_CSGO_TeamPreviewCharacterPosition
    C_BaseEntity <|-- C_CSMinimapBoundary
    C_BaseEntity <|-- C_CSPetPlacement
    C_BaseEntity <|-- C_CSPlayerResource
    C_BaseEntity <|-- C_ColorCorrection
    C_BaseEntity <|-- C_CsmFovOverride
    C_BaseEntity <|-- C_EntityFlame
    C_BaseEntity <|-- C_EnvCombinedLightProbeVolume
    C_BaseEntity <|-- C_EnvCubemap
    C_BaseEntity <|-- C_EnvCubemapFog
    C_BaseEntity <|-- C_EnvDetailController
    C_BaseEntity <|-- C_EnvLightProbeVolume
    C_BaseEntity <|-- C_EnvVolumetricFogController
    C_BaseEntity <|-- C_EnvVolumetricFogVolume
    C_BaseEntity <|-- C_EnvWind
    C_BaseEntity <|-- C_EnvWindClientside
    C_BaseEntity <|-- C_EnvWindController
    C_BaseEntity <|-- C_EnvWindVolume
    C_BaseEntity <|-- C_FogController
    C_BaseEntity <|-- C_GameRulesProxy
    C_BaseEntity <|-- C_GlobalLight
    C_BaseEntity <|-- C_GradientFog
    C_BaseEntity <|-- C_HandleTest
    C_BaseEntity <|-- C_InfoLadderDismount
    C_BaseEntity <|-- C_InfoVisibilityBox
    C_BaseEntity <|-- C_MapVetoPickController
    C_BaseEntity <|-- C_PathParticleRope
    C_BaseEntity <|-- C_PlayerPing
    C_BaseEntity <|-- C_PlayerVisibility
    C_BaseEntity <|-- C_PointCamera
    C_BaseEntity <|-- C_PointEntity
    C_BaseEntity <|-- C_PointValueRemapper
    C_BaseEntity <|-- C_PortraitWorldCallbackHandler
    C_BaseEntity <|-- C_SkyCamera
    C_BaseEntity <|-- C_SoundAreaEntityBase
    C_BaseEntity <|-- C_SoundEventEntity
    C_BaseEntity <|-- C_SoundOpvarSetPointBase
    C_BaseEntity <|-- C_Team
    C_BaseEntity <|-- C_TintController
    C_BaseEntity <|-- C_TonemapController2
    C_BaseEntity <|-- C_VoteController
    C_BaseEntity --> CBodyComponent
    C_BaseEntity *-- CNetworkTransmitComponent
    C_BaseEntity *-- GameTick_t
    C_BaseEntity --> CGameSceneNode
    C_BaseEntity --> CRenderComponent
    C_BaseEntity --> CCollisionProperty
    C_BaseEntity *-- TakeDamageFlags_t
    C_BaseEntity *-- EntityPlatformTypes_t
    C_BaseEntity *-- GameTime_t
    C_BaseEntity *-- CNetworkVelocityVector
```

## Memory layout

85 fields (82 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_iszPrivateVScripts` | CUtlSymbolLarge | [CEntityInstance](../entity2/CEntityInstance.md) |  |
| `0x10` | `m_pEntity` | [CEntityIdentity](../entity2/CEntityIdentity.md)* | [CEntityInstance](../entity2/CEntityInstance.md) | CEntityIdentity pointer — the entity's identity record (name, class, handle, flags). |
| `0x28` | `m_CScriptComponent` | [CScriptComponent](../entity2/CScriptComponent.md)* | [CEntityInstance](../entity2/CEntityInstance.md) | VScript component attached to the entity, when scripted. |
| `0x30` | `m_CBodyComponent` | [CBodyComponent](../client/CBodyComponent.md)* |  |  |
| `0x38` | `m_NetworkTransmitComponent` | [CNetworkTransmitComponent](../server/CNetworkTransmitComponent.md) |  | `MNotSaved` |
| `0x328` | `m_nLastThinkTick` | [GameTick_t](../entity2/GameTick_t.md) |  | `MNotSaved` |
| `0x330` | `m_pGameSceneNode` | [CGameSceneNode](../client/CGameSceneNode.md)* |  | `MNotSaved` |
| `0x338` | `m_pRenderComponent` | [CRenderComponent](../client/CRenderComponent.md)* |  | `MNotSaved` |
| `0x340` | `m_pCollision` | [CCollisionProperty](../client/CCollisionProperty.md)* |  | `MNotSaved` |
| `0x348` | `m_iMaxHealth` | int32 |  | `MNotSaved` |
| `0x34c` | `m_iHealth` | int32 |  |  |
| `0x350` | `m_flDamageAccumulator` | float32 |  | `MNotSaved` |
| `0x354` | `m_lifeState` | uint8 |  | `MNotSaved` |
| `0x355` | `m_bTakesDamage` | bool |  | `MNotSaved` |
| `0x358` | `m_nTakeDamageFlags` | [TakeDamageFlags_t](../server/TakeDamageFlags_t.md) |  | `MNotSaved` |
| `0x360` | `m_nPlatformType` | [EntityPlatformTypes_t](../server/EntityPlatformTypes_t.md) |  |  |
| `0x361` | `m_ubInterpolationFrame` | uint8 |  | `MNotSaved` |
| `0x364` | `m_hSceneObjectController` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > |  |  |
| `0x368` | `m_nNoInterpolationTick` | int32 |  | `MNotSaved` |
| `0x36c` | `m_nVisibilityNoInterpolationTick` | int32 |  | `MNotSaved` |
| `0x370` | `m_flProxyRandomValue` | float32 |  | `MNotSaved` |
| `0x374` | `m_iEFlags` | int32 |  | `MNotSaved` |
| `0x378` | `m_nWaterType` | uint8 |  | `MNotSaved` |
| `0x379` | `m_bInterpolateEvenWithNoModel` | bool |  | `MNotSaved` |
| `0x37a` | `m_bPredictionEligible` | bool |  | `MNotSaved` |
| `0x37b` | `m_bApplyLayerMatchIDToModel` | bool |  | `MNotSaved` |
| `0x37c` | `m_tokLayerMatchID` | CUtlStringToken |  | `MNotSaved` |
| `0x380` | `m_nSubclassID` | CUtlStringToken |  |  |
| `0x390` | `m_nSimulationTick` | int32 |  | `MNotSaved` |
| `0x394` | `m_iCurrentThinkContext` | int32 |  | `MNotSaved` |
| `0x398` | `m_aThinkFunctions` | CUtlVector< thinkfunc_t > |  | `MNotSaved` |
| `0x3b0` | `m_bDisabledContextThinks` | bool |  |  |
| `0x3b4` | `m_flAnimTime` | float32 |  | `MNotSaved` |
| `0x3b8` | `m_flSimulationTime` | float32 |  | `MNotSaved` |
| `0x3bc` | `m_nSceneObjectOverrideFlags` | uint8 |  |  |
| `0x3bd` | `m_bHasSuccessfullyInterpolated` | bool |  | `MNotSaved` |
| `0x3be` | `m_bHasAddedVarsToInterpolation` | bool |  | `MNotSaved` |
| `0x3bf` | `m_bRenderEvenWhenNotSuccessfullyInterpolated` | bool |  | `MNotSaved` |
| `0x3c0` | `m_nInterpolationLatchDirtyFlags` | int32[2] |  | `MNotSaved` |
| `0x3c8` | `m_ListEntry` | uint16[11] |  | `MNotSaved` |
| `0x3e0` | `m_flCreateTime` | [GameTime_t](../entity2/GameTime_t.md) |  | `MNotSaved` |
| `0x3e4` | `m_EntClientFlags` | uint16 |  | `MNotSaved` |
| `0x3e6` | `m_bClientSideRagdoll` | bool |  | `MNotSaved` |
| `0x3e7` | `m_iTeamNum` | uint8 |  | `MNotSaved` |
| `0x3e8` | `m_spawnflags` | uint32 |  |  |
| `0x3ec` | `m_nNextThinkTick` | [GameTick_t](../entity2/GameTick_t.md) |  | `MNotSaved` |
| `0x3f4` | `m_fFlags` | uint32 |  | `MSaveBehavior` |
| `0x3f8` | `m_vecAbsVelocity` | Vector |  | `MNotSaved` |
| `0x404` | `m_vecServerVelocity` | [CNetworkVelocityVector](../server/CNetworkVelocityVector.md) |  | `MNotSaved` |
| `0x430` | `m_vecVelocity` | [CNetworkVelocityVector](../server/CNetworkVelocityVector.md) |  |  |
| `0x510` | `m_vecBaseVelocity` | Vector |  | `MNotSaved` |
| `0x51c` | `m_hEffectEntity` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > |  | `MNotSaved` |
| `0x520` | `m_hOwnerEntity` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > |  |  |
| `0x524` | `m_MoveCollide` | [MoveCollide_t](../server/MoveCollide_t.md) |  | `MNotSaved` |
| `0x525` | `m_MoveType` | [MoveType_t](../server/MoveType_t.md) |  |  |
| `0x526` | `m_nActualMoveType` | [MoveType_t](../server/MoveType_t.md) |  |  |
| `0x528` | `m_flWaterLevel` | float32 |  | `MNotSaved` |
| `0x52c` | `m_fEffects` | uint32 |  | `MNotSaved` |
| `0x530` | `m_hGroundEntity` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > |  | `MNotSaved` |
| `0x534` | `m_nGroundBodyIndex` | int32 |  | `MNotSaved` |
| `0x538` | `m_flFriction` | float32 |  | `MNotSaved` |
| `0x53c` | `m_flElasticity` | float32 |  | `MNotSaved` |
| `0x540` | `m_flGravityScale` | float32 |  | `MNotSaved` |
| `0x544` | `m_flTimeScale` | float32 |  | `MNotSaved` |
| `0x548` | `m_bAnimatedEveryTick` | bool |  | `MNotSaved` |
| `0x549` | `m_bGravityDisabled` | bool |  |  |
| `0x54c` | `m_flNavIgnoreUntilTime` | [GameTime_t](../entity2/GameTime_t.md) |  | `MNotSaved` |
| `0x550` | `m_hThink` | uint16 |  | `MNotSaved` |
| `0x560` | `m_fBBoxVisFlags` | uint8 |  | `MNotSaved` |
| `0x564` | `m_flActualGravityScale` | float32 |  |  |
| `0x568` | `m_bGravityActuallyDisabled` | bool |  |  |
| `0x569` | `m_bPredictable` | bool |  | `MNotSaved` |
| `0x56a` | `m_bRenderWithViewModels` | bool |  |  |
| `0x56c` | `m_nFirstPredictableCommand` | int32 |  | `MNotSaved` |
| `0x570` | `m_nLastPredictableCommand` | int32 |  | `MNotSaved` |
| `0x574` | `m_hOldMoveParent` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > |  | `MNotSaved` |
| `0x578` | `m_Particles` | [CParticleProperty](../particleslib/CParticleProperty.md) |  | `MNotSaved` |
| `0x5a8` | `m_vecAngVelocity` | QAngle |  |  |
| `0x5b4` | `m_DataChangeEventRef` | int32 |  | `MNotSaved` |
| `0x5b8` | `m_dependencies` | CUtlVector< CEntityHandle > |  | `MNotSaved` |
| `0x5d0` | `m_nCreationTick` | int32 |  | `MNotSaved` |
| `0x5e1` | `m_bAnimTimeChanged` | bool |  | `MNotSaved` |
| `0x5e2` | `m_bSimulationTimeChanged` | bool |  | `MNotSaved` |
| `0x5f0` | `m_sUniqueHammerID` | CUtlString |  | `MNotSaved` |
| `0x5f8` | `m_nBloodType` | [BloodType](../server/BloodType.md) |  |  |
