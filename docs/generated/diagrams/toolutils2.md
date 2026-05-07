---
layout: default
title: "UML: toolutils2"
parent: Schemas
nav_exclude: true
---

# UML: toolutils2

Class relationships (inheritance and composition) for the `toolutils2` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CSimpleAssetTypeInfo <|-- CVMMDAssetTypeInfo
    CSimpleAssetTypeInfo <|-- CResourceAssetTypeInfo
    CSimpleAssetTypeInfo <|-- CBitmapAssetTypeInfo
    CResourceAssetTypeInfo <|-- CMapAssetTypeInfo
    CBaseToolInfo <|-- CEngineToolInfo
    CBaseToolInfo <|-- CExternalToolInfo
    CAssetWarningCheck *-- AssetWarningFixType_t
    CResourceAssetTypeInfo *-- ResourceBlockTypeInfo_t
    CToolsConfig *-- CEngineToolInfo
    CToolsConfig *-- CExternalToolInfo
    ResourceBlockTypeInfo_t *-- ResourceDataEncodingType_t
    CAssetTagInfo *-- AutoTagVDataCondition_t
    CAssetTypeConfig --> CSimpleAssetTypeInfo
    CAssetTypeConfig --> CSubassetTypeInfo
    CAssetTypeConfig --> CAssetWarning
    CDetailPropType *-- CDetailPropModel
    CModuleManifests *-- CManifestInfo
    CSimpleAssetTypeInfo *-- AssetEngineCommand_t
    CAssetWarning *-- CAssetWarningCheck
```
