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
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_BaseLerp
    CPulseCell_Base <|-- CPulseCell_BaseRequirement
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_BaseState
    CPulseCell_Base <|-- CPulseCell_BaseValue
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_BaseState <|-- CPulseCell_BooleanSwitchState
    CPulseCell_WaitForCursorsWithTagBase <|-- CPulseCell_CursorQueue
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_FireCursors
    CPulseCell_BaseFlow <|-- CPulseCell_Inflow_BaseEntrypoint
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_EntOutputHandler
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_EventHandler
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_GraphHook
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_Method
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_ObservableVariableListener
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Inflow_Wait
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Inflow_Yield
    CPulseCell_BaseFlow <|-- CPulseCell_InlineNodeSkipSelector
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_IntervalTimer
    CPulseCell_BaseRequirement <|-- CPulseCell_IsRequirementValid
    CPulseCell_BaseRequirement <|-- CPulseCell_LimitCount
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleOrdered
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleRandom
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleShuffled
    CPulseCell_BaseFlow <|-- CPulseCell_PickBestOutflowSelector
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Step_CallExternalMethod
    CPulseCell_BaseFlow <|-- CPulseCell_Step_DebugLog
    CPulseCell_BaseFlow <|-- CPulseCell_Step_PublicOutput
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Timeline
    CPulseCell_Base <|-- CPulseCell_Unknown
    CPulseCell_BaseValue <|-- CPulseCell_Value_Curve
    CPulseCell_BaseValue <|-- CPulseCell_Value_Gradient
    CPulseCell_BaseValue <|-- CPulseCell_Value_RandomFloat
    CPulseCell_BaseValue <|-- CPulseCell_Value_RandomInt
    CPulseCell_WaitForCursorsWithTagBase <|-- CPulseCell_WaitForCursorsWithTag
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_WaitForCursorsWithTagBase
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_WaitForObservable
    CPulse_OutflowConnection <|-- CPulse_ResumePoint
    CPulse_OutflowConnection <|-- SignatureOutflow_Continue
    CPulse_ResumePoint <|-- SignatureOutflow_Resume
    CPulseCell_BaseLerp *-- CPulse_ResumePoint
    CPulseCell_BaseYieldingInflow *-- CPulse_ResumePoint
    CPulseCell_BooleanSwitchState *-- CPulse_OutflowConnection
    CPulseCell_FireCursors *-- CPulse_OutflowConnection
    CPulseCell_FireCursors *-- CPulse_ResumePoint
    CPulseCell_Inflow_Wait *-- CPulse_ResumePoint
    CPulseCell_Inflow_Yield *-- CPulse_ResumePoint
    CPulseCell_InlineNodeSkipSelector *-- PulseSelectorOutflowList_t
    CPulseCell_InlineNodeSkipSelector *-- CPulse_OutflowConnection
    CPulseCell_IntervalTimer *-- CPulse_ResumePoint
    CPulseCell_IntervalTimer *-- SignatureOutflow_Continue
    CPulseCell_Outflow_CycleOrdered *-- CPulse_OutflowConnection
    CPulseCell_Outflow_CycleRandom *-- CPulse_OutflowConnection
    CPulseCell_Outflow_CycleShuffled *-- CPulse_OutflowConnection
    CPulseCell_PickBestOutflowSelector *-- PulseSelectorOutflowList_t
    CPulseCell_Step_CallExternalMethod *-- CPulse_ResumePoint
    CPulseCell_Timeline *-- CPulse_ResumePoint
    "CPulseCell_Timeline::TimelineEvent_t" *-- CPulse_OutflowConnection
    CPulseCell_WaitForCursorsWithTagBase *-- CPulse_ResumePoint
    CPulseCell_WaitForObservable *-- CPulse_ResumePoint
    CPulseGraphDef --> CPulseCell_Base
    CPulseGraphDef --> CPulse_InvokeBinding
    CPulseGraphDef --> CPulse_CallInfo
    CPulseGraphDef *-- CPulse_BlackboardReference
    OutflowWithRequirements_t *-- CPulse_OutflowConnection
    "PulseNodeDynamicOutflows_t::DynamicOutflow_t" *-- CPulse_OutflowConnection
    PulseSelectorOutflowList_t *-- OutflowWithRequirements_t
```
