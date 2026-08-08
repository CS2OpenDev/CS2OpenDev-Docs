---
layout: default
title: CMixControlRemap
nav_exclude: true
---

[Schemas](../../schemas.md) / [sounddoc_lib](../sounddoc_lib.md) / CMixControlRemap

# CMixControlRemap

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** sounddoc_lib

**Inherits from:** [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md)

**Metadata:** `MPropertyDescription Remap a control value using a clamped linear range or clamped power curve.  Allows you to stretch and clip a control signal.`, `MPropertyFriendlyName VMix Control Remap Node`

**Relationships:**

```mermaid
classDiagram
    CMixPropertyBase <|-- CMixControlRemap
```

## Memory layout

10 fields (5 declared here, 5 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyDescription Node name` `MPropertyFriendlyName Name` `MPropertySortPriority 1` |
| `0x10` | `m_Comment` | CUtlString | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyDescription Description of how this is used  the graph for people reading the graph` `MPropertySortPriority -2` |
| `0x18` | `m_bActive` | bool | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x19` | `m_bSolo` | bool | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x1a` | `m_bEditProperties` | bool | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x20` | `m_flInputMin` | float32 |  | `MPropertyFriendlyName Input Min` |
| `0x24` | `m_flInputMax` | float32 |  | `MPropertyFriendlyName Input Max` |
| `0x28` | `m_flOutputStart` | float32 |  | `MPropertyFriendlyName Output Start` |
| `0x2c` | `m_flOutputEnd` | float32 |  | `MPropertyFriendlyName Output End` |
| `0x30` | `m_flPower` | float32 |  | `MPropertyAttributeRange biased 0.02 20` `MPropertyFriendlyName Nonlinear power (1.0 = linear)` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CMixControlRemap&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_Comment&quot;: &quot;&quot;,
	&quot;m_bActive&quot;: true,
	&quot;m_bSolo&quot;: false,
	&quot;m_bEditProperties&quot;: false,
	&quot;m_flInputMin&quot;: 0.000000,
	&quot;m_flInputMax&quot;: 1.000000,
	&quot;m_flOutputStart&quot;: 0.000000,
	&quot;m_flOutputEnd&quot;: 1.000000,
	&quot;m_flPower&quot;: 1.000000
}</pre>
</details>
