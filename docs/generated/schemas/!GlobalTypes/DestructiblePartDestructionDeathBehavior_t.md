---
layout: default
title: DestructiblePartDestructionDeathBehavior_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [!GlobalTypes](../!GlobalTypes.md) / DestructiblePartDestructionDeathBehavior_t

# DestructiblePartDestructionDeathBehavior_t

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** !GlobalTypes

## Values

| Name | Value | Description |
|------|-------|-------------|
| `eDoNotKill` | 0 | Does not kill the entity when the part is destroyed |
| `eKill` | 1 | Kills the entity, using the normal codepath to determine kill type, when the part is destroyed |
| `eGib` | 2 | Kills and gibs the entity when the part is destroyed |
| `eRemove` | 3 | Kills and instantly removes the entity when the part is destroyed |
