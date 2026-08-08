---
layout: default
title: "CNmSkeleton::SecondarySkeleton_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [animlib](../animlib.md) / CNmSkeleton::SecondarySkeleton_t

# CNmSkeleton::SecondarySkeleton_t

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** animlib

**Relationships:**

```mermaid
classDiagram
    "CNmSkeleton::SecondarySkeleton_t" *-- InfoForResourceTypeCNmSkeleton
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_attachToBoneID` | CGlobalSymbol |  |  |
| `0x8` | `m_skeleton` | CStrongHandle< [InfoForResourceTypeCNmSkeleton](../resourcesystem/InfoForResourceTypeCNmSkeleton.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_attachToBoneID&quot;: &quot;&quot;,
	&quot;m_skeleton&quot;: &quot;&quot;
}</pre>
</details>
