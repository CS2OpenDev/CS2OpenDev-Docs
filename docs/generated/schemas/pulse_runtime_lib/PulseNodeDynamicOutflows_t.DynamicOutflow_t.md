---
layout: default
title: "PulseNodeDynamicOutflows_t::DynamicOutflow_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [pulse_runtime_lib](../pulse_runtime_lib.md) / PulseNodeDynamicOutflows_t::DynamicOutflow_t

# PulseNodeDynamicOutflows_t::DynamicOutflow_t

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 8 · **Module:** pulse_runtime_lib

**Relationships:**

```mermaid
classDiagram
    "PulseNodeDynamicOutflows_t::DynamicOutflow_t" *-- CPulse_OutflowConnection
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_OutflowID` | CGlobalSymbol |  |  |
| `0x8` | `m_Connection` | [CPulse_OutflowConnection](../pulse_runtime_lib/CPulse_OutflowConnection.md) |  | `MFgdFromSchemaCompletelySkipField` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_OutflowID&quot;: &quot;&quot;,
	&quot;m_Connection&quot;:
	{
		&quot;m_SourceOutflowName&quot;: &quot;&quot;,
		&quot;m_nDestChunk&quot;: -1,
		&quot;m_nInstruction&quot;: -1
	}
}</pre>
</details>
