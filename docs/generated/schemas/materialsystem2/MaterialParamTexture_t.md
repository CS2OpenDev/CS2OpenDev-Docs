---
title: MaterialParamTexture_t
module: materialsystem2
kind: class
---

[Schemas](../../schemas.md) / [materialsystem2](../materialsystem2.md) / MaterialParamTexture_t

# MaterialParamTexture_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** materialsystem2

**Inherits from:** [MaterialParam_t](../materialsystem2/MaterialParam_t.md)

**Relationships:**

```mermaid
classDiagram
    MaterialParam_t <|-- MaterialParamTexture_t
    MaterialParamTexture_t *-- InfoForResourceTypeCTextureBase
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString | [MaterialParam_t](../materialsystem2/MaterialParam_t.md) |  |
| `0x8` | `m_pValue` | CStrongHandle< [InfoForResourceTypeCTextureBase](../resourcesystem/InfoForResourceTypeCTextureBase.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_pValue&quot;: &quot;&quot;
}</pre>
</details>
