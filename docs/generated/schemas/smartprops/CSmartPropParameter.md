---
layout: default
title: CSmartPropParameter
nav_exclude: true
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / CSmartPropParameter

# CSmartPropParameter

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 255 · **Module:** smartprops

**Derived by:** [CSmartPropChoice](../smartprops/CSmartPropChoice.md), [CSmartPropVariable](../smartprops/CSmartPropVariable.md)

**Metadata:** `MVDataAnonymousNode`, `MVDataNodeType 1`, `MVDataRoot`

**Relationships:**

```mermaid
classDiagram
    CSmartPropParameter <|-- CSmartPropChoice
    CSmartPropParameter <|-- CSmartPropVariable
```

## Memory layout

1 fields (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nElementID` | int32 |  | `MPropertySuppressField` `MVDataUniqueMonotonicInt _editor/next_element_id` |
