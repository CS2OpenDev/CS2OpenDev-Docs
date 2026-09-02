---
title: CMixEnvelopeTrigger
module: sounddoc_lib
kind: class
---

[Schemas](../../schemas.md) / [sounddoc_lib](../sounddoc_lib.md) / CMixEnvelopeTrigger

# CMixEnvelopeTrigger

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** sounddoc_lib

**Inherits from:** [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md)

**Metadata:** `MPropertyDescription Used to create reverb effects based on a model of a reverb plate.`, `MPropertyFriendlyName VMix Envelope Trigger Control Node`

**Relationships:**

```mermaid
classDiagram
    CMixPropertyBase <|-- CMixEnvelopeTrigger
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
| `0x20` | `m_flBaseValue` | float32 |  | `MPropertyFriendlyName Base Value` |
| `0x24` | `m_flDestinationValue` | float32 |  | `MPropertyFriendlyName Destination Value` |
| `0x28` | `m_flAttackTime` | float32 |  | `MPropertyFriendlyName Attack Time (seconds)` |
| `0x2c` | `m_flHoldTime` | float32 |  | `MPropertyFriendlyName Hold Time (seconds)` |
| `0x30` | `m_flReleaseTime` | float32 |  | `MPropertyFriendlyName Release Time (seconds)` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CMixEnvelopeTrigger&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_Comment&quot;: &quot;&quot;,
	&quot;m_bActive&quot;: true,
	&quot;m_bSolo&quot;: false,
	&quot;m_bEditProperties&quot;: false,
	&quot;m_flBaseValue&quot;: 0.000000,
	&quot;m_flDestinationValue&quot;: 1.000000,
	&quot;m_flAttackTime&quot;: 0.400000,
	&quot;m_flHoldTime&quot;: 0.200000,
	&quot;m_flReleaseTime&quot;: 0.400000
}</pre>
</details>
