---
layout: default
title: CManifestInfo
nav_exclude: true
---

[Schemas](../../schemas.md) / [toolutils2](../toolutils2.md) / CManifestInfo

# CManifestInfo

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** toolutils2

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_Name` | CUtlString |  |  |
| `0x8` | `m_Group` | CUtlString |  |  |
| `0x10` | `m_Mod` | CUtlString |  |  |
| `0x18` | `m_SourceFile` | CUtlString |  |  |
| `0x20` | `m_nSourceLine` | int32 |  |  |
| `0x28` | `m_Resources` | CUtlVector< CUtlString > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_Name&quot;: &quot;&quot;,
	&quot;m_Group&quot;: &quot;&quot;,
	&quot;m_Mod&quot;: &quot;&quot;,
	&quot;m_SourceFile&quot;: &quot;&quot;,
	&quot;m_nSourceLine&quot;: 0,
	&quot;m_Resources&quot;:
	[
	]
}</pre>
</details>
