---
title: ColorChoice_t
module: smartprops
kind: class
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / ColorChoice_t

# ColorChoice_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 128 bytes (`0x80`) · **Align:** 8 · **Module:** smartprops

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_Color` | CSmartPropAttributeColor |  | `MPropertyDescription Color to be applied if this choice is selected.` |
| `0x40` | `m_flWeight` | CSmartPropAttributeFloat |  | `MPropertyDescription Relative weight of this choice, higher weighted choices are more likely to be selected.` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_Color&quot;:
	[
		255,
		255,
		255
	],
	&quot;m_flWeight&quot;: 1.000000
}</pre>
</details>
