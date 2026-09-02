---
layout: default
title: CAttachment
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / CAttachment

# CAttachment

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 144 bytes (`0x90`) · **Align:** 16 · **Module:** modellib

## Memory layout

8 fields (8 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString |  |  |
| `0x8` | `m_influenceNames` | CUtlString[3] |  |  |
| `0x20` | `m_vInfluenceRotations` | Quaternion[3] |  |  |
| `0x50` | `m_vInfluenceOffsets` | Vector[3] |  |  |
| `0x74` | `m_influenceWeights` | float32[3] |  |  |
| `0x80` | `m_bInfluenceRootTransform` | bool[3] |  |  |
| `0x83` | `m_nInfluences` | uint8 |  |  |
| `0x84` | `m_bIgnoreRotation` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_influenceNames&quot;:
	[
		&quot;&quot;,
		&quot;&quot;,
		&quot;&quot;
	],
	&quot;m_vInfluenceRotations&quot;:
	[
		[
			0.000000,
			0.000000,
			0.000000,
			1.000000
		],
		[
			0.000000,
			0.000000,
			0.000000,
			1.000000
		],
		[
			0.000000,
			0.000000,
			0.000000,
			1.000000
		]
	],
	&quot;m_vInfluenceOffsets&quot;:
	[
		[
			0.000000,
			0.000000,
			0.000000
		],
		[
			0.000000,
			0.000000,
			0.000000
		],
		[
			0.000000,
			0.000000,
			0.000000
		]
	],
	&quot;m_influenceWeights&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_bInfluenceRootTransform&quot;:
	[
		false,
		false,
		false
	],
	&quot;m_nInfluences&quot;: 0,
	&quot;m_bIgnoreRotation&quot;: false
}</pre>
</details>
