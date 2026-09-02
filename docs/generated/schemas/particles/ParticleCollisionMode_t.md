---
layout: default
title: ParticleCollisionMode_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [particles](../particles.md) / ParticleCollisionMode_t

# ParticleCollisionMode_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** particles

## Values

| Name | Value | Description |
|------|-------|-------------|
| `COLLISION_MODE_DISABLED` | -1 (`0xffffffff`) | Collision Disabled |
| `COLLISION_MODE_INITIAL_TRACE_DOWN` | 0 | Initial Trace Down |
| `COLLISION_MODE_PER_FRAME_PLANESET` | 1 | Per-Frame Planeset |
| `COLLISION_MODE_USE_NEAREST_TRACE` | 2 | Trace Caching |
| `COLLISION_MODE_PER_PARTICLE_TRACE` | 3 | Per-Particle Trace |
