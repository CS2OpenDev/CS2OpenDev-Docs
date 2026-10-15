---
title: inv_image_camera_t
module: client
kind: class
---

[Schemas](../../schemas.md) / [client](../client.md) / inv_image_camera_t

# inv_image_camera_t

> Source: **Build 25947352** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 4 · **Module:** client

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `angle` | QAngle |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Angle` |
| `0xc` | `fov_h` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 360` `MPropertyFriendlyName Horizontal FOV` |
| `0x10` | `fov_v` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 360` `MPropertyFriendlyName Vertical FOV` |
| `0x14` | `znear` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 1000` `MPropertyFriendlyName Z Near` |
| `0x18` | `zfar` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 1000` `MPropertyFriendlyName Z Far` |
| `0x1c` | `target` | Vector |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Target` |
| `0x28` | `target_nudge` | Vector |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Target Nudge` |
| `0x34` | `orbit_distance` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 1000` `MPropertyFriendlyName Orbit Distance` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;angle&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;fov_h&quot;: 0.000000,
	&quot;fov_v&quot;: 45.000000,
	&quot;znear&quot;: 4.000000,
	&quot;zfar&quot;: 1000.000000,
	&quot;target&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;target_nudge&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;orbit_distance&quot;: 0.000000
}</pre>
</details>
