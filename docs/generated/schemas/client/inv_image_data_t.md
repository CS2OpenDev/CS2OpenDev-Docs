---
layout: default
title: inv_image_data_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / inv_image_data_t

# inv_image_data_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 232 bytes (`0xe8`) · **Align:** 8 · **Module:** client

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `map` | inv_image_map_t |  | `MPropertyAutoExpandSelf` `MPropertyFriendlyName Map` |
| `0x10` | `item` | inv_image_item_t |  | `MPropertyAutoExpandSelf` `MPropertyFriendlyName Item` |
| `0x30` | `camera` | inv_image_camera_t |  | `MPropertyAutoExpandSelf` `MPropertyFriendlyName Camera` |
| `0x64` | `lightsun` | inv_image_light_sun_t |  | `MPropertyAutoExpandSelf` `MPropertyDescription Shadowed.` `MPropertyFriendlyName Sun light` |
| `0x80` | `lightfill` | inv_image_light_fill_t |  | `MPropertyAutoExpandSelf` `MPropertyDescription No Shadows.` `MPropertyFriendlyName Fill light` |
| `0x9c` | `light0` | inv_image_light_barn_t |  | `MPropertyAutoExpandSelf` `MPropertyDescription Shadowed.` `MPropertyFriendlyName Barn light 0` |
| `0xbc` | `light1` | inv_image_light_barn_t |  | `MPropertyAutoExpandSelf` `MPropertyDescription Shadowed.` `MPropertyFriendlyName Barn light 1` |
| `0xdc` | `clearcolor` | inv_image_clearcolor_t |  | `MPropertyAutoExpandSelf` `MPropertyDescription` `MPropertyFriendlyName Clear Color` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;map&quot;:
	{
		&quot;map_name&quot;: &quot;ui/icon_generation_basic_nuke_bombsitea&quot;,
		&quot;map_rotation&quot;: 0.000000
	},
	&quot;item&quot;:
	{
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
	},
	&quot;camera&quot;:
	{
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
	},
	&quot;lightsun&quot;:
	{
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
	},
	&quot;lightfill&quot;:
	{
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
	},
	&quot;light0&quot;:
	{
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
	},
	&quot;light1&quot;:
	{
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
	},
	&quot;clearcolor&quot;:
	{
		&quot;color&quot;:
		[
			0.200000,
			0.200000,
			0.200000
		]
	}
}</pre>
</details>
