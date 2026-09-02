---
title: CTextureSheetDoc_Frame
module: texturelib
kind: class
---

[Schemas](../../schemas.md) / [texturelib](../texturelib.md) / CTextureSheetDoc_Frame

# CTextureSheetDoc_Frame

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** texturelib

**Metadata:** `MPropertyAutoExpandSelf`, `MPropertyCustomEditor SheetSequenceFrame`

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sImageName` | CUtlString |  |  |
| `0x8` | `m_fDisplayTime` | float32 |  |  |
| `0xc` | `m_bCropEnabled` | bool |  |  |
| `0x10` | `m_srcCropXStart` | int32 |  |  |
| `0x14` | `m_srcCropYStart` | int32 |  |  |
| `0x18` | `m_srcCropXEnd` | int32 |  |  |
| `0x1c` | `m_srcCropYEnd` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sImageName&quot;: &quot;&quot;,
	&quot;m_fDisplayTime&quot;: 1.000000,
	&quot;m_bCropEnabled&quot;: false,
	&quot;m_srcCropXStart&quot;: -1,
	&quot;m_srcCropYStart&quot;: -1,
	&quot;m_srcCropXEnd&quot;: -1,
	&quot;m_srcCropYEnd&quot;: -1
}</pre>
</details>
