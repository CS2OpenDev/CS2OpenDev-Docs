---
layout: default
title: navlib
parent: Schemas
nav_exclude: true
---

# Module: navlib

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

[📊 View UML Diagram](../diagrams/navlib.md)

17 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CNavAttribute](navlib/CNavAttribute.md) | class | 8 | 0 | [CNavFlags](navlib/CNavFlags.md) |
| [CNavFlags](navlib/CNavFlags.md) | class | 8 | 1 |  |
| [CNavHullPresetVData](navlib/CNavHullPresetVData.md) | class | 24 | 1 |  |
| [CNavHullVData](navlib/CNavHullVData.md) | class | 60 | 15 |  |
| [CNavPathCost](navlib/CNavPathCost.md) | class | 48 | 12 | [INavPathCost](navlib/INavPathCost.md) |
| [CNavVolume](navlib/CNavVolume.md) | class | 120 | 0 |  |
| [CNavVolumeAll](navlib/CNavVolumeAll.md) | class | 160 | 0 | [CNavVolumeVector](navlib/CNavVolumeVector.md) |
| [CNavVolumeSphere](navlib/CNavVolumeSphere.md) | class | 136 | 2 | [CNavVolume](navlib/CNavVolume.md) |
| [CNavVolumeSphericalShell](navlib/CNavVolumeSphericalShell.md) | class | 144 | 1 | [CNavVolumeSphere](navlib/CNavVolumeSphere.md) |
| [CNavVolumeVector](navlib/CNavVolumeVector.md) | class | 160 | 1 | [CNavVolume](navlib/CNavVolume.md) |
| [Extent](navlib/Extent.md) | class | 24 | 2 |  |
| [INavPathCost](navlib/INavPathCost.md) | class | 16 | 1 |  |
| [NavGravity_t](navlib/NavGravity_t.md) | class | 16 | 2 |  |
| [NavHull_t](navlib/NavHull_t.md) | class | 4 | 1 |  |
| [NavAttributeDynamicType](navlib/NavAttributeDynamicType.md) | enum | — | 22 |  |
| [NavAttributeEnum](navlib/NavAttributeEnum.md) | enum | — | 20 |  |
| [NavDirType](navlib/NavDirType.md) | enum | — | 5 |  |
