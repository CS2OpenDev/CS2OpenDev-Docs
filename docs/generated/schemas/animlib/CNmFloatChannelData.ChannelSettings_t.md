---
layout: default
title: "CNmFloatChannelData::ChannelSettings_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmFloatChannelData::ChannelSettings_t

# CNmFloatChannelData::ChannelSettings_t

**Kind:** class · **Size:** 12 bytes (`0xc`) · **Align:** 4 · **Module:** animlib

**Relationships:**

```mermaid
classDiagram
    "CNmFloatChannelData::ChannelSettings_t" *-- NmCompressionSettings_t
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_range` | [NmCompressionSettings_t](../animlib/NmCompressionSettings_t.md)::QuantizationRange_t |  |  |
| `0x8` | `m_bIsStatic` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_range&quot;:
	{
		&quot;m_flRangeStart&quot;: 0.000000,
		&quot;m_flRangeLength&quot;: -1.000000
	},
	&quot;m_bIsStatic&quot;: false
}</pre>
</details>
