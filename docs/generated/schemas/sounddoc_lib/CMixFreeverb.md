---
title: CMixFreeverb
module: sounddoc_lib
kind: class
---

[Schemas](../../schemas.md) / [sounddoc_lib](../sounddoc_lib.md) / CMixFreeverb

# CMixFreeverb

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** sounddoc_lib

**Inherits from:** [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md)

**Metadata:** `MPropertyDescription Used to create reverb effects based on a symmetrical room.`, `MPropertyFriendlyName VMix Freeverb Audio Node`

**Relationships:**

```mermaid
classDiagram
    CMixPropertyBase <|-- CMixFreeverb
```

## Memory layout

9 fields (4 declared here, 5 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyDescription Node name` `MPropertyFriendlyName Name` `MPropertySortPriority 1` |
| `0x10` | `m_Comment` | CUtlString | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyDescription Description of how this is used  the graph for people reading the graph` `MPropertySortPriority -2` |
| `0x18` | `m_bActive` | bool | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x19` | `m_bSolo` | bool | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x1a` | `m_bEditProperties` | bool | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x20` | `m_flRoomSize` | float32 |  | `MPropertyAttributeRange 0.0 1.0` `MPropertyFriendlyName Size` |
| `0x24` | `m_flDamp` | float32 |  | `MPropertyAttributeRange 0.0 1.0` `MPropertyFriendlyName Dampening Factor` |
| `0x28` | `m_flWidth` | float32 |  | `MPropertyAttributeRange 0.0 1.0` `MPropertyFriendlyName Width` |
| `0x2c` | `m_flLateReflections` | float32 |  | `MPropertyAttributeRange 0.0 1.0` `MPropertyFriendlyName Late Reflections` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CMixFreeverb&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_Comment&quot;: &quot;&quot;,
	&quot;m_bActive&quot;: true,
	&quot;m_bSolo&quot;: false,
	&quot;m_bEditProperties&quot;: false,
	&quot;m_flRoomSize&quot;: 0.500000,
	&quot;m_flDamp&quot;: 0.500000,
	&quot;m_flWidth&quot;: 0.500000,
	&quot;m_flLateReflections&quot;: 1.000000
}</pre>
</details>
