---
title: CFootPinningItem
module: animgraphdoclib
kind: class
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CFootPinningItem

# CFootPinningItem

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** animgraphdoclib

**Metadata:** `MPropertyElementNameFn`, `MPropertyFriendlyName Item`

**Relationships:**

```mermaid
classDiagram
    CFootPinningItem *-- AnimTagID
    CFootPinningItem *-- AnimParamID
```

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_footName` | CUtlString |  | `MPropertyAttributeChoiceName Foot` `MPropertyFriendlyName Foot` |
| `0x8` | `m_targetBoneName` | CUtlString |  | `MPropertyAttributeChoiceName Bone` `MPropertyFriendlyName Target Bone` |
| `0x10` | `m_ikChainName` | CUtlString |  | `MPropertyAttributeChoiceName IKChain` `MPropertyFriendlyName IK Chain` |
| `0x18` | `m_tag` | [AnimTagID](../modellib/AnimTagID.md) |  | `MPropertyAttributeChoiceName Tag` `MPropertyFriendlyName Tag` |
| `0x20` | `m_paramName` | CUtlString |  | `MPropertySuppressField` |
| `0x28` | `m_param` | [AnimParamID](../modellib/AnimParamID.md) |  | `MPropertyAttributeChoiceName BoolParameter` `MPropertyFriendlyName Parameter` |
| `0x2c` | `m_flMaxRotationLeft` | float32 |  | `MPropertyAttributeRange 0 180` `MPropertyFriendlyName Max Left Rotation` |
| `0x30` | `m_flMaxRotationRight` | float32 |  | `MPropertyAttributeRange 0 180` `MPropertyFriendlyName Max Right Rotation` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_footName&quot;: &quot;&quot;,
	&quot;m_targetBoneName&quot;: &quot;&quot;,
	&quot;m_ikChainName&quot;: &quot;&quot;,
	&quot;m_tag&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_paramName&quot;: &quot;&quot;,
	&quot;m_param&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_flMaxRotationLeft&quot;: 90.000000,
	&quot;m_flMaxRotationRight&quot;: 90.000000
}</pre>
</details>
