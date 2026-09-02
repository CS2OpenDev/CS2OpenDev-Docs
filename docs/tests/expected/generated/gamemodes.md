---
layout: default
title: Game Modes
nav_order: 9
---

# Game Modes & Map Groups

> Source: **Build 9000001** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Game types and their nested game modes (from `gamemodes.txt`): max players, map groups, and per-mode convar overrides.

## Game type: `classic`

6 modes.

### `casual`

- **Name token:** `#SFUI_GameModeCasual`
- **Max players:** 20
- **Map groups:** `template#include`

### `competitive`

- **Name token:** `#SFUI_GameModeCompetitive`
- **Max players:** 10
- **Map groups:** `template#include`

### `new_user_training`

- **Name token:** `#SFUI_GameModeCompetitive`
- **Max players:** 10
- **Map groups:** `mg_de_dust2`

### `retakes`

- **Name token:** `#SFUI_GameModeRetakes`
- **Max players:** 7
- **Map groups:** `mg_casualalpha`, `mg_casualdelta`

### `scrimcomp2v2`

- **Name token:** `#SFUI_GameModeScrimComp2v2`
- **Max players:** 4
- **Map groups:** `template#include`

### `scrimcomp5v5`

- **Name token:** `#SFUI_GameModeScrimComp5v5`
- **Max players:** 10
- **Map groups:** `template#include`

## Map groups

3 map groups.

| id | Maps |
|----|------|
| `mg_active` | `de_dust2`, `de_inferno`, `de_mirage`, `de_nuke`, `de_overpass`, `de_train`, `de_vertigo` |
| `mg_ar_baggage` | `ar_baggage` |
| `mg_ar_dizzy` | `ar_dizzy` |
