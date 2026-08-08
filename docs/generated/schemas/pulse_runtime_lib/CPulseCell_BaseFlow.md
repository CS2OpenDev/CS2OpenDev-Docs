---
layout: default
title: CPulseCell_BaseFlow
nav_exclude: true
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / CPulseCell_BaseFlow

# CPulseCell_BaseFlow

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** pulse_runtime_lib

**Inherits from:** [CPulseCell_Base](../pulse_runtime_lib/CPulseCell_Base.md)

**Derived by:** [CPulseCell_BaseYieldingInflow](../pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md), [CPulseCell_ExampleSelector](../pulse_system/CPulseCell_ExampleSelector.md), [CPulseCell_Inflow_BaseEntrypoint](../pulse_runtime_lib/CPulseCell_Inflow_BaseEntrypoint.md), [CPulseCell_InlineNodeSkipSelector](../pulse_runtime_lib/CPulseCell_InlineNodeSkipSelector.md), [CPulseCell_Outflow_CycleOrdered](../pulse_runtime_lib/CPulseCell_Outflow_CycleOrdered.md), [CPulseCell_Outflow_CycleRandom](../pulse_runtime_lib/CPulseCell_Outflow_CycleRandom.md), [CPulseCell_Outflow_CycleShuffled](../pulse_runtime_lib/CPulseCell_Outflow_CycleShuffled.md), [CPulseCell_Outflow_TestExplicitYesNo](../pulse_system/CPulseCell_Outflow_TestExplicitYesNo.md), [CPulseCell_Outflow_TestRandomYesNo](../pulse_system/CPulseCell_Outflow_TestRandomYesNo.md), [CPulseCell_PickBestOutflowSelector](../pulse_runtime_lib/CPulseCell_PickBestOutflowSelector.md), [CPulseCell_SoundEventStart](../server/CPulseCell_SoundEventStart.md), [CPulseCell_Step_DebugLog](../pulse_runtime_lib/CPulseCell_Step_DebugLog.md), [CPulseCell_Step_EntFire](../client/CPulseCell_Step_EntFire.md), [CPulseCell_Step_FollowEntity](../server/CPulseCell_Step_FollowEntity.md), [CPulseCell_Step_PublicOutput](../pulse_runtime_lib/CPulseCell_Step_PublicOutput.md), [CPulseCell_Step_SetAnimGraphParam](../server/CPulseCell_Step_SetAnimGraphParam.md), [CPulseCell_Step_TestDomainCreateFakeEntity](../pulse_system/CPulseCell_Step_TestDomainCreateFakeEntity.md), [CPulseCell_Step_TestDomainDestroyFakeEntity](../pulse_system/CPulseCell_Step_TestDomainDestroyFakeEntity.md), [CPulseCell_Step_TestDomainEntFire](../pulse_system/CPulseCell_Step_TestDomainEntFire.md), [CPulseCell_Step_TestDomainTracepoint](../pulse_system/CPulseCell_Step_TestDomainTracepoint.md), [CPulseCell_Test_MultiInflow_NoDefault](../pulse_system/CPulseCell_Test_MultiInflow_NoDefault.md), [CPulseCell_Test_MultiInflow_WithDefault](../pulse_system/CPulseCell_Test_MultiInflow_WithDefault.md), [CPulseCell_Test_MultiOutflow_WithParams](../pulse_system/CPulseCell_Test_MultiOutflow_WithParams.md), [CPulseCell_Test_NoInflow](../pulse_system/CPulseCell_Test_NoInflow.md), [CSmartPropPulse_BaseQueryableFlow](../smartprops/CSmartPropPulse_BaseQueryableFlow.md), [CSmartPropPulse_CreateRotator](../smartprops/CSmartPropPulse_CreateRotator.md), [CSmartPropPulse_CreateSizer](../smartprops/CSmartPropPulse_CreateSizer.md), [CSmartPropPulse_FitOnLine](../smartprops/CSmartPropPulse_FitOnLine.md), [CSmartPropPulse_Group](../smartprops/CSmartPropPulse_Group.md), [CSmartPropPulse_PickOneSelector](../smartprops/CSmartPropPulse_PickOneSelector.md), [CSmartPropPulse_PlaceInSphere](../smartprops/CSmartPropPulse_PlaceInSphere.md), [CSmartPropPulse_SmartProp](../smartprops/CSmartPropPulse_SmartProp.md)

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_BaseFlow <|-- CPulseCell_Inflow_BaseEntrypoint
    CPulseCell_BaseFlow <|-- CPulseCell_InlineNodeSkipSelector
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleOrdered
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleRandom
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleShuffled
    CPulseCell_BaseFlow <|-- CPulseCell_PickBestOutflowSelector
    CPulseCell_BaseFlow <|-- CPulseCell_Step_DebugLog
    CPulseCell_BaseFlow <|-- CPulseCell_Step_PublicOutput
    CPulseCell_BaseFlow <|-- CSmartPropPulse_BaseQueryableFlow
    CPulseCell_BaseFlow <|-- CSmartPropPulse_CreateRotator
    CPulseCell_BaseFlow <|-- CSmartPropPulse_CreateSizer
    CPulseCell_BaseFlow <|-- CSmartPropPulse_FitOnLine
    CPulseCell_BaseFlow <|-- CSmartPropPulse_Group
    CPulseCell_BaseFlow <|-- CSmartPropPulse_PickOneSelector
    CPulseCell_BaseFlow <|-- CSmartPropPulse_PlaceInSphere
    CPulseCell_BaseFlow <|-- CSmartPropPulse_SmartProp
    CPulseCell_BaseFlow <|-- CPulseCell_Step_EntFire
    CPulseCell_BaseFlow <|-- CPulseCell_ExampleSelector
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_TestExplicitYesNo
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_TestRandomYesNo
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainCreateFakeEntity
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainDestroyFakeEntity
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainEntFire
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainTracepoint
    CPulseCell_BaseFlow <|-- CPulseCell_Test_MultiInflow_NoDefault
    CPulseCell_BaseFlow <|-- CPulseCell_Test_MultiInflow_WithDefault
    CPulseCell_BaseFlow <|-- CPulseCell_Test_MultiOutflow_WithParams
    CPulseCell_BaseFlow <|-- CPulseCell_Test_NoInflow
    CPulseCell_BaseFlow <|-- CPulseCell_SoundEventStart
    CPulseCell_BaseFlow <|-- CPulseCell_Step_FollowEntity
    CPulseCell_BaseFlow <|-- CPulseCell_Step_SetAnimGraphParam
```

## Memory layout

1 fields (0 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nEditorNodeID` | [PulseDocNodeID_t](../pulse_runtime_lib/PulseDocNodeID_t.md) | [CPulseCell_Base](../pulse_runtime_lib/CPulseCell_Base.md) | `MFgdFromSchemaCompletelySkipField` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CPulseCell_BaseFlow&quot;,
	&quot;m_nEditorNodeID&quot;: -1
}</pre>
</details>
