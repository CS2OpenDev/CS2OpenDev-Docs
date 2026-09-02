---
layout: default
title: FeEffectDesc_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [physicslib](../physicslib.md) / FeEffectDesc_t

# FeEffectDesc_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** physicslib

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `sName` | CUtlString |  |  |
| `0x8` | `nNameHash` | uint32 |  |  |
| `0xc` | `nType` | int32 |  |  |
| `0x10` | `m_Params` | KeyValues3 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;sName&quot;: &quot;&quot;,
	&quot;nNameHash&quot;: 0,
	&quot;nType&quot;: 0,
	&quot;m_Params&quot;: null
}</pre>
</details>
