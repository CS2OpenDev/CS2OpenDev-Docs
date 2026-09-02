---
layout: default
title: scenesystem
parent: Schemas
nav_exclude: true
---

# Module: scenesystem

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

[📊 View UML Diagram](../diagrams/scenesystem.md)

15 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CSSDSEndFrameViewInfo](scenesystem/CSSDSEndFrameViewInfo.md) | class | 16 | 2 |  |
| [CSSDSMsg_EndFrame](scenesystem/CSSDSMsg_EndFrame.md) | class | 24 | 1 |  |
| [CSSDSMsg_LayerBase](scenesystem/CSSDSMsg_LayerBase.md) | class | 48 | 5 |  |
| [CSSDSMsg_PostLayer](scenesystem/CSSDSMsg_PostLayer.md) | class | 48 | 0 | [CSSDSMsg_LayerBase](scenesystem/CSSDSMsg_LayerBase.md) |
| [CSSDSMsg_PreLayer](scenesystem/CSSDSMsg_PreLayer.md) | class | 48 | 0 | [CSSDSMsg_LayerBase](scenesystem/CSSDSMsg_LayerBase.md) |
| [CSSDSMsg_ViewRender](scenesystem/CSSDSMsg_ViewRender.md) | class | 24 | 2 |  |
| [CSSDSMsg_ViewTarget](scenesystem/CSSDSMsg_ViewTarget.md) | class | 48 | 10 |  |
| [CSSDSMsg_ViewTargetList](scenesystem/CSSDSMsg_ViewTargetList.md) | class | 48 | 3 |  |
| [SceneViewId_t](scenesystem/SceneViewId_t.md) | class | 16 | 2 |  |
| [DecalRtEncoding_t](scenesystem/DecalRtEncoding_t.md) | enum | — | 6 |  |
| [DisableShadows_t](scenesystem/DisableShadows_t.md) | enum | — | 5 |  |
| [ESceneObjectMeshletVisualization](scenesystem/ESceneObjectMeshletVisualization.md) | enum | — | 3 |  |
| [ESceneObjectVisualization](scenesystem/ESceneObjectVisualization.md) | enum | — | 6 |  |
| [ESceneViewDebugOverlaysListenerDataType_t](scenesystem/ESceneViewDebugOverlaysListenerDataType_t.md) | enum | — | 7 |  |
| [ESilhouetteType_t](scenesystem/ESilhouetteType_t.md) | enum | — | 4 |  |
