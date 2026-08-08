---
layout: default
title: pulse_system
parent: Schemas
nav_exclude: true
---

# Module: pulse_system

[📊 View UML Diagram](../diagrams/pulse_system.md)

42 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CPulseCell_ExampleCriteria](pulse_system/CPulseCell_ExampleCriteria.md) | class | 72 | 0 | [CPulseCell_BaseRequirement](pulse_runtime_lib/CPulseCell_BaseRequirement.md) |
| [CPulseCell_ExampleCriteria::Criteria_t](pulse_system/CPulseCell_ExampleCriteria.Criteria_t.md) | class | 12 | 3 |  |
| [CPulseCell_ExampleSelector](pulse_system/CPulseCell_ExampleSelector.md) | class | 96 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Outflow_TestExplicitYesNo](pulse_system/CPulseCell_Outflow_TestExplicitYesNo.md) | class | 216 | 2 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Outflow_TestRandomYesNo](pulse_system/CPulseCell_Outflow_TestRandomYesNo.md) | class | 216 | 2 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Step_TestDomainCreateFakeEntity](pulse_system/CPulseCell_Step_TestDomainCreateFakeEntity.md) | class | 72 | 0 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Step_TestDomainDestroyFakeEntity](pulse_system/CPulseCell_Step_TestDomainDestroyFakeEntity.md) | class | 72 | 0 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Step_TestDomainEntFire](pulse_system/CPulseCell_Step_TestDomainEntFire.md) | class | 80 | 1 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Step_TestDomainTracepoint](pulse_system/CPulseCell_Step_TestDomainTracepoint.md) | class | 72 | 0 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_TestEnums](pulse_system/CPulseCell_TestEnums.md) | class | 80 | 2 | [CPulseCell_BaseValue](pulse_runtime_lib/CPulseCell_BaseValue.md) |
| [CPulseCell_TestWaitWithAutoTracepoints](pulse_system/CPulseCell_TestWaitWithAutoTracepoints.md) | class | 296 | 2 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_TestWaitWithCursorState](pulse_system/CPulseCell_TestWaitWithCursorState.md) | class | 360 | 2 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_TestWaitWithCursorState::CursorState_t](pulse_system/CPulseCell_TestWaitWithCursorState.CursorState_t.md) | class | 36 | 5 |  |
| [CPulseCell_TestWaitWithCursorState::InstanceState_t](pulse_system/CPulseCell_TestWaitWithCursorState.InstanceState_t.md) | class | 4 | 1 |  |
| [CPulseCell_TestYieldForever](pulse_system/CPulseCell_TestYieldForever.md) | class | 216 | 0 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_TestYieldWithObservables](pulse_system/CPulseCell_TestYieldWithObservables.md) | class | 544 | 5 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_Test_MultiInflow_NoDefault](pulse_system/CPulseCell_Test_MultiInflow_NoDefault.md) | class | 72 | 0 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Test_MultiInflow_WithDefault](pulse_system/CPulseCell_Test_MultiInflow_WithDefault.md) | class | 72 | 0 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Test_MultiOutflow_WithParams](pulse_system/CPulseCell_Test_MultiOutflow_WithParams.md) | class | 216 | 2 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Test_MultiOutflow_WithParams_Yielding](pulse_system/CPulseCell_Test_MultiOutflow_WithParams_Yielding.md) | class | 576 | 5 | [CPulseCell_BaseYieldingInflow](pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) |
| [CPulseCell_Test_MultiOutflow_WithParams_Yielding::CursorState_t](pulse_system/CPulseCell_Test_MultiOutflow_WithParams_Yielding.CursorState_t.md) | class | 4 | 1 |  |
| [CPulseCell_Test_NoInflow](pulse_system/CPulseCell_Test_NoInflow.md) | class | 72 | 0 | [CPulseCell_BaseFlow](pulse_runtime_lib/CPulseCell_BaseFlow.md) |
| [CPulseCell_Val_TestDomainFindEntityByName](pulse_system/CPulseCell_Val_TestDomainFindEntityByName.md) | class | 72 | 0 | [CPulseCell_BaseValue](pulse_runtime_lib/CPulseCell_BaseValue.md) |
| [CPulseCell_Val_TestDomainGetEntityName](pulse_system/CPulseCell_Val_TestDomainGetEntityName.md) | class | 72 | 0 | [CPulseCell_BaseValue](pulse_runtime_lib/CPulseCell_BaseValue.md) |
| [CPulseCell_Value_TestValue50](pulse_system/CPulseCell_Value_TestValue50.md) | class | 72 | 0 | [CPulseCell_BaseValue](pulse_runtime_lib/CPulseCell_BaseValue.md) |
| [CPulseGraphInstance_TestDomain](pulse_system/CPulseGraphInstance_TestDomain.md) | class | 344 | 9 | [CBasePulseGraphInstance](pulse_runtime_lib/CBasePulseGraphInstance.md) |
| [CPulseGraphInstance_TestDomain_Derived](pulse_system/CPulseGraphInstance_TestDomain_Derived.md) | class | 352 | 1 | [CPulseGraphInstance_TestDomain](pulse_system/CPulseGraphInstance_TestDomain.md) |
| [CPulseGraphInstance_TestDomain_FakeEntityOwner](pulse_system/CPulseGraphInstance_TestDomain_FakeEntityOwner.md) | class | 272 | 0 | [CBasePulseGraphInstance](pulse_runtime_lib/CBasePulseGraphInstance.md) |
| [CPulseGraphInstance_TestDomain_UseReadOnlyBlackboardView](pulse_system/CPulseGraphInstance_TestDomain_UseReadOnlyBlackboardView.md) | class | 344 | 0 | [CPulseGraphInstance_TestDomain](pulse_system/CPulseGraphInstance_TestDomain.md) |
| [CPulseGraphInstance_TurtleGraphics](pulse_system/CPulseGraphInstance_TurtleGraphics.md) | class | 312 | 0 | [CBasePulseGraphInstance](pulse_runtime_lib/CBasePulseGraphInstance.md) |
| [CPulseTestFuncs_LibraryA](pulse_system/CPulseTestFuncs_LibraryA.md) | class | 1 | 0 |  |
| [CPulseTurtleGraphicsCursor](pulse_system/CPulseTurtleGraphicsCursor.md) | class | 240 | 4 | [CPulseExecCursor](pulse_runtime_lib/CPulseExecCursor.md) |
| [CTestDomainDerived_Cursor](pulse_system/CTestDomainDerived_Cursor.md) | class | 224 | 2 | [CPulseExecCursor](pulse_runtime_lib/CPulseExecCursor.md) |
| [FakeEntityDerivedA_tAPI](pulse_system/FakeEntityDerivedA_tAPI.md) | class | 8 | 0 |  |
| [FakeEntityDerivedB_tAPI](pulse_system/FakeEntityDerivedB_tAPI.md) | class | 8 | 0 |  |
| [FakeEntity_tAPI](pulse_system/FakeEntity_tAPI.md) | class | 8 | 0 |  |
| [TestComponent_t](pulse_system/TestComponent_t.md) | class | 16 | 1 |  |
| [TestComponent_tAPI](pulse_system/TestComponent_tAPI.md) | class | 8 | 0 |  |
| [PulseTestEnumColor_t](pulse_system/PulseTestEnumColor_t.md) | enum | — | 5 |  |
| [PulseTestEnumFlagsAlt_t](pulse_system/PulseTestEnumFlagsAlt_t.md) | enum | — | 2 |  |
| [PulseTestEnumFlags_t](pulse_system/PulseTestEnumFlags_t.md) | enum | — | 4 |  |
| [PulseTestEnumShape_t](pulse_system/PulseTestEnumShape_t.md) | enum | — | 3 |  |
