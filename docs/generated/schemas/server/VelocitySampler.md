---
title: VelocitySampler
module: server
kind: class
---

[Schemas](../../schemas.md) / [server](../server.md) / VelocitySampler

# VelocitySampler

> Source: **Build 26281801** · 2026-10-28 · `windows-x86_64` · schema `0.13.0`

**Kind:** class · **Size:** 20 bytes (`0x14`) · **Align:** n/a (unspecified) · **Module:** server

**Relationships:**

```mermaid
classDiagram
    VelocitySampler *-- GameTime_t
```

## Memory layout

3 fields (3 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_prevSample` | Vector |  |  |
| `0xc` | `m_fPrevSampleTime` | [GameTime_t](../entity2/GameTime_t.md) |  |  |
| `0x10` | `m_fIdealSampleRate` | float32 |  |  |
