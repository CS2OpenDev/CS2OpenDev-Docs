---
layout: default
title: SignatureOutflow_Resume
nav_exclude: true
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / SignatureOutflow_Resume

# SignatureOutflow_Resume

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 255 · **Module:** pulse_runtime_lib

**Inherits from:** [CPulse_ResumePoint](../pulse_runtime_lib/CPulse_ResumePoint.md)

**Relationships:**

```mermaid
classDiagram
    CPulse_ResumePoint <|-- SignatureOutflow_Resume
    CPulse_OutflowConnection <|-- CPulse_ResumePoint
```

## Memory layout

4 fields (0 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_SourceOutflowName` | PulseSymbol_t | [CPulse_OutflowConnection](../pulse_runtime_lib/CPulse_OutflowConnection.md) |  |
| `0x10` | `m_nDestChunk` | [PulseRuntimeChunkIndex_t](../pulse_runtime_lib/PulseRuntimeChunkIndex_t.md) | [CPulse_OutflowConnection](../pulse_runtime_lib/CPulse_OutflowConnection.md) |  |
| `0x14` | `m_nInstruction` | int32 | [CPulse_OutflowConnection](../pulse_runtime_lib/CPulse_OutflowConnection.md) |  |
| `0x18` | `m_OutflowRegisterMap` | [PulseRegisterMap_t](../pulse_runtime_lib/PulseRegisterMap_t.md) | [CPulse_OutflowConnection](../pulse_runtime_lib/CPulse_OutflowConnection.md) |  |
