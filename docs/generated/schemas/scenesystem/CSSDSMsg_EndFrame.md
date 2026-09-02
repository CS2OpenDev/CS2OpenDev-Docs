---
layout: default
title: CSSDSMsg_EndFrame
nav_exclude: true
---

[Schemas](../../schemas.md) / [scenesystem](../scenesystem.md) / CSSDSMsg_EndFrame

# CSSDSMsg_EndFrame

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 8 · **Module:** scenesystem

**Relationships:**

```mermaid
classDiagram
    CSSDSMsg_EndFrame *-- CSSDSEndFrameViewInfo
```

## Memory layout

1 field (1 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_Views` | CUtlVector< [CSSDSEndFrameViewInfo](../scenesystem/CSSDSEndFrameViewInfo.md) > |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_Views&quot;:
	[
	]
}</pre>
</details>
