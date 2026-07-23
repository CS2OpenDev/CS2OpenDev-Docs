---
layout: default
title: pulse_system
parent: Schemas
nav_exclude: true
---

# Module: pulse_system

[📊 View UML Diagram](../diagrams/pulse_system.md)

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [CPulseCell_ExampleCriteria](#cpulsecell_examplecriteria) | class | CPulseCell_BaseRequirement | 0 |
| [CPulseCell_ExampleCriteria::Criteria_t](#cpulsecell_examplecriteriacriteria_t) | class |  | 3 |
| [CPulseCell_ExampleSelector](#cpulsecell_exampleselector) | class | CPulseCell_BaseFlow | 1 |
| [CPulseCell_Outflow_TestExplicitYesNo](#cpulsecell_outflow_testexplicityesno) | class | CPulseCell_BaseFlow | 2 |
| [CPulseCell_Outflow_TestRandomYesNo](#cpulsecell_outflow_testrandomyesno) | class | CPulseCell_BaseFlow | 2 |
| [CPulseCell_Step_TestDomainCreateFakeEntity](#cpulsecell_step_testdomaincreatefakeentity) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_Step_TestDomainDestroyFakeEntity](#cpulsecell_step_testdomaindestroyfakeentity) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_Step_TestDomainEntFire](#cpulsecell_step_testdomainentfire) | class | CPulseCell_BaseFlow | 1 |
| [CPulseCell_Step_TestDomainTracepoint](#cpulsecell_step_testdomaintracepoint) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_TestEnums](#cpulsecell_testenums) | class | CPulseCell_BaseValue | 2 |
| [CPulseCell_TestWaitWithAutoTracepoints](#cpulsecell_testwaitwithautotracepoints) | class | CPulseCell_BaseYieldingInflow | 2 |
| [CPulseCell_TestWaitWithCursorState](#cpulsecell_testwaitwithcursorstate) | class | CPulseCell_BaseYieldingInflow | 2 |
| [CPulseCell_TestWaitWithCursorState::CursorState_t](#cpulsecell_testwaitwithcursorstatecursorstate_t) | class |  | 5 |
| [CPulseCell_TestWaitWithCursorState::InstanceState_t](#cpulsecell_testwaitwithcursorstateinstancestate_t) | class |  | 1 |
| [CPulseCell_TestYieldForever](#cpulsecell_testyieldforever) | class | CPulseCell_BaseYieldingInflow | 0 |
| [CPulseCell_TestYieldWithObservables](#cpulsecell_testyieldwithobservables) | class | CPulseCell_BaseYieldingInflow | 5 |
| [CPulseCell_Test_MultiInflow_NoDefault](#cpulsecell_test_multiinflow_nodefault) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_Test_MultiInflow_WithDefault](#cpulsecell_test_multiinflow_withdefault) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_Test_MultiOutflow_WithParams](#cpulsecell_test_multioutflow_withparams) | class | CPulseCell_BaseFlow | 2 |
| [CPulseCell_Test_MultiOutflow_WithParams_Yielding](#cpulsecell_test_multioutflow_withparams_yielding) | class | CPulseCell_BaseYieldingInflow | 5 |
| [CPulseCell_Test_MultiOutflow_WithParams_Yielding::CursorState_t](#cpulsecell_test_multioutflow_withparams_yieldingcursorstate_t) | class |  | 1 |
| [CPulseCell_Test_NoInflow](#cpulsecell_test_noinflow) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_Val_TestDomainFindEntityByName](#cpulsecell_val_testdomainfindentitybyname) | class | CPulseCell_BaseValue | 0 |
| [CPulseCell_Val_TestDomainGetEntityName](#cpulsecell_val_testdomaingetentityname) | class | CPulseCell_BaseValue | 0 |
| [CPulseCell_Value_TestValue50](#cpulsecell_value_testvalue50) | class | CPulseCell_BaseValue | 0 |
| [CPulseGraphInstance_TestDomain](#cpulsegraphinstance_testdomain) | class | CBasePulseGraphInstance | 9 |
| [CPulseGraphInstance_TestDomain_Derived](#cpulsegraphinstance_testdomain_derived) | class | CPulseGraphInstance_TestDomain | 1 |
| [CPulseGraphInstance_TestDomain_FakeEntityOwner](#cpulsegraphinstance_testdomain_fakeentityowner) | class | CBasePulseGraphInstance | 0 |
| [CPulseGraphInstance_TestDomain_UseReadOnlyBlackboardView](#cpulsegraphinstance_testdomain_usereadonlyblackboardview) | class | CPulseGraphInstance_TestDomain | 0 |
| [CPulseGraphInstance_TurtleGraphics](#cpulsegraphinstance_turtlegraphics) | class | CBasePulseGraphInstance | 0 |
| [CPulseTestFuncs_LibraryA](#cpulsetestfuncs_librarya) | class |  | 0 |
| [CPulseTurtleGraphicsCursor](#cpulseturtlegraphicscursor) | class | CPulseExecCursor | 4 |
| [CTestDomainDerived_Cursor](#ctestdomainderived_cursor) | class | CPulseExecCursor | 2 |
| [FakeEntityDerivedA_tAPI](#fakeentityderiveda_tapi) | class |  | 0 |
| [FakeEntityDerivedB_tAPI](#fakeentityderivedb_tapi) | class |  | 0 |
| [FakeEntity_tAPI](#fakeentity_tapi) | class |  | 0 |
| [PulseTestEnumColor_t](#pulsetestenumcolor_t) | enum |  | 5 |
| [PulseTestEnumFlagsAlt_t](#pulsetestenumflagsalt_t) | enum |  | 2 |
| [PulseTestEnumFlags_t](#pulsetestenumflags_t) | enum |  | 4 |
| [PulseTestEnumShape_t](#pulsetestenumshape_t) | enum |  | 3 |
| [TestComponent_t](#testcomponent_t) | class |  | 1 |
| [TestComponent_tAPI](#testcomponent_tapi) | class |  | 0 |

---

### CPulseCell_ExampleCriteria

**Inherits from:** [CPulseCell_BaseRequirement](pulse_runtime_lib.md#cpulsecell_baserequirement)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyDescription An example of requirement data with ports`, `MPropertyFriendlyName Example Criteria`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseRequirement <|-- CPulseCell_ExampleCriteria
    CPulseCell_Base <|-- CPulseCell_BaseRequirement
```

### CPulseCell_ExampleCriteria::Criteria_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flFloatValue1` | float32 |  |
| `m_flFloatValue2` | float32 |  |
| `m_bMyBool` | bool |  |

### CPulseCell_ExampleSelector

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyDescription Evaluate the requirements of each connected node`, `MPropertyFriendlyName Select Example Criteria`, `MPulseEditorCanvasItemSpecKV3`, `MPulseEditorHeaderIcon`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_ExampleSelector
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_ExampleSelector *-- PulseSelectorOutflowList_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_OutflowList` | [PulseSelectorOutflowList_t](../schemas/pulse_runtime_lib.md#pulseselectoroutflowlist_t) |  |

### CPulseCell_Outflow_TestExplicitYesNo

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyDescription Test node that picks between two outflows as specified in the test domain.`, `MPropertyFriendlyName [Test] Explicit Yes/No Outflow`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_TestExplicitYesNo
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_Outflow_TestExplicitYesNo *-- CPulse_OutflowConnection
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Yes` | [CPulse_OutflowConnection](../schemas/pulse_runtime_lib.md#cpulse_outflowconnection) | `MPropertyFriendlyName Yes` |
| `m_No` | [CPulse_OutflowConnection](../schemas/pulse_runtime_lib.md#cpulse_outflowconnection) | `MPropertyFriendlyName No` |

### CPulseCell_Outflow_TestRandomYesNo

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyDescription Test node that randomly picks between two outflows.`, `MPropertyFriendlyName [Test] Random Yes/No Outflow`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_TestRandomYesNo
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_Outflow_TestRandomYesNo *-- CPulse_OutflowConnection
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Yes` | [CPulse_OutflowConnection](../schemas/pulse_runtime_lib.md#cpulse_outflowconnection) | `MPropertyDescription Randomly taken half of the time` `MPropertyFriendlyName Yes` |
| `m_No` | [CPulse_OutflowConnection](../schemas/pulse_runtime_lib.md#cpulse_outflowconnection) | `MPropertyDescription Randomly taken half of the time` `MPropertyFriendlyName No` |

### CPulseCell_Step_TestDomainCreateFakeEntity

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyFriendlyName Spawn Fake Entity`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainCreateFakeEntity
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Step_TestDomainDestroyFakeEntity

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyFriendlyName Destroy Fake Entity`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainDestroyFakeEntity
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Step_TestDomainEntFire

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyFriendlyName Fake Ent-Fire`, `MPulseEditorHeaderText`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainEntFire
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Input` | CUtlString |  |

### CPulseCell_Step_TestDomainTracepoint

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyFriendlyName Tracepoint`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainTracepoint
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_TestEnums

**Inherits from:** [CPulseCell_BaseValue](pulse_runtime_lib.md#cpulsecell_basevalue)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyFriendlyName Test Enums`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseValue <|-- CPulseCell_TestEnums
    CPulseCell_Base <|-- CPulseCell_BaseValue
    CPulseCell_TestEnums *-- PulseTestEnumColor_t
    CPulseCell_TestEnums *-- PulseTestEnumFlags_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nReferenceColor` | [PulseTestEnumColor_t](../schemas/pulse_system.md#pulsetestenumcolor_t) |  |
| `m_nReferenceFlags` | [PulseTestEnumFlags_t](../schemas/pulse_system.md#pulsetestenumflags_t) |  |

### CPulseCell_TestWaitWithAutoTracepoints

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyFriendlyName Wait and Trace`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_TestWaitWithAutoTracepoints
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_TestWaitWithAutoTracepoints *-- CPulse_ResumePoint
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_TracePrefix` | CUtlString |  |
| `m_WakeResume` | [CPulse_ResumePoint](../schemas/pulse_runtime_lib.md#cpulse_resumepoint) |  |

### CPulseCell_TestWaitWithCursorState

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_TestWaitWithCursorState
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_TestWaitWithCursorState *-- CPulse_ResumePoint
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_WakeResume` | [CPulse_ResumePoint](../schemas/pulse_runtime_lib.md#cpulse_resumepoint) |  |
| `m_WakeFail` | [CPulse_ResumePoint](../schemas/pulse_runtime_lib.md#cpulse_resumepoint) |  |

### CPulseCell_TestWaitWithCursorState::CursorState_t

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    "CPulseCell_TestWaitWithCursorState::CursorState_t" *-- CPulseCell_TestWaitWithCursorState
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `flWaitValue` | float32 |  |
| `bFail` | bool |  |
| `m_hSelfCursor` | HYieldedCursor |  |
| `m_hSelfCellInstanceUntyped` | HPulseCellBase |  |
| `m_hSelfCellInstance` | HPulseCell< [CPulseCell_TestWaitWithCursorState](../schemas/pulse_system.md#cpulsecell_testwaitwithcursorstate) > |  |

### CPulseCell_TestWaitWithCursorState::InstanceState_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nDummy` | int32 |  |

### CPulseCell_TestYieldForever

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_TestYieldForever
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_TestYieldWithObservables

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_TestYieldWithObservables
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_TestYieldWithObservables *-- CPulse_ResumePoint
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flWatchForFloatValue` | float32 |  |
| `m_LiveFloatValue` | CPulseObservableExpression< float32 > |  |
| `m_WatchForStringValue` | CUtlString |  |
| `m_LiveStringValue` | CPulseObservableExpression< CUtlString > |  |
| `m_WakeResume` | [CPulse_ResumePoint](../schemas/pulse_runtime_lib.md#cpulse_resumepoint) |  |

### CPulseCell_Test_MultiInflow_NoDefault

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Test_MultiInflow_NoDefault
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Test_MultiInflow_WithDefault

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Test_MultiInflow_WithDefault
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Test_MultiOutflow_WithParams

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Test_MultiOutflow_WithParams
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_Test_MultiOutflow_WithParams *-- SignatureOutflow_Continue
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Out1` | [SignatureOutflow_Continue](../schemas/pulse_runtime_lib.md#signatureoutflow_continue) |  |
| `m_Out2` | [SignatureOutflow_Continue](../schemas/pulse_runtime_lib.md#signatureoutflow_continue) |  |

### CPulseCell_Test_MultiOutflow_WithParams_Yielding

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Test_MultiOutflow_WithParams_Yielding
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_Test_MultiOutflow_WithParams_Yielding *-- SignatureOutflow_Continue
    CPulseCell_Test_MultiOutflow_WithParams_Yielding *-- SignatureOutflow_Resume
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Out1` | [SignatureOutflow_Continue](../schemas/pulse_runtime_lib.md#signatureoutflow_continue) |  |
| `m_AsyncChild1` | [SignatureOutflow_Continue](../schemas/pulse_runtime_lib.md#signatureoutflow_continue) |  |
| `m_AsyncChild2` | [SignatureOutflow_Continue](../schemas/pulse_runtime_lib.md#signatureoutflow_continue) |  |
| `m_YieldResume1` | [SignatureOutflow_Resume](../schemas/pulse_runtime_lib.md#signatureoutflow_resume) |  |
| `m_YieldResume2` | [SignatureOutflow_Resume](../schemas/pulse_runtime_lib.md#signatureoutflow_resume) |  |

### CPulseCell_Test_MultiOutflow_WithParams_Yielding::CursorState_t

**Metadata:** `MGetKV3ClassDefaults`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `nTestStep` | int32 |  |

### CPulseCell_Test_NoInflow

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Test_NoInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Val_TestDomainFindEntityByName

**Inherits from:** [CPulseCell_BaseValue](pulse_runtime_lib.md#cpulsecell_basevalue)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyFriendlyName Find Fake Entity`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseValue <|-- CPulseCell_Val_TestDomainFindEntityByName
    CPulseCell_Base <|-- CPulseCell_BaseValue
```

### CPulseCell_Val_TestDomainGetEntityName

**Inherits from:** [CPulseCell_BaseValue](pulse_runtime_lib.md#cpulsecell_basevalue)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyFriendlyName Get Fake Entity Name`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseValue <|-- CPulseCell_Val_TestDomainGetEntityName
    CPulseCell_Base <|-- CPulseCell_BaseValue
```

### CPulseCell_Value_TestValue50

**Inherits from:** [CPulseCell_BaseValue](pulse_runtime_lib.md#cpulsecell_basevalue)

**Metadata:** `MGetKV3ClassDefaults`, `MPropertyDescription Test node that just generates the integer 50. Nothing to see here!`, `MPropertyFriendlyName [Test] Int Value 50`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseValue <|-- CPulseCell_Value_TestValue50
    CPulseCell_Base <|-- CPulseCell_BaseValue
```

### CPulseGraphInstance_TestDomain

**Inherits from:** [CBasePulseGraphInstance](pulse_runtime_lib.md#cbasepulsegraphinstance)

**Derived by:** [CPulseGraphInstance_TestDomain_Derived](pulse_system.md#cpulsegraphinstance_testdomain_derived), [CPulseGraphInstance_TestDomain_UseReadOnlyBlackboardView](pulse_system.md#cpulsegraphinstance_testdomain_usereadonlyblackboardview)

**Relationships:**

```mermaid
classDiagram
    CBasePulseGraphInstance <|-- CPulseGraphInstance_TestDomain
    CPulseGraphInstance_TestDomain <|-- CPulseGraphInstance_TestDomain_Derived
    CPulseGraphInstance_TestDomain <|-- CPulseGraphInstance_TestDomain_UseReadOnlyBlackboardView
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bIsRunningUnitTests` | bool |  |
| `m_bExplicitTimeStepping` | bool |  |
| `m_bExpectingToDestroyWithYieldedCursors` | bool |  |
| `m_bQuietTracepoints` | bool |  |
| `m_bExpectingCursorTerminatedDueToMaxInstructions` | bool |  |
| `m_nCursorsTerminatedDueToMaxInstructions` | int32 |  |
| `m_nNextValidateIndex` | int32 |  |
| `m_Tracepoints` | CUtlVector< CUtlString > |  |
| `m_bTestYesOrNoPath` | bool |  |

### CPulseGraphInstance_TestDomain_Derived

**Inherits from:** [CPulseGraphInstance_TestDomain](pulse_system.md#cpulsegraphinstance_testdomain)

**Relationships:**

```mermaid
classDiagram
    CPulseGraphInstance_TestDomain <|-- CPulseGraphInstance_TestDomain_Derived
    CBasePulseGraphInstance <|-- CPulseGraphInstance_TestDomain
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInstanceValueX` | int32 |  |

### CPulseGraphInstance_TestDomain_FakeEntityOwner

**Inherits from:** [CBasePulseGraphInstance](pulse_runtime_lib.md#cbasepulsegraphinstance)

**Relationships:**

```mermaid
classDiagram
    CBasePulseGraphInstance <|-- CPulseGraphInstance_TestDomain_FakeEntityOwner
```

### CPulseGraphInstance_TestDomain_UseReadOnlyBlackboardView

**Inherits from:** [CPulseGraphInstance_TestDomain](pulse_system.md#cpulsegraphinstance_testdomain)

**Relationships:**

```mermaid
classDiagram
    CPulseGraphInstance_TestDomain <|-- CPulseGraphInstance_TestDomain_UseReadOnlyBlackboardView
    CBasePulseGraphInstance <|-- CPulseGraphInstance_TestDomain
```

### CPulseGraphInstance_TurtleGraphics

**Inherits from:** [CBasePulseGraphInstance](pulse_runtime_lib.md#cbasepulsegraphinstance)

**Relationships:**

```mermaid
classDiagram
    CBasePulseGraphInstance <|-- CPulseGraphInstance_TurtleGraphics
```

### CPulseTestFuncs_LibraryA

**Metadata:** `MPropertyDescription Library for interacting with a few global test values.`

### CPulseTurtleGraphicsCursor

**Inherits from:** [CPulseExecCursor](pulse_runtime_lib.md#cpulseexeccursor)

**Relationships:**

```mermaid
classDiagram
    CPulseExecCursor <|-- CPulseTurtleGraphicsCursor
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Color` | Color |  |
| `m_vPos` | Vector2D |  |
| `m_flHeadingDeg` | float32 |  |
| `m_bPenUp` | bool |  |

### CTestDomainDerived_Cursor

**Inherits from:** [CPulseExecCursor](pulse_runtime_lib.md#cpulseexeccursor)

**Relationships:**

```mermaid
classDiagram
    CPulseExecCursor <|-- CTestDomainDerived_Cursor
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nCursorValueA` | int32 |  |
| `m_nCursorValueB` | int32 |  |

### FakeEntityDerivedA_tAPI

### FakeEntityDerivedB_tAPI

### FakeEntity_tAPI

### PulseTestEnumColor_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `BLACK` | 0 | Black |
| `WHITE` | 1 | White |
| `RED` | 2 | Red |
| `GREEN` | 3 | Green |
| `BLUE` | 4 | Blue |

### PulseTestEnumFlagsAlt_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `NONE` | 0 |  |
| `FIRST` | 1 |  |

### PulseTestEnumFlags_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `NONE` | 0 | None |
| `FIRST` | 1 | First |
| `SECOND` | 2 | Second |
| `THIRD` | 4 | Third |

### PulseTestEnumShape_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `CIRCLE` | 100 | Circle |
| `SQUARE` | 200 | Square |
| `TRIANGLE` | 300 | Triangle |

### TestComponent_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_ComponentData` | CUtlString |  |

### TestComponent_tAPI
