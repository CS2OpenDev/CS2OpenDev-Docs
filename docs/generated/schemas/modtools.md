---
layout: default
title: modtools
parent: Schemas
nav_exclude: true
---

# Module: modtools

[📊 View UML Diagram](../diagrams/modtools.md)

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [CNmGraphDocAimCSNode](#cnmgraphdocaimcsnode) | class | CNmGraphDocFlowNode | 3 |
| [CnmGraphDocSnapWeaponNode](#cnmgraphdocsnapweaponnode) | class | CNmGraphDocFlowNode | 0 |

---

### CNmGraphDocAimCSNode

**Inherits from:** [CNmGraphDocFlowNode](animdoclib.md#cnmgraphdocflownode)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CNmGraphDocFlowNode <|-- CNmGraphDocAimCSNode
    CNmGraphDocNode <|-- CNmGraphDocFlowNode
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_flActionBlendTimeSeconds` | float32 |  |
| `m_flHandIKBlendInTimeSeconds` | float32 |  |
| `m_flPlantingBlendTimeSeconds` | float32 |  |

### CnmGraphDocSnapWeaponNode

**Inherits from:** [CNmGraphDocFlowNode](animdoclib.md#cnmgraphdocflownode)

**Metadata:** `MGetKV3ClassDefaults`

**Relationships:**

```mermaid
classDiagram
    CNmGraphDocFlowNode <|-- CnmGraphDocSnapWeaponNode
    CNmGraphDocNode <|-- CNmGraphDocFlowNode
```
