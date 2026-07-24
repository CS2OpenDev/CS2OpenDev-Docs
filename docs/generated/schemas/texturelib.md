---
layout: default
title: texturelib
parent: Schemas
nav_exclude: true
---

# Module: texturelib

[📊 View UML Diagram](../diagrams/texturelib.md)

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [CTextureSheetDoc](#ctexturesheetdoc) | class |  | 5 |
| [CTextureSheetDoc_Frame](#ctexturesheetdoc_frame) | class |  | 7 |
| [CTextureSheetDoc_Sequence](#ctexturesheetdoc_sequence) | class |  | 5 |
| [CTextureSheetDoc_SequenceDecalParams](#ctexturesheetdoc_sequencedecalparams) | class |  | 9 |

---

### CTextureSheetDoc

**Metadata:** `MGetKV3ClassDefaults {
	"m_ePackingMode": "PCKM_FLAT",
	"m_NumMips": 2,
	"m_bHasDecalParams": false,
	"m_sLayoutOwnerSheet": "",
	"m_Sequences":
	{
	},
	"generic_data_type": "CTextureSheetDoc"
}`, `MVDataFileExtension mks`, `MVDataPreviewWidget sheet_file_preview`, `MVDataRoot`, `MVDataSingleton`

**Relationships:**

```mermaid
classDiagram
    CTextureSheetDoc *-- PackingMode_t
    CTextureSheetDoc --> CTextureSheetDoc_Sequence
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_ePackingMode` | [PackingMode_t](../schemas/!GlobalTypes.md#packingmode_t) |  |
| `m_NumMips` | int32 |  |
| `m_bHasDecalParams` | bool | `MPropertySuppressExpr m_sLayoutOwnerSheet != "" ` |
| `m_sLayoutOwnerSheet` | CUtlString | `MPropertyAttributeEditor AssetBrowse( mks )` |
| `m_Sequences` | CUtlStringMap< [CTextureSheetDoc_Sequence](../schemas/texturelib.md#ctexturesheetdoc_sequence)* > | `MVDataPromoteField 1` |

### CTextureSheetDoc_Frame

**Metadata:** `MGetKV3ClassDefaults {
	"m_sImageName": "",
	"m_fDisplayTime": 1.000000,
	"m_bCropEnabled": false,
	"m_srcCropXStart": -1,
	"m_srcCropYStart": -1,
	"m_srcCropXEnd": -1,
	"m_srcCropYEnd": -1
}`, `MPropertyAutoExpandSelf`, `MPropertyCustomEditor SheetSequenceFrame`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_sImageName` | CUtlString |  |
| `m_fDisplayTime` | float32 |  |
| `m_bCropEnabled` | bool |  |
| `m_srcCropXStart` | int32 |  |
| `m_srcCropYStart` | int32 |  |
| `m_srcCropXEnd` | int32 |  |
| `m_srcCropYEnd` | int32 |  |

### CTextureSheetDoc_Sequence

**Metadata:** `MGetKV3ClassDefaults {
	"m_ChannelMode": "RGBA",
	"m_LoopMode": "CLAMP",
	"m_AlphaCropMode": "NONE",
	"m_DecalParams":
	{
		"m_flScale": 1.000000,
		"m_flDepth": 4.000000,
		"m_flScaleVariation": 0.250000,
		"m_flStartFadeTime": 10.000000,
		"m_flFadeDuration": 3.000000,
		"m_flAnimationScale": 1.000000,
		"m_flAnimationStartTime": 0.000000,
		"m_flAlignWithGravityFactor": 0.000000,
		"m_nDecalRtEncoding": "kDecalInvalid"
	},
	"m_Frames":
	[
	]
}`

**Relationships:**

```mermaid
classDiagram
    CTextureSheetDoc_Sequence *-- SequenceChannelMode_t
    CTextureSheetDoc_Sequence *-- SequenceLoopMode_t
    CTextureSheetDoc_Sequence *-- SequenceAlphaCropMode_t
    CTextureSheetDoc_Sequence *-- CTextureSheetDoc_SequenceDecalParams
    CTextureSheetDoc_Sequence *-- CTextureSheetDoc_Frame
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_ChannelMode` | [SequenceChannelMode_t](../schemas/!GlobalTypes.md#sequencechannelmode_t) | `MPropertyAutoRebuildOnChange` |
| `m_LoopMode` | [SequenceLoopMode_t](../schemas/!GlobalTypes.md#sequenceloopmode_t) |  |
| `m_AlphaCropMode` | [SequenceAlphaCropMode_t](../schemas/!GlobalTypes.md#sequencealphacropmode_t) |  |
| `m_DecalParams` | [CTextureSheetDoc_SequenceDecalParams](../schemas/texturelib.md#ctexturesheetdoc_sequencedecalparams) | `MPropertySuppressExpr !__SheetFileHasDecalParams` |
| `m_Frames` | CUtlVector< [CTextureSheetDoc_Frame](../schemas/texturelib.md#ctexturesheetdoc_frame) > | `MPropertyAutoExpandSelf` |

### CTextureSheetDoc_SequenceDecalParams

**Metadata:** `MGetKV3ClassDefaults {
	"m_flScale": 1.000000,
	"m_flDepth": 4.000000,
	"m_flScaleVariation": 0.250000,
	"m_flStartFadeTime": 10.000000,
	"m_flFadeDuration": 3.000000,
	"m_flAnimationScale": 1.000000,
	"m_flAnimationStartTime": 0.000000,
	"m_flAlignWithGravityFactor": 0.000000,
	"m_nDecalRtEncoding": "kDecalInvalid"
}`, `MPropertyAutoExpandSelf`

**Relationships:**

```mermaid
classDiagram
    CTextureSheetDoc_SequenceDecalParams *-- DecalRtEncoding_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flScale` | float32 |  |
| `m_flDepth` | float32 |  |
| `m_flScaleVariation` | float32 |  |
| `m_flStartFadeTime` | float32 |  |
| `m_flFadeDuration` | float32 |  |
| `m_flAnimationScale` | float32 |  |
| `m_flAnimationStartTime` | float32 |  |
| `m_flAlignWithGravityFactor` | float32 |  |
| `m_nDecalRtEncoding` | [DecalRtEncoding_t](../schemas/!GlobalTypes.md#decalrtencoding_t) |  |
