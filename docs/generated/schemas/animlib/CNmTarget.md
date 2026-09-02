---
layout: default
title: CNmTarget
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmTarget

# CNmTarget

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 16 · **Module:** animlib

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_transform` | CTransform |  |  |
| `0x20` | `m_boneID` | CGlobalSymbol |  |  |
| `0x28` | `m_bIsBoneTarget` | bool |  |  |
| `0x29` | `m_bIsUsingBoneSpaceOffsets` | bool |  |  |
| `0x2a` | `m_bHasOffsets` | bool |  |  |
| `0x2b` | `m_bIsSet` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_transform&quot;:
	[
		0.000000,
		0.000000,
		0.000000,
		1.000000,
		0.000000,
		0.000000,
		0.000000,
		1.000000
	],
	&quot;m_boneID&quot;: &quot;&quot;,
	&quot;m_bIsBoneTarget&quot;: false,
	&quot;m_bIsUsingBoneSpaceOffsets&quot;: true,
	&quot;m_bHasOffsets&quot;: false,
	&quot;m_bIsSet&quot;: false
}</pre>
</details>
