---
layout: default
title: "UML: soundsystem_voicecontainers"
parent: Schemas
nav_exclude: true
---

# UML: soundsystem_voicecontainers

Class relationships (inheritance and composition) for the `soundsystem_voicecontainers` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CVoiceContainerDecayingSineWave <|-- CVoiceContainerAmpedDecayingSineWave
    CVoiceContainerGenerator <|-- CVoiceContainerAsyncGenerator
    CVoiceContainerBase <|-- CVoiceContainerBlender
    CVoiceContainerGenerator <|-- CVoiceContainerDecayingSineWave
    CVoiceContainerBase <|-- CVoiceContainerDefault
    CVoiceContainerBase <|-- CVoiceContainerEnum
    CVoiceContainerAnalysisBase <|-- CVoiceContainerEnvelopeAnalyzer
    CVoiceContainerBase <|-- CVoiceContainerGenerator
    CVoiceContainerAsyncGenerator <|-- CVoiceContainerGranulator
    CVoiceContainerBase <|-- CVoiceContainerLoopTrigger
    CVoiceContainerLoopTrigger <|-- CVoiceContainerLoopTriggerWithRandomPanner
    CVoiceContainerBase <|-- CVoiceContainerLoopXFade
    CVoiceContainerBase <|-- CVoiceContainerMultiBlender
    CVoiceContainerGenerator <|-- CVoiceContainerNull
    CVoiceContainerBase <|-- CVoiceContainerParameterBlender
    CVoiceContainerAsyncGenerator <|-- CVoiceContainerRandomSampler
    CVoiceContainerGenerator <|-- CVoiceContainerRealtimeFMSineWave
    CVoiceContainerBase <|-- CVoiceContainerSelector
    CVoiceContainerBase <|-- CVoiceContainerSet
    CVoiceContainerGenerator <|-- CVoiceContainerShapedNoise
    CVoiceContainerAsyncGenerator <|-- CVoiceContainerStaticAdditiveSynth
    CVoiceContainerBase <|-- CVoiceContainerSwitch
    CVoiceContainerAsyncGenerator <|-- CVoiceContainerTapePlayer
    CVoiceContainerBase <|-- CVoiceContainerVsndRadioButton
    CVoiceContainerBase <|-- CVoiceContainerVsndTrigger
    CAudioSentence *-- CAudioPhonemeTag
    CAudioSentence *-- CAudioEmphasisSample
    CAudioSentence *-- CAudioMorphData
    CSoundContainerReference --> CVoiceContainerBase
    CSoundContainerReferenceArray --> CVoiceContainerBase
    CVSound *-- CAudioSentence
    CVSound *-- CVSoundFormat_t
    CVoiceContainerBase *-- CVSound
    CVoiceContainerBase --> CVoiceContainerAnalysisBase
    CVoiceContainerBlender *-- CSoundContainerReference
    CVoiceContainerEnum *-- CSoundContainerReferenceArray
    CVoiceContainerEnvelopeAnalyzer *-- EMode_t
    CVoiceContainerLoopTrigger *-- CSoundContainerReference
    CVoiceContainerLoopTriggerWithRandomPanner *-- CRandomPannerControls
    CVoiceContainerLoopXFade *-- CSoundContainerReference
    CVoiceContainerMultiBlender *-- CSoundContainerReferenceArray
    CVoiceContainerParameterBlender *-- CSoundContainerReference
    CVoiceContainerSelector *-- PlayBackMode_t
    CVoiceContainerSelector *-- CSoundContainerReferenceArray
    CVoiceContainerSet *-- CVoiceContainerSetElement
    CVoiceContainerSetElement *-- CSoundContainerReference
    CVoiceContainerStaticAdditiveSynth *-- `CVoiceContainerStaticAdditiveSynth::CTone`
    `CVoiceContainerStaticAdditiveSynth::CHarmonic` *-- EWaveform
    `CVoiceContainerStaticAdditiveSynth::CHarmonic` *-- EMidiNote
    `CVoiceContainerStaticAdditiveSynth::CHarmonic` *-- `CVoiceContainerStaticAdditiveSynth::CGainScalePerInstance`
    `CVoiceContainerStaticAdditiveSynth::CTone` *-- `CVoiceContainerStaticAdditiveSynth::CHarmonic`
    CVoiceContainerSwitch *-- CSoundContainerReference
    CVoiceContainerVsndRadioButton *-- CVsndRadioButtonSlot
    CVoiceContainerVsndTrigger *-- CVsndTriggerSlot
    CVsndRadioButtonSlot *-- CSoundContainerReference
    CVsndRadioButtonSlot *-- EVsndPlaybackMode
    CVsndTriggerSlot *-- CSoundContainerReference
    CVsndTriggerSlot *-- EVsndTriggerMode
```
