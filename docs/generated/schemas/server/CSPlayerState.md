---
layout: default
title: CSPlayerState
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / CSPlayerState

# CSPlayerState

Connection / spawn state machine for a CS2 player (m_iPlayerState).

**Kind:** enum · **Underlying:** `uint32_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `STATE_ACTIVE` | 0 |  |
| `STATE_WELCOME` | 1 |  |
| `STATE_PICKINGTEAM` | 2 |  |
| `STATE_PICKINGCLASS` | 3 |  |
| `STATE_DEATH_ANIM` | 4 |  |
| `STATE_DEATH_WAIT_FOR_KEY` | 5 |  |
| `STATE_OBSERVER_MODE` | 6 |  |
| `STATE_GUNGAME_RESPAWN` | 7 |  |
| `STATE_DORMANT` | 8 |  |
| `NUM_PLAYER_STATES` | 9 |  |
