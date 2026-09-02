---
layout: default
title: MoveType_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / MoveType_t

# MoveType_t

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

How an entity is moved and simulated each tick (m_MoveType).

**Kind:** enum · **Underlying:** `uint8_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `MOVETYPE_NONE` | 0 | Not moved by the engine. |
| `MOVETYPE_OBSOLETE` | 1 |  |
| `MOVETYPE_WALK` | 2 | Player-style ground movement (walk/run/jump). |
| `MOVETYPE_FLY` | 3 | Flies in a straight line, ignoring gravity. |
| `MOVETYPE_FLYGRAVITY` | 4 | Ballistic arc under gravity (thrown grenades, projectiles). |
| `MOVETYPE_MAX_BITS` | 5 |  |
| `MOVETYPE_VPHYSICS` | 5 | Driven by the VPhysics simulation. |
| `MOVETYPE_PUSH` | 6 | Pushes other entities without being blocked (movers/doors). |
| `MOVETYPE_NOCLIP` | 7 | Free movement with no collision (noclip). |
| `MOVETYPE_OBSERVER` | 8 | Spectator free-look movement. |
| `MOVETYPE_LADDER` | 9 | Climbing a ladder. |
| `MOVETYPE_CUSTOM` | 10 | Movement handled by custom game code. |
| `MOVETYPE_INVALID` | 11 |  |
| `MOVETYPE_LAST` | 11 |  |
