---
title: CCSBot
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CCSBot

# CCSBot

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 24120 bytes (`0x5e38`) · **Align:** n/a (unspecified) · **Module:** server

**Inherits from:** [CBot](../server/CBot.md)

**Relationships:**

```mermaid
classDiagram
    CBot <|-- CCSBot
    CCSBot *-- CountdownTimer
    CCSBot --> CCSPlayerPawn
    CCSBot --> CBaseEntity
    CCSBot *-- IntervalTimer
    CCSBot *-- GameTime_t
```

## Memory layout

153 fields (140 declared here, 13 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x10` | `m_pController` | [CCSPlayerController](../server/CCSPlayerController.md)* | [CBot](../server/CBot.md) |  |
| `0x18` | `m_pPlayer` | [CCSPlayerPawn](../server/CCSPlayerPawn.md)* | [CBot](../server/CBot.md) |  |
| `0x20` | `m_bHasSpawned` | bool | [CBot](../server/CBot.md) |  |
| `0x24` | `m_id` | uint32 | [CBot](../server/CBot.md) |  |
| `0xc0` | `m_isRunning` | bool | [CBot](../server/CBot.md) |  |
| `0xc1` | `m_isCrouching` | bool | [CBot](../server/CBot.md) |  |
| `0xc4` | `m_forwardSpeed` | float32 | [CBot](../server/CBot.md) |  |
| `0xc8` | `m_leftSpeed` | float32 | [CBot](../server/CBot.md) |  |
| `0xcc` | `m_verticalSpeed` | float32 | [CBot](../server/CBot.md) |  |
| `0xd0` | `m_buttonFlags` | uint64 | [CBot](../server/CBot.md) |  |
| `0xd8` | `m_jumpTimestamp` | float32 | [CBot](../server/CBot.md) |  |
| `0xdc` | `m_viewForward` | Vector | [CBot](../server/CBot.md) |  |
| `0xf8` | `m_postureStackIndex` | int32 | [CBot](../server/CBot.md) |  |
| `0x108` | `m_eyePosition` | VectorWS |  |  |
| `0x114` | `m_name` | char[64] |  |  |
| `0x154` | `m_combatRange` | float32 |  |  |
| `0x158` | `m_isRogue` | bool |  |  |
| `0x160` | `m_rogueTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x17c` | `m_diedLastRound` | bool |  |  |
| `0x180` | `m_safeTime` | float32 |  |  |
| `0x184` | `m_wasSafe` | bool |  |  |
| `0x18c` | `m_blindFire` | bool |  |  |
| `0x190` | `m_surpriseTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x1a8` | `m_bAllowActive` | bool |  |  |
| `0x1a9` | `m_isFollowing` | bool |  |  |
| `0x1ac` | `m_leader` | CHandle< [CCSPlayerPawn](../server/CCSPlayerPawn.md) > |  |  |
| `0x1b0` | `m_followTimestamp` | float32 |  |  |
| `0x1b4` | `m_allowAutoFollowTime` | float32 |  |  |
| `0x1b8` | `m_hurryTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x1d0` | `m_alertTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x1e8` | `m_sneakTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x200` | `m_panicTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x5c8` | `m_stateTimestamp` | float32 |  |  |
| `0x5cc` | `m_isAttacking` | bool |  |  |
| `0x5cd` | `m_isOpeningDoor` | bool |  |  |
| `0x5d4` | `m_taskEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x5e4` | `m_goalPosition` | VectorWS |  |  |
| `0x5f0` | `m_goalEntity` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x5f4` | `m_avoid` | CHandle< [CBaseEntity](../server/CBaseEntity.md) > |  |  |
| `0x5f8` | `m_avoidTimestamp` | float32 |  |  |
| `0x5fc` | `m_isStopping` | bool |  |  |
| `0x5fd` | `m_hasVisitedEnemySpawn` | bool |  |  |
| `0x600` | `m_stillTimer` | [IntervalTimer](../server/IntervalTimer.md) |  |  |
| `0x610` | `m_bEyeAnglesUnderPathFinderControl` | bool |  |  |
| `0x4f00` | `m_pathIndex` | int32 |  |  |
| `0x4f04` | `m_areaEnteredTimestamp` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x4f08` | `m_repathTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x4f20` | `m_avoidFriendTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x4f38` | `m_isFriendInTheWay` | bool |  |  |
| `0x4f40` | `m_politeTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x4f58` | `m_isWaitingBehindFriend` | bool |  |  |
| `0x4f84` | `m_pathLadderEnd` | float32 |  |  |
| `0x4fd0` | `m_mustRunTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x4fe8` | `m_waitTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x5000` | `m_updateTravelDistanceTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x5018` | `m_playerTravelDistance` | float32[64] |  |  |
| `0x5118` | `m_travelDistancePhase` | uint8 |  |  |
| `0x52b0` | `m_hostageEscortCount` | uint8 |  |  |
| `0x52b4` | `m_hostageEscortCountTimestamp` | float32 |  |  |
| `0x52b8` | `m_desiredTeam` | int32 |  |  |
| `0x52bc` | `m_hasJoined` | bool |  |  |
| `0x52bd` | `m_isWaitingForHostage` | bool |  |  |
| `0x52c0` | `m_inhibitWaitingForHostageTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x52d8` | `m_waitForHostageTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x52f0` | `m_noisePosition` | VectorWS |  |  |
| `0x52fc` | `m_noiseTravelDistance` | float32 |  |  |
| `0x5300` | `m_noiseTimestamp` | float32 |  |  |
| `0x5308` | `m_noiseSource` | [CCSPlayerPawn](../server/CCSPlayerPawn.md)* |  |  |
| `0x5320` | `m_noiseBendTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x5338` | `m_bentNoisePosition` | VectorWS |  |  |
| `0x5344` | `m_bendNoisePositionValid` | bool |  |  |
| `0x5348` | `m_lookAroundStateTimestamp` | float32 |  |  |
| `0x534c` | `m_lookAheadAngle` | float32 |  |  |
| `0x5350` | `m_lookUpAngle` | float32 |  |  |
| `0x5354` | `m_forwardAngle` | float32 |  |  |
| `0x5358` | `m_inhibitLookAroundTimestamp` | float32 |  |  |
| `0x5360` | `m_lookAtSpot` | VectorWS |  |  |
| `0x5370` | `m_lookAtSpotDuration` | float32 |  |  |
| `0x5374` | `m_lookAtSpotTimestamp` | float32 |  |  |
| `0x5378` | `m_lookAtSpotAngleTolerance` | float32 |  |  |
| `0x537c` | `m_lookAtSpotClearIfClose` | bool |  |  |
| `0x537d` | `m_lookAtSpotAttack` | bool |  |  |
| `0x5380` | `m_lookAtDesc` | char* |  |  |
| `0x5388` | `m_peripheralTimestamp` | float32 |  |  |
| `0x5510` | `m_approachPointCount` | uint8 |  |  |
| `0x5514` | `m_approachPointViewPosition` | VectorWS |  |  |
| `0x5520` | `m_viewSteadyTimer` | [IntervalTimer](../server/IntervalTimer.md) |  |  |
| `0x5538` | `m_tossGrenadeTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x5558` | `m_isAvoidingGrenade` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x5578` | `m_spotCheckTimestamp` | float32 |  |  |
| `0x5980` | `m_checkedHidingSpotCount` | int32 |  |  |
| `0x5984` | `m_lookPitch` | float32 |  |  |
| `0x5988` | `m_lookPitchVel` | float32 |  |  |
| `0x598c` | `m_lookYaw` | float32 |  |  |
| `0x5990` | `m_lookYawVel` | float32 |  |  |
| `0x5994` | `m_targetSpot` | VectorWS |  |  |
| `0x59a0` | `m_targetSpotVelocity` | Vector |  |  |
| `0x59ac` | `m_targetSpotPredicted` | VectorWS |  |  |
| `0x59b8` | `m_aimError` | QAngle |  |  |
| `0x59c4` | `m_aimGoal` | QAngle |  |  |
| `0x59d0` | `m_targetSpotTime` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x59d4` | `m_aimFocus` | float32 |  |  |
| `0x59d8` | `m_aimFocusInterval` | float32 |  |  |
| `0x59dc` | `m_aimFocusNextUpdate` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x59e8` | `m_ignoreEnemiesTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x5a00` | `m_enemy` | CHandle< [CCSPlayerPawn](../server/CCSPlayerPawn.md) > |  |  |
| `0x5a04` | `m_isEnemyVisible` | bool |  |  |
| `0x5a05` | `m_visibleEnemyParts` | uint8 |  |  |
| `0x5a08` | `m_lastEnemyPosition` | VectorWS |  |  |
| `0x5a14` | `m_lastSawEnemyTimestamp` | float32 |  |  |
| `0x5a18` | `m_firstSawEnemyTimestamp` | float32 |  |  |
| `0x5a1c` | `m_currentEnemyAcquireTimestamp` | float32 |  |  |
| `0x5a20` | `m_enemyDeathTimestamp` | float32 |  |  |
| `0x5a24` | `m_friendDeathTimestamp` | float32 |  |  |
| `0x5a28` | `m_isLastEnemyDead` | bool |  |  |
| `0x5a2c` | `m_nearbyEnemyCount` | int32 |  |  |
| `0x5c38` | `m_bomber` | CHandle< [CCSPlayerPawn](../server/CCSPlayerPawn.md) > |  |  |
| `0x5c3c` | `m_nearbyFriendCount` | int32 |  |  |
| `0x5c40` | `m_closestVisibleFriend` | CHandle< [CCSPlayerPawn](../server/CCSPlayerPawn.md) > |  |  |
| `0x5c44` | `m_closestVisibleHumanFriend` | CHandle< [CCSPlayerPawn](../server/CCSPlayerPawn.md) > |  |  |
| `0x5c48` | `m_attentionInterval` | [IntervalTimer](../server/IntervalTimer.md) |  |  |
| `0x5c58` | `m_attacker` | CHandle< [CCSPlayerPawn](../server/CCSPlayerPawn.md) > |  |  |
| `0x5c5c` | `m_attackedTimestamp` | float32 |  |  |
| `0x5c60` | `m_burnedByFlamesTimer` | [IntervalTimer](../server/IntervalTimer.md) |  |  |
| `0x5c70` | `m_lastVictimID` | int32 |  |  |
| `0x5c74` | `m_isAimingAtEnemy` | bool |  |  |
| `0x5c75` | `m_isRapidFiring` | bool |  |  |
| `0x5c78` | `m_equipTimer` | [IntervalTimer](../server/IntervalTimer.md) |  |  |
| `0x5c88` | `m_zoomTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x5ca0` | `m_fireWeaponTimestamp` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x5ca8` | `m_lookForWeaponsOnGroundTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x5cc0` | `m_bIsSleeping` | bool |  |  |
| `0x5cc1` | `m_isEnemySniperVisible` | bool |  |  |
| `0x5cc8` | `m_sawEnemySniperTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x5d80` | `m_enemyQueueIndex` | uint8 |  |  |
| `0x5d81` | `m_enemyQueueCount` | uint8 |  |  |
| `0x5d82` | `m_enemyQueueAttendIndex` | uint8 |  |  |
| `0x5d83` | `m_isStuck` | bool |  |  |
| `0x5d84` | `m_stuckTimestamp` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x5d88` | `m_stuckSpot` | VectorWS |  |  |
| `0x5d98` | `m_wiggleTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x5db0` | `m_stuckJumpTimer` | [CountdownTimer](../server/CountdownTimer.md) |  |  |
| `0x5dc8` | `m_nextCleanupCheckTimestamp` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x5dcc` | `m_avgVel` | float32[10] |  |  |
| `0x5df4` | `m_avgVelIndex` | int32 |  |  |
| `0x5df8` | `m_avgVelCount` | int32 |  |  |
| `0x5dfc` | `m_lastOrigin` | VectorWS |  |  |
| `0x5e0c` | `m_lastRadioRecievedTimestamp` | float32 |  |  |
| `0x5e10` | `m_lastRadioSentTimestamp` | float32 |  |  |
| `0x5e14` | `m_radioSubject` | CHandle< [CCSPlayerPawn](../server/CCSPlayerPawn.md) > |  |  |
| `0x5e18` | `m_radioPosition` | VectorWS |  |  |
| `0x5e24` | `m_voiceEndTimestamp` | float32 |  |  |
| `0x5e30` | `m_lastValidReactionQueueFrame` | int32 |  |  |
