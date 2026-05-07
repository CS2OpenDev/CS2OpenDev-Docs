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
    CVoiceContainerGenerator <|-- CVoiceContainerDecayingSineWave
    CVoiceContainerBase <|-- CVoiceContainerLoopTrigger
    CVoiceContainerBase <|-- CVoiceContainerEnum
    CVoiceContainerBase <|-- CVoiceContainerSwitch
    CVoiceContainerBase <|-- CVoiceContainerSelector
    CVoiceContainerBase <|-- CVoiceContainerMultiBlender
    CVoiceContainerDefault <|-- CVoiceContainerEnvelope
    CVoiceContainerDecayingSineWave <|-- CVoiceContainerAmpedDecayingSineWave
    CVoiceContainerBase <|-- CVoiceContainerParameterBlender
    CVoiceContainerAsyncGenerator <|-- CVoiceContainerTapePlayer
    CVoiceContainerGenerator <|-- CVoiceContainerAsyncGenerator
    CVoiceContainerBase <|-- CVoiceContainerSet
    CVoiceContainerBase <|-- CVoiceContainerGenerator
    CVoiceContainerAnalysisBase <|-- CVoiceContainerEnvelopeAnalyzer
    CVoiceContainerBase <|-- CVoiceContainerLoopXFade
    CVoiceContainerAsyncGenerator <|-- CVoiceContainerGranulator
    CVoiceContainerGenerator <|-- CVoiceContainerShapedNoise
    CVoiceContainerAsyncGenerator <|-- CVoiceContainerStaticAdditiveSynth
    CVoiceContainerGenerator <|-- CVoiceContainerRealtimeFMSineWave
    CVoiceContainerGenerator <|-- CVoiceContainerNull
    CVoiceContainerBase <|-- CVoiceContainerDefault
    CVoiceContainerAsyncGenerator <|-- CVoiceContainerRandomSampler
    CVoiceContainerBase <|-- CVoiceContainerBlender
    CVoiceContainerLoopTrigger *-- CSoundContainerReference
    CVoiceContainerEnum *-- CSoundContainerReferenceArray
    CVoiceContainerSwitch *-- CSoundContainerReference
    CVoiceContainerSelector *-- PlayBackMode_t
    CVoiceContainerSelector *-- CSoundContainerReferenceArray
    CVoiceContainerMultiBlender *-- CSoundContainerReferenceArray
    CVoiceContainerEnvelope --> CVoiceContainerAnalysisBase
    CVoiceContainerParameterBlender *-- CSoundContainerReference
    CAudioSentence *-- CAudioPhonemeTag
    CAudioSentence *-- CAudioEmphasisSample
    CAudioSentence *-- CAudioMorphData
    CSoundContainerReferenceArray --> CVoiceContainerBase
    CVoiceContainerSetElement *-- CSoundContainerReference
    CVoiceContainerSet *-- CVoiceContainerSetElement
    CVoiceContainerEnvelopeAnalyzer *-- EMode_t
    CVoiceContainerLoopXFade *-- CSoundContainerReference
    CVoiceContainerBase *-- CVSound
    CVoiceContainerBase --> CVoiceContainerAnalysisBase
    CSoundContainerReference --> CVoiceContainerBase
    CVSound *-- CVSoundFormat_t
    CVSound *-- CAudioSentence
    "CVoiceContainerStaticAdditiveSynth::CTone" *-- CVoiceContainerStaticAdditiveSynth
    "CVoiceContainerStaticAdditiveSynth::CHarmonic" *-- EWaveform
    "CVoiceContainerStaticAdditiveSynth::CHarmonic" *-- EMidiNote
    "CVoiceContainerStaticAdditiveSynth::CHarmonic" *-- CVoiceContainerStaticAdditiveSynth
    CVoiceContainerBlender *-- CSoundContainerReference
```
