---
layout: default
title: CPulseCell_Step_TestDomainEntFire
nav_exclude: true
---

[Schemas](../../schemas.md) / [pulse_system](../pulse_system.md) / CPulseCell_Step_TestDomainEntFire

# CPulseCell_Step_TestDomainEntFire

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 8 · **Module:** pulse_system

**Inherits from:** [CPulseCell_BaseFlow](../pulse_runtime_lib/CPulseCell_BaseFlow.md)

**Metadata:** `MPropertyFriendlyName Fake Ent-Fire`, `MPulseEditorHeaderText Fire input {m_Input}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainEntFire
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nEditorNodeID` | [PulseDocNodeID_t](../pulse_runtime_lib/PulseDocNodeID_t.md) | [CPulseCell_Base](../pulse_runtime_lib/CPulseCell_Base.md) | `MFgdFromSchemaCompletelySkipField` |
| `0x48` | `m_Input` | CUtlString |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CPulseCell_Step_TestDomainEntFire&quot;,
	&quot;m_nEditorNodeID&quot;: -1,
	&quot;m_Input&quot;: &quot;&quot;
}</pre>
</details>
