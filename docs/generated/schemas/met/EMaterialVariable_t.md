---
title: EMaterialVariable_t
module: met
kind: class
---

[Schemas](../../schemas.md) / [met](../met.md) / EMaterialVariable_t

# EMaterialVariable_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 248 bytes (`0xf8`) · **Align:** 8 · **Module:** met

## Memory layout

36 fields (36 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_Name` | CUtlString |  |  |
| `0x8` | `m_ExportName` | CUtlString |  |  |
| `0x10` | `m_UiName` | CUtlString |  |  |
| `0x18` | `m_UiOptions` | CUtlString |  |  |
| `0x20` | `m_bEnabled` | bool |  |  |
| `0x21` | `m_bHidden` | bool |  |  |
| `0x28` | `m_EnumLabel` | CUtlString |  |  |
| `0x30` | `m_nLayerId` | int32 |  |  |
| `0x34` | `m_bLayerAllowOverride` | bool |  |  |
| `0x35` | `m_bLayerReference` | bool |  |  |
| `0x38` | `m_inheritedValue` | CUtlString |  |  |
| `0x40` | `m_inheritedValueSource` | CUtlString |  |  |
| `0x48` | `m_Group` | CUtlString |  |  |
| `0x50` | `m_SubGroup` | CUtlString |  |  |
| `0x58` | `m_nSortKeyGroup` | int32 |  |  |
| `0x5c` | `m_nSortKeySubGroup` | int32 |  |  |
| `0x60` | `m_nSortKeyVariable` | int32 |  |  |
| `0x68` | `m_error` | CUtlString |  |  |
| `0x70` | `m_expression` | CUtlString |  |  |
| `0x78` | `m_referencedExpressionPath` | CUtlString |  |  |
| `0x80` | `m_referencedValuePath` | CUtlString |  |  |
| `0x88` | `m_nElements` | int32 |  |  |
| `0x90` | `m_value` | CUtlString |  |  |
| `0x98` | `m_default` | CUtlString |  |  |
| `0xa0` | `m_min` | CUtlString |  |  |
| `0xa8` | `m_max` | CUtlString |  |  |
| `0xb0` | `m_step` | CUtlString |  |  |
| `0xb8` | `m_precision` | CUtlString |  |  |
| `0xc0` | `m_bInitialTextureInput` | bool |  |  |
| `0xc4` | `m_nTextureAutoFillCount` | int32 |  |  |
| `0xc8` | `m_alternateInput` | CUtlString |  |  |
| `0xd0` | `m_defaultColor` | CUtlString |  |  |
| `0xd8` | `m_defaultInput` | CUtlString |  |  |
| `0xe0` | `m_textureSuffix` | CUtlString |  |  |
| `0xe8` | `m_defaultSlider` | CUtlString |  |  |
| `0xf0` | `m_fDefaultSlider` | float32[2] |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_Name&quot;: &quot;&quot;,
	&quot;m_ExportName&quot;: &quot;&quot;,
	&quot;m_UiName&quot;: &quot;&quot;,
	&quot;m_UiOptions&quot;: &quot;&quot;,
	&quot;m_bEnabled&quot;: false,
	&quot;m_bHidden&quot;: false,
	&quot;m_EnumLabel&quot;: &quot;&quot;,
	&quot;m_nLayerId&quot;: -1,
	&quot;m_bLayerAllowOverride&quot;: true,
	&quot;m_bLayerReference&quot;: false,
	&quot;m_inheritedValue&quot;: &quot;&quot;,
	&quot;m_inheritedValueSource&quot;: &quot;&quot;,
	&quot;m_Group&quot;: &quot;&quot;,
	&quot;m_SubGroup&quot;: &quot;&quot;,
	&quot;m_nSortKeyGroup&quot;: -1,
	&quot;m_nSortKeySubGroup&quot;: -1,
	&quot;m_nSortKeyVariable&quot;: -1,
	&quot;m_error&quot;: &quot;&quot;,
	&quot;m_expression&quot;: &quot;&quot;,
	&quot;m_referencedExpressionPath&quot;: &quot;&quot;,
	&quot;m_referencedValuePath&quot;: &quot;&quot;,
	&quot;m_nElements&quot;: 1,
	&quot;m_value&quot;: &quot;&quot;,
	&quot;m_default&quot;: &quot;&quot;,
	&quot;m_min&quot;: &quot;&quot;,
	&quot;m_max&quot;: &quot;&quot;,
	&quot;m_step&quot;: &quot;&quot;,
	&quot;m_precision&quot;: &quot;&quot;,
	&quot;m_bInitialTextureInput&quot;: true,
	&quot;m_nTextureAutoFillCount&quot;: 0,
	&quot;m_alternateInput&quot;: &quot;&quot;,
	&quot;m_defaultColor&quot;: &quot;[0 0 0 0]&quot;,
	&quot;m_defaultInput&quot;: &quot;&quot;,
	&quot;m_textureSuffix&quot;: &quot;&quot;,
	&quot;m_defaultSlider&quot;: &quot;[0 0 0 0]&quot;,
	&quot;m_fDefaultSlider&quot;:
	[
		0.000000,
		0.000000
	]
}</pre>
</details>
