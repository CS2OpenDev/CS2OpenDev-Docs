---
layout: default
title: "CNmGraphDocDataDictionary::ParameterSet_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animdoclib](../animdoclib.md) / CNmGraphDocDataDictionary::ParameterSet_t

# CNmGraphDocDataDictionary::ParameterSet_t

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animdoclib

**Metadata:** `MPropertyAutoExpandSelf`

**Relationships:**

```mermaid
classDiagram
    "CNmGraphDocDataDictionary::ParameterSet_t" *-- CNmGraphDocDataDictionary
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString |  | `MPropertyFlattenIntoParentRow` |
| `0x8` | `m_parameters` | CUtlVector< [CNmGraphDocDataDictionary](../animdoclib/CNmGraphDocDataDictionary.md)::Parameter_t > |  | `MPropertyAutoExpandSelf` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_parameters&quot;:
	[
	]
}</pre>
</details>
