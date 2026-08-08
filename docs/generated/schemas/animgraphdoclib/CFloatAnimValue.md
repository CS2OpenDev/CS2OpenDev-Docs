---
layout: default
title: CFloatAnimValue
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CFloatAnimValue

# CFloatAnimValue

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animgraphdoclib

**Relationships:**

```mermaid
classDiagram
    CFloatAnimValue *-- AnimParamID
    CFloatAnimValue *-- EAnimValueSource
```

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_flConstValue` | float32 |  | `MPropertySuppressField` |
| `0x10` | `m_paramName` | CUtlString |  | `MPropertySuppressField` |
| `0x18` | `m_paramID` | [AnimParamID](../modellib/AnimParamID.md) |  | `MPropertySuppressField` |
| `0x1c` | `m_eSource` | [EAnimValueSource](../!GlobalTypes/EAnimValueSource.md) |  | `MPropertySuppressField` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CFloatAnimValue&quot;,
	&quot;m_flConstValue&quot;: 0.000000,
	&quot;m_paramName&quot;: &quot;&quot;,
	&quot;m_paramID&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_eSource&quot;: &quot;Constant&quot;
}</pre>
</details>
