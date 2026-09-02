---
layout: default
title: CTransitionUpdateData
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CTransitionUpdateData

# CTransitionUpdateData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 3 bytes (`0x3`) · **Align:** 1 · **Module:** animgraphlib

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` bit 0 | `m_bDisabled` | bitfield:1 |  |  |
| `0x0` bits 1..7 | `m_nHandshakeMaskToDisableFirst` | bitfield:7 |  |  |
| `0x0` | `m_srcStateIndex` | uint8 |  |  |
| `0x1` | `m_destStateIndex` | uint8 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_srcStateIndex&quot;: 0,
	&quot;m_destStateIndex&quot;: 0,
	&quot;m_nHandshakeMaskToDisableFirst&quot;: 0,
	&quot;m_bDisabled&quot;: 0
}</pre>
</details>
