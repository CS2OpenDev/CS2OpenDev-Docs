---
layout: default
title: CWeaponSSG08
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CWeaponSSG08

# CWeaponSSG08

**Kind:** class · **Size:** 4208 bytes (`0x1070`) · **Align:** 16 · **Module:** server

**Inherits from:** [CCSWeaponBaseGun](../server/CCSWeaponBaseGun.md)

**Relationships:**

```mermaid
classDiagram
    CCSWeaponBaseGun <|-- CWeaponSSG08
    CCSWeaponBase <|-- CCSWeaponBaseGun
    CBasePlayerWeapon <|-- CCSWeaponBase
    CEconEntity <|-- CBasePlayerWeapon
    CBaseAnimGraph <|-- CEconEntity
```

## Memory layout

225 fields (0 declared here, 225 inherited). Offsets are absolute from the object base.

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
| `0x358` | `m_nTakeDamageFlags` | [TakeDamageFlags_t](../!GlobalTypes/TakeDamageFlags_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x360` | `m_nPlatformType` | [EntityPlatformTypes_t](../!GlobalTypes/EntityPlatformTypes_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) |  |
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
| `0x524` | `m_MoveCollide` | [MoveCollide_t](../!GlobalTypes/MoveCollide_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x525` | `m_MoveType` | [MoveType_t](../!GlobalTypes/MoveType_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x526` | `m_nActualMoveType` | [MoveType_t](../!GlobalTypes/MoveType_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) |  |
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
| `0x5f8` | `m_nBloodType` | [BloodType](../!GlobalTypes/BloodType.md) | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x978` | `m_AttributeManager` | [CAttributeContainer](../server/CAttributeContainer.md) | [CEconEntity](../server/CEconEntity.md) |  |
| `0xaf0` | `m_CRenderComponent` | [CRenderComponent](../server/CRenderComponent.md)* | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xaf8` | `m_CHitboxComponent` | [CHitboxComponent](../server/CHitboxComponent.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb10` | `m_pChoreoComponent` | [CChoreoComponent](../server/CChoreoComponent.md)* | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb18` | `m_nDestructiblePartInitialStateDestructed0` | [HitGroup_t](../!GlobalTypes/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb1c` | `m_nDestructiblePartInitialStateDestructed1` | [HitGroup_t](../!GlobalTypes/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb20` | `m_nDestructiblePartInitialStateDestructed2` | [HitGroup_t](../!GlobalTypes/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb24` | `m_nDestructiblePartInitialStateDestructed3` | [HitGroup_t](../!GlobalTypes/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb28` | `m_nDestructiblePartInitialStateDestructed4` | [HitGroup_t](../!GlobalTypes/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb2c` | `m_nDestructiblePartInitialStateDestructed0_PartIndex` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb30` | `m_nDestructiblePartInitialStateDestructed1_PartIndex` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb34` | `m_nDestructiblePartInitialStateDestructed2_PartIndex` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb38` | `m_nDestructiblePartInitialStateDestructed3_PartIndex` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb3c` | `m_nDestructiblePartInitialStateDestructed4_PartIndex` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb40` | `m_bDestructiblePartInitialStateDestructed0_GenerateBreakpieces` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb41` | `m_bDestructiblePartInitialStateDestructed1_GenerateBreakpieces` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb42` | `m_bDestructiblePartInitialStateDestructed2_GenerateBreakpieces` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb43` | `m_bDestructiblePartInitialStateDestructed3_GenerateBreakpieces` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb44` | `m_bDestructiblePartInitialStateDestructed4_GenerateBreakpieces` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb48` | `m_pDestructiblePartsSystemComponent` | [CDestructiblePartsComponent](../server/CDestructiblePartsComponent.md)* | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc70` | `m_OriginalOwnerXuidLow` | uint32 | [CEconEntity](../server/CEconEntity.md) |  |
| `0xc70` | `m_bInitModelEffects` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xc71` | `m_bDoingModelEffects` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xc74` | `m_OriginalOwnerXuidHigh` | uint32 | [CEconEntity](../server/CEconEntity.md) |  |
| `0xc74` | `m_iOldHealth` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xc78` | `m_nFallbackPaintKit` | int32 | [CEconEntity](../server/CEconEntity.md) |  |
| `0xc78` | `m_nRenderMode` | [RenderMode_t](../!GlobalTypes/RenderMode_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc79` | `m_nRenderFX` | [RenderFx_t](../!GlobalTypes/RenderFx_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc7a` | `m_bAllowFadeInView` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc7c` | `m_nFallbackSeed` | int32 | [CEconEntity](../server/CEconEntity.md) |  |
| `0xc80` | `m_flFallbackWear` | float32 | [CEconEntity](../server/CEconEntity.md) |  |
| `0xc84` | `m_nFallbackStatTrak` | int32 | [CEconEntity](../server/CEconEntity.md) |  |
| `0xc88` | `m_hOldProvidee` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > | [CEconEntity](../server/CEconEntity.md) |  |
| `0xc8c` | `m_iOldOwnerClass` | int32 | [CEconEntity](../server/CEconEntity.md) |  |
| `0xc90` | `m_nNextPrimaryAttackTick` | [GameTick_t](../entity2/GameTick_t.md) | [CBasePlayerWeapon](../server/CBasePlayerWeapon.md) |  |
| `0xc94` | `m_flNextPrimaryAttackTickRatio` | float32 | [CBasePlayerWeapon](../server/CBasePlayerWeapon.md) |  |
| `0xc98` | `m_nNextSecondaryAttackTick` | [GameTick_t](../entity2/GameTick_t.md) | [CBasePlayerWeapon](../server/CBasePlayerWeapon.md) |  |
| `0xc98` | `m_clrRender` | Color | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc9c` | `m_flNextSecondaryAttackTickRatio` | float32 | [CBasePlayerWeapon](../server/CBasePlayerWeapon.md) |  |
| `0xca0` | `m_iClip1` | int32 | [CBasePlayerWeapon](../server/CBasePlayerWeapon.md) |  |
| `0xca0` | `m_vecRenderAttributes` | C_UtlVectorEmbeddedNetworkVar< [EntityRenderAttribute_t](../server/EntityRenderAttribute_t.md) > | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xca4` | `m_iClip2` | int32 | [CBasePlayerWeapon](../server/CBasePlayerWeapon.md) |  |
| `0xca8` | `m_pReserveAmmo` | int32[2] | [CBasePlayerWeapon](../server/CBasePlayerWeapon.md) |  |
| `0xcb0` | `m_OnPlayerUse` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBasePlayerWeapon](../server/CBasePlayerWeapon.md) |  |
| `0xcd8` | `m_bRemoveable` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xcd9` | `m_bPlayerAmmoStockOnPickup` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xcda` | `m_bRequireUseToTouch` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xcdc` | `m_iWeaponGameplayAnimState` | [WeaponGameplayAnimState](../!GlobalTypes/WeaponGameplayAnimState.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xce0` | `m_flWeaponGameplayAnimStateTimestamp` | [GameTime_t](../entity2/GameTime_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xce4` | `m_flInspectCancelCompleteTime` | [GameTime_t](../entity2/GameTime_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xce8` | `m_bInspectPending` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xce9` | `m_bInspectShouldLoop` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd14` | `m_nLastEmptySoundCmdNum` | int32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd20` | `m_bRenderToCubemaps` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xd21` | `m_bNoInterpolate` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xd28` | `m_Collision` | [CCollisionProperty](../server/CCollisionProperty.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xd30` | `m_bFireOnEmpty` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd38` | `m_OnPlayerPickup` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd50` | `m_weaponMode` | [CSWeaponMode](../!GlobalTypes/CSWeaponMode.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd54` | `m_flTurningInaccuracyDelta` | float32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd58` | `m_vecTurningInaccuracyEyeDirLast` | Vector | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd64` | `m_flTurningInaccuracy` | float32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd68` | `m_fAccuracyPenalty` | float32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd6c` | `m_flLastAccuracyUpdateTime` | [GameTime_t](../entity2/GameTime_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd70` | `m_fAccuracySmoothedForZoom` | float32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd74` | `m_iRecoilIndex` | int32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd78` | `m_flRecoilIndex` | float32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd7c` | `m_bBurstMode` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd80` | `m_nPostponeFireReadyTicks` | [GameTick_t](../entity2/GameTick_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd84` | `m_flPostponeFireReadyFrac` | float32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd88` | `m_bInReload` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd8c` | `m_nDeployTick` | [GameTick_t](../entity2/GameTick_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd90` | `m_flDroppedAtTime` | [GameTime_t](../entity2/GameTime_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd98` | `m_bIsHauledBack` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd99` | `m_bSilencerOn` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xd9c` | `m_flTimeSilencerSwitchComplete` | [GameTime_t](../entity2/GameTime_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xda0` | `m_flWeaponActionPlaybackRate` | float32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xda4` | `m_iOriginalTeamNumber` | int32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xda8` | `m_iMostRecentTeamNumber` | int32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xdac` | `m_bDroppedNearBuyZone` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xdb0` | `m_flNextAttackRenderTimeOffset` | float32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xdc8` | `m_bCanBePickedUp` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xdc9` | `m_bUseCanOverrideNextOwnerTouchTime` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xdcc` | `m_nextOwnerTouchTime` | [GameTime_t](../entity2/GameTime_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xdd0` | `m_nextPrevOwnerTouchTime` | [GameTime_t](../entity2/GameTime_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xdd8` | `m_nextPrevOwnerUseTime` | [GameTime_t](../entity2/GameTime_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xddc` | `m_hPrevOwner` | CHandle< [CCSPlayerPawn](../server/CCSPlayerPawn.md) > | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xde0` | `m_nDropTick` | [GameTick_t](../entity2/GameTick_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xde0` | `m_Glow` | [CGlowProperty](../server/CGlowProperty.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xde4` | `m_bWasActiveWeaponWhenDropped` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xe04` | `m_donated` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xe08` | `m_fLastShotTime` | [GameTime_t](../entity2/GameTime_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xe0c` | `m_bWasOwnedByCT` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xe0d` | `m_bWasOwnedByTerrorist` | bool | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xe10` | `m_numRemoveUnownedWeaponThink` | int32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xe38` | `m_flGlowBackfaceMult` | float32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe3c` | `m_fadeMinDist` | float32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe40` | `m_fadeMaxDist` | float32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe44` | `m_flFadeScale` | float32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe48` | `m_flShadowStrength` | float32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe4c` | `m_nObjectCulling` | uint8 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe4d` | `m_nRequiredDecalRtEncoding` | [DecalRtEncoding_t](../!GlobalTypes/DecalRtEncoding_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe50` | `m_bodyGroupChoices` | CUtlOrderedMap< CGlobalSymbol, int32 > | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe70` | `m_IronSightController` | [CIronSightController](../server/CIronSightController.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xe78` | `m_vecViewOffset` | [CNetworkViewOffsetVector](../server/CNetworkViewOffsetVector.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xe88` | `m_iIronSightMode` | int32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xe8c` | `m_flLastLOSTraceFailureTime` | [GameTime_t](../entity2/GameTime_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xe90` | `m_flWatTickOffset` | float32 | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xea0` | `m_flLastShakeTime` | [GameTime_t](../entity2/GameTime_t.md) | [CCSWeaponBase](../server/CCSWeaponBase.md) |  |
| `0xf58` | `m_pClientAlphaProperty` | [CClientAlphaProperty](../client/CClientAlphaProperty.md)* | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xf60` | `m_ClientOverrideTint` | Color | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xf64` | `m_bUseClientOverrideTint` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xfa0` | `m_bvDisabledHitGroups` | uint32[1] | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MKV3TransferSaveOpsForField GetHitgroupDisableListSaveRestoreOps` |
| `0xfb0` | `m_graphControllerManager` | [CAnimGraphControllerManager](../server/CAnimGraphControllerManager.md) | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1048` | `m_pMainGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1050` | `m_zoomLevel` | int32 | [CCSWeaponBaseGun](../server/CCSWeaponBaseGun.md) |  |
| `0x1050` | `m_bInitiallyPopulateInterpHistory` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1052` | `m_bSuppressAnimEventSounds` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1054` | `m_iBurstShotsRemaining` | int32 | [CCSWeaponBaseGun](../server/CCSWeaponBaseGun.md) |  |
| `0x1058` | `m_OnLayerCycleUpdated` | CEntityOutputTemplate< float32 > | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x1060` | `m_silencedModelIndex` | int32 | [CCSWeaponBaseGun](../server/CCSWeaponBaseGun.md) |  |
| `0x1064` | `m_inPrecache` | bool | [CCSWeaponBaseGun](../server/CCSWeaponBaseGun.md) |  |
| `0x1065` | `m_bNeedsBoltAction` | bool | [CCSWeaponBaseGun](../server/CCSWeaponBaseGun.md) |  |
| `0x1068` | `m_nRevolverCylinderIdx` | int32 | [CCSWeaponBaseGun](../server/CCSWeaponBaseGun.md) |  |
| `0x106c` | `m_bSkillReloadAvailable` | bool | [CCSWeaponBaseGun](../server/CCSWeaponBaseGun.md) |  |
| `0x106d` | `m_bSkillReloadLiftedReloadKey` | bool | [CCSWeaponBaseGun](../server/CCSWeaponBaseGun.md) |  |
| `0x106e` | `m_bSkillBoltInterruptAvailable` | bool | [CCSWeaponBaseGun](../server/CCSWeaponBaseGun.md) |  |
| `0x106f` | `m_bSkillBoltLiftedFireKey` | bool | [CCSWeaponBaseGun](../server/CCSWeaponBaseGun.md) |  |
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

**Also inherits (secondary base classes):** [IHasAttributes](../server/IHasAttributes.md) — additional-base fields sit at a shifted offset the schema does not record; see each base's own page for its layout.
