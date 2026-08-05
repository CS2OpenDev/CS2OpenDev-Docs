---
layout: default
title: Schema History
nav_order: 15
---

# Schema History

{: .note }
> Source: CS2 build **24537688** · 2026-08-03 · `windows-x86_64` · schema `0.5.0`

Field-precise, build-to-build evolution of the CS2 C++ entity schema, derived by diffing every committed `entity_schema.json` snapshot (SchemaTracker's cumulative `schema_evolution.json`, Layer A).  Unlike the coarse [Changelog](changelog.html) — which only reports *that* a class changed — this reports *which field* was added, removed, retyped, or moved.

- **Platform:** `windows-x86_64` (the canonical render; `linux-x86_64` differs only in offsets/sizes)
- **Baseline build:** `10832117` · **Latest build:** `24537688`
- **Transitions:** 378 total, **138 with structural changes** (240 no-op builds)
- **Full per-field history:** the portable [`field_history.json`](downstream-codegen-schemas/field_history.json) carries first/last-seen and the type history for every `(class, field)` across all builds.

To bring an instance captured under build *X* forward to build *Y*, apply each transition in `[X, Y)` in order.  Every op carries both endpoints, so the same chain replays backward.

## Transitions with structural changes

| Transition | Classes +/−/~ | Enums +/−/~ | Field ops |
|------------|---------------|-------------|-----------|
| `24304127` → `24537688` | 0 / 0 / 6 | 0 / 0 / 1 | 99 |
| `24248951` → `24304127` | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `24074625` → `24116939` | 232 / 59 / 1075 | 96 / 15 / 27 | 4785 |
| `23773332` → `23994866` | 0 / 0 / 1 | 0 / 0 / 0 | 5 |
| `23333587` → `23354238` | 0 / 0 / 1 | 0 / 0 / 0 | 11 |
| `23296257` → `23333587` | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `23241720` → `23296257` | 0 / 0 / 6 | 0 / 0 / 0 | 30 |
| `23187627` → `23241720` | 0 / 0 / 2 | 0 / 0 / 0 | 122 |
| `23118419` → `23135875` | 0 / 0 / 10 | 0 / 0 / 0 | 294 |
| `23018732` → `23038025` | 0 / 0 / 6 | 0 / 0 / 0 | 161 |
| `22948967` → `23000122` | 0 / 2 / 12 | 0 / 1 / 0 | 174 |
| `22880072` → `22894272` | 2 / 0 / 5 | 0 / 0 / 0 | 216 |
| `22877907` → `22880072` | 775 / 0 / 0 | 49 / 0 / 0 | 0 |
| `22876476` → `22877907` | 0 / 775 / 2 | 0 / 49 / 0 | 118 |
| `22627914` → `22876476` | 164 / 28 / 1423 | 36 / 3 / 11 | 11112 |
| `22370414` → `22405124` | 0 / 0 / 3 | 0 / 0 / 0 | 13 |
| `22336282` → `22368164` | 0 / 0 / 1 | 0 / 0 / 0 | 9 |
| `22266770` → `22303696` | 0 / 0 / 1 | 0 / 0 / 0 | 120 |
| `21868850` → `22063930` | 0 / 0 / 1 | 0 / 0 / 0 | 120 |
| `21708006` → `21789745` | 0 / 0 / 5 | 0 / 0 / 0 | 195 |
| `21626952` → `21657141` | 0 / 0 / 1 | 0 / 0 / 0 | 1 |
| `21609678` → `21626952` | 0 / 0 / 1 | 0 / 0 / 0 | 4 |
| `21595680` → `21609678` | 0 / 0 / 9 | 0 / 0 / 0 | 52 |
| `21529689` → `21593048` | 437 / 16 / 1042 | 32 / 3 / 14 | 7624 |
| `20670159` → `20775075` | 0 / 0 / 9 | 0 / 0 / 1 | 35 |
| `20596740` → `20670159` | 0 / 0 / 4 | 0 / 0 / 0 | 6 |
| `20535897` → `20596740` | 2 / 2 / 30 | 0 / 0 / 0 | 95 |
| `20442176` → `20503857` | 2 / 0 / 7 | 0 / 0 / 0 | 155 |
| `20392228` → `20410358` | 0 / 0 / 3 | 0 / 0 / 0 | 44 |
| `20278147` → `20392228` | 90 / 15 / 963 | 9 / 1 / 11 | 5927 |
| `20215164` → `20230584` | 2 / 0 / 6 | 0 / 0 / 0 | 0 |
| `20116868` → `20134212` | 0 / 0 / 8 | 0 / 0 / 0 | 109 |
| `20101391` → `20116868` | 0 / 0 / 3 | 0 / 0 / 0 | 0 |
| `20084900` → `20101391` | 0 / 0 / 2 | 0 / 0 / 0 | 18 |
| `20024151` → `20040136` | 2 / 2 / 3 | 0 / 0 / 0 | 14 |
| `20022951` → `20024151` | 0 / 0 / 2 | 0 / 0 / 0 | 2 |
| `20011206` → `20022951` | 0 / 0 / 2 | 0 / 0 / 0 | 16 |
| `19932965` → `20007038` | 20 / 49 / 519 | 11 / 5 / 8 | 2941 |
| `19903381` → `19916932` | 0 / 0 / 1 | 0 / 0 / 0 | 71 |
| `19762064` → `19847200` | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `19657793` → `19747060` | 0 / 0 / 20 | 1 / 0 / 0 | 216 |
| `19605004` → `19644975` | 0 / 0 / 9 | 0 / 0 / 0 | 290 |
| `19450283` → `19602992` | 57 / 301 / 239 | 15 / 14 / 18 | 985 |
| `19421827` → `19450283` | 0 / 0 / 2 | 0 / 0 / 0 | 8 |
| `19406478` → `19421827` | 0 / 0 / 48 | 0 / 0 / 0 | 41 |
| `19391961` → `19406478` | 0 / 0 / 50 | 0 / 0 / 0 | 75 |
| `19251152` → `19388062` | 1442 / 204 / 1482 | 99 / 16 / 40 | 8188 |
| `19222571` → `19236816` | 0 / 0 / 1 | 0 / 0 / 0 | 89 |
| `18816418` → `19083876` | 0 / 1 / 5 | 0 / 0 / 1 | 7 |
| `18382650` → `18394927` | 0 / 0 / 2 | 0 / 0 / 0 | 4 |
| `18185360` → `18380903` | 1 / 0 / 5 | 0 / 0 / 0 | 320 |
| `17800215` → `17931128` | 0 / 27 / 48 | 0 / 0 / 3 | 87 |
| `17732524` → `17800215` | 0 / 0 / 8 | 0 / 0 / 0 | 248 |
| `17230622` → `17272995` | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `17148705` → `17162095` | 0 / 0 / 1 | 0 / 0 / 0 | 2 |
| `17032840` → `17084099` | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `16958277` → `17006600` | 0 / 0 / 1 | 0 / 0 / 0 | 3 |
| `16806987` → `16933364` | 0 / 0 / 2 | 0 / 0 / 0 | 45 |
| `16687167` → `16794210` | 0 / 0 / 10 | 0 / 0 / 0 | 11 |
| `16382602` → `16398395` | 1 / 0 / 16 | 1 / 0 / 0 | 203 |
| `16243257` → `16320304` | 6 / 0 / 8 | 0 / 0 / 0 | 66 |
| `16213816` → `16228412` | 0 / 0 / 2 | 0 / 0 / 0 | 5 |
| `16184206` → `16213816` | 0 / 0 / 65 | 0 / 0 / 0 | 207 |
| `16087659` → `16156846` | 0 / 0 / 114 | 0 / 0 / 0 | 90 |
| `16071819` → `16087659` | 0 / 0 / 4 | 0 / 0 / 0 | 3 |
| `16015437` → `16057663` | 7 / 1 / 474 | 1 / 0 / 0 | 3002 |
| `15923186` → `15936283` | 0 / 0 / 2 | 1 / 0 / 0 | 14 |
| `15656858` → `15908369` | 251 / 10 / 1398 | 38 / 1 / 19 | 8800 |
| `15582507` → `15644071` | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `15372392` → `15424813` | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `15324295` → `15372392` | 2 / 0 / 13 | 0 / 0 / 0 | 368 |
| `15309899` → `15312306` | 0 / 0 / 1 | 0 / 0 / 0 | 1 |
| `15155775` → `15309899` | 0 / 0 / 2 | 0 / 0 / 0 | 28 |
| `14851576` → `14864281` | 42 / 0 / 0 | 14 / 0 / 0 | 0 |
| `14850494` → `14851576` | 0 / 42 / 0 | 0 / 14 / 0 | 0 |
| `14787627` → `14836768` | 0 / 0 / 69 | 0 / 0 / 1 | 314 |
| `14684351` → `14711932` | 0 / 0 / 1 | 0 / 0 / 0 | 1 |
| `14672345` → `14684351` | 0 / 0 / 5 | 0 / 0 / 0 | 125 |
| `14553911` → `14602005` | 0 / 20 / 9 | 0 / 0 / 1 | 12 |
| `14487420` → `14536966` | 0 / 0 / 59 | 0 / 0 / 0 | 66 |
| `14446408` → `14470938` | 224 / 41 / 1046 | 40 / 2 / 24 | 6767 |
| `14249031` → `14296060` | 0 / 1 / 0 | 0 / 0 / 0 | 0 |
| `14191516` → `14225153` | 0 / 0 / 1 | 0 / 0 / 0 | 1 |
| `14139085` → `14178987` | 0 / 1 / 134 | 0 / 0 / 1 | 680 |
| `14075664` → `14139085` | 0 / 0 / 9 | 0 / 0 / 0 | 136 |
| `13804656` → `13829089` | 0 / 0 / 1 | 0 / 0 / 0 | 1 |
| `13735017` → `13758187` | 0 / 0 / 2 | 0 / 0 / 0 | 1 |
| `13687128` → `13735017` | 0 / 0 / 1 | 0 / 0 / 0 | 7 |
| `13481434` → `13593156` | 0 / 0 / 9 | 0 / 0 / 1 | 113 |
| `13460160` → `13470915` | 0 / 0 / 3 | 0 / 0 / 0 | 8 |
| `13439412` → `13460160` | 41 / 0 / 0 | 3 / 0 / 0 | 0 |
| `13438770` → `13439412` | 0 / 41 / 0 | 0 / 3 / 0 | 0 |
| `13240071` → `13385739` | 129 / 32 / 2674 | 355 / 0 / 0 | 13991 |
| `12957241` → `12995320` | 0 / 0 / 1 | 0 / 0 / 0 | 2 |
| `12934552` → `12956327` | 0 / 0 / 64 | 0 / 0 / 0 | 232 |
| `12895370` → `12905434` | 0 / 0 / 10 | 0 / 0 / 0 | 12 |
| `12873276` → `12895370` | 0 / 0 / 73 | 0 / 0 / 0 | 179 |
| `12854667` → `12873276` | 0 / 0 / 12 | 0 / 0 / 0 | 92 |
| `12756335` → `12843950` | 0 / 19 / 119 | 0 / 0 / 0 | 213 |
| `12736853` → `12756335` | 1 / 0 / 0 | 0 / 0 / 0 | 0 |
| `12725887` → `12726829` | 0 / 0 / 2 | 0 / 0 / 0 | 0 |
| `12693482` → `12725887` | 2 / 0 / 86 | 0 / 0 / 0 | 230 |
| `12666450` → `12693482` | 0 / 0 / 7 | 0 / 0 / 0 | 307 |
| `12656218` → `12666450` | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `12617548` → `12656218` | 0 / 0 / 119 | 0 / 0 / 0 | 172 |
| `12616847` → `12617548` | 60 / 0 / 0 | 0 / 0 / 0 | 0 |
| `12616521` → `12616847` | 0 / 60 / 0 | 0 / 0 / 0 | 0 |
| `12607859` → `12616521` | 0 / 0 / 17 | 0 / 0 / 0 | 369 |
| `12547359` → `12606072` | 11 / 0 / 149 | 0 / 0 / 0 | 951 |
| `12494887` → `12535846` | 1 / 0 / 2 | 0 / 0 / 0 | 8 |
| `12465841` → `12485612` | 1 / 0 / 56 | 0 / 0 / 0 | 95 |
| `12438553` → `12465841` | 1 / 0 / 10 | 0 / 0 / 0 | 238 |
| `12416747` → `12427908` | 2 / 0 / 33 | 0 / 0 / 0 | 113 |
| `12377892` → `12398121` | 0 / 0 / 5 | 0 / 0 / 0 | 7 |
| `12349504` → `12358457` | 0 / 0 / 6 | 0 / 0 / 0 | 156 |
| `12328020` → `12338824` | 0 / 0 / 54 | 0 / 0 / 0 | 53 |
| `12312218` → `12321656` | 0 / 0 / 2 | 0 / 0 / 0 | 2 |
| `12192623` → `12299470` | 45 / 94 / 297 | 0 / 0 / 0 | 2088 |
| `12184506` → `12192623` | 0 / 0 / 9 | 0 / 0 / 0 | 10 |
| `12147839` → `12182426` | 0 / 1 / 308 | 0 / 0 / 0 | 2056 |
| `12136709` → `12146510` | 0 / 0 / 5 | 0 / 0 / 0 | 126 |
| `12085105` → `12093437` | 0 / 0 / 7 | 0 / 0 / 0 | 70 |
| `11979365` → `12083517` | 20 / 6 / 95 | 0 / 0 / 0 | 745 |
| `11887584` → `11949605` | 2 / 0 / 86 | 0 / 0 / 0 | 298 |
| `11852153` → `11862226` | 1 / 1 / 4 | 0 / 0 / 0 | 20 |
| `11785765` → `11852153` | 10 / 3 / 184 | 0 / 0 / 0 | 1092 |
| `11732520` → `11743491` | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `11724280` → `11732520` | 0 / 0 / 54 | 0 / 0 / 0 | 106 |
| `11602641` → `11723163` | 13 / 10 / 23 | 0 / 0 / 0 | 421 |
| `11593506` → `11602641` | 0 / 0 / 1 | 0 / 0 / 0 | 108 |
| `11519750` → `11593506` | 16 / 131 / 358 | 0 / 0 / 0 | 2801 |
| `11473523` → `11483104` | 0 / 0 / 4 | 0 / 0 / 0 | 6 |
| `11437123` → `11472786` | 4 / 1 / 24 | 0 / 0 / 0 | 99 |
| `11428378` → `11437123` | 0 / 0 / 2 | 0 / 0 / 0 | 4 |
| `11408339` → `11418830` | 0 / 0 / 2 | 0 / 0 / 0 | 4 |
| `11081546` → `11408339` | 173 / 135 / 1334 | 0 / 0 / 0 | 8789 |
| `10894923` → `10898038` | 4 / 0 / 2 | 0 / 0 / 0 | 8 |
| `10853092` → `10894923` | 50 / 11 / 503 | 0 / 0 / 0 | 3133 |

## Most recent structural changes

### `24304127` → `24537688`

**Classes changed (6):**

| Class | Field ops | Layout |
|-------|-----------|--------|
| `client.dll/C_CSGO_PreviewPlayer` | ~offset×2 | resize 13568→13584 |
| `client.dll/C_CSGO_PreviewPlayerAlias_csgo_player_previewmodel` | — | resize 13568→13584 |
| `client.dll/C_CSGO_TeamPreviewModel` | — | resize 13568→13584 |
| `client.dll/C_CSPlayerPawn` | ＋field×1, ~offset×73 | resize 13408→13424 |
| `client.dll/C_CSWeaponBase` | ~offset×15 | — |
| `server.dll/CCSPlayerPawn` | ＋field×1, ~offset×7 | — |

### `24248951` → `24304127`

**Classes changed (1):**

| Class | Field ops | Layout |
|-------|-----------|--------|
| `client.dll/C_PlantedC4` | — | resize 5904→5936 |

### `24074625` → `24116939`

**Classes added (232):** `!GlobalTypes/AABBWS_t`, `!GlobalTypes/AI_FacingServices_DebugSnapshotData_t`, `!GlobalTypes/AI_GroundRootMotionMotor_DebugSnapshotData_t`, `!GlobalTypes/AI_GroundRootMotionMotor_DebugSnapshotData_t::Event_t`, `!GlobalTypes/AI_MotorServices_DebugSnapshotData_t`, `!GlobalTypes/AI_MotorServices_DebugSnapshotData_t::MotorPathWaypoint_t`, `!GlobalTypes/ActorMapping_t`, `!GlobalTypes/AggregateVertexEmissiveStreamOnDiskData_t`, `!GlobalTypes/CAnimGraph2InstancePtr`, `!GlobalTypes/CAnimGraphControllerPtr`, `!GlobalTypes/CAudioAmpNodeDesc`, `!GlobalTypes/CAudioAutoFilterNodeDesc`, `!GlobalTypes/CAudioBlendDesc`, `!GlobalTypes/CAudioBoxverb2NodeDesc`, `!GlobalTypes/CAudioBoxverbNodeDesc`, `!GlobalTypes/CAudioConvolutionNodeDesc`, `!GlobalTypes/CAudioDelayNodeDesc`, `!GlobalTypes/CAudioDiffusorNodeDesc`, `!GlobalTypes/CAudioDualCompressorNodeDesc`, `!GlobalTypes/CAudioDynamics3BandNodeDesc`, `!GlobalTypes/CAudioDynamicsCompressorNodeDesc`, `!GlobalTypes/CAudioDynamicsLimiterNodeDesc`, `!GlobalTypes/CAudioDynamicsNodeDesc`, `!GlobalTypes/CAudioEQ8NodeDesc`, `!GlobalTypes/CAudioEffectChainNodeDesc`, `!GlobalTypes/CAudioEnvelopeNodeDesc`, `!GlobalTypes/CAudioFilterNodeDesc`, `!GlobalTypes/CAudioFlangerNodeDesc`, `!GlobalTypes/CAudioFreeverbNodeDesc`, `!GlobalTypes/CAudioMeterNodeDesc`, `!GlobalTypes/CAudioMixerNodeDesc`, `!GlobalTypes/CAudioModDelayNodeDesc`, `!GlobalTypes/CAudioOscNodeDesc`, `!GlobalTypes/CAudioOutputNodeDesc`, `!GlobalTypes/CAudioPannerNodeDesc`, `!GlobalTypes/CAudioPitchShiftNodeDesc`, `!GlobalTypes/CAudioPlateverbNodeDesc`, `!GlobalTypes/CAudioProcessorNodeDesc`, `!GlobalTypes/CAudioShaperNodeDesc`, `!GlobalTypes/CAudioSourceNodeDesc` … (+192 more)

**Classes removed (59):** `!GlobalTypes/AI_MotorGroundAnimgraph_DebugSnapshotData_t`, `!GlobalTypes/AI_MotorGroundAnimgraph_DebugSnapshotData_t::Event_t`, `!GlobalTypes/AI_Motor_DebugSnapshotData_t`, `!GlobalTypes/CAnimEventListener`, `!GlobalTypes/CAnimEventListenerBase`, `!GlobalTypes/CAnimEventQueueListener`, `!GlobalTypes/CCompressorGroup`, `!GlobalTypes/CSceneCriteria`, `!GlobalTypes/CSceneOpportunity`, `!GlobalTypes/CSceneRequest`, `!GlobalTypes/CVoiceContainerEnvelope`, `!GlobalTypes/CastSphereSATParams_t`, `!GlobalTypes/ExternalAnimGraph_t`, `!GlobalTypes/SceneInterestTags_t`, `!GlobalTypes/SceneOpportunityActor_t`, `!GlobalTypes/SceneOpportunityHandle_t`, `!GlobalTypes/SceneRequestHandle_t`, `!GlobalTypes/SceneRequestTargetMapPair_t`, `animationsystem.dll/CPulseCell_WaitForCursorsWithTagBase::CursorState_t`, `animationsystem.dll/PulseObservableBoolExpression_t`, `assetbrowser.dll/CPulseCell_WaitForCursorsWithTagBase::CursorState_t`, `assetbrowser.dll/PulseObservableBoolExpression_t`, `assetpreview.dll/CPulseCell_WaitForCursorsWithTagBase::CursorState_t`, `assetpreview.dll/PulseObservableBoolExpression_t`, `assetrename.dll/CPulseCell_WaitForCursorsWithTagBase::CursorState_t`, `assetrename.dll/PulseObservableBoolExpression_t`, `client.dll/CInfoInteraction`, `client.dll/CPulseAnimFuncs`, `client.dll/CPulseCell_WaitForCursorsWithTagBase::CursorState_t`, `client.dll/CScenePayloadVData`, `client.dll/PulseObservableBoolExpression_t`, `hammer.dll/CPulseCell_WaitForCursorsWithTagBase::CursorState_t`, `hammer.dll/PulseObservableBoolExpression_t`, `met.dll/CPulseCell_WaitForCursorsWithTagBase::CursorState_t`, `met.dll/PulseObservableBoolExpression_t`, `modeldoc_editor.dll/CPulseCell_WaitForCursorsWithTagBase::CursorState_t`, `modeldoc_editor.dll/PulseObservableBoolExpression_t`, `modeldoc_utils.dll/CPulseCell_WaitForCursorsWithTagBase::CursorState_t`, `modeldoc_utils.dll/PulseObservableBoolExpression_t`, `particles.dll/CPulseCell_WaitForCursorsWithTagBase::CursorState_t` … (+19 more)

**Classes changed (1075):**

| Class | Field ops | Layout |
|-------|-----------|--------|
| `!GlobalTypes/AI_BaseNPCAnimGraph_DebugSnapshotData_t` | ＋field×6, ~offset×2, −field×2 | resize 40→64, reparent, flags |
| `!GlobalTypes/AI_BaseNPC_DebugSnapshotData_t` | ＋field×7, ~offset×2, −field×4 | resize 120→376 |
| `!GlobalTypes/AI_DefaultNPC_DebugSnapshotData_t` | ＋field×1, ~offset×1, −field×3 | resize 168→120 |
| `!GlobalTypes/AI_DefaultNPC_DebugSnapshotData_t::PathQuery_t` | ＋field×2, −field×2 | — |
| `!GlobalTypes/AI_Navigator_DebugSnapshotData_t` | ＋field×5, ~offset×2, −field×4 | reparent, flags |
| `!GlobalTypes/AI_Navigator_DebugSnapshotData_t::Waypoint_t` | ＋field×1 | resize 20→24 |
| `!GlobalTypes/AggregateMeshInfo_t` | ＋field×2, ~offset×1 | resize 36→44 |
| `!GlobalTypes/AggregateRTProxySceneObject_t` | ＋field×1 | resize 104→120 |
| `!GlobalTypes/AggregateSceneObject_t` | ＋field×1 | — |
| `!GlobalTypes/AutoRoomDoorwayPairs_t` | ~type×2 | realign, flags |
| `!GlobalTypes/CAI_Expresser` | ＋field×2 | realign, flags |
| `!GlobalTypes/CAI_ExpresserWithFollowup` | — | realign, flags |
| `!GlobalTypes/CAnimGraphControllerManager` | ~offset×1 | resize 176→152 |
| `!GlobalTypes/CBaseTrailRenderer` | ＋field×1, ~offset×1 | resize 12520→12888 |
| `!GlobalTypes/CBreakableStageHelper` | — | realign, flags |
| `!GlobalTypes/CCS2ChickenGraphController` | ~offset×8, −field×1 | resize 344→320 |
| `!GlobalTypes/CCS2UIPawnGraphController` | ＋field×1, ~offset×11 | resize 448→472 |
| `!GlobalTypes/CClientAlphaProperty` | — | realign, flags |
| `!GlobalTypes/CConstantForceController` | — | realign, flags |
| `!GlobalTypes/CDebugSnapshotData_t` | ~meta×1 | — |
| `!GlobalTypes/CDecalInstance` | ＋field×1, ~offset×6 | — |
| `!GlobalTypes/CDetailPropModel` | ＋field×1, ~offset×15 | resize 320→328 |
| `!GlobalTypes/CEntityAttributeTable` | ~type×2 | — |
| `!GlobalTypes/CFlashlightEffect` | ~type×1 | — |
| `!GlobalTypes/CFogScatteringLayer` | — | resize 64→72 |
| `!GlobalTypes/CGameChoreoServices` | — | realign, flags |
| `!GlobalTypes/CGlobalLightBase` | ~type×3 | — |
| `!GlobalTypes/CInfoChoreoAnchorPosition` | ＋field×4, ~offset×4, −field×2 | resize 56→80, realign, flags |
| `!GlobalTypes/CMaterialDrawDescriptor` | ＋field×1, ~offset×8 | resize 264→280 |
| `!GlobalTypes/CMotorController` | ~type×1 | realign, flags |
| `!GlobalTypes/CMovementStatsProperty` | — | realign, flags |
| `!GlobalTypes/CMultiplayer_Expresser` | — | realign, flags |
| `!GlobalTypes/CNPCPhysicsHull` | — | resize 56→64, flags |
| `!GlobalTypes/CNetworkTransmitComponent` | — | realign, flags |
| `!GlobalTypes/CNmAdditiveBlendTask` | — | resize 208→256, realign |
| `!GlobalTypes/CNmAimCSTask` | — | resize 256→304 |
| `!GlobalTypes/CNmBlendTask` | — | resize 208→256, realign |
| `!GlobalTypes/CNmBlendTaskBase` | — | resize 208→256 |
| `!GlobalTypes/CNmCachedPoseReadTask` | — | resize 80→128, realign |
| `!GlobalTypes/CNmCachedPoseWriteTask` | — | resize 80→128, realign |
| `!GlobalTypes/CNmChainLookatNode::CDefinition` | ＋field×4, ~offset×5, −field×2 | resize 56→120 |
| `!GlobalTypes/CNmChainLookatTask` | −field×11 | resize 128→288, realign |
| `!GlobalTypes/CNmClip` | ＋field×1, ~offset×6, −field×4 | resize 576→512 |
| `!GlobalTypes/CNmFollowBoneTask` | — | resize 104→144, realign |
| `!GlobalTypes/CNmFootIKTask` | ~offset×12 | resize 272→320 |
| `!GlobalTypes/CNmGraphDocBoneMaskNode` | ＋field×1 | resize 520→528 |
| `!GlobalTypes/CNmGraphDocDataDictionary::IDSet_t` | ~meta×2 | — |
| `!GlobalTypes/CNmGraphDocDataDictionary::ParameterSet_t` | ~meta×1 | — |
| `!GlobalTypes/CNmGraphDocDataDictionary::Parameter_t` | ~meta×1 | — |
| `!GlobalTypes/CNmGraphInstance` | — | resize 992→976 |
| `!GlobalTypes/CNmModelSpaceBlendTask` | — | resize 208→256, realign |
| `!GlobalTypes/CNmOverlayBlendTask` | — | resize 208→256, realign |
| `!GlobalTypes/CNmPoseTask` | — | resize 72→112 |
| `!GlobalTypes/CNmPreviewArchetype` | — | resize 48→64 |
| `!GlobalTypes/CNmReferencePoseTask` | — | resize 72→112, realign |
| `!GlobalTypes/CNmRootMotionOverrideNode::CDefinition` | ＋field×1, ~offset×3 | — |
| `!GlobalTypes/CNmSampleTask` | — | resize 88→128, realign |
| `!GlobalTypes/CNmScaleTask` | — | resize 160→208, realign |
| `!GlobalTypes/CNmSkeleton` | ＋field×1, ~offset×1 | resize 192→208 |
| `!GlobalTypes/CNmSkeletonDocument` | ＋field×1, ~offset×1, ~type×1 | resize 264→288 |
| … | _1015 more changed classes — see `field_history.json`_ | |
