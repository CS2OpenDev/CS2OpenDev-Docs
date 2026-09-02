---
title: CSmartPropElement_PlaceOnMesh
module: smartprops
kind: class
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / CSmartPropElement_PlaceOnMesh

# CSmartPropElement_PlaceOnMesh

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 232 bytes (`0xe8`) · **Align:** 8 · **Module:** smartprops

**Inherits from:** [CSmartPropElement_Deformer](../smartprops/CSmartPropElement_Deformer.md)

**Metadata:** `MPropertyDescription Place Children on Mesh Components.`, `MPropertyFriendlyName Place on Mesh`, `MVDataExperimentalNodeSet`

**Relationships:**

```mermaid
classDiagram
    CSmartPropElement_Deformer <|-- CSmartPropElement_PlaceOnMesh
    CSmartPropElement_Group <|-- CSmartPropElement_Deformer
    CSmartPropElement <|-- CSmartPropElement_Group
    CSmartPropElement_PlaceOnMesh *-- CSmartPropAttributeOrientationMode
```

## Memory layout

8 fields (2 declared here, 6 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nElementID` | int32 | [CSmartPropElement](../smartprops/CSmartPropElement.md) | `MPropertySuppressField` `MVDataUniqueMonotonicInt _editor/next_element_id` |
| `0x10` | `m_bEnabled` | CSmartPropAttributeBool | [CSmartPropElement](../smartprops/CSmartPropElement.md) | `MPropertyDescription Is this element enabled? If not enabled, this element will not be evaluted and will have no effect on the result.` `MPropertySortPriority 10` `MVDataEnableKey` |
| `0x50` | `m_sLabel` | CUtlString | [CSmartPropElement](../smartprops/CSmartPropElement.md) | `MPropertyDescription Optional text that will appear in the outliner to help organize Smart Prop elements and communicate their purpose to other users.` `MPropertyFriendlyName Label` |
| `0x58` | `m_SelectionCriteria` | CUtlVector< [CSmartPropSelectionCriteria](../smartprops/CSmartPropSelectionCriteria.md)* > | [CSmartPropElement](../smartprops/CSmartPropElement.md) | `MPropertyFriendlyName Selection Criteria` `MVDataPromoteField 2` |
| `0x70` | `m_Modifiers` | CUtlVector< [CSmartPropModifier](../smartprops/CSmartPropModifier.md)* > | [CSmartPropElement](../smartprops/CSmartPropElement.md) | `MPropertyFriendlyName Modifiers` `MVDataPromoteField 2` |
| `0x88` | `m_Children` | CUtlVector< [CSmartPropElement](../smartprops/CSmartPropElement.md)* > | [CSmartPropElement_Group](../smartprops/CSmartPropElement_Group.md) | `MPropertyDescription List of child elements which will appear if this element appears` `MPropertyFriendlyName Children` `MVDataPromoteField 1` |
| `0xa0` | `m_nPickMode` | [CSmartPropAttributeOrientationMode](../smartprops/CSmartPropAttributeOrientationMode.md) |  | `MPropertyDescription Determine how child elements are oriented when mapped to face.` `MPropertyFriendlyName Orientation Mode` `MPropertyStartGroup` |
| `0xe0` | `m_MeshName` | CUtlString |  | `MPropertyDescription` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CSmartPropElement_PlaceOnMesh&quot;,
	&quot;m_nElementID&quot;: -1,
	&quot;m_bEnabled&quot;: true,
	&quot;m_sLabel&quot;: &quot;&quot;,
	&quot;m_SelectionCriteria&quot;:
	[
	],
	&quot;m_Modifiers&quot;:
	[
	],
	&quot;m_Children&quot;:
	[
	],
	&quot;m_nPickMode&quot;: &quot;FIRST_CLOSED_EDGE&quot;,
	&quot;m_MeshName&quot;: &quot;&quot;
}</pre>
</details>
