---
layout: default
title: inv_image_camera_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / inv_image_camera_t

# inv_image_camera_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 52 bytes (`0x34`) · **Align:** 4 · **Module:** client

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `angle` | QAngle |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Angle` |
| `0xc` | `fov` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 360` `MPropertyFriendlyName FOV` |
| `0x10` | `znear` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 1000` `MPropertyFriendlyName Z Near` |
| `0x14` | `zfar` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 1000` `MPropertyFriendlyName Z Far` |
| `0x18` | `target` | Vector |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Target` |
| `0x24` | `target_nudge` | Vector |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyFriendlyName Target Nudge` |
| `0x30` | `orbit_distance` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange 0 1000` `MPropertyFriendlyName Orbit Distance` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;angle&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;fov&quot;: 45.000000,
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
