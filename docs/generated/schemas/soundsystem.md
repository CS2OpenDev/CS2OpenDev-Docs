---
layout: default
title: soundsystem
parent: Schemas
nav_exclude: true
---

# Module: soundsystem

[📊 View UML Diagram](../diagrams/soundsystem.md)

35 types. Each links to its own page with the full field layout.

| Type | Kind | Size | Fields | Inherits |
|------|------|------|--------|----------|
| [CDSPMixgroupModifier](soundsystem/CDSPMixgroupModifier.md) | class | 32 | 6 |  |
| [CDSPPresetMixgroupModifierTable](soundsystem/CDSPPresetMixgroupModifierTable.md) | class | 24 | 1 |  |
| [CDspPresetModifierList](soundsystem/CDspPresetModifierList.md) | class | 32 | 2 |  |
| [CSndBeatPattern](soundsystem/CSndBeatPattern.md) | class | 152 | 15 |  |
| [CSndBeatPatternManager](soundsystem/CSndBeatPatternManager.md) | class | 144 | 2 |  |
| [CSndBeatTrack](soundsystem/CSndBeatTrack.md) | class | 152 | 5 |  |
| [CSndSeqInstBaseSchema](soundsystem/CSndSeqInstBaseSchema.md) | class | 32 | 5 |  |
| [CSndSeqInstMidiSampler](soundsystem/CSndSeqInstMidiSampler.md) | class | 224 | 11 | [CSndSeqInstBaseSchema](soundsystem/CSndSeqInstBaseSchema.md) |
| [CSndSeqInstSndEvtSchema](soundsystem/CSndSeqInstSndEvtSchema.md) | class | 32 | 0 | [CSndSeqInstBaseSchema](soundsystem/CSndSeqInstBaseSchema.md) |
| [CSndSeqInstruments](soundsystem/CSndSeqInstruments.md) | class | 40 | 0 | [ISndSeqInstruments](soundsystem/ISndSeqInstruments.md) |
| [CSosGroupActionLimitSchema](soundsystem/CSosGroupActionLimitSchema.md) | class | 24 | 5 | [CSosGroupActionSchema](soundsystem/CSosGroupActionSchema.md) |
| [CSosGroupActionMemberCountEnvelopeSchema](soundsystem/CSosGroupActionMemberCountEnvelopeSchema.md) | class | 48 | 8 | [CSosGroupActionSchema](soundsystem/CSosGroupActionSchema.md) |
| [CSosGroupActionOcclusionSchema](soundsystem/CSosGroupActionOcclusionSchema.md) | class | 32 | 6 | [CSosGroupActionSchema](soundsystem/CSosGroupActionSchema.md) |
| [CSosGroupActionSchema](soundsystem/CSosGroupActionSchema.md) | class | 8 | 0 |  |
| [CSosGroupActionSetSoundeventParameterSchema](soundsystem/CSosGroupActionSetSoundeventParameterSchema.md) | class | 40 | 5 | [CSosGroupActionSchema](soundsystem/CSosGroupActionSchema.md) |
| [CSosGroupActionSoundeventClusterSchema](soundsystem/CSosGroupActionSoundeventClusterSchema.md) | class | 80 | 7 | [CSosGroupActionSchema](soundsystem/CSosGroupActionSchema.md) |
| [CSosGroupActionSoundeventCountSchema](soundsystem/CSosGroupActionSoundeventCountSchema.md) | class | 24 | 2 | [CSosGroupActionSchema](soundsystem/CSosGroupActionSchema.md) |
| [CSosGroupActionSoundeventMinMaxValuesSchema](soundsystem/CSosGroupActionSoundeventMinMaxValuesSchema.md) | class | 64 | 10 | [CSosGroupActionSchema](soundsystem/CSosGroupActionSchema.md) |
| [CSosGroupActionSoundeventPrioritySchema](soundsystem/CSosGroupActionSoundeventPrioritySchema.md) | class | 56 | 4 | [CSosGroupActionSchema](soundsystem/CSosGroupActionSchema.md) |
| [CSosGroupActionTimeBlockLimitSchema](soundsystem/CSosGroupActionTimeBlockLimitSchema.md) | class | 16 | 2 | [CSosGroupActionSchema](soundsystem/CSosGroupActionSchema.md) |
| [CSosGroupActionTimeLimitSchema](soundsystem/CSosGroupActionTimeLimitSchema.md) | class | 16 | 1 | [CSosGroupActionSchema](soundsystem/CSosGroupActionSchema.md) |
| [CSosSoundEventGroupSchema](soundsystem/CSosSoundEventGroupSchema.md) | class | 112 | 16 |  |
| [CSoundEventMetaData](soundsystem/CSoundEventMetaData.md) | class | 8 | 1 |  |
| [CVoiceContainerVMixSnd](soundsystem/CVoiceContainerVMixSnd.md) | class | 472 | 0 | [CVoiceContainerBase](soundsystem_voicecontainers/CVoiceContainerBase.md) |
| [ISndSeqInstruments](soundsystem/ISndSeqInstruments.md) | class | 8 | 0 |  |
| [KeyGroup_t](soundsystem/KeyGroup_t.md) | class | 16 | 5 |  |
| [SamplerVoice_t](soundsystem/SamplerVoice_t.md) | class | 8 | 1 |  |
| [SelectedEditItemInfo_t](soundsystem/SelectedEditItemInfo_t.md) | class | 24 | 1 |  |
| [SndBeatEventKeyedFloats_t](soundsystem/SndBeatEventKeyedFloats_t.md) | class | 24 | 1 | [SndBeatEventKeys_t](soundsystem/SndBeatEventKeys_t.md) |
| [SndBeatEventKeyedMidiNotes_t](soundsystem/SndBeatEventKeyedMidiNotes_t.md) | class | 24 | 3 | [SndBeatEventKeys_t](soundsystem/SndBeatEventKeys_t.md) |
| [SndBeatEventKeyedSndEvts_t](soundsystem/SndBeatEventKeyedSndEvts_t.md) | class | 24 | 1 | [SndBeatEventKeys_t](soundsystem/SndBeatEventKeys_t.md) |
| [SndBeatEventKeys_t](soundsystem/SndBeatEventKeys_t.md) | class | 16 | 1 |  |
| [SndBeatTimeSignature_t](soundsystem/SndBeatTimeSignature_t.md) | class | 2 | 2 |  |
| [SosEditItemInfo_t](soundsystem/SosEditItemInfo_t.md) | class | 48 | 5 |  |
| [VelocityZone_t](soundsystem/VelocityZone_t.md) | class | 20 | 4 |  |
