---
layout: default
title: "UML: soundsystem_lowlevel"
parent: Schemas
nav_exclude: true
---

# UML: soundsystem_lowlevel

Class relationships (inheritance and composition) for the `soundsystem_lowlevel` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CVMixBaseProcessorDesc <|-- CVMixAutoFilterProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixBoxverb2ProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixDelayProcessorDesc
    CVMixInputBase <|-- CVMixControlMeter
    CVMixBaseProcessorDesc <|-- CVMixDualCompressorProcessorDesc
    CVMixInputBase <|-- CVMixVsndInput
    CVMixBaseProcessorDesc <|-- CVMixPlateReverbProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixVocoderProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixStereoDelayProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixPannerProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixSteamAudioPathingProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixSubgraphSwitchProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixFilterProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixConvolutionProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixFreeverbProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixEffectChainProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixFlangerProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixOscProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixShaperProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixModDelayProcessorDesc
    CVMixInputBase <|-- CVMixControlOutput
    CVMixBaseProcessorDesc <|-- CVMixSteamAudioHybridReverbProcessorDesc
    CVMixInputBase <|-- CVMixImpulseResponseInput
    CVMixInputBase <|-- CVMixNameInput
    CVMixInputBase <|-- CVMixControlInputArray
    CVMixBaseProcessorDesc <|-- CVMixDynamicsProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixPresetDSPProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixUtilityProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixDiffusorProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixEQ8ProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixDynamics3BandProcessorDesc
    CVMixInputBase <|-- CVMixNameInputMeter
    CVMixBaseProcessorDesc <|-- CVMixDynamicsCompressorProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixBoxverbProcessorDesc
    CVMixInputBase <|-- CVMixControlInput
    CVMixBaseProcessorDesc <|-- CVMixEnvelopeProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixSteamAudioHRTFProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixSteamAudioDirectProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixPitchShiftProcessorDesc
    CVMixAutoFilterProcessorDesc *-- VMixAutoFilterDesc_t
    VMixOscDesc_t *-- VMixLFOShape_t
    VMixFilterDesc_t *-- VMixFilterType_t
    VMixFilterDesc_t *-- VMixFilterSlope_t
    CVMixBoxverb2ProcessorDesc *-- VMixBoxverbDesc_t
    CVMixDelayProcessorDesc *-- VMixDelayDesc_t
    VMixUtilityDesc_t *-- VMixChannelOperation_t
    CVMixDualCompressorProcessorDesc *-- VMixDualCompressorDesc_t
    CVMixPlateReverbProcessorDesc *-- VMixPlateverbDesc_t
    VMixAutoFilterDesc_t *-- VMixFilterDesc_t
    VMixAutoFilterDesc_t *-- VMixLFOShape_t
    CVMixVocoderProcessorDesc *-- VMixVocoderDesc_t
    CVMixPannerProcessorDesc *-- VMixPannerDesc_t
    CVMixSubgraphSwitchProcessorDesc *-- VMixSubgraphSwitchDesc_t
    CVMixFilterProcessorDesc *-- VMixFilterDesc_t
    CVMixConvolutionProcessorDesc *-- VMixConvolutionDesc_t
    CVMixFreeverbProcessorDesc *-- VMixFreeverbDesc_t
    CVMixEffectChainProcessorDesc *-- VMixEffectChainDesc_t
    CVMixFlangerProcessorDesc *-- VMixFlangerDesc_t
    CVMixOscProcessorDesc *-- VMixOscDesc_t
    CVMixShaperProcessorDesc *-- VMixShaperDesc_t
    CVMixModDelayProcessorDesc *-- VMixModDelayDesc_t
    CVMixDynamicsProcessorDesc *-- VMixDynamicsDesc_t
    VMixEQ8Desc_t *-- VMixFilterDesc_t
    VMixDelayDesc_t *-- VMixFilterDesc_t
    CVMixPresetDSPProcessorDesc *-- VMixPresetDSPDesc_t
    CVMixUtilityProcessorDesc *-- VMixUtilityDesc_t
    CVMixDiffusorProcessorDesc *-- VMixDiffusorDesc_t
    VMixDualCompressorDesc_t *-- VMixDynamicsBand_t
    CVMixEQ8ProcessorDesc *-- VMixEQ8Desc_t
    VMixDynamics3BandDesc_t *-- VMixDynamicsBand_t
    VMixBoxverbDesc_t *-- VMixFilterDesc_t
    CVMixDynamics3BandProcessorDesc *-- VMixDynamics3BandDesc_t
    VMixModDelayDesc_t *-- VMixFilterDesc_t
    VMixPannerDesc_t *-- VMixPannerType_t
    CVMixDynamicsCompressorProcessorDesc *-- VMixDynamicsCompressorDesc_t
    CVMixBoxverbProcessorDesc *-- VMixBoxverbDesc_t
    CVMixCommand *-- VMixGraphCommandID_t
    CVMixEnvelopeProcessorDesc *-- VMixEnvelopeDesc_t
    VMixSubgraphSwitchDesc_t *-- VMixSubgraphSwitchInterpolationType_t
    CVMixPitchShiftProcessorDesc *-- VMixPitchShiftDesc_t
```
