---
title: CSPlayerState
module: server
kind: enum
---

[Schemas](../../schemas.md) / [server](../server.md) / CSPlayerState

# CSPlayerState

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Connection / spawn state machine for a CS2 player (m_iPlayerState).

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `STATE_ACTIVE` | 0 | In active play, controlling a pawn. |
| `STATE_WELCOME` | 1 | Just connected; showing the intro / welcome screen. |
| `STATE_PICKINGTEAM` | 2 | Choosing a team. |
| `STATE_PICKINGCLASS` | 3 |  |
| `STATE_DEATH_ANIM` | 4 | Playing the death animation. |
| `STATE_DEATH_WAIT_FOR_KEY` | 5 |  |
| `STATE_OBSERVER_MODE` | 6 | Spectating (dead or connected as an observer). |
| `STATE_GUNGAME_RESPAWN` | 7 |  |
| `STATE_DORMANT` | 8 | Not yet fully in the game (loading / intermission). |
| `NUM_PLAYER_STATES` | 9 |  |
