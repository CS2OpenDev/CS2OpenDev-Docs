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
    CVMixBaseProcessorDesc <|-- CVMixBoxverbProcessorDesc
    CVMixInputBase <|-- CVMixControlInput
    CVMixInputBase <|-- CVMixControlInputArray
    CVMixInputBase <|-- CVMixControlMeter
    CVMixInputBase <|-- CVMixControlOutput
    CVMixBaseProcessorDesc <|-- CVMixConvolutionProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixDelayProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixDiffusorProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixDualCompressorProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixDynamics3BandProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixDynamicsCompressorProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixDynamicsProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixEQ8ProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixEffectChainProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixEnvelopeProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixFilterProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixFlangerProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixFreeverbProcessorDesc
    CVMixInputBase <|-- CVMixImpulseResponseInput
    CVMixBaseProcessorDesc <|-- CVMixModDelayProcessorDesc
    CVMixInputBase <|-- CVMixNameInput
    CVMixInputBase <|-- CVMixNameInputMeter
    CVMixBaseProcessorDesc <|-- CVMixOscProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixPannerProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixPitchShiftProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixPlateReverbProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixPresetDSPProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixShaperProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixSteamAudioDirectProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixSteamAudioHRTFProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixSteamAudioHybridReverbProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixSteamAudioPathingProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixStereoDelayProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixSubgraphSwitchProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixUtilityProcessorDesc
    CVMixBaseProcessorDesc <|-- CVMixVocoderProcessorDesc
    CVMixInputBase <|-- CVMixVsndInput
    CVMixAutoFilterProcessorDesc *-- VMixAutoFilterDesc_t
    CVMixBoxverb2ProcessorDesc *-- VMixBoxverbDesc_t
    CVMixBoxverbProcessorDesc *-- VMixBoxverbDesc_t
    CVMixConvolutionProcessorDesc *-- VMixConvolutionDesc_t
    CVMixDelayProcessorDesc *-- VMixDelayDesc_t
    CVMixDiffusorProcessorDesc *-- VMixDiffusorDesc_t
    CVMixDualCompressorProcessorDesc *-- VMixDualCompressorDesc_t
    CVMixDynamics3BandProcessorDesc *-- VMixDynamics3BandDesc_t
    CVMixDynamicsCompressorProcessorDesc *-- VMixDynamicsCompressorDesc_t
    CVMixDynamicsProcessorDesc *-- VMixDynamicsDesc_t
    CVMixEQ8ProcessorDesc *-- VMixEQ8Desc_t
    CVMixEffectChainProcessorDesc *-- VMixEffectChainDesc_t
    CVMixEnvelopeProcessorDesc *-- VMixEnvelopeDesc_t
    CVMixFilterProcessorDesc *-- VMixFilterDesc_t
    CVMixFlangerProcessorDesc *-- VMixFlangerDesc_t
    CVMixFreeverbProcessorDesc *-- VMixFreeverbDesc_t
    CVMixModDelayProcessorDesc *-- VMixModDelayDesc_t
    CVMixOscProcessorDesc *-- VMixOscDesc_t
    CVMixPannerProcessorDesc *-- VMixPannerDesc_t
    CVMixPitchShiftProcessorDesc *-- VMixPitchShiftDesc_t
    CVMixPlateReverbProcessorDesc *-- VMixPlateverbDesc_t
    CVMixPresetDSPProcessorDesc *-- VMixPresetDSPDesc_t
    CVMixShaperProcessorDesc *-- VMixShaperDesc_t
    CVMixSubgraphSwitchProcessorDesc *-- VMixSubgraphSwitchDesc_t
    CVMixUtilityProcessorDesc *-- VMixUtilityDesc_t
    CVMixVocoderProcessorDesc *-- VMixVocoderDesc_t
    VMixAutoFilterDesc_t *-- VMixFilterDesc_t
    VMixBoxverbDesc_t *-- VMixFilterDesc_t
    VMixDelayDesc_t *-- VMixFilterDesc_t
    VMixDualCompressorDesc_t *-- VMixDynamicsBand_t
    VMixDynamics3BandDesc_t *-- VMixDynamicsBand_t
    VMixEQ8Desc_t *-- VMixFilterDesc_t
    VMixModDelayDesc_t *-- VMixFilterDesc_t
```
