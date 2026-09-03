---
title: RagdollCreationParams_t
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / RagdollCreationParams_t

# RagdollCreationParams_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** 4 · **Module:** server

## Memory layout

5 fields (5 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_vForce` | Vector |  | `MNotSaved` |
| `0xc` | `m_nForceBone` | int32 |  | `MNotSaved` |
| `0x10` | `m_bForceCurrentWorldTransform` | bool |  |  |
| `0x11` | `m_bUseLRURetirement` | bool |  |  |
| `0x14` | `m_nHealthToGrant` | int32 |  |  |

<details><summary>KV3 class defaults</summary>

<pre>{
	&quot;m_bForceCurrentWorldTransform&quot;: false,
	&quot;m_bUseLRURetirement&quot;: true,
	&quot;m_nHealthToGrant&quot;: 0
}</pre>
</details>
