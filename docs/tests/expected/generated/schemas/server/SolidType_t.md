---
title: SolidType_t
module: server
kind: enum
---

[Schemas](../../schemas.md) / [server](../server.md) / SolidType_t

# SolidType_t

> Source: **Build 9000001** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Collision solid type used for an entity's physics representation (m_nSolidType).

**Kind:** enum · **Underlying:** `uint8_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `SOLID_NONE` | 0 | No collision. |
| `SOLID_BSP` | 1 |  |
| `SOLID_BBOX` | 2 | Axis-aligned bounding box. |
| `SOLID_OBB` | 3 | Oriented bounding box. |
| `SOLID_SPHERE` | 4 | Sphere. |
| `SOLID_POINT` | 5 |  |
| `SOLID_VPHYSICS` | 6 | Full VPhysics collision mesh. |
| `SOLID_CAPSULE` | 7 | Capsule (used by player/character collision). |
| `SOLID_CYLINDER` | 8 | Cylinder. |
| `SOLID_LAST` | 9 |  |
