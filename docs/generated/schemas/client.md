---
layout: default
title: client
parent: Schemas
nav_exclude: true
---

# Module: client

[📊 View UML Diagram](../diagrams/client.md)

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [ActiveModelConfig_t](#activemodelconfig_t) | class |  | 4 |
| [AnimGraph2SerializedPoseRecipeSlot_t](#animgraph2serializedposerecipeslot_t) | class |  | 1 |
| [CAttributeList](#cattributelist) | class |  | 2 |
| [CAttributeManager](#cattributemanager) | class |  | 6 |
| [CAttributeManager::cached_attribute_float_t](#cattributemanagercached_attribute_float_t) | class |  | 3 |
| [CBarnLightAPI](#cbarnlightapi) | class |  | 0 |
| [CBaseAnimGraph](#cbaseanimgraph) | class | C_BaseModelEntity | 17 |
| [CBaseAnimGraphAPI](#cbaseanimgraphapi) | class |  | 0 |
| [CBaseAnimGraphAlias_baseanimating](#cbaseanimgraphalias_baseanimating) | class | CBaseAnimGraph | 0 |
| [CBaseAnimGraphController](#cbaseanimgraphcontroller) | class | CSkeletonAnimationController | 32 |
| [CBaseEntity_SharedAPI](#cbaseentity_sharedapi) | class |  | 0 |
| [CBaseFilter](#cbasefilter) | class | CLogicalEntity | 3 |
| [CBaseGrenade_API](#cbasegrenade_api) | class |  | 0 |
| [CBaseModelEntityAPI](#cbasemodelentityapi) | class |  | 0 |
| [CBasePlayerController](#cbaseplayercontroller) | class | C_BaseEntity | 17 |
| [CBasePlayerControllerAPI](#cbaseplayercontrollerapi) | class |  | 0 |
| [CBasePlayerVData](#cbaseplayervdata) | class | CEntitySubclassVDataBase | 15 |
| [CBasePlayerWeaponVData](#cbaseplayerweaponvdata) | class | CEntitySubclassVDataBase | 32 |
| [CBaseProp](#cbaseprop) | class | CBaseAnimGraph | 4 |
| [CBaseTriggerAPI](#cbasetriggerapi) | class |  | 0 |
| [CBodyComponent](#cbodycomponent) | class | CEntityComponent | 2 |
| [CBodyComponentBaseAnimGraph](#cbodycomponentbaseanimgraph) | class | CBodyComponentSkeletonInstance | 1 |
| [CBodyComponentBaseModelEntity](#cbodycomponentbasemodelentity) | class | CBodyComponentSkeletonInstance | 0 |
| [CBodyComponentPoint](#cbodycomponentpoint) | class | CBodyComponent | 1 |
| [CBodyComponentSkeletonInstance](#cbodycomponentskeletoninstance) | class | CBodyComponent | 1 |
| [CBombTarget](#cbombtarget) | class | C_BaseTrigger | 1 |
| [CBuoyancyHelper](#cbuoyancyhelper) | class |  | 11 |
| [CCS2PawnGraphController](#ccs2pawngraphcontroller) | class | CCS2WeaponGraphController | 28 |
| [CCS2UIPawnGraphController](#ccs2uipawngraphcontroller) | class | CAnimGraphControllerBase | 14 |
| [CCS2WeaponGraphController](#ccs2weapongraphcontroller) | class | CAnimGraphControllerBase | 20 |
| [CCSGO_EndOfMatchLineupEnd](#ccsgo_endofmatchlineupend) | class | C_CSGO_EndOfMatchLineupEndpoint | 0 |
| [CCSGO_TeamPreviewCharacterPosition_API](#ccsgo_teampreviewcharacterposition_api) | class |  | 0 |
| [CCSGO_WingmanIntroCharacterPosition](#ccsgo_wingmanintrocharacterposition) | class | C_CSGO_TeamIntroCharacterPosition | 0 |
| [CCSGO_WingmanIntroCounterTerroristPosition](#ccsgo_wingmanintrocounterterroristposition) | class | CCSGO_WingmanIntroCharacterPosition | 0 |
| [CCSGO_WingmanIntroTerroristPosition](#ccsgo_wingmanintroterroristposition) | class | CCSGO_WingmanIntroCharacterPosition | 0 |
| [CCSGameModeRules](#ccsgamemoderules) | class |  | 1 |
| [CCSGameModeRules_ArmsRace](#ccsgamemoderules_armsrace) | class | CCSGameModeRules | 1 |
| [CCSGameModeRules_Deathmatch](#ccsgamemoderules_deathmatch) | class | CCSGameModeRules | 3 |
| [CCSGameModeRules_Noop](#ccsgamemoderules_noop) | class | CCSGameModeRules | 0 |
| [CCSObserver_CameraServices](#ccsobserver_cameraservices) | class | CCSPlayerBase_CameraServices | 1 |
| [CCSObserver_MovementServices](#ccsobserver_movementservices) | class | CPlayer_MovementServices | 0 |
| [CCSObserver_ObserverServices](#ccsobserver_observerservices) | class | CPlayer_ObserverServices | 1 |
| [CCSObserver_UseServices](#ccsobserver_useservices) | class | CPlayer_UseServices | 0 |
| [CCSPlayerBase_CameraServices](#ccsplayerbase_cameraservices) | class | CPlayer_CameraServices | 6 |
| [CCSPlayerController](#ccsplayercontroller) | class | CBasePlayerController | 68 |
| [CCSPlayerController_API](#ccsplayercontroller_api) | class |  | 0 |
| [CCSPlayerController_ActionTrackingServices](#ccsplayercontroller_actiontrackingservices) | class | CPlayerControllerComponent | 5 |
| [CCSPlayerController_DamageServices](#ccsplayercontroller_damageservices) | class | CPlayerControllerComponent | 2 |
| [CCSPlayerController_InGameMoneyServices](#ccsplayercontroller_ingamemoneyservices) | class | CPlayerControllerComponent | 4 |
| [CCSPlayerController_InventoryServices](#ccsplayercontroller_inventoryservices) | class | CPlayerControllerComponent | 9 |
| [CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t](#ccsplayercontroller_inventoryservicesnetworkedloadoutslot_t) | class |  | 3 |
| [CCSPlayerLegacyJump](#ccsplayerlegacyjump) | class |  | 2 |
| [CCSPlayerModernJump](#ccsplayermodernjump) | class |  | 9 |
| [CCSPlayer_ActionTrackingServices](#ccsplayer_actiontrackingservices) | class | CPlayerPawnComponent | 4 |
| [CCSPlayer_AimPunchServices](#ccsplayer_aimpunchservices) | class | CPlayerPawnComponent | 6 |
| [CCSPlayer_BulletServices](#ccsplayer_bulletservices) | class | CPlayerPawnComponent | 1 |
| [CCSPlayer_BuyServices](#ccsplayer_buyservices) | class | CPlayerPawnComponent | 1 |
| [CCSPlayer_CameraServices](#ccsplayer_cameraservices) | class | CCSPlayerBase_CameraServices | 2 |
| [CCSPlayer_DamageReactServices](#ccsplayer_damagereactservices) | class | CPlayerPawnComponent | 0 |
| [CCSPlayer_GlowServices](#ccsplayer_glowservices) | class | CPlayerPawnComponent | 0 |
| [CCSPlayer_HostageServices](#ccsplayer_hostageservices) | class | CPlayerPawnComponent | 2 |
| [CCSPlayer_ItemServices](#ccsplayer_itemservices) | class | CPlayer_ItemServices | 2 |
| [CCSPlayer_MovementServices](#ccsplayer_movementservices) | class | CPlayer_MovementServices_Humanoid | 49 |
| [CCSPlayer_PingServices](#ccsplayer_pingservices) | class | CPlayerPawnComponent | 1 |
| [CCSPlayer_UseServices](#ccsplayer_useservices) | class | CPlayer_UseServices | 0 |
| [CCSPlayer_WaterServices](#ccsplayer_waterservices) | class | CPlayer_WaterServices | 3 |
| [CCSPlayer_WeaponServices](#ccsplayer_weaponservices) | class | CPlayer_WeaponServices | 5 |
| [CCSWeaponBaseVData](#ccsweaponbasevdata) | class | CBasePlayerWeaponVData | 84 |
| [CCSWeaponBase_API](#ccsweaponbase_api) | class |  | 0 |
| [CCS_PortraitWorldCallbackHandler](#ccs_portraitworldcallbackhandler) | class | C_BaseEntity | 0 |
| [CCashStack](#ccashstack) | class | C_BaseModelEntity | 1 |
| [CChoreoComponent](#cchoreocomponent) | class |  | 6 |
| [CChoreoInfoTarget](#cchoreoinfotarget) | class | C_PointEntity | 0 |
| [CCitadelSoundOpvarSetOBB](#ccitadelsoundopvarsetobb) | class | C_BaseEntity | 8 |
| [CClientAlphaProperty](#cclientalphaproperty) | class | IClientAlphaProperty | 11 |
| [CCollisionProperty](#ccollisionproperty) | class |  | 17 |
| [CDamageRecord](#cdamagerecord) | class |  | 15 |
| [CDestructiblePartsComponent](#cdestructiblepartscomponent) | class |  | 4 |
| [CEconItemAttribute](#ceconitemattribute) | class |  | 5 |
| [CEffectData](#ceffectdata) | class |  | 20 |
| [CEnvCombinedLightProbeVolumeAPI](#cenvcombinedlightprobevolumeapi) | class |  | 0 |
| [CEnvCubemapAPI](#cenvcubemapapi) | class |  | 0 |
| [CEnvLightProbeVolumeAPI](#cenvlightprobevolumeapi) | class |  | 0 |
| [CEnvSkyAPI](#cenvskyapi) | class |  | 0 |
| [CEnvSoundscape](#cenvsoundscape) | class | C_BaseEntity | 11 |
| [CEnvSoundscapeAlias_snd_soundscape](#cenvsoundscapealias_snd_soundscape) | class | CEnvSoundscape | 0 |
| [CEnvSoundscapeProxy](#cenvsoundscapeproxy) | class | CEnvSoundscape | 1 |
| [CEnvSoundscapeProxyAlias_snd_soundscape_proxy](#cenvsoundscapeproxyalias_snd_soundscape_proxy) | class | CEnvSoundscapeProxy | 0 |
| [CEnvSoundscapeTriggerable](#cenvsoundscapetriggerable) | class | CEnvSoundscape | 0 |
| [CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable](#cenvsoundscapetriggerablealias_snd_soundscape_triggerable) | class | CEnvSoundscapeTriggerable | 0 |
| [CEnvWindSharedAPI](#cenvwindsharedapi) | class |  | 0 |
| [CExplosionTypeData](#cexplosiontypedata) | class |  | 5 |
| [CFilterAttributeInt](#cfilterattributeint) | class | CBaseFilter | 1 |
| [CFilterClass](#cfilterclass) | class | CBaseFilter | 1 |
| [CFilterLOS](#cfilterlos) | class | CBaseFilter | 0 |
| [CFilterMassGreater](#cfiltermassgreater) | class | CBaseFilter | 1 |
| [CFilterModel](#cfiltermodel) | class | CBaseFilter | 1 |
| [CFilterMultiple](#cfiltermultiple) | class | CBaseFilter | 3 |
| [CFilterMultipleAPI](#cfiltermultipleapi) | class |  | 0 |
| [CFilterName](#cfiltername) | class | CBaseFilter | 1 |
| [CFilterProximity](#cfilterproximity) | class | CBaseFilter | 1 |
| [CFilterTeam](#cfilterteam) | class | CBaseFilter | 1 |
| [CFlashbangProjectile_API](#cflashbangprojectile_api) | class |  | 0 |
| [CFlashlightEffect](#cflashlighteffect) | class |  | 13 |
| [CFootstepControl_API](#cfootstepcontrol_api) | class |  | 0 |
| [CFuncRetakeBarrier](#cfuncretakebarrier) | class | C_DynamicProp | 0 |
| [CFuncWater](#cfuncwater) | class | C_BaseModelEntity | 1 |
| [CGameSceneNode](#cgamescenenode) | class |  | 34 |
| [CGameSceneNodeHandle](#cgamescenenodehandle) | class |  | 2 |
| [CGlobalLightBase](#cgloballightbase) | class |  | 43 |
| [CGlowProperty](#cglowproperty) | class |  | 11 |
| [CGrenadeTracer](#cgrenadetracer) | class | C_BaseModelEntity | 2 |
| [CGrenadeTracer_API](#cgrenadetracer_api) | class |  | 0 |
| [CHitboxComponent](#chitboxcomponent) | class | CEntityComponent | 1 |
| [CHostageRescueZone](#chostagerescuezone) | class | CHostageRescueZoneShim | 0 |
| [CHostageRescueZoneShim](#chostagerescuezoneshim) | class | C_BaseTrigger | 0 |
| [CInfoDynamicShadowHint](#cinfodynamicshadowhint) | class | C_PointEntity | 5 |
| [CInfoDynamicShadowHintBox](#cinfodynamicshadowhintbox) | class | CInfoDynamicShadowHint | 2 |
| [CInfoFan](#cinfofan) | class | C_PointEntity | 4 |
| [CInfoOffscreenPanoramaTexture](#cinfooffscreenpanoramatexture) | class | C_PointEntity | 12 |
| [CInfoParticleTarget](#cinfoparticletarget) | class | C_PointEntity | 0 |
| [CInfoTarget](#cinfotarget) | class | C_PointEntity | 0 |
| [CInfoWorldLayer](#cinfoworldlayer) | class | C_BaseEntity | 8 |
| [CInterpolatedValue](#cinterpolatedvalue) | class |  | 5 |
| [CInventoryImageData](#cinventoryimagedata) | class |  | 3 |
| [CLightComponent](#clightcomponent) | class | CEntityComponent | 70 |
| [CLightEntityAPI](#clightentityapi) | class |  | 0 |
| [CLogicRelay](#clogicrelay) | class | CLogicalEntity | 7 |
| [CLogicRelayAPI](#clogicrelayapi) | class |  | 0 |
| [CLogicalEntity](#clogicalentity) | class | C_BaseEntity | 0 |
| [CMapInfo](#cmapinfo) | class | C_PointEntity | 15 |
| [CMapInfo_API](#cmapinfo_api) | class |  | 0 |
| [CModelState](#cmodelstate) | class |  | 14 |
| [CNetworkedSequenceOperation](#cnetworkedsequenceoperation) | class |  | 8 |
| [CParticleSystemAPI](#cparticlesystemapi) | class |  | 0 |
| [CPathNode](#cpathnode) | class | C_PointEntity | 6 |
| [CPathQueryComponent](#cpathquerycomponent) | class | CEntityComponent, CPathQueryUtil | 0 |
| [CPathSimple](#cpathsimple) | class | C_BaseEntity | 3 |
| [CPathSimpleAPI](#cpathsimpleapi) | class |  | 0 |
| [CPathWithDynamicNodes](#cpathwithdynamicnodes) | class | CPathSimple | 2 |
| [CPlayerSprayDecalRenderHelper](#cplayerspraydecalrenderhelper) | class |  | 0 |
| [CPlayer_AutoaimServices](#cplayer_autoaimservices) | class | CPlayerPawnComponent | 0 |
| [CPlayer_CameraServices](#cplayer_cameraservices) | class | CPlayerPawnComponent | 20 |
| [CPlayer_FlashlightServices](#cplayer_flashlightservices) | class | CPlayerPawnComponent | 0 |
| [CPlayer_ItemServices](#cplayer_itemservices) | class | CPlayerPawnComponent | 0 |
| [CPlayer_MovementServices](#cplayer_movementservices) | class | CPlayerPawnComponent | 18 |
| [CPlayer_MovementServices_Humanoid](#cplayer_movementservices_humanoid) | class | CPlayer_MovementServices | 6 |
| [CPlayer_ObserverServices](#cplayer_observerservices) | class | CPlayerPawnComponent | 6 |
| [CPlayer_UseServices](#cplayer_useservices) | class | CPlayerPawnComponent | 0 |
| [CPlayer_WaterServices](#cplayer_waterservices) | class | CPlayerPawnComponent | 0 |
| [CPlayer_WeaponServices](#cplayer_weaponservices) | class | CPlayerPawnComponent | 4 |
| [CPointChildModifier](#cpointchildmodifier) | class | C_PointEntity | 1 |
| [CPointOffScreenIndicatorUi](#cpointoffscreenindicatorui) | class | C_PointClientUIWorldPanel | 4 |
| [CPointOrient](#cpointorient) | class | C_BaseEntity | 7 |
| [CPointTemplate](#cpointtemplate) | class | CLogicalEntity | 12 |
| [CPointTemplateAPI](#cpointtemplateapi) | class |  | 0 |
| [CPointValueRemapperAPI](#cpointvalueremapperapi) | class |  | 0 |
| [CPrecipitationVData](#cprecipitationvdata) | class | CEntitySubclassVDataBase | 11 |
| [CPropDataComponent](#cpropdatacomponent) | class | CEntityComponent | 10 |
| [CPulseCell_LerpCameraSettings](#cpulsecell_lerpcamerasettings) | class | CPulseCell_BaseLerp | 3 |
| [CPulseCell_LerpCameraSettings::CursorState_t](#cpulsecell_lerpcamerasettingscursorstate_t) | class | CPulseCell_BaseLerp::CursorState_t | 3 |
| [CPulseCell_PlaySequence](#cpulsecell_playsequence) | class | CPulseCell_BaseYieldingInflow | 3 |
| [CPulseCell_PlaySequence::CursorState_t](#cpulsecell_playsequencecursorstate_t) | class |  | 1 |
| [CPulseCell_Step_EntFire](#cpulsecell_step_entfire) | class | CPulseCell_BaseFlow | 1 |
| [CPulseGameBlackboard](#cpulsegameblackboard) | class | C_BaseEntity | 2 |
| [CRagdollManager](#cragdollmanager) | class | C_BaseEntity | 1 |
| [CRenderComponent](#crendercomponent) | class | CEntityComponent | 5 |
| [CSMatchStats_t](#csmatchstats_t) | class | CSPerRoundStats_t | 5 |
| [CSPerRoundStats_t](#csperroundstats_t) | class |  | 13 |
| [CServerOnlyModelEntity](#cserveronlymodelentity) | class | C_BaseModelEntity | 0 |
| [CSkeletonInstance](#cskeletoninstance) | class | CGameSceneNode | 7 |
| [CSkyboxReference](#cskyboxreference) | class | C_BaseEntity | 2 |
| [CSoundOpvarSetBoxEntity](#csoundopvarsetboxentity) | class | C_SoundOpvarSetPointEntity | 0 |
| [CSpriteOriented](#cspriteoriented) | class | C_Sprite | 0 |
| [CTakeDamageResultAPI](#ctakedamageresultapi) | class |  | 0 |
| [CTimeline](#ctimeline) | class | IntervalTimer | 7 |
| [CTriggerFan](#ctriggerfan) | class | C_BaseTrigger | 9 |
| [CWaterSplasher](#cwatersplasher) | class | C_BaseModelEntity | 0 |
| [C_AK47](#c_ak47) | class | C_CSWeaponBaseGun | 0 |
| [C_AttributeContainer](#c_attributecontainer) | class | CAttributeManager | 3 |
| [C_BarnLight](#c_barnlight) | class | C_BaseModelEntity | 76 |
| [C_BaseButton](#c_basebutton) | class | C_BaseToggle | 3 |
| [C_BaseCSGrenade](#c_basecsgrenade) | class | C_CSWeaponBase | 14 |
| [C_BaseCSGrenadeProjectile](#c_basecsgrenadeprojectile) | class | C_BaseGrenade | 16 |
| [C_BaseClientUIEntity](#c_baseclientuientity) | class | C_BaseModelEntity | 4 |
| [C_BaseCombatCharacter](#c_basecombatcharacter) | class | CBaseAnimGraph | 6 |
| [C_BaseCombatCharacter::WaterWakeMode_t](#c_basecombatcharacterwaterwakemode_t) | enum |  | 5 |
| [C_BaseDoor](#c_basedoor) | class | C_BaseToggle | 1 |
| [C_BaseEntity](#c_baseentity) | class | CEntityInstance | 82 |
| [C_BaseEntityAPI](#c_baseentityapi) | class |  | 0 |
| [C_BaseGrenade](#c_basegrenade) | class | CBaseAnimGraph | 12 |
| [C_BaseModelEntity](#c_basemodelentity) | class | C_BaseEntity | 44 |
| [C_BaseModelEntity::Emphasized_Phoneme](#c_basemodelentityemphasized_phoneme) | class |  | 5 |
| [C_BasePlayerPawn](#c_baseplayerpawn) | class | C_BaseCombatCharacter | 28 |
| [C_BasePlayerWeapon](#c_baseplayerweapon) | class | C_EconEntity | 7 |
| [C_BasePropDoor](#c_basepropdoor) | class | C_DynamicProp | 8 |
| [C_BaseToggle](#c_basetoggle) | class | C_BaseModelEntity | 0 |
| [C_BaseTrigger](#c_basetrigger) | class | C_BaseToggle | 12 |
| [C_Beam](#c_beam) | class | C_BaseModelEntity | 23 |
| [C_Breakable](#c_breakable) | class | C_BaseModelEntity | 0 |
| [C_BreakableProp](#c_breakableprop) | class | CBaseProp | 29 |
| [C_BulletHitModel](#c_bullethitmodel) | class | CBaseAnimGraph | 6 |
| [C_C4](#c_c4) | class | C_CSWeaponBase | 10 |
| [C_CS2HudModelAddon](#c_cs2hudmodeladdon) | class | C_LateUpdatedAnimating | 0 |
| [C_CS2HudModelArms](#c_cs2hudmodelarms) | class | C_CS2HudModelBase | 0 |
| [C_CS2HudModelBase](#c_cs2hudmodelbase) | class | C_LateUpdatedAnimating | 0 |
| [C_CS2HudModelWeapon](#c_cs2hudmodelweapon) | class | C_CS2HudModelBase | 0 |
| [C_CS2WeaponModuleBase](#c_cs2weaponmodulebase) | class | CBaseAnimGraph | 0 |
| [C_CSGO_CounterTerroristTeamIntroCamera](#c_csgo_counterterroristteamintrocamera) | class | C_CSGO_TeamPreviewCamera | 0 |
| [C_CSGO_CounterTerroristWingmanIntroCamera](#c_csgo_counterterroristwingmanintrocamera) | class | C_CSGO_TeamPreviewCamera | 0 |
| [C_CSGO_EndOfMatchCamera](#c_csgo_endofmatchcamera) | class | C_CSGO_TeamPreviewCamera | 0 |
| [C_CSGO_EndOfMatchCharacterPosition](#c_csgo_endofmatchcharacterposition) | class | C_CSGO_TeamPreviewCharacterPosition | 0 |
| [C_CSGO_EndOfMatchLineupEndpoint](#c_csgo_endofmatchlineupendpoint) | class | C_BaseEntity | 0 |
| [C_CSGO_EndOfMatchLineupStart](#c_csgo_endofmatchlineupstart) | class | C_CSGO_EndOfMatchLineupEndpoint | 0 |
| [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath) | class | C_BaseEntity | 14 |
| [C_CSGO_MapPreviewCameraPathNode](#c_csgo_mappreviewcamerapathnode) | class | C_BaseEntity | 10 |
| [C_CSGO_MapPreviewCameraPathNode_API](#c_csgo_mappreviewcamerapathnode_api) | class |  | 0 |
| [C_CSGO_MapPreviewCameraPath_API](#c_csgo_mappreviewcamerapath_api) | class |  | 0 |
| [C_CSGO_PreviewModel](#c_csgo_previewmodel) | class | CBaseAnimGraph | 4 |
| [C_CSGO_PreviewModelAlias_csgo_item_previewmodel](#c_csgo_previewmodelalias_csgo_item_previewmodel) | class | C_CSGO_PreviewModel | 0 |
| [C_CSGO_PreviewModel_API](#c_csgo_previewmodel_api) | class |  | 0 |
| [C_CSGO_PreviewPlayer](#c_csgo_previewplayer) | class | C_CSPlayerPawn | 2 |
| [C_CSGO_PreviewPlayerAlias_csgo_player_previewmodel](#c_csgo_previewplayeralias_csgo_player_previewmodel) | class | C_CSGO_PreviewPlayer | 0 |
| [C_CSGO_PreviewPlayer_API](#c_csgo_previewplayer_api) | class |  | 0 |
| [C_CSGO_TeamIntroCharacterPosition](#c_csgo_teamintrocharacterposition) | class | C_CSGO_TeamPreviewCharacterPosition | 0 |
| [C_CSGO_TeamIntroCounterTerroristPosition](#c_csgo_teamintrocounterterroristposition) | class | C_CSGO_TeamIntroCharacterPosition | 0 |
| [C_CSGO_TeamIntroTerroristPosition](#c_csgo_teamintroterroristposition) | class | C_CSGO_TeamIntroCharacterPosition | 0 |
| [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera) | class | C_CSGO_MapPreviewCameraPath | 1 |
| [C_CSGO_TeamPreviewCamera_API](#c_csgo_teampreviewcamera_api) | class |  | 0 |
| [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition) | class | C_BaseEntity | 8 |
| [C_CSGO_TeamPreviewModel](#c_csgo_teampreviewmodel) | class | C_CSGO_PreviewPlayer | 0 |
| [C_CSGO_TeamSelectCamera](#c_csgo_teamselectcamera) | class | C_CSGO_TeamPreviewCamera | 0 |
| [C_CSGO_TeamSelectCharacterPosition](#c_csgo_teamselectcharacterposition) | class | C_CSGO_TeamPreviewCharacterPosition | 0 |
| [C_CSGO_TeamSelectCounterTerroristPosition](#c_csgo_teamselectcounterterroristposition) | class | C_CSGO_TeamSelectCharacterPosition | 0 |
| [C_CSGO_TeamSelectTerroristPosition](#c_csgo_teamselectterroristposition) | class | C_CSGO_TeamSelectCharacterPosition | 0 |
| [C_CSGO_TerroristTeamIntroCamera](#c_csgo_terroristteamintrocamera) | class | C_CSGO_TeamPreviewCamera | 0 |
| [C_CSGO_TerroristWingmanIntroCamera](#c_csgo_terroristwingmanintrocamera) | class | C_CSGO_TeamPreviewCamera | 0 |
| [C_CSGameRules](#c_csgamerules) | class | C_TeamplayRules | 98 |
| [C_CSGameRulesProxy](#c_csgamerulesproxy) | class | C_GameRulesProxy | 1 |
| [C_CSMinimapBoundary](#c_csminimapboundary) | class | C_BaseEntity | 0 |
| [C_CSObserverPawn](#c_csobserverpawn) | class | C_CSPlayerPawnBase | 1 |
| [C_CSObserverPawn_API](#c_csobserverpawn_api) | class |  | 0 |
| [C_CSPetPlacement](#c_cspetplacement) | class | C_BaseEntity | 0 |
| [C_CSPlayerPawn](#c_csplayerpawn) | class | C_CSPlayerPawnBase | 101 |
| [C_CSPlayerPawnBase](#c_csplayerpawnbase) | class | C_BasePlayerPawn | 26 |
| [C_CSPlayerPawnBase_API](#c_csplayerpawnbase_api) | class |  | 0 |
| [C_CSPlayerPawn_API](#c_csplayerpawn_api) | class |  | 0 |
| [C_CSPlayerResource](#c_csplayerresource) | class | C_BaseEntity | 10 |
| [C_CSTeam](#c_csteam) | class | C_Team | 10 |
| [C_CSWeaponBase](#c_csweaponbase) | class | C_BasePlayerWeapon | 54 |
| [C_CSWeaponBaseGun](#c_csweaponbasegun) | class | C_CSWeaponBase | 7 |
| [C_CSWeaponBaseShotgun](#c_csweaponbaseshotgun) | class | C_CSWeaponBase | 0 |
| [C_Chicken](#c_chicken) | class | C_DynamicProp, IHasAttributes | 5 |
| [C_ClientRagdoll](#c_clientragdoll) | class | CBaseAnimGraph | 14 |
| [C_ColorCorrection](#c_colorcorrection) | class | C_BaseEntity | 18 |
| [C_ColorCorrectionVolume](#c_colorcorrectionvolume) | class | C_BaseTrigger | 9 |
| [C_CommandContext](#c_commandcontext) | class |  | 2 |
| [C_CsmFovOverride](#c_csmfovoverride) | class | C_BaseEntity | 2 |
| [C_CsmFovOverride_API](#c_csmfovoverride_api) | class |  | 0 |
| [C_DEagle](#c_deagle) | class | C_CSWeaponBaseGun | 0 |
| [C_DecoyGrenade](#c_decoygrenade) | class | C_BaseCSGrenade | 0 |
| [C_DecoyProjectile](#c_decoyprojectile) | class | C_BaseCSGrenadeProjectile | 3 |
| [C_DynamicLight](#c_dynamiclight) | class | C_BaseModelEntity | 7 |
| [C_DynamicProp](#c_dynamicprop) | class | C_BreakableProp | 24 |
| [C_DynamicPropAlias_cable_dynamic](#c_dynamicpropalias_cable_dynamic) | class | C_DynamicProp | 0 |
| [C_DynamicPropAlias_dynamic_prop](#c_dynamicpropalias_dynamic_prop) | class | C_DynamicProp | 0 |
| [C_DynamicPropAlias_prop_dynamic_override](#c_dynamicpropalias_prop_dynamic_override) | class | C_DynamicProp | 0 |
| [C_EconEntity](#c_econentity) | class | CBaseAnimGraph, IHasAttributes | 20 |
| [C_EconEntity::AttachedModelData_t](#c_econentityattachedmodeldata_t) | class |  | 1 |
| [C_EconItemView](#c_econitemview) | class | IEconItemInterface | 29 |
| [C_EconWearable](#c_econwearable) | class | C_EconEntity | 2 |
| [C_EntityDissolve](#c_entitydissolve) | class | C_BaseModelEntity | 13 |
| [C_EntityFlame](#c_entityflame) | class | C_BaseEntity | 3 |
| [C_EnvCombinedLightProbeVolume](#c_envcombinedlightprobevolume) | class | C_BaseEntity | 29 |
| [C_EnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume](#c_envcombinedlightprobevolumealias_func_combined_light_probe_volume) | class | C_EnvCombinedLightProbeVolume | 0 |
| [C_EnvCubemap](#c_envcubemap) | class | C_BaseEntity | 18 |
| [C_EnvCubemapBox](#c_envcubemapbox) | class | C_EnvCubemap | 0 |
| [C_EnvCubemapFog](#c_envcubemapfog) | class | C_BaseEntity | 24 |
| [C_EnvDecal](#c_envdecal) | class | C_BaseModelEntity | 9 |
| [C_EnvDetailController](#c_envdetailcontroller) | class | C_BaseEntity | 2 |
| [C_EnvLightProbeVolume](#c_envlightprobevolume) | class | C_BaseEntity | 22 |
| [C_EnvParticleGlow](#c_envparticleglow) | class | C_ParticleSystem | 5 |
| [C_EnvSky](#c_envsky) | class | C_BaseModelEntity | 12 |
| [C_EnvVolumetricFogController](#c_envvolumetricfogcontroller) | class | C_BaseEntity | 36 |
| [C_EnvVolumetricFogVolume](#c_envvolumetricfogvolume) | class | C_BaseEntity | 18 |
| [C_EnvWind](#c_envwind) | class | C_BaseEntity | 1 |
| [C_EnvWindClientside](#c_envwindclientside) | class | C_BaseEntity | 1 |
| [C_EnvWindController](#c_envwindcontroller) | class | C_BaseEntity | 11 |
| [C_EnvWindShared](#c_envwindshared) | class |  | 15 |
| [C_EnvWindVolume](#c_envwindvolume) | class | C_BaseEntity | 9 |
| [C_FireCrackerBlast](#c_firecrackerblast) | class | C_Inferno | 0 |
| [C_Fish](#c_fish) | class | CBaseAnimGraph | 23 |
| [C_Flashbang](#c_flashbang) | class | C_BaseCSGrenade | 0 |
| [C_FlashbangProjectile](#c_flashbangprojectile) | class | C_BaseCSGrenadeProjectile | 0 |
| [C_FogController](#c_fogcontroller) | class | C_BaseEntity | 3 |
| [C_FootstepControl](#c_footstepcontrol) | class | C_BaseTrigger | 2 |
| [C_FuncBrush](#c_funcbrush) | class | C_BaseModelEntity | 0 |
| [C_FuncConveyor](#c_funcconveyor) | class | C_BaseModelEntity | 8 |
| [C_FuncElectrifiedVolume](#c_funcelectrifiedvolume) | class | C_FuncBrush | 3 |
| [C_FuncLadder](#c_funcladder) | class | C_BaseModelEntity | 9 |
| [C_FuncMonitor](#c_funcmonitor) | class | C_FuncBrush | 8 |
| [C_FuncMoveLinear](#c_funcmovelinear) | class | C_BaseToggle | 0 |
| [C_FuncMover](#c_funcmover) | class | C_BaseToggle | 0 |
| [C_FuncRotating](#c_funcrotating) | class | C_BaseModelEntity | 0 |
| [C_FuncTrackTrain](#c_functracktrain) | class | C_BaseModelEntity | 3 |
| [C_GameRules](#c_gamerules) | class |  | 4 |
| [C_GameRulesProxy](#c_gamerulesproxy) | class | C_BaseEntity | 0 |
| [C_GlobalLight](#c_globallight) | class | C_BaseEntity, CGlobalLightBase | 1 |
| [C_GradientFog](#c_gradientfog) | class | C_BaseEntity | 16 |
| [C_HEGrenade](#c_hegrenade) | class | C_BaseCSGrenade | 0 |
| [C_HEGrenadeProjectile](#c_hegrenadeprojectile) | class | C_BaseCSGrenadeProjectile | 0 |
| [C_HandleTest](#c_handletest) | class | C_BaseEntity | 2 |
| [C_Hostage](#c_hostage) | class | C_BaseCombatCharacter | 23 |
| [C_HostageCarriableProp](#c_hostagecarriableprop) | class | CBaseAnimGraph | 0 |
| [C_IncendiaryGrenade](#c_incendiarygrenade) | class | C_MolotovGrenade | 0 |
| [C_Inferno](#c_inferno) | class | C_BaseModelEntity | 24 |
| [C_InfoInstructorHintHostageRescueZone](#c_infoinstructorhinthostagerescuezone) | class | C_PointEntity | 0 |
| [C_InfoLadderDismount](#c_infoladderdismount) | class | C_BaseEntity | 0 |
| [C_InfoVisibilityBox](#c_infovisibilitybox) | class | C_BaseEntity | 3 |
| [C_IronSightController](#c_ironsightcontroller) | class |  | 13 |
| [C_Item](#c_item) | class | C_EconEntity | 1 |
| [C_ItemDogtags](#c_itemdogtags) | class | C_Item | 2 |
| [C_Item_Healthshot](#c_item_healthshot) | class | C_WeaponBaseItem | 0 |
| [C_KeychainModule](#c_keychainmodule) | class | C_CS2WeaponModuleBase | 2 |
| [C_Knife](#c_knife) | class | C_CSWeaponBase | 1 |
| [C_LateUpdatedAnimating](#c_lateupdatedanimating) | class | CBaseAnimGraph | 0 |
| [C_LightDirectionalEntity](#c_lightdirectionalentity) | class | C_LightEntity | 0 |
| [C_LightEntity](#c_lightentity) | class | C_BaseModelEntity | 1 |
| [C_LightEnvironmentEntity](#c_lightenvironmententity) | class | C_LightDirectionalEntity | 0 |
| [C_LightOrthoEntity](#c_lightorthoentity) | class | C_LightEntity | 0 |
| [C_LightSpotEntity](#c_lightspotentity) | class | C_LightEntity | 0 |
| [C_LocalTempEntity](#c_localtempentity) | class | CBaseAnimGraph | 25 |
| [C_MapPreviewParticleSystem](#c_mappreviewparticlesystem) | class | C_ParticleSystem | 0 |
| [C_MapVetoPickController](#c_mapvetopickcontroller) | class | C_BaseEntity | 17 |
| [C_ModelPointEntity](#c_modelpointentity) | class | C_BaseModelEntity | 0 |
| [C_MolotovGrenade](#c_molotovgrenade) | class | C_BaseCSGrenade | 0 |
| [C_MolotovProjectile](#c_molotovprojectile) | class | C_BaseCSGrenadeProjectile | 1 |
| [C_Multimeter](#c_multimeter) | class | CBaseAnimGraph | 1 |
| [C_MultiplayRules](#c_multiplayrules) | class | C_GameRules | 0 |
| [C_NametagModule](#c_nametagmodule) | class | C_CS2WeaponModuleBase | 1 |
| [C_NetTestBaseCombatCharacter](#c_nettestbasecombatcharacter) | class | C_BaseCombatCharacter | 0 |
| [C_OmniLight](#c_omnilight) | class | C_BarnLight | 3 |
| [C_ParticleSystem](#c_particlesystem) | class | C_BaseModelEntity | 26 |
| [C_PathParticleRope](#c_pathparticlerope) | class | C_BaseEntity | 16 |
| [C_PathParticleRopeAlias_path_particle_rope_clientside](#c_pathparticleropealias_path_particle_rope_clientside) | class | C_PathParticleRope | 0 |
| [C_PhysBox](#c_physbox) | class | C_Breakable | 0 |
| [C_PhysMagnet](#c_physmagnet) | class | CBaseAnimGraph | 2 |
| [C_PhysPropClientside](#c_physpropclientside) | class | C_BreakableProp | 5 |
| [C_PhysicsProp](#c_physicsprop) | class | C_BreakableProp | 1 |
| [C_PhysicsPropMultiplayer](#c_physicspropmultiplayer) | class | C_PhysicsProp | 0 |
| [C_PlantedC4](#c_plantedc4) | class | CBaseAnimGraph, IHasAttributes | 29 |
| [C_PlayerPing](#c_playerping) | class | C_BaseEntity | 5 |
| [C_PlayerSprayDecal](#c_playerspraydecal) | class | C_ModelPointEntity | 16 |
| [C_PlayerVisibility](#c_playervisibility) | class | C_BaseEntity | 6 |
| [C_PointCamera](#c_pointcamera) | class | C_BaseEntity | 26 |
| [C_PointCameraVFOV](#c_pointcameravfov) | class | C_PointCamera | 1 |
| [C_PointClientUIDialog](#c_pointclientuidialog) | class | C_BaseClientUIEntity | 2 |
| [C_PointClientUIHUD](#c_pointclientuihud) | class | C_BaseClientUIEntity | 13 |
| [C_PointClientUIWorldPanel](#c_pointclientuiworldpanel) | class | C_BaseClientUIEntity | 30 |
| [C_PointClientUIWorldTextPanel](#c_pointclientuiworldtextpanel) | class | C_PointClientUIWorldPanel | 1 |
| [C_PointCommentaryNode](#c_pointcommentarynode) | class | CBaseAnimGraph | 14 |
| [C_PointEntity](#c_pointentity) | class | C_BaseEntity | 0 |
| [C_PointValueRemapper](#c_pointvalueremapper) | class | C_BaseEntity | 25 |
| [C_PointWorldText](#c_pointworldtext) | class | C_ModelPointEntity | 19 |
| [C_PortraitWorldCallbackHandler](#c_portraitworldcallbackhandler) | class | C_BaseEntity | 0 |
| [C_PostProcessingVolume](#c_postprocessingvolume) | class | C_BaseTrigger | 12 |
| [C_Precipitation](#c_precipitation) | class | C_BaseTrigger | 8 |
| [C_PrecipitationBlocker](#c_precipitationblocker) | class | C_BaseModelEntity | 0 |
| [C_PropDoorRotating](#c_propdoorrotating) | class | C_BasePropDoor | 0 |
| [C_RagdollProp](#c_ragdollprop) | class | CBaseAnimGraph | 9 |
| [C_RagdollPropAttached](#c_ragdollpropattached) | class | C_RagdollProp | 7 |
| [C_RectLight](#c_rectlight) | class | C_BarnLight | 1 |
| [C_RetakeGameRules](#c_retakegamerules) | class |  | 6 |
| [C_RopeKeyframe](#c_ropekeyframe) | class | C_BaseModelEntity | 40 |
| [C_RopeKeyframe::CPhysicsDelegate](#c_ropekeyframecphysicsdelegate) | class |  | 1 |
| [C_SceneEntity](#c_sceneentity) | class | C_PointEntity | 13 |
| [C_SceneEntity::QueuedEvents_t](#c_sceneentityqueuedevents_t) | class |  | 1 |
| [C_ShatterGlassShardPhysics](#c_shatterglassshardphysics) | class | C_BaseModelEntity | 1 |
| [C_SingleplayRules](#c_singleplayrules) | class | C_GameRules | 0 |
| [C_SkyCamera](#c_skycamera) | class | C_BaseEntity | 4 |
| [C_SmokeGrenade](#c_smokegrenade) | class | C_BaseCSGrenade | 0 |
| [C_SmokeGrenadeProjectile](#c_smokegrenadeprojectile) | class | C_BaseCSGrenadeProjectile | 10 |
| [C_SoundAreaEntityBase](#c_soundareaentitybase) | class | C_BaseEntity | 4 |
| [C_SoundAreaEntityOrientedBox](#c_soundareaentityorientedbox) | class | C_SoundAreaEntityBase | 2 |
| [C_SoundAreaEntitySphere](#c_soundareaentitysphere) | class | C_SoundAreaEntityBase | 1 |
| [C_SoundEventAABBEntity](#c_soundeventaabbentity) | class | C_SoundEventEntity | 2 |
| [C_SoundEventConeEntity](#c_soundeventconeentity) | class | C_SoundEventEntity | 5 |
| [C_SoundEventEntity](#c_soundevententity) | class | C_BaseEntity | 15 |
| [C_SoundEventEntityAlias_snd_event_point](#c_soundevententityalias_snd_event_point) | class | C_SoundEventEntity | 0 |
| [C_SoundEventOBBEntity](#c_soundeventobbentity) | class | C_SoundEventEntity | 2 |
| [C_SoundEventPathCornerEntity](#c_soundeventpathcornerentity) | class | C_SoundEventEntity | 1 |
| [C_SoundEventSphereEntity](#c_soundeventsphereentity) | class | C_SoundEventEntity | 1 |
| [C_SoundOpvarSetAABBEntity](#c_soundopvarsetaabbentity) | class | CSoundOpvarSetBoxEntity | 0 |
| [C_SoundOpvarSetAutoRoomEntity](#c_soundopvarsetautoroomentity) | class | C_SoundOpvarSetPointEntity | 0 |
| [C_SoundOpvarSetOBBEntity](#c_soundopvarsetobbentity) | class | C_SoundOpvarSetAABBEntity | 0 |
| [C_SoundOpvarSetOBBWindEntity](#c_soundopvarsetobbwindentity) | class | C_SoundOpvarSetPointBase | 0 |
| [C_SoundOpvarSetPathCornerEntity](#c_soundopvarsetpathcornerentity) | class | C_SoundOpvarSetPointEntity | 0 |
| [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase) | class | C_BaseEntity | 6 |
| [C_SoundOpvarSetPointEntity](#c_soundopvarsetpointentity) | class | C_SoundOpvarSetPointBase | 0 |
| [C_SpotlightEnd](#c_spotlightend) | class | C_BaseModelEntity | 2 |
| [C_Sprite](#c_sprite) | class | C_BaseModelEntity | 24 |
| [C_StattrakModule](#c_stattrakmodule) | class | C_CS2WeaponModuleBase | 1 |
| [C_Team](#c_team) | class | C_BaseEntity | 4 |
| [C_TeamplayRules](#c_teamplayrules) | class | C_MultiplayRules | 0 |
| [C_TextureBasedAnimatable](#c_texturebasedanimatable) | class | C_BaseModelEntity | 8 |
| [C_TintController](#c_tintcontroller) | class | C_BaseEntity | 0 |
| [C_TonemapController2](#c_tonemapcontroller2) | class | C_BaseEntity | 5 |
| [C_TonemapController2Alias_env_tonemap_controller2](#c_tonemapcontroller2alias_env_tonemap_controller2) | class | C_TonemapController2 | 0 |
| [C_TriggerBuoyancy](#c_triggerbuoyancy) | class | C_BaseTrigger | 2 |
| [C_TriggerLerpObject](#c_triggerlerpobject) | class | C_BaseTrigger | 0 |
| [C_TriggerMultiple](#c_triggermultiple) | class | C_BaseTrigger | 0 |
| [C_TriggerPhysics](#c_triggerphysics) | class | C_BaseTrigger | 13 |
| [C_TriggerVolume](#c_triggervolume) | class | C_BaseModelEntity | 0 |
| [C_VoteController](#c_votecontroller) | class | C_BaseEntity | 7 |
| [C_WaterBullet](#c_waterbullet) | class | CBaseAnimGraph | 0 |
| [C_WeaponAWP](#c_weaponawp) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponAug](#c_weaponaug) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponBaseItem](#c_weaponbaseitem) | class | C_CSWeaponBase | 2 |
| [C_WeaponBizon](#c_weaponbizon) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponCZ75a](#c_weaponcz75a) | class | C_CSWeaponBaseGun | 1 |
| [C_WeaponElite](#c_weaponelite) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponFamas](#c_weaponfamas) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponFiveSeven](#c_weaponfiveseven) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponG3SG1](#c_weapong3sg1) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponGalilAR](#c_weapongalilar) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponGlock](#c_weaponglock) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponHKP2000](#c_weaponhkp2000) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponM249](#c_weaponm249) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponM4A1](#c_weaponm4a1) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponM4A1Silencer](#c_weaponm4a1silencer) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponMAC10](#c_weaponmac10) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponMP5SD](#c_weaponmp5sd) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponMP7](#c_weaponmp7) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponMP9](#c_weaponmp9) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponMag7](#c_weaponmag7) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponNOVA](#c_weaponnova) | class | C_CSWeaponBaseShotgun | 0 |
| [C_WeaponNegev](#c_weaponnegev) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponP250](#c_weaponp250) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponP90](#c_weaponp90) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponRevolver](#c_weaponrevolver) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponSCAR20](#c_weaponscar20) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponSG556](#c_weaponsg556) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponSSG08](#c_weaponssg08) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponSawedoff](#c_weaponsawedoff) | class | C_CSWeaponBaseShotgun | 0 |
| [C_WeaponTaser](#c_weapontaser) | class | C_CSWeaponBaseGun | 2 |
| [C_WeaponTec9](#c_weapontec9) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponUMP45](#c_weaponump45) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponUSPSilencer](#c_weaponuspsilencer) | class | C_CSWeaponBaseGun | 0 |
| [C_WeaponXM1014](#c_weaponxm1014) | class | C_CSWeaponBaseShotgun | 0 |
| [C_World](#c_world) | class | C_BaseModelEntity | 0 |
| [C_WorldModelGloves](#c_worldmodelgloves) | class | CBaseAnimGraph | 0 |
| [C_fogplayerparams_t](#c_fogplayerparams_t) | class |  | 14 |
| [CountdownTimer](#countdowntimer) | class |  | 4 |
| [DestructiblePartDamageRequestAPI](#destructiblepartdamagerequestapi) | class |  | 0 |
| [EngineCountdownTimer](#enginecountdowntimer) | class |  | 3 |
| [EntityRenderAttribute_t](#entityrenderattribute_t) | class |  | 2 |
| [EntitySpottedState_t](#entityspottedstate_t) | class |  | 2 |
| [FilterDamageType](#filterdamagetype) | class | CBaseFilter | 1 |
| [FilterHealth](#filterhealth) | class | CBaseFilter | 3 |
| [IClientAlphaProperty](#iclientalphaproperty) | class |  | 0 |
| [IntervalTimer](#intervaltimer) | class |  | 2 |
| [PhysicsRagdollPose_t](#physicsragdollpose_t) | class |  | 3 |
| [SellbackPurchaseEntry_t](#sellbackpurchaseentry_t) | class |  | 5 |
| [SequenceHistory_t](#sequencehistory_t) | class |  | 6 |
| [ServerAuthoritativeWeaponSlot_t](#serverauthoritativeweaponslot_t) | class |  | 3 |
| [TimedEvent](#timedevent) | class |  | 2 |
| [VPhysicsCollisionAttribute_t](#vphysicscollisionattribute_t) | class |  | 11 |
| [ViewAngleServerChange_t](#viewangleserverchange_t) | class |  | 3 |
| [WeaponPurchaseCount_t](#weaponpurchasecount_t) | class |  | 2 |
| [WeaponPurchaseTracker_t](#weaponpurchasetracker_t) | class |  | 1 |
| [audioparams_t](#audioparams_t) | class |  | 5 |
| [fogparams_t](#fogparams_t) | class |  | 25 |
| [inv_image_camera_t](#inv_image_camera_t) | class |  | 7 |
| [inv_image_clearcolor_t](#inv_image_clearcolor_t) | class |  | 1 |
| [inv_image_data_t](#inv_image_data_t) | class |  | 8 |
| [inv_image_item_t](#inv_image_item_t) | class |  | 3 |
| [inv_image_light_barn_t](#inv_image_light_barn_t) | class |  | 4 |
| [inv_image_light_fill_t](#inv_image_light_fill_t) | class |  | 3 |
| [inv_image_light_sun_t](#inv_image_light_sun_t) | class |  | 3 |
| [inv_image_map_t](#inv_image_map_t) | class |  | 2 |
| [screenfade_t](#screenfade_t) | class |  | 5 |
| [screenshake_t](#screenshake_t) | class |  | 9 |
| [shard_model_desc_t](#shard_model_desc_t) | class |  | 13 |
| [sky3dparams_t](#sky3dparams_t) | class |  | 6 |

---

### ActiveModelConfig_t

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "ActiveModelConfig_t",
	"m_Handle": 0,
	"m_Name": "",
	"m_AssociatedEntities":
	[
	],
	"m_AssociatedEntityNames":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    ActiveModelConfig_t *-- ModelConfigHandle_t
    ActiveModelConfig_t --> C_BaseModelEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Handle` | [ModelConfigHandle_t](../schemas/server.md#modelconfighandle_t) |  |
| `m_Name` | CUtlSymbolLarge |  |
| `m_AssociatedEntities` | C_NetworkUtlVectorBase< CHandle< [C_BaseModelEntity](../schemas/client.md#c_basemodelentity) > > |  |
| `m_AssociatedEntityNames` | C_NetworkUtlVectorBase< CUtlSymbolLarge > |  |

### AnimGraph2SerializedPoseRecipeSlot_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_topology` | CUtlBinaryBlock | `MNotSaved` |

### CAttributeList

**Relationships:**

```mermaid
classDiagram
    CAttributeList *-- CEconItemAttribute
    CAttributeList --> CAttributeManager
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Attributes` | C_UtlVectorEmbeddedNetworkVar< [CEconItemAttribute](../schemas/client.md#ceconitemattribute) > |  |
| `m_pManager` | [CAttributeManager](../schemas/client.md#cattributemanager)* |  |

### CAttributeManager

**Derived by:** [CAttributeContainer](server.md#cattributecontainer), [C_AttributeContainer](client.md#c_attributecontainer)

**Relationships:**

```mermaid
classDiagram
    CAttributeManager <|-- C_AttributeContainer
    CAttributeManager <|-- CAttributeContainer
    CAttributeManager --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Providers` | CUtlVector< CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > > |  |
| `m_iReapplyProvisionParity` | int32 |  |
| `m_hOuter` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_bPreventLoopback` | bool |  |
| `m_ProviderType` | attributeprovidertypes_t |  |
| `m_CachedResults` | CUtlVector< [CAttributeManager](../schemas/client.md#cattributemanager)::cached_attribute_float_t > |  |

### CAttributeManager::cached_attribute_float_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `flIn` | float32 |  |
| `iAttribHook` | CUtlSymbolLarge |  |
| `flOut` | float32 |  |

### CBarnLightAPI

### CBaseAnimGraph

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Derived by:** [CBaseAnimGraphAlias_baseanimating](client.md#cbaseanimgraphalias_baseanimating), [CBaseCombatCharacter](server.md#cbasecombatcharacter), [CBaseGrenade](server.md#cbasegrenade), [CBaseProp](client.md#cbaseprop), [CConstraintAnchor](server.md#cconstraintanchor), [CEconEntity](server.md#ceconentity), [CFish](server.md#cfish), [CHostageCarriableProp](server.md#chostagecarriableprop), [CItem](server.md#citem), [CItemSoda](server.md#citemsoda), [CPhysMagnet](server.md#cphysmagnet), [CPlantedC4](server.md#cplantedc4), [CPointCommentaryNode](server.md#cpointcommentarynode), [CRagdollProp](server.md#cragdollprop), [CWaterBullet](server.md#cwaterbullet), [C_BaseCombatCharacter](client.md#c_basecombatcharacter), [C_BaseGrenade](client.md#c_basegrenade), [C_BulletHitModel](client.md#c_bullethitmodel), [C_CS2WeaponModuleBase](client.md#c_cs2weaponmodulebase), [C_CSGO_PreviewModel](client.md#c_csgo_previewmodel), [C_ClientRagdoll](client.md#c_clientragdoll), [C_EconEntity](client.md#c_econentity), [C_Fish](client.md#c_fish), [C_HostageCarriableProp](client.md#c_hostagecarriableprop), [C_LateUpdatedAnimating](client.md#c_lateupdatedanimating), [C_LocalTempEntity](client.md#c_localtempentity), [C_Multimeter](client.md#c_multimeter), [C_PhysMagnet](client.md#c_physmagnet), [C_PlantedC4](client.md#c_plantedc4), [C_PointCommentaryNode](client.md#c_pointcommentarynode), [C_RagdollProp](client.md#c_ragdollprop), [C_WaterBullet](client.md#c_waterbullet), [C_WorldModelGloves](client.md#c_worldmodelgloves)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    CBaseAnimGraph <|-- CBaseAnimGraphAlias_baseanimating
    CBaseAnimGraph <|-- CBaseProp
    CBaseAnimGraph <|-- C_BaseCombatCharacter
    CBaseAnimGraph <|-- C_BaseGrenade
    CBaseAnimGraph <|-- C_BulletHitModel
    CBaseAnimGraph <|-- C_CS2WeaponModuleBase
    CBaseAnimGraph <|-- C_CSGO_PreviewModel
    CBaseAnimGraph <|-- C_ClientRagdoll
    CBaseAnimGraph <|-- C_EconEntity
    CBaseAnimGraph <|-- C_Fish
    CBaseAnimGraph <|-- C_HostageCarriableProp
    CBaseAnimGraph <|-- C_LateUpdatedAnimating
    CBaseAnimGraph <|-- C_LocalTempEntity
    CBaseAnimGraph <|-- C_Multimeter
    CBaseAnimGraph <|-- C_PhysMagnet
    CBaseAnimGraph <|-- C_PlantedC4
    CBaseAnimGraph <|-- C_PointCommentaryNode
    CBaseAnimGraph <|-- C_RagdollProp
    CBaseAnimGraph <|-- C_WaterBullet
    CBaseAnimGraph <|-- C_WorldModelGloves
    CBaseAnimGraph <|-- CBaseCombatCharacter
    CBaseAnimGraph <|-- CBaseGrenade
    CBaseAnimGraph <|-- CConstraintAnchor
    CBaseAnimGraph <|-- CEconEntity
    CBaseAnimGraph <|-- CFish
    CBaseAnimGraph <|-- CHostageCarriableProp
    CBaseAnimGraph <|-- CItem
    CBaseAnimGraph <|-- CItemSoda
    CBaseAnimGraph <|-- CPhysMagnet
    CBaseAnimGraph <|-- CPlantedC4
    CBaseAnimGraph <|-- CPointCommentaryNode
    CBaseAnimGraph <|-- CRagdollProp
    CBaseAnimGraph <|-- CWaterBullet
    CBaseAnimGraph *-- CAnimGraphControllerManager
    CBaseAnimGraph *-- CAnimGraphControllerPtr
    CBaseAnimGraph *-- CEntityIOOutput
    CBaseAnimGraph --> IPhysicsRagdollControl
    CBaseAnimGraph *-- PhysicsRagdollPose_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_graphControllerManager` | [CAnimGraphControllerManager](../schemas/server.md#canimgraphcontrollermanager) |  |
| `m_pMainGraphController` | [CAnimGraphControllerPtr](../schemas/server.md#canimgraphcontrollerptr) |  |
| `m_bInitiallyPopulateInterpHistory` | bool |  |
| `m_bSuppressAnimEventSounds` | bool |  |
| `m_OnLayerCycleUpdated` | CEntityOutputTemplate< float32 > |  |
| `m_OnExternalChoreoGraphChanged` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_bAnimGraphUpdateEnabled` | bool |  |
| `m_bAnimationUpdateScheduled` | bool | `MNotSaved` |
| `m_vecForce` | Vector | `MNotSaved` |
| `m_nForceBone` | int32 | `MNotSaved` |
| `m_pClientsideRagdoll` | [CBaseAnimGraph](../schemas/client.md#cbaseanimgraph)* | `MNotSaved` |
| `m_bBuiltRagdoll` | bool | `MNotSaved` |
| `m_pRagdollControl` | [IPhysicsRagdollControl](../schemas/vphysics2.md#iphysicsragdollcontrol)* | `MPhysPtr` |
| `m_RagdollPose` | [PhysicsRagdollPose_t](../schemas/client.md#physicsragdollpose_t) |  |
| `m_bRagdollEnabled` | bool |  |
| `m_bRagdollClientSide` | bool | `MNotSaved` |
| `m_bHasAnimatedMaterialAttributes` | bool | `MNotSaved` |

### CBaseAnimGraphAPI

### CBaseAnimGraphAlias_baseanimating

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- CBaseAnimGraphAlias_baseanimating
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### CBaseAnimGraphController

**Inherits from:** [CSkeletonAnimationController](server.md#cskeletonanimationcontroller)

**Metadata:** `MGetKV3ClassDefaults {
	"m_nAnimationAlgorithm": "eInvalid",
	"m_nNextExternalGraphHandle": 0,
	"m_vecSecondarySkeletonSlotIDs":
	[
	],
	"m_vecSecondarySkeletons":
	[
	],
	"m_nSecondarySkeletonMasterCount": 0,
	"m_flSoundSyncTime": 0.000000,
	"m_nActiveIKChainMask": 0,
	"m_hSequence": -1,
	"m_flSeqStartTime": null,
	"m_flSeqFixedCycle": 0.000000,
	"m_nAnimLoopMode": "ANIM_LOOP_MODE_USE_SEQUENCE_SETTINGS",
	"m_flPlaybackRate": 1.000000,
	"m_nNotifyState": "eDoNotNotify",
	"m_bNetworkedAnimationInputsChanged": false,
	"m_bNetworkedSequenceChanged": false,
	"m_bLastUpdateSkipped": false,
	"m_bSequenceFinished": false,
	"m_nPrevAnimUpdateTick": null,
	"m_hGraphDefinitionAG2": "",
	"m_nServerGraphInstanceIteration": 0,
	"m_nServerSerializationContextIteration": 0,
	"m_primaryGraphId": 0,
	"m_vecExternalGraphIds":
	[
	],
	"m_vecExternalClipIds":
	[
	],
	"m_sAnimGraph2Identifier": "",
	"m_pGraphInstanceAG2": null,
	"m_vecExternalGraphs": null,
	"m_nPrevAnimationAlgorithm": "eNone"
}`

**Relationships:**

```mermaid
classDiagram
    CSkeletonAnimationController <|-- CBaseAnimGraphController
    ISkeletonAnimationController <|-- CSkeletonAnimationController
    CBaseAnimGraphController *-- AnimationAlgorithm_t
    CBaseAnimGraphController *-- ExternalAnimGraphHandle_t
    CBaseAnimGraphController --> CBaseAnimGraph
    CBaseAnimGraphController *-- HSequence
    CBaseAnimGraphController *-- GameTime_t
    CBaseAnimGraphController *-- AnimLoopMode_t
    CBaseAnimGraphController *-- SequenceFinishNotifyState_t
    CBaseAnimGraphController *-- GameTick_t
    CBaseAnimGraphController *-- InfoForResourceTypeCNmGraphDefinition
    CBaseAnimGraphController *-- AnimGraph2SerializedPoseRecipeSlot_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nAnimationAlgorithm` | [AnimationAlgorithm_t](../schemas/!GlobalTypes.md#animationalgorithm_t) |  |
| `m_nNextExternalGraphHandle` | [ExternalAnimGraphHandle_t](../schemas/server.md#externalanimgraphhandle_t) |  |
| `m_vecSecondarySkeletonSlotIDs` | C_NetworkUtlVectorBase< CGlobalSymbol > |  |
| `m_vecSecondarySkeletons` | C_NetworkUtlVectorBase< CHandle< [CBaseAnimGraph](../schemas/client.md#cbaseanimgraph) > > |  |
| `m_nSecondarySkeletonMasterCount` | int32 |  |
| `m_flSoundSyncTime` | float32 |  |
| `m_nActiveIKChainMask` | uint32 |  |
| `m_hSequence` | [HSequence](../schemas/animationsystem.md#hsequence) |  |
| `m_flSeqStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flSeqFixedCycle` | float32 |  |
| `m_nAnimLoopMode` | [AnimLoopMode_t](../schemas/!GlobalTypes.md#animloopmode_t) |  |
| `m_flPlaybackRate` | CNetworkedQuantizedFloat |  |
| `m_nNotifyState` | [SequenceFinishNotifyState_t](../schemas/!GlobalTypes.md#sequencefinishnotifystate_t) |  |
| `m_bNetworkedAnimationInputsChanged` | bool |  |
| `m_bNetworkedSequenceChanged` | bool |  |
| `m_bLastUpdateSkipped` | bool |  |
| `m_bSequenceFinished` | bool |  |
| `m_nPrevAnimUpdateTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_hGraphDefinitionAG2` | CStrongHandle< [InfoForResourceTypeCNmGraphDefinition](../schemas/resourcesystem.md#infoforresourcetypecnmgraphdefinition) > |  |
| `m_SerializePoseRecipeAG2Slots` | C_UtlVectorEmbeddedNetworkVar< [AnimGraph2SerializedPoseRecipeSlot_t](../schemas/client.md#animgraph2serializedposerecipeslot_t) > | `MNotSaved` |
| `m_SerializePoseRecipeAG2Dynamic` | C_NetworkUtlVectorBase< uint8 > | `MNotSaved` |
| `m_nSerializePoseRecipeAG2ActiveSlot` | uint32 | `MNotSaved` |
| `m_nSerializePoseRecipeVersionAG2` | int32 | `MNotSaved` |
| `m_nServerGraphInstanceIteration` | int32 |  |
| `m_nServerSerializationContextIteration` | int32 |  |
| `m_primaryGraphId` | [ResourceId_t](../schemas/resourcefile.md#resourceid_t) |  |
| `m_vecExternalGraphIds` | C_NetworkUtlVectorBase< [ResourceId_t](../schemas/resourcefile.md#resourceid_t) > |  |
| `m_vecExternalClipIds` | C_NetworkUtlVectorBase< [ResourceId_t](../schemas/resourcefile.md#resourceid_t) > |  |
| `m_sAnimGraph2Identifier` | CGlobalSymbol |  |
| `m_pGraphInstanceAG2` | [CAnimGraph2InstancePtr](../schemas/server.md#canimgraph2instanceptr) |  |
| `m_vecExternalGraphs` | [CExternalAnimGraphList](../schemas/server.md#cexternalanimgraphlist) |  |
| `m_nPrevAnimationAlgorithm` | [AnimationAlgorithm_t](../schemas/!GlobalTypes.md#animationalgorithm_t) |  |

### CBaseEntity_SharedAPI

### CBaseFilter

**Inherits from:** [CLogicalEntity](client.md#clogicalentity)

**Derived by:** [CFilterAttributeInt](client.md#cfilterattributeint), [CFilterClass](client.md#cfilterclass), [CFilterContext](server.md#cfiltercontext), [CFilterEnemy](server.md#cfilterenemy), [CFilterLOS](client.md#cfilterlos), [CFilterMassGreater](client.md#cfiltermassgreater), [CFilterModel](client.md#cfiltermodel), [CFilterMultiple](client.md#cfiltermultiple), [CFilterName](client.md#cfiltername), [CFilterProximity](client.md#cfilterproximity), [CFilterTeam](client.md#cfilterteam), [FilterDamageType](client.md#filterdamagetype), [FilterHealth](client.md#filterhealth)

**Relationships:**

```mermaid
classDiagram
    CLogicalEntity <|-- CBaseFilter
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
    CBaseFilter <|-- CFilterAttributeInt
    CBaseFilter <|-- CFilterClass
    CBaseFilter <|-- CFilterLOS
    CBaseFilter <|-- CFilterMassGreater
    CBaseFilter <|-- CFilterModel
    CBaseFilter <|-- CFilterMultiple
    CBaseFilter <|-- CFilterName
    CBaseFilter <|-- CFilterProximity
    CBaseFilter <|-- CFilterTeam
    CBaseFilter <|-- FilterDamageType
    CBaseFilter <|-- FilterHealth
    CBaseFilter <|-- CFilterContext
    CBaseFilter <|-- CFilterEnemy
    CBaseFilter *-- CEntityIOOutput
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bNegated` | bool |  |
| `m_OnPass` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnFail` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |

### CBaseGrenade_API

### CBaseModelEntityAPI

### CBasePlayerController

Base class for all player controller entities in Source 2.  A controller is the persistent, session-level entity that represents a connected client; it is never recreated between rounds.  The controller owns one or more pawn entities (the physical in-world representation).


**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [CCSPlayerController](client.md#ccsplayercontroller)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- CBasePlayerController
    CEntityInstance <|-- C_BaseEntity
    CBasePlayerController <|-- CCSPlayerController
    CBasePlayerController *-- C_CommandContext
    CBasePlayerController --> C_BasePlayerPawn
    CBasePlayerController *-- PlayerConnectedState
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_CommandContext` | [C_CommandContext](../schemas/client.md#c_commandcontext) | `MNotSaved` |
| `m_nInButtonsWhichAreToggles` | uint64 | `MNotSaved` |
| `m_nTickBase` | uint32 | Server tick number at the time of the most-recent usercmd from this client. *Only sent to the owning player (LocalPlayerExclusive). Used for lag compensation and prediction.* `MNotSaved` |
| `m_hPawn` | CHandle< [C_BasePlayerPawn](../schemas/client.md#c_baseplayerpawn) > | CHandle to the base pawn currently controlled by this controller. *For CS2 human players the concrete type is CCSPlayerPawn.  Use m_hPlayerPawn on CCSPlayerController for the typed handle.* |
| `m_bKnownTeamMismatch` | bool |  |
| `m_hPredictedPawn` | CHandle< [C_BasePlayerPawn](../schemas/client.md#c_baseplayerpawn) > | `MNotSaved` |
| `m_nSplitScreenSlot` | CSplitScreenSlot | `MNotSaved` |
| `m_hSplitOwner` | CHandle< [CBasePlayerController](../schemas/client.md#cbaseplayercontroller) > | `MNotSaved` |
| `m_hSplitScreenPlayers` | CUtlVector< CHandle< [CBasePlayerController](../schemas/client.md#cbaseplayercontroller) > > | `MNotSaved` |
| `m_bIsHLTV` | bool |  |
| `m_iConnected` | [PlayerConnectedState](../schemas/!GlobalTypes.md#playerconnectedstate) | PlayerConnectedState enum – 0 = Disconnected, 1 = Connected, 2 = Connecting. `MNotSaved` |
| `m_iMostConnected` | [PlayerConnectedState](../schemas/!GlobalTypes.md#playerconnectedstate) | `MNotSaved` |
| `m_iszPlayerName` | char[128] | Display name of the player, as reported by Steam (up to 128 bytes, UTF-8). `MNotSaved` |
| `m_steamID` | uint64 | 64-bit Steam account ID (SteamID64) of the connected client. *Transmitted as a fixed64; only sent to the owning player and GOTV.* `MNotSaved` |
| `m_bIsLocalPlayerController` | bool | `MNotSaved` |
| `m_bNoClipEnabled` | bool | True when sv_cheats noclip is active for this player. |
| `m_iDesiredFOV` | uint32 | Field-of-view override requested by the player (0 = use server default). |

### CBasePlayerControllerAPI

### CBasePlayerVData

**Inherits from:** [CEntitySubclassVDataBase](server.md#centitysubclassvdatabase)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CBasePlayerVData",
	"m_sModelName": "",
	"m_sModelNameAg2Override": "",
	"m_flHeadDamageMultiplier": 3.000000,
	"m_flChestDamageMultiplier": 1.000000,
	"m_flStomachDamageMultiplier": 1.000000,
	"m_flArmDamageMultiplier": 1.000000,
	"m_flLegDamageMultiplier": 1.000000,
	"m_flHoldBreathTime": 15.000000,
	"m_flDrowningDamageInterval": 1.000000,
	"m_nDrowningDamageInitial": 10,
	"m_nDrowningDamageMax": 10,
	"m_nWaterSpeed": 100,
	"m_flUseRange": 55.000000,
	"m_flUseAngleTolerance": 45.000000,
	"m_flCrouchTime": 0.400000
}`

**Relationships:**

```mermaid
classDiagram
    CEntitySubclassVDataBase <|-- CBasePlayerVData
    CBasePlayerVData *-- InfoForResourceTypeCModel
    CBasePlayerVData *-- CSkillFloat
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_sModelName` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeCModel](../schemas/resourcesystem.md#infoforresourcetypecmodel) > > | `MPropertyProvidesEditContextString ToolEditContext_ID_VMDL` |
| `m_sModelNameAg2Override` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeCModel](../schemas/resourcesystem.md#infoforresourcetypecmodel) > > | `MPropertyProvidesEditContextString ToolEditContext_ID_VMDL` |
| `m_flHeadDamageMultiplier` | [CSkillFloat](../schemas/server.md#cskillfloat) |  |
| `m_flChestDamageMultiplier` | [CSkillFloat](../schemas/server.md#cskillfloat) |  |
| `m_flStomachDamageMultiplier` | [CSkillFloat](../schemas/server.md#cskillfloat) |  |
| `m_flArmDamageMultiplier` | [CSkillFloat](../schemas/server.md#cskillfloat) |  |
| `m_flLegDamageMultiplier` | [CSkillFloat](../schemas/server.md#cskillfloat) |  |
| `m_flHoldBreathTime` | float32 | `MPropertyGroupName Water` |
| `m_flDrowningDamageInterval` | float32 | `MPropertyDescription Seconds between drowning ticks` `MPropertyGroupName Water` |
| `m_nDrowningDamageInitial` | int32 | `MPropertyDescription Amount of damage done on the first drowning tick (+1 each subsequent interval)` `MPropertyGroupName Water` |
| `m_nDrowningDamageMax` | int32 | `MPropertyDescription Max damage done by a drowning tick` `MPropertyGroupName Water` |
| `m_nWaterSpeed` | int32 | `MPropertyGroupName Water` |
| `m_flUseRange` | float32 | `MPropertyGroupName Use` |
| `m_flUseAngleTolerance` | float32 | `MPropertyGroupName Use` |
| `m_flCrouchTime` | float32 | `MPropertyDescription Time to move between crouch and stand` `MPropertyGroupName Crouch` |

### CBasePlayerWeaponVData

**Inherits from:** [CEntitySubclassVDataBase](server.md#centitysubclassvdatabase)

**Derived by:** [CCSWeaponBaseVData](client.md#ccsweaponbasevdata)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CBasePlayerWeaponVData",
	"m_szWorldModel": "",
	"m_szWorldModelAg2Override": "",
	"m_sToolsOnlyOwnerModelName": "",
	"m_bBuiltRightHanded": true,
	"m_bAllowFlipping": true,
	"m_sMuzzleAttachment": "muzzle",
	"m_szMuzzleFlashParticle": "",
	"m_szMuzzleFlashParticleConfig": "",
	"m_szBarrelSmokeParticle": "",
	"m_nMuzzleSmokeShotThreshold": 4,
	"m_flMuzzleSmokeTimeout": 0.250000,
	"m_flMuzzleSmokeDecrementRate": 1.000000,
	"m_bGenerateMuzzleLight": true,
	"m_bLinkedCooldowns": false,
	"m_iFlags": "",
	"m_iWeight": 0,
	"m_bAutoSwitchTo": true,
	"m_bAutoSwitchFrom": true,
	"m_nPrimaryAmmoType": "",
	"m_nSecondaryAmmoType": "",
	"m_iMaxClip1": 0,
	"m_iMaxClip2": 0,
	"m_iDefaultClip1": -1,
	"m_iDefaultClip2": -1,
	"m_bReserveAmmoAsClips": false,
	"m_bTreatAsSingleClip": false,
	"m_bKeepLoadedAmmo": false,
	"m_iRumbleEffect": "RUMBLE_INVALID",
	"m_flDropSpeed": 300.000000,
	"m_iSlot": 0,
	"m_iPosition": 0,
	"m_aShootSounds":
	{
	}
}`

**Relationships:**

```mermaid
classDiagram
    CEntitySubclassVDataBase <|-- CBasePlayerWeaponVData
    CBasePlayerWeaponVData <|-- CCSWeaponBaseVData
    CBasePlayerWeaponVData *-- InfoForResourceTypeCModel
    CBasePlayerWeaponVData *-- InfoForResourceTypeIParticleSystemDefinition
    CBasePlayerWeaponVData *-- ItemFlagTypes_t
    CBasePlayerWeaponVData *-- AmmoIndex_t
    CBasePlayerWeaponVData *-- RumbleEffect_t
    CBasePlayerWeaponVData *-- WeaponSound_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_szWorldModel` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeCModel](../schemas/resourcesystem.md#infoforresourcetypecmodel) > > | `MPropertyDescription Model used on the ground or held by an entity` `MPropertyProvidesEditContextString ToolEditContext_ID_VMDL` `MPropertyStartGroup Visuals` |
| `m_szWorldModelAg2Override` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeCModel](../schemas/resourcesystem.md#infoforresourcetypecmodel) > > | `MPropertyDescription Model used on the ground or held by an entity` `MPropertyProvidesEditContextString ToolEditContext_ID_VMDL` |
| `m_sToolsOnlyOwnerModelName` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeCModel](../schemas/resourcesystem.md#infoforresourcetypecmodel) > > | `MPropertyDescription Model used by the tools only to populate comboboxes for things like animgraph parameter pickers` |
| `m_bBuiltRightHanded` | bool | `MPropertyDescription Was the weapon was built right-handed?` |
| `m_bAllowFlipping` | bool | `MPropertyDescription Allows flipping the model, regardless of whether it is built left or right handed` |
| `m_sMuzzleAttachment` | CAttachmentNameSymbolWithStorage | `MPropertyDescription Attachment to fire bullets from` |
| `m_szMuzzleFlashParticle` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeIParticleSystemDefinition](../schemas/resourcesystem.md#infoforresourcetypeiparticlesystemdefinition) > > | `MPropertyDescription Effect when firing this weapon` |
| `m_szMuzzleFlashParticleConfig` | CUtlString | `MPropertyAttributeEditor ParticleConfigName()` `MPropertyDescription Effect Config for Muzzle Flash - if set, will use this config specified in the particle effect, using whatever CP configuration is specified there, vdata muzzleflash attachment will be ignored` `MPropertyEditContextOverrideKey ToolEditContext_ID_VPCF` |
| `m_szBarrelSmokeParticle` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeIParticleSystemDefinition](../schemas/resourcesystem.md#infoforresourcetypeiparticlesystemdefinition) > > | `MPropertyDescription Barrel smoke after firing this weapon` |
| `m_nMuzzleSmokeShotThreshold` | uint8 | `MPropertyDescription Barrel smoke shot threshold to create smoke` |
| `m_flMuzzleSmokeTimeout` | float32 | `MPropertyDescription Barrel smoke shot timeout` |
| `m_flMuzzleSmokeDecrementRate` | float32 | `MPropertyDescription Barrel smoke decrement rate when not firing` |
| `m_bGenerateMuzzleLight` | bool |  |
| `m_bLinkedCooldowns` | bool | `MPropertyDescription Should both primary and secondary attacks be cooled down together (so cooling down primary attack would cooldown both primary + secondary attacks)?` `MPropertyStartGroup Behavior` |
| `m_iFlags` | [ItemFlagTypes_t](../schemas/!GlobalTypes.md#itemflagtypes_t) |  |
| `m_iWeight` | int32 | `MPropertyDescription This value used to determine this weapon's importance in autoselection` |
| `m_bAutoSwitchTo` | bool | `MPropertyDescription Whether this weapon is safe to automatically switch to (should be false for eg. explosives that can the player may accidentally hurt themselves with)` `MPropertyFriendlyName Safe To Auto-Switch To` |
| `m_bAutoSwitchFrom` | bool | `MPropertyFriendlyName Safe To Auto-Switch Away From` |
| `m_nPrimaryAmmoType` | [AmmoIndex_t](../schemas/server.md#ammoindex_t) | `MPropertyAttributeEditor VDataChoice( scripts/ammo.vdata )` `MPropertyCustomFGDType string` `MPropertyStartGroup Ammo` |
| `m_nSecondaryAmmoType` | [AmmoIndex_t](../schemas/server.md#ammoindex_t) | `MPropertyAttributeEditor VDataChoice( scripts/ammo.vdata )` `MPropertyCustomFGDType string` |
| `m_iMaxClip1` | int32 | `MPropertyAttributeRange 0 255` `MPropertyDescription How many bullets this gun can fire before it reloads (0 if no clip)` `MPropertyFriendlyName Primary Clip Size` |
| `m_iMaxClip2` | int32 | `MPropertyAttributeRange 0 255` `MPropertyDescription How many secondary bullets this gun can fire before it reloads (0 if no clip)` `MPropertyFriendlyName Secondary Clip Size` |
| `m_iDefaultClip1` | int32 | `MPropertyAttributeRange -1 255` `MPropertyDescription Primary Initial Clip (-1 means use clip size)` |
| `m_iDefaultClip2` | int32 | `MPropertyAttributeRange -1 255` `MPropertyDescription Secondary Initial Clip (-1 means use clip size)` |
| `m_bReserveAmmoAsClips` | bool | `MPropertyDescription Indicates whether to treat reserve ammo as clips (reloads) instead of raw bullets` |
| `m_bTreatAsSingleClip` | bool | `MPropertyDescription Regardless of ammo position, we'll always use clip1 as where our bullets come from` |
| `m_bKeepLoadedAmmo` | bool | `MPropertyDescription Indicates whether to keep any loaded ammo in the weapon on reload` |
| `m_iRumbleEffect` | [RumbleEffect_t](../schemas/!GlobalTypes.md#rumbleeffect_t) | `MPropertyStartGroup UI` |
| `m_flDropSpeed` | float32 |  |
| `m_iSlot` | int32 | `MPropertyDescription Which 'column' to display this weapon in the HUD` `MPropertyFriendlyName HUD Bucket` |
| `m_iPosition` | int32 | `MPropertyDescription Which 'row' to display this weapon in the HUD` `MPropertyFriendlyName HUD Bucket Position` |
| `m_aShootSounds` | CUtlOrderedMap< [WeaponSound_t](../schemas/!GlobalTypes.md#weaponsound_t), CSoundEventName > | `MPropertyStartGroup Sounds` |

### CBaseProp

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Derived by:** [CBreakableProp](server.md#cbreakableprop), [C_BreakableProp](client.md#c_breakableprop)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- CBaseProp
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    CBaseProp <|-- C_BreakableProp
    CBaseProp <|-- CBreakableProp
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bModelOverrodeBlockLOS` | bool |  |
| `m_iShapeType` | int32 |  |
| `m_bConformToCollisionBounds` | bool |  |
| `m_mPreferredCatchTransform` | CTransform |  |

### CBaseTriggerAPI

### CBodyComponent

**Inherits from:** [CEntityComponent](entity2.md#centitycomponent)

**Derived by:** [CBodyComponentPoint](client.md#cbodycomponentpoint), [CBodyComponentSkeletonInstance](client.md#cbodycomponentskeletoninstance)

**Metadata:** `MGetKV3ClassDefaults {
}`

**Relationships:**

```mermaid
classDiagram
    CEntityComponent <|-- CBodyComponent
    CBodyComponent <|-- CBodyComponentPoint
    CBodyComponent <|-- CBodyComponentSkeletonInstance
    CBodyComponent --> CGameSceneNode
    CBodyComponent *-- CNetworkVarChainer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_pSceneNode` | [CGameSceneNode](../schemas/client.md#cgamescenenode)* | `MNotSaved` |
| `__m_pChainEntity` | [CNetworkVarChainer](../schemas/entity2.md#cnetworkvarchainer) | `MNotSaved` |

### CBodyComponentBaseAnimGraph

**Inherits from:** [CBodyComponentSkeletonInstance](client.md#cbodycomponentskeletoninstance)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CBodyComponentBaseAnimGraph",
	"m_skeletonInstance":
	{
		"m_hParent":
		{
			"m_hOwner": null,
			"m_name": ""
		},
		"m_vecOrigin":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"m_angRotation":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"m_flScale": 1.000000,
		"m_vecAbsOrigin": null,
		"m_angAbsRotation":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"m_flAbsScale": 1.000000,
		"m_bDormant": false,
		"m_bForceParentToBeNetworked": false,
		"m_name": "",
		"m_hierarchyAttachName": "",
		"m_flClientLocalScale": 1.000000,
		"m_modelState":
		{
			"m_hModel": "",
			"m_ModelName": "",
			"m_flRootBoneOffset_x": 0.000000,
			"m_flRootBoneOffset_y": 0.000000,
			"m_flRootBoneOffset_z": 0.000000,
			"m_nRootBoneOffsetResetSerialNumber": 0,
			"m_bClientClothCreationSuppressed": false,
			"m_nAnimStateNoInterpSerialNumber": 0,
			"m_MeshGroupMask": 9223372036854775808,
			"m_nBodyGroupChoices":
			[
			],
			"m_nIdealMotionType": 3,
			"m_nForceLOD": -1,
			"m_nClothUpdateFlags": 0
		},
		"m_bDisableSolidCollisionsForHierarchy": false,
		"m_materialGroup": "",
		"m_nHitboxSet": 0
	},
	"m_animationController":
	{
		"m_nAnimationAlgorithm": "eInvalid",
		"m_nNextExternalGraphHandle": 0,
		"m_vecSecondarySkeletonSlotIDs":
		[
		],
		"m_vecSecondarySkeletons":
		[
		],
		"m_nSecondarySkeletonMasterCount": 0,
		"m_flSoundSyncTime": 0.000000,
		"m_nActiveIKChainMask": 0,
		"m_hSequence": -1,
		"m_flSeqStartTime": null,
		"m_flSeqFixedCycle": 0.000000,
		"m_nAnimLoopMode": "ANIM_LOOP_MODE_USE_SEQUENCE_SETTINGS",
		"m_flPlaybackRate": 1.000000,
		"m_nNotifyState": "eDoNotNotify",
		"m_bNetworkedAnimationInputsChanged": false,
		"m_bNetworkedSequenceChanged": false,
		"m_bLastUpdateSkipped": false,
		"m_bSequenceFinished": false,
		"m_nPrevAnimUpdateTick": null,
		"m_hGraphDefinitionAG2": "",
		"m_nServerGraphInstanceIteration": 0,
		"m_nServerSerializationContextIteration": 0,
		"m_primaryGraphId": 0,
		"m_vecExternalGraphIds":
		[
		],
		"m_vecExternalClipIds":
		[
		],
		"m_sAnimGraph2Identifier": "",
		"m_pGraphInstanceAG2": null,
		"m_vecExternalGraphs": null,
		"m_nPrevAnimationAlgorithm": "eNone"
	}
}`

**Relationships:**

```mermaid
classDiagram
    CBodyComponentSkeletonInstance <|-- CBodyComponentBaseAnimGraph
    CBodyComponent <|-- CBodyComponentSkeletonInstance
    CEntityComponent <|-- CBodyComponent
    CBodyComponentBaseAnimGraph *-- CBaseAnimGraphController
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_animationController` | [CBaseAnimGraphController](../schemas/client.md#cbaseanimgraphcontroller) |  |

### CBodyComponentBaseModelEntity

**Inherits from:** [CBodyComponentSkeletonInstance](client.md#cbodycomponentskeletoninstance)

**Relationships:**

```mermaid
classDiagram
    CBodyComponentSkeletonInstance <|-- CBodyComponentBaseModelEntity
    CBodyComponent <|-- CBodyComponentSkeletonInstance
    CEntityComponent <|-- CBodyComponent
```

### CBodyComponentPoint

**Inherits from:** [CBodyComponent](client.md#cbodycomponent)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CBodyComponent <|-- CBodyComponentPoint
    CEntityComponent <|-- CBodyComponent
    CBodyComponentPoint *-- CGameSceneNode
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_sceneNode` | [CGameSceneNode](../schemas/client.md#cgamescenenode) |  |

### CBodyComponentSkeletonInstance

**Inherits from:** [CBodyComponent](client.md#cbodycomponent)

**Derived by:** [CBodyComponentBaseAnimGraph](client.md#cbodycomponentbaseanimgraph), [CBodyComponentBaseModelEntity](client.md#cbodycomponentbasemodelentity)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CBodyComponent <|-- CBodyComponentSkeletonInstance
    CEntityComponent <|-- CBodyComponent
    CBodyComponentSkeletonInstance <|-- CBodyComponentBaseAnimGraph
    CBodyComponentSkeletonInstance <|-- CBodyComponentBaseModelEntity
    CBodyComponentSkeletonInstance *-- CSkeletonInstance
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_skeletonInstance` | [CSkeletonInstance](../schemas/client.md#cskeletoninstance) |  |

### CBombTarget

**Inherits from:** [C_BaseTrigger](client.md#c_basetrigger)

**Relationships:**

```mermaid
classDiagram
    C_BaseTrigger <|-- CBombTarget
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bBombPlantedHere` | bool |  |

### CBuoyancyHelper

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CBuoyancyHelper",
	"m_nFluidType": "",
	"m_flFluidDensity": 1.000000,
	"m_flNeutrallyBuoyantGravity": 0.000000,
	"m_flNeutrallyBuoyantLinearDamping": 0.000000,
	"m_flNeutrallyBuoyantAngularDamping": 0.000000,
	"m_bNeutrallyBuoyant": false,
	"m_vecFractionOfWheelSubmergedForWheelFriction":
	[
	],
	"m_vecWheelFrictionScales":
	[
	],
	"m_vecFractionOfWheelSubmergedForWheelDrag":
	[
	],
	"m_vecWheelDrag":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    CBuoyancyHelper --> IPhysicsMotionController
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_pController` | [IPhysicsMotionController](../schemas/vphysics2.md#iphysicsmotioncontroller)* | `MPhysPtr` |
| `m_nFluidType` | CUtlStringToken |  |
| `m_flFluidDensity` | float32 |  |
| `m_flNeutrallyBuoyantGravity` | float32 |  |
| `m_flNeutrallyBuoyantLinearDamping` | float32 |  |
| `m_flNeutrallyBuoyantAngularDamping` | float32 |  |
| `m_bNeutrallyBuoyant` | bool |  |
| `m_vecFractionOfWheelSubmergedForWheelFriction` | CUtlVector< float32 > |  |
| `m_vecWheelFrictionScales` | CUtlVector< float32 > |  |
| `m_vecFractionOfWheelSubmergedForWheelDrag` | CUtlVector< float32 > |  |
| `m_vecWheelDrag` | CUtlVector< float32 > |  |

### CCS2PawnGraphController

**Inherits from:** [CCS2WeaponGraphController](client.md#ccs2weapongraphcontroller)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CCS2PawnGraphController",
	"m_hExternalGraph": 4294967295,
	"m_action": null,
	"m_bActionReset": null,
	"m_flWeaponActionSpeedScale": null,
	"m_weaponCategory": null,
	"m_weaponType": null,
	"m_weaponExtraInfo": null,
	"m_flWeaponAmmo": null,
	"m_flWeaponAmmoMax": null,
	"m_flWeaponAmmoReserve": null,
	"m_bWeaponIsSilenced": null,
	"m_flWeaponIronsightAmount": null,
	"m_bIsUsingLegacyModel": null,
	"m_idleVariation": null,
	"m_deployVariation": null,
	"m_attackType": null,
	"m_attackThrowStrength": null,
	"m_flAttackVariation": null,
	"m_inspectVariation": null,
	"m_inspectExtraInfo": null,
	"m_reloadStage": null,
	"m_bIsDefusing": null,
	"m_moveType": null,
	"m_moveDirectionID": null,
	"m_flMoveSpeedX": null,
	"m_flMoveSpeedY": null,
	"m_flMoveSpeedHorizontal": null,
	"m_flPreviousMoveSpeedHorizontal": null,
	"m_flCrouchAmount": null,
	"m_bIsWalking": null,
	"m_flWeaponDropAmount": null,
	"m_groundAction": null,
	"m_groundActionDirectionID": null,
	"m_flGroundTurnAngleOrVelocity": null,
	"m_flLadderCycle": null,
	"m_flLadderYaw": null,
	"m_flLadderYawBackwards": null,
	"m_airAction": null,
	"m_flAirHeightAboveGround": null,
	"m_leftFootTarget": null,
	"m_rightFootTarget": null,
	"m_flFlashedAmount": null,
	"m_flAimPitchAngle": null,
	"m_flAimYawAngle": null,
	"m_flinchHead": null,
	"m_flinchHeadRestart": null,
	"m_flinchBody": null,
	"m_flinchBodyRestart": null,
	"m_flinchIsOnFire": null
}`

**Relationships:**

```mermaid
classDiagram
    CCS2WeaponGraphController <|-- CCS2PawnGraphController
    CAnimGraphControllerBase <|-- CCS2WeaponGraphController
    CCS2PawnGraphController *-- CNmTarget
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bIsDefusing` | CAnimGraph2ParamOptionalRef< bool > |  |
| `m_moveType` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_moveDirectionID` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_flMoveSpeedX` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flMoveSpeedY` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flMoveSpeedHorizontal` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flPreviousMoveSpeedHorizontal` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flCrouchAmount` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_bIsWalking` | CAnimGraph2ParamOptionalRef< bool > |  |
| `m_flWeaponDropAmount` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_groundAction` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_groundActionDirectionID` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_flGroundTurnAngleOrVelocity` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flLadderCycle` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flLadderYaw` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flLadderYawBackwards` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_airAction` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_flAirHeightAboveGround` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_leftFootTarget` | CAnimGraph2ParamOptionalRef< [CNmTarget](../schemas/animlib.md#cnmtarget) > |  |
| `m_rightFootTarget` | CAnimGraph2ParamOptionalRef< [CNmTarget](../schemas/animlib.md#cnmtarget) > |  |
| `m_flFlashedAmount` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flAimPitchAngle` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flAimYawAngle` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flinchHead` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_flinchHeadRestart` | CAnimGraph2ParamOptionalRef< bool > |  |
| `m_flinchBody` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_flinchBodyRestart` | CAnimGraph2ParamOptionalRef< bool > |  |
| `m_flinchIsOnFire` | CAnimGraph2ParamOptionalRef< bool > |  |

### CCS2UIPawnGraphController

**Inherits from:** [CAnimGraphControllerBase](server.md#canimgraphcontrollerbase)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CCS2UIPawnGraphController",
	"m_hExternalGraph": 4294967295,
	"m_nAnimationSeed": null,
	"m_characterMode": null,
	"m_bCharacterModeReset": null,
	"m_nTeamPreviewVariant": null,
	"m_nTeamPreviewRandom": null,
	"m_nTeamPreviewPosition": null,
	"m_endOfMatchCelebration": null,
	"m_action": null,
	"m_bannerAnimation": null,
	"m_weaponCategory": null,
	"m_weaponType": null,
	"m_weaponState": null,
	"m_inspectTurnAngle": null,
	"m_bCT": null
}`

**Relationships:**

```mermaid
classDiagram
    CAnimGraphControllerBase <|-- CCS2UIPawnGraphController
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nAnimationSeed` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_characterMode` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_bCharacterModeReset` | CAnimGraph2ParamOptionalRef< bool > |  |
| `m_nTeamPreviewVariant` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_nTeamPreviewRandom` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_nTeamPreviewPosition` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_endOfMatchCelebration` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_action` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_bannerAnimation` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_weaponCategory` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_weaponType` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_weaponState` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_inspectTurnAngle` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_bCT` | CAnimGraph2ParamOptionalRef< bool > |  |

### CCS2WeaponGraphController

**Inherits from:** [CAnimGraphControllerBase](server.md#canimgraphcontrollerbase)

**Derived by:** [CCS2PawnGraphController](client.md#ccs2pawngraphcontroller)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CCS2WeaponGraphController",
	"m_hExternalGraph": 4294967295,
	"m_action": null,
	"m_bActionReset": null,
	"m_flWeaponActionSpeedScale": null,
	"m_weaponCategory": null,
	"m_weaponType": null,
	"m_weaponExtraInfo": null,
	"m_flWeaponAmmo": null,
	"m_flWeaponAmmoMax": null,
	"m_flWeaponAmmoReserve": null,
	"m_bWeaponIsSilenced": null,
	"m_flWeaponIronsightAmount": null,
	"m_bIsUsingLegacyModel": null,
	"m_idleVariation": null,
	"m_deployVariation": null,
	"m_attackType": null,
	"m_attackThrowStrength": null,
	"m_flAttackVariation": null,
	"m_inspectVariation": null,
	"m_inspectExtraInfo": null,
	"m_reloadStage": null
}`

**Relationships:**

```mermaid
classDiagram
    CAnimGraphControllerBase <|-- CCS2WeaponGraphController
    CCS2WeaponGraphController <|-- CCS2PawnGraphController
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_action` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_bActionReset` | CAnimGraph2ParamOptionalRef< bool > |  |
| `m_flWeaponActionSpeedScale` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_weaponCategory` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_weaponType` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_weaponExtraInfo` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_flWeaponAmmo` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flWeaponAmmoMax` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flWeaponAmmoReserve` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_bWeaponIsSilenced` | CAnimGraph2ParamOptionalRef< bool > |  |
| `m_flWeaponIronsightAmount` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_bIsUsingLegacyModel` | CAnimGraph2ParamOptionalRef< bool > |  |
| `m_idleVariation` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_deployVariation` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_attackType` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_attackThrowStrength` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_flAttackVariation` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_inspectVariation` | CAnimGraph2ParamOptionalRef< float32 > |  |
| `m_inspectExtraInfo` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |
| `m_reloadStage` | CAnimGraph2ParamOptionalRef< CGlobalSymbol > |  |

### CCSGO_EndOfMatchLineupEnd

**Inherits from:** [C_CSGO_EndOfMatchLineupEndpoint](client.md#c_csgo_endofmatchlineupendpoint)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_EndOfMatchLineupEndpoint <|-- CCSGO_EndOfMatchLineupEnd
    C_BaseEntity <|-- C_CSGO_EndOfMatchLineupEndpoint
    CEntityInstance <|-- C_BaseEntity
```

### CCSGO_TeamPreviewCharacterPosition_API

### CCSGO_WingmanIntroCharacterPosition

**Inherits from:** [C_CSGO_TeamIntroCharacterPosition](client.md#c_csgo_teamintrocharacterposition)

**Derived by:** [CCSGO_WingmanIntroCounterTerroristPosition](client.md#ccsgo_wingmanintrocounterterroristposition), [CCSGO_WingmanIntroTerroristPosition](client.md#ccsgo_wingmanintroterroristposition)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamIntroCharacterPosition <|-- CCSGO_WingmanIntroCharacterPosition
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_TeamIntroCharacterPosition
    C_BaseEntity <|-- C_CSGO_TeamPreviewCharacterPosition
    CEntityInstance <|-- C_BaseEntity
    CCSGO_WingmanIntroCharacterPosition <|-- CCSGO_WingmanIntroCounterTerroristPosition
    CCSGO_WingmanIntroCharacterPosition <|-- CCSGO_WingmanIntroTerroristPosition
```

### CCSGO_WingmanIntroCounterTerroristPosition

**Inherits from:** [CCSGO_WingmanIntroCharacterPosition](client.md#ccsgo_wingmanintrocharacterposition)

**Relationships:**

```mermaid
classDiagram
    CCSGO_WingmanIntroCharacterPosition <|-- CCSGO_WingmanIntroCounterTerroristPosition
    C_CSGO_TeamIntroCharacterPosition <|-- CCSGO_WingmanIntroCharacterPosition
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_TeamIntroCharacterPosition
    C_BaseEntity <|-- C_CSGO_TeamPreviewCharacterPosition
    CEntityInstance <|-- C_BaseEntity
```

### CCSGO_WingmanIntroTerroristPosition

**Inherits from:** [CCSGO_WingmanIntroCharacterPosition](client.md#ccsgo_wingmanintrocharacterposition)

**Relationships:**

```mermaid
classDiagram
    CCSGO_WingmanIntroCharacterPosition <|-- CCSGO_WingmanIntroTerroristPosition
    C_CSGO_TeamIntroCharacterPosition <|-- CCSGO_WingmanIntroCharacterPosition
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_TeamIntroCharacterPosition
    C_BaseEntity <|-- C_CSGO_TeamPreviewCharacterPosition
    CEntityInstance <|-- C_BaseEntity
```

### CCSGameModeRules

**Derived by:** [CCSGameModeRules_ArmsRace](client.md#ccsgamemoderules_armsrace), [CCSGameModeRules_Deathmatch](client.md#ccsgamemoderules_deathmatch), [CCSGameModeRules_Noop](client.md#ccsgamemoderules_noop)

**Relationships:**

```mermaid
classDiagram
    CCSGameModeRules <|-- CCSGameModeRules_ArmsRace
    CCSGameModeRules <|-- CCSGameModeRules_Deathmatch
    CCSGameModeRules <|-- CCSGameModeRules_Noop
    CCSGameModeRules *-- CNetworkVarChainer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `__m_pChainEntity` | [CNetworkVarChainer](../schemas/entity2.md#cnetworkvarchainer) | `MNotSaved` |

### CCSGameModeRules_ArmsRace

**Inherits from:** [CCSGameModeRules](client.md#ccsgamemoderules)

**Relationships:**

```mermaid
classDiagram
    CCSGameModeRules <|-- CCSGameModeRules_ArmsRace
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_WeaponSequence` | C_NetworkUtlVectorBase< CUtlString > |  |

### CCSGameModeRules_Deathmatch

**Inherits from:** [CCSGameModeRules](client.md#ccsgamemoderules)

**Relationships:**

```mermaid
classDiagram
    CCSGameModeRules <|-- CCSGameModeRules_Deathmatch
    CCSGameModeRules_Deathmatch *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flDMBonusStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flDMBonusTimeLength` | float32 |  |
| `m_sDMBonusWeapon` | CUtlString |  |

### CCSGameModeRules_Noop

**Inherits from:** [CCSGameModeRules](client.md#ccsgamemoderules)

**Relationships:**

```mermaid
classDiagram
    CCSGameModeRules <|-- CCSGameModeRules_Noop
```

### CCSObserver_CameraServices

**Inherits from:** [CCSPlayerBase_CameraServices](client.md#ccsplayerbase_cameraservices)

**Relationships:**

```mermaid
classDiagram
    CCSPlayerBase_CameraServices <|-- CCSObserver_CameraServices
    CPlayer_CameraServices <|-- CCSPlayerBase_CameraServices
    CPlayerPawnComponent <|-- CPlayer_CameraServices
    CCSObserver_CameraServices --> C_PostProcessingVolume
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hPrevPostProcessingVolume` | CHandle< [C_PostProcessingVolume](../schemas/client.md#c_postprocessingvolume) > |  |

### CCSObserver_MovementServices

**Inherits from:** [CPlayer_MovementServices](client.md#cplayer_movementservices)

**Relationships:**

```mermaid
classDiagram
    CPlayer_MovementServices <|-- CCSObserver_MovementServices
    CPlayerPawnComponent <|-- CPlayer_MovementServices
```

### CCSObserver_ObserverServices

**Inherits from:** [CPlayer_ObserverServices](client.md#cplayer_observerservices)

**Relationships:**

```mermaid
classDiagram
    CPlayer_ObserverServices <|-- CCSObserver_ObserverServices
    CPlayerPawnComponent <|-- CPlayer_ObserverServices
    CCSObserver_ObserverServices *-- ObserverInterpState_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_obsInterpState` | [ObserverInterpState_t](../schemas/!GlobalTypes.md#observerinterpstate_t) |  |

### CCSObserver_UseServices

**Inherits from:** [CPlayer_UseServices](client.md#cplayer_useservices)

**Relationships:**

```mermaid
classDiagram
    CPlayer_UseServices <|-- CCSObserver_UseServices
    CPlayerPawnComponent <|-- CPlayer_UseServices
```

### CCSPlayerBase_CameraServices

**Inherits from:** [CPlayer_CameraServices](client.md#cplayer_cameraservices)

**Derived by:** [CCSObserver_CameraServices](client.md#ccsobserver_cameraservices), [CCSPlayer_CameraServices](client.md#ccsplayer_cameraservices)

**Relationships:**

```mermaid
classDiagram
    CPlayer_CameraServices <|-- CCSPlayerBase_CameraServices
    CPlayerPawnComponent <|-- CPlayer_CameraServices
    CCSPlayerBase_CameraServices <|-- CCSObserver_CameraServices
    CCSPlayerBase_CameraServices <|-- CCSPlayer_CameraServices
    CCSPlayerBase_CameraServices *-- GameTime_t
    CCSPlayerBase_CameraServices --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iFOV` | uint32 |  |
| `m_iFOVStart` | uint32 |  |
| `m_flFOVTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flFOVRate` | float32 |  |
| `m_hZoomOwner` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_flLastShotFOV` | float32 |  |

### CCSPlayerController

The server-side controller entity for a CS2 player.  One CCSPlayerController exists per connected client for the lifetime of the connection; it persists across rounds.  The controller owns a CCSPlayerPawn (the physical in-world representation) which may be recreated each round.


> 📝 The controller / pawn split mirrors the Source 2 architecture described in the HL2SDK: a lightweight controller manages session-level state (score, team, competitive rank) while the pawn carries per-round physics and animation state.  Demo parsers should track m_hPlayerPawn to find the corresponding pawn entity handle each round.


**Inherits from:** [CBasePlayerController](client.md#cbaseplayercontroller)

**Relationships:**

```mermaid
classDiagram
    CBasePlayerController <|-- CCSPlayerController
    C_BaseEntity <|-- CBasePlayerController
    CEntityInstance <|-- C_BaseEntity
    CCSPlayerController --> CCSPlayerController_InGameMoneyServices
    CCSPlayerController --> CCSPlayerController_InventoryServices
    CCSPlayerController --> CCSPlayerController_ActionTrackingServices
    CCSPlayerController --> CCSPlayerController_DamageServices
    CCSPlayerController *-- GameTime_t
    CCSPlayerController *-- QuestProgress
    CCSPlayerController --> C_CSPlayerPawn
    CCSPlayerController --> C_CSObserverPawn
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_pInGameMoneyServices` | [CCSPlayerController_InGameMoneyServices](../schemas/client.md#ccsplayercontroller_ingamemoneyservices)* |  |
| `m_pInventoryServices` | [CCSPlayerController_InventoryServices](../schemas/client.md#ccsplayercontroller_inventoryservices)* |  |
| `m_pActionTrackingServices` | [CCSPlayerController_ActionTrackingServices](../schemas/client.md#ccsplayercontroller_actiontrackingservices)* |  |
| `m_pDamageServices` | [CCSPlayerController_DamageServices](../schemas/client.md#ccsplayercontroller_damageservices)* |  |
| `m_iPing` | uint32 | Player's current network round-trip latency, in milliseconds. *Smoothed by m_flSmoothedPing server-side; updated roughly every 5 s.* |
| `m_bHasCommunicationAbuseMute` | bool |  |
| `m_uiCommunicationMuteFlags` | uint32 |  |
| `m_szCrosshairCodes` | CUtlSymbolLarge | Encoded crosshair configuration string (same format as the cl_crosshair_reticle_* convars share-code). |
| `m_iPendingTeamNum` | uint8 | Team number the player will be moved to at the next team-change opportunity. |
| `m_flForceTeamTime` | [GameTime_t](../schemas/entity2.md#gametime_t) | GameTime after which team-forcing is no longer applied. |
| `m_iCompTeammateColor` | int32 |  |
| `m_bEverPlayedOnTeam` | bool | True once this player has played at least one round as a non-spectator. |
| `m_flPreviousForceJoinTeamTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_szClan` | CUtlSymbolLarge | Player's clan tag string, displayed next to the name in the scoreboard. |
| `m_sSanitizedPlayerName` | CUtlString |  |
| `m_iCoachingTeam` | int32 | Team number this player is coaching (0 if not coaching). |
| `m_nPlayerDominated` | uint64 | 64-bit bitmask; bit N set means this player is dominating player-slot N. |
| `m_nPlayerDominatingMe` | uint64 | 64-bit mask of player-slot bits that are currently dominating this player.
 |
| `m_iCompetitiveRanking` | int32 | Player's current Premier/Competitive numeric skill rating. |
| `m_iCompetitiveWins` | int32 | Total number of ranked wins accumulated on this account. |
| `m_iCompetitiveRankType` | int8 | Rank type identifier (e.g. 0 = unranked, 11 = Premier, 12 = Competitive). |
| `m_iCompetitiveRankingPredicted_Win` | int32 | Predicted rating delta if the match ends in a win for this player. |
| `m_iCompetitiveRankingPredicted_Loss` | int32 | Predicted rating delta if the match ends in a loss. |
| `m_iCompetitiveRankingPredicted_Tie` | int32 | Predicted rating delta if the match ends in a tie/draw. |
| `m_nEndMatchNextMapVote` | int32 | Index of the map this player has voted for in the end-of-match map vote. |
| `m_unActiveQuestId` | uint16 | Active operation mission ID for this player (0 if none active). |
| `m_rtActiveMissionPeriod` | uint32 |  |
| `m_nQuestProgressReason` | [QuestProgress](../schemas/server.md#questprogress)::Reason | Reason code for the last quest-progress update sent to this player. |
| `m_unPlayerTvControlFlags` | uint32 |  |
| `m_iDraftIndex` | int32 |  |
| `m_msQueuedModeDisconnectionTimestamp` | uint32 |  |
| `m_uiAbandonRecordedReason` | uint32 |  |
| `m_eNetworkDisconnectionReason` | uint32 |  |
| `m_bCannotBeKicked` | bool |  |
| `m_bEverFullyConnected` | bool |  |
| `m_bAbandonAllowsSurrender` | bool |  |
| `m_bAbandonOffersInstantSurrender` | bool |  |
| `m_bDisconnection1MinWarningPrinted` | bool |  |
| `m_bScoreReported` | bool |  |
| `m_nDisconnectionTick` | int32 | Server tick at which this player disconnected (used for reconnect grace period). |
| `m_bControllingBot` | bool | True when this human controller has taken over a bot pawn. |
| `m_bHasControlledBotThisRound` | bool | True if the player took over a bot at any point this round. |
| `m_bHasBeenControlledByPlayerThisRound` | bool |  |
| `m_nBotsControlledThisRound` | int32 |  |
| `m_bCanControlObservedBot` | bool | True when the player is allowed to take control of the bot they are spectating. |
| `m_hPlayerPawn` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > | CHandle pointing to the player's active CCSPlayerPawn. *Becomes invalid (INVALID_EHANDLE) when the player is dead and their pawn has been removed.  Check m_bPawnIsAlive before dereferencing.
* |
| `m_hObserverPawn` | CHandle< [C_CSObserverPawn](../schemas/client.md#c_csobserverpawn) > | CHandle to the CCSObserverPawn when the player is spectating. *Valid only while the player is in spectator mode; otherwise INVALID_EHANDLE.* |
| `m_bPawnIsAlive` | bool | True while the player's pawn is alive and spawned. |
| `m_iPawnHealth` | uint32 | Current health of the pawn, networked to teammates and spectators. *Only sent to TeammateAndSpectatorExclusive group; enemies do not receive this.* |
| `m_iPawnArmor` | int32 | Current armor value of the pawn (0–100 for vest, 100+ for helmet). |
| `m_bPawnHasDefuser` | bool | True when the pawn is carrying a defuse kit. |
| `m_bPawnHasHelmet` | bool | True when the pawn has a full helmet (takes head-shot armor penalty into account). |
| `m_nPawnCharacterDefIndex` | uint16 | Item definition index of the character/agent skin equipped on the pawn. |
| `m_iPawnLifetimeStart` | int32 | Server tick on which the current pawn was spawned. |
| `m_iPawnLifetimeEnd` | int32 | Server tick on which the current pawn died (0 while still alive). |
| `m_iPawnBotDifficulty` | int32 |  |
| `m_hOriginalControllerOfCurrentPawn` | CHandle< [CCSPlayerController](../schemas/client.md#ccsplayercontroller) > | When a human takes over a bot, this holds a handle back to the original bot controller so the pawn can be returned after the human disconnects.
 |
| `m_iScore` | int32 | Lifetime score for this connection (frags minus team-kills, etc.). |
| `m_recentKillQueue` | uint8[8] | Circular buffer of the 8 most-recent enemy kills this round (pawn entity indices). *Used to determine domination/revenge streaks.* |
| `m_nFirstKill` | uint8 | Index within m_recentKillQueue of the oldest valid entry. |
| `m_nKillCount` | uint8 | Number of valid entries currently in m_recentKillQueue. |
| `m_bMvpNoMusic` | bool | True when the MVP jingle should be suppressed for this player's MVP award. |
| `m_eMvpReason` | int32 | Reason for the most recent MVP award (enum: 1 = most kills, 2 = bomb defuse, 3 = bomb plant, etc.). |
| `m_iMusicKitID` | int32 | Item definition index of the music kit active for this player. |
| `m_iMusicKitMVPs` | int32 | Number of MVPs awarded while this music kit has been equipped (affects music kit stat tracking). |
| `m_iMVPs` | int32 | Number of MVP stars the player has earned in the current match. |
| `m_bIsPlayerNameDirty` | bool |  |
| `m_bFireBulletsSeedSynchronized` | bool | True once the client's bullet-fire PRNG seed has been synchronised with the server. *Only sent to the owning player (LocalPlayerExclusive).* |

### CCSPlayerController_API

### CCSPlayerController_ActionTrackingServices

**Inherits from:** [CPlayerControllerComponent](server.md#cplayercontrollercomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerControllerComponent <|-- CCSPlayerController_ActionTrackingServices
    CCSPlayerController_ActionTrackingServices *-- CSPerRoundStats_t
    CCSPlayerController_ActionTrackingServices *-- CSMatchStats_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_perRoundStats` | C_UtlVectorEmbeddedNetworkVar< [CSPerRoundStats_t](../schemas/client.md#csperroundstats_t) > |  |
| `m_matchStats` | [CSMatchStats_t](../schemas/client.md#csmatchstats_t) |  |
| `m_iNumRoundKills` | int32 |  |
| `m_iNumRoundKillsHeadshots` | int32 |  |
| `m_flTotalRoundDamageDealt` | float32 |  |

### CCSPlayerController_DamageServices

**Inherits from:** [CPlayerControllerComponent](server.md#cplayercontrollercomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerControllerComponent <|-- CCSPlayerController_DamageServices
    CCSPlayerController_DamageServices *-- CDamageRecord
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSendUpdate` | int32 |  |
| `m_DamageList` | C_UtlVectorEmbeddedNetworkVar< [CDamageRecord](../schemas/client.md#cdamagerecord) > |  |

### CCSPlayerController_InGameMoneyServices

**Inherits from:** [CPlayerControllerComponent](server.md#cplayercontrollercomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerControllerComponent <|-- CCSPlayerController_InGameMoneyServices
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iAccount` | int32 |  |
| `m_iStartAccount` | int32 |  |
| `m_iTotalCashSpent` | int32 |  |
| `m_iCashSpentThisRound` | int32 |  |

### CCSPlayerController_InventoryServices

**Inherits from:** [CPlayerControllerComponent](server.md#cplayercontrollercomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerControllerComponent <|-- CCSPlayerController_InventoryServices
    CCSPlayerController_InventoryServices *-- MedalRank_t
    CCSPlayerController_InventoryServices *-- ServerAuthoritativeWeaponSlot_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vecNetworkableLoadout` | CUtlVector< [CCSPlayerController_InventoryServices](../schemas/client.md#ccsplayercontroller_inventoryservices)::NetworkedLoadoutSlot_t > |  |
| `m_unMusicID` | uint16 |  |
| `m_rank` | [MedalRank_t](../schemas/!GlobalTypes.md#medalrank_t)[6] |  |
| `m_nPersonaDataPublicLevel` | int32 |  |
| `m_nPersonaDataPublicCommendsLeader` | int32 |  |
| `m_nPersonaDataPublicCommendsTeacher` | int32 |  |
| `m_nPersonaDataPublicCommendsFriendly` | int32 |  |
| `m_nPersonaDataXpTrailLevel` | int32 |  |
| `m_vecServerAuthoritativeWeaponSlots` | C_UtlVectorEmbeddedNetworkVar< [ServerAuthoritativeWeaponSlot_t](../schemas/client.md#serverauthoritativeweaponslot_t) > |  |

### CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t

**Relationships:**

```mermaid
classDiagram
    "CCSPlayerController_InventoryServices::NetworkedLoadoutSlot_t" --> C_EconItemView
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `pItem` | [C_EconItemView](../schemas/client.md#c_econitemview)* |  |
| `team` | uint16 |  |
| `slot` | uint16 |  |

### CCSPlayerLegacyJump

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bOldJumpPressed` | bool |  |
| `m_flJumpPressedTime` | float32 |  |

### CCSPlayerModernJump

**Relationships:**

```mermaid
classDiagram
    CCSPlayerModernJump *-- GameTick_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nLastActualJumpPressTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_flLastActualJumpPressFrac` | float32 |  |
| `m_nLastUsableJumpPressTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_flLastUsableJumpPressFrac` | float32 |  |
| `m_nLastLandedTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_flLastLandedFrac` | float32 |  |
| `m_flLastLandedVelocityX` | float32 |  |
| `m_flLastLandedVelocityY` | float32 |  |
| `m_flLastLandedVelocityZ` | float32 |  |

### CCSPlayer_ActionTrackingServices

Component tracking scoring-relevant actions: weapon purchases and hostage rescue status.


**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CCSPlayer_ActionTrackingServices
    CCSPlayer_ActionTrackingServices --> C_BasePlayerWeapon
    CCSPlayer_ActionTrackingServices *-- WeaponPurchaseTracker_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hLastWeaponBeforeC4AutoSwitch` | CHandle< [C_BasePlayerWeapon](../schemas/client.md#c_baseplayerweapon) > |  |
| `m_bIsRescuing` | bool | True while the player is escorting a hostage to the rescue zone. |
| `m_weaponPurchasesThisMatch` | [WeaponPurchaseTracker_t](../schemas/client.md#weaponpurchasetracker_t) | WeaponPurchaseTracker_t recording which weapons were bought during the match (used for match-stats). |
| `m_weaponPurchasesThisRound` | [WeaponPurchaseTracker_t](../schemas/client.md#weaponpurchasetracker_t) | WeaponPurchaseTracker_t recording which weapons were bought this round (used for in-round stats and economy tracking). |

### CCSPlayer_AimPunchServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CCSPlayer_AimPunchServices
    CCSPlayer_AimPunchServices *-- GameTick_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_predictableBaseTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_predictableBaseTickInterpAmount` | float32 |  |
| `m_predictableBaseAngle` | QAngle |  |
| `m_predictableBaseAngleVel` | QAngle |  |
| `m_unpredictableBaseTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_unpredictableBaseAngle` | QAngle |  |

### CCSPlayer_BulletServices

Component tracking bullet-hit statistics registered on the server side.


**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CCSPlayer_BulletServices
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_totalHitsOnServer` | int32 | Cumulative number of bullet hits this player has registered on the server this round. |

### CCSPlayer_BuyServices

Component that records the player's sellback-eligible purchases for the current round.


**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CCSPlayer_BuyServices
    CCSPlayer_BuyServices *-- SellbackPurchaseEntry_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vecSellbackPurchaseEntries` | C_UtlVectorEmbeddedNetworkVar< [SellbackPurchaseEntry_t](../schemas/client.md#sellbackpurchaseentry_t) > | Vector of SellbackPurchaseEntry_t structs; each entry represents a weapon or equipment purchase that can still be sold back before freeze time expires. |

### CCSPlayer_CameraServices

**Inherits from:** [CCSPlayerBase_CameraServices](client.md#ccsplayerbase_cameraservices)

**Relationships:**

```mermaid
classDiagram
    CCSPlayerBase_CameraServices <|-- CCSPlayer_CameraServices
    CPlayer_CameraServices <|-- CCSPlayerBase_CameraServices
    CPlayerPawnComponent <|-- CPlayer_CameraServices
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flDeathCamTilt` | float32 |  |
| `m_vClientScopeInaccuracy` | Vector |  |

### CCSPlayer_DamageReactServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CCSPlayer_DamageReactServices
```

### CCSPlayer_GlowServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CCSPlayer_GlowServices
```

### CCSPlayer_HostageServices

Component tracking whether this player is currently carrying a hostage.


**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CCSPlayer_HostageServices
    CCSPlayer_HostageServices --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hCarriedHostage` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > | CHandle to the CHostage entity currently being carried by this player (INVALID_EHANDLE if none). |
| `m_hCarriedHostageProp` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > | CHandle to the ragdoll/prop entity representing the carried hostage visually. |

### CCSPlayer_ItemServices

**Inherits from:** [CPlayer_ItemServices](client.md#cplayer_itemservices)

**Relationships:**

```mermaid
classDiagram
    CPlayer_ItemServices <|-- CCSPlayer_ItemServices
    CPlayerPawnComponent <|-- CPlayer_ItemServices
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bHasDefuser` | bool |  |
| `m_bHasHelmet` | bool |  |

### CCSPlayer_MovementServices

**Inherits from:** [CPlayer_MovementServices_Humanoid](client.md#cplayer_movementservices_humanoid)

**Relationships:**

```mermaid
classDiagram
    CPlayer_MovementServices_Humanoid <|-- CCSPlayer_MovementServices
    CPlayer_MovementServices <|-- CPlayer_MovementServices_Humanoid
    CPlayerPawnComponent <|-- CPlayer_MovementServices
    CCSPlayer_MovementServices *-- CCSPlayerAnimationState
    CCSPlayer_MovementServices *-- GameTime_t
    CCSPlayer_MovementServices *-- CCSPlayerLegacyJump
    CCSPlayer_MovementServices *-- CCSPlayerModernJump
    CCSPlayer_MovementServices *-- GameTick_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_AnimationState` | [CCSPlayerAnimationState](../schemas/server.md#ccsplayeranimationstate) |  |
| `m_bUsingGroundTopologyOffset` | bool |  |
| `m_flUsingGroundTopologyOffsetTransitionSmoothing` | float32 |  |
| `m_vecLadderNormal` | Vector |  |
| `m_nLadderSurfacePropIndex` | int32 |  |
| `m_bDucked` | bool |  |
| `m_flDuckAmount` | float32 |  |
| `m_flDuckSpeed` | float32 |  |
| `m_bDuckOverride` | bool |  |
| `m_bDesiresDuck` | bool |  |
| `m_bDucking` | bool |  |
| `m_flDuckRootOffset` | float32 |  |
| `m_flDuckViewOffset` | float32 |  |
| `m_flLastDuckTime` | float32 |  |
| `m_flBombPlantViewOffset` | float32 |  |
| `m_vecLastPositionAtFullCrouchSpeed` | Vector2D |  |
| `m_duckUntilOnGround` | bool |  |
| `m_bHasWalkMovedSinceLastJump` | bool |  |
| `m_bInStuckTest` | bool |  |
| `m_nTraceCount` | int32 |  |
| `m_StuckLast` | int32 |  |
| `m_bSpeedCropped` | bool |  |
| `m_nOldWaterLevel` | int32 |  |
| `m_flWaterEntryTime` | float32 |  |
| `m_vecForward` | Vector |  |
| `m_vecLeft` | Vector |  |
| `m_vecUp` | Vector |  |
| `m_nGameCodeHasMovedPlayerAfterCommand` | int32 |  |
| `m_fStashGrenadeParameterWhen` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bUseFrictionStashedSpeed` | bool |  |
| `m_flUseFrictionStashedSpeedUntilFrac` | float32 |  |
| `m_flFrictionStashedSpeed` | float32 |  |
| `m_flStamina` | float32 |  |
| `m_flHeightAtJumpStart` | float32 |  |
| `m_flMaxJumpHeightThisJump` | float32 |  |
| `m_flMaxJumpHeightLastJump` | float32 |  |
| `m_flStaminaAtJumpStart` | float32 |  |
| `m_flVelMulAtJumpStart` | float32 |  |
| `m_flAccumulatedJumpError` | float32 |  |
| `m_LegacyJump` | [CCSPlayerLegacyJump](../schemas/client.md#ccsplayerlegacyjump) |  |
| `m_ModernJump` | [CCSPlayerModernJump](../schemas/client.md#ccsplayermodernjump) |  |
| `m_nLastJumpTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_flLastJumpFrac` | float32 |  |
| `m_flLastJumpVelocityZ` | float32 |  |
| `m_bJumpApexPending` | bool |  |
| `m_flTicksSinceLastSurfingDetected` | float32 |  |
| `m_bWasSurfing` | bool |  |
| `m_vecWalkWishVel` | Vector2D |  |
| `m_bHasEverProcessedCommand` | bool |  |

### CCSPlayer_PingServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CCSPlayer_PingServices
    CCSPlayer_PingServices --> C_PlayerPing
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hPlayerPing` | CHandle< [C_PlayerPing](../schemas/client.md#c_playerping) > |  |

### CCSPlayer_UseServices

**Inherits from:** [CPlayer_UseServices](client.md#cplayer_useservices)

**Relationships:**

```mermaid
classDiagram
    CPlayer_UseServices <|-- CCSPlayer_UseServices
    CPlayerPawnComponent <|-- CPlayer_UseServices
```

### CCSPlayer_WaterServices

**Inherits from:** [CPlayer_WaterServices](client.md#cplayer_waterservices)

**Relationships:**

```mermaid
classDiagram
    CPlayer_WaterServices <|-- CCSPlayer_WaterServices
    CPlayerPawnComponent <|-- CPlayer_WaterServices
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flWaterJumpTime` | float32 |  |
| `m_vecWaterJumpVel` | Vector |  |
| `m_flSwimSoundTime` | float32 |  |

### CCSPlayer_WeaponServices

Component attached to CCSPlayerPawn that manages the active weapon and weapon-switch timing for a CS2 player.


**Inherits from:** [CPlayer_WeaponServices](client.md#cplayer_weaponservices)

**Relationships:**

```mermaid
classDiagram
    CPlayer_WeaponServices <|-- CCSPlayer_WeaponServices
    CPlayerPawnComponent <|-- CPlayer_WeaponServices
    CCSPlayer_WeaponServices *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flNextAttack` | [GameTime_t](../schemas/entity2.md#gametime_t) | GameTime before which no weapon switch is permitted (e.g. after throwing a grenade). *Only sent to the owning player (LocalPlayerExclusive).* |
| `m_nOldTotalShootPositionHistoryCount` | uint32 |  |
| `m_nOldTotalInputHistoryCount` | uint32 |  |
| `m_networkAnimTiming` | C_NetworkUtlVectorBase< uint8 > | Byte array encoding animation transition timing for the active weapon, used to synchronise viewmodel animations across client and server. |
| `m_bBlockInspectUntilNextGraphUpdate` | bool | True when the inspect animation is suppressed until the animation graph ticks again (prevents stutter). |

### CCSWeaponBaseVData

**Inherits from:** [CBasePlayerWeaponVData](client.md#cbaseplayerweaponvdata)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CCSWeaponBaseVData",
	"m_szWorldModel": "",
	"m_szWorldModelAg2Override": "",
	"m_sToolsOnlyOwnerModelName": "",
	"m_bBuiltRightHanded": true,
	"m_bAllowFlipping": true,
	"m_sMuzzleAttachment": "muzzle",
	"m_szMuzzleFlashParticle": "",
	"m_szMuzzleFlashParticleConfig": "",
	"m_szBarrelSmokeParticle": "",
	"m_nMuzzleSmokeShotThreshold": 4,
	"m_flMuzzleSmokeTimeout": 0.250000,
	"m_flMuzzleSmokeDecrementRate": 1.000000,
	"m_bGenerateMuzzleLight": true,
	"m_bLinkedCooldowns": false,
	"m_iFlags": "",
	"m_iWeight": 0,
	"m_bAutoSwitchTo": true,
	"m_bAutoSwitchFrom": true,
	"m_nPrimaryAmmoType": "",
	"m_nSecondaryAmmoType": "",
	"m_iMaxClip1": 0,
	"m_iMaxClip2": 0,
	"m_iDefaultClip1": -1,
	"m_iDefaultClip2": -1,
	"m_bReserveAmmoAsClips": false,
	"m_bTreatAsSingleClip": false,
	"m_bKeepLoadedAmmo": false,
	"m_iRumbleEffect": "RUMBLE_INVALID",
	"m_flDropSpeed": 300.000000,
	"m_iSlot": 0,
	"m_iPosition": 0,
	"m_aShootSounds":
	{
	},
	"m_WeaponType": "WEAPONTYPE_UNKNOWN",
	"m_WeaponCategory": "WEAPONCATEGORY_OTHER",
	"m_szAnimSkeleton": "",
	"m_vecMuzzlePos0":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_vecMuzzlePos1":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_szTracerParticle": "",
	"m_GearSlot": "GEAR_SLOT_INVALID",
	"m_GearSlotPosition": -1,
	"m_DefaultLoadoutSlot": "LOADOUT_SLOT_INVALID",
	"m_nPrice": 0,
	"m_nKillAward": 0,
	"m_nPrimaryReserveAmmoMax": 0,
	"m_nSecondaryReserveAmmoMax": 0,
	"m_bMeleeWeapon": false,
	"m_bHasBurstMode": false,
	"m_bIsRevolver": false,
	"m_bCannotShootUnderwater": false,
	"m_szName": "",
	"m_eSilencerType": "WEAPONSILENCER_NONE",
	"m_nCrosshairMinDistance": 0,
	"m_nCrosshairDeltaDistance": 0,
	"m_bIsFullAuto": false,
	"m_nNumBullets": 0,
	"m_bReloadsSingleShells": false,
	"m_flCycleTime": 0.000000,
	"m_flCycleTimeWhenInBurstMode": 0.000000,
	"m_flTimeBetweenBurstShots": 0.000000,
	"m_flMaxSpeed": 0.000000,
	"m_flSpread": 0.000000,
	"m_flInaccuracyCrouch": 0.000000,
	"m_flInaccuracyStand": 0.000000,
	"m_flInaccuracyJump": 0.000000,
	"m_flInaccuracyLand": 0.000000,
	"m_flInaccuracyLadder": 0.000000,
	"m_flInaccuracyFire": 0.000000,
	"m_flInaccuracyMove": 0.000000,
	"m_flRecoilAngle": 0.000000,
	"m_flRecoilAngleVariance": 0.000000,
	"m_flRecoilMagnitude": 0.000000,
	"m_flRecoilMagnitudeVariance": 0.000000,
	"m_nTracerFrequency": 0,
	"m_flInaccuracyJumpInitial": 0.000000,
	"m_flInaccuracyJumpApex": 0.000000,
	"m_flInaccuracyReload": 0.000000,
	"m_flDeployDuration": 0.000000,
	"m_flDisallowAttackAfterReloadStartDuration": 0.000000,
	"m_nBurstShotCount": 2,
	"m_bAllowBurstHolster": true,
	"m_nRecoilSeed": 0,
	"m_nSpreadSeed": 0,
	"m_flAttackMovespeedFactor": 0.000000,
	"m_flInaccuracyPitchShift": 0.000000,
	"m_flInaccuracyAltSoundThreshold": 0.000000,
	"m_szUseRadioSubtitle": "",
	"m_bUnzoomsAfterShot": false,
	"m_bHideViewModelWhenZoomed": false,
	"m_nZoomLevels": 0,
	"m_nZoomFOV1": 0,
	"m_nZoomFOV2": 0,
	"m_flZoomTime0": 0.000000,
	"m_flZoomTime1": 0.000000,
	"m_flZoomTime2": 0.000000,
	"m_flIronSightPullUpSpeed": 8.000000,
	"m_flIronSightPutDownSpeed": 4.000000,
	"m_flIronSightFOV": 80.000000,
	"m_flIronSightPivotForward": 10.000000,
	"m_flIronSightLooseness": 0.500000,
	"m_nDamage": 0,
	"m_flHeadshotMultiplier": 0.000000,
	"m_flArmorRatio": 0.000000,
	"m_flPenetration": 0.000000,
	"m_flRange": 0.000000,
	"m_flRangeModifier": 0.000000,
	"m_flFlinchVelocityModifierLarge": 0.000000,
	"m_flFlinchVelocityModifierSmall": 0.000000,
	"m_flRecoveryTimeCrouch": 0.000000,
	"m_flRecoveryTimeStand": 0.000000,
	"m_flRecoveryTimeCrouchFinal": 0.000000,
	"m_flRecoveryTimeStandFinal": 0.000000,
	"m_nRecoveryTransitionStartBullet": 0,
	"m_nRecoveryTransitionEndBullet": 0,
	"m_flThrowVelocity": 0.000000,
	"m_vSmokeColor":
	[
		1.000000,
		1.000000,
		1.000000
	],
	"m_szAnimClass": ""
}`, `MPropertySuppressBaseClassField m_iPosition`, `MPropertySuppressBaseClassField m_iSlot`

**Relationships:**

```mermaid
classDiagram
    CBasePlayerWeaponVData <|-- CCSWeaponBaseVData
    CEntitySubclassVDataBase <|-- CBasePlayerWeaponVData
    CCSWeaponBaseVData *-- CSWeaponType
    CCSWeaponBaseVData *-- CSWeaponCategory
    CCSWeaponBaseVData *-- InfoForResourceTypeCNmSkeleton
    CCSWeaponBaseVData *-- InfoForResourceTypeIParticleSystemDefinition
    CCSWeaponBaseVData *-- CSWeaponSilencerType
    CCSWeaponBaseVData *-- CFiringModeFloat
    CCSWeaponBaseVData *-- CFiringModeInt
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_WeaponType` | [CSWeaponType](../schemas/!GlobalTypes.md#csweapontype) |  |
| `m_WeaponCategory` | [CSWeaponCategory](../schemas/!GlobalTypes.md#csweaponcategory) |  |
| `m_szAnimSkeleton` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeCNmSkeleton](../schemas/resourcesystem.md#infoforresourcetypecnmskeleton) > > | `MPropertyStartGroup Visuals` |
| `m_vecMuzzlePos0` | Vector |  |
| `m_vecMuzzlePos1` | Vector |  |
| `m_szTracerParticle` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeIParticleSystemDefinition](../schemas/resourcesystem.md#infoforresourcetypeiparticlesystemdefinition) > > | `MPropertyDescription Effect to actually fire into the world from this weapon` |
| `m_GearSlot` | gear_slot_t | `MPropertyDescription Which 'column' to display this weapon in the HUD` `MPropertyFriendlyName HUD Bucket` `MPropertyStartGroup HUD Positions` |
| `m_GearSlotPosition` | int32 |  |
| `m_DefaultLoadoutSlot` | loadout_slot_t | `MPropertyDescription Default team (non Terrorist or Counter-Terrorist) 'row' to display this weapon in the HUD.` `MPropertyFriendlyName HUD Bucket Position` |
| `m_nPrice` | int32 | `MPropertyStartGroup In-Game Data` |
| `m_nKillAward` | int32 |  |
| `m_nPrimaryReserveAmmoMax` | int32 |  |
| `m_nSecondaryReserveAmmoMax` | int32 |  |
| `m_bMeleeWeapon` | bool |  |
| `m_bHasBurstMode` | bool |  |
| `m_bIsRevolver` | bool |  |
| `m_bCannotShootUnderwater` | bool |  |
| `m_szName` | CGlobalSymbol | `MPropertyFriendlyName In-Code weapon name` |
| `m_eSilencerType` | [CSWeaponSilencerType](../schemas/!GlobalTypes.md#csweaponsilencertype) |  |
| `m_nCrosshairMinDistance` | int32 |  |
| `m_nCrosshairDeltaDistance` | int32 |  |
| `m_bIsFullAuto` | bool |  |
| `m_nNumBullets` | int32 |  |
| `m_bReloadsSingleShells` | bool |  |
| `m_flCycleTime` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) | `MPropertyStartGroup Firing Mode Data` |
| `m_flCycleTimeWhenInBurstMode` | float32 |  |
| `m_flTimeBetweenBurstShots` | float32 |  |
| `m_flMaxSpeed` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_flSpread` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_flInaccuracyCrouch` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_flInaccuracyStand` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_flInaccuracyJump` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_flInaccuracyLand` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_flInaccuracyLadder` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_flInaccuracyFire` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_flInaccuracyMove` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_flRecoilAngle` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_flRecoilAngleVariance` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_flRecoilMagnitude` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_flRecoilMagnitudeVariance` | [CFiringModeFloat](../schemas/server.md#cfiringmodefloat) |  |
| `m_nTracerFrequency` | [CFiringModeInt](../schemas/server.md#cfiringmodeint) |  |
| `m_flInaccuracyJumpInitial` | float32 |  |
| `m_flInaccuracyJumpApex` | float32 |  |
| `m_flInaccuracyReload` | float32 |  |
| `m_flDeployDuration` | float32 |  |
| `m_flDisallowAttackAfterReloadStartDuration` | float32 |  |
| `m_nBurstShotCount` | int32 |  |
| `m_bAllowBurstHolster` | bool |  |
| `m_nRecoilSeed` | int32 | `MPropertyStartGroup Firing` |
| `m_nSpreadSeed` | int32 |  |
| `m_flAttackMovespeedFactor` | float32 |  |
| `m_flInaccuracyPitchShift` | float32 |  |
| `m_flInaccuracyAltSoundThreshold` | float32 |  |
| `m_szUseRadioSubtitle` | CUtlString |  |
| `m_bUnzoomsAfterShot` | bool | `MPropertyStartGroup Zooming` |
| `m_bHideViewModelWhenZoomed` | bool |  |
| `m_nZoomLevels` | int32 |  |
| `m_nZoomFOV1` | int32 |  |
| `m_nZoomFOV2` | int32 |  |
| `m_flZoomTime0` | float32 |  |
| `m_flZoomTime1` | float32 |  |
| `m_flZoomTime2` | float32 |  |
| `m_flIronSightPullUpSpeed` | float32 | `MPropertyStartGroup Iron Sights` |
| `m_flIronSightPutDownSpeed` | float32 |  |
| `m_flIronSightFOV` | float32 |  |
| `m_flIronSightPivotForward` | float32 |  |
| `m_flIronSightLooseness` | float32 |  |
| `m_nDamage` | int32 | `MPropertyStartGroup Damage` |
| `m_flHeadshotMultiplier` | float32 |  |
| `m_flArmorRatio` | float32 |  |
| `m_flPenetration` | float32 |  |
| `m_flRange` | float32 |  |
| `m_flRangeModifier` | float32 |  |
| `m_flFlinchVelocityModifierLarge` | float32 |  |
| `m_flFlinchVelocityModifierSmall` | float32 |  |
| `m_flRecoveryTimeCrouch` | float32 | `MPropertyStartGroup Recovery` |
| `m_flRecoveryTimeStand` | float32 |  |
| `m_flRecoveryTimeCrouchFinal` | float32 |  |
| `m_flRecoveryTimeStandFinal` | float32 |  |
| `m_nRecoveryTransitionStartBullet` | int32 |  |
| `m_nRecoveryTransitionEndBullet` | int32 |  |
| `m_flThrowVelocity` | float32 | `MPropertyStartGroup Grenade Data` |
| `m_vSmokeColor` | Vector |  |
| `m_szAnimClass` | CGlobalSymbol |  |

### CCSWeaponBase_API

### CCS_PortraitWorldCallbackHandler

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- CCS_PortraitWorldCallbackHandler
    CEntityInstance <|-- C_BaseEntity
```

### CCashStack

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- CCashStack
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nCashStackValue` | int32 |  |

### CChoreoComponent

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CChoreoComponent",
	"m_hOwner": null,
	"m_nExernalChoreoGraphCount": 0,
	"m_sActiveExternalChoreoGraphSlotID": "",
	"m_nNextSceneEventId": 0,
	"m_flAllowResponsesEndTime": null
}`

**Relationships:**

```mermaid
classDiagram
    CChoreoComponent *-- CNetworkVarChainer
    CChoreoComponent --> C_BaseModelEntity
    CChoreoComponent *-- SceneEventId_t
    CChoreoComponent *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `__m_pChainEntity` | [CNetworkVarChainer](../schemas/entity2.md#cnetworkvarchainer) | `MNotSaved` |
| `m_hOwner` | CHandle< [C_BaseModelEntity](../schemas/client.md#c_basemodelentity) > |  |
| `m_nExernalChoreoGraphCount` | int32 |  |
| `m_sActiveExternalChoreoGraphSlotID` | CGlobalSymbol |  |
| `m_nNextSceneEventId` | [SceneEventId_t](../schemas/server.md#sceneeventid_t) |  |
| `m_flAllowResponsesEndTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |

### CChoreoInfoTarget

**Inherits from:** [C_PointEntity](client.md#c_pointentity)

**Relationships:**

```mermaid
classDiagram
    C_PointEntity <|-- CChoreoInfoTarget
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
```

### CCitadelSoundOpvarSetOBB

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- CCitadelSoundOpvarSetOBB
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iszStackName` | CUtlSymbolLarge |  |
| `m_iszOperatorName` | CUtlSymbolLarge |  |
| `m_iszOpvarName` | CUtlSymbolLarge |  |
| `m_vDistanceInnerMins` | Vector |  |
| `m_vDistanceInnerMaxs` | Vector |  |
| `m_vDistanceOuterMins` | Vector |  |
| `m_vDistanceOuterMaxs` | Vector |  |
| `m_nAABBDirection` | int32 |  |

### CClientAlphaProperty

**Inherits from:** [IClientAlphaProperty](client.md#iclientalphaproperty)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CClientAlphaProperty",
	"m_nDistFadeStart": 0,
	"m_nDistFadeEnd": 0,
	"m_nDesyncOffset": 0,
	"m_bAlphaOverride": 0,
	"m_bShadowAlphaOverride": 0,
	"m_nRenderMode": 0,
	"m_nRenderFX": 0,
	"m_nAlpha": 255,
	"m_flFadeScale": 0.000000,
	"m_flRenderFxStartTime": null,
	"m_flRenderFxDuration": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    IClientAlphaProperty <|-- CClientAlphaProperty
    CClientAlphaProperty *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bAlphaOverride` | bitfield:1 |  |
| `m_bShadowAlphaOverride` | bitfield:1 |  |
| `m_nDesyncOffset` | bitfield:14 |  |
| `m_nRenderFX` | bitfield:5 |  |
| `m_nRenderMode` | bitfield:3 |  |
| `m_nDistFadeStart` | uint16 |  |
| `m_nDistFadeEnd` | uint16 |  |
| `m_nAlpha` | uint8 |  |
| `m_flFadeScale` | float32 |  |
| `m_flRenderFxStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flRenderFxDuration` | float32 |  |

### CCollisionProperty

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CCollisionProperty",
	"m_collisionAttribute":
	{
		"m_nInteractsAs": 131072,
		"m_nInteractsWith": 0,
		"m_nInteractsExclude": 0,
		"m_nEntityId": 0,
		"m_nOwnerId": 4294967295,
		"m_nHierarchyId": 0,
		"m_nDetailLayerMask": 0,
		"m_nDetailLayerMaskType": 0,
		"m_nTargetDetailLayer": 0,
		"m_nCollisionGroup": 4,
		"m_nCollisionFunctionMask": 7
	},
	"m_vecMins":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_vecMaxs":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_usSolidFlags": 0,
	"m_nSolidType": "SOLID_NONE",
	"m_triggerBloat": 0,
	"m_nSurroundType": "USE_OBB_COLLISION_BOUNDS",
	"m_CollisionGroup": 4,
	"m_nEnablePhysics": 1,
	"m_flBoundingRadius": 0.000000,
	"m_vecSpecifiedSurroundingMins":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_vecSpecifiedSurroundingMaxs":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_vecSurroundingMaxs":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_vecSurroundingMins":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_vCapsuleCenter1":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_vCapsuleCenter2":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_flCapsuleRadius": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    CCollisionProperty *-- VPhysicsCollisionAttribute_t
    CCollisionProperty *-- SolidType_t
    CCollisionProperty *-- SurroundingBoundsType_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_collisionAttribute` | [VPhysicsCollisionAttribute_t](../schemas/client.md#vphysicscollisionattribute_t) |  |
| `m_vecMins` | Vector | `MSaveBehavior` |
| `m_vecMaxs` | Vector | `MSaveBehavior` |
| `m_usSolidFlags` | uint8 |  |
| `m_nSolidType` | [SolidType_t](../schemas/!GlobalTypes.md#solidtype_t) |  |
| `m_triggerBloat` | uint8 |  |
| `m_nSurroundType` | [SurroundingBoundsType_t](../schemas/!GlobalTypes.md#surroundingboundstype_t) |  |
| `m_CollisionGroup` | uint8 |  |
| `m_nEnablePhysics` | uint8 |  |
| `m_flBoundingRadius` | float32 |  |
| `m_vecSpecifiedSurroundingMins` | Vector |  |
| `m_vecSpecifiedSurroundingMaxs` | Vector |  |
| `m_vecSurroundingMaxs` | Vector |  |
| `m_vecSurroundingMins` | Vector |  |
| `m_vCapsuleCenter1` | Vector |  |
| `m_vCapsuleCenter2` | Vector |  |
| `m_flCapsuleRadius` | float32 |  |

### CDamageRecord

**Relationships:**

```mermaid
classDiagram
    CDamageRecord --> C_CSPlayerPawn
    CDamageRecord --> CCSPlayerController
    CDamageRecord *-- EKillTypes_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_PlayerDamager` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |
| `m_PlayerRecipient` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |
| `m_hPlayerControllerDamager` | CHandle< [CCSPlayerController](../schemas/client.md#ccsplayercontroller) > |  |
| `m_hPlayerControllerRecipient` | CHandle< [CCSPlayerController](../schemas/client.md#ccsplayercontroller) > |  |
| `m_szPlayerDamagerName` | CUtlString |  |
| `m_szPlayerRecipientName` | CUtlString |  |
| `m_DamagerXuid` | uint64 |  |
| `m_RecipientXuid` | uint64 |  |
| `m_flBulletsDamage` | float32 |  |
| `m_flDamage` | float32 |  |
| `m_flActualHealthRemoved` | float32 |  |
| `m_iNumHits` | int32 |  |
| `m_iLastBulletUpdate` | int32 |  |
| `m_bIsOtherEnemy` | bool |  |
| `m_killType` | [EKillTypes_t](../schemas/!GlobalTypes.md#ekilltypes_t) |  |

### CDestructiblePartsComponent

**Metadata:** `MGetKV3ClassDefaults {
	"m_vecDamageTakenByHitGroup":
	[
	],
	"m_hOwner": null,
	"m_pAnimGraphDestructibleGraphController": null
}`

**Relationships:**

```mermaid
classDiagram
    CDestructiblePartsComponent *-- CNetworkVarChainer
    CDestructiblePartsComponent --> C_BaseModelEntity
    CDestructiblePartsComponent *-- CAnimGraphControllerPtr
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `__m_pChainEntity` | [CNetworkVarChainer](../schemas/entity2.md#cnetworkvarchainer) | `MNotSaved` |
| `m_vecDamageTakenByHitGroup` | CUtlVector< uint16 > |  |
| `m_hOwner` | CHandle< [C_BaseModelEntity](../schemas/client.md#c_basemodelentity) > |  |
| `m_pAnimGraphDestructibleGraphController` | [CAnimGraphControllerPtr](../schemas/server.md#canimgraphcontrollerptr) |  |

### CEconItemAttribute

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iAttributeDefinitionIndex` | uint16 |  |
| `m_flValue` | float32 |  |
| `m_flInitialValue` | float32 |  |
| `m_nRefundableCurrency` | int32 |  |
| `m_bSetBonus` | bool |  |

### CEffectData

**Relationships:**

```mermaid
classDiagram
    CEffectData *-- InfoForResourceTypeIParticleSystemDefinition
    CEffectData *-- AttachmentHandle_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vOrigin` | VectorWS |  |
| `m_vStart` | VectorWS |  |
| `m_vNormal` | Vector |  |
| `m_vAngles` | QAngle |  |
| `m_hEntity` | CEntityHandle |  |
| `m_hOtherEntity` | CEntityHandle |  |
| `m_flScale` | float32 |  |
| `m_flMagnitude` | float32 |  |
| `m_flRadius` | float32 |  |
| `m_nSurfaceProp` | CUtlStringToken |  |
| `m_nEffectIndex` | CWeakHandle< [InfoForResourceTypeIParticleSystemDefinition](../schemas/resourcesystem.md#infoforresourcetypeiparticlesystemdefinition) > |  |
| `m_nDamageType` | uint32 |  |
| `m_nPenetrate` | uint8 |  |
| `m_nMaterial` | uint16 |  |
| `m_nHitBox` | int16 |  |
| `m_nColor` | uint8 |  |
| `m_fFlags` | uint8 |  |
| `m_nAttachmentIndex` | [AttachmentHandle_t](../schemas/modellib.md#attachmenthandle_t) |  |
| `m_nAttachmentName` | CUtlStringToken |  |
| `m_iEffectName` | uint16 |  |

### CEnvCombinedLightProbeVolumeAPI

### CEnvCubemapAPI

### CEnvLightProbeVolumeAPI

### CEnvSkyAPI

### CEnvSoundscape

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [CEnvSoundscapeAlias_snd_soundscape](client.md#cenvsoundscapealias_snd_soundscape), [CEnvSoundscapeProxy](client.md#cenvsoundscapeproxy), [CEnvSoundscapeTriggerable](client.md#cenvsoundscapetriggerable)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- CEnvSoundscape
    CEntityInstance <|-- C_BaseEntity
    CEnvSoundscape <|-- CEnvSoundscapeAlias_snd_soundscape
    CEnvSoundscape <|-- CEnvSoundscapeProxy
    CEnvSoundscape <|-- CEnvSoundscapeTriggerable
    CEnvSoundscape *-- CEntityIOOutput
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_OnPlay` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_flRadius` | float32 |  |
| `m_soundEventName` | CGameSoundEventName |  |
| `m_bOverrideWithEvent` | bool |  |
| `m_soundscapeIndex` | int32 | `MNotSaved` |
| `m_soundscapeEntityListId` | int32 | `MNotSaved` |
| `m_positionNames` | CUtlSymbolLarge[8] |  |
| `m_hProxySoundscape` | CHandle< [CEnvSoundscape](../schemas/client.md#cenvsoundscape) > |  |
| `m_bDisabled` | bool |  |
| `m_soundscapeName` | CUtlSymbolLarge |  |
| `m_soundEventHash` | uint32 | `MNotSaved` |

### CEnvSoundscapeAlias_snd_soundscape

**Inherits from:** [CEnvSoundscape](client.md#cenvsoundscape)

**Relationships:**

```mermaid
classDiagram
    CEnvSoundscape <|-- CEnvSoundscapeAlias_snd_soundscape
    C_BaseEntity <|-- CEnvSoundscape
    CEntityInstance <|-- C_BaseEntity
```

### CEnvSoundscapeProxy

**Inherits from:** [CEnvSoundscape](client.md#cenvsoundscape)

**Derived by:** [CEnvSoundscapeProxyAlias_snd_soundscape_proxy](client.md#cenvsoundscapeproxyalias_snd_soundscape_proxy)

**Relationships:**

```mermaid
classDiagram
    CEnvSoundscape <|-- CEnvSoundscapeProxy
    C_BaseEntity <|-- CEnvSoundscape
    CEntityInstance <|-- C_BaseEntity
    CEnvSoundscapeProxy <|-- CEnvSoundscapeProxyAlias_snd_soundscape_proxy
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_MainSoundscapeName` | CUtlSymbolLarge |  |

### CEnvSoundscapeProxyAlias_snd_soundscape_proxy

**Inherits from:** [CEnvSoundscapeProxy](client.md#cenvsoundscapeproxy)

**Relationships:**

```mermaid
classDiagram
    CEnvSoundscapeProxy <|-- CEnvSoundscapeProxyAlias_snd_soundscape_proxy
    CEnvSoundscape <|-- CEnvSoundscapeProxy
    C_BaseEntity <|-- CEnvSoundscape
    CEntityInstance <|-- C_BaseEntity
```

### CEnvSoundscapeTriggerable

**Inherits from:** [CEnvSoundscape](client.md#cenvsoundscape)

**Derived by:** [CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable](client.md#cenvsoundscapetriggerablealias_snd_soundscape_triggerable)

**Relationships:**

```mermaid
classDiagram
    CEnvSoundscape <|-- CEnvSoundscapeTriggerable
    C_BaseEntity <|-- CEnvSoundscape
    CEntityInstance <|-- C_BaseEntity
    CEnvSoundscapeTriggerable <|-- CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable
```

### CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable

**Inherits from:** [CEnvSoundscapeTriggerable](client.md#cenvsoundscapetriggerable)

**Relationships:**

```mermaid
classDiagram
    CEnvSoundscapeTriggerable <|-- CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable
    CEnvSoundscape <|-- CEnvSoundscapeTriggerable
    C_BaseEntity <|-- CEnvSoundscape
    CEntityInstance <|-- C_BaseEntity
```

### CEnvWindSharedAPI

### CExplosionTypeData

**Metadata:** `MGetKV3ClassDefaults {
	"m_SoundName": "",
	"m_ParticleEffect": "",
	"m_bIsIncindiary": false,
	"m_bHasForces": false,
	"m_DecalType": "Scorch"
}`, `MVDataAssociatedFile scripts/explosion_types.vdata`, `MVDataOverlayType 1`, `MVDataRoot`

**Relationships:**

```mermaid
classDiagram
    CExplosionTypeData *-- InfoForResourceTypeIParticleSystemDefinition
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_SoundName` | CSoundEventName |  |
| `m_ParticleEffect` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeIParticleSystemDefinition](../schemas/resourcesystem.md#infoforresourcetypeiparticlesystemdefinition) > > |  |
| `m_bIsIncindiary` | bool | `MPropertyDescription Whether this explosion relates to fire` |
| `m_bHasForces` | bool | `MPropertyDescription Whether this explosion has explosive forces` |
| `m_DecalType` | CGlobalSymbol | `MPropertyDescription Decal to use when this explosion occurs` |

### CFilterAttributeInt

**Inherits from:** [CBaseFilter](client.md#cbasefilter)

**Relationships:**

```mermaid
classDiagram
    CBaseFilter <|-- CFilterAttributeInt
    CLogicalEntity <|-- CBaseFilter
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_sAttributeName` | CUtlSymbolLarge |  |

### CFilterClass

**Inherits from:** [CBaseFilter](client.md#cbasefilter)

**Relationships:**

```mermaid
classDiagram
    CBaseFilter <|-- CFilterClass
    CLogicalEntity <|-- CBaseFilter
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iFilterClass` | CUtlSymbolLarge |  |

### CFilterLOS

**Inherits from:** [CBaseFilter](client.md#cbasefilter)

**Relationships:**

```mermaid
classDiagram
    CBaseFilter <|-- CFilterLOS
    CLogicalEntity <|-- CBaseFilter
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
```

### CFilterMassGreater

**Inherits from:** [CBaseFilter](client.md#cbasefilter)

**Relationships:**

```mermaid
classDiagram
    CBaseFilter <|-- CFilterMassGreater
    CLogicalEntity <|-- CBaseFilter
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_fFilterMass` | float32 |  |

### CFilterModel

**Inherits from:** [CBaseFilter](client.md#cbasefilter)

**Relationships:**

```mermaid
classDiagram
    CBaseFilter <|-- CFilterModel
    CLogicalEntity <|-- CBaseFilter
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iFilterModel` | CUtlSymbolLarge |  |

### CFilterMultiple

**Inherits from:** [CBaseFilter](client.md#cbasefilter)

**Relationships:**

```mermaid
classDiagram
    CBaseFilter <|-- CFilterMultiple
    CLogicalEntity <|-- CBaseFilter
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
    CFilterMultiple --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nFilterType` | filter_t |  |
| `m_iFilterName` | CUtlSymbolLarge[10] |  |
| `m_hFilter` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) >[10] |  |

### CFilterMultipleAPI

### CFilterName

**Inherits from:** [CBaseFilter](client.md#cbasefilter)

**Relationships:**

```mermaid
classDiagram
    CBaseFilter <|-- CFilterName
    CLogicalEntity <|-- CBaseFilter
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iFilterName` | CUtlSymbolLarge |  |

### CFilterProximity

**Inherits from:** [CBaseFilter](client.md#cbasefilter)

**Relationships:**

```mermaid
classDiagram
    CBaseFilter <|-- CFilterProximity
    CLogicalEntity <|-- CBaseFilter
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flRadius` | float32 |  |

### CFilterTeam

**Inherits from:** [CBaseFilter](client.md#cbasefilter)

**Relationships:**

```mermaid
classDiagram
    CBaseFilter <|-- CFilterTeam
    CLogicalEntity <|-- CBaseFilter
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iFilterTeam` | int32 |  |

### CFlashbangProjectile_API

### CFlashlightEffect

**Relationships:**

```mermaid
classDiagram
    CFlashlightEffect *-- InfoForResourceTypeCTextureBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bIsOn` | bool |  |
| `m_bMuzzleFlashEnabled` | bool |  |
| `m_flMuzzleFlashBrightness` | float32 |  |
| `m_quatMuzzleFlashOrientation` | Quaternion |  |
| `m_vecMuzzleFlashOrigin` | VectorWS |  |
| `m_flFov` | float32 |  |
| `m_flFarZ` | float32 |  |
| `m_flLinearAtten` | float32 |  |
| `m_bCastsShadows` | bool |  |
| `m_flCurrentPullBackDist` | float32 |  |
| `m_FlashlightTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_MuzzleFlashTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_textureName` | char[64] |  |

### CFootstepControl_API

### CFuncRetakeBarrier

**Inherits from:** [C_DynamicProp](client.md#c_dynamicprop)

**Relationships:**

```mermaid
classDiagram
    C_DynamicProp <|-- CFuncRetakeBarrier
    C_BreakableProp <|-- C_DynamicProp
    CBaseProp <|-- C_BreakableProp
    CBaseAnimGraph <|-- CBaseProp
    C_BaseModelEntity <|-- CBaseAnimGraph
```

### CFuncWater

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- CFuncWater
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    CFuncWater *-- CBuoyancyHelper
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_BuoyancyHelper` | [CBuoyancyHelper](../schemas/client.md#cbuoyancyhelper) |  |

### CGameSceneNode

**Derived by:** [CSkeletonInstance](client.md#cskeletoninstance)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CGameSceneNode <|-- CSkeletonInstance
    CGameSceneNode --> CEntityInstance
    CGameSceneNode *-- CGameSceneNodeHandle
    CGameSceneNode *-- CNetworkOriginCellCoordQuantizedVector
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bBoneMergeFlex` | bitfield:1 | `MNotSaved` |
| `m_bDirtyBoneMergeBoneToRoot` | bitfield:1 | `MNotSaved` |
| `m_bDirtyBoneMergeInfo` | bitfield:1 | `MNotSaved` |
| `m_bDirtyHierarchy` | bitfield:1 | `MNotSaved` |
| `m_bNetworkedAnglesChanged` | bitfield:1 | `MNotSaved` |
| `m_bNetworkedPositionChanged` | bitfield:1 | `MNotSaved` |
| `m_bNetworkedScaleChanged` | bitfield:1 | `MNotSaved` |
| `m_bWillBeCallingPostDataUpdate` | bitfield:1 | `MNotSaved` |
| `m_nLatchAbsOrigin` | bitfield:2 | `MNotSaved` |
| `m_nodeToWorld` | CTransformWS | `MNotSaved` |
| `m_pOwner` | [CEntityInstance](../schemas/entity2.md#centityinstance)* | `MNotSaved` |
| `m_pParent` | [CGameSceneNode](../schemas/client.md#cgamescenenode)* | `MNotSaved` |
| `m_pChild` | [CGameSceneNode](../schemas/client.md#cgamescenenode)* | `MNotSaved` |
| `m_pNextSibling` | [CGameSceneNode](../schemas/client.md#cgamescenenode)* | `MNotSaved` |
| `m_hParent` | [CGameSceneNodeHandle](../schemas/client.md#cgamescenenodehandle) |  |
| `m_vecOrigin` | [CNetworkOriginCellCoordQuantizedVector](../schemas/server.md#cnetworkorigincellcoordquantizedvector) |  |
| `m_angRotation` | QAngle |  |
| `m_flScale` | float32 |  |
| `m_vecAbsOrigin` | VectorWS |  |
| `m_angAbsRotation` | QAngle |  |
| `m_flAbsScale` | float32 |  |
| `m_vecWrappedLocalOrigin` | Vector | `MNotSaved` |
| `m_angWrappedLocalRotation` | QAngle | `MNotSaved` |
| `m_flWrappedScale` | float32 | `MNotSaved` |
| `m_nParentAttachmentOrBone` | int16 | `MNotSaved` |
| `m_bDebugAbsOriginChanges` | bool | `MNotSaved` |
| `m_bDormant` | bool |  |
| `m_bForceParentToBeNetworked` | bool |  |
| `m_nHierarchicalDepth` | uint8 | `MNotSaved` |
| `m_nHierarchyType` | uint8 | `MNotSaved` |
| `m_nDoNotSetAnimTimeInInvalidatePhysicsCount` | uint8 | `MNotSaved` |
| `m_name` | CUtlStringToken |  |
| `m_hierarchyAttachName` | CUtlStringToken |  |
| `m_flClientLocalScale` | float32 |  |

### CGameSceneNodeHandle

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CGameSceneNodeHandle",
	"m_hOwner": null,
	"m_name": ""
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hOwner` | CEntityHandle |  |
| `m_name` | CUtlStringToken |  |

### CGlobalLightBase

**Derived by:** [C_GlobalLight](client.md#c_globallight)

**Relationships:**

```mermaid
classDiagram
    CGlobalLightBase <|-- C_GlobalLight
    CGlobalLightBase --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bSpotLight` | bool |  |
| `m_SpotLightOrigin` | VectorWS |  |
| `m_SpotLightAngles` | QAngle |  |
| `m_ShadowDirection` | Vector |  |
| `m_AmbientDirection` | Vector |  |
| `m_SpecularDirection` | Vector |  |
| `m_InspectorSpecularDirection` | Vector |  |
| `m_flSpecularPower` | float32 |  |
| `m_flSpecularIndependence` | float32 |  |
| `m_SpecularColor` | Color |  |
| `m_bStartDisabled` | bool |  |
| `m_bEnabled` | bool |  |
| `m_LightColor` | Color |  |
| `m_AmbientColor1` | Color |  |
| `m_AmbientColor2` | Color |  |
| `m_AmbientColor3` | Color |  |
| `m_flSunDistance` | float32 |  |
| `m_flFOV` | float32 |  |
| `m_flNearZ` | float32 |  |
| `m_flFarZ` | float32 |  |
| `m_bEnableShadows` | bool |  |
| `m_bOldEnableShadows` | bool |  |
| `m_bBackgroundClearNotRequired` | bool |  |
| `m_flCloudScale` | float32 |  |
| `m_flCloud1Speed` | float32 |  |
| `m_flCloud1Direction` | float32 |  |
| `m_flCloud2Speed` | float32 |  |
| `m_flCloud2Direction` | float32 |  |
| `m_flAmbientScale1` | float32 |  |
| `m_flAmbientScale2` | float32 |  |
| `m_flGroundScale` | float32 |  |
| `m_flLightScale` | float32 |  |
| `m_flFoWDarkness` | float32 |  |
| `m_bEnableSeparateSkyboxFog` | bool |  |
| `m_vFowColor` | Vector |  |
| `m_ViewOrigin` | VectorWS |  |
| `m_ViewAngles` | QAngle |  |
| `m_flViewFoV` | float32 |  |
| `m_WorldPoints` | VectorWS[8] |  |
| `m_vFogOffsetLayer0` | Vector2D |  |
| `m_vFogOffsetLayer1` | Vector2D |  |
| `m_hEnvWind` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_hEnvSky` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |

### CGlowProperty

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CGlowProperty",
	"m_iGlowType": 0,
	"m_bEligibleForScreenHighlight": false
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_fGlowColor` | Vector | `MNotSaved` |
| `m_iGlowType` | int32 |  |
| `m_iGlowTeam` | int32 | `MNotSaved` |
| `m_nGlowRange` | int32 | `MNotSaved` |
| `m_nGlowRangeMin` | int32 | `MNotSaved` |
| `m_glowColorOverride` | Color | `MNotSaved` |
| `m_bFlashing` | bool | `MNotSaved` |
| `m_flGlowTime` | float32 | `MNotSaved` |
| `m_flGlowStartTime` | float32 | `MNotSaved` |
| `m_bEligibleForScreenHighlight` | bool |  |
| `m_bGlowing` | bool | `MNotSaved` |

### CGrenadeTracer

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- CGrenadeTracer
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    CGrenadeTracer *-- GrenadeType_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flTracerDuration` | float32 |  |
| `m_nType` | [GrenadeType_t](../schemas/!GlobalTypes.md#grenadetype_t) |  |

### CGrenadeTracer_API

### CHitboxComponent

**Inherits from:** [CEntityComponent](entity2.md#centitycomponent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CHitboxComponent",
	"m_flBoundsExpandRadius": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    CEntityComponent <|-- CHitboxComponent
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flBoundsExpandRadius` | float32 |  |

### CHostageRescueZone

**Inherits from:** [CHostageRescueZoneShim](client.md#chostagerescuezoneshim)

**Relationships:**

```mermaid
classDiagram
    CHostageRescueZoneShim <|-- CHostageRescueZone
    C_BaseTrigger <|-- CHostageRescueZoneShim
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
```

### CHostageRescueZoneShim

**Inherits from:** [C_BaseTrigger](client.md#c_basetrigger)

**Derived by:** [CHostageRescueZone](client.md#chostagerescuezone)

**Relationships:**

```mermaid
classDiagram
    C_BaseTrigger <|-- CHostageRescueZoneShim
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    CHostageRescueZoneShim <|-- CHostageRescueZone
```

### CInfoDynamicShadowHint

**Inherits from:** [C_PointEntity](client.md#c_pointentity)

**Derived by:** [CInfoDynamicShadowHintBox](client.md#cinfodynamicshadowhintbox)

**Relationships:**

```mermaid
classDiagram
    C_PointEntity <|-- CInfoDynamicShadowHint
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
    CInfoDynamicShadowHint <|-- CInfoDynamicShadowHintBox
    CInfoDynamicShadowHint --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bDisabled` | bool |  |
| `m_flRange` | float32 |  |
| `m_nImportance` | int32 |  |
| `m_nLightChoice` | int32 |  |
| `m_hLight` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |

### CInfoDynamicShadowHintBox

**Inherits from:** [CInfoDynamicShadowHint](client.md#cinfodynamicshadowhint)

**Relationships:**

```mermaid
classDiagram
    CInfoDynamicShadowHint <|-- CInfoDynamicShadowHintBox
    C_PointEntity <|-- CInfoDynamicShadowHint
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vBoxMins` | Vector |  |
| `m_vBoxMaxs` | Vector |  |

### CInfoFan

**Inherits from:** [C_PointEntity](client.md#c_pointentity)

**Relationships:**

```mermaid
classDiagram
    C_PointEntity <|-- CInfoFan
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_fFanForceMaxRadius` | float32 |  |
| `m_fFanForceMinRadius` | float32 |  |
| `m_flCurveDistRange` | float32 |  |
| `m_FanForceCurveString` | CUtlSymbolLarge |  |

### CInfoOffscreenPanoramaTexture

**Inherits from:** [C_PointEntity](client.md#c_pointentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_PointEntity <|-- CInfoOffscreenPanoramaTexture
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
    CInfoOffscreenPanoramaTexture --> C_BaseModelEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bDisabled` | bool |  |
| `m_nResolutionX` | int32 |  |
| `m_nResolutionY` | int32 |  |
| `m_szPanelType` | CUtlSymbolLarge |  |
| `m_szLayoutFileName` | CUtlSymbolLarge |  |
| `m_RenderAttrName` | CUtlSymbolLarge |  |
| `m_TargetEntities` | C_NetworkUtlVectorBase< CHandle< [C_BaseModelEntity](../schemas/client.md#c_basemodelentity) > > |  |
| `m_nTargetChangeCount` | int32 |  |
| `m_vecCSSClasses` | C_NetworkUtlVectorBase< CUtlSymbolLarge > |  |
| `m_szTargetsName` | CUtlSymbolLarge |  |
| `m_AdditionalTargetEntities` | CUtlVector< CHandle< [C_BaseModelEntity](../schemas/client.md#c_basemodelentity) > > |  |
| `m_bCheckCSSClasses` | bool | `MNotSaved` |

### CInfoParticleTarget

**Inherits from:** [C_PointEntity](client.md#c_pointentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_PointEntity <|-- CInfoParticleTarget
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
```

### CInfoTarget

**Inherits from:** [C_PointEntity](client.md#c_pointentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_PointEntity <|-- CInfoTarget
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
```

### CInfoWorldLayer

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- CInfoWorldLayer
    CEntityInstance <|-- C_BaseEntity
    CInfoWorldLayer *-- CEntityIOOutput
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_pOutputOnEntitiesSpawned` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_worldName` | CUtlSymbolLarge | `MNotSaved` |
| `m_layerName` | CUtlSymbolLarge | `MNotSaved` |
| `m_bWorldLayerVisible` | bool |  |
| `m_bEntitiesSpawned` | bool |  |
| `m_bCreateAsChildSpawnGroup` | bool |  |
| `m_hLayerSpawnGroup` | uint32 | `MNotSaved` |
| `m_bWorldLayerActuallyVisible` | bool | `MNotSaved` |

### CInterpolatedValue

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flStartTime` | float32 |  |
| `m_flEndTime` | float32 |  |
| `m_flStartValue` | float32 |  |
| `m_flEndValue` | float32 |  |
| `m_nInterpType` | int32 |  |

### CInventoryImageData

**Metadata:** `MGetKV3ClassDefaults {
	"m_nNodeType": "NODE_TYPE_INVALID",
	"name": "",
	"inventory_image_data":
	{
		"map":
		{
			"map_name": "ui/icon_generation_basic_nuke_bombsitea",
			"map_rotation": 0.000000
		},
		"item":
		{
			"position":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"angle":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"pose_sequence": ""
		},
		"camera":
		{
			"angle":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"fov": 45.000000,
			"znear": 4.000000,
			"zfar": 1000.000000,
			"target":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"target_nudge":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"orbit_distance": 0.000000
		},
		"lightsun":
		{
			"color":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"angle":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"brightness": 1.000000
		},
		"lightfill":
		{
			"color":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"angle":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"brightness": 1.000000
		},
		"light0":
		{
			"color":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"angle":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"brightness": 0.000000,
			"orbit_distance": 1.000000
		},
		"light1":
		{
			"color":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"angle":
			[
				0.000000,
				0.000000,
				0.000000
			],
			"brightness": 0.000000,
			"orbit_distance": 1.000000
		},
		"clearcolor":
		{
			"color":
			[
				0.200000,
				0.200000,
				0.200000
			]
		}
	}
}`, `MVDataHideNodeClass`, `MVDataOutlinerDetailExpr name`, `MVDataOutlinerLeafColorFn`, `MVDataOutlinerLeafDetailFn`, `MVDataOutlinerLeafNameFn`, `MVDataOverlayType 1`, `MVDataPostSaveFixupFn`, `MVDataPreLoadFixupFn`, `MVDataPreviewWidget csgo_inv_image_preview`, `MVDataRoot`, `MVDataVirtualNodeFactoryFn`

**Relationships:**

```mermaid
classDiagram
    CInventoryImageData *-- InventoryNodeType_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nNodeType` | [InventoryNodeType_t](../schemas/!GlobalTypes.md#inventorynodetype_t) | `MPropertySuppressField` |
| `name` | CUtlString | `MPropertyFriendlyName Item Name` `MPropertyReadOnly` `MPropertyReadonlyExpr 1` `MPropertySuppressExpr name == ""` |
| `inventory_image_data` | inv_image_data_t | `MPropertyAutoExpandSelf` `MPropertyFriendlyName Inventory Image Data` |

### CLightComponent

**Inherits from:** [CEntityComponent](entity2.md#centitycomponent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CLightComponent",
	"m_Color":
	[
		0,
		0,
		0,
		0
	],
	"m_SecondaryColor":
	[
		0,
		0,
		0,
		0
	],
	"m_flBrightness": 0.000000,
	"m_flBrightnessScale": 1.000000,
	"m_flBrightnessMult": 1.000000,
	"m_flRange": 0.000000,
	"m_flFalloff": 0.000000,
	"m_flAttenuation0": 0.000000,
	"m_flAttenuation1": 0.000000,
	"m_flAttenuation2": 0.000000,
	"m_flTheta": 0.000000,
	"m_flPhi": 0.000000,
	"m_hLightCookie": "",
	"m_nCascades": 0,
	"m_nCastShadows": 0,
	"m_nShadowWidth": 0,
	"m_nShadowHeight": 0,
	"m_bRenderDiffuse": true,
	"m_nRenderSpecular": 1,
	"m_bRenderTransmissive": true,
	"m_flOrthoLightWidth": 0.000000,
	"m_flOrthoLightHeight": 0.000000,
	"m_nStyle": 0,
	"m_Pattern": "",
	"m_nCascadeRenderStaticObjects": -1,
	"m_flShadowCascadeCrossFade": 0.000000,
	"m_flShadowCascadeDistanceFade": 0.000000,
	"m_flShadowCascadeDistance0": 0.000000,
	"m_flShadowCascadeDistance1": 0.000000,
	"m_flShadowCascadeDistance2": 0.000000,
	"m_flShadowCascadeDistance3": 0.000000,
	"m_nShadowCascadeResolution0": 0,
	"m_nShadowCascadeResolution1": 0,
	"m_nShadowCascadeResolution2": 0,
	"m_nShadowCascadeResolution3": 0,
	"m_bUsesBakedShadowing": false,
	"m_nShadowPriority": -1,
	"m_nBakedShadowIndex": -1,
	"m_nLightPathUniqueId": 0,
	"m_nLightMapUniqueId": 0,
	"m_bRenderToCubemaps": true,
	"m_bAllowSSTGeneration": true,
	"m_nDirectLight": 0,
	"m_nBounceLight": 0,
	"m_flBounceScale": 0.000000,
	"m_flFadeMinDist": 0.000000,
	"m_flFadeMaxDist": 0.000000,
	"m_flShadowFadeMinDist": 0.000000,
	"m_flShadowFadeMaxDist": 0.000000,
	"m_bEnabled": false,
	"m_bFlicker": false,
	"m_bPrecomputedFieldsValid": false,
	"m_vPrecomputedBoundsMins":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_vPrecomputedBoundsMaxs":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_vPrecomputedOBBOrigin":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_vPrecomputedOBBAngles":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_vPrecomputedOBBExtent":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"m_flPrecomputedMaxRange": 0.000000,
	"m_nFogLightingMode": 0,
	"m_flFogContributionStength": 1.000000,
	"m_flNearClipPlane": 1.000000,
	"m_SkyColor":
	[
		0,
		0,
		0,
		0
	],
	"m_flSkyIntensity": 0.000000,
	"m_SkyAmbientBounce":
	[
		0,
		0,
		0,
		0
	],
	"m_bUseSecondaryColor": false,
	"m_flLightStyleStartTime": null,
	"m_flCapsuleLength": 0.000000,
	"m_flMinRoughness": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    CEntityComponent <|-- CLightComponent
    CLightComponent *-- CNetworkVarChainer
    CLightComponent *-- InfoForResourceTypeCTextureBase
    CLightComponent *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `__m_pChainEntity` | [CNetworkVarChainer](../schemas/entity2.md#cnetworkvarchainer) | `MNotSaved` |
| `m_Color` | Color |  |
| `m_SecondaryColor` | Color |  |
| `m_flBrightness` | float32 |  |
| `m_flBrightnessScale` | float32 |  |
| `m_flBrightnessMult` | float32 |  |
| `m_flRange` | float32 |  |
| `m_flFalloff` | float32 |  |
| `m_flAttenuation0` | float32 |  |
| `m_flAttenuation1` | float32 |  |
| `m_flAttenuation2` | float32 |  |
| `m_flTheta` | float32 |  |
| `m_flPhi` | float32 |  |
| `m_hLightCookie` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_nCascades` | int32 |  |
| `m_nCastShadows` | int32 |  |
| `m_nShadowWidth` | int32 |  |
| `m_nShadowHeight` | int32 |  |
| `m_bRenderDiffuse` | bool |  |
| `m_nRenderSpecular` | int32 |  |
| `m_bRenderTransmissive` | bool |  |
| `m_flOrthoLightWidth` | float32 |  |
| `m_flOrthoLightHeight` | float32 |  |
| `m_nStyle` | int32 |  |
| `m_Pattern` | CUtlString |  |
| `m_nCascadeRenderStaticObjects` | int32 |  |
| `m_flShadowCascadeCrossFade` | float32 |  |
| `m_flShadowCascadeDistanceFade` | float32 |  |
| `m_flShadowCascadeDistance0` | float32 |  |
| `m_flShadowCascadeDistance1` | float32 |  |
| `m_flShadowCascadeDistance2` | float32 |  |
| `m_flShadowCascadeDistance3` | float32 |  |
| `m_nShadowCascadeResolution0` | int32 |  |
| `m_nShadowCascadeResolution1` | int32 |  |
| `m_nShadowCascadeResolution2` | int32 |  |
| `m_nShadowCascadeResolution3` | int32 |  |
| `m_bUsesBakedShadowing` | bool |  |
| `m_nShadowPriority` | int32 |  |
| `m_nBakedShadowIndex` | int32 |  |
| `m_nLightPathUniqueId` | int32 |  |
| `m_nLightMapUniqueId` | int32 |  |
| `m_bRenderToCubemaps` | bool |  |
| `m_bAllowSSTGeneration` | bool |  |
| `m_nDirectLight` | int32 |  |
| `m_nBounceLight` | int32 |  |
| `m_flBounceScale` | float32 |  |
| `m_flFadeMinDist` | float32 |  |
| `m_flFadeMaxDist` | float32 |  |
| `m_flShadowFadeMinDist` | float32 |  |
| `m_flShadowFadeMaxDist` | float32 |  |
| `m_bEnabled` | bool |  |
| `m_bFlicker` | bool |  |
| `m_bPrecomputedFieldsValid` | bool |  |
| `m_vPrecomputedBoundsMins` | Vector |  |
| `m_vPrecomputedBoundsMaxs` | Vector |  |
| `m_vPrecomputedOBBOrigin` | Vector |  |
| `m_vPrecomputedOBBAngles` | QAngle |  |
| `m_vPrecomputedOBBExtent` | Vector |  |
| `m_flPrecomputedMaxRange` | float32 |  |
| `m_nFogLightingMode` | int32 |  |
| `m_flFogContributionStength` | float32 |  |
| `m_flNearClipPlane` | float32 |  |
| `m_SkyColor` | Color |  |
| `m_flSkyIntensity` | float32 |  |
| `m_SkyAmbientBounce` | Color |  |
| `m_bUseSecondaryColor` | bool |  |
| `m_bMixedShadows` | bool | `MNotSaved` |
| `m_flLightStyleStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flCapsuleLength` | float32 |  |
| `m_flMinRoughness` | float32 |  |

### CLightEntityAPI

### CLogicRelay

**Inherits from:** [CLogicalEntity](client.md#clogicalentity)

**Relationships:**

```mermaid
classDiagram
    CLogicalEntity <|-- CLogicRelay
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
    CLogicRelay *-- CEntityIOOutput
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_OnSpawn` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnTrigger` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_bDisabled` | bool |  |
| `m_bWaitForRefire` | bool |  |
| `m_bTriggerOnce` | bool |  |
| `m_bFastRetrigger` | bool |  |
| `m_bPassthoughCaller` | bool |  |

### CLogicRelayAPI

### CLogicalEntity

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [CBaseFilter](client.md#cbasefilter), [CEnvFade](server.md#cenvfade), [CEnvGlobal](server.md#cenvglobal), [CFuncMoverRouter](server.md#cfuncmoverrouter), [CInfoSpawnGroupLoadUnload](server.md#cinfospawngrouploadunload), [CLogicAchievement](server.md#clogicachievement), [CLogicActivityEvent](server.md#clogicactivityevent), [CLogicAutosave](server.md#clogicautosave), [CLogicBranch](server.md#clogicbranch), [CLogicBranchList](server.md#clogicbranchlist), [CLogicCase](server.md#clogiccase), [CLogicCollisionPair](server.md#clogiccollisionpair), [CLogicCompare](server.md#clogiccompare), [CLogicDistanceAutosave](server.md#clogicdistanceautosave), [CLogicDistanceCheck](server.md#clogicdistancecheck), [CLogicEventListener](server.md#clogiceventlistener), [CLogicGameEvent](server.md#clogicgameevent), [CLogicGameEventListener](server.md#clogicgameeventlistener), [CLogicLineToEntity](server.md#clogiclinetoentity), [CLogicMeasureMovement](server.md#clogicmeasuremovement), [CLogicNavigation](server.md#clogicnavigation), [CLogicPlayerProxy](server.md#clogicplayerproxy), [CLogicRelay](client.md#clogicrelay), [CMapSharedEnvironment](server.md#cmapsharedenvironment), [CMathColorBlend](server.md#cmathcolorblend), [CMathCounter](server.md#cmathcounter), [CMathRemap](server.md#cmathremap), [CMultiLightProxy](server.md#cmultilightproxy), [CMultiSource](server.md#cmultisource), [CPathKeyFrame](server.md#cpathkeyframe), [CPathMoverEntitySpawner](server.md#cpathmoverentityspawner), [CPhysConstraint](server.md#cphysconstraint), [CPhysMotor](server.md#cphysmotor), [CPhysicsEntitySolver](server.md#cphysicsentitysolver), [CPointTemplate](client.md#cpointtemplate), [CSceneListManager](server.md#cscenelistmanager), [CSoundStackSave](server.md#csoundstacksave), [CTestPulseIO](server.md#ctestpulseio), [CTimerEntity](server.md#ctimerentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
    CLogicalEntity <|-- CBaseFilter
    CLogicalEntity <|-- CLogicRelay
    CLogicalEntity <|-- CPointTemplate
    CLogicalEntity <|-- CEnvFade
    CLogicalEntity <|-- CEnvGlobal
    CLogicalEntity <|-- CFuncMoverRouter
    CLogicalEntity <|-- CInfoSpawnGroupLoadUnload
    CLogicalEntity <|-- CLogicAchievement
    CLogicalEntity <|-- CLogicActivityEvent
    CLogicalEntity <|-- CLogicAutosave
    CLogicalEntity <|-- CLogicBranch
    CLogicalEntity <|-- CLogicBranchList
    CLogicalEntity <|-- CLogicCase
    CLogicalEntity <|-- CLogicCollisionPair
    CLogicalEntity <|-- CLogicCompare
    CLogicalEntity <|-- CLogicDistanceAutosave
    CLogicalEntity <|-- CLogicDistanceCheck
    CLogicalEntity <|-- CLogicEventListener
    CLogicalEntity <|-- CLogicGameEvent
    CLogicalEntity <|-- CLogicGameEventListener
    CLogicalEntity <|-- CLogicLineToEntity
    CLogicalEntity <|-- CLogicMeasureMovement
    CLogicalEntity <|-- CLogicNavigation
    CLogicalEntity <|-- CLogicPlayerProxy
    CLogicalEntity <|-- CMapSharedEnvironment
    CLogicalEntity <|-- CMathColorBlend
    CLogicalEntity <|-- CMathCounter
    CLogicalEntity <|-- CMathRemap
    CLogicalEntity <|-- CMultiLightProxy
    CLogicalEntity <|-- CMultiSource
    CLogicalEntity <|-- CPathKeyFrame
    CLogicalEntity <|-- CPathMoverEntitySpawner
    CLogicalEntity <|-- CPhysConstraint
    CLogicalEntity <|-- CPhysMotor
    CLogicalEntity <|-- CPhysicsEntitySolver
    CLogicalEntity <|-- CSceneListManager
    CLogicalEntity <|-- CSoundStackSave
    CLogicalEntity <|-- CTestPulseIO
    CLogicalEntity <|-- CTimerEntity
```

### CMapInfo

**Inherits from:** [C_PointEntity](client.md#c_pointentity)

**Relationships:**

```mermaid
classDiagram
    C_PointEntity <|-- CMapInfo
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iBuyingStatus` | int32 |  |
| `m_flBombRadius` | float32 |  |
| `m_iPetPopulation` | int32 |  |
| `m_bUseNormalSpawnsForDM` | bool |  |
| `m_bDisableAutoGeneratedDMSpawns` | bool |  |
| `m_flBotMaxVisionDistance` | float32 |  |
| `m_iHostageCount` | int32 |  |
| `m_bFadePlayerVisibilityFarZ` | bool |  |
| `m_bRainTraceToSkyEnabled` | bool |  |
| `m_bGPUCullSkybox` | bool |  |
| `m_flEnvRainStrength` | float32 |  |
| `m_flEnvPuddleRippleStrength` | float32 |  |
| `m_flEnvPuddleRippleDirection` | float32 |  |
| `m_flEnvWetnessCoverage` | float32 |  |
| `m_flEnvWetnessDryingAmount` | float32 |  |

### CMapInfo_API

### CModelState

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CModelState *-- InfoForResourceTypeCModel
    CModelState --> IPhysAggregateInstance
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hModel` | CStrongHandle< [InfoForResourceTypeCModel](../schemas/resourcesystem.md#infoforresourcetypecmodel) > |  |
| `m_ModelName` | CUtlSymbolLarge |  |
| `m_pVPhysicsAggregate` | [IPhysAggregateInstance](../schemas/vphysics2.md#iphysaggregateinstance)* | `MPhysPtr` |
| `m_flRootBoneOffset_x` | float32 |  |
| `m_flRootBoneOffset_y` | float32 |  |
| `m_flRootBoneOffset_z` | float32 |  |
| `m_nRootBoneOffsetResetSerialNumber` | uint8 |  |
| `m_bClientClothCreationSuppressed` | bool |  |
| `m_nAnimStateNoInterpSerialNumber` | uint8 |  |
| `m_MeshGroupMask` | uint64 |  |
| `m_nBodyGroupChoices` | C_NetworkUtlVectorBase< int32 > |  |
| `m_nIdealMotionType` | int8 |  |
| `m_nForceLOD` | int8 |  |
| `m_nClothUpdateFlags` | int8 |  |

### CNetworkedSequenceOperation

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CNetworkedSequenceOperation",
	"m_hSequence": -1,
	"m_flPrevCycle": 0.000000,
	"m_flCycle": 0.000000,
	"m_flWeight": 1.000000,
	"m_bSequenceChangeNetworked": false,
	"m_bDiscontinuity": false,
	"m_flPrevCycleFromDiscontinuity": 0.000000,
	"m_flPrevCycleForAnimEventDetection": 0.000000
}`

**Relationships:**

```mermaid
classDiagram
    CNetworkedSequenceOperation *-- HSequence
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hSequence` | [HSequence](../schemas/animationsystem.md#hsequence) |  |
| `m_flPrevCycle` | float32 |  |
| `m_flCycle` | float32 |  |
| `m_flWeight` | CNetworkedQuantizedFloat |  |
| `m_bSequenceChangeNetworked` | bool |  |
| `m_bDiscontinuity` | bool |  |
| `m_flPrevCycleFromDiscontinuity` | float32 |  |
| `m_flPrevCycleForAnimEventDetection` | float32 |  |

### CParticleSystemAPI

### CPathNode

**Inherits from:** [C_PointEntity](client.md#c_pointentity)

**Derived by:** [CMoverPathNode](server.md#cmoverpathnode)

**Relationships:**

```mermaid
classDiagram
    C_PointEntity <|-- CPathNode
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
    CPathNode <|-- CMoverPathNode
    CPathNode --> CPathWithDynamicNodes
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vInTangentLocal` | Vector |  |
| `m_vOutTangentLocal` | Vector |  |
| `m_strParentPathUniqueID` | CUtlString |  |
| `m_strPathNodeParameter` | CUtlString |  |
| `m_xWSPrevParent` | CTransformWS |  |
| `m_hPath` | CHandle< [CPathWithDynamicNodes](../schemas/client.md#cpathwithdynamicnodes) > |  |

### CPathQueryComponent

**Inherits from:** [CEntityComponent](entity2.md#centitycomponent), [CPathQueryUtil](server.md#cpathqueryutil)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CEntityComponent <|-- CPathQueryComponent
```

### CPathSimple

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [CPathWithDynamicNodes](client.md#cpathwithdynamicnodes)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- CPathSimple
    CEntityInstance <|-- C_BaseEntity
    CPathSimple <|-- CPathWithDynamicNodes
    CPathSimple *-- CPathQueryComponent
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_CPathQueryComponent` | [CPathQueryComponent](../schemas/client.md#cpathquerycomponent) |  |
| `m_pathString` | CUtlString |  |
| `m_bClosedLoop` | bool |  |

### CPathSimpleAPI

### CPathWithDynamicNodes

**Inherits from:** [CPathSimple](client.md#cpathsimple)

**Derived by:** [CPathMover](server.md#cpathmover)

**Relationships:**

```mermaid
classDiagram
    CPathSimple <|-- CPathWithDynamicNodes
    C_BaseEntity <|-- CPathSimple
    CEntityInstance <|-- C_BaseEntity
    CPathWithDynamicNodes <|-- CPathMover
    CPathWithDynamicNodes --> CPathNode
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vecPathNodes` | C_NetworkUtlVectorBase< CHandle< [CPathNode](../schemas/client.md#cpathnode) > > |  |
| `m_xInitialPathWorldToLocal` | CTransform |  |

### CPlayerSprayDecalRenderHelper

### CPlayer_AutoaimServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_AutoaimServices
```

### CPlayer_CameraServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Derived by:** [CCSPlayerBase_CameraServices](client.md#ccsplayerbase_cameraservices)

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

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vecCsViewPunchAngle` | QAngle |  |
| `m_nCsViewPunchAngleTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_flCsViewPunchAngleTickRatio` | float32 |  |
| `m_PlayerFog` | [C_fogplayerparams_t](../schemas/client.md#c_fogplayerparams_t) |  |
| `m_hColorCorrectionCtrl` | CHandle< [C_ColorCorrection](../schemas/client.md#c_colorcorrection) > |  |
| `m_hViewEntity` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_hTonemapController` | CHandle< [C_TonemapController2](../schemas/client.md#c_tonemapcontroller2) > |  |
| `m_audio` | audioparams_t |  |
| `m_PostProcessingVolumes` | C_NetworkUtlVectorBase< CHandle< [C_PostProcessingVolume](../schemas/client.md#c_postprocessingvolume) > > |  |
| `m_flOldPlayerZ` | float32 |  |
| `m_flOldPlayerViewOffsetZ` | float32 |  |
| `m_CurrentFog` | fogparams_t |  |
| `m_hOldFogController` | CHandle< [C_FogController](../schemas/client.md#c_fogcontroller) > |  |
| `m_bOverrideFogColor` | bool[5] |  |
| `m_OverrideFogColor` | Color[5] |  |
| `m_bOverrideFogStartEnd` | bool[5] |  |
| `m_fOverrideFogStart` | float32[5] |  |
| `m_fOverrideFogEnd` | float32[5] |  |
| `m_hActivePostProcessingVolume` | CHandle< [C_PostProcessingVolume](../schemas/client.md#c_postprocessingvolume) > |  |
| `m_angDemoViewAngles` | QAngle |  |

### CPlayer_FlashlightServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_FlashlightServices
```

### CPlayer_ItemServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Derived by:** [CCSPlayer_ItemServices](client.md#ccsplayer_itemservices)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_ItemServices
    CPlayer_ItemServices <|-- CCSPlayer_ItemServices
```

### CPlayer_MovementServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Derived by:** [CCSObserver_MovementServices](client.md#ccsobserver_movementservices), [CPlayer_MovementServices_Humanoid](client.md#cplayer_movementservices_humanoid)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_MovementServices
    CPlayer_MovementServices <|-- CCSObserver_MovementServices
    CPlayer_MovementServices <|-- CPlayer_MovementServices_Humanoid
    CPlayer_MovementServices *-- CInButtonState
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nImpulse` | int32 |  |
| `m_nButtons` | [CInButtonState](../schemas/server.md#cinbuttonstate) | `MNotSaved` |
| `m_nQueuedButtonDownMask` | uint64 |  |
| `m_nQueuedButtonChangeMask` | uint64 |  |
| `m_nButtonDoublePressed` | uint64 |  |
| `m_pButtonPressedCmdNumber` | uint32[64] | `MNotSaved` |
| `m_nLastCommandNumberProcessed` | uint32 | `MNotSaved` |
| `m_nToggleButtonDownMask` | uint64 |  |
| `m_flCmdForwardMove` | float32 |  |
| `m_flCmdLeftMove` | float32 |  |
| `m_flCmdUpMove` | float32 |  |
| `m_flMaxspeed` | float32 |  |
| `m_arrForceSubtickMoveWhen` | float32[4] |  |
| `m_flForwardMove` | float32 |  |
| `m_flLeftMove` | float32 |  |
| `m_flUpMove` | float32 |  |
| `m_vecLastMovementImpulses` | Vector |  |
| `m_vecOldViewAngles` | QAngle |  |

### CPlayer_MovementServices_Humanoid

**Inherits from:** [CPlayer_MovementServices](client.md#cplayer_movementservices)

**Derived by:** [CCSPlayer_MovementServices](client.md#ccsplayer_movementservices)

**Relationships:**

```mermaid
classDiagram
    CPlayer_MovementServices <|-- CPlayer_MovementServices_Humanoid
    CPlayerPawnComponent <|-- CPlayer_MovementServices
    CPlayer_MovementServices_Humanoid <|-- CCSPlayer_MovementServices
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flStepSoundTime` | float32 |  |
| `m_flFallVelocity` | float32 |  |
| `m_groundNormal` | Vector | `MNotSaved` |
| `m_flSurfaceFriction` | float32 |  |
| `m_surfaceProps` | CUtlStringToken | `MNotSaved` |
| `m_nStepside` | int32 |  |

### CPlayer_ObserverServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Derived by:** [CCSObserver_ObserverServices](client.md#ccsobserver_observerservices)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_ObserverServices
    CPlayer_ObserverServices <|-- CCSObserver_ObserverServices
    CPlayer_ObserverServices --> C_BaseEntity
    CPlayer_ObserverServices *-- ObserverMode_t
    CPlayer_ObserverServices *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iObserverMode` | uint8 |  |
| `m_hObserverTarget` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_iObserverLastMode` | [ObserverMode_t](../schemas/!GlobalTypes.md#observermode_t) |  |
| `m_bForcedObserverMode` | bool |  |
| `m_flObserverChaseDistance` | float32 | `MNotSaved` |
| `m_flObserverChaseDistanceCalcTime` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |

### CPlayer_UseServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Derived by:** [CCSObserver_UseServices](client.md#ccsobserver_useservices), [CCSPlayer_UseServices](client.md#ccsplayer_useservices)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_UseServices
    CPlayer_UseServices <|-- CCSObserver_UseServices
    CPlayer_UseServices <|-- CCSPlayer_UseServices
```

### CPlayer_WaterServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Derived by:** [CCSPlayer_WaterServices](client.md#ccsplayer_waterservices)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_WaterServices
    CPlayer_WaterServices <|-- CCSPlayer_WaterServices
```

### CPlayer_WeaponServices

**Inherits from:** [CPlayerPawnComponent](server.md#cplayerpawncomponent)

**Derived by:** [CCSPlayer_WeaponServices](client.md#ccsplayer_weaponservices)

**Relationships:**

```mermaid
classDiagram
    CPlayerPawnComponent <|-- CPlayer_WeaponServices
    CPlayer_WeaponServices <|-- CCSPlayer_WeaponServices
    CPlayer_WeaponServices --> C_BasePlayerWeapon
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hMyWeapons` | C_NetworkUtlVectorBase< CHandle< [C_BasePlayerWeapon](../schemas/client.md#c_baseplayerweapon) > > |  |
| `m_hActiveWeapon` | CHandle< [C_BasePlayerWeapon](../schemas/client.md#c_baseplayerweapon) > |  |
| `m_hLastWeapon` | CHandle< [C_BasePlayerWeapon](../schemas/client.md#c_baseplayerweapon) > |  |
| `m_iAmmo` | uint16[32] |  |

### CPointChildModifier

**Inherits from:** [C_PointEntity](client.md#c_pointentity)

**Relationships:**

```mermaid
classDiagram
    C_PointEntity <|-- CPointChildModifier
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bOrphanInsteadOfDeletingChildrenOnRemove` | bool |  |

### CPointOffScreenIndicatorUi

**Inherits from:** [C_PointClientUIWorldPanel](client.md#c_pointclientuiworldpanel)

**Relationships:**

```mermaid
classDiagram
    C_PointClientUIWorldPanel <|-- CPointOffScreenIndicatorUi
    C_BaseClientUIEntity <|-- C_PointClientUIWorldPanel
    C_BaseModelEntity <|-- C_BaseClientUIEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    CPointOffScreenIndicatorUi --> C_PointClientUIWorldPanel
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bBeenEnabled` | bool | `MNotSaved` |
| `m_bHide` | bool | `MNotSaved` |
| `m_flSeenTargetTime` | float32 | `MNotSaved` |
| `m_pTargetPanel` | [C_PointClientUIWorldPanel](../schemas/client.md#c_pointclientuiworldpanel)* | `MNotSaved` |

### CPointOrient

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- CPointOrient
    CEntityInstance <|-- C_BaseEntity
    CPointOrient --> C_BaseEntity
    CPointOrient *-- PointOrientGoalDirectionType_t
    CPointOrient *-- PointOrientConstraint_t
    CPointOrient *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iszSpawnTargetName` | CUtlSymbolLarge |  |
| `m_hTarget` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_bActive` | bool |  |
| `m_nGoalDirection` | [PointOrientGoalDirectionType_t](../schemas/!GlobalTypes.md#pointorientgoaldirectiontype_t) |  |
| `m_nConstraint` | [PointOrientConstraint_t](../schemas/!GlobalTypes.md#pointorientconstraint_t) |  |
| `m_flMaxTurnRate` | float32 |  |
| `m_flLastGameTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |

### CPointTemplate

**Inherits from:** [CLogicalEntity](client.md#clogicalentity)

**Relationships:**

```mermaid
classDiagram
    CLogicalEntity <|-- CPointTemplate
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
    CPointTemplate *-- PointTemplateClientOnlyEntityBehavior_t
    CPointTemplate *-- PointTemplateOwnerSpawnGroupType_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iszWorldName` | CUtlSymbolLarge |  |
| `m_iszSource2EntityLumpName` | CUtlSymbolLarge |  |
| `m_iszEntityFilterName` | CUtlSymbolLarge |  |
| `m_flTimeoutInterval` | float32 |  |
| `m_bAsynchronouslySpawnEntities` | bool |  |
| `m_clientOnlyEntityBehavior` | [PointTemplateClientOnlyEntityBehavior_t](../schemas/!GlobalTypes.md#pointtemplateclientonlyentitybehavior_t) | `MNotSaved` |
| `m_ownerSpawnGroupType` | [PointTemplateOwnerSpawnGroupType_t](../schemas/!GlobalTypes.md#pointtemplateownerspawngrouptype_t) | `MNotSaved` |
| `m_createdSpawnGroupHandles` | CUtlVector< uint32 > |  |
| `m_SpawnedEntityHandles` | CUtlVector< CEntityHandle > |  |
| `m_ScriptSpawnCallback` | HSCRIPT | `MNotSaved` |
| `m_ScriptCallbackScope` | HSCRIPT | `MNotSaved` |
| `m_OnEntitySpawned` | CEntityOutputTemplate< CUtlVector< CEntityHandle > > |  |

### CPointTemplateAPI

### CPointValueRemapperAPI

### CPrecipitationVData

**Inherits from:** [CEntitySubclassVDataBase](server.md#centitysubclassvdatabase)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CPrecipitationVData",
	"m_szParticlePrecipitationEffect": "",
	"m_szParticlePrecipitationPuddleEffect": "",
	"m_szParticlePrecipitationPostEffect": "",
	"m_flInnerDistance": 32.000000,
	"m_nAttachType": "PATTACH_ABSORIGIN_FOLLOW",
	"m_bBatchSameVolumeType": true,
	"m_nRTEnvCP": -1,
	"m_nRTEnvCPComponent": 0,
	"m_szModifier": "",
	"m_nUseSnapshotFromSurfaceGraph": -1,
	"m_snapshotFilter":
	{
		"m_flMaxRadius": 200.000000
	}
}`

**Relationships:**

```mermaid
classDiagram
    CEntitySubclassVDataBase <|-- CPrecipitationVData
    CPrecipitationVData *-- InfoForResourceTypeIParticleSystemDefinition
    CPrecipitationVData *-- ParticleAttachment_t
    CPrecipitationVData *-- PrecipitationFilter_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_szParticlePrecipitationEffect` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeIParticleSystemDefinition](../schemas/resourcesystem.md#infoforresourcetypeiparticlesystemdefinition) > > |  |
| `m_szParticlePrecipitationPuddleEffect` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeIParticleSystemDefinition](../schemas/resourcesystem.md#infoforresourcetypeiparticlesystemdefinition) > > |  |
| `m_szParticlePrecipitationPostEffect` | CResourceNameTyped< CWeakHandle< [InfoForResourceTypeIParticleSystemDefinition](../schemas/resourcesystem.md#infoforresourcetypeiparticlesystemdefinition) > > |  |
| `m_flInnerDistance` | float32 |  |
| `m_nAttachType` | [ParticleAttachment_t](../schemas/!GlobalTypes.md#particleattachment_t) |  |
| `m_bBatchSameVolumeType` | bool |  |
| `m_nRTEnvCP` | int32 |  |
| `m_nRTEnvCPComponent` | int32 |  |
| `m_szModifier` | CUtlString |  |
| `m_nUseSnapshotFromSurfaceGraph` | int32 | `MPropertyDescription If set, we will populate a snapshot from the surface graph` |
| `m_snapshotFilter` | [PrecipitationFilter_t](../schemas/server.md#precipitationfilter_t) |  |

### CPropDataComponent

**Inherits from:** [CEntityComponent](entity2.md#centitycomponent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CPropDataComponent",
	"m_flDmgModBullet": 1.000000,
	"m_flDmgModClub": 1.000000,
	"m_flDmgModExplosive": 1.000000,
	"m_flDmgModFire": 1.000000,
	"m_iszPhysicsDamageTableName": "",
	"m_iszBasePropData": "",
	"m_nInteractions": 0,
	"m_bSpawnMotionDisabled": false,
	"m_nDisableTakePhysicsDamageSpawnFlag": 0,
	"m_nMotionDisabledSpawnFlag": 0
}`

**Relationships:**

```mermaid
classDiagram
    CEntityComponent <|-- CPropDataComponent
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flDmgModBullet` | float32 |  |
| `m_flDmgModClub` | float32 |  |
| `m_flDmgModExplosive` | float32 |  |
| `m_flDmgModFire` | float32 |  |
| `m_iszPhysicsDamageTableName` | CUtlSymbolLarge |  |
| `m_iszBasePropData` | CUtlSymbolLarge |  |
| `m_nInteractions` | int32 |  |
| `m_bSpawnMotionDisabled` | bool |  |
| `m_nDisableTakePhysicsDamageSpawnFlag` | int32 |  |
| `m_nMotionDisabledSpawnFlag` | int32 |  |

### CPulseCell_LerpCameraSettings

**Inherits from:** [CPulseCell_BaseLerp](pulse_runtime_lib.md#cpulsecell_baselerp)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CPulseCell_LerpCameraSettings",
	"m_nEditorNodeID": -1,
	"m_BaseFlow_OnAfterCancel":
	{
		"m_SourceOutflowName": "",
		"m_nDestChunk": -1,
		"m_nInstruction": -1
	},
	"m_BaseFlow_WhileActive":
	{
		"m_SourceOutflowName": "",
		"m_nDestChunk": -1,
		"m_nInstruction": -1
	},
	"m_WakeResume":
	{
		"m_SourceOutflowName": "",
		"m_nDestChunk": -1,
		"m_nInstruction": -1
	},
	"m_flSeconds": 4.000000,
	"m_Start":
	{
		"m_flNearBlurryDistance": -1.000000,
		"m_flNearCrispDistance": -1.000000,
		"m_flFarCrispDistance": -1.000000,
		"m_flFarBlurryDistance": -1.000000
	},
	"m_End":
	{
		"m_flNearBlurryDistance": -1.000000,
		"m_flNearCrispDistance": -1.000000,
		"m_flFarCrispDistance": -1.000000,
		"m_flFarBlurryDistance": -1.000000
	}
}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseLerp <|-- CPulseCell_LerpCameraSettings
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_BaseLerp
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_LerpCameraSettings *-- PointCameraSettings_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flSeconds` | float32 |  |
| `m_Start` | [PointCameraSettings_t](../schemas/server.md#pointcamerasettings_t) |  |
| `m_End` | [PointCameraSettings_t](../schemas/server.md#pointcamerasettings_t) |  |

### CPulseCell_LerpCameraSettings::CursorState_t

**Inherits from:** [CPulseCell_BaseLerp::CursorState_t](pulse_runtime_lib.md#cpulsecell_baselerpcursorstate_t)

**Metadata:** `MGetKV3ClassDefaults {
	"m_StartTime": null,
	"m_EndTime": null,
	"m_hCamera": null,
	"m_OverlaidStart":
	{
		"m_flNearBlurryDistance": -1.000000,
		"m_flNearCrispDistance": -1.000000,
		"m_flFarCrispDistance": -1.000000,
		"m_flFarBlurryDistance": -1.000000
	},
	"m_OverlaidEnd":
	{
		"m_flNearBlurryDistance": -1.000000,
		"m_flNearCrispDistance": -1.000000,
		"m_flFarCrispDistance": -1.000000,
		"m_flFarBlurryDistance": -1.000000
	}
}`

**Relationships:**

```mermaid
classDiagram
    "CPulseCell_BaseLerp::CursorState_t" <|-- "CPulseCell_LerpCameraSettings::CursorState_t"
    "CPulseCell_LerpCameraSettings::CursorState_t" --> C_PointCamera
    "CPulseCell_LerpCameraSettings::CursorState_t" *-- PointCameraSettings_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hCamera` | CHandle< [C_PointCamera](../schemas/client.md#c_pointcamera) > |  |
| `m_OverlaidStart` | [PointCameraSettings_t](../schemas/server.md#pointcamerasettings_t) |  |
| `m_OverlaidEnd` | [PointCameraSettings_t](../schemas/server.md#pointcamerasettings_t) |  |

### CPulseCell_PlaySequence

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CPulseCell_PlaySequence",
	"m_nEditorNodeID": -1,
	"m_BaseFlow_OnAfterCancel":
	{
		"m_SourceOutflowName": "",
		"m_nDestChunk": -1,
		"m_nInstruction": -1
	},
	"m_BaseFlow_WhileActive":
	{
		"m_SourceOutflowName": "",
		"m_nDestChunk": -1,
		"m_nInstruction": -1
	},
	"m_SequenceName": "",
	"m_PulseAnimEvents":
	{
		"m_Outflows":
		[
		]
	},
	"m_OnFinished":
	{
		"m_SourceOutflowName": "",
		"m_nDestChunk": -1,
		"m_nInstruction": -1
	}
}`, `MPropertyDescription Play the specified animation sequence on a NON-ANIMGRAPH entity, and wait for it to complete.`, `MPropertyFriendlyName Play Sequence`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_PlaySequence
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_PlaySequence *-- PulseNodeDynamicOutflows_t
    CPulseCell_PlaySequence *-- CPulse_ResumePoint
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_SequenceName` | CUtlString | `MPropertyAttributeSuggestionName pulse_model_sequence_name` |
| `m_PulseAnimEvents` | [PulseNodeDynamicOutflows_t](../schemas/pulse_runtime_lib.md#pulsenodedynamicoutflows_t) |  |
| `m_OnFinished` | [CPulse_ResumePoint](../schemas/pulse_runtime_lib.md#cpulse_resumepoint) |  |

### CPulseCell_PlaySequence::CursorState_t

**Metadata:** `MGetKV3ClassDefaults {
	"m_hTarget": null
}`

**Relationships:**

```mermaid
classDiagram
    "CPulseCell_PlaySequence::CursorState_t" --> CBaseAnimGraph
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hTarget` | CHandle< [CBaseAnimGraph](../schemas/client.md#cbaseanimgraph) > |  |

### CPulseCell_Step_EntFire

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CPulseCell_Step_EntFire",
	"m_nEditorNodeID": -1,
	"m_Input": ""
}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Step_EntFire
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Input` | CUtlString |  |

### CPulseGameBlackboard

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- CPulseGameBlackboard
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_strGraphName` | CUtlString |  |
| `m_strStateBlob` | CUtlString |  |

### CRagdollManager

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- CRagdollManager
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iCurrentMaxRagdollCount` | int8 |  |

### CRenderComponent

**Inherits from:** [CEntityComponent](entity2.md#centitycomponent)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CRenderComponent"
}`

**Relationships:**

```mermaid
classDiagram
    CEntityComponent <|-- CRenderComponent
    CRenderComponent *-- CNetworkVarChainer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `__m_pChainEntity` | [CNetworkVarChainer](../schemas/entity2.md#cnetworkvarchainer) | `MNotSaved` |
| `m_bIsRenderingWithViewModels` | bool | `MNotSaved` |
| `m_nSplitscreenFlags` | uint32 | `MNotSaved` |
| `m_bEnableRendering` | bool | `MNotSaved` |
| `m_bInterpolationReadyToDraw` | bool | `MNotSaved` |

### CSMatchStats_t

**Inherits from:** [CSPerRoundStats_t](client.md#csperroundstats_t)

**Relationships:**

```mermaid
classDiagram
    CSPerRoundStats_t <|-- CSMatchStats_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iEnemy5Ks` | int32 |  |
| `m_iEnemy4Ks` | int32 |  |
| `m_iEnemy3Ks` | int32 |  |
| `m_iEnemyKnifeKills` | int32 |  |
| `m_iEnemyTaserKills` | int32 |  |

### CSPerRoundStats_t

**Derived by:** [CSMatchStats_t](client.md#csmatchstats_t)

**Relationships:**

```mermaid
classDiagram
    CSPerRoundStats_t <|-- CSMatchStats_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iKills` | int32 |  |
| `m_iDeaths` | int32 |  |
| `m_iAssists` | int32 |  |
| `m_iDamage` | int32 |  |
| `m_iEquipmentValue` | int32 |  |
| `m_iMoneySaved` | int32 |  |
| `m_iKillReward` | int32 |  |
| `m_iLiveTime` | int32 |  |
| `m_iHeadShotKills` | int32 |  |
| `m_iObjective` | int32 |  |
| `m_iCashEarned` | int32 |  |
| `m_iUtilityDamage` | int32 |  |
| `m_iEnemiesFlashed` | int32 |  |

### CServerOnlyModelEntity

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Derived by:** [CCSPlace](server.md#ccsplace), [CFogVolume](server.md#cfogvolume)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- CServerOnlyModelEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    CServerOnlyModelEntity <|-- CCSPlace
    CServerOnlyModelEntity <|-- CFogVolume
```

### CSkeletonInstance

**Inherits from:** [CGameSceneNode](client.md#cgamescenenode)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CGameSceneNode <|-- CSkeletonInstance
    CSkeletonInstance *-- CModelState
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_modelState` | [CModelState](../schemas/client.md#cmodelstate) |  |
| `m_bUseParentRenderBounds` | bool | `MNotSaved` |
| `m_bDisableSolidCollisionsForHierarchy` | bool |  |
| `m_bDirtyMotionType` | bool | `MNotSaved` |
| `m_bIsGeneratingLatchedParentSpaceState` | bool | `MNotSaved` |
| `m_materialGroup` | CUtlStringToken |  |
| `m_nHitboxSet` | uint8 |  |

### CSkyboxReference

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- CSkyboxReference
    CEntityInstance <|-- C_BaseEntity
    CSkyboxReference --> C_SkyCamera
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_worldGroupId` | WorldGroupId_t |  |
| `m_hSkyCamera` | CHandle< [C_SkyCamera](../schemas/client.md#c_skycamera) > | `MNotSaved` |

### CSoundOpvarSetBoxEntity

**Inherits from:** [C_SoundOpvarSetPointEntity](client.md#c_soundopvarsetpointentity)

**Derived by:** [CSoundOpvarSetAABBEntity](server.md#csoundopvarsetaabbentity), [C_SoundOpvarSetAABBEntity](client.md#c_soundopvarsetaabbentity)

**Relationships:**

```mermaid
classDiagram
    C_SoundOpvarSetPointEntity <|-- CSoundOpvarSetBoxEntity
    C_SoundOpvarSetPointBase <|-- C_SoundOpvarSetPointEntity
    C_BaseEntity <|-- C_SoundOpvarSetPointBase
    CEntityInstance <|-- C_BaseEntity
    CSoundOpvarSetBoxEntity <|-- C_SoundOpvarSetAABBEntity
    CSoundOpvarSetBoxEntity <|-- CSoundOpvarSetAABBEntity
```

### CSpriteOriented

**Inherits from:** [C_Sprite](client.md#c_sprite)

**Relationships:**

```mermaid
classDiagram
    C_Sprite <|-- CSpriteOriented
    C_BaseModelEntity <|-- C_Sprite
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### CTakeDamageResultAPI

### CTimeline

**Inherits from:** [IntervalTimer](client.md#intervaltimer)

**Metadata:** `MGetKV3ClassDefaults null`

**Relationships:**

```mermaid
classDiagram
    IntervalTimer <|-- CTimeline
    CTimeline *-- TimelineCompression_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flValues` | float32[64] |  |
| `m_nValueCounts` | int32[64] |  |
| `m_nBucketCount` | int32 |  |
| `m_flInterval` | float32 |  |
| `m_flFinalValue` | float32 |  |
| `m_nCompressionType` | [TimelineCompression_t](../schemas/!GlobalTypes.md#timelinecompression_t) |  |
| `m_bStopped` | bool |  |

### CTriggerFan

**Inherits from:** [C_BaseTrigger](client.md#c_basetrigger)

**Relationships:**

```mermaid
classDiagram
    C_BaseTrigger <|-- CTriggerFan
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    CTriggerFan --> CInfoFan
    CTriggerFan *-- CountdownTimer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vFanOriginOffset` | Vector |  |
| `m_vDirection` | Vector |  |
| `m_bPushTowardsInfoTarget` | bool |  |
| `m_bPushAwayFromInfoTarget` | bool |  |
| `m_qNoiseDelta` | Quaternion |  |
| `m_hInfoFan` | CHandle< [CInfoFan](../schemas/client.md#cinfofan) > |  |
| `m_flForce` | float32 |  |
| `m_bFalloff` | bool |  |
| `m_RampTimer` | [CountdownTimer](../schemas/client.md#countdowntimer) |  |

### CWaterSplasher

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- CWaterSplasher
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_AK47

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_AK47
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_AttributeContainer

**Inherits from:** [CAttributeManager](client.md#cattributemanager)

**Relationships:**

```mermaid
classDiagram
    CAttributeManager <|-- C_AttributeContainer
    C_AttributeContainer *-- C_EconItemView
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Item` | [C_EconItemView](../schemas/client.md#c_econitemview) |  |
| `m_iExternalItemProviderRegisteredToken` | int32 |  |
| `m_ullRegisteredAsItemID` | uint64 |  |

### C_BarnLight

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Derived by:** [C_OmniLight](client.md#c_omnilight), [C_RectLight](client.md#c_rectlight)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_BarnLight
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BarnLight <|-- C_OmniLight
    C_BarnLight <|-- C_RectLight
    C_BarnLight *-- GameTime_t
    C_BarnLight --> C_BaseModelEntity
    C_BarnLight *-- CEntityIOOutput
    C_BarnLight *-- InfoForResourceTypeCTextureBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bEnabled` | bool |  |
| `m_nColorMode` | int32 |  |
| `m_Color` | Color |  |
| `m_flColorTemperature` | float32 |  |
| `m_flBrightness` | float32 |  |
| `m_flBrightnessScale` | float32 |  |
| `m_nDirectLight` | int32 |  |
| `m_nBakedShadowIndex` | int32 |  |
| `m_nLightPathUniqueId` | int32 |  |
| `m_nLightMapUniqueId` | int32 |  |
| `m_nLuminaireShape` | int32 |  |
| `m_flLuminaireSize` | float32 |  |
| `m_flLuminaireAnisotropy` | float32 |  |
| `m_LightStyleString` | CUtlString |  |
| `m_flLightStyleStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_QueuedLightStyleStrings` | C_NetworkUtlVectorBase< CUtlString > |  |
| `m_LightStyleEvents` | C_NetworkUtlVectorBase< CUtlString > |  |
| `m_LightStyleTargets` | C_NetworkUtlVectorBase< CHandle< [C_BaseModelEntity](../schemas/client.md#c_basemodelentity) > > |  |
| `m_StyleEvent` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput)[4] |  |
| `m_hLightCookie` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_flShape` | float32 |  |
| `m_flSoftX` | float32 |  |
| `m_flSoftY` | float32 |  |
| `m_flSkirt` | float32 |  |
| `m_flSkirtNear` | float32 |  |
| `m_vSizeParams` | Vector |  |
| `m_flRange` | float32 |  |
| `m_vShear` | Vector |  |
| `m_nBakeSpecularToCubemaps` | int32 |  |
| `m_vBakeSpecularToCubemapsSize` | Vector |  |
| `m_flBakeSpecularToCubemapsScale` | float32 |  |
| `m_nCastShadows` | int32 |  |
| `m_nShadowMapSize` | int32 |  |
| `m_nShadowPriority` | int32 |  |
| `m_bContactShadow` | bool |  |
| `m_bForceShadowsEnabled` | bool |  |
| `m_nBounceLight` | int32 |  |
| `m_flBounceScale` | float32 |  |
| `m_flMinRoughness` | float32 |  |
| `m_vAlternateColor` | Vector |  |
| `m_fAlternateColorBrightness` | float32 |  |
| `m_nFog` | int32 |  |
| `m_flFogStrength` | float32 |  |
| `m_nFogShadows` | int32 |  |
| `m_flFogScale` | float32 |  |
| `m_flFadeSizeStart` | float32 |  |
| `m_flFadeSizeEnd` | float32 |  |
| `m_flShadowFadeSizeStart` | float32 |  |
| `m_flShadowFadeSizeEnd` | float32 |  |
| `m_bPrecomputedFieldsValid` | bool |  |
| `m_vPrecomputedBoundsMins` | Vector |  |
| `m_vPrecomputedBoundsMaxs` | Vector |  |
| `m_vPrecomputedOBBOrigin` | Vector |  |
| `m_vPrecomputedOBBAngles` | QAngle |  |
| `m_vPrecomputedOBBExtent` | Vector |  |
| `m_nPrecomputedSubFrusta` | int32 |  |
| `m_vPrecomputedOBBOrigin0` | Vector |  |
| `m_vPrecomputedOBBAngles0` | QAngle |  |
| `m_vPrecomputedOBBExtent0` | Vector |  |
| `m_vPrecomputedOBBOrigin1` | Vector |  |
| `m_vPrecomputedOBBAngles1` | QAngle |  |
| `m_vPrecomputedOBBExtent1` | Vector |  |
| `m_vPrecomputedOBBOrigin2` | Vector |  |
| `m_vPrecomputedOBBAngles2` | QAngle |  |
| `m_vPrecomputedOBBExtent2` | Vector |  |
| `m_vPrecomputedOBBOrigin3` | Vector |  |
| `m_vPrecomputedOBBAngles3` | QAngle |  |
| `m_vPrecomputedOBBExtent3` | Vector |  |
| `m_vPrecomputedOBBOrigin4` | Vector |  |
| `m_vPrecomputedOBBAngles4` | QAngle |  |
| `m_vPrecomputedOBBExtent4` | Vector |  |
| `m_vPrecomputedOBBOrigin5` | Vector |  |
| `m_vPrecomputedOBBAngles5` | QAngle |  |
| `m_vPrecomputedOBBExtent5` | Vector |  |
| `m_bInitialBoneSetup` | bool | `MNotSaved` |
| `m_VisClusters` | C_NetworkUtlVectorBase< uint16 > |  |

### C_BaseButton

**Inherits from:** [C_BaseToggle](client.md#c_basetoggle)

**Relationships:**

```mermaid
classDiagram
    C_BaseToggle <|-- C_BaseButton
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BaseButton --> C_BaseModelEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_glowEntity` | CHandle< [C_BaseModelEntity](../schemas/client.md#c_basemodelentity) > |  |
| `m_usable` | bool |  |
| `m_szDisplayText` | CUtlSymbolLarge |  |

### C_BaseCSGrenade

**Inherits from:** [C_CSWeaponBase](client.md#c_csweaponbase)

**Derived by:** [C_DecoyGrenade](client.md#c_decoygrenade), [C_Flashbang](client.md#c_flashbang), [C_HEGrenade](client.md#c_hegrenade), [C_MolotovGrenade](client.md#c_molotovgrenade), [C_SmokeGrenade](client.md#c_smokegrenade)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBase <|-- C_BaseCSGrenade
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseCSGrenade <|-- C_DecoyGrenade
    C_BaseCSGrenade <|-- C_Flashbang
    C_BaseCSGrenade <|-- C_HEGrenade
    C_BaseCSGrenade <|-- C_MolotovGrenade
    C_BaseCSGrenade <|-- C_SmokeGrenade
    C_BaseCSGrenade *-- GameTime_t
    C_BaseCSGrenade *-- GameTick_t
    C_BaseCSGrenade --> C_CSWeaponBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bClientPredictDelete` | bool |  |
| `m_bRedraw` | bool |  |
| `m_bIsHeldByPlayer` | bool |  |
| `m_bPinPulled` | bool |  |
| `m_bJumpThrow` | bool |  |
| `m_bThrowAnimating` | bool |  |
| `m_fThrowTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flThrowStrength` | float32 |  |
| `m_fDropTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_fPinPullTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bJustPulledPin` | bool |  |
| `m_nNextHoldTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_flNextHoldFrac` | float32 |  |
| `m_hSwitchToWeaponAfterThrow` | CHandle< [C_CSWeaponBase](../schemas/client.md#c_csweaponbase) > |  |

### C_BaseCSGrenadeProjectile

**Inherits from:** [C_BaseGrenade](client.md#c_basegrenade)

**Derived by:** [C_DecoyProjectile](client.md#c_decoyprojectile), [C_FlashbangProjectile](client.md#c_flashbangprojectile), [C_HEGrenadeProjectile](client.md#c_hegrenadeprojectile), [C_MolotovProjectile](client.md#c_molotovprojectile), [C_SmokeGrenadeProjectile](client.md#c_smokegrenadeprojectile)

**Relationships:**

```mermaid
classDiagram
    C_BaseGrenade <|-- C_BaseCSGrenadeProjectile
    CBaseAnimGraph <|-- C_BaseGrenade
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BaseCSGrenadeProjectile <|-- C_DecoyProjectile
    C_BaseCSGrenadeProjectile <|-- C_FlashbangProjectile
    C_BaseCSGrenadeProjectile <|-- C_HEGrenadeProjectile
    C_BaseCSGrenadeProjectile <|-- C_MolotovProjectile
    C_BaseCSGrenadeProjectile <|-- C_SmokeGrenadeProjectile
    C_BaseCSGrenadeProjectile *-- InfoForResourceTypeIParticleSystemDefinition
    C_BaseCSGrenadeProjectile *-- GameTime_t
    C_BaseCSGrenadeProjectile *-- ParticleIndex_t
    C_BaseCSGrenadeProjectile *-- InfoForResourceTypeIParticleSnapshot
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vInitialPosition` | VectorWS |  |
| `m_vInitialVelocity` | Vector |  |
| `m_nBounces` | int32 |  |
| `m_nExplodeEffectIndex` | CStrongHandle< [InfoForResourceTypeIParticleSystemDefinition](../schemas/resourcesystem.md#infoforresourcetypeiparticlesystemdefinition) > |  |
| `m_nExplodeEffectTickBegin` | int32 |  |
| `m_vecExplodeEffectOrigin` | VectorWS |  |
| `m_flSpawnTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `vecLastTrailLinePos` | Vector |  |
| `flNextTrailLineTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bExplodeEffectBegan` | bool |  |
| `m_bCanCreateGrenadeTrail` | bool |  |
| `m_nSnapshotTrajectoryEffectIndex` | [ParticleIndex_t](../schemas/server.md#particleindex_t) |  |
| `m_hSnapshotTrajectoryParticleSnapshot` | CStrongHandle< [InfoForResourceTypeIParticleSnapshot](../schemas/resourcesystem.md#infoforresourcetypeiparticlesnapshot) > |  |
| `m_arrTrajectoryTrailPoints` | CUtlVector< Vector > |  |
| `m_arrTrajectoryTrailPointCreationTimes` | CUtlVector< float32 > |  |
| `m_flTrajectoryTrailEffectCreationTime` | float32 |  |

### C_BaseClientUIEntity

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Derived by:** [C_PointClientUIDialog](client.md#c_pointclientuidialog), [C_PointClientUIHUD](client.md#c_pointclientuihud), [C_PointClientUIWorldPanel](client.md#c_pointclientuiworldpanel)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_BaseClientUIEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BaseClientUIEntity <|-- C_PointClientUIDialog
    C_BaseClientUIEntity <|-- C_PointClientUIHUD
    C_BaseClientUIEntity <|-- C_PointClientUIWorldPanel
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bEnabled` | bool |  |
| `m_DialogXMLName` | CUtlSymbolLarge |  |
| `m_PanelClassName` | CUtlSymbolLarge |  |
| `m_PanelID` | CUtlSymbolLarge |  |

### C_BaseCombatCharacter

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Derived by:** [C_BasePlayerPawn](client.md#c_baseplayerpawn), [C_Hostage](client.md#c_hostage), [C_NetTestBaseCombatCharacter](client.md#c_nettestbasecombatcharacter)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_BaseCombatCharacter
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BaseCombatCharacter <|-- C_BasePlayerPawn
    C_BaseCombatCharacter <|-- C_Hostage
    C_BaseCombatCharacter <|-- C_NetTestBaseCombatCharacter
    C_BaseCombatCharacter --> C_EconWearable
    C_BaseCombatCharacter *-- AttachmentHandle_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hMyWearables` | C_NetworkUtlVectorBase< CHandle< [C_EconWearable](../schemas/client.md#c_econwearable) > > | `MNotSaved` |
| `m_leftFootAttachment` | [AttachmentHandle_t](../schemas/modellib.md#attachmenthandle_t) | `MNotSaved` |
| `m_rightFootAttachment` | [AttachmentHandle_t](../schemas/modellib.md#attachmenthandle_t) | `MNotSaved` |
| `m_nWaterWakeMode` | [C_BaseCombatCharacter](../schemas/client.md#c_basecombatcharacter)::WaterWakeMode_t | `MNotSaved` |
| `m_flWaterWorldZ` | float32 | `MNotSaved` |
| `m_flWaterNextTraceTime` | float32 | `MNotSaved` |

### C_BaseCombatCharacter::WaterWakeMode_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `WATER_WAKE_NONE` | 0 |  |
| `WATER_WAKE_IDLE` | 1 |  |
| `WATER_WAKE_WALKING` | 2 |  |
| `WATER_WAKE_RUNNING` | 3 |  |
| `WATER_WAKE_WATER_OVERHEAD` | 4 |  |

### C_BaseDoor

**Inherits from:** [C_BaseToggle](client.md#c_basetoggle)

**Relationships:**

```mermaid
classDiagram
    C_BaseToggle <|-- C_BaseDoor
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bIsUsable` | bool | `MNotSaved` |

### C_BaseEntity

**Inherits from:** [CEntityInstance](entity2.md#centityinstance)

**Derived by:** [CBasePlayerController](client.md#cbaseplayercontroller), [CCS_PortraitWorldCallbackHandler](client.md#ccs_portraitworldcallbackhandler), [CCitadelSoundOpvarSetOBB](client.md#ccitadelsoundopvarsetobb), [CEnvSoundscape](client.md#cenvsoundscape), [CInfoWorldLayer](client.md#cinfoworldlayer), [CLogicalEntity](client.md#clogicalentity), [CPathSimple](client.md#cpathsimple), [CPointOrient](client.md#cpointorient), [CPulseGameBlackboard](client.md#cpulsegameblackboard), [CRagdollManager](client.md#cragdollmanager), [CSkyboxReference](client.md#cskyboxreference), [C_BaseModelEntity](client.md#c_basemodelentity), [C_CSGO_EndOfMatchLineupEndpoint](client.md#c_csgo_endofmatchlineupendpoint), [C_CSGO_MapPreviewCameraPath](client.md#c_csgo_mappreviewcamerapath), [C_CSGO_MapPreviewCameraPathNode](client.md#c_csgo_mappreviewcamerapathnode), [C_CSGO_TeamPreviewCharacterPosition](client.md#c_csgo_teampreviewcharacterposition), [C_CSMinimapBoundary](client.md#c_csminimapboundary), [C_CSPetPlacement](client.md#c_cspetplacement), [C_CSPlayerResource](client.md#c_csplayerresource), [C_ColorCorrection](client.md#c_colorcorrection), [C_CsmFovOverride](client.md#c_csmfovoverride), [C_EntityFlame](client.md#c_entityflame), [C_EnvCombinedLightProbeVolume](client.md#c_envcombinedlightprobevolume), [C_EnvCubemap](client.md#c_envcubemap), [C_EnvCubemapFog](client.md#c_envcubemapfog), [C_EnvDetailController](client.md#c_envdetailcontroller), [C_EnvLightProbeVolume](client.md#c_envlightprobevolume), [C_EnvVolumetricFogController](client.md#c_envvolumetricfogcontroller), [C_EnvVolumetricFogVolume](client.md#c_envvolumetricfogvolume), [C_EnvWind](client.md#c_envwind), [C_EnvWindClientside](client.md#c_envwindclientside), [C_EnvWindController](client.md#c_envwindcontroller), [C_EnvWindVolume](client.md#c_envwindvolume), [C_FogController](client.md#c_fogcontroller), [C_GameRulesProxy](client.md#c_gamerulesproxy), [C_GlobalLight](client.md#c_globallight), [C_GradientFog](client.md#c_gradientfog), [C_HandleTest](client.md#c_handletest), [C_InfoLadderDismount](client.md#c_infoladderdismount), [C_InfoVisibilityBox](client.md#c_infovisibilitybox), [C_MapVetoPickController](client.md#c_mapvetopickcontroller), [C_PathParticleRope](client.md#c_pathparticlerope), [C_PlayerPing](client.md#c_playerping), [C_PlayerVisibility](client.md#c_playervisibility), [C_PointCamera](client.md#c_pointcamera), [C_PointEntity](client.md#c_pointentity), [C_PointValueRemapper](client.md#c_pointvalueremapper), [C_PortraitWorldCallbackHandler](client.md#c_portraitworldcallbackhandler), [C_SkyCamera](client.md#c_skycamera), [C_SoundAreaEntityBase](client.md#c_soundareaentitybase), [C_SoundEventEntity](client.md#c_soundevententity), [C_SoundOpvarSetPointBase](client.md#c_soundopvarsetpointbase), [C_Team](client.md#c_team), [C_TintController](client.md#c_tintcontroller), [C_TonemapController2](client.md#c_tonemapcontroller2), [C_VoteController](client.md#c_votecontroller)

**Relationships:**

```mermaid
classDiagram
    CEntityInstance <|-- C_BaseEntity
    C_BaseEntity <|-- CBasePlayerController
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

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_CBodyComponent` | [CBodyComponent](../schemas/client.md#cbodycomponent)* |  |
| `m_NetworkTransmitComponent` | [CNetworkTransmitComponent](../schemas/server.md#cnetworktransmitcomponent) | `MNotSaved` |
| `m_nLastThinkTick` | [GameTick_t](../schemas/entity2.md#gametick_t) | `MNotSaved` |
| `m_pGameSceneNode` | [CGameSceneNode](../schemas/client.md#cgamescenenode)* | `MNotSaved` |
| `m_pRenderComponent` | [CRenderComponent](../schemas/client.md#crendercomponent)* | `MNotSaved` |
| `m_pCollision` | [CCollisionProperty](../schemas/client.md#ccollisionproperty)* | `MNotSaved` |
| `m_iMaxHealth` | int32 | `MNotSaved` |
| `m_iHealth` | int32 |  |
| `m_flDamageAccumulator` | float32 | `MNotSaved` |
| `m_lifeState` | uint8 | `MNotSaved` |
| `m_bTakesDamage` | bool | `MNotSaved` |
| `m_nTakeDamageFlags` | [TakeDamageFlags_t](../schemas/!GlobalTypes.md#takedamageflags_t) | `MNotSaved` |
| `m_nPlatformType` | [EntityPlatformTypes_t](../schemas/!GlobalTypes.md#entityplatformtypes_t) |  |
| `m_ubInterpolationFrame` | uint8 | `MNotSaved` |
| `m_hSceneObjectController` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_nNoInterpolationTick` | int32 | `MNotSaved` |
| `m_nVisibilityNoInterpolationTick` | int32 | `MNotSaved` |
| `m_flProxyRandomValue` | float32 | `MNotSaved` |
| `m_iEFlags` | int32 | `MNotSaved` |
| `m_nWaterType` | uint8 | `MNotSaved` |
| `m_bInterpolateEvenWithNoModel` | bool | `MNotSaved` |
| `m_bPredictionEligible` | bool | `MNotSaved` |
| `m_bApplyLayerMatchIDToModel` | bool | `MNotSaved` |
| `m_tokLayerMatchID` | CUtlStringToken | `MNotSaved` |
| `m_nSubclassID` | CUtlStringToken |  |
| `m_nSimulationTick` | int32 | `MNotSaved` |
| `m_iCurrentThinkContext` | int32 | `MNotSaved` |
| `m_aThinkFunctions` | CUtlVector< thinkfunc_t > | `MNotSaved` |
| `m_bDisabledContextThinks` | bool |  |
| `m_flAnimTime` | float32 | `MNotSaved` |
| `m_flSimulationTime` | float32 | `MNotSaved` |
| `m_nSceneObjectOverrideFlags` | uint8 |  |
| `m_bHasSuccessfullyInterpolated` | bool | `MNotSaved` |
| `m_bHasAddedVarsToInterpolation` | bool | `MNotSaved` |
| `m_bRenderEvenWhenNotSuccessfullyInterpolated` | bool | `MNotSaved` |
| `m_nInterpolationLatchDirtyFlags` | int32[2] | `MNotSaved` |
| `m_ListEntry` | uint16[11] | `MNotSaved` |
| `m_flCreateTime` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `m_EntClientFlags` | uint16 | `MNotSaved` |
| `m_bClientSideRagdoll` | bool | `MNotSaved` |
| `m_iTeamNum` | uint8 | `MNotSaved` |
| `m_spawnflags` | uint32 |  |
| `m_nNextThinkTick` | [GameTick_t](../schemas/entity2.md#gametick_t) | `MNotSaved` |
| `m_fFlags` | uint32 | `MSaveBehavior` |
| `m_vecAbsVelocity` | Vector | `MNotSaved` |
| `m_vecServerVelocity` | [CNetworkVelocityVector](../schemas/server.md#cnetworkvelocityvector) | `MNotSaved` |
| `m_vecVelocity` | [CNetworkVelocityVector](../schemas/server.md#cnetworkvelocityvector) |  |
| `m_vecBaseVelocity` | Vector | `MNotSaved` |
| `m_hEffectEntity` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > | `MNotSaved` |
| `m_hOwnerEntity` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_MoveCollide` | [MoveCollide_t](../schemas/!GlobalTypes.md#movecollide_t) | `MNotSaved` |
| `m_MoveType` | [MoveType_t](../schemas/!GlobalTypes.md#movetype_t) |  |
| `m_nActualMoveType` | [MoveType_t](../schemas/!GlobalTypes.md#movetype_t) |  |
| `m_flWaterLevel` | float32 | `MNotSaved` |
| `m_fEffects` | uint32 | `MNotSaved` |
| `m_hGroundEntity` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > | `MNotSaved` |
| `m_nGroundBodyIndex` | int32 | `MNotSaved` |
| `m_flFriction` | float32 | `MNotSaved` |
| `m_flElasticity` | float32 | `MNotSaved` |
| `m_flGravityScale` | float32 | `MNotSaved` |
| `m_flTimeScale` | float32 | `MNotSaved` |
| `m_bAnimatedEveryTick` | bool | `MNotSaved` |
| `m_bGravityDisabled` | bool |  |
| `m_flNavIgnoreUntilTime` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `m_hThink` | uint16 | `MNotSaved` |
| `m_fBBoxVisFlags` | uint8 | `MNotSaved` |
| `m_flActualGravityScale` | float32 |  |
| `m_bGravityActuallyDisabled` | bool |  |
| `m_bPredictable` | bool | `MNotSaved` |
| `m_bRenderWithViewModels` | bool |  |
| `m_nFirstPredictableCommand` | int32 | `MNotSaved` |
| `m_nLastPredictableCommand` | int32 | `MNotSaved` |
| `m_hOldMoveParent` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > | `MNotSaved` |
| `m_Particles` | [CParticleProperty](../schemas/particleslib.md#cparticleproperty) | `MNotSaved` |
| `m_vecAngVelocity` | QAngle |  |
| `m_DataChangeEventRef` | int32 | `MNotSaved` |
| `m_dependencies` | CUtlVector< CEntityHandle > | `MNotSaved` |
| `m_nCreationTick` | int32 | `MNotSaved` |
| `m_bAnimTimeChanged` | bool | `MNotSaved` |
| `m_bSimulationTimeChanged` | bool | `MNotSaved` |
| `m_sUniqueHammerID` | CUtlString | `MNotSaved` |
| `m_nBloodType` | [BloodType](../schemas/!GlobalTypes.md#bloodtype) |  |

### C_BaseEntityAPI

### C_BaseGrenade

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Derived by:** [C_BaseCSGrenadeProjectile](client.md#c_basecsgrenadeprojectile)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_BaseGrenade
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BaseGrenade <|-- C_BaseCSGrenadeProjectile
    C_BaseGrenade *-- GameTime_t
    C_BaseGrenade --> C_CSPlayerPawn
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bHasWarnedAI` | bool |  |
| `m_bIsSmokeGrenade` | bool |  |
| `m_bIsLive` | bool |  |
| `m_DmgRadius` | float32 |  |
| `m_flDetonateTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flWarnAITime` | float32 |  |
| `m_flDamage` | float32 |  |
| `m_iszBounceSound` | CUtlSymbolLarge |  |
| `m_ExplosionSound` | CUtlString |  |
| `m_hThrower` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |
| `m_flNextAttack` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_hOriginalThrower` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |

### C_BaseModelEntity

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [CBaseAnimGraph](client.md#cbaseanimgraph), [CCashStack](client.md#ccashstack), [CFuncWater](client.md#cfuncwater), [CGrenadeTracer](client.md#cgrenadetracer), [CServerOnlyModelEntity](client.md#cserveronlymodelentity), [CWaterSplasher](client.md#cwatersplasher), [C_BarnLight](client.md#c_barnlight), [C_BaseClientUIEntity](client.md#c_baseclientuientity), [C_BaseToggle](client.md#c_basetoggle), [C_Beam](client.md#c_beam), [C_Breakable](client.md#c_breakable), [C_DynamicLight](client.md#c_dynamiclight), [C_EntityDissolve](client.md#c_entitydissolve), [C_EnvDecal](client.md#c_envdecal), [C_EnvSky](client.md#c_envsky), [C_FuncBrush](client.md#c_funcbrush), [C_FuncConveyor](client.md#c_funcconveyor), [C_FuncLadder](client.md#c_funcladder), [C_FuncRotating](client.md#c_funcrotating), [C_FuncTrackTrain](client.md#c_functracktrain), [C_Inferno](client.md#c_inferno), [C_LightEntity](client.md#c_lightentity), [C_ModelPointEntity](client.md#c_modelpointentity), [C_ParticleSystem](client.md#c_particlesystem), [C_PrecipitationBlocker](client.md#c_precipitationblocker), [C_RopeKeyframe](client.md#c_ropekeyframe), [C_ShatterGlassShardPhysics](client.md#c_shatterglassshardphysics), [C_SpotlightEnd](client.md#c_spotlightend), [C_Sprite](client.md#c_sprite), [C_TextureBasedAnimatable](client.md#c_texturebasedanimatable), [C_TriggerVolume](client.md#c_triggervolume), [C_World](client.md#c_world)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseModelEntity <|-- CCashStack
    C_BaseModelEntity <|-- CFuncWater
    C_BaseModelEntity <|-- CGrenadeTracer
    C_BaseModelEntity <|-- CServerOnlyModelEntity
    C_BaseModelEntity <|-- CWaterSplasher
    C_BaseModelEntity <|-- C_BarnLight
    C_BaseModelEntity <|-- C_BaseClientUIEntity
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseModelEntity <|-- C_Beam
    C_BaseModelEntity <|-- C_Breakable
    C_BaseModelEntity <|-- C_DynamicLight
    C_BaseModelEntity <|-- C_EntityDissolve
    C_BaseModelEntity <|-- C_EnvDecal
    C_BaseModelEntity <|-- C_EnvSky
    C_BaseModelEntity <|-- C_FuncBrush
    C_BaseModelEntity <|-- C_FuncConveyor
    C_BaseModelEntity <|-- C_FuncLadder
    C_BaseModelEntity <|-- C_FuncRotating
    C_BaseModelEntity <|-- C_FuncTrackTrain
    C_BaseModelEntity <|-- C_Inferno
    C_BaseModelEntity <|-- C_LightEntity
    C_BaseModelEntity <|-- C_ModelPointEntity
    C_BaseModelEntity <|-- C_ParticleSystem
    C_BaseModelEntity <|-- C_PrecipitationBlocker
    C_BaseModelEntity <|-- C_RopeKeyframe
    C_BaseModelEntity <|-- C_ShatterGlassShardPhysics
    C_BaseModelEntity <|-- C_SpotlightEnd
    C_BaseModelEntity <|-- C_Sprite
    C_BaseModelEntity <|-- C_TextureBasedAnimatable
    C_BaseModelEntity <|-- C_TriggerVolume
    C_BaseModelEntity <|-- C_World
    C_BaseModelEntity --> CRenderComponent
    C_BaseModelEntity *-- CHitboxComponent
    C_BaseModelEntity --> CChoreoComponent
    C_BaseModelEntity *-- HitGroup_t
    C_BaseModelEntity --> CDestructiblePartsComponent
    C_BaseModelEntity *-- RenderMode_t
    C_BaseModelEntity *-- RenderFx_t
    C_BaseModelEntity *-- EntityRenderAttribute_t
    C_BaseModelEntity *-- CCollisionProperty
    C_BaseModelEntity *-- CGlowProperty
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_CRenderComponent` | [CRenderComponent](../schemas/client.md#crendercomponent)* | `MNotSaved` |
| `m_CHitboxComponent` | [CHitboxComponent](../schemas/client.md#chitboxcomponent) |  |
| `m_pChoreoComponent` | [CChoreoComponent](../schemas/client.md#cchoreocomponent)* |  |
| `m_nDestructiblePartInitialStateDestructed0` | [HitGroup_t](../schemas/!GlobalTypes.md#hitgroup_t) |  |
| `m_nDestructiblePartInitialStateDestructed1` | [HitGroup_t](../schemas/!GlobalTypes.md#hitgroup_t) |  |
| `m_nDestructiblePartInitialStateDestructed2` | [HitGroup_t](../schemas/!GlobalTypes.md#hitgroup_t) |  |
| `m_nDestructiblePartInitialStateDestructed3` | [HitGroup_t](../schemas/!GlobalTypes.md#hitgroup_t) |  |
| `m_nDestructiblePartInitialStateDestructed4` | [HitGroup_t](../schemas/!GlobalTypes.md#hitgroup_t) |  |
| `m_nDestructiblePartInitialStateDestructed0_PartIndex` | int32 |  |
| `m_nDestructiblePartInitialStateDestructed1_PartIndex` | int32 |  |
| `m_nDestructiblePartInitialStateDestructed2_PartIndex` | int32 |  |
| `m_nDestructiblePartInitialStateDestructed3_PartIndex` | int32 |  |
| `m_nDestructiblePartInitialStateDestructed4_PartIndex` | int32 |  |
| `m_bDestructiblePartInitialStateDestructed0_GenerateBreakpieces` | bool |  |
| `m_bDestructiblePartInitialStateDestructed1_GenerateBreakpieces` | bool |  |
| `m_bDestructiblePartInitialStateDestructed2_GenerateBreakpieces` | bool |  |
| `m_bDestructiblePartInitialStateDestructed3_GenerateBreakpieces` | bool |  |
| `m_bDestructiblePartInitialStateDestructed4_GenerateBreakpieces` | bool |  |
| `m_pDestructiblePartsSystemComponent` | [CDestructiblePartsComponent](../schemas/client.md#cdestructiblepartscomponent)* |  |
| `m_bInitModelEffects` | bool | `MNotSaved` |
| `m_bDoingModelEffects` | bool | `MNotSaved` |
| `m_iOldHealth` | int32 | `MNotSaved` |
| `m_nRenderMode` | [RenderMode_t](../schemas/!GlobalTypes.md#rendermode_t) |  |
| `m_nRenderFX` | [RenderFx_t](../schemas/!GlobalTypes.md#renderfx_t) |  |
| `m_bAllowFadeInView` | bool |  |
| `m_clrRender` | Color |  |
| `m_vecRenderAttributes` | C_UtlVectorEmbeddedNetworkVar< [EntityRenderAttribute_t](../schemas/client.md#entityrenderattribute_t) > |  |
| `m_bRenderToCubemaps` | bool |  |
| `m_bNoInterpolate` | bool |  |
| `m_Collision` | [CCollisionProperty](../schemas/client.md#ccollisionproperty) |  |
| `m_Glow` | [CGlowProperty](../schemas/client.md#cglowproperty) |  |
| `m_flGlowBackfaceMult` | float32 |  |
| `m_fadeMinDist` | float32 |  |
| `m_fadeMaxDist` | float32 |  |
| `m_flFadeScale` | float32 |  |
| `m_flShadowStrength` | float32 |  |
| `m_nObjectCulling` | uint8 |  |
| `m_nRequiredDecalRtEncoding` | [DecalRtEncoding_t](../schemas/!GlobalTypes.md#decalrtencoding_t) |  |
| `m_bodyGroupChoices` | CUtlOrderedMap< CGlobalSymbol, int32 > |  |
| `m_vecViewOffset` | [CNetworkViewOffsetVector](../schemas/server.md#cnetworkviewoffsetvector) |  |
| `m_pClientAlphaProperty` | [CClientAlphaProperty](../schemas/client.md#cclientalphaproperty)* | `MNotSaved` |
| `m_ClientOverrideTint` | Color | `MNotSaved` |
| `m_bUseClientOverrideTint` | bool | `MNotSaved` |
| `m_bvDisabledHitGroups` | uint32[1] | `MKV3TransferSaveOpsForField GetHitgroupDisableListSaveRestoreOps` |

### C_BaseModelEntity::Emphasized_Phoneme

**Metadata:** `MGetKV3ClassDefaults {
	"m_sClassName": "",
	"m_flAmount": 0.000000,
	"m_bRequired": false,
	"m_bBasechecked": false,
	"m_bValid": false
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_sClassName` | CUtlString |  |
| `m_flAmount` | float32 |  |
| `m_bRequired` | bool |  |
| `m_bBasechecked` | bool |  |
| `m_bValid` | bool |  |

### C_BasePlayerPawn

**Inherits from:** [C_BaseCombatCharacter](client.md#c_basecombatcharacter)

**Derived by:** [C_CSPlayerPawnBase](client.md#c_csplayerpawnbase)

**Relationships:**

```mermaid
classDiagram
    C_BaseCombatCharacter <|-- C_BasePlayerPawn
    CBaseAnimGraph <|-- C_BaseCombatCharacter
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BasePlayerPawn <|-- C_CSPlayerPawnBase
    C_BasePlayerPawn --> CPlayer_WeaponServices
    C_BasePlayerPawn --> CPlayer_ItemServices
    C_BasePlayerPawn --> CPlayer_AutoaimServices
    C_BasePlayerPawn --> CPlayer_ObserverServices
    C_BasePlayerPawn --> CPlayer_WaterServices
    C_BasePlayerPawn --> CPlayer_UseServices
    C_BasePlayerPawn --> CPlayer_FlashlightServices
    C_BasePlayerPawn --> CPlayer_CameraServices
    C_BasePlayerPawn --> CPlayer_MovementServices
    C_BasePlayerPawn *-- ViewAngleServerChange_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_pWeaponServices` | [CPlayer_WeaponServices](../schemas/client.md#cplayer_weaponservices)* |  |
| `m_pItemServices` | [CPlayer_ItemServices](../schemas/client.md#cplayer_itemservices)* |  |
| `m_pAutoaimServices` | [CPlayer_AutoaimServices](../schemas/client.md#cplayer_autoaimservices)* |  |
| `m_pObserverServices` | [CPlayer_ObserverServices](../schemas/client.md#cplayer_observerservices)* |  |
| `m_pWaterServices` | [CPlayer_WaterServices](../schemas/client.md#cplayer_waterservices)* |  |
| `m_pUseServices` | [CPlayer_UseServices](../schemas/client.md#cplayer_useservices)* |  |
| `m_pFlashlightServices` | [CPlayer_FlashlightServices](../schemas/client.md#cplayer_flashlightservices)* |  |
| `m_pCameraServices` | [CPlayer_CameraServices](../schemas/client.md#cplayer_cameraservices)* |  |
| `m_pMovementServices` | [CPlayer_MovementServices](../schemas/client.md#cplayer_movementservices)* |  |
| `m_ServerViewAngleChanges` | C_UtlVectorEmbeddedNetworkVar< [ViewAngleServerChange_t](../schemas/client.md#viewangleserverchange_t) > | `MNotSaved` |
| `v_angle` | QAngle |  |
| `v_anglePrevious` | QAngle |  |
| `m_iHideHUD` | uint32 |  |
| `m_skybox3d` | sky3dparams_t |  |
| `m_flDeathTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_vecPredictionError` | Vector | `MNotSaved` |
| `m_flPredictionErrorTime` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `m_vecLastCameraSetupLocalOrigin` | Vector | `MNotSaved` |
| `m_flLastCameraSetupTime` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `m_flFOVSensitivityAdjust` | float32 | `MNotSaved` |
| `m_flMouseSensitivity` | float32 | `MNotSaved` |
| `m_vOldOrigin` | Vector | `MNotSaved` |
| `m_flOldSimulationTime` | float32 | `MNotSaved` |
| `m_nLastExecutedCommandNumber` | int32 | `MNotSaved` |
| `m_nLastExecutedCommandTick` | int32 | `MNotSaved` |
| `m_hController` | CHandle< [CBasePlayerController](../schemas/client.md#cbaseplayercontroller) > |  |
| `m_hDefaultController` | CHandle< [CBasePlayerController](../schemas/client.md#cbaseplayercontroller) > |  |
| `m_bIsSwappingToPredictableController` | bool | `MNotSaved` |

### C_BasePlayerWeapon

**Inherits from:** [C_EconEntity](client.md#c_econentity)

**Derived by:** [C_CSWeaponBase](client.md#c_csweaponbase)

**Relationships:**

```mermaid
classDiagram
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_BasePlayerWeapon *-- GameTick_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nNextPrimaryAttackTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_flNextPrimaryAttackTickRatio` | float32 |  |
| `m_nNextSecondaryAttackTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_flNextSecondaryAttackTickRatio` | float32 |  |
| `m_iClip1` | int32 |  |
| `m_iClip2` | int32 |  |
| `m_pReserveAmmo` | int32[2] |  |

### C_BasePropDoor

**Inherits from:** [C_DynamicProp](client.md#c_dynamicprop)

**Derived by:** [C_PropDoorRotating](client.md#c_propdoorrotating)

**Relationships:**

```mermaid
classDiagram
    C_DynamicProp <|-- C_BasePropDoor
    C_BreakableProp <|-- C_DynamicProp
    CBaseProp <|-- C_BreakableProp
    CBaseAnimGraph <|-- CBaseProp
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BasePropDoor <|-- C_PropDoorRotating
    C_BasePropDoor *-- DoorState_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_eDoorState` | [DoorState_t](../schemas/!GlobalTypes.md#doorstate_t) | `MNotSaved` |
| `m_modelChanged` | bool | `MNotSaved` |
| `m_bLocked` | bool | `MNotSaved` |
| `m_bNoNPCs` | bool | `MNotSaved` |
| `m_closedPosition` | VectorWS | `MNotSaved` |
| `m_closedAngles` | QAngle | `MNotSaved` |
| `m_hMaster` | CHandle< [C_BasePropDoor](../schemas/client.md#c_basepropdoor) > | `MNotSaved` |
| `m_vWhereToSetLightingOrigin` | VectorWS | `MNotSaved` |

### C_BaseToggle

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Derived by:** [C_BaseButton](client.md#c_basebutton), [C_BaseDoor](client.md#c_basedoor), [C_BaseTrigger](client.md#c_basetrigger), [C_FuncMoveLinear](client.md#c_funcmovelinear), [C_FuncMover](client.md#c_funcmover)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BaseToggle <|-- C_BaseButton
    C_BaseToggle <|-- C_BaseDoor
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseToggle <|-- C_FuncMoveLinear
    C_BaseToggle <|-- C_FuncMover
```

### C_BaseTrigger

**Inherits from:** [C_BaseToggle](client.md#c_basetoggle)

**Derived by:** [CBombTarget](client.md#cbombtarget), [CHostageRescueZoneShim](client.md#chostagerescuezoneshim), [CTriggerFan](client.md#ctriggerfan), [C_ColorCorrectionVolume](client.md#c_colorcorrectionvolume), [C_FootstepControl](client.md#c_footstepcontrol), [C_PostProcessingVolume](client.md#c_postprocessingvolume), [C_Precipitation](client.md#c_precipitation), [C_TriggerBuoyancy](client.md#c_triggerbuoyancy), [C_TriggerLerpObject](client.md#c_triggerlerpobject), [C_TriggerMultiple](client.md#c_triggermultiple), [C_TriggerPhysics](client.md#c_triggerphysics)

**Relationships:**

```mermaid
classDiagram
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BaseTrigger <|-- CBombTarget
    C_BaseTrigger <|-- CHostageRescueZoneShim
    C_BaseTrigger <|-- CTriggerFan
    C_BaseTrigger <|-- C_ColorCorrectionVolume
    C_BaseTrigger <|-- C_FootstepControl
    C_BaseTrigger <|-- C_PostProcessingVolume
    C_BaseTrigger <|-- C_Precipitation
    C_BaseTrigger <|-- C_TriggerBuoyancy
    C_BaseTrigger <|-- C_TriggerLerpObject
    C_BaseTrigger <|-- C_TriggerMultiple
    C_BaseTrigger <|-- C_TriggerPhysics
    C_BaseTrigger *-- CEntityIOOutput
    C_BaseTrigger --> C_BaseEntity
    C_BaseTrigger --> CBaseFilter
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_OnStartTouch` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnStartTouchAll` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnEndTouch` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnEndTouchAll` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnTouching` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnTouchingEachEntity` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnNotTouching` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnTouchingChanged` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_hTouchingEntities` | CUtlVector< CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > > |  |
| `m_iFilterName` | CUtlSymbolLarge |  |
| `m_hFilter` | CHandle< [CBaseFilter](../schemas/client.md#cbasefilter) > |  |
| `m_bDisabled` | bool |  |

### C_Beam

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_Beam
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_Beam *-- GameTime_t
    C_Beam *-- InfoForResourceTypeIMaterial2
    C_Beam *-- BeamType_t
    C_Beam --> C_BaseEntity
    C_Beam *-- AttachmentHandle_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flFrameRate` | float32 |  |
| `m_flHDRColorScale` | float32 |  |
| `m_flFireTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flDamage` | float32 |  |
| `m_nNumBeamEnts` | uint8 |  |
| `m_queryHandleHalo` | int32 | `MNotSaved` |
| `m_hBaseMaterial` | CStrongHandle< [InfoForResourceTypeIMaterial2](../schemas/resourcesystem.md#infoforresourcetypeimaterial2) > |  |
| `m_nHaloIndex` | CStrongHandle< [InfoForResourceTypeIMaterial2](../schemas/resourcesystem.md#infoforresourcetypeimaterial2) > |  |
| `m_nBeamType` | [BeamType_t](../schemas/!GlobalTypes.md#beamtype_t) |  |
| `m_nBeamFlags` | uint32 |  |
| `m_hAttachEntity` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) >[10] |  |
| `m_nAttachIndex` | [AttachmentHandle_t](../schemas/modellib.md#attachmenthandle_t)[10] |  |
| `m_fWidth` | float32 |  |
| `m_fEndWidth` | float32 |  |
| `m_fFadeLength` | float32 |  |
| `m_fHaloScale` | float32 |  |
| `m_fAmplitude` | float32 |  |
| `m_fStartFrame` | float32 |  |
| `m_fSpeed` | float32 |  |
| `m_flFrame` | float32 |  |
| `m_bTurnedOff` | bool |  |
| `m_vecEndPos` | VectorWS |  |
| `m_hEndEntity` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |

### C_Breakable

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Derived by:** [C_PhysBox](client.md#c_physbox)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_Breakable
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_Breakable <|-- C_PhysBox
```

### C_BreakableProp

**Inherits from:** [CBaseProp](client.md#cbaseprop)

**Derived by:** [C_DynamicProp](client.md#c_dynamicprop), [C_PhysPropClientside](client.md#c_physpropclientside), [C_PhysicsProp](client.md#c_physicsprop)

**Relationships:**

```mermaid
classDiagram
    CBaseProp <|-- C_BreakableProp
    CBaseAnimGraph <|-- CBaseProp
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BreakableProp <|-- C_DynamicProp
    C_BreakableProp <|-- C_PhysPropClientside
    C_BreakableProp <|-- C_PhysicsProp
    C_BreakableProp *-- CPropDataComponent
    C_BreakableProp *-- CEntityIOOutput
    C_BreakableProp --> C_BaseEntity
    C_BreakableProp *-- PerformanceMode_t
    C_BreakableProp *-- GameTime_t
    C_BreakableProp *-- BreakableContentsType_t
    C_BreakableProp --> C_BasePlayerPawn
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_CPropDataComponent` | [CPropDataComponent](../schemas/client.md#cpropdatacomponent) |  |
| `m_OnStartDeath` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnBreak` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnHealthChanged` | CEntityOutputTemplate< float32 > |  |
| `m_OnTakeDamage` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_impactEnergyScale` | float32 |  |
| `m_iMinHealthDmg` | int32 |  |
| `m_flPressureDelay` | float32 |  |
| `m_flDefBurstScale` | float32 |  |
| `m_vDefBurstOffset` | Vector |  |
| `m_hBreaker` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_PerformanceMode` | [PerformanceMode_t](../schemas/!GlobalTypes.md#performancemode_t) |  |
| `m_flPreventDamageBeforeTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_BreakableContentsType` | [BreakableContentsType_t](../schemas/!GlobalTypes.md#breakablecontentstype_t) |  |
| `m_strBreakableContentsPropGroupOverride` | CUtlString |  |
| `m_strBreakableContentsParticleOverride` | CUtlString |  |
| `m_bHasBreakPiecesOrCommands` | bool |  |
| `m_explodeDamage` | float32 |  |
| `m_explodeRadius` | float32 |  |
| `m_sExplosionType` | CGlobalSymbol |  |
| `m_explosionDelay` | float32 |  |
| `m_explosionBuildupSound` | CUtlSymbolLarge |  |
| `m_explosionCustomEffect` | CUtlSymbolLarge |  |
| `m_explosionCustomSound` | CUtlSymbolLarge |  |
| `m_explosionModifier` | CUtlSymbolLarge |  |
| `m_hPhysicsAttacker` | CHandle< [C_BasePlayerPawn](../schemas/client.md#c_baseplayerpawn) > |  |
| `m_flLastPhysicsInfluenceTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flDefaultFadeScale` | float32 |  |
| `m_hLastAttacker` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |

### C_BulletHitModel

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_BulletHitModel
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_BulletHitModel --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_matLocal` | matrix3x4_t |  |
| `m_iBoneIndex` | int32 |  |
| `m_hPlayerParent` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_bIsHit` | bool |  |
| `m_flTimeCreated` | float32 |  |
| `m_vecStartPos` | VectorWS |  |

### C_C4

**Inherits from:** [C_CSWeaponBase](client.md#c_csweaponbase)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBase <|-- C_C4
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_C4 *-- ParticleIndex_t
    C_C4 *-- C4LightEffect_t
    C_C4 *-- GameTime_t
    C_C4 *-- EntitySpottedState_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_activeLightParticleIndex` | [ParticleIndex_t](../schemas/server.md#particleindex_t) |  |
| `m_eActiveLightEffect` | [C4LightEffect_t](../schemas/!GlobalTypes.md#c4lighteffect_t) |  |
| `m_bStartedArming` | bool |  |
| `m_fArmedTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bBombPlacedAnimation` | bool |  |
| `m_bIsPlantingViaUse` | bool |  |
| `m_entitySpottedState` | [EntitySpottedState_t](../schemas/client.md#entityspottedstate_t) |  |
| `m_nSpotRules` | int32 |  |
| `m_bPlayedArmingBeeps` | bool[7] |  |
| `m_bBombPlanted` | bool |  |

### C_CS2HudModelAddon

**Inherits from:** [C_LateUpdatedAnimating](client.md#c_lateupdatedanimating)

**Relationships:**

```mermaid
classDiagram
    C_LateUpdatedAnimating <|-- C_CS2HudModelAddon
    CBaseAnimGraph <|-- C_LateUpdatedAnimating
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_CS2HudModelArms

**Inherits from:** [C_CS2HudModelBase](client.md#c_cs2hudmodelbase)

**Relationships:**

```mermaid
classDiagram
    C_CS2HudModelBase <|-- C_CS2HudModelArms
    C_LateUpdatedAnimating <|-- C_CS2HudModelBase
    CBaseAnimGraph <|-- C_LateUpdatedAnimating
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
```

### C_CS2HudModelBase

**Inherits from:** [C_LateUpdatedAnimating](client.md#c_lateupdatedanimating)

**Derived by:** [C_CS2HudModelArms](client.md#c_cs2hudmodelarms), [C_CS2HudModelWeapon](client.md#c_cs2hudmodelweapon)

**Relationships:**

```mermaid
classDiagram
    C_LateUpdatedAnimating <|-- C_CS2HudModelBase
    CBaseAnimGraph <|-- C_LateUpdatedAnimating
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_CS2HudModelBase <|-- C_CS2HudModelArms
    C_CS2HudModelBase <|-- C_CS2HudModelWeapon
```

### C_CS2HudModelWeapon

**Inherits from:** [C_CS2HudModelBase](client.md#c_cs2hudmodelbase)

**Relationships:**

```mermaid
classDiagram
    C_CS2HudModelBase <|-- C_CS2HudModelWeapon
    C_LateUpdatedAnimating <|-- C_CS2HudModelBase
    CBaseAnimGraph <|-- C_LateUpdatedAnimating
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
```

### C_CS2WeaponModuleBase

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Derived by:** [C_KeychainModule](client.md#c_keychainmodule), [C_NametagModule](client.md#c_nametagmodule), [C_StattrakModule](client.md#c_stattrakmodule)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_CS2WeaponModuleBase
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_CS2WeaponModuleBase <|-- C_KeychainModule
    C_CS2WeaponModuleBase <|-- C_NametagModule
    C_CS2WeaponModuleBase <|-- C_StattrakModule
```

### C_CSGO_CounterTerroristTeamIntroCamera

**Inherits from:** [C_CSGO_TeamPreviewCamera](client.md#c_csgo_teampreviewcamera)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamPreviewCamera <|-- C_CSGO_CounterTerroristTeamIntroCamera
    C_CSGO_MapPreviewCameraPath <|-- C_CSGO_TeamPreviewCamera
    C_BaseEntity <|-- C_CSGO_MapPreviewCameraPath
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGO_CounterTerroristWingmanIntroCamera

**Inherits from:** [C_CSGO_TeamPreviewCamera](client.md#c_csgo_teampreviewcamera)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamPreviewCamera <|-- C_CSGO_CounterTerroristWingmanIntroCamera
    C_CSGO_MapPreviewCameraPath <|-- C_CSGO_TeamPreviewCamera
    C_BaseEntity <|-- C_CSGO_MapPreviewCameraPath
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGO_EndOfMatchCamera

**Inherits from:** [C_CSGO_TeamPreviewCamera](client.md#c_csgo_teampreviewcamera)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamPreviewCamera <|-- C_CSGO_EndOfMatchCamera
    C_CSGO_MapPreviewCameraPath <|-- C_CSGO_TeamPreviewCamera
    C_BaseEntity <|-- C_CSGO_MapPreviewCameraPath
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGO_EndOfMatchCharacterPosition

**Inherits from:** [C_CSGO_TeamPreviewCharacterPosition](client.md#c_csgo_teampreviewcharacterposition)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_EndOfMatchCharacterPosition
    C_BaseEntity <|-- C_CSGO_TeamPreviewCharacterPosition
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGO_EndOfMatchLineupEndpoint

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [CCSGO_EndOfMatchLineupEnd](client.md#ccsgo_endofmatchlineupend), [C_CSGO_EndOfMatchLineupStart](client.md#c_csgo_endofmatchlineupstart)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_CSGO_EndOfMatchLineupEndpoint
    CEntityInstance <|-- C_BaseEntity
    C_CSGO_EndOfMatchLineupEndpoint <|-- CCSGO_EndOfMatchLineupEnd
    C_CSGO_EndOfMatchLineupEndpoint <|-- C_CSGO_EndOfMatchLineupStart
```

### C_CSGO_EndOfMatchLineupStart

**Inherits from:** [C_CSGO_EndOfMatchLineupEndpoint](client.md#c_csgo_endofmatchlineupendpoint)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_EndOfMatchLineupEndpoint <|-- C_CSGO_EndOfMatchLineupStart
    C_BaseEntity <|-- C_CSGO_EndOfMatchLineupEndpoint
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGO_MapPreviewCameraPath

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [C_CSGO_TeamPreviewCamera](client.md#c_csgo_teampreviewcamera)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_CSGO_MapPreviewCameraPath
    CEntityInstance <|-- C_BaseEntity
    C_CSGO_MapPreviewCameraPath <|-- C_CSGO_TeamPreviewCamera
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flZFar` | float32 |  |
| `m_flZNear` | float32 |  |
| `m_bLoop` | bool |  |
| `m_bVerticalFOV` | bool |  |
| `m_bConstantSpeed` | bool |  |
| `m_flDuration` | float32 |  |
| `m_flPathLength` | float32 |  |
| `m_flPathDuration` | float32 |  |
| `m_bDofEnabled` | bool |  |
| `m_flDofNearBlurry` | float32 |  |
| `m_flDofNearCrisp` | float32 |  |
| `m_flDofFarCrisp` | float32 |  |
| `m_flDofFarBlurry` | float32 |  |
| `m_flDofTiltToGround` | float32 |  |

### C_CSGO_MapPreviewCameraPathNode

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_CSGO_MapPreviewCameraPathNode
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_szParentPathUniqueID` | CUtlSymbolLarge |  |
| `m_nPathIndex` | int32 |  |
| `m_vInTangentLocal` | Vector |  |
| `m_vOutTangentLocal` | Vector |  |
| `m_flFOV` | float32 |  |
| `m_flCameraSpeed` | float32 |  |
| `m_flEaseIn` | float32 |  |
| `m_flEaseOut` | float32 |  |
| `m_vInTangentWorld` | Vector |  |
| `m_vOutTangentWorld` | Vector |  |

### C_CSGO_MapPreviewCameraPathNode_API

### C_CSGO_MapPreviewCameraPath_API

### C_CSGO_PreviewModel

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Derived by:** [C_CSGO_PreviewModelAlias_csgo_item_previewmodel](client.md#c_csgo_previewmodelalias_csgo_item_previewmodel)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_CSGO_PreviewModel
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_CSGO_PreviewModel <|-- C_CSGO_PreviewModelAlias_csgo_item_previewmodel
    C_CSGO_PreviewModel *-- AnimLoopMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_defaultAnim` | CUtlString |  |
| `m_nDefaultAnimLoopMode` | [AnimLoopMode_t](../schemas/!GlobalTypes.md#animloopmode_t) |  |
| `m_flInitialModelScale` | float32 |  |
| `m_sInitialWeaponState` | CUtlString |  |

### C_CSGO_PreviewModelAlias_csgo_item_previewmodel

**Inherits from:** [C_CSGO_PreviewModel](client.md#c_csgo_previewmodel)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_PreviewModel <|-- C_CSGO_PreviewModelAlias_csgo_item_previewmodel
    CBaseAnimGraph <|-- C_CSGO_PreviewModel
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGO_PreviewModel_API

### C_CSGO_PreviewPlayer

**Inherits from:** [C_CSPlayerPawn](client.md#c_csplayerpawn)

**Derived by:** [C_CSGO_PreviewPlayerAlias_csgo_player_previewmodel](client.md#c_csgo_previewplayeralias_csgo_player_previewmodel), [C_CSGO_TeamPreviewModel](client.md#c_csgo_teampreviewmodel)

**Relationships:**

```mermaid
classDiagram
    C_CSPlayerPawn <|-- C_CSGO_PreviewPlayer
    C_CSPlayerPawnBase <|-- C_CSPlayerPawn
    C_BasePlayerPawn <|-- C_CSPlayerPawnBase
    C_BaseCombatCharacter <|-- C_BasePlayerPawn
    CBaseAnimGraph <|-- C_BaseCombatCharacter
    C_CSGO_PreviewPlayer <|-- C_CSGO_PreviewPlayerAlias_csgo_player_previewmodel
    C_CSGO_PreviewPlayer <|-- C_CSGO_TeamPreviewModel
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_animgraphCharacterModeString` | CGlobalSymbol |  |
| `m_flInitialModelScale` | float32 |  |

### C_CSGO_PreviewPlayerAlias_csgo_player_previewmodel

**Inherits from:** [C_CSGO_PreviewPlayer](client.md#c_csgo_previewplayer)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_PreviewPlayer <|-- C_CSGO_PreviewPlayerAlias_csgo_player_previewmodel
    C_CSPlayerPawn <|-- C_CSGO_PreviewPlayer
    C_CSPlayerPawnBase <|-- C_CSPlayerPawn
    C_BasePlayerPawn <|-- C_CSPlayerPawnBase
    C_BaseCombatCharacter <|-- C_BasePlayerPawn
```

### C_CSGO_PreviewPlayer_API

### C_CSGO_TeamIntroCharacterPosition

**Inherits from:** [C_CSGO_TeamPreviewCharacterPosition](client.md#c_csgo_teampreviewcharacterposition)

**Derived by:** [CCSGO_WingmanIntroCharacterPosition](client.md#ccsgo_wingmanintrocharacterposition), [C_CSGO_TeamIntroCounterTerroristPosition](client.md#c_csgo_teamintrocounterterroristposition), [C_CSGO_TeamIntroTerroristPosition](client.md#c_csgo_teamintroterroristposition)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_TeamIntroCharacterPosition
    C_BaseEntity <|-- C_CSGO_TeamPreviewCharacterPosition
    CEntityInstance <|-- C_BaseEntity
    C_CSGO_TeamIntroCharacterPosition <|-- CCSGO_WingmanIntroCharacterPosition
    C_CSGO_TeamIntroCharacterPosition <|-- C_CSGO_TeamIntroCounterTerroristPosition
    C_CSGO_TeamIntroCharacterPosition <|-- C_CSGO_TeamIntroTerroristPosition
```

### C_CSGO_TeamIntroCounterTerroristPosition

**Inherits from:** [C_CSGO_TeamIntroCharacterPosition](client.md#c_csgo_teamintrocharacterposition)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamIntroCharacterPosition <|-- C_CSGO_TeamIntroCounterTerroristPosition
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_TeamIntroCharacterPosition
    C_BaseEntity <|-- C_CSGO_TeamPreviewCharacterPosition
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGO_TeamIntroTerroristPosition

**Inherits from:** [C_CSGO_TeamIntroCharacterPosition](client.md#c_csgo_teamintrocharacterposition)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamIntroCharacterPosition <|-- C_CSGO_TeamIntroTerroristPosition
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_TeamIntroCharacterPosition
    C_BaseEntity <|-- C_CSGO_TeamPreviewCharacterPosition
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGO_TeamPreviewCamera

**Inherits from:** [C_CSGO_MapPreviewCameraPath](client.md#c_csgo_mappreviewcamerapath)

**Derived by:** [C_CSGO_CounterTerroristTeamIntroCamera](client.md#c_csgo_counterterroristteamintrocamera), [C_CSGO_CounterTerroristWingmanIntroCamera](client.md#c_csgo_counterterroristwingmanintrocamera), [C_CSGO_EndOfMatchCamera](client.md#c_csgo_endofmatchcamera), [C_CSGO_TeamSelectCamera](client.md#c_csgo_teamselectcamera), [C_CSGO_TerroristTeamIntroCamera](client.md#c_csgo_terroristteamintrocamera), [C_CSGO_TerroristWingmanIntroCamera](client.md#c_csgo_terroristwingmanintrocamera)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_MapPreviewCameraPath <|-- C_CSGO_TeamPreviewCamera
    C_BaseEntity <|-- C_CSGO_MapPreviewCameraPath
    CEntityInstance <|-- C_BaseEntity
    C_CSGO_TeamPreviewCamera <|-- C_CSGO_CounterTerroristTeamIntroCamera
    C_CSGO_TeamPreviewCamera <|-- C_CSGO_CounterTerroristWingmanIntroCamera
    C_CSGO_TeamPreviewCamera <|-- C_CSGO_EndOfMatchCamera
    C_CSGO_TeamPreviewCamera <|-- C_CSGO_TeamSelectCamera
    C_CSGO_TeamPreviewCamera <|-- C_CSGO_TerroristTeamIntroCamera
    C_CSGO_TeamPreviewCamera <|-- C_CSGO_TerroristWingmanIntroCamera
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nVariant` | int32 |  |

### C_CSGO_TeamPreviewCamera_API

### C_CSGO_TeamPreviewCharacterPosition

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [C_CSGO_EndOfMatchCharacterPosition](client.md#c_csgo_endofmatchcharacterposition), [C_CSGO_TeamIntroCharacterPosition](client.md#c_csgo_teamintrocharacterposition), [C_CSGO_TeamSelectCharacterPosition](client.md#c_csgo_teamselectcharacterposition)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_CSGO_TeamPreviewCharacterPosition
    CEntityInstance <|-- C_BaseEntity
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_EndOfMatchCharacterPosition
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_TeamIntroCharacterPosition
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_TeamSelectCharacterPosition
    C_CSGO_TeamPreviewCharacterPosition *-- C_EconItemView
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nVariant` | int32 |  |
| `m_nRandom` | int32 |  |
| `m_nOrdinal` | int32 |  |
| `m_sWeaponName` | CUtlString |  |
| `m_xuid` | uint64 |  |
| `m_agentItem` | [C_EconItemView](../schemas/client.md#c_econitemview) |  |
| `m_glovesItem` | [C_EconItemView](../schemas/client.md#c_econitemview) |  |
| `m_weaponItem` | [C_EconItemView](../schemas/client.md#c_econitemview) |  |

### C_CSGO_TeamPreviewModel

**Inherits from:** [C_CSGO_PreviewPlayer](client.md#c_csgo_previewplayer)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_PreviewPlayer <|-- C_CSGO_TeamPreviewModel
    C_CSPlayerPawn <|-- C_CSGO_PreviewPlayer
    C_CSPlayerPawnBase <|-- C_CSPlayerPawn
    C_BasePlayerPawn <|-- C_CSPlayerPawnBase
    C_BaseCombatCharacter <|-- C_BasePlayerPawn
```

### C_CSGO_TeamSelectCamera

**Inherits from:** [C_CSGO_TeamPreviewCamera](client.md#c_csgo_teampreviewcamera)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamPreviewCamera <|-- C_CSGO_TeamSelectCamera
    C_CSGO_MapPreviewCameraPath <|-- C_CSGO_TeamPreviewCamera
    C_BaseEntity <|-- C_CSGO_MapPreviewCameraPath
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGO_TeamSelectCharacterPosition

**Inherits from:** [C_CSGO_TeamPreviewCharacterPosition](client.md#c_csgo_teampreviewcharacterposition)

**Derived by:** [C_CSGO_TeamSelectCounterTerroristPosition](client.md#c_csgo_teamselectcounterterroristposition), [C_CSGO_TeamSelectTerroristPosition](client.md#c_csgo_teamselectterroristposition)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_TeamSelectCharacterPosition
    C_BaseEntity <|-- C_CSGO_TeamPreviewCharacterPosition
    CEntityInstance <|-- C_BaseEntity
    C_CSGO_TeamSelectCharacterPosition <|-- C_CSGO_TeamSelectCounterTerroristPosition
    C_CSGO_TeamSelectCharacterPosition <|-- C_CSGO_TeamSelectTerroristPosition
```

### C_CSGO_TeamSelectCounterTerroristPosition

**Inherits from:** [C_CSGO_TeamSelectCharacterPosition](client.md#c_csgo_teamselectcharacterposition)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamSelectCharacterPosition <|-- C_CSGO_TeamSelectCounterTerroristPosition
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_TeamSelectCharacterPosition
    C_BaseEntity <|-- C_CSGO_TeamPreviewCharacterPosition
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGO_TeamSelectTerroristPosition

**Inherits from:** [C_CSGO_TeamSelectCharacterPosition](client.md#c_csgo_teamselectcharacterposition)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamSelectCharacterPosition <|-- C_CSGO_TeamSelectTerroristPosition
    C_CSGO_TeamPreviewCharacterPosition <|-- C_CSGO_TeamSelectCharacterPosition
    C_BaseEntity <|-- C_CSGO_TeamPreviewCharacterPosition
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGO_TerroristTeamIntroCamera

**Inherits from:** [C_CSGO_TeamPreviewCamera](client.md#c_csgo_teampreviewcamera)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamPreviewCamera <|-- C_CSGO_TerroristTeamIntroCamera
    C_CSGO_MapPreviewCameraPath <|-- C_CSGO_TeamPreviewCamera
    C_BaseEntity <|-- C_CSGO_MapPreviewCameraPath
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGO_TerroristWingmanIntroCamera

**Inherits from:** [C_CSGO_TeamPreviewCamera](client.md#c_csgo_teampreviewcamera)

**Relationships:**

```mermaid
classDiagram
    C_CSGO_TeamPreviewCamera <|-- C_CSGO_TerroristWingmanIntroCamera
    C_CSGO_MapPreviewCameraPath <|-- C_CSGO_TeamPreviewCamera
    C_BaseEntity <|-- C_CSGO_MapPreviewCameraPath
    CEntityInstance <|-- C_BaseEntity
```

### C_CSGameRules

**Inherits from:** [C_TeamplayRules](client.md#c_teamplayrules)

**Relationships:**

```mermaid
classDiagram
    C_TeamplayRules <|-- C_CSGameRules
    C_MultiplayRules <|-- C_TeamplayRules
    C_GameRules <|-- C_MultiplayRules
    C_CSGameRules *-- GameTime_t
    C_CSGameRules --> CCSGameModeRules
    C_CSGameRules *-- C_RetakeGameRules
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bFreezePeriod` | bool |  |
| `m_bWarmupPeriod` | bool |  |
| `m_fWarmupPeriodEnd` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_fWarmupPeriodStart` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bTerroristTimeOutActive` | bool |  |
| `m_bCTTimeOutActive` | bool |  |
| `m_flTerroristTimeOutRemaining` | float32 |  |
| `m_flCTTimeOutRemaining` | float32 |  |
| `m_nTerroristTimeOuts` | int32 |  |
| `m_nCTTimeOuts` | int32 |  |
| `m_bTechnicalTimeOut` | bool |  |
| `m_bMatchWaitingForResume` | bool |  |
| `m_iFreezeTime` | int32 |  |
| `m_iRoundTime` | int32 |  |
| `m_fMatchStartTime` | float32 |  |
| `m_fRoundStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flRestartRoundTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bGameRestart` | bool |  |
| `m_flGameStartTime` | float32 |  |
| `m_timeUntilNextPhaseStarts` | float32 |  |
| `m_gamePhase` | int32 |  |
| `m_totalRoundsPlayed` | int32 |  |
| `m_nRoundsPlayedThisPhase` | int32 |  |
| `m_nOvertimePlaying` | int32 |  |
| `m_iHostagesRemaining` | int32 |  |
| `m_bAnyHostageReached` | bool |  |
| `m_bMapHasBombTarget` | bool |  |
| `m_bMapHasRescueZone` | bool |  |
| `m_bMapHasBuyZone` | bool |  |
| `m_bIsQueuedMatchmaking` | bool |  |
| `m_nQueuedMatchmakingMode` | int32 |  |
| `m_bIsValveDS` | bool |  |
| `m_bLogoMap` | bool |  |
| `m_bPlayAllStepSoundsOnServer` | bool |  |
| `m_iSpectatorSlotCount` | int32 |  |
| `m_MatchDevice` | int32 |  |
| `m_bHasMatchStarted` | bool |  |
| `m_nNextMapInMapgroup` | int32 |  |
| `m_szTournamentEventName` | char[512] |  |
| `m_szTournamentEventStage` | char[512] |  |
| `m_szMatchStatTxt` | char[512] |  |
| `m_szTournamentPredictionsTxt` | char[512] |  |
| `m_nTournamentPredictionsPct` | int32 |  |
| `m_flCMMItemDropRevealStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flCMMItemDropRevealEndTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bIsDroppingItems` | bool |  |
| `m_bIsQuestEligible` | bool |  |
| `m_bIsHltvActive` | bool |  |
| `m_bBombPlanted` | bool |  |
| `m_arrProhibitedItemIndices` | uint16[100] |  |
| `m_arrTournamentActiveCasterAccounts` | uint32[4] |  |
| `m_numBestOfMaps` | int32 |  |
| `m_nHalloweenMaskListSeed` | int32 |  |
| `m_bBombDropped` | bool |  |
| `m_iRoundWinStatus` | int32 |  |
| `m_eRoundWinReason` | int32 |  |
| `m_bTCantBuy` | bool |  |
| `m_bCTCantBuy` | bool |  |
| `m_iMatchStats_RoundResults` | int32[30] |  |
| `m_iMatchStats_PlayersAlive_CT` | int32[30] |  |
| `m_iMatchStats_PlayersAlive_T` | int32[30] |  |
| `m_TeamRespawnWaveTimes` | float32[32] |  |
| `m_flNextRespawnWave` | [GameTime_t](../schemas/entity2.md#gametime_t)[32] |  |
| `m_vMinimapMins` | VectorWS |  |
| `m_vMinimapMaxs` | VectorWS |  |
| `m_MinimapVerticalSectionHeights` | float32[8] |  |
| `m_ullLocalMatchID` | uint64 |  |
| `m_nEndMatchMapGroupVoteTypes` | int32[10] |  |
| `m_nEndMatchMapGroupVoteOptions` | int32[10] |  |
| `m_nEndMatchMapVoteWinner` | int32 |  |
| `m_iNumConsecutiveCTLoses` | int32 |  |
| `m_iNumConsecutiveTerroristLoses` | int32 |  |
| `m_nMatchAbortedEarlyReason` | int32 |  |
| `m_bHasTriggeredRoundStartMusic` | bool |  |
| `m_bSwitchingTeamsAtRoundReset` | bool |  |
| `m_pGameModeRules` | [CCSGameModeRules](../schemas/client.md#ccsgamemoderules)* |  |
| `m_RetakeRules` | [C_RetakeGameRules](../schemas/client.md#c_retakegamerules) |  |
| `m_nMatchEndCount` | uint8 |  |
| `m_nTTeamIntroVariant` | int32 |  |
| `m_nCTTeamIntroVariant` | int32 |  |
| `m_bTeamIntroPeriod` | bool |  |
| `m_iRoundEndWinnerTeam` | int32 |  |
| `m_eRoundEndReason` | int32 |  |
| `m_bRoundEndShowTimerDefend` | bool |  |
| `m_iRoundEndTimerTime` | int32 |  |
| `m_sRoundEndFunFactToken` | CUtlString |  |
| `m_iRoundEndFunFactPlayerSlot` | CPlayerSlot |  |
| `m_iRoundEndFunFactData1` | int32 |  |
| `m_iRoundEndFunFactData2` | int32 |  |
| `m_iRoundEndFunFactData3` | int32 |  |
| `m_sRoundEndMessage` | CUtlString |  |
| `m_iRoundEndPlayerCount` | int32 |  |
| `m_bRoundEndNoMusic` | bool |  |
| `m_iRoundEndLegacy` | int32 |  |
| `m_nRoundEndCount` | uint8 |  |
| `m_iRoundStartRoundNumber` | int32 |  |
| `m_nRoundStartCount` | uint8 |  |
| `m_flLastPerfSampleTime` | float64 |  |

### C_CSGameRulesProxy

**Inherits from:** [C_GameRulesProxy](client.md#c_gamerulesproxy)

**Relationships:**

```mermaid
classDiagram
    C_GameRulesProxy <|-- C_CSGameRulesProxy
    C_BaseEntity <|-- C_GameRulesProxy
    CEntityInstance <|-- C_BaseEntity
    C_CSGameRulesProxy --> C_CSGameRules
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_pGameRules` | [C_CSGameRules](../schemas/client.md#c_csgamerules)* |  |

### C_CSMinimapBoundary

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_CSMinimapBoundary
    CEntityInstance <|-- C_BaseEntity
```

### C_CSObserverPawn

**Inherits from:** [C_CSPlayerPawnBase](client.md#c_csplayerpawnbase)

**Relationships:**

```mermaid
classDiagram
    C_CSPlayerPawnBase <|-- C_CSObserverPawn
    C_BasePlayerPawn <|-- C_CSPlayerPawnBase
    C_BaseCombatCharacter <|-- C_BasePlayerPawn
    CBaseAnimGraph <|-- C_BaseCombatCharacter
    C_BaseModelEntity <|-- CBaseAnimGraph
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hDetectParentChange` | CEntityHandle |  |

### C_CSObserverPawn_API

### C_CSPetPlacement

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_CSPetPlacement
    CEntityInstance <|-- C_BaseEntity
```

### C_CSPlayerPawn

**Inherits from:** [C_CSPlayerPawnBase](client.md#c_csplayerpawnbase)

**Derived by:** [C_CSGO_PreviewPlayer](client.md#c_csgo_previewplayer)

**Relationships:**

```mermaid
classDiagram
    C_CSPlayerPawnBase <|-- C_CSPlayerPawn
    C_BasePlayerPawn <|-- C_CSPlayerPawnBase
    C_BaseCombatCharacter <|-- C_BasePlayerPawn
    CBaseAnimGraph <|-- C_BaseCombatCharacter
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_CSPlayerPawn <|-- C_CSGO_PreviewPlayer
    C_CSPlayerPawn --> CCSPlayer_BulletServices
    C_CSPlayerPawn --> CCSPlayer_HostageServices
    C_CSPlayerPawn --> CCSPlayer_BuyServices
    C_CSPlayerPawn --> CCSPlayer_GlowServices
    C_CSPlayerPawn --> CCSPlayer_ActionTrackingServices
    C_CSPlayerPawn --> CCSPlayer_AimPunchServices
    C_CSPlayerPawn --> CCSPlayer_DamageReactServices
    C_CSPlayerPawn *-- GameTime_t
    C_CSPlayerPawn *-- C_EconItemView
    C_CSPlayerPawn --> C_CS2HudModelArms
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_pBulletServices` | [CCSPlayer_BulletServices](../schemas/client.md#ccsplayer_bulletservices)* |  |
| `m_pHostageServices` | [CCSPlayer_HostageServices](../schemas/client.md#ccsplayer_hostageservices)* |  |
| `m_pBuyServices` | [CCSPlayer_BuyServices](../schemas/client.md#ccsplayer_buyservices)* |  |
| `m_pGlowServices` | [CCSPlayer_GlowServices](../schemas/client.md#ccsplayer_glowservices)* |  |
| `m_pActionTrackingServices` | [CCSPlayer_ActionTrackingServices](../schemas/client.md#ccsplayer_actiontrackingservices)* |  |
| `m_pAimPunchServices` | [CCSPlayer_AimPunchServices](../schemas/client.md#ccsplayer_aimpunchservices)* |  |
| `m_pDamageReactServices` | [CCSPlayer_DamageReactServices](../schemas/client.md#ccsplayer_damagereactservices)* |  |
| `m_flHealthShotBoostExpirationTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flLastFiredWeaponTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bHasFemaleVoice` | bool |  |
| `m_flLandingTimeSeconds` | float32 |  |
| `m_flOldFallVelocity` | float32 |  |
| `m_szLastPlaceName` | char[18] |  |
| `m_bPrevDefuser` | bool |  |
| `m_bPrevHelmet` | bool |  |
| `m_nPrevArmorVal` | int32 |  |
| `m_nPrevGrenadeAmmoCount` | int32 |  |
| `m_unPreviousWeaponHash` | uint32 |  |
| `m_unWeaponHash` | uint32 |  |
| `m_bInBuyZone` | bool |  |
| `m_bPreviouslyInBuyZone` | bool |  |
| `m_bInLanding` | bool |  |
| `m_flLandingStartTime` | float32 |  |
| `m_bInHostageRescueZone` | bool |  |
| `m_bInBombZone` | bool |  |
| `m_bIsBuyMenuOpen` | bool |  |
| `m_flTimeOfLastInjury` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flNextSprayDecalTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_iRetakesOffering` | int32 |  |
| `m_iRetakesOfferingCard` | int32 |  |
| `m_bRetakesHasDefuseKit` | bool |  |
| `m_bRetakesMVPLastRound` | bool |  |
| `m_iRetakesMVPBoostItem` | int32 |  |
| `m_RetakesMVPBoostExtraUtility` | loadout_slot_t |  |
| `m_bNeedToReApplyGloves` | bool |  |
| `m_EconGloves` | [C_EconItemView](../schemas/client.md#c_econitemview) |  |
| `m_nEconGlovesChanged` | uint8 |  |
| `m_bMustSyncRagdollState` | bool |  |
| `m_nRagdollDamageBone` | int32 |  |
| `m_vRagdollDamageForce` | Vector |  |
| `m_szRagdollDamageWeaponName` | char[64] |  |
| `m_bRagdollDamageHeadshot` | bool |  |
| `m_vRagdollServerOrigin` | VectorWS |  |
| `m_lastLandTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bOnGroundLastTick` | bool |  |
| `m_hHudModelArms` | CHandle< [C_CS2HudModelArms](../schemas/client.md#c_cs2hudmodelarms) > |  |
| `m_qDeathEyeAngles` | QAngle |  |
| `m_bLeftHanded` | bool |  |
| `m_fSwitchedHandednessTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flViewmodelOffsetX` | float32 |  |
| `m_flViewmodelOffsetY` | float32 |  |
| `m_flViewmodelOffsetZ` | float32 |  |
| `m_flViewmodelFOV` | float32 |  |
| `m_vecPlayerPatchEconIndices` | uint32[5] |  |
| `m_GunGameImmunityColor` | Color |  |
| `m_vecBulletHitModels` | CUtlVector< [C_BulletHitModel](../schemas/client.md#c_bullethitmodel)* > |  |
| `m_bIsWalking` | bool |  |
| `m_entitySpottedState` | [EntitySpottedState_t](../schemas/client.md#entityspottedstate_t) |  |
| `m_bIsScoped` | bool |  |
| `m_bResumeZoom` | bool |  |
| `m_bIsDefusing` | bool |  |
| `m_bIsGrabbingHostage` | bool |  |
| `m_iBlockingUseActionInProgress` | [CSPlayerBlockingUseAction_t](../schemas/!GlobalTypes.md#csplayerblockinguseaction_t) |  |
| `m_flEmitSoundTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bInNoDefuseArea` | bool |  |
| `m_nWhichBombZone` | int32 |  |
| `m_iShotsFired` | int32 |  |
| `m_flFlinchStack` | float32 |  |
| `m_flVelocityModifier` | float32 |  |
| `m_bWaitForNoAttack` | bool |  |
| `m_ignoreLadderJumpTime` | float32 |  |
| `m_bKilledByHeadshot` | bool |  |
| `m_ArmorValue` | int32 |  |
| `m_unCurrentEquipmentValue` | uint16 |  |
| `m_unRoundStartEquipmentValue` | uint16 |  |
| `m_unFreezetimeEndEquipmentValue` | uint16 |  |
| `m_nLastKillerIndex` | CEntityIndex |  |
| `m_bOldIsScoped` | bool |  |
| `m_bHasDeathInfo` | bool |  |
| `m_flDeathInfoTime` | float32 |  |
| `m_vecDeathInfoOrigin` | VectorWS |  |
| `m_grenadeParameterStashTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bGrenadeParametersStashed` | bool |  |
| `m_angStashedShootAngles` | QAngle |  |
| `m_vecStashedGrenadeThrowPosition` | VectorWS |  |
| `m_vecStashedVelocity` | Vector |  |
| `m_bShouldAutobuyDMWeapons` | bool |  |
| `m_fImmuneToGunGameDamageTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bGunGameImmunity` | bool |  |
| `m_fImmuneToGunGameDamageTimeLast` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_fMolotovDamageTime` | float32 |  |
| `m_nPlayerInfernoBodyFx` | [ParticleIndex_t](../schemas/server.md#particleindex_t) |  |
| `m_angEyeAngles` | QAngle |  |
| `m_arrOldEyeAnglesTimes` | [GameTime_t](../schemas/entity2.md#gametime_t)[4] |  |
| `m_arrOldEyeAngles` | QAngle[4] |  |
| `m_angEyeAnglesVelocity` | QAngle |  |
| `m_iIDEntIndex` | CEntityIndex |  |
| `m_delayTargetIDTimer` | [CountdownTimer](../schemas/client.md#countdowntimer) |  |
| `m_iTargetItemEntIdx` | CEntityIndex |  |
| `m_iOldIDEntIndex` | CEntityIndex |  |
| `m_holdTargetIDTimer` | [CountdownTimer](../schemas/client.md#countdowntimer) |  |

### C_CSPlayerPawnBase

**Inherits from:** [C_BasePlayerPawn](client.md#c_baseplayerpawn)

**Derived by:** [C_CSObserverPawn](client.md#c_csobserverpawn), [C_CSPlayerPawn](client.md#c_csplayerpawn)

**Relationships:**

```mermaid
classDiagram
    C_BasePlayerPawn <|-- C_CSPlayerPawnBase
    C_BaseCombatCharacter <|-- C_BasePlayerPawn
    CBaseAnimGraph <|-- C_BaseCombatCharacter
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    C_CSPlayerPawnBase <|-- C_CSObserverPawn
    C_CSPlayerPawnBase <|-- C_CSPlayerPawn
    C_CSPlayerPawnBase --> CCSPlayer_PingServices
    C_CSPlayerPawnBase *-- CSPlayerState
    C_CSPlayerPawnBase *-- GameTime_t
    C_CSPlayerPawnBase --> CCSPlayerController
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_pPingServices` | [CCSPlayer_PingServices](../schemas/client.md#ccsplayer_pingservices)* |  |
| `m_previousPlayerState` | [CSPlayerState](../schemas/!GlobalTypes.md#csplayerstate) |  |
| `m_iPlayerState` | [CSPlayerState](../schemas/!GlobalTypes.md#csplayerstate) |  |
| `m_bHasMovedSinceSpawn` | bool |  |
| `m_flLastSpawnTimeIndex` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_iProgressBarDuration` | int32 |  |
| `m_flProgressBarStartTime` | float32 |  |
| `m_flClientDeathTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flFlashBangTime` | float32 |  |
| `m_flFlashScreenshotAlpha` | float32 |  |
| `m_flFlashOverlayAlpha` | float32 |  |
| `m_bFlashBuildUp` | bool |  |
| `m_bFlashDspHasBeenCleared` | bool |  |
| `m_bFlashScreenshotHasBeenGrabbed` | bool |  |
| `m_flFlashMaxAlpha` | float32 |  |
| `m_flFlashDuration` | float32 |  |
| `m_flClientHealthFadeChangeTimestamp` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_nClientHealthFadeParityValue` | int32 |  |
| `m_fNextThinkPushAway` | float32 |  |
| `m_flCurrentMusicStartTime` | float32 |  |
| `m_flMusicRoundStartTime` | float32 |  |
| `m_bDeferStartMusicOnWarmup` | bool |  |
| `m_flLastSmokeOverlayAlpha` | float32 |  |
| `m_flLastSmokeAge` | float32 |  |
| `m_vLastSmokeOverlayColor` | Vector |  |
| `m_hOriginalController` | CHandle< [CCSPlayerController](../schemas/client.md#ccsplayercontroller) > |  |

### C_CSPlayerPawnBase_API

### C_CSPlayerPawn_API

### C_CSPlayerResource

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_CSPlayerResource
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bHostageAlive` | bool[12] |  |
| `m_isHostageFollowingSomeone` | bool[12] |  |
| `m_iHostageEntityIDs` | CEntityIndex[12] |  |
| `m_bombsiteCenterA` | VectorWS |  |
| `m_bombsiteCenterB` | VectorWS |  |
| `m_hostageRescueX` | int32[4] |  |
| `m_hostageRescueY` | int32[4] |  |
| `m_hostageRescueZ` | int32[4] |  |
| `m_bEndMatchNextMapAllVoted` | bool |  |
| `m_foundGoalPositions` | bool |  |

### C_CSTeam

**Inherits from:** [C_Team](client.md#c_team)

**Relationships:**

```mermaid
classDiagram
    C_Team <|-- C_CSTeam
    C_BaseEntity <|-- C_Team
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_szTeamMatchStat` | char[512] |  |
| `m_numMapVictories` | int32 |  |
| `m_bSurrendered` | bool |  |
| `m_scoreFirstHalf` | int32 |  |
| `m_scoreSecondHalf` | int32 |  |
| `m_scoreOvertime` | int32 |  |
| `m_szClanTeamname` | char[129] |  |
| `m_iClanID` | uint32 |  |
| `m_szTeamFlagImage` | char[8] |  |
| `m_szTeamLogoImage` | char[8] |  |

### C_CSWeaponBase

**Inherits from:** [C_BasePlayerWeapon](client.md#c_baseplayerweapon)

**Derived by:** [C_BaseCSGrenade](client.md#c_basecsgrenade), [C_C4](client.md#c_c4), [C_CSWeaponBaseGun](client.md#c_csweaponbasegun), [C_CSWeaponBaseShotgun](client.md#c_csweaponbaseshotgun), [C_Knife](client.md#c_knife), [C_WeaponBaseItem](client.md#c_weaponbaseitem)

**Relationships:**

```mermaid
classDiagram
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    C_CSWeaponBase <|-- C_BaseCSGrenade
    C_CSWeaponBase <|-- C_C4
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_CSWeaponBase <|-- C_CSWeaponBaseShotgun
    C_CSWeaponBase <|-- C_Knife
    C_CSWeaponBase <|-- C_WeaponBaseItem
    C_CSWeaponBase *-- WeaponGameplayAnimState
    C_CSWeaponBase *-- GameTime_t
    C_CSWeaponBase *-- CEntityIOOutput
    C_CSWeaponBase *-- CSWeaponMode
    C_CSWeaponBase *-- GameTick_t
    C_CSWeaponBase --> C_CSPlayerPawn
    C_CSWeaponBase *-- C_IronSightController
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iWeaponGameplayAnimState` | [WeaponGameplayAnimState](../schemas/!GlobalTypes.md#weapongameplayanimstate) |  |
| `m_flWeaponGameplayAnimStateTimestamp` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flInspectCancelCompleteTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bInspectPending` | bool |  |
| `m_bInspectShouldLoop` | bool |  |
| `m_flCrosshairDistance` | float32 |  |
| `m_iAmmoLastCheck` | int32 |  |
| `m_nLastEmptySoundCmdNum` | int32 |  |
| `m_bFireOnEmpty` | bool |  |
| `m_OnPlayerPickup` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_weaponMode` | [CSWeaponMode](../schemas/!GlobalTypes.md#csweaponmode) |  |
| `m_flTurningInaccuracyDelta` | float32 |  |
| `m_vecTurningInaccuracyEyeDirLast` | Vector |  |
| `m_flTurningInaccuracy` | float32 |  |
| `m_fAccuracyPenalty` | float32 |  |
| `m_flLastAccuracyUpdateTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_fAccuracySmoothedForZoom` | float32 |  |
| `m_iRecoilIndex` | int32 |  |
| `m_flRecoilIndex` | float32 |  |
| `m_bBurstMode` | bool |  |
| `m_flLastBurstModeChangeTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_nPostponeFireReadyTicks` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_flPostponeFireReadyFrac` | float32 |  |
| `m_bInReload` | bool |  |
| `m_nDeployTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_flDroppedAtTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bIsHauledBack` | bool |  |
| `m_bSilencerOn` | bool |  |
| `m_flTimeSilencerSwitchComplete` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flWeaponActionPlaybackRate` | float32 |  |
| `m_iOriginalTeamNumber` | int32 |  |
| `m_iMostRecentTeamNumber` | int32 |  |
| `m_bDroppedNearBuyZone` | bool |  |
| `m_flNextAttackRenderTimeOffset` | float32 |  |
| `m_bClearWeaponIdentifyingUGC` | bool |  |
| `m_bVisualsDataSet` | bool |  |
| `m_bUIWeapon` | bool |  |
| `m_nCustomEconReloadEventId` | int32 |  |
| `m_bCanBePickedUp` | bool |  |
| `m_nextPrevOwnerUseTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_hPrevOwner` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |
| `m_nDropTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_bWasActiveWeaponWhenDropped` | bool |  |
| `m_donated` | bool |  |
| `m_fLastShotTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bWasOwnedByCT` | bool |  |
| `m_bWasOwnedByTerrorist` | bool |  |
| `m_flNextClientFireBulletTime` | float32 |  |
| `m_flNextClientFireBulletTime_Repredict` | float32 |  |
| `m_IronSightController` | [C_IronSightController](../schemas/client.md#c_ironsightcontroller) |  |
| `m_iIronSightMode` | int32 |  |
| `m_flLastLOSTraceFailureTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flWatTickOffset` | float32 |  |
| `m_flLastShakeTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |

### C_CSWeaponBaseGun

**Inherits from:** [C_CSWeaponBase](client.md#c_csweaponbase)

**Derived by:** [C_AK47](client.md#c_ak47), [C_DEagle](client.md#c_deagle), [C_WeaponAWP](client.md#c_weaponawp), [C_WeaponAug](client.md#c_weaponaug), [C_WeaponBizon](client.md#c_weaponbizon), [C_WeaponCZ75a](client.md#c_weaponcz75a), [C_WeaponElite](client.md#c_weaponelite), [C_WeaponFamas](client.md#c_weaponfamas), [C_WeaponFiveSeven](client.md#c_weaponfiveseven), [C_WeaponG3SG1](client.md#c_weapong3sg1), [C_WeaponGalilAR](client.md#c_weapongalilar), [C_WeaponGlock](client.md#c_weaponglock), [C_WeaponHKP2000](client.md#c_weaponhkp2000), [C_WeaponM249](client.md#c_weaponm249), [C_WeaponM4A1](client.md#c_weaponm4a1), [C_WeaponM4A1Silencer](client.md#c_weaponm4a1silencer), [C_WeaponMAC10](client.md#c_weaponmac10), [C_WeaponMP5SD](client.md#c_weaponmp5sd), [C_WeaponMP7](client.md#c_weaponmp7), [C_WeaponMP9](client.md#c_weaponmp9), [C_WeaponMag7](client.md#c_weaponmag7), [C_WeaponNegev](client.md#c_weaponnegev), [C_WeaponP250](client.md#c_weaponp250), [C_WeaponP90](client.md#c_weaponp90), [C_WeaponRevolver](client.md#c_weaponrevolver), [C_WeaponSCAR20](client.md#c_weaponscar20), [C_WeaponSG556](client.md#c_weaponsg556), [C_WeaponSSG08](client.md#c_weaponssg08), [C_WeaponTaser](client.md#c_weapontaser), [C_WeaponTec9](client.md#c_weapontec9), [C_WeaponUMP45](client.md#c_weaponump45), [C_WeaponUSPSilencer](client.md#c_weaponuspsilencer)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_CSWeaponBaseGun <|-- C_AK47
    C_CSWeaponBaseGun <|-- C_DEagle
    C_CSWeaponBaseGun <|-- C_WeaponAWP
    C_CSWeaponBaseGun <|-- C_WeaponAug
    C_CSWeaponBaseGun <|-- C_WeaponBizon
    C_CSWeaponBaseGun <|-- C_WeaponCZ75a
    C_CSWeaponBaseGun <|-- C_WeaponElite
    C_CSWeaponBaseGun <|-- C_WeaponFamas
    C_CSWeaponBaseGun <|-- C_WeaponFiveSeven
    C_CSWeaponBaseGun <|-- C_WeaponG3SG1
    C_CSWeaponBaseGun <|-- C_WeaponGalilAR
    C_CSWeaponBaseGun <|-- C_WeaponGlock
    C_CSWeaponBaseGun <|-- C_WeaponHKP2000
    C_CSWeaponBaseGun <|-- C_WeaponM249
    C_CSWeaponBaseGun <|-- C_WeaponM4A1
    C_CSWeaponBaseGun <|-- C_WeaponM4A1Silencer
    C_CSWeaponBaseGun <|-- C_WeaponMAC10
    C_CSWeaponBaseGun <|-- C_WeaponMP5SD
    C_CSWeaponBaseGun <|-- C_WeaponMP7
    C_CSWeaponBaseGun <|-- C_WeaponMP9
    C_CSWeaponBaseGun <|-- C_WeaponMag7
    C_CSWeaponBaseGun <|-- C_WeaponNegev
    C_CSWeaponBaseGun <|-- C_WeaponP250
    C_CSWeaponBaseGun <|-- C_WeaponP90
    C_CSWeaponBaseGun <|-- C_WeaponRevolver
    C_CSWeaponBaseGun <|-- C_WeaponSCAR20
    C_CSWeaponBaseGun <|-- C_WeaponSG556
    C_CSWeaponBaseGun <|-- C_WeaponSSG08
    C_CSWeaponBaseGun <|-- C_WeaponTaser
    C_CSWeaponBaseGun <|-- C_WeaponTec9
    C_CSWeaponBaseGun <|-- C_WeaponUMP45
    C_CSWeaponBaseGun <|-- C_WeaponUSPSilencer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_zoomLevel` | int32 |  |
| `m_iBurstShotsRemaining` | int32 |  |
| `m_iSilencerBodygroup` | int32 |  |
| `m_silencedModelIndex` | int32 |  |
| `m_inPrecache` | bool |  |
| `m_bNeedsBoltAction` | bool |  |
| `m_nRevolverCylinderIdx` | int32 |  |

### C_CSWeaponBaseShotgun

**Inherits from:** [C_CSWeaponBase](client.md#c_csweaponbase)

**Derived by:** [C_WeaponNOVA](client.md#c_weaponnova), [C_WeaponSawedoff](client.md#c_weaponsawedoff), [C_WeaponXM1014](client.md#c_weaponxm1014)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBase <|-- C_CSWeaponBaseShotgun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_CSWeaponBaseShotgun <|-- C_WeaponNOVA
    C_CSWeaponBaseShotgun <|-- C_WeaponSawedoff
    C_CSWeaponBaseShotgun <|-- C_WeaponXM1014
```

### C_Chicken

**Inherits from:** [C_DynamicProp](client.md#c_dynamicprop), [IHasAttributes](server.md#ihasattributes)

**Relationships:**

```mermaid
classDiagram
    C_DynamicProp <|-- C_Chicken
    C_BreakableProp <|-- C_DynamicProp
    CBaseProp <|-- C_BreakableProp
    CBaseAnimGraph <|-- CBaseProp
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_Chicken --> C_CSPlayerPawn
    C_Chicken *-- C_AttributeContainer
    C_Chicken *-- ParticleIndex_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_leader` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |
| `m_AttributeManager` | [C_AttributeContainer](../schemas/client.md#c_attributecontainer) |  |
| `m_bAttributesInitialized` | bool |  |
| `m_hWaterWakeParticles` | [ParticleIndex_t](../schemas/server.md#particleindex_t) |  |
| `m_bIsPreviewModel` | bool |  |

### C_ClientRagdoll

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_ClientRagdoll
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_ClientRagdoll *-- GameTime_t
    C_ClientRagdoll *-- AttachmentHandle_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bFadeOut` | bool |  |
| `m_bImportant` | bool |  |
| `m_flEffectTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_gibDespawnTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_iCurrentFriction` | int32 |  |
| `m_iMinFriction` | int32 |  |
| `m_iMaxFriction` | int32 |  |
| `m_iFrictionAnimState` | int32 |  |
| `m_bReleaseRagdoll` | bool |  |
| `m_iEyeAttachment` | [AttachmentHandle_t](../schemas/modellib.md#attachmenthandle_t) |  |
| `m_bFadingOut` | bool |  |
| `m_flScaleEnd` | float32[10] |  |
| `m_flScaleTimeStart` | [GameTime_t](../schemas/entity2.md#gametime_t)[10] |  |
| `m_flScaleTimeEnd` | [GameTime_t](../schemas/entity2.md#gametime_t)[10] |  |

### C_ColorCorrection

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_ColorCorrection
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vecOrigin` | VectorWS | `MNotSaved` |
| `m_MinFalloff` | float32 | `MNotSaved` |
| `m_MaxFalloff` | float32 | `MNotSaved` |
| `m_flFadeInDuration` | float32 | `MNotSaved` |
| `m_flFadeOutDuration` | float32 | `MNotSaved` |
| `m_flMaxWeight` | float32 | `MNotSaved` |
| `m_flCurWeight` | float32 | `MNotSaved` |
| `m_netlookupFilename` | char[512] | `MNotSaved` |
| `m_bEnabled` | bool | `MNotSaved` |
| `m_bMaster` | bool | `MNotSaved` |
| `m_bClientSide` | bool | `MNotSaved` |
| `m_bExclusive` | bool | `MNotSaved` |
| `m_bEnabledOnClient` | bool[1] | `MNotSaved` |
| `m_flCurWeightOnClient` | float32[1] | `MNotSaved` |
| `m_bFadingIn` | bool[1] | `MNotSaved` |
| `m_flFadeStartWeight` | float32[1] | `MNotSaved` |
| `m_flFadeStartTime` | float32[1] | `MNotSaved` |
| `m_flFadeDuration` | float32[1] | `MNotSaved` |

### C_ColorCorrectionVolume

**Inherits from:** [C_BaseTrigger](client.md#c_basetrigger)

**Relationships:**

```mermaid
classDiagram
    C_BaseTrigger <|-- C_ColorCorrectionVolume
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_ColorCorrectionVolume *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_LastEnterWeight` | float32 | `MNotSaved` |
| `m_LastEnterTime` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `m_LastExitWeight` | float32 | `MNotSaved` |
| `m_LastExitTime` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `m_bEnabled` | bool | `MNotSaved` |
| `m_MaxWeight` | float32 | `MNotSaved` |
| `m_FadeDuration` | float32 | `MNotSaved` |
| `m_Weight` | float32 | `MNotSaved` |
| `m_lookupFilename` | char[512] | `MNotSaved` |

### C_CommandContext

**Metadata:** `MGetKV3ClassDefaults {
	"needsprocessing": false,
	"command_number": 0
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `needsprocessing` | bool |  |
| `command_number` | int32 |  |

### C_CsmFovOverride

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_CsmFovOverride
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_cameraName` | CUtlString |  |
| `m_flCsmFovOverrideValue` | float32 |  |

### C_CsmFovOverride_API

### C_DEagle

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_DEagle
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_DecoyGrenade

**Inherits from:** [C_BaseCSGrenade](client.md#c_basecsgrenade)

**Relationships:**

```mermaid
classDiagram
    C_BaseCSGrenade <|-- C_DecoyGrenade
    C_CSWeaponBase <|-- C_BaseCSGrenade
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_DecoyProjectile

**Inherits from:** [C_BaseCSGrenadeProjectile](client.md#c_basecsgrenadeprojectile)

**Relationships:**

```mermaid
classDiagram
    C_BaseCSGrenadeProjectile <|-- C_DecoyProjectile
    C_BaseGrenade <|-- C_BaseCSGrenadeProjectile
    CBaseAnimGraph <|-- C_BaseGrenade
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    C_DecoyProjectile *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nDecoyShotTick` | int32 |  |
| `m_nClientLastKnownDecoyShotTick` | int32 |  |
| `m_flTimeParticleEffectSpawn` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |

### C_DynamicLight

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_DynamicLight
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Flags` | uint8 | `MNotSaved` |
| `m_LightStyle` | uint8 | `MNotSaved` |
| `m_Radius` | float32 | `MNotSaved` |
| `m_Exponent` | int32 | `MNotSaved` |
| `m_InnerAngle` | float32 | `MNotSaved` |
| `m_OuterAngle` | float32 | `MNotSaved` |
| `m_SpotRadius` | float32 | `MNotSaved` |

### C_DynamicProp

**Inherits from:** [C_BreakableProp](client.md#c_breakableprop)

**Derived by:** [CFuncRetakeBarrier](client.md#cfuncretakebarrier), [C_BasePropDoor](client.md#c_basepropdoor), [C_Chicken](client.md#c_chicken), [C_DynamicPropAlias_cable_dynamic](client.md#c_dynamicpropalias_cable_dynamic), [C_DynamicPropAlias_dynamic_prop](client.md#c_dynamicpropalias_dynamic_prop), [C_DynamicPropAlias_prop_dynamic_override](client.md#c_dynamicpropalias_prop_dynamic_override)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BreakableProp <|-- C_DynamicProp
    CBaseProp <|-- C_BreakableProp
    CBaseAnimGraph <|-- CBaseProp
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    C_DynamicProp <|-- CFuncRetakeBarrier
    C_DynamicProp <|-- C_BasePropDoor
    C_DynamicProp <|-- C_Chicken
    C_DynamicProp <|-- C_DynamicPropAlias_cable_dynamic
    C_DynamicProp <|-- C_DynamicPropAlias_dynamic_prop
    C_DynamicProp <|-- C_DynamicPropAlias_prop_dynamic_override
    C_DynamicProp *-- CEntityIOOutput
    C_DynamicProp *-- AnimLoopMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bUseHitboxesForRenderBox` | bool |  |
| `m_bUseAnimGraph` | bool |  |
| `m_pOutputAnimBegun` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_pOutputAnimOver` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_pOutputAnimLoopCycleOver` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnAnimReachedStart` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_OnAnimReachedEnd` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_iszIdleAnim` | CUtlSymbolLarge |  |
| `m_nIdleAnimLoopMode` | [AnimLoopMode_t](../schemas/!GlobalTypes.md#animloopmode_t) |  |
| `m_bRandomizeCycle` | bool |  |
| `m_bStartDisabled` | bool |  |
| `m_bFiredStartEndOutput` | bool |  |
| `m_bForceNpcExclude` | bool | `MNotSaved` |
| `m_bCreateMovableSurfaceGraph` | bool |  |
| `m_bCreateNonSolid` | bool | `MNotSaved` |
| `m_bIsOverrideProp` | bool | `MNotSaved` |
| `m_iInitialGlowState` | int32 |  |
| `m_nGlowRange` | int32 |  |
| `m_nGlowRangeMin` | int32 |  |
| `m_glowColor` | Color |  |
| `m_nGlowTeam` | int32 |  |
| `m_iCachedFrameCount` | int32 | `MNotSaved` |
| `m_vecCachedRenderMins` | Vector | `MNotSaved` |
| `m_vecCachedRenderMaxs` | Vector | `MNotSaved` |

### C_DynamicPropAlias_cable_dynamic

**Inherits from:** [C_DynamicProp](client.md#c_dynamicprop)

**Relationships:**

```mermaid
classDiagram
    C_DynamicProp <|-- C_DynamicPropAlias_cable_dynamic
    C_BreakableProp <|-- C_DynamicProp
    CBaseProp <|-- C_BreakableProp
    CBaseAnimGraph <|-- CBaseProp
    C_BaseModelEntity <|-- CBaseAnimGraph
```

### C_DynamicPropAlias_dynamic_prop

**Inherits from:** [C_DynamicProp](client.md#c_dynamicprop)

**Relationships:**

```mermaid
classDiagram
    C_DynamicProp <|-- C_DynamicPropAlias_dynamic_prop
    C_BreakableProp <|-- C_DynamicProp
    CBaseProp <|-- C_BreakableProp
    CBaseAnimGraph <|-- CBaseProp
    C_BaseModelEntity <|-- CBaseAnimGraph
```

### C_DynamicPropAlias_prop_dynamic_override

**Inherits from:** [C_DynamicProp](client.md#c_dynamicprop)

**Relationships:**

```mermaid
classDiagram
    C_DynamicProp <|-- C_DynamicPropAlias_prop_dynamic_override
    C_BreakableProp <|-- C_DynamicProp
    CBaseProp <|-- C_BreakableProp
    CBaseAnimGraph <|-- CBaseProp
    C_BaseModelEntity <|-- CBaseAnimGraph
```

### C_EconEntity

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph), [IHasAttributes](server.md#ihasattributes)

**Derived by:** [C_BasePlayerWeapon](client.md#c_baseplayerweapon), [C_EconWearable](client.md#c_econwearable), [C_Item](client.md#c_item)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_EconEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_EconEntity <|-- C_BasePlayerWeapon
    C_EconEntity <|-- C_EconWearable
    C_EconEntity <|-- C_Item
    C_EconEntity *-- C_AttributeContainer
    C_EconEntity --> CBaseAnimGraph
    C_EconEntity --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flFlexDelayTime` | float32 |  |
| `m_flFlexDelayedWeight` | float32* |  |
| `m_bAttributesInitialized` | bool |  |
| `m_AttributeManager` | [C_AttributeContainer](../schemas/client.md#c_attributecontainer) |  |
| `m_OriginalOwnerXuidLow` | uint32 |  |
| `m_OriginalOwnerXuidHigh` | uint32 |  |
| `m_nFallbackPaintKit` | int32 |  |
| `m_nFallbackSeed` | int32 |  |
| `m_flFallbackWear` | float32 |  |
| `m_nFallbackStatTrak` | int32 |  |
| `m_bClientside` | bool |  |
| `m_bParticleSystemsCreated` | bool |  |
| `m_vecAttachedParticles` | CUtlVector< int32 > |  |
| `m_hViewmodelAttachment` | CHandle< [CBaseAnimGraph](../schemas/client.md#cbaseanimgraph) > |  |
| `m_iOldTeam` | int32 |  |
| `m_bAttachmentDirty` | bool |  |
| `m_nUnloadedModelIndex` | int32 |  |
| `m_iNumOwnerValidationRetries` | int32 |  |
| `m_hOldProvidee` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_vecAttachedModels` | CUtlVector< [C_EconEntity](../schemas/client.md#c_econentity)::AttachedModelData_t > |  |

### C_EconEntity::AttachedModelData_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iModelDisplayFlags` | int32 |  |

### C_EconItemView

**Inherits from:** [IEconItemInterface](server.md#ieconiteminterface)

**Relationships:**

```mermaid
classDiagram
    IEconItemInterface <|-- C_EconItemView
    C_EconItemView *-- CAttributeList
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bInventoryImageRgbaRequested` | bool |  |
| `m_bInventoryImageTriedCache` | bool |  |
| `m_nInventoryImageRgbaWidth` | int32 |  |
| `m_nInventoryImageRgbaHeight` | int32 |  |
| `m_szCurrentLoadCachedFileName` | char[260] |  |
| `m_bRestoreCustomMaterialAfterPrecache` | bool |  |
| `m_iItemDefinitionIndex` | uint16 |  |
| `m_iEntityQuality` | int32 |  |
| `m_iEntityLevel` | uint32 |  |
| `m_iItemID` | uint64 |  |
| `m_iItemIDHigh` | uint32 |  |
| `m_iItemIDLow` | uint32 |  |
| `m_iAccountID` | uint32 |  |
| `m_iInventoryPosition` | uint32 |  |
| `m_bInitialized` | bool |  |
| `m_bDisallowSOC` | bool |  |
| `m_bIsStoreItem` | bool |  |
| `m_bIsTradeItem` | bool |  |
| `m_iEntityQuantity` | int32 |  |
| `m_iRarityOverride` | int32 |  |
| `m_iQualityOverride` | int32 |  |
| `m_iOriginOverride` | int32 |  |
| `m_ubStyleOverride` | uint8 |  |
| `m_unClientFlags` | uint8 |  |
| `m_AttributeList` | [CAttributeList](../schemas/client.md#cattributelist) |  |
| `m_NetworkedDynamicAttributes` | [CAttributeList](../schemas/client.md#cattributelist) |  |
| `m_szCustomName` | char[161] |  |
| `m_szCustomNameOverride` | char[161] |  |
| `m_bInitializedTags` | bool |  |

### C_EconWearable

**Inherits from:** [C_EconEntity](client.md#c_econentity)

**Relationships:**

```mermaid
classDiagram
    C_EconEntity <|-- C_EconWearable
    CBaseAnimGraph <|-- C_EconEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nForceSkin` | int32 |  |
| `m_bAlwaysAllow` | bool |  |

### C_EntityDissolve

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_EntityDissolve
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_EntityDissolve *-- GameTime_t
    C_EntityDissolve *-- EntityDissolveType_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `m_flFadeInStart` | float32 | `MNotSaved` |
| `m_flFadeInLength` | float32 | `MNotSaved` |
| `m_flFadeOutModelStart` | float32 | `MNotSaved` |
| `m_flFadeOutModelLength` | float32 | `MNotSaved` |
| `m_flFadeOutStart` | float32 | `MNotSaved` |
| `m_flFadeOutLength` | float32 | `MNotSaved` |
| `m_flNextSparkTime` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `m_nDissolveType` | [EntityDissolveType_t](../schemas/!GlobalTypes.md#entitydissolvetype_t) | `MNotSaved` |
| `m_vDissolverOrigin` | VectorWS | `MNotSaved` |
| `m_nMagnitude` | uint32 | `MNotSaved` |
| `m_bCoreExplode` | bool | `MNotSaved` |
| `m_bLinkedToServerEnt` | bool | `MNotSaved` |

### C_EntityFlame

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_EntityFlame
    CEntityInstance <|-- C_BaseEntity
    C_EntityFlame --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hEntAttached` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_hOldAttached` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_bCheapEffect` | bool |  |

### C_EnvCombinedLightProbeVolume

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [C_EnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume](client.md#c_envcombinedlightprobevolumealias_func_combined_light_probe_volume)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_EnvCombinedLightProbeVolume
    CEntityInstance <|-- C_BaseEntity
    C_EnvCombinedLightProbeVolume <|-- C_EnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume
    C_EnvCombinedLightProbeVolume *-- InfoForResourceTypeCTextureBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Entity_Color` | Color |  |
| `m_Entity_flBrightness` | float32 |  |
| `m_Entity_hCubemapTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_bCustomCubemapTexture` | bool |  |
| `m_Entity_hLightProbeTexture_AmbientCube` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeTexture_SDF` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeTexture_SH2_DC` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeTexture_SH2_R` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeTexture_SH2_G` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeTexture_SH2_B` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeDirectLightIndicesTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeDirectLightScalarsTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeDirectLightShadowsTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_vBoxMins` | Vector |  |
| `m_Entity_vBoxMaxs` | Vector |  |
| `m_Entity_bMoveable` | bool |  |
| `m_Entity_nHandshake` | int32 |  |
| `m_Entity_nEnvCubeMapArrayIndex` | int32 |  |
| `m_Entity_nPriority` | int32 |  |
| `m_Entity_bStartDisabled` | bool |  |
| `m_Entity_flEdgeFadeDist` | float32 |  |
| `m_Entity_vEdgeFadeDists` | Vector |  |
| `m_Entity_nLightProbeSizeX` | int32 |  |
| `m_Entity_nLightProbeSizeY` | int32 |  |
| `m_Entity_nLightProbeSizeZ` | int32 |  |
| `m_Entity_nLightProbeAtlasX` | int32 |  |
| `m_Entity_nLightProbeAtlasY` | int32 |  |
| `m_Entity_nLightProbeAtlasZ` | int32 |  |
| `m_Entity_bEnabled` | bool |  |

### C_EnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume

**Inherits from:** [C_EnvCombinedLightProbeVolume](client.md#c_envcombinedlightprobevolume)

**Relationships:**

```mermaid
classDiagram
    C_EnvCombinedLightProbeVolume <|-- C_EnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume
    C_BaseEntity <|-- C_EnvCombinedLightProbeVolume
    CEntityInstance <|-- C_BaseEntity
```

### C_EnvCubemap

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [C_EnvCubemapBox](client.md#c_envcubemapbox)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_EnvCubemap
    CEntityInstance <|-- C_BaseEntity
    C_EnvCubemap <|-- C_EnvCubemapBox
    C_EnvCubemap *-- InfoForResourceTypeCTextureBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Entity_hCubemapTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_bCustomCubemapTexture` | bool |  |
| `m_Entity_flInfluenceRadius` | float32 |  |
| `m_Entity_vBoxProjectMins` | Vector |  |
| `m_Entity_vBoxProjectMaxs` | Vector |  |
| `m_Entity_bMoveable` | bool |  |
| `m_Entity_nHandshake` | int32 |  |
| `m_Entity_nEnvCubeMapArrayIndex` | int32 |  |
| `m_Entity_nPriority` | int32 |  |
| `m_Entity_flEdgeFadeDist` | float32 |  |
| `m_Entity_vEdgeFadeDists` | Vector |  |
| `m_Entity_flDiffuseScale` | float32 |  |
| `m_Entity_bStartDisabled` | bool |  |
| `m_Entity_bDefaultEnvMap` | bool |  |
| `m_Entity_bDefaultSpecEnvMap` | bool |  |
| `m_Entity_bIndoorCubeMap` | bool |  |
| `m_Entity_bCopyDiffuseFromDefaultCubemap` | bool |  |
| `m_Entity_bEnabled` | bool |  |

### C_EnvCubemapBox

**Inherits from:** [C_EnvCubemap](client.md#c_envcubemap)

**Relationships:**

```mermaid
classDiagram
    C_EnvCubemap <|-- C_EnvCubemapBox
    C_BaseEntity <|-- C_EnvCubemap
    CEntityInstance <|-- C_BaseEntity
```

### C_EnvCubemapFog

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_EnvCubemapFog
    CEntityInstance <|-- C_BaseEntity
    C_EnvCubemapFog *-- InfoForResourceTypeIMaterial2
    C_EnvCubemapFog *-- InfoForResourceTypeCTextureBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flEndDistance` | float32 |  |
| `m_flStartDistance` | float32 |  |
| `m_flFogFalloffExponent` | float32 |  |
| `m_bHeightFogEnabled` | bool |  |
| `m_flFogHeightWidth` | float32 |  |
| `m_flFogHeightEnd` | float32 |  |
| `m_flFogHeightStart` | float32 |  |
| `m_flFogHeightExponent` | float32 |  |
| `m_flLODBias` | float32 |  |
| `m_bActive` | bool |  |
| `m_bStartDisabled` | bool |  |
| `m_flFogMaxOpacity` | float32 |  |
| `m_nCubemapSourceType` | int32 |  |
| `m_hSkyMaterial` | CStrongHandle< [InfoForResourceTypeIMaterial2](../schemas/resourcesystem.md#infoforresourcetypeimaterial2) > |  |
| `m_iszSkyEntity` | CUtlSymbolLarge |  |
| `m_nHeightFogType` | int32 |  |
| `m_nFogHeightBlendMode` | int32 |  |
| `m_nFogHeightCoordinateSpace` | int32 |  |
| `m_nDistanceFogType` | int32 |  |
| `m_DistanceFogCurveString` | CUtlSymbolLarge |  |
| `m_HeightFogCurveString` | CUtlSymbolLarge |  |
| `m_hFogCubemapTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_bHasHeightFogEnd` | bool |  |
| `m_bFirstTime` | bool |  |

### C_EnvDecal

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_EnvDecal
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_EnvDecal *-- InfoForResourceTypeIMaterial2
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hDecalMaterial` | CStrongHandle< [InfoForResourceTypeIMaterial2](../schemas/resourcesystem.md#infoforresourcetypeimaterial2) > |  |
| `m_flWidth` | float32 |  |
| `m_flHeight` | float32 |  |
| `m_flDepth` | float32 |  |
| `m_nRenderOrder` | uint32 |  |
| `m_bProjectOnWorld` | bool |  |
| `m_bProjectOnCharacters` | bool |  |
| `m_bProjectOnWater` | bool |  |
| `m_flDepthSortBias` | float32 |  |

### C_EnvDetailController

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_EnvDetailController
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flFadeStartDist` | float32 |  |
| `m_flFadeEndDist` | float32 |  |

### C_EnvLightProbeVolume

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_EnvLightProbeVolume
    CEntityInstance <|-- C_BaseEntity
    C_EnvLightProbeVolume *-- InfoForResourceTypeCTextureBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Entity_hLightProbeTexture_AmbientCube` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeTexture_SDF` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeTexture_SH2_DC` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeTexture_SH2_R` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeTexture_SH2_G` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeTexture_SH2_B` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeDirectLightIndicesTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeDirectLightScalarsTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_hLightProbeDirectLightShadowsTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_Entity_vBoxMins` | Vector |  |
| `m_Entity_vBoxMaxs` | Vector |  |
| `m_Entity_bMoveable` | bool |  |
| `m_Entity_nHandshake` | int32 |  |
| `m_Entity_nPriority` | int32 |  |
| `m_Entity_bStartDisabled` | bool |  |
| `m_Entity_nLightProbeSizeX` | int32 |  |
| `m_Entity_nLightProbeSizeY` | int32 |  |
| `m_Entity_nLightProbeSizeZ` | int32 |  |
| `m_Entity_nLightProbeAtlasX` | int32 |  |
| `m_Entity_nLightProbeAtlasY` | int32 |  |
| `m_Entity_nLightProbeAtlasZ` | int32 |  |
| `m_Entity_bEnabled` | bool |  |

### C_EnvParticleGlow

**Inherits from:** [C_ParticleSystem](client.md#c_particlesystem)

**Relationships:**

```mermaid
classDiagram
    C_ParticleSystem <|-- C_EnvParticleGlow
    C_BaseModelEntity <|-- C_ParticleSystem
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_EnvParticleGlow *-- InfoForResourceTypeCTextureBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flAlphaScale` | float32 |  |
| `m_flRadiusScale` | float32 |  |
| `m_flSelfIllumScale` | float32 |  |
| `m_ColorTint` | Color |  |
| `m_hTextureOverride` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |

### C_EnvSky

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_EnvSky
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_EnvSky *-- InfoForResourceTypeIMaterial2
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hSkyMaterial` | CStrongHandle< [InfoForResourceTypeIMaterial2](../schemas/resourcesystem.md#infoforresourcetypeimaterial2) > |  |
| `m_hSkyMaterialLightingOnly` | CStrongHandle< [InfoForResourceTypeIMaterial2](../schemas/resourcesystem.md#infoforresourcetypeimaterial2) > |  |
| `m_bStartDisabled` | bool |  |
| `m_vTintColor` | Color |  |
| `m_vTintColorLightingOnly` | Color |  |
| `m_flBrightnessScale` | float32 |  |
| `m_nFogType` | int32 |  |
| `m_flFogMinStart` | float32 |  |
| `m_flFogMinEnd` | float32 |  |
| `m_flFogMaxStart` | float32 |  |
| `m_flFogMaxEnd` | float32 |  |
| `m_bEnabled` | bool |  |

### C_EnvVolumetricFogController

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_EnvVolumetricFogController
    CEntityInstance <|-- C_BaseEntity
    C_EnvVolumetricFogController *-- GameTime_t
    C_EnvVolumetricFogController *-- InfoForResourceTypeCTextureBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flScattering` | float32 |  |
| `m_TintColor` | Color |  |
| `m_flAnisotropy` | float32 |  |
| `m_flFadeSpeed` | float32 |  |
| `m_flDrawDistance` | float32 |  |
| `m_flFadeInStart` | float32 |  |
| `m_flFadeInEnd` | float32 |  |
| `m_flIndirectStrength` | float32 |  |
| `m_nVolumeDepth` | int32 |  |
| `m_fFirstVolumeSliceThickness` | float32 |  |
| `m_nIndirectTextureDimX` | int32 |  |
| `m_nIndirectTextureDimY` | int32 |  |
| `m_nIndirectTextureDimZ` | int32 |  |
| `m_vBoxMins` | Vector |  |
| `m_vBoxMaxs` | Vector |  |
| `m_bActive` | bool |  |
| `m_flStartAnisoTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flStartScatterTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flStartDrawDistanceTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flStartAnisotropy` | float32 |  |
| `m_flStartScattering` | float32 |  |
| `m_flStartDrawDistance` | float32 |  |
| `m_flDefaultAnisotropy` | float32 |  |
| `m_flDefaultScattering` | float32 |  |
| `m_flDefaultDrawDistance` | float32 |  |
| `m_bStartDisabled` | bool |  |
| `m_bEnableIndirect` | bool |  |
| `m_bIsMaster` | bool |  |
| `m_hFogIndirectTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_nForceRefreshCount` | int32 |  |
| `m_fNoiseSpeed` | float32 |  |
| `m_fNoiseStrength` | float32 |  |
| `m_vNoiseScale` | Vector |  |
| `m_fWindSpeed` | float32 |  |
| `m_vWindDirection` | Vector |  |
| `m_bFirstTime` | bool |  |

### C_EnvVolumetricFogVolume

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_EnvVolumetricFogVolume
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bActive` | bool |  |
| `m_vBoxMins` | Vector |  |
| `m_vBoxMaxs` | Vector |  |
| `m_bStartDisabled` | bool |  |
| `m_bIndirectUseLPVs` | bool |  |
| `m_flStrength` | float32 |  |
| `m_nFalloffShape` | int32 |  |
| `m_flFalloffExponent` | float32 |  |
| `m_flHeightFogDepth` | float32 |  |
| `m_fHeightFogEdgeWidth` | float32 |  |
| `m_fIndirectLightStrength` | float32 |  |
| `m_fSunLightStrength` | float32 |  |
| `m_fNoiseStrength` | float32 |  |
| `m_TintColor` | Color |  |
| `m_bOverrideTintColor` | bool |  |
| `m_bOverrideIndirectLightStrength` | bool |  |
| `m_bOverrideSunLightStrength` | bool |  |
| `m_bOverrideNoiseStrength` | bool |  |

### C_EnvWind

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_EnvWind
    CEntityInstance <|-- C_BaseEntity
    C_EnvWind *-- C_EnvWindShared
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_EnvWindShared` | [C_EnvWindShared](../schemas/client.md#c_envwindshared) | `MNotSaved` |

### C_EnvWindClientside

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_EnvWindClientside
    CEntityInstance <|-- C_BaseEntity
    C_EnvWindClientside *-- C_EnvWindShared
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_EnvWindShared` | [C_EnvWindShared](../schemas/client.md#c_envwindshared) | `MNotSaved` |

### C_EnvWindController

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_EnvWindController
    CEntityInstance <|-- C_BaseEntity
    C_EnvWindController *-- C_EnvWindShared
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_EnvWindShared` | [C_EnvWindShared](../schemas/client.md#c_envwindshared) |  |
| `m_fDirectionVariation` | float32 |  |
| `m_fSpeedVariation` | float32 |  |
| `m_fTurbulence` | float32 |  |
| `m_fVolumeHalfExtentXY` | float32 |  |
| `m_fVolumeHalfExtentZ` | float32 |  |
| `m_nVolumeResolutionXY` | int32 |  |
| `m_nVolumeResolutionZ` | int32 |  |
| `m_nClipmapLevels` | int32 |  |
| `m_bIsMaster` | bool |  |
| `m_bFirstTime` | bool |  |

### C_EnvWindShared

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "C_EnvWindShared",
	"m_iMinWind": 0,
	"m_iMaxWind": 0,
	"m_windRadius": 0,
	"m_iMinGust": 0,
	"m_iMaxGust": 0,
	"m_flMinGustDelay": 0.000000,
	"m_flMaxGustDelay": 0.000000,
	"m_flGustDuration": 0.000000,
	"m_iGustDirChange": 0
}`

**Relationships:**

```mermaid
classDiagram
    C_EnvWindShared *-- GameTime_t
    C_EnvWindShared --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `m_iWindSeed` | uint32 | `MNotSaved` |
| `m_iMinWind` | uint16 |  |
| `m_iMaxWind` | uint16 |  |
| `m_windRadius` | int32 |  |
| `m_iMinGust` | uint16 |  |
| `m_iMaxGust` | uint16 |  |
| `m_flMinGustDelay` | float32 |  |
| `m_flMaxGustDelay` | float32 |  |
| `m_flGustDuration` | float32 |  |
| `m_iGustDirChange` | uint16 |  |
| `m_iInitialWindDir` | uint16 | `MNotSaved` |
| `m_flInitialWindSpeed` | float32 | `MNotSaved` |
| `m_location` | VectorWS | `MNotSaved` |
| `m_hEntOwner` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > | `MNotSaved` |

### C_EnvWindVolume

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_EnvWindVolume
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bActive` | bool |  |
| `m_vBoxMins` | Vector |  |
| `m_vBoxMaxs` | Vector |  |
| `m_bStartDisabled` | bool |  |
| `m_nShape` | int32 |  |
| `m_fWindSpeedMultiplier` | float32 |  |
| `m_fWindTurbulenceMultiplier` | float32 |  |
| `m_fWindSpeedVariationMultiplier` | float32 |  |
| `m_fWindDirectionVariationMultiplier` | float32 |  |

### C_FireCrackerBlast

**Inherits from:** [C_Inferno](client.md#c_inferno)

**Relationships:**

```mermaid
classDiagram
    C_Inferno <|-- C_FireCrackerBlast
    C_BaseModelEntity <|-- C_Inferno
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_Fish

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_Fish
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_Fish *-- CountdownTimer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_pos` | VectorWS | `MNotSaved` |
| `m_vel` | Vector | `MNotSaved` |
| `m_angles` | QAngle | `MNotSaved` |
| `m_localLifeState` | int32 | `MNotSaved` |
| `m_deathDepth` | float32 | `MNotSaved` |
| `m_deathAngle` | float32 | `MNotSaved` |
| `m_buoyancy` | float32 | `MNotSaved` |
| `m_wiggleTimer` | [CountdownTimer](../schemas/client.md#countdowntimer) | `MNotSaved` |
| `m_wigglePhase` | float32 | `MNotSaved` |
| `m_wiggleRate` | float32 | `MNotSaved` |
| `m_actualPos` | VectorWS | `MNotSaved` |
| `m_actualAngles` | QAngle | `MNotSaved` |
| `m_poolOrigin` | VectorWS | `MNotSaved` |
| `m_waterLevel` | float32 | `MNotSaved` |
| `m_gotUpdate` | bool | `MNotSaved` |
| `m_x` | float32 | `MNotSaved` |
| `m_y` | float32 | `MNotSaved` |
| `m_z` | float32 | `MNotSaved` |
| `m_angle` | float32 | `MNotSaved` |
| `m_errorHistory` | float32[20] | `MNotSaved` |
| `m_errorHistoryIndex` | int32 | `MNotSaved` |
| `m_errorHistoryCount` | int32 | `MNotSaved` |
| `m_averageError` | float32 | `MNotSaved` |

### C_Flashbang

**Inherits from:** [C_BaseCSGrenade](client.md#c_basecsgrenade)

**Relationships:**

```mermaid
classDiagram
    C_BaseCSGrenade <|-- C_Flashbang
    C_CSWeaponBase <|-- C_BaseCSGrenade
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_FlashbangProjectile

**Inherits from:** [C_BaseCSGrenadeProjectile](client.md#c_basecsgrenadeprojectile)

**Relationships:**

```mermaid
classDiagram
    C_BaseCSGrenadeProjectile <|-- C_FlashbangProjectile
    C_BaseGrenade <|-- C_BaseCSGrenadeProjectile
    CBaseAnimGraph <|-- C_BaseGrenade
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
```

### C_FogController

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_FogController
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_fog` | fogparams_t | `MNotSaved` |
| `m_bUseAngles` | bool |  |
| `m_iChangedVariables` | int32 |  |

### C_FootstepControl

**Inherits from:** [C_BaseTrigger](client.md#c_basetrigger)

**Relationships:**

```mermaid
classDiagram
    C_BaseTrigger <|-- C_FootstepControl
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_source` | CUtlSymbolLarge |  |
| `m_destination` | CUtlSymbolLarge |  |

### C_FuncBrush

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Derived by:** [C_FuncElectrifiedVolume](client.md#c_funcelectrifiedvolume), [C_FuncMonitor](client.md#c_funcmonitor)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_FuncBrush
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_FuncBrush <|-- C_FuncElectrifiedVolume
    C_FuncBrush <|-- C_FuncMonitor
```

### C_FuncConveyor

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_FuncConveyor
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_FuncConveyor *-- GameTick_t
    C_FuncConveyor --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vecMoveDirEntitySpace` | Vector |  |
| `m_flTargetSpeed` | float32 |  |
| `m_nTransitionStartTick` | [GameTick_t](../schemas/entity2.md#gametick_t) |  |
| `m_nTransitionDurationTicks` | int32 |  |
| `m_flTransitionStartSpeed` | float32 |  |
| `m_hConveyorModels` | C_NetworkUtlVectorBase< CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > > |  |
| `m_flCurrentConveyorOffset` | float32 |  |
| `m_flCurrentConveyorSpeed` | float32 |  |

### C_FuncElectrifiedVolume

**Inherits from:** [C_FuncBrush](client.md#c_funcbrush)

**Relationships:**

```mermaid
classDiagram
    C_FuncBrush <|-- C_FuncElectrifiedVolume
    C_BaseModelEntity <|-- C_FuncBrush
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_FuncElectrifiedVolume *-- ParticleIndex_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nAmbientEffect` | [ParticleIndex_t](../schemas/server.md#particleindex_t) | `MNotSaved` |
| `m_EffectName` | CUtlSymbolLarge | `MNotSaved` |
| `m_bState` | bool | `MNotSaved` |

### C_FuncLadder

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_FuncLadder
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_FuncLadder --> C_InfoLadderDismount
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vecLadderDir` | Vector |  |
| `m_Dismounts` | CUtlVector< CHandle< [C_InfoLadderDismount](../schemas/client.md#c_infoladderdismount) > > | `MNotSaved` |
| `m_vecLocalTop` | Vector |  |
| `m_vecPlayerMountPositionTop` | VectorWS |  |
| `m_vecPlayerMountPositionBottom` | VectorWS |  |
| `m_flAutoRideSpeed` | float32 |  |
| `m_bDisabled` | bool |  |
| `m_bFakeLadder` | bool |  |
| `m_bHasSlack` | bool |  |

### C_FuncMonitor

**Inherits from:** [C_FuncBrush](client.md#c_funcbrush)

**Relationships:**

```mermaid
classDiagram
    C_FuncBrush <|-- C_FuncMonitor
    C_BaseModelEntity <|-- C_FuncBrush
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_FuncMonitor --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_targetCamera` | CUtlString |  |
| `m_nResolutionEnum` | int32 |  |
| `m_bRenderShadows` | bool |  |
| `m_bUseUniqueColorTarget` | bool |  |
| `m_brushModelName` | CUtlString |  |
| `m_hTargetCamera` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_bEnabled` | bool |  |
| `m_bDraw3DSkybox` | bool |  |

### C_FuncMoveLinear

**Inherits from:** [C_BaseToggle](client.md#c_basetoggle)

**Relationships:**

```mermaid
classDiagram
    C_BaseToggle <|-- C_FuncMoveLinear
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_FuncMover

**Inherits from:** [C_BaseToggle](client.md#c_basetoggle)

**Relationships:**

```mermaid
classDiagram
    C_BaseToggle <|-- C_FuncMover
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_FuncRotating

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_FuncRotating
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_FuncTrackTrain

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_FuncTrackTrain
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nLongAxis` | int32 | `MNotSaved` |
| `m_flRadius` | float32 | `MNotSaved` |
| `m_flLineLength` | float32 | `MNotSaved` |

### C_GameRules

**Derived by:** [C_MultiplayRules](client.md#c_multiplayrules), [C_SingleplayRules](client.md#c_singleplayrules)

**Relationships:**

```mermaid
classDiagram
    C_GameRules <|-- C_MultiplayRules
    C_GameRules <|-- C_SingleplayRules
    C_GameRules *-- CNetworkVarChainer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `__m_pChainEntity` | [CNetworkVarChainer](../schemas/entity2.md#cnetworkvarchainer) | `MNotSaved` |
| `m_nTotalPausedTicks` | int32 |  |
| `m_nPauseStartTick` | int32 |  |
| `m_bGamePaused` | bool |  |

### C_GameRulesProxy

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [C_CSGameRulesProxy](client.md#c_csgamerulesproxy)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_GameRulesProxy
    CEntityInstance <|-- C_BaseEntity
    C_GameRulesProxy <|-- C_CSGameRulesProxy
```

### C_GlobalLight

**Inherits from:** [C_BaseEntity](client.md#c_baseentity), [CGlobalLightBase](client.md#cgloballightbase)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_GlobalLight
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_WindClothForceHandle` | uint16 | `MNotSaved` |

### C_GradientFog

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_GradientFog
    CEntityInstance <|-- C_BaseEntity
    C_GradientFog *-- InfoForResourceTypeCTextureBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hGradientFogTexture` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_flFogStartDistance` | float32 |  |
| `m_flFogEndDistance` | float32 |  |
| `m_bHeightFogEnabled` | bool |  |
| `m_flFogStartHeight` | float32 |  |
| `m_flFogEndHeight` | float32 |  |
| `m_flFarZ` | float32 |  |
| `m_flFogMaxOpacity` | float32 |  |
| `m_flFogFalloffExponent` | float32 |  |
| `m_flFogVerticalExponent` | float32 |  |
| `m_fogColor` | Color |  |
| `m_flFogStrength` | float32 |  |
| `m_flFadeTime` | float32 |  |
| `m_bStartDisabled` | bool |  |
| `m_bIsEnabled` | bool |  |
| `m_bGradientFogNeedsTextures` | bool |  |

### C_HEGrenade

**Inherits from:** [C_BaseCSGrenade](client.md#c_basecsgrenade)

**Relationships:**

```mermaid
classDiagram
    C_BaseCSGrenade <|-- C_HEGrenade
    C_CSWeaponBase <|-- C_BaseCSGrenade
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_HEGrenadeProjectile

**Inherits from:** [C_BaseCSGrenadeProjectile](client.md#c_basecsgrenadeprojectile)

**Relationships:**

```mermaid
classDiagram
    C_BaseCSGrenadeProjectile <|-- C_HEGrenadeProjectile
    C_BaseGrenade <|-- C_BaseCSGrenadeProjectile
    CBaseAnimGraph <|-- C_BaseGrenade
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
```

### C_HandleTest

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_HandleTest
    CEntityInstance <|-- C_BaseEntity
    C_HandleTest --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Handle` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_bSendHandle` | bool |  |

### C_Hostage

**Inherits from:** [C_BaseCombatCharacter](client.md#c_basecombatcharacter)

**Relationships:**

```mermaid
classDiagram
    C_BaseCombatCharacter <|-- C_Hostage
    CBaseAnimGraph <|-- C_BaseCombatCharacter
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_Hostage *-- EntitySpottedState_t
    C_Hostage --> C_BaseEntity
    C_Hostage *-- CountdownTimer
    C_Hostage --> C_CSPlayerPawn
    C_Hostage *-- GameTime_t
    C_Hostage *-- AttachmentHandle_t
    C_Hostage --> CBasePlayerController
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_entitySpottedState` | [EntitySpottedState_t](../schemas/client.md#entityspottedstate_t) |  |
| `m_leader` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_reuseTimer` | [CountdownTimer](../schemas/client.md#countdowntimer) |  |
| `m_vel` | Vector |  |
| `m_isRescued` | bool |  |
| `m_jumpedThisFrame` | bool |  |
| `m_nHostageState` | int32 |  |
| `m_bHandsHaveBeenCut` | bool |  |
| `m_hHostageGrabber` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |
| `m_fLastGrabTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_vecGrabbedPos` | VectorWS |  |
| `m_flRescueStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flGrabSuccessTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flDropStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flDeadOrRescuedTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_blinkTimer` | [CountdownTimer](../schemas/client.md#countdowntimer) |  |
| `m_lookAt` | VectorWS |  |
| `m_lookAroundTimer` | [CountdownTimer](../schemas/client.md#countdowntimer) |  |
| `m_isInit` | bool |  |
| `m_eyeAttachment` | [AttachmentHandle_t](../schemas/modellib.md#attachmenthandle_t) |  |
| `m_chestAttachment` | [AttachmentHandle_t](../schemas/modellib.md#attachmenthandle_t) |  |
| `m_pPredictionOwner` | [CBasePlayerController](../schemas/client.md#cbaseplayercontroller)* |  |
| `m_fNewestAlphaThinkTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |

### C_HostageCarriableProp

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_HostageCarriableProp
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_IncendiaryGrenade

**Inherits from:** [C_MolotovGrenade](client.md#c_molotovgrenade)

**Relationships:**

```mermaid
classDiagram
    C_MolotovGrenade <|-- C_IncendiaryGrenade
    C_BaseCSGrenade <|-- C_MolotovGrenade
    C_CSWeaponBase <|-- C_BaseCSGrenade
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
```

### C_Inferno

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Derived by:** [C_FireCrackerBlast](client.md#c_firecrackerblast)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_Inferno
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_Inferno <|-- C_FireCrackerBlast
    C_Inferno *-- ParticleIndex_t
    C_Inferno *-- InfoForResourceTypeIParticleSnapshot
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nfxFireDamageEffect` | [ParticleIndex_t](../schemas/server.md#particleindex_t) |  |
| `m_hInfernoPointsSnapshot` | CStrongHandle< [InfoForResourceTypeIParticleSnapshot](../schemas/resourcesystem.md#infoforresourcetypeiparticlesnapshot) > |  |
| `m_hInfernoFillerPointsSnapshot` | CStrongHandle< [InfoForResourceTypeIParticleSnapshot](../schemas/resourcesystem.md#infoforresourcetypeiparticlesnapshot) > |  |
| `m_hInfernoOutlinePointsSnapshot` | CStrongHandle< [InfoForResourceTypeIParticleSnapshot](../schemas/resourcesystem.md#infoforresourcetypeiparticlesnapshot) > |  |
| `m_hInfernoClimbingOutlinePointsSnapshot` | CStrongHandle< [InfoForResourceTypeIParticleSnapshot](../schemas/resourcesystem.md#infoforresourcetypeiparticlesnapshot) > |  |
| `m_hInfernoDecalsSnapshot` | CStrongHandle< [InfoForResourceTypeIParticleSnapshot](../schemas/resourcesystem.md#infoforresourcetypeiparticlesnapshot) > |  |
| `m_firePositions` | VectorWS[64] |  |
| `m_fireParentPositions` | VectorWS[64] |  |
| `m_bFireIsBurning` | bool[64] |  |
| `m_BurnNormal` | Vector[64] |  |
| `m_fireCount` | int32 |  |
| `m_nInfernoType` | int32 |  |
| `m_nFireLifetime` | float32 |  |
| `m_bInPostEffectTime` | bool |  |
| `m_lastFireCount` | int32 |  |
| `m_nFireEffectTickBegin` | int32 |  |
| `m_drawableCount` | int32 |  |
| `m_blosCheck` | bool |  |
| `m_nlosperiod` | int32 |  |
| `m_maxFireHalfWidth` | float32 |  |
| `m_maxFireHeight` | float32 |  |
| `m_minBounds` | VectorWS |  |
| `m_maxBounds` | VectorWS |  |
| `m_flLastGrassBurnThink` | float32 |  |

### C_InfoInstructorHintHostageRescueZone

**Inherits from:** [C_PointEntity](client.md#c_pointentity)

**Relationships:**

```mermaid
classDiagram
    C_PointEntity <|-- C_InfoInstructorHintHostageRescueZone
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_InfoLadderDismount

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_InfoLadderDismount
    CEntityInstance <|-- C_BaseEntity
```

### C_InfoVisibilityBox

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_InfoVisibilityBox
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nMode` | int32 |  |
| `m_vBoxSize` | Vector |  |
| `m_bEnabled` | bool |  |

### C_IronSightController

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bIronSightAvailable` | bool |  |
| `m_flIronSightAmount` | float32 |  |
| `m_flIronSightAmountGained` | float32 |  |
| `m_flIronSightAmountBiased` | float32 |  |
| `m_flIronSightAmount_Interpolated` | float32 |  |
| `m_flIronSightAmountGained_Interpolated` | float32 |  |
| `m_flIronSightAmountBiased_Interpolated` | float32 |  |
| `m_flInterpolationLastUpdated` | float32 |  |
| `m_angDeltaAverage` | QAngle[8] |  |
| `m_angViewLast` | QAngle |  |
| `m_vecDotCoords` | Vector2D |  |
| `m_flFiringInaccuracyExtraWidthMultiplier` | float32 |  |
| `m_flSpeedRatio` | float32 |  |

### C_Item

**Inherits from:** [C_EconEntity](client.md#c_econentity)

**Derived by:** [C_ItemDogtags](client.md#c_itemdogtags)

**Relationships:**

```mermaid
classDiagram
    C_EconEntity <|-- C_Item
    CBaseAnimGraph <|-- C_EconEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_Item <|-- C_ItemDogtags
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_pReticleHintTextName` | char[256] |  |

### C_ItemDogtags

**Inherits from:** [C_Item](client.md#c_item)

**Relationships:**

```mermaid
classDiagram
    C_Item <|-- C_ItemDogtags
    C_EconEntity <|-- C_Item
    CBaseAnimGraph <|-- C_EconEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    C_ItemDogtags --> C_CSPlayerPawn
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_OwningPlayer` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |
| `m_KillingPlayer` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |

### C_Item_Healthshot

**Inherits from:** [C_WeaponBaseItem](client.md#c_weaponbaseitem)

**Relationships:**

```mermaid
classDiagram
    C_WeaponBaseItem <|-- C_Item_Healthshot
    C_CSWeaponBase <|-- C_WeaponBaseItem
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_KeychainModule

**Inherits from:** [C_CS2WeaponModuleBase](client.md#c_cs2weaponmodulebase)

**Relationships:**

```mermaid
classDiagram
    C_CS2WeaponModuleBase <|-- C_KeychainModule
    CBaseAnimGraph <|-- C_CS2WeaponModuleBase
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nKeychainDefID` | uint32 |  |
| `m_nKeychainSeed` | uint32 |  |

### C_Knife

**Inherits from:** [C_CSWeaponBase](client.md#c_csweaponbase)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBase <|-- C_Knife
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bFirstAttack` | bool |  |

### C_LateUpdatedAnimating

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Derived by:** [C_CS2HudModelAddon](client.md#c_cs2hudmodeladdon), [C_CS2HudModelBase](client.md#c_cs2hudmodelbase)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_LateUpdatedAnimating
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_LateUpdatedAnimating <|-- C_CS2HudModelAddon
    C_LateUpdatedAnimating <|-- C_CS2HudModelBase
```

### C_LightDirectionalEntity

**Inherits from:** [C_LightEntity](client.md#c_lightentity)

**Derived by:** [C_LightEnvironmentEntity](client.md#c_lightenvironmententity)

**Relationships:**

```mermaid
classDiagram
    C_LightEntity <|-- C_LightDirectionalEntity
    C_BaseModelEntity <|-- C_LightEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_LightDirectionalEntity <|-- C_LightEnvironmentEntity
```

### C_LightEntity

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Derived by:** [C_LightDirectionalEntity](client.md#c_lightdirectionalentity), [C_LightOrthoEntity](client.md#c_lightorthoentity), [C_LightSpotEntity](client.md#c_lightspotentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_LightEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_LightEntity <|-- C_LightDirectionalEntity
    C_LightEntity <|-- C_LightOrthoEntity
    C_LightEntity <|-- C_LightSpotEntity
    C_LightEntity --> CLightComponent
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_CLightComponent` | [CLightComponent](../schemas/client.md#clightcomponent)* |  |

### C_LightEnvironmentEntity

**Inherits from:** [C_LightDirectionalEntity](client.md#c_lightdirectionalentity)

**Relationships:**

```mermaid
classDiagram
    C_LightDirectionalEntity <|-- C_LightEnvironmentEntity
    C_LightEntity <|-- C_LightDirectionalEntity
    C_BaseModelEntity <|-- C_LightEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_LightOrthoEntity

**Inherits from:** [C_LightEntity](client.md#c_lightentity)

**Relationships:**

```mermaid
classDiagram
    C_LightEntity <|-- C_LightOrthoEntity
    C_BaseModelEntity <|-- C_LightEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_LightSpotEntity

**Inherits from:** [C_LightEntity](client.md#c_lightentity)

**Relationships:**

```mermaid
classDiagram
    C_LightEntity <|-- C_LightSpotEntity
    C_BaseModelEntity <|-- C_LightEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_LocalTempEntity

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_LocalTempEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_LocalTempEntity *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `flags` | int32 | `MNotSaved` |
| `die` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `m_flFrameMax` | float32 | `MNotSaved` |
| `x` | float32 | `MNotSaved` |
| `y` | float32 | `MNotSaved` |
| `fadeSpeed` | float32 | `MNotSaved` |
| `bounceFactor` | float32 | `MNotSaved` |
| `hitSound` | int32 | `MNotSaved` |
| `priority` | int32 | `MNotSaved` |
| `tentOffset` | Vector | `MNotSaved` |
| `m_vecTempEntAngVelocity` | QAngle | `MNotSaved` |
| `tempent_renderamt` | int32 | `MNotSaved` |
| `m_vecNormal` | Vector | `MNotSaved` |
| `m_flSpriteScale` | float32 | `MNotSaved` |
| `m_nFlickerFrame` | int32 | `MNotSaved` |
| `m_flFrameRate` | float32 | `MNotSaved` |
| `m_flFrame` | float32 | `MNotSaved` |
| `m_pszImpactEffect` | char* | `MNotSaved` |
| `m_pszParticleEffect` | char* | `MNotSaved` |
| `m_bParticleCollision` | bool | `MNotSaved` |
| `m_iLastCollisionFrame` | int32 | `MNotSaved` |
| `m_vLastCollisionOrigin` | VectorWS | `MNotSaved` |
| `m_vecTempEntVelocity` | Vector | `MNotSaved` |
| `m_vecPrevAbsOrigin` | VectorWS | `MNotSaved` |
| `m_vecTempEntAcceleration` | Vector | `MNotSaved` |

### C_MapPreviewParticleSystem

**Inherits from:** [C_ParticleSystem](client.md#c_particlesystem)

**Relationships:**

```mermaid
classDiagram
    C_ParticleSystem <|-- C_MapPreviewParticleSystem
    C_BaseModelEntity <|-- C_ParticleSystem
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_MapVetoPickController

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_MapVetoPickController
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nDraftType` | int32 |  |
| `m_nTeamWinningCoinToss` | int32 |  |
| `m_nTeamWithFirstChoice` | int32[64] |  |
| `m_nVoteMapIdsList` | int32[7] |  |
| `m_nAccountIDs` | int32[64] |  |
| `m_nMapId0` | int32[64] |  |
| `m_nMapId1` | int32[64] |  |
| `m_nMapId2` | int32[64] |  |
| `m_nMapId3` | int32[64] |  |
| `m_nMapId4` | int32[64] |  |
| `m_nMapId5` | int32[64] |  |
| `m_nStartingSide0` | int32[64] |  |
| `m_nCurrentPhase` | int32 |  |
| `m_nPhaseStartTick` | int32 |  |
| `m_nPhaseDurationTicks` | int32 |  |
| `m_nPostDataUpdateTick` | int32 |  |
| `m_bDisabledHud` | bool |  |

### C_ModelPointEntity

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Derived by:** [C_PlayerSprayDecal](client.md#c_playerspraydecal), [C_PointWorldText](client.md#c_pointworldtext)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_ModelPointEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_ModelPointEntity <|-- C_PlayerSprayDecal
    C_ModelPointEntity <|-- C_PointWorldText
```

### C_MolotovGrenade

**Inherits from:** [C_BaseCSGrenade](client.md#c_basecsgrenade)

**Derived by:** [C_IncendiaryGrenade](client.md#c_incendiarygrenade)

**Relationships:**

```mermaid
classDiagram
    C_BaseCSGrenade <|-- C_MolotovGrenade
    C_CSWeaponBase <|-- C_BaseCSGrenade
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
    C_MolotovGrenade <|-- C_IncendiaryGrenade
```

### C_MolotovProjectile

**Inherits from:** [C_BaseCSGrenadeProjectile](client.md#c_basecsgrenadeprojectile)

**Relationships:**

```mermaid
classDiagram
    C_BaseCSGrenadeProjectile <|-- C_MolotovProjectile
    C_BaseGrenade <|-- C_BaseCSGrenadeProjectile
    CBaseAnimGraph <|-- C_BaseGrenade
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bIsIncGrenade` | bool |  |

### C_Multimeter

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_Multimeter
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_Multimeter --> C_PlantedC4
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hTargetC4` | CHandle< [C_PlantedC4](../schemas/client.md#c_plantedc4) > |  |

### C_MultiplayRules

**Inherits from:** [C_GameRules](client.md#c_gamerules)

**Derived by:** [C_TeamplayRules](client.md#c_teamplayrules)

**Relationships:**

```mermaid
classDiagram
    C_GameRules <|-- C_MultiplayRules
    C_MultiplayRules <|-- C_TeamplayRules
```

### C_NametagModule

**Inherits from:** [C_CS2WeaponModuleBase](client.md#c_cs2weaponmodulebase)

**Relationships:**

```mermaid
classDiagram
    C_CS2WeaponModuleBase <|-- C_NametagModule
    CBaseAnimGraph <|-- C_CS2WeaponModuleBase
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_strNametagString` | CUtlString |  |

### C_NetTestBaseCombatCharacter

**Inherits from:** [C_BaseCombatCharacter](client.md#c_basecombatcharacter)

**Relationships:**

```mermaid
classDiagram
    C_BaseCombatCharacter <|-- C_NetTestBaseCombatCharacter
    CBaseAnimGraph <|-- C_BaseCombatCharacter
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_OmniLight

**Inherits from:** [C_BarnLight](client.md#c_barnlight)

**Relationships:**

```mermaid
classDiagram
    C_BarnLight <|-- C_OmniLight
    C_BaseModelEntity <|-- C_BarnLight
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flInnerAngle` | float32 |  |
| `m_flOuterAngle` | float32 |  |
| `m_bShowLight` | bool |  |

### C_ParticleSystem

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Derived by:** [C_EnvParticleGlow](client.md#c_envparticleglow), [C_MapPreviewParticleSystem](client.md#c_mappreviewparticlesystem)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_ParticleSystem
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_ParticleSystem <|-- C_EnvParticleGlow
    C_ParticleSystem <|-- C_MapPreviewParticleSystem
    C_ParticleSystem *-- InfoForResourceTypeIParticleSystemDefinition
    C_ParticleSystem *-- GameTime_t
    C_ParticleSystem --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_szSnapshotFileName` | char[512] |  |
| `m_bActive` | bool |  |
| `m_bFrozen` | bool |  |
| `m_flFreezeTransitionDuration` | float32 |  |
| `m_nStopType` | int32 | `MNotSaved` |
| `m_bAnimateDuringGameplayPause` | bool |  |
| `m_iEffectIndex` | CStrongHandle< [InfoForResourceTypeIParticleSystemDefinition](../schemas/resourcesystem.md#infoforresourcetypeiparticlesystemdefinition) > | `MNotSaved` |
| `m_flStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flPreSimTime` | float32 |  |
| `m_vServerControlPoints` | Vector[4] |  |
| `m_iServerControlPointAssignments` | uint8[4] |  |
| `m_hControlPointEnts` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) >[64] |  |
| `m_bDataStringLocalized` | bool |  |
| `m_strDataString` | CUtlString |  |
| `m_bNoSave` | bool |  |
| `m_bNoFreeze` | bool |  |
| `m_bNoRamp` | bool |  |
| `m_bStartActive` | bool |  |
| `m_iszEffectName` | CUtlSymbolLarge |  |
| `m_iszControlPointNames` | CUtlSymbolLarge[64] |  |
| `m_nDataCP` | int32 |  |
| `m_vecDataCPValue` | Vector |  |
| `m_nTintCP` | int32 |  |
| `m_clrTint` | Color |  |
| `m_bOldActive` | bool | `MNotSaved` |
| `m_bOldFrozen` | bool | `MNotSaved` |

### C_PathParticleRope

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [C_PathParticleRopeAlias_path_particle_rope_clientside](client.md#c_pathparticleropealias_path_particle_rope_clientside)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_PathParticleRope
    CEntityInstance <|-- C_BaseEntity
    C_PathParticleRope <|-- C_PathParticleRopeAlias_path_particle_rope_clientside
    C_PathParticleRope *-- InfoForResourceTypeIParticleSystemDefinition
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bStartActive` | bool |  |
| `m_flMaxSimulationTime` | float32 |  |
| `m_iszEffectName` | CUtlSymbolLarge |  |
| `m_PathNodes_Name` | CUtlVector< CUtlSymbolLarge > |  |
| `m_flParticleSpacing` | float32 |  |
| `m_flSlack` | float32 |  |
| `m_flRadius` | float32 |  |
| `m_ColorTint` | Color |  |
| `m_nEffectState` | int32 |  |
| `m_iEffectIndex` | CStrongHandle< [InfoForResourceTypeIParticleSystemDefinition](../schemas/resourcesystem.md#infoforresourcetypeiparticlesystemdefinition) > | `MNotSaved` |
| `m_PathNodes_Position` | C_NetworkUtlVectorBase< Vector > |  |
| `m_PathNodes_TangentIn` | C_NetworkUtlVectorBase< Vector > |  |
| `m_PathNodes_TangentOut` | C_NetworkUtlVectorBase< Vector > |  |
| `m_PathNodes_Color` | C_NetworkUtlVectorBase< Vector > |  |
| `m_PathNodes_PinEnabled` | C_NetworkUtlVectorBase< bool > |  |
| `m_PathNodes_RadiusScale` | C_NetworkUtlVectorBase< float32 > |  |

### C_PathParticleRopeAlias_path_particle_rope_clientside

**Inherits from:** [C_PathParticleRope](client.md#c_pathparticlerope)

**Relationships:**

```mermaid
classDiagram
    C_PathParticleRope <|-- C_PathParticleRopeAlias_path_particle_rope_clientside
    C_BaseEntity <|-- C_PathParticleRope
    CEntityInstance <|-- C_BaseEntity
```

### C_PhysBox

**Inherits from:** [C_Breakable](client.md#c_breakable)

**Relationships:**

```mermaid
classDiagram
    C_Breakable <|-- C_PhysBox
    C_BaseModelEntity <|-- C_Breakable
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_PhysMagnet

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_PhysMagnet
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_PhysMagnet --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_aAttachedObjectsFromServer` | CUtlVector< int32 > | `MNotSaved` |
| `m_aAttachedObjects` | CUtlVector< CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > > | `MNotSaved` |

### C_PhysPropClientside

**Inherits from:** [C_BreakableProp](client.md#c_breakableprop)

**Relationships:**

```mermaid
classDiagram
    C_BreakableProp <|-- C_PhysPropClientside
    CBaseProp <|-- C_BreakableProp
    CBaseAnimGraph <|-- CBaseProp
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    C_PhysPropClientside *-- GameTime_t
    C_PhysPropClientside *-- DamageTypes_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flTouchDelta` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `m_fDeathTime` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `m_vecDamagePosition` | VectorWS | `MNotSaved` |
| `m_vecDamageDirection` | Vector | `MNotSaved` |
| `m_nDamageType` | [DamageTypes_t](../schemas/!GlobalTypes.md#damagetypes_t) | `MNotSaved` |

### C_PhysicsProp

**Inherits from:** [C_BreakableProp](client.md#c_breakableprop)

**Derived by:** [C_PhysicsPropMultiplayer](client.md#c_physicspropmultiplayer)

**Relationships:**

```mermaid
classDiagram
    C_BreakableProp <|-- C_PhysicsProp
    CBaseProp <|-- C_BreakableProp
    CBaseAnimGraph <|-- CBaseProp
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    C_PhysicsProp <|-- C_PhysicsPropMultiplayer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bAwake` | bool | `MNotSaved` |

### C_PhysicsPropMultiplayer

**Inherits from:** [C_PhysicsProp](client.md#c_physicsprop)

**Relationships:**

```mermaid
classDiagram
    C_PhysicsProp <|-- C_PhysicsPropMultiplayer
    C_BreakableProp <|-- C_PhysicsProp
    CBaseProp <|-- C_BreakableProp
    CBaseAnimGraph <|-- CBaseProp
    C_BaseModelEntity <|-- CBaseAnimGraph
```

### C_PlantedC4

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph), [IHasAttributes](server.md#ihasattributes)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_PlantedC4
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_PlantedC4 *-- EntitySpottedState_t
    C_PlantedC4 *-- GameTime_t
    C_PlantedC4 --> C_CSPlayerPawn
    C_PlantedC4 *-- C_AttributeContainer
    C_PlantedC4 --> C_Multimeter
    C_PlantedC4 --> CBasePlayerController
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bBombTicking` | bool |  |
| `m_nBombSite` | int32 |  |
| `m_nSourceSoundscapeHash` | int32 |  |
| `m_entitySpottedState` | [EntitySpottedState_t](../schemas/client.md#entityspottedstate_t) |  |
| `m_flNextGlow` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flNextBeep` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flC4Blow` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bCannotBeDefused` | bool |  |
| `m_bHasExploded` | bool |  |
| `m_flTimerLength` | float32 |  |
| `m_bBeingDefused` | bool |  |
| `m_bTriggerWarning` | float32 |  |
| `m_bExplodeWarning` | float32 |  |
| `m_bC4Activated` | bool |  |
| `m_bTenSecWarning` | bool |  |
| `m_flDefuseLength` | float32 |  |
| `m_flDefuseCountDown` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bBombDefused` | bool |  |
| `m_hBombDefuser` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |
| `m_AttributeManager` | [C_AttributeContainer](../schemas/client.md#c_attributecontainer) |  |
| `m_hDefuserMultimeter` | CHandle< [C_Multimeter](../schemas/client.md#c_multimeter) > |  |
| `m_flNextRadarFlashTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_bRadarFlash` | bool |  |
| `m_pBombDefuser` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |
| `m_fLastDefuseTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_pPredictionOwner` | [CBasePlayerController](../schemas/client.md#cbaseplayercontroller)* |  |
| `m_vecC4ExplodeSpectatePos` | VectorWS |  |
| `m_vecC4ExplodeSpectateAng` | QAngle |  |
| `m_flC4ExplodeSpectateDuration` | float32 |  |

### C_PlayerPing

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_PlayerPing
    CEntityInstance <|-- C_BaseEntity
    C_PlayerPing --> C_CSPlayerPawn
    C_PlayerPing --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hPlayer` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |
| `m_hPingedEntity` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_iType` | int32 |  |
| `m_bUrgent` | bool |  |
| `m_szPlaceName` | char[18] |  |

### C_PlayerSprayDecal

**Inherits from:** [C_ModelPointEntity](client.md#c_modelpointentity)

**Relationships:**

```mermaid
classDiagram
    C_ModelPointEntity <|-- C_PlayerSprayDecal
    C_BaseModelEntity <|-- C_ModelPointEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_PlayerSprayDecal *-- CPlayerSprayDecalRenderHelper
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nUniqueID` | int32 |  |
| `m_unAccountID` | uint32 |  |
| `m_unTraceID` | uint32 |  |
| `m_rtGcTime` | uint32 |  |
| `m_vecEndPos` | VectorWS |  |
| `m_vecStart` | VectorWS |  |
| `m_vecLeft` | Vector |  |
| `m_vecNormal` | Vector |  |
| `m_nPlayer` | int32 |  |
| `m_nEntity` | int32 |  |
| `m_nHitbox` | int32 |  |
| `m_flCreationTime` | float32 |  |
| `m_nTintID` | int32 |  |
| `m_nVersion` | uint8 |  |
| `m_ubSignature` | uint8[128] |  |
| `m_SprayRenderHelper` | [CPlayerSprayDecalRenderHelper](../schemas/client.md#cplayerspraydecalrenderhelper) |  |

### C_PlayerVisibility

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_PlayerVisibility
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flVisibilityStrength` | float32 |  |
| `m_flFogDistanceMultiplier` | float32 |  |
| `m_flFogMaxDensityMultiplier` | float32 |  |
| `m_flFadeTime` | float32 |  |
| `m_bStartDisabled` | bool |  |
| `m_bIsEnabled` | bool |  |

### C_PointCamera

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [C_PointCameraVFOV](client.md#c_pointcameravfov)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_PointCamera
    CEntityInstance <|-- C_BaseEntity
    C_PointCamera <|-- C_PointCameraVFOV
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_FOV` | float32 |  |
| `m_Resolution` | float32 |  |
| `m_bFogEnable` | bool |  |
| `m_FogColor` | Color |  |
| `m_flFogStart` | float32 |  |
| `m_flFogEnd` | float32 |  |
| `m_flFogMaxDensity` | float32 |  |
| `m_bActive` | bool |  |
| `m_bUseScreenAspectRatio` | bool |  |
| `m_flAspectRatio` | float32 |  |
| `m_bNoSky` | bool |  |
| `m_fBrightness` | float32 |  |
| `m_flZFar` | float32 |  |
| `m_flZNear` | float32 |  |
| `m_bCanHLTVUse` | bool |  |
| `m_bAlignWithParent` | bool |  |
| `m_bDofEnabled` | bool |  |
| `m_flDofNearBlurry` | float32 |  |
| `m_flDofNearCrisp` | float32 |  |
| `m_flDofFarCrisp` | float32 |  |
| `m_flDofFarBlurry` | float32 |  |
| `m_flDofTiltToGround` | float32 |  |
| `m_TargetFOV` | float32 |  |
| `m_DegreesPerSecond` | float32 |  |
| `m_bIsOn` | bool |  |
| `m_pNext` | [C_PointCamera](../schemas/client.md#c_pointcamera)* | `MNotSaved` |

### C_PointCameraVFOV

**Inherits from:** [C_PointCamera](client.md#c_pointcamera)

**Relationships:**

```mermaid
classDiagram
    C_PointCamera <|-- C_PointCameraVFOV
    C_BaseEntity <|-- C_PointCamera
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flVerticalFOV` | float32 |  |

### C_PointClientUIDialog

**Inherits from:** [C_BaseClientUIEntity](client.md#c_baseclientuientity)

**Relationships:**

```mermaid
classDiagram
    C_BaseClientUIEntity <|-- C_PointClientUIDialog
    C_BaseModelEntity <|-- C_BaseClientUIEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_PointClientUIDialog --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hActivator` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_bStartEnabled` | bool |  |

### C_PointClientUIHUD

**Inherits from:** [C_BaseClientUIEntity](client.md#c_baseclientuientity)

**Relationships:**

```mermaid
classDiagram
    C_BaseClientUIEntity <|-- C_PointClientUIHUD
    C_BaseModelEntity <|-- C_BaseClientUIEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bCheckCSSClasses` | bool | `MNotSaved` |
| `m_bIgnoreInput` | bool |  |
| `m_flWidth` | float32 |  |
| `m_flHeight` | float32 |  |
| `m_flDPI` | float32 |  |
| `m_flInteractDistance` | float32 |  |
| `m_flDepthOffset` | float32 |  |
| `m_unOwnerContext` | uint32 |  |
| `m_unHorizontalAlign` | uint32 |  |
| `m_unVerticalAlign` | uint32 |  |
| `m_unOrientation` | uint32 |  |
| `m_bAllowInteractionFromAllSceneWorlds` | bool |  |
| `m_vecCSSClasses` | C_NetworkUtlVectorBase< CUtlSymbolLarge > |  |

### C_PointClientUIWorldPanel

**Inherits from:** [C_BaseClientUIEntity](client.md#c_baseclientuientity)

**Derived by:** [CPointOffScreenIndicatorUi](client.md#cpointoffscreenindicatorui), [C_PointClientUIWorldTextPanel](client.md#c_pointclientuiworldtextpanel)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseClientUIEntity <|-- C_PointClientUIWorldPanel
    C_BaseModelEntity <|-- C_BaseClientUIEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_PointClientUIWorldPanel <|-- CPointOffScreenIndicatorUi
    C_PointClientUIWorldPanel <|-- C_PointClientUIWorldTextPanel
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bForceRecreateNextUpdate` | bool | `MNotSaved` |
| `m_bMoveViewToPlayerNextThink` | bool | `MNotSaved` |
| `m_bCheckCSSClasses` | bool | `MNotSaved` |
| `m_anchorDeltaTransform` | CTransform | `MNotSaved` |
| `m_pOffScreenIndicator` | [CPointOffScreenIndicatorUi](../schemas/client.md#cpointoffscreenindicatorui)* | `MNotSaved` |
| `m_bIgnoreInput` | bool |  |
| `m_bLit` | bool |  |
| `m_bFollowPlayerAcrossTeleport` | bool |  |
| `m_flWidth` | float32 |  |
| `m_flHeight` | float32 |  |
| `m_flDPI` | float32 |  |
| `m_flInteractDistance` | float32 |  |
| `m_flDepthOffset` | float32 |  |
| `m_unOwnerContext` | uint32 |  |
| `m_unHorizontalAlign` | uint32 |  |
| `m_unVerticalAlign` | uint32 |  |
| `m_unOrientation` | uint32 |  |
| `m_bAllowInteractionFromAllSceneWorlds` | bool |  |
| `m_vecCSSClasses` | C_NetworkUtlVectorBase< CUtlSymbolLarge > |  |
| `m_bOpaque` | bool |  |
| `m_bNoDepth` | bool |  |
| `m_bVisibleWhenParentNoDraw` | bool |  |
| `m_bRenderBackface` | bool |  |
| `m_bUseOffScreenIndicator` | bool |  |
| `m_bExcludeFromSaveGames` | bool |  |
| `m_bGrabbable` | bool |  |
| `m_bOnlyRenderToTexture` | bool |  |
| `m_bDisableMipGen` | bool |  |
| `m_nExplicitImageLayout` | int32 |  |
| `m_bIgnoreParentOrientation` | bool |  |

### C_PointClientUIWorldTextPanel

**Inherits from:** [C_PointClientUIWorldPanel](client.md#c_pointclientuiworldpanel)

**Relationships:**

```mermaid
classDiagram
    C_PointClientUIWorldPanel <|-- C_PointClientUIWorldTextPanel
    C_BaseClientUIEntity <|-- C_PointClientUIWorldPanel
    C_BaseModelEntity <|-- C_BaseClientUIEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_messageText` | char[512] |  |

### C_PointCommentaryNode

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_PointCommentaryNode
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_PointCommentaryNode *-- GameTime_t
    C_PointCommentaryNode --> CSoundPatch
    C_PointCommentaryNode --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bActive` | bool |  |
| `m_bWasActive` | bool |  |
| `m_flEndTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flStartTimeInCommentary` | float32 |  |
| `m_iszCommentaryFile` | CUtlSymbolLarge |  |
| `m_iszTitle` | CUtlSymbolLarge |  |
| `m_iszSpeakers` | CUtlSymbolLarge |  |
| `m_iNodeNumber` | int32 |  |
| `m_iNodeNumberMax` | int32 |  |
| `m_bListenedTo` | bool |  |
| `m_sndCommentary` | [CSoundPatch](../schemas/server.md#csoundpatch)* |  |
| `m_hViewPosition` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_bRestartAfterRestore` | bool | `MNotSaved` |

### C_PointEntity

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [CChoreoInfoTarget](client.md#cchoreoinfotarget), [CInfoDynamicShadowHint](client.md#cinfodynamicshadowhint), [CInfoFan](client.md#cinfofan), [CInfoOffscreenPanoramaTexture](client.md#cinfooffscreenpanoramatexture), [CInfoParticleTarget](client.md#cinfoparticletarget), [CInfoTarget](client.md#cinfotarget), [CMapInfo](client.md#cmapinfo), [CPathNode](client.md#cpathnode), [CPointChildModifier](client.md#cpointchildmodifier), [C_InfoInstructorHintHostageRescueZone](client.md#c_infoinstructorhinthostagerescuezone), [C_SceneEntity](client.md#c_sceneentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
    C_PointEntity <|-- CChoreoInfoTarget
    C_PointEntity <|-- CInfoDynamicShadowHint
    C_PointEntity <|-- CInfoFan
    C_PointEntity <|-- CInfoOffscreenPanoramaTexture
    C_PointEntity <|-- CInfoParticleTarget
    C_PointEntity <|-- CInfoTarget
    C_PointEntity <|-- CMapInfo
    C_PointEntity <|-- CPathNode
    C_PointEntity <|-- CPointChildModifier
    C_PointEntity <|-- C_InfoInstructorHintHostageRescueZone
    C_PointEntity <|-- C_SceneEntity
```

### C_PointValueRemapper

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_PointValueRemapper
    CEntityInstance <|-- C_BaseEntity
    C_PointValueRemapper *-- ValueRemapperInputType_t
    C_PointValueRemapper --> C_BaseEntity
    C_PointValueRemapper *-- ValueRemapperOutputType_t
    C_PointValueRemapper *-- ValueRemapperHapticsType_t
    C_PointValueRemapper *-- ValueRemapperMomentumType_t
    C_PointValueRemapper *-- ValueRemapperRatchetType_t
    C_PointValueRemapper *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bDisabled` | bool |  |
| `m_bDisabledOld` | bool |  |
| `m_bUpdateOnClient` | bool |  |
| `m_nInputType` | [ValueRemapperInputType_t](../schemas/!GlobalTypes.md#valueremapperinputtype_t) |  |
| `m_hRemapLineStart` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_hRemapLineEnd` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_flMaximumChangePerSecond` | float32 |  |
| `m_flDisengageDistance` | float32 |  |
| `m_flEngageDistance` | float32 |  |
| `m_bRequiresUseKey` | bool |  |
| `m_nOutputType` | [ValueRemapperOutputType_t](../schemas/!GlobalTypes.md#valueremapperoutputtype_t) |  |
| `m_hOutputEntities` | C_NetworkUtlVectorBase< CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > > | `MNotSaved` |
| `m_nHapticsType` | [ValueRemapperHapticsType_t](../schemas/!GlobalTypes.md#valueremapperhapticstype_t) |  |
| `m_nMomentumType` | [ValueRemapperMomentumType_t](../schemas/!GlobalTypes.md#valueremappermomentumtype_t) |  |
| `m_flMomentumModifier` | float32 |  |
| `m_flSnapValue` | float32 |  |
| `m_flCurrentMomentum` | float32 |  |
| `m_nRatchetType` | [ValueRemapperRatchetType_t](../schemas/!GlobalTypes.md#valueremapperratchettype_t) |  |
| `m_flRatchetOffset` | float32 |  |
| `m_flInputOffset` | float32 |  |
| `m_bEngaged` | bool |  |
| `m_bFirstUpdate` | bool |  |
| `m_flPreviousValue` | float32 |  |
| `m_flPreviousUpdateTickTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_vecPreviousTestPoint` | VectorWS |  |

### C_PointWorldText

**Inherits from:** [C_ModelPointEntity](client.md#c_modelpointentity)

**Relationships:**

```mermaid
classDiagram
    C_ModelPointEntity <|-- C_PointWorldText
    C_BaseModelEntity <|-- C_ModelPointEntity
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_PointWorldText *-- PointWorldTextJustifyHorizontal_t
    C_PointWorldText *-- PointWorldTextJustifyVertical_t
    C_PointWorldText *-- PointWorldTextReorientMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bForceRecreateNextUpdate` | bool | `MNotSaved` |
| `m_nTextWidthPx` | int32 |  |
| `m_nTextHeightPx` | int32 |  |
| `m_messageText` | char[512] |  |
| `m_FontName` | char[64] | `MNotSaved` |
| `m_BackgroundMaterialName` | char[64] | `MNotSaved` |
| `m_bEnabled` | bool | `MNotSaved` |
| `m_bFullbright` | bool | `MNotSaved` |
| `m_flWorldUnitsPerPx` | float32 | `MNotSaved` |
| `m_flFontSize` | float32 | `MNotSaved` |
| `m_flDepthOffset` | float32 | `MNotSaved` |
| `m_bDrawBackground` | bool | `MNotSaved` |
| `m_flBackgroundBorderWidth` | float32 | `MNotSaved` |
| `m_flBackgroundBorderHeight` | float32 | `MNotSaved` |
| `m_flBackgroundWorldToUV` | float32 | `MNotSaved` |
| `m_Color` | Color | `MNotSaved` |
| `m_nJustifyHorizontal` | [PointWorldTextJustifyHorizontal_t](../schemas/!GlobalTypes.md#pointworldtextjustifyhorizontal_t) | `MNotSaved` |
| `m_nJustifyVertical` | [PointWorldTextJustifyVertical_t](../schemas/!GlobalTypes.md#pointworldtextjustifyvertical_t) | `MNotSaved` |
| `m_nReorientMode` | [PointWorldTextReorientMode_t](../schemas/!GlobalTypes.md#pointworldtextreorientmode_t) | `MNotSaved` |

### C_PortraitWorldCallbackHandler

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_PortraitWorldCallbackHandler
    CEntityInstance <|-- C_BaseEntity
```

### C_PostProcessingVolume

**Inherits from:** [C_BaseTrigger](client.md#c_basetrigger)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseTrigger <|-- C_PostProcessingVolume
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_PostProcessingVolume *-- InfoForResourceTypeCPostProcessingResource
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hPostSettings` | CStrongHandle< [InfoForResourceTypeCPostProcessingResource](../schemas/resourcesystem.md#infoforresourcetypecpostprocessingresource) > |  |
| `m_flFadeDuration` | float32 |  |
| `m_flMinLogExposure` | float32 |  |
| `m_flMaxLogExposure` | float32 |  |
| `m_flMinExposure` | float32 |  |
| `m_flMaxExposure` | float32 |  |
| `m_flExposureCompensation` | float32 |  |
| `m_flExposureFadeSpeedUp` | float32 |  |
| `m_flExposureFadeSpeedDown` | float32 |  |
| `m_flTonemapEVSmoothingRange` | float32 |  |
| `m_bMaster` | bool |  |
| `m_bExposureControl` | bool |  |

### C_Precipitation

**Inherits from:** [C_BaseTrigger](client.md#c_basetrigger)

**Relationships:**

```mermaid
classDiagram
    C_BaseTrigger <|-- C_Precipitation
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_Precipitation *-- TimedEvent
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flDensity` | float32 | `MNotSaved` |
| `m_flParticleInnerDist` | float32 | `MNotSaved` |
| `m_pParticleDef` | char* | `MNotSaved` |
| `m_tParticlePrecipTraceTimer` | [TimedEvent](../schemas/client.md#timedevent)[1] | `MNotSaved` |
| `m_bActiveParticlePrecipEmitter` | bool[1] | `MNotSaved` |
| `m_bParticlePrecipInitialized` | bool | `MNotSaved` |
| `m_bHasSimulatedSinceLastSceneObjectUpdate` | bool | `MNotSaved` |
| `m_nAvailableSheetSequencesMaxIndex` | int32 | `MNotSaved` |

### C_PrecipitationBlocker

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_PrecipitationBlocker
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_PropDoorRotating

**Inherits from:** [C_BasePropDoor](client.md#c_basepropdoor)

**Relationships:**

```mermaid
classDiagram
    C_BasePropDoor <|-- C_PropDoorRotating
    C_DynamicProp <|-- C_BasePropDoor
    C_BreakableProp <|-- C_DynamicProp
    CBaseProp <|-- C_BreakableProp
    CBaseAnimGraph <|-- CBaseProp
```

### C_RagdollProp

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Derived by:** [C_RagdollPropAttached](client.md#c_ragdollpropattached)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_RagdollProp
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_RagdollProp <|-- C_RagdollPropAttached
    C_RagdollProp --> C_BaseEntity
    C_RagdollProp *-- AttachmentHandle_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_ragEnabled` | C_NetworkUtlVectorBase< bool > | `MNotSaved` |
| `m_ragPos` | C_NetworkUtlVectorBase< Vector > | `MNotSaved` |
| `m_ragAngles` | C_NetworkUtlVectorBase< QAngle > | `MNotSaved` |
| `m_flBlendWeight` | float32 | `MNotSaved` |
| `m_hRagdollSource` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > | `MNotSaved` |
| `m_iEyeAttachment` | [AttachmentHandle_t](../schemas/modellib.md#attachmenthandle_t) | `MNotSaved` |
| `m_flBlendWeightCurrent` | float32 | `MNotSaved` |
| `m_parentPhysicsBoneIndices` | CUtlVector< int32 > | `MNotSaved` |
| `m_worldSpaceBoneComputationOrder` | CUtlVector< int32 > | `MNotSaved` |

### C_RagdollPropAttached

**Inherits from:** [C_RagdollProp](client.md#c_ragdollprop)

**Relationships:**

```mermaid
classDiagram
    C_RagdollProp <|-- C_RagdollPropAttached
    CBaseAnimGraph <|-- C_RagdollProp
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_boneIndexAttached` | uint32 | `MNotSaved` |
| `m_ragdollAttachedObjectIndex` | uint32 | `MNotSaved` |
| `m_attachmentPointBoneSpace` | Vector | `MNotSaved` |
| `m_attachmentPointRagdollSpace` | Vector | `MNotSaved` |
| `m_vecOffset` | Vector | `MNotSaved` |
| `m_parentTime` | float32 | `MNotSaved` |
| `m_bHasParent` | bool | `MNotSaved` |

### C_RectLight

**Inherits from:** [C_BarnLight](client.md#c_barnlight)

**Relationships:**

```mermaid
classDiagram
    C_BarnLight <|-- C_RectLight
    C_BaseModelEntity <|-- C_BarnLight
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bShowLight` | bool |  |

### C_RetakeGameRules

**Relationships:**

```mermaid
classDiagram
    C_RetakeGameRules --> C_CSPlayerPawn
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nMatchSeed` | int32 |  |
| `m_bBlockersPresent` | bool |  |
| `m_bRoundInProgress` | bool |  |
| `m_iFirstSecondHalfRound` | int32 |  |
| `m_iBombSite` | int32 |  |
| `m_hBombPlanter` | CHandle< [C_CSPlayerPawn](../schemas/client.md#c_csplayerpawn) > |  |

### C_RopeKeyframe

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_RopeKeyframe
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_RopeKeyframe *-- InfoForResourceTypeIMaterial2
    C_RopeKeyframe --> C_BaseEntity
    C_RopeKeyframe *-- AttachmentHandle_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bEndPointAttachmentAnglesDirty` | bitfield:1 | `MNotSaved` |
| `m_bEndPointAttachmentPositionsDirty` | bitfield:1 | `MNotSaved` |
| `m_bNewDataThisFrame` | bitfield:1 | `MNotSaved` |
| `m_bPhysicsInitted` | bitfield:1 | `MNotSaved` |
| `m_LinksTouchingSomething` | CBitVec< 10 > | `MNotSaved` |
| `m_nLinksTouchingSomething` | int32 | `MNotSaved` |
| `m_bApplyWind` | bool | `MNotSaved` |
| `m_fPrevLockedPoints` | int32 | `MNotSaved` |
| `m_iForcePointMoveCounter` | int32 | `MNotSaved` |
| `m_bPrevEndPointPos` | bool[2] | `MNotSaved` |
| `m_vPrevEndPointPos` | VectorWS[2] | `MNotSaved` |
| `m_flCurScroll` | float32 | `MNotSaved` |
| `m_flScrollSpeed` | float32 | `MNotSaved` |
| `m_RopeFlags` | uint16 | `MNotSaved` |
| `m_iRopeMaterialModelIndex` | CStrongHandle< [InfoForResourceTypeIMaterial2](../schemas/resourcesystem.md#infoforresourcetypeimaterial2) > | `MNotSaved` |
| `m_nSegments` | uint8 | `MNotSaved` |
| `m_hStartPoint` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > | `MNotSaved` |
| `m_hEndPoint` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > | `MNotSaved` |
| `m_iStartAttachment` | [AttachmentHandle_t](../schemas/modellib.md#attachmenthandle_t) | `MNotSaved` |
| `m_iEndAttachment` | [AttachmentHandle_t](../schemas/modellib.md#attachmenthandle_t) | `MNotSaved` |
| `m_Subdiv` | uint8 | `MNotSaved` |
| `m_RopeLength` | int16 | `MNotSaved` |
| `m_Slack` | int16 | `MNotSaved` |
| `m_TextureScale` | float32 | `MNotSaved` |
| `m_fLockedPoints` | uint8 | `MNotSaved` |
| `m_nChangeCount` | uint8 | `MNotSaved` |
| `m_Width` | float32 | `MNotSaved` |
| `m_PhysicsDelegate` | [C_RopeKeyframe](../schemas/client.md#c_ropekeyframe)::CPhysicsDelegate | `MNotSaved` |
| `m_hMaterial` | CStrongHandle< [InfoForResourceTypeIMaterial2](../schemas/resourcesystem.md#infoforresourcetypeimaterial2) > | `MNotSaved` |
| `m_TextureHeight` | int32 | `MNotSaved` |
| `m_vecImpulse` | Vector | `MNotSaved` |
| `m_vecPreviousImpulse` | Vector | `MNotSaved` |
| `m_flCurrentGustTimer` | float32 | `MNotSaved` |
| `m_flCurrentGustLifetime` | float32 | `MNotSaved` |
| `m_flTimeToNextGust` | float32 | `MNotSaved` |
| `m_vWindDir` | Vector | `MNotSaved` |
| `m_vColorMod` | Vector | `MNotSaved` |
| `m_vCachedEndPointAttachmentPos` | VectorWS[2] | `MNotSaved` |
| `m_vCachedEndPointAttachmentAngle` | QAngle[2] | `MNotSaved` |
| `m_bConstrainBetweenEndpoints` | bool | `MNotSaved` |

### C_RopeKeyframe::CPhysicsDelegate

**Relationships:**

```mermaid
classDiagram
    "C_RopeKeyframe::CPhysicsDelegate" --> C_RopeKeyframe
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_pKeyframe` | [C_RopeKeyframe](../schemas/client.md#c_ropekeyframe)* |  |

### C_SceneEntity

**Inherits from:** [C_PointEntity](client.md#c_pointentity)

**Relationships:**

```mermaid
classDiagram
    C_PointEntity <|-- C_SceneEntity
    C_BaseEntity <|-- C_PointEntity
    CEntityInstance <|-- C_BaseEntity
    C_SceneEntity --> C_BaseModelEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bIsPlayingBack` | bool | `MNotSaved` |
| `m_bPaused` | bool | `MNotSaved` |
| `m_bMultiplayer` | bool | `MNotSaved` |
| `m_bAutogenerated` | bool | `MNotSaved` |
| `m_bAllRequirementsComplete` | bool | `MNotSaved` |
| `m_flForceClientTime` | float32 | `MNotSaved` |
| `m_nSceneStringIndex` | uint16 | `MNotSaved` |
| `m_bClientOnly` | bool | `MNotSaved` |
| `m_hOwner` | CHandle< [C_BaseModelEntity](../schemas/client.md#c_basemodelentity) > | `MNotSaved` |
| `m_hActorList` | C_NetworkUtlVectorBase< CHandle< [C_BaseModelEntity](../schemas/client.md#c_basemodelentity) > > | `MNotSaved` |
| `m_bWasPlaying` | bool | `MNotSaved` |
| `m_QueuedEvents` | CUtlVector< [C_SceneEntity](../schemas/client.md#c_sceneentity)::QueuedEvents_t > | `MNotSaved` |
| `m_flCurrentTime` | float32 | `MNotSaved` |

### C_SceneEntity::QueuedEvents_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `starttime` | float32 |  |

### C_ShatterGlassShardPhysics

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_ShatterGlassShardPhysics
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_ShardDesc` | shard_model_desc_t | `MNotSaved` |

### C_SingleplayRules

**Inherits from:** [C_GameRules](client.md#c_gamerules)

**Relationships:**

```mermaid
classDiagram
    C_GameRules <|-- C_SingleplayRules
```

### C_SkyCamera

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_SkyCamera
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_skyboxData` | sky3dparams_t | `MNotSaved` |
| `m_skyboxSlotToken` | CUtlStringToken |  |
| `m_bUseAngles` | bool |  |
| `m_pNext` | [C_SkyCamera](../schemas/client.md#c_skycamera)* | `MNotSaved` |

### C_SmokeGrenade

**Inherits from:** [C_BaseCSGrenade](client.md#c_basecsgrenade)

**Relationships:**

```mermaid
classDiagram
    C_BaseCSGrenade <|-- C_SmokeGrenade
    C_CSWeaponBase <|-- C_BaseCSGrenade
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_SmokeGrenadeProjectile

**Inherits from:** [C_BaseCSGrenadeProjectile](client.md#c_basecsgrenadeprojectile)

**Relationships:**

```mermaid
classDiagram
    C_BaseCSGrenadeProjectile <|-- C_SmokeGrenadeProjectile
    C_BaseGrenade <|-- C_BaseCSGrenadeProjectile
    CBaseAnimGraph <|-- C_BaseGrenade
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nSmokeEffectTickBegin` | int32 |  |
| `m_bDidSmokeEffect` | bool |  |
| `m_nRandomSeed` | int32 |  |
| `m_vSmokeColor` | Vector |  |
| `m_vSmokeDetonationPos` | VectorWS |  |
| `m_VoxelFrameData` | C_NetworkUtlVectorBase< uint8 > |  |
| `m_nVoxelFrameDataSize` | int32 |  |
| `m_nVoxelUpdate` | int32 |  |
| `m_bSmokeVolumeDataReceived` | bool |  |
| `m_bSmokeEffectSpawned` | bool |  |

### C_SoundAreaEntityBase

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [C_SoundAreaEntityOrientedBox](client.md#c_soundareaentityorientedbox), [C_SoundAreaEntitySphere](client.md#c_soundareaentitysphere)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_SoundAreaEntityBase
    CEntityInstance <|-- C_BaseEntity
    C_SoundAreaEntityBase <|-- C_SoundAreaEntityOrientedBox
    C_SoundAreaEntityBase <|-- C_SoundAreaEntitySphere
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bDisabled` | bool |  |
| `m_bWasEnabled` | bool | `MNotSaved` |
| `m_iszSoundAreaType` | CUtlSymbolLarge |  |
| `m_vPos` | Vector |  |

### C_SoundAreaEntityOrientedBox

**Inherits from:** [C_SoundAreaEntityBase](client.md#c_soundareaentitybase)

**Relationships:**

```mermaid
classDiagram
    C_SoundAreaEntityBase <|-- C_SoundAreaEntityOrientedBox
    C_BaseEntity <|-- C_SoundAreaEntityBase
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vMin` | Vector |  |
| `m_vMax` | Vector |  |

### C_SoundAreaEntitySphere

**Inherits from:** [C_SoundAreaEntityBase](client.md#c_soundareaentitybase)

**Relationships:**

```mermaid
classDiagram
    C_SoundAreaEntityBase <|-- C_SoundAreaEntitySphere
    C_BaseEntity <|-- C_SoundAreaEntityBase
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flRadius` | float32 |  |

### C_SoundEventAABBEntity

**Inherits from:** [C_SoundEventEntity](client.md#c_soundevententity)

**Relationships:**

```mermaid
classDiagram
    C_SoundEventEntity <|-- C_SoundEventAABBEntity
    C_BaseEntity <|-- C_SoundEventEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vMins` | Vector |  |
| `m_vMaxs` | Vector |  |

### C_SoundEventConeEntity

**Inherits from:** [C_SoundEventEntity](client.md#c_soundevententity)

**Relationships:**

```mermaid
classDiagram
    C_SoundEventEntity <|-- C_SoundEventConeEntity
    C_BaseEntity <|-- C_SoundEventEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flEmitterAngle` | float32 |  |
| `m_flSweetSpotAngle` | float32 |  |
| `m_flAttenMin` | float32 |  |
| `m_flAttenMax` | float32 |  |
| `m_iszParameterName` | CUtlSymbolLarge |  |

### C_SoundEventEntity

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [C_SoundEventAABBEntity](client.md#c_soundeventaabbentity), [C_SoundEventConeEntity](client.md#c_soundeventconeentity), [C_SoundEventEntityAlias_snd_event_point](client.md#c_soundevententityalias_snd_event_point), [C_SoundEventOBBEntity](client.md#c_soundeventobbentity), [C_SoundEventPathCornerEntity](client.md#c_soundeventpathcornerentity), [C_SoundEventSphereEntity](client.md#c_soundeventsphereentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_SoundEventEntity
    CEntityInstance <|-- C_BaseEntity
    C_SoundEventEntity <|-- C_SoundEventAABBEntity
    C_SoundEventEntity <|-- C_SoundEventConeEntity
    C_SoundEventEntity <|-- C_SoundEventEntityAlias_snd_event_point
    C_SoundEventEntity <|-- C_SoundEventOBBEntity
    C_SoundEventEntity <|-- C_SoundEventPathCornerEntity
    C_SoundEventEntity <|-- C_SoundEventSphereEntity
    C_SoundEventEntity *-- CEntityIOOutput
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bClientSideOnly` | bitfield:1 | `MNotSaved` |
| `m_bStartOnSpawn` | bool |  |
| `m_bToLocalPlayer` | bool |  |
| `m_bStopOnNew` | bool |  |
| `m_bSaveRestore` | bool |  |
| `m_bSavedIsPlaying` | bool |  |
| `m_flSavedElapsedTime` | float32 |  |
| `m_iszSourceEntityName` | CUtlSymbolLarge |  |
| `m_iszAttachmentName` | CUtlSymbolLarge |  |
| `m_onGUIDChanged` | CEntityOutputTemplate< SndOpEventGuid_t > |  |
| `m_onSoundFinished` | [CEntityIOOutput](../schemas/entity2.md#centityiooutput) |  |
| `m_flClientCullRadius` | float32 |  |
| `m_iszSoundName` | CUtlSymbolLarge |  |
| `m_hSource` | CEntityHandle |  |
| `m_nEntityIndexSelection` | int32 |  |

### C_SoundEventEntityAlias_snd_event_point

**Inherits from:** [C_SoundEventEntity](client.md#c_soundevententity)

**Relationships:**

```mermaid
classDiagram
    C_SoundEventEntity <|-- C_SoundEventEntityAlias_snd_event_point
    C_BaseEntity <|-- C_SoundEventEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_SoundEventOBBEntity

**Inherits from:** [C_SoundEventEntity](client.md#c_soundevententity)

**Relationships:**

```mermaid
classDiagram
    C_SoundEventEntity <|-- C_SoundEventOBBEntity
    C_BaseEntity <|-- C_SoundEventEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vMins` | Vector |  |
| `m_vMaxs` | Vector |  |

### C_SoundEventPathCornerEntity

**Inherits from:** [C_SoundEventEntity](client.md#c_soundevententity)

**Relationships:**

```mermaid
classDiagram
    C_SoundEventEntity <|-- C_SoundEventPathCornerEntity
    C_BaseEntity <|-- C_SoundEventEntity
    CEntityInstance <|-- C_BaseEntity
    C_SoundEventPathCornerEntity *-- SoundeventPathCornerPairNetworked_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vecCornerPairsNetworked` | C_NetworkUtlVectorBase< [SoundeventPathCornerPairNetworked_t](../schemas/server.md#soundeventpathcornerpairnetworked_t) > | `MNotSaved` |

### C_SoundEventSphereEntity

**Inherits from:** [C_SoundEventEntity](client.md#c_soundevententity)

**Relationships:**

```mermaid
classDiagram
    C_SoundEventEntity <|-- C_SoundEventSphereEntity
    C_BaseEntity <|-- C_SoundEventEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flRadius` | float32 |  |

### C_SoundOpvarSetAABBEntity

**Inherits from:** [CSoundOpvarSetBoxEntity](client.md#csoundopvarsetboxentity)

**Derived by:** [C_SoundOpvarSetOBBEntity](client.md#c_soundopvarsetobbentity)

**Relationships:**

```mermaid
classDiagram
    CSoundOpvarSetBoxEntity <|-- C_SoundOpvarSetAABBEntity
    C_SoundOpvarSetPointEntity <|-- CSoundOpvarSetBoxEntity
    C_SoundOpvarSetPointBase <|-- C_SoundOpvarSetPointEntity
    C_BaseEntity <|-- C_SoundOpvarSetPointBase
    CEntityInstance <|-- C_BaseEntity
    C_SoundOpvarSetAABBEntity <|-- C_SoundOpvarSetOBBEntity
```

### C_SoundOpvarSetAutoRoomEntity

**Inherits from:** [C_SoundOpvarSetPointEntity](client.md#c_soundopvarsetpointentity)

**Relationships:**

```mermaid
classDiagram
    C_SoundOpvarSetPointEntity <|-- C_SoundOpvarSetAutoRoomEntity
    C_SoundOpvarSetPointBase <|-- C_SoundOpvarSetPointEntity
    C_BaseEntity <|-- C_SoundOpvarSetPointBase
    CEntityInstance <|-- C_BaseEntity
```

### C_SoundOpvarSetOBBEntity

**Inherits from:** [C_SoundOpvarSetAABBEntity](client.md#c_soundopvarsetaabbentity)

**Relationships:**

```mermaid
classDiagram
    C_SoundOpvarSetAABBEntity <|-- C_SoundOpvarSetOBBEntity
    CSoundOpvarSetBoxEntity <|-- C_SoundOpvarSetAABBEntity
    C_SoundOpvarSetPointEntity <|-- CSoundOpvarSetBoxEntity
    C_SoundOpvarSetPointBase <|-- C_SoundOpvarSetPointEntity
    C_BaseEntity <|-- C_SoundOpvarSetPointBase
```

### C_SoundOpvarSetOBBWindEntity

**Inherits from:** [C_SoundOpvarSetPointBase](client.md#c_soundopvarsetpointbase)

**Relationships:**

```mermaid
classDiagram
    C_SoundOpvarSetPointBase <|-- C_SoundOpvarSetOBBWindEntity
    C_BaseEntity <|-- C_SoundOpvarSetPointBase
    CEntityInstance <|-- C_BaseEntity
```

### C_SoundOpvarSetPathCornerEntity

**Inherits from:** [C_SoundOpvarSetPointEntity](client.md#c_soundopvarsetpointentity)

**Relationships:**

```mermaid
classDiagram
    C_SoundOpvarSetPointEntity <|-- C_SoundOpvarSetPathCornerEntity
    C_SoundOpvarSetPointBase <|-- C_SoundOpvarSetPointEntity
    C_BaseEntity <|-- C_SoundOpvarSetPointBase
    CEntityInstance <|-- C_BaseEntity
```

### C_SoundOpvarSetPointBase

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [C_SoundOpvarSetOBBWindEntity](client.md#c_soundopvarsetobbwindentity), [C_SoundOpvarSetPointEntity](client.md#c_soundopvarsetpointentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_SoundOpvarSetPointBase
    CEntityInstance <|-- C_BaseEntity
    C_SoundOpvarSetPointBase <|-- C_SoundOpvarSetOBBWindEntity
    C_SoundOpvarSetPointBase <|-- C_SoundOpvarSetPointEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iszStackName` | CUtlSymbolLarge |  |
| `m_iszOperatorName` | CUtlSymbolLarge |  |
| `m_iszOpvarName` | CUtlSymbolLarge |  |
| `m_iOpvarIndex` | int32 |  |
| `m_bUseAutoCompare` | bool |  |
| `m_bFastRefresh` | bool |  |

### C_SoundOpvarSetPointEntity

**Inherits from:** [C_SoundOpvarSetPointBase](client.md#c_soundopvarsetpointbase)

**Derived by:** [CSoundOpvarSetBoxEntity](client.md#csoundopvarsetboxentity), [C_SoundOpvarSetAutoRoomEntity](client.md#c_soundopvarsetautoroomentity), [C_SoundOpvarSetPathCornerEntity](client.md#c_soundopvarsetpathcornerentity)

**Relationships:**

```mermaid
classDiagram
    C_SoundOpvarSetPointBase <|-- C_SoundOpvarSetPointEntity
    C_BaseEntity <|-- C_SoundOpvarSetPointBase
    CEntityInstance <|-- C_BaseEntity
    C_SoundOpvarSetPointEntity <|-- CSoundOpvarSetBoxEntity
    C_SoundOpvarSetPointEntity <|-- C_SoundOpvarSetAutoRoomEntity
    C_SoundOpvarSetPointEntity <|-- C_SoundOpvarSetPathCornerEntity
```

### C_SpotlightEnd

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_SpotlightEnd
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flLightScale` | float32 | `MNotSaved` |
| `m_Radius` | float32 | `MNotSaved` |

### C_Sprite

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Derived by:** [CSpriteOriented](client.md#cspriteoriented)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_Sprite
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_Sprite <|-- CSpriteOriented
    C_Sprite *-- InfoForResourceTypeIMaterial2
    C_Sprite --> C_BaseEntity
    C_Sprite *-- AttachmentHandle_t
    C_Sprite *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hSpriteMaterial` | CStrongHandle< [InfoForResourceTypeIMaterial2](../schemas/resourcesystem.md#infoforresourcetypeimaterial2) > |  |
| `m_hAttachedToEntity` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_nAttachment` | [AttachmentHandle_t](../schemas/modellib.md#attachmenthandle_t) |  |
| `m_flSpriteFramerate` | float32 |  |
| `m_flFrame` | float32 |  |
| `m_flDieTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_nBrightness` | uint32 |  |
| `m_flBrightnessDuration` | float32 |  |
| `m_flSpriteScale` | float32 |  |
| `m_flScaleDuration` | float32 |  |
| `m_bWorldSpaceScale` | bool |  |
| `m_flGlowProxySize` | float32 |  |
| `m_flHDRColorScale` | float32 |  |
| `m_flLastTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flMaxFrame` | float32 |  |
| `m_flStartScale` | float32 |  |
| `m_flDestScale` | float32 |  |
| `m_flScaleTimeStart` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_nStartBrightness` | int32 |  |
| `m_nDestBrightness` | int32 |  |
| `m_flBrightnessTimeStart` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_nSpriteWidth` | int32 | `MNotSaved` |
| `m_nSpriteHeight` | int32 | `MNotSaved` |
| `m_flSpeed` | float32 |  |

### C_StattrakModule

**Inherits from:** [C_CS2WeaponModuleBase](client.md#c_cs2weaponmodulebase)

**Relationships:**

```mermaid
classDiagram
    C_CS2WeaponModuleBase <|-- C_StattrakModule
    CBaseAnimGraph <|-- C_CS2WeaponModuleBase
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bKnife` | bool |  |

### C_Team

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [C_CSTeam](client.md#c_csteam)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_Team
    CEntityInstance <|-- C_BaseEntity
    C_Team <|-- C_CSTeam
    C_Team --> CBasePlayerController
    C_Team --> C_BasePlayerPawn
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_aPlayerControllers` | C_NetworkUtlVectorBase< CHandle< [CBasePlayerController](../schemas/client.md#cbaseplayercontroller) > > |  |
| `m_aPlayers` | C_NetworkUtlVectorBase< CHandle< [C_BasePlayerPawn](../schemas/client.md#c_baseplayerpawn) > > |  |
| `m_iScore` | int32 |  |
| `m_szTeamname` | char[129] |  |

### C_TeamplayRules

**Inherits from:** [C_MultiplayRules](client.md#c_multiplayrules)

**Derived by:** [C_CSGameRules](client.md#c_csgamerules)

**Relationships:**

```mermaid
classDiagram
    C_MultiplayRules <|-- C_TeamplayRules
    C_GameRules <|-- C_MultiplayRules
    C_TeamplayRules <|-- C_CSGameRules
```

### C_TextureBasedAnimatable

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_TextureBasedAnimatable
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_TextureBasedAnimatable *-- InfoForResourceTypeCTextureBase
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bLoop` | bool |  |
| `m_flFPS` | float32 |  |
| `m_hPositionKeys` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_hRotationKeys` | CStrongHandle< [InfoForResourceTypeCTextureBase](../schemas/resourcesystem.md#infoforresourcetypectexturebase) > |  |
| `m_vAnimationBoundsMin` | Vector |  |
| `m_vAnimationBoundsMax` | Vector |  |
| `m_flStartTime` | float32 | `MNotSaved` |
| `m_flStartFrame` | float32 |  |

### C_TintController

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_TintController
    CEntityInstance <|-- C_BaseEntity
```

### C_TonemapController2

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Derived by:** [C_TonemapController2Alias_env_tonemap_controller2](client.md#c_tonemapcontroller2alias_env_tonemap_controller2)

**Metadata:** `MEntityAllowsPortraitWorldSpawn`

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_TonemapController2
    CEntityInstance <|-- C_BaseEntity
    C_TonemapController2 <|-- C_TonemapController2Alias_env_tonemap_controller2
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flAutoExposureMin` | float32 |  |
| `m_flAutoExposureMax` | float32 |  |
| `m_flExposureAdaptationSpeedUp` | float32 |  |
| `m_flExposureAdaptationSpeedDown` | float32 |  |
| `m_flTonemapEVSmoothingRange` | float32 |  |

### C_TonemapController2Alias_env_tonemap_controller2

**Inherits from:** [C_TonemapController2](client.md#c_tonemapcontroller2)

**Relationships:**

```mermaid
classDiagram
    C_TonemapController2 <|-- C_TonemapController2Alias_env_tonemap_controller2
    C_BaseEntity <|-- C_TonemapController2
    CEntityInstance <|-- C_BaseEntity
```

### C_TriggerBuoyancy

**Inherits from:** [C_BaseTrigger](client.md#c_basetrigger)

**Relationships:**

```mermaid
classDiagram
    C_BaseTrigger <|-- C_TriggerBuoyancy
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
    C_TriggerBuoyancy *-- CBuoyancyHelper
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_BuoyancyHelper` | [CBuoyancyHelper](../schemas/client.md#cbuoyancyhelper) |  |
| `m_flFluidDensity` | float32 |  |

### C_TriggerLerpObject

**Inherits from:** [C_BaseTrigger](client.md#c_basetrigger)

**Relationships:**

```mermaid
classDiagram
    C_BaseTrigger <|-- C_TriggerLerpObject
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_TriggerMultiple

**Inherits from:** [C_BaseTrigger](client.md#c_basetrigger)

**Relationships:**

```mermaid
classDiagram
    C_BaseTrigger <|-- C_TriggerMultiple
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_TriggerPhysics

**Inherits from:** [C_BaseTrigger](client.md#c_basetrigger)

**Relationships:**

```mermaid
classDiagram
    C_BaseTrigger <|-- C_TriggerPhysics
    C_BaseToggle <|-- C_BaseTrigger
    C_BaseModelEntity <|-- C_BaseToggle
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_gravityScale` | float32 |  |
| `m_linearLimit` | float32 |  |
| `m_linearDamping` | float32 |  |
| `m_angularLimit` | float32 |  |
| `m_angularDamping` | float32 |  |
| `m_linearForce` | float32 |  |
| `m_flFrequency` | float32 |  |
| `m_flDampingRatio` | float32 |  |
| `m_vecLinearForcePointAt` | Vector |  |
| `m_bCollapseToForcePoint` | bool |  |
| `m_vecLinearForcePointAtWorld` | VectorWS |  |
| `m_vecLinearForceDirection` | Vector |  |
| `m_bConvertToDebrisWhenPossible` | bool |  |

### C_TriggerVolume

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_TriggerVolume
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_VoteController

**Inherits from:** [C_BaseEntity](client.md#c_baseentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseEntity <|-- C_VoteController
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iActiveIssueIndex` | int32 |  |
| `m_iOnlyTeamToVote` | int32 |  |
| `m_nVoteOptionCount` | int32[5] |  |
| `m_nPotentialVotes` | int32 |  |
| `m_bVotesDirty` | bool |  |
| `m_bTypeDirty` | bool |  |
| `m_bIsYesNoVote` | bool |  |

### C_WaterBullet

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_WaterBullet
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_WeaponAWP

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponAWP
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponAug

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponAug
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponBaseItem

**Inherits from:** [C_CSWeaponBase](client.md#c_csweaponbase)

**Derived by:** [C_Item_Healthshot](client.md#c_item_healthshot)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBase <|-- C_WeaponBaseItem
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_WeaponBaseItem <|-- C_Item_Healthshot
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bSequenceInProgress` | bool |  |
| `m_bRedraw` | bool |  |

### C_WeaponBizon

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponBizon
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponCZ75a

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponCZ75a
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bMagazineRemoved` | bool |  |

### C_WeaponElite

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponElite
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponFamas

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponFamas
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponFiveSeven

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponFiveSeven
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponG3SG1

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponG3SG1
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponGalilAR

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponGalilAR
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponGlock

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponGlock
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponHKP2000

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponHKP2000
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponM249

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponM249
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponM4A1

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponM4A1
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponM4A1Silencer

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponM4A1Silencer
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponMAC10

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponMAC10
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponMP5SD

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponMP5SD
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponMP7

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponMP7
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponMP9

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponMP9
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponMag7

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponMag7
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponNOVA

**Inherits from:** [C_CSWeaponBaseShotgun](client.md#c_csweaponbaseshotgun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseShotgun <|-- C_WeaponNOVA
    C_CSWeaponBase <|-- C_CSWeaponBaseShotgun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponNegev

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponNegev
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponP250

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponP250
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponP90

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponP90
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponRevolver

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponRevolver
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponSCAR20

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponSCAR20
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponSG556

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponSG556
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponSSG08

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponSSG08
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponSawedoff

**Inherits from:** [C_CSWeaponBaseShotgun](client.md#c_csweaponbaseshotgun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseShotgun <|-- C_WeaponSawedoff
    C_CSWeaponBase <|-- C_CSWeaponBaseShotgun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponTaser

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponTaser
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
    C_WeaponTaser *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_fFireTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_nLastAttackTick` | int32 |  |

### C_WeaponTec9

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponTec9
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponUMP45

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponUMP45
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponUSPSilencer

**Inherits from:** [C_CSWeaponBaseGun](client.md#c_csweaponbasegun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseGun <|-- C_WeaponUSPSilencer
    C_CSWeaponBase <|-- C_CSWeaponBaseGun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_WeaponXM1014

**Inherits from:** [C_CSWeaponBaseShotgun](client.md#c_csweaponbaseshotgun)

**Relationships:**

```mermaid
classDiagram
    C_CSWeaponBaseShotgun <|-- C_WeaponXM1014
    C_CSWeaponBase <|-- C_CSWeaponBaseShotgun
    C_BasePlayerWeapon <|-- C_CSWeaponBase
    C_EconEntity <|-- C_BasePlayerWeapon
    CBaseAnimGraph <|-- C_EconEntity
```

### C_World

**Inherits from:** [C_BaseModelEntity](client.md#c_basemodelentity)

**Relationships:**

```mermaid
classDiagram
    C_BaseModelEntity <|-- C_World
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_WorldModelGloves

**Inherits from:** [CBaseAnimGraph](client.md#cbaseanimgraph)

**Relationships:**

```mermaid
classDiagram
    CBaseAnimGraph <|-- C_WorldModelGloves
    C_BaseModelEntity <|-- CBaseAnimGraph
    C_BaseEntity <|-- C_BaseModelEntity
    CEntityInstance <|-- C_BaseEntity
```

### C_fogplayerparams_t

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    C_fogplayerparams_t --> C_FogController
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hCtrl` | CHandle< [C_FogController](../schemas/client.md#c_fogcontroller) > |  |
| `m_flTransitionTime` | float32 |  |
| `m_OldColor` | Color |  |
| `m_flOldStart` | float32 |  |
| `m_flOldEnd` | float32 |  |
| `m_flOldMaxDensity` | float32 | `MNotSaved` |
| `m_flOldHDRColorScale` | float32 | `MNotSaved` |
| `m_flOldFarZ` | float32 | `MNotSaved` |
| `m_NewColor` | Color |  |
| `m_flNewStart` | float32 |  |
| `m_flNewEnd` | float32 |  |
| `m_flNewMaxDensity` | float32 | `MNotSaved` |
| `m_flNewHDRColorScale` | float32 | `MNotSaved` |
| `m_flNewFarZ` | float32 | `MNotSaved` |

### CountdownTimer

**Metadata:** `MGetKV3ClassDefaults null`

**Relationships:**

```mermaid
classDiagram
    CountdownTimer *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_duration` | float32 |  |
| `m_timestamp` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_timescale` | float32 |  |
| `m_nWorldGroupId` | WorldGroupId_t |  |

### DestructiblePartDamageRequestAPI

### EngineCountdownTimer

**Metadata:** `MGetKV3ClassDefaults null`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_duration` | float32 |  |
| `m_timestamp` | float32 | `MKV3TransferSaveOpsForField GetEngineTimeSaveRestoreOps` |
| `m_timescale` | float32 |  |

### EntityRenderAttribute_t

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "EntityRenderAttribute_t",
	"m_ID": <HIDDEN FOR DIFF>,
	"m_Values":
	[
		0.000000,
		0.000000,
		0.000000,
		0.000000
	]
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_ID` | CUtlStringToken |  |
| `m_Values` | Vector4D |  |

### EntitySpottedState_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bSpotted` | bool |  |
| `m_bSpottedByMask` | uint32[2] |  |

### FilterDamageType

**Inherits from:** [CBaseFilter](client.md#cbasefilter)

**Relationships:**

```mermaid
classDiagram
    CBaseFilter <|-- FilterDamageType
    CLogicalEntity <|-- CBaseFilter
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_iDamageType` | int32 |  |

### FilterHealth

**Inherits from:** [CBaseFilter](client.md#cbasefilter)

**Relationships:**

```mermaid
classDiagram
    CBaseFilter <|-- FilterHealth
    CLogicalEntity <|-- CBaseFilter
    C_BaseEntity <|-- CLogicalEntity
    CEntityInstance <|-- C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bAdrenalineActive` | bool |  |
| `m_iHealthMin` | int32 |  |
| `m_iHealthMax` | int32 |  |

### IClientAlphaProperty

**Derived by:** [CClientAlphaProperty](client.md#cclientalphaproperty)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    IClientAlphaProperty <|-- CClientAlphaProperty
```

### IntervalTimer

**Derived by:** [CTimeline](client.md#ctimeline)

**Metadata:** `MGetKV3ClassDefaults null`

**Relationships:**

```mermaid
classDiagram
    IntervalTimer <|-- CTimeline
    IntervalTimer *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_timestamp` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_nWorldGroupId` | WorldGroupId_t |  |

### PhysicsRagdollPose_t

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "PhysicsRagdollPose_t",
	"m_Transforms":
	[
	],
	"m_hOwner": null
}`

**Relationships:**

```mermaid
classDiagram
    PhysicsRagdollPose_t --> C_BaseEntity
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Transforms` | C_NetworkUtlVectorBase< CTransform > |  |
| `m_hOwner` | CHandle< [C_BaseEntity](../schemas/client.md#c_baseentity) > |  |
| `m_bSetFromDebugHistory` | bool | `MNotSaved` |

### SellbackPurchaseEntry_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_unDefIdx` | uint16 |  |
| `m_nCost` | int32 |  |
| `m_nPrevArmor` | int32 |  |
| `m_bPrevHelmet` | bool |  |
| `m_hItem` | CEntityHandle |  |

### SequenceHistory_t

**Relationships:**

```mermaid
classDiagram
    SequenceHistory_t *-- HSequence
    SequenceHistory_t *-- GameTime_t
    SequenceHistory_t *-- AnimLoopMode_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_hSequence` | [HSequence](../schemas/animationsystem.md#hsequence) |  |
| `m_flSeqStartTime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `m_flSeqFixedCycle` | float32 |  |
| `m_nSeqLoopMode` | [AnimLoopMode_t](../schemas/!GlobalTypes.md#animloopmode_t) |  |
| `m_flPlaybackRate` | float32 |  |
| `m_flCyclesPerSecond` | float32 |  |

### ServerAuthoritativeWeaponSlot_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `unClass` | uint16 |  |
| `unSlot` | uint16 |  |
| `unItemDefIdx` | uint16 |  |

### TimedEvent

**Metadata:** `MGetKV3ClassDefaults {
	"m_TimeBetweenEvents": -1.000000,
	"m_fNextEvent": 0.000000
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_TimeBetweenEvents` | float32 |  |
| `m_fNextEvent` | float32 |  |

### VPhysicsCollisionAttribute_t

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "VPhysicsCollisionAttribute_t",
	"m_nInteractsAs": 0,
	"m_nInteractsWith": 0,
	"m_nInteractsExclude": 0,
	"m_nEntityId": 0,
	"m_nOwnerId": 0,
	"m_nHierarchyId": 0,
	"m_nDetailLayerMask": 0,
	"m_nDetailLayerMaskType": 0,
	"m_nTargetDetailLayer": 0,
	"m_nCollisionGroup": 0,
	"m_nCollisionFunctionMask": 0
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInteractsAs` | uint64 |  |
| `m_nInteractsWith` | uint64 |  |
| `m_nInteractsExclude` | uint64 |  |
| `m_nEntityId` | uint32 |  |
| `m_nOwnerId` | uint32 |  |
| `m_nHierarchyId` | uint16 |  |
| `m_nDetailLayerMask` | uint16 |  |
| `m_nDetailLayerMaskType` | uint8 |  |
| `m_nTargetDetailLayer` | uint8 |  |
| `m_nCollisionGroup` | uint8 |  |
| `m_nCollisionFunctionMask` | uint8 |  |

### ViewAngleServerChange_t

**Relationships:**

```mermaid
classDiagram
    ViewAngleServerChange_t *-- FixAngleSet_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nType` | [FixAngleSet_t](../schemas/!GlobalTypes.md#fixangleset_t) |  |
| `qAngle` | QAngle |  |
| `nIndex` | uint32 |  |

### WeaponPurchaseCount_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nItemDefIndex` | uint16 |  |
| `m_nCount` | uint16 |  |

### WeaponPurchaseTracker_t

**Relationships:**

```mermaid
classDiagram
    WeaponPurchaseTracker_t *-- WeaponPurchaseCount_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_weaponPurchases` | C_UtlVectorEmbeddedNetworkVar< [WeaponPurchaseCount_t](../schemas/client.md#weaponpurchasecount_t) > |  |

### audioparams_t

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "audioparams_t",
	"localSound":
	[
		null,
		null,
		null,
		null,
		null,
		null,
		null,
		null
	],
	"soundscapeIndex": 0,
	"localBits": 0,
	"soundscapeEntityListIndex": 0,
	"soundEventHash": 0
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `localSound` | VectorWS[8] |  |
| `soundscapeIndex` | int32 |  |
| `localBits` | uint8 |  |
| `soundscapeEntityListIndex` | int32 |  |
| `soundEventHash` | uint32 |  |

### fogparams_t

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "fogparams_t",
	"dirPrimary":
	[
		1.000000,
		0.000000,
		0.000000
	],
	"colorPrimary":
	[
		0,
		0,
		0,
		0
	],
	"colorSecondary":
	[
		0,
		0,
		0,
		0
	],
	"start": 0.000000,
	"end": 0.000000,
	"farz": 0.000000,
	"maxdensity": 0.000000,
	"exponent": 0.000000,
	"HDRColorScale": 0.000000,
	"duration": 0.000000,
	"blendtobackground": 0.000000,
	"scattering": 0.000000,
	"locallightscale": 1.000000,
	"enable": false,
	"blend": false
}`

**Relationships:**

```mermaid
classDiagram
    fogparams_t *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `dirPrimary` | Vector |  |
| `colorPrimary` | Color |  |
| `colorSecondary` | Color |  |
| `colorPrimaryLerpTo` | Color | `MNotSaved` |
| `colorSecondaryLerpTo` | Color | `MNotSaved` |
| `start` | float32 |  |
| `end` | float32 |  |
| `farz` | float32 |  |
| `maxdensity` | float32 |  |
| `exponent` | float32 |  |
| `HDRColorScale` | float32 |  |
| `skyboxFogFactor` | float32 | `MNotSaved` |
| `skyboxFogFactorLerpTo` | float32 | `MNotSaved` |
| `startLerpTo` | float32 | `MNotSaved` |
| `endLerpTo` | float32 | `MNotSaved` |
| `maxdensityLerpTo` | float32 | `MNotSaved` |
| `lerptime` | [GameTime_t](../schemas/entity2.md#gametime_t) | `MNotSaved` |
| `duration` | float32 |  |
| `blendtobackground` | float32 |  |
| `scattering` | float32 |  |
| `locallightscale` | float32 |  |
| `enable` | bool |  |
| `blend` | bool |  |
| `m_bPadding2` | bool | `MNotSaved` |
| `m_bPadding` | bool | `MNotSaved` |

### inv_image_camera_t

**Metadata:** `MGetKV3ClassDefaults {
	"angle":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"fov": 45.000000,
	"znear": 4.000000,
	"zfar": 1000.000000,
	"target":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"target_nudge":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"orbit_distance": 0.000000
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `angle` | QAngle | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Angle` |
| `fov` | float32 | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 360` `MPropertyFriendlyName FOV` |
| `znear` | float32 | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 1000` `MPropertyFriendlyName Z Near` |
| `zfar` | float32 | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 1000` `MPropertyFriendlyName Z Far` |
| `target` | Vector | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Target` |
| `target_nudge` | Vector | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Target Nudge` |
| `orbit_distance` | float32 | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 1000` `MPropertyFriendlyName Orbit Distance` |

### inv_image_clearcolor_t

**Metadata:** `MGetKV3ClassDefaults {
	"color":
	[
		0.200000,
		0.200000,
		0.200000
	]
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `color` | Vector | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeEditor VectorColor()` `MPropertyFriendlyName ClearColor` |

### inv_image_data_t

**Metadata:** `MGetKV3ClassDefaults {
	"map":
	{
		"map_name": "ui/icon_generation_basic_nuke_bombsitea",
		"map_rotation": 0.000000
	},
	"item":
	{
		"position":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"angle":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"pose_sequence": ""
	},
	"camera":
	{
		"angle":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"fov": 45.000000,
		"znear": 4.000000,
		"zfar": 1000.000000,
		"target":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"target_nudge":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"orbit_distance": 0.000000
	},
	"lightsun":
	{
		"color":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"angle":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"brightness": 1.000000
	},
	"lightfill":
	{
		"color":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"angle":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"brightness": 1.000000
	},
	"light0":
	{
		"color":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"angle":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"brightness": 0.000000,
		"orbit_distance": 1.000000
	},
	"light1":
	{
		"color":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"angle":
		[
			0.000000,
			0.000000,
			0.000000
		],
		"brightness": 0.000000,
		"orbit_distance": 1.000000
	},
	"clearcolor":
	{
		"color":
		[
			0.200000,
			0.200000,
			0.200000
		]
	}
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `map` | inv_image_map_t | `MPropertyAutoExpandSelf` `MPropertyFriendlyName Map` |
| `item` | inv_image_item_t | `MPropertyAutoExpandSelf` `MPropertyFriendlyName Item` |
| `camera` | inv_image_camera_t | `MPropertyAutoExpandSelf` `MPropertyFriendlyName Camera` |
| `lightsun` | inv_image_light_sun_t | `MPropertyAutoExpandSelf` `MPropertyDescription Shadowed.` `MPropertyFriendlyName Sun light` |
| `lightfill` | inv_image_light_fill_t | `MPropertyAutoExpandSelf` `MPropertyDescription No Shadows.` `MPropertyFriendlyName Fill light` |
| `light0` | inv_image_light_barn_t | `MPropertyAutoExpandSelf` `MPropertyDescription Shadowed.` `MPropertyFriendlyName Barn light 0` |
| `light1` | inv_image_light_barn_t | `MPropertyAutoExpandSelf` `MPropertyDescription Shadowed.` `MPropertyFriendlyName Barn light 1` |
| `clearcolor` | inv_image_clearcolor_t | `MPropertyAutoExpandSelf` `MPropertyDescription` `MPropertyFriendlyName Clear Color` |

### inv_image_item_t

**Metadata:** `MGetKV3ClassDefaults {
	"position":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"angle":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"pose_sequence": ""
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `position` | Vector | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Position` |
| `angle` | QAngle | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Angle` |
| `pose_sequence` | CUtlString | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Pose Sequence` |

### inv_image_light_barn_t

**Metadata:** `MGetKV3ClassDefaults {
	"color":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"angle":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"brightness": 0.000000,
	"orbit_distance": 1.000000
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `color` | Vector | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeEditor VectorColor()` `MPropertyFriendlyName Color` |
| `angle` | QAngle | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Angle` |
| `brightness` | float32 | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 10` `MPropertyFriendlyName Brightness` |
| `orbit_distance` | float32 | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 1000` `MPropertyFriendlyName Orbit Distance` |

### inv_image_light_fill_t

**Metadata:** `MGetKV3ClassDefaults {
	"color":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"angle":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"brightness": 1.000000
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `color` | Vector | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeEditor VectorColor()` `MPropertyFriendlyName Color` |
| `angle` | QAngle | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Angle` |
| `brightness` | float32 | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 10` `MPropertyFriendlyName Brightness` |

### inv_image_light_sun_t

**Metadata:** `MGetKV3ClassDefaults {
	"color":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"angle":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"brightness": 1.000000
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `color` | Vector | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeEditor VectorColor()` `MPropertyFriendlyName Color` |
| `angle` | QAngle | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Angle` |
| `brightness` | float32 | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 10` `MPropertyFriendlyName Brightness` |

### inv_image_map_t

**Metadata:** `MGetKV3ClassDefaults {
	"map_name": "ui/icon_generation_basic_nuke_bombsitea",
	"map_rotation": 0.000000
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `map_name` | CUtlString | `MPropertyFriendlyName Map` `MPropertyLeafChoiceProviderFn` |
| `map_rotation` | float32 | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange -180 180` `MPropertyFriendlyName Rotation` |

### screenfade_t

**Metadata:** `MGetKV3ClassDefaults {
	"Speed": 0.000000,
	"End": 0.000000,
	"Reset": 0.000000,
	"m_Color":
	[
		0,
		0,
		0,
		0
	],
	"Flags": 0
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `Speed` | float32 |  |
| `End` | float32 |  |
| `Reset` | float32 |  |
| `m_Color` | Color |  |
| `Flags` | int32 |  |

### screenshake_t

**Metadata:** `MGetKV3ClassDefaults {
	"endtime": null,
	"duration": 0.000000,
	"amplitude": 0.000000,
	"frequency": 0.000000,
	"nextShake": null,
	"offset":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"angle": 0.000000,
	"direction":
	[
		0.000000,
		0.000000,
		0.000000
	],
	"nShakeType": 0
}`

**Relationships:**

```mermaid
classDiagram
    screenshake_t *-- GameTime_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `endtime` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `duration` | float32 |  |
| `amplitude` | float32 |  |
| `frequency` | float32 |  |
| `nextShake` | [GameTime_t](../schemas/entity2.md#gametime_t) |  |
| `offset` | Vector |  |
| `angle` | float32 |  |
| `direction` | Vector |  |
| `nShakeType` | uint8 |  |

### shard_model_desc_t

**Relationships:**

```mermaid
classDiagram
    shard_model_desc_t *-- InfoForResourceTypeIMaterial2
    shard_model_desc_t *-- ShardSolid_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nModelID` | int32 |  |
| `m_hMaterialBase` | CStrongHandle< [InfoForResourceTypeIMaterial2](../schemas/resourcesystem.md#infoforresourcetypeimaterial2) > |  |
| `m_hMaterialDamageOverlay` | CStrongHandle< [InfoForResourceTypeIMaterial2](../schemas/resourcesystem.md#infoforresourcetypeimaterial2) > |  |
| `m_solid` | [ShardSolid_t](../schemas/!GlobalTypes.md#shardsolid_t) |  |
| `m_vecPanelSize` | Vector2D |  |
| `m_vecStressPositionA` | Vector2D |  |
| `m_vecStressPositionB` | Vector2D |  |
| `m_vecPanelVertices` | C_NetworkUtlVectorBase< Vector2D > |  |
| `m_vInitialPanelVertices` | C_NetworkUtlVectorBase< Vector4D > |  |
| `m_flGlassHalfThickness` | float32 |  |
| `m_bHasParent` | bool |  |
| `m_bParentFrozen` | bool |  |
| `m_SurfacePropStringToken` | CUtlStringToken |  |

### sky3dparams_t

**Metadata:** `MGetKV3ClassDefaults null`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `scale` | int16 |  |
| `origin` | VectorWS |  |
| `bClip3DSkyBoxNearToWorldFar` | bool | `MNotSaved` |
| `flClip3DSkyBoxNearToWorldFarOffset` | float32 | `MNotSaved` |
| `fog` | fogparams_t | `MNotSaved` |
| `m_nWorldGroupID` | WorldGroupId_t |  |
