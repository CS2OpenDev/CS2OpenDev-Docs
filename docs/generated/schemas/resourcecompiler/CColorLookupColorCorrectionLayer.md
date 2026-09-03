---
title: CColorLookupColorCorrectionLayer
module: resourcecompiler
kind: class
---

[Schemas](../../schemas.md) / [resourcecompiler](../resourcecompiler.md) / CColorLookupColorCorrectionLayer

# CColorLookupColorCorrectionLayer

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 8 · **Module:** resourcecompiler

**Inherits from:** [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md)

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CColorLookupColorCorrectionLayer
```

## Memory layout

7 fields (3 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x10` | `m_nOpacityPercent` | int32 | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x14` | `m_bVisible` | bool | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x18` | `m_pLayerMask` | [CLayerMask](../resourcecompiler/CLayerMask.md)* | [CColorCorrectionLayer](../resourcecompiler/CColorCorrectionLayer.md) |  |
| `0x28` | `m_fileName` | CUtlString |  |  |
| `0x30` | `m_lut` | CUtlVector< float32 > |  |  |
| `0x48` | `m_nDim` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CColorLookupColorCorrectionLayer&quot;,
	&quot;m_name&quot;: &quot;Lookup Table 1&quot;,
	&quot;m_nOpacityPercent&quot;: 100,
	&quot;m_bVisible&quot;: true,
	&quot;m_pLayerMask&quot;: null,
	&quot;m_fileName&quot;: &quot;&quot;,
	&quot;m_lut&quot;:
	[
	],
	&quot;m_nDim&quot;: 0
}</pre>
</details>
