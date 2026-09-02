---
title: ManifestTestResource_t
module: resourcesystem
kind: class
---

[Schemas](../../schemas.md) / [resourcesystem](../resourcesystem.md) / ManifestTestResource_t

# ManifestTestResource_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 16 bytes (`0x10`) · **Align:** 8 · **Module:** resourcesystem

**Relationships:**

```mermaid
classDiagram
    ManifestTestResource_t *-- InfoForResourceTypeManifestTestResource_t
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_name` | CUtlString |  | `MKV3TransferName name` |
| `0x8` | `m_child` | CStrongHandle< [InfoForResourceTypeManifestTestResource_t](../resourcesystem/InfoForResourceTypeManifestTestResource_t.md) > |  | `MKV3TransferName child` |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;name&quot;: &quot;&quot;,
	&quot;child&quot;: &quot;&quot;
}</pre>
</details>
