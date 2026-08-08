---
layout: default
title: CBaseEntity
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CBaseEntity

# CBaseEntity

Root entity class in Source 2 from which all server-side entities derive. Provides health, team, physics, timing, and transmit state.


**Kind:** class · **Size:** 1192 bytes (`0x4a8`) · **Align:** 8 · **Module:** server

**Inherits from:** [CEntityInstance](../entity2/CEntityInstance.md)

**Derived by:** [CAI_ChangeHintGroup](../server/CAI_ChangeHintGroup.md), [CBaseModelEntity](../server/CBaseModelEntity.md), [CCSGO_EndOfMatchLineupEndpoint](../server/CCSGO_EndOfMatchLineupEndpoint.md), [CCSGO_TeamPreviewCharacterPosition](../server/CCSGO_TeamPreviewCharacterPosition.md), [CCSMinimapBoundary](../server/CCSMinimapBoundary.md), [CCSPetPlacement](../server/CCSPetPlacement.md), [CCSPlayerResource](../server/CCSPlayerResource.md), [CCSPointScriptEntity](../server/CCSPointScriptEntity.md), [CColorCorrection](../server/CColorCorrection.md), [CCommentaryAuto](../server/CCommentaryAuto.md), [CDebugHistory](../server/CDebugHistory.md), [CEnableMotionFixup](../server/CEnableMotionFixup.md), [CEntityFlame](../server/CEntityFlame.md), [CEnvBeverage](../server/CEnvBeverage.md), [CEnvCombinedLightProbeVolume](../server/CEnvCombinedLightProbeVolume.md), [CEnvCubemap](../server/CEnvCubemap.md), [CEnvCubemapFog](../server/CEnvCubemapFog.md), [CEnvDetailController](../server/CEnvDetailController.md), [CEnvEntityIgniter](../server/CEnvEntityIgniter.md), [CEnvLightProbeVolume](../server/CEnvLightProbeVolume.md), [CEnvVolumetricFogController](../server/CEnvVolumetricFogController.md), [CEnvVolumetricFogVolume](../server/CEnvVolumetricFogVolume.md), [CEnvWind](../server/CEnvWind.md), [CEnvWindController](../server/CEnvWindController.md), [CEnvWindVolume](../server/CEnvWindVolume.md), [CFishPool](../server/CFishPool.md), [CFogController](../server/CFogController.md), [CFuncPropRespawnZone](../server/CFuncPropRespawnZone.md), [CFuncTimescale](../server/CFuncTimescale.md), [CGameGibManager](../server/CGameGibManager.md), [CGameRulesProxy](../server/CGameRulesProxy.md), [CGradientFog](../server/CGradientFog.md), [CHandleDummy](../server/CHandleDummy.md), [CHandleTest](../server/CHandleTest.md), [CInfoLadderDismount](../server/CInfoLadderDismount.md), [CInfoVisibilityBox](../server/CInfoVisibilityBox.md), [CLogicAuto](../server/CLogicAuto.md), [CLogicGameStateReport](../server/CLogicGameStateReport.md), [CLogicNPCCounter](../server/CLogicNPCCounter.md), [CMapVetoPickController](../server/CMapVetoPickController.md), [CNullEntity](../server/CNullEntity.md), [CPathParticleRope](../server/CPathParticleRope.md), [CPhysicsSpring](../server/CPhysicsSpring.md), [CPhysicsWire](../server/CPhysicsWire.md), [CPlayerPing](../server/CPlayerPing.md), [CPlayerVisibility](../server/CPlayerVisibility.md), [CPointCamera](../server/CPointCamera.md), [CPointEntity](../server/CPointEntity.md), [CPointEntityFinder](../server/CPointEntityFinder.md), [CPointPulse](../server/CPointPulse.md), [CPointValueRemapper](../server/CPointValueRemapper.md), [CScriptedSequence](../server/CScriptedSequence.md), [CServerOnlyEntity](../server/CServerOnlyEntity.md), [CSkyCamera](../server/CSkyCamera.md), [CSoundAreaEntityBase](../server/CSoundAreaEntityBase.md), [CSoundEventEntity](../server/CSoundEventEntity.md), [CSoundEventParameter](../server/CSoundEventParameter.md), [CSoundOpvarSetEntity](../server/CSoundOpvarSetEntity.md), [CSoundOpvarSetPointBase](../server/CSoundOpvarSetPointBase.md), [CTeam](../server/CTeam.md), [CTestEffect](../server/CTestEffect.md), [CTonemapController2](../server/CTonemapController2.md), [CVoteController](../server/CVoteController.md)

**Relationships:**

```mermaid
classDiagram
    CEntityInstance <|-- CBaseEntity
    CBaseEntity <|-- CAI_ChangeHintGroup
    CBaseEntity <|-- CBaseModelEntity
    CBaseEntity <|-- CCSGO_EndOfMatchLineupEndpoint
    CBaseEntity <|-- CCSGO_TeamPreviewCharacterPosition
    CBaseEntity <|-- CCSMinimapBoundary
    CBaseEntity <|-- CCSPetPlacement
    CBaseEntity <|-- CCSPlayerResource
    CBaseEntity <|-- CCSPointScriptEntity
    CBaseEntity <|-- CColorCorrection
    CBaseEntity <|-- CCommentaryAuto
    CBaseEntity <|-- CDebugHistory
    CBaseEntity <|-- CEnableMotionFixup
    CBaseEntity <|-- CEntityFlame
    CBaseEntity <|-- CEnvBeverage
    CBaseEntity <|-- CEnvCombinedLightProbeVolume
    CBaseEntity <|-- CEnvCubemap
    CBaseEntity <|-- CEnvCubemapFog
    CBaseEntity <|-- CEnvDetailController
    CBaseEntity <|-- CEnvEntityIgniter
    CBaseEntity <|-- CEnvLightProbeVolume
    CBaseEntity <|-- CEnvVolumetricFogController
    CBaseEntity <|-- CEnvVolumetricFogVolume
    CBaseEntity <|-- CEnvWind
    CBaseEntity <|-- CEnvWindController
    CBaseEntity <|-- CEnvWindVolume
    CBaseEntity <|-- CFishPool
    CBaseEntity <|-- CFogController
    CBaseEntity <|-- CFuncPropRespawnZone
    CBaseEntity <|-- CFuncTimescale
    CBaseEntity <|-- CGameGibManager
    CBaseEntity <|-- CGameRulesProxy
    CBaseEntity <|-- CGradientFog
    CBaseEntity <|-- CHandleDummy
    CBaseEntity <|-- CHandleTest
    CBaseEntity <|-- CInfoLadderDismount
    CBaseEntity <|-- CInfoVisibilityBox
    CBaseEntity <|-- CLogicAuto
    CBaseEntity <|-- CLogicGameStateReport
    CBaseEntity <|-- CLogicNPCCounter
    CBaseEntity <|-- CMapVetoPickController
    CBaseEntity <|-- CNullEntity
    CBaseEntity <|-- CPathParticleRope
    CBaseEntity <|-- CPhysicsSpring
    CBaseEntity <|-- CPhysicsWire
    CBaseEntity <|-- CPlayerPing
    CBaseEntity <|-- CPlayerVisibility
    CBaseEntity <|-- CPointCamera
    CBaseEntity <|-- CPointEntity
    CBaseEntity <|-- CPointEntityFinder
    CBaseEntity <|-- CPointPulse
    CBaseEntity <|-- CPointValueRemapper
    CBaseEntity <|-- CScriptedSequence
    CBaseEntity <|-- CServerOnlyEntity
    CBaseEntity <|-- CSkyCamera
    CBaseEntity <|-- CSoundAreaEntityBase
    CBaseEntity <|-- CSoundEventEntity
    CBaseEntity <|-- CSoundEventParameter
    CBaseEntity <|-- CSoundOpvarSetEntity
    CBaseEntity <|-- CSoundOpvarSetPointBase
    CBaseEntity <|-- CTeam
    CBaseEntity <|-- CTestEffect
    CBaseEntity <|-- CTonemapController2
    CBaseEntity <|-- CVoteController
    CBaseEntity --> CBodyComponent
    CBaseEntity *-- CNetworkTransmitComponent
    CBaseEntity *-- GameTick_t
    CBaseEntity *-- ResponseContext_t
    CBaseEntity *-- TakeDamageFlags_t
    CBaseEntity *-- EntityPlatformTypes_t
    CBaseEntity *-- MoveCollide_t
    CBaseEntity *-- MoveType_t
    CBaseEntity --> CBaseFilter
    CBaseEntity *-- GameTime_t
```

## Memory layout

88 fields (85 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_iszPrivateVScripts` | CUtlSymbolLarge | [CEntityInstance](../entity2/CEntityInstance.md) |  |
| `0x10` | `m_pEntity` | [CEntityIdentity](../entity2/CEntityIdentity.md)* | [CEntityInstance](../entity2/CEntityInstance.md) |  |
| `0x28` | `m_CScriptComponent` | [CScriptComponent](../entity2/CScriptComponent.md)* | [CEntityInstance](../entity2/CEntityInstance.md) |  |
| `0x30` | `m_CBodyComponent` | [CBodyComponent](../server/CBodyComponent.md)* |  |  |
| `0x38` | `m_NetworkTransmitComponent` | [CNetworkTransmitComponent](../server/CNetworkTransmitComponent.md) |  |  |
| `0x248` | `m_aThinkFunctions` | CUtlVector< thinkfunc_t > |  |  |
| `0x260` | `m_iCurrentThinkContext` | int32 |  | `MNotSaved` |
| `0x264` | `m_nLastThinkTick` | [GameTick_t](../entity2/GameTick_t.md) |  |  |
| `0x268` | `m_bDisabledContextThinks` | bool |  |  |
| `0x278` | `m_isSteadyState` | CTypedBitVec< 64 > |  | `MNotSaved` |
| `0x280` | `m_lastNetworkChange` | float32 |  | `MNotSaved` |
| `0x288` | `m_think` | BASEPTR |  |  |
| `0x290` | `m_ResponseContexts` | CUtlVector< [ResponseContext_t](../server/ResponseContext_t.md) > |  |  |
| `0x2a8` | `m_iszResponseContext` | CUtlSymbolLarge |  |  |
| `0x2b0` | `m_pfnTouch` | ENTITYFUNCPTR |  |  |
| `0x2b8` | `m_pfnUse` | USEPTR |  |  |
| `0x2c0` | `m_pfnBlocked` | ENTITYFUNCPTR |  |  |
| `0x2c8` | `m_pfnMoveDone` | BASEPTR |  |  |
| `0x2d0` | `m_iHealth` | int32 |  | Current health points of the entity. Serialised with the 'ClampHealth' encoder so values above max are clamped. *Sent only to the Player network group and LocalPlayerExclusive.* |
| `0x2d4` | `m_iMaxHealth` | int32 |  | Maximum health points; used to normalise health bars in the HUD. |
| `0x2d8` | `m_lifeState` | uint8 |  | LIFE_STATE enum: 0 = Alive, 1 = Dying, 2 = Dead, 3 = Respawnable, 4 = Discardbody. |
| `0x2dc` | `m_flDamageAccumulator` | float32 |  |  |
| `0x2e0` | `m_bTakesDamage` | bool |  |  |
| `0x2e8` | `m_nTakeDamageFlags` | [TakeDamageFlags_t](../!GlobalTypes/TakeDamageFlags_t.md) |  |  |
| `0x2f0` | `m_nPlatformType` | [EntityPlatformTypes_t](../!GlobalTypes/EntityPlatformTypes_t.md) |  |  |
| `0x2f2` | `m_MoveCollide` | [MoveCollide_t](../!GlobalTypes/MoveCollide_t.md) |  |  |
| `0x2f3` | `m_MoveType` | [MoveType_t](../!GlobalTypes/MoveType_t.md) |  |  |
| `0x2f4` | `m_nPreviouslySetMoveType` | [MoveType_t](../!GlobalTypes/MoveType_t.md) |  |  |
| `0x2f5` | `m_nActualMoveType` | [MoveType_t](../!GlobalTypes/MoveType_t.md) |  |  |
| `0x2f6` | `m_nWaterTouch` | uint8 |  | `MNotSaved` |
| `0x2f7` | `m_nSlimeTouch` | uint8 |  | `MNotSaved` |
| `0x2f8` | `m_bRestoreInHierarchy` | bool |  |  |
| `0x300` | `m_target` | CUtlSymbolLarge |  |  |
| `0x308` | `m_hDamageFilter` | CHandle< [CBaseFilter](../server/CBaseFilter.md) > |  |  |
| `0x310` | `m_iszDamageFilterName` | CUtlSymbolLarge |  |  |
| `0x318` | `m_flMoveDoneTime` | float32 |  |  |
| `0x31c` | `m_nSubclassID` | CUtlStringToken |  |  |
| `0x328` | `m_flAnimTime` | float32 |  | Floating-point timestamp of the most-recent animation update; used by the client for animation interpolation. `MKV3TransferSaveOpsForField GetEngineTimeSaveRestoreOps` |
| `0x32c` | `m_flSimulationTime` | float32 |  | Floating-point timestamp of the most-recent physics simulation step; used by the client for position interpolation. `MKV3TransferSaveOpsForField GetEngineTimeSaveRestoreOps` |
| `0x330` | `m_flCreateTime` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x334` | `m_bClientSideRagdoll` | bool |  |  |
| `0x335` | `m_ubInterpolationFrame` | uint8 |  |  |
| `0x338` | `m_vPrevVPhysicsUpdatePos` | VectorWS |  |  |
| `0x344` | `m_iTeamNum` | uint8 |  | Team number: 0 = Unassigned, 1 = Spectator, 2 = Terrorist, 3 = Counter-Terrorist. |
| `0x348` | `m_iGlobalname` | CUtlSymbolLarge |  | `MSaveBehavior` |
| `0x350` | `m_iSentToClients` | int32 |  | `MNotSaved` |
| `0x358` | `m_sUniqueHammerID` | CUtlString |  |  |
| `0x360` | `m_spawnflags` | uint32 |  |  |
| `0x364` | `m_nNextThinkTick` | [GameTick_t](../entity2/GameTick_t.md) |  | Server tick on which the entity's Think() function will next execute (-1 = never). |
| `0x368` | `m_nSimulationTick` | int32 |  | `MKV3TransferSaveOpsForField GetEngineTickSaveRestoreOps` |
| `0x370` | `m_OnKilled` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) |  |  |
| `0x388` | `m_fFlags` | uint32 |  | Entity flags bitmask (FL_ONGROUND = 1, FL_DUCKING = 4, FL_INWATER = 8, FL_FROZEN = 0x200, etc.). |
| `0x38c` | `m_vecAbsVelocity` | Vector |  |  |
| `0x398` | `m_vecVelocity` | [CNetworkVelocityVector](../server/CNetworkVelocityVector.md) |  | Current world-space velocity vector of the entity. |
| `0x3c8` | `m_vecBaseVelocity` | Vector |  | Additional world-space velocity contributed by moving platforms, conveyor belts, etc. |
| `0x3d4` | `m_nPushEnumCount` | int32 |  | `MNotSaved` |
| `0x3d8` | `m_pCollision` | [CCollisionProperty](../server/CCollisionProperty.md)* |  | `MNotSaved` |
| `0x3e0` | `m_hEffectEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x3e4` | `m_hOwnerEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  | CHandle to the entity that owns or spawned this entity (e.g. the thrower of a grenade). |
| `0x3e8` | `m_fEffects` | uint32 |  | Effect flags bitmask (EF_NODRAW = 32, EF_NORECEIVESHADOW = 64, etc.). |
| `0x3ec` | `m_hGroundEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  | CHandle to the entity this entity is standing on (INVALID_EHANDLE if airborne). |
| `0x3f0` | `m_nGroundBodyIndex` | int32 |  |  |
| `0x3f4` | `m_flFriction` | float32 |  | Surface friction multiplier (1.0 = normal; lower values make the entity slide more). |
| `0x3f8` | `m_flElasticity` | float32 |  |  |
| `0x3fc` | `m_flGravityScale` | float32 |  | Gravity scale multiplier (1.0 = normal; 0 = no gravity). |
| `0x400` | `m_flTimeScale` | float32 |  | Time-scale multiplier applied to this entity's simulation (1.0 = real time; used by bullet time effects). |
| `0x404` | `m_flWaterLevel` | float32 |  |  |
| `0x408` | `m_bGravityDisabled` | bool |  |  |
| `0x409` | `m_bAnimatedEveryTick` | bool |  | True when the entity's animation must be updated every server tick regardless of network interest. |
| `0x40c` | `m_flActualGravityScale` | float32 |  |  |
| `0x410` | `m_bGravityActuallyDisabled` | bool |  |  |
| `0x411` | `m_bDisableLowViolence` | bool |  |  |
| `0x412` | `m_nWaterType` | uint8 |  |  |
| `0x414` | `m_iEFlags` | int32 |  |  |
| `0x418` | `m_OnUser1` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) |  |  |
| `0x430` | `m_OnUser2` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) |  |  |
| `0x448` | `m_OnUser3` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) |  |  |
| `0x460` | `m_OnUser4` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) |  |  |
| `0x478` | `m_iInitialTeamNum` | int32 |  |  |
| `0x47c` | `m_flNavIgnoreUntilTime` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x480` | `m_vecAngVelocity` | QAngle |  |  |
| `0x48c` | `m_bNetworkQuantizeOriginAndAngles` | bool |  |  |
| `0x48d` | `m_bLagCompensate` | bool |  |  |
| `0x490` | `m_pBlocker` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x494` | `m_flLocalTime` | float32 |  |  |
| `0x498` | `m_flVPhysicsUpdateLocalTime` | float32 |  |  |
| `0x49c` | `m_nBloodType` | [BloodType](../!GlobalTypes/BloodType.md) |  |  |
| `0x4a0` | `m_pPulseGraphInstance` | [CPulseGraphInstance_ServerEntity](../server/CPulseGraphInstance_ServerEntity.md)* |  | `MKV3TransferSaveOpsForField GetPulseInstanceSaveRestoreOps` |
