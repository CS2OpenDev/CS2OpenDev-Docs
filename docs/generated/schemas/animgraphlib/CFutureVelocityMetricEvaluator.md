---
layout: default
title: CFutureVelocityMetricEvaluator
nav_exclude: true
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CFutureVelocityMetricEvaluator

# CFutureVelocityMetricEvaluator

**Kind:** class · **Size:** 96 bytes (`0x60`) · **Align:** 8 · **Module:** animgraphlib

**Inherits from:** [CMotionMetricEvaluator](../animgraphlib/CMotionMetricEvaluator.md)

**Relationships:**

```mermaid
classDiagram
    CMotionMetricEvaluator <|-- CFutureVelocityMetricEvaluator
    CFutureVelocityMetricEvaluator *-- VelocityMetricMode
```

## Memory layout

8 fields (4 declared here, 4 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x18` | `m_means` | CUtlVector< float32 > | [CMotionMetricEvaluator](../animgraphlib/CMotionMetricEvaluator.md) |  |
| `0x30` | `m_standardDeviations` | CUtlVector< float32 > | [CMotionMetricEvaluator](../animgraphlib/CMotionMetricEvaluator.md) |  |
| `0x48` | `m_flWeight` | float32 | [CMotionMetricEvaluator](../animgraphlib/CMotionMetricEvaluator.md) |  |
| `0x4c` | `m_nDimensionStartIndex` | int32 | [CMotionMetricEvaluator](../animgraphlib/CMotionMetricEvaluator.md) |  |
| `0x50` | `m_flDistance` | float32 |  |  |
| `0x54` | `m_flStoppingDistance` | float32 |  |  |
| `0x58` | `m_flTargetSpeed` | float32 |  |  |
| `0x5c` | `m_eMode` | [VelocityMetricMode](../!GlobalTypes/VelocityMetricMode.md) |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CFutureVelocityMetricEvaluator&quot;,
	&quot;m_means&quot;:
	[
	],
	&quot;m_standardDeviations&quot;:
	[
	],
	&quot;m_flWeight&quot;: 0.000000,
	&quot;m_nDimensionStartIndex&quot;: -1,
	&quot;m_flDistance&quot;: 0.000000,
	&quot;m_flStoppingDistance&quot;: 0.000000,
	&quot;m_flTargetSpeed&quot;: 0.000000,
	&quot;m_eMode&quot;: &quot;DirectionOnly&quot;
}</pre>
</details>
