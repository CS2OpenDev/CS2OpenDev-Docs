---
layout: default
title: AI_Navigator_DebugSnapshotData_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / AI_Navigator_DebugSnapshotData_t

# AI_Navigator_DebugSnapshotData_t

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 8 · **Module:** server

**Metadata:** `MDebugSnapshotDataRenderFn`, `MPropertyFriendlyName Navigator`

## Memory layout

7 fields (7 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `s_movement_id` | CGlobalSymbol |  |  |
| `0x8` | `s_movement_serial_number` | uint32 |  |  |
| `0x10` | `s_goal_source_location` | CUtlString |  |  |
| `0x18` | `last_waypoint_pos` | VectorWS |  |  |
| `0x24` | `goal_location` | VectorWS |  |  |
| `0x30` | `waypoints` | CUtlVector< [AI_Navigator_DebugSnapshotData_t](../server/AI_Navigator_DebugSnapshotData_t.md)::Waypoint_t > |  |  |
| `0x48` | `s_arrival_movement_gait_set` | CGlobalSymbol |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;s_movement_id&quot;: &quot;&quot;,
	&quot;s_movement_serial_number&quot;: 0,
	&quot;s_goal_source_location&quot;: &quot;&quot;,
	&quot;last_waypoint_pos&quot;: null,
	&quot;goal_location&quot;: null,
	&quot;waypoints&quot;:
	[
	],
	&quot;s_arrival_movement_gait_set&quot;: &quot;&quot;
}</pre>
</details>
