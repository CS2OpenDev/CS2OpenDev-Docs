---
layout: default
title: CAnimGraphDoc_FootCycleMetric
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphdoclib](../animgraphdoclib.md) / CAnimGraphDoc_FootCycleMetric

# CAnimGraphDoc_FootCycleMetric

**Kind:** class · **Size:** 64 bytes (`0x40`) · **Align:** 8 · **Module:** animgraphdoclib

**Inherits from:** [CAnimGraphDoc_MotionMetric](../animgraphdoclib/CAnimGraphDoc_MotionMetric.md)

**Metadata:** `MPropertyFriendlyName Foot Cycle Metric`

**Relationships:**

```mermaid
classDiagram
    CAnimGraphDoc_MotionMetric <|-- CAnimGraphDoc_FootCycleMetric
```

## Memory layout

2 fields (1 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x20` | `m_flWeight` | float32 | [CAnimGraphDoc_MotionMetric](../animgraphdoclib/CAnimGraphDoc_MotionMetric.md) | `MPropertySuppressField` |
| `0x28` | `m_feet` | CUtlVector< CUtlString > |  | `MPropertyAttributeChoiceName Foot` `MPropertyAutoExpandSelf` `MPropertyFriendlyName Foot` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CAnimGraphDoc_FootCycleMetric&quot;,
	&quot;m_flWeight&quot;: 1.000000,
	&quot;m_feet&quot;:
	[
	]
}</pre>
</details>
