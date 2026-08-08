---
layout: default
title: engine2
parent: Schemas
nav_exclude: true
---

# Module: engine2

[📊 View UML Diagram](../diagrams/engine2.md)

42 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [EngineLoopState_t](engine2/EngineLoopState_t.md) | class | 40 | 4 |  |
| [EventAdvanceTick_t](engine2/EventAdvanceTick_t.md) | class | 64 | 4 | [EventSimulate_t](engine2/EventSimulate_t.md) |
| [EventAppShutdown_t](engine2/EventAppShutdown_t.md) | class | 4 | 1 |  |
| [EventBugBugComplete_t](engine2/EventBugBugComplete_t.md) | class | 8 | 1 |  |
| [EventBugBug_t](engine2/EventBugBug_t.md) | class | 32 | 0 |  |
| [EventClientAdvanceNonRenderedFrame_t](engine2/EventClientAdvanceNonRenderedFrame_t.md) | class | 1 | 0 |  |
| [EventClientAdvanceTick_t](engine2/EventClientAdvanceTick_t.md) | class | 64 | 0 | [EventAdvanceTick_t](engine2/EventAdvanceTick_t.md) |
| [EventClientFrameSimulate_t](engine2/EventClientFrameSimulate_t.md) | class | 56 | 4 |  |
| [EventClientOutput_t](engine2/EventClientOutput_t.md) | class | 56 | 5 |  |
| [EventClientPauseSimulate_t](engine2/EventClientPauseSimulate_t.md) | class | 48 | 0 | [EventSimulate_t](engine2/EventSimulate_t.md) |
| [EventClientPollInput_t](engine2/EventClientPollInput_t.md) | class | 48 | 2 |  |
| [EventClientPollNetworking_t](engine2/EventClientPollNetworking_t.md) | class | 4 | 1 |  |
| [EventClientPostAdvanceTick_t](engine2/EventClientPostAdvanceTick_t.md) | class | 64 | 0 | [EventPostAdvanceTick_t](engine2/EventPostAdvanceTick_t.md) |
| [EventClientPostOutput_t](engine2/EventClientPostOutput_t.md) | class | 64 | 5 |  |
| [EventClientPostSimulate_t](engine2/EventClientPostSimulate_t.md) | class | 48 | 0 | [EventSimulate_t](engine2/EventSimulate_t.md) |
| [EventClientPreOutputParallelWithServer_t](engine2/EventClientPreOutputParallelWithServer_t.md) | class | 72 | 0 | [EventClientPreOutput_t](engine2/EventClientPreOutput_t.md) |
| [EventClientPreOutput_t](engine2/EventClientPreOutput_t.md) | class | 72 | 6 |  |
| [EventClientPreSimulate_t](engine2/EventClientPreSimulate_t.md) | class | 48 | 0 | [EventSimulate_t](engine2/EventSimulate_t.md) |
| [EventClientProcessGameInput_t](engine2/EventClientProcessGameInput_t.md) | class | 48 | 3 |  |
| [EventClientProcessInput_t](engine2/EventClientProcessInput_t.md) | class | 56 | 4 |  |
| [EventClientProcessNetworking_t](engine2/EventClientProcessNetworking_t.md) | class | 4 | 1 |  |
| [EventClientSceneSystemThreadStateChange_t](engine2/EventClientSceneSystemThreadStateChange_t.md) | class | 1 | 1 |  |
| [EventClientSimulate_t](engine2/EventClientSimulate_t.md) | class | 48 | 0 | [EventSimulate_t](engine2/EventSimulate_t.md) |
| [EventFrameBoundary_t](engine2/EventFrameBoundary_t.md) | class | 4 | 1 |  |
| [EventModInitialized_t](engine2/EventModInitialized_t.md) | class | 1 | 0 |  |
| [EventPostAdvanceTick_t](engine2/EventPostAdvanceTick_t.md) | class | 64 | 4 | [EventSimulate_t](engine2/EventSimulate_t.md) |
| [EventPostDataUpdate_t](engine2/EventPostDataUpdate_t.md) | class | 16 | 1 |  |
| [EventPreDataUpdate_t](engine2/EventPreDataUpdate_t.md) | class | 16 | 1 |  |
| [EventProfileStorageAvailable_t](engine2/EventProfileStorageAvailable_t.md) | class | 4 | 1 |  |
| [EventServerAdvanceTick_t](engine2/EventServerAdvanceTick_t.md) | class | 64 | 0 | [EventAdvanceTick_t](engine2/EventAdvanceTick_t.md) |
| [EventServerBeginAsyncPostTickWork_t](engine2/EventServerBeginAsyncPostTickWork_t.md) | class | 1 | 1 |  |
| [EventServerBeginSimulate_t](engine2/EventServerBeginSimulate_t.md) | class | 48 | 0 | [EventSimulate_t](engine2/EventSimulate_t.md) |
| [EventServerEndAsyncPostTickWork_t](engine2/EventServerEndAsyncPostTickWork_t.md) | class | 1 | 0 |  |
| [EventServerEndSimulate_t](engine2/EventServerEndSimulate_t.md) | class | 1 | 1 |  |
| [EventServerPollNetworking_t](engine2/EventServerPollNetworking_t.md) | class | 48 | 0 | [EventSimulate_t](engine2/EventSimulate_t.md) |
| [EventServerPostAdvanceTick_t](engine2/EventServerPostAdvanceTick_t.md) | class | 72 | 1 | [EventPostAdvanceTick_t](engine2/EventPostAdvanceTick_t.md) |
| [EventServerPostSimulate_t](engine2/EventServerPostSimulate_t.md) | class | 56 | 1 | [EventSimulate_t](engine2/EventSimulate_t.md) |
| [EventServerProcessNetworking_t](engine2/EventServerProcessNetworking_t.md) | class | 48 | 0 | [EventSimulate_t](engine2/EventSimulate_t.md) |
| [EventSetTime_t](engine2/EventSetTime_t.md) | class | 96 | 8 |  |
| [EventSimpleLoopFrameUpdate_t](engine2/EventSimpleLoopFrameUpdate_t.md) | class | 48 | 3 |  |
| [EventSimulate_t](engine2/EventSimulate_t.md) | class | 48 | 3 |  |
| [EventSplitScreenStateChanged_t](engine2/EventSplitScreenStateChanged_t.md) | class | 1 | 0 |  |
