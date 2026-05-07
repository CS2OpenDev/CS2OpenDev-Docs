---
layout: default
title: "UML: worldrenderer"
parent: Schemas
nav_exclude: true
---

# UML: worldrenderer

Class relationships (inheritance and composition) for the `worldrenderer` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    BaseSceneObjectOverride_t <|-- MaterialOverride_t
    BaseSceneObjectOverride_t <|-- ExtraVertexStreamOverride_t
    CVoxelVisibility *-- VoxelVisBlockOffset_t
    EntityKeyValueData_t *-- EntityIOConnectionData_t
    AggregateRTProxySceneObject_t *-- RTProxyBLAS_t
    AggregateRTProxySceneObject_t *-- RTProxyInstanceInfo_t
    World_t *-- WorldBuilderParams_t
    World_t *-- NodeData_t
    World_t *-- BakedLightingInfo_t
    AggregateMeshInfo_t *-- ObjectTypeFlags_t
    AggregateMeshInfo_t *-- AggregateInstanceStream_t
    WorldNode_t *-- SceneObject_t
    WorldNode_t *-- AggregateSceneObject_t
    WorldNode_t *-- ClutterSceneObject_t
    WorldNode_t *-- AggregateRTProxySceneObject_t
    WorldNode_t *-- ExtraVertexStreamOverride_t
    WorldNode_t *-- MaterialOverride_t
    WorldNode_t *-- WorldNodeOnDiskBufferData_t
    WorldNode_t *-- AggregateInstanceStreamOnDiskData_t
    WorldNode_t *-- AggregateVertexAlbedoStreamOnDiskData_t
    WorldNode_t *-- BakedLightingInfo_t
    PermEntityLumpData_t *-- EntityKeyValueData_t
    WorldBuilderParams_t *-- BakedLightingInfo_t
    ClutterSceneObject_t *-- ObjectTypeFlags_t
    ClutterSceneObject_t *-- ClutterTile_t
    AggregateSceneObject_t *-- ObjectTypeFlags_t
    AggregateSceneObject_t *-- AggregateMeshInfo_t
    AggregateSceneObject_t *-- AggregateLODSetup_t
    SceneObject_t *-- ObjectTypeFlags_t
    RTProxyInstanceInfo_t *-- RTProxyInstanceFlags_t
```
