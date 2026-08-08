---
layout: default
title: inv_image_light_sun_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / inv_image_light_sun_t

# inv_image_light_sun_t

**Kind:** class · **Size:** 28 bytes (`0x1c`) · **Align:** 4 · **Module:** client

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `color` | Vector |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeEditor VectorColor()` `MPropertyFriendlyName Color` |
| `0xc` | `angle` | QAngle |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Angle` |
| `0x18` | `brightness` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 10` `MPropertyFriendlyName Brightness` |

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
	&quot;brightness&quot;: 1.000000
}</pre>
</details>
