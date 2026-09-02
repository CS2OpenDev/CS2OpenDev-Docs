---
title: LifeState_t
module: server
kind: enum
---

[Schemas](../../schemas.md) / [server](../server.md) / LifeState_t

# LifeState_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Alive/dead state of a pawn (m_lifeState).

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `LIFE_ALIVE` | 0 | Alive and playable. |
| `LIFE_DYING` | 1 | Playing the death animation; not yet fully dead. |
| `LIFE_DEAD` | 2 | Dead. |
| `LIFE_RESPAWNABLE` | 3 | Dead and eligible to respawn. |
| `LIFE_RESPAWNING` | 4 | In the process of respawning. |
| `NUM_LIFESTATES` | 5 |  |
