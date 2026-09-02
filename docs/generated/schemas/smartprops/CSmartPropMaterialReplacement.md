---
layout: default
title: CSmartPropMaterialReplacement
nav_exclude: true
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / CSmartPropMaterialReplacement

# CSmartPropMaterialReplacement

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 128 bytes (`0x80`) · **Align:** 8 · **Module:** smartprops

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_OriginalMaterial` | CSmartPropAttributeMaterialName |  | `MPropertyAttributeEditor SmartPropAttributeEditor(MaterialInSmartProp)` `MPropertyDescription Original material to replace. This is the material specified in the model, including any material group asignment within the model. Does not consider any existing material overrides specified within the smart prop.` `MPropertyFriendlyName Original Material` |
| `0x40` | `m_ReplacementMaterial` | CSmartPropAttributeMaterialName |  | `MPropertyDescription New material to replace the original material with.` `MPropertyFriendlyName New Material` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_OriginalMaterial&quot;: &quot;&quot;,
	&quot;m_ReplacementMaterial&quot;: &quot;&quot;
}</pre>
</details>
