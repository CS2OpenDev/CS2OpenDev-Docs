---
layout: default
title: Network Messages
nav_order: 8
---

# Network & Demo Messages

{: .note }
> Source: CS2 build **24662694** · 2026-08-10 · `windows-x86_64` · schema `0.5.1`

The wire-protocol tables: integer message IDs mapped to the protobuf message type carried, recovered from a static RTTI scan of the shipped binaries.  Each type links to its definition on the [protobuf pages](protobufs.md).

## Bidirectional (3)

| ID | Message type |
|----|--------------|
| 16 | [`CBidirMsg_RebroadcastGameEvent`](proto/netmessages.md) |
| 17 | [`CBidirMsg_RebroadcastSource`](proto/netmessages.md) |
| 19 | [`CBidirMsg_PredictionEvent`](proto/netmessages.md) |

## ClcMessages (15)

| ID | Message type |
|----|--------------|
| 20 | [`CCLCMsg_ClientInfo`](proto/netmessages.md) |
| 21 | [`CCLCMsg_Move`](proto/netmessages.md) |
| 22 | [`CCLCMsg_VoiceData`](proto/netmessages.md) |
| 23 | [`CCLCMsg_BaselineAck`](proto/netmessages.md) |
| 25 | [`CCLCMsg_RespondCvarValue`](proto/netmessages.md) |
| 27 | [`CCLCMsg_LoadingProgress`](proto/netmessages.md) |
| 28 | [`CCLCMsg_SplitPlayerConnect`](proto/netmessages.md) |
| 30 | [`CCLCMsg_SplitPlayerDisconnect`](proto/netmessages.md) |
| 31 | [`CCLCMsg_ServerStatus`](proto/netmessages.md) |
| 33 | [`CCLCMsg_RequestPause`](proto/netmessages.md) |
| 34 | [`CCLCMsg_CmdKeyValues`](proto/netmessages.md) |
| 35 | [`CCLCMsg_RconServerDetails`](proto/netmessages.md) |
| 36 | [`CCLCMsg_HltvReplay`](proto/netmessages.md) |
| 37 | [`CCLCMsg_Diagnostic`](proto/netmessages.md) |
| 75 | [`CCLCMsg_HltvFixupOperatorTick`](proto/netmessages.md) |

## ClientMessages (3)

| ID | Message type |
|----|--------------|
| 280 | [`CClientMsg_CustomGameEvent`](proto/clientmessages.md) |
| 281 | [`CClientMsg_CustomGameEventBounce`](proto/clientmessages.md) |
| 282 | [`CClientMsg_ClientUIEvent`](proto/clientmessages.md) |

## Decals (4)

| ID | Message type |
|----|--------------|
| 201 | [`CMsgPlaceDecalEvent`](proto/gameevents.md) |
| 202 | [`CMsgClearWorldDecalsEvent`](proto/gameevents.md) |
| 203 | [`CMsgClearEntityDecalsEvent`](proto/gameevents.md) |
| 204 | [`CMsgClearDecalsForEntityEvent`](proto/gameevents.md) |

## GameEvents (3)

| ID | Message type |
|----|--------------|
| 213 | [`CMsgClothStiffenAnimEvent`](proto/gameevents.md) |
| 214 | [`CMsgClothEffectAnimEvent`](proto/gameevents.md) |
| 453 | [`CMsgPlayerBulletHit`](proto/cs_gameevents.md) |

## NetMessages (12)

| ID | Message type |
|----|--------------|
| 0 | [`CNETMsg_NOP`](proto/networkbasetypes.md) |
| 3 | [`CNETMsg_SplitScreenUser`](proto/networkbasetypes.md) |
| 4 | [`CNETMsg_Tick`](proto/networkbasetypes.md) |
| 5 | [`CNETMsg_StringCmd`](proto/networkbasetypes.md) |
| 6 | [`CNETMsg_SetConVar`](proto/networkbasetypes.md) |
| 7 | [`CNETMsg_SignonState`](proto/networkbasetypes.md) |
| 8 | [`CNETMsg_SpawnGroup_Load`](proto/networkbasetypes.md) |
| 9 | [`CNETMsg_SpawnGroup_ManifestUpdate`](proto/networkbasetypes.md) |
| 11 | [`CNETMsg_SpawnGroup_SetCreationTick`](proto/networkbasetypes.md) |
| 12 | [`CNETMsg_SpawnGroup_Unload`](proto/networkbasetypes.md) |
| 13 | [`CNETMsg_SpawnGroup_LoadCompleted`](proto/networkbasetypes.md) |
| 15 | [`CNETMsg_DebugOverlay`](proto/networkbasetypes.md) |

## PeerToPeer (3)

| ID | Message type |
|----|--------------|
| 256 | [`CP2P_TextMessage`](proto/c_peer2peer_netmessages.md) |
| 257 | [`CP2P_Voice`](proto/c_peer2peer_netmessages.md) |
| 258 | [`CP2P_Ping`](proto/c_peer2peer_netmessages.md) |

## Sounds (5)

| ID | Message type |
|----|--------------|
| 208 | [`CMsgSosStartSoundEvent`](proto/gameevents.md) |
| 209 | [`CMsgSosStopSoundEvent`](proto/gameevents.md) |
| 210 | [`CMsgSosSetSoundEventParams`](proto/gameevents.md) |
| 211 | [`CMsgSosSetLibraryStackFields`](proto/gameevents.md) |
| 212 | [`CMsgSosStopSoundEventHash`](proto/gameevents.md) |

## Source1Legacy (3)

| ID | Message type |
|----|--------------|
| 205 | [`CMsgSource1LegacyGameEventList`](proto/gameevents.md) |
| 206 | [`CMsgSource1LegacyListenEvents`](proto/gameevents.md) |
| 207 | [`CMsgSource1LegacyGameEvent`](proto/gameevents.md) |

## SvcMessages (29)

| ID | Message type |
|----|--------------|
| 40 | [`CSVCMsg_ServerInfo`](proto/netmessages.md) |
| 41 | [`CSVCMsg_FlattenedSerializer`](proto/netmessages.md) |
| 42 | [`CSVCMsg_ClassInfo`](proto/netmessages.md) |
| 43 | [`CSVCMsg_SetPause`](proto/netmessages.md) |
| 44 | [`CSVCMsg_CreateStringTable`](proto/netmessages.md) |
| 45 | [`CSVCMsg_UpdateStringTable`](proto/netmessages.md) |
| 46 | [`CSVCMsg_VoiceInit`](proto/netmessages.md) |
| 47 | [`CSVCMsg_VoiceData`](proto/netmessages.md) |
| 48 | [`CSVCMsg_Print`](proto/netmessages.md) |
| 49 | [`CSVCMsg_Sounds`](proto/netmessages.md) |
| 50 | [`CSVCMsg_SetView`](proto/netmessages.md) |
| 51 | [`CSVCMsg_ClearAllStringTables`](proto/netmessages.md) |
| 52 | [`CSVCMsg_CmdKeyValues`](proto/netmessages.md) |
| 54 | [`CSVCMsg_SplitScreen`](proto/netmessages.md) |
| 55 | [`CSVCMsg_PacketEntities`](proto/netmessages.md) |
| 56 | [`CSVCMsg_Prefetch`](proto/netmessages.md) |
| 57 | [`CSVCMsg_Menu`](proto/netmessages.md) |
| 58 | [`CSVCMsg_GetCvarValue`](proto/netmessages.md) |
| 59 | [`CSVCMsg_StopSound`](proto/netmessages.md) |
| 60 | [`CSVCMsg_PeerList`](proto/netmessages.md) |
| 61 | [`CSVCMsg_PacketReliable`](proto/netmessages.md) |
| 62 | [`CSVCMsg_HLTVStatus`](proto/netmessages.md) |
| 63 | [`CSVCMsg_ServerSteamID`](proto/netmessages.md) |
| 70 | [`CSVCMsg_FullFrameSplit`](proto/netmessages.md) |
| 71 | [`CSVCMsg_RconServerDetails`](proto/netmessages.md) |
| 72 | [`CSVCMsg_UserMessage`](proto/netmessages.md) |
| 74 | [`CSVCMsg_HltvReplay`](proto/netmessages.md) |
| 76 | [`CSVCMsg_UserCommands`](proto/netmessages.md) |
| 77 | [`CSVCMsg_NextMsgPredicted`](proto/netmessages.md) |

## TempEntities (23)

| ID | Message type |
|----|--------------|
| 400 | [`CMsgTEEffectDispatch`](proto/te.md) |
| 401 | [`CMsgTEArmorRicochet`](proto/te.md) |
| 402 | [`CMsgTEBeamEntPoint`](proto/te.md) |
| 403 | [`CMsgTEBeamEnts`](proto/te.md) |
| 404 | [`CMsgTEBeamPoints`](proto/te.md) |
| 405 | [`CMsgTEBeamRing`](proto/te.md) |
| 408 | [`CMsgTEBubbles`](proto/te.md) |
| 409 | [`CMsgTEBubbleTrail`](proto/te.md) |
| 410 | [`CMsgTEDecal`](proto/te.md) |
| 411 | [`CMsgTEWorldDecal`](proto/te.md) |
| 412 | [`CMsgTEEnergySplash`](proto/te.md) |
| 413 | [`CMsgTEFizz`](proto/te.md) |
| 415 | [`CMsgTEGlowSprite`](proto/te.md) |
| 416 | [`CMsgTEImpact`](proto/te.md) |
| 417 | [`CMsgTEMuzzleFlash`](proto/te.md) |
| 418 | [`CMsgTEBloodStream`](proto/te.md) |
| 419 | [`CMsgTEExplosion`](proto/te.md) |
| 420 | [`CMsgTEDust`](proto/te.md) |
| 421 | [`CMsgTELargeFunnel`](proto/te.md) |
| 422 | [`CMsgTESparks`](proto/te.md) |
| 423 | [`CMsgTEPhysicsProp`](proto/te.md) |
| 426 | [`CMsgTESmoke`](proto/te.md) |
| 452 | [`CMsgTEFireBullets`](proto/cs_gameevents.md) |

## UserMessages (89)

| ID | Message type |
|----|--------------|
| 101 | [`CUserMessageAchievementEvent`](proto/usermessages.md) |
| 104 | [`CUserMessageCurrentTimescale`](proto/usermessages.md) |
| 105 | [`CUserMessageDesiredTimescale`](proto/usermessages.md) |
| 106 | [`CUserMessageFade`](proto/usermessages.md) |
| 110 | [`CUserMessageHudMsg`](proto/usermessages.md) |
| 111 | [`CUserMessageHudText`](proto/usermessages.md) |
| 113 | [`CUserMessageColoredText`](proto/usermessages.md) |
| 114 | [`CUserMessageRequestState`](proto/usermessages.md) |
| 115 | [`CUserMessageResetHUD`](proto/usermessages.md) |
| 116 | [`CUserMessageRumble`](proto/usermessages.md) |
| 117 | [`CUserMessageSayText`](proto/usermessages.md) |
| 118 | [`CUserMessageSayText2`](proto/usermessages.md) |
| 119 | [`CUserMessageSayTextChannel`](proto/usermessages.md) |
| 120 | [`CUserMessageShake`](proto/usermessages.md) |
| 121 | [`CUserMessageShakeDir`](proto/usermessages.md) |
| 122 | [`CUserMessageWaterShake`](proto/usermessages.md) |
| 124 | [`CUserMessageTextMsg`](proto/usermessages.md) |
| 125 | [`CUserMessageScreenTilt`](proto/usermessages.md) |
| 128 | [`CUserMessageVoiceMask`](proto/usermessages.md) |
| 130 | [`CUserMessageSendAudio`](proto/usermessages.md) |
| 131 | [`CUserMessageItemPickup`](proto/usermessages.md) |
| 132 | [`CUserMessageAmmoDenied`](proto/usermessages.md) |
| 134 | [`CUserMessageShowMenu`](proto/usermessages.md) |
| 135 | [`CUserMessageCreditsMsg`](proto/usermessages.md) |
| 137 | [`CEntityMessageScreenOverlay`](proto/usermessages.md) |
| 139 | [`CEntityMessagePropagateForce`](proto/usermessages.md) |
| 140 | [`CEntityMessageDoSpark`](proto/usermessages.md) |
| 142 | [`CUserMessageCloseCaptionPlaceholder`](proto/usermessages.md) |
| 143 | [`CUserMessageCameraTransition`](proto/usermessages.md) |
| 144 | [`CUserMessageAudioParameter`](proto/usermessages.md) |
| 145 | [`CUserMsg_ParticleManager`](proto/usermessages.md) |
| 146 | [`CUserMsg_HudError`](proto/usermessages.md) |
| 148 | [`CUserMsg_CustomGameEvent`](proto/usermessages.md) |
| 150 | [`CUserMessageHapticsManagerPulse`](proto/usermessages.md) |
| 151 | [`CUserMessageHapticsManagerEffect`](proto/usermessages.md) |
| 153 | [`CUserMessageUpdateCssClasses`](proto/usermessages.md) |
| 154 | [`CUserMessageServerFrameTime`](proto/usermessages.md) |
| 155 | [`CUserMessageLagCompensationError`](proto/usermessages.md) |
| 156 | [`CUserMessageRequestDllStatus`](proto/usermessages.md) |
| 157 | [`CUserMessageRequestUtilAction`](proto/usermessages.md) |
| 160 | [`CUserMessageRequestInventory`](proto/usermessages.md) |
| 162 | [`CUserMessageRequestDiagnostic`](proto/usermessages.md) |
| 165 | [`CUserMessage_NotifyResponseFound`](proto/usermessages.md) |
| 166 | [`CUserMessage_PlayResponseConditional`](proto/usermessages.md) |
| 301 | [`CCSUsrMsg_VGUIMenu`](proto/cstrike15_usermessages.md) |
| 317 | [`CCSUsrMsg_SendAudio`](proto/cstrike15_usermessages.md) |
| 318 | [`CCSUsrMsg_RawAudio`](proto/cstrike15_usermessages.md) |
| 321 | [`CCSUsrMsg_Damage`](proto/cstrike15_usermessages.md) |
| 322 | [`CCSUsrMsg_RadioText`](proto/cstrike15_usermessages.md) |
| 323 | [`CCSUsrMsg_HintText`](proto/cstrike15_usermessages.md) |
| 324 | [`CCSUsrMsg_KeyHintText`](proto/cstrike15_usermessages.md) |
| 325 | [`CCSUsrMsg_ProcessSpottedEntityUpdate`](proto/cstrike15_usermessages.md) |
| 327 | [`CCSUsrMsg_AdjustMoney`](proto/cstrike15_usermessages.md) |
| 330 | [`CCSUsrMsg_KillCam`](proto/cstrike15_usermessages.md) |
| 334 | [`CCSUsrMsg_MatchEndConditions`](proto/cstrike15_usermessages.md) |
| 335 | [`CCSUsrMsg_DisconnectToLobby`](proto/cstrike15_usermessages.md) |
| 336 | [`CCSUsrMsg_PlayerStatsUpdate`](proto/cstrike15_usermessages.md) |
| 345 | [`CCSUsrMsg_CallVoteFailed`](proto/cstrike15_usermessages.md) |
| 346 | [`CCSUsrMsg_VoteStart`](proto/cstrike15_usermessages.md) |
| 347 | [`CCSUsrMsg_VotePass`](proto/cstrike15_usermessages.md) |
| 348 | [`CCSUsrMsg_VoteFailed`](proto/cstrike15_usermessages.md) |
| 349 | [`CCSUsrMsg_VoteSetup`](proto/cstrike15_usermessages.md) |
| 350 | [`CCSUsrMsg_ServerRankRevealAll`](proto/cstrike15_usermessages.md) |
| 351 | [`CCSUsrMsg_SendLastKillerDamageToClient`](proto/cstrike15_usermessages.md) |
| 352 | [`CCSUsrMsg_ServerRankUpdate`](proto/cstrike15_usermessages.md) |
| 361 | [`CCSUsrMsg_SendPlayerItemDrops`](proto/cstrike15_usermessages.md) |
| 362 | [`CCSUsrMsg_RoundBackupFilenames`](proto/cstrike15_usermessages.md) |
| 363 | [`CCSUsrMsg_SendPlayerItemFound`](proto/cstrike15_usermessages.md) |
| 364 | [`CCSUsrMsg_ReportHit`](proto/cstrike15_usermessages.md) |
| 365 | [`CCSUsrMsg_XpUpdate`](proto/cstrike15_usermessages.md) |
| 366 | [`CCSUsrMsg_QuestProgress`](proto/cstrike15_usermessages.md) |
| 367 | [`CCSUsrMsg_ScoreLeaderboardData`](proto/cstrike15_usermessages.md) |
| 368 | [`CCSUsrMsg_PlayerDecalDigitalSignature`](proto/cstrike15_usermessages.md) |
| 369 | [`CCSUsrMsg_WeaponSound`](proto/cstrike15_usermessages.md) |
| 370 | [`CCSUsrMsg_UpdateScreenHealthBar`](proto/cstrike15_usermessages.md) |
| 371 | [`CCSUsrMsg_EntityOutlineHighlight`](proto/cstrike15_usermessages.md) |
| 372 | [`CCSUsrMsg_SSUI`](proto/cstrike15_usermessages.md) |
| 373 | [`CCSUsrMsg_SurvivalStats`](proto/cstrike15_usermessages.md) |
| 374 | [`CCSUsrMsg_DisconnectToLobby`](proto/cstrike15_usermessages.md) |
| 375 | [`CCSUsrMsg_EndOfMatchAllPlayersData`](proto/cstrike15_usermessages.md) |
| 376 | [`CCSUsrMsg_PostRoundDamageReport`](proto/cstrike15_usermessages.md) |
| 379 | [`CCSUsrMsg_RoundEndReportData`](proto/cstrike15_usermessages.md) |
| 380 | [`CCSUsrMsg_CurrentRoundOdds`](proto/cstrike15_usermessages.md) |
| 381 | [`CCSUsrMsg_DeepStats`](proto/cstrike15_usermessages.md) |
| 383 | [`CCSUsrMsg_ShootInfo`](proto/cstrike15_usermessages.md) |
| 385 | [`CCSUsrMsg_CounterStrafe`](proto/cstrike15_usermessages.md) |
| 387 | [`CCSUsrMsg_RecurringMissionSchema`](proto/cstrike15_usermessages.md) |
| 388 | [`CCSUsrMsg_SendPlayerLoadout`](proto/cstrike15_usermessages.md) |
| 389 | [`CCSUsrMsg_WeaponMagDrop`](proto/cstrike15_usermessages.md) |

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
