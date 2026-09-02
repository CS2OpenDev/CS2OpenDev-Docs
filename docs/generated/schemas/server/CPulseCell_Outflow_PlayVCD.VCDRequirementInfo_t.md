---
layout: default
title: "CPulseCell_Outflow_PlayVCD::VCDRequirementInfo_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CPulseCell_Outflow_PlayVCD::VCDRequirementInfo_t

# CPulseCell_Outflow_PlayVCD::VCDRequirementInfo_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 8 · **Module:** server

**Relationships:**

```mermaid
classDiagram
    `CPulseCell_Outflow_PlayVCD::VCDRequirementInfo_t` *-- CPulse_OutflowConnection
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nEventID` | int32 |  |  |
| `0x8` | `m_Outflow` | [CPulse_OutflowConnection](../pulse_runtime_lib/CPulse_OutflowConnection.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nEventID&quot;: -1,
	&quot;m_Outflow&quot;:
	{
		&quot;m_SourceOutflowName&quot;: &quot;&quot;,
		&quot;m_nDestChunk&quot;: -1,
		&quot;m_nInstruction&quot;: -1
	}
}</pre>
</details>
