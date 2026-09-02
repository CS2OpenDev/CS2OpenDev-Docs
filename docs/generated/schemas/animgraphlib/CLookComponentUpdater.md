---
title: CLookComponentUpdater
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CLookComponentUpdater

# CLookComponentUpdater

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** animgraphlib

**Inherits from:** [CAnimComponentUpdater](../animgraphlib/CAnimComponentUpdater.md)

**Relationships:**

```mermaid
classDiagram
    CAnimComponentUpdater <|-- CLookComponentUpdater
    CLookComponentUpdater *-- CAnimParamHandle
```

## Memory layout

13 fields (9 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_name` | CUtlString | [CAnimComponentUpdater](../animgraphlib/CAnimComponentUpdater.md) |  |
| `0x20` | `m_id` | [AnimComponentID](../modellib/AnimComponentID.md) | [CAnimComponentUpdater](../animgraphlib/CAnimComponentUpdater.md) |  |
| `0x24` | `m_networkMode` | [AnimNodeNetworkMode](../animgraphlib/AnimNodeNetworkMode.md) | [CAnimComponentUpdater](../animgraphlib/CAnimComponentUpdater.md) |  |
| `0x28` | `m_bStartEnabled` | bool | [CAnimComponentUpdater](../animgraphlib/CAnimComponentUpdater.md) |  |
| `0x34` | `m_hLookHeading` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x36` | `m_hLookHeadingNormalized` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x38` | `m_hLookHeadingVelocity` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x3a` | `m_hLookPitch` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x3c` | `m_hLookDistance` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x3e` | `m_hLookDirection` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x40` | `m_hLookTarget` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x42` | `m_hLookTargetWorldSpace` | [CAnimParamHandle](../animgraphlib/CAnimParamHandle.md) |  |  |
| `0x44` | `m_bNetworkLookTarget` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CLookComponentUpdater&quot;,
	&quot;m_name&quot;: &quot;&quot;,
	&quot;m_id&quot;:
	{
		&quot;m_id&quot;: &lt;HIDDEN FOR DIFF&gt;,
	},
	&quot;m_networkMode&quot;: &quot;ServerAuthoritative&quot;,
	&quot;m_bStartEnabled&quot;: false,
	&quot;m_hLookHeading&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hLookHeadingNormalized&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hLookHeadingVelocity&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hLookPitch&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hLookDistance&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hLookDirection&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hLookTarget&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_hLookTargetWorldSpace&quot;:
	{
		&quot;m_type&quot;: &quot;ANIMPARAM_UNKNOWN&quot;,
		&quot;m_index&quot;: 255
	},
	&quot;m_bNetworkLookTarget&quot;: true
}</pre>
</details>
