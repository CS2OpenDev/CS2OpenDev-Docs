---
title: CAnimDataChannelDesc
module: animationsystem
kind: class
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / CAnimDataChannelDesc

# CAnimDataChannelDesc

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 144 bytes (`0x90`) · **Align:** 8 · **Module:** animationsystem

## Memory layout

9 fields (9 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_szChannelClass` | CBufferString |  |  |
| `0x10` | `m_szVariableName` | CBufferString |  |  |
| `0x20` | `m_nFlags` | int32 |  |  |
| `0x24` | `m_nType` | int32 |  |  |
| `0x28` | `m_szGrouping` | CBufferString |  |  |
| `0x38` | `m_szDescription` | CBufferString |  |  |
| `0x48` | `m_szElementNameArray` | CUtlVector< CBufferString > |  |  |
| `0x60` | `m_nElementIndexArray` | CUtlVector< int32 > |  |  |
| `0x78` | `m_nElementMaskArray` | CUtlVector< uint32 > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_szChannelClass&quot;: &quot;&quot;,
	&quot;m_szVariableName&quot;: &quot;&quot;,
	&quot;m_nFlags&quot;: 0,
	&quot;m_nType&quot;: 0,
	&quot;m_szGrouping&quot;: &quot;&quot;,
	&quot;m_szDescription&quot;: &quot;&quot;,
	&quot;m_szElementNameArray&quot;:
	[
	],
	&quot;m_nElementIndexArray&quot;:
	[
	],
	&quot;m_nElementMaskArray&quot;:
	[
	]
}</pre>
</details>
