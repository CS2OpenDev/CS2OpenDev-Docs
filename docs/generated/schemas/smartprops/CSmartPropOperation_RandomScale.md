---
title: CSmartPropOperation_RandomScale
module: smartprops
kind: class
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / CSmartPropOperation_RandomScale

# CSmartPropOperation_RandomScale

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 272 bytes (`0x110`) · **Align:** 8 · **Module:** smartprops

**Inherits from:** [CSmartPropTransformOperation](../smartprops/CSmartPropTransformOperation.md)

**Metadata:** `MPropertyDescription Apply a random scale to the current transform.`, `MPropertyFriendlyName Transform: Random Scale`, `MVDataClassGroup Transform`

**Relationships:**

```mermaid
classDiagram
    CSmartPropTransformOperation <|-- CSmartPropOperation_RandomScale
    CSmartPropOperation <|-- CSmartPropTransformOperation
    CSmartPropModifier <|-- CSmartPropOperation
```

## Memory layout

4 fields (3 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_bEnabled` | CSmartPropAttributeBool | [CSmartPropModifier](../smartprops/CSmartPropModifier.md) | `MVDataEnableKey` |
| `0x50` | `m_flRandomScaleMin` | CSmartPropAttributeFloat |  | `MPropertyDescription Minimum scale range` |
| `0x90` | `m_flRandomScaleMax` | CSmartPropAttributeFloat |  | `MPropertyDescription Maximum scale range` |
| `0xd0` | `m_flSnapIncrement` | CSmartPropAttributeFloat |  | `MPropertyDescription If non-zero, specifies the increment to which the randomly selected scale value will be snapped. Note that the snap value is absolute, not relative to the min or max, but if the min or max are not multiples of the snap value they can still be selected.` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CSmartPropOperation_RandomScale&quot;,
	&quot;m_bEnabled&quot;: true,
	&quot;m_flRandomScaleMin&quot;: 1.000000,
	&quot;m_flRandomScaleMax&quot;: 1.000000,
	&quot;m_flSnapIncrement&quot;: 0.000000
}</pre>
</details>
