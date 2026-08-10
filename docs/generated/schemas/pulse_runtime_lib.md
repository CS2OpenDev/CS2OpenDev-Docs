---
layout: default
title: pulse_runtime_lib
parent: Schemas
nav_exclude: true
---

# Module: pulse_runtime_lib

[📊 View UML Diagram](../diagrams/pulse_runtime_lib.md)

109 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CBasePulseGraphInstance](pulse_runtime_lib/CBasePulseGraphInstance.md) | class | 272 | 0 |  |
| [CPulseArraylib](pulse_runtime_lib/CPulseArraylib.md) | class | 1 | 0 |  |
| [CPulseBreakpointLocation](pulse_runtime_lib/CPulseBreakpointLocation.md) | class | 40 | 3 |  |
| [CPulseCell_Base](pulse_runtime_lib/CPulseCell_Base.md) | class | 72 | 1 |  |
| [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) | class | 72 | 0 | [CPulseCell_Base](pulse_runtime_lib/CPulseCell_Base.md) |
| [CPulseCell_BaseLerp](pulse_runtime_lib/CPulseCell_BaseLerp.md) | class | 288 | 1 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_BaseLerp::CursorState_t](pulse_runtime_lib/CPulseCell_BaseLerp.CursorState_t.md) | class | 8 | 2 |  |
| [CPulseCell_BaseRequirement](pulse_runtime_lib/CPulseCell_BaseRequirement.md) | class | 72 | 0 | [CPulseCell_Base](pulse_runtime_lib/CPulseCell_Base.md) |
| [CPulseCell_BaseState](pulse_runtime_lib/CPulseCell_BaseState.md) | class | 216 | 0 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_BaseValue](pulse_runtime_lib/CPulseCell_BaseValue.md) | class | 72 | 0 | [CPulseCell_Base](pulse_runtime_lib/CPulseCell_Base.md) |
| [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) | class | 216 | 2 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_BooleanSwitchState](pulse_runtime_lib/CPulseCell_BooleanSwitchState.md) | class | 480 | 3 | [CPulseCell_BaseState](pulse_runtime_lib/CPulseCell_BaseState.md) |
| [CPulseCell_CursorQueue](pulse_runtime_lib/CPulseCell_CursorQueue.md) | class | 304 | 1 | [CPulseCell_WaitForCursorsWithTagBase](pulse_runtime_lib/CPulseCell_WaitForCursorsWithTagBase.md) |
| [CPulseCell_FireCursors](pulse_runtime_lib/CPulseCell_FireCursors.md) | class | 320 | 3 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_Inflow_BaseEntrypoint](pulse_runtime_lib/CPulseCell_Inflow_BaseEntrypoint.md) | class | 128 | 2 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Inflow_EntOutputHandler](pulse_runtime_lib/CPulseCell_Inflow_EntOutputHandler.md) | class | 184 | 3 | [CPulseCell_Inflow_BaseEntrypoint](pulse_runtime_lib/CPulseCell_Inflow_BaseEntrypoint.md) |
| [CPulseCell_Inflow_EventHandler](pulse_runtime_lib/CPulseCell_Inflow_EventHandler.md) | class | 144 | 1 | [CPulseCell_Inflow_BaseEntrypoint](pulse_runtime_lib/CPulseCell_Inflow_BaseEntrypoint.md) |
| [CPulseCell_Inflow_GraphHook](pulse_runtime_lib/CPulseCell_Inflow_GraphHook.md) | class | 144 | 1 | [CPulseCell_Inflow_BaseEntrypoint](pulse_runtime_lib/CPulseCell_Inflow_BaseEntrypoint.md) |
| [CPulseCell_Inflow_Method](pulse_runtime_lib/CPulseCell_Inflow_Method.md) | class | 200 | 5 | [CPulseCell_Inflow_BaseEntrypoint](pulse_runtime_lib/CPulseCell_Inflow_BaseEntrypoint.md) |
| [CPulseCell_Inflow_ObservableVariableListener](pulse_runtime_lib/CPulseCell_Inflow_ObservableVariableListener.md) | class | 136 | 2 | [CPulseCell_Inflow_BaseEntrypoint](pulse_runtime_lib/CPulseCell_Inflow_BaseEntrypoint.md) |
| [CPulseCell_Inflow_Wait](pulse_runtime_lib/CPulseCell_Inflow_Wait.md) | class | 288 | 1 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_Inflow_Yield](pulse_runtime_lib/CPulseCell_Inflow_Yield.md) | class | 288 | 1 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_InlineNodeSkipSelector](pulse_runtime_lib/CPulseCell_InlineNodeSkipSelector.md) | class | 176 | 4 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_IntervalTimer](pulse_runtime_lib/CPulseCell_IntervalTimer.md) | class | 360 | 2 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_IntervalTimer::CursorState_t](pulse_runtime_lib/CPulseCell_IntervalTimer.CursorState_t.md) | class | 20 | 5 |  |
| [CPulseCell_IsRequirementValid](pulse_runtime_lib/CPulseCell_IsRequirementValid.md) | class | 72 | 0 | [CPulseCell_BaseRequirement](pulse_runtime_lib/CPulseCell_BaseRequirement.md) |
| [CPulseCell_IsRequirementValid::Criteria_t](pulse_runtime_lib/CPulseCell_IsRequirementValid.Criteria_t.md) | class | 1 | 1 |  |
| [CPulseCell_LimitCount](pulse_runtime_lib/CPulseCell_LimitCount.md) | class | 80 | 1 | [CPulseCell_BaseRequirement](pulse_runtime_lib/CPulseCell_BaseRequirement.md) |
| [CPulseCell_LimitCount::Criteria_t](pulse_runtime_lib/CPulseCell_LimitCount.Criteria_t.md) | class | 1 | 1 |  |
| [CPulseCell_LimitCount::InstanceState_t](pulse_runtime_lib/CPulseCell_LimitCount.InstanceState_t.md) | class | 4 | 1 |  |
| [CPulseCell_Outflow_CycleOrdered](pulse_runtime_lib/CPulseCell_Outflow_CycleOrdered.md) | class | 96 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Outflow_CycleOrdered::InstanceState_t](pulse_runtime_lib/CPulseCell_Outflow_CycleOrdered.InstanceState_t.md) | class | 4 | 1 |  |
| [CPulseCell_Outflow_CycleRandom](pulse_runtime_lib/CPulseCell_Outflow_CycleRandom.md) | class | 96 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Outflow_CycleShuffled](pulse_runtime_lib/CPulseCell_Outflow_CycleShuffled.md) | class | 96 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Outflow_CycleShuffled::InstanceState_t](pulse_runtime_lib/CPulseCell_Outflow_CycleShuffled.InstanceState_t.md) | class | 40 | 2 |  |
| [CPulseCell_PickBestOutflowSelector](pulse_runtime_lib/CPulseCell_PickBestOutflowSelector.md) | class | 104 | 2 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Step_CallExternalMethod](pulse_runtime_lib/CPulseCell_Step_CallExternalMethod.md) | class | 336 | 5 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_Step_DebugLog](pulse_runtime_lib/CPulseCell_Step_DebugLog.md) | class | 72 | 0 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Step_PublicOutput](pulse_runtime_lib/CPulseCell_Step_PublicOutput.md) | class | 80 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Timeline](pulse_runtime_lib/CPulseCell_Timeline.md) | class | 320 | 3 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_Timeline::TimelineEvent_t](pulse_runtime_lib/CPulseCell_Timeline.TimelineEvent_t.md) | class | 80 | 2 |  |
| [CPulseCell_Unknown](pulse_runtime_lib/CPulseCell_Unknown.md) | class | 88 | 1 | [CPulseCell_Base](pulse_runtime_lib/CPulseCell_Base.md) |
| [CPulseCell_Value_Curve](pulse_runtime_lib/CPulseCell_Value_Curve.md) | class | 136 | 1 | [CPulseCell_BaseValue](pulse_runtime_lib/CPulseCell_BaseValue.md) |
| [CPulseCell_Value_Gradient](pulse_runtime_lib/CPulseCell_Value_Gradient.md) | class | 96 | 1 | [CPulseCell_BaseValue](pulse_runtime_lib/CPulseCell_BaseValue.md) |
| [CPulseCell_Value_RandomFloat](pulse_runtime_lib/CPulseCell_Value_RandomFloat.md) | class | 72 | 0 | [CPulseCell_BaseValue](pulse_runtime_lib/CPulseCell_BaseValue.md) |
| [CPulseCell_Value_RandomInt](pulse_runtime_lib/CPulseCell_Value_RandomInt.md) | class | 72 | 0 | [CPulseCell_BaseValue](pulse_runtime_lib/CPulseCell_BaseValue.md) |
| [CPulseCell_WaitForCursorsWithTag](pulse_runtime_lib/CPulseCell_WaitForCursorsWithTag.md) | class | 304 | 2 | [CPulseCell_WaitForCursorsWithTagBase](pulse_runtime_lib/CPulseCell_WaitForCursorsWithTagBase.md) |
| [CPulseCell_WaitForCursorsWithTagBase](pulse_runtime_lib/CPulseCell_WaitForCursorsWithTagBase.md) | class | 296 | 2 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_WaitForObservable](pulse_runtime_lib/CPulseCell_WaitForObservable.md) | class | 408 | 2 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCursorFuncs](pulse_runtime_lib/CPulseCursorFuncs.md) | class | 1 | 0 |  |
| [CPulseEnumlib](pulse_runtime_lib/CPulseEnumlib.md) | class | 1 | 0 |  |
| [CPulseExecCursor](pulse_runtime_lib/CPulseExecCursor.md) | class | 216 | 0 |  |
| [CPulseGraphDef](pulse_runtime_lib/CPulseGraphDef.md) | class | 432 | 14 |  |
| [CPulseGraphExecutionHistory](pulse_runtime_lib/CPulseGraphExecutionHistory.md) | class | 120 | 5 |  |
| [CPulseMathlib](pulse_runtime_lib/CPulseMathlib.md) | class | 1 | 0 |  |
| [CPulseRuntimeMethodArg](pulse_runtime_lib/CPulseRuntimeMethodArg.md) | class | 128 | 3 |  |
| [CPulseStringlib](pulse_runtime_lib/CPulseStringlib.md) | class | 1 | 0 |  |
| [CPulseTestScriptLib](pulse_runtime_lib/CPulseTestScriptLib.md) | class | 1 | 0 |  |
| [CPulse_BlackboardReference](pulse_runtime_lib/CPulse_BlackboardReference.md) | class | 40 | 4 |  |
| [CPulse_CallInfo](pulse_runtime_lib/CPulse_CallInfo.md) | class | 88 | 6 |  |
| [CPulse_Chunk](pulse_runtime_lib/CPulse_Chunk.md) | class | 88 | 3 |  |
| [CPulse_Constant](pulse_runtime_lib/CPulse_Constant.md) | class | 48 | 2 |  |
| [CPulse_DomainValue](pulse_runtime_lib/CPulse_DomainValue.md) | class | 48 | 3 |  |
| [CPulse_InstructionDebug](pulse_runtime_lib/CPulse_InstructionDebug.md) | class | 24 | 3 |  |
| [CPulse_InvokeBinding](pulse_runtime_lib/CPulse_InvokeBinding.md) | class | 176 | 5 |  |
| [CPulse_OutflowConnection](pulse_runtime_lib/CPulse_OutflowConnection.md) | class | 72 | 4 |  |
| [CPulse_OutputConnection](pulse_runtime_lib/CPulse_OutputConnection.md) | class | 64 | 4 |  |
| [CPulse_PublicOutput](pulse_runtime_lib/CPulse_PublicOutput.md) | class | 40 | 3 |  |
| [CPulse_RegisterInfo](pulse_runtime_lib/CPulse_RegisterInfo.md) | class | 96 | 5 |  |
| [CPulse_ResumePoint](pulse_runtime_lib/CPulse_ResumePoint.md) | class | 72 | 0 | [CPulse_OutflowConnection](pulse_runtime_lib/CPulse_OutflowConnection.md) |
| [CPulse_Variable](pulse_runtime_lib/CPulse_Variable.md) | class | 96 | 9 |  |
| [OutflowWithRequirements_t](pulse_runtime_lib/OutflowWithRequirements_t.md) | class | 128 | 4 |  |
| [PGDInstruction_t](pulse_runtime_lib/PGDInstruction_t.md) | class | 56 | 12 |  |
| [PulseCursorID_t](pulse_runtime_lib/PulseCursorID_t.md) | class | 4 | 1 |  |
| [PulseCursorYieldToken_t](pulse_runtime_lib/PulseCursorYieldToken_t.md) | class | 4 | 1 |  |
| [PulseDocNodeID_t](pulse_runtime_lib/PulseDocNodeID_t.md) | class | 4 | 1 |  |
| [PulseGraphExecutionHistoryCursorDesc_t](pulse_runtime_lib/PulseGraphExecutionHistoryCursorDesc_t.md) | class | 48 | 6 |  |
| [PulseGraphExecutionHistoryEntry_t](pulse_runtime_lib/PulseGraphExecutionHistoryEntry_t.md) | class | 32 | 5 |  |
| [PulseGraphExecutionHistoryNodeDesc_t](pulse_runtime_lib/PulseGraphExecutionHistoryNodeDesc_t.md) | class | 32 | 2 |  |
| [PulseGraphInstanceID_t](pulse_runtime_lib/PulseGraphInstanceID_t.md) | class | 4 | 1 |  |
| [PulseNodeDynamicOutflows_t](pulse_runtime_lib/PulseNodeDynamicOutflows_t.md) | class | 24 | 1 |  |
| [PulseNodeDynamicOutflows_t::DynamicOutflow_t](pulse_runtime_lib/PulseNodeDynamicOutflows_t.DynamicOutflow_t.md) | class | 80 | 2 |  |
| [PulseRegisterMap_t](pulse_runtime_lib/PulseRegisterMap_t.md) | class | 48 | 3 |  |
| [PulseRuntimeBlackboardReferenceIndex_t](pulse_runtime_lib/PulseRuntimeBlackboardReferenceIndex_t.md) | class | 2 | 1 |  |
| [PulseRuntimeCallInfoIndex_t](pulse_runtime_lib/PulseRuntimeCallInfoIndex_t.md) | class | 4 | 1 |  |
| [PulseRuntimeCellIndex_t](pulse_runtime_lib/PulseRuntimeCellIndex_t.md) | class | 4 | 1 |  |
| [PulseRuntimeChunkIndex_t](pulse_runtime_lib/PulseRuntimeChunkIndex_t.md) | class | 4 | 1 |  |
| [PulseRuntimeConstantIndex_t](pulse_runtime_lib/PulseRuntimeConstantIndex_t.md) | class | 2 | 1 |  |
| [PulseRuntimeDomainValueIndex_t](pulse_runtime_lib/PulseRuntimeDomainValueIndex_t.md) | class | 2 | 1 |  |
| [PulseRuntimeEntrypointIndex_t](pulse_runtime_lib/PulseRuntimeEntrypointIndex_t.md) | class | 4 | 1 |  |
| [PulseRuntimeInvokeIndex_t](pulse_runtime_lib/PulseRuntimeInvokeIndex_t.md) | class | 4 | 1 |  |
| [PulseRuntimeOutputIndex_t](pulse_runtime_lib/PulseRuntimeOutputIndex_t.md) | class | 4 | 1 |  |
| [PulseRuntimeRegisterIndex_t](pulse_runtime_lib/PulseRuntimeRegisterIndex_t.md) | class | 2 | 1 |  |
| [PulseRuntimeStateOffset_t](pulse_runtime_lib/PulseRuntimeStateOffset_t.md) | class | 2 | 1 |  |
| [PulseRuntimeVarIndex_t](pulse_runtime_lib/PulseRuntimeVarIndex_t.md) | class | 4 | 1 |  |
| [PulseSelectorOutflowList_t](pulse_runtime_lib/PulseSelectorOutflowList_t.md) | class | 24 | 1 |  |
| [SignatureOutflow_Continue](pulse_runtime_lib/SignatureOutflow_Continue.md) | class | 72 | 0 | [CPulse_OutflowConnection](pulse_runtime_lib/CPulse_OutflowConnection.md) |
| [SignatureOutflow_Resume](pulse_runtime_lib/SignatureOutflow_Resume.md) | class | 72 | 0 | [CPulse_ResumePoint](pulse_runtime_lib/CPulse_ResumePoint.md) |
| [EPulseGraphExecutionHistoryFlag](pulse_runtime_lib/EPulseGraphExecutionHistoryFlag.md) | enum | — | 6 |  |
| [PulseApiFeature_t](pulse_runtime_lib/PulseApiFeature_t.md) | enum | — | 6 |  |
| [PulseBestOutflowRules_t](pulse_runtime_lib/PulseBestOutflowRules_t.md) | enum | — | 2 |  |
| [PulseCursorCancelPriority_t](pulse_runtime_lib/PulseCursorCancelPriority_t.md) | enum | — | 4 |  |
| [PulseCursorWakePriority_t](pulse_runtime_lib/PulseCursorWakePriority_t.md) | enum | — | 2 |  |
| [PulseDomainValueType_t](pulse_runtime_lib/PulseDomainValueType_t.md) | enum | — | 4 |  |
| [PulseDurationStringFormat_t](pulse_runtime_lib/PulseDurationStringFormat_t.md) | enum | — | 1 |  |
| [PulseInstructionCode_t](pulse_runtime_lib/PulseInstructionCode_t.md) | enum | — | 126 |  |
| [PulseMethodCallMode_t](pulse_runtime_lib/PulseMethodCallMode_t.md) | enum | — | 2 |  |
| [PulseValueType_t](pulse_runtime_lib/PulseValueType_t.md) | enum | — | 35 |  |
| [PulseVariableKeysSource_t](pulse_runtime_lib/PulseVariableKeysSource_t.md) | enum | — | 7 |  |
