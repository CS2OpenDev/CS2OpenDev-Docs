---
title: PathMoverEntitySpawn
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / PathMoverEntitySpawn

# PathMoverEntitySpawn

> Source: **Build 26281801** · 2026-10-28 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 40 bytes (`0x28`) · **Align:** 8 · **Module:** server

**Relationships:**

```mermaid
classDiagram
    PathMoverEntitySpawn --> CFuncMover
    PathMoverEntitySpawn --> CBaseEntity
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `hMover` | CHandle< [CFuncMover](../server/CFuncMover.md) > |  |  |
| `0x8` | `vecOtherEntities` | CUtlVector< CHandle< [CBaseEntity](../server/CBaseEntity.md) > > |  |  |
| `0x20` | `nSpawnNumber` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;hMover&quot;: null,
	&quot;vecOtherEntities&quot;:
	[
	],
	&quot;nSpawnNumber&quot;: -1
}</pre>
</details>
