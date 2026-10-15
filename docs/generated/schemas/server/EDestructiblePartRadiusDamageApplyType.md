---
title: EDestructiblePartRadiusDamageApplyType
module: server
kind: enum
---

[Schemas](../../schemas.md) / [server](../server.md) / EDestructiblePartRadiusDamageApplyType

# EDestructiblePartRadiusDamageApplyType

> Source: **Build 25947352** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `ScaleByExplosionRadius` | 0 | Damage is scaled proportionally based on distance from the epicenter. |
| `PrioritizeClosestPart` | 1 | Damage is dumped to the closest alive part, and the remainder is scaled as in ScaleByExplosionRadius algorithm. |
