---
layout: default
title: CColorTintColorCorrectionLayer
nav_exclude: true
---

[Schemas](../../schemas.md) / [resourcecompiler](../resourcecompiler.md) / CColorTintColorCorrectionLayer

# CColorTintColorCorrectionLayer

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** resourcecompiler

**Inherits from:** [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md)

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CColorTintColorCorrectionLayer
```

## Memory layout

9 fields (5 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x10` | `m_nOpacityPercent` | int32 | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x14` | `m_bVisible` | bool | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x18` | `m_pLayerMask` | [CLayerMask](../resourcecompiler/CLayerMask.md)* | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x28` | `m_nTintColorR` | int32 |  |  |
| `0x2c` | `m_nTintColorG` | int32 |  |  |
| `0x30` | `m_nTintColorB` | int32 |  |  |
| `0x34` | `m_nStrength` | int32 |  |  |
| `0x38` | `m_bPreserveLuminosity` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CColorTintColorCorrectionLayer&quot;,
	&quot;m_name&quot;: &quot;Color Tint 1&quot;,
	&quot;m_nOpacityPercent&quot;: 100,
	&quot;m_bVisible&quot;: true,
	&quot;m_pLayerMask&quot;: null,
	&quot;m_nTintColorR&quot;: 255,
	&quot;m_nTintColorG&quot;: 150,
	&quot;m_nTintColorB&quot;: 20,
	&quot;m_nStrength&quot;: 20,
	&quot;m_bPreserveLuminosity&quot;: true
}</pre>
</details>
