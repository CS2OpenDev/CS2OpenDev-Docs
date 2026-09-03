---
title: CModuleManifests
module: toolutils2
kind: class
---

[Schemas](../../schemas.md) / [toolutils2](../toolutils2.md) / CModuleManifests

# CModuleManifests

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** toolutils2

**Relationships:**

```mermaid
classDiagram
    CModuleManifests *-- CManifestInfo
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_Manifests` | CUtlVector< [CManifestInfo](../toolutils2/CManifestInfo.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_Manifests&quot;:
	[
	]
}</pre>
</details>
