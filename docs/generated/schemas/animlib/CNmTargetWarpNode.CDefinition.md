---
layout: default
title: "CNmTargetWarpNode::CDefinition"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmTargetWarpNode::CDefinition

# CNmTargetWarpNode::CDefinition

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 8 · **Module:** animlib

**Inherits from:** [CNmPoseNode::CDefinition](../animlib/CNmPoseNode.CDefinition.md)

**Relationships:**

```mermaid
classDiagram
    "CNmPoseNode::CDefinition" <|-- "CNmTargetWarpNode::CDefinition"
    "CNmGraphNode::CDefinition" <|-- "CNmPoseNode::CDefinition"
    "CNmTargetWarpNode::CDefinition" *-- CNmRootMotionData
```

## Memory layout

12 fields (11 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_nNodeIdx` | int16 | [CNmGraphNode::CDefinition](../animlib/CNmGraphNode.CDefinition.md) |  |
| `0x10` | `m_nClipReferenceNodeIdx` | int16 |  |  |
| `0x12` | `m_nTargetValueNodeIdx` | int16 |  |  |
| `0x14` | `m_samplingMode` | [CNmRootMotionData](../animlib/CNmRootMotionData.md)::SamplingMode_t |  |  |
| `0x15` | `m_targetUpdateRule` | CNmTargetWarpNode::TargetUpdateRule_t |  |  |
| `0x16` | `m_bAlignWithTargetAtLastWarpEvent` | bool |  |  |
| `0x18` | `m_flSamplingPositionErrorThresholdSq` | float32 |  |  |
| `0x1c` | `m_flMaxTangentLength` | float32 |  |  |
| `0x20` | `m_flLerpFallbackDistanceThreshold` | float32 |  |  |
| `0x24` | `m_flTargetUpdateDistanceThreshold` | float32 |  |  |
| `0x28` | `m_flTargetUpdateAngleThresholdRadians` | float32 |  |  |
| `0x30` | `m_alignmentBoneID` | CGlobalSymbol |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNmTargetWarpNode::CDefinition&quot;,
	&quot;m_nNodeIdx&quot;: -1,
	&quot;m_nClipReferenceNodeIdx&quot;: -1,
	&quot;m_nTargetValueNodeIdx&quot;: -1,
	&quot;m_samplingMode&quot;: &quot;Delta&quot;,
	&quot;m_targetUpdateRule&quot;: &quot;None&quot;,
	&quot;m_bAlignWithTargetAtLastWarpEvent&quot;: false,
	&quot;m_flSamplingPositionErrorThresholdSq&quot;: 0.000000,
	&quot;m_flMaxTangentLength&quot;: 1.250000,
	&quot;m_flLerpFallbackDistanceThreshold&quot;: 0.100000,
	&quot;m_flTargetUpdateDistanceThreshold&quot;: 0.100000,
	&quot;m_flTargetUpdateAngleThresholdRadians&quot;: 0.087266,
	&quot;m_alignmentBoneID&quot;: &quot;&quot;
}</pre>
</details>
