---
layout: default
title: ragdoll_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / ragdoll_t

# ragdoll_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 80 bytes (`0x50`) · **Align:** 8 · **Module:** server

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `list` | CUtlVector< ragdollelement_t > |  |  |
| `0x18` | `hierarchyJoints` | CUtlVector< ragdollhierarchyjoint_t > |  |  |
| `0x30` | `boneIndex` | CUtlVector< int32 > |  |  |
| `0x48` | `allowStretch` | bool |  |  |
| `0x49` | `unused` | bool |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;list&quot;:
	[
	],
	&quot;hierarchyJoints&quot;:
	[
	],
	&quot;boneIndex&quot;:
	[
	],
	&quot;allowStretch&quot;: false,
	&quot;unused&quot;: false
}</pre>
</details>
