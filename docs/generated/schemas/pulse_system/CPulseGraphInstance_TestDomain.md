---
title: CPulseGraphInstance_TestDomain
module: pulse_system
kind: class
---

[Schemas](../../schemas.md) / [pulse_system](../pulse_system.md) / CPulseGraphInstance_TestDomain

# CPulseGraphInstance_TestDomain

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 208 bytes (`0xd0`) · **Align:** n/a (unspecified) · **Module:** pulse_system

**Inherits from:** [CBasePulseGraphInstance](../pulse_runtime_lib/CBasePulseGraphInstance.md)

**Derived by:** [CPulseGraphInstance_TestDomain_Derived](../pulse_system/CPulseGraphInstance_TestDomain_Derived.md), [CPulseGraphInstance_TestDomain_UseReadOnlyBlackboardView](../pulse_system/CPulseGraphInstance_TestDomain_UseReadOnlyBlackboardView.md)

**Relationships:**

```mermaid
classDiagram
    CBasePulseGraphInstance <|-- CPulseGraphInstance_TestDomain
    CPulseGraphInstance_TestDomain <|-- CPulseGraphInstance_TestDomain_Derived
    CPulseGraphInstance_TestDomain <|-- CPulseGraphInstance_TestDomain_UseReadOnlyBlackboardView
```

## Memory layout

9 fields (9 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0xa0` | `m_bIsRunningUnitTests` | bool |  |  |
| `0xa1` | `m_bExplicitTimeStepping` | bool |  |  |
| `0xa2` | `m_bExpectingToDestroyWithYieldedCursors` | bool |  |  |
| `0xa3` | `m_bQuietTracepoints` | bool |  |  |
| `0xa4` | `m_bExpectingCursorTerminatedDueToMaxInstructions` | bool |  |  |
| `0xa8` | `m_nCursorsTerminatedDueToMaxInstructions` | int32 |  |  |
| `0xac` | `m_nNextValidateIndex` | int32 |  |  |
| `0xb0` | `m_Tracepoints` | CUtlVector< CUtlString > |  |  |
| `0xc8` | `m_bTestYesOrNoPath` | bool |  |  |
