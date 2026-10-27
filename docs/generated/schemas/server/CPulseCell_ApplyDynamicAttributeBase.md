---
title: CPulseCell_ApplyDynamicAttributeBase
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / CPulseCell_ApplyDynamicAttributeBase

# CPulseCell_ApplyDynamicAttributeBase

> Source: **Build 26144732** · 2026-10-22 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 216 bytes (`0xd8`) · **Align:** n/a (unspecified) · **Module:** server

**Inherits from:** [CPulseCell_BaseYieldingInflow](../pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md)

**Derived by:** [CPulseCell_ApplyDynamicAttributeEHandle](../server/CPulseCell_ApplyDynamicAttributeEHandle.md), [CPulseCell_ApplyDynamicAttributeInt](../server/CPulseCell_ApplyDynamicAttributeInt.md), [CPulseCell_ApplyDynamicAttributeString](../server/CPulseCell_ApplyDynamicAttributeString.md)

**Metadata:** `MPropertyDescription Applies dynamic attributes onto an entity, as long as the cursor is active on this node`, `MPropertyFriendlyName Apply Dynamic Attribute To Entity`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_ApplyDynamicAttributeBase
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_ApplyDynamicAttributeBase <|-- CPulseCell_ApplyDynamicAttributeEHandle
    CPulseCell_ApplyDynamicAttributeBase <|-- CPulseCell_ApplyDynamicAttributeInt
    CPulseCell_ApplyDynamicAttributeBase <|-- CPulseCell_ApplyDynamicAttributeString
```

## Memory layout

3 fields (0 declared here, 3 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nEditorNodeID` | [PulseDocNodeID_t](../pulse_runtime_lib/PulseDocNodeID_t.md) | [CPulseCell_Base](../pulse_runtime_lib/CPulseCell_Base.md) | `MFgdFromSchemaCompletelySkipField` |
| `0x48` | `m_BaseFlow_OnAfterCancel` | [CPulse_ResumePoint](../pulse_runtime_lib/CPulse_ResumePoint.md) | [CPulseCell_BaseYieldingInflow](../pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) | `MPulseFGDSkipField` |
| `0x90` | `m_BaseFlow_WhileActive` | [CPulse_ResumePoint](../pulse_runtime_lib/CPulse_ResumePoint.md) | [CPulseCell_BaseYieldingInflow](../pulse_runtime_lib/CPulseCell_BaseYieldingInflow.md) | `MPulseFGDSkipField` |
