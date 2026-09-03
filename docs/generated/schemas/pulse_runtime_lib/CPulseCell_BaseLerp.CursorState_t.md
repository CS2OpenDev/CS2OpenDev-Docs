---
title: "CPulseCell_BaseLerp::CursorState_t"
module: pulse_runtime_lib
kind: class
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / CPulseCell_BaseLerp::CursorState_t

# CPulseCell_BaseLerp::CursorState_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 8 bytes (`0x8`) · **Align:** 4 · **Module:** pulse_runtime_lib

**Derived by:** [CPulseCell_LerpCameraSettings::CursorState_t](../client/CPulseCell_LerpCameraSettings.CursorState_t.md), [CPulseCell_LerpCameraSettings::CursorState_t](../client/CPulseCell_LerpCameraSettings.CursorState_t.md)

**Relationships:**

```mermaid
classDiagram
    `CPulseCell_BaseLerp::CursorState_t` <|-- `CPulseCell_LerpCameraSettings::CursorState_t`
    `CPulseCell_BaseLerp::CursorState_t` *-- GameTime_t
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_StartTime` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x4` | `m_EndTime` | [GameTime_t](../entity2/GameTime_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_StartTime&quot;: null,
	&quot;m_EndTime&quot;: null
}</pre>
</details>
