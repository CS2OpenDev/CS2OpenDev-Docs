---
title: sky3dparams_t (server)
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / sky3dparams_t

# sky3dparams_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 144 bytes (`0x90`) · **Align:** 8 · **Module:** server

**Twin:** [sky3dparams_t (client)](../client/sky3dparams_t.md)

## Memory layout

6 fields (6 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `scale` | int16 |  |  |
| `0xc` | `origin` | VectorWS |  |  |
| `0x18` | `bClip3DSkyBoxNearToWorldFar` | bool |  | `MNotSaved` |
| `0x1c` | `flClip3DSkyBoxNearToWorldFarOffset` | float32 |  | `MNotSaved` |
| `0x20` | `fog` | fogparams_t |  | `MNotSaved` |
| `0x88` | `m_nWorldGroupID` | WorldGroupId_t |  |  |

<details><summary>KV3 class defaults</summary>

<pre>null</pre>
</details>
