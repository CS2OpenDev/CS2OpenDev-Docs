---
layout: default
title: inv_image_item_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / inv_image_item_t

# inv_image_item_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** client

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `position` | Vector |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Position` |
| `0xc` | `angle` | QAngle |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Angle` |
| `0x18` | `pose_sequence` | CUtlString |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Pose Sequence` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;position&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;angle&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;pose_sequence&quot;: &quot;&quot;
}</pre>
</details>
