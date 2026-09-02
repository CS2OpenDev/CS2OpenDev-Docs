---
title: C_RectLight
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / C_RectLight

# C_RectLight

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 4808 bytes (`0x12c8`) · **Align:** 8 · **Module:** client

**Inherits from:** [C_BarnLight](../client/C_BarnLight.md)

**Relationships:**

```mermaid
classDiagram
    C_BarnLight <|-- C_RectLight
    C_BaseModelEntity <|-- C_BarnLight
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

## Memory layout

206 fields (1 declared here, 205 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_iszPrivateVScripts` | CUtlSymbolLarge | [CEntityInstance](../entity2/CEntityInstance.md) |  |
| `0x10` | `m_pEntity` | [CEntityIdentity](../entity2/CEntityIdentity.md)* | [CEntityInstance](../entity2/CEntityInstance.md) | CEntityIdentity pointer: the entity's identity record (name, class, handle, flags). |
| `0x28` | `m_CScriptComponent` | [CScriptComponent](../entity2/CScriptComponent.md)* | [CEntityInstance](../entity2/CEntityInstance.md) | VScript component attached to the entity, when scripted. |
| `0x30` | `m_CBodyComponent` | [CBodyComponent](../client/CBodyComponent.md)* | [C_BaseEntity](../client/C_BaseEntity.md) |  |
| `0x38` | `m_NetworkTransmitComponent` | [CNetworkTransmitComponent](../server/CNetworkTransmitComponent.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x328` | `m_nLastThinkTick` | [GameTick_t](../entity2/GameTick_t.md) | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x330` | `m_pGameSceneNode` | [CGameSceneNode](../client/CGameSceneNode.md)* | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x338` | `m_pRenderComponent` | [CRenderComponent](../client/CRenderComponent.md)* | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
| `0x340` | `m_pCollision` | [CCollisionProperty](../client/CCollisionProperty.md)* | [C_BaseEntity](../client/C_BaseEntity.md) | `MNotSaved` |
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
| `0xaf0` | `m_CRenderComponent` | [CRenderComponent](../client/CRenderComponent.md)* | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xaf8` | `m_CHitboxComponent` | [CHitboxComponent](../client/CHitboxComponent.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb10` | `m_pChoreoComponent` | [CChoreoComponent](../client/CChoreoComponent.md)* | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb18` | `m_nDestructiblePartInitialStateDestructed0` | [HitGroup_t](../server/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb1c` | `m_nDestructiblePartInitialStateDestructed1` | [HitGroup_t](../server/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb20` | `m_nDestructiblePartInitialStateDestructed2` | [HitGroup_t](../server/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb24` | `m_nDestructiblePartInitialStateDestructed3` | [HitGroup_t](../server/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xb28` | `m_nDestructiblePartInitialStateDestructed4` | [HitGroup_t](../server/HitGroup_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
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
| `0xb48` | `m_pDestructiblePartsSystemComponent` | [CDestructiblePartsComponent](../client/CDestructiblePartsComponent.md)* | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc70` | `m_bInitModelEffects` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xc71` | `m_bDoingModelEffects` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xc74` | `m_iOldHealth` | int32 | [C_BaseModelEntity](../client/C_BaseModelEntity.md) | `MNotSaved` |
| `0xc78` | `m_nRenderMode` | [RenderMode_t](../server/RenderMode_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc79` | `m_nRenderFX` | [RenderFx_t](../server/RenderFx_t.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc7a` | `m_bAllowFadeInView` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xc98` | `m_clrRender` | Color | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xca0` | `m_vecRenderAttributes` | C_UtlVectorEmbeddedNetworkVar< [EntityRenderAttribute_t](../client/EntityRenderAttribute_t.md) > | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xd20` | `m_bRenderToCubemaps` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xd21` | `m_bNoInterpolate` | bool | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xd28` | `m_Collision` | [CCollisionProperty](../client/CCollisionProperty.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
| `0xde0` | `m_Glow` | [CGlowProperty](../client/CGlowProperty.md) | [C_BaseModelEntity](../client/C_BaseModelEntity.md) |  |
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
| `0xfb0` | `m_bEnabled` | bool | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfb4` | `m_nColorMode` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfb8` | `m_Color` | Color | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfbc` | `m_flColorTemperature` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfc0` | `m_flBrightness` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfc4` | `m_flBrightnessScale` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfc8` | `m_nDirectLight` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfcc` | `m_nBakedShadowIndex` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfd0` | `m_nLightPathUniqueId` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfd4` | `m_nLightMapUniqueId` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfd8` | `m_nLuminaireShape` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfdc` | `m_flLuminaireSize` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfe0` | `m_flLuminaireAnisotropy` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xfe8` | `m_LightStyleString` | CUtlString | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xff0` | `m_flLightStyleStartTime` | [GameTime_t](../entity2/GameTime_t.md) | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0xff8` | `m_QueuedLightStyleStrings` | C_NetworkUtlVectorBase< CUtlString > | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1010` | `m_LightStyleEvents` | C_NetworkUtlVectorBase< CUtlString > | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1028` | `m_LightStyleTargets` | C_NetworkUtlVectorBase< CHandle< [C_BaseModelEntity](../client/C_BaseModelEntity.md) > > | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1040` | `m_StyleEvent` | [CEntityIOOutput](../entity2/CEntityIOOutput.md)[4] | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10a0` | `m_hLightCookie` | CStrongHandle< [InfoForResourceTypeCTextureBase](../resourcesystem/InfoForResourceTypeCTextureBase.md) > | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10a8` | `m_flShape` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10ac` | `m_flSoftX` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10b0` | `m_flSoftY` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10b4` | `m_flSkirt` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10b8` | `m_flSkirtNear` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10bc` | `m_vSizeParams` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10c8` | `m_flRange` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10cc` | `m_vShear` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10d8` | `m_nBakeSpecularToCubemaps` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10dc` | `m_vBakeSpecularToCubemapsSize` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10e8` | `m_flBakeSpecularToCubemapsScale` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10ec` | `m_nCastShadows` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10f0` | `m_nShadowMapSize` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10f4` | `m_nShadowPriority` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10f8` | `m_bContactShadow` | bool | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10f9` | `m_bForceShadowsEnabled` | bool | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x10fc` | `m_nBounceLight` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1100` | `m_flBounceScale` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1104` | `m_flMinRoughness` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1108` | `m_vAlternateColor` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1114` | `m_fAlternateColorBrightness` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1118` | `m_nFog` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x111c` | `m_flFogStrength` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1120` | `m_nFogShadows` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1124` | `m_flFogScale` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1128` | `m_flFadeSizeStart` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x112c` | `m_flFadeSizeEnd` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1130` | `m_flShadowFadeSizeStart` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1134` | `m_flShadowFadeSizeEnd` | float32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1138` | `m_bPrecomputedFieldsValid` | bool | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x113c` | `m_vPrecomputedBoundsMins` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1148` | `m_vPrecomputedBoundsMaxs` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1154` | `m_vPrecomputedOBBOrigin` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1160` | `m_vPrecomputedOBBAngles` | QAngle | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x116c` | `m_vPrecomputedOBBExtent` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1178` | `m_nPrecomputedSubFrusta` | int32 | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x117c` | `m_vPrecomputedOBBOrigin0` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1188` | `m_vPrecomputedOBBAngles0` | QAngle | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1194` | `m_vPrecomputedOBBExtent0` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x11a0` | `m_vPrecomputedOBBOrigin1` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x11ac` | `m_vPrecomputedOBBAngles1` | QAngle | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x11b8` | `m_vPrecomputedOBBExtent1` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x11c4` | `m_vPrecomputedOBBOrigin2` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x11d0` | `m_vPrecomputedOBBAngles2` | QAngle | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x11dc` | `m_vPrecomputedOBBExtent2` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x11e8` | `m_vPrecomputedOBBOrigin3` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x11f4` | `m_vPrecomputedOBBAngles3` | QAngle | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1200` | `m_vPrecomputedOBBExtent3` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x120c` | `m_vPrecomputedOBBOrigin4` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1218` | `m_vPrecomputedOBBAngles4` | QAngle | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1224` | `m_vPrecomputedOBBExtent4` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1230` | `m_vPrecomputedOBBOrigin5` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x123c` | `m_vPrecomputedOBBAngles5` | QAngle | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1248` | `m_vPrecomputedOBBExtent5` | Vector | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x1298` | `m_bInitialBoneSetup` | bool | [C_BarnLight](../client/C_BarnLight.md) | `MNotSaved` |
| `0x12a0` | `m_VisClusters` | C_NetworkUtlVectorBase< uint16 > | [C_BarnLight](../client/C_BarnLight.md) |  |
| `0x12c0` | `m_bShowLight` | bool |  |  |
