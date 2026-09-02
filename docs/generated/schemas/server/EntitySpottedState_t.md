---
title: EntitySpottedState_t (server)
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / EntitySpottedState_t

# EntitySpottedState_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 24 bytes (`0x18`) · **Align:** n/a (unspecified) · **Module:** server

**Twin:** [EntitySpottedState_t (client)](../client/EntitySpottedState_t.md)

## Memory layout

2 fields (2 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x8` | `m_bSpotted` | bool |  |  |
| `0xc` | `m_bSpottedByMask` | uint32[2] |  |  |
