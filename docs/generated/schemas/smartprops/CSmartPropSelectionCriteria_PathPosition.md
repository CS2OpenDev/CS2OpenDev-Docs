---
layout: default
title: CSmartPropSelectionCriteria_PathPosition
nav_exclude: true
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / CSmartPropSelectionCriteria_PathPosition

# CSmartPropSelectionCriteria_PathPosition

**Kind:** class · **Size:** 392 bytes (`0x188`) · **Align:** 8 · **Module:** smartprops

**Inherits from:** [CSmartPropSelectionCriteria](../smartprops/CSmartPropSelectionCriteria.md)

**Metadata:** `MPropertyDescription Specifies the path positions at which this element may appear.`, `MPropertyFriendlyName Valid Path Positions`, `MVDataComponentValidGrandParents`

**Relationships:**

```mermaid
classDiagram
    CSmartPropSelectionCriteria <|-- CSmartPropSelectionCriteria_PathPosition
    CSmartPropSelectionCriteria_PathPosition *-- CSmartPropAttributePathPositions
```

## Memory layout

6 fields (5 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_bEnabled` | CSmartPropAttributeBool | [CSmartPropSelectionCriteria](../smartprops/CSmartPropSelectionCriteria.md) | `MVDataEnableKey` |
| `0x48` | `m_PlaceAtPositions` | [CSmartPropAttributePathPositions](../smartprops/CSmartPropAttributePathPositions.md) |  | `MPropertyDescription Specifies the method to use to determine which positions this element should be placed at along the path.` |
| `0x88` | `m_nPlaceEveryNthPosition` | CSmartPropAttributeInt |  | `MPropertyDescription Specifies the spacing between positions. For example, a value of 1 will place the element at very position, 2 every other position, 3 every third position` `MPropertySuppressExpr ( m_PlaceAtPositions == ALL ) \|\| ( m_PlaceAtPositions == START_AND_END ) \|\| ( m_PlaceAtPositions == CONTROL_POINTS )` |
| `0xc8` | `m_nNthPositionIndexOffset` | CSmartPropAttributeInt |  | `MPropertyDescription Specifies an offset to use when determining the Nth position to place an element at. For example if placing at every third position with an offset of 0, an element will appear at positions 1, 4, 7, and so on. But if an offset of 2 is set instead of 0, then an element will appear at positions 3, 6, and 9 and so on.` `MPropertySuppressExpr ( m_PlaceAtPositions == ALL ) \|\| ( m_PlaceAtPositions == START_AND_END ) \|\| ( m_PlaceAtPositions == CONTROL_POINTS )` |
| `0x108` | `m_bAllowAtStart` | CSmartPropAttributeBool |  | `MPropertyDescription Should this element be placed at the first positions on the path` |
| `0x148` | `m_bAllowAtEnd` | CSmartPropAttributeBool |  | `MPropertyDescription Should this element be placed at the last positions on the path` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CSmartPropSelectionCriteria_PathPosition&quot;,
	&quot;m_bEnabled&quot;: true,
	&quot;m_PlaceAtPositions&quot;: &quot;ALL&quot;,
	&quot;m_nPlaceEveryNthPosition&quot;: 2,
	&quot;m_nNthPositionIndexOffset&quot;: 0,
	&quot;m_bAllowAtStart&quot;: true,
	&quot;m_bAllowAtEnd&quot;: true
}</pre>
</details>
