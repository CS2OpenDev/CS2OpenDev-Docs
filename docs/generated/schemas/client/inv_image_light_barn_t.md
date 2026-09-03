---
title: inv_image_light_barn_t
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / inv_image_light_barn_t

# inv_image_light_barn_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 4 · **Module:** client

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `color` | Vector |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeEditor VectorColor()` `MPropertyFriendlyName Color` |
| `0xc` | `angle` | QAngle |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Angle` |
| `0x18` | `brightness` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 10` `MPropertyFriendlyName Brightness` |
| `0x1c` | `orbit_distance` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 1000` `MPropertyFriendlyName Orbit Distance` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;color&quot;:
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
	&quot;brightness&quot;: 0.000000,
	&quot;orbit_distance&quot;: 1.000000
}</pre>
</details>
