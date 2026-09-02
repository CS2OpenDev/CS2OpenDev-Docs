---
layout: default
title: CSoundEnvelope
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CSoundEnvelope

# CSoundEnvelope

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 4 · **Module:** server

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_current` | float32 |  |  |
| `0x4` | `m_target` | float32 |  |  |
| `0x8` | `m_rate` | float32 |  |  |
| `0xc` | `m_forceupdate` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_current&quot;: 0.000000,
	&quot;m_target&quot;: 0.000000,
	&quot;m_rate&quot;: 0.000000,
	&quot;m_forceupdate&quot;: false
}</pre>
</details>
