---
title: CPhysicsPropRespawnable
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CPhysicsPropRespawnable

# CPhysicsPropRespawnable

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 3184 bytes (`0xc70`) · **Align:** 16 · **Module:** server

**Inherits from:** [CPhysicsProp](../server/CPhysicsProp.md)

**Relationships:**

```mermaid
classDiagram
    CPhysicsProp <|-- CPhysicsPropRespawnable
    CBreakableProp <|-- CPhysicsProp
    CBaseProp <|-- CBreakableProp
    CBaseAnimGraph <|-- CBaseProp
    CBaseModelEntity <|-- CBaseAnimGraph
```

## Memory layout

227 fields (5 declared here, 222 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_iszPrivateVScripts` | CUtlSymbolLarge | [CEntityInstance](../entity2/CEntityInstance.md) |  |
| `0x10` | `m_pEntity` | [CEntityIdentity](../entity2/CEntityIdentity.md)* | [CEntityInstance](../entity2/CEntityInstance.md) | CEntityIdentity pointer — the entity's identity record (name, class, handle, flags). |
| `0x28` | `m_CScriptComponent` | [CScriptComponent](../entity2/CScriptComponent.md)* | [CEntityInstance](../entity2/CEntityInstance.md) | VScript component attached to the entity, when scripted. |
| `0x30` | `m_CBodyComponent` | [CBodyComponent](../server/CBodyComponent.md)* | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x38` | `m_NetworkTransmitComponent` | [CNetworkTransmitComponent](../server/CNetworkTransmitComponent.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x248` | `m_aThinkFunctions` | CUtlVector< thinkfunc_t > | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x260` | `m_iCurrentThinkContext` | int32 | [CBaseEntity](../server/CBaseEntity.md) | `MNotSaved` |
| `0x264` | `m_nLastThinkTick` | [GameTick_t](../entity2/GameTick_t.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x268` | `m_bDisabledContextThinks` | bool | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x278` | `m_isSteadyState` | CTypedBitVec< 64 > | [CBaseEntity](../server/CBaseEntity.md) | `MNotSaved` |
| `0x280` | `m_lastNetworkChange` | float32 | [CBaseEntity](../server/CBaseEntity.md) | `MNotSaved` |
| `0x288` | `m_think` | BASEPTR | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x290` | `m_ResponseContexts` | CUtlVector< [ResponseContext_t](../server/ResponseContext_t.md) > | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2a8` | `m_iszResponseContext` | CUtlSymbolLarge | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2b0` | `m_pfnTouch` | ENTITYFUNCPTR | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2b8` | `m_pfnUse` | USEPTR | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2c0` | `m_pfnBlocked` | ENTITYFUNCPTR | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2c8` | `m_pfnMoveDone` | BASEPTR | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2d0` | `m_iHealth` | int32 | [CBaseEntity](../server/CBaseEntity.md) | Current health points of the entity. Serialised with the 'ClampHealth' encoder so values above max are clamped. *Sent only to the Player network group and LocalPlayerExclusive.* |
| `0x2d4` | `m_iMaxHealth` | int32 | [CBaseEntity](../server/CBaseEntity.md) | Maximum health points; used to normalise health bars in the HUD. |
| `0x2d8` | `m_lifeState` | uint8 | [CBaseEntity](../server/CBaseEntity.md) | LIFE_STATE enum: 0 = Alive, 1 = Dying, 2 = Dead, 3 = Respawnable, 4 = Discardbody. |
| `0x2dc` | `m_flDamageAccumulator` | float32 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2e0` | `m_bTakesDamage` | bool | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2e8` | `m_nTakeDamageFlags` | [TakeDamageFlags_t](../server/TakeDamageFlags_t.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2f0` | `m_nPlatformType` | [EntityPlatformTypes_t](../server/EntityPlatformTypes_t.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2f2` | `m_MoveCollide` | [MoveCollide_t](../server/MoveCollide_t.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2f3` | `m_MoveType` | [MoveType_t](../server/MoveType_t.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2f4` | `m_nPreviouslySetMoveType` | [MoveType_t](../server/MoveType_t.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2f5` | `m_nActualMoveType` | [MoveType_t](../server/MoveType_t.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x2f6` | `m_nWaterTouch` | uint8 | [CBaseEntity](../server/CBaseEntity.md) | `MNotSaved` |
| `0x2f7` | `m_nSlimeTouch` | uint8 | [CBaseEntity](../server/CBaseEntity.md) | `MNotSaved` |
| `0x2f8` | `m_bRestoreInHierarchy` | bool | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x300` | `m_target` | CUtlSymbolLarge | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x308` | `m_hDamageFilter` | CHandle< [CBaseFilter](../server/CBaseFilter.md) > | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x310` | `m_iszDamageFilterName` | CUtlSymbolLarge | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x318` | `m_flMoveDoneTime` | float32 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x31c` | `m_nSubclassID` | CUtlStringToken | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x328` | `m_flAnimTime` | float32 | [CBaseEntity](../server/CBaseEntity.md) | Floating-point timestamp of the most-recent animation update; used by the client for animation interpolation. `MKV3TransferSaveOpsForField GetEngineTimeSaveRestoreOps` |
| `0x32c` | `m_flSimulationTime` | float32 | [CBaseEntity](../server/CBaseEntity.md) | Floating-point timestamp of the most-recent physics simulation step; used by the client for position interpolation. `MKV3TransferSaveOpsForField GetEngineTimeSaveRestoreOps` |
| `0x330` | `m_flCreateTime` | [GameTime_t](../entity2/GameTime_t.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x334` | `m_bClientSideRagdoll` | bool | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x335` | `m_ubInterpolationFrame` | uint8 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x338` | `m_vPrevVPhysicsUpdatePos` | VectorWS | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x344` | `m_iTeamNum` | uint8 | [CBaseEntity](../server/CBaseEntity.md) | Team number: 0 = Unassigned, 1 = Spectator, 2 = Terrorist, 3 = Counter-Terrorist. |
| `0x348` | `m_iGlobalname` | CUtlSymbolLarge | [CBaseEntity](../server/CBaseEntity.md) | `MSaveBehavior` |
| `0x350` | `m_iSentToClients` | int32 | [CBaseEntity](../server/CBaseEntity.md) | `MNotSaved` |
| `0x358` | `m_sUniqueHammerID` | CUtlString | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x360` | `m_spawnflags` | uint32 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x364` | `m_nNextThinkTick` | [GameTick_t](../entity2/GameTick_t.md) | [CBaseEntity](../server/CBaseEntity.md) | Server tick on which the entity's Think() function will next execute (-1 = never). |
| `0x368` | `m_nSimulationTick` | int32 | [CBaseEntity](../server/CBaseEntity.md) | `MKV3TransferSaveOpsForField GetEngineTickSaveRestoreOps` |
| `0x370` | `m_OnKilled` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x388` | `m_fFlags` | uint32 | [CBaseEntity](../server/CBaseEntity.md) | Entity flags bitmask (FL_ONGROUND = 1, FL_DUCKING = 4, FL_INWATER = 8, FL_FROZEN = 0x200, etc.). |
| `0x38c` | `m_vecAbsVelocity` | Vector | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x398` | `m_vecVelocity` | [CNetworkVelocityVector](../server/CNetworkVelocityVector.md) | [CBaseEntity](../server/CBaseEntity.md) | Current world-space velocity vector of the entity. |
| `0x3c8` | `m_vecBaseVelocity` | Vector | [CBaseEntity](../server/CBaseEntity.md) | Additional world-space velocity contributed by moving platforms, conveyor belts, etc. |
| `0x3d4` | `m_nPushEnumCount` | int32 | [CBaseEntity](../server/CBaseEntity.md) | `MNotSaved` |
| `0x3d8` | `m_pCollision` | [CCollisionProperty](../server/CCollisionProperty.md)* | [CBaseEntity](../server/CBaseEntity.md) | `MNotSaved` |
| `0x3e0` | `m_hEffectEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x3e4` | `m_hOwnerEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > | [CBaseEntity](../server/CBaseEntity.md) | CHandle to the entity that owns or spawned this entity (e.g. the thrower of a grenade). |
| `0x3e8` | `m_fEffects` | uint32 | [CBaseEntity](../server/CBaseEntity.md) | Effect flags bitmask (EF_NODRAW = 32, EF_NORECEIVESHADOW = 64, etc.). |
| `0x3ec` | `m_hGroundEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > | [CBaseEntity](../server/CBaseEntity.md) | CHandle to the entity this entity is standing on (INVALID_EHANDLE if airborne). |
| `0x3f0` | `m_nGroundBodyIndex` | int32 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x3f4` | `m_flFriction` | float32 | [CBaseEntity](../server/CBaseEntity.md) | Surface friction multiplier (1.0 = normal; lower values make the entity slide more). |
| `0x3f8` | `m_flElasticity` | float32 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x3fc` | `m_flGravityScale` | float32 | [CBaseEntity](../server/CBaseEntity.md) | Gravity scale multiplier (1.0 = normal; 0 = no gravity). |
| `0x400` | `m_flTimeScale` | float32 | [CBaseEntity](../server/CBaseEntity.md) | Time-scale multiplier applied to this entity's simulation (1.0 = real time; used by bullet time effects). |
| `0x404` | `m_flWaterLevel` | float32 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x408` | `m_bGravityDisabled` | bool | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x409` | `m_bAnimatedEveryTick` | bool | [CBaseEntity](../server/CBaseEntity.md) | True when the entity's animation must be updated every server tick regardless of network interest. |
| `0x40c` | `m_flActualGravityScale` | float32 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x410` | `m_bGravityActuallyDisabled` | bool | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x411` | `m_bDisableLowViolence` | bool | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x412` | `m_nWaterType` | uint8 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x414` | `m_iEFlags` | int32 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x418` | `m_OnUser1` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x430` | `m_OnUser2` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x448` | `m_OnUser3` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x460` | `m_OnUser4` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x478` | `m_iInitialTeamNum` | int32 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x47c` | `m_flNavIgnoreUntilTime` | [GameTime_t](../entity2/GameTime_t.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x480` | `m_vecAngVelocity` | QAngle | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x48c` | `m_bNetworkQuantizeOriginAndAngles` | bool | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x48d` | `m_bLagCompensate` | bool | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x490` | `m_pBlocker` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x494` | `m_flLocalTime` | float32 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x498` | `m_flVPhysicsUpdateLocalTime` | float32 | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x49c` | `m_nBloodType` | [BloodType](../server/BloodType.md) | [CBaseEntity](../server/CBaseEntity.md) |  |
| `0x4a0` | `m_pPulseGraphInstance` | [CPulseGraphInstance_ServerEntity](../server/CPulseGraphInstance_ServerEntity.md)* | [CBaseEntity](../server/CBaseEntity.md) | `MKV3TransferSaveOpsForField GetPulseInstanceSaveRestoreOps` |
| `0x4a8` | `m_CRenderComponent` | [CRenderComponent](../server/CRenderComponent.md)* | [CBaseModelEntity](../server/CBaseModelEntity.md) | `MNotSaved` |
| `0x4b0` | `m_CHitboxComponent` | [CHitboxComponent](../server/CHitboxComponent.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4c8` | `m_pChoreoComponent` | [CChoreoComponent](../server/CChoreoComponent.md)* | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4d0` | `m_nDestructiblePartInitialStateDestructed0` | [HitGroup_t](../server/HitGroup_t.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4d4` | `m_nDestructiblePartInitialStateDestructed1` | [HitGroup_t](../server/HitGroup_t.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4d8` | `m_nDestructiblePartInitialStateDestructed2` | [HitGroup_t](../server/HitGroup_t.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4dc` | `m_nDestructiblePartInitialStateDestructed3` | [HitGroup_t](../server/HitGroup_t.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4e0` | `m_nDestructiblePartInitialStateDestructed4` | [HitGroup_t](../server/HitGroup_t.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4e4` | `m_nDestructiblePartInitialStateDestructed0_PartIndex` | int32 | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4e8` | `m_nDestructiblePartInitialStateDestructed1_PartIndex` | int32 | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4ec` | `m_nDestructiblePartInitialStateDestructed2_PartIndex` | int32 | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4f0` | `m_nDestructiblePartInitialStateDestructed3_PartIndex` | int32 | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4f4` | `m_nDestructiblePartInitialStateDestructed4_PartIndex` | int32 | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4f8` | `m_bDestructiblePartInitialStateDestructed0_GenerateBreakpieces` | bool | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4f9` | `m_bDestructiblePartInitialStateDestructed1_GenerateBreakpieces` | bool | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4fa` | `m_bDestructiblePartInitialStateDestructed2_GenerateBreakpieces` | bool | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4fb` | `m_bDestructiblePartInitialStateDestructed3_GenerateBreakpieces` | bool | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x4fc` | `m_bDestructiblePartInitialStateDestructed4_GenerateBreakpieces` | bool | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x500` | `m_pDestructiblePartsSystemComponent` | [CDestructiblePartsComponent](../server/CDestructiblePartsComponent.md)* | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x508` | `m_OnDestructibleHitGroupDamageLevelChanged` | CEntityOutputTemplate< [CBaseModelEntity::OnDamageLevelChangedArgs_t](../server/CBaseModelEntity.OnDamageLevelChangedArgs_t.md) > | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x530` | `m_flDissolveStartTime` | [GameTime_t](../entity2/GameTime_t.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x538` | `m_OnIgnite` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x550` | `m_nRenderMode` | [RenderMode_t](../server/RenderMode_t.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) | RenderMode_t enum controlling transparency and rendering method (0 = Normal, 5 = Translucent, etc.). |
| `0x551` | `m_nRenderFX` | [RenderFx_t](../server/RenderFx_t.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) | RenderFx_t enum for special rendering effects (pulsing, fading, hologram, etc.). |
| `0x552` | `m_bAllowFadeInView` | bool | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x570` | `m_clrRender` | Color | [CBaseModelEntity](../server/CBaseModelEntity.md) | RGBA tint colour multiplied onto the entity's diffuse texture. |
| `0x578` | `m_vecRenderAttributes` | CUtlVectorEmbeddedNetworkVar< [EntityRenderAttribute_t](../server/EntityRenderAttribute_t.md) > | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x5e0` | `m_bRenderToCubemaps` | bool | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x5e1` | `m_bNoInterpolate` | bool | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x5e8` | `m_Collision` | [CCollisionProperty](../server/CCollisionProperty.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) | CCollisionProperty struct encoding the entity's collision bounding box shape and flags. |
| `0x6a0` | `m_Glow` | [CGlowProperty](../server/CGlowProperty.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) | CGlowProperty struct controlling the entity's glow outline (colour, radius, visibility rules). |
| `0x6f8` | `m_flGlowBackfaceMult` | float32 | [CBaseModelEntity](../server/CBaseModelEntity.md) | Multiplier for the glow effect on back-facing surfaces of the model. |
| `0x6fc` | `m_fadeMinDist` | float32 | [CBaseModelEntity](../server/CBaseModelEntity.md) | Minimum distance (world units) at which the entity starts to fade out. |
| `0x700` | `m_fadeMaxDist` | float32 | [CBaseModelEntity](../server/CBaseModelEntity.md) | Distance at which the entity is fully faded out and invisible. |
| `0x704` | `m_flFadeScale` | float32 | [CBaseModelEntity](../server/CBaseModelEntity.md) | Scale factor applied to fade distances; 0 disables distance fading. |
| `0x708` | `m_flShadowStrength` | float32 | [CBaseModelEntity](../server/CBaseModelEntity.md) | Opacity of this entity's cast shadow (0 = no shadow, 1 = full shadow). |
| `0x70c` | `m_nObjectCulling` | uint8 | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x710` | `m_bodyGroupChoices` | CUtlOrderedMap< CGlobalSymbol, int32 > | [CBaseModelEntity](../server/CBaseModelEntity.md) |  |
| `0x738` | `m_vecViewOffset` | [CNetworkViewOffsetVector](../server/CNetworkViewOffsetVector.md) | [CBaseModelEntity](../server/CBaseModelEntity.md) | Offset from the entity origin to the player's view position (eye height). |
| `0x768` | `m_bvDisabledHitGroups` | uint32[1] | [CBaseModelEntity](../server/CBaseModelEntity.md) | `MKV3TransferSaveOpsForField GetHitgroupDisableListSaveRestoreOps` |
| `0x770` | `m_graphControllerManager` | [CAnimGraphControllerManager](../server/CAnimGraphControllerManager.md) | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x808` | `m_pMainGraphController` | [CAnimGraphControllerPtr](../server/CAnimGraphControllerPtr.md) | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | The primary animation-graph controller instance for this entity. |
| `0x810` | `m_bInitiallyPopulateInterpHistory` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x818` | `m_OnLayerCycleUpdated` | CEntityOutputTemplate< float32 > | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x838` | `m_OnExternalChoreoGraphChanged` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x850` | `m_pChoreoServices` | [IChoreoServices](../server/IChoreoServices.md)* | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MKV3TransferSaveOpsForField GetChoreoServicesSaveRestoreOps` |
| `0x858` | `m_bAnimGraphUpdateEnabled` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x859` | `m_bAnimationUpdateScheduled` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MNotSaved` |
| `0x85c` | `m_vecForce` | Vector | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MNotSaved` |
| `0x868` | `m_nForceBone` | int32 | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MNotSaved` |
| `0x878` | `m_pRagdollControl` | [IPhysicsRagdollControl](../vphysics2/IPhysicsRagdollControl.md)* | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MPhysPtr` |
| `0x880` | `m_RagdollPose` | [PhysicsRagdollPose_t](../server/PhysicsRagdollPose_t.md) | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x8a8` | `m_bRagdollEnabled` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | True while the entity is simulated as a ragdoll rather than animated. |
| `0x8a9` | `m_bRagdollClientSide` | bool | [CBaseAnimGraph](../server/CBaseAnimGraph.md) | `MNotSaved` |
| `0x8b0` | `m_xParentedRagdollRootInEntitySpace` | CTransform | [CBaseAnimGraph](../server/CBaseAnimGraph.md) |  |
| `0x960` | `m_bModelOverrodeBlockLOS` | bool | [CBaseProp](../server/CBaseProp.md) |  |
| `0x964` | `m_iShapeType` | int32 | [CBaseProp](../server/CBaseProp.md) |  |
| `0x968` | `m_bConformToCollisionBounds` | bool | [CBaseProp](../server/CBaseProp.md) |  |
| `0x970` | `m_mPreferredCatchTransform` | CTransform | [CBaseProp](../server/CBaseProp.md) |  |
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
| `0xb00` | `m_MotionEnabled` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xb18` | `m_OnAwakened` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xb30` | `m_OnAwake` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xb48` | `m_OnAsleep` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xb60` | `m_OnPlayerUse` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xb78` | `m_OnOutOfWorld` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xb90` | `m_OnPlayerPickup` | [CEntityIOOutput](../entity2/CEntityIOOutput.md) | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xba8` | `m_bForceNavIgnore` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xba9` | `m_bNoNavmeshBlocker` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbaa` | `m_bForceNpcExclude` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbac` | `m_massScale` | float32 | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbb0` | `m_buoyancyScale` | float32 | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbb4` | `m_damageType` | int32 | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbb8` | `m_damageToEnableMotion` | int32 | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbbc` | `m_flForceToEnableMotion` | float32 | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbc0` | `m_bThrownByPlayer` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbc1` | `m_bDroppedByPlayer` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbc2` | `m_bTouchedByPlayer` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbc3` | `m_bFirstCollisionAfterLaunch` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbc4` | `m_bHasBeenAwakened` | bool | [CPhysicsProp](../server/CPhysicsProp.md) | `MNotSaved` |
| `0xbc5` | `m_bIsOverrideProp` | bool | [CPhysicsProp](../server/CPhysicsProp.md) | `MNotSaved` |
| `0xbc8` | `m_flLastBurn` | [GameTime_t](../entity2/GameTime_t.md) | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbcc` | `m_nDynamicContinuousContactBehavior` | [DynamicContinuousContactBehavior_t](../physicslib/DynamicContinuousContactBehavior_t.md) | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbd0` | `m_fNextCheckDisableMotionContactsTime` | [GameTime_t](../entity2/GameTime_t.md) | [CPhysicsProp](../server/CPhysicsProp.md) | `MNotSaved` |
| `0xbd4` | `m_iInitialGlowState` | int32 | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbd8` | `m_nGlowRange` | int32 | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbdc` | `m_nGlowRangeMin` | int32 | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbe0` | `m_glowColor` | Color | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbe4` | `m_bShouldAutoConvertBackFromDebris` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbe5` | `m_bMuteImpactEffects` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbe8` | `m_nNavObstacleType` | [INavObstacle::NavObstacleType_t](../server/INavObstacle.NavObstacleType_t.md) | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbec` | `m_bUpdateNavWhenMoving` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbed` | `m_bForceNavObstacleCut` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbee` | `m_bAllowObstacleConvexHullMerging` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbef` | `m_bAcceptDamageFromHeldObjects` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbf0` | `m_bEnableUseOutput` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbf4` | `m_CrateType` | [CPhysicsProp::CrateType_t](../server/CPhysicsProp.CrateType_t.md) | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xbf8` | `m_strItemClass` | CUtlSymbolLarge[4] | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xc18` | `m_nItemCount` | int32[4] | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xc28` | `m_bRemovableForAmmoBalancing` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xc29` | `m_bAwake` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xc2a` | `m_bAttachedToReferenceFrame` | bool | [CPhysicsProp](../server/CPhysicsProp.md) |  |
| `0xc30` | `m_vOriginalSpawnOrigin` | VectorWS |  |  |
| `0xc3c` | `m_vOriginalSpawnAngles` | QAngle |  |  |
| `0xc48` | `m_vOriginalMins` | Vector |  |  |
| `0xc54` | `m_vOriginalMaxs` | Vector |  |  |
| `0xc60` | `m_flRespawnDuration` | float32 |  |  |
