---
layout: default
title: CPulseCell_Step_SetAnimGraphParam
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CPulseCell_Step_SetAnimGraphParam

# CPulseCell_Step_SetAnimGraphParam

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 8 · **Module:** server

**Inherits from:** [CPulseCell_BaseFlow](../pulse_runtime_lib/CPulseCell_BaseFlow.md)

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Step_SetAnimGraphParam
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nEditorNodeID` | [PulseDocNodeID_t](../pulse_runtime_lib/PulseDocNodeID_t.md) | [CPulseCell_Base](../pulse_runtime_lib/CPulseCell_Base.md) | `MFgdFromSchemaCompletelySkipField` |
| `0x48` | `m_ParamName` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CPulseCell_Step_SetAnimGraphParam&quot;,
	&quot;m_nEditorNodeID&quot;: -1,
	&quot;m_ParamName&quot;: &quot;&quot;
}</pre>
</details>
