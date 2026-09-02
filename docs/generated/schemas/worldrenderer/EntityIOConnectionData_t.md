---
layout: default
title: EntityIOConnectionData_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [worldrenderer](../worldrenderer.md) / EntityIOConnectionData_t

# EntityIOConnectionData_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** worldrenderer

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_outputName` | CUtlString |  |  |
| `0x8` | `m_targetType` | uint32 |  |  |
| `0x10` | `m_targetName` | CUtlString |  |  |
| `0x18` | `m_inputName` | CUtlString |  |  |
| `0x20` | `m_overrideParam` | CUtlString |  |  |
| `0x28` | `m_flDelay` | float32 |  |  |
| `0x2c` | `m_nTimesToFire` | int32 |  |  |
| `0x30` | `m_paramMap` | KeyValues3 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_outputName&quot;: &quot;&quot;,
	&quot;m_targetType&quot;: 0,
	&quot;m_targetName&quot;: &quot;&quot;,
	&quot;m_inputName&quot;: &quot;&quot;,
	&quot;m_overrideParam&quot;: &quot;&quot;,
	&quot;m_flDelay&quot;: 0.000000,
	&quot;m_nTimesToFire&quot;: 0,
	&quot;m_paramMap&quot;: null
}</pre>
</details>
