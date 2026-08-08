---
layout: default
title: MaterialGroupChoice_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / MaterialGroupChoice_t

# MaterialGroupChoice_t

**Kind:** class · **Size:** 128 bytes (`0x80`) · **Align:** 8 · **Module:** smartprops

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_MaterialGroupName` | CSmartPropAttributeMaterialGroup |  | `MPropertyAttributeEditor SmartPropAttributeEditor( MaterialGroupFromVariable )` `MPropertyDescription Specifies the name of the material group (skin) to use when displaying the specified model.` `MPropertyFriendlyName Material Group` |
| `0x40` | `m_flWeight` | CSmartPropAttributeFloat |  | `MPropertyDescription Relative weight of this choice, higher weighted choices are more likely to be selected.` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_MaterialGroupName&quot;: &quot;&quot;,
	&quot;m_flWeight&quot;: 1.000000
}</pre>
</details>
