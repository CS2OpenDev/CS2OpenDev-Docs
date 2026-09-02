---
layout: default
title: ModelAnimGraph2Ref_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [modellib](../modellib.md) / ModelAnimGraph2Ref_t

# ModelAnimGraph2Ref_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** modellib

**Relationships:**

```mermaid
classDiagram
    ModelAnimGraph2Ref_t *-- InfoForResourceTypeCNmGraphDefinition
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_sIdentifier` | CUtlString |  |  |
| `0x8` | `m_hGraph` | CStrongHandle< [InfoForResourceTypeCNmGraphDefinition](../resourcesystem/InfoForResourceTypeCNmGraphDefinition.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_sIdentifier&quot;: &quot;&quot;,
	&quot;m_hGraph&quot;: &quot;&quot;
}</pre>
</details>
