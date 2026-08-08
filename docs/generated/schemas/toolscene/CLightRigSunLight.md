---
layout: default
title: CLightRigSunLight
nav_exclude: true
---

[Schemas](../../schemas.md) / [toolscene](../toolscene.md) / CLightRigSunLight

# CLightRigSunLight

**Kind:** class · **Size:** 84 bytes (`0x54`) · **Align:** 4 · **Module:** toolscene

**Inherits from:** [CLightRigLight](../toolscene/CLightRigLight.md)

**Relationships:**

```mermaid
classDiagram
    CLightRigLight <|-- CLightRigSunLight
```

## Memory layout

16 fields (5 declared here, 11 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_vPosition` | Vector | [CLightRigLight](../toolscene/CLightRigLight.md) |  |
| `0xc` | `m_vDirection` | Vector | [CLightRigLight](../toolscene/CLightRigLight.md) |  |
| `0x18` | `m_vLookAt` | Vector | [CLightRigLight](../toolscene/CLightRigLight.md) |  |
| `0x24` | `m_Color` | Color | [CLightRigLight](../toolscene/CLightRigLight.md) |  |
| `0x28` | `m_flAxisScale` | float32 | [CLightRigLight](../toolscene/CLightRigLight.md) |  |
| `0x2c` | `m_flRadius` | float32 | [CLightRigLight](../toolscene/CLightRigLight.md) |  |
| `0x30` | `m_flBrightness` | float32 | [CLightRigLight](../toolscene/CLightRigLight.md) |  |
| `0x34` | `m_flLightSourceRadius` | float32 | [CLightRigLight](../toolscene/CLightRigLight.md) |  |
| `0x38` | `m_flDistance` | float32 | [CLightRigLight](../toolscene/CLightRigLight.md) |  |
| `0x3c` | `m_bRelativePositioning` | bool | [CLightRigLight](../toolscene/CLightRigLight.md) |  |
| `0x3d` | `m_bParentToCamera` | bool | [CLightRigLight](../toolscene/CLightRigLight.md) |  |
| `0x40` | `m_flShadowCascadeDistance0` | float32 |  |  |
| `0x44` | `m_flShadowCascadeDistance1` | float32 |  |  |
| `0x48` | `m_flShadowCascadeDistance2` | float32 |  |  |
| `0x4c` | `m_flShadowCascadeDistance3` | float32 |  |  |
| `0x50` | `m_bCastShadows` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_vPosition&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vDirection&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_vLookAt&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_Color&quot;:
	[
		255,
		255,
		255
	],
	&quot;m_flAxisScale&quot;: 1.000000,
	&quot;m_flRadius&quot;: 10000.000000,
	&quot;m_flBrightness&quot;: 1.000000,
	&quot;m_flLightSourceRadius&quot;: 0.000000,
	&quot;m_flDistance&quot;: 1.500000,
	&quot;m_bRelativePositioning&quot;: false,
	&quot;m_bParentToCamera&quot;: false,
	&quot;m_flShadowCascadeDistance0&quot;: 0.000000,
	&quot;m_flShadowCascadeDistance1&quot;: 0.000000,
	&quot;m_flShadowCascadeDistance2&quot;: 0.000000,
	&quot;m_flShadowCascadeDistance3&quot;: 0.000000,
	&quot;m_bCastShadows&quot;: false
}</pre>
</details>
