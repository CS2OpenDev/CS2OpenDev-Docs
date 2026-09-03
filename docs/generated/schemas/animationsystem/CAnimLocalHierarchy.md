---
title: CAnimLocalHierarchy
module: animationsystem
kind: class
---

[Schemas](../../schemas.md) / [animationsystem](../animationsystem.md) / CAnimLocalHierarchy

# CAnimLocalHierarchy

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** animationsystem

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sBone` | CBufferString |  |  |
| `0x10` | `m_sNewParent` | CBufferString |  |  |
| `0x20` | `m_nStartFrame` | int32 |  |  |
| `0x24` | `m_nPeakFrame` | int32 |  |  |
| `0x28` | `m_nTailFrame` | int32 |  |  |
| `0x2c` | `m_nEndFrame` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sBone&quot;: &quot;&quot;,
	&quot;m_sNewParent&quot;: &quot;&quot;,
	&quot;m_nStartFrame&quot;: 0,
	&quot;m_nPeakFrame&quot;: 0,
	&quot;m_nTailFrame&quot;: 0,
	&quot;m_nEndFrame&quot;: 0
}</pre>
</details>
