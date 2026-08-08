---
layout: default
title: EDestructiblePartRadiusDamageApplyType
nav_exclude: true
---

[Schemas](../../schemas.md) / [!GlobalTypes](../!GlobalTypes.md) / EDestructiblePartRadiusDamageApplyType

# EDestructiblePartRadiusDamageApplyType

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** !GlobalTypes

## Values

| Name | Value | Description |
|------|-------|-------------|
| `ScaleByExplosionRadius` | 0 | Damage is scaled proportionally based on distance from the epicenter. |
| `PrioritizeClosestPart` | 1 | Damage is dumped to the closest alive part, and the remainder is scaled as in ScaleByExplosionRadius algorithm. |
