---
title: CNavPathCost
module: navlib
kind: class
---

[Schemas](../../schemas.md) / [navlib](../navlib.md) / CNavPathCost

# CNavPathCost

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** navlib

**Inherits from:** [INavPathCost](../navlib/INavPathCost.md)

**Derived by:** [ApproachAreaCost](../server/ApproachAreaCost.md), [CNavPathCostForTests](../server/CNavPathCostForTests.md), [ChickenPathCost](../server/ChickenPathCost.md), [HostagePathCost](../server/HostagePathCost.md), [PathCost](../server/PathCost.md)

**Relationships:**

```mermaid
classDiagram
    INavPathCost <|-- CNavPathCost
    CNavPathCost <|-- ApproachAreaCost
    CNavPathCost <|-- CNavPathCostForTests
    CNavPathCost <|-- ChickenPathCost
    CNavPathCost <|-- HostagePathCost
    CNavPathCost <|-- PathCost
```

## Memory layout

13 fields (12 declared here, 1 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_navHull` | [NavHull_t](../navlib/NavHull_t.md) | [INavPathCost](../navlib/INavPathCost.md) |  |
| `0x10` | `m_bAllowLadders` | bool |  |  |
| `0x11` | `m_bCanFly` | bool |  |  |
| `0x12` | `m_bCanSwim` | bool |  |  |
| `0x14` | `m_flWaterToGroundMaxHeight` | float32 |  |  |
| `0x18` | `m_flGroundToWaterMaxHeight` | float32 |  |  |
| `0x1c` | `m_flGroundToWaterTransitionDistance` | float32 |  |  |
| `0x20` | `m_flWaterToGroundTransitionDistance` | float32 |  |  |
| `0x24` | `m_flFlyingTransitionTolerance` | float32 |  |  |
| `0x28` | `m_bOptimizeFlySpacePathfinds` | bool |  |  |
| `0x29` | `m_bStringPullFlySpacePathfinds` | bool |  |  |
| `0x2a` | `m_bSupportsTransitions` | bool |  |  |
| `0x2c` | `m_flTransitionPenalty` | float32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CNavPathCost&quot;,
	&quot;m_navHull&quot;:
	{
		&quot;m_nHullIdx&quot;: 0
	},
	&quot;m_bAllowLadders&quot;: true,
	&quot;m_bCanFly&quot;: false,
	&quot;m_bCanSwim&quot;: false,
	&quot;m_flWaterToGroundMaxHeight&quot;: 100.000000,
	&quot;m_flGroundToWaterMaxHeight&quot;: 100.000000,
	&quot;m_flGroundToWaterTransitionDistance&quot;: -1.000000,
	&quot;m_flWaterToGroundTransitionDistance&quot;: -1.000000,
	&quot;m_flFlyingTransitionTolerance&quot;: 140.000000,
	&quot;m_bOptimizeFlySpacePathfinds&quot;: true,
	&quot;m_bStringPullFlySpacePathfinds&quot;: false,
	&quot;m_bSupportsTransitions&quot;: false,
	&quot;m_flTransitionPenalty&quot;: 200.000000
}</pre>
</details>
