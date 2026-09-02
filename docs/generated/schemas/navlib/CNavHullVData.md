---
layout: default
title: CNavHullVData
nav_exclude: true
---

[Schemas](../../schemas.md) / [navlib](../navlib.md) / CNavHullVData

# CNavHullVData

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 60 bytes (`0x3c`) · **Align:** 4 · **Module:** navlib

**Metadata:** `MVDataRoot`

## Memory layout

15 fields (15 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_bAgentEnabled` | bool |  | `MPropertyDescription Is this agent enabled for generation? ( will result in 0 nav areas for this agent if not ).` `MPropertyFriendlyName Enabled` |
| `0x4` | `m_agentRadius` | float32 |  | `MPropertyDescription Radius of navigating agent capsule.` `MPropertyFriendlyName Radius` |
| `0x8` | `m_agentHeight` | float32 |  | `MPropertyDescription Height of navigating agent capsule.` `MPropertyFriendlyName Height` |
| `0xc` | `m_agentShortHeightEnabled` | bool |  | `MPropertyDescription Enable shorter navigating agent capsules ( crouch ) in addition to regular height capsules.` `MPropertyFriendlyName Enable Crouch Height` |
| `0x10` | `m_agentShortHeight` | float32 |  | `MPropertyDescription Crouch height of navigating agent capsules if enabled.` `MPropertyFriendlyName Crouch height` |
| `0x14` | `m_agentCrawlEnabled` | bool |  | `MPropertyDescription Enable even shorter navigating agent capsules ( crawl ) in addition to regular height capsules.` `MPropertyFriendlyName Enable Crawl Height` |
| `0x18` | `m_agentCrawlHeight` | float32 |  | `MPropertyDescription Crawl height of navigating agent capsules if enabled.` `MPropertyFriendlyName Crawl height` |
| `0x1c` | `m_agentMaxClimb` | float32 |  | `MPropertyDescription Max vertical offset that the agent simply ignores and walks over.` `MPropertyFriendlyName Max Climb` |
| `0x20` | `m_agentMaxSlope` | int32 |  | `MPropertyDescription Max ground slope to be considered walkable.` `MPropertyFriendlyName Max Slope` |
| `0x24` | `m_agentMaxJumpDownDist` | float32 |  | `MPropertyDescription Max vertical offset at which to create a jump connection ( possibly one-way ).` `MPropertyFriendlyName Max Jump Down Distance` |
| `0x28` | `m_agentMaxJumpHorizDistBase` | float32 |  | `MPropertyDescription Max horizontal offset over which to create a jump connection ( actually a parameter into the true threshold function ).` `MPropertyFriendlyName Max Horizontal Jump Distance` |
| `0x2c` | `m_agentMaxJumpUpDist` | float32 |  | `MPropertyDescription Max vertical offset at which to make a jump connection two-way.` `MPropertyFriendlyName Max Jump Up Distance` |
| `0x30` | `m_agentBorderErosion` | int32 |  | `MPropertyDescription Border erosion in voxel units ( -1 to use default value based on agent radius ).` `MPropertyFriendlyName Border Erosion` |
| `0x34` | `m_flowMapGenerationEnabled` | bool |  | `MPropertyDescription Enables super node nav information to be generated` `MPropertyFriendlyName Hierarchical Nav` |
| `0x38` | `m_flowMapNodeMaxRadius` | float32 |  | `MPropertyDescription Maximum radius of a super node - larger means lower resolution` `MPropertyFriendlyName Hierarchical Nav Max Super Node radius` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_bAgentEnabled&quot;: true,
	&quot;m_agentRadius&quot;: 15.000000,
	&quot;m_agentHeight&quot;: 71.000000,
	&quot;m_agentShortHeightEnabled&quot;: false,
	&quot;m_agentShortHeight&quot;: 35.500000,
	&quot;m_agentCrawlEnabled&quot;: false,
	&quot;m_agentCrawlHeight&quot;: 17.500000,
	&quot;m_agentMaxClimb&quot;: 17.500000,
	&quot;m_agentMaxSlope&quot;: 50,
	&quot;m_agentMaxJumpDownDist&quot;: 240.000000,
	&quot;m_agentMaxJumpHorizDistBase&quot;: 64.000000,
	&quot;m_agentMaxJumpUpDist&quot;: 0.000000,
	&quot;m_agentBorderErosion&quot;: -1,
	&quot;m_flowMapGenerationEnabled&quot;: false,
	&quot;m_flowMapNodeMaxRadius&quot;: 400.000000
}</pre>
</details>
