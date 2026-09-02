---
title: CLocalContrastLayer
module: resourcecompiler
kind: class
---

[Schemas](../../schemas.md) / [resourcecompiler](../resourcecompiler.md) / CLocalContrastLayer

# CLocalContrastLayer

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** resourcecompiler

**Inherits from:** [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md)

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CLocalContrastLayer
    CLocalContrastLayer *-- PostProcessingLocalContrastParameters_t
```

## Memory layout

5 fields (1 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x10` | `m_nOpacityPercent` | int32 | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x14` | `m_bVisible` | bool | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x18` | `m_pLayerMask` | [CLayerMask](../resourcecompiler/CLayerMask.md)* | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x28` | `m_params` | [PostProcessingLocalContrastParameters_t](../materialsystem2/PostProcessingLocalContrastParameters_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CLocalContrastLayer&quot;,
	&quot;m_name&quot;: &quot;Local Contrast 1&quot;,
	&quot;m_nOpacityPercent&quot;: 100,
	&quot;m_bVisible&quot;: true,
	&quot;m_pLayerMask&quot;: null,
	&quot;m_params&quot;:
	{
		&quot;m_flLocalContrastStrength&quot;: 0.000000,
		&quot;m_flLocalContrastEdgeStrength&quot;: 0.000000,
		&quot;m_flLocalContrastVignetteStart&quot;: 0.000000,
		&quot;m_flLocalContrastVignetteEnd&quot;: 0.000000,
		&quot;m_flLocalContrastVignetteBlur&quot;: 0.000000
	}
}</pre>
</details>
