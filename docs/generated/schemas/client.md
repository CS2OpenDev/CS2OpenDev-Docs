---
layout: default
title: client
parent: Schemas
nav_exclude: true
---

# Module: client

[📊 View UML Diagram](../diagrams/client.md)

484 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [ActiveModelConfig_t](client/ActiveModelConfig_t.md) | class | 112 | 4 |  |
| [AnimGraph2SerializedPoseRecipeSlot_t](client/AnimGraph2SerializedPoseRecipeSlot_t.md) | class | 64 | 1 |  |
| [CAttributeList](client/CAttributeList.md) | class | 120 | 2 |  |
| [CAttributeManager](client/CAttributeManager.md) | class | 80 | 6 |  |
| [CAttributeManager::cached_attribute_float_t](client/CAttributeManager.cached_attribute_float_t.md) | class | 24 | 3 |  |
| [CBarnLightAPI](client/CBarnLightAPI.md) | class | 8 | 0 |  |
| [CBaseAnimGraph](client/CBaseAnimGraph.md) | class | 4480 | 17 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [CBaseAnimGraphAPI](client/CBaseAnimGraphAPI.md) | class | 8 | 0 |  |
| [CBaseAnimGraphAlias_baseanimating](client/CBaseAnimGraphAlias_baseanimating.md) | class | 4480 | 0 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [CBaseAnimGraphController](client/CBaseAnimGraphController.md) | class | 1696 | 32 | [CSkeletonAnimationController](server/CSkeletonAnimationController.md) |
| [CBaseEntity_SharedAPI](client/CBaseEntity_SharedAPI.md) | class | 8 | 0 |  |
| [CBaseFilter](client/CBaseFilter.md) | class | 1592 | 3 | [CLogicalEntity](client/CLogicalEntity.md) |
| [CBaseGrenade_API](client/CBaseGrenade_API.md) | class | 8 | 0 |  |
| [CBaseModelEntityAPI](client/CBaseModelEntityAPI.md) | class | 8 | 0 |  |
| [CBasePlayerController](client/CBasePlayerController.md) | class | 2040 | 17 | [C_BaseEntity](client/C_BaseEntity.md) |
| [CBasePlayerControllerAPI](client/CBasePlayerControllerAPI.md) | class | 8 | 0 |  |
| [CBasePlayerVData](client/CBasePlayerVData.md) | class | 600 | 15 | [CEntitySubclassVDataBase](server/CEntitySubclassVDataBase.md) |
| [CBasePlayerWeaponVData](client/CBasePlayerWeaponVData.md) | class | 1312 | 32 | [CEntitySubclassVDataBase](server/CEntitySubclassVDataBase.md) |
| [CBaseProp](client/CBaseProp.md) | class | 4528 | 4 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [CBaseTriggerAPI](client/CBaseTriggerAPI.md) | class | 8 | 0 |  |
| [CBodyComponent](client/CBodyComponent.md) | class | 120 | 2 | [CEntityComponent](entity2/CEntityComponent.md) |
| [CBodyComponentBaseAnimGraph](client/CBodyComponentBaseAnimGraph.md) | class | 2992 | 1 | [CBodyComponentSkeletonInstance](client/CBodyComponentSkeletonInstance.md) |
| [CBodyComponentBaseModelEntity](client/CBodyComponentBaseModelEntity.md) | class | 1296 | 0 | [CBodyComponentSkeletonInstance](client/CBodyComponentSkeletonInstance.md) |
| [CBodyComponentPoint](client/CBodyComponentPoint.md) | class | 432 | 1 | [CBodyComponent](client/CBodyComponent.md) |
| [CBodyComponentSkeletonInstance](client/CBodyComponentSkeletonInstance.md) | class | 1296 | 1 | [CBodyComponent](client/CBodyComponent.md) |
| [CBombTarget](client/CBombTarget.md) | class | 4256 | 1 | [C_BaseTrigger](client/C_BaseTrigger.md) |
| [CBuoyancyHelper](client/CBuoyancyHelper.md) | class | 280 | 11 |  |
| [CCS2PawnGraphController](client/CCS2PawnGraphController.md) | class | 1344 | 28 | [CCS2WeaponGraphController](client/CCS2WeaponGraphController.md) |
| [CCS2UIPawnGraphController](client/CCS2UIPawnGraphController.md) | class | 472 | 14 | [CAnimGraphControllerBase](server/CAnimGraphControllerBase.md) |
| [CCS2WeaponGraphController](client/CCS2WeaponGraphController.md) | class | 672 | 20 | [CAnimGraphControllerBase](server/CAnimGraphControllerBase.md) |
| [CCSGO_EndOfMatchLineupEnd](client/CCSGO_EndOfMatchLineupEnd.md) | class | 1536 | 0 | [C_CSGO_EndOfMatchLineupEndpoint](client/C_CSGO_EndOfMatchLineupEndpoint.md) |
| [CCSGO_TeamPreviewCharacterPosition_API](client/CCSGO_TeamPreviewCharacterPosition_API.md) | class | 8 | 0 |  |
| [CCSGO_WingmanIntroCharacterPosition](client/CCSGO_WingmanIntroCharacterPosition.md) | class | 5024 | 0 | [C_CSGO_TeamIntroCharacterPosition](client/C_CSGO_TeamIntroCharacterPosition.md) |
| [CCSGO_WingmanIntroCounterTerroristPosition](client/CCSGO_WingmanIntroCounterTerroristPosition.md) | class | 5024 | 0 | [CCSGO_WingmanIntroCharacterPosition](client/CCSGO_WingmanIntroCharacterPosition.md) |
| [CCSGO_WingmanIntroTerroristPosition](client/CCSGO_WingmanIntroTerroristPosition.md) | class | 5024 | 0 | [CCSGO_WingmanIntroCharacterPosition](client/CCSGO_WingmanIntroCharacterPosition.md) |
| [CCSGameModeRules](client/CCSGameModeRules.md) | class | 48 | 1 |  |
| [CCSGameModeRules_ArmsRace](client/CCSGameModeRules_ArmsRace.md) | class | 72 | 1 | [CCSGameModeRules](client/CCSGameModeRules.md) |
| [CCSGameModeRules_Deathmatch](client/CCSGameModeRules_Deathmatch.md) | class | 64 | 3 | [CCSGameModeRules](client/CCSGameModeRules.md) |
| [CCSGameModeRules_Noop](client/CCSGameModeRules_Noop.md) | class | 48 | 0 | [CCSGameModeRules](client/CCSGameModeRules.md) |
| [CCSObserver_CameraServices](client/CCSObserver_CameraServices.md) | class | 688 | 1 | [CCSPlayerBase_CameraServices](client/CCSPlayerBase_CameraServices.md) |
| [CCSObserver_MovementServices](client/CCSObserver_MovementServices.md) | class | 600 | 0 | [CPlayer_MovementServices](client/CPlayer_MovementServices.md) |
| [CCSObserver_ObserverServices](client/CCSObserver_ObserverServices.md) | class | 240 | 1 | [CPlayer_ObserverServices](client/CPlayer_ObserverServices.md) |
| [CCSObserver_UseServices](client/CCSObserver_UseServices.md) | class | 72 | 0 | [CPlayer_UseServices](client/CPlayer_UseServices.md) |
| [CCSPlayerBase_CameraServices](client/CCSPlayerBase_CameraServices.md) | class | 680 | 6 | [CPlayer_CameraServices](client/CPlayer_CameraServices.md) |
| [CCSPlayerController](client/CCSPlayerController.md) | class | 2400 | 68 | [CBasePlayerController](client/CBasePlayerController.md) |
| [CCSPlayerController_API](client/CCSPlayerController_API.md) | class | 8 | 0 |  |
| [CCSPlayerController_ActionTrackingServices](client/CCSPlayerController_ActionTrackingServices.md) | class | 312 | 5 | [CPlayerControllerComponent](server/CPlayerControllerComponent.md) |
| [CCSPlayerController_DamageServices](client/CCSPlayerController_DamageServices.md) | class | 176 | 2 | [CPlayerControllerComponent](server/CPlayerControllerComponent.md) |
| [CCSPlayerController_InGameMoneyServices](client/CCSPlayerController_InGameMoneyServices.md) | class | 80 | 4 | [CPlayerControllerComponent](server/CPlayerControllerComponent.md) |
| [CCSPlayerController_InventoryServices](client/CCSPlayerController_InventoryServices.md) | class | 240 | 9 | [CPlayerControllerComponent](server/CPlayerControllerComponent.md) |
| [CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t](client/CCSPlayerController_InventoryServices.NetworkedLoadoutSlot_t.md) | class | 200 | 3 |  |
| [CCSPlayerLegacyJump](client/CCSPlayerLegacyJump.md) | class | 24 | 2 |  |
| [CCSPlayerModernJump](client/CCSPlayerModernJump.md) | class | 56 | 9 |  |
| [CCSPlayer_ActionTrackingServices](client/CCSPlayer_ActionTrackingServices.md) | class | 304 | 4 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_AimPunchServices](client/CCSPlayer_AimPunchServices.md) | class | 232 | 6 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_BulletServices](client/CCSPlayer_BulletServices.md) | class | 168 | 1 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_BuyServices](client/CCSPlayer_BuyServices.md) | class | 176 | 1 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_CameraServices](client/CCSPlayer_CameraServices.md) | class | 832 | 2 | [CCSPlayerBase_CameraServices](client/CCSPlayerBase_CameraServices.md) |
| [CCSPlayer_DamageReactServices](client/CCSPlayer_DamageReactServices.md) | class | 80 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_GlowServices](client/CCSPlayer_GlowServices.md) | class | 80 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_HostageServices](client/CCSPlayer_HostageServices.md) | class | 80 | 2 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_ItemServices](client/CCSPlayer_ItemServices.md) | class | 80 | 2 | [CPlayer_ItemServices](client/CPlayer_ItemServices.md) |
| [CCSPlayer_MovementServices](client/CCSPlayer_MovementServices.md) | class | 4064 | 49 | [CPlayer_MovementServices_Humanoid](client/CPlayer_MovementServices_Humanoid.md) |
| [CCSPlayer_PingServices](client/CCSPlayer_PingServices.md) | class | 80 | 1 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_UseServices](client/CCSPlayer_UseServices.md) | class | 72 | 0 | [CPlayer_UseServices](client/CPlayer_UseServices.md) |
| [CCSPlayer_WaterServices](client/CCSPlayer_WaterServices.md) | class | 112 | 3 | [CPlayer_WaterServices](client/CPlayer_WaterServices.md) |
| [CCSPlayer_WeaponServices](client/CCSPlayer_WeaponServices.md) | class | 5584 | 5 | [CPlayer_WeaponServices](client/CPlayer_WeaponServices.md) |
| [CCSWeaponBaseVData](client/CCSWeaponBaseVData.md) | class | 2216 | 84 | [CBasePlayerWeaponVData](client/CBasePlayerWeaponVData.md) |
| [CCSWeaponBase_API](client/CCSWeaponBase_API.md) | class | 8 | 0 |  |
| [CCS_PortraitWorldCallbackHandler](client/CCS_PortraitWorldCallbackHandler.md) | class | 1544 | 0 | [C_BaseEntity](client/C_BaseEntity.md) |
| [CCashStack](client/CCashStack.md) | class | 4024 | 1 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [CChoreoComponent](client/CChoreoComponent.md) | class | 128 | 6 |  |
| [CChoreoInfoTarget](client/CChoreoInfoTarget.md) | class | 1536 | 0 | [C_PointEntity](client/C_PointEntity.md) |
| [CCitadelSoundOpvarSetOBB](client/CCitadelSoundOpvarSetOBB.md) | class | 1640 | 8 | [C_BaseEntity](client/C_BaseEntity.md) |
| [CClientAlphaProperty](client/CClientAlphaProperty.md) | class | 48 | 11 | [IClientAlphaProperty](client/IClientAlphaProperty.md) |
| [CCollisionProperty](client/CCollisionProperty.md) | class | 184 | 17 |  |
| [CDamageRecord](client/CDamageRecord.md) | class | 120 | 15 |  |
| [CDestructiblePartsComponent](client/CDestructiblePartsComponent.md) | class | 112 | 4 |  |
| [CEconItemAttribute](client/CEconItemAttribute.md) | class | 72 | 5 |  |
| [CEffectData](client/CEffectData.md) | class | 120 | 20 |  |
| [CEnvCombinedLightProbeVolumeAPI](client/CEnvCombinedLightProbeVolumeAPI.md) | class | 8 | 0 |  |
| [CEnvCubemapAPI](client/CEnvCubemapAPI.md) | class | 8 | 0 |  |
| [CEnvLightProbeVolumeAPI](client/CEnvLightProbeVolumeAPI.md) | class | 8 | 0 |  |
| [CEnvSkyAPI](client/CEnvSkyAPI.md) | class | 8 | 0 |  |
| [CEnvSoundscape](client/CEnvSoundscape.md) | class | 1680 | 11 | [C_BaseEntity](client/C_BaseEntity.md) |
| [CEnvSoundscapeAlias_snd_soundscape](client/CEnvSoundscapeAlias_snd_soundscape.md) | class | 1680 | 0 | [CEnvSoundscape](client/CEnvSoundscape.md) |
| [CEnvSoundscapeProxy](client/CEnvSoundscapeProxy.md) | class | 1688 | 1 | [CEnvSoundscape](client/CEnvSoundscape.md) |
| [CEnvSoundscapeProxyAlias_snd_soundscape_proxy](client/CEnvSoundscapeProxyAlias_snd_soundscape_proxy.md) | class | 1688 | 0 | [CEnvSoundscapeProxy](client/CEnvSoundscapeProxy.md) |
| [CEnvSoundscapeTriggerable](client/CEnvSoundscapeTriggerable.md) | class | 1680 | 0 | [CEnvSoundscape](client/CEnvSoundscape.md) |
| [CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable](client/CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable.md) | class | 1680 | 0 | [CEnvSoundscapeTriggerable](client/CEnvSoundscapeTriggerable.md) |
| [CEnvWindSharedAPI](client/CEnvWindSharedAPI.md) | class | 8 | 0 |  |
| [CExplosionTypeData](client/CExplosionTypeData.md) | class | 256 | 5 |  |
| [CFilterAttributeInt](client/CFilterAttributeInt.md) | class | 1600 | 1 | [CBaseFilter](client/CBaseFilter.md) |
| [CFilterClass](client/CFilterClass.md) | class | 1600 | 1 | [CBaseFilter](client/CBaseFilter.md) |
| [CFilterLOS](client/CFilterLOS.md) | class | 1592 | 0 | [CBaseFilter](client/CBaseFilter.md) |
| [CFilterMassGreater](client/CFilterMassGreater.md) | class | 1600 | 1 | [CBaseFilter](client/CBaseFilter.md) |
| [CFilterModel](client/CFilterModel.md) | class | 1600 | 1 | [CBaseFilter](client/CBaseFilter.md) |
| [CFilterMultiple](client/CFilterMultiple.md) | class | 1720 | 3 | [CBaseFilter](client/CBaseFilter.md) |
| [CFilterMultipleAPI](client/CFilterMultipleAPI.md) | class | 8 | 0 |  |
| [CFilterName](client/CFilterName.md) | class | 1600 | 1 | [CBaseFilter](client/CBaseFilter.md) |
| [CFilterProximity](client/CFilterProximity.md) | class | 1600 | 1 | [CBaseFilter](client/CBaseFilter.md) |
| [CFilterTeam](client/CFilterTeam.md) | class | 1600 | 1 | [CBaseFilter](client/CBaseFilter.md) |
| [CFlashbangProjectile_API](client/CFlashbangProjectile_API.md) | class | 8 | 0 |  |
| [CFlashlightEffect](client/CFlashlightEffect.md) | class | 736 | 13 |  |
| [CFootstepControl_API](client/CFootstepControl_API.md) | class | 8 | 0 |  |
| [CFuncRetakeBarrier](client/CFuncRetakeBarrier.md) | class | 5088 | 0 | [C_DynamicProp](client/C_DynamicProp.md) |
| [CFuncWater](client/CFuncWater.md) | class | 4296 | 1 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [CGameSceneNode](client/CGameSceneNode.md) | class | 304 | 34 |  |
| [CGameSceneNodeHandle](client/CGameSceneNodeHandle.md) | class | 16 | 2 |  |
| [CGlobalLightBase](client/CGlobalLightBase.md) | class | 1216 | 43 |  |
| [CGlowProperty](client/CGlowProperty.md) | class | 88 | 11 |  |
| [CGrenadeTracer](client/CGrenadeTracer.md) | class | 5200 | 2 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [CGrenadeTracer_API](client/CGrenadeTracer_API.md) | class | 8 | 0 |  |
| [CHitboxComponent](client/CHitboxComponent.md) | class | 24 | 1 | [CEntityComponent](entity2/CEntityComponent.md) |
| [CHostageRescueZone](client/CHostageRescueZone.md) | class | 4272 | 0 | [CHostageRescueZoneShim](client/CHostageRescueZoneShim.md) |
| [CHostageRescueZoneShim](client/CHostageRescueZoneShim.md) | class | 4248 | 0 | [C_BaseTrigger](client/C_BaseTrigger.md) |
| [CInfoDynamicShadowHint](client/CInfoDynamicShadowHint.md) | class | 1560 | 5 | [C_PointEntity](client/C_PointEntity.md) |
| [CInfoDynamicShadowHintBox](client/CInfoDynamicShadowHintBox.md) | class | 1584 | 2 | [CInfoDynamicShadowHint](client/CInfoDynamicShadowHint.md) |
| [CInfoFan](client/CInfoFan.md) | class | 1624 | 4 | [C_PointEntity](client/C_PointEntity.md) |
| [CInfoOffscreenPanoramaTexture](client/CInfoOffscreenPanoramaTexture.md) | class | 2056 | 12 | [C_PointEntity](client/C_PointEntity.md) |
| [CInfoParticleTarget](client/CInfoParticleTarget.md) | class | 1536 | 0 | [C_PointEntity](client/C_PointEntity.md) |
| [CInfoTarget](client/CInfoTarget.md) | class | 1536 | 0 | [C_PointEntity](client/C_PointEntity.md) |
| [CInfoWorldLayer](client/CInfoWorldLayer.md) | class | 1592 | 8 | [C_BaseEntity](client/C_BaseEntity.md) |
| [CInterpolatedValue](client/CInterpolatedValue.md) | class | 20 | 5 |  |
| [CInventoryImageData](client/CInventoryImageData.md) | class | 248 | 3 |  |
| [CLightComponent](client/CLightComponent.md) | class | 496 | 70 | [CEntityComponent](entity2/CEntityComponent.md) |
| [CLightEntityAPI](client/CLightEntityAPI.md) | class | 8 | 0 |  |
| [CLogicRelay](client/CLogicRelay.md) | class | 1592 | 7 | [CLogicalEntity](client/CLogicalEntity.md) |
| [CLogicRelayAPI](client/CLogicRelayAPI.md) | class | 8 | 0 |  |
| [CLogicalEntity](client/CLogicalEntity.md) | class | 1536 | 0 | [C_BaseEntity](client/C_BaseEntity.md) |
| [CMapInfo](client/CMapInfo.md) | class | 1584 | 15 | [C_PointEntity](client/C_PointEntity.md) |
| [CMapInfo_API](client/CMapInfo_API.md) | class | 8 | 0 |  |
| [CModelState](client/CModelState.md) | class | 688 | 14 |  |
| [CNetworkedSequenceOperation](client/CNetworkedSequenceOperation.md) | class | 40 | 8 |  |
| [CParticleSystemAPI](client/CParticleSystemAPI.md) | class | 8 | 0 |  |
| [CPathNode](client/CPathNode.md) | class | 1632 | 6 | [C_PointEntity](client/C_PointEntity.md) |
| [CPathQueryComponent](client/CPathQueryComponent.md) | class | 160 | 0 | [CEntityComponent](entity2/CEntityComponent.md), [CPathQueryUtil](server/CPathQueryUtil.md) |
| [CPathSimple](client/CPathSimple.md) | class | 1808 | 3 | [C_BaseEntity](client/C_BaseEntity.md) |
| [CPathSimpleAPI](client/CPathSimpleAPI.md) | class | 8 | 0 |  |
| [CPathWithDynamicNodes](client/CPathWithDynamicNodes.md) | class | 1872 | 2 | [CPathSimple](client/CPathSimple.md) |
| [CPlayerSprayDecalRenderHelper](client/CPlayerSprayDecalRenderHelper.md) | class | 48 | 0 |  |
| [CPlayer_AutoaimServices](client/CPlayer_AutoaimServices.md) | class | 72 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_CameraServices](client/CPlayer_CameraServices.md) | class | 656 | 20 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_FlashlightServices](client/CPlayer_FlashlightServices.md) | class | 72 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_ItemServices](client/CPlayer_ItemServices.md) | class | 72 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_MovementServices](client/CPlayer_MovementServices.md) | class | 600 | 18 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_MovementServices_Humanoid](client/CPlayer_MovementServices_Humanoid.md) | class | 648 | 6 | [CPlayer_MovementServices](client/CPlayer_MovementServices.md) |
| [CPlayer_ObserverServices](client/CPlayer_ObserverServices.md) | class | 96 | 6 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_UseServices](client/CPlayer_UseServices.md) | class | 72 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_WaterServices](client/CPlayer_WaterServices.md) | class | 72 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_WeaponServices](client/CPlayer_WeaponServices.md) | class | 168 | 4 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPointChildModifier](client/CPointChildModifier.md) | class | 1544 | 1 | [C_PointEntity](client/C_PointEntity.md) |
| [CPointOffScreenIndicatorUi](client/CPointOffScreenIndicatorUi.md) | class | 4640 | 4 | [C_PointClientUIWorldPanel](client/C_PointClientUIWorldPanel.md) |
| [CPointOrient](client/CPointOrient.md) | class | 1568 | 7 | [C_BaseEntity](client/C_BaseEntity.md) |
| [CPointTemplate](client/CPointTemplate.md) | class | 1688 | 12 | [CLogicalEntity](client/CLogicalEntity.md) |
| [CPointTemplateAPI](client/CPointTemplateAPI.md) | class | 8 | 0 |  |
| [CPointValueRemapperAPI](client/CPointValueRemapperAPI.md) | class | 8 | 0 |  |
| [CPrecipitationVData](client/CPrecipitationVData.md) | class | 752 | 11 | [CEntitySubclassVDataBase](server/CEntitySubclassVDataBase.md) |
| [CPropDataComponent](client/CPropDataComponent.md) | class | 64 | 10 | [CEntityComponent](entity2/CEntityComponent.md) |
| [CPulseCell_LerpCameraSettings](client/CPulseCell_LerpCameraSettings.md) | class | 328 | 3 | [CPulseCell_BaseLerp](pulse_runtime_lib/CPulseCell_BaseLerp.md) |
| [CPulseCell_LerpCameraSettings::CursorState_t](client/CPulseCell_LerpCameraSettings.CursorState_t.md) | class | 44 | 3 | [CPulseCell_BaseLerp::CursorState_t](pulse_runtime_lib/CPulseCell_BaseLerp.CursorState_t.md) |
| [CPulseCell_PlaySequence](client/CPulseCell_PlaySequence.md) | class | 320 | 3 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_PlaySequence::CursorState_t](client/CPulseCell_PlaySequence.CursorState_t.md) | class | 4 | 1 |  |
| [CPulseCell_Step_EntFire](client/CPulseCell_Step_EntFire.md) | class | 80 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseGameBlackboard](client/CPulseGameBlackboard.md) | class | 1560 | 2 | [C_BaseEntity](client/C_BaseEntity.md) |
| [CRagdollManager](client/CRagdollManager.md) | class | 1544 | 1 | [C_BaseEntity](client/C_BaseEntity.md) |
| [CRenderComponent](client/CRenderComponent.md) | class | 208 | 5 | [CEntityComponent](entity2/CEntityComponent.md) |
| [CSMatchStats_t](client/CSMatchStats_t.md) | class | 128 | 5 | [CSPerRoundStats_t](client/CSPerRoundStats_t.md) |
| [CSPerRoundStats_t](client/CSPerRoundStats_t.md) | class | 104 | 13 |  |
| [CServerOnlyModelEntity](client/CServerOnlyModelEntity.md) | class | 4016 | 0 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [CSkeletonInstance](client/CSkeletonInstance.md) | class | 1168 | 7 | [CGameSceneNode](client/CGameSceneNode.md) |
| [CSkyboxReference](client/CSkyboxReference.md) | class | 1544 | 2 | [C_BaseEntity](client/C_BaseEntity.md) |
| [CSoundOpvarSetBoxEntity](client/CSoundOpvarSetBoxEntity.md) | class | 1568 | 0 | [C_SoundOpvarSetPointEntity](client/C_SoundOpvarSetPointEntity.md) |
| [CSpriteOriented](client/CSpriteOriented.md) | class | 4144 | 0 | [C_Sprite](client/C_Sprite.md) |
| [CTakeDamageResultAPI](client/CTakeDamageResultAPI.md) | class | 8 | 0 |  |
| [CTimeline](client/CTimeline.md) | class | 552 | 7 | [IntervalTimer](client/IntervalTimer.md) |
| [CTriggerFan](client/CTriggerFan.md) | class | 4352 | 9 | [C_BaseTrigger](client/C_BaseTrigger.md) |
| [CWaterSplasher](client/CWaterSplasher.md) | class | 4016 | 0 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_AK47](client/C_AK47.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_AttributeContainer](client/C_AttributeContainer.md) | class | 1232 | 3 | [CAttributeManager](client/CAttributeManager.md) |
| [C_BarnLight](client/C_BarnLight.md) | class | 4800 | 76 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_BaseButton](client/C_BaseButton.md) | class | 4032 | 3 | [C_BaseToggle](client/C_BaseToggle.md) |
| [C_BaseCSGrenade](client/C_BaseCSGrenade.md) | class | 7584 | 14 | [C_CSWeaponBase](client/C_CSWeaponBase.md) |
| [C_BaseCSGrenadeProjectile](client/C_BaseCSGrenadeProjectile.md) | class | 4704 | 16 | [C_BaseGrenade](client/C_BaseGrenade.md) |
| [C_BaseClientUIEntity](client/C_BaseClientUIEntity.md) | class | 4064 | 4 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_BaseCombatCharacter](client/C_BaseCombatCharacter.md) | class | 4616 | 6 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_BaseDoor](client/C_BaseDoor.md) | class | 4024 | 1 | [C_BaseToggle](client/C_BaseToggle.md) |
| [C_BaseEntity](client/C_BaseEntity.md) | class | 1536 | 82 | [CEntityInstance](entity2/CEntityInstance.md) |
| [C_BaseEntityAPI](client/C_BaseEntityAPI.md) | class | 8 | 0 |  |
| [C_BaseGrenade](client/C_BaseGrenade.md) | class | 4552 | 12 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_BaseModelEntity](client/C_BaseModelEntity.md) | class | 4016 | 44 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_BaseModelEntity::Emphasized_Phoneme](client/C_BaseModelEntity.Emphasized_Phoneme.md) | class | 32 | 5 |  |
| [C_BasePlayerPawn](client/C_BasePlayerPawn.md) | class | 5088 | 28 | [C_BaseCombatCharacter](client/C_BaseCombatCharacter.md) |
| [C_BasePlayerWeapon](client/C_BasePlayerWeapon.md) | class | 5928 | 7 | [C_EconEntity](client/C_EconEntity.md) |
| [C_BasePropDoor](client/C_BasePropDoor.md) | class | 5120 | 8 | [C_DynamicProp](client/C_DynamicProp.md) |
| [C_BaseToggle](client/C_BaseToggle.md) | class | 4016 | 0 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_BaseTrigger](client/C_BaseTrigger.md) | class | 4248 | 12 | [C_BaseToggle](client/C_BaseToggle.md) |
| [C_Beam](client/C_Beam.md) | class | 4200 | 23 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_Breakable](client/C_Breakable.md) | class | 4016 | 0 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_BreakableProp](client/C_BreakableProp.md) | class | 4848 | 29 | [CBaseProp](client/CBaseProp.md) |
| [C_BulletHitModel](client/C_BulletHitModel.md) | class | 4560 | 6 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_C4](client/C_C4.md) | class | 7456 | 10 | [C_CSWeaponBase](client/C_CSWeaponBase.md) |
| [C_CS2HudModelAddon](client/C_CS2HudModelAddon.md) | class | 4688 | 0 | [C_LateUpdatedAnimating](client/C_LateUpdatedAnimating.md) |
| [C_CS2HudModelArms](client/C_CS2HudModelArms.md) | class | 4992 | 0 | [C_CS2HudModelBase](client/C_CS2HudModelBase.md) |
| [C_CS2HudModelBase](client/C_CS2HudModelBase.md) | class | 4720 | 0 | [C_LateUpdatedAnimating](client/C_LateUpdatedAnimating.md) |
| [C_CS2HudModelWeapon](client/C_CS2HudModelWeapon.md) | class | 4784 | 0 | [C_CS2HudModelBase](client/C_CS2HudModelBase.md) |
| [C_CS2WeaponModuleBase](client/C_CS2WeaponModuleBase.md) | class | 4488 | 0 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_CSGO_CounterTerroristTeamIntroCamera](client/C_CSGO_CounterTerroristTeamIntroCamera.md) | class | 1680 | 0 | [C_CSGO_TeamPreviewCamera](client/C_CSGO_TeamPreviewCamera.md) |
| [C_CSGO_CounterTerroristWingmanIntroCamera](client/C_CSGO_CounterTerroristWingmanIntroCamera.md) | class | 1680 | 0 | [C_CSGO_TeamPreviewCamera](client/C_CSGO_TeamPreviewCamera.md) |
| [C_CSGO_EndOfMatchCamera](client/C_CSGO_EndOfMatchCamera.md) | class | 1680 | 0 | [C_CSGO_TeamPreviewCamera](client/C_CSGO_TeamPreviewCamera.md) |
| [C_CSGO_EndOfMatchCharacterPosition](client/C_CSGO_EndOfMatchCharacterPosition.md) | class | 5024 | 0 | [C_CSGO_TeamPreviewCharacterPosition](client/C_CSGO_TeamPreviewCharacterPosition.md) |
| [C_CSGO_EndOfMatchLineupEndpoint](client/C_CSGO_EndOfMatchLineupEndpoint.md) | class | 1536 | 0 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_CSGO_EndOfMatchLineupStart](client/C_CSGO_EndOfMatchLineupStart.md) | class | 1536 | 0 | [C_CSGO_EndOfMatchLineupEndpoint](client/C_CSGO_EndOfMatchLineupEndpoint.md) |
| [C_CSGO_MapPreviewCameraPath](client/C_CSGO_MapPreviewCameraPath.md) | class | 1672 | 14 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_CSGO_MapPreviewCameraPathNode](client/C_CSGO_MapPreviewCameraPathNode.md) | class | 1616 | 10 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_CSGO_MapPreviewCameraPathNode_API](client/C_CSGO_MapPreviewCameraPathNode_API.md) | class | 8 | 0 |  |
| [C_CSGO_MapPreviewCameraPath_API](client/C_CSGO_MapPreviewCameraPath_API.md) | class | 8 | 0 |  |
| [C_CSGO_PreviewModel](client/C_CSGO_PreviewModel.md) | class | 5776 | 4 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_CSGO_PreviewModelAlias_csgo_item_previewmodel](client/C_CSGO_PreviewModelAlias_csgo_item_previewmodel.md) | class | 5776 | 0 | [C_CSGO_PreviewModel](client/C_CSGO_PreviewModel.md) |
| [C_CSGO_PreviewModel_API](client/C_CSGO_PreviewModel_API.md) | class | 8 | 0 |  |
| [C_CSGO_PreviewPlayer](client/C_CSGO_PreviewPlayer.md) | class | 13584 | 2 | [C_CSPlayerPawn](client/C_CSPlayerPawn.md) |
| [C_CSGO_PreviewPlayerAlias_csgo_player_previewmodel](client/C_CSGO_PreviewPlayerAlias_csgo_player_previewmodel.md) | class | 13584 | 0 | [C_CSGO_PreviewPlayer](client/C_CSGO_PreviewPlayer.md) |
| [C_CSGO_PreviewPlayer_API](client/C_CSGO_PreviewPlayer_API.md) | class | 8 | 0 |  |
| [C_CSGO_TeamIntroCharacterPosition](client/C_CSGO_TeamIntroCharacterPosition.md) | class | 5024 | 0 | [C_CSGO_TeamPreviewCharacterPosition](client/C_CSGO_TeamPreviewCharacterPosition.md) |
| [C_CSGO_TeamIntroCounterTerroristPosition](client/C_CSGO_TeamIntroCounterTerroristPosition.md) | class | 5024 | 0 | [C_CSGO_TeamIntroCharacterPosition](client/C_CSGO_TeamIntroCharacterPosition.md) |
| [C_CSGO_TeamIntroTerroristPosition](client/C_CSGO_TeamIntroTerroristPosition.md) | class | 5024 | 0 | [C_CSGO_TeamIntroCharacterPosition](client/C_CSGO_TeamIntroCharacterPosition.md) |
| [C_CSGO_TeamPreviewCamera](client/C_CSGO_TeamPreviewCamera.md) | class | 1680 | 1 | [C_CSGO_MapPreviewCameraPath](client/C_CSGO_MapPreviewCameraPath.md) |
| [C_CSGO_TeamPreviewCamera_API](client/C_CSGO_TeamPreviewCamera_API.md) | class | 8 | 0 |  |
| [C_CSGO_TeamPreviewCharacterPosition](client/C_CSGO_TeamPreviewCharacterPosition.md) | class | 5024 | 8 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_CSGO_TeamPreviewModel](client/C_CSGO_TeamPreviewModel.md) | class | 13584 | 0 | [C_CSGO_PreviewPlayer](client/C_CSGO_PreviewPlayer.md) |
| [C_CSGO_TeamSelectCamera](client/C_CSGO_TeamSelectCamera.md) | class | 1680 | 0 | [C_CSGO_TeamPreviewCamera](client/C_CSGO_TeamPreviewCamera.md) |
| [C_CSGO_TeamSelectCharacterPosition](client/C_CSGO_TeamSelectCharacterPosition.md) | class | 5024 | 0 | [C_CSGO_TeamPreviewCharacterPosition](client/C_CSGO_TeamPreviewCharacterPosition.md) |
| [C_CSGO_TeamSelectCounterTerroristPosition](client/C_CSGO_TeamSelectCounterTerroristPosition.md) | class | 5024 | 0 | [C_CSGO_TeamSelectCharacterPosition](client/C_CSGO_TeamSelectCharacterPosition.md) |
| [C_CSGO_TeamSelectTerroristPosition](client/C_CSGO_TeamSelectTerroristPosition.md) | class | 5024 | 0 | [C_CSGO_TeamSelectCharacterPosition](client/C_CSGO_TeamSelectCharacterPosition.md) |
| [C_CSGO_TerroristTeamIntroCamera](client/C_CSGO_TerroristTeamIntroCamera.md) | class | 1680 | 0 | [C_CSGO_TeamPreviewCamera](client/C_CSGO_TeamPreviewCamera.md) |
| [C_CSGO_TerroristWingmanIntroCamera](client/C_CSGO_TerroristWingmanIntroCamera.md) | class | 1680 | 0 | [C_CSGO_TeamPreviewCamera](client/C_CSGO_TeamPreviewCamera.md) |
| [C_CSGameRules](client/C_CSGameRules.md) | class | 20320 | 98 | [C_TeamplayRules](client/C_TeamplayRules.md) |
| [C_CSGameRulesProxy](client/C_CSGameRulesProxy.md) | class | 1544 | 1 | [C_GameRulesProxy](client/C_GameRulesProxy.md) |
| [C_CSMinimapBoundary](client/C_CSMinimapBoundary.md) | class | 1536 | 0 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_CSObserverPawn](client/C_CSObserverPawn.md) | class | 5256 | 1 | [C_CSPlayerPawnBase](client/C_CSPlayerPawnBase.md) |
| [C_CSObserverPawn_API](client/C_CSObserverPawn_API.md) | class | 8 | 0 |  |
| [C_CSPetPlacement](client/C_CSPetPlacement.md) | class | 1536 | 0 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_CSPlayerPawn](client/C_CSPlayerPawn.md) | class | 13424 | 102 | [C_CSPlayerPawnBase](client/C_CSPlayerPawnBase.md) |
| [C_CSPlayerPawnBase](client/C_CSPlayerPawnBase.md) | class | 5248 | 26 | [C_BasePlayerPawn](client/C_BasePlayerPawn.md) |
| [C_CSPlayerPawnBase_API](client/C_CSPlayerPawnBase_API.md) | class | 8 | 0 |  |
| [C_CSPlayerPawn_API](client/C_CSPlayerPawn_API.md) | class | 8 | 0 |  |
| [C_CSPlayerResource](client/C_CSPlayerResource.md) | class | 1688 | 10 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_CSTeam](client/C_CSTeam.md) | class | 2408 | 10 | [C_Team](client/C_Team.md) |
| [C_CSWeaponBase](client/C_CSWeaponBase.md) | class | 7392 | 54 | [C_BasePlayerWeapon](client/C_BasePlayerWeapon.md) |
| [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) | class | 7440 | 7 | [C_CSWeaponBase](client/C_CSWeaponBase.md) |
| [C_CSWeaponBaseShotgun](client/C_CSWeaponBaseShotgun.md) | class | 7392 | 0 | [C_CSWeaponBase](client/C_CSWeaponBase.md) |
| [C_Chicken](client/C_Chicken.md) | class | 6320 | 5 | [C_DynamicProp](client/C_DynamicProp.md), [IHasAttributes](server/IHasAttributes.md) |
| [C_ClientRagdoll](client/C_ClientRagdoll.md) | class | 4632 | 14 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_ColorCorrection](client/C_ColorCorrection.md) | class | 2120 | 18 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_ColorCorrectionVolume](client/C_ColorCorrectionVolume.md) | class | 4800 | 9 | [C_BaseTrigger](client/C_BaseTrigger.md) |
| [C_CommandContext](client/C_CommandContext.md) | class | 168 | 2 |  |
| [C_CsmFovOverride](client/C_CsmFovOverride.md) | class | 1552 | 2 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_CsmFovOverride_API](client/C_CsmFovOverride_API.md) | class | 8 | 0 |  |
| [C_DEagle](client/C_DEagle.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_DecoyGrenade](client/C_DecoyGrenade.md) | class | 7584 | 0 | [C_BaseCSGrenade](client/C_BaseCSGrenade.md) |
| [C_DecoyProjectile](client/C_DecoyProjectile.md) | class | 4752 | 3 | [C_BaseCSGrenadeProjectile](client/C_BaseCSGrenadeProjectile.md) |
| [C_DynamicLight](client/C_DynamicLight.md) | class | 4056 | 7 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_DynamicProp](client/C_DynamicProp.md) | class | 5056 | 24 | [C_BreakableProp](client/C_BreakableProp.md) |
| [C_DynamicPropAlias_cable_dynamic](client/C_DynamicPropAlias_cable_dynamic.md) | class | 5056 | 0 | [C_DynamicProp](client/C_DynamicProp.md) |
| [C_DynamicPropAlias_dynamic_prop](client/C_DynamicPropAlias_dynamic_prop.md) | class | 5056 | 0 | [C_DynamicProp](client/C_DynamicProp.md) |
| [C_DynamicPropAlias_prop_dynamic_override](client/C_DynamicPropAlias_prop_dynamic_override.md) | class | 5056 | 0 | [C_DynamicProp](client/C_DynamicProp.md) |
| [C_EconEntity](client/C_EconEntity.md) | class | 5872 | 20 | [CBaseAnimGraph](client/CBaseAnimGraph.md), [IHasAttributes](server/IHasAttributes.md) |
| [C_EconEntity::AttachedModelData_t](client/C_EconEntity.AttachedModelData_t.md) | class | 4 | 1 |  |
| [C_EconItemView](client/C_EconItemView.md) | class | 1136 | 29 | [IEconItemInterface](server/IEconItemInterface.md) |
| [C_EconWearable](client/C_EconWearable.md) | class | 5880 | 2 | [C_EconEntity](client/C_EconEntity.md) |
| [C_EntityDissolve](client/C_EntityDissolve.md) | class | 4088 | 13 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_EntityFlame](client/C_EntityFlame.md) | class | 1608 | 3 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_EnvCombinedLightProbeVolume](client/C_EnvCombinedLightProbeVolume.md) | class | 5960 | 29 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_EnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume](client/C_EnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume.md) | class | 5960 | 0 | [C_EnvCombinedLightProbeVolume](client/C_EnvCombinedLightProbeVolume.md) |
| [C_EnvCubemap](client/C_EnvCubemap.md) | class | 1768 | 18 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_EnvCubemapBox](client/C_EnvCubemapBox.md) | class | 1768 | 0 | [C_EnvCubemap](client/C_EnvCubemap.md) |
| [C_EnvCubemapFog](client/C_EnvCubemapFog.md) | class | 1792 | 24 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_EnvDecal](client/C_EnvDecal.md) | class | 4072 | 9 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_EnvDetailController](client/C_EnvDetailController.md) | class | 1544 | 2 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_EnvLightProbeVolume](client/C_EnvLightProbeVolume.md) | class | 5776 | 22 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_EnvParticleGlow](client/C_EnvParticleGlow.md) | class | 5528 | 5 | [C_ParticleSystem](client/C_ParticleSystem.md) |
| [C_EnvSky](client/C_EnvSky.md) | class | 4112 | 12 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_EnvVolumetricFogController](client/C_EnvVolumetricFogController.md) | class | 1712 | 36 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_EnvVolumetricFogVolume](client/C_EnvVolumetricFogVolume.md) | class | 1608 | 18 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_EnvWind](client/C_EnvWind.md) | class | 1784 | 1 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_EnvWindClientside](client/C_EnvWindClientside.md) | class | 1784 | 1 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_EnvWindController](client/C_EnvWindController.md) | class | 1824 | 11 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_EnvWindShared](client/C_EnvWindShared.md) | class | 248 | 15 |  |
| [C_EnvWindVolume](client/C_EnvWindVolume.md) | class | 1592 | 9 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_FireCrackerBlast](client/C_FireCrackerBlast.md) | class | 34240 | 0 | [C_Inferno](client/C_Inferno.md) |
| [C_Fish](client/C_Fish.md) | class | 4720 | 23 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_Flashbang](client/C_Flashbang.md) | class | 7584 | 0 | [C_BaseCSGrenade](client/C_BaseCSGrenade.md) |
| [C_FlashbangProjectile](client/C_FlashbangProjectile.md) | class | 4704 | 0 | [C_BaseCSGrenadeProjectile](client/C_BaseCSGrenadeProjectile.md) |
| [C_FogController](client/C_FogController.md) | class | 1648 | 3 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_FootstepControl](client/C_FootstepControl.md) | class | 4264 | 2 | [C_BaseTrigger](client/C_BaseTrigger.md) |
| [C_FuncBrush](client/C_FuncBrush.md) | class | 4016 | 0 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_FuncConveyor](client/C_FuncConveyor.md) | class | 4088 | 8 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_FuncElectrifiedVolume](client/C_FuncElectrifiedVolume.md) | class | 4040 | 3 | [C_FuncBrush](client/C_FuncBrush.md) |
| [C_FuncLadder](client/C_FuncLadder.md) | class | 4104 | 9 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_FuncMonitor](client/C_FuncMonitor.md) | class | 5168 | 8 | [C_FuncBrush](client/C_FuncBrush.md) |
| [C_FuncMoveLinear](client/C_FuncMoveLinear.md) | class | 4016 | 0 | [C_BaseToggle](client/C_BaseToggle.md) |
| [C_FuncMover](client/C_FuncMover.md) | class | 4016 | 0 | [C_BaseToggle](client/C_BaseToggle.md) |
| [C_FuncRotating](client/C_FuncRotating.md) | class | 4016 | 0 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_FuncTrackTrain](client/C_FuncTrackTrain.md) | class | 4032 | 3 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_GameRules](client/C_GameRules.md) | class | 64 | 4 |  |
| [C_GameRulesProxy](client/C_GameRulesProxy.md) | class | 1536 | 0 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_GlobalLight](client/C_GlobalLight.md) | class | 2800 | 1 | [C_BaseEntity](client/C_BaseEntity.md), [CGlobalLightBase](client/CGlobalLightBase.md) |
| [C_GradientFog](client/C_GradientFog.md) | class | 1688 | 16 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_HEGrenade](client/C_HEGrenade.md) | class | 7584 | 0 | [C_BaseCSGrenade](client/C_BaseCSGrenade.md) |
| [C_HEGrenadeProjectile](client/C_HEGrenadeProjectile.md) | class | 4704 | 0 | [C_BaseCSGrenadeProjectile](client/C_BaseCSGrenadeProjectile.md) |
| [C_HandleTest](client/C_HandleTest.md) | class | 1544 | 2 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_Hostage](client/C_Hostage.md) | class | 4824 | 23 | [C_BaseCombatCharacter](client/C_BaseCombatCharacter.md) |
| [C_HostageCarriableProp](client/C_HostageCarriableProp.md) | class | 4488 | 0 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_IncendiaryGrenade](client/C_IncendiaryGrenade.md) | class | 7584 | 0 | [C_MolotovGrenade](client/C_MolotovGrenade.md) |
| [C_Inferno](client/C_Inferno.md) | class | 34240 | 24 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_InfoInstructorHintHostageRescueZone](client/C_InfoInstructorHintHostageRescueZone.md) | class | 1536 | 0 | [C_PointEntity](client/C_PointEntity.md) |
| [C_InfoLadderDismount](client/C_InfoLadderDismount.md) | class | 1536 | 0 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_InfoVisibilityBox](client/C_InfoVisibilityBox.md) | class | 1560 | 3 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_IronSightController](client/C_IronSightController.md) | class | 176 | 13 |  |
| [C_Item](client/C_Item.md) | class | 6128 | 1 | [C_EconEntity](client/C_EconEntity.md) |
| [C_ItemDogtags](client/C_ItemDogtags.md) | class | 6136 | 2 | [C_Item](client/C_Item.md) |
| [C_Item_Healthshot](client/C_Item_Healthshot.md) | class | 7408 | 0 | [C_WeaponBaseItem](client/C_WeaponBaseItem.md) |
| [C_KeychainModule](client/C_KeychainModule.md) | class | 4496 | 2 | [C_CS2WeaponModuleBase](client/C_CS2WeaponModuleBase.md) |
| [C_Knife](client/C_Knife.md) | class | 7408 | 1 | [C_CSWeaponBase](client/C_CSWeaponBase.md) |
| [C_LateUpdatedAnimating](client/C_LateUpdatedAnimating.md) | class | 4672 | 0 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_LightDirectionalEntity](client/C_LightDirectionalEntity.md) | class | 4024 | 0 | [C_LightEntity](client/C_LightEntity.md) |
| [C_LightEntity](client/C_LightEntity.md) | class | 4024 | 1 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_LightEnvironmentEntity](client/C_LightEnvironmentEntity.md) | class | 4024 | 0 | [C_LightDirectionalEntity](client/C_LightDirectionalEntity.md) |
| [C_LightOrthoEntity](client/C_LightOrthoEntity.md) | class | 4024 | 0 | [C_LightEntity](client/C_LightEntity.md) |
| [C_LightSpotEntity](client/C_LightSpotEntity.md) | class | 4024 | 0 | [C_LightEntity](client/C_LightEntity.md) |
| [C_LocalTempEntity](client/C_LocalTempEntity.md) | class | 4648 | 25 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_MapPreviewParticleSystem](client/C_MapPreviewParticleSystem.md) | class | 5504 | 0 | [C_ParticleSystem](client/C_ParticleSystem.md) |
| [C_MapVetoPickController](client/C_MapVetoPickController.md) | class | 3912 | 17 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_ModelPointEntity](client/C_ModelPointEntity.md) | class | 4016 | 0 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_MolotovGrenade](client/C_MolotovGrenade.md) | class | 7584 | 0 | [C_BaseCSGrenade](client/C_BaseCSGrenade.md) |
| [C_MolotovProjectile](client/C_MolotovProjectile.md) | class | 4744 | 1 | [C_BaseCSGrenadeProjectile](client/C_BaseCSGrenadeProjectile.md) |
| [C_Multimeter](client/C_Multimeter.md) | class | 4488 | 1 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_MultiplayRules](client/C_MultiplayRules.md) | class | 64 | 0 | [C_GameRules](client/C_GameRules.md) |
| [C_NametagModule](client/C_NametagModule.md) | class | 4496 | 1 | [C_CS2WeaponModuleBase](client/C_CS2WeaponModuleBase.md) |
| [C_NetTestBaseCombatCharacter](client/C_NetTestBaseCombatCharacter.md) | class | 4616 | 0 | [C_BaseCombatCharacter](client/C_BaseCombatCharacter.md) |
| [C_OmniLight](client/C_OmniLight.md) | class | 4816 | 3 | [C_BarnLight](client/C_BarnLight.md) |
| [C_ParticleSystem](client/C_ParticleSystem.md) | class | 5504 | 26 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_PathParticleRope](client/C_PathParticleRope.md) | class | 1808 | 16 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_PathParticleRopeAlias_path_particle_rope_clientside](client/C_PathParticleRopeAlias_path_particle_rope_clientside.md) | class | 1808 | 0 | [C_PathParticleRope](client/C_PathParticleRope.md) |
| [C_PhysBox](client/C_PhysBox.md) | class | 4016 | 0 | [C_Breakable](client/C_Breakable.md) |
| [C_PhysMagnet](client/C_PhysMagnet.md) | class | 4528 | 2 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_PhysPropClientside](client/C_PhysPropClientside.md) | class | 4896 | 5 | [C_BreakableProp](client/C_BreakableProp.md) |
| [C_PhysicsProp](client/C_PhysicsProp.md) | class | 4864 | 1 | [C_BreakableProp](client/C_BreakableProp.md) |
| [C_PhysicsPropMultiplayer](client/C_PhysicsPropMultiplayer.md) | class | 4864 | 0 | [C_PhysicsProp](client/C_PhysicsProp.md) |
| [C_PlantedC4](client/C_PlantedC4.md) | class | 5936 | 29 | [CBaseAnimGraph](client/CBaseAnimGraph.md), [IHasAttributes](server/IHasAttributes.md) |
| [C_PlayerPing](client/C_PlayerPing.md) | class | 1616 | 5 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_PlayerSprayDecal](client/C_PlayerSprayDecal.md) | class | 4288 | 16 | [C_ModelPointEntity](client/C_ModelPointEntity.md) |
| [C_PlayerVisibility](client/C_PlayerVisibility.md) | class | 1584 | 6 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_PointCamera](client/C_PointCamera.md) | class | 1632 | 26 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_PointCameraVFOV](client/C_PointCameraVFOV.md) | class | 1640 | 1 | [C_PointCamera](client/C_PointCamera.md) |
| [C_PointClientUIDialog](client/C_PointClientUIDialog.md) | class | 4072 | 2 | [C_BaseClientUIEntity](client/C_BaseClientUIEntity.md) |
| [C_PointClientUIHUD](client/C_PointClientUIHUD.md) | class | 4520 | 13 | [C_BaseClientUIEntity](client/C_BaseClientUIEntity.md) |
| [C_PointClientUIWorldPanel](client/C_PointClientUIWorldPanel.md) | class | 4624 | 30 | [C_BaseClientUIEntity](client/C_BaseClientUIEntity.md) |
| [C_PointClientUIWorldTextPanel](client/C_PointClientUIWorldTextPanel.md) | class | 5136 | 1 | [C_PointClientUIWorldPanel](client/C_PointClientUIWorldPanel.md) |
| [C_PointCommentaryNode](client/C_PointCommentaryNode.md) | class | 4576 | 14 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_PointEntity](client/C_PointEntity.md) | class | 1536 | 0 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_PointValueRemapper](client/C_PointValueRemapper.md) | class | 1656 | 25 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_PointWorldText](client/C_PointWorldText.md) | class | 4744 | 19 | [C_ModelPointEntity](client/C_ModelPointEntity.md) |
| [C_PortraitWorldCallbackHandler](client/C_PortraitWorldCallbackHandler.md) | class | 1544 | 0 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_PostProcessingVolume](client/C_PostProcessingVolume.md) | class | 4312 | 12 | [C_BaseTrigger](client/C_BaseTrigger.md) |
| [C_Precipitation](client/C_Precipitation.md) | class | 4312 | 8 | [C_BaseTrigger](client/C_BaseTrigger.md) |
| [C_PrecipitationBlocker](client/C_PrecipitationBlocker.md) | class | 4016 | 0 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_PropDoorRotating](client/C_PropDoorRotating.md) | class | 5120 | 0 | [C_BasePropDoor](client/C_BasePropDoor.md) |
| [C_RagdollProp](client/C_RagdollProp.md) | class | 4616 | 9 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_RagdollPropAttached](client/C_RagdollPropAttached.md) | class | 4672 | 7 | [C_RagdollProp](client/C_RagdollProp.md) |
| [C_RectLight](client/C_RectLight.md) | class | 4808 | 1 | [C_BarnLight](client/C_BarnLight.md) |
| [C_RetakeGameRules](client/C_RetakeGameRules.md) | class | 344 | 6 |  |
| [C_RopeKeyframe](client/C_RopeKeyframe.md) | class | 4896 | 40 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_RopeKeyframe::CPhysicsDelegate](client/C_RopeKeyframe.CPhysicsDelegate.md) | class | 16 | 1 |  |
| [C_SceneEntity](client/C_SceneEntity.md) | class | 1640 | 13 | [C_PointEntity](client/C_PointEntity.md) |
| [C_SceneEntity::QueuedEvents_t](client/C_SceneEntity.QueuedEvents_t.md) | class | 24 | 1 |  |
| [C_ShatterGlassShardPhysics](client/C_ShatterGlassShardPhysics.md) | class | 4152 | 1 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_SingleplayRules](client/C_SingleplayRules.md) | class | 64 | 0 | [C_GameRules](client/C_GameRules.md) |
| [C_SkyCamera](client/C_SkyCamera.md) | class | 1696 | 4 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_SmokeGrenade](client/C_SmokeGrenade.md) | class | 7584 | 0 | [C_BaseCSGrenade](client/C_BaseCSGrenade.md) |
| [C_SmokeGrenadeProjectile](client/C_SmokeGrenadeProjectile.md) | class | 5144 | 10 | [C_BaseCSGrenadeProjectile](client/C_BaseCSGrenadeProjectile.md) |
| [C_SoundAreaEntityBase](client/C_SoundAreaEntityBase.md) | class | 1576 | 4 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_SoundAreaEntityOrientedBox](client/C_SoundAreaEntityOrientedBox.md) | class | 1600 | 2 | [C_SoundAreaEntityBase](client/C_SoundAreaEntityBase.md) |
| [C_SoundAreaEntitySphere](client/C_SoundAreaEntitySphere.md) | class | 1584 | 1 | [C_SoundAreaEntityBase](client/C_SoundAreaEntityBase.md) |
| [C_SoundEventAABBEntity](client/C_SoundEventAABBEntity.md) | class | 1752 | 2 | [C_SoundEventEntity](client/C_SoundEventEntity.md) |
| [C_SoundEventConeEntity](client/C_SoundEventConeEntity.md) | class | 1752 | 5 | [C_SoundEventEntity](client/C_SoundEventEntity.md) |
| [C_SoundEventEntity](client/C_SoundEventEntity.md) | class | 1728 | 15 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_SoundEventEntityAlias_snd_event_point](client/C_SoundEventEntityAlias_snd_event_point.md) | class | 1728 | 0 | [C_SoundEventEntity](client/C_SoundEventEntity.md) |
| [C_SoundEventOBBEntity](client/C_SoundEventOBBEntity.md) | class | 1768 | 2 | [C_SoundEventEntity](client/C_SoundEventEntity.md) |
| [C_SoundEventPathCornerEntity](client/C_SoundEventPathCornerEntity.md) | class | 1752 | 1 | [C_SoundEventEntity](client/C_SoundEventEntity.md) |
| [C_SoundEventSphereEntity](client/C_SoundEventSphereEntity.md) | class | 1736 | 1 | [C_SoundEventEntity](client/C_SoundEventEntity.md) |
| [C_SoundOpvarSetAABBEntity](client/C_SoundOpvarSetAABBEntity.md) | class | 1568 | 0 | [CSoundOpvarSetBoxEntity](client/CSoundOpvarSetBoxEntity.md) |
| [C_SoundOpvarSetAutoRoomEntity](client/C_SoundOpvarSetAutoRoomEntity.md) | class | 1568 | 0 | [C_SoundOpvarSetPointEntity](client/C_SoundOpvarSetPointEntity.md) |
| [C_SoundOpvarSetOBBEntity](client/C_SoundOpvarSetOBBEntity.md) | class | 1568 | 0 | [C_SoundOpvarSetAABBEntity](client/C_SoundOpvarSetAABBEntity.md) |
| [C_SoundOpvarSetOBBWindEntity](client/C_SoundOpvarSetOBBWindEntity.md) | class | 1568 | 0 | [C_SoundOpvarSetPointBase](client/C_SoundOpvarSetPointBase.md) |
| [C_SoundOpvarSetPathCornerEntity](client/C_SoundOpvarSetPathCornerEntity.md) | class | 1568 | 0 | [C_SoundOpvarSetPointEntity](client/C_SoundOpvarSetPointEntity.md) |
| [C_SoundOpvarSetPointBase](client/C_SoundOpvarSetPointBase.md) | class | 1568 | 6 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_SoundOpvarSetPointEntity](client/C_SoundOpvarSetPointEntity.md) | class | 1568 | 0 | [C_SoundOpvarSetPointBase](client/C_SoundOpvarSetPointBase.md) |
| [C_SpotlightEnd](client/C_SpotlightEnd.md) | class | 4032 | 2 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_Sprite](client/C_Sprite.md) | class | 4144 | 24 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_StattrakModule](client/C_StattrakModule.md) | class | 4496 | 1 | [C_CS2WeaponModuleBase](client/C_CS2WeaponModuleBase.md) |
| [C_Team](client/C_Team.md) | class | 1720 | 4 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_TeamplayRules](client/C_TeamplayRules.md) | class | 64 | 0 | [C_MultiplayRules](client/C_MultiplayRules.md) |
| [C_TextureBasedAnimatable](client/C_TextureBasedAnimatable.md) | class | 4072 | 8 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_TintController](client/C_TintController.md) | class | 1560 | 0 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_TonemapController2](client/C_TonemapController2.md) | class | 1560 | 5 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_TonemapController2Alias_env_tonemap_controller2](client/C_TonemapController2Alias_env_tonemap_controller2.md) | class | 1560 | 0 | [C_TonemapController2](client/C_TonemapController2.md) |
| [C_TriggerBuoyancy](client/C_TriggerBuoyancy.md) | class | 4536 | 2 | [C_BaseTrigger](client/C_BaseTrigger.md) |
| [C_TriggerLerpObject](client/C_TriggerLerpObject.md) | class | 4248 | 0 | [C_BaseTrigger](client/C_BaseTrigger.md) |
| [C_TriggerMultiple](client/C_TriggerMultiple.md) | class | 4248 | 0 | [C_BaseTrigger](client/C_BaseTrigger.md) |
| [C_TriggerPhysics](client/C_TriggerPhysics.md) | class | 4328 | 13 | [C_BaseTrigger](client/C_BaseTrigger.md) |
| [C_TriggerVolume](client/C_TriggerVolume.md) | class | 4016 | 0 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_VoteController](client/C_VoteController.md) | class | 1592 | 7 | [C_BaseEntity](client/C_BaseEntity.md) |
| [C_WaterBullet](client/C_WaterBullet.md) | class | 4480 | 0 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_WeaponAWP](client/C_WeaponAWP.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponAug](client/C_WeaponAug.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponBaseItem](client/C_WeaponBaseItem.md) | class | 7408 | 2 | [C_CSWeaponBase](client/C_CSWeaponBase.md) |
| [C_WeaponBizon](client/C_WeaponBizon.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponCZ75a](client/C_WeaponCZ75a.md) | class | 7456 | 1 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponElite](client/C_WeaponElite.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponFamas](client/C_WeaponFamas.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponFiveSeven](client/C_WeaponFiveSeven.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponG3SG1](client/C_WeaponG3SG1.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponGalilAR](client/C_WeaponGalilAR.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponGlock](client/C_WeaponGlock.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponHKP2000](client/C_WeaponHKP2000.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponM249](client/C_WeaponM249.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponM4A1](client/C_WeaponM4A1.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponM4A1Silencer](client/C_WeaponM4A1Silencer.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponMAC10](client/C_WeaponMAC10.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponMP5SD](client/C_WeaponMP5SD.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponMP7](client/C_WeaponMP7.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponMP9](client/C_WeaponMP9.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponMag7](client/C_WeaponMag7.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponNOVA](client/C_WeaponNOVA.md) | class | 7392 | 0 | [C_CSWeaponBaseShotgun](client/C_CSWeaponBaseShotgun.md) |
| [C_WeaponNegev](client/C_WeaponNegev.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponP250](client/C_WeaponP250.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponP90](client/C_WeaponP90.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponRevolver](client/C_WeaponRevolver.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponSCAR20](client/C_WeaponSCAR20.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponSG556](client/C_WeaponSG556.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponSSG08](client/C_WeaponSSG08.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponSawedoff](client/C_WeaponSawedoff.md) | class | 7392 | 0 | [C_CSWeaponBaseShotgun](client/C_CSWeaponBaseShotgun.md) |
| [C_WeaponTaser](client/C_WeaponTaser.md) | class | 7456 | 2 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponTec9](client/C_WeaponTec9.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponUMP45](client/C_WeaponUMP45.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponUSPSilencer](client/C_WeaponUSPSilencer.md) | class | 7440 | 0 | [C_CSWeaponBaseGun](client/C_CSWeaponBaseGun.md) |
| [C_WeaponXM1014](client/C_WeaponXM1014.md) | class | 7392 | 0 | [C_CSWeaponBaseShotgun](client/C_CSWeaponBaseShotgun.md) |
| [C_World](client/C_World.md) | class | 4016 | 0 | [C_BaseModelEntity](client/C_BaseModelEntity.md) |
| [C_WorldModelGloves](client/C_WorldModelGloves.md) | class | 4488 | 0 | [CBaseAnimGraph](client/CBaseAnimGraph.md) |
| [C_fogplayerparams_t](client/C_fogplayerparams_t.md) | class | 64 | 14 |  |
| [CountdownTimer](client/CountdownTimer.md) | class | 24 | 4 |  |
| [DestructiblePartDamageRequestAPI](client/DestructiblePartDamageRequestAPI.md) | class | 8 | 0 |  |
| [EngineCountdownTimer](client/EngineCountdownTimer.md) | class | 24 | 3 |  |
| [EntityRenderAttribute_t](client/EntityRenderAttribute_t.md) | class | 72 | 2 |  |
| [EntitySpottedState_t](client/EntitySpottedState_t.md) | class | 24 | 2 |  |
| [FilterDamageType](client/FilterDamageType.md) | class | 1600 | 1 | [CBaseFilter](client/CBaseFilter.md) |
| [FilterHealth](client/FilterHealth.md) | class | 1608 | 3 | [CBaseFilter](client/CBaseFilter.md) |
| [IClientAlphaProperty](client/IClientAlphaProperty.md) | class | 8 | 0 |  |
| [IntervalTimer](client/IntervalTimer.md) | class | 16 | 2 |  |
| [PhysicsRagdollPose_t](client/PhysicsRagdollPose_t.md) | class | 72 | 3 |  |
| [SellbackPurchaseEntry_t](client/SellbackPurchaseEntry_t.md) | class | 72 | 5 |  |
| [SequenceHistory_t](client/SequenceHistory_t.md) | class | 24 | 6 |  |
| [ServerAuthoritativeWeaponSlot_t](client/ServerAuthoritativeWeaponSlot_t.md) | class | 56 | 3 |  |
| [TimedEvent](client/TimedEvent.md) | class | 8 | 2 |  |
| [VPhysicsCollisionAttribute_t](client/VPhysicsCollisionAttribute_t.md) | class | 48 | 11 |  |
| [ViewAngleServerChange_t](client/ViewAngleServerChange_t.md) | class | 72 | 3 |  |
| [WeaponPurchaseCount_t](client/WeaponPurchaseCount_t.md) | class | 56 | 2 |  |
| [WeaponPurchaseTracker_t](client/WeaponPurchaseTracker_t.md) | class | 112 | 1 |  |
| [audioparams_t](client/audioparams_t.md) | class | 120 | 5 |  |
| [fogparams_t](client/fogparams_t.md) | class | 104 | 25 |  |
| [inv_image_camera_t](client/inv_image_camera_t.md) | class | 52 | 7 |  |
| [inv_image_clearcolor_t](client/inv_image_clearcolor_t.md) | class | 12 | 1 |  |
| [inv_image_data_t](client/inv_image_data_t.md) | class | 232 | 8 |  |
| [inv_image_item_t](client/inv_image_item_t.md) | class | 32 | 3 |  |
| [inv_image_light_barn_t](client/inv_image_light_barn_t.md) | class | 32 | 4 |  |
| [inv_image_light_fill_t](client/inv_image_light_fill_t.md) | class | 28 | 3 |  |
| [inv_image_light_sun_t](client/inv_image_light_sun_t.md) | class | 28 | 3 |  |
| [inv_image_map_t](client/inv_image_map_t.md) | class | 16 | 2 |  |
| [screenfade_t](client/screenfade_t.md) | class | 40 | 5 |  |
| [screenshake_t](client/screenshake_t.md) | class | 56 | 9 |  |
| [shard_model_desc_t](client/shard_model_desc_t.md) | class | 128 | 13 |  |
| [sky3dparams_t](client/sky3dparams_t.md) | class | 144 | 6 |  |
| [C_BaseCombatCharacter::WaterWakeMode_t](client/C_BaseCombatCharacter.WaterWakeMode_t.md) | enum | — | 5 |  |
