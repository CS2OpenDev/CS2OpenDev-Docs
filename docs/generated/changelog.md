---
title: Changelog
---

# Build Changelog

> Source: **Build 26598758** · 2026-11-11 · `windows-x86_64` · schema `0.13.0`

Difference between build **26445667** and **26598758** (`windows-x86_64`), grouped by data family.

Families diffed: `classes`, `enums`, `convars`, `commands`, `engine_constants`, `cs_script_api`, `entity_io`.

## classes (+0 / −0 / ~6)

| Entry | Field changes |
|-------|---------------|
| `!GlobalTypes/CNmAimCSNode::CDefinition` | field_count: `11` → `12` |
| `!GlobalTypes/CNmGraphDocAimCSNode` | field_count: `3` → `4` |
| `!GlobalTypes/EventClientPollNetworking_t` | field_count: `1` → `2` |
| `client.dll/CMapInfo` | field_count: `15` → `16` |
| `client.dll/C_Hostage` | field_count: `23` → `22` |
| `server.dll/CMapInfo` | field_count: `15` → `16` |

## convars (+15 / −2 / ~0)

**Added:** `cl_clockdrift_max_secs`, `cl_packetentities_merge_before_decode`, `r_csgo_frost_dry_time`, `r_csgo_frost_force`, `r_csgo_frost_grow_time`, `r_csgo_frost_heat_barrel_position`, `r_csgo_frost_heat_cool_time`, `r_csgo_frost_heat_light_delay`, `r_csgo_frost_heat_light_time`, `r_csgo_frost_heat_per_shot`, `r_csgo_frost_indoor_distance`, `r_csgo_frost_melt_time`, `r_csgo_parallax`, `videocfg_parallax_detail`, `vprof_lite_auto`

**Removed:** `cl_clockdrift_max_ticks`, `sv_recvbuf_messages`

## commands (+3 / −0 / ~0)

**Added:** `vprof_lite_dump`, `vprof_lite_start`, `vprof_lite_stop`

## entity_io (+0 / −0 / ~1)

| Entry | Field changes |
|-------|---------------|
| `info_map_parameters` | keyvalue:frostenabled:  → `boolean` |
