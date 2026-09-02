---
layout: default
title: vphysics_save_ragdoll_control_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [vphysics2](../vphysics2.md) / vphysics_save_ragdoll_control_t

# vphysics_save_ragdoll_control_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** class · **Size:** 56 bytes (`0x38`) · **Align:** 4 · **Module:** vphysics2

## Memory layout

10 fields (10 declared here, 0 inherited). Offsets are absolute from the object base.

| Offset | Field | Type | From | Annotations |
|--------|-------|------|------|-------------|
| `0x0` | `m_flMinSpringFrequency` | float32 |  |  |
| `0x4` | `m_flMaxSpringFrequency` | float32 |  |  |
| `0x8` | `m_flMaxStretch` | float32 |  |  |
| `0xc` | `m_bSolidCollisionAtZeroWeight` | bool |  |  |
| `0xd` | `m_bRequiresDynamicBodies` | bool |  |  |
| `0xe` | `m_bIgnoreTeleport` | bool |  |  |
| `0x10` | `m_vLinearVelocityAccumulator` | Vector |  |  |
| `0x1c` | `m_vAngularVelocityAccumulator` | RotationVector |  |  |
| `0x28` | `m_vForceAccumulator` | Vector |  |  |
| `0x34` | `m_nBodyCount` | int32 |  |  |
