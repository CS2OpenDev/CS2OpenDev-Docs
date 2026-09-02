---
layout: default
title: CAudioMorphData
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem_voicecontainers](../soundsystem_voicecontainers.md) / CAudioMorphData

# CAudioMorphData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 104 bytes (`0x68`) · **Align:** 8 · **Module:** soundsystem_voicecontainers

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_times` | CUtlVector< float32 > |  |  |
| `0x18` | `m_nameHashCodes` | CUtlVector< uint32 > |  |  |
| `0x30` | `m_nameStrings` | CUtlVector< CUtlString > |  |  |
| `0x48` | `m_samples` | CUtlVector< CUtlVector< float32 > > |  |  |
| `0x60` | `m_flEaseIn` | float32 |  |  |
| `0x64` | `m_flEaseOut` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_times&quot;:
	[
	],
	&quot;m_nameHashCodes&quot;:
	[
	],
	&quot;m_nameStrings&quot;:
	[
	],
	&quot;m_samples&quot;:
	[
	],
	&quot;m_flEaseIn&quot;: 0.200000,
	&quot;m_flEaseOut&quot;: 0.200000
}</pre>
</details>
