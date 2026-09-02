---
layout: default
title: CMotionDataSet
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CMotionDataSet

# CMotionDataSet

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 32 bytes (`0x20`) · **Align:** 8 · **Module:** animgraphlib

**Relationships:**

```mermaid
classDiagram
    CMotionDataSet *-- CMotionGraphGroup
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_groups` | CUtlVector< [CMotionGraphGroup](../animgraphlib/CMotionGraphGroup.md) > |  |  |
| `0x18` | `m_nDimensionCount` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_groups&quot;:
	[
	],
	&quot;m_nDimensionCount&quot;: 0
}</pre>
</details>
