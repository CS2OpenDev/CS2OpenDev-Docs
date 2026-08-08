---
layout: default
title: CSmartPropOperation_SaveColor
nav_exclude: true
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / CSmartPropOperation_SaveColor

# CSmartPropOperation_SaveColor

**Kind:** class · **Size:** 88 bytes (`0x58`) · **Align:** 8 · **Module:** smartprops

**Inherits from:** [CSmartPropOperation](../smartprops/CSmartPropOperation.md)

**Metadata:** `MPropertyDescription Save the current color tint value to a specified variable`, `MPropertyFriendlyName Save Current Color`, `MVDataClassGroup State`

**Relationships:**

```mermaid
classDiagram
    CSmartPropOperation <|-- CSmartPropOperation_SaveColor
    CSmartPropModifier <|-- CSmartPropOperation
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_bEnabled` | CSmartPropAttributeBool | [CSmartPropModifier](../smartprops/CSmartPropModifier.md) | `MVDataEnableKey` |
| `0x50` | `m_VariableName` | CUtlString |  | `MPropertyAttributeEditor SmartPropItemNameEditor( Variable:Color )` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CSmartPropOperation_SaveColor&quot;,
	&quot;m_bEnabled&quot;: true,
	&quot;m_VariableName&quot;: &quot;&quot;
}</pre>
</details>
