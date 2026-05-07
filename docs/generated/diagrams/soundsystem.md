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
    CSosGroupActionSchema <|-- CSosGroupActionTimeLimitSchema
    CSosGroupActionSchema <|-- CSosGroupActionMemberCountEnvelopeSchema
    CSosGroupActionSchema <|-- CSosGroupActionTimeBlockLimitSchema
    CSosGroupActionSchema <|-- CSosGroupActionLimitSchema
    CSosGroupActionSchema <|-- CSosGroupActionSoundeventCountSchema
    CSndSeqInstBaseSchema <|-- CSndSeqInstMidiSampler
    ISndSeqInstruments <|-- CSndSeqInstruments
    CSndSeqInstBaseSchema <|-- CSndSeqInstSndEvtSchema
    CSosGroupActionSchema <|-- CSosGroupActionSoundeventPrioritySchema
    CSosGroupActionSchema <|-- CSosGroupActionSoundeventMinMaxValuesSchema
    CSosGroupActionSchema <|-- CSosGroupActionSetSoundeventParameterSchema
    CSosGroupActionSchema <|-- CSosGroupActionSoundeventClusterSchema
    CSosGroupActionSchema <|-- CSosGroupActionOcclusionSchema
    CSosGroupActionLimitSchema *-- SosActionStopType_t
    CSosGroupActionLimitSchema *-- SosActionLimitSortType_t
    KeyGroup_t --> VelocityZone_t
    SosEditItemInfo_t *-- SosEditItemType_t
    CDspPresetModifierList *-- CDSPMixgroupModifier
    CSndSeqInstBaseSchema *-- SndSeqInstrumentType_t
    CSndSeqInstBaseSchema *-- SndSeqPlayerType_t
    CSosSoundEventGroupSchema *-- SosGroupType_t
    CSosSoundEventGroupSchema *-- SosGroupFieldBehavior_t
    CSosSoundEventGroupSchema --> CSosGroupActionSchema
    SelectedEditItemInfo_t *-- SosEditItemInfo_t
    CSosGroupActionSetSoundeventParameterSchema *-- SosActionSetParamSortType_t
    CDSPPresetMixgroupModifierTable *-- CDspPresetModifierList
```
