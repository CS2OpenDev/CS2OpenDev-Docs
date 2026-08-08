---
layout: default
title: CPulseCell_Inflow_EntOutputHandler
nav_exclude: true
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / CPulseCell_Inflow_EntOutputHandler

# CPulseCell_Inflow_EntOutputHandler

**Kind:** class · **Size:** 184 bytes (`0xb8`) · **Align:** 8 · **Module:** pulse_runtime_lib

**Inherits from:** [CPulseCell_Inflow_BaseEntrypoint](../pulse_runtime_lib/CPulseCell_Inflow_BaseEntrypoint.md)

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_EntOutputHandler
    CPulseCell_BaseFlow <|-- CPulseCell_Inflow_BaseEntrypoint
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

## Memory layout

6 fields (3 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nEditorNodeID` | [PulseDocNodeID_t](../pulse_runtime_lib/PulseDocNodeID_t.md) | [CPulseCell_Base](../pulse_runtime_lib/CPulseCell_Base.md) | `MFgdFromSchemaCompletelySkipField` |
| `0x48` | `m_EntryChunk` | [PulseRuntimeChunkIndex_t](../pulse_runtime_lib/PulseRuntimeChunkIndex_t.md) | [CPulseCell_Inflow_BaseEntrypoint](../pulse_runtime_lib/CPulseCell_Inflow_BaseEntrypoint.md) |  |
| `0x50` | `m_RegisterMap` | [PulseRegisterMap_t](../pulse_runtime_lib/PulseRegisterMap_t.md) | [CPulseCell_Inflow_BaseEntrypoint](../pulse_runtime_lib/CPulseCell_Inflow_BaseEntrypoint.md) |  |
| `0x80` | `m_SourceEntity` | PulseSymbol_t |  |  |
| `0x90` | `m_SourceOutput` | PulseSymbol_t |  |  |
| `0xa0` | `m_ExpectedParamType` | CPulseValueFullType |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CPulseCell_Inflow_EntOutputHandler&quot;,
	&quot;m_nEditorNodeID&quot;: -1,
	&quot;m_EntryChunk&quot;: -1,
	&quot;m_RegisterMap&quot;:
	{
		&quot;m_Inparams&quot;: null,
		&quot;m_Outparams&quot;: null
	},
	&quot;m_SourceEntity&quot;: &quot;&quot;,
	&quot;m_SourceOutput&quot;: &quot;&quot;,
	&quot;m_ExpectedParamType&quot;: &quot;PVAL_VOID&quot;
}</pre>
</details>
