---
title: soundsystem_lowlevel
module: soundsystem_lowlevel
---

# Module: soundsystem_lowlevel

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

[📊 View UML Diagram](../diagrams/soundsystem_lowlevel.md)

80 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CVMixAdditionalOutput](soundsystem_lowlevel/CVMixAdditionalOutput.md) | class | 16 | 1 |  |
| [CVMixAudioMeter](soundsystem_lowlevel/CVMixAudioMeter.md) | class | 24 | 2 |  |
| [CVMixAutoFilterProcessorDesc](soundsystem_lowlevel/CVMixAutoFilterProcessorDesc.md) | class | 80 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixAutomaticControlInput](soundsystem_lowlevel/CVMixAutomaticControlInput.md) | class | 16 | 4 |  |
| [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) | class | 32 | 3 |  |
| [CVMixBoxverb2ProcessorDesc](soundsystem_lowlevel/CVMixBoxverb2ProcessorDesc.md) | class | 112 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixBoxverbProcessorDesc](soundsystem_lowlevel/CVMixBoxverbProcessorDesc.md) | class | 112 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixCommand](soundsystem_lowlevel/CVMixCommand.md) | class | 32 | 8 |  |
| [CVMixControlInput](soundsystem_lowlevel/CVMixControlInput.md) | class | 24 | 1 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixControlInputArray](soundsystem_lowlevel/CVMixControlInputArray.md) | class | 24 | 1 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixControlMeter](soundsystem_lowlevel/CVMixControlMeter.md) | class | 24 | 1 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixControlOutput](soundsystem_lowlevel/CVMixControlOutput.md) | class | 24 | 1 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixConvolutionProcessorDesc](soundsystem_lowlevel/CVMixConvolutionProcessorDesc.md) | class | 64 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixCurveHeader](soundsystem_lowlevel/CVMixCurveHeader.md) | class | 8 | 2 |  |
| [CVMixDelayProcessorDesc](soundsystem_lowlevel/CVMixDelayProcessorDesc.md) | class | 72 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixDiffusorProcessorDesc](soundsystem_lowlevel/CVMixDiffusorProcessorDesc.md) | class | 48 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixDualCompressorProcessorDesc](soundsystem_lowlevel/CVMixDualCompressorProcessorDesc.md) | class | 88 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixDynamics3BandProcessorDesc](soundsystem_lowlevel/CVMixDynamics3BandProcessorDesc.md) | class | 176 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixDynamicsCompressorProcessorDesc](soundsystem_lowlevel/CVMixDynamicsCompressorProcessorDesc.md) | class | 72 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixDynamicsProcessorDesc](soundsystem_lowlevel/CVMixDynamicsProcessorDesc.md) | class | 80 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixEQ8ProcessorDesc](soundsystem_lowlevel/CVMixEQ8ProcessorDesc.md) | class | 160 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixEffectChainProcessorDesc](soundsystem_lowlevel/CVMixEffectChainProcessorDesc.md) | class | 40 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixEnvelopeProcessorDesc](soundsystem_lowlevel/CVMixEnvelopeProcessorDesc.md) | class | 48 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixFilterProcessorDesc](soundsystem_lowlevel/CVMixFilterProcessorDesc.md) | class | 48 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixFlangerProcessorDesc](soundsystem_lowlevel/CVMixFlangerProcessorDesc.md) | class | 72 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixFreeverbProcessorDesc](soundsystem_lowlevel/CVMixFreeverbProcessorDesc.md) | class | 48 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixGraphDescData](soundsystem_lowlevel/CVMixGraphDescData.md) | class | 16 | 3 |  |
| [CVMixImpulseResponseInput](soundsystem_lowlevel/CVMixImpulseResponseInput.md) | class | 16 | 0 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) | class | 16 | 1 |  |
| [CVMixModDelayProcessorDesc](soundsystem_lowlevel/CVMixModDelayProcessorDesc.md) | class | 80 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixNameInput](soundsystem_lowlevel/CVMixNameInput.md) | class | 32 | 1 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixNameInputMeter](soundsystem_lowlevel/CVMixNameInputMeter.md) | class | 24 | 1 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixOscProcessorDesc](soundsystem_lowlevel/CVMixOscProcessorDesc.md) | class | 48 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixPannerProcessorDesc](soundsystem_lowlevel/CVMixPannerProcessorDesc.md) | class | 40 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixPitchShiftProcessorDesc](soundsystem_lowlevel/CVMixPitchShiftProcessorDesc.md) | class | 48 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixPlateReverbProcessorDesc](soundsystem_lowlevel/CVMixPlateReverbProcessorDesc.md) | class | 64 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixPresetDSPProcessorDesc](soundsystem_lowlevel/CVMixPresetDSPProcessorDesc.md) | class | 48 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixShaperProcessorDesc](soundsystem_lowlevel/CVMixShaperProcessorDesc.md) | class | 56 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixSteamAudioDirectProcessorDesc](soundsystem_lowlevel/CVMixSteamAudioDirectProcessorDesc.md) | class | 32 | 0 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixSteamAudioHRTFProcessorDesc](soundsystem_lowlevel/CVMixSteamAudioHRTFProcessorDesc.md) | class | 32 | 0 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixSteamAudioHybridReverbProcessorDesc](soundsystem_lowlevel/CVMixSteamAudioHybridReverbProcessorDesc.md) | class | 32 | 0 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixSteamAudioPathingProcessorDesc](soundsystem_lowlevel/CVMixSteamAudioPathingProcessorDesc.md) | class | 32 | 0 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixStereoDelayProcessorDesc](soundsystem_lowlevel/CVMixStereoDelayProcessorDesc.md) | class | 32 | 0 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixSubgraphSwitchProcessorDesc](soundsystem_lowlevel/CVMixSubgraphSwitchProcessorDesc.md) | class | 88 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixUtilityProcessorDesc](soundsystem_lowlevel/CVMixUtilityProcessorDesc.md) | class | 56 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixVocoderProcessorDesc](soundsystem_lowlevel/CVMixVocoderProcessorDesc.md) | class | 72 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixVsndInput](soundsystem_lowlevel/CVMixVsndInput.md) | class | 32 | 2 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [VMixAutoFilterDesc_t](soundsystem_lowlevel/VMixAutoFilterDesc_t.md) | class | 44 | 8 |  |
| [VMixBoxverbDesc_t](soundsystem_lowlevel/VMixBoxverbDesc_t.md) | class | 80 | 17 |  |
| [VMixConvolutionDesc_t](soundsystem_lowlevel/VMixConvolutionDesc_t.md) | class | 32 | 8 |  |
| [VMixDelayDesc_t](soundsystem_lowlevel/VMixDelayDesc_t.md) | class | 40 | 7 |  |
| [VMixDiffusorDesc_t](soundsystem_lowlevel/VMixDiffusorDesc_t.md) | class | 16 | 4 |  |
| [VMixDualCompressorDesc_t](soundsystem_lowlevel/VMixDualCompressorDesc_t.md) | class | 52 | 5 |  |
| [VMixDynamics3BandDesc_t](soundsystem_lowlevel/VMixDynamics3BandDesc_t.md) | class | 144 | 10 |  |
| [VMixDynamicsBand_t](soundsystem_lowlevel/VMixDynamicsBand_t.md) | class | 36 | 10 |  |
| [VMixDynamicsCompressorDesc_t](soundsystem_lowlevel/VMixDynamicsCompressorDesc_t.md) | class | 36 | 9 |  |
| [VMixDynamicsDesc_t](soundsystem_lowlevel/VMixDynamicsDesc_t.md) | class | 48 | 12 |  |
| [VMixEQ8Desc_t](soundsystem_lowlevel/VMixEQ8Desc_t.md) | class | 128 | 1 |  |
| [VMixEffectChainDesc_t](soundsystem_lowlevel/VMixEffectChainDesc_t.md) | class | 8 | 1 |  |
| [VMixEnvelopeDesc_t](soundsystem_lowlevel/VMixEnvelopeDesc_t.md) | class | 12 | 3 |  |
| [VMixFilterDesc_t](soundsystem_lowlevel/VMixFilterDesc_t.md) | class | 16 | 6 |  |
| [VMixFlangerDesc_t](soundsystem_lowlevel/VMixFlangerDesc_t.md) | class | 36 | 9 |  |
| [VMixFreeverbDesc_t](soundsystem_lowlevel/VMixFreeverbDesc_t.md) | class | 16 | 4 |  |
| [VMixModDelayDesc_t](soundsystem_lowlevel/VMixModDelayDesc_t.md) | class | 48 | 9 |  |
| [VMixOscDesc_t](soundsystem_lowlevel/VMixOscDesc_t.md) | class | 12 | 3 |  |
| [VMixPannerDesc_t](soundsystem_lowlevel/VMixPannerDesc_t.md) | class | 8 | 2 |  |
| [VMixPitchShiftDesc_t](soundsystem_lowlevel/VMixPitchShiftDesc_t.md) | class | 16 | 4 |  |
| [VMixPlateverbDesc_t](soundsystem_lowlevel/VMixPlateverbDesc_t.md) | class | 28 | 7 |  |
| [VMixPresetDSPDesc_t](soundsystem_lowlevel/VMixPresetDSPDesc_t.md) | class | 16 | 1 |  |
| [VMixShaperDesc_t](soundsystem_lowlevel/VMixShaperDesc_t.md) | class | 20 | 5 |  |
| [VMixSubgraphSwitchDesc_t](soundsystem_lowlevel/VMixSubgraphSwitchDesc_t.md) | class | 56 | 6 |  |
| [VMixUtilityDesc_t](soundsystem_lowlevel/VMixUtilityDesc_t.md) | class | 24 | 6 |  |
| [VMixVocoderDesc_t](soundsystem_lowlevel/VMixVocoderDesc_t.md) | class | 40 | 10 |  |
| [VMixChannelOperation_t](soundsystem_lowlevel/VMixChannelOperation_t.md) | enum | — | 6 |  |
| [VMixFilterSlope_t](soundsystem_lowlevel/VMixFilterSlope_t.md) | enum | — | 9 |  |
| [VMixFilterType_t](soundsystem_lowlevel/VMixFilterType_t.md) | enum | — | 10 |  |
| [VMixGraphCommandID_t](soundsystem_lowlevel/VMixGraphCommandID_t.md) | enum | — | 40 |  |
| [VMixLFOShape_t](soundsystem_lowlevel/VMixLFOShape_t.md) | enum | — | 5 |  |
| [VMixPannerType_t](soundsystem_lowlevel/VMixPannerType_t.md) | enum | — | 2 |  |
| [VMixSubgraphSwitchInterpolationType_t](soundsystem_lowlevel/VMixSubgraphSwitchInterpolationType_t.md) | enum | — | 3 |  |
