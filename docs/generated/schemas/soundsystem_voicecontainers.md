---
title: soundsystem_voicecontainers
module: soundsystem_voicecontainers
---

# Module: soundsystem_voicecontainers

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

[📊 View UML Diagram](../diagrams/soundsystem_voicecontainers.md)

49 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CAudioEmphasisSample](soundsystem_voicecontainers/CAudioEmphasisSample.md) | class | 8 | 2 |  |
| [CAudioMorphData](soundsystem_voicecontainers/CAudioMorphData.md) | class | 104 | 6 |  |
| [CAudioPhonemeTag](soundsystem_voicecontainers/CAudioPhonemeTag.md) | class | 12 | 3 |  |
| [CAudioSentence](soundsystem_voicecontainers/CAudioSentence.md) | class | 160 | 4 |  |
| [CRandomPannerControls](soundsystem_voicecontainers/CRandomPannerControls.md) | class | 32 | 5 |  |
| [CSoundContainerReference](soundsystem_voicecontainers/CSoundContainerReference.md) | class | 32 | 4 |  |
| [CSoundContainerReferenceArray](soundsystem_voicecontainers/CSoundContainerReferenceArray.md) | class | 56 | 3 |  |
| [CSoundInfoHeader](soundsystem_voicecontainers/CSoundInfoHeader.md) | class | 1 | 0 |  |
| [CVSound](soundsystem_voicecontainers/CVSound.md) | class | 64 | 9 |  |
| [CVoiceContainerAmpedDecayingSineWave](soundsystem_voicecontainers/CVoiceContainerAmpedDecayingSineWave.md) | class | 128 | 1 | [CVoiceContainerDecayingSineWave](soundsystem_voicecontainers/CVoiceContainerDecayingSineWave.md) |
| [CVoiceContainerAnalysisBase](soundsystem_voicecontainers/CVoiceContainerAnalysisBase.md) | class | 72 | 1 |  |
| [CVoiceContainerAsyncGenerator](soundsystem_voicecontainers/CVoiceContainerAsyncGenerator.md) | class | 128 | 0 | [CVoiceContainerGenerator](soundsystem_voicecontainers/CVoiceContainerGenerator.md) |
| [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) | class | 112 | 2 |  |
| [CVoiceContainerBlender](soundsystem_voicecontainers/CVoiceContainerBlender.md) | class | 184 | 3 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVoiceContainerDecayingSineWave](soundsystem_voicecontainers/CVoiceContainerDecayingSineWave.md) | class | 120 | 2 | [CVoiceContainerGenerator](soundsystem_voicecontainers/CVoiceContainerGenerator.md) |
| [CVoiceContainerDefault](soundsystem_voicecontainers/CVoiceContainerDefault.md) | class | 112 | 0 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVoiceContainerEnum](soundsystem_voicecontainers/CVoiceContainerEnum.md) | class | 176 | 3 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVoiceContainerEnvelopeAnalyzer](soundsystem_voicecontainers/CVoiceContainerEnvelopeAnalyzer.md) | class | 88 | 3 | [CVoiceContainerAnalysisBase](soundsystem_voicecontainers/CVoiceContainerAnalysisBase.md) |
| [CVoiceContainerGenerator](soundsystem_voicecontainers/CVoiceContainerGenerator.md) | class | 112 | 0 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVoiceContainerGranulator](soundsystem_voicecontainers/CVoiceContainerGranulator.md) | class | 344 | 6 | [CVoiceContainerAsyncGenerator](soundsystem_voicecontainers/CVoiceContainerAsyncGenerator.md) |
| [CVoiceContainerLoopTrigger](soundsystem_voicecontainers/CVoiceContainerLoopTrigger.md) | class | 160 | 5 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVoiceContainerLoopTriggerWithRandomPanner](soundsystem_voicecontainers/CVoiceContainerLoopTriggerWithRandomPanner.md) | class | 192 | 1 | [CVoiceContainerLoopTrigger](soundsystem_voicecontainers/CVoiceContainerLoopTrigger.md) |
| [CVoiceContainerLoopXFade](soundsystem_voicecontainers/CVoiceContainerLoopXFade.md) | class | 168 | 8 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVoiceContainerMultiBlender](soundsystem_voicecontainers/CVoiceContainerMultiBlender.md) | class | 176 | 3 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVoiceContainerNull](soundsystem_voicecontainers/CVoiceContainerNull.md) | class | 112 | 0 | [CVoiceContainerGenerator](soundsystem_voicecontainers/CVoiceContainerGenerator.md) |
| [CVoiceContainerParameterBlender](soundsystem_voicecontainers/CVoiceContainerParameterBlender.md) | class | 448 | 8 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVoiceContainerRandomSampler](soundsystem_voicecontainers/CVoiceContainerRandomSampler.md) | class | 424 | 6 | [CVoiceContainerAsyncGenerator](soundsystem_voicecontainers/CVoiceContainerAsyncGenerator.md) |
| [CVoiceContainerRealtimeFMSineWave](soundsystem_voicecontainers/CVoiceContainerRealtimeFMSineWave.md) | class | 128 | 3 | [CVoiceContainerGenerator](soundsystem_voicecontainers/CVoiceContainerGenerator.md) |
| [CVoiceContainerSelector](soundsystem_voicecontainers/CVoiceContainerSelector.md) | class | 232 | 3 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVoiceContainerSet](soundsystem_voicecontainers/CVoiceContainerSet.md) | class | 160 | 1 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVoiceContainerSetElement](soundsystem_voicecontainers/CVoiceContainerSetElement.md) | class | 40 | 2 |  |
| [CVoiceContainerShapedNoise](soundsystem_voicecontainers/CVoiceContainerShapedNoise.md) | class | 328 | 9 | [CVoiceContainerGenerator](soundsystem_voicecontainers/CVoiceContainerGenerator.md) |
| [CVoiceContainerStaticAdditiveSynth](soundsystem_voicecontainers/CVoiceContainerStaticAdditiveSynth.md) | class | 176 | 1 | [CVoiceContainerAsyncGenerator](soundsystem_voicecontainers/CVoiceContainerAsyncGenerator.md) |
| [CVoiceContainerStaticAdditiveSynth::CGainScalePerInstance](soundsystem_voicecontainers/CVoiceContainerStaticAdditiveSynth.CGainScalePerInstance.md) | class | 16 | 4 |  |
| [CVoiceContainerStaticAdditiveSynth::CHarmonic](soundsystem_voicecontainers/CVoiceContainerStaticAdditiveSynth.CHarmonic.md) | class | 104 | 7 |  |
| [CVoiceContainerStaticAdditiveSynth::CTone](soundsystem_voicecontainers/CVoiceContainerStaticAdditiveSynth.CTone.md) | class | 96 | 3 |  |
| [CVoiceContainerSwitch](soundsystem_voicecontainers/CVoiceContainerSwitch.md) | class | 136 | 1 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVoiceContainerTapePlayer](soundsystem_voicecontainers/CVoiceContainerTapePlayer.md) | class | 192 | 4 | [CVoiceContainerAsyncGenerator](soundsystem_voicecontainers/CVoiceContainerAsyncGenerator.md) |
| [CVoiceContainerVsndRadioButton](soundsystem_voicecontainers/CVoiceContainerVsndRadioButton.md) | class | 2296 | 17 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVoiceContainerVsndTrigger](soundsystem_voicecontainers/CVoiceContainerVsndTrigger.md) | class | 2296 | 17 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [CVsndRadioButtonSlot](soundsystem_voicecontainers/CVsndRadioButtonSlot.md) | class | 136 | 10 |  |
| [CVsndTriggerSlot](soundsystem_voicecontainers/CVsndTriggerSlot.md) | class | 136 | 9 |  |
| [CVSoundFormat_t](soundsystem_voicecontainers/CVSoundFormat_t.md) | enum | — | 4 |  |
| [EMidiNote](soundsystem_voicecontainers/EMidiNote.md) | enum | — | 13 |  |
| [EMode_t](soundsystem_voicecontainers/EMode_t.md) | enum | — | 2 |  |
| [EVsndPlaybackMode](soundsystem_voicecontainers/EVsndPlaybackMode.md) | enum | — | 2 |  |
| [EVsndTriggerMode](soundsystem_voicecontainers/EVsndTriggerMode.md) | enum | — | 2 |  |
| [EWaveform](soundsystem_voicecontainers/EWaveform.md) | enum | — | 5 |  |
| [PlayBackMode_t](soundsystem_voicecontainers/PlayBackMode_t.md) | enum | — | 5 |  |
