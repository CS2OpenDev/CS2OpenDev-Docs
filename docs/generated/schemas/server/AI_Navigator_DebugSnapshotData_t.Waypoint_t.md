---
layout: default
title: "AI_Navigator_DebugSnapshotData_t::Waypoint_t"
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / AI_Navigator_DebugSnapshotData_t::Waypoint_t

# AI_Navigator_DebugSnapshotData_t::Waypoint_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 4 · **Module:** server

## Memory layout

4 fields (4 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `position` | VectorWS |  |  |
| `0xc` | `nav_type` | uint32 |  |  |
| `0x10` | `flags` | uint32 |  |  |
| `0x14` | `is_pathcorner` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;position&quot;: null,
	&quot;nav_type&quot;: 0,
	&quot;flags&quot;: 0,
	&quot;is_pathcorner&quot;: false
}</pre>
</details>
