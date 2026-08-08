---
layout: default
title: CAnimEventDefinition
nav_exclude: true
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / CAnimEventDefinition

# CAnimEventDefinition

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** animationsystem

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nFrame` | int32 |  |  |
| `0xc` | `m_nEndFrame` | int32 |  |  |
| `0x10` | `m_flCycle` | float32 |  |  |
| `0x14` | `m_flDuration` | float32 |  |  |
| `0x18` | `m_EventData` | KeyValues3 |  |  |
| `0x28` | `m_sLegacyOptions` | CBufferString |  | `MKV3TransferName m_sOptions` |
| `0x38` | `m_sEventName` | CGlobalSymbol |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nFrame&quot;: 0,
	&quot;m_nEndFrame&quot;: -1,
	&quot;m_flCycle&quot;: 0.000000,
	&quot;m_flDuration&quot;: 0.000000,
	&quot;m_EventData&quot;: null,
	&quot;m_sOptions&quot;: &quot;&quot;,
	&quot;m_sEventName&quot;: &quot;&quot;
}</pre>
</details>
