---
layout: default
title: CMixSum
nav_exclude: true
---

[Schemas](../../schemas.md) / [sounddoc_lib](../sounddoc_lib.md) / CMixSum

# CMixSum

**Kind:** class · **Size:** 128 bytes (`0x80`) · **Align:** 8 · **Module:** sounddoc_lib

**Inherits from:** [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md)

**Metadata:** `MPropertyDescription Mixes audio tracks together into a single track.  Mix levels can be automated.`, `MPropertyFriendlyName VMix Mixer Audio Node`

**Relationships:**

```mermaid
classDiagram
    CMixPropertyBase <|-- CMixSum
```

## Memory layout

14 fields (9 declared here, 5 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_name` | CUtlString | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyDescription Node name` `MPropertyFriendlyName Name` `MPropertySortPriority 1` |
| `0x10` | `m_Comment` | CUtlString | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyDescription Description of how this is used  the graph for people reading the graph` `MPropertySortPriority -2` |
| `0x18` | `m_bActive` | bool | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x19` | `m_bSolo` | bool | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x1a` | `m_bEditProperties` | bool | [CMixPropertyBase](../sounddoc_lib/CMixPropertyBase.md) | `MPropertyHideField` `MPropertySortPriority -1` |
| `0x20` | `m_flVolume1` | float32 |  | `MPropertyFriendlyName Volume:1` |
| `0x24` | `m_flVolume2` | float32 |  | `MPropertyFriendlyName Volume:2` |
| `0x28` | `m_flVolume3` | float32 |  | `MPropertyFriendlyName Volume:3` |
| `0x2c` | `m_flVolume4` | float32 |  | `MPropertyFriendlyName Volume:4` |
| `0x30` | `m_flVolume5` | float32 |  | `MPropertyFriendlyName Volume:5` |
| `0x34` | `m_flVolume6` | float32 |  | `MPropertyFriendlyName Volume:6` |
| `0x38` | `m_flVolume7` | float32 |  | `MPropertyFriendlyName Volume:7` |
| `0x3c` | `m_flVolume8` | float32 |  | `MPropertyFriendlyName Volume:8` |
| `0x40` | `m_channelName` | CUtlString[8] |  | `MPropertyFriendlyName Channel Name` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CMixSum&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_Comment&quot;: &quot;&quot;,
	&quot;m_bActive&quot;: true,
	&quot;m_bSolo&quot;: false,
	&quot;m_bEditProperties&quot;: false,
	&quot;m_flVolume1&quot;: 1.000000,
	&quot;m_flVolume2&quot;: 1.000000,
	&quot;m_flVolume3&quot;: 1.000000,
	&quot;m_flVolume4&quot;: 1.000000,
	&quot;m_flVolume5&quot;: 1.000000,
	&quot;m_flVolume6&quot;: 1.000000,
	&quot;m_flVolume7&quot;: 1.000000,
	&quot;m_flVolume8&quot;: 1.000000,
	&quot;m_channelName&quot;:
	[
		&quot;Vol:1&quot;,
		&quot;Vol:2&quot;,
		&quot;Vol:3&quot;,
		&quot;Vol:4&quot;,
		&quot;Vol:5&quot;,
		&quot;Vol:6&quot;,
		&quot;Vol:7&quot;,
		&quot;Vol:8&quot;
	]
}</pre>
</details>
