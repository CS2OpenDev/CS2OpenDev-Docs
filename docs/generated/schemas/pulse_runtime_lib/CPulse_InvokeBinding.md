---
layout: default
title: CPulse_InvokeBinding
nav_exclude: true
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / CPulse_InvokeBinding

# CPulse_InvokeBinding

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 176 bytes (`0xb0`) · **Align:** 8 · **Module:** pulse_runtime_lib

**Relationships:**

```mermaid
classDiagram
    CPulse_InvokeBinding *-- PulseRegisterMap_t
    CPulse_InvokeBinding *-- PulseRuntimeCellIndex_t
    CPulse_InvokeBinding *-- PulseRuntimeChunkIndex_t
```

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_RegisterMap` | [PulseRegisterMap_t](../pulse_runtime_lib/PulseRegisterMap_t.md) |  |  |
| `0x30` | `m_FuncName` | PulseSymbol_t |  |  |
| `0x40` | `m_nCellIndex` | [PulseRuntimeCellIndex_t](../pulse_runtime_lib/PulseRuntimeCellIndex_t.md) |  |  |
| `0x44` | `m_nSrcChunk` | [PulseRuntimeChunkIndex_t](../pulse_runtime_lib/PulseRuntimeChunkIndex_t.md) |  |  |
| `0x48` | `m_nSrcInstruction` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_RegisterMap&quot;:
	{
		&quot;m_Inparams&quot;: null,
		&quot;m_Outparams&quot;: null
	},
	&quot;m_FuncName&quot;: &quot;&quot;,
	&quot;m_nCellIndex&quot;: -1,
	&quot;m_nSrcChunk&quot;: -1,
	&quot;m_nSrcInstruction&quot;: -1
}</pre>
</details>
