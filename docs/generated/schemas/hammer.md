---
layout: default
title: hammer
parent: Schemas
nav_exclude: true
---

# Module: hammer

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [ColorOptionsEditableData_t](#coloroptionseditabledata_t) | class |  | 9 |
| [GeneralOptionsEditableData_t](#generaloptionseditabledata_t) | class |  | 16 |
| [ImportExportOptionsEditableData_t](#importexportoptionseditabledata_t) | class |  | 6 |
| [ImportExportOptionsEditableData_t::ExportDefaultFormat_t](#importexportoptionseditabledata_texportdefaultformat_t) | enum |  | 3 |
| [ImportExportOptionsEditableData_t::ExportEncoding_t](#importexportoptionseditabledata_texportencoding_t) | enum |  | 2 |
| [ImportExportOptionsEditableData_t::ExportFbxUnit_t](#importexportoptionseditabledata_texportfbxunit_t) | enum |  | 2 |
| [TexturesOptionsEditableData_t](#texturesoptionseditabledata_t) | class |  | 1 |
| [ToolsOptionsEditableData_t](#toolsoptionseditabledata_t) | class |  | 9 |
| [View2DOptionsEditableData_t](#view2doptionseditabledata_t) | class |  | 4 |
| [View3DOptionsEditableData_t](#view3doptionseditabledata_t) | class |  | 21 |

---

### ColorOptionsEditableData_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `bUseCustom` | bool | `MPropertyFriendlyName "Use Custom Colors"` |
| `bWhiteOnBlack` | bool | `MPropertyFriendlyName "White on black"` |
| `clrGrid` | Color | `MPropertyFriendlyName "Grid Color"` |
| `clrGridFractional` | Color | `MPropertyFriendlyName "Grid Color for sub 1-unit lines"` |
| `clrGrid10` | Color | `MPropertyFriendlyName "Grid Color for every 10th line"` |
| `clrGrid1024` | Color | `MPropertyFriendlyName "Grid Color for every 1024 units line"` |
| `clrBrush` | Color | `MPropertyFriendlyName "Brush Color"` |
| `clrSelection` | Color | `MPropertyFriendlyName "Color of the selected brushes"` |
| `clrToolSelection` | Color | `MPropertyFriendlyName "Color of the selection tool"` |

### GeneralOptionsEditableData_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `iUndoLevels` | int32 | `MPropertyFriendlyName "Maximum number of undo levels"` |
| `bSaveChangesOnBuildMap` | bool | `MPropertyFriendlyName "Save changes when building map"` |
| `bRenderFullyUnlitAsFullbright` | bool | `MPropertyFriendlyName "Render unlit maps as fullbright"` |
| `bShowSelectionModeChangeNotificationIcons` | bool | `MPropertyFriendlyName "Show selection mode notification icons"` |
| `bShowToolChangeNotificationIcons` | bool | `MPropertyFriendlyName "Show tool notification icons"` |
| `bPauseGameOnActivate` | bool | `MPropertyFriendlyName "Pause the game when hammer is activated"` |
| `SolidEntity` | CUtlString | `MPropertyFriendlyName "Default solid entity to create when using tie to entity"` |
| `PointEntity` | CUtlString | `MPropertyFriendlyName "Default point entity to select in the entity tool"` |
| `PathEntity` | CUtlString | `MPropertyFriendlyName "Default path entity to select in the path tool"` |
| `bReportMapCompileCrashes` | bool | `MPropertyFriendlyName "Report crashes during map compile"` |
| `bViewFocusStealing` | bool | `MPropertyFriendlyName "Steal focus on mouse hover"` |
| `bMoveSelectedEnabled` | bool | `MPropertyFriendlyName "Allow drag move of selected objects"` |
| `bPreviewMotionExtraction` | bool | `MPropertyFriendlyName "Apply extracted motion when previewing animations"` |
| `nViewportFontSize` | int32 | `MPropertyFriendlyName "Font size for text in 2d and 3d viewports"` |
| `flVertexSnapRadius` | float32 | `MPropertyFriendlyName "Radius to use when snapping to vertex"` |
| `m_bForceStaticPropsForModelDrags` | bool | `MPropertyFriendlyName "Force model drag-and-drop to create prop_static"` |

### ImportExportOptionsEditableData_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `bExportProps` | bool | `MPropertyFriendlyName "Export Props"` |
| `bExportHidden` | bool | `MPropertyFriendlyName "Export Hidden Objects"` |
| `bExportFbxEmbedTextures` | bool | `MPropertyFriendlyName "Export FBX Embed Textures From Content If Available"` `MPropertySuppressField` |
| `nExportFbxUnit` | [ImportExportOptionsEditableData_t](../schemas/hammer.md#importexportoptionseditabledata_t)::ExportFbxUnit_t | `MPropertyFriendlyName "Export Hammer Units To FBX Units"` |
| `nExportDefaultFormat` | [ImportExportOptionsEditableData_t](../schemas/hammer.md#importexportoptionseditabledata_t)::ExportDefaultFormat_t | `MPropertyFriendlyName "Export Default Format"` |
| `nExportEncoding` | [ImportExportOptionsEditableData_t](../schemas/hammer.md#importexportoptionseditabledata_t)::ExportEncoding_t | `MPropertyFriendlyName "Export Encoding"` |

### ImportExportOptionsEditableData_t::ExportDefaultFormat_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `DEFAULT_FORMAT_DMX` | 0 | DMX |
| `DEFAULT_FORMAT_OBJ` | 1 | OBJ |
| `DEFAULT_FORMAT_FBX` | 2 | FBX |

### ImportExportOptionsEditableData_t::ExportEncoding_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `EXPORT_ENCODING_TEXT` | 0 | Text |
| `EXPORT_ENCODING_BINARY` | 1 | Binary |

### ImportExportOptionsEditableData_t::ExportFbxUnit_t

**Values:**

| Name | Value | Description |
|------|-------|-------------|
| `FBX_UNIT_CENTIMETERS` | 0 | Centimeters |
| `FBX_UNIT_INCHES` | 1 | Inches |

### TexturesOptionsEditableData_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_DefaultMaterialName` | CUtlString | `MPropertyFriendlyName "Default Material Name"` `MPropertyAttributeEditor "AssetBrowse( vmat )"` |

### ToolsOptionsEditableData_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `bTranslateToolAlignToSurface` | bool | `MPropertyFriendlyName "Translate Tool Align To Surface"` |
| `bRotateToolUseRelativeMode` | bool | `MPropertyFriendlyName "Rotate Tool Use Relative Mode"` |
| `bPivotToolSnapToBBox` | bool | `MPropertyFriendlyName "Pivot Tool Snap To Bounding Box"` |
| `bEdgeSelectionPreviewEdgeLength` | bool | `MPropertyFriendlyName "Show edge length on edge selection preview"` |
| `bShowSelectionBounds` | bool | `MPropertyFriendlyName "Show selection bounding box"` |
| `bShowSelectionDimensions` | bool | `MPropertyFriendlyName "Show selection dimensions"` |
| `bShowSelectedEdgeAngles` | bool | `MPropertyFriendlyName "Show angles between selected edge pairs"` |
| `bShowTranslationDistance` | bool | `MPropertyFriendlyName "Show distance when using the translation gizmo"` |
| `bConvertMeshHardEdgesFromUVBoundaries` | bool | `MPropertyFriendlyName "Set hard edges from UVs when converting a model to a mesh"` |

### View2DOptionsEditableData_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `bNudge` | bool | `MPropertyFriendlyName "Enable Nudge"` |
| `bUsegroupcolors` | bool | `MPropertyFriendlyName "Use group colors for brush color"` |
| `iGridIntensity` | int32 | `MPropertyFriendlyName "Grid Intensity"` |
| `bShowEntityNames` | bool | `MPropertyFriendlyName "Show Entity names"` |

### View3DOptionsEditableData_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `bReverseY` | bool | `MPropertyFriendlyName "Reverse Y"` |
| `flPanSpeed` | float32 | `MPropertyFriendlyName "Pan Speed"` |
| `flRotationScale` | float32 | `MPropertyFriendlyName "Rotation scale"` |
| `nForwardSpeedMax` | int32 | `MPropertyFriendlyName "Forward speed max (world units/sec)"` |
| `nTimeToMaxSpeed` | int32 | `MPropertyFriendlyName "Time to max speed (ms)"` |
| `flFOV` | int32 | `MPropertyFriendlyName "Field of View (degrees)"` |
| `szResolutionGate` | CUtlString | `MPropertyFriendlyName "Resolution Gate"` |
| `iBackPlane` | int32 | `MPropertyFriendlyName "Backplane distance"` |
| `flNearPlane` | float32 | `MPropertyFriendlyName "Nearplane distance"` |
| `flShadowFarPlane` | float32 | `MPropertyFriendlyName "Default light_environment draw distance"` |
| `bMouseWheelControlsFarPlane` | bool | `MPropertyFriendlyName "Alt+Mouse wheel adjusts backplane distance"` |
| `nMouseMoveZoomSensitivity` | int32 | `MPropertyFriendlyName "Zoom sensitivity using mouse move"` |
| `nMouseWheelZoomSensitivity` | int32 | `MPropertyFriendlyName "Zoom sensitivity using mousewheel"` |
| `nCameraTargetDist` | int32 | `MPropertyFriendlyName "Default distance of camera from point it is set to center view on"` |
| `iGridIntensity` | int32 | `MPropertyFriendlyName "Grid Intensity"` |
| `fSelectionOverlayAlpha` | float32 | `MPropertyFriendlyName "Alpha of selection mask (0..1)"` |
| `bShowSelectionOutline` | bool | `MPropertyFriendlyName "Outline selected objects"` |
| `bSelectionOutlineDepth` | bool | `MPropertyFriendlyName "Use depth for selection outline"` |
| `fToolsVisSSAORadiusScale` | float32 | `MPropertyFriendlyName "Unlit SSAO Radius Scale"` |
| `fToolsVisSSAOPowerScale` | float32 | `MPropertyFriendlyName "Unlit SSAO Power Scale"` |
| `bPostProcessingEnabled` | bool | `MPropertyFriendlyName "Enable Post Processing"` |
