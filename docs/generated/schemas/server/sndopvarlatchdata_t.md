---
layout: default
title: sndopvarlatchdata_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / sndopvarlatchdata_t

# sndopvarlatchdata_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** server

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_iszStack` | CUtlSymbolLarge |  |  |
| `0x10` | `m_iszOperator` | CUtlSymbolLarge |  |  |
| `0x18` | `m_iszOpvar` | CUtlSymbolLarge |  |  |
| `0x20` | `m_flVal` | float32 |  |  |
| `0x24` | `m_vPos` | VectorWS |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;sndopvarlatchdata_t&quot;,
	&quot;m_iszStack&quot;: &quot;&quot;,
	&quot;m_iszOperator&quot;: &quot;&quot;,
	&quot;m_iszOpvar&quot;: &quot;&quot;,
	&quot;m_flVal&quot;: 0.000000,
	&quot;m_vPos&quot;: null
}</pre>
</details>
