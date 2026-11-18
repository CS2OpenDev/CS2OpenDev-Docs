---
title: Changelog
---

# Build Changelog

> Source: **Build 26748068** · 2026-11-18 · `windows-x86_64` · schema `0.13.0`

Difference between build **26598758** and **26748068** (`windows-x86_64`), grouped by data family.

Families diffed: `classes`, `enums`, `convars`, `commands`, `engine_constants`, `cs_script_api`, `entity_io`.

## convars (+2 / −12 / ~6)

**Added:** `player_competitive_maplist_2v2_10_0_7B2B4F7`, `player_competitive_maplist_8_10_0_25074C46`

**Removed:** `player_competitive_maplist_2v2_10_0_D684D4E1`, `player_competitive_maplist_8_10_0_A062AC6A`, `r_csgo_frost_dry_time`, `r_csgo_frost_force`, `r_csgo_frost_grow_time`, `r_csgo_frost_heat_barrel_position`, `r_csgo_frost_heat_cool_time`, `r_csgo_frost_heat_light_delay`, `r_csgo_frost_heat_light_time`, `r_csgo_frost_heat_per_shot`, `r_csgo_frost_indoor_distance`, `r_csgo_frost_melt_time`

| Entry | Field changes |
|-------|---------------|
| `mp_endwarmup_player_count` | flags: `gamedll,clientdll,replicated,release` → `gamedll,release,commandline_enforced` |
| `mp_match_end_changelevel` | flags: `gamedll,clientdll,replicated,release,commandline_enforced` → `gamedll,release,commandline_enforced` |
| `mp_match_end_restart` | flags: `gamedll,clientdll,replicated,release` → `gamedll,release,commandline_enforced` |
| `mp_verbose_changelevel_spew` | flags: `gamedll,clientdll,replicated,release` → `gamedll,release` |
| `mp_warmuptime_all_players_connected` | flags: `gamedll,clientdll,replicated,release,commandline_enforced` → `gamedll,release,commandline_enforced` |
| `mp_warmuptime_match_cancelled` | flags: `gamedll,clientdll,replicated,release,commandline_enforced` → `gamedll,release,commandline_enforced` |
