---
layout: default
title: CSSDSMsg_ViewTarget
nav_exclude: true
---

[Schemas](../../schemas.md) / [scenesystem](../scenesystem.md) / CSSDSMsg_ViewTarget

# CSSDSMsg_ViewTarget

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** scenesystem

## Memory layout

10 fields (10 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_Name` | CUtlString |  |  |
| `0x8` | `m_TextureId` | uint64 |  |  |
| `0x10` | `m_nWidth` | int32 |  |  |
| `0x14` | `m_nHeight` | int32 |  |  |
| `0x18` | `m_nRequestedWidth` | int32 |  |  |
| `0x1c` | `m_nRequestedHeight` | int32 |  |  |
| `0x20` | `m_nNumMipLevels` | int32 |  |  |
| `0x24` | `m_nDepth` | int32 |  |  |
| `0x28` | `m_nMultisampleNumSamples` | int32 |  |  |
| `0x2c` | `m_nFormat` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_Name&quot;: &quot;&quot;,
	&quot;m_TextureId&quot;: 0,
	&quot;m_nWidth&quot;: 0,
	&quot;m_nHeight&quot;: 0,
	&quot;m_nRequestedWidth&quot;: 0,
	&quot;m_nRequestedHeight&quot;: 0,
	&quot;m_nNumMipLevels&quot;: 0,
	&quot;m_nDepth&quot;: 0,
	&quot;m_nMultisampleNumSamples&quot;: 0,
	&quot;m_nFormat&quot;: 0
}</pre>
</details>
