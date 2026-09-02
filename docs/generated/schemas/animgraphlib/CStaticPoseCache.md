---
title: CStaticPoseCache
module: animgraphlib
kind: class
---

[Schemas](../../schemas.md) / [animgraphlib](../animgraphlib.md) / CStaticPoseCache

# CStaticPoseCache

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 48 bytes (`0x30`) · **Align:** 8 · **Module:** animgraphlib

**Derived by:** [CStaticPoseCacheBuilder](../animgraphlib/CStaticPoseCacheBuilder.md)

**Relationships:**

```mermaid
classDiagram
    CStaticPoseCache <|-- CStaticPoseCacheBuilder
    CStaticPoseCache *-- CCachedPose
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x10` | `m_poses` | CUtlVector< [CCachedPose](../animgraphlib/CCachedPose.md) > |  |  |
| `0x28` | `m_nBoneCount` | int32 |  |  |
| `0x2c` | `m_nMorphCount` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;_class&quot;: &quot;CStaticPoseCache&quot;,
	&quot;m_poses&quot;:
	[
	],
	&quot;m_nBoneCount&quot;: 0,
	&quot;m_nMorphCount&quot;: 0
}</pre>
</details>
