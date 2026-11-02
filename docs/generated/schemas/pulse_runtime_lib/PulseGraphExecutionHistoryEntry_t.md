---
title: PulseGraphExecutionHistoryEntry_t
module: pulse_runtime_lib
kind: class
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / PulseGraphExecutionHistoryEntry_t

# PulseGraphExecutionHistoryEntry_t

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** pulse_runtime_lib

**Relationships:**

```mermaid
classDiagram
    PulseGraphExecutionHistoryEntry_t *-- PulseCursorID_t
    PulseGraphExecutionHistoryEntry_t *-- PulseDocNodeID_t
```

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `nCursorID` | [PulseCursorID_t](../pulse_runtime_lib/PulseCursorID_t.md) |  |  |
| `0x4` | `nEditorID` | [PulseDocNodeID_t](../pulse_runtime_lib/PulseDocNodeID_t.md) |  |  |
| `0x8` | `seqPoint` | PulseSymbol_t |  |  |
| `0x18` | `flExecTime` | float32 |  |  |
| `0x1c` | `unFlags` | uint32 |  |  |
| `0x20` | `tagName` | PulseSymbol_t |  |  |
| `0x30` | `childID` | [PulseCursorID_t](../pulse_runtime_lib/PulseCursorID_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;nCursorID&quot;: -1,
	&quot;nEditorID&quot;: -1,
	&quot;seqPoint&quot;: &quot;&quot;,
	&quot;flExecTime&quot;: 0.000000,
	&quot;unFlags&quot;: 0,
	&quot;tagName&quot;: &quot;&quot;,
	&quot;childID&quot;: -1
}</pre>
</details>
