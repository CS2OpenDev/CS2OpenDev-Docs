---
layout: default
title: CPulseCell_Base
nav_exclude: true
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / CPulseCell_Base

# CPulseCell_Base

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** pulse_runtime_lib

**Derived by:** [CPulseCell_BaseFlow](../pulse_runtime_lib/CPulseCell_BaseFlow.md), [CPulseCell_BaseRequirement](../pulse_runtime_lib/CPulseCell_BaseRequirement.md), [CPulseCell_BaseValue](../pulse_runtime_lib/CPulseCell_BaseValue.md), [CPulseCell_Unknown](../pulse_runtime_lib/CPulseCell_Unknown.md)

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_Base <|-- CPulseCell_BaseRequirement
    CPulseCell_Base <|-- CPulseCell_BaseValue
    CPulseCell_Base <|-- CPulseCell_Unknown
    CPulseCell_Base *-- PulseDocNodeID_t
```

## Memory layout

1 fields (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nEditorNodeID` | [PulseDocNodeID_t](../pulse_runtime_lib/PulseDocNodeID_t.md) |  | `MFgdFromSchemaCompletelySkipField` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CPulseCell_Base&quot;,
	&quot;m_nEditorNodeID&quot;: -1
}</pre>
</details>
