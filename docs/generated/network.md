---
layout: default
title: Network Messages
nav_order: 8
---

# Network & Demo Messages

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

The wire-protocol tables: integer message IDs mapped to the protobuf message type carried, recovered from a static RTTI scan of the shipped binaries.  Each type links to its definition on the [protobuf pages](protobufs.md).

## Bidirectional

3 message ids.

| ID | Message type |
|----|--------------|
| 16 | [`CBidirMsg_RebroadcastGameEvent`](proto/netmessages.md#cbidirmsg_rebroadcastgameevent) |
| 17 | [`CBidirMsg_RebroadcastSource`](proto/netmessages.md#cbidirmsg_rebroadcastsource) |
| 19 | [`CBidirMsg_PredictionEvent`](proto/netmessages.md#cbidirmsg_predictionevent) |

## ClcMessages

15 message ids.

| ID | Message type |
|----|--------------|
| 20 | [`CCLCMsg_ClientInfo`](proto/netmessages.md#cclcmsg_clientinfo) |
| 21 | [`CCLCMsg_Move`](proto/netmessages.md#cclcmsg_move) |
| 22 | [`CCLCMsg_VoiceData`](proto/netmessages.md#cclcmsg_voicedata) |
| 23 | [`CCLCMsg_BaselineAck`](proto/netmessages.md#cclcmsg_baselineack) |
| 25 | [`CCLCMsg_RespondCvarValue`](proto/netmessages.md#cclcmsg_respondcvarvalue) |
| 27 | [`CCLCMsg_LoadingProgress`](proto/netmessages.md#cclcmsg_loadingprogress) |
| 28 | [`CCLCMsg_SplitPlayerConnect`](proto/netmessages.md#cclcmsg_splitplayerconnect) |
| 30 | [`CCLCMsg_SplitPlayerDisconnect`](proto/netmessages.md#cclcmsg_splitplayerdisconnect) |
| 31 | [`CCLCMsg_ServerStatus`](proto/netmessages.md#cclcmsg_serverstatus) |
| 33 | [`CCLCMsg_RequestPause`](proto/netmessages.md#cclcmsg_requestpause) |
| 34 | [`CCLCMsg_CmdKeyValues`](proto/netmessages.md#cclcmsg_cmdkeyvalues) |
| 35 | [`CCLCMsg_RconServerDetails`](proto/netmessages.md#cclcmsg_rconserverdetails) |
| 36 | [`CCLCMsg_HltvReplay`](proto/netmessages.md#cclcmsg_hltvreplay) |
| 37 | [`CCLCMsg_Diagnostic`](proto/netmessages.md#cclcmsg_diagnostic) |
| 75 | [`CCLCMsg_HltvFixupOperatorTick`](proto/netmessages.md#cclcmsg_hltvfixupoperatortick) |

## ClientMessages

3 message ids.

| ID | Message type |
|----|--------------|
| 280 | [`CClientMsg_CustomGameEvent`](proto/clientmessages.md#cclientmsg_customgameevent) |
| 281 | [`CClientMsg_CustomGameEventBounce`](proto/clientmessages.md#cclientmsg_customgameeventbounce) |
| 282 | [`CClientMsg_ClientUIEvent`](proto/clientmessages.md#cclientmsg_clientuievent) |

## Decals

4 message ids.

| ID | Message type |
|----|--------------|
| 201 | [`CMsgPlaceDecalEvent`](proto/gameevents.md#cmsgplacedecalevent) |
| 202 | [`CMsgClearWorldDecalsEvent`](proto/gameevents.md#cmsgclearworlddecalsevent) |
| 203 | [`CMsgClearEntityDecalsEvent`](proto/gameevents.md#cmsgclearentitydecalsevent) |
| 204 | [`CMsgClearDecalsForEntityEvent`](proto/gameevents.md#cmsgcleardecalsforentityevent) |

## GameEvents

3 message ids.

| ID | Message type |
|----|--------------|
| 213 | [`CMsgClothStiffenAnimEvent`](proto/gameevents.md#cmsgclothstiffenanimevent) |
| 214 | [`CMsgClothEffectAnimEvent`](proto/gameevents.md#cmsgclotheffectanimevent) |
| 453 | [`CMsgPlayerBulletHit`](proto/cs_gameevents.md#cmsgplayerbullethit) |

## NetMessages

12 message ids.

| ID | Message type |
|----|--------------|
| 0 | [`CNETMsg_NOP`](proto/networkbasetypes.md#cnetmsg_nop) |
| 3 | [`CNETMsg_SplitScreenUser`](proto/networkbasetypes.md#cnetmsg_splitscreenuser) |
| 4 | [`CNETMsg_Tick`](proto/networkbasetypes.md#cnetmsg_tick) |
| 5 | [`CNETMsg_StringCmd`](proto/networkbasetypes.md#cnetmsg_stringcmd) |
| 6 | [`CNETMsg_SetConVar`](proto/networkbasetypes.md#cnetmsg_setconvar) |
| 7 | [`CNETMsg_SignonState`](proto/networkbasetypes.md#cnetmsg_signonstate) |
| 8 | [`CNETMsg_SpawnGroup_Load`](proto/networkbasetypes.md#cnetmsg_spawngroup_load) |
| 9 | [`CNETMsg_SpawnGroup_ManifestUpdate`](proto/networkbasetypes.md#cnetmsg_spawngroup_manifestupdate) |
| 11 | [`CNETMsg_SpawnGroup_SetCreationTick`](proto/networkbasetypes.md#cnetmsg_spawngroup_setcreationtick) |
| 12 | [`CNETMsg_SpawnGroup_Unload`](proto/networkbasetypes.md#cnetmsg_spawngroup_unload) |
| 13 | [`CNETMsg_SpawnGroup_LoadCompleted`](proto/networkbasetypes.md#cnetmsg_spawngroup_loadcompleted) |
| 15 | [`CNETMsg_DebugOverlay`](proto/networkbasetypes.md#cnetmsg_debugoverlay) |

## PeerToPeer

3 message ids.

| ID | Message type |
|----|--------------|
| 256 | [`CP2P_TextMessage`](proto/c_peer2peer_netmessages.md#cp2p_textmessage) |
| 257 | [`CP2P_Voice`](proto/c_peer2peer_netmessages.md#cp2p_voice) |
| 258 | [`CP2P_Ping`](proto/c_peer2peer_netmessages.md#cp2p_ping) |

## Sounds

5 message ids.

| ID | Message type |
|----|--------------|
| 208 | [`CMsgSosStartSoundEvent`](proto/gameevents.md#cmsgsosstartsoundevent) |
| 209 | [`CMsgSosStopSoundEvent`](proto/gameevents.md#cmsgsosstopsoundevent) |
| 210 | [`CMsgSosSetSoundEventParams`](proto/gameevents.md#cmsgsossetsoundeventparams) |
| 211 | [`CMsgSosSetLibraryStackFields`](proto/gameevents.md#cmsgsossetlibrarystackfields) |
| 212 | [`CMsgSosStopSoundEventHash`](proto/gameevents.md#cmsgsosstopsoundeventhash) |

## Source1Legacy

3 message ids.

| ID | Message type |
|----|--------------|
| 205 | [`CMsgSource1LegacyGameEventList`](proto/gameevents.md#cmsgsource1legacygameeventlist) |
| 206 | [`CMsgSource1LegacyListenEvents`](proto/gameevents.md#cmsgsource1legacylistenevents) |
| 207 | [`CMsgSource1LegacyGameEvent`](proto/gameevents.md#cmsgsource1legacygameevent) |

## SvcMessages

29 message ids.

| ID | Message type |
|----|--------------|
| 40 | [`CSVCMsg_ServerInfo`](proto/netmessages.md#csvcmsg_serverinfo) |
| 41 | [`CSVCMsg_FlattenedSerializer`](proto/netmessages.md#csvcmsg_flattenedserializer) |
| 42 | [`CSVCMsg_ClassInfo`](proto/netmessages.md#csvcmsg_classinfo) |
| 43 | [`CSVCMsg_SetPause`](proto/netmessages.md#csvcmsg_setpause) |
| 44 | [`CSVCMsg_CreateStringTable`](proto/netmessages.md#csvcmsg_createstringtable) |
| 45 | [`CSVCMsg_UpdateStringTable`](proto/netmessages.md#csvcmsg_updatestringtable) |
| 46 | [`CSVCMsg_VoiceInit`](proto/netmessages.md#csvcmsg_voiceinit) |
| 47 | [`CSVCMsg_VoiceData`](proto/netmessages.md#csvcmsg_voicedata) |
| 48 | [`CSVCMsg_Print`](proto/netmessages.md#csvcmsg_print) |
| 49 | [`CSVCMsg_Sounds`](proto/netmessages.md#csvcmsg_sounds) |
| 50 | [`CSVCMsg_SetView`](proto/netmessages.md#csvcmsg_setview) |
| 51 | [`CSVCMsg_ClearAllStringTables`](proto/netmessages.md#csvcmsg_clearallstringtables) |
| 52 | [`CSVCMsg_CmdKeyValues`](proto/netmessages.md#csvcmsg_cmdkeyvalues) |
| 54 | [`CSVCMsg_SplitScreen`](proto/netmessages.md#csvcmsg_splitscreen) |
| 55 | [`CSVCMsg_PacketEntities`](proto/netmessages.md#csvcmsg_packetentities) |
| 56 | [`CSVCMsg_Prefetch`](proto/netmessages.md#csvcmsg_prefetch) |
| 57 | [`CSVCMsg_Menu`](proto/netmessages.md#csvcmsg_menu) |
| 58 | [`CSVCMsg_GetCvarValue`](proto/netmessages.md#csvcmsg_getcvarvalue) |
| 59 | [`CSVCMsg_StopSound`](proto/netmessages.md#csvcmsg_stopsound) |
| 60 | [`CSVCMsg_PeerList`](proto/netmessages.md#csvcmsg_peerlist) |
| 61 | [`CSVCMsg_PacketReliable`](proto/netmessages.md#csvcmsg_packetreliable) |
| 62 | [`CSVCMsg_HLTVStatus`](proto/netmessages.md#csvcmsg_hltvstatus) |
| 63 | [`CSVCMsg_ServerSteamID`](proto/netmessages.md#csvcmsg_serversteamid) |
| 70 | [`CSVCMsg_FullFrameSplit`](proto/netmessages.md#csvcmsg_fullframesplit) |
| 71 | [`CSVCMsg_RconServerDetails`](proto/netmessages.md#csvcmsg_rconserverdetails) |
| 72 | [`CSVCMsg_UserMessage`](proto/netmessages.md#csvcmsg_usermessage) |
| 74 | [`CSVCMsg_HltvReplay`](proto/netmessages.md#csvcmsg_hltvreplay) |
| 76 | [`CSVCMsg_UserCommands`](proto/netmessages.md#csvcmsg_usercommands) |
| 77 | [`CSVCMsg_NextMsgPredicted`](proto/netmessages.md#csvcmsg_nextmsgpredicted) |

## TempEntities

23 message ids.

| ID | Message type |
|----|--------------|
| 400 | [`CMsgTEEffectDispatch`](proto/te.md#cmsgteeffectdispatch) |
| 401 | [`CMsgTEArmorRicochet`](proto/te.md#cmsgtearmorricochet) |
| 402 | [`CMsgTEBeamEntPoint`](proto/te.md#cmsgtebeamentpoint) |
| 403 | [`CMsgTEBeamEnts`](proto/te.md#cmsgtebeaments) |
| 404 | [`CMsgTEBeamPoints`](proto/te.md#cmsgtebeampoints) |
| 405 | [`CMsgTEBeamRing`](proto/te.md#cmsgtebeamring) |
| 408 | [`CMsgTEBubbles`](proto/te.md#cmsgtebubbles) |
| 409 | [`CMsgTEBubbleTrail`](proto/te.md#cmsgtebubbletrail) |
| 410 | [`CMsgTEDecal`](proto/te.md#cmsgtedecal) |
| 411 | [`CMsgTEWorldDecal`](proto/te.md#cmsgteworlddecal) |
| 412 | [`CMsgTEEnergySplash`](proto/te.md#cmsgteenergysplash) |
| 413 | [`CMsgTEFizz`](proto/te.md#cmsgtefizz) |
| 415 | [`CMsgTEGlowSprite`](proto/te.md#cmsgteglowsprite) |
| 416 | [`CMsgTEImpact`](proto/te.md#cmsgteimpact) |
| 417 | [`CMsgTEMuzzleFlash`](proto/te.md#cmsgtemuzzleflash) |
| 418 | [`CMsgTEBloodStream`](proto/te.md#cmsgtebloodstream) |
| 419 | [`CMsgTEExplosion`](proto/te.md#cmsgteexplosion) |
| 420 | [`CMsgTEDust`](proto/te.md#cmsgtedust) |
| 421 | [`CMsgTELargeFunnel`](proto/te.md#cmsgtelargefunnel) |
| 422 | [`CMsgTESparks`](proto/te.md#cmsgtesparks) |
| 423 | [`CMsgTEPhysicsProp`](proto/te.md#cmsgtephysicsprop) |
| 426 | [`CMsgTESmoke`](proto/te.md#cmsgtesmoke) |
| 452 | [`CMsgTEFireBullets`](proto/cs_gameevents.md#cmsgtefirebullets) |

## UserMessages

90 message ids.

| ID | Message type |
|----|--------------|
| 101 | [`CUserMessageAchievementEvent`](proto/usermessages.md#cusermessageachievementevent) |
| 104 | [`CUserMessageCurrentTimescale`](proto/usermessages.md#cusermessagecurrenttimescale) |
| 105 | [`CUserMessageDesiredTimescale`](proto/usermessages.md#cusermessagedesiredtimescale) |
| 106 | [`CUserMessageFade`](proto/usermessages.md#cusermessagefade) |
| 110 | [`CUserMessageHudMsg`](proto/usermessages.md#cusermessagehudmsg) |
| 111 | [`CUserMessageHudText`](proto/usermessages.md#cusermessagehudtext) |
| 113 | [`CUserMessageColoredText`](proto/usermessages.md#cusermessagecoloredtext) |
| 114 | [`CUserMessageRequestState`](proto/usermessages.md#cusermessagerequeststate) |
| 115 | [`CUserMessageResetHUD`](proto/usermessages.md#cusermessageresethud) |
| 116 | [`CUserMessageRumble`](proto/usermessages.md#cusermessagerumble) |
| 117 | [`CUserMessageSayText`](proto/usermessages.md#cusermessagesaytext) |
| 118 | [`CUserMessageSayText2`](proto/usermessages.md#cusermessagesaytext2) |
| 119 | [`CUserMessageSayTextChannel`](proto/usermessages.md#cusermessagesaytextchannel) |
| 120 | [`CUserMessageShake`](proto/usermessages.md#cusermessageshake) |
| 121 | [`CUserMessageShakeDir`](proto/usermessages.md#cusermessageshakedir) |
| 122 | [`CUserMessageWaterShake`](proto/usermessages.md#cusermessagewatershake) |
| 124 | [`CUserMessageTextMsg`](proto/usermessages.md#cusermessagetextmsg) |
| 125 | [`CUserMessageScreenTilt`](proto/usermessages.md#cusermessagescreentilt) |
| 128 | [`CUserMessageVoiceMask`](proto/usermessages.md#cusermessagevoicemask) |
| 130 | [`CUserMessageSendAudio`](proto/usermessages.md#cusermessagesendaudio) |
| 131 | [`CUserMessageItemPickup`](proto/usermessages.md#cusermessageitempickup) |
| 132 | [`CUserMessageAmmoDenied`](proto/usermessages.md#cusermessageammodenied) |
| 134 | [`CUserMessageShowMenu`](proto/usermessages.md#cusermessageshowmenu) |
| 135 | [`CUserMessageCreditsMsg`](proto/usermessages.md#cusermessagecreditsmsg) |
| 137 | [`CEntityMessageScreenOverlay`](proto/usermessages.md#centitymessagescreenoverlay) |
| 139 | [`CEntityMessagePropagateForce`](proto/usermessages.md#centitymessagepropagateforce) |
| 140 | [`CEntityMessageDoSpark`](proto/usermessages.md#centitymessagedospark) |
| 142 | [`CUserMessageCloseCaptionPlaceholder`](proto/usermessages.md#cusermessageclosecaptionplaceholder) |
| 143 | [`CUserMessageCameraTransition`](proto/usermessages.md#cusermessagecameratransition) |
| 144 | [`CUserMessageAudioParameter`](proto/usermessages.md#cusermessageaudioparameter) |
| 145 | [`CUserMsg_ParticleManager`](proto/usermessages.md#cusermsg_particlemanager) |
| 146 | [`CUserMsg_HudError`](proto/usermessages.md#cusermsg_huderror) |
| 148 | [`CUserMsg_CustomGameEvent`](proto/usermessages.md#cusermsg_customgameevent) |
| 150 | [`CUserMessageHapticsManagerPulse`](proto/usermessages.md#cusermessagehapticsmanagerpulse) |
| 151 | [`CUserMessageHapticsManagerEffect`](proto/usermessages.md#cusermessagehapticsmanagereffect) |
| 153 | [`CUserMessageUpdateCssClasses`](proto/usermessages.md#cusermessageupdatecssclasses) |
| 154 | [`CUserMessageServerFrameTime`](proto/usermessages.md#cusermessageserverframetime) |
| 155 | [`CUserMessageLagCompensationError`](proto/usermessages.md#cusermessagelagcompensationerror) |
| 156 | [`CUserMessageRequestDllStatus`](proto/usermessages.md#cusermessagerequestdllstatus) |
| 157 | [`CUserMessageRequestUtilAction`](proto/usermessages.md#cusermessagerequestutilaction) |
| 160 | [`CUserMessageRequestInventory`](proto/usermessages.md#cusermessagerequestinventory) |
| 162 | [`CUserMessageRequestDiagnostic`](proto/usermessages.md#cusermessagerequestdiagnostic) |
| 165 | [`CUserMessage_NotifyResponseFound`](proto/usermessages.md#cusermessage_notifyresponsefound) |
| 166 | [`CUserMessage_PlayResponseConditional`](proto/usermessages.md#cusermessage_playresponseconditional) |
| 301 | [`CCSUsrMsg_VGUIMenu`](proto/cstrike15_usermessages.md#ccsusrmsg_vguimenu) |
| 317 | [`CCSUsrMsg_SendAudio`](proto/cstrike15_usermessages.md#ccsusrmsg_sendaudio) |
| 318 | [`CCSUsrMsg_RawAudio`](proto/cstrike15_usermessages.md#ccsusrmsg_rawaudio) |
| 321 | [`CCSUsrMsg_Damage`](proto/cstrike15_usermessages.md#ccsusrmsg_damage) |
| 322 | [`CCSUsrMsg_RadioText`](proto/cstrike15_usermessages.md#ccsusrmsg_radiotext) |
| 323 | [`CCSUsrMsg_HintText`](proto/cstrike15_usermessages.md#ccsusrmsg_hinttext) |
| 324 | [`CCSUsrMsg_KeyHintText`](proto/cstrike15_usermessages.md#ccsusrmsg_keyhinttext) |
| 325 | [`CCSUsrMsg_ProcessSpottedEntityUpdate`](proto/cstrike15_usermessages.md#ccsusrmsg_processspottedentityupdate) |
| 327 | [`CCSUsrMsg_AdjustMoney`](proto/cstrike15_usermessages.md#ccsusrmsg_adjustmoney) |
| 330 | [`CCSUsrMsg_KillCam`](proto/cstrike15_usermessages.md#ccsusrmsg_killcam) |
| 334 | [`CCSUsrMsg_MatchEndConditions`](proto/cstrike15_usermessages.md#ccsusrmsg_matchendconditions) |
| 335 | [`CCSUsrMsg_DisconnectToLobby`](proto/cstrike15_usermessages.md#ccsusrmsg_disconnecttolobby) |
| 336 | [`CCSUsrMsg_PlayerStatsUpdate`](proto/cstrike15_usermessages.md#ccsusrmsg_playerstatsupdate) |
| 345 | [`CCSUsrMsg_CallVoteFailed`](proto/cstrike15_usermessages.md#ccsusrmsg_callvotefailed) |
| 346 | [`CCSUsrMsg_VoteStart`](proto/cstrike15_usermessages.md#ccsusrmsg_votestart) |
| 347 | [`CCSUsrMsg_VotePass`](proto/cstrike15_usermessages.md#ccsusrmsg_votepass) |
| 348 | [`CCSUsrMsg_VoteFailed`](proto/cstrike15_usermessages.md#ccsusrmsg_votefailed) |
| 349 | [`CCSUsrMsg_VoteSetup`](proto/cstrike15_usermessages.md#ccsusrmsg_votesetup) |
| 350 | [`CCSUsrMsg_ServerRankRevealAll`](proto/cstrike15_usermessages.md#ccsusrmsg_serverrankrevealall) |
| 351 | [`CCSUsrMsg_SendLastKillerDamageToClient`](proto/cstrike15_usermessages.md#ccsusrmsg_sendlastkillerdamagetoclient) |
| 352 | [`CCSUsrMsg_ServerRankUpdate`](proto/cstrike15_usermessages.md#ccsusrmsg_serverrankupdate) |
| 361 | [`CCSUsrMsg_SendPlayerItemDrops`](proto/cstrike15_usermessages.md#ccsusrmsg_sendplayeritemdrops) |
| 362 | [`CCSUsrMsg_RoundBackupFilenames`](proto/cstrike15_usermessages.md#ccsusrmsg_roundbackupfilenames) |
| 363 | [`CCSUsrMsg_SendPlayerItemFound`](proto/cstrike15_usermessages.md#ccsusrmsg_sendplayeritemfound) |
| 364 | [`CCSUsrMsg_ReportHit`](proto/cstrike15_usermessages.md#ccsusrmsg_reporthit) |
| 365 | [`CCSUsrMsg_XpUpdate`](proto/cstrike15_usermessages.md#ccsusrmsg_xpupdate) |
| 366 | [`CCSUsrMsg_QuestProgress`](proto/cstrike15_usermessages.md#ccsusrmsg_questprogress) |
| 367 | [`CCSUsrMsg_ScoreLeaderboardData`](proto/cstrike15_usermessages.md#ccsusrmsg_scoreleaderboarddata) |
| 368 | [`CCSUsrMsg_PlayerDecalDigitalSignature`](proto/cstrike15_usermessages.md#ccsusrmsg_playerdecaldigitalsignature) |
| 369 | [`CCSUsrMsg_WeaponSound`](proto/cstrike15_usermessages.md#ccsusrmsg_weaponsound) |
| 370 | [`CCSUsrMsg_UpdateScreenHealthBar`](proto/cstrike15_usermessages.md#ccsusrmsg_updatescreenhealthbar) |
| 371 | [`CCSUsrMsg_EntityOutlineHighlight`](proto/cstrike15_usermessages.md#ccsusrmsg_entityoutlinehighlight) |
| 372 | [`CCSUsrMsg_SSUI`](proto/cstrike15_usermessages.md#ccsusrmsg_ssui) |
| 373 | [`CCSUsrMsg_SurvivalStats`](proto/cstrike15_usermessages.md#ccsusrmsg_survivalstats) |
| 374 | [`CCSUsrMsg_DisconnectToLobby`](proto/cstrike15_usermessages.md#ccsusrmsg_disconnecttolobby) |
| 375 | [`CCSUsrMsg_EndOfMatchAllPlayersData`](proto/cstrike15_usermessages.md#ccsusrmsg_endofmatchallplayersdata) |
| 376 | [`CCSUsrMsg_PostRoundDamageReport`](proto/cstrike15_usermessages.md#ccsusrmsg_postrounddamagereport) |
| 379 | [`CCSUsrMsg_RoundEndReportData`](proto/cstrike15_usermessages.md#ccsusrmsg_roundendreportdata) |
| 380 | [`CCSUsrMsg_CurrentRoundOdds`](proto/cstrike15_usermessages.md#ccsusrmsg_currentroundodds) |
| 381 | [`CCSUsrMsg_DeepStats`](proto/cstrike15_usermessages.md#ccsusrmsg_deepstats) |
| 383 | [`CCSUsrMsg_ShootInfo`](proto/cstrike15_usermessages.md#ccsusrmsg_shootinfo) |
| 385 | [`CCSUsrMsg_CounterStrafe`](proto/cstrike15_usermessages.md#ccsusrmsg_counterstrafe) |
| 387 | [`CCSUsrMsg_RecurringMissionSchema`](proto/cstrike15_usermessages.md#ccsusrmsg_recurringmissionschema) |
| 388 | [`CCSUsrMsg_SendPlayerLoadout`](proto/cstrike15_usermessages.md#ccsusrmsg_sendplayerloadout) |
| 389 | [`CCSUsrMsg_WeaponMagDrop`](proto/cstrike15_usermessages.md#ccsusrmsg_weaponmagdrop) |
| 390 | `CCSUsrMsg_CustomHudClicked` |

## Demo stream messages

19 command ids in the `.dem` stream.

The command-ID table for demo playback — a flat id space where a single id can bind more than one message type.

| ID | Message type |
|----|--------------|
| 0 | [`CDemoStop`](proto/demo.md#cdemostop) |
| 1 | [`CDemoFileHeader`](proto/demo.md#cdemofileheader) |
| 2 | [`CDemoFileInfo`](proto/demo.md#cdemofileinfo) |
| 3 | [`CDemoSyncTick`](proto/demo.md#cdemosynctick) |
| 4 | [`CDemoSendTables`](proto/demo.md#cdemosendtables) |
| 5 | [`CDemoClassInfo`](proto/demo.md#cdemoclassinfo) |
| 6 | [`CDemoStringTables`](proto/demo.md#cdemostringtables) |
| 7 | [`CDemoPacket`](proto/demo.md#cdemopacket) |
| 9 | [`CDemoConsoleCmd`](proto/demo.md#cdemoconsolecmd) |
| 10 | [`CDemoCustomData`](proto/demo.md#cdemocustomdata) |
| 11 | [`CDemoCustomDataCallbacks`](proto/demo.md#cdemocustomdatacallbacks) |
| 12 | [`CDemoUserCmd`](proto/demo.md#cdemousercmd) |
| 13 | [`CDemoFullPacket`](proto/demo.md#cdemofullpacket) |
| 14 | [`CDemoSaveGame`](proto/demo.md#cdemosavegame) |
| 15 | [`CDemoSpawnGroups`](proto/demo.md#cdemospawngroups) |
| 15 | [`CDemoSpawnGroupsHLTVBroadcast`](proto/demo.md#cdemospawngroupshltvbroadcast) |
| 16 | [`CDemoAnimationData`](proto/demo.md#cdemoanimationdata) |
| 17 | [`CDemoAnimationHeader`](proto/demo.md#cdemoanimationheader) |
| 18 | [`CDemoRecovery`](proto/demo.md#cdemorecovery) |
