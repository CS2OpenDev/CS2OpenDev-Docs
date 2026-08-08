---
layout: default
title: MaterialParamInt_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [materialsystem2](../materialsystem2.md) / MaterialParamInt_t

# MaterialParamInt_t

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** materialsystem2

**Inherits from:** [MaterialParam_t](../materialsystem2/MaterialParam_t.md)

**Relationships:**

```mermaid
classDiagram
    MaterialParam_t <|-- MaterialParamInt_t
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString | [MaterialParam_t](../materialsystem2/MaterialParam_t.md) |  |
| `0x8` | `m_nValue` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_nValue&quot;: 0
}</pre>
</details>
