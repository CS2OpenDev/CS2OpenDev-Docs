---
title: CPulseGraphInstance_TestDomain_Derived
module: pulse_system
kind: class
---

[Schemas](../../schemas.md) / [pulse_system](../pulse_system.md) / CPulseGraphInstance_TestDomain_Derived

# CPulseGraphInstance_TestDomain_Derived

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 352 bytes (`0x160`) · **Align:** n/a (unspecified) · **Module:** pulse_system

**Inherits from:** [CPulseGraphInstance_TestDomain](../pulse_system/CPulseGraphInstance_TestDomain.md)

**Relationships:**

```mermaid
classDiagram
    CPulseGraphInstance_TestDomain <|-- CPulseGraphInstance_TestDomain_Derived
    CBasePulseGraphInstance <|-- CPulseGraphInstance_TestDomain
```

## Memory layout

10 fields (1 declared here, 9 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x128` | `m_bIsRunningUnitTests` | bool | [CPulseGraphInstance_TestDomain](../pulse_system/CPulseGraphInstance_TestDomain.md) |  |
| `0x129` | `m_bExplicitTimeStepping` | bool | [CPulseGraphInstance_TestDomain](../pulse_system/CPulseGraphInstance_TestDomain.md) |  |
| `0x12a` | `m_bExpectingToDestroyWithYieldedCursors` | bool | [CPulseGraphInstance_TestDomain](../pulse_system/CPulseGraphInstance_TestDomain.md) |  |
| `0x12b` | `m_bQuietTracepoints` | bool | [CPulseGraphInstance_TestDomain](../pulse_system/CPulseGraphInstance_TestDomain.md) |  |
| `0x12c` | `m_bExpectingCursorTerminatedDueToMaxInstructions` | bool | [CPulseGraphInstance_TestDomain](../pulse_system/CPulseGraphInstance_TestDomain.md) |  |
| `0x130` | `m_nCursorsTerminatedDueToMaxInstructions` | int32 | [CPulseGraphInstance_TestDomain](../pulse_system/CPulseGraphInstance_TestDomain.md) |  |
| `0x134` | `m_nNextValidateIndex` | int32 | [CPulseGraphInstance_TestDomain](../pulse_system/CPulseGraphInstance_TestDomain.md) |  |
| `0x138` | `m_Tracepoints` | CUtlVector< CUtlString > | [CPulseGraphInstance_TestDomain](../pulse_system/CPulseGraphInstance_TestDomain.md) |  |
| `0x150` | `m_bTestYesOrNoPath` | bool | [CPulseGraphInstance_TestDomain](../pulse_system/CPulseGraphInstance_TestDomain.md) |  |
| `0x158` | `m_nInstanceValueX` | int32 |  |  |
