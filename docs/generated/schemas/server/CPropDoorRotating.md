---
layout: default
title: CPropDoorRotating
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CPropDoorRotating

# CPropDoorRotating

**Kind:** class · **Size:** 3648 bytes (`0xe40`) · **Align:** 16 · **Module:** server

**Inherits from:** [CBasePropDoor](../server/CBasePropDoor.md)

**Derived by:** [CPropDoorRotatingBreakable](../server/CPropDoorRotatingBreakable.md)

**Relationships:**

```mermaid
classDiagram
    CBasePropDoor <|-- CPropDoorRotating
    CDynamicProp <|-- CBasePropDoor
    CBreakableProp <|-- CDynamicProp
    CBaseProp <|-- CBreakableProp
    CBaseAnimGraph <|-- CBaseProp
    CPropDoorRotating <|-- CPropDoorRotatingBreakable
    CPropDoorRotating *-- PropDoorRotatingSpawnPos_t
    CPropDoorRotating *-- PropDoorRotatingOpenDirection_e
    CPropDoorRotating --> CEntityBlocker
```

## Memory layout

263 fields (18 declared here, 245 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_iszPrivateVScripts` | CUtlSymbolLarge | [CEntityInstance](../entity2/CEntityInstance.md) |  |
| `0x10` | `m_pEntity` | [CEntityIdentity](../entity2/CEntityIdentity.md)* | [CEntityInstance](../entity2/CEntityInstance.md) |  |
| `0x28` | `m_CScriptComponent` | [CScriptComponent](../entity2/CScriptComponent.md)* | [CEntityInstance](../entity2/CEntityInstance.md) |  |
| `0x30` | `m_CBodyComponent` | [CBodyComponent](../server/CBodyComponent.md)* | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x38` | `m_NetworkTransmitComponent` | [CNetworkTransmitComponent](../server/CNetworkTransmitComponent.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x328` | `m_nLastThinkTick` | [GameTick_t](../entity2/GameTick_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x330` | `m_pGameSceneNode` | [CGameSceneNode](../server/CGameSceneNode.md)* | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x338` | `m_pRenderComponent` | [CRenderComponent](../server/CRenderComponent.md)* | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x340` | `m_pCollision` | [CCollisionProperty](../server/CCollisionProperty.md)* | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x348` | `m_iMaxHealth` | int32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x34c` | `m_iHealth` | int32 | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x350` | `m_flDamageAccumulator` | float32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x354` | `m_lifeState` | uint8 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x355` | `m_bTakesDamage` | bool | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x358` | `m_nTakeDamageFlags` | [TakeDamageFlags_t](../server/TakeDamageFlags_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x360` | `m_nPlatformType` | [EntityPlatformTypes_t](../server/EntityPlatformTypes_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x361` | `m_ubInterpolationFrame` | uint8 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x364` | `m_hSceneObjectController` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x368` | `m_nNoInterpolationTick` | int32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x36c` | `m_nVisibilityNoInterpolationTick` | int32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x370` | `m_flProxyRandomValue` | float32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x374` | `m_iEFlags` | int32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x378` | `m_nWaterType` | uint8 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x379` | `m_bInterpolateEvenWithNoModel` | bool | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x37a` | `m_bPredictionEligible` | bool | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x37b` | `m_bApplyLayerMatchIDToModel` | bool | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x37c` | `m_tokLayerMatchID` | CUtlStringToken | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x380` | `m_nSubclassID` | CUtlStringToken | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x390` | `m_nSimulationTick` | int32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x394` | `m_iCurrentThinkContext` | int32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x398` | `m_aThinkFunctions` | CUtlVector< thinkfunc_t > | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3b0` | `m_bDisabledContextThinks` | bool | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x3b4` | `m_flAnimTime` | float32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3b8` | `m_flSimulationTime` | float32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3bc` | `m_nSceneObjectOverrideFlags` | uint8 | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x3bd` | `m_bHasSuccessfullyInterpolated` | bool | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3be` | `m_bHasAddedVarsToInterpolation` | bool | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3bf` | `m_bRenderEvenWhenNotSuccessfullyInterpolated` | bool | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3c0` | `m_nInterpolationLatchDirtyFlags` | int32[2] | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3c8` | `m_ListEntry` | uint16[11] | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3e0` | `m_flCreateTime` | [GameTime_t](../entity2/GameTime_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3e4` | `m_EntClientFlags` | uint16 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3e6` | `m_bClientSideRagdoll` | bool | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3e7` | `m_iTeamNum` | uint8 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3e8` | `m_spawnflags` | uint32 | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x3ec` | `m_nNextThinkTick` | [GameTick_t](../entity2/GameTick_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x3f4` | `m_fFlags` | uint32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MSaveBehavior` |
| `0x3f8` | `m_vecAbsVelocity` | Vector | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x404` | `m_vecServerVelocity` | [CNetworkVelocityVector](../server/CNetworkVelocityVector.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x430` | `m_vecVelocity` | [CNetworkVelocityVector](../server/CNetworkVelocityVector.md) | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x510` | `m_vecBaseVelocity` | Vector | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x51c` | `m_hEffectEntity` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x520` | `m_hOwnerEntity` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x524` | `m_MoveCollide` | [MoveCollide_t](../server/MoveCollide_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x525` | `m_MoveType` | [MoveType_t](../server/MoveType_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x526` | `m_nActualMoveType` | [MoveType_t](../server/MoveType_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x528` | `m_flWaterLevel` | float32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x52c` | `m_fEffects` | uint32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x530` | `m_hGroundEntity` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x534` | `m_nGroundBodyIndex` | int32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x538` | `m_flFriction` | float32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x53c` | `m_flElasticity` | float32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x540` | `m_flGravityScale` | float32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x544` | `m_flTimeScale` | float32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x548` | `m_bAnimatedEveryTick` | bool | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x549` | `m_bGravityDisabled` | bool | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x54c` | `m_flNavIgnoreUntilTime` | [GameTime_t](../entity2/GameTime_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x550` | `m_hThink` | uint16 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x560` | `m_fBBoxVisFlags` | uint8 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x564` | `m_flActualGravityScale` | float32 | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x568` | `m_bGravityActuallyDisabled` | bool | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x569` | `m_bPredictable` | bool | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x56a` | `m_bRenderWithViewModels` | bool | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x56c` | `m_nFirstPredictableCommand` | int32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x570` | `m_nLastPredictableCommand` | int32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x574` | `m_hOldMoveParent` | CHandle< [C_BaseEntity](../client/C_BaseEntity.md) > | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x578` | `m_Particles` | [CParticleProperty](../particleslib/CParticleProperty.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x5a8` | `m_vecAngVelocity` | QAngle | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x5b4` | `m_DataChangeEventRef` | int32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x5b8` | `m_dependencies` | CUtlVector< CEntityHandle > | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x5d0` | `m_nCreationTick` | int32 | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x5e1` | `m_bAnimTimeChanged` | bool | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x5e2` | `m_bSimulationTimeChanged` | bool | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x5f0` | `m_sUniqueHammerID` | CUtlString | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x5f8` | `m_nBloodType` | [BloodType](../server/BloodType.md) | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x998` | `m_CPropDataComponent` | [CPropDataComponent](../server/CPropDataComponent.md) | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0x9d8` | `m_OnStartDeath` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0x9f0` | `m_OnBreak` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa08` | `m_OnHealthChanged` | CEntityOutputTemplate< float32 > | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa28` | `m_OnTakeDamage` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa40` | `m_impactEnergyScale` | float32 | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa44` | `m_iMinHealthDmg` | int32 | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa48` | `m_preferredCarryAngles` | QAngle | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa54` | `m_flPressureDelay` | float32 | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa58` | `m_flDefBurstScale` | float32 | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa5c` | `m_vDefBurstOffset` | Vector | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa68` | `m_hBreaker` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa6c` | `m_PerformanceMode` | [PerformanceMode_t](../server/PerformanceMode_t.md) | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa70` | `m_flPreventDamageBeforeTime` | [GameTime_t](../entity2/GameTime_t.md) | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa74` | `m_BreakableContentsType` | [BreakableContentsType_t](../server/BreakableContentsType_t.md) | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa78` | `m_strBreakableContentsPropGroupOverride` | CUtlString | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa80` | `m_strBreakableContentsParticleOverride` | CUtlString | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa88` | `m_bHasBreakPiecesOrCommands` | bool | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa8c` | `m_explodeDamage` | float32 | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa90` | `m_explodeRadius` | float32 | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xa98` | `m_sExplosionType` | CGlobalSymbol | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xaa0` | `m_explosionDelay` | float32 | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xaa8` | `m_explosionBuildupSound` | CUtlSymbolLarge | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xab0` | `m_explosionCustomEffect` | CUtlSymbolLarge | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xab8` | `m_explosionCustomSound` | CUtlSymbolLarge | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xac0` | `m_explosionModifier` | CUtlSymbolLarge | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xac8` | `m_hPhysicsAttacker` | CHandle< [CBasePlayerPawn](../server/CBasePlayerPawn.md) > | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xacc` | `m_flLastPhysicsInfluenceTime` | [GameTime_t](../entity2/GameTime_t.md) | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xad0` | `m_flDefaultFadeScale` | float32 | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xad4` | `m_hLastAttacker` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xad8` | `m_iszPuntSound` | CUtlSymbolLarge | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xae0` | `m_bUsePuntSound` | bool | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xae1` | `m_bOriginalBlockLOS` | bool | [CBreakableProp](../server/CBreakableProp.md) |  |
| `0xaf0` | `m_CRenderComponent` | [CRenderComponent](../server/CRenderComponent.md)* | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xaf8` | `m_bCreateNavObstacle` | bool | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xaf8` | `m_CHitboxComponent` | [CHitboxComponent](../server/CHitboxComponent.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xaf9` | `m_bNavObstacleUpdatesOverridden` | bool | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xafa` | `m_bUseHitboxesForRenderBox` | bool | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xafb` | `m_bUseAnimGraph` | bool | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb00` | `m_pOutputAnimBegun` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb10` | `m_pChoreoComponent` | [CChoreoComponent](../server/CChoreoComponent.md)* | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb18` | `m_pOutputAnimOver` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb18` | `m_nDestructiblePartInitialStateDestructed0` | [HitGroup_t](../server/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb1c` | `m_nDestructiblePartInitialStateDestructed1` | [HitGroup_t](../server/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb20` | `m_nDestructiblePartInitialStateDestructed2` | [HitGroup_t](../server/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb24` | `m_nDestructiblePartInitialStateDestructed3` | [HitGroup_t](../server/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb28` | `m_nDestructiblePartInitialStateDestructed4` | [HitGroup_t](../server/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb2c` | `m_nDestructiblePartInitialStateDestructed0_PartIndex` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb30` | `m_pOutputAnimLoopCycleOver` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb30` | `m_nDestructiblePartInitialStateDestructed1_PartIndex` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb34` | `m_nDestructiblePartInitialStateDestructed2_PartIndex` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb38` | `m_nDestructiblePartInitialStateDestructed3_PartIndex` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb3c` | `m_nDestructiblePartInitialStateDestructed4_PartIndex` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb40` | `m_bDestructiblePartInitialStateDestructed0_GenerateBreakpieces` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb41` | `m_bDestructiblePartInitialStateDestructed1_GenerateBreakpieces` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb42` | `m_bDestructiblePartInitialStateDestructed2_GenerateBreakpieces` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb43` | `m_bDestructiblePartInitialStateDestructed3_GenerateBreakpieces` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb44` | `m_bDestructiblePartInitialStateDestructed4_GenerateBreakpieces` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb48` | `m_OnAnimReachedStart` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb48` | `m_pDestructiblePartsSystemComponent` | [CDestructiblePartsComponent](../server/CDestructiblePartsComponent.md)* | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb60` | `m_OnAnimReachedEnd` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb78` | `m_iszIdleAnim` | CUtlSymbolLarge | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb80` | `m_nIdleAnimLoopMode` | [AnimLoopMode_t](../server/AnimLoopMode_t.md) | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb84` | `m_bRandomizeCycle` | bool | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb85` | `m_bStartDisabled` | bool | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb86` | `m_bFiredStartEndOutput` | bool | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb87` | `m_bForceNpcExclude` | bool | [CDynamicProp](../server/CDynamicProp.md) | `MNotSaved` |
| `0xb88` | `m_bCreateMovableSurfaceGraph` | bool | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb89` | `m_bCreateNonSolid` | bool | [CDynamicProp](../server/CDynamicProp.md) | `MNotSaved` |
| `0xb8a` | `m_bIsOverrideProp` | bool | [CDynamicProp](../server/CDynamicProp.md) | `MNotSaved` |
| `0xb8c` | `m_iInitialGlowState` | int32 | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb90` | `m_nGlowRange` | int32 | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb94` | `m_nGlowRangeMin` | int32 | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb98` | `m_glowColor` | Color | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xb9c` | `m_nGlowTeam` | int32 | [CDynamicProp](../server/CDynamicProp.md) |  |
| `0xbb0` | `m_flAutoReturnDelay` | float32 | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xbb8` | `m_hDoorList` | CUtlVector< CHandle< [CBasePropDoor](../server/CBasePropDoor.md) > > | [CBasePropDoor](../server/CBasePropDoor.md) | `MNotSaved` |
| `0xbd0` | `m_nHardwareType` | int32 | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xbd4` | `m_bNeedsHardware` | bool | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xbd8` | `m_eDoorState` | [DoorState_t](../server/DoorState_t.md) | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xbdc` | `m_bLocked` | bool | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xbdd` | `m_bNoNPCs` | bool | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xbe0` | `m_closedPosition` | VectorWS | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xbec` | `m_closedAngles` | QAngle | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xbf8` | `m_hBlocker` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xbfc` | `m_bFirstBlocked` | bool | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc00` | `m_ls` | locksound_t | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc20` | `m_bForceClosed` | bool | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc24` | `m_vecLatchWorldPosition` | VectorWS | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc30` | `m_hActivator` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc34` | `m_flSpeed` | float32 | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc50` | `m_SoundMoving` | CGameSoundEventName | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc58` | `m_SoundOpen` | CGameSoundEventName | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc60` | `m_SoundClose` | CGameSoundEventName | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc68` | `m_SoundLock` | CGameSoundEventName | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc70` | `m_SoundUnlock` | CGameSoundEventName | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc70` | `m_bInitModelEffects` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xc71` | `m_bDoingModelEffects` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xc74` | `m_iOldHealth` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xc78` | `m_SoundLatch` | CGameSoundEventName | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc78` | `m_nRenderMode` | [RenderMode_t](../server/RenderMode_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc79` | `m_nRenderFX` | [RenderFx_t](../server/RenderFx_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc7a` | `m_bAllowFadeInView` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc80` | `m_SoundPound` | CGameSoundEventName | [CBasePropDoor](../server/CBasePropDoor.md) | `MNotSaved` |
| `0xc88` | `m_SoundJiggle` | CGameSoundEventName | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc90` | `m_SoundLockedAnim` | CGameSoundEventName | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xc98` | `m_numCloseAttempts` | int32 | [CBasePropDoor](../server/CBasePropDoor.md) | `MNotSaved` |
| `0xc98` | `m_clrRender` | Color | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc9c` | `m_nPhysicsMaterial` | CUtlStringToken | [CBasePropDoor](../server/CBasePropDoor.md) | `MNotSaved` |
| `0xca0` | `m_SlaveName` | CUtlSymbolLarge | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xca0` | `m_vecRenderAttributes` | C_UtlVectorEmbeddedNetworkVar< [EntityRenderAttribute_t](../server/EntityRenderAttribute_t.md) > | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xca8` | `m_hMaster` | CHandle< [CBasePropDoor](../server/CBasePropDoor.md) > | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xcb0` | `m_OnBlockedClosing` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xcc8` | `m_OnBlockedOpening` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xce0` | `m_OnUnblockedClosing` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xcf8` | `m_OnUnblockedOpening` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xd10` | `m_OnFullyClosed` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xd20` | `m_bRenderToCubemaps` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xd21` | `m_bNoInterpolate` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xd28` | `m_OnFullyOpen` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xd28` | `m_Collision` | [CCollisionProperty](../server/CCollisionProperty.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xd40` | `m_OnClose` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xd58` | `m_OnOpen` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xd70` | `m_OnLockedUse` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xd88` | `m_OnAjarOpen` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBasePropDoor](../server/CBasePropDoor.md) |  |
| `0xda0` | `m_vecAxis` | Vector |  |  |
| `0xdac` | `m_flDistance` | float32 |  |  |
| `0xdb0` | `m_eSpawnPosition` | [PropDoorRotatingSpawnPos_t](../server/PropDoorRotatingSpawnPos_t.md) |  |  |
| `0xdb4` | `m_eOpenDirection` | [PropDoorRotatingOpenDirection_e](../server/PropDoorRotatingOpenDirection_e.md) |  |  |
| `0xdb8` | `m_eCurrentOpenDirection` | [PropDoorRotatingOpenDirection_e](../server/PropDoorRotatingOpenDirection_e.md) |  | `MNotSaved` |
| `0xdbc` | `m_eDefaultCheckDirection` | doorCheck_e |  | `MNotSaved` |
| `0xdc0` | `m_flAjarAngle` | float32 |  |  |
| `0xdc4` | `m_angRotationAjarDeprecated` | QAngle |  |  |
| `0xdd0` | `m_angRotationClosed` | QAngle |  |  |
| `0xddc` | `m_angRotationOpenForward` | QAngle |  |  |
| `0xde0` | `m_Glow` | [CGlowProperty](../server/CGlowProperty.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xde8` | `m_angRotationOpenBack` | QAngle |  |  |
| `0xdf4` | `m_angGoal` | QAngle |  |  |
| `0xe00` | `m_vecForwardBoundsMin` | Vector |  | `MNotSaved` |
| `0xe0c` | `m_vecForwardBoundsMax` | Vector |  | `MNotSaved` |
| `0xe18` | `m_vecBackBoundsMin` | Vector |  | `MNotSaved` |
| `0xe24` | `m_vecBackBoundsMax` | Vector |  | `MNotSaved` |
| `0xe30` | `m_bAjarDoorShouldntAlwaysOpen` | bool |  |  |
| `0xe34` | `m_hEntityBlocker` | CHandle< [CEntityBlocker](../server/CEntityBlocker.md) > |  |  |
| `0xe38` | `m_flGlowBackfaceMult` | float32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe3c` | `m_fadeMinDist` | float32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe40` | `m_fadeMaxDist` | float32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe44` | `m_flFadeScale` | float32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe48` | `m_flShadowStrength` | float32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe4c` | `m_nObjectCulling` | uint8 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe4d` | `m_nRequiredDecalRtEncoding` | [DecalRtEncoding_t](../scenesystem/DecalRtEncoding_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe50` | `m_bodyGroupChoices` | CUtlOrderedMap< CGlobalSymbol, int32 > | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe78` | `m_vecViewOffset` | [CNetworkViewOffsetVector](../server/CNetworkViewOffsetVector.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xf58` | `m_pClientAlphaProperty` | [CClientAlphaProperty](../client/CClientAlphaProperty.md)* | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xf60` | `m_ClientOverrideTint` | Color | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xf64` | `m_bUseClientOverrideTint` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xfa0` | `m_bvDisabledHitGroups` | uint32[1] | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MKV3TransferSaveOpsForField GetHitgroupDisableListSaveRestoreOps` |
| `0xfb0` | `m_graphControllerManager` | [CAnimGraphControllerManager](../server/CAnimGraphControllerManager.md) | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1048` | `m_pMainGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1050` | `m_bInitiallyPopulateInterpHistory` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1052` | `m_bSuppressAnimEventSounds` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1058` | `m_OnLayerCycleUpdated` | CEntityOutputTemplate< float32 > | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1078` | `m_OnExternalChoreoGraphChanged` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1098` | `m_bAnimGraphUpdateEnabled` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1099` | `m_bAnimationUpdateScheduled` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MNotSaved` |
| `0x109c` | `m_vecForce` | Vector | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MNotSaved` |
| `0x10a8` | `m_nForceBone` | int32 | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MNotSaved` |
| `0x10b0` | `m_pClientsideRagdoll` | [CBaseAnimGraph](../server/CBaseAnimGraph.md)* | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MNotSaved` |
| `0x10b8` | `m_bBuiltRagdoll` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MNotSaved` |
| `0x10c8` | `m_pRagdollControl` | [IPhysicsRagdollControl](../vphysics2/IPhysicsRagdollControl.md)* | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MPhysPtr` |
| `0x10d0` | `m_RagdollPose` | [PhysicsRagdollPose_t](../server/PhysicsRagdollPose_t.md) | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1118` | `m_bRagdollEnabled` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1119` | `m_bRagdollClientSide` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MNotSaved` |
| `0x1128` | `m_bHasAnimatedMaterialAttributes` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MNotSaved` |
| `0x1180` | `m_bModelOverrodeBlockLOS` | bool | [CBaseProp](../server/CBaseProp.md) |  |
| `0x1184` | `m_iShapeType` | int32 | [CBaseProp](../server/CBaseProp.md) |  |
| `0x1188` | `m_bConformToCollisionBounds` | bool | [CBaseProp](../server/CBaseProp.md) |  |
| `0x1190` | `m_mPreferredCatchTransform` | CTransform | [CBaseProp](../server/CBaseProp.md) |  |
