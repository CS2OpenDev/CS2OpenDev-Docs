---
layout: default
title: "UML: soundsystem"
parent: Schemas
nav_exclude: true
---

# UML: soundsystem

Class relationships (inheritance and composition) for the `soundsystem` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CSndSeqInstBaseSchema <|-- CSndSeqInstMidiSampler
    CSndSeqInstBaseSchema <|-- CSndSeqInstSndEvtSchema
    ISndSeqInstruments <|-- CSndSeqInstruments
    CSosGroupActionSchema <|-- CSosGroupActionLimitSchema
    CSosGroupActionSchema <|-- CSosGroupActionMemberCountEnvelopeSchema
    CSosGroupActionSchema <|-- CSosGroupActionOcclusionSchema
    CSosGroupActionSchema <|-- CSosGroupActionSetSoundeventParameterSchema
    CSosGroupActionSchema <|-- CSosGroupActionSoundeventClusterSchema
    CSosGroupActionSchema <|-- CSosGroupActionSoundeventCountSchema
    CSosGroupActionSchema <|-- CSosGroupActionSoundeventMinMaxValuesSchema
    CSosGroupActionSchema <|-- CSosGroupActionSoundeventPrioritySchema
    CSosGroupActionSchema <|-- CSosGroupActionTimeBlockLimitSchema
    CSosGroupActionSchema <|-- CSosGroupActionTimeLimitSchema
    CVoiceContainerBase <|-- CVoiceContainerVMixSnd
    SndBeatEventKeys_t <|-- SndBeatEventKeyedFloats_t
    SndBeatEventKeys_t <|-- SndBeatEventKeyedMidiNotes_t
    SndBeatEventKeys_t <|-- SndBeatEventKeyedSndEvts_t
    CDSPPresetMixgroupModifierTable *-- CDspPresetModifierList
    CDspPresetModifierList *-- CDSPMixgroupModifier
    CSndBeatPattern *-- SndBeatLaunchSyncType_t
    CSndBeatPattern *-- SndBeatTimeSignature_t
    CSndBeatPattern *-- SndBeatEventType_t
    CSndBeatPattern *-- SndBeatKeyType_t
    CSndBeatPattern *-- SndBeatEventKeys_t
    CSndBeatPattern *-- SndBeatEventKeyedFloats_t
    CSndBeatPattern *-- SndBeatEventKeyedSndEvts_t
    CSndBeatPattern *-- SndBeatEventKeyedMidiNotes_t
    CSndBeatPatternManager *-- CSndBeatPattern
    CSndBeatPatternManager *-- CSndBeatTrack
    CSndBeatTrack *-- SndBeatTrackPlaybackType_t
    CSndSeqInstBaseSchema *-- SndSeqInstrumentType_t
    CSosGroupActionLimitSchema *-- SosActionStopType_t
    CSosGroupActionLimitSchema *-- SosActionLimitSortType_t
    CSosGroupActionSetSoundeventParameterSchema *-- SosActionSetParamSortType_t
    CSosSoundEventGroupSchema *-- SosGroupType_t
    CSosSoundEventGroupSchema *-- SosGroupFieldBehavior_t
    CSosSoundEventGroupSchema --> CSosGroupActionSchema
    KeyGroup_t --> VelocityZone_t
    SelectedEditItemInfo_t *-- SosEditItemInfo_t
    SosEditItemInfo_t *-- SosEditItemType_t
```
