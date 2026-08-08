---
layout: default
title: inv_image_map_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [client](../client.md) / inv_image_map_t

# inv_image_map_t

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** client

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `map_name` | CUtlString |  | `MPropertyFriendlyName Map` `MPropertyLeafChoiceProviderFn` |
| `0x8` | `map_rotation` | float32 |  | `MCustomFGDMetadata { reset_to_default_icon = true }` `MPropertyAttributeRange -180 180` `MPropertyFriendlyName Rotation` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;map_name&quot;: &quot;ui/icon_generation_basic_nuke_bombsitea&quot;,
	&quot;map_rotation&quot;: 0.000000
}</pre>
</details>
