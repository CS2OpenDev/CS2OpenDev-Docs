---
layout: default
title: resourcecompiler
parent: Schemas
nav_exclude: true
---

# Module: resourcecompiler

[📊 View UML Diagram](../diagrams/resourcecompiler.md)

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [CBloomLayer](#cbloomlayer) | class | CColorCorrectionLayer | 1 |
| [CBrightnessContrastColorCorrectionLayer](#cbrightnesscontrastcolorcorrectionlayer) | class | CColorCorrectionLayer | 2 |
| [CColorBalanceColorCorrectionLayer](#ccolorbalancecolorcorrectionlayer) | class | CColorCorrectionLayer | 10 |
| [CColorCorrectionLayer](#ccolorcorrectionlayer) | class |  | 4 |
| [CColorLookupColorCorrectionLayer](#ccolorlookupcolorcorrectionlayer) | class | CColorCorrectionLayer | 3 |
| [CColorTintColorCorrectionLayer](#ccolortintcolorcorrectionlayer) | class | CColorCorrectionLayer | 5 |
| [CCurvesColorCorrectionLayer](#ccurvescolorcorrectionlayer) | class | CColorCorrectionLayer | 4 |
| [CFogScatteringLayer](#cfogscatteringlayer) | class | CColorCorrectionLayer | 1 |
| [CHueSaturationColorCorrectionLayer](#chuesaturationcolorcorrectionlayer) | class | CColorCorrectionLayer | 21 |
| [CLayerMask](#clayermask) | class |  | 4 |
| [CLevelsColorCorrectionLayer](#clevelscolorcorrectionlayer) | class | CColorCorrectionLayer | 20 |
| [CLocalContrastLayer](#clocalcontrastlayer) | class | CColorCorrectionLayer | 1 |
| [CPostProcessData](#cpostprocessdata) | class |  | 1 |
| [CToneMappingLayer](#ctonemappinglayer) | class | CColorCorrectionLayer | 1 |
| [CVibranceColorCorrectionLayer](#cvibrancecolorcorrectionlayer) | class | CColorCorrectionLayer | 2 |
| [CVignetteLayer](#cvignettelayer) | class | CColorCorrectionLayer | 1 |
| [LayerMaskType_t](#layermasktype_t) | enum |  | 2 |
| [LayerType_t](#layertype_t) | enum |  | 14 |

---

### CBloomLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CBloomLayer",
	"m_name": "Bloom 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_params":
	{
		"m_blendMode": "BLOOM_BLEND_ADD",
		"m_flBloomStrength": 2.000000,
		"m_flScreenBloomStrength": 1.000000,
		"m_flBlurBloomStrength": 1.000000,
		"m_flBloomThreshold": 0.000000,
		"m_flBloomThresholdWidth": 1.000000,
		"m_flSkyboxBloomStrength": 1.000000,
		"m_flBloomStartValue": 1.000000,
		"m_flComputeBloomStrength": 0.030000,
		"m_flComputeBloomThreshold": 1.000000,
		"m_flComputeBloomRadius": 0.600000,
		"m_flComputeBloomEffectsScale": 1.000000,
		"m_flComputeBloomLensDirtStrength": 0.000000,
		"m_flComputeBloomLensDirtBlackLevel": 0.100000,
		"m_flBlurWeight":
		[
			0.200000,
			0.200000,
			0.200000,
			0.200000,
			0.200000
		],
		"m_vBlurTint":
		[
			[
				1.000000,
				1.000000,
				1.000000
			],
			[
				1.000000,
				1.000000,
				1.000000
			],
			[
				1.000000,
				1.000000,
				1.000000
			],
			[
				1.000000,
				1.000000,
				1.000000
			],
			[
				1.000000,
				1.000000,
				1.000000
			]
		]
	}
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CBloomLayer
    CBloomLayer *-- PostProcessingBloomParameters_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_params` | [PostProcessingBloomParameters_t](../schemas/materialsystem2.md#postprocessingbloomparameters_t) |  |

### CBrightnessContrastColorCorrectionLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CBrightnessContrastColorCorrectionLayer",
	"m_name": "Brightness/Contrast 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_nBrightness": 0,
	"m_nContrast": 0
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CBrightnessContrastColorCorrectionLayer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nBrightness` | int32 |  |
| `m_nContrast` | int32 |  |

### CColorBalanceColorCorrectionLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CColorBalanceColorCorrectionLayer",
	"m_name": "Color Balance 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_nRedCyanBalS": 0,
	"m_nRedCyanBalM": 0,
	"m_nRedCyanBalH": 0,
	"m_nGreenMagentaBalS": 0,
	"m_nGreenMagentaBalM": 0,
	"m_nGreenMagentaBalH": 0,
	"m_nBlueYellowBalS": 0,
	"m_nBlueYellowBalM": 0,
	"m_nBlueYellowBalH": 0,
	"m_bPreserveLuminosity": true
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CColorBalanceColorCorrectionLayer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nRedCyanBalS` | int32 |  |
| `m_nRedCyanBalM` | int32 |  |
| `m_nRedCyanBalH` | int32 |  |
| `m_nGreenMagentaBalS` | int32 |  |
| `m_nGreenMagentaBalM` | int32 |  |
| `m_nGreenMagentaBalH` | int32 |  |
| `m_nBlueYellowBalS` | int32 |  |
| `m_nBlueYellowBalM` | int32 |  |
| `m_nBlueYellowBalH` | int32 |  |
| `m_bPreserveLuminosity` | bool |  |

### CColorCorrectionLayer

**Derived by:** [CBloomLayer](resourcecompiler.md#cbloomlayer), [CBrightnessContrastColorCorrectionLayer](resourcecompiler.md#cbrightnesscontrastcolorcorrectionlayer), [CColorBalanceColorCorrectionLayer](resourcecompiler.md#ccolorbalancecolorcorrectionlayer), [CColorLookupColorCorrectionLayer](resourcecompiler.md#ccolorlookupcolorcorrectionlayer), [CColorTintColorCorrectionLayer](resourcecompiler.md#ccolortintcolorcorrectionlayer), [CCurvesColorCorrectionLayer](resourcecompiler.md#ccurvescolorcorrectionlayer), [CFogScatteringLayer](resourcecompiler.md#cfogscatteringlayer), [CHueSaturationColorCorrectionLayer](resourcecompiler.md#chuesaturationcolorcorrectionlayer), [CLevelsColorCorrectionLayer](resourcecompiler.md#clevelscolorcorrectionlayer), [CLocalContrastLayer](resourcecompiler.md#clocalcontrastlayer), [CToneMappingLayer](resourcecompiler.md#ctonemappinglayer), [CVibranceColorCorrectionLayer](resourcecompiler.md#cvibrancecolorcorrectionlayer), [CVignetteLayer](resourcecompiler.md#cvignettelayer)

**Metadata:** `MGetKV3ClassDefaults Could not parse KV3 Defaults`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CBloomLayer
    CColorCorrectionLayer <|-- CFogScatteringLayer
    CColorCorrectionLayer <|-- CColorBalanceColorCorrectionLayer
    CColorCorrectionLayer <|-- CVignetteLayer
    CColorCorrectionLayer <|-- CHueSaturationColorCorrectionLayer
    CColorCorrectionLayer <|-- CColorTintColorCorrectionLayer
    CColorCorrectionLayer <|-- CLevelsColorCorrectionLayer
    CColorCorrectionLayer <|-- CToneMappingLayer
    CColorCorrectionLayer <|-- CColorLookupColorCorrectionLayer
    CColorCorrectionLayer <|-- CCurvesColorCorrectionLayer
    CColorCorrectionLayer <|-- CBrightnessContrastColorCorrectionLayer
    CColorCorrectionLayer <|-- CLocalContrastLayer
    CColorCorrectionLayer <|-- CVibranceColorCorrectionLayer
    CColorCorrectionLayer --> CLayerMask
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_name` | CUtlString |  |
| `m_nOpacityPercent` | int32 |  |
| `m_bVisible` | bool |  |
| `m_pLayerMask` | [CLayerMask](../schemas/resourcecompiler.md#clayermask)* |  |

### CColorLookupColorCorrectionLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CColorLookupColorCorrectionLayer",
	"m_name": "Lookup Table 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_fileName": "",
	"m_lut":
	[
	],
	"m_nDim": 0
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CColorLookupColorCorrectionLayer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_fileName` | CUtlString |  |
| `m_lut` | CUtlVector<float32> |  |
| `m_nDim` | int32 |  |

### CColorTintColorCorrectionLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CColorTintColorCorrectionLayer",
	"m_name": "Color Tint 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_nTintColorR": 255,
	"m_nTintColorG": 150,
	"m_nTintColorB": 20,
	"m_nStrength": 20,
	"m_bPreserveLuminosity": true
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CColorTintColorCorrectionLayer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nTintColorR` | int32 |  |
| `m_nTintColorG` | int32 |  |
| `m_nTintColorB` | int32 |  |
| `m_nStrength` | int32 |  |
| `m_bPreserveLuminosity` | bool |  |

### CCurvesColorCorrectionLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CCurvesColorCorrectionLayer",
	"m_name": "Curves 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_curvePointsRGB":
	[
		[
			0.000000,
			0.000000
		],
		[
			255.000000,
			255.000000
		]
	],
	"m_curvePointsR":
	[
		[
			0.000000,
			0.000000
		],
		[
			255.000000,
			255.000000
		]
	],
	"m_curvePointsG":
	[
		[
			0.000000,
			0.000000
		],
		[
			255.000000,
			255.000000
		]
	],
	"m_curvePointsB":
	[
		[
			0.000000,
			0.000000
		],
		[
			255.000000,
			255.000000
		]
	]
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CCurvesColorCorrectionLayer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_curvePointsRGB` | CUtlVector<Vector2D> |  |
| `m_curvePointsR` | CUtlVector<Vector2D> |  |
| `m_curvePointsG` | CUtlVector<Vector2D> |  |
| `m_curvePointsB` | CUtlVector<Vector2D> |  |

### CFogScatteringLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CFogScatteringLayer",
	"m_name": "Fog Scattering 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_params":
	{
		"m_fRadius": 0.750000,
		"m_fScale": 0.000000,
		"m_fCubemapScale": 1.000000,
		"m_fVolumetricScale": 1.000000,
		"m_fGradientScale": 1.000000
	}
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CFogScatteringLayer
    CFogScatteringLayer *-- PostProcessingFogScatteringParameters_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_params` | [PostProcessingFogScatteringParameters_t](../schemas/materialsystem2.md#postprocessingfogscatteringparameters_t) |  |

### CHueSaturationColorCorrectionLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CHueSaturationColorCorrectionLayer",
	"m_name": "Hue/Saturation 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_nHueMaster": 0,
	"m_nHueRed": 0,
	"m_nHueYellow": 0,
	"m_nHueGreen": 0,
	"m_nHueCyan": 0,
	"m_nHueBlue": 0,
	"m_nHueMagenta": 0,
	"m_nSaturationMaster": 0,
	"m_nSaturationRed": 0,
	"m_nSaturationYellow": 0,
	"m_nSaturationGreen": 0,
	"m_nSaturationCyan": 0,
	"m_nSaturationBlue": 0,
	"m_nSaturationMagenta": 0,
	"m_nBrightnessMaster": 0,
	"m_nBrightnessRed": 0,
	"m_nBrightnessYellow": 0,
	"m_nBrightnessGreen": 0,
	"m_nBrightnessCyan": 0,
	"m_nBrightnessBlue": 0,
	"m_nBrightnessMagenta": 0
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CHueSaturationColorCorrectionLayer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nHueMaster` | int32 |  |
| `m_nHueRed` | int32 |  |
| `m_nHueYellow` | int32 |  |
| `m_nHueGreen` | int32 |  |
| `m_nHueCyan` | int32 |  |
| `m_nHueBlue` | int32 |  |
| `m_nHueMagenta` | int32 |  |
| `m_nSaturationMaster` | int32 |  |
| `m_nSaturationRed` | int32 |  |
| `m_nSaturationYellow` | int32 |  |
| `m_nSaturationGreen` | int32 |  |
| `m_nSaturationCyan` | int32 |  |
| `m_nSaturationBlue` | int32 |  |
| `m_nSaturationMagenta` | int32 |  |
| `m_nBrightnessMaster` | int32 |  |
| `m_nBrightnessRed` | int32 |  |
| `m_nBrightnessYellow` | int32 |  |
| `m_nBrightnessGreen` | int32 |  |
| `m_nBrightnessCyan` | int32 |  |
| `m_nBrightnessBlue` | int32 |  |
| `m_nBrightnessMagenta` | int32 |  |

### CLayerMask

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CLayerMask",
	"m_nLumMaskCenter": 128,
	"m_nLumMaskWidth": 82,
	"m_nLumMaskShape": 0,
	"m_bInverted": false
}`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nLumMaskCenter` | int32 |  |
| `m_nLumMaskWidth` | int32 |  |
| `m_nLumMaskShape` | int32 |  |
| `m_bInverted` | bool |  |

### CLevelsColorCorrectionLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CLevelsColorCorrectionLayer",
	"m_name": "Levels 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_nInputBlackPointRGB": 0,
	"m_nInputBlackPointR": 0,
	"m_nInputBlackPointG": 0,
	"m_nInputBlackPointB": 0,
	"m_nInputWhitePointRGB": 255,
	"m_nInputWhitePointR": 255,
	"m_nInputWhitePointG": 255,
	"m_nInputWhitePointB": 255,
	"m_nOutputBlackPointRGB": 0,
	"m_nOutputBlackPointR": 0,
	"m_nOutputBlackPointG": 0,
	"m_nOutputBlackPointB": 0,
	"m_nOutputWhitePointRGB": 255,
	"m_nOutputWhitePointR": 255,
	"m_nOutputWhitePointG": 255,
	"m_nOutputWhitePointB": 255,
	"m_flGammaRGB": 1.000000,
	"m_flGammaR": 1.000000,
	"m_flGammaG": 1.000000,
	"m_flGammaB": 1.000000
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CLevelsColorCorrectionLayer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nInputBlackPointRGB` | int32 |  |
| `m_nInputBlackPointR` | int32 |  |
| `m_nInputBlackPointG` | int32 |  |
| `m_nInputBlackPointB` | int32 |  |
| `m_nInputWhitePointRGB` | int32 |  |
| `m_nInputWhitePointR` | int32 |  |
| `m_nInputWhitePointG` | int32 |  |
| `m_nInputWhitePointB` | int32 |  |
| `m_nOutputBlackPointRGB` | int32 |  |
| `m_nOutputBlackPointR` | int32 |  |
| `m_nOutputBlackPointG` | int32 |  |
| `m_nOutputBlackPointB` | int32 |  |
| `m_nOutputWhitePointRGB` | int32 |  |
| `m_nOutputWhitePointR` | int32 |  |
| `m_nOutputWhitePointG` | int32 |  |
| `m_nOutputWhitePointB` | int32 |  |
| `m_flGammaRGB` | float32 |  |
| `m_flGammaR` | float32 |  |
| `m_flGammaG` | float32 |  |
| `m_flGammaB` | float32 |  |

### CLocalContrastLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CLocalContrastLayer",
	"m_name": "Local Contrast 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_params":
	{
		"m_flLocalContrastStrength": 0.000000,
		"m_flLocalContrastEdgeStrength": 0.000000,
		"m_flLocalContrastVignetteStart": 0.000000,
		"m_flLocalContrastVignetteEnd": 0.000000,
		"m_flLocalContrastVignetteBlur": 0.000000
	}
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CLocalContrastLayer
    CLocalContrastLayer *-- PostProcessingLocalContrastParameters_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_params` | [PostProcessingLocalContrastParameters_t](../schemas/materialsystem2.md#postprocessinglocalcontrastparameters_t) |  |

### CPostProcessData

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CPostProcessData",
	"m_layers":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    CPostProcessData --> CColorCorrectionLayer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_layers` | CUtlVector<[CColorCorrectionLayer](../schemas/resourcecompiler.md#ccolorcorrectionlayer)*> |  |

### CToneMappingLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CToneMappingLayer",
	"m_name": "Tone Mapping 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_params":
	{
		"m_flExposureBias": 0.000000,
		"m_flShoulderStrength": 0.150000,
		"m_flLinearStrength": 0.500000,
		"m_flLinearAngle": 0.100000,
		"m_flToeStrength": 0.200000,
		"m_flToeNum": 0.020000,
		"m_flToeDenom": 0.300000,
		"m_flWhitePoint": 4.000000,
		"m_flLuminanceSource": 0.000000,
		"m_flExposureBiasShadows": 0.000000,
		"m_flExposureBiasHighlights": 0.000000,
		"m_flMinShadowLum": 0.000000,
		"m_flMaxShadowLum": 0.500000,
		"m_flMinHighlightLum": 2.000000,
		"m_flMaxHighlightLum": 8.000000
	}
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CToneMappingLayer
    CToneMappingLayer *-- PostProcessingTonemapParameters_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_params` | [PostProcessingTonemapParameters_t](../schemas/materialsystem2.md#postprocessingtonemapparameters_t) |  |

### CVibranceColorCorrectionLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CVibranceColorCorrectionLayer",
	"m_name": "Saturation/Vibrance 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_nVibrance": 0,
	"m_nSaturation": 0
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CVibranceColorCorrectionLayer
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nVibrance` | int32 |  |
| `m_nSaturation` | int32 |  |

### CVignetteLayer

**Inherits from:** [CColorCorrectionLayer](resourcecompiler.md#ccolorcorrectionlayer)

**Metadata:** `MGetKV3ClassDefaults {
	"_class": "CVignetteLayer",
	"m_name": "Vignette 1",
	"m_nOpacityPercent": 100,
	"m_bVisible": true,
	"m_pLayerMask": null,
	"m_params":
	{
		"m_flVignetteStrength": 0.000000,
		"m_vCenter":
		[
			0.000000,
			0.000000
		],
		"m_flRadius": 0.500000,
		"m_flRoundness": 1.000000,
		"m_flFeather": 0.500000,
		"m_vColorTint":
		[
			1.000000,
			1.000000,
			1.000000
		]
	}
}`

**Relationships:**

```mermaid
classDiagram
    CColorCorrectionLayer <|-- CVignetteLayer
    CVignetteLayer *-- PostProcessingVignetteParameters_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_params` | [PostProcessingVignetteParameters_t](../schemas/materialsystem2.md#postprocessingvignetteparameters_t) |  |

### LayerMaskType_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `LAYER_MASK_LUMINOSITY` | 0 |  |
| `LAYER_MASK_COLOR_RANGE` | 1 |  |

### LayerType_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `LAYER_TYPE_LEVELS` | 0 |  |
| `LAYER_TYPE_VIBRANCE` | 1 |  |
| `LAYER_TYPE_BRIGHTNESS_CONTRAST` | 2 |  |
| `LAYER_TYPE_LUT` | 3 |  |
| `LAYER_TYPE_COLOR_BALANCE` | 4 |  |
| `LAYER_TYPE_COLOR_TINT` | 5 |  |
| `LAYER_TYPE_HUE_SATURATION` | 6 |  |
| `LAYER_TYPE_CURVES` | 7 |  |
| `LAYER_TYPE_TONEMAPPING` | 8 |  |
| `LAYER_TYPE_BLOOM` | 9 |  |
| `LAYER_TYPE_VIGNETTE` | 10 |  |
| `LAYER_TYPE_LOCAL_CONTRAST` | 11 |  |
| `LAYER_TYPE_FOG_SCATTERING` | 12 |  |
| `MAX_LAYER_TYPES` | 13 |  |
