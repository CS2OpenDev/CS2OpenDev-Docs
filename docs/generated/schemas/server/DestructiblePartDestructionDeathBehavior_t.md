---
title: DestructiblePartDestructionDeathBehavior_t
module: server
kind: enum
---

[Schemas](../../schemas.md) / [server](../server.md) / DestructiblePartDestructionDeathBehavior_t

# DestructiblePartDestructionDeathBehavior_t

> Source: **Build 25966348** · 2026-10-15 · `windows-x86_64` · schema `0.12.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `eDoNotKill` | 0 | Does not kill the entity when the part is destroyed |
| `eKill` | 1 | Kills the entity, using the normal codepath to determine kill type, when the part is destroyed |
| `eGib` | 2 | Kills and gibs the entity when the part is destroyed |
| `eRemove` | 3 | Kills and instantly removes the entity when the part is destroyed |
