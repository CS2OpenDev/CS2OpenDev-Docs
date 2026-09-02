---
layout: default
title: SelectedEditItemInfo_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [soundsystem](../soundsystem.md) / SelectedEditItemInfo_t

# SelectedEditItemInfo_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** soundsystem

**Relationships:**

```mermaid
classDiagram
    SelectedEditItemInfo_t *-- SosEditItemInfo_t
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_EditItems` | CUtlVector< [SosEditItemInfo_t](../soundsystem/SosEditItemInfo_t.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_EditItems&quot;:
	[
	]
}</pre>
</details>
