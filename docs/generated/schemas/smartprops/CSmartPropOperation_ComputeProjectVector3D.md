---
title: CSmartPropOperation_ComputeProjectVector3D
module: smartprops
kind: class
---

[Schemas](../../schemas.md) / [smartprops](../smartprops.md) / CSmartPropOperation_ComputeProjectVector3D

# CSmartPropOperation_ComputeProjectVector3D

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 472 bytes (`0x1d8`) · **Align:** 8 · **Module:** smartprops

**Inherits from:** [CSmartPropOperation](../smartprops/CSmartPropOperation.md)

**Metadata:** `MPropertyDescription Project Vector A onto Vector B`, `MPropertyFriendlyName Project Vector`, `MVDataClassGroup Compute`

**Relationships:**

```mermaid
classDiagram
    CSmartPropOperation <|-- CSmartPropOperation_ComputeProjectVector3D
    CSmartPropModifier <|-- CSmartPropOperation
    CSmartPropOperation_ComputeProjectVector3D *-- CSmartPropAttributeCoordinateSpace
```

## Memory layout

8 fields (7 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_bEnabled` | CSmartPropAttributeBool | [CSmartPropModifier](../smartprops/CSmartPropModifier.md) | `MVDataEnableKey` |
| `0x50` | `m_OutputVariableName` | CUtlString |  | `MPropertyAttributeEditor SmartPropItemNameEditor( Variable:Vector3 )` `MPropertyFriendlyName Output Variable` |
| `0x58` | `m_OutputCoordinateSpace` | [CSmartPropAttributeCoordinateSpace](../smartprops/CSmartPropAttributeCoordinateSpace.md) |  | `MPropertyDescription Specifies the coordinate space that vector should be returned in.` |
| `0x98` | `m_InputVectorA` | CSmartPropAttributeVector |  | `MPropertyFriendlyName Vector A` `MPropertyGroupName +Vector A` |
| `0xd8` | `m_CoordinateSpaceA` | [CSmartPropAttributeCoordinateSpace](../smartprops/CSmartPropAttributeCoordinateSpace.md) |  | `MPropertyDescription Specifies the coordinate space of vector A.` `MPropertyGroupName +Vector A` |
| `0x118` | `m_InputVectorB` | CSmartPropAttributeVector |  | `MPropertyFriendlyName Vector B` `MPropertyGroupName +Vector B` |
| `0x158` | `m_CoordinateSpaceB` | [CSmartPropAttributeCoordinateSpace](../smartprops/CSmartPropAttributeCoordinateSpace.md) |  | `MPropertyDescription Specifies the coordinate space of posivectortion B.` `MPropertyGroupName +Vector B` |
| `0x198` | `m_bPlane` | CSmartPropAttributeBool |  | `MPropertyDescription Interpret Vector B as plane normal.` `MPropertyFriendlyName Projection to plane` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CSmartPropOperation_ComputeProjectVector3D&quot;,
	&quot;m_bEnabled&quot;: true,
	&quot;m_OutputVariableName&quot;: &quot;&quot;,
	&quot;m_OutputCoordinateSpace&quot;: &quot;WORLD&quot;,
	&quot;m_InputVectorA&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_CoordinateSpaceA&quot;: &quot;WORLD&quot;,
	&quot;m_InputVectorB&quot;:
	[
		0.000000,
		0.000000,
		0.000000
	],
	&quot;m_CoordinateSpaceB&quot;: &quot;WORLD&quot;,
	&quot;m_bPlane&quot;: false
}</pre>
</details>
