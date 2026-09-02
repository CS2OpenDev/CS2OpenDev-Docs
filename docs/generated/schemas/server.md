---
layout: default
title: server
parent: Schemas
nav_exclude: true
---

# Module: server

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

[📊 View UML Diagram](../diagrams/server.md)

1141 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [AI_BaseNPCAnimGraph_DebugSnapshotData_t](server/AI_BaseNPCAnimGraph_DebugSnapshotData_t.md) | class | 64 | 8 |  |
| [AI_BaseNPC_DebugSnapshotData_t](server/AI_BaseNPC_DebugSnapshotData_t.md) | class | 376 | 13 | [DebugSnapshotBaseStructuredData_t](server/DebugSnapshotBaseStructuredData_t.md) |
| [AI_DefaultNPC_DebugSnapshotData_t](server/AI_DefaultNPC_DebugSnapshotData_t.md) | class | 120 | 6 | [DebugSnapshotBaseStructuredData_t](server/DebugSnapshotBaseStructuredData_t.md) |
| [AI_DefaultNPC_DebugSnapshotData_t::PathQuery_t](server/AI_DefaultNPC_DebugSnapshotData_t.PathQuery_t.md) | class | 40 | 5 |  |
| [AI_FacingServices_DebugSnapshotData_t](server/AI_FacingServices_DebugSnapshotData_t.md) | class | 72 | 7 |  |
| [AI_GroundRootMotionMotor_DebugSnapshotData_t](server/AI_GroundRootMotionMotor_DebugSnapshotData_t.md) | class | 136 | 18 | [DebugSnapshotBaseStructuredData_t](server/DebugSnapshotBaseStructuredData_t.md) |
| [AI_GroundRootMotionMotor_DebugSnapshotData_t::Event_t](server/AI_GroundRootMotionMotor_DebugSnapshotData_t.Event_t.md) | class | 24 | 2 |  |
| [AI_MotorServices_DebugSnapshotData_t](server/AI_MotorServices_DebugSnapshotData_t.md) | class | 48 | 4 |  |
| [AI_MotorServices_DebugSnapshotData_t::MotorPathWaypoint_t](server/AI_MotorServices_DebugSnapshotData_t.MotorPathWaypoint_t.md) | class | 20 | 3 |  |
| [AI_Navigator_DebugSnapshotData_t](server/AI_Navigator_DebugSnapshotData_t.md) | class | 80 | 7 |  |
| [AI_Navigator_DebugSnapshotData_t::Waypoint_t](server/AI_Navigator_DebugSnapshotData_t.Waypoint_t.md) | class | 24 | 4 |  |
| [ActiveModelConfig_t](server/ActiveModelConfig_t.md) | class | 112 | 4 |  |
| [ActorMapping_t](server/ActorMapping_t.md) | class | 16 | 2 |  |
| [AmmoIndex_t](server/AmmoIndex_t.md) | class | 1 | 1 |  |
| [AmmoTypeInfo_t](server/AmmoTypeInfo_t.md) | class | 56 | 5 |  |
| [AnimGraph2SerializedPoseRecipeSlot_t](server/AnimGraph2SerializedPoseRecipeSlot_t.md) | class | 64 | 1 |  |
| [AutoRoomDoorwayPairs_t](server/AutoRoomDoorwayPairs_t.md) | class | 24 | 2 |  |
| [CAI_ChangeHintGroup](server/CAI_ChangeHintGroup.md) | class | 1224 | 4 | [CBaseEntity](server/CBaseEntity.md) |
| [CAI_Expresser](server/CAI_Expresser.md) | class | 160 | 13 |  |
| [CAI_ExpresserWithFollowup](server/CAI_ExpresserWithFollowup.md) | class | 160 | 0 | [CAI_Expresser](server/CAI_Expresser.md) |
| [CAK47](server/CAK47.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CAmbientGeneric](server/CAmbientGeneric.md) | class | 1360 | 10 | [CPointEntity](server/CPointEntity.md) |
| [CAnimGraph2InstancePtr](server/CAnimGraph2InstancePtr.md) | class | 16 | 0 |  |
| [CAnimGraphControllerBase](server/CAnimGraphControllerBase.md) | class | 136 | 1 |  |
| [CAnimGraphControllerManager](server/CAnimGraphControllerManager.md) | class | 152 | 2 |  |
| [CAnimGraphControllerPtr](server/CAnimGraphControllerPtr.md) | class | 8 | 1 |  |
| [CAttributeContainer](server/CAttributeContainer.md) | class | 760 | 1 | [CAttributeManager](server/CAttributeManager.md) |
| [CAttributeList](server/CAttributeList.md) | class | 120 | 2 |  |
| [CAttributeManager](server/CAttributeManager.md) | class | 80 | 6 |  |
| [CAttributeManager::cached_attribute_float_t](server/CAttributeManager.cached_attribute_float_t.md) | class | 24 | 3 |  |
| [CBarnLight](server/CBarnLight.md) | class | 2648 | 77 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CBarnLightAPI](server/CBarnLightAPI.md) | class | 8 | 0 |  |
| [CBaseAnimGraph](server/CBaseAnimGraph.md) | class | 2400 | 15 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CBaseAnimGraphAPI](server/CBaseAnimGraphAPI.md) | class | 8 | 0 |  |
| [CBaseAnimGraphAlias_baseanimating](server/CBaseAnimGraphAlias_baseanimating.md) | class | 2400 | 0 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CBaseAnimGraphController](server/CBaseAnimGraphController.md) | class | 1616 | 31 | [CSkeletonAnimationController](server/CSkeletonAnimationController.md) |
| [CBaseAnimGraphDestructibleParts_GraphController](server/CBaseAnimGraphDestructibleParts_GraphController.md) | class | 136 | 0 | [CAnimGraphControllerBase](server/CAnimGraphControllerBase.md) |
| [CBaseAnimGraphVariationUserData](server/CBaseAnimGraphVariationUserData.md) | class | 8 | 0 | [CNmGraphVariationUserData](animlib/CNmGraphVariationUserData.md) |
| [CBaseButton](server/CBaseButton.md) | class | 2288 | 26 | [CBaseToggle](server/CBaseToggle.md) |
| [CBaseCSGrenade](server/CBaseCSGrenade.md) | class | 4240 | 13 | [CCSWeaponBase](server/CCSWeaponBase.md) |
| [CBaseCSGrenadeProjectile](server/CBaseCSGrenadeProjectile.md) | class | 2656 | 16 | [CBaseGrenade](server/CBaseGrenade.md) |
| [CBaseClientUIEntity](server/CBaseClientUIEntity.md) | class | 2256 | 14 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CBaseCombatCharacter](server/CBaseCombatCharacter.md) | class | 2608 | 10 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CBaseDMStart](server/CBaseDMStart.md) | class | 1200 | 1 | [CPointEntity](server/CPointEntity.md) |
| [CBaseDoor](server/CBaseDoor.md) | class | 2424 | 29 | [CBaseToggle](server/CBaseToggle.md) |
| [CBaseEntity](server/CBaseEntity.md) | class | 1192 | 85 | [CEntityInstance](entity2/CEntityInstance.md) |
| [CBaseEntityAPI](server/CBaseEntityAPI.md) | class | 8 | 0 |  |
| [CBaseEntity_SharedAPI](server/CBaseEntity_SharedAPI.md) | class | 8 | 0 |  |
| [CBaseFilter](server/CBaseFilter.md) | class | 1248 | 3 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CBaseGrenade](server/CBaseGrenade.md) | class | 2544 | 15 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CBaseGrenade_API](server/CBaseGrenade_API.md) | class | 8 | 0 |  |
| [CBaseIssue](server/CBaseIssue.md) | class | 376 | 6 |  |
| [CBaseModelEntity](server/CBaseModelEntity.md) | class | 1904 | 40 | [CBaseEntity](server/CBaseEntity.md) |
| [CBaseModelEntity::OnDamageLevelChangedArgs_t](server/CBaseModelEntity.OnDamageLevelChangedArgs_t.md) | class | 16 | 4 |  |
| [CBaseModelEntityAPI](server/CBaseModelEntityAPI.md) | class | 8 | 0 |  |
| [CBaseMoveBehavior](server/CBaseMoveBehavior.md) | class | 1312 | 11 | [CPathKeyFrame](server/CPathKeyFrame.md) |
| [CBasePlatTrain](server/CBasePlatTrain.md) | class | 2072 | 5 | [CBaseToggle](server/CBaseToggle.md) |
| [CBasePlayerController](server/CBasePlayerController.md) | class | 2000 | 25 | [CBaseEntity](server/CBaseEntity.md) |
| [CBasePlayerControllerAPI](server/CBasePlayerControllerAPI.md) | class | 8 | 0 |  |
| [CBasePlayerPawn](server/CBasePlayerPawn.md) | class | 3040 | 25 | [CBaseCombatCharacter](server/CBaseCombatCharacter.md) |
| [CBasePlayerVData](server/CBasePlayerVData.md) | class | 600 | 15 | [CEntitySubclassVDataBase](server/CEntitySubclassVDataBase.md) |
| [CBasePlayerWeapon](server/CBasePlayerWeapon.md) | class | 3280 | 8 | [CEconEntity](server/CEconEntity.md) |
| [CBasePlayerWeaponVData](server/CBasePlayerWeaponVData.md) | class | 1312 | 32 | [CEntitySubclassVDataBase](server/CEntitySubclassVDataBase.md) |
| [CBaseProp](server/CBaseProp.md) | class | 2448 | 4 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CBasePropDoor](server/CBasePropDoor.md) | class | 3488 | 39 | [CDynamicProp](server/CDynamicProp.md) |
| [CBaseToggle](server/CBaseToggle.md) | class | 2032 | 16 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CBaseTrigger](server/CBaseTrigger.md) | class | 2280 | 13 | [CBaseToggle](server/CBaseToggle.md) |
| [CBaseTriggerAPI](server/CBaseTriggerAPI.md) | class | 8 | 0 |  |
| [CBeam](server/CBeam.md) | class | 2064 | 23 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CBlood](server/CBlood.md) | class | 1224 | 4 | [CPointEntity](server/CPointEntity.md) |
| [CBodyComponent](server/CBodyComponent.md) | class | 120 | 2 | [CEntityComponent](entity2/CEntityComponent.md) |
| [CBodyComponentBaseAnimGraph](server/CBodyComponentBaseAnimGraph.md) | class | 2864 | 1 | [CBodyComponentSkeletonInstance](server/CBodyComponentSkeletonInstance.md) |
| [CBodyComponentBaseModelEntity](server/CBodyComponentBaseModelEntity.md) | class | 1248 | 0 | [CBodyComponentSkeletonInstance](server/CBodyComponentSkeletonInstance.md) |
| [CBodyComponentPoint](server/CBodyComponentPoint.md) | class | 400 | 1 | [CBodyComponent](server/CBodyComponent.md) |
| [CBodyComponentSkeletonInstance](server/CBodyComponentSkeletonInstance.md) | class | 1248 | 1 | [CBodyComponent](server/CBodyComponent.md) |
| [CBombTarget](server/CBombTarget.md) | class | 2376 | 9 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CBot](server/CBot.md) | class | 256 | 13 |  |
| [CBreakable](server/CBreakable.md) | class | 2120 | 16 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CBreakableProp](server/CBreakableProp.md) | class | 2800 | 33 | [CBaseProp](server/CBaseProp.md) |
| [CBreakableStageHelper](server/CBreakableStageHelper.md) | class | 24 | 2 |  |
| [CBtActionAim](server/CBtActionAim.md) | class | 248 | 12 | [CBtNode](server/CBtNode.md) |
| [CBtActionCombatPositioning](server/CBtActionCombatPositioning.md) | class | 176 | 4 | [CBtNode](server/CBtNode.md) |
| [CBtActionMoveTo](server/CBtActionMoveTo.md) | class | 232 | 14 | [CBtNode](server/CBtNode.md) |
| [CBtActionParachutePositioning](server/CBtActionParachutePositioning.md) | class | 120 | 1 | [CBtNode](server/CBtNode.md) |
| [CBtNode](server/CBtNode.md) | class | 88 | 0 |  |
| [CBtNodeComposite](server/CBtNodeComposite.md) | class | 88 | 0 | [CBtNode](server/CBtNode.md) |
| [CBtNodeCondition](server/CBtNodeCondition.md) | class | 96 | 1 | [CBtNodeDecorator](server/CBtNodeDecorator.md) |
| [CBtNodeConditionInactive](server/CBtNodeConditionInactive.md) | class | 152 | 3 | [CBtNodeCondition](server/CBtNodeCondition.md) |
| [CBtNodeDecorator](server/CBtNodeDecorator.md) | class | 88 | 0 | [CBtNode](server/CBtNode.md) |
| [CBuoyancyHelper](server/CBuoyancyHelper.md) | class | 280 | 11 |  |
| [CBuyZone](server/CBuyZone.md) | class | 2288 | 1 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CBuyZone_API](server/CBuyZone_API.md) | class | 8 | 0 |  |
| [CC4](server/CC4.md) | class | 4304 | 11 | [CCSWeaponBase](server/CCSWeaponBase.md) |
| [CCS2ChickenGraphController](server/CCS2ChickenGraphController.md) | class | 320 | 9 | [CAnimGraphControllerBase](server/CAnimGraphControllerBase.md) |
| [CCS2PawnGraphController](server/CCS2PawnGraphController.md) | class | 2088 | 28 | [CCS2WeaponGraphController](server/CCS2WeaponGraphController.md) |
| [CCS2WeaponGraphController](server/CCS2WeaponGraphController.md) | class | 1416 | 20 | [CAnimGraphControllerBase](server/CAnimGraphControllerBase.md) |
| [CCSBot](server/CCSBot.md) | class | 24128 | 140 | [CBot](server/CBot.md) |
| [CCSCustomHudLayout](server/CCSCustomHudLayout.md) | class | 2024 | 6 | [CBaseEntity](server/CBaseEntity.md) |
| [CCSCustomHudLayoutState](server/CCSCustomHudLayoutState.md) | class | 408 | 4 |  |
| [CCSCustomHudLayout_API](server/CCSCustomHudLayout_API.md) | class | 8 | 0 |  |
| [CCSGO_EndOfMatchLineupEnd](server/CCSGO_EndOfMatchLineupEnd.md) | class | 1192 | 0 | [CCSGO_EndOfMatchLineupEndpoint](server/CCSGO_EndOfMatchLineupEndpoint.md) |
| [CCSGO_EndOfMatchLineupEndpoint](server/CCSGO_EndOfMatchLineupEndpoint.md) | class | 1192 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [CCSGO_EndOfMatchLineupStart](server/CCSGO_EndOfMatchLineupStart.md) | class | 1192 | 0 | [CCSGO_EndOfMatchLineupEndpoint](server/CCSGO_EndOfMatchLineupEndpoint.md) |
| [CCSGO_TeamIntroCharacterPosition](server/CCSGO_TeamIntroCharacterPosition.md) | class | 3264 | 0 | [CCSGO_TeamPreviewCharacterPosition](server/CCSGO_TeamPreviewCharacterPosition.md) |
| [CCSGO_TeamIntroCounterTerroristPosition](server/CCSGO_TeamIntroCounterTerroristPosition.md) | class | 3264 | 0 | [CCSGO_TeamIntroCharacterPosition](server/CCSGO_TeamIntroCharacterPosition.md) |
| [CCSGO_TeamIntroTerroristPosition](server/CCSGO_TeamIntroTerroristPosition.md) | class | 3264 | 0 | [CCSGO_TeamIntroCharacterPosition](server/CCSGO_TeamIntroCharacterPosition.md) |
| [CCSGO_TeamPreviewCharacterPosition](server/CCSGO_TeamPreviewCharacterPosition.md) | class | 3264 | 8 | [CBaseEntity](server/CBaseEntity.md) |
| [CCSGO_TeamPreviewCharacterPosition_API](server/CCSGO_TeamPreviewCharacterPosition_API.md) | class | 8 | 0 |  |
| [CCSGO_TeamSelectCharacterPosition](server/CCSGO_TeamSelectCharacterPosition.md) | class | 3264 | 0 | [CCSGO_TeamPreviewCharacterPosition](server/CCSGO_TeamPreviewCharacterPosition.md) |
| [CCSGO_TeamSelectCounterTerroristPosition](server/CCSGO_TeamSelectCounterTerroristPosition.md) | class | 3264 | 0 | [CCSGO_TeamSelectCharacterPosition](server/CCSGO_TeamSelectCharacterPosition.md) |
| [CCSGO_TeamSelectTerroristPosition](server/CCSGO_TeamSelectTerroristPosition.md) | class | 3264 | 0 | [CCSGO_TeamSelectCharacterPosition](server/CCSGO_TeamSelectCharacterPosition.md) |
| [CCSGO_WingmanIntroCharacterPosition](server/CCSGO_WingmanIntroCharacterPosition.md) | class | 3264 | 0 | [CCSGO_TeamIntroCharacterPosition](server/CCSGO_TeamIntroCharacterPosition.md) |
| [CCSGO_WingmanIntroCounterTerroristPosition](server/CCSGO_WingmanIntroCounterTerroristPosition.md) | class | 3264 | 0 | [CCSGO_WingmanIntroCharacterPosition](server/CCSGO_WingmanIntroCharacterPosition.md) |
| [CCSGO_WingmanIntroTerroristPosition](server/CCSGO_WingmanIntroTerroristPosition.md) | class | 3264 | 0 | [CCSGO_WingmanIntroCharacterPosition](server/CCSGO_WingmanIntroCharacterPosition.md) |
| [CCSGameModeRules](server/CCSGameModeRules.md) | class | 48 | 1 |  |
| [CCSGameModeRules_ArmsRace](server/CCSGameModeRules_ArmsRace.md) | class | 136 | 1 | [CCSGameModeRules](server/CCSGameModeRules.md) |
| [CCSGameModeRules_Deathmatch](server/CCSGameModeRules_Deathmatch.md) | class | 136 | 3 | [CCSGameModeRules](server/CCSGameModeRules.md) |
| [CCSGameModeRules_Noop](server/CCSGameModeRules_Noop.md) | class | 48 | 0 | [CCSGameModeRules](server/CCSGameModeRules.md) |
| [CCSGameRules](server/CCSGameRules.md) | class | 70728 | 189 | [CTeamplayRules](server/CTeamplayRules.md) |
| [CCSGameRulesProxy](server/CCSGameRulesProxy.md) | class | 1200 | 1 | [CGameRulesProxy](server/CGameRulesProxy.md) |
| [CCSMinimapBoundary](server/CCSMinimapBoundary.md) | class | 1192 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [CCSObserverPawn](server/CCSObserverPawn.md) | class | 3424 | 0 | [CCSPlayerPawnBase](server/CCSPlayerPawnBase.md) |
| [CCSObserverPawn_API](server/CCSObserverPawn_API.md) | class | 8 | 0 |  |
| [CCSObserver_CameraServices](server/CCSObserver_CameraServices.md) | class | 432 | 0 | [CCSPlayerBase_CameraServices](server/CCSPlayerBase_CameraServices.md) |
| [CCSObserver_MovementServices](server/CCSObserver_MovementServices.md) | class | 600 | 0 | [CPlayer_MovementServices](server/CPlayer_MovementServices.md) |
| [CCSObserver_ObserverServices](server/CCSObserver_ObserverServices.md) | class | 128 | 0 | [CPlayer_ObserverServices](server/CPlayer_ObserverServices.md) |
| [CCSObserver_UseServices](server/CCSObserver_UseServices.md) | class | 72 | 0 | [CPlayer_UseServices](server/CPlayer_UseServices.md) |
| [CCSPetPlacement](server/CCSPetPlacement.md) | class | 1192 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [CCSPlace](server/CCSPlace.md) | class | 1936 | 1 | [CServerOnlyModelEntity](server/CServerOnlyModelEntity.md) |
| [CCSPlace_API](server/CCSPlace_API.md) | class | 8 | 0 |  |
| [CCSPlayerAnimationState](server/CCSPlayerAnimationState.md) | class | 224 | 16 |  |
| [CCSPlayerBase_CameraServices](server/CCSPlayerBase_CameraServices.md) | class | 432 | 7 | [CPlayer_CameraServices](server/CPlayer_CameraServices.md) |
| [CCSPlayerCamera](server/CCSPlayerCamera.md) | class | 1200 | 3 | [CBaseEntity](server/CBaseEntity.md) |
| [CCSPlayerController](server/CCSPlayerController.md) | class | 2728 | 92 | [CBasePlayerController](server/CBasePlayerController.md) |
| [CCSPlayerController_API](server/CCSPlayerController_API.md) | class | 8 | 0 |  |
| [CCSPlayerController_ActionTrackingServices](server/CCSPlayerController_ActionTrackingServices.md) | class | 1072 | 5 | [CPlayerControllerComponent](server/CPlayerControllerComponent.md) |
| [CCSPlayerController_DamageServices](server/CCSPlayerController_DamageServices.md) | class | 208 | 2 | [CPlayerControllerComponent](server/CPlayerControllerComponent.md) |
| [CCSPlayerController_InGameMoneyServices](server/CCSPlayerController_InGameMoneyServices.md) | class | 88 | 6 | [CPlayerControllerComponent](server/CPlayerControllerComponent.md) |
| [CCSPlayerController_InventoryServices](server/CCSPlayerController_InventoryServices.md) | class | 4064 | 10 | [CPlayerControllerComponent](server/CPlayerControllerComponent.md) |
| [CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t](server/CCSPlayerController_InventoryServices.NetworkedLoadoutSlot_t.md) | class | 16 | 3 |  |
| [CCSPlayerLegacyJump](server/CCSPlayerLegacyJump.md) | class | 24 | 2 |  |
| [CCSPlayerModernJump](server/CCSPlayerModernJump.md) | class | 56 | 9 |  |
| [CCSPlayerPawn](server/CCSPlayerPawn.md) | class | 4992 | 105 | [CCSPlayerPawnBase](server/CCSPlayerPawnBase.md) |
| [CCSPlayerPawnBase](server/CCSPlayerPawnBase.md) | class | 3376 | 15 | [CBasePlayerPawn](server/CBasePlayerPawn.md) |
| [CCSPlayerPawnBase_API](server/CCSPlayerPawnBase_API.md) | class | 8 | 0 |  |
| [CCSPlayerPawn_API](server/CCSPlayerPawn_API.md) | class | 8 | 0 |  |
| [CCSPlayerResource](server/CCSPlayerResource.md) | class | 1344 | 10 | [CBaseEntity](server/CBaseEntity.md) |
| [CCSPlayer_ActionTrackingServices](server/CCSPlayer_ActionTrackingServices.md) | class | 784 | 4 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_AimPunchServices](server/CCSPlayer_AimPunchServices.md) | class | 232 | 6 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_BulletServices](server/CCSPlayer_BulletServices.md) | class | 112 | 1 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_BuyServices](server/CCSPlayer_BuyServices.md) | class | 344 | 1 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_CameraServices](server/CCSPlayer_CameraServices.md) | class | 432 | 0 | [CCSPlayerBase_CameraServices](server/CCSPlayerBase_CameraServices.md) |
| [CCSPlayer_DamageReactServices](server/CCSPlayer_DamageReactServices.md) | class | 104 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_HostageServices](server/CCSPlayer_HostageServices.md) | class | 80 | 2 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_ItemServices](server/CCSPlayer_ItemServices.md) | class | 80 | 2 | [CPlayer_ItemServices](server/CPlayer_ItemServices.md) |
| [CCSPlayer_MovementServices](server/CCSPlayer_MovementServices.md) | class | 4064 | 50 | [CPlayer_MovementServices_Humanoid](server/CPlayer_MovementServices_Humanoid.md) |
| [CCSPlayer_PingServices](server/CCSPlayer_PingServices.md) | class | 96 | 2 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_RadioServices](server/CCSPlayer_RadioServices.md) | class | 104 | 5 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CCSPlayer_UseServices](server/CCSPlayer_UseServices.md) | class | 88 | 3 | [CPlayer_UseServices](server/CPlayer_UseServices.md) |
| [CCSPlayer_WaterServices](server/CCSPlayer_WaterServices.md) | class | 128 | 6 | [CPlayer_WaterServices](server/CPlayer_WaterServices.md) |
| [CCSPlayer_WeaponServices](server/CCSPlayer_WeaponServices.md) | class | 6272 | 13 | [CPlayer_WeaponServices](server/CPlayer_WeaponServices.md) |
| [CCSPointPulseAPI](server/CCSPointPulseAPI.md) | class | 1 | 0 |  |
| [CCSPointScriptEntity](server/CCSPointScriptEntity.md) | class | 1576 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [CCSPointScriptEntity_API](server/CCSPointScriptEntity_API.md) | class | 8 | 0 |  |
| [CCSSprite](server/CCSSprite.md) | class | 2016 | 0 | [CSprite](server/CSprite.md) |
| [CCSTeam](server/CCSTeam.md) | class | 2080 | 14 | [CTeam](server/CTeam.md) |
| [CCSWeaponBase](server/CCSWeaponBase.md) | class | 4176 | 52 | [CBasePlayerWeapon](server/CBasePlayerWeapon.md) |
| [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) | class | 4208 | 10 | [CCSWeaponBase](server/CCSWeaponBase.md) |
| [CCSWeaponBaseShotgun](server/CCSWeaponBaseShotgun.md) | class | 4176 | 0 | [CCSWeaponBase](server/CCSWeaponBase.md) |
| [CCSWeaponBaseVData](server/CCSWeaponBaseVData.md) | class | 2216 | 84 | [CBasePlayerWeaponVData](server/CBasePlayerWeaponVData.md) |
| [CCSWeaponBase_API](server/CCSWeaponBase_API.md) | class | 8 | 0 |  |
| [CCashStack](server/CCashStack.md) | class | 1912 | 1 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CChangeLevel](server/CChangeLevel.md) | class | 2328 | 7 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CChicken](server/CChicken.md) | class | 12480 | 23 | [CDynamicProp](server/CDynamicProp.md), [IHasAttributes](server/IHasAttributes.md) |
| [CChicken_API](server/CChicken_API.md) | class | 8 | 0 |  |
| [CChoreoComponent](server/CChoreoComponent.md) | class | 128 | 6 |  |
| [CChoreoInfoTarget](server/CChoreoInfoTarget.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CChoreo_GraphController](server/CChoreo_GraphController.md) | class | 272 | 3 | [CAnimGraphControllerBase](server/CAnimGraphControllerBase.md) |
| [CCitadelSoundOpvarSetOBB](server/CCitadelSoundOpvarSetOBB.md) | class | 1272 | 8 | [CBaseEntity](server/CBaseEntity.md) |
| [CCollisionProperty](server/CCollisionProperty.md) | class | 184 | 17 |  |
| [CColorCorrection](server/CColorCorrection.md) | class | 1760 | 17 | [CBaseEntity](server/CBaseEntity.md) |
| [CColorCorrectionVolume](server/CColorCorrectionVolume.md) | class | 2824 | 8 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CCommentaryAuto](server/CCommentaryAuto.md) | class | 1264 | 3 | [CBaseEntity](server/CBaseEntity.md) |
| [CCommentarySystem](server/CCommentarySystem.md) | class | 96 | 10 |  |
| [CCommentaryViewPosition](server/CCommentaryViewPosition.md) | class | 2016 | 0 | [CSprite](server/CSprite.md) |
| [CConstantForceController](server/CConstantForceController.md) | class | 64 | 4 |  |
| [CConstraintAnchor](server/CConstraintAnchor.md) | class | 2416 | 1 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CCopyRecipientFilter](server/CCopyRecipientFilter.md) | class | 56 | 3 |  |
| [CCredits](server/CCredits.md) | class | 1224 | 3 | [CPointEntity](server/CPointEntity.md) |
| [CDEagle](server/CDEagle.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CDamageRecord](server/CDamageRecord.md) | class | 120 | 15 |  |
| [CDebugDrawHistoryData](server/CDebugDrawHistoryData.md) | class | 120 | 9 |  |
| [CDebugHistory](server/CDebugHistory.md) | class | 4101264 | 1 | [CBaseEntity](server/CBaseEntity.md) |
| [CDebugSnapshotData_t](server/CDebugSnapshotData_t.md) | class | 304 | 14 |  |
| [CDecalGroupVData](server/CDecalGroupVData.md) | class | 32 | 2 |  |
| [CDecalInstance](server/CDecalInstance.md) | class | 192 | 27 |  |
| [CDecoyGrenade](server/CDecoyGrenade.md) | class | 4240 | 0 | [CBaseCSGrenade](server/CBaseCSGrenade.md) |
| [CDecoyProjectile](server/CDecoyProjectile.md) | class | 2720 | 4 | [CBaseCSGrenadeProjectile](server/CBaseCSGrenadeProjectile.md) |
| [CDestructiblePart](server/CDestructiblePart.md) | class | 80 | 7 |  |
| [CDestructiblePart_DamageLevel](server/CDestructiblePart_DamageLevel.md) | class | 72 | 10 |  |
| [CDestructiblePartsComponent](server/CDestructiblePartsComponent.md) | class | 112 | 4 |  |
| [CDestructiblePartsSystemData](server/CDestructiblePartsSystemData.md) | class | 48 | 2 |  |
| [CDynamicLight](server/CDynamicLight.md) | class | 1928 | 9 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CDynamicNavConnectionsVolume](server/CDynamicNavConnectionsVolume.md) | class | 2360 | 7 | [CTriggerMultiple](server/CTriggerMultiple.md) |
| [CDynamicProp](server/CDynamicProp.md) | class | 2976 | 23 | [CBreakableProp](server/CBreakableProp.md) |
| [CDynamicPropAlias_cable_dynamic](server/CDynamicPropAlias_cable_dynamic.md) | class | 2976 | 0 | [CDynamicProp](server/CDynamicProp.md) |
| [CDynamicPropAlias_dynamic_prop](server/CDynamicPropAlias_dynamic_prop.md) | class | 2976 | 0 | [CDynamicProp](server/CDynamicProp.md) |
| [CDynamicPropAlias_prop_dynamic_override](server/CDynamicPropAlias_prop_dynamic_override.md) | class | 2976 | 0 | [CDynamicProp](server/CDynamicProp.md) |
| [CEconEntity](server/CEconEntity.md) | class | 3216 | 9 | [CBaseAnimGraph](server/CBaseAnimGraph.md), [IHasAttributes](server/IHasAttributes.md) |
| [CEconItemAttribute](server/CEconItemAttribute.md) | class | 72 | 5 |  |
| [CEconItemView](server/CEconItemView.md) | class | 680 | 13 | [IEconItemInterface](server/IEconItemInterface.md) |
| [CEconWearable](server/CEconWearable.md) | class | 3232 | 2 | [CEconEntity](server/CEconEntity.md) |
| [CEffectData](server/CEffectData.md) | class | 112 | 20 |  |
| [CEmptyGraphController](server/CEmptyGraphController.md) | class | 136 | 0 | [CAnimGraphControllerBase](server/CAnimGraphControllerBase.md) |
| [CEnableMotionFixup](server/CEnableMotionFixup.md) | class | 1192 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [CEntityBlocker](server/CEntityBlocker.md) | class | 1904 | 0 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CEntityDissolve](server/CEntityDissolve.md) | class | 1952 | 10 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CEntityFlame](server/CEntityFlame.md) | class | 1256 | 10 | [CBaseEntity](server/CBaseEntity.md) |
| [CEntitySubclassVDataBase](server/CEntitySubclassVDataBase.md) | class | 40 | 0 |  |
| [CEnvBeam](server/CEnvBeam.md) | class | 2216 | 19 | [CBeam](server/CBeam.md) |
| [CEnvBeverage](server/CEnvBeverage.md) | class | 1200 | 2 | [CBaseEntity](server/CBaseEntity.md) |
| [CEnvCombinedLightProbeVolume](server/CEnvCombinedLightProbeVolume.md) | class | 5616 | 29 | [CBaseEntity](server/CBaseEntity.md) |
| [CEnvCombinedLightProbeVolumeAPI](server/CEnvCombinedLightProbeVolumeAPI.md) | class | 8 | 0 |  |
| [CEnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume](server/CEnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume.md) | class | 5616 | 0 | [CEnvCombinedLightProbeVolume](server/CEnvCombinedLightProbeVolume.md) |
| [CEnvCubemap](server/CEnvCubemap.md) | class | 1424 | 18 | [CBaseEntity](server/CBaseEntity.md) |
| [CEnvCubemapAPI](server/CEnvCubemapAPI.md) | class | 8 | 0 |  |
| [CEnvCubemapBox](server/CEnvCubemapBox.md) | class | 1424 | 0 | [CEnvCubemap](server/CEnvCubemap.md) |
| [CEnvCubemapFog](server/CEnvCubemapFog.md) | class | 1448 | 24 | [CBaseEntity](server/CBaseEntity.md) |
| [CEnvDecal](server/CEnvDecal.md) | class | 1936 | 9 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CEnvDetailController](server/CEnvDetailController.md) | class | 1200 | 2 | [CBaseEntity](server/CBaseEntity.md) |
| [CEnvEntityIgniter](server/CEnvEntityIgniter.md) | class | 1200 | 1 | [CBaseEntity](server/CBaseEntity.md) |
| [CEnvEntityMaker](server/CEnvEntityMaker.md) | class | 1320 | 12 | [CPointEntity](server/CPointEntity.md) |
| [CEnvExplosion](server/CEnvExplosion.md) | class | 1992 | 15 | [CModelPointEntity](server/CModelPointEntity.md) |
| [CEnvFade](server/CEnvFade.md) | class | 1232 | 4 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CEnvGlobal](server/CEnvGlobal.md) | class | 1248 | 5 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CEnvHudHint](server/CEnvHudHint.md) | class | 1200 | 1 | [CPointEntity](server/CPointEntity.md) |
| [CEnvHudHint_API](server/CEnvHudHint_API.md) | class | 8 | 0 |  |
| [CEnvInstructorHint](server/CEnvInstructorHint.md) | class | 1304 | 24 | [CPointEntity](server/CPointEntity.md) |
| [CEnvInstructorVRHint](server/CEnvInstructorVRHint.md) | class | 1256 | 9 | [CPointEntity](server/CPointEntity.md) |
| [CEnvLaser](server/CEnvLaser.md) | class | 2104 | 5 | [CBeam](server/CBeam.md) |
| [CEnvLightProbeVolume](server/CEnvLightProbeVolume.md) | class | 5432 | 22 | [CBaseEntity](server/CBaseEntity.md) |
| [CEnvLightProbeVolumeAPI](server/CEnvLightProbeVolumeAPI.md) | class | 8 | 0 |  |
| [CEnvMuzzleFlash](server/CEnvMuzzleFlash.md) | class | 1208 | 2 | [CPointEntity](server/CPointEntity.md) |
| [CEnvParticleGlow](server/CEnvParticleGlow.md) | class | 3344 | 5 | [CParticleSystem](server/CParticleSystem.md) |
| [CEnvShake](server/CEnvShake.md) | class | 1272 | 11 | [CPointEntity](server/CPointEntity.md) |
| [CEnvSky](server/CEnvSky.md) | class | 2000 | 12 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CEnvSkyAPI](server/CEnvSkyAPI.md) | class | 8 | 0 |  |
| [CEnvSoundscape](server/CEnvSoundscape.md) | class | 1336 | 11 | [CBaseEntity](server/CBaseEntity.md) |
| [CEnvSoundscapeAlias_snd_soundscape](server/CEnvSoundscapeAlias_snd_soundscape.md) | class | 1336 | 0 | [CEnvSoundscape](server/CEnvSoundscape.md) |
| [CEnvSoundscapeProxy](server/CEnvSoundscapeProxy.md) | class | 1344 | 1 | [CEnvSoundscape](server/CEnvSoundscape.md) |
| [CEnvSoundscapeProxyAlias_snd_soundscape_proxy](server/CEnvSoundscapeProxyAlias_snd_soundscape_proxy.md) | class | 1344 | 0 | [CEnvSoundscapeProxy](server/CEnvSoundscapeProxy.md) |
| [CEnvSoundscapeTriggerable](server/CEnvSoundscapeTriggerable.md) | class | 1336 | 0 | [CEnvSoundscape](server/CEnvSoundscape.md) |
| [CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable](server/CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable.md) | class | 1336 | 0 | [CEnvSoundscapeTriggerable](server/CEnvSoundscapeTriggerable.md) |
| [CEnvSpark](server/CEnvSpark.md) | class | 1232 | 5 | [CPointEntity](server/CPointEntity.md) |
| [CEnvSplash](server/CEnvSplash.md) | class | 1200 | 1 | [CPointEntity](server/CPointEntity.md) |
| [CEnvTilt](server/CEnvTilt.md) | class | 1208 | 4 | [CPointEntity](server/CPointEntity.md) |
| [CEnvViewPunch](server/CEnvViewPunch.md) | class | 1208 | 2 | [CPointEntity](server/CPointEntity.md) |
| [CEnvVolumetricFogController](server/CEnvVolumetricFogController.md) | class | 1368 | 36 | [CBaseEntity](server/CBaseEntity.md) |
| [CEnvVolumetricFogVolume](server/CEnvVolumetricFogVolume.md) | class | 1264 | 18 | [CBaseEntity](server/CBaseEntity.md) |
| [CEnvWind](server/CEnvWind.md) | class | 1496 | 1 | [CBaseEntity](server/CBaseEntity.md) |
| [CEnvWindController](server/CEnvWindController.md) | class | 1536 | 11 | [CBaseEntity](server/CBaseEntity.md) |
| [CEnvWindShared](server/CEnvWindShared.md) | class | 304 | 17 |  |
| [CEnvWindSharedAPI](server/CEnvWindSharedAPI.md) | class | 8 | 0 |  |
| [CEnvWindVolume](server/CEnvWindVolume.md) | class | 1248 | 9 | [CBaseEntity](server/CBaseEntity.md) |
| [CExplosionTypeData](server/CExplosionTypeData.md) | class | 256 | 5 |  |
| [CExternalAnimGraphList](server/CExternalAnimGraphList.md) | class | 32 | 0 |  |
| [CFilterAttributeInt](server/CFilterAttributeInt.md) | class | 1256 | 1 | [CBaseFilter](server/CBaseFilter.md) |
| [CFilterClass](server/CFilterClass.md) | class | 1256 | 1 | [CBaseFilter](server/CBaseFilter.md) |
| [CFilterContext](server/CFilterContext.md) | class | 1256 | 1 | [CBaseFilter](server/CBaseFilter.md) |
| [CFilterEnemy](server/CFilterEnemy.md) | class | 1280 | 5 | [CBaseFilter](server/CBaseFilter.md) |
| [CFilterLOS](server/CFilterLOS.md) | class | 1248 | 0 | [CBaseFilter](server/CBaseFilter.md) |
| [CFilterMassGreater](server/CFilterMassGreater.md) | class | 1256 | 1 | [CBaseFilter](server/CBaseFilter.md) |
| [CFilterModel](server/CFilterModel.md) | class | 1256 | 1 | [CBaseFilter](server/CBaseFilter.md) |
| [CFilterMultiple](server/CFilterMultiple.md) | class | 1376 | 3 | [CBaseFilter](server/CBaseFilter.md) |
| [CFilterMultipleAPI](server/CFilterMultipleAPI.md) | class | 8 | 0 |  |
| [CFilterName](server/CFilterName.md) | class | 1256 | 1 | [CBaseFilter](server/CBaseFilter.md) |
| [CFilterProximity](server/CFilterProximity.md) | class | 1256 | 1 | [CBaseFilter](server/CBaseFilter.md) |
| [CFilterTeam](server/CFilterTeam.md) | class | 1256 | 1 | [CBaseFilter](server/CBaseFilter.md) |
| [CFireCrackerBlast](server/CFireCrackerBlast.md) | class | 5112 | 0 | [CInferno](server/CInferno.md) |
| [CFiringModeFloat](server/CFiringModeFloat.md) | class | 8 | 1 |  |
| [CFiringModeInt](server/CFiringModeInt.md) | class | 8 | 1 |  |
| [CFish](server/CFish.md) | class | 2672 | 24 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CFishPool](server/CFishPool.md) | class | 1280 | 7 | [CBaseEntity](server/CBaseEntity.md) |
| [CFlashbang](server/CFlashbang.md) | class | 4240 | 0 | [CBaseCSGrenade](server/CBaseCSGrenade.md) |
| [CFlashbangProjectile](server/CFlashbangProjectile.md) | class | 2672 | 3 | [CBaseCSGrenadeProjectile](server/CBaseCSGrenadeProjectile.md) |
| [CFlashbangProjectile_API](server/CFlashbangProjectile_API.md) | class | 8 | 0 |  |
| [CFloatExponentialMovingAverage](server/CFloatExponentialMovingAverage.md) | class | 20 | 0 |  |
| [CFloatMovingAverage](server/CFloatMovingAverage.md) | class | 32 | 0 |  |
| [CFogController](server/CFogController.md) | class | 1304 | 3 | [CBaseEntity](server/CBaseEntity.md) |
| [CFogTrigger](server/CFogTrigger.md) | class | 2384 | 1 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CFogVolume](server/CFogVolume.md) | class | 1944 | 5 | [CServerOnlyModelEntity](server/CServerOnlyModelEntity.md) |
| [CFootstepControl](server/CFootstepControl.md) | class | 2296 | 2 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CFootstepControl_API](server/CFootstepControl_API.md) | class | 8 | 0 |  |
| [CFootstepTableHandle](server/CFootstepTableHandle.md) | class | 8 | 0 |  |
| [CFuncBrush](server/CFuncBrush.md) | class | 1936 | 6 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncConveyor](server/CFuncConveyor.md) | class | 1984 | 10 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncConveyor_API](server/CFuncConveyor_API.md) | class | 8 | 0 |  |
| [CFuncElectrifiedVolume](server/CFuncElectrifiedVolume.md) | class | 1992 | 4 | [CFuncBrush](server/CFuncBrush.md) |
| [CFuncIllusionary](server/CFuncIllusionary.md) | class | 1904 | 0 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncInteractionLayerClip](server/CFuncInteractionLayerClip.md) | class | 1928 | 3 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncLadder](server/CFuncLadder.md) | class | 2048 | 12 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncLadderAlias_func_useableladder](server/CFuncLadderAlias_func_useableladder.md) | class | 2048 | 0 | [CFuncLadder](server/CFuncLadder.md) |
| [CFuncMonitor](server/CFuncMonitor.md) | class | 1968 | 9 | [CFuncBrush](server/CFuncBrush.md) |
| [CFuncMoveLinear](server/CFuncMoveLinear.md) | class | 2168 | 14 | [CBaseToggle](server/CBaseToggle.md) |
| [CFuncMoveLinearAlias_momentary_door](server/CFuncMoveLinearAlias_momentary_door.md) | class | 2168 | 0 | [CFuncMoveLinear](server/CFuncMoveLinear.md) |
| [CFuncMover](server/CFuncMover.md) | class | 2608 | 98 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncMoverAPI](server/CFuncMoverAPI.md) | class | 8 | 0 |  |
| [CFuncMoverRouter](server/CFuncMoverRouter.md) | class | 1256 | 4 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CFuncNavBlocker](server/CFuncNavBlocker.md) | class | 1928 | 2 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncNavObstruction](server/CFuncNavObstruction.md) | class | 1936 | 2 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncPlat](server/CFuncPlat.md) | class | 2088 | 2 | [CBasePlatTrain](server/CBasePlatTrain.md) |
| [CFuncPlatRot](server/CFuncPlatRot.md) | class | 2112 | 2 | [CFuncPlat](server/CFuncPlat.md) |
| [CFuncPropRespawnZone](server/CFuncPropRespawnZone.md) | class | 1192 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [CFuncRetakeBarrier](server/CFuncRetakeBarrier.md) | class | 3008 | 0 | [CDynamicProp](server/CDynamicProp.md) |
| [CFuncRotating](server/CFuncRotating.md) | class | 2104 | 19 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncRotator](server/CFuncRotator.md) | class | 2288 | 38 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncShatterglass](server/CFuncShatterglass.md) | class | 2208 | 26 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncTankTrain](server/CFuncTankTrain.md) | class | 2224 | 1 | [CFuncTrackTrain](server/CFuncTrackTrain.md) |
| [CFuncTimescale](server/CFuncTimescale.md) | class | 1216 | 5 | [CBaseEntity](server/CBaseEntity.md) |
| [CFuncTrackAuto](server/CFuncTrackAuto.md) | class | 2168 | 0 | [CFuncTrackChange](server/CFuncTrackChange.md) |
| [CFuncTrackChange](server/CFuncTrackChange.md) | class | 2168 | 9 | [CFuncPlatRot](server/CFuncPlatRot.md) |
| [CFuncTrackTrain](server/CFuncTrackTrain.md) | class | 2200 | 38 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncTrain](server/CFuncTrain.md) | class | 2112 | 7 | [CBasePlatTrain](server/CBasePlatTrain.md) |
| [CFuncTrainControls](server/CFuncTrainControls.md) | class | 1904 | 0 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncVPhysicsClip](server/CFuncVPhysicsClip.md) | class | 1912 | 1 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncVehicleClip](server/CFuncVehicleClip.md) | class | 1904 | 0 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncWall](server/CFuncWall.md) | class | 1912 | 1 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CFuncWallToggle](server/CFuncWallToggle.md) | class | 1912 | 0 | [CFuncWall](server/CFuncWall.md) |
| [CFuncWater](server/CFuncWater.md) | class | 2184 | 1 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CGameChoreoServices](server/CGameChoreoServices.md) | class | 32 | 5 | [IChoreoServices](server/IChoreoServices.md) |
| [CGameEnd](server/CGameEnd.md) | class | 1920 | 0 | [CRulePointEntity](server/CRulePointEntity.md) |
| [CGameGibManager](server/CGameGibManager.md) | class | 1232 | 4 | [CBaseEntity](server/CBaseEntity.md) |
| [CGameMoney](server/CGameMoney.md) | class | 1984 | 4 | [CRulePointEntity](server/CRulePointEntity.md) |
| [CGameMoney_API](server/CGameMoney_API.md) | class | 8 | 0 |  |
| [CGamePlayerEquip](server/CGamePlayerEquip.md) | class | 1944 | 0 | [CRulePointEntity](server/CRulePointEntity.md) |
| [CGamePlayerZone](server/CGamePlayerZone.md) | class | 2024 | 4 | [CRuleBrushEntity](server/CRuleBrushEntity.md) |
| [CGameRules](server/CGameRules.md) | class | 208 | 8 |  |
| [CGameRulesProxy](server/CGameRulesProxy.md) | class | 1192 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [CGameSceneNode](server/CGameSceneNode.md) | class | 272 | 31 |  |
| [CGameSceneNodeHandle](server/CGameSceneNodeHandle.md) | class | 16 | 2 |  |
| [CGameScriptedMoveData](server/CGameScriptedMoveData.md) | class | 116 | 18 |  |
| [CGameScriptedMoveDef_t](server/CGameScriptedMoveDef_t.md) | class | 48 | 9 |  |
| [CGameStateReportAPI](server/CGameStateReportAPI.md) | class | 8 | 0 |  |
| [CGameText](server/CGameText.md) | class | 1952 | 2 | [CRulePointEntity](server/CRulePointEntity.md) |
| [CGenericConstraint](server/CGenericConstraint.md) | class | 1544 | 49 | [CPhysConstraint](server/CPhysConstraint.md) |
| [CGlowProperty](server/CGlowProperty.md) | class | 88 | 11 |  |
| [CGradientFog](server/CGradientFog.md) | class | 1256 | 16 | [CBaseEntity](server/CBaseEntity.md) |
| [CGunTarget](server/CGunTarget.md) | class | 2072 | 4 | [CBaseToggle](server/CBaseToggle.md) |
| [CHEGrenade](server/CHEGrenade.md) | class | 4240 | 0 | [CBaseCSGrenade](server/CBaseCSGrenade.md) |
| [CHEGrenadeProjectile](server/CHEGrenadeProjectile.md) | class | 2656 | 0 | [CBaseCSGrenadeProjectile](server/CBaseCSGrenadeProjectile.md) |
| [CHandleDummy](server/CHandleDummy.md) | class | 1192 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [CHandleTest](server/CHandleTest.md) | class | 1200 | 2 | [CBaseEntity](server/CBaseEntity.md) |
| [CHintMessage](server/CHintMessage.md) | class | 40 | 3 |  |
| [CHintMessageQueue](server/CHintMessageQueue.md) | class | 40 | 3 |  |
| [CHitboxComponent](server/CHitboxComponent.md) | class | 24 | 1 | [CEntityComponent](entity2/CEntityComponent.md) |
| [CHostage](server/CHostage.md) | class | 11456 | 39 | [CHostageExpresserShim](server/CHostageExpresserShim.md) |
| [CHostageAlias_info_hostage_spawn](server/CHostageAlias_info_hostage_spawn.md) | class | 11456 | 0 | [CHostage](server/CHostage.md) |
| [CHostageCarriableProp](server/CHostageCarriableProp.md) | class | 2400 | 0 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CHostageExpresserShim](server/CHostageExpresserShim.md) | class | 2624 | 1 | [CBaseCombatCharacter](server/CBaseCombatCharacter.md) |
| [CHostageRescueZone](server/CHostageRescueZone.md) | class | 2312 | 0 | [CHostageRescueZoneShim](server/CHostageRescueZoneShim.md) |
| [CHostageRescueZoneShim](server/CHostageRescueZoneShim.md) | class | 2280 | 0 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CHostage_API](server/CHostage_API.md) | class | 8 | 0 |  |
| [CInButtonState](server/CInButtonState.md) | class | 32 | 1 |  |
| [CIncendiaryGrenade](server/CIncendiaryGrenade.md) | class | 4240 | 0 | [CMolotovGrenade](server/CMolotovGrenade.md) |
| [CInferno](server/CInferno.md) | class | 5112 | 24 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CInfoChoreoAnchor](server/CInfoChoreoAnchor.md) | class | 1240 | 2 | [CPointEntity](server/CPointEntity.md) |
| [CInfoChoreoAnchorPosition](server/CInfoChoreoAnchorPosition.md) | class | 80 | 8 |  |
| [CInfoData](server/CInfoData.md) | class | 2112 | 0 | [CServerOnlyEntity](server/CServerOnlyEntity.md) |
| [CInfoDeathmatchSpawn](server/CInfoDeathmatchSpawn.md) | class | 1208 | 0 | [SpawnPoint](server/SpawnPoint.md) |
| [CInfoDynamicShadowHint](server/CInfoDynamicShadowHint.md) | class | 1216 | 5 | [CPointEntity](server/CPointEntity.md) |
| [CInfoDynamicShadowHintBox](server/CInfoDynamicShadowHintBox.md) | class | 1240 | 2 | [CInfoDynamicShadowHint](server/CInfoDynamicShadowHint.md) |
| [CInfoFan](server/CInfoFan.md) | class | 1280 | 4 | [CPointEntity](server/CPointEntity.md) |
| [CInfoGameEventProxy](server/CInfoGameEventProxy.md) | class | 1208 | 2 | [CPointEntity](server/CPointEntity.md) |
| [CInfoInstructorHintBombTargetA](server/CInfoInstructorHintBombTargetA.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CInfoInstructorHintBombTargetB](server/CInfoInstructorHintBombTargetB.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CInfoInstructorHintHostageRescueZone](server/CInfoInstructorHintHostageRescueZone.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CInfoInstructorHintTarget](server/CInfoInstructorHintTarget.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CInfoLadderDismount](server/CInfoLadderDismount.md) | class | 1192 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [CInfoLandmark](server/CInfoLandmark.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CInfoOffscreenPanoramaTexture](server/CInfoOffscreenPanoramaTexture.md) | class | 1320 | 11 | [CPointEntity](server/CPointEntity.md) |
| [CInfoParticleTarget](server/CInfoParticleTarget.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CInfoPlayerCounterterrorist](server/CInfoPlayerCounterterrorist.md) | class | 1208 | 0 | [SpawnPoint](server/SpawnPoint.md) |
| [CInfoPlayerStart](server/CInfoPlayerStart.md) | class | 1208 | 3 | [CPointEntity](server/CPointEntity.md) |
| [CInfoPlayerTerrorist](server/CInfoPlayerTerrorist.md) | class | 1208 | 0 | [SpawnPoint](server/SpawnPoint.md) |
| [CInfoSpawnGroupLandmark](server/CInfoSpawnGroupLandmark.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CInfoSpawnGroupLoadUnload](server/CInfoSpawnGroupLoadUnload.md) | class | 1408 | 13 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CInfoTarget](server/CInfoTarget.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CInfoTargetServerOnly](server/CInfoTargetServerOnly.md) | class | 1192 | 0 | [CServerOnlyPointEntity](server/CServerOnlyPointEntity.md) |
| [CInfoTeleportDestination](server/CInfoTeleportDestination.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CInfoVisibilityBox](server/CInfoVisibilityBox.md) | class | 1216 | 3 | [CBaseEntity](server/CBaseEntity.md) |
| [CInfoWorldLayer](server/CInfoWorldLayer.md) | class | 1240 | 7 | [CBaseEntity](server/CBaseEntity.md) |
| [CInstancedSceneEntity](server/CInstancedSceneEntity.md) | class | 2056 | 7 | [CSceneEntity](server/CSceneEntity.md) |
| [CInstructorEventEntity](server/CInstructorEventEntity.md) | class | 1216 | 3 | [CPointEntity](server/CPointEntity.md) |
| [CIronSightController](server/CIronSightController.md) | class | 24 | 4 |  |
| [CItem](server/CItem.md) | class | 2560 | 8 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CItemAssaultSuit](server/CItemAssaultSuit.md) | class | 2560 | 0 | [CItem](server/CItem.md) |
| [CItemDefuser](server/CItemDefuser.md) | class | 2592 | 2 | [CItem](server/CItem.md) |
| [CItemDefuserAlias_item_defuser](server/CItemDefuserAlias_item_defuser.md) | class | 2592 | 0 | [CItemDefuser](server/CItemDefuser.md) |
| [CItemDogtags](server/CItemDogtags.md) | class | 2576 | 2 | [CItem](server/CItem.md) |
| [CItemGeneric](server/CItemGeneric.md) | class | 2864 | 32 | [CItem](server/CItem.md) |
| [CItemGenericTriggerHelper](server/CItemGenericTriggerHelper.md) | class | 1912 | 1 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CItemKevlar](server/CItemKevlar.md) | class | 2560 | 0 | [CItem](server/CItem.md) |
| [CItemSoda](server/CItemSoda.md) | class | 2400 | 0 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CItem_Healthshot](server/CItem_Healthshot.md) | class | 4192 | 0 | [CWeaponBaseItem](server/CWeaponBaseItem.md) |
| [CKeepUpright](server/CKeepUpright.md) | class | 1256 | 8 | [CPointEntity](server/CPointEntity.md) |
| [CKnife](server/CKnife.md) | class | 4192 | 1 | [CCSWeaponBase](server/CCSWeaponBase.md) |
| [CLightComponent](server/CLightComponent.md) | class | 448 | 71 | [CEntityComponent](entity2/CEntityComponent.md) |
| [CLightDirectionalEntity](server/CLightDirectionalEntity.md) | class | 1912 | 0 | [CLightEntity](server/CLightEntity.md) |
| [CLightEntity](server/CLightEntity.md) | class | 1912 | 1 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CLightEntityAPI](server/CLightEntityAPI.md) | class | 8 | 0 |  |
| [CLightEnvironmentEntity](server/CLightEnvironmentEntity.md) | class | 1912 | 0 | [CLightDirectionalEntity](server/CLightDirectionalEntity.md) |
| [CLightOrthoEntity](server/CLightOrthoEntity.md) | class | 1912 | 0 | [CLightEntity](server/CLightEntity.md) |
| [CLightSpotEntity](server/CLightSpotEntity.md) | class | 1912 | 0 | [CLightEntity](server/CLightEntity.md) |
| [CLogicAchievement](server/CLogicAchievement.md) | class | 1232 | 3 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicActiveAutosave](server/CLogicActiveAutosave.md) | class | 1224 | 4 | [CLogicAutosave](server/CLogicAutosave.md) |
| [CLogicActivityEvent](server/CLogicActivityEvent.md) | class | 1216 | 4 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicAuto](server/CLogicAuto.md) | class | 1440 | 11 | [CBaseEntity](server/CBaseEntity.md) |
| [CLogicAutosave](server/CLogicAutosave.md) | class | 1208 | 3 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicBranch](server/CLogicBranch.md) | class | 1272 | 4 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicBranchList](server/CLogicBranchList.md) | class | 1424 | 6 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicCase](server/CLogicCase.md) | class | 2288 | 6 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicCollisionPair](server/CLogicCollisionPair.md) | class | 1216 | 7 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicCompare](server/CLogicCompare.md) | class | 1328 | 6 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicDistanceAutosave](server/CLogicDistanceAutosave.md) | class | 1216 | 6 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicDistanceCheck](server/CLogicDistanceCheck.md) | class | 1288 | 7 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicEventListener](server/CLogicEventListener.md) | class | 1256 | 4 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicEventListener_API](server/CLogicEventListener_API.md) | class | 8 | 0 |  |
| [CLogicGameEvent](server/CLogicGameEvent.md) | class | 1200 | 1 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicGameEventListener](server/CLogicGameEventListener.md) | class | 1256 | 5 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicGameStateReport](server/CLogicGameStateReport.md) | class | 1392 | 1 | [CBaseEntity](server/CBaseEntity.md) |
| [CLogicLineToEntity](server/CLogicLineToEntity.md) | class | 1248 | 4 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicMeasureMovement](server/CLogicMeasureMovement.md) | class | 1240 | 9 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicNPCCounter](server/CLogicNPCCounter.md) | class | 1832 | 48 | [CBaseEntity](server/CBaseEntity.md) |
| [CLogicNPCCounterAABB](server/CLogicNPCCounterAABB.md) | class | 1880 | 4 | [CLogicNPCCounter](server/CLogicNPCCounter.md) |
| [CLogicNPCCounterOBB](server/CLogicNPCCounterOBB.md) | class | 1880 | 0 | [CLogicNPCCounterAABB](server/CLogicNPCCounterAABB.md) |
| [CLogicNavigation](server/CLogicNavigation.md) | class | 1208 | 2 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicPlayerProxy](server/CLogicPlayerProxy.md) | class | 1304 | 5 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicProximity](server/CLogicProximity.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CLogicRelay](server/CLogicRelay.md) | class | 1248 | 7 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CLogicRelayAPI](server/CLogicRelayAPI.md) | class | 8 | 0 |  |
| [CLogicScript](server/CLogicScript.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CLogicalEntity](server/CLogicalEntity.md) | class | 1192 | 0 | [CServerOnlyEntity](server/CServerOnlyEntity.md) |
| [CMapInfo](server/CMapInfo.md) | class | 1240 | 15 | [CPointEntity](server/CPointEntity.md) |
| [CMapInfo_API](server/CMapInfo_API.md) | class | 8 | 0 |  |
| [CMapSharedEnvironment](server/CMapSharedEnvironment.md) | class | 1208 | 1 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CMapVetoPickController](server/CMapVetoPickController.md) | class | 3752 | 24 | [CBaseEntity](server/CBaseEntity.md) |
| [CMapVetoPickController_API](server/CMapVetoPickController_API.md) | class | 8 | 0 |  |
| [CMarkupSearchHelper](server/CMarkupSearchHelper.md) | class | 688 | 7 |  |
| [CMarkupSearch_PathCostAreaFilter](server/CMarkupSearch_PathCostAreaFilter.md) | class | 696 | 1 | [INavPathCostAreaFilter](server/INavPathCostAreaFilter.md) |
| [CMarkupVolume](server/CMarkupVolume.md) | class | 1912 | 1 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CMarkupVolumeTagged](server/CMarkupVolumeTagged.md) | class | 1968 | 7 | [CMarkupVolume](server/CMarkupVolume.md) |
| [CMarkupVolumeTagged_Nav](server/CMarkupVolumeTagged_Nav.md) | class | 1976 | 1 | [CMarkupVolumeTagged](server/CMarkupVolumeTagged.md) |
| [CMarkupVolumeTagged_NavGame](server/CMarkupVolumeTagged_NavGame.md) | class | 2016 | 3 | [CMarkupVolumeWithRef](server/CMarkupVolumeWithRef.md) |
| [CMarkupVolumeWithRef](server/CMarkupVolumeWithRef.md) | class | 2008 | 4 | [CMarkupVolumeTagged](server/CMarkupVolumeTagged.md) |
| [CMathColorBlend](server/CMathColorBlend.md) | class | 1240 | 5 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CMathCounter](server/CMathCounter.md) | class | 1368 | 11 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CMathRemap](server/CMathRemap.md) | class | 1344 | 11 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CMessage](server/CMessage.md) | class | 1248 | 6 | [CPointEntity](server/CPointEntity.md) |
| [CMessageEntity](server/CMessageEntity.md) | class | 1216 | 5 | [CPointEntity](server/CPointEntity.md) |
| [CModelPointEntity](server/CModelPointEntity.md) | class | 1904 | 0 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CModelState](server/CModelState.md) | class | 656 | 14 |  |
| [CMolotovGrenade](server/CMolotovGrenade.md) | class | 4240 | 0 | [CBaseCSGrenade](server/CBaseCSGrenade.md) |
| [CMolotovProjectile](server/CMolotovProjectile.md) | class | 2912 | 3 | [CBaseCSGrenadeProjectile](server/CBaseCSGrenadeProjectile.md) |
| [CMomentaryRotButton](server/CMomentaryRotButton.md) | class | 2472 | 14 | [CRotButton](server/CRotButton.md) |
| [CMotorController](server/CMotorController.md) | class | 32 | 4 |  |
| [CMovementStatsProperty](server/CMovementStatsProperty.md) | class | 64 | 2 |  |
| [CMoverPathNode](server/CMoverPathNode.md) | class | 1440 | 5 | [CPathNode](server/CPathNode.md) |
| [CMultiLightProxy](server/CMultiLightProxy.md) | class | 1256 | 8 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CMultiSource](server/CMultiSource.md) | class | 1488 | 5 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CMultiplayRules](server/CMultiplayRules.md) | class | 208 | 0 | [CGameRules](server/CGameRules.md) |
| [CMultiplayer_Expresser](server/CMultiplayer_Expresser.md) | class | 168 | 1 | [CAI_ExpresserWithFollowup](server/CAI_ExpresserWithFollowup.md) |
| [CNMEventPulseState_t](server/CNMEventPulseState_t.md) | class | 8 | 1 |  |
| [CNavSpaceInfo](server/CNavSpaceInfo.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CNavVolumeBreadthFirstSearch](server/CNavVolumeBreadthFirstSearch.md) | class | 192 | 2 | [CNavVolumeCalculatedVector](server/CNavVolumeCalculatedVector.md) |
| [CNavVolumeCalculatedVector](server/CNavVolumeCalculatedVector.md) | class | 160 | 0 | [CNavVolume](navlib/CNavVolume.md) |
| [CNavVolumeMarkupVolume](server/CNavVolumeMarkupVolume.md) | class | 224 | 0 | [CNavVolume](navlib/CNavVolume.md) |
| [CNavWalkable](server/CNavWalkable.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CNetworkOriginCellCoordQuantizedVector](server/CNetworkOriginCellCoordQuantizedVector.md) | class | 48 | 7 |  |
| [CNetworkOriginCellCoordQuantizedVectorWS](server/CNetworkOriginCellCoordQuantizedVectorWS.md) | class | 48 | 7 |  |
| [CNetworkOriginQuantizedVector](server/CNetworkOriginQuantizedVector.md) | class | 40 | 3 |  |
| [CNetworkOriginQuantizedVectorWS](server/CNetworkOriginQuantizedVectorWS.md) | class | 40 | 3 |  |
| [CNetworkTransmitComponent](server/CNetworkTransmitComponent.md) | class | 464 | 1 |  |
| [CNetworkVelocityVector](server/CNetworkVelocityVector.md) | class | 40 | 3 |  |
| [CNetworkViewOffsetVector](server/CNetworkViewOffsetVector.md) | class | 40 | 3 |  |
| [CNetworkedSequenceOperation](server/CNetworkedSequenceOperation.md) | class | 40 | 8 |  |
| [CNmAimCSNode::CDefinition](server/CNmAimCSNode.CDefinition.md) | class | 56 | 11 | [CNmPassthroughNode::CDefinition](animlib/CNmPassthroughNode.CDefinition.md) |
| [CNmAimCSTask](server/CNmAimCSTask.md) | class | 304 | 0 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [CNmEventConsumer](server/CNmEventConsumer.md) | class | 176 | 0 |  |
| [CNmEventConsumerAttributes](server/CNmEventConsumerAttributes.md) | class | 176 | 0 | [CNmEventConsumer](server/CNmEventConsumer.md) |
| [CNmEventConsumerLegacy](server/CNmEventConsumerLegacy.md) | class | 1000 | 0 | [CNmEventConsumer](server/CNmEventConsumer.md) |
| [CNmEventConsumerParticle](server/CNmEventConsumerParticle.md) | class | 176 | 0 | [CNmEventConsumer](server/CNmEventConsumer.md) |
| [CNmEventConsumerPulse](server/CNmEventConsumerPulse.md) | class | 200 | 0 | [CNmEventConsumer](server/CNmEventConsumer.md) |
| [CNmEventConsumerSound](server/CNmEventConsumerSound.md) | class | 184 | 0 | [CNmEventConsumer](server/CNmEventConsumer.md) |
| [CNmSnapWeaponNode::CDefinition](server/CNmSnapWeaponNode.CDefinition.md) | class | 32 | 3 | [CNmPassthroughNode::CDefinition](animlib/CNmPassthroughNode.CDefinition.md) |
| [CNmSnapWeaponTask](server/CNmSnapWeaponTask.md) | class | 128 | 0 | [CNmPoseTask](animlib/CNmPoseTask.md) |
| [CNullEntity](server/CNullEntity.md) | class | 1192 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [COmniLight](server/COmniLight.md) | class | 2664 | 3 | [CBarnLight](server/CBarnLight.md) |
| [COrnamentProp](server/COrnamentProp.md) | class | 2992 | 1 | [CDynamicProp](server/CDynamicProp.md) |
| [CParticleSystem](server/CParticleSystem.md) | class | 3320 | 24 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CParticleSystemAPI](server/CParticleSystemAPI.md) | class | 8 | 0 |  |
| [CPathCorner](server/CPathCorner.md) | class | 1232 | 4 | [CPointEntity](server/CPointEntity.md) |
| [CPathCornerCrash](server/CPathCornerCrash.md) | class | 1232 | 0 | [CPathCorner](server/CPathCorner.md) |
| [CPathKeyFrame](server/CPathKeyFrame.md) | class | 1264 | 8 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CPathMover](server/CPathMover.md) | class | 1600 | 6 | [CPathWithDynamicNodes](server/CPathWithDynamicNodes.md) |
| [CPathMoverEntitySpawner](server/CPathMoverEntitySpawner.md) | class | 1384 | 16 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CPathNode](server/CPathNode.md) | class | 1280 | 6 | [CPointEntity](server/CPointEntity.md) |
| [CPathParticleRope](server/CPathParticleRope.md) | class | 1424 | 16 | [CBaseEntity](server/CBaseEntity.md) |
| [CPathParticleRopeAlias_path_particle_rope_clientside](server/CPathParticleRopeAlias_path_particle_rope_clientside.md) | class | 1424 | 0 | [CPathParticleRope](server/CPathParticleRope.md) |
| [CPathQueryComponent](server/CPathQueryComponent.md) | class | 160 | 0 | [CEntityComponent](entity2/CEntityComponent.md), [CPathQueryUtil](server/CPathQueryUtil.md) |
| [CPathQueryUtil](server/CPathQueryUtil.md) | class | 128 | 5 |  |
| [CPathSimple](server/CPathSimple.md) | class | 1456 | 3 | [CBaseEntity](server/CBaseEntity.md) |
| [CPathSimpleAPI](server/CPathSimpleAPI.md) | class | 8 | 0 |  |
| [CPathTrack](server/CPathTrack.md) | class | 1256 | 10 | [CPointEntity](server/CPointEntity.md) |
| [CPathWithDynamicNodes](server/CPathWithDynamicNodes.md) | class | 1520 | 2 | [CPathSimple](server/CPathSimple.md) |
| [CPhysBallSocket](server/CPhysBallSocket.md) | class | 1312 | 6 | [CPhysConstraint](server/CPhysConstraint.md) |
| [CPhysBox](server/CPhysBox.md) | class | 2344 | 18 | [CBreakable](server/CBreakable.md) |
| [CPhysConstraint](server/CPhysConstraint.md) | class | 1288 | 14 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CPhysExplosion](server/CPhysExplosion.md) | class | 1256 | 11 | [CPointEntity](server/CPointEntity.md) |
| [CPhysFixed](server/CPhysFixed.md) | class | 1328 | 8 | [CPhysConstraint](server/CPhysConstraint.md) |
| [CPhysForce](server/CPhysForce.md) | class | 1288 | 7 | [CPointEntity](server/CPointEntity.md) |
| [CPhysHinge](server/CPhysHinge.md) | class | 1656 | 19 | [CPhysConstraint](server/CPhysConstraint.md) |
| [CPhysHingeAlias_phys_hinge_local](server/CPhysHingeAlias_phys_hinge_local.md) | class | 1656 | 0 | [CPhysHinge](server/CPhysHinge.md) |
| [CPhysImpact](server/CPhysImpact.md) | class | 1208 | 3 | [CPointEntity](server/CPointEntity.md) |
| [CPhysLength](server/CPhysLength.md) | class | 1336 | 5 | [CPhysConstraint](server/CPhysConstraint.md) |
| [CPhysMagnet](server/CPhysMagnet.md) | class | 2512 | 12 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CPhysMotor](server/CPhysMotor.md) | class | 1296 | 15 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CPhysMotorAPI](server/CPhysMotorAPI.md) | class | 8 | 0 |  |
| [CPhysPulley](server/CPhysPulley.md) | class | 1336 | 4 | [CPhysConstraint](server/CPhysConstraint.md) |
| [CPhysSlideConstraint](server/CPhysSlideConstraint.md) | class | 1488 | 10 | [CPhysConstraint](server/CPhysConstraint.md) |
| [CPhysThruster](server/CPhysThruster.md) | class | 1304 | 1 | [CPhysForce](server/CPhysForce.md) |
| [CPhysTorque](server/CPhysTorque.md) | class | 1304 | 1 | [CPhysForce](server/CPhysForce.md) |
| [CPhysWheelConstraint](server/CPhysWheelConstraint.md) | class | 1344 | 12 | [CPhysConstraint](server/CPhysConstraint.md) |
| [CPhysicalButton](server/CPhysicalButton.md) | class | 2288 | 0 | [CBaseButton](server/CBaseButton.md) |
| [CPhysicsBodyGameMarkup](server/CPhysicsBodyGameMarkup.md) | class | 16 | 2 |  |
| [CPhysicsBodyGameMarkupData](server/CPhysicsBodyGameMarkupData.md) | class | 40 | 1 |  |
| [CPhysicsEntitySolver](server/CPhysicsEntitySolver.md) | class | 1232 | 4 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CPhysicsProp](server/CPhysicsProp.md) | class | 3120 | 42 | [CBreakableProp](server/CBreakableProp.md) |
| [CPhysicsPropMultiplayer](server/CPhysicsPropMultiplayer.md) | class | 3120 | 0 | [CPhysicsProp](server/CPhysicsProp.md) |
| [CPhysicsPropOverride](server/CPhysicsPropOverride.md) | class | 3120 | 0 | [CPhysicsProp](server/CPhysicsProp.md) |
| [CPhysicsPropRespawnable](server/CPhysicsPropRespawnable.md) | class | 3184 | 5 | [CPhysicsProp](server/CPhysicsProp.md) |
| [CPhysicsShake](server/CPhysicsShake.md) | class | 24 | 1 |  |
| [CPhysicsSpring](server/CPhysicsSpring.md) | class | 1264 | 9 | [CBaseEntity](server/CBaseEntity.md) |
| [CPhysicsWire](server/CPhysicsWire.md) | class | 1200 | 1 | [CBaseEntity](server/CBaseEntity.md) |
| [CPlantedC4](server/CPlantedC4.md) | class | 3456 | 27 | [CBaseAnimGraph](server/CBaseAnimGraph.md), [IHasAttributes](server/IHasAttributes.md) |
| [CPlantedC4_API](server/CPlantedC4_API.md) | class | 8 | 0 |  |
| [CPlatTrigger](server/CPlatTrigger.md) | class | 1912 | 1 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CPlayerControllerComponent](server/CPlayerControllerComponent.md) | class | 64 | 1 |  |
| [CPlayerPawnComponent](server/CPlayerPawnComponent.md) | class | 72 | 2 |  |
| [CPlayerPing](server/CPlayerPing.md) | class | 1232 | 5 | [CBaseEntity](server/CBaseEntity.md) |
| [CPlayerSprayDecal](server/CPlayerSprayDecal.md) | class | 2120 | 15 | [CModelPointEntity](server/CModelPointEntity.md) |
| [CPlayerVisibility](server/CPlayerVisibility.md) | class | 1216 | 6 | [CBaseEntity](server/CBaseEntity.md) |
| [CPlayer_AutoaimServices](server/CPlayer_AutoaimServices.md) | class | 72 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_CameraServices](server/CPlayer_CameraServices.md) | class | 376 | 12 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_FlashlightServices](server/CPlayer_FlashlightServices.md) | class | 72 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_ItemServices](server/CPlayer_ItemServices.md) | class | 72 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_MovementServices](server/CPlayer_MovementServices.md) | class | 600 | 18 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_MovementServices_Humanoid](server/CPlayer_MovementServices_Humanoid.md) | class | 656 | 7 | [CPlayer_MovementServices](server/CPlayer_MovementServices.md) |
| [CPlayer_ObserverServices](server/CPlayer_ObserverServices.md) | class | 88 | 4 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_UseServices](server/CPlayer_UseServices.md) | class | 72 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_WaterServices](server/CPlayer_WaterServices.md) | class | 72 | 0 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPlayer_WeaponServices](server/CPlayer_WeaponServices.md) | class | 176 | 5 | [CPlayerPawnComponent](server/CPlayerPawnComponent.md) |
| [CPointAngleSensor](server/CPointAngleSensor.md) | class | 1352 | 12 | [CPointEntity](server/CPointEntity.md) |
| [CPointAngularVelocitySensor](server/CPointAngularVelocitySensor.md) | class | 1400 | 16 | [CPointEntity](server/CPointEntity.md) |
| [CPointBroadcastClientCommand](server/CPointBroadcastClientCommand.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CPointCamera](server/CPointCamera.md) | class | 1288 | 26 | [CBaseEntity](server/CBaseEntity.md) |
| [CPointCameraVFOV](server/CPointCameraVFOV.md) | class | 1296 | 1 | [CPointCamera](server/CPointCamera.md) |
| [CPointChildModifier](server/CPointChildModifier.md) | class | 1200 | 1 | [CPointEntity](server/CPointEntity.md) |
| [CPointClientCommand](server/CPointClientCommand.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CPointClientUIDialog](server/CPointClientUIDialog.md) | class | 2264 | 2 | [CBaseClientUIEntity](server/CBaseClientUIEntity.md) |
| [CPointClientUIWorldPanel](server/CPointClientUIWorldPanel.md) | class | 2352 | 25 | [CBaseClientUIEntity](server/CBaseClientUIEntity.md) |
| [CPointClientUIWorldTextPanel](server/CPointClientUIWorldTextPanel.md) | class | 2864 | 1 | [CPointClientUIWorldPanel](server/CPointClientUIWorldPanel.md) |
| [CPointCommentaryNode](server/CPointCommentaryNode.md) | class | 2624 | 30 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CPointEntity](server/CPointEntity.md) | class | 1192 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [CPointEntityFinder](server/CPointEntityFinder.md) | class | 1256 | 7 | [CBaseEntity](server/CBaseEntity.md) |
| [CPointGamestatsCounter](server/CPointGamestatsCounter.md) | class | 1208 | 2 | [CPointEntity](server/CPointEntity.md) |
| [CPointGiveAmmo](server/CPointGiveAmmo.md) | class | 1200 | 1 | [CPointEntity](server/CPointEntity.md) |
| [CPointGiveAmmo_API](server/CPointGiveAmmo_API.md) | class | 8 | 0 |  |
| [CPointHurt](server/CPointHurt.md) | class | 1224 | 6 | [CPointEntity](server/CPointEntity.md) |
| [CPointOrient](server/CPointOrient.md) | class | 1224 | 7 | [CBaseEntity](server/CBaseEntity.md) |
| [CPointPrefab](server/CPointPrefab.md) | class | 1328 | 7 | [CServerOnlyPointEntity](server/CServerOnlyPointEntity.md) |
| [CPointPrefabAPI](server/CPointPrefabAPI.md) | class | 8 | 0 |  |
| [CPointProximitySensor](server/CPointProximitySensor.md) | class | 1232 | 3 | [CPointEntity](server/CPointEntity.md) |
| [CPointPulse](server/CPointPulse.md) | class | 1192 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [CPointPush](server/CPointPush.md) | class | 1232 | 7 | [CPointEntity](server/CPointEntity.md) |
| [CPointServerCommand](server/CPointServerCommand.md) | class | 1192 | 0 | [CPointEntity](server/CPointEntity.md) |
| [CPointTeleport](server/CPointTeleport.md) | class | 1224 | 4 | [CServerOnlyPointEntity](server/CServerOnlyPointEntity.md) |
| [CPointTeleportAPI](server/CPointTeleportAPI.md) | class | 8 | 0 |  |
| [CPointTemplate](server/CPointTemplate.md) | class | 1344 | 12 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CPointTemplateAPI](server/CPointTemplateAPI.md) | class | 8 | 0 |  |
| [CPointValueRemapper](server/CPointValueRemapper.md) | class | 1616 | 44 | [CBaseEntity](server/CBaseEntity.md) |
| [CPointValueRemapperAPI](server/CPointValueRemapperAPI.md) | class | 8 | 0 |  |
| [CPointVelocitySensor](server/CPointVelocitySensor.md) | class | 1256 | 6 | [CPointEntity](server/CPointEntity.md) |
| [CPointWorldText](server/CPointWorldText.md) | class | 2592 | 16 | [CModelPointEntity](server/CModelPointEntity.md) |
| [CPostProcessingVolume](server/CPostProcessingVolume.md) | class | 2344 | 12 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CPrecipitation](server/CPrecipitation.md) | class | 2280 | 0 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CPrecipitationBlocker](server/CPrecipitationBlocker.md) | class | 1904 | 0 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CPrecipitationVData](server/CPrecipitationVData.md) | class | 752 | 11 | [CEntitySubclassVDataBase](server/CEntitySubclassVDataBase.md) |
| [CPropDataComponent](server/CPropDataComponent.md) | class | 64 | 10 | [CEntityComponent](entity2/CEntityComponent.md) |
| [CPropDoorRotating](server/CPropDoorRotating.md) | class | 3648 | 18 | [CBasePropDoor](server/CBasePropDoor.md) |
| [CPropDoorRotatingBreakable](server/CPropDoorRotatingBreakable.md) | class | 3680 | 4 | [CPropDoorRotating](server/CPropDoorRotating.md) |
| [CPulseCell_LerpCameraSettings](server/CPulseCell_LerpCameraSettings.md) | class | 328 | 3 | [CPulseCell_BaseLerp](pulse_runtime_lib/CPulseCell_BaseLerp.md) |
| [CPulseCell_LerpCameraSettings::CursorState_t](server/CPulseCell_LerpCameraSettings.CursorState_t.md) | class | 44 | 3 | [CPulseCell_BaseLerp::CursorState_t](pulse_runtime_lib/CPulseCell_BaseLerp.CursorState_t.md) |
| [CPulseCell_Outflow_ListenForAnimgraphTag](server/CPulseCell_Outflow_ListenForAnimgraphTag.md) | class | 368 | 3 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_Outflow_ListenForEntityOutput](server/CPulseCell_Outflow_ListenForEntityOutput.md) | class | 312 | 4 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_Outflow_ListenForEntityOutput::CursorState_t](server/CPulseCell_Outflow_ListenForEntityOutput.CursorState_t.md) | class | 4 | 1 |  |
| [CPulseCell_Outflow_PlayDynamicVCD](server/CPulseCell_Outflow_PlayDynamicVCD.md) | class | 312 | 0 | [CPulseCell_Outflow_PlayVCDBase](server/CPulseCell_Outflow_PlayVCDBase.md) |
| [CPulseCell_Outflow_PlaySceneBase](server/CPulseCell_Outflow_PlaySceneBase.md) | class | 312 | 2 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_Outflow_PlaySceneBase::CursorState_t](server/CPulseCell_Outflow_PlaySceneBase.CursorState_t.md) | class | 40 | 3 |  |
| [CPulseCell_Outflow_PlaySequence](server/CPulseCell_Outflow_PlaySequence.md) | class | 320 | 1 | [CPulseCell_Outflow_PlaySceneBase](server/CPulseCell_Outflow_PlaySceneBase.md) |
| [CPulseCell_Outflow_PlayVCD](server/CPulseCell_Outflow_PlayVCD.md) | class | 488 | 4 | [CPulseCell_Outflow_PlayVCDBase](server/CPulseCell_Outflow_PlayVCDBase.md) |
| [CPulseCell_Outflow_PlayVCD::VCDRequirementInfo_t](server/CPulseCell_Outflow_PlayVCD.VCDRequirementInfo_t.md) | class | 80 | 2 |  |
| [CPulseCell_Outflow_PlayVCDBase](server/CPulseCell_Outflow_PlayVCDBase.md) | class | 312 | 0 | [CPulseCell_Outflow_PlaySceneBase](server/CPulseCell_Outflow_PlaySceneBase.md) |
| [CPulseCell_Outflow_PlayVOLine](server/CPulseCell_Outflow_PlayVOLine.md) | class | 288 | 1 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_Outflow_PlayVOLine::CursorState_t](server/CPulseCell_Outflow_PlayVOLine.CursorState_t.md) | class | 4 | 1 |  |
| [CPulseCell_Outflow_ScriptedSequence](server/CPulseCell_Outflow_ScriptedSequence.md) | class | 408 | 9 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_Outflow_ScriptedSequence::CursorState_t](server/CPulseCell_Outflow_ScriptedSequence.CursorState_t.md) | class | 4 | 1 |  |
| [CPulseCell_PlaySequence](server/CPulseCell_PlaySequence.md) | class | 320 | 3 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_PlaySequence::CursorState_t](server/CPulseCell_PlaySequence.CursorState_t.md) | class | 4 | 1 |  |
| [CPulseCell_SoundEventStart](server/CPulseCell_SoundEventStart.md) | class | 80 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Step_EntFire](server/CPulseCell_Step_EntFire.md) | class | 80 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Step_FollowEntity](server/CPulseCell_Step_FollowEntity.md) | class | 88 | 2 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Step_SetAnimGraphParam](server/CPulseCell_Step_SetAnimGraphParam.md) | class | 80 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseFuncs_GameParticleManager](server/CPulseFuncs_GameParticleManager.md) | class | 1 | 0 |  |
| [CPulseGameBlackboard](server/CPulseGameBlackboard.md) | class | 1216 | 2 | [CBaseEntity](server/CBaseEntity.md) |
| [CPulseGraphInstance_GameBlackboard](server/CPulseGraphInstance_GameBlackboard.md) | class | 472 | 0 | [CPulseGraphInstance_ServerEntity](server/CPulseGraphInstance_ServerEntity.md) |
| [CPulseGraphInstance_ServerEntity](server/CPulseGraphInstance_ServerEntity.md) | class | 456 | 6 | [CBasePulseGraphInstance](pulse_runtime_lib/CBasePulseGraphInstance.md) |
| [CPulsePhysicsConstraintsFuncs](server/CPulsePhysicsConstraintsFuncs.md) | class | 1 | 0 |  |
| [CPulseServerCursor](server/CPulseServerCursor.md) | class | 240 | 2 | [CPulseExecCursor](pulse_runtime_lib/CPulseExecCursor.md) |
| [CPulseServerFuncs](server/CPulseServerFuncs.md) | class | 1 | 0 |  |
| [CPulseServerFuncs_Sounds](server/CPulseServerFuncs_Sounds.md) | class | 1 | 0 |  |
| [CPushable](server/CPushable.md) | class | 2120 | 0 | [CBreakable](server/CBreakable.md) |
| [CRR_Response](server/CRR_Response.md) | class | 464 | 10 |  |
| [CRagdollConstraint](server/CRagdollConstraint.md) | class | 1328 | 9 | [CPhysConstraint](server/CPhysConstraint.md) |
| [CRagdollMagnet](server/CRagdollMagnet.md) | class | 1216 | 4 | [CPointEntity](server/CPointEntity.md) |
| [CRagdollManager](server/CRagdollManager.md) | class | 1208 | 4 | [CBaseEntity](server/CBaseEntity.md) |
| [CRagdollProp](server/CRagdollProp.md) | class | 2848 | 34 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CRagdollPropAlias_physics_prop_ragdoll](server/CRagdollPropAlias_physics_prop_ragdoll.md) | class | 2848 | 0 | [CRagdollProp](server/CRagdollProp.md) |
| [CRagdollPropAttached](server/CRagdollPropAttached.md) | class | 2912 | 6 | [CRagdollProp](server/CRagdollProp.md) |
| [CRandSimTimer](server/CRandSimTimer.md) | class | 16 | 2 | [CSimpleSimTimer](server/CSimpleSimTimer.md) |
| [CRandStopwatch](server/CRandStopwatch.md) | class | 20 | 2 | [CStopwatchBase](server/CStopwatchBase.md) |
| [CRectLight](server/CRectLight.md) | class | 2656 | 1 | [CBarnLight](server/CBarnLight.md) |
| [CRelativeLocation](server/CRelativeLocation.md) | class | 56 | 4 |  |
| [CRelativeTransform](server/CRelativeTransform.md) | class | 96 | 4 |  |
| [CRemapFloat](server/CRemapFloat.md) | class | 16 | 1 |  |
| [CRenderComponent](server/CRenderComponent.md) | class | 176 | 5 | [CEntityComponent](entity2/CEntityComponent.md) |
| [CResponseCriteriaSet](server/CResponseCriteriaSet.md) | class | 56 | 2 |  |
| [CResponseQueue](server/CResponseQueue.md) | class | 80 | 1 |  |
| [CRetakeGameRules](server/CRetakeGameRules.md) | class | 496 | 6 |  |
| [CRevertSaved](server/CRevertSaved.md) | class | 1920 | 3 | [CModelPointEntity](server/CModelPointEntity.md) |
| [CRopeKeyframe](server/CRopeKeyframe.md) | class | 1992 | 21 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CRopeKeyframeAlias_move_rope](server/CRopeKeyframeAlias_move_rope.md) | class | 1992 | 0 | [CRopeKeyframe](server/CRopeKeyframe.md) |
| [CRopeOverlapHit](server/CRopeOverlapHit.md) | class | 32 | 2 |  |
| [CRotButton](server/CRotButton.md) | class | 2288 | 0 | [CBaseButton](server/CBaseButton.md) |
| [CRotDoor](server/CRotDoor.md) | class | 2432 | 1 | [CBaseDoor](server/CBaseDoor.md) |
| [CRotatorTarget](server/CRotatorTarget.md) | class | 1224 | 2 | [CPointEntity](server/CPointEntity.md) |
| [CRuleBrushEntity](server/CRuleBrushEntity.md) | class | 1912 | 0 | [CRuleEntity](server/CRuleEntity.md) |
| [CRuleEntity](server/CRuleEntity.md) | class | 1912 | 1 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CRulePointEntity](server/CRulePointEntity.md) | class | 1920 | 1 | [CRuleEntity](server/CRuleEntity.md) |
| [CSAdditionalMatchStats_t](server/CSAdditionalMatchStats_t.md) | class | 296 | 12 | [CSAdditionalPerRoundStats_t](server/CSAdditionalPerRoundStats_t.md) |
| [CSAdditionalPerRoundStats_t](server/CSAdditionalPerRoundStats_t.md) | class | 248 | 12 |  |
| [CSMatchStats_t](server/CSMatchStats_t.md) | class | 192 | 21 | [CSPerRoundStats_t](server/CSPerRoundStats_t.md) |
| [CSPerRoundStats_t](server/CSPerRoundStats_t.md) | class | 104 | 13 |  |
| [CSceneEntity](server/CSceneEntity.md) | class | 2032 | 65 | [CPointEntity](server/CPointEntity.md) |
| [CSceneEntityAlias_logic_choreographed_scene](server/CSceneEntityAlias_logic_choreographed_scene.md) | class | 2032 | 0 | [CSceneEntity](server/CSceneEntity.md) |
| [CSceneEventInfo](server/CSceneEventInfo.md) | class | 120 | 20 |  |
| [CSceneListManager](server/CSceneListManager.md) | class | 1408 | 3 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CScriptItem](server/CScriptItem.md) | class | 2576 | 1 | [CItem](server/CItem.md) |
| [CScriptNavBlocker](server/CScriptNavBlocker.md) | class | 1944 | 1 | [CFuncNavBlocker](server/CFuncNavBlocker.md) |
| [CScriptTriggerHurt](server/CScriptTriggerHurt.md) | class | 2432 | 1 | [CTriggerHurt](server/CTriggerHurt.md) |
| [CScriptTriggerMultiple](server/CScriptTriggerMultiple.md) | class | 2320 | 1 | [CTriggerMultiple](server/CTriggerMultiple.md) |
| [CScriptTriggerOnce](server/CScriptTriggerOnce.md) | class | 2320 | 1 | [CTriggerOnce](server/CTriggerOnce.md) |
| [CScriptTriggerPush](server/CScriptTriggerPush.md) | class | 2352 | 1 | [CTriggerPush](server/CTriggerPush.md) |
| [CScriptUniformRandomStream](server/CScriptUniformRandomStream.md) | class | 160 | 2 |  |
| [CScriptedSequence](server/CScriptedSequence.md) | class | 1776 | 77 | [CBaseEntity](server/CBaseEntity.md) |
| [CServerOnlyEntity](server/CServerOnlyEntity.md) | class | 1192 | 0 | [CBaseEntity](server/CBaseEntity.md) |
| [CServerOnlyModelEntity](server/CServerOnlyModelEntity.md) | class | 1904 | 0 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CServerOnlyPointEntity](server/CServerOnlyPointEntity.md) | class | 1192 | 0 | [CServerOnlyEntity](server/CServerOnlyEntity.md) |
| [CServerRagdollTrigger](server/CServerRagdollTrigger.md) | class | 2280 | 0 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CShatterGlassShard](server/CShatterGlassShard.md) | class | 184 | 28 |  |
| [CShatterGlassShardPhysics](server/CShatterGlassShardPhysics.md) | class | 2048 | 4 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CShower](server/CShower.md) | class | 1912 | 1 | [CModelPointEntity](server/CModelPointEntity.md) |
| [CSimTimer](server/CSimTimer.md) | class | 12 | 1 | [CSimpleSimTimer](server/CSimpleSimTimer.md) |
| [CSimpleMarkupVolumeTagged](server/CSimpleMarkupVolumeTagged.md) | class | 1968 | 0 | [CMarkupVolumeTagged](server/CMarkupVolumeTagged.md) |
| [CSimpleSimTimer](server/CSimpleSimTimer.md) | class | 8 | 2 |  |
| [CSimpleStopwatch](server/CSimpleStopwatch.md) | class | 12 | 0 | [CStopwatchBase](server/CStopwatchBase.md) |
| [CSingleplayRules](server/CSingleplayRules.md) | class | 216 | 1 | [CGameRules](server/CGameRules.md) |
| [CSkeletonAnimationController](server/CSkeletonAnimationController.md) | class | 16 | 1 | [ISkeletonAnimationController](server/ISkeletonAnimationController.md) |
| [CSkeletonInstance](server/CSkeletonInstance.md) | class | 1120 | 8 | [CGameSceneNode](server/CGameSceneNode.md) |
| [CSkillDamage](server/CSkillDamage.md) | class | 24 | 3 |  |
| [CSkillFloat](server/CSkillFloat.md) | class | 16 | 1 |  |
| [CSkillInt](server/CSkillInt.md) | class | 16 | 1 |  |
| [CSkyCamera](server/CSkyCamera.md) | class | 1352 | 4 | [CBaseEntity](server/CBaseEntity.md) |
| [CSkyboxReference](server/CSkyboxReference.md) | class | 1200 | 2 | [CBaseEntity](server/CBaseEntity.md) |
| [CSmokeGrenade](server/CSmokeGrenade.md) | class | 4256 | 0 | [CBaseCSGrenade](server/CBaseCSGrenade.md) |
| [CSmokeGrenadeProjectile](server/CSmokeGrenadeProjectile.md) | class | 11616 | 12 | [CBaseCSGrenadeProjectile](server/CBaseCSGrenadeProjectile.md) |
| [CSmoothFunc](server/CSmoothFunc.md) | class | 32 | 5 |  |
| [CSoundAreaEntityBase](server/CSoundAreaEntityBase.md) | class | 1224 | 3 | [CBaseEntity](server/CBaseEntity.md) |
| [CSoundAreaEntityOrientedBox](server/CSoundAreaEntityOrientedBox.md) | class | 1248 | 2 | [CSoundAreaEntityBase](server/CSoundAreaEntityBase.md) |
| [CSoundAreaEntitySphere](server/CSoundAreaEntitySphere.md) | class | 1232 | 1 | [CSoundAreaEntityBase](server/CSoundAreaEntityBase.md) |
| [CSoundEnvelope](server/CSoundEnvelope.md) | class | 16 | 4 |  |
| [CSoundEventAABBEntity](server/CSoundEventAABBEntity.md) | class | 1408 | 2 | [CSoundEventEntity](server/CSoundEventEntity.md) |
| [CSoundEventConeEntity](server/CSoundEventConeEntity.md) | class | 1408 | 5 | [CSoundEventEntity](server/CSoundEventEntity.md) |
| [CSoundEventEntity](server/CSoundEventEntity.md) | class | 1384 | 14 | [CBaseEntity](server/CBaseEntity.md) |
| [CSoundEventEntityAlias_snd_event_point](server/CSoundEventEntityAlias_snd_event_point.md) | class | 1384 | 0 | [CSoundEventEntity](server/CSoundEventEntity.md) |
| [CSoundEventOBBEntity](server/CSoundEventOBBEntity.md) | class | 1424 | 2 | [CSoundEventEntity](server/CSoundEventEntity.md) |
| [CSoundEventParameter](server/CSoundEventParameter.md) | class | 1232 | 2 | [CBaseEntity](server/CBaseEntity.md) |
| [CSoundEventPathCornerEntity](server/CSoundEventPathCornerEntity.md) | class | 1544 | 7 | [CSoundEventEntity](server/CSoundEventEntity.md) |
| [CSoundEventSphereEntity](server/CSoundEventSphereEntity.md) | class | 1392 | 1 | [CSoundEventEntity](server/CSoundEventEntity.md) |
| [CSoundOpvarSetAABBEntity](server/CSoundOpvarSetAABBEntity.md) | class | 1704 | 0 | [CSoundOpvarSetBoxEntity](server/CSoundOpvarSetBoxEntity.md) |
| [CSoundOpvarSetAutoRoomEntity](server/CSoundOpvarSetAutoRoomEntity.md) | class | 1664 | 5 | [CSoundOpvarSetPointEntity](server/CSoundOpvarSetPointEntity.md) |
| [CSoundOpvarSetBoxEntity](server/CSoundOpvarSetBoxEntity.md) | class | 1704 | 9 | [CSoundOpvarSetPointEntity](server/CSoundOpvarSetPointEntity.md) |
| [CSoundOpvarSetEntity](server/CSoundOpvarSetEntity.md) | class | 1280 | 8 | [CBaseEntity](server/CBaseEntity.md) |
| [CSoundOpvarSetOBBEntity](server/CSoundOpvarSetOBBEntity.md) | class | 1704 | 0 | [CSoundOpvarSetAABBEntity](server/CSoundOpvarSetAABBEntity.md) |
| [CSoundOpvarSetOBBWindEntity](server/CSoundOpvarSetOBBWindEntity.md) | class | 1424 | 8 | [CSoundOpvarSetPointBase](server/CSoundOpvarSetPointBase.md) |
| [CSoundOpvarSetPathCornerEntity](server/CSoundOpvarSetPathCornerEntity.md) | class | 1648 | 4 | [CSoundOpvarSetPointEntity](server/CSoundOpvarSetPointEntity.md) |
| [CSoundOpvarSetPointBase](server/CSoundOpvarSetPointBase.md) | class | 1360 | 11 | [CBaseEntity](server/CBaseEntity.md) |
| [CSoundOpvarSetPointEntity](server/CSoundOpvarSetPointEntity.md) | class | 1600 | 24 | [CSoundOpvarSetPointBase](server/CSoundOpvarSetPointBase.md) |
| [CSoundPatch](server/CSoundPatch.md) | class | 176 | 13 |  |
| [CSoundStackSave](server/CSoundStackSave.md) | class | 1200 | 1 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CSplineConstraint](server/CSplineConstraint.md) | class | 1464 | 15 | [CPhysConstraint](server/CPhysConstraint.md) |
| [CSpotlightEnd](server/CSpotlightEnd.md) | class | 1936 | 4 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CSprite](server/CSprite.md) | class | 2016 | 24 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CSpriteAlias_env_glow](server/CSpriteAlias_env_glow.md) | class | 2016 | 0 | [CSprite](server/CSprite.md) |
| [CSpriteOriented](server/CSpriteOriented.md) | class | 2016 | 0 | [CSprite](server/CSprite.md) |
| [CStopwatch](server/CStopwatch.md) | class | 16 | 1 | [CStopwatchBase](server/CStopwatchBase.md) |
| [CStopwatchBase](server/CStopwatchBase.md) | class | 12 | 1 | [CSimpleSimTimer](server/CSimpleSimTimer.md) |
| [CTakeDamageInfo](server/CTakeDamageInfo.md) | class | 280 | 22 |  |
| [CTakeDamageResult](server/CTakeDamageResult.md) | class | 96 | 15 |  |
| [CTakeDamageResultAPI](server/CTakeDamageResultAPI.md) | class | 8 | 0 |  |
| [CTakeDamageSummaryScopeGuard](server/CTakeDamageSummaryScopeGuard.md) | class | 32 | 1 |  |
| [CTankTargetChange](server/CTankTargetChange.md) | class | 1216 | 2 | [CPointEntity](server/CPointEntity.md) |
| [CTankTrainAI](server/CTankTrainAI.md) | class | 1256 | 7 | [CPointEntity](server/CPointEntity.md) |
| [CTeam](server/CTeam.md) | class | 1376 | 4 | [CBaseEntity](server/CBaseEntity.md) |
| [CTeamplayRules](server/CTeamplayRules.md) | class | 208 | 0 | [CMultiplayRules](server/CMultiplayRules.md) |
| [CTestEffect](server/CTestEffect.md) | class | 1400 | 5 | [CBaseEntity](server/CBaseEntity.md) |
| [CTestPulseIO](server/CTestPulseIO.md) | class | 1952 | 23 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CTestPulseIO::EntityHandleIntArgs_t](server/CTestPulseIO.EntityHandleIntArgs_t.md) | class | 8 | 2 |  |
| [CTestPulseIO::EntityNameStringArgs_t](server/CTestPulseIO.EntityNameStringArgs_t.md) | class | 16 | 2 |  |
| [CTestPulseIO::FloatStringArgs_t](server/CTestPulseIO.FloatStringArgs_t.md) | class | 16 | 2 |  |
| [CTestPulseIO::ThreeStringArgs_t](server/CTestPulseIO.ThreeStringArgs_t.md) | class | 24 | 3 |  |
| [CTestPulseIOAPI](server/CTestPulseIOAPI.md) | class | 8 | 0 |  |
| [CTestPulseIOComponent](server/CTestPulseIOComponent.md) | class | 48 | 2 |  |
| [CTestPulseIOComponent_API](server/CTestPulseIOComponent_API.md) | class | 8 | 0 |  |
| [CTestPulseIOComponent_Derived](server/CTestPulseIOComponent_Derived.md) | class | 48 | 0 | [CTestPulseIOComponent](server/CTestPulseIOComponent.md) |
| [CTestPulseIOComponent_DerivedAPI](server/CTestPulseIOComponent_DerivedAPI.md) | class | 8 | 0 |  |
| [CTextureBasedAnimatable](server/CTextureBasedAnimatable.md) | class | 1960 | 8 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CTimeline](server/CTimeline.md) | class | 552 | 7 | [IntervalTimer](server/IntervalTimer.md) |
| [CTimerEntity](server/CTimerEntity.md) | class | 1304 | 13 | [CLogicalEntity](server/CLogicalEntity.md) |
| [CTonemapController2](server/CTonemapController2.md) | class | 1216 | 5 | [CBaseEntity](server/CBaseEntity.md) |
| [CTonemapController2Alias_env_tonemap_controller2](server/CTonemapController2Alias_env_tonemap_controller2.md) | class | 1216 | 0 | [CTonemapController2](server/CTonemapController2.md) |
| [CTonemapTrigger](server/CTonemapTrigger.md) | class | 2296 | 2 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTouchExpansionComponent](server/CTouchExpansionComponent.md) | class | 80 | 0 | [CEntityComponent](entity2/CEntityComponent.md) |
| [CTriggerActiveWeaponDetect](server/CTriggerActiveWeaponDetect.md) | class | 2312 | 2 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerBombReset](server/CTriggerBombReset.md) | class | 2280 | 0 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerBrush](server/CTriggerBrush.md) | class | 1984 | 5 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CTriggerBuoyancy](server/CTriggerBuoyancy.md) | class | 2568 | 2 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerCallback](server/CTriggerCallback.md) | class | 2288 | 0 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerDetectBulletFire](server/CTriggerDetectBulletFire.md) | class | 2312 | 2 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerDetectExplosion](server/CTriggerDetectExplosion.md) | class | 2344 | 1 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerFan](server/CTriggerFan.md) | class | 2480 | 25 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerGameEvent](server/CTriggerGameEvent.md) | class | 2304 | 3 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerGravity](server/CTriggerGravity.md) | class | 2280 | 0 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerHostageReset](server/CTriggerHostageReset.md) | class | 2280 | 0 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerHurt](server/CTriggerHurt.md) | class | 2416 | 14 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerImpact](server/CTriggerImpact.md) | class | 2360 | 4 | [CTriggerMultiple](server/CTriggerMultiple.md) |
| [CTriggerLerpObject](server/CTriggerLerpObject.md) | class | 2440 | 16 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerLook](server/CTriggerLook.md) | class | 2408 | 15 | [CTriggerOnce](server/CTriggerOnce.md) |
| [CTriggerMultiple](server/CTriggerMultiple.md) | class | 2304 | 1 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerOnce](server/CTriggerOnce.md) | class | 2304 | 0 | [CTriggerMultiple](server/CTriggerMultiple.md) |
| [CTriggerPhysics](server/CTriggerPhysics.md) | class | 2376 | 14 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerProximity](server/CTriggerProximity.md) | class | 2336 | 5 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerPush](server/CTriggerPush.md) | class | 2336 | 8 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerRemove](server/CTriggerRemove.md) | class | 2304 | 1 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerSave](server/CTriggerSave.md) | class | 2296 | 4 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerSndSosOpvar](server/CTriggerSndSosOpvar.md) | class | 3144 | 14 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerSoundscape](server/CTriggerSoundscape.md) | class | 2320 | 3 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerTeleport](server/CTriggerTeleport.md) | class | 2296 | 4 | [CBaseTrigger](server/CBaseTrigger.md) |
| [CTriggerVolume](server/CTriggerVolume.md) | class | 1920 | 2 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CVectorExponentialMovingAverage](server/CVectorExponentialMovingAverage.md) | class | 44 | 0 |  |
| [CVectorMovingAverage](server/CVectorMovingAverage.md) | class | 32 | 0 |  |
| [CVoteController](server/CVoteController.md) | class | 1624 | 14 | [CBaseEntity](server/CBaseEntity.md) |
| [CWaterBullet](server/CWaterBullet.md) | class | 2400 | 0 | [CBaseAnimGraph](server/CBaseAnimGraph.md) |
| [CWeaponAWP](server/CWeaponAWP.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponAug](server/CWeaponAug.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponBaseItem](server/CWeaponBaseItem.md) | class | 4192 | 2 | [CCSWeaponBase](server/CCSWeaponBase.md) |
| [CWeaponBizon](server/CWeaponBizon.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponCZ75a](server/CWeaponCZ75a.md) | class | 4224 | 1 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponElite](server/CWeaponElite.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponFamas](server/CWeaponFamas.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponFiveSeven](server/CWeaponFiveSeven.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponG3SG1](server/CWeaponG3SG1.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponGalilAR](server/CWeaponGalilAR.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponGlock](server/CWeaponGlock.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponHKP2000](server/CWeaponHKP2000.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponM249](server/CWeaponM249.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponM4A1](server/CWeaponM4A1.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponM4A1Silencer](server/CWeaponM4A1Silencer.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponMAC10](server/CWeaponMAC10.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponMP5SD](server/CWeaponMP5SD.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponMP7](server/CWeaponMP7.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponMP9](server/CWeaponMP9.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponMag7](server/CWeaponMag7.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponNOVA](server/CWeaponNOVA.md) | class | 4176 | 0 | [CCSWeaponBaseShotgun](server/CCSWeaponBaseShotgun.md) |
| [CWeaponNegev](server/CWeaponNegev.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponP250](server/CWeaponP250.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponP90](server/CWeaponP90.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponRevolver](server/CWeaponRevolver.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponSCAR20](server/CWeaponSCAR20.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponSG556](server/CWeaponSG556.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponSSG08](server/CWeaponSSG08.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponSawedoff](server/CWeaponSawedoff.md) | class | 4176 | 0 | [CCSWeaponBaseShotgun](server/CCSWeaponBaseShotgun.md) |
| [CWeaponTaser](server/CWeaponTaser.md) | class | 4224 | 2 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponTec9](server/CWeaponTec9.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponUMP45](server/CWeaponUMP45.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponUSPSilencer](server/CWeaponUSPSilencer.md) | class | 4208 | 0 | [CCSWeaponBaseGun](server/CCSWeaponBaseGun.md) |
| [CWeaponXM1014](server/CWeaponXM1014.md) | class | 4176 | 0 | [CCSWeaponBaseShotgun](server/CCSWeaponBaseShotgun.md) |
| [CWorld](server/CWorld.md) | class | 1904 | 0 | [CBaseModelEntity](server/CBaseModelEntity.md) |
| [CWorldCompositionChunkReferenceElement_t](server/CWorldCompositionChunkReferenceElement_t.md) | class | 16 | 2 |  |
| [CodeGenAABB_t](server/CodeGenAABB_t.md) | class | 24 | 2 |  |
| [ConstraintSoundInfo](server/ConstraintSoundInfo.md) | class | 152 | 10 |  |
| [CountdownTimer](server/CountdownTimer.md) | class | 24 | 4 |  |
| [DebugDrawBoneTransforms_t](server/DebugDrawBoneTransforms_t.md) | class | 4144 | 1 | [DebugSnapshotBaseStructuredData_t](server/DebugSnapshotBaseStructuredData_t.md) |
| [DebugSnapshotBaseStructuredData_t](server/DebugSnapshotBaseStructuredData_t.md) | class | 8 | 0 |  |
| [DecalGroupOption_t](server/DecalGroupOption_t.md) | class | 32 | 6 |  |
| [DestructiblePartDamageRequestAPI](server/DestructiblePartDamageRequestAPI.md) | class | 8 | 0 |  |
| [DestructiblePartDamageRequest_t](server/DestructiblePartDamageRequest_t.md) | class | 60 | 10 |  |
| [DynamicVolumeDef_t](server/DynamicVolumeDef_t.md) | class | 48 | 8 |  |
| [EngineCountdownTimer](server/EngineCountdownTimer.md) | class | 24 | 3 |  |
| [EntityRenderAttribute_t](server/EntityRenderAttribute_t.md) | class | 72 | 2 |  |
| [EntitySpottedState_t](server/EntitySpottedState_t.md) | class | 24 | 2 |  |
| [ExternalAnimGraphHandle_t](server/ExternalAnimGraphHandle_t.md) | class | 4 | 1 |  |
| [FilterDamageType](server/FilterDamageType.md) | class | 1256 | 1 | [CBaseFilter](server/CBaseFilter.md) |
| [FilterHealth](server/FilterHealth.md) | class | 1264 | 3 | [CBaseFilter](server/CBaseFilter.md) |
| [FuncMoverMovementSummary_t](server/FuncMoverMovementSummary_t.md) | class | 32 | 8 |  |
| [FuncRotatorRotationSummary_t](server/FuncRotatorRotationSummary_t.md) | class | 8 | 2 |  |
| [GAME_HEADER](server/GAME_HEADER.md) | class | 32 | 4 |  |
| [GameAmmoTypeInfo_t](server/GameAmmoTypeInfo_t.md) | class | 80 | 2 | [AmmoTypeInfo_t](server/AmmoTypeInfo_t.md) |
| [HUDPanelDialogVariableString_t](server/HUDPanelDialogVariableString_t.md) | class | 32 | 4 |  |
| [HUDPanelHasClass_t](server/HUDPanelHasClass_t.md) | class | 8 | 3 |  |
| [HullFlags_t](server/HullFlags_t.md) | class | 10 | 10 |  |
| [IChoreoServices](server/IChoreoServices.md) | class | 8 | 0 |  |
| [IEconItemInterface](server/IEconItemInterface.md) | class | 8 | 0 |  |
| [IHasAttributes](server/IHasAttributes.md) | class | 8 | 0 |  |
| [INavObstacle](server/INavObstacle.md) | class | 16 | 1 |  |
| [INavPathCostAreaFilter](server/INavPathCostAreaFilter.md) | class | 8 | 0 |  |
| [IRagdoll](server/IRagdoll.md) | class | 8 | 0 |  |
| [ISkeletonAnimationController](server/ISkeletonAnimationController.md) | class | 8 | 0 |  |
| [IntervalTimer](server/IntervalTimer.md) | class | 16 | 2 |  |
| [ModelConfigHandle_t](server/ModelConfigHandle_t.md) | class | 4 | 1 |  |
| [ParticleIndex_t](server/ParticleIndex_t.md) | class | 4 | 1 |  |
| [ParticleNode_t](server/ParticleNode_t.md) | class | 36 | 7 |  |
| [PathMoverEntitySpawn](server/PathMoverEntitySpawn.md) | class | 32 | 2 |  |
| [PhysBlockHeader_t](server/PhysBlockHeader_t.md) | class | 16 | 2 |  |
| [PhysObjectHeader_t](server/PhysObjectHeader_t.md) | class | 64 | 8 |  |
| [PhysicsRagdollPose_t](server/PhysicsRagdollPose_t.md) | class | 40 | 3 |  |
| [PointCameraSettings_t](server/PointCameraSettings_t.md) | class | 16 | 4 |  |
| [PrecipitationFilter_t](server/PrecipitationFilter_t.md) | class | 4 | 1 |  |
| [PulseScriptedSequenceData_t](server/PulseScriptedSequenceData_t.md) | class | 56 | 12 |  |
| [QuestProgress](server/QuestProgress.md) | class | 1 | 0 |  |
| [RagdollCreationParams_t](server/RagdollCreationParams_t.md) | class | 24 | 5 |  |
| [RelationshipOverride_t](server/RelationshipOverride_t.md) | class | 16 | 2 | [Relationship_t](server/Relationship_t.md) |
| [Relationship_t](server/Relationship_t.md) | class | 8 | 2 |  |
| [ResponseContext_t](server/ResponseContext_t.md) | class | 24 | 3 |  |
| [ResponseFollowup](server/ResponseFollowup.md) | class | 49 | 8 |  |
| [ResponseParams](server/ResponseParams.md) | class | 32 | 3 |  |
| [RotatorHistoryEntry_t](server/RotatorHistoryEntry_t.md) | class | 32 | 2 |  |
| [RotatorQueueEntry_t](server/RotatorQueueEntry_t.md) | class | 32 | 2 |  |
| [SAVE_HEADER](server/SAVE_HEADER.md) | class | 96 | 7 |  |
| [SPAWNGROUP_HEADER](server/SPAWNGROUP_HEADER.md) | class | 80 | 5 |  |
| [SceneEventId_t](server/SceneEventId_t.md) | class | 4 | 1 |  |
| [SellbackPurchaseEntry_t](server/SellbackPurchaseEntry_t.md) | class | 72 | 5 |  |
| [SequenceHistory_t](server/SequenceHistory_t.md) | class | 24 | 6 |  |
| [ServerAuthoritativeWeaponSlot_t](server/ServerAuthoritativeWeaponSlot_t.md) | class | 56 | 3 |  |
| [SimpleConstraintSoundProfile](server/SimpleConstraintSoundProfile.md) | class | 32 | 5 |  |
| [SoundCommand_t](server/SoundCommand_t.md) | class | 32 | 4 |  |
| [SoundOpvarTraceResult_t](server/SoundOpvarTraceResult_t.md) | class | 20 | 3 |  |
| [SoundeventPathCornerPairNetworked_t](server/SoundeventPathCornerPairNetworked_t.md) | class | 36 | 5 |  |
| [SpawnPoint](server/SpawnPoint.md) | class | 1208 | 3 | [CServerOnlyPointEntity](server/CServerOnlyPointEntity.md) |
| [SpawnPoint_API](server/SpawnPoint_API.md) | class | 8 | 0 |  |
| [SummaryTakeDamageInfo_t](server/SummaryTakeDamageInfo_t.md) | class | 392 | 4 |  |
| [VPhysicsCollisionAttribute_t](server/VPhysicsCollisionAttribute_t.md) | class | 48 | 11 |  |
| [VelocitySampler](server/VelocitySampler.md) | class | 20 | 3 |  |
| [ViewAngleServerChange_t](server/ViewAngleServerChange_t.md) | class | 72 | 3 |  |
| [WaterWheelDrag_t](server/WaterWheelDrag_t.md) | class | 8 | 2 |  |
| [WaterWheelFrictionScale_t](server/WaterWheelFrictionScale_t.md) | class | 8 | 2 |  |
| [WeaponPurchaseCount_t](server/WeaponPurchaseCount_t.md) | class | 56 | 2 |  |
| [WeaponPurchaseTracker_t](server/WeaponPurchaseTracker_t.md) | class | 112 | 1 |  |
| [WrappedPhysicsJoint_t](server/WrappedPhysicsJoint_t.md) | class | 8 | 1 |  |
| [audioparams_t](server/audioparams_t.md) | class | 120 | 5 |  |
| [dynpitchvol_base_t](server/dynpitchvol_base_t.md) | class | 100 | 25 |  |
| [dynpitchvol_t](server/dynpitchvol_t.md) | class | 100 | 0 | [dynpitchvol_base_t](server/dynpitchvol_base_t.md) |
| [entitytable_t](server/entitytable_t.md) | class | 80 | 10 |  |
| [fogparams_t](server/fogparams_t.md) | class | 104 | 25 |  |
| [fogplayerparams_t](server/fogplayerparams_t.md) | class | 64 | 14 |  |
| [globalentity_t](server/globalentity_t.md) | class | 12 | 4 |  |
| [globalentitydatabase_t](server/globalentitydatabase_t.md) | class | 120 | 1 |  |
| [hudtextparms_t](server/hudtextparms_t.md) | class | 20 | 6 |  |
| [lerpdata_t](server/lerpdata_t.md) | class | 80 | 6 |  |
| [levellist_t](server/levellist_t.md) | class | 48 | 5 |  |
| [locksound_t](server/locksound_t.md) | class | 32 | 3 |  |
| [magnetted_objects_t](server/magnetted_objects_t.md) | class | 16 | 1 |  |
| [modifiedconvars_t](server/modifiedconvars_t.md) | class | 384 | 3 |  |
| [physics_save_sphere_t](server/physics_save_sphere_t.md) | class | 4 | 1 |  |
| [ragdoll_t](server/ragdoll_t.md) | class | 80 | 5 |  |
| [ragdollelement_t](server/ragdollelement_t.md) | class | 48 | 4 |  |
| [ragdollhierarchyjoint_t](server/ragdollhierarchyjoint_t.md) | class | 16 | 2 |  |
| [shard_model_desc_t](server/shard_model_desc_t.md) | class | 128 | 13 |  |
| [sky3dparams_t](server/sky3dparams_t.md) | class | 144 | 6 |  |
| [sndopvarlatchdata_t](server/sndopvarlatchdata_t.md) | class | 48 | 5 |  |
| [thinkfunc_t](server/thinkfunc_t.md) | class | 32 | 5 |  |
| [AmmoFlags_t](server/AmmoFlags_t.md) | enum | — | 3 |  |
| [AmmoPosition_t](server/AmmoPosition_t.md) | enum | — | 4 |  |
| [AnimGraphDebugDrawType_t](server/AnimGraphDebugDrawType_t.md) | enum | — | 5 |  |
| [AnimLoopMode_t](server/AnimLoopMode_t.md) | enum | — | 5 |  |
| [AnimationAlgorithm_t](server/AnimationAlgorithm_t.md) | enum | — | 6 |  |
| [BeamType_t](server/BeamType_t.md) | enum | — | 7 |  |
| [BeginDeathLifeStateTransition_t](server/BeginDeathLifeStateTransition_t.md) | enum | — | 2 |  |
| [Bidirectional_Messages](server/Bidirectional_Messages.md) | enum | — | 4 |  |
| [BloodType](server/BloodType.md) | enum | — | 9 |  |
| [BodySectionMutex_t](server/BodySectionMutex_t.md) | enum | — | 4 |  |
| [BreakableContentsType_t](server/BreakableContentsType_t.md) | enum | — | 4 |  |
| [BrushSolidities_e](server/BrushSolidities_e.md) | enum | — | 3 |  |
| [C4LightEffect_t](server/C4LightEffect_t.md) | enum | — | 3 |  |
| [CCSPlayerAnimationState::AirAction_t](server/CCSPlayerAnimationState.AirAction_t.md) | enum | — | 4 |  |
| [CCSPlayerAnimationState::Direction_t](server/CCSPlayerAnimationState.Direction_t.md) | enum | — | 9 |  |
| [CCSPlayerAnimationState::GroundMoveState_t](server/CCSPlayerAnimationState.GroundMoveState_t.md) | enum | — | 7 |  |
| [CCSPlayerAnimationState::MoveType_t](server/CCSPlayerAnimationState.MoveType_t.md) | enum | — | 4 |  |
| [CDebugOverlayCombinedTypes_t](server/CDebugOverlayCombinedTypes_t.md) | enum | — | 3 |  |
| [CDebugOverlayFilterTextType_t](server/CDebugOverlayFilterTextType_t.md) | enum | — | 4 |  |
| [CDebugOverlayFilterType_t](server/CDebugOverlayFilterType_t.md) | enum | — | 11 |  |
| [CFuncMover::FollowConstraint_t](server/CFuncMover.FollowConstraint_t.md) | enum | — | 4 |  |
| [CFuncMover::FollowEntityDirection_t](server/CFuncMover.FollowEntityDirection_t.md) | enum | — | 3 |  |
| [CFuncMover::Move_t](server/CFuncMover.Move_t.md) | enum | — | 3 |  |
| [CFuncMover::OrientationUpdate_t](server/CFuncMover.OrientationUpdate_t.md) | enum | — | 9 |  |
| [CFuncMover::PathRebuildStrategy_t](server/CFuncMover.PathRebuildStrategy_t.md) | enum | — | 3 |  |
| [CFuncMover::TransitionToPathNodeAction_t](server/CFuncMover.TransitionToPathNodeAction_t.md) | enum | — | 4 |  |
| [CFuncRotator::Rotate_t](server/CFuncRotator.Rotate_t.md) | enum | — | 7 |  |
| [CFuncRotator::RotationAxis_t](server/CFuncRotator.RotationAxis_t.md) | enum | — | 4 |  |
| [CInfoChoreoLocatorShapeType_t](server/CInfoChoreoLocatorShapeType_t.md) | enum | — | 5 |  |
| [CLC_Messages](server/CLC_Messages.md) | enum | — | 14 |  |
| [CLogicBranchList::LogicBranchListenerLastState_t](server/CLogicBranchList.LogicBranchListenerLastState_t.md) | enum | — | 4 |  |
| [CPhysicsProp::CrateType_t](server/CPhysicsProp.CrateType_t.md) | enum | — | 2 |  |
| [CRR_Response::ResponseEnum_t](server/CRR_Response.ResponseEnum_t.md) | enum | — | 2 |  |
| [CSPlayerBlockingUseAction_t](server/CSPlayerBlockingUseAction_t.md) | enum | — | 8 |  |
| [CSPlayerState](server/CSPlayerState.md) | enum | — | 10 |  |
| [CSWeaponCategory](server/CSWeaponCategory.md) | enum | — | 7 |  |
| [CSWeaponMode](server/CSWeaponMode.md) | enum | — | 3 |  |
| [CSWeaponNameID](server/CSWeaponNameID.md) | enum | — | 66 |  |
| [CSWeaponSilencerType](server/CSWeaponSilencerType.md) | enum | — | 3 |  |
| [CSWeaponType](server/CSWeaponType.md) | enum | — | 13 |  |
| [CanPlaySequence_t](server/CanPlaySequence_t.md) | enum | — | 3 |  |
| [ChatIgnoreType_t](server/ChatIgnoreType_t.md) | enum | — | 3 |  |
| [ChoreoExternalAnimgraphControlState_t](server/ChoreoExternalAnimgraphControlState_t.md) | enum | — | 8 |  |
| [ChoreoLookAtMode_t](server/ChoreoLookAtMode_t.md) | enum | — | 4 |  |
| [ChoreoLookAtSpeed_t](server/ChoreoLookAtSpeed_t.md) | enum | — | 4 |  |
| [ChoreoStrafeMode_t](server/ChoreoStrafeMode_t.md) | enum | — | 3 |  |
| [Class_T](server/Class_T.md) | enum | — | 14 |  |
| [DIALOG_TYPE](server/DIALOG_TYPE.md) | enum | — | 5 |  |
| [DamageTypes_t](server/DamageTypes_t.md) | enum | — | 22 |  |
| [DebugOverlayBits_t](server/DebugOverlayBits_t.md) | enum | — | 43 |  |
| [DecalFlags_t](server/DecalFlags_t.md) | enum | — | 5 |  |
| [DestructiblePartDestructionDeathBehavior_t](server/DestructiblePartDestructionDeathBehavior_t.md) | enum | — | 4 |  |
| [Disposition_t](server/Disposition_t.md) | enum | — | 10 |  |
| [DoorState_t](server/DoorState_t.md) | enum | — | 5 |  |
| [EBaseClientMessages](server/EBaseClientMessages.md) | enum | — | 7 |  |
| [EBaseEntityMessages](server/EBaseEntityMessages.md) | enum | — | 5 |  |
| [EBaseGameEvents](server/EBaseGameEvents.md) | enum | — | 15 |  |
| [EBasePredictionEvents](server/EBasePredictionEvents.md) | enum | — | 3 |  |
| [EBaseUserMessages](server/EBaseUserMessages.md) | enum | — | 51 |  |
| [ECSPredictionEvents](server/ECSPredictionEvents.md) | enum | — | 2 |  |
| [ECSUsrMsg_DisconnectToLobby_Action](server/ECSUsrMsg_DisconnectToLobby_Action.md) | enum | — | 2 |  |
| [EChickenActivity](server/EChickenActivity.md) | enum | — | 7 |  |
| [EClientReportingVersion](server/EClientReportingVersion.md) | enum | — | 3 |  |
| [EClientUIEvent](server/EClientUIEvent.md) | enum | — | 3 |  |
| [ECommunityItemAttribute](server/ECommunityItemAttribute.md) | enum | — | 10 |  |
| [ECommunityItemClass](server/ECommunityItemClass.md) | enum | — | 11 |  |
| [EContributionScoreFlag_t](server/EContributionScoreFlag_t.md) | enum | — | 3 |  |
| [ECsgoGCMsg](server/ECsgoGCMsg.md) | enum | — | 109 |  |
| [ECsgoGameEvents](server/ECsgoGameEvents.md) | enum | — | 4 |  |
| [ECsgoSteamUserStat](server/ECsgoSteamUserStat.md) | enum | — | 3 |  |
| [ECstrike15UserMessages](server/ECstrike15UserMessages.md) | enum | — | 79 |  |
| [EDemoCommands](server/EDemoCommands.md) | enum | — | 22 |  |
| [EDestructiblePartDamagePassThroughType](server/EDestructiblePartDamagePassThroughType.md) | enum | — | 4 |  |
| [EDestructiblePartRadiusDamageApplyType](server/EDestructiblePartRadiusDamageApplyType.md) | enum | — | 2 |  |
| [EDestructibleParts_DestroyParameterFlags](server/EDestructibleParts_DestroyParameterFlags.md) | enum | — | 9 |  |
| [EGCBaseClientMsg](server/EGCBaseClientMsg.md) | enum | — | 11 |  |
| [EGCBaseMsg](server/EGCBaseMsg.md) | enum | — | 15 |  |
| [EGCBaseProtoObjectTypes](server/EGCBaseProtoObjectTypes.md) | enum | — | 2 |  |
| [EGCItemCustomizationNotification](server/EGCItemCustomizationNotification.md) | enum | — | 28 |  |
| [EGCItemMsg](server/EGCItemMsg.md) | enum | — | 133 |  |
| [EGCMsgResponse](server/EGCMsgResponse.md) | enum | — | 11 |  |
| [EGCSystemMsg](server/EGCSystemMsg.md) | enum | — | 92 |  |
| [EGCToGCMsg](server/EGCToGCMsg.md) | enum | — | 8 |  |
| [EHapticPulseType](server/EHapticPulseType.md) | enum | — | 3 |  |
| [EHitGroup](server/EHitGroup.md) | enum | — | 10 |  |
| [EHudPanelClassStatus_t](server/EHudPanelClassStatus_t.md) | enum | — | 3 |  |
| [EInButtonState](server/EInButtonState.md) | enum | — | 9 |  |
| [EInitSystemResult](server/EInitSystemResult.md) | enum | — | 9 |  |
| [EKillTypes_t](server/EKillTypes_t.md) | enum | — | 8 |  |
| [ENetworkDisconnectionReason](server/ENetworkDisconnectionReason.md) | enum | — | 121 |  |
| [EOverrideBlockLOS_t](server/EOverrideBlockLOS_t.md) | enum | — | 3 |  |
| [EProceduralRagdollWeightIndexPropagationMethod](server/EProceduralRagdollWeightIndexPropagationMethod.md) | enum | — | 2 |  |
| [EProtoDebugVisiblity](server/EProtoDebugVisiblity.md) | enum | — | 5 |  |
| [EQueryCvarValueStatus](server/EQueryCvarValueStatus.md) | enum | — | 4 |  |
| [ESOMsg](server/ESOMsg.md) | enum | — | 8 |  |
| [ESource2PlayStatsFieldType](server/ESource2PlayStatsFieldType.md) | enum | — | 18 |  |
| [ESplitScreenMessageType](server/ESplitScreenMessageType.md) | enum | — | 2 |  |
| [ETEProtobufIds](server/ETEProtobufIds.md) | enum | — | 23 |  |
| [ETeam](server/ETeam.md) | enum | — | 4 |  |
| [EUnlockStyle](server/EUnlockStyle.md) | enum | — | 6 |  |
| [EWeaponType](server/EWeaponType.md) | enum | — | 12 |  |
| [EntFinderMethod_t](server/EntFinderMethod_t.md) | enum | — | 3 |  |
| [EntityAttachmentType_t](server/EntityAttachmentType_t.md) | enum | — | 4 |  |
| [EntityDissolveType_t](server/EntityDissolveType_t.md) | enum | — | 5 |  |
| [EntityDistanceMode_t](server/EntityDistanceMode_t.md) | enum | — | 3 |  |
| [EntityEffects_t](server/EntityEffects_t.md) | enum | — | 7 |  |
| [EntityPlatformTypes_t](server/EntityPlatformTypes_t.md) | enum | — | 3 |  |
| [EntitySubclassScope_t](server/EntitySubclassScope_t.md) | enum | — | 4 |  |
| [Explosions](server/Explosions.md) | enum | — | 3 |  |
| [ExternalAnimGraphInactiveBehavior_t](server/ExternalAnimGraphInactiveBehavior_t.md) | enum | — | 3 |  |
| [FixAngleSet_t](server/FixAngleSet_t.md) | enum | — | 3 |  |
| [Flags_t](server/Flags_t.md) | enum | — | 23 |  |
| [ForcedCrouchState_t](server/ForcedCrouchState_t.md) | enum | — | 3 |  |
| [FuncDoorSpawnPos_t](server/FuncDoorSpawnPos_t.md) | enum | — | 2 |  |
| [FuncMoverMovementSummaryFlags_t](server/FuncMoverMovementSummaryFlags_t.md) | enum | — | 9 |  |
| [FuncRotatorRotationSummaryFlags_t](server/FuncRotatorRotationSummaryFlags_t.md) | enum | — | 8 |  |
| [GCClientLauncherType](server/GCClientLauncherType.md) | enum | — | 4 |  |
| [GCConnectionStatus](server/GCConnectionStatus.md) | enum | — | 5 |  |
| [GCProtoBufMsgSrc](server/GCProtoBufMsgSrc.md) | enum | — | 5 |  |
| [GC_BannedWordType](server/GC_BannedWordType.md) | enum | — | 2 |  |
| [GLOBALESTATE](server/GLOBALESTATE.md) | enum | — | 3 |  |
| [GameAnimEventIndex_t](server/GameAnimEventIndex_t.md) | enum | — | 50 |  |
| [GrenadeType_t](server/GrenadeType_t.md) | enum | — | 6 |  |
| [HierarchyType_t](server/HierarchyType_t.md) | enum | — | 6 |  |
| [HitGroup_t](server/HitGroup_t.md) | enum | — | 14 |  |
| [HoverPoseFlags_t](server/HoverPoseFlags_t.md) | enum | — | 3 |  |
| [Hull_t](server/Hull_t.md) | enum | — | 12 |  |
| [IChoreoServices::ChoreoState_t](server/IChoreoServices.ChoreoState_t.md) | enum | — | 7 |  |
| [IChoreoServices::ScriptState_t](server/IChoreoServices.ScriptState_t.md) | enum | — | 5 |  |
| [INavObstacle::NavObstacleType_t](server/INavObstacle.NavObstacleType_t.md) | enum | — | 5 |  |
| [InputBitMask_t](server/InputBitMask_t.md) | enum | — | 21 |  |
| [ItemFlagTypes_t](server/ItemFlagTypes_t.md) | enum | — | 9 |  |
| [LatchDirtyPermission_t](server/LatchDirtyPermission_t.md) | enum | — | 6 |  |
| [LessonPanelLayoutFileTypes_t](server/LessonPanelLayoutFileTypes_t.md) | enum | — | 3 |  |
| [LifeState_t](server/LifeState_t.md) | enum | — | 6 |  |
| [Materials](server/Materials.md) | enum | — | 12 |  |
| [MedalRank_t](server/MedalRank_t.md) | enum | — | 5 |  |
| [ModifyDamageReturn_t](server/ModifyDamageReturn_t.md) | enum | — | 2 |  |
| [MoveCollide_t](server/MoveCollide_t.md) | enum | — | 6 |  |
| [MoveLinearAuthoredPos_t](server/MoveLinearAuthoredPos_t.md) | enum | — | 3 |  |
| [MoveMountingAmount_t](server/MoveMountingAmount_t.md) | enum | — | 4 |  |
| [MoveType_t](server/MoveType_t.md) | enum | — | 14 |  |
| [NET_Messages](server/NET_Messages.md) | enum | — | 13 |  |
| [NPCFollowFormation_t](server/NPCFollowFormation_t.md) | enum | — | 5 |  |
| [NavScopeFlags_t](server/NavScopeFlags_t.md) | enum | — | 4 |  |
| [NavScope_t](server/NavScope_t.md) | enum | — | 5 |  |
| [ObserverInterpState_t](server/ObserverInterpState_t.md) | enum | — | 4 |  |
| [ObserverMode_t](server/ObserverMode_t.md) | enum | — | 6 |  |
| [OnFrame](server/OnFrame.md) | enum | — | 3 |  |
| [PARTICLE_MESSAGE](server/PARTICLE_MESSAGE.md) | enum | — | 42 |  |
| [PerformanceMode_t](server/PerformanceMode_t.md) | enum | — | 2 |  |
| [PlayerConnectedState](server/PlayerConnectedState.md) | enum | — | 7 |  |
| [PointOrientConstraint_t](server/PointOrientConstraint_t.md) | enum | — | 2 |  |
| [PointOrientGoalDirectionType_t](server/PointOrientGoalDirectionType_t.md) | enum | — | 5 |  |
| [PointTemplateClientOnlyEntityBehavior_t](server/PointTemplateClientOnlyEntityBehavior_t.md) | enum | — | 2 |  |
| [PointTemplateOwnerSpawnGroupType_t](server/PointTemplateOwnerSpawnGroupType_t.md) | enum | — | 3 |  |
| [PointWorldTextJustifyHorizontal_t](server/PointWorldTextJustifyHorizontal_t.md) | enum | — | 3 |  |
| [PointWorldTextJustifyVertical_t](server/PointWorldTextJustifyVertical_t.md) | enum | — | 3 |  |
| [PointWorldTextReorientMode_t](server/PointWorldTextReorientMode_t.md) | enum | — | 2 |  |
| [PrefetchType](server/PrefetchType.md) | enum | — | 1 |  |
| [PreviewCharacterBannerAnimation](server/PreviewCharacterBannerAnimation.md) | enum | — | 30 |  |
| [PreviewCharacterMode](server/PreviewCharacterMode.md) | enum | — | 11 |  |
| [PreviewEOMCelebration](server/PreviewEOMCelebration.md) | enum | — | 24 |  |
| [PreviewWeaponState](server/PreviewWeaponState.md) | enum | — | 6 |  |
| [PropDoorRotatingOpenDirection_e](server/PropDoorRotatingOpenDirection_e.md) | enum | — | 3 |  |
| [PropDoorRotatingSpawnPos_t](server/PropDoorRotatingSpawnPos_t.md) | enum | — | 4 |  |
| [PulseCollisionGroup_t](server/PulseCollisionGroup_t.md) | enum | — | 1 |  |
| [PulseNPCCondition_t](server/PulseNPCCondition_t.md) | enum | — | 5 |  |
| [PulseTraceContents_t](server/PulseTraceContents_t.md) | enum | — | 2 |  |
| [QuestProgress::Reason](server/QuestProgress.Reason.md) | enum | — | 13 |  |
| [QuestType](server/QuestType.md) | enum | — | 2 |  |
| [RelativeLocationType_t](server/RelativeLocationType_t.md) | enum | — | 4 |  |
| [RenderFx_t](server/RenderFx_t.md) | enum | — | 18 |  |
| [RenderMode_t](server/RenderMode_t.md) | enum | — | 4 |  |
| [ReplayEventType_t](server/ReplayEventType_t.md) | enum | — | 5 |  |
| [RequestPause_t](server/RequestPause_t.md) | enum | — | 3 |  |
| [RotatorTargetSpace_t](server/RotatorTargetSpace_t.md) | enum | — | 2 |  |
| [RumbleEffect_t](server/RumbleEffect_t.md) | enum | — | 27 |  |
| [SVC_Messages](server/SVC_Messages.md) | enum | — | 31 |  |
| [SVC_Messages_LowFrequency](server/SVC_Messages_LowFrequency.md) | enum | — | 1 |  |
| [SaveRestoreTableFlags_t](server/SaveRestoreTableFlags_t.md) | enum | — | 22 |  |
| [SceneOnPlayerDeath_t](server/SceneOnPlayerDeath_t.md) | enum | — | 2 |  |
| [ScriptedConflictResponse_t](server/ScriptedConflictResponse_t.md) | enum | — | 2 |  |
| [ScriptedOnDeath_t](server/ScriptedOnDeath_t.md) | enum | — | 4 |  |
| [SequenceFinishNotifyState_t](server/SequenceFinishNotifyState_t.md) | enum | — | 3 |  |
| [ShadowType_t](server/ShadowType_t.md) | enum | — | 2 |  |
| [ShakeCommand_t](server/ShakeCommand_t.md) | enum | — | 7 |  |
| [ShardSolid_t](server/ShardSolid_t.md) | enum | — | 2 |  |
| [ShatterDamageCause](server/ShatterDamageCause.md) | enum | — | 5 |  |
| [ShatterGlassEntityPoolState_t](server/ShatterGlassEntityPoolState_t.md) | enum | — | 3 |  |
| [ShatterGlassStressType](server/ShatterGlassStressType.md) | enum | — | 4 |  |
| [SignonState_t](server/SignonState_t.md) | enum | — | 8 |  |
| [SolidType_t](server/SolidType_t.md) | enum | — | 10 |  |
| [SoundEventStartType_t](server/SoundEventStartType_t.md) | enum | — | 3 |  |
| [SpawnGroupFlags_t](server/SpawnGroupFlags_t.md) | enum | — | 8 |  |
| [StanceType_t](server/StanceType_t.md) | enum | — | 5 |  |
| [SubclassVDataChangeType_t](server/SubclassVDataChangeType_t.md) | enum | — | 3 |  |
| [SurroundingBoundsType_t](server/SurroundingBoundsType_t.md) | enum | — | 10 |  |
| [TOGGLE_STATE](server/TOGGLE_STATE.md) | enum | — | 8 |  |
| [TRAIN_CODE](server/TRAIN_CODE.md) | enum | — | 3 |  |
| [TakeDamageFlags_t](server/TakeDamageFlags_t.md) | enum | — | 22 |  |
| [TestInputOutputCombinationsEnum_t](server/TestInputOutputCombinationsEnum_t.md) | enum | — | 3 |  |
| [TimelineCompression_t](server/TimelineCompression_t.md) | enum | — | 5 |  |
| [Touch_t](server/Touch_t.md) | enum | — | 5 |  |
| [TrackOrientationType_t](server/TrackOrientationType_t.md) | enum | — | 3 |  |
| [TrainOrientationType_t](server/TrainOrientationType_t.md) | enum | — | 4 |  |
| [TrainVelocityType_t](server/TrainVelocityType_t.md) | enum | — | 3 |  |
| [ValueRemapperHapticsType_t](server/ValueRemapperHapticsType_t.md) | enum | — | 2 |  |
| [ValueRemapperInputType_t](server/ValueRemapperInputType_t.md) | enum | — | 2 |  |
| [ValueRemapperMomentumType_t](server/ValueRemapperMomentumType_t.md) | enum | — | 4 |  |
| [ValueRemapperOutputType_t](server/ValueRemapperOutputType_t.md) | enum | — | 4 |  |
| [ValueRemapperRatchetType_t](server/ValueRemapperRatchetType_t.md) | enum | — | 2 |  |
| [VoiceDataFormat_t](server/VoiceDataFormat_t.md) | enum | — | 3 |  |
| [WaterLevel_t](server/WaterLevel_t.md) | enum | — | 7 |  |
| [WeaponAttackType_t](server/WeaponAttackType_t.md) | enum | — | 4 |  |
| [WeaponGameplayAnimState](server/WeaponGameplayAnimState.md) | enum | — | 29 |  |
| [WeaponSound_t](server/WeaponSound_t.md) | enum | — | 25 |  |
| [WeaponSwitchReason_t](server/WeaponSwitchReason_t.md) | enum | — | 5 |  |
| [WorldTextPanelHorizontalAlign_t](server/WorldTextPanelHorizontalAlign_t.md) | enum | — | 3 |  |
| [WorldTextPanelOrientation_t](server/WorldTextPanelOrientation_t.md) | enum | — | 3 |  |
| [WorldTextPanelVerticalAlign_t](server/WorldTextPanelVerticalAlign_t.md) | enum | — | 3 |  |
| [attributeprovidertypes_t](server/attributeprovidertypes_t.md) | enum | — | 2 |  |
| [doorCheck_e](server/doorCheck_e.md) | enum | — | 3 |  |
| [eRollType](server/eRollType.md) | enum | — | 5 |  |
| [eSplinePushType](server/eSplinePushType.md) | enum | — | 3 |  |
| [filter_t](server/filter_t.md) | enum | — | 2 |  |
| [gear_slot_t](server/gear_slot_t.md) | enum | — | 17 |  |
| [loadout_slot_t](server/loadout_slot_t.md) | enum | — | 74 |  |
| [navproperties_t](server/navproperties_t.md) | enum | — | 1 |  |
| [soundcommands_t](server/soundcommands_t.md) | enum | — | 5 |  |
| [vote_create_failed_t](server/vote_create_failed_t.md) | enum | — | 35 |  |
