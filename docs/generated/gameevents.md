---
layout: default
title: Game Events
nav_order: 6
---

# Game Events Reference

Game events extracted from CS2's `.gameevents` resource files. These events are fired by the game engine and server to signal in-game occurrences such as player actions, round state changes, and UI notifications.

## Field Types

| Type | Description |
|------|-------------|
| `bool` | Unsigned int, 1 bit |
| `byte` | Unsigned int, 8 bit |
| `ehandle` | Entity handle |
| `float` | Float, 32 bit |
| `int` | Signed integer |
| `local` | Any data, not networked |
| `long` | Signed int, 32 bit |
| `none` | Value is not networked |
| `player_controller` | Player controller entity reference |
| `player_controller_and_pawn` | Player controller + pawn entity reference |
| `player_pawn` | Player pawn entity reference |
| `short` | Signed int, 16 bit |
| `string` | A zero-terminated string |
| `uint64` | Unsigned 64-bit integer (string-encoded) |

## Summary

**Total events:** 195

| Source | Events | Description |
|--------|--------|-------------|
| `game.gameevents` | 50 | Game Events |
| `mod.gameevents` | 145 | CS2 (Counter-Strike) Events |

## Event Index

| Event | Source | Fields | Description |
|-------|--------|--------|-------------|
| [add_bullet_hit_marker](#add_bullet_hit_marker) | `game.gameevents` | 12 |  |
| [add_player_sonar_icon](#add_player_sonar_icon) | `game.gameevents` | 4 |  |
| [begin_new_match](#begin_new_match) | `game.gameevents` | 0 |  |
| [break_prop](#break_prop) | `game.gameevents` | 2 |  |
| [client_loadout_changed](#client_loadout_changed) | `game.gameevents` | 0 |  |
| [dm_bonus_weapon_start](#dm_bonus_weapon_start) | `game.gameevents` | 2 |  |
| [door_break](#door_break) | `game.gameevents` | 2 |  |
| [door_closed](#door_closed) | `game.gameevents` | 2 |  |
| [door_open](#door_open) | `game.gameevents` | 2 |  |
| [endmatch_cmm_start_reveal_items](#endmatch_cmm_start_reveal_items) | `game.gameevents` | 0 |  |
| [endmatch_mapvote_selecting_map](#endmatch_mapvote_selecting_map) | `game.gameevents` | 11 |  |
| [entity_visible](#entity_visible) | `game.gameevents` | 4 |  |
| [game_end](#game_end) | `game.gameevents` | 1 | a game ended |
| [game_init](#game_init) | `game.gameevents` | 0 | sent when a new game is started |
| [game_newmap](#game_newmap) | `game.gameevents` | 1 | send when new map is completely loaded |
| [game_start](#game_start) | `game.gameevents` | 4 | a new game starts |
| [gameui_hidden](#gameui_hidden) | `game.gameevents` | 0 |  |
| [instructor_server_hint_create](#instructor_server_hint_create) | `game.gameevents` | 20 | create a hint using data supplied entirely by the server/map. Intended for hints to smooth playtests before content is ready to make the hint unneccessary. NOT INTENDED AS A SHIPPABLE CRUTCH |
| [instructor_server_hint_stop](#instructor_server_hint_stop) | `game.gameevents` | 1 | destroys a server/map created hint |
| [inventory_updated](#inventory_updated) | `game.gameevents` | 0 |  |
| [player_chat](#player_chat) | `game.gameevents` | 3 | a public player chat |
| [player_decal](#player_decal) | `game.gameevents` | 1 |  |
| [player_score](#player_score) | `game.gameevents` | 4 | players scores changed |
| [player_shoot](#player_shoot) | `game.gameevents` | 3 | player shoot his weapon |
| [player_team](#player_team) | `game.gameevents` | 6 | Fired when a player switches teams (T ↔ CT, or to/from Spectator).  `team` is the new team; `oldteam` is the previous. `disconnect=true` indicates the team change was caused by the player leaving rather than a deliberate switch.
 |
| [read_game_titledata](#read_game_titledata) | `game.gameevents` | 1 | read user titledata from profile |
| [reset_game_titledata](#reset_game_titledata) | `game.gameevents` | 1 | reset user titledata; do not automatically write profile |
| [round_announce_final](#round_announce_final) | `game.gameevents` | 0 |  |
| [round_announce_last_round_half](#round_announce_last_round_half) | `game.gameevents` | 0 |  |
| [round_announce_match_point](#round_announce_match_point) | `game.gameevents` | 0 |  |
| [round_announce_match_start](#round_announce_match_start) | `game.gameevents` | 0 |  |
| [round_announce_warmup](#round_announce_warmup) | `game.gameevents` | 0 |  |
| [round_end](#round_end) | `game.gameevents` | 4 | Fired when a round concludes.  Carries the winning team (`winner`), the reason for the win (`reason`, see RoundEndReason table below), and a human-readable `message` string.
 |
| [round_end_upload_stats](#round_end_upload_stats) | `game.gameevents` | 0 |  |
| [round_officially_ended](#round_officially_ended) | `game.gameevents` | 0 |  |
| [round_time_warning](#round_time_warning) | `game.gameevents` | 0 |  |
| [survival_announce_phase](#survival_announce_phase) | `game.gameevents` | 1 |  |
| [ugc_file_download_finished](#ugc_file_download_finished) | `game.gameevents` | 1 |  |
| [ugc_file_download_start](#ugc_file_download_start) | `game.gameevents` | 2 |  |
| [ugc_map_download_error](#ugc_map_download_error) | `game.gameevents` | 2 |  |
| [ugc_map_info_received](#ugc_map_info_received) | `game.gameevents` | 1 |  |
| [ugc_map_unsubscribed](#ugc_map_unsubscribed) | `game.gameevents` | 1 |  |
| [vote_cast](#vote_cast) | `game.gameevents` | 3 |  |
| [vote_changed](#vote_changed) | `game.gameevents` | 6 |  |
| [vote_ended](#vote_ended) | `game.gameevents` | 0 |  |
| [vote_options](#vote_options) | `game.gameevents` | 6 |  |
| [vote_started](#vote_started) | `game.gameevents` | 4 |  |
| [warmup_end](#warmup_end) | `game.gameevents` | 0 |  |
| [weaponhud_selection](#weaponhud_selection) | `game.gameevents` | 3 |  |
| [write_game_titledata](#write_game_titledata) | `game.gameevents` | 1 | write user titledata in profile |
| [achievement_earned_local](#achievement_earned_local) | `mod.gameevents` | 2 |  |
| [achievement_info_loaded](#achievement_info_loaded) | `mod.gameevents` | 0 |  |
| [ammo_pickup](#ammo_pickup) | `mod.gameevents` | 3 |  |
| [ammo_refill](#ammo_refill) | `mod.gameevents` | 2 |  |
| [announce_phase_end](#announce_phase_end) | `mod.gameevents` | 0 |  |
| [bomb_abortdefuse](#bomb_abortdefuse) | `mod.gameevents` | 1 |  |
| [bomb_abortplant](#bomb_abortplant) | `mod.gameevents` | 2 |  |
| [bomb_beep](#bomb_beep) | `mod.gameevents` | 1 | Fired on each beep of an armed C4.  `entindex` references the `CPlantedC4`.  Cadence accelerates as detonation approaches.
 |
| [bomb_begindefuse](#bomb_begindefuse) | `mod.gameevents` | 2 |  |
| [bomb_beginplant](#bomb_beginplant) | `mod.gameevents` | 2 | Fired the moment a player begins the C4 plant animation.  The plant can still be interrupted (player damaged, switches weapon, leaves site); listen for `bomb_planted` to confirm completion.
 |
| [bomb_defused](#bomb_defused) | `mod.gameevents` | 3 | Fired when the C4 is successfully defused.  `userid` is the defuser; `site` is the bombsite.
 |
| [bomb_dropped](#bomb_dropped) | `mod.gameevents` | 2 | Fired when a player carrying the C4 drops it (death, voluntary drop, disconnect).  `entindex` identifies the C4 world entity now sitting on the ground.
 |
| [bomb_exploded](#bomb_exploded) | `mod.gameevents` | 3 | Fired when the C4 detonates (defuse failed / timer expired). `userid` is the original planter (the actor who armed it), not the player nearest the explosion.
 |
| [bomb_pickup](#bomb_pickup) | `mod.gameevents` | 1 | Fired when a player picks up a dropped C4.  `userid` here is a `player_pawn` (not `player_controller_and_pawn`) — only the pawn half is meaningful.
 |
| [bomb_planted](#bomb_planted) | `mod.gameevents` | 3 | Fired when the C4 is successfully armed.  `site` is the bombsite index (0=A, 1=B).  At this point a `CPlantedC4` entity exists and the 40-second countdown begins.
 |
| [bullet_damage](#bullet_damage) | `mod.gameevents` | 24 | Fired on every firearm-projectile hit landed on a player.  Far richer than `player_hurt`: includes shot angles, aim-punch, inaccuracy components, penetration count, and lag-compensation type.  This is the right event for ballistics analysis and cheat-detection heuristics.
 |
| [bullet_impact](#bullet_impact) | `mod.gameevents` | 4 |  |
| [buymenu_close](#buymenu_close) | `mod.gameevents` | 1 |  |
| [buymenu_open](#buymenu_open) | `mod.gameevents` | 0 |  |
| [buytime_ended](#buytime_ended) | `mod.gameevents` | 0 |  |
| [choppers_incoming_warning](#choppers_incoming_warning) | `mod.gameevents` | 1 |  |
| [client_disconnect](#client_disconnect) | `mod.gameevents` | 0 |  |
| [clientside_reload_custom_econ](#clientside_reload_custom_econ) | `mod.gameevents` | 1 |  |
| [cs_game_disconnected](#cs_game_disconnected) | `mod.gameevents` | 0 |  |
| [cs_intermission](#cs_intermission) | `mod.gameevents` | 0 |  |
| [cs_match_end_restart](#cs_match_end_restart) | `mod.gameevents` | 0 |  |
| [cs_pre_restart](#cs_pre_restart) | `mod.gameevents` | 0 |  |
| [cs_prev_next_spectator](#cs_prev_next_spectator) | `mod.gameevents` | 1 |  |
| [cs_round_final_beep](#cs_round_final_beep) | `mod.gameevents` | 0 | Fired on the final pre-explosion beep of the planted C4.  Useful for demo-parsing tooling that wants to mark "bomb is about to detonate" without polling `m_flC4Blow` on the C4 entity.
 |
| [cs_round_start_beep](#cs_round_start_beep) | `mod.gameevents` | 0 |  |
| [cs_win_panel_match](#cs_win_panel_match) | `mod.gameevents` | 0 |  |
| [cs_win_panel_round](#cs_win_panel_round) | `mod.gameevents` | 9 |  |
| [decoy_detonate](#decoy_detonate) | `mod.gameevents` | 5 | Fired each time a decoy grenade fires its fake gunshot sound. Multiple per decoy lifetime.
 |
| [decoy_firing](#decoy_firing) | `mod.gameevents` | 5 |  |
| [decoy_started](#decoy_started) | `mod.gameevents` | 5 |  |
| [defuser_dropped](#defuser_dropped) | `mod.gameevents` | 1 |  |
| [defuser_pickup](#defuser_pickup) | `mod.gameevents` | 2 |  |
| [door_moving](#door_moving) | `mod.gameevents` | 2 |  |
| [drone_above_roof](#drone_above_roof) | `mod.gameevents` | 2 |  |
| [drone_cargo_detached](#drone_cargo_detached) | `mod.gameevents` | 3 |  |
| [drone_dispatched](#drone_dispatched) | `mod.gameevents` | 3 |  |
| [dronegun_attack](#dronegun_attack) | `mod.gameevents` | 1 |  |
| [dz_item_interaction](#dz_item_interaction) | `mod.gameevents` | 3 |  |
| [enable_restart_voting](#enable_restart_voting) | `mod.gameevents` | 1 |  |
| [enter_bombzone](#enter_bombzone) | `mod.gameevents` | 3 |  |
| [enter_buyzone](#enter_buyzone) | `mod.gameevents` | 2 |  |
| [enter_rescue_zone](#enter_rescue_zone) | `mod.gameevents` | 1 |  |
| [exit_bombzone](#exit_bombzone) | `mod.gameevents` | 3 |  |
| [exit_buyzone](#exit_buyzone) | `mod.gameevents` | 2 |  |
| [exit_rescue_zone](#exit_rescue_zone) | `mod.gameevents` | 1 |  |
| [firstbombs_incoming_warning](#firstbombs_incoming_warning) | `mod.gameevents` | 1 |  |
| [flashbang_detonate](#flashbang_detonate) | `mod.gameevents` | 5 | Fired when a flashbang explodes.  Per-player flash duration is *not* on this event — read `m_flFlashDuration` / `m_flFlashMaxAlpha` on each affected `CCSPlayerPawn` instead.
 |
| [game_phase_changed](#game_phase_changed) | `mod.gameevents` | 1 |  |
| [gg_killed_enemy](#gg_killed_enemy) | `mod.gameevents` | 5 |  |
| [grenade_bounce](#grenade_bounce) | `mod.gameevents` | 1 |  |
| [grenade_thrown](#grenade_thrown) | `mod.gameevents` | 2 | Fired when a grenade leaves a player's hand.  Pair with the matching `<type>_detonate` event for landing/explosion location.
 |
| [guardian_wave_restart](#guardian_wave_restart) | `mod.gameevents` | 0 |  |
| [hegrenade_detonate](#hegrenade_detonate) | `mod.gameevents` | 5 | Fired when an HE grenade explodes.  `x`/`y`/`z` is the world position of the detonation; `entityid` is the projectile's entity index (now removed).
 |
| [hide_deathpanel](#hide_deathpanel) | `mod.gameevents` | 0 |  |
| [hltv_changed_mode](#hltv_changed_mode) | `mod.gameevents` | 3 |  |
| [hostage_call_for_help](#hostage_call_for_help) | `mod.gameevents` | 1 |  |
| [hostage_follows](#hostage_follows) | `mod.gameevents` | 2 |  |
| [hostage_hurt](#hostage_hurt) | `mod.gameevents` | 2 |  |
| [hostage_killed](#hostage_killed) | `mod.gameevents` | 2 | Fired when a hostage entity is killed.  CTs incur a money penalty; this event is the canonical hook for that bookkeeping. `hostage` is the hostage entity index, not the hostage definition.
 |
| [hostage_rescued](#hostage_rescued) | `mod.gameevents` | 3 | Fired when a hostage reaches a rescue zone.  `site` is the rescue-zone index when a map carries more than one.
 |
| [hostage_rescued_all](#hostage_rescued_all) | `mod.gameevents` | 0 |  |
| [hostage_stops_following](#hostage_stops_following) | `mod.gameevents` | 2 |  |
| [inferno_expire](#inferno_expire) | `mod.gameevents` | 4 |  |
| [inferno_extinguish](#inferno_extinguish) | `mod.gameevents` | 4 |  |
| [inferno_startburn](#inferno_startburn) | `mod.gameevents` | 4 |  |
| [inspect_weapon](#inspect_weapon) | `mod.gameevents` | 1 |  |
| [item_equip](#item_equip) | `mod.gameevents` | 9 | Fired when a player switches to a different weapon or gear slot. Carries flags describing the equipped item (silencer, tracers, paint kit) so demo tooling doesn't need a second lookup.
 |
| [item_pickup](#item_pickup) | `mod.gameevents` | 4 | Fired when a player picks up a weapon or piece of gear.  `item` is the classname / definition string (`tmp`, `hegrenade`, `nvgs`, …); `defindex` is the Steam economy item definition index of the specific skin / version picked up.
 |
| [item_pickup_failed](#item_pickup_failed) | `mod.gameevents` | 4 |  |
| [item_pickup_slerp](#item_pickup_slerp) | `mod.gameevents` | 3 |  |
| [item_purchase](#item_purchase) | `mod.gameevents` | 4 |  |
| [item_remove](#item_remove) | `mod.gameevents` | 3 |  |
| [jointeam_failed](#jointeam_failed) | `mod.gameevents` | 2 |  |
| [loot_crate_opened](#loot_crate_opened) | `mod.gameevents` | 2 |  |
| [loot_crate_visible](#loot_crate_visible) | `mod.gameevents` | 3 |  |
| [match_end_conditions](#match_end_conditions) | `mod.gameevents` | 4 |  |
| [material_default_complete](#material_default_complete) | `mod.gameevents` | 0 |  |
| [mb_input_lock_cancel](#mb_input_lock_cancel) | `mod.gameevents` | 0 |  |
| [mb_input_lock_success](#mb_input_lock_success) | `mod.gameevents` | 0 |  |
| [molotov_detonate](#molotov_detonate) | `mod.gameevents` | 4 | Fired when a Molotov / Incendiary grenade ignites and begins laying fire.  The resulting `CInferno` entity carries the per-fragment damage volumes.
 |
| [nav_blocked](#nav_blocked) | `mod.gameevents` | 2 |  |
| [nav_generate](#nav_generate) | `mod.gameevents` | 0 |  |
| [nextlevel_changed](#nextlevel_changed) | `mod.gameevents` | 3 | a game event, name may be 32 characters long |
| [open_crate_instr](#open_crate_instr) | `mod.gameevents` | 3 |  |
| [other_death](#other_death) | `mod.gameevents` | 12 |  |
| [parachute_deploy](#parachute_deploy) | `mod.gameevents` | 1 |  |
| [parachute_pickup](#parachute_pickup) | `mod.gameevents` | 1 |  |
| [player_avenged_teammate](#player_avenged_teammate) | `mod.gameevents` | 2 |  |
| [player_blind](#player_blind) | `mod.gameevents` | 4 |  |
| [player_death](#player_death) | `mod.gameevents` | 22 | Fired when a player dies.  Carries `userid` (the victim) and `attacker`.  Detailed kill information (weapon, headshot, assister, penetration count, no-scope flag, distance) lives on the legacy `cs_gameevents.proto` user-message `CMsgSource1LegacyGameEvent` payload — extract those keys when parsing demos.
 |
| [player_falldamage](#player_falldamage) | `mod.gameevents` | 2 |  |
| [player_footstep](#player_footstep) | `mod.gameevents` | 1 |  |
| [player_given_c4](#player_given_c4) | `mod.gameevents` | 1 |  |
| [player_hurt](#player_hurt) | `mod.gameevents` | 8 | Fired when a player takes damage from any source.  The pre-CS2 `weapon` / `dmg_armor` / `dmg_health` / `hitgroup` fields were removed in CS2; for those, use `bullet_damage` (firearm damage) or correlate with the relevant grenade-detonation event.
 |
| [player_jump](#player_jump) | `mod.gameevents` | 1 |  |
| [player_ping](#player_ping) | `mod.gameevents` | 6 |  |
| [player_ping_stop](#player_ping_stop) | `mod.gameevents` | 1 |  |
| [player_radio](#player_radio) | `mod.gameevents` | 2 |  |
| [player_reset_vote](#player_reset_vote) | `mod.gameevents` | 2 |  |
| [player_sound](#player_sound) | `mod.gameevents` | 4 |  |
| [player_spawned](#player_spawned) | `mod.gameevents` | 2 |  |
| [repost_xbox_achievements](#repost_xbox_achievements) | `mod.gameevents` | 1 |  |
| [round_end](#round_end) | `mod.gameevents` | 6 | Fired when a round concludes.  Carries the winning team (`winner`), the reason for the win (`reason`, see RoundEndReason table below), and a human-readable `message` string.
 |
| [round_mvp](#round_mvp) | `mod.gameevents` | 6 | Fired at the end of a round to announce the MVP and the music kit that played.  `reason` enumerates why this player was selected (kills, defuse, plant, …); `musickitid` is the Steam item definition index of the MVP anthem.
 |
| [round_poststart](#round_poststart) | `mod.gameevents` | 0 | sent after all other round restart actions |
| [round_prestart](#round_prestart) | `mod.gameevents` | 0 | sent before all other round restart actions |
| [seasoncoin_levelup](#seasoncoin_levelup) | `mod.gameevents` | 3 |  |
| [sfuievent](#sfuievent) | `mod.gameevents` | 3 |  |
| [show_deathpanel](#show_deathpanel) | `mod.gameevents` | 7 |  |
| [show_survival_respawn_status](#show_survival_respawn_status) | `mod.gameevents` | 3 |  |
| [silencer_detach](#silencer_detach) | `mod.gameevents` | 1 |  |
| [silencer_off](#silencer_off) | `mod.gameevents` | 1 |  |
| [silencer_on](#silencer_on) | `mod.gameevents` | 1 |  |
| [smoke_beacon_paradrop](#smoke_beacon_paradrop) | `mod.gameevents` | 2 |  |
| [smokegrenade_detonate](#smokegrenade_detonate) | `mod.gameevents` | 5 | Fired when a smoke grenade pops and begins emitting smoke. Pair with `smokegrenade_expired` for the lifetime window.
 |
| [smokegrenade_expired](#smokegrenade_expired) | `mod.gameevents` | 5 | Fired when a smoke cloud fully dissipates.
 |
| [spec_mode_updated](#spec_mode_updated) | `mod.gameevents` | 1 |  |
| [start_halftime](#start_halftime) | `mod.gameevents` | 0 |  |
| [start_vote](#start_vote) | `mod.gameevents` | 3 |  |
| [survival_no_respawns_final](#survival_no_respawns_final) | `mod.gameevents` | 1 |  |
| [survival_no_respawns_warning](#survival_no_respawns_warning) | `mod.gameevents` | 1 |  |
| [survival_paradrop_break](#survival_paradrop_break) | `mod.gameevents` | 1 |  |
| [survival_paradrop_spawn](#survival_paradrop_spawn) | `mod.gameevents` | 1 |  |
| [survival_teammate_respawn](#survival_teammate_respawn) | `mod.gameevents` | 1 |  |
| [switch_team](#switch_team) | `mod.gameevents` | 5 |  |
| [tagrenade_detonate](#tagrenade_detonate) | `mod.gameevents` | 5 |  |
| [team_intro_end](#team_intro_end) | `mod.gameevents` | 0 |  |
| [team_intro_start](#team_intro_start) | `mod.gameevents` | 0 |  |
| [teamchange_pending](#teamchange_pending) | `mod.gameevents` | 2 |  |
| [tournament_reward](#tournament_reward) | `mod.gameevents` | 3 |  |
| [trial_time_expired](#trial_time_expired) | `mod.gameevents` | 1 |  |
| [update_matchmaking_stats](#update_matchmaking_stats) | `mod.gameevents` | 0 |  |
| [vip_escaped](#vip_escaped) | `mod.gameevents` | 1 |  |
| [vip_killed](#vip_killed) | `mod.gameevents` | 2 |  |
| [weapon_fire](#weapon_fire) | `mod.gameevents` | 3 | Fired each time a player pulls the trigger and a shot is taken. `weapon` is the lowercase classname (`ak47`, `awp`, `knife`, `hegrenade`, …).  Use `bullet_damage` for the *hit* event counterpart.
 |
| [weapon_fire_on_empty](#weapon_fire_on_empty) | `mod.gameevents` | 2 |  |
| [weapon_reload](#weapon_reload) | `mod.gameevents` | 1 |  |
| [weapon_zoom](#weapon_zoom) | `mod.gameevents` | 1 |  |
| [weapon_zoom_rifle](#weapon_zoom_rifle) | `mod.gameevents` | 1 |  |
| [write_profile_data](#write_profile_data) | `mod.gameevents` | 0 |  |

---

## Game Events

*Source: `game.gameevents`*

### add_bullet_hit_marker

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `bone` | `short` |  |
| `pos_x` | `short` |  |
| `pos_y` | `short` |  |
| `pos_z` | `short` |  |
| `ang_x` | `short` |  |
| `ang_y` | `short` |  |
| `ang_z` | `short` |  |
| `start_x` | `short` |  |
| `start_y` | `short` |  |
| `start_z` | `short` |  |
| `hit` | `bool` |  |

### add_player_sonar_icon

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `pos_x` | `float` |  |
| `pos_y` | `float` |  |
| `pos_z` | `float` |  |

### begin_new_match

*No fields — this event carries no additional data.*

### break_prop

| Field | Type | Description |
|-------|------|-------------|
| `entindex` | `long` |  |
| `userid` | `player_pawn` |  |

### client_loadout_changed

*No fields — this event carries no additional data.*

### dm_bonus_weapon_start

| Field | Type | Description |
|-------|------|-------------|
| `time` | `short` | The length of time that this bonus lasts |
| `Pos` | `short` | Loadout position of the bonus weapon |

### door_break

| Field | Type | Description |
|-------|------|-------------|
| `entindex` | `long` |  |
| `dmgstate` | `long` |  |

### door_closed

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_pawn` | Who closed the door |
| `entindex` | `long` |  |

### door_open

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_pawn` | Who closed the door |
| `entindex` | `long` |  |

### endmatch_cmm_start_reveal_items

*No fields — this event carries no additional data.*

### endmatch_mapvote_selecting_map

| Field | Type | Description |
|-------|------|-------------|
| `count` | `byte` | Number of "ties" |
| `slot1` | `byte` |  |
| `slot2` | `byte` |  |
| `slot3` | `byte` |  |
| `slot4` | `byte` |  |
| `slot5` | `byte` |  |
| `slot6` | `byte` |  |
| `slot7` | `byte` |  |
| `slot8` | `byte` |  |
| `slot9` | `byte` |  |
| `slot10` | `byte` |  |

### entity_visible

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | The player who sees the entity |
| `subject` | `short` | Entindex of the entity they see |
| `classname` | `string` | Classname of the entity they see |
| `entityname` | `string` | name of the entity they see |

### game_end

a game ended

| Field | Type | Description |
|-------|------|-------------|
| `winner` | `byte` | winner team/user id |

### game_init

sent when a new game is started

*No fields — this event carries no additional data.*

### game_newmap

send when new map is completely loaded

| Field | Type | Description |
|-------|------|-------------|
| `mapname` | `string` | map name |

### game_start

a new game starts

| Field | Type | Description |
|-------|------|-------------|
| `roundslimit` | `long` | max round |
| `timelimit` | `long` | time limit |
| `fraglimit` | `long` | frag limit |
| `objective` | `string` | round objective |

### gameui_hidden

*No fields — this event carries no additional data.*

### instructor_server_hint_create

create a hint using data supplied entirely by the server/map. Intended for hints to smooth playtests before content is ready to make the hint unneccessary. NOT INTENDED AS A SHIPPABLE CRUTCH

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | user ID of the player that triggered the hint |
| `hint_name` | `string` | what to name the hint. For referencing it again later (e.g. a kill command for the hint instead of a timeout) |
| `hint_replace_key` | `string` | type name so that messages of the same type will replace each other |
| `hint_target` | `long` | entity id that the hint should display at |
| `hint_activator_userid` | `player_controller` | userid id of the activator |
| `hint_timeout` | `short` | how long in seconds until the hint automatically times out, 0 = never |
| `hint_icon_onscreen` | `string` | the hint icon to use when the hint is onscreen. e.g. "icon_alert_red" |
| `hint_icon_offscreen` | `string` | the hint icon to use when the hint is offscreen. e.g. "icon_alert" |
| `hint_caption` | `string` | the hint caption. e.g. "#ThisIsDangerous" |
| `hint_activator_caption` | `string` | the hint caption that only the activator sees e.g. "#YouPushedItGood" |
| `hint_color` | `string` | the hint color in "r,g,b" format where each component is 0-255 |
| `hint_icon_offset` | `float` | how far on the z axis to offset the hint from entity origin |
| `hint_range` | `float` | range before the hint is culled |
| `hint_flags` | `long` | hint flags |
| `hint_binding` | `string` | bindings to use when use_binding is the onscreen icon |
| `hint_gamepad_binding` | `string` | gamepad bindings to use when use_binding is the onscreen icon |
| `hint_allow_nodraw_target` | `bool` | if false, the hint will dissappear if the target entity is invisible |
| `hint_nooffscreen` | `bool` | if true, the hint will not show when outside the player view |
| `hint_forcecaption` | `bool` | if true, the hint caption will show even if the hint is occluded |
| `hint_local_player_only` | `bool` | if true, only the local player will see the hint |

### instructor_server_hint_stop

destroys a server/map created hint

| Field | Type | Description |
|-------|------|-------------|
| `hint_name` | `string` | The hint to stop. Will stop ALL hints with this name |

### inventory_updated

*No fields — this event carries no additional data.*

### player_chat

a public player chat

| Field | Type | Description |
|-------|------|-------------|
| `teamonly` | `bool` | true if team only chat |
| `userid` | `short` | chatting player |
| `text` | `string` | chat text |

### player_decal

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_pawn` |  |

### player_score

players scores changed

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | user ID on server |
| `kills` | `short` | # of kills |
| `deaths` | `short` | # of deaths |
| `score` | `short` | total game score |

### player_shoot

player shoot his weapon

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | user ID on server |
| `weapon` | `byte` | weapon ID |
| `mode` | `byte` | weapon mode |

### player_team

Fired when a player switches teams (T ↔ CT, or to/from Spectator).  `team` is the new team; `oldteam` is the previous. `disconnect=true` indicates the team change was caused by the player leaving rather than a deliberate switch.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player |
| `team` | `byte` | team id |
| `oldteam` | `byte` | old team id |
| `disconnect` | `bool` | team change because player disconnects |
| `silent` | `bool` |  |
| `isbot` | `bool` | true if player is a bot |

### read_game_titledata

read user titledata from profile

| Field | Type | Description |
|-------|------|-------------|
| `controllerId` | `short` | Controller id of user |

### reset_game_titledata

reset user titledata; do not automatically write profile

| Field | Type | Description |
|-------|------|-------------|
| `controllerId` | `short` | Controller id of user |

### round_announce_final

*No fields — this event carries no additional data.*

### round_announce_last_round_half

*No fields — this event carries no additional data.*

### round_announce_match_point

*No fields — this event carries no additional data.*

### round_announce_match_start

*No fields — this event carries no additional data.*

### round_announce_warmup

*No fields — this event carries no additional data.*

### round_end

Fired when a round concludes.  Carries the winning team (`winner`), the reason for the win (`reason`, see RoundEndReason table below), and a human-readable `message` string.


> 📝 The `winner` value uses the same team-number scheme as the `Team` constant in `well_known_constants.json` (2=T, 3=CT, 0/1 for draw / unassigned).  The `reason` byte enumerates win conditions: bomb detonation, defusal, time expiry, eliminations, surrender, etc. — full mapping is in `public/cstrike15_gameconstants.h` upstream.


| Field | Type | Description |
|-------|------|-------------|
| `winner` | `byte` | winner team/user i |
| `reason` | `byte` | reson why team won |
| `message` | `string` | end round message |
| `legacy` | `byte` | server-generated legacy value |

### round_end_upload_stats

*No fields — this event carries no additional data.*

### round_officially_ended

*No fields — this event carries no additional data.*

### round_time_warning

*No fields — this event carries no additional data.*

### survival_announce_phase

| Field | Type | Description |
|-------|------|-------------|
| `phase` | `short` | The phase # |

### ugc_file_download_finished

| Field | Type | Description |
|-------|------|-------------|
| `hcontent` | `uint64` | id of this specific content (may be image or map) |

### ugc_file_download_start

| Field | Type | Description |
|-------|------|-------------|
| `hcontent` | `uint64` | id of this specific content (may be image or map) |
| `published_file_id` | `uint64` | id of the associated content package |

### ugc_map_download_error

| Field | Type | Description |
|-------|------|-------------|
| `published_file_id` | `uint64` |  |
| `error_code` | `long` |  |

### ugc_map_info_received

| Field | Type | Description |
|-------|------|-------------|
| `published_file_id` | `uint64` |  |

### ugc_map_unsubscribed

| Field | Type | Description |
|-------|------|-------------|
| `published_file_id` | `uint64` |  |

### vote_cast

| Field | Type | Description |
|-------|------|-------------|
| `vote_option` | `byte` | which option the player voted on |
| `team` | `short` |  |
| `userid` | `player_controller` | player who voted |

### vote_changed

| Field | Type | Description |
|-------|------|-------------|
| `vote_option1` | `byte` |  |
| `vote_option2` | `byte` |  |
| `vote_option3` | `byte` |  |
| `vote_option4` | `byte` |  |
| `vote_option5` | `byte` |  |
| `potentialVotes` | `byte` |  |

### vote_ended

*No fields — this event carries no additional data.*

### vote_options

| Field | Type | Description |
|-------|------|-------------|
| `count` | `byte` | Number of options - up to MAX_VOTE_OPTIONS |
| `option1` | `string` |  |
| `option2` | `string` |  |
| `option3` | `string` |  |
| `option4` | `string` |  |
| `option5` | `string` |  |

### vote_started

| Field | Type | Description |
|-------|------|-------------|
| `issue` | `string` |  |
| `param1` | `string` |  |
| `team` | `byte` |  |
| `initiator` | `long` | entity id of the player who initiated the vote |

### warmup_end

*No fields — this event carries no additional data.*

### weaponhud_selection

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | Player who this event applies to |
| `mode` | `byte` | EWeaponHudSelectionMode (switch / pickup / drop) |
| `entindex` | `long` | Weapon entity index |

### write_game_titledata

write user titledata in profile

| Field | Type | Description |
|-------|------|-------------|
| `controllerId` | `short` | Controller id of user |

## CS2 (Counter-Strike) Events

*Source: `mod.gameevents`*

### achievement_earned_local

| Field | Type | Description |
|-------|------|-------------|
| `achievement` | `short` | achievement ID |
| `splitscreenplayer` | `short` | splitscreen ID |

### achievement_info_loaded

*No fields — this event carries no additional data.*

### ammo_pickup

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `item` | `string` | either a weapon such as 'tmp' or 'hegrenade', or an item such as 'nvgs' |
| `index` | `long` | the weapon entindex |

### ammo_refill

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `success` | `bool` |  |

### announce_phase_end

*No fields — this event carries no additional data.*

### bomb_abortdefuse

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who was defusing |

### bomb_abortplant

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who is planting the bomb |
| `site` | `short` | bombsite index |

### bomb_beep

Fired on each beep of an armed C4.  `entindex` references the `CPlantedC4`.  Cadence accelerates as detonation approaches.


| Field | Type | Description |
|-------|------|-------------|
| `entindex` | `long` | c4 entity |

### bomb_begindefuse

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who is defusing |
| `haskit` | `bool` |  |

### bomb_beginplant

Fired the moment a player begins the C4 plant animation.  The plant can still be interrupted (player damaged, switches weapon, leaves site); listen for `bomb_planted` to confirm completion.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who is planting the bomb |
| `site` | `short` | bombsite index |

### bomb_defused

Fired when the C4 is successfully defused.  `userid` is the defuser; `site` is the bombsite.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who defused the bomb |
| `site` | `short` | bombsite index |
| `c4` | `short` |  |

### bomb_dropped

Fired when a player carrying the C4 drops it (death, voluntary drop, disconnect).  `entindex` identifies the C4 world entity now sitting on the ground.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who dropped the bomb |
| `entindex` | `long` |  |

### bomb_exploded

Fired when the C4 detonates (defuse failed / timer expired). `userid` is the original planter (the actor who armed it), not the player nearest the explosion.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who planted the bomb |
| `site` | `short` | bombsite index |
| `c4` | `short` |  |

### bomb_pickup

Fired when a player picks up a dropped C4.  `userid` here is a `player_pawn` (not `player_controller_and_pawn`) — only the pawn half is meaningful.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_pawn` | player pawn who picked up the bomb |

### bomb_planted

Fired when the C4 is successfully armed.  `site` is the bombsite index (0=A, 1=B).  At this point a `CPlantedC4` entity exists and the 40-second countdown begins.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who planted the bomb |
| `site` | `short` | bombsite index |
| `c4` | `short` |  |

### bullet_damage

Fired on every firearm-projectile hit landed on a player.  Far richer than `player_hurt`: includes shot angles, aim-punch, inaccuracy components, penetration count, and lag-compensation type.  This is the right event for ballistics analysis and cheat-detection heuristics.


| Field | Type | Description |
|-------|------|-------------|
| `victim` | `player_controller_and_pawn` | player index who was hurt |
| `attacker` | `player_controller_and_pawn` | player index who attacked |
| `distance` | `float` | how far the bullet travelled before it hit the player |
| `damage_dir_x` | `float` | direction vector of the bullet |
| `damage_dir_y` | `float` | direction vector of the bullet |
| `damage_dir_z` | `float` | direction vector of the bullet |
| `num_penetrations` | `byte` | Count of solid surfaces the bullet passed through before hitting the victim. how many surfaces were penetrated |
| `no_scope` | `bool` | True if the attacker fired while not scoped on a sniper rifle. was the shooter noscoped? |
| `in_air` | `bool` | True if the attacker was airborne when the shot connected. was the shooter jumping? |
| `shoot_ang_x` | `float` | shoot angle x |
| `shoot_ang_y` | `float` | shoot angle y |
| `shoot_ang_z` | `float` | shoot angle z |
| `aim_punch_x` | `float` | aim punch x |
| `aim_punch_y` | `float` | aim punch y |
| `aim_punch_z` | `float` | aim punch z |
| `attack_tick_count` | `int` | attack tick |
| `attack_tick_frac` | `float` | attack frac |
| `render_tick_count` | `int` | render tick |
| `render_tick_frac` | `float` | render frac |
| `inaccuracy_total` | `float` | total inaccuracy |
| `inaccuracy_move` | `float` | move inaccuracy |
| `inaccuracy_air` | `float` | air inaccuracy |
| `recoil_index` | `float` | Position in the weapon's recoil pattern.  Float so the server-side prediction can interpolate. recoil index. Yes this is really a float. |
| `type` | `int` | lag compensation type |

### bullet_impact

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### buymenu_close

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### buymenu_open

*No fields — this event carries no additional data.*

### buytime_ended

*No fields — this event carries no additional data.*

### choppers_incoming_warning

| Field | Type | Description |
|-------|------|-------------|
| `global` | `bool` |  |

### client_disconnect

*No fields — this event carries no additional data.*

### clientside_reload_custom_econ

| Field | Type | Description |
|-------|------|-------------|
| `steamid` | `string` |  |

### cs_game_disconnected

*No fields — this event carries no additional data.*

### cs_intermission

*No fields — this event carries no additional data.*

### cs_match_end_restart

*No fields — this event carries no additional data.*

### cs_pre_restart

*No fields — this event carries no additional data.*

### cs_prev_next_spectator

| Field | Type | Description |
|-------|------|-------------|
| `next` | `bool` |  |

### cs_round_final_beep

Fired on the final pre-explosion beep of the planted C4.  Useful for demo-parsing tooling that wants to mark "bomb is about to detonate" without polling `m_flC4Blow` on the C4 entity.


*No fields — this event carries no additional data.*

### cs_round_start_beep

*No fields — this event carries no additional data.*

### cs_win_panel_match

*No fields — this event carries no additional data.*

### cs_win_panel_round

| Field | Type | Description |
|-------|------|-------------|
| `show_timer_defend` | `bool` |  |
| `show_timer_attack` | `bool` |  |
| `timer_time` | `short` |  |
| `final_event` | `byte` | define in cs_gamerules.h |
| `funfact_token` | `string` |  |
| `funfact_player` | `player_controller` |  |
| `funfact_data1` | `long` |  |
| `funfact_data2` | `long` |  |
| `funfact_data3` | `long` |  |

### decoy_detonate

Fired each time a decoy grenade fires its fake gunshot sound. Multiple per decoy lifetime.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### decoy_firing

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### decoy_started

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### defuser_dropped

| Field | Type | Description |
|-------|------|-------------|
| `entityid` | `long` | defuser's entity ID |

### defuser_pickup

| Field | Type | Description |
|-------|------|-------------|
| `entityid` | `long` | defuser's entity ID |
| `userid` | `player_controller_and_pawn` | player who picked up the defuser |

### door_moving

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entindex` | `long` |  |

### drone_above_roof

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `cargo` | `short` |  |

### drone_cargo_detached

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `cargo` | `short` |  |
| `delivered` | `bool` |  |

### drone_dispatched

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `priority` | `short` |  |
| `drone_dispatched` | `short` |  |

### dronegun_attack

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### dz_item_interaction

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player entindex |
| `subject` | `short` | crate entindex |
| `type` | `string` | type of crate (metal, wood, or paradrop) |

### enable_restart_voting

| Field | Type | Description |
|-------|------|-------------|
| `enable` | `bool` |  |

### enter_bombzone

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `hasbomb` | `bool` |  |
| `isplanted` | `bool` |  |

### enter_buyzone

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `canbuy` | `bool` |  |

### enter_rescue_zone

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### exit_bombzone

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `hasbomb` | `bool` |  |
| `isplanted` | `bool` |  |

### exit_buyzone

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `canbuy` | `bool` |  |

### exit_rescue_zone

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### firstbombs_incoming_warning

| Field | Type | Description |
|-------|------|-------------|
| `global` | `bool` |  |

### flashbang_detonate

Fired when a flashbang explodes.  Per-player flash duration is *not* on this event — read `m_flFlashDuration` / `m_flFlashMaxAlpha` on each affected `CCSPlayerPawn` instead.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### game_phase_changed

| Field | Type | Description |
|-------|------|-------------|
| `new_phase` | `short` |  |

### gg_killed_enemy

| Field | Type | Description |
|-------|------|-------------|
| `victimid` | `player_controller` | user ID who died |
| `attackerid` | `player_controller` | user ID who killed |
| `dominated` | `short` | did killer dominate victim with this kill |
| `revenge` | `short` | did killer get revenge on victim with this kill |
| `bonus` | `bool` | did killer kill with a bonus weapon? |

### grenade_bounce

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### grenade_thrown

Fired when a grenade leaves a player's hand.  Pair with the matching `<type>_detonate` event for landing/explosion location.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `weapon` | `string` | weapon name used |

### guardian_wave_restart

*No fields — this event carries no additional data.*

### hegrenade_detonate

Fired when an HE grenade explodes.  `x`/`y`/`z` is the world position of the detonation; `entityid` is the projectile's entity index (now removed).


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### hide_deathpanel

*No fields — this event carries no additional data.*

### hltv_changed_mode

| Field | Type | Description |
|-------|------|-------------|
| `oldmode` | `long` |  |
| `newmode` | `long` |  |
| `obs_target` | `long` |  |

### hostage_call_for_help

| Field | Type | Description |
|-------|------|-------------|
| `hostage` | `short` | hostage entity index |

### hostage_follows

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who touched the hostage |
| `hostage` | `short` | hostage entity index |

### hostage_hurt

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who hurt the hostage |
| `hostage` | `short` | hostage entity index |

### hostage_killed

Fired when a hostage entity is killed.  CTs incur a money penalty; this event is the canonical hook for that bookkeeping. `hostage` is the hostage entity index, not the hostage definition.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who killed the hostage |
| `hostage` | `short` | hostage entity index |

### hostage_rescued

Fired when a hostage reaches a rescue zone.  `site` is the rescue-zone index when a map carries more than one.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who rescued the hostage |
| `hostage` | `short` | hostage entity index |
| `site` | `short` | rescue site index |

### hostage_rescued_all

*No fields — this event carries no additional data.*

### hostage_stops_following

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who rescued the hostage |
| `hostage` | `short` | hostage entity index |

### inferno_expire

| Field | Type | Description |
|-------|------|-------------|
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### inferno_extinguish

| Field | Type | Description |
|-------|------|-------------|
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### inferno_startburn

| Field | Type | Description |
|-------|------|-------------|
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### inspect_weapon

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### item_equip

Fired when a player switches to a different weapon or gear slot. Carries flags describing the equipped item (silencer, tracers, paint kit) so demo tooling doesn't need a second lookup.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `item` | `string` | either a weapon such as 'tmp' or 'hegrenade', or an item such as 'nvgs' |
| `defindex` | `long` |  |
| `canzoom` | `bool` |  |
| `hassilencer` | `bool` |  |
| `issilenced` | `bool` |  |
| `hastracers` | `bool` |  |
| `weptype` | `short` |  |
| `ispainted` | `bool` |  |

### item_pickup

Fired when a player picks up a weapon or piece of gear.  `item` is the classname / definition string (`tmp`, `hegrenade`, `nvgs`, …); `defindex` is the Steam economy item definition index of the specific skin / version picked up.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `item` | `string` | either a weapon such as 'tmp' or 'hegrenade', or an item such as 'nvgs' |
| `silent` | `bool` |  |
| `defindex` | `long` |  |

### item_pickup_failed

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `item` | `string` |  |
| `reason` | `short` |  |
| `limit` | `short` |  |

### item_pickup_slerp

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `index` | `short` |  |
| `behavior` | `short` |  |

### item_purchase

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `team` | `short` |  |
| `loadout` | `short` |  |
| `weapon` | `string` |  |

### item_remove

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `item` | `string` | either a weapon such as 'tmp' or 'hegrenade', or an item such as 'nvgs' |
| `defindex` | `long` |  |

### jointeam_failed

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `reason` | `byte` | 0 = team_full |

### loot_crate_opened

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player entindex |
| `type` | `string` | type of crate (metal, wood, or paradrop) |

### loot_crate_visible

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player entindex |
| `subject` | `short` | crate entindex |
| `type` | `string` | type of crate (metal, wood, or paradrop) |

### match_end_conditions

| Field | Type | Description |
|-------|------|-------------|
| `frags` | `long` |  |
| `max_rounds` | `long` |  |
| `win_rounds` | `long` |  |
| `time` | `long` |  |

### material_default_complete

*No fields — this event carries no additional data.*

### mb_input_lock_cancel

*No fields — this event carries no additional data.*

### mb_input_lock_success

*No fields — this event carries no additional data.*

### molotov_detonate

Fired when a Molotov / Incendiary grenade ignites and begins laying fire.  The resulting `CInferno` entity carries the per-fragment damage volumes.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### nav_blocked

| Field | Type | Description |
|-------|------|-------------|
| `area` | `long` |  |
| `blocked` | `bool` |  |

### nav_generate

*No fields — this event carries no additional data.*

### nextlevel_changed

a game event, name may be 32 characters long

| Field | Type | Description |
|-------|------|-------------|
| `nextlevel` | `string` |  |
| `mapgroup` | `string` |  |
| `skirmishmode` | `string` |  |

### open_crate_instr

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player entindex |
| `subject` | `short` | crate entindex |
| `type` | `string` | type of crate (metal, wood, or paradrop) |

### other_death

| Field | Type | Description |
|-------|------|-------------|
| `otherid` | `short` | other entity ID who died |
| `othertype` | `string` | other entity type |
| `attacker` | `short` | user ID who killed |
| `weapon` | `string` | weapon name killer used |
| `weapon_itemid` | `string` | inventory item id of weapon killer used |
| `weapon_fauxitemid` | `string` | faux item id of weapon killer used |
| `weapon_originalowner_xuid` | `string` |  |
| `headshot` | `bool` | singals a headshot |
| `penetrated` | `short` | number of objects shot penetrated before killing target |
| `noscope` | `bool` | kill happened without a scope, used for death notice icon |
| `thrusmoke` | `bool` | hitscan weapon went through smoke grenade |
| `attackerblind` | `bool` | attacker was blind from flashbang |

### parachute_deploy

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### parachute_pickup

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### player_avenged_teammate

| Field | Type | Description |
|-------|------|-------------|
| `avenger_id` | `player_controller` |  |
| `avenged_player_id` | `player_controller` |  |

### player_blind

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `attacker` | `player_controller` | user ID who threw the flash |
| `entityid` | `short` | the flashbang going off |
| `blind_duration` | `float` |  |

### player_death

Fired when a player dies.  Carries `userid` (the victim) and `attacker`.  Detailed kill information (weapon, headshot, assister, penetration count, no-scope flag, distance) lives on the legacy `cs_gameevents.proto` user-message `CMsgSource1LegacyGameEvent` payload — extract those keys when parsing demos.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | user who died |
| `attacker` | `player_controller_and_pawn` | player who killed |
| `assister` | `player_controller_and_pawn` | player who assisted in the kill |
| `assistedflash` | `bool` | assister helped with a flash |
| `weapon` | `string` | weapon name killer used |
| `weapon_itemid` | `string` | inventory item id of weapon killer used |
| `weapon_fauxitemid` | `string` | faux item id of weapon killer used |
| `weapon_originalowner_xuid` | `string` |  |
| `headshot` | `bool` | singals a headshot |
| `dominated` | `short` | did killer dominate victim with this kill |
| `revenge` | `short` | did killer get revenge on victim with this kill |
| `wipe` | `short` | is the kill resulting in squad wipe |
| `penetrated` | `short` | number of objects shot penetrated before killing target |
| `noreplay` | `bool` | if replay data is unavailable, this will be present and set to false |
| `noscope` | `bool` | kill happened without a scope, used for death notice icon |
| `thrusmoke` | `bool` | hitscan weapon went through smoke grenade |
| `attackerblind` | `bool` | attacker was blind from flashbang |
| `distance` | `float` | distance to victim in meters |
| `dmg_health` | `short` | damage done to health |
| `dmg_armor` | `byte` | damage done to armor |
| `hitgroup` | `byte` | hitgroup that was damaged |
| `attackerinair` | `bool` | attacker was in midair |

### player_falldamage

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `damage` | `float` |  |

### player_footstep

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### player_given_c4

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | user ID who received the c4 |

### player_hurt

Fired when a player takes damage from any source.  The pre-CS2 `weapon` / `dmg_armor` / `dmg_health` / `hitgroup` fields were removed in CS2; for those, use `bullet_damage` (firearm damage) or correlate with the relevant grenade-detonation event.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player index who was hurt |
| `attacker` | `player_controller_and_pawn` | player index who attacked |
| `health` | `byte` | remaining health points |
| `armor` | `byte` | remaining armor points |
| `weapon` | `string` | weapon name attacker used, if not the world |
| `dmg_health` | `short` | damage done to health |
| `dmg_armor` | `byte` | damage done to armor |
| `hitgroup` | `byte` | hitgroup that was damaged |

### player_jump

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### player_ping

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |
| `urgent` | `bool` |  |

### player_ping_stop

| Field | Type | Description |
|-------|------|-------------|
| `entityid` | `short` |  |

### player_radio

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `slot` | `short` |  |

### player_reset_vote

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `vote` | `bool` |  |

### player_sound

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `radius` | `int` |  |
| `duration` | `float` |  |
| `step` | `bool` |  |

### player_spawned

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `inrestart` | `bool` | true if restart is pending |

### repost_xbox_achievements

| Field | Type | Description |
|-------|------|-------------|
| `splitscreenplayer` | `short` | splitscreen ID |

### round_end

Fired when a round concludes.  Carries the winning team (`winner`), the reason for the win (`reason`, see RoundEndReason table below), and a human-readable `message` string.


> 📝 The `winner` value uses the same team-number scheme as the `Team` constant in `well_known_constants.json` (2=T, 3=CT, 0/1 for draw / unassigned).  The `reason` byte enumerates win conditions: bomb detonation, defusal, time expiry, eliminations, surrender, etc. — full mapping is in `public/cstrike15_gameconstants.h` upstream.


| Field | Type | Description |
|-------|------|-------------|
| `winner` | `byte` | winner team/user i |
| `reason` | `byte` | reson why team won |
| `message` | `string` | end round message |
| `legacy` | `byte` | server-generated legacy value |
| `player_count` | `short` | total number of players alive at the end of round, used for statistics gathering, computed on the server in the event client is in replay when receiving this message |
| `nomusic` | `byte` | if set, don't play round end music, because action is still on-going |

### round_mvp

Fired at the end of a round to announce the MVP and the music kit that played.  `reason` enumerates why this player was selected (kills, defuse, plant, …); `musickitid` is the Steam item definition index of the MVP anthem.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `reason` | `short` |  |
| `value` | `long` |  |
| `musickitmvps` | `long` |  |
| `nomusic` | `byte` |  |
| `musickitid` | `long` |  |

### round_poststart

sent after all other round restart actions

*No fields — this event carries no additional data.*

### round_prestart

sent before all other round restart actions

*No fields — this event carries no additional data.*

### seasoncoin_levelup

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `category` | `short` |  |
| `rank` | `short` |  |

### sfuievent

| Field | Type | Description |
|-------|------|-------------|
| `action` | `string` |  |
| `data` | `string` |  |
| `slot` | `byte` |  |

### show_deathpanel

| Field | Type | Description |
|-------|------|-------------|
| `victim` | `player_controller_and_pawn` | endindex of the one who was killed |
| `killer` | `ehandle` | entindex of the killer entity |
| `killer_controller` | `player_controller` |  |
| `hits_taken` | `short` |  |
| `damage_taken` | `short` |  |
| `hits_given` | `short` |  |
| `damage_given` | `short` |  |

### show_survival_respawn_status

| Field | Type | Description |
|-------|------|-------------|
| `loc_token` | `string` |  |
| `duration` | `long` |  |
| `userid` | `player_controller_and_pawn` |  |

### silencer_detach

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### silencer_off

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### silencer_on

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### smoke_beacon_paradrop

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `paradrop` | `short` |  |

### smokegrenade_detonate

Fired when a smoke grenade pops and begins emitting smoke. Pair with `smokegrenade_expired` for the lifetime window.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### smokegrenade_expired

Fired when a smoke cloud fully dissipates.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### spec_mode_updated

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | entindex of the player |

### start_halftime

*No fields — this event carries no additional data.*

### start_vote

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `type` | `byte` |  |
| `vote_parameter` | `short` |  |

### survival_no_respawns_final

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### survival_no_respawns_warning

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### survival_paradrop_break

| Field | Type | Description |
|-------|------|-------------|
| `entityid` | `short` |  |

### survival_paradrop_spawn

| Field | Type | Description |
|-------|------|-------------|
| `entityid` | `short` |  |

### survival_teammate_respawn

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### switch_team

| Field | Type | Description |
|-------|------|-------------|
| `numPlayers` | `short` | number of active players on both T and CT |
| `numSpectators` | `short` | number of spectators |
| `avg_rank` | `short` | average rank of human players |
| `numTSlotsFree` | `short` |  |
| `numCTSlotsFree` | `short` |  |

### tagrenade_detonate

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### team_intro_end

*No fields — this event carries no additional data.*

### team_intro_start

*No fields — this event carries no additional data.*

### teamchange_pending

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `toteam` | `byte` |  |

### tournament_reward

| Field | Type | Description |
|-------|------|-------------|
| `defindex` | `long` |  |
| `totalrewards` | `long` |  |
| `accountid` | `long` |  |

### trial_time_expired

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player whose time has expired |

### update_matchmaking_stats

*No fields — this event carries no additional data.*

### vip_escaped

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player who was the VIP |

### vip_killed

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player who was the VIP |
| `attacker` | `player_controller` | user ID who killed the VIP |

### weapon_fire

Fired each time a player pulls the trigger and a shot is taken. `weapon` is the lowercase classname (`ak47`, `awp`, `knife`, `hegrenade`, …).  Use `bullet_damage` for the *hit* event counterpart.


| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `weapon` | `string` | weapon name used |
| `silenced` | `bool` | is weapon silenced |

### weapon_fire_on_empty

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `weapon` | `string` | weapon name used |

### weapon_reload

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### weapon_zoom

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### weapon_zoom_rifle

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### write_profile_data

*No fields — this event carries no additional data.*
