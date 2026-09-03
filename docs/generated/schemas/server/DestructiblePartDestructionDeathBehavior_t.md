---
title: DestructiblePartDestructionDeathBehavior_t
module: server
kind: enum
---

[Schemas](../../schemas.md) / [server](../server.md) / DestructiblePartDestructionDeathBehavior_t

# DestructiblePartDestructionDeathBehavior_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `eDoNotKill` | 0 | Does not kill the entity when the part is destroyed |
| `eKill` | 1 | Kills the entity, using the normal codepath to determine kill type, when the part is destroyed |
| `eGib` | 2 | Kills and gibs the entity when the part is destroyed |
| `eRemove` | 3 | Kills and instantly removes the entity when the part is destroyed |
