---
layout: default
title: EDestructiblePartRadiusDamageApplyType
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / EDestructiblePartRadiusDamageApplyType

# EDestructiblePartRadiusDamageApplyType

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `ScaleByExplosionRadius` | 0 | Damage is scaled proportionally based on distance from the epicenter. |
| `PrioritizeClosestPart` | 1 | Damage is dumped to the closest alive part, and the remainder is scaled as in ScaleByExplosionRadius algorithm. |
