---
layout: default
title: Game Modes
nav_order: 9
---

# Game Modes & Map Groups

{: .note }
> Source: CS2 build **24304127** · 2026-07-20 · `windows-x86_64` · schema `0.5.0`

Game types and their nested game modes (from `gamemodes.txt`): max players, map groups, and per-mode convar overrides.

## Game type: `classic` (6 modes)

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

## Game type: `cooperative` (2 modes)

### `cooperative`

- **Name token:** `#SFUI_GameModeCooperative`
- **Max players:** 20

### `coopmission`

- **Name token:** `#SFUI_GameModeCoopMission`
- **Max players:** 10

## Game type: `custom` (1 modes)

### `custom`

- **Name token:** `#SFUI_GameModeCustom`
- **Max players:** 100

## Game type: `freeforall` (1 modes)

### `survival`

- **Name token:** `#SFUI_GameModeSurvival`
- **Max players:** 16
- **Map groups:** `mg_dz_sirocco`

## Game type: `gungame` (3 modes)

### `deathmatch`

- **Name token:** `#SFUI_Deathmatch`
- **Max players:** 16
- **Map groups:** `template#include`

### `gungameprogressive`

- **Name token:** `#SFUI_GameModeGGProgressive`
- **Max players:** 16
- **Map groups:** `mg_armsrace`

### `gungametrbomb`

- **Name token:** `#SFUI_GameModeGGBomb`
- **Max players:** 16
- **Map groups:** `mg_demolition`

## Game type: `skirmish` (1 modes)

### `skirmish`

- **Name token:** `#SFUI_GameModeSkirmish`
- **Max players:** 16
- **Map groups:** `mg_skirmish_armsrace`

## Game type: `training` (1 modes)

### `training`

- **Name token:** `#SFUI_GameTypeTraining`
- **Max players:** 1

## Map groups (185)

| id | Maps |
|----|------|
| `mg_active` | `de_dust2`, `de_inferno`, `de_mirage`, `de_nuke`, `de_overpass`, `de_train`, `de_vertigo` |
| `mg_ar_baggage` | `ar_baggage` |
| `mg_ar_dizzy` | `ar_dizzy` |
| `mg_ar_lake` | `de_lake` |
| `mg_ar_lunacy` | `ar_lunacy` |
| `mg_ar_monastery` | `ar_monastery` |
| `mg_ar_pool_day` | `ar_pool_day` |
| `mg_ar_safehouse` | `de_safehouse` |
| `mg_ar_shoots` | `ar_shoots` |
| `mg_ar_shoots_night` | `ar_shoots_night` |
| `mg_ar_stmarc` | `de_stmarc` |
| `mg_armsrace` | `ar_baggage`, `ar_pool_day`, `ar_shoots`, `ar_shoots_night` |
| `mg_casualalpha` | `de_cache`, `de_dust2`, `de_inferno`, `de_mirage`, `de_vertigo` |
| `mg_casualcharlie` | `cs_shelter`, `de_boulder`, `de_fachwerk` |
| `mg_casualdelta` | `de_ancient_night`, `de_anubis`, `de_nuke`, `de_overpass`, `de_train` |
| `mg_casualsigma` | `de_dust2`, `de_inferno`, `de_mirage`, `de_vertigo` |
| `mg_coop_autumn` | `coop_autumn` |
| `mg_coop_cementplant` | `coop_cementplant` |
| `mg_coop_fall` | `coop_fall` |
| `mg_coop_kasbah` | `coop_kasbah` |
| `mg_cs_agency` | `cs_agency` |
| `mg_cs_alpine` | `cs_alpine` |
| `mg_cs_apollo` | `cs_apollo` |
| `mg_cs_assault` | `cs_assault` |
| `mg_cs_backalley` | `cs_backalley` |
| `mg_cs_climb` | `cs_climb` |
| `mg_cs_cruise` | `cs_cruise` |
| `mg_cs_downtown` | `cs_downtown` |
| `mg_cs_insertion` | `cs_insertion` |
| `mg_cs_insertion2` | `cs_insertion2` |
| `mg_cs_italy` | `cs_italy` |
| `mg_cs_militia` | `cs_militia` |
| `mg_cs_motel` | `cs_motel` |
| `mg_cs_museum` | `cs_museum` |
| `mg_cs_office` | `cs_office` |
| `mg_cs_rush` | `cs_rush` |
| `mg_cs_shelter` | `cs_shelter` |
| `mg_cs_siege` | `cs_siege` |
| `mg_cs_thunder` | `cs_thunder` |
| `mg_cs_workout` | `cs_workout` |
| `mg_de_abbey` | `de_abbey` |
| `mg_de_ali` | `de_ali` |
| `mg_de_ancient` | `de_ancient` |
| `mg_de_ancient_night` | `de_ancient_night` |
| `mg_de_anubis` | `de_anubis` |
| `mg_de_assembly` | `de_assembly` |
| `mg_de_austria` | `de_austria` |
| `mg_de_aztec` | `de_aztec` |
| `mg_de_bank` | `de_bank` |
| `mg_de_basalt` | `de_basalt` |
| `mg_de_bazaar` | `de_bazaar` |
| `mg_de_biome` | `de_biome` |
| `mg_de_blackgold` | `de_blackgold` |
| `mg_de_blagai` | `de_blagai` |
| `mg_de_boulder` | `de_boulder` |
| `mg_de_boyard` | `de_boyard` |
| `mg_de_breach` | `de_breach` |
| `mg_de_brewery` | `de_brewery` |
| `mg_de_cache` | `de_cache` |
| `mg_de_cache_scrimmagemap` | `de_cache_scrimmagemap` |
| `mg_de_calavera` | `de_calavera` |
| `mg_de_canals` | `de_canals` |
| `mg_de_castle` | `de_castle` |
| `mg_de_cbble` | `de_cbble` |
| `mg_de_chalice` | `de_chalice` |
| `mg_de_chinatown` | `de_chinatown` |
| `mg_de_chlorine` | `de_chlorine` |
| `mg_de_coast` | `de_coast` |
| `mg_de_crete` | `de_crete` |
| `mg_de_debris` | `de_debris` |
| `mg_de_dogtown` | `de_dogtown` |
| `mg_de_dust` | `de_dust` |
| `mg_de_dust2` | `de_dust2` |
| `mg_de_edin` | `de_edin` |
| `mg_de_eldorado` | `de_eldorado` |
| `mg_de_elysion` | `de_elysion` |
| `mg_de_empire` | `de_empire` |
| `mg_de_engage` | `de_engage` |
| `mg_de_extraction` | `de_extraction` |
| `mg_de_facade` | `de_facade` |
| `mg_de_fachwerk` | `de_fachwerk` |
| `mg_de_favela` | `de_favela` |
| `mg_de_golden` | `de_golden` |
| `mg_de_grail` | `de_grail` |
| `mg_de_grind` | `de_grind` |
| `mg_de_guard` | `de_guard` |
| `mg_de_gwalior` | `de_gwalior` |
| `mg_de_hive` | `de_hive` |
| `mg_de_inferno` | `de_inferno` |
| `mg_de_iris` | `de_iris` |
| `mg_de_jura` | `de_jura` |
| `mg_de_lake` | `de_lake` |
| `mg_de_library` | `de_library` |
| `mg_de_lite` | `de_lite` |
| `mg_de_log` | `de_log` |
| `mg_de_marquis` | `de_marquis` |
| `mg_de_memento` | `de_memento` |
| `mg_de_mikla` | `de_mikla` |
| `mg_de_mills` | `de_mills` |
| `mg_de_mirage` | `de_mirage` |
| `mg_de_mirage_scrimmagemap` | `de_mirage_scrimmagemap` |
| `mg_de_mist` | `de_mist` |
| `mg_de_mocha` | `de_mocha` |
| `mg_de_mutiny` | `de_mutiny` |
| `mg_de_nuke` | `de_nuke` |
| `mg_de_overgrown` | `de_overgrown` |
| `mg_de_overpass` | `de_overpass` |
| `mg_de_palacio` | `de_palacio` |
| `mg_de_palais` | `de_palais` |
| `mg_de_pitstop` | `de_pitstop` |
| `mg_de_poseidon` | `de_poseidon` |
| `mg_de_prime` | `de_prime` |
| `mg_de_rails` | `de_rails` |
| `mg_de_ravine` | `de_ravine` |
| `mg_de_resort` | `de_resort` |
| `mg_de_rooftop` | `de_rooftop` |
| `mg_de_royal` | `de_royal` |
| `mg_de_ruby` | `de_ruby` |
| `mg_de_ruins` | `de_ruins` |
| `mg_de_safehouse` | `de_safehouse` |
| `mg_de_sanctum` | `de_sanctum` |
| `mg_de_santorini` | `de_santorini` |
| `mg_de_seaside` | `de_seaside` |
| `mg_de_season` | `de_season` |
| `mg_de_shipped` | `de_shipped` |
| `mg_de_shortdust` | `de_shortdust` |
| `mg_de_shortnuke` | `de_shortnuke` |
| `mg_de_shorttrain` | `de_shorttrain` |
| `mg_de_stmarc` | `de_stmarc` |
| `mg_de_stronghold` | `de_stronghold` |
| `mg_de_studio` | `de_studio` |
| `mg_de_subzero` | `de_subzero` |
| `mg_de_sugarcane` | `de_sugarcane` |
| `mg_de_swamp` | `de_swamp` |
| `mg_de_thera` | `de_thera` |
| `mg_de_thrill` | `de_thrill` |
| `mg_de_train` | `de_train` |
| `mg_de_transit` | `de_transit` |
| `mg_de_tulip` | `de_tulip` |
| `mg_de_tuscan` | `de_tuscan` |
| `mg_de_vertigo` | `de_vertigo` |
| `mg_de_warden` | `de_warden` |
| `mg_de_whistle` | `de_whistle` |
| `mg_de_zoo` | `de_zoo` |
| `mg_deathmatch` | `ar_baggage`, `ar_monastery`, `ar_shoots`, `cs_assault`, `cs_italy`, `cs_militia`, `cs_office`, `de_aztec`, `de_bank`, `de_cbble`, `de_dust`, `de_dust2`, `de_inferno`, `de_mirage`, `de_nuke`, `de_overpass`, `de_safehouse`, `de_shortdust`, `de_stmarc`, `de_sugarcane`, `de_vertigo` |
| `mg_demolition` | `de_safehouse`, `de_shortdust` |
| `mg_dust247` | `de_dust2` |
| `mg_dz_blacksite` | `dz_blacksite` |
| `mg_dz_county` | `dz_county` |
| `mg_dz_ember` | `dz_ember` |
| `mg_dz_frostbite` | `dz_frostbite` |
| `mg_dz_junglety` | `dz_junglety` |
| `mg_dz_sirocco` | `dz_sirocco` |
| `mg_dz_vineyard` | `dz_vineyard` |
| `mg_gd_bank` | `gd_bank` |
| `mg_gd_cbble` | `gd_cbble` |
| `mg_gd_crashsite` | `gd_crashsite` |
| `mg_gd_dizzy` | `gd_dizzy` |
| `mg_gd_lake` | `gd_lake` |
| `mg_gd_lunacy` | `gd_lunacy` |
| `mg_gd_rialto` | `gd_rialto` |
| `mg_gd_sugarcane` | `gd_sugarcane` |
| `mg_hostage` | `cs_italy`, `cs_office` |
| `mg_lobby_mapveto` | `lobby_mapveto` |
| `mg_lowgravity` | `ar_dizzy`, `ar_lunacy`, `ar_shoots`, `de_safehouse` |
| `mg_op_breakout` | `cs_insertion`, `cs_rush`, `de_blackgold`, `de_castle`, `de_mist`, `de_overgrown` |
| `mg_op_op05` | `cs_backalley`, `cs_workout`, `de_bazaar`, `de_facade`, `de_marquis`, `de_season`, `de_train` |
| `mg_op_op06` | `cs_agency`, `de_log`, `de_rails`, `de_resort`, `de_season`, `de_zoo` |
| `mg_op_op07` | `cs_cruise`, `de_coast`, `de_empire`, `de_mikla`, `de_royal`, `de_santorini`, `de_tulip` |
| `mg_op_op08` | `cs_agency`, `cs_insertion`, `de_austria`, `de_blackgold`, `de_lite`, `de_shipped`, `de_thrill` |
| `mg_reserves` | `de_canals`, `de_dust` |
| `mg_skirmish_armsrace` | `ar_baggage`, `ar_pool_day`, `ar_shoots`, `ar_shoots_night` |
| `mg_skirmish_demolition` | `de_bank`, `de_safehouse`, `de_shortdust`, `de_stmarc`, `de_sugarcane` |
| `mg_skirmish_dm_freeforall` | `cs_assault`, `cs_italy`, `cs_militia`, `cs_office`, `de_ancient`, `de_cbble`, `de_dust2`, `de_inferno`, `de_mirage`, `de_nuke`, `de_overpass`, `de_stmarc`, `de_vertigo` |
| `mg_skirmish_flyingscoutsman` | `ar_dizzy`, `ar_lunacy`, `ar_shoots`, `de_safehouse` |
| `mg_skirmish_headshots` | `cs_agency`, `de_blackgold`, `de_cache`, `de_cbble`, `de_inferno`, `de_nuke` |
| `mg_skirmish_heavyassaultsuit` | `de_austria`, `de_dust2`, `de_mirage`, `de_overpass`, `de_shipped` |
| `mg_skirmish_huntergatherers` | `cs_insertion`, `de_canals`, `de_cbble`, `de_dust2`, `de_nuke`, `de_thrill`, `de_train` |
| `mg_skirmish_retakes` | `de_ancient`, `de_dust2`, `de_inferno`, `de_mirage`, `de_nuke`, `de_overpass`, `de_train`, `de_vertigo` |
| `mg_skirmish_stabstabzap` | `de_austria`, `de_safehouse`, `gd_rialto` |
| `mg_skirmish_triggerdiscipline` | `de_austria`, `de_dust2`, `de_inferno`, `de_lite`, `de_mirage`, `de_thrill` |
| `mg_training1` | `training1` |
| `random_ar` |  |
| `random_classic` |  |
| `random_demo` |  |
