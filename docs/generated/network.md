---
layout: default
title: Network Messages
nav_order: 8
---

# Network & Demo Messages

{: .note }
> Source: CS2 build **24134959** · 2026-07-09 · `windows-x86_64` · schema `0.4.0`

The wire-protocol tables: integer message IDs mapped to the protobuf message type carried, recovered from a static RTTI scan of the shipped binaries.  Each type links to its definition on the [protobuf pages](protobufs.md).

## Bidirectional (3)

| ID | Message type |
|----|--------------|
| 16 | `CBidirMsg_RebroadcastGameEvent` |
| 17 | `CBidirMsg_RebroadcastSource` |
| 19 | `CBidirMsg_PredictionEvent` |

## ClcMessages (15)

| ID | Message type |
|----|--------------|
| 20 | `CCLCMsg_ClientInfo` |
| 21 | `CCLCMsg_Move` |
| 22 | `CCLCMsg_VoiceData` |
| 23 | `CCLCMsg_BaselineAck` |
| 25 | `CCLCMsg_RespondCvarValue` |
| 27 | `CCLCMsg_LoadingProgress` |
| 28 | `CCLCMsg_SplitPlayerConnect` |
| 30 | `CCLCMsg_SplitPlayerDisconnect` |
| 31 | `CCLCMsg_ServerStatus` |
| 33 | `CCLCMsg_RequestPause` |
| 34 | `CCLCMsg_CmdKeyValues` |
| 35 | `CCLCMsg_RconServerDetails` |
| 36 | `CCLCMsg_HltvReplay` |
| 37 | `CCLCMsg_Diagnostic` |
| 75 | `CCLCMsg_HltvFixupOperatorTick` |

## ClientMessages (3)

| ID | Message type |
|----|--------------|
| 280 | `CClientMsg_CustomGameEvent` |
| 281 | `CClientMsg_CustomGameEventBounce` |
| 282 | `CClientMsg_ClientUIEvent` |

## Decals (4)

| ID | Message type |
|----|--------------|
| 201 | `CMsgPlaceDecalEvent` |
| 202 | `CMsgClearWorldDecalsEvent` |
| 203 | `CMsgClearEntityDecalsEvent` |
| 204 | `CMsgClearDecalsForEntityEvent` |

## GameEvents (3)

| ID | Message type |
|----|--------------|
| 213 | `CMsgClothStiffenAnimEvent` |
| 214 | `CMsgClothEffectAnimEvent` |
| 453 | `CMsgPlayerBulletHit` |

## NetMessages (12)

| ID | Message type |
|----|--------------|
| 0 | `CNETMsg_NOP` |
| 3 | `CNETMsg_SplitScreenUser` |
| 4 | `CNETMsg_Tick` |
| 5 | `CNETMsg_StringCmd` |
| 6 | `CNETMsg_SetConVar` |
| 7 | `CNETMsg_SignonState` |
| 8 | `CNETMsg_SpawnGroup_Load` |
| 9 | `CNETMsg_SpawnGroup_ManifestUpdate` |
| 11 | `CNETMsg_SpawnGroup_SetCreationTick` |
| 12 | `CNETMsg_SpawnGroup_Unload` |
| 13 | `CNETMsg_SpawnGroup_LoadCompleted` |
| 15 | `CNETMsg_DebugOverlay` |

## PeerToPeer (3)

| ID | Message type |
|----|--------------|
| 256 | [`CP2P_TextMessage`](proto/c_peer2peer_netmessages.md) |
| 257 | [`CP2P_Voice`](proto/c_peer2peer_netmessages.md) |
| 258 | [`CP2P_Ping`](proto/c_peer2peer_netmessages.md) |

## Sounds (5)

| ID | Message type |
|----|--------------|
| 208 | `CMsgSosStartSoundEvent` |
| 209 | `CMsgSosStopSoundEvent` |
| 210 | `CMsgSosSetSoundEventParams` |
| 211 | `CMsgSosSetLibraryStackFields` |
| 212 | `CMsgSosStopSoundEventHash` |

## Source1Legacy (3)

| ID | Message type |
|----|--------------|
| 205 | `CMsgSource1LegacyGameEventList` |
| 206 | `CMsgSource1LegacyListenEvents` |
| 207 | `CMsgSource1LegacyGameEvent` |

## SvcMessages (29)

| ID | Message type |
|----|--------------|
| 40 | `CSVCMsg_ServerInfo` |
| 41 | `CSVCMsg_FlattenedSerializer` |
| 42 | `CSVCMsg_ClassInfo` |
| 43 | `CSVCMsg_SetPause` |
| 44 | `CSVCMsg_CreateStringTable` |
| 45 | `CSVCMsg_UpdateStringTable` |
| 46 | `CSVCMsg_VoiceInit` |
| 47 | `CSVCMsg_VoiceData` |
| 48 | `CSVCMsg_Print` |
| 49 | `CSVCMsg_Sounds` |
| 50 | `CSVCMsg_SetView` |
| 51 | `CSVCMsg_ClearAllStringTables` |
| 52 | `CSVCMsg_CmdKeyValues` |
| 54 | `CSVCMsg_SplitScreen` |
| 55 | `CSVCMsg_PacketEntities` |
| 56 | `CSVCMsg_Prefetch` |
| 57 | `CSVCMsg_Menu` |
| 58 | `CSVCMsg_GetCvarValue` |
| 59 | `CSVCMsg_StopSound` |
| 60 | `CSVCMsg_PeerList` |
| 61 | `CSVCMsg_PacketReliable` |
| 62 | `CSVCMsg_HLTVStatus` |
| 63 | `CSVCMsg_ServerSteamID` |
| 70 | `CSVCMsg_FullFrameSplit` |
| 71 | `CSVCMsg_RconServerDetails` |
| 72 | `CSVCMsg_UserMessage` |
| 74 | `CSVCMsg_HltvReplay` |
| 76 | `CSVCMsg_UserCommands` |
| 77 | `CSVCMsg_NextMsgPredicted` |

## TempEntities (23)

| ID | Message type |
|----|--------------|
| 400 | `CMsgTEEffectDispatch` |
| 401 | `CMsgTEArmorRicochet` |
| 402 | `CMsgTEBeamEntPoint` |
| 403 | `CMsgTEBeamEnts` |
| 404 | `CMsgTEBeamPoints` |
| 405 | `CMsgTEBeamRing` |
| 408 | `CMsgTEBubbles` |
| 409 | `CMsgTEBubbleTrail` |
| 410 | `CMsgTEDecal` |
| 411 | `CMsgTEWorldDecal` |
| 412 | `CMsgTEEnergySplash` |
| 413 | `CMsgTEFizz` |
| 415 | `CMsgTEGlowSprite` |
| 416 | `CMsgTEImpact` |
| 417 | `CMsgTEMuzzleFlash` |
| 418 | `CMsgTEBloodStream` |
| 419 | `CMsgTEExplosion` |
| 420 | `CMsgTEDust` |
| 421 | `CMsgTELargeFunnel` |
| 422 | `CMsgTESparks` |
| 423 | `CMsgTEPhysicsProp` |
| 426 | `CMsgTESmoke` |
| 452 | `CMsgTEFireBullets` |

## UserMessages (89)

| ID | Message type |
|----|--------------|
| 101 | `CUserMessageAchievementEvent` |
| 104 | `CUserMessageCurrentTimescale` |
| 105 | `CUserMessageDesiredTimescale` |
| 106 | `CUserMessageFade` |
| 110 | `CUserMessageHudMsg` |
| 111 | `CUserMessageHudText` |
| 113 | `CUserMessageColoredText` |
| 114 | `CUserMessageRequestState` |
| 115 | `CUserMessageResetHUD` |
| 116 | `CUserMessageRumble` |
| 117 | `CUserMessageSayText` |
| 118 | `CUserMessageSayText2` |
| 119 | `CUserMessageSayTextChannel` |
| 120 | `CUserMessageShake` |
| 121 | `CUserMessageShakeDir` |
| 122 | `CUserMessageWaterShake` |
| 124 | `CUserMessageTextMsg` |
| 125 | `CUserMessageScreenTilt` |
| 128 | `CUserMessageVoiceMask` |
| 130 | `CUserMessageSendAudio` |
| 131 | `CUserMessageItemPickup` |
| 132 | `CUserMessageAmmoDenied` |
| 134 | `CUserMessageShowMenu` |
| 135 | `CUserMessageCreditsMsg` |
| 137 | `CEntityMessageScreenOverlay` |
| 139 | `CEntityMessagePropagateForce` |
| 140 | `CEntityMessageDoSpark` |
| 142 | `CUserMessageCloseCaptionPlaceholder` |
| 143 | `CUserMessageCameraTransition` |
| 144 | `CUserMessageAudioParameter` |
| 145 | `CUserMsg_ParticleManager` |
| 146 | `CUserMsg_HudError` |
| 148 | `CUserMsg_CustomGameEvent` |
| 150 | `CUserMessageHapticsManagerPulse` |
| 151 | `CUserMessageHapticsManagerEffect` |
| 153 | `CUserMessageUpdateCssClasses` |
| 154 | `CUserMessageServerFrameTime` |
| 155 | `CUserMessageLagCompensationError` |
| 156 | `CUserMessageRequestDllStatus` |
| 157 | `CUserMessageRequestUtilAction` |
| 160 | `CUserMessageRequestInventory` |
| 162 | `CUserMessageRequestDiagnostic` |
| 165 | `CUserMessage_NotifyResponseFound` |
| 166 | `CUserMessage_PlayResponseConditional` |
| 301 | `CCSUsrMsg_VGUIMenu` |
| 317 | `CCSUsrMsg_SendAudio` |
| 318 | `CCSUsrMsg_RawAudio` |
| 321 | `CCSUsrMsg_Damage` |
| 322 | `CCSUsrMsg_RadioText` |
| 323 | `CCSUsrMsg_HintText` |
| 324 | `CCSUsrMsg_KeyHintText` |
| 325 | `CCSUsrMsg_ProcessSpottedEntityUpdate` |
| 327 | `CCSUsrMsg_AdjustMoney` |
| 330 | `CCSUsrMsg_KillCam` |
| 334 | `CCSUsrMsg_MatchEndConditions` |
| 335 | `CCSUsrMsg_DisconnectToLobby` |
| 336 | `CCSUsrMsg_PlayerStatsUpdate` |
| 345 | `CCSUsrMsg_CallVoteFailed` |
| 346 | `CCSUsrMsg_VoteStart` |
| 347 | `CCSUsrMsg_VotePass` |
| 348 | `CCSUsrMsg_VoteFailed` |
| 349 | `CCSUsrMsg_VoteSetup` |
| 350 | `CCSUsrMsg_ServerRankRevealAll` |
| 351 | `CCSUsrMsg_SendLastKillerDamageToClient` |
| 352 | `CCSUsrMsg_ServerRankUpdate` |
| 361 | `CCSUsrMsg_SendPlayerItemDrops` |
| 362 | `CCSUsrMsg_RoundBackupFilenames` |
| 363 | `CCSUsrMsg_SendPlayerItemFound` |
| 364 | `CCSUsrMsg_ReportHit` |
| 365 | `CCSUsrMsg_XpUpdate` |
| 366 | `CCSUsrMsg_QuestProgress` |
| 367 | `CCSUsrMsg_ScoreLeaderboardData` |
| 368 | `CCSUsrMsg_PlayerDecalDigitalSignature` |
| 369 | `CCSUsrMsg_WeaponSound` |
| 370 | `CCSUsrMsg_UpdateScreenHealthBar` |
| 371 | `CCSUsrMsg_EntityOutlineHighlight` |
| 372 | `CCSUsrMsg_SSUI` |
| 373 | `CCSUsrMsg_SurvivalStats` |
| 374 | `CCSUsrMsg_DisconnectToLobby` |
| 375 | `CCSUsrMsg_EndOfMatchAllPlayersData` |
| 376 | `CCSUsrMsg_PostRoundDamageReport` |
| 379 | `CCSUsrMsg_RoundEndReportData` |
| 380 | `CCSUsrMsg_CurrentRoundOdds` |
| 381 | `CCSUsrMsg_DeepStats` |
| 383 | `CCSUsrMsg_ShootInfo` |
| 385 | `CCSUsrMsg_CounterStrafe` |
| 387 | `CCSUsrMsg_RecurringMissionSchema` |
| 388 | `CCSUsrMsg_SendPlayerLoadout` |
| 389 | `CCSUsrMsg_WeaponMagDrop` |

## Demo stream (`.dem`) messages (19)

The command-ID table for demo playback — a flat id space where a single id can bind more than one message type.

| ID | Message type |
|----|--------------|
| 0 | [`CDemoStop`](proto/demo.md) |
| 1 | [`CDemoFileHeader`](proto/demo.md) |
| 2 | [`CDemoFileInfo`](proto/demo.md) |
| 3 | [`CDemoSyncTick`](proto/demo.md) |
| 4 | [`CDemoSendTables`](proto/demo.md) |
| 5 | [`CDemoClassInfo`](proto/demo.md) |
| 6 | [`CDemoStringTables`](proto/demo.md) |
| 7 | [`CDemoPacket`](proto/demo.md) |
| 9 | [`CDemoConsoleCmd`](proto/demo.md) |
| 10 | [`CDemoCustomData`](proto/demo.md) |
| 11 | [`CDemoCustomDataCallbacks`](proto/demo.md) |
| 12 | [`CDemoUserCmd`](proto/demo.md) |
| 13 | [`CDemoFullPacket`](proto/demo.md) |
| 14 | [`CDemoSaveGame`](proto/demo.md) |
| 15 | [`CDemoSpawnGroups`](proto/demo.md) |
| 15 | [`CDemoSpawnGroupsHLTVBroadcast`](proto/demo.md) |
| 16 | [`CDemoAnimationData`](proto/demo.md) |
| 17 | [`CDemoAnimationHeader`](proto/demo.md) |
| 18 | [`CDemoRecovery`](proto/demo.md) |
