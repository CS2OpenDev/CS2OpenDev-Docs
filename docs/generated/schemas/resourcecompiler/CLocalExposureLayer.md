---
layout: default
title: CLocalExposureLayer
nav_exclude: true
---

[Schemas](../../schemas.md) / [resourcecompiler](../resourcecompiler.md) / CLocalExposureLayer

# CLocalExposureLayer

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** resourcecompiler

**Inherits from:** [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md)

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CLocalExposureLayer
    CLocalExposureLayer *-- PostProcessingLocalExposureParameters_t
```

## Memory layout

5 fields (1 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x10` | `m_nOpacityPercent` | int32 | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x14` | `m_bVisible` | bool | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x18` | `m_pLayerMask` | [CLayerMask](../resourcecompiler/CLayerMask.md)* | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x28` | `m_params` | [PostProcessingLocalExposureParameters_t](../materialsystem2/PostProcessingLocalExposureParameters_t.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CLocalExposureLayer&quot;,
	&quot;m_name&quot;: &quot;Local Exposure 1&quot;,
	&quot;m_nOpacityPercent&quot;: 100,
	&quot;m_bVisible&quot;: true,
	&quot;m_pLayerMask&quot;: null,
	&quot;m_params&quot;:
	{
		&quot;m_fShadowOffsetEV&quot;: 0.000000,
		&quot;m_fHighlightOffsetEV&quot;: 0.000000,
		&quot;m_fSigma&quot;: 0.500000,
		&quot;m_fBoostLocalContrast&quot;: 0.000000
	}
}</pre>
</details>
