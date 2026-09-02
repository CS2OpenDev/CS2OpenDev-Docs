---
title: "UML: animationsystem"
---

# UML: animationsystem

Class relationships (inheritance and composition) for the `animationsystem` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    AnimationSnapshotBase_t <|-- AnimationSnapshot_t
    AnimationDecodeDebugDump_t *-- AnimationProcessingType_t
    AnimationDecodeDebugDump_t *-- AnimationDecodeDebugDumpElement_t
    AnimationSnapshotBase_t *-- AnimationSnapshotType_t
    AnimationSnapshotBase_t *-- AnimationDecodeDebugDumpElement_t
    CAnimData *-- CAnimDesc
    CAnimData *-- CAnimDecoder
    CAnimData *-- CAnimFrameSegment
    CAnimDesc *-- CAnimDesc_Flag
    CAnimDesc *-- CAnimEncodedFrames
    CAnimDesc *-- CAnimMovement
    CAnimDesc *-- CAnimEventDefinition
    CAnimDesc *-- CAnimActivity
    CAnimDesc *-- CAnimLocalHierarchy
    CAnimDesc *-- CAnimSequenceParams
    CAnimEncodeDifference *-- CAnimBoneDifference
    CAnimEncodeDifference *-- CAnimMorphDifference
    CAnimEncodeDifference *-- CAnimUserDifference
    CAnimEncodedFrames *-- CAnimFrameBlockAnim
    CAnimEncodedFrames *-- CAnimEncodeDifference
    CAnimKeyData *-- CAnimBone
    CAnimKeyData *-- CAnimUser
    CAnimKeyData *-- CAnimDataChannelDesc
    CAnimationGroup *-- CAnimKeyData
    CMoodVData *-- MoodType_t
    CMoodVData *-- MoodAnimationLayer_t
    CSeqAutoLayer *-- CSeqAutoLayerFlag
    CSeqCmdSeqDesc *-- CSeqSeqDescFlag
    CSeqCmdSeqDesc *-- CSeqTransition
    CSeqCmdSeqDesc *-- CSeqCmdLayer
    CSeqCmdSeqDesc *-- CAnimEventDefinition
    CSeqCmdSeqDesc *-- CAnimActivity
    CSeqCmdSeqDesc *-- CSeqPoseSetting
    CSeqMultiFetch *-- CSeqMultiFetchFlag
    CSeqS1SeqDesc *-- CSeqSeqDescFlag
    CSeqS1SeqDesc *-- CSeqMultiFetch
    CSeqS1SeqDesc *-- CSeqAutoLayer
    CSeqS1SeqDesc *-- CSeqIKLock
    CSeqS1SeqDesc *-- CSeqTransition
    CSeqS1SeqDesc *-- CAnimActivity
    CSeqSynthAnimDesc *-- CSeqSeqDescFlag
    CSeqSynthAnimDesc *-- CSeqTransition
    CSeqSynthAnimDesc *-- CAnimActivity
    CSequenceGroupData *-- CSeqS1SeqDesc
    CSequenceGroupData *-- CSeqSynthAnimDesc
    CSequenceGroupData *-- CSeqCmdSeqDesc
    CSequenceGroupData *-- CSeqBoneMaskList
    CSequenceGroupData *-- CSeqScaleSet
    CSequenceGroupData *-- CSeqPoseParamDesc
    CSequenceGroupData *-- CSeqIKLock
    MoodAnimationLayer_t *-- MoodAnimation_t
```
