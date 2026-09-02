---
layout: default
title: Relationship_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / Relationship_t

# Relationship_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 8 bytes (`0x8`) · **Align:** 4 · **Module:** server

**Derived by:** [RelationshipOverride_t](../server/RelationshipOverride_t.md)

**Relationships:**

```mermaid
classDiagram
    Relationship_t <|-- RelationshipOverride_t
    Relationship_t *-- Disposition_t
```

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `disposition` | [Disposition_t](../server/Disposition_t.md) |  |  |
| `0x4` | `priority` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;disposition&quot;: &quot;D_NU&quot;,
	&quot;priority&quot;: 0
}</pre>
</details>
