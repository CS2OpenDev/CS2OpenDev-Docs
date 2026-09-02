---
layout: default
title: AI_FacingServices_DebugSnapshotData_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / AI_FacingServices_DebugSnapshotData_t

# AI_FacingServices_DebugSnapshotData_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 72 bytes (`0x48`) · **Align:** 8 · **Module:** server

**Metadata:** `MDebugSnapshotDataRenderFn`, `MPropertyFriendlyName Facing Services`

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `npc_position` | VectorWS |  |  |
| `0x10` | `facing_target_source` | CGlobalSymbol |  |  |
| `0x18` | `facing_target` | VectorWS |  |  |
| `0x28` | `schedule_facing_priority` | CGlobalSymbol |  |  |
| `0x30` | `strafing_source` | CGlobalSymbol |  |  |
| `0x38` | `strafing_enabled` | bool |  |  |
| `0x40` | `movement_id` | CGlobalSymbol |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;npc_position&quot;: null,
	&quot;facing_target_source&quot;: &quot;&quot;,
	&quot;facing_target&quot;: null,
	&quot;schedule_facing_priority&quot;: &quot;&quot;,
	&quot;strafing_source&quot;: &quot;&quot;,
	&quot;strafing_enabled&quot;: false,
	&quot;movement_id&quot;: &quot;&quot;
}</pre>
</details>
