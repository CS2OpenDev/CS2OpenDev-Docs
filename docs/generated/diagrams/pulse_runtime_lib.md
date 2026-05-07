---
layout: default
title: "UML: pulse_runtime_lib"
parent: Schemas
nav_exclude: true
---

# UML: pulse_runtime_lib

Class relationships (inheritance and composition) for the `pulse_runtime_lib` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_IntervalTimer
    CPulseCell_BaseValue <|-- CPulseCell_Value_RandomInt
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleOrdered
    CPulseCell_BaseFlow <|-- CPulseCell_Step_DebugLog
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_BaseLerp
    CPulseCell_BaseFlow <|-- CPulseCell_Inflow_BaseEntrypoint
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_WaitForObservable
    CPulseCell_WaitForCursorsWithTagBase <|-- CPulseCell_WaitForCursorsWithTag
    CPulseCell_BaseValue <|-- CPulseCell_Value_RandomFloat
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_EntOutputHandler
    CPulse_OutflowConnection <|-- SignatureOutflow_Continue
    CPulseCell_BaseValue <|-- CPulseCell_Value_Curve
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleShuffled
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_Method
    CPulseCell_BaseState <|-- CPulseCell_BooleanSwitchState
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_ObservableVariableListener
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Step_CallExternalMethod
    CPulse_ResumePoint <|-- SignatureOutflow_Resume
    CPulseCell_BaseRequirement <|-- CPulseCell_LimitCount
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Timeline
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_EventHandler
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleRandom
    CPulse_OutflowConnection <|-- CPulse_ResumePoint
    CPulseCell_Base <|-- CPulseCell_BaseValue
    CPulseCell_BaseFlow <|-- CPulseCell_InlineNodeSkipSelector
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_FireCursors
    CPulseCell_BaseValue <|-- CPulseCell_Value_Gradient
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_BaseState
    CPulseCell_Base <|-- CPulseCell_Unknown
    CPulseCell_Base <|-- CPulseCell_BaseRequirement
    CPulseCell_WaitForCursorsWithTagBase <|-- CPulseCell_CursorQueue
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Inflow_Wait
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_GraphHook
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Inflow_Yield
    CPulseCell_BaseRequirement <|-- CPulseCell_IsRequirementValid
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_WaitForCursorsWithTagBase
    CPulseCell_BaseFlow <|-- CPulseCell_PickBestOutflowSelector
    CPulseCell_BaseFlow <|-- CPulseCell_Step_PublicOutput
    CPulseCell_IntervalTimer *-- CPulse_ResumePoint
    CPulseCell_IntervalTimer *-- SignatureOutflow_Continue
    CPulseCell_Outflow_CycleOrdered *-- CPulse_OutflowConnection
    PulseObservableBoolExpression_t *-- CPulse_OutflowConnection
    PulseObservableBoolExpression_t *-- PulseRuntimeVarIndex_t
    PulseObservableBoolExpression_t *-- PulseRuntimeBlackboardReferenceIndex_t
    CPulseCell_BaseLerp *-- CPulse_ResumePoint
    PulseSelectorOutflowList_t *-- OutflowWithRequirements_t
    CPulseCell_Inflow_BaseEntrypoint *-- PulseRuntimeChunkIndex_t
    CPulseCell_Inflow_BaseEntrypoint *-- PulseRegisterMap_t
    CPulseCell_WaitForObservable *-- PulseObservableBoolExpression_t
    CPulseCell_WaitForObservable *-- CPulse_ResumePoint
    CPulseCell_WaitForCursorsWithTag *-- PulseCursorCancelPriority_t
    CPulseGraphDef --> CPulse_Chunk
    CPulseGraphDef --> CPulseCell_Base
    CPulseGraphDef *-- CPulse_Variable
    CPulseGraphDef *-- CPulse_PublicOutput
    CPulseGraphDef --> CPulse_InvokeBinding
    CPulseGraphDef --> CPulse_CallInfo
    CPulseGraphDef *-- CPulse_Constant
    CPulseGraphDef *-- CPulse_DomainValue
    CPulseGraphDef *-- CPulse_BlackboardReference
    CPulseGraphDef --> CPulse_OutputConnection
    CPulse_CallInfo *-- PulseDocNodeID_t
    CPulse_CallInfo *-- PulseRegisterMap_t
    CPulse_CallInfo *-- PulseRuntimeChunkIndex_t
    CPulse_BlackboardReference *-- PulseDocNodeID_t
    CPulseCell_Outflow_CycleShuffled *-- CPulse_OutflowConnection
    "PulseNodeDynamicOutflows_t::DynamicOutflow_t" *-- CPulse_OutflowConnection
    CPulseCell_Inflow_Method *-- CPulseRuntimeMethodArg
    CPulse_InvokeBinding *-- PulseRegisterMap_t
    CPulse_InvokeBinding *-- PulseRuntimeCellIndex_t
    CPulse_InvokeBinding *-- PulseRuntimeChunkIndex_t
    CPulseCell_BooleanSwitchState *-- PulseObservableBoolExpression_t
    CPulseCell_BooleanSwitchState *-- CPulse_OutflowConnection
    CPulseCell_Inflow_ObservableVariableListener *-- PulseRuntimeBlackboardReferenceIndex_t
    CPulseCell_Step_CallExternalMethod *-- PulseRuntimeBlackboardReferenceIndex_t
    CPulseCell_Step_CallExternalMethod *-- CPulseRuntimeMethodArg
    CPulseCell_Step_CallExternalMethod *-- PulseMethodCallMode_t
    CPulseCell_Step_CallExternalMethod *-- CPulse_ResumePoint
    CPulseCell_Timeline *-- CPulse_ResumePoint
    CPulseCell_Outflow_CycleRandom *-- CPulse_OutflowConnection
    CPulseCell_InlineNodeSkipSelector *-- PulseDocNodeID_t
    CPulseCell_InlineNodeSkipSelector *-- PulseSelectorOutflowList_t
    CPulseCell_InlineNodeSkipSelector *-- CPulse_OutflowConnection
    CPulseCell_FireCursors *-- CPulse_OutflowConnection
    CPulseCell_FireCursors *-- CPulse_ResumePoint
    CPulseCell_Inflow_Wait *-- CPulse_ResumePoint
    CPulseCell_Inflow_Yield *-- CPulse_ResumePoint
    CPulseCell_Base *-- PulseDocNodeID_t
    CPulse_OutflowConnection *-- PulseRuntimeChunkIndex_t
    CPulse_OutflowConnection *-- PulseRegisterMap_t
    "CPulseCell_Timeline::TimelineEvent_t" *-- CPulse_OutflowConnection
    CPulseCell_WaitForCursorsWithTagBase *-- CPulse_ResumePoint
    OutflowWithRequirements_t *-- CPulse_OutflowConnection
    OutflowWithRequirements_t *-- PulseDocNodeID_t
    CPulseCell_PickBestOutflowSelector *-- PulseBestOutflowRules_t
    CPulseCell_PickBestOutflowSelector *-- PulseSelectorOutflowList_t
    CPulseCell_Step_PublicOutput *-- PulseRuntimeOutputIndex_t
    CPulse_InstructionDebug *-- PulseDocNodeID_t
    CPulse_RegisterInfo *-- PulseRuntimeRegisterIndex_t
    CPulse_DomainValue *-- PulseDomainValueType_t
    CPulse_Variable *-- PulseVariableKeysSource_t
    CPulse_Variable *-- PulseDocNodeID_t
    PGDInstruction_t *-- PulseInstructionCode_t
    PGDInstruction_t *-- PulseRuntimeVarIndex_t
    PGDInstruction_t *-- PulseRuntimeRegisterIndex_t
    PGDInstruction_t *-- PulseRuntimeInvokeIndex_t
    PGDInstruction_t *-- PulseRuntimeChunkIndex_t
    PGDInstruction_t *-- PulseRuntimeCallInfoIndex_t
    PGDInstruction_t *-- PulseRuntimeConstantIndex_t
    PGDInstruction_t *-- PulseRuntimeDomainValueIndex_t
    PGDInstruction_t *-- PulseRuntimeBlackboardReferenceIndex_t
    CPulseGraphExecutionHistory *-- PulseGraphInstanceID_t
    CPulseGraphExecutionHistory --> PulseGraphExecutionHistoryEntry_t
    CPulseGraphExecutionHistory --> PulseDocNodeID_t
    CPulseGraphExecutionHistory --> PulseGraphExecutionHistoryNodeDesc_t
    CPulseGraphExecutionHistory --> PulseCursorID_t
    CPulseGraphExecutionHistory --> PulseGraphExecutionHistoryCursorDesc_t
    PulseGraphExecutionHistoryEntry_t *-- PulseCursorID_t
    PulseGraphExecutionHistoryEntry_t *-- PulseDocNodeID_t
    CPulse_PublicOutput *-- CPulseRuntimeMethodArg
    PulseGraphExecutionHistoryCursorDesc_t *-- PulseCursorID_t
    PulseGraphExecutionHistoryCursorDesc_t *-- PulseDocNodeID_t
    CPulse_Chunk *-- PGDInstruction_t
    CPulse_Chunk *-- CPulse_RegisterInfo
    CPulse_Chunk *-- CPulse_InstructionDebug
```
