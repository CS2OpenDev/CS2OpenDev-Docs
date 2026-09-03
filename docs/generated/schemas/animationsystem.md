---
title: animationsystem
module: animationsystem
---

# Module: animationsystem

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

[📊 View UML Diagram](../diagrams/animationsystem.md)

54 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [AnimationDecodeDebugDumpElement_t](animationsystem/AnimationDecodeDebugDumpElement_t.md) | class | 112 | 6 |  |
| [AnimationDecodeDebugDump_t](animationsystem/AnimationDecodeDebugDump_t.md) | class | 32 | 2 |  |
| [AnimationSnapshotBase_t](animationsystem/AnimationSnapshotBase_t.md) | class | 272 | 9 |  |
| [AnimationSnapshot_t](animationsystem/AnimationSnapshot_t.md) | class | 288 | 2 | [AnimationSnapshotBase_t](animationsystem/AnimationSnapshotBase_t.md) |
| [CAnimActivity](animationsystem/CAnimActivity.md) | class | 32 | 4 |  |
| [CAnimBone](animationsystem/CAnimBone.md) | class | 72 | 7 |  |
| [CAnimBoneDifference](animationsystem/CAnimBoneDifference.md) | class | 48 | 5 |  |
| [CAnimData](animationsystem/CAnimData.md) | class | 112 | 5 |  |
| [CAnimDataChannelDesc](animationsystem/CAnimDataChannelDesc.md) | class | 144 | 9 |  |
| [CAnimDecoder](animationsystem/CAnimDecoder.md) | class | 24 | 3 |  |
| [CAnimDesc](animationsystem/CAnimDesc.md) | class | 464 | 15 |  |
| [CAnimDesc_Flag](animationsystem/CAnimDesc_Flag.md) | class | 8 | 8 |  |
| [CAnimEncodeDifference](animationsystem/CAnimEncodeDifference.md) | class | 168 | 7 |  |
| [CAnimEncodedFrames](animationsystem/CAnimEncodedFrames.md) | class | 216 | 5 |  |
| [CAnimEnum](animationsystem/CAnimEnum.md) | class | 1 | 1 |  |
| [CAnimEventDefinition](animationsystem/CAnimEventDefinition.md) | class | 64 | 7 |  |
| [CAnimFrameBlockAnim](animationsystem/CAnimFrameBlockAnim.md) | class | 32 | 3 |  |
| [CAnimFrameSegment](animationsystem/CAnimFrameSegment.md) | class | 32 | 4 |  |
| [CAnimKeyData](animationsystem/CAnimKeyData.md) | class | 120 | 6 |  |
| [CAnimLocalHierarchy](animationsystem/CAnimLocalHierarchy.md) | class | 48 | 6 |  |
| [CAnimMorphDifference](animationsystem/CAnimMorphDifference.md) | class | 16 | 1 |  |
| [CAnimMovement](animationsystem/CAnimMovement.md) | class | 44 | 7 |  |
| [CAnimSequenceParams](animationsystem/CAnimSequenceParams.md) | class | 8 | 2 |  |
| [CAnimUser](animationsystem/CAnimUser.md) | class | 24 | 2 |  |
| [CAnimUserDifference](animationsystem/CAnimUserDifference.md) | class | 24 | 2 |  |
| [CAnimationGroup](animationsystem/CAnimationGroup.md) | class | 328 | 8 |  |
| [CMoodVData](animationsystem/CMoodVData.md) | class | 256 | 3 |  |
| [CSeqAutoLayer](animationsystem/CSeqAutoLayer.md) | class | 28 | 7 |  |
| [CSeqAutoLayerFlag](animationsystem/CSeqAutoLayerFlag.md) | class | 8 | 8 |  |
| [CSeqBoneMaskList](animationsystem/CSeqBoneMaskList.md) | class | 96 | 5 |  |
| [CSeqCmdLayer](animationsystem/CSeqCmdLayer.md) | class | 24 | 9 |  |
| [CSeqCmdSeqDesc](animationsystem/CSeqCmdSeqDesc.md) | class | 144 | 12 |  |
| [CSeqIKLock](animationsystem/CSeqIKLock.md) | class | 12 | 4 |  |
| [CSeqMultiFetch](animationsystem/CSeqMultiFetch.md) | class | 112 | 10 |  |
| [CSeqMultiFetchFlag](animationsystem/CSeqMultiFetchFlag.md) | class | 6 | 6 |  |
| [CSeqPoseParamDesc](animationsystem/CSeqPoseParamDesc.md) | class | 32 | 5 |  |
| [CSeqPoseSetting](animationsystem/CSeqPoseSetting.md) | class | 64 | 8 |  |
| [CSeqS1SeqDesc](animationsystem/CSeqS1SeqDesc.md) | class | 288 | 11 |  |
| [CSeqScaleSet](animationsystem/CSeqScaleSet.md) | class | 80 | 5 |  |
| [CSeqSeqDescFlag](animationsystem/CSeqSeqDescFlag.md) | class | 11 | 11 |  |
| [CSeqSynthAnimDesc](animationsystem/CSeqSynthAnimDesc.md) | class | 64 | 6 |  |
| [CSeqTransition](animationsystem/CSeqTransition.md) | class | 8 | 2 |  |
| [CSequenceGroupData](animationsystem/CSequenceGroupData.md) | class | 312 | 14 |  |
| [FollowAttachmentData](animationsystem/FollowAttachmentData.md) | class | 8 | 2 |  |
| [HSequence](animationsystem/HSequence.md) | class | 4 | 1 |  |
| [MoodAnimationLayer_t](animationsystem/MoodAnimationLayer_t.md) | class | 96 | 12 |  |
| [MoodAnimation_t](animationsystem/MoodAnimation_t.md) | class | 16 | 2 |  |
| [AnimationProcessingType_t](animationsystem/AnimationProcessingType_t.md) | enum | — | 6 |  |
| [AnimationSnapshotType_t](animationsystem/AnimationSnapshotType_t.md) | enum | — | 7 |  |
| [BoneTransformSpace_t](animationsystem/BoneTransformSpace_t.md) | enum | — | 4 |  |
| [MoodType_t](animationsystem/MoodType_t.md) | enum | — | 2 |  |
| [ParticleAttachment_t](animationsystem/ParticleAttachment_t.md) | enum | — | 18 |  |
| [SeqCmd_t](animationsystem/SeqCmd_t.md) | enum | — | 17 |  |
| [SeqPoseSetting_t](animationsystem/SeqPoseSetting_t.md) | enum | — | 4 |  |
