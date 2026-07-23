---
layout: default
title: "UML: steamaudio"
parent: Schemas
nav_exclude: true
---

# UML: steamaudio

Class relationships (inheritance and composition) for the `steamaudio` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CSteamAudioBakedDimensionsData *-- SteamAudioCustomDataDimensionsSettings_t
    CSteamAudioBakedDimensionsData *-- CSteamAudioProbeData
    CSteamAudioBakedDimensionsData *-- CSteamAudioAmbisonicsField
    CSteamAudioBakedMaterialsData *-- CSteamAudioProbeData
    CSteamAudioBakedOcclusionData *-- SteamAudioCustomDataOcclusionSettings_t
    CSteamAudioBakedOcclusionData *-- CSteamAudioProbeData
    CSteamAudioBakedPathingData *-- CSteamAudioProbeData
    CSteamAudioBakedReverbData *-- CSteamAudioSceneData
    CSteamAudioBakedReverbData *-- CSteamAudioProbeData
    CSteamAudioBakedReverbData *-- CSteamAudioProbeGrid
    CSteamAudioBakedReverbData *-- SteamAudioReverbSettings_t
    CSteamAudioBakedReverbData *-- SteamAudioReverbClusteringSettings_t
    CSteamAudioBakedReverbData *-- SteamAudioReverbCompressionSettings_t
    CSteamAudioBakedReverbData *-- CSteamAudioCompressedReverb
    CSteamAudioProbeGrid *-- CSteamAudioProbeLineSegment
```
