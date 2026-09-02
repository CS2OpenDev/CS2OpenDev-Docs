---
layout: default
title: AnimationDecodeDebugDumpElement_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / AnimationDecodeDebugDumpElement_t

# AnimationDecodeDebugDumpElement_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 112 bytes (`0x70`) · **Align:** 8 · **Module:** animationsystem

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_nEntityIndex` | int32 |  |  |
| `0x8` | `m_modelName` | CUtlString |  |  |
| `0x10` | `m_poseParams` | CUtlVector< CUtlString > |  |  |
| `0x28` | `m_decodeOps` | CUtlVector< CUtlString > |  |  |
| `0x40` | `m_internalOps` | CUtlVector< CUtlString > |  |  |
| `0x58` | `m_decodedAnims` | CUtlVector< CUtlString > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_nEntityIndex&quot;: 0,
	&quot;m_modelName&quot;: &quot;&quot;,
	&quot;m_poseParams&quot;:
	[
	],
	&quot;m_decodeOps&quot;:
	[
	],
	&quot;m_internalOps&quot;:
	[
	],
	&quot;m_decodedAnims&quot;:
	[
	]
}</pre>
</details>
