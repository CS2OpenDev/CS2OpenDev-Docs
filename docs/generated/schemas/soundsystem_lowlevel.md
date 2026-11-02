---
title: soundsystem_lowlevel
module: soundsystem_lowlevel
---

# Module: soundsystem_lowlevel

> Source: **Build 26334290** · 2026-10-30 · `windows-x86_64` · schema `0.13.0`

[📊 View UML Diagram](../diagrams/soundsystem_lowlevel.md)

94 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CVMixAdditionalOutput](soundsystem_lowlevel/CVMixAdditionalOutput.md) | class | 16 | 1 |  |
| [CVMixAudioMeter](soundsystem_lowlevel/CVMixAudioMeter.md) | class | 24 | 3 |  |
| [CVMixAutoFilterProcessorDesc](soundsystem_lowlevel/CVMixAutoFilterProcessorDesc.md) | class | 88 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixAutomaticControlInput](soundsystem_lowlevel/CVMixAutomaticControlInput.md) | class | 24 | 3 |  |
| [CVMixBaseGraphDescription](soundsystem_lowlevel/CVMixBaseGraphDescription.md) | class | 208 | 15 |  |
| [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) | class | 40 | 7 |  |
| [CVMixBoxverb2ProcessorDesc](soundsystem_lowlevel/CVMixBoxverb2ProcessorDesc.md) | class | 120 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixBoxverbProcessorDesc](soundsystem_lowlevel/CVMixBoxverbProcessorDesc.md) | class | 120 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixCommand](soundsystem_lowlevel/CVMixCommand.md) | class | 32 | 8 |  |
| [CVMixControlInput](soundsystem_lowlevel/CVMixControlInput.md) | class | 24 | 1 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixControlMeter](soundsystem_lowlevel/CVMixControlMeter.md) | class | 24 | 1 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixControlOutput](soundsystem_lowlevel/CVMixControlOutput.md) | class | 24 | 1 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixConvolutionProcessorDesc](soundsystem_lowlevel/CVMixConvolutionProcessorDesc.md) | class | 80 | 2 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixDataOffset](soundsystem_lowlevel/CVMixDataOffset.md) | class | 4 | 1 |  |
| [CVMixDelayProcessorDesc](soundsystem_lowlevel/CVMixDelayProcessorDesc.md) | class | 88 | 3 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixDiffusorProcessorDesc](soundsystem_lowlevel/CVMixDiffusorProcessorDesc.md) | class | 56 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixDualCompressorProcessorDesc](soundsystem_lowlevel/CVMixDualCompressorProcessorDesc.md) | class | 104 | 4 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixDynamics3BandProcessorDesc](soundsystem_lowlevel/CVMixDynamics3BandProcessorDesc.md) | class | 184 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixDynamicsCompressorProcessorDesc](soundsystem_lowlevel/CVMixDynamicsCompressorProcessorDesc.md) | class | 96 | 4 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixDynamicsProcessorDesc](soundsystem_lowlevel/CVMixDynamicsProcessorDesc.md) | class | 96 | 3 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixEQ8ProcessorDesc](soundsystem_lowlevel/CVMixEQ8ProcessorDesc.md) | class | 208 | 2 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixEffectChainProcessorDesc](soundsystem_lowlevel/CVMixEffectChainProcessorDesc.md) | class | 56 | 2 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixEnvelopeProcessorDesc](soundsystem_lowlevel/CVMixEnvelopeProcessorDesc.md) | class | 64 | 3 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixFilterProcessorDesc](soundsystem_lowlevel/CVMixFilterProcessorDesc.md) | class | 64 | 3 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixFlangerProcessorDesc](soundsystem_lowlevel/CVMixFlangerProcessorDesc.md) | class | 88 | 4 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixFreeverbProcessorDesc](soundsystem_lowlevel/CVMixFreeverbProcessorDesc.md) | class | 56 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixGraphInput](soundsystem_lowlevel/CVMixGraphInput.md) | class | 24 | 1 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixHeap](soundsystem_lowlevel/CVMixHeap.md) | class | 16 | 1 |  |
| [CVMixImpulseResponseInput](soundsystem_lowlevel/CVMixImpulseResponseInput.md) | class | 16 | 0 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) | class | 16 | 1 |  |
| [CVMixModDelayProcessorDesc](soundsystem_lowlevel/CVMixModDelayProcessorDesc.md) | class | 104 | 5 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixNameInputMeter](soundsystem_lowlevel/CVMixNameInputMeter.md) | class | 24 | 1 | [CVMixInputBase](soundsystem_lowlevel/CVMixInputBase.md) |
| [CVMixOscProcessorDesc](soundsystem_lowlevel/CVMixOscProcessorDesc.md) | class | 64 | 3 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixPannerProcessorDesc](soundsystem_lowlevel/CVMixPannerProcessorDesc.md) | class | 56 | 2 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixParameterBool](soundsystem_lowlevel/CVMixParameterBool.md) | class | 4 | 1 |  |
| [CVMixParameterEffectName](soundsystem_lowlevel/CVMixParameterEffectName.md) | class | 4 | 1 |  |
| [CVMixParameterFloat](soundsystem_lowlevel/CVMixParameterFloat.md) | class | 4 | 1 |  |
| [CVMixPitchShiftProcessorDesc](soundsystem_lowlevel/CVMixPitchShiftProcessorDesc.md) | class | 64 | 2 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixPlateReverbProcessorDesc](soundsystem_lowlevel/CVMixPlateReverbProcessorDesc.md) | class | 72 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixPresetDSPProcessorDesc](soundsystem_lowlevel/CVMixPresetDSPProcessorDesc.md) | class | 64 | 2 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixRuntimeGraph](soundsystem_lowlevel/CVMixRuntimeGraph.md) | class | 296 | 5 | [CVMixBaseGraphDescription](soundsystem_lowlevel/CVMixBaseGraphDescription.md) |
| [CVMixShaperProcessorDesc](soundsystem_lowlevel/CVMixShaperProcessorDesc.md) | class | 64 | 2 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixSteamAudioDirectProcessorDesc](soundsystem_lowlevel/CVMixSteamAudioDirectProcessorDesc.md) | class | 144 | 25 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixSteamAudioHRTFProcessorDesc](soundsystem_lowlevel/CVMixSteamAudioHRTFProcessorDesc.md) | class | 80 | 9 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixSteamAudioHybridReverbProcessorDesc](soundsystem_lowlevel/CVMixSteamAudioHybridReverbProcessorDesc.md) | class | 64 | 5 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixSteamAudioPathingProcessorDesc](soundsystem_lowlevel/CVMixSteamAudioPathingProcessorDesc.md) | class | 72 | 7 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixStereoDelayProcessorDesc](soundsystem_lowlevel/CVMixStereoDelayProcessorDesc.md) | class | 48 | 2 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixSubgraphSwitchProcessorDesc](soundsystem_lowlevel/CVMixSubgraphSwitchProcessorDesc.md) | class | 104 | 3 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixSubmix](soundsystem_lowlevel/CVMixSubmix.md) | class | 56 | 7 |  |
| [CVMixUtilityProcessorDesc](soundsystem_lowlevel/CVMixUtilityProcessorDesc.md) | class | 64 | 1 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixVocoderProcessorDesc](soundsystem_lowlevel/CVMixVocoderProcessorDesc.md) | class | 88 | 2 | [CVMixBaseProcessorDesc](soundsystem_lowlevel/CVMixBaseProcessorDesc.md) |
| [CVMixVsndInput](soundsystem_lowlevel/CVMixVsndInput.md) | class | 24 | 1 |  |
| [VMixAutoFilterDesc_t](soundsystem_lowlevel/VMixAutoFilterDesc_t.md) | class | 44 | 8 |  |
| [VMixBoxverbDesc_t](soundsystem_lowlevel/VMixBoxverbDesc_t.md) | class | 80 | 17 |  |
| [VMixConvolutionDesc_t](soundsystem_lowlevel/VMixConvolutionDesc_t.md) | class | 32 | 8 |  |
| [VMixDelayDesc_t](soundsystem_lowlevel/VMixDelayDesc_t.md) | class | 40 | 7 |  |
| [VMixDiffusorDesc_t](soundsystem_lowlevel/VMixDiffusorDesc_t.md) | class | 16 | 4 |  |
| [VMixDualCompressorDesc_t](soundsystem_lowlevel/VMixDualCompressorDesc_t.md) | class | 52 | 5 |  |
| [VMixDynamics3BandDesc_t](soundsystem_lowlevel/VMixDynamics3BandDesc_t.md) | class | 144 | 10 |  |
| [VMixDynamicsBand_t](soundsystem_lowlevel/VMixDynamicsBand_t.md) | class | 36 | 10 |  |
| [VMixDynamicsCompressorDesc_t](soundsystem_lowlevel/VMixDynamicsCompressorDesc_t.md) | class | 40 | 11 |  |
| [VMixDynamicsDesc_t](soundsystem_lowlevel/VMixDynamicsDesc_t.md) | class | 48 | 12 |  |
| [VMixEQ8Desc_t](soundsystem_lowlevel/VMixEQ8Desc_t.md) | class | 160 | 1 |  |
| [VMixEQFilterDesc_t](soundsystem_lowlevel/VMixEQFilterDesc_t.md) | class | 20 | 1 | [VMixFilterDesc_t](soundsystem_lowlevel/VMixFilterDesc_t.md) |
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
| [VMixPointerFixupEntry_t](soundsystem_lowlevel/VMixPointerFixupEntry_t.md) | class | 8 | 2 |  |
| [VMixPresetDSPDesc_t](soundsystem_lowlevel/VMixPresetDSPDesc_t.md) | class | 16 | 1 |  |
| [VMixShaperDesc_t](soundsystem_lowlevel/VMixShaperDesc_t.md) | class | 20 | 5 |  |
| [VMixSubgraphSwitchDesc_t](soundsystem_lowlevel/VMixSubgraphSwitchDesc_t.md) | class | 56 | 6 |  |
| [VMixUtilityDesc_t](soundsystem_lowlevel/VMixUtilityDesc_t.md) | class | 24 | 6 |  |
| [VMixVocoderDesc_t](soundsystem_lowlevel/VMixVocoderDesc_t.md) | class | 40 | 10 |  |
| [VMixAutoControlType_t](soundsystem_lowlevel/VMixAutoControlType_t.md) | enum | — | 14 |  |
| [VMixChannelOperation_t](soundsystem_lowlevel/VMixChannelOperation_t.md) | enum | — | 6 |  |
| [VMixFilterChannelSet_t](soundsystem_lowlevel/VMixFilterChannelSet_t.md) | enum | — | 6 |  |
| [VMixFilterSlope_t](soundsystem_lowlevel/VMixFilterSlope_t.md) | enum | — | 9 |  |
| [VMixFilterType_t](soundsystem_lowlevel/VMixFilterType_t.md) | enum | — | 10 |  |
| [VMixGraphCommandID_t](soundsystem_lowlevel/VMixGraphCommandID_t.md) | enum | — | 34 |  |
| [VMixLFOShape_t](soundsystem_lowlevel/VMixLFOShape_t.md) | enum | — | 5 |  |
| [VMixMixDownRule_t](soundsystem_lowlevel/VMixMixDownRule_t.md) | enum | — | 5 |  |
| [VMixOffsetCategory_t](soundsystem_lowlevel/VMixOffsetCategory_t.md) | enum | — | 4 |  |
| [VMixOffsetType_t](soundsystem_lowlevel/VMixOffsetType_t.md) | enum | — | 13 |  |
| [VMixPannerType_t](soundsystem_lowlevel/VMixPannerType_t.md) | enum | — | 2 |  |
| [VMixSendOperator_t](soundsystem_lowlevel/VMixSendOperator_t.md) | enum | — | 10 |  |
| [VMixSubgraphSwitchInterpolationType_t](soundsystem_lowlevel/VMixSubgraphSwitchInterpolationType_t.md) | enum | — | 3 |  |
| [VMixUpMixRule_t](soundsystem_lowlevel/VMixUpMixRule_t.md) | enum | — | 2 |  |
