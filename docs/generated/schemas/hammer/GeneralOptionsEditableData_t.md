---
layout: default
title: GeneralOptionsEditableData_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [hammer](../hammer.md) / GeneralOptionsEditableData_t

# GeneralOptionsEditableData_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** n/a (unspecified) · **Module:** hammer

## Memory layout

16 fields (16 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `iUndoLevels` | int32 |  | `MPropertyFriendlyName Maximum number of undo levels` |
| `0x4` | `bSaveChangesOnBuildMap` | bool |  | `MPropertyFriendlyName Save changes when building map` |
| `0x5` | `bRenderFullyUnlitAsFullbright` | bool |  | `MPropertyFriendlyName Render unlit maps as fullbright` |
| `0x6` | `bShowSelectionModeChangeNotificationIcons` | bool |  | `MPropertyFriendlyName Show selection mode notification icons` |
| `0x7` | `bShowToolChangeNotificationIcons` | bool |  | `MPropertyFriendlyName Show tool notification icons` |
| `0x8` | `bPauseGameOnActivate` | bool |  | `MPropertyFriendlyName Pause the game when hammer is activated` |
| `0x10` | `SolidEntity` | CUtlString |  | `MPropertyFriendlyName Default solid entity to create when using tie to entity` |
| `0x18` | `PointEntity` | CUtlString |  | `MPropertyFriendlyName Default point entity to select in the entity tool` |
| `0x20` | `PathEntity` | CUtlString |  | `MPropertyFriendlyName Default path entity to select in the path tool` |
| `0x28` | `bReportMapCompileCrashes` | bool |  | `MPropertyFriendlyName Report crashes during map compile` |
| `0x29` | `bViewFocusStealing` | bool |  | `MPropertyFriendlyName Steal focus on mouse hover` |
| `0x2a` | `bMoveSelectedEnabled` | bool |  | `MPropertyFriendlyName Allow drag move of selected objects` |
| `0x2b` | `bPreviewMotionExtraction` | bool |  | `MPropertyFriendlyName Apply extracted motion when previewing animations` |
| `0x2c` | `nViewportFontSize` | int32 |  | `MPropertyFriendlyName Font size for text in 2d and 3d viewports` |
| `0x30` | `flVertexSnapRadius` | float32 |  | `MPropertyFriendlyName Radius to use when snapping to vertex` |
| `0x34` | `m_bForceStaticPropsForModelDrags` | bool |  | `MPropertyFriendlyName Force model drag-and-drop to create prop_static` |
