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

**Total events:** 288

| Source | Events | Description |
|--------|--------|-------------|
| `core.gameevents` | 94 | Core Engine Events |
| `game.gameevents` | 49 | Game Events |
| `mod.gameevents` | 145 | CS2 (Counter-Strike) Events |

## Event Index

| Event | Source | Fields | Description |
|-------|--------|--------|-------------|
| [server_spawn](#server_spawn) | `core.gameevents` | 10 | send once a server starts |
| [server_pre_shutdown](#server_pre_shutdown) | `core.gameevents` | 1 | server is about to be shut down |
| [server_shutdown](#server_shutdown) | `core.gameevents` | 1 | server shut down |
| [server_message](#server_message) | `core.gameevents` | 1 | a generic server message |
| [server_cvar](#server_cvar) | `core.gameevents` | 2 | a server console var has changed |
| [player_activate](#player_activate) | `core.gameevents` | 1 |  |
| [player_connect_full](#player_connect_full) | `core.gameevents` | 1 | player has sent final message in the connection sequence |
| [player_full_update](#player_full_update) | `core.gameevents` | 2 |  |
| [player_connect](#player_connect) | `core.gameevents` | 5 | a new client connected |
| [player_disconnect](#player_disconnect) | `core.gameevents` | 6 | a client was disconnected |
| [player_info](#player_info) | `core.gameevents` | 4 | a player changed his name |
| [player_spawn](#player_spawn) | `core.gameevents` | 1 | player spawned in game |
| [player_team](#player_team) | `core.gameevents` | 7 |  |
| [local_player_team](#local_player_team) | `core.gameevents` | 0 |  |
| [local_player_controller_team](#local_player_controller_team) | `core.gameevents` | 0 |  |
| [player_changename](#player_changename) | `core.gameevents` | 3 |  |
| [player_hurt](#player_hurt) | `core.gameevents` | 3 |  |
| [player_chat](#player_chat) | `core.gameevents` | 4 | a public player chat |
| [local_player_pawn_changed](#local_player_pawn_changed) | `core.gameevents` | 0 |  |
| [teamplay_broadcast_audio](#teamplay_broadcast_audio) | `core.gameevents` | 2 | emits a sound to everyone on a team |
| [finale_start](#finale_start) | `core.gameevents` | 1 |  |
| [player_stats_updated](#player_stats_updated) | `core.gameevents` | 1 |  |
| [user_data_downloaded](#user_data_downloaded) | `core.gameevents` | 0 | fired when achievements/stats are downloaded from Steam or XBox Live |
| [ragdoll_dissolved](#ragdoll_dissolved) | `core.gameevents` | 1 |  |
| [team_info](#team_info) | `core.gameevents` | 2 | info about team |
| [team_score](#team_score) | `core.gameevents` | 2 | team score changed |
| [hltv_cameraman](#hltv_cameraman) | `core.gameevents` | 1 | a spectator/player is a cameraman |
| [hltv_chase](#hltv_chase) | `core.gameevents` | 7 | shot of a single entity |
| [hltv_rank_camera](#hltv_rank_camera) | `core.gameevents` | 3 | a camera ranking |
| [hltv_rank_entity](#hltv_rank_entity) | `core.gameevents` | 3 | an entity ranking |
| [hltv_fixed](#hltv_fixed) | `core.gameevents` | 8 | show from fixed view |
| [hltv_message](#hltv_message) | `core.gameevents` | 1 | a HLTV message send by moderators |
| [hltv_status](#hltv_status) | `core.gameevents` | 4 | general HLTV status |
| [hltv_title](#hltv_title) | `core.gameevents` | 1 |  |
| [hltv_chat](#hltv_chat) | `core.gameevents` | 2 | a HLTV chat msg sent by spectators |
| [hltv_versioninfo](#hltv_versioninfo) | `core.gameevents` | 1 |  |
| [hltv_replay](#hltv_replay) | `core.gameevents` | 2 |  |
| [hltv_replay_status](#hltv_replay_status) | `core.gameevents` | 1 |  |
| [demo_start](#demo_start) | `core.gameevents` | 3 |  |
| [demo_stop](#demo_stop) | `core.gameevents` | 0 |  |
| [demo_skip](#demo_skip) | `core.gameevents` | 4 |  |
| [map_shutdown](#map_shutdown) | `core.gameevents` | 0 |  |
| [map_transition](#map_transition) | `core.gameevents` | 0 |  |
| [hostname_changed](#hostname_changed) | `core.gameevents` | 1 |  |
| [difficulty_changed](#difficulty_changed) | `core.gameevents` | 3 |  |
| [game_message](#game_message) | `core.gameevents` | 2 | a message send by game logic to everyone |
| [game_newmap](#game_newmap) | `core.gameevents` | 2 | send when new map is completely loaded |
| [round_start](#round_start) | `core.gameevents` | 3 |  |
| [round_end](#round_end) | `core.gameevents` | 4 |  |
| [round_start_pre_entity](#round_start_pre_entity) | `core.gameevents` | 0 |  |
| [round_start_post_nav](#round_start_post_nav) | `core.gameevents` | 0 |  |
| [round_freeze_end](#round_freeze_end) | `core.gameevents` | 0 |  |
| [teamplay_round_start](#teamplay_round_start) | `core.gameevents` | 1 | round restart |
| [player_death](#player_death) | `core.gameevents` | 2 | a game event, name may be 32 charaters long |
| [player_footstep](#player_footstep) | `core.gameevents` | 1 |  |
| [player_hintmessage](#player_hintmessage) | `core.gameevents` | 1 |  |
| [break_breakable](#break_breakable) | `core.gameevents` | 3 |  |
| [broken_breakable](#broken_breakable) | `core.gameevents` | 3 |  |
| [break_prop](#break_prop) | `core.gameevents` | 5 |  |
| [entity_killed](#entity_killed) | `core.gameevents` | 4 |  |
| [door_close](#door_close) | `core.gameevents` | 2 |  |
| [vote_started](#vote_started) | `core.gameevents` | 5 |  |
| [vote_failed](#vote_failed) | `core.gameevents` | 1 |  |
| [vote_passed](#vote_passed) | `core.gameevents` | 3 |  |
| [vote_changed](#vote_changed) | `core.gameevents` | 3 |  |
| [vote_cast_yes](#vote_cast_yes) | `core.gameevents` | 2 |  |
| [vote_cast_no](#vote_cast_no) | `core.gameevents` | 2 |  |
| [achievement_event](#achievement_event) | `core.gameevents` | 3 |  |
| [achievement_earned](#achievement_earned) | `core.gameevents` | 2 |  |
| [achievement_write_failed](#achievement_write_failed) | `core.gameevents` | 0 |  |
| [bonus_updated](#bonus_updated) | `core.gameevents` | 4 |  |
| [spec_target_updated](#spec_target_updated) | `core.gameevents` | 2 |  |
| [spec_mode_updated](#spec_mode_updated) | `core.gameevents` | 1 |  |
| [entity_visible](#entity_visible) | `core.gameevents` | 4 |  |
| [gameinstructor_draw](#gameinstructor_draw) | `core.gameevents` | 0 |  |
| [gameinstructor_nodraw](#gameinstructor_nodraw) | `core.gameevents` | 0 |  |
| [flare_ignite_npc](#flare_ignite_npc) | `core.gameevents` | 1 |  |
| [helicopter_grenade_punt_miss](#helicopter_grenade_punt_miss) | `core.gameevents` | 0 |  |
| [physgun_pickup](#physgun_pickup) | `core.gameevents` | 1 |  |
| [inventory_updated](#inventory_updated) | `core.gameevents` | 2 |  |
| [cart_updated](#cart_updated) | `core.gameevents` | 0 |  |
| [store_pricesheet_updated](#store_pricesheet_updated) | `core.gameevents` | 0 |  |
| [item_schema_initialized](#item_schema_initialized) | `core.gameevents` | 0 |  |
| [drop_rate_modified](#drop_rate_modified) | `core.gameevents` | 0 |  |
| [event_ticket_modified](#event_ticket_modified) | `core.gameevents` | 0 |  |
| [gc_connected](#gc_connected) | `core.gameevents` | 0 |  |
| [instructor_start_lesson](#instructor_start_lesson) | `core.gameevents` | 6 |  |
| [instructor_close_lesson](#instructor_close_lesson) | `core.gameevents` | 2 |  |
| [instructor_server_hint_create](#instructor_server_hint_create) | `core.gameevents` | 27 | create a hint using data supplied entirely by the server/map. Intended for hints to smooth playtests before content is ready to make the hint unneccessary. NOT INTENDED AS A SHIPPABLE CRUTCH |
| [instructor_server_hint_stop](#instructor_server_hint_stop) | `core.gameevents` | 2 | destroys a server/map created hint |
| [set_instructor_group_enabled](#set_instructor_group_enabled) | `core.gameevents` | 2 |  |
| [clientside_lesson_closed](#clientside_lesson_closed) | `core.gameevents` | 1 |  |
| [dynamic_shadow_light_changed](#dynamic_shadow_light_changed) | `core.gameevents` | 0 |  |
| [bot_takeover](#bot_takeover) | `core.gameevents` | 5 |  |
| [player_team](#player_team) | `game.gameevents` | 6 | player change his team |
| [player_chat](#player_chat) | `game.gameevents` | 3 | a public player chat |
| [player_score](#player_score) | `game.gameevents` | 4 | players scores changed |
| [player_shoot](#player_shoot) | `game.gameevents` | 3 | player shoot his weapon |
| [game_init](#game_init) | `game.gameevents` | 0 | sent when a new game is started |
| [game_newmap](#game_newmap) | `game.gameevents` | 1 | send when new map is completely loaded |
| [game_start](#game_start) | `game.gameevents` | 4 | a new game starts |
| [game_end](#game_end) | `game.gameevents` | 1 | a game ended |
| [round_announce_match_point](#round_announce_match_point) | `game.gameevents` | 0 |  |
| [round_announce_final](#round_announce_final) | `game.gameevents` | 0 |  |
| [round_announce_last_round_half](#round_announce_last_round_half) | `game.gameevents` | 0 |  |
| [round_announce_match_start](#round_announce_match_start) | `game.gameevents` | 0 |  |
| [round_announce_warmup](#round_announce_warmup) | `game.gameevents` | 0 |  |
| [warmup_end](#warmup_end) | `game.gameevents` | 0 |  |
| [round_end](#round_end) | `game.gameevents` | 4 |  |
| [round_end_upload_stats](#round_end_upload_stats) | `game.gameevents` | 0 |  |
| [round_officially_ended](#round_officially_ended) | `game.gameevents` | 0 |  |
| [round_time_warning](#round_time_warning) | `game.gameevents` | 0 |  |
| [ugc_map_info_received](#ugc_map_info_received) | `game.gameevents` | 1 |  |
| [ugc_map_unsubscribed](#ugc_map_unsubscribed) | `game.gameevents` | 1 |  |
| [ugc_map_download_error](#ugc_map_download_error) | `game.gameevents` | 2 |  |
| [ugc_file_download_finished](#ugc_file_download_finished) | `game.gameevents` | 1 |  |
| [ugc_file_download_start](#ugc_file_download_start) | `game.gameevents` | 2 |  |
| [begin_new_match](#begin_new_match) | `game.gameevents` | 0 |  |
| [dm_bonus_weapon_start](#dm_bonus_weapon_start) | `game.gameevents` | 2 |  |
| [survival_announce_phase](#survival_announce_phase) | `game.gameevents` | 1 |  |
| [break_prop](#break_prop) | `game.gameevents` | 2 |  |
| [player_decal](#player_decal) | `game.gameevents` | 1 |  |
| [entity_visible](#entity_visible) | `game.gameevents` | 4 |  |
| [instructor_server_hint_create](#instructor_server_hint_create) | `game.gameevents` | 20 | create a hint using data supplied entirely by the server/map. Intended for hints to smooth playtests before content is ready to make the hint unneccessary. NOT INTENDED AS A SHIPPABLE CRUTCH |
| [instructor_server_hint_stop](#instructor_server_hint_stop) | `game.gameevents` | 1 | destroys a server/map created hint |
| [read_game_titledata](#read_game_titledata) | `game.gameevents` | 1 | read user titledata from profile |
| [write_game_titledata](#write_game_titledata) | `game.gameevents` | 1 | write user titledata in profile |
| [reset_game_titledata](#reset_game_titledata) | `game.gameevents` | 1 | reset user titledata; do not automatically write profile |
| [weaponhud_selection](#weaponhud_selection) | `game.gameevents` | 3 |  |
| [vote_ended](#vote_ended) | `game.gameevents` | 0 |  |
| [vote_started](#vote_started) | `game.gameevents` | 4 |  |
| [vote_changed](#vote_changed) | `game.gameevents` | 6 |  |
| [vote_cast](#vote_cast) | `game.gameevents` | 3 |  |
| [vote_options](#vote_options) | `game.gameevents` | 6 |  |
| [endmatch_mapvote_selecting_map](#endmatch_mapvote_selecting_map) | `game.gameevents` | 11 |  |
| [endmatch_cmm_start_reveal_items](#endmatch_cmm_start_reveal_items) | `game.gameevents` | 0 |  |
| [inventory_updated](#inventory_updated) | `game.gameevents` | 0 |  |
| [client_loadout_changed](#client_loadout_changed) | `game.gameevents` | 0 |  |
| [add_player_sonar_icon](#add_player_sonar_icon) | `game.gameevents` | 4 |  |
| [door_open](#door_open) | `game.gameevents` | 2 |  |
| [door_closed](#door_closed) | `game.gameevents` | 2 |  |
| [door_break](#door_break) | `game.gameevents` | 2 |  |
| [add_bullet_hit_marker](#add_bullet_hit_marker) | `game.gameevents` | 12 |  |
| [player_death](#player_death) | `mod.gameevents` | 22 | a game event, name may be 32 characters long |
| [other_death](#other_death) | `mod.gameevents` | 12 |  |
| [player_hurt](#player_hurt) | `mod.gameevents` | 8 |  |
| [bullet_damage](#bullet_damage) | `mod.gameevents` | 24 |  |
| [item_purchase](#item_purchase) | `mod.gameevents` | 4 |  |
| [bomb_beginplant](#bomb_beginplant) | `mod.gameevents` | 2 |  |
| [bomb_abortplant](#bomb_abortplant) | `mod.gameevents` | 2 |  |
| [bomb_planted](#bomb_planted) | `mod.gameevents` | 2 |  |
| [bomb_defused](#bomb_defused) | `mod.gameevents` | 2 |  |
| [bomb_exploded](#bomb_exploded) | `mod.gameevents` | 2 |  |
| [bomb_dropped](#bomb_dropped) | `mod.gameevents` | 2 |  |
| [bomb_pickup](#bomb_pickup) | `mod.gameevents` | 1 |  |
| [defuser_dropped](#defuser_dropped) | `mod.gameevents` | 1 |  |
| [defuser_pickup](#defuser_pickup) | `mod.gameevents` | 2 |  |
| [announce_phase_end](#announce_phase_end) | `mod.gameevents` | 0 |  |
| [cs_intermission](#cs_intermission) | `mod.gameevents` | 0 |  |
| [bomb_begindefuse](#bomb_begindefuse) | `mod.gameevents` | 2 |  |
| [bomb_abortdefuse](#bomb_abortdefuse) | `mod.gameevents` | 1 |  |
| [hostage_follows](#hostage_follows) | `mod.gameevents` | 2 |  |
| [hostage_hurt](#hostage_hurt) | `mod.gameevents` | 2 |  |
| [hostage_killed](#hostage_killed) | `mod.gameevents` | 2 |  |
| [hostage_rescued](#hostage_rescued) | `mod.gameevents` | 3 |  |
| [hostage_stops_following](#hostage_stops_following) | `mod.gameevents` | 2 |  |
| [hostage_rescued_all](#hostage_rescued_all) | `mod.gameevents` | 0 |  |
| [hostage_call_for_help](#hostage_call_for_help) | `mod.gameevents` | 1 |  |
| [vip_escaped](#vip_escaped) | `mod.gameevents` | 1 |  |
| [vip_killed](#vip_killed) | `mod.gameevents` | 2 |  |
| [player_radio](#player_radio) | `mod.gameevents` | 2 |  |
| [bomb_beep](#bomb_beep) | `mod.gameevents` | 1 |  |
| [weapon_fire](#weapon_fire) | `mod.gameevents` | 3 |  |
| [weapon_fire_on_empty](#weapon_fire_on_empty) | `mod.gameevents` | 2 |  |
| [grenade_thrown](#grenade_thrown) | `mod.gameevents` | 2 |  |
| [weapon_reload](#weapon_reload) | `mod.gameevents` | 1 |  |
| [weapon_zoom](#weapon_zoom) | `mod.gameevents` | 1 |  |
| [silencer_detach](#silencer_detach) | `mod.gameevents` | 1 |  |
| [inspect_weapon](#inspect_weapon) | `mod.gameevents` | 1 |  |
| [weapon_zoom_rifle](#weapon_zoom_rifle) | `mod.gameevents` | 1 |  |
| [player_spawned](#player_spawned) | `mod.gameevents` | 2 |  |
| [item_pickup](#item_pickup) | `mod.gameevents` | 4 |  |
| [item_pickup_slerp](#item_pickup_slerp) | `mod.gameevents` | 3 |  |
| [item_pickup_failed](#item_pickup_failed) | `mod.gameevents` | 4 |  |
| [item_remove](#item_remove) | `mod.gameevents` | 3 |  |
| [ammo_pickup](#ammo_pickup) | `mod.gameevents` | 3 |  |
| [item_equip](#item_equip) | `mod.gameevents` | 9 |  |
| [enter_buyzone](#enter_buyzone) | `mod.gameevents` | 2 |  |
| [exit_buyzone](#exit_buyzone) | `mod.gameevents` | 2 |  |
| [buytime_ended](#buytime_ended) | `mod.gameevents` | 0 |  |
| [enter_bombzone](#enter_bombzone) | `mod.gameevents` | 3 |  |
| [exit_bombzone](#exit_bombzone) | `mod.gameevents` | 3 |  |
| [enter_rescue_zone](#enter_rescue_zone) | `mod.gameevents` | 1 |  |
| [exit_rescue_zone](#exit_rescue_zone) | `mod.gameevents` | 1 |  |
| [silencer_off](#silencer_off) | `mod.gameevents` | 1 |  |
| [silencer_on](#silencer_on) | `mod.gameevents` | 1 |  |
| [buymenu_open](#buymenu_open) | `mod.gameevents` | 0 |  |
| [buymenu_close](#buymenu_close) | `mod.gameevents` | 1 |  |
| [round_prestart](#round_prestart) | `mod.gameevents` | 0 | sent before all other round restart actions |
| [round_poststart](#round_poststart) | `mod.gameevents` | 0 | sent after all other round restart actions |
| [round_end](#round_end) | `mod.gameevents` | 6 |  |
| [grenade_bounce](#grenade_bounce) | `mod.gameevents` | 1 |  |
| [hegrenade_detonate](#hegrenade_detonate) | `mod.gameevents` | 5 |  |
| [flashbang_detonate](#flashbang_detonate) | `mod.gameevents` | 5 |  |
| [smokegrenade_detonate](#smokegrenade_detonate) | `mod.gameevents` | 5 |  |
| [smokegrenade_expired](#smokegrenade_expired) | `mod.gameevents` | 5 |  |
| [molotov_detonate](#molotov_detonate) | `mod.gameevents` | 4 |  |
| [decoy_detonate](#decoy_detonate) | `mod.gameevents` | 5 |  |
| [decoy_started](#decoy_started) | `mod.gameevents` | 5 |  |
| [tagrenade_detonate](#tagrenade_detonate) | `mod.gameevents` | 5 |  |
| [inferno_startburn](#inferno_startburn) | `mod.gameevents` | 4 |  |
| [inferno_expire](#inferno_expire) | `mod.gameevents` | 4 |  |
| [inferno_extinguish](#inferno_extinguish) | `mod.gameevents` | 4 |  |
| [decoy_firing](#decoy_firing) | `mod.gameevents` | 5 |  |
| [bullet_impact](#bullet_impact) | `mod.gameevents` | 4 |  |
| [player_footstep](#player_footstep) | `mod.gameevents` | 1 |  |
| [player_jump](#player_jump) | `mod.gameevents` | 1 |  |
| [player_blind](#player_blind) | `mod.gameevents` | 4 |  |
| [player_falldamage](#player_falldamage) | `mod.gameevents` | 2 |  |
| [door_moving](#door_moving) | `mod.gameevents` | 2 |  |
| [mb_input_lock_success](#mb_input_lock_success) | `mod.gameevents` | 0 |  |
| [mb_input_lock_cancel](#mb_input_lock_cancel) | `mod.gameevents` | 0 |  |
| [nav_blocked](#nav_blocked) | `mod.gameevents` | 2 |  |
| [nav_generate](#nav_generate) | `mod.gameevents` | 0 |  |
| [achievement_info_loaded](#achievement_info_loaded) | `mod.gameevents` | 0 |  |
| [spec_mode_updated](#spec_mode_updated) | `mod.gameevents` | 1 |  |
| [hltv_changed_mode](#hltv_changed_mode) | `mod.gameevents` | 3 |  |
| [cs_game_disconnected](#cs_game_disconnected) | `mod.gameevents` | 0 |  |
| [cs_round_final_beep](#cs_round_final_beep) | `mod.gameevents` | 0 |  |
| [cs_round_start_beep](#cs_round_start_beep) | `mod.gameevents` | 0 |  |
| [cs_win_panel_round](#cs_win_panel_round) | `mod.gameevents` | 9 |  |
| [cs_win_panel_match](#cs_win_panel_match) | `mod.gameevents` | 0 |  |
| [cs_match_end_restart](#cs_match_end_restart) | `mod.gameevents` | 0 |  |
| [cs_pre_restart](#cs_pre_restart) | `mod.gameevents` | 0 |  |
| [show_deathpanel](#show_deathpanel) | `mod.gameevents` | 7 |  |
| [hide_deathpanel](#hide_deathpanel) | `mod.gameevents` | 0 |  |
| [player_avenged_teammate](#player_avenged_teammate) | `mod.gameevents` | 2 |  |
| [achievement_earned_local](#achievement_earned_local) | `mod.gameevents` | 2 |  |
| [repost_xbox_achievements](#repost_xbox_achievements) | `mod.gameevents` | 1 |  |
| [match_end_conditions](#match_end_conditions) | `mod.gameevents` | 4 |  |
| [round_mvp](#round_mvp) | `mod.gameevents` | 6 |  |
| [show_survival_respawn_status](#show_survival_respawn_status) | `mod.gameevents` | 3 |  |
| [client_disconnect](#client_disconnect) | `mod.gameevents` | 0 |  |
| [gg_killed_enemy](#gg_killed_enemy) | `mod.gameevents` | 5 |  |
| [switch_team](#switch_team) | `mod.gameevents` | 5 |  |
| [write_profile_data](#write_profile_data) | `mod.gameevents` | 0 |  |
| [trial_time_expired](#trial_time_expired) | `mod.gameevents` | 1 |  |
| [update_matchmaking_stats](#update_matchmaking_stats) | `mod.gameevents` | 0 |  |
| [player_reset_vote](#player_reset_vote) | `mod.gameevents` | 2 |  |
| [enable_restart_voting](#enable_restart_voting) | `mod.gameevents` | 1 |  |
| [sfuievent](#sfuievent) | `mod.gameevents` | 3 |  |
| [start_vote](#start_vote) | `mod.gameevents` | 3 |  |
| [player_given_c4](#player_given_c4) | `mod.gameevents` | 1 |  |
| [jointeam_failed](#jointeam_failed) | `mod.gameevents` | 2 |  |
| [teamchange_pending](#teamchange_pending) | `mod.gameevents` | 2 |  |
| [material_default_complete](#material_default_complete) | `mod.gameevents` | 0 |  |
| [cs_prev_next_spectator](#cs_prev_next_spectator) | `mod.gameevents` | 1 |  |
| [nextlevel_changed](#nextlevel_changed) | `mod.gameevents` | 3 | a game event, name may be 32 characters long |
| [seasoncoin_levelup](#seasoncoin_levelup) | `mod.gameevents` | 3 |  |
| [tournament_reward](#tournament_reward) | `mod.gameevents` | 3 |  |
| [start_halftime](#start_halftime) | `mod.gameevents` | 0 |  |
| [ammo_refill](#ammo_refill) | `mod.gameevents` | 2 |  |
| [parachute_pickup](#parachute_pickup) | `mod.gameevents` | 1 |  |
| [parachute_deploy](#parachute_deploy) | `mod.gameevents` | 1 |  |
| [dronegun_attack](#dronegun_attack) | `mod.gameevents` | 1 |  |
| [drone_dispatched](#drone_dispatched) | `mod.gameevents` | 3 |  |
| [loot_crate_visible](#loot_crate_visible) | `mod.gameevents` | 3 |  |
| [loot_crate_opened](#loot_crate_opened) | `mod.gameevents` | 2 |  |
| [open_crate_instr](#open_crate_instr) | `mod.gameevents` | 3 |  |
| [smoke_beacon_paradrop](#smoke_beacon_paradrop) | `mod.gameevents` | 2 |  |
| [survival_paradrop_spawn](#survival_paradrop_spawn) | `mod.gameevents` | 1 |  |
| [survival_paradrop_break](#survival_paradrop_break) | `mod.gameevents` | 1 |  |
| [drone_cargo_detached](#drone_cargo_detached) | `mod.gameevents` | 3 |  |
| [drone_above_roof](#drone_above_roof) | `mod.gameevents` | 2 |  |
| [choppers_incoming_warning](#choppers_incoming_warning) | `mod.gameevents` | 1 |  |
| [firstbombs_incoming_warning](#firstbombs_incoming_warning) | `mod.gameevents` | 1 |  |
| [dz_item_interaction](#dz_item_interaction) | `mod.gameevents` | 3 |  |
| [survival_teammate_respawn](#survival_teammate_respawn) | `mod.gameevents` | 1 |  |
| [survival_no_respawns_warning](#survival_no_respawns_warning) | `mod.gameevents` | 1 |  |
| [survival_no_respawns_final](#survival_no_respawns_final) | `mod.gameevents` | 1 |  |
| [player_ping](#player_ping) | `mod.gameevents` | 6 |  |
| [player_ping_stop](#player_ping_stop) | `mod.gameevents` | 1 |  |
| [player_sound](#player_sound) | `mod.gameevents` | 4 |  |
| [guardian_wave_restart](#guardian_wave_restart) | `mod.gameevents` | 0 |  |
| [team_intro_start](#team_intro_start) | `mod.gameevents` | 0 |  |
| [team_intro_end](#team_intro_end) | `mod.gameevents` | 0 |  |
| [game_phase_changed](#game_phase_changed) | `mod.gameevents` | 1 |  |
| [clientside_reload_custom_econ](#clientside_reload_custom_econ) | `mod.gameevents` | 1 |  |

---

## Core Engine Events

*Source: `core.gameevents`*

### server_spawn

send once a server starts

| Field | Type | Description |
|-------|------|-------------|
| `hostname` | `string` | public host name |
| `address` | `string` | hostame, IP or DNS name |
| `port` | `short` | server port |
| `game` | `string` | game dir |
| `mapname` | `string` | map name |
| `addonname` | `string` | addon name |
| `maxplayers` | `long` | max players |
| `os` | `string` | WIN32, LINUX |
| `dedicated` | `bool` | true if dedicated server |
| `password` | `bool` | true if password protected |

### server_pre_shutdown

server is about to be shut down

| Field | Type | Description |
|-------|------|-------------|
| `reason` | `string` | reason why server is about to be shut down |

### server_shutdown

server shut down

| Field | Type | Description |
|-------|------|-------------|
| `reason` | `string` | reason why server was shut down |

### server_message

a generic server message

| Field | Type | Description |
|-------|------|-------------|
| `text` | `string` | the message text |

### server_cvar

a server console var has changed

| Field | Type | Description |
|-------|------|-------------|
| `cvarname` | `string` | cvar name, eg "mp_roundtime" |
| `cvarvalue` | `string` | new cvar value |

### player_activate

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | user ID on server |

### player_connect_full

player has sent final message in the connection sequence

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | user ID on server (unique on server) |

### player_full_update

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | user ID on server |
| `count` | `short` | Number of this full update |

### player_connect

a new client connected

| Field | Type | Description |
|-------|------|-------------|
| `name` | `string` | player name |
| `userid` | `player_controller` | user ID on server (unique on server) |
| `networkid` | `string` | player network (i.e steam) id |
| `xuid` | `uint64` | steam id |
| `bot` | `bool` |  |

### player_disconnect

a client was disconnected

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | user ID on server |
| `reason` | `short` | see networkdisconnect enum protobuf |
| `name` | `string` | player name |
| `networkid` | `string` | player network (i.e steam) id |
| `xuid` | `uint64` | steam id |
| `PlayerID` | `short` |  |

### player_info

a player changed his name

| Field | Type | Description |
|-------|------|-------------|
| `name` | `string` | player name |
| `userid` | `player_controller` | user ID on server (unique on server) |
| `steamid` | `uint64` | player network (i.e steam) id |
| `bot` | `bool` | true if player is a AI bot |

### player_spawn

player spawned in game

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### player_team

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `team` | `byte` | team id |
| `oldteam` | `byte` | old team id |
| `disconnect` | `bool` | team change because player disconnects |
| `silent` | `bool` |  |
| `name` | `string` |  |
| `isbot` | `bool` |  |

### local_player_team

*No fields — this event carries no additional data.*

### local_player_controller_team

*No fields — this event carries no additional data.*

### player_changename

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | user ID on server |
| `oldname` | `string` | players old (current) name |
| `newname` | `string` | players new name |

### player_hurt

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who was hurt |
| `attacker` | `player_controller_and_pawn` | player who attacked |
| `health` | `byte` | remaining health points |

### player_chat

a public player chat

| Field | Type | Description |
|-------|------|-------------|
| `teamonly` | `bool` | true if team only chat |
| `userid` | `player_controller` | chatting player |
| `playerid` | `short` | chatting player ID |
| `text` | `string` | chat text |

### local_player_pawn_changed

*No fields — this event carries no additional data.*

### teamplay_broadcast_audio

emits a sound to everyone on a team

| Field | Type | Description |
|-------|------|-------------|
| `team` | `byte` | unique team id |
| `sound` | `string` | name of the sound to emit |

### finale_start

| Field | Type | Description |
|-------|------|-------------|
| `rushes` | `short` |  |

### player_stats_updated

| Field | Type | Description |
|-------|------|-------------|
| `forceupload` | `bool` |  |

### user_data_downloaded

fired when achievements/stats are downloaded from Steam or XBox Live

*No fields — this event carries no additional data.*

### ragdoll_dissolved

| Field | Type | Description |
|-------|------|-------------|
| `entindex` | `long` |  |

### team_info

info about team

| Field | Type | Description |
|-------|------|-------------|
| `teamid` | `byte` | unique team id |
| `teamname` | `string` | team name eg "Team Blue" |

### team_score

team score changed

| Field | Type | Description |
|-------|------|-------------|
| `teamid` | `byte` | team id |
| `score` | `short` | total team score |

### hltv_cameraman

a spectator/player is a cameraman

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | camera man entity index |

### hltv_chase

shot of a single entity

| Field | Type | Description |
|-------|------|-------------|
| `target1` | `player_controller` | primary traget index |
| `target2` | `player_controller` | secondary traget index or 0 |
| `distance` | `short` | camera distance |
| `theta` | `short` | view angle horizontal |
| `phi` | `short` | view angle vertical |
| `inertia` | `byte` | camera inertia |
| `ineye` | `byte` | diretcor suggests to show ineye |

### hltv_rank_camera

a camera ranking

| Field | Type | Description |
|-------|------|-------------|
| `index` | `byte` | fixed camera index |
| `rank` | `float` | ranking, how interesting is this camera view |
| `target` | `player_controller` | best/closest target entity |

### hltv_rank_entity

an entity ranking

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player slot |
| `rank` | `float` | ranking, how interesting is this entity to view |
| `target` | `player_controller` | best/closest target entity |

### hltv_fixed

show from fixed view

| Field | Type | Description |
|-------|------|-------------|
| `posx` | `long` | camera position in world |
| `posy` | `long` |  |
| `posz` | `long` |  |
| `theta` | `short` | camera angles |
| `phi` | `short` |  |
| `offset` | `short` |  |
| `fov` | `float` |  |
| `target` | `player_controller` | follow this player |

### hltv_message

a HLTV message send by moderators

| Field | Type | Description |
|-------|------|-------------|
| `text` | `string` |  |

### hltv_status

general HLTV status

| Field | Type | Description |
|-------|------|-------------|
| `clients` | `long` | number of HLTV spectators |
| `slots` | `long` | number of HLTV slots |
| `proxies` | `short` | number of HLTV proxies |
| `master` | `string` | disptach master IP:port |

### hltv_title

| Field | Type | Description |
|-------|------|-------------|
| `text` | `string` |  |

### hltv_chat

a HLTV chat msg sent by spectators

| Field | Type | Description |
|-------|------|-------------|
| `text` | `string` |  |
| `steamID` | `uint64` | steam id |

### hltv_versioninfo

| Field | Type | Description |
|-------|------|-------------|
| `version` | `long` |  |

### hltv_replay

| Field | Type | Description |
|-------|------|-------------|
| `delay` | `long` | number of seconds in killer replay delay |
| `reason` | `long` | reason for replay	(ReplayEventType_t) |

### hltv_replay_status

| Field | Type | Description |
|-------|------|-------------|
| `reason` | `long` | reason for hltv replay status change () |

### demo_start

**Properties:** `local=1`

| Field | Type | Description |
|-------|------|-------------|
| `dota_combatlog_list` | `local` | CSVCMsgList_GameEvents that are combat log events |
| `dota_hero_chase_list` | `local` | CSVCMsgList_GameEvents |
| `dota_pick_hero_list` | `local` | CSVCMsgList_GameEvents |

### demo_stop

*No fields — this event carries no additional data.*

### demo_skip

**Properties:** `local=1`

| Field | Type | Description |
|-------|------|-------------|
| `playback_tick` | `long` | current playback tick |
| `skipto_tick` | `long` | tick we're going to |
| `user_message_list` | `local` | CSVCMsgList_UserMessages |
| `dota_hero_chase_list` | `local` | CSVCMsgList_GameEvents |

### map_shutdown

*No fields — this event carries no additional data.*

### map_transition

*No fields — this event carries no additional data.*

### hostname_changed

| Field | Type | Description |
|-------|------|-------------|
| `hostname` | `string` |  |

### difficulty_changed

| Field | Type | Description |
|-------|------|-------------|
| `newDifficulty` | `short` |  |
| `oldDifficulty` | `short` |  |
| `strDifficulty` | `string` | new difficulty as string |

### game_message

a message send by game logic to everyone

| Field | Type | Description |
|-------|------|-------------|
| `target` | `byte` | 0 = console, 1 = HUD |
| `text` | `string` | the message text |

### game_newmap

send when new map is completely loaded

| Field | Type | Description |
|-------|------|-------------|
| `mapname` | `string` | map name |
| `transition` | `bool` | true if this is a transition from one map to another |

### round_start

| Field | Type | Description |
|-------|------|-------------|
| `timelimit` | `long` | round time limit in seconds |
| `fraglimit` | `long` | frag limit in seconds |
| `objective` | `string` | round objective |

### round_end

| Field | Type | Description |
|-------|------|-------------|
| `winner` | `byte` | winner team/user i |
| `reason` | `byte` | reson why team won |
| `message` | `string` | end round message |
| `time` | `float` |  |

### round_start_pre_entity

*No fields — this event carries no additional data.*

### round_start_post_nav

*No fields — this event carries no additional data.*

### round_freeze_end

*No fields — this event carries no additional data.*

### teamplay_round_start

round restart

| Field | Type | Description |
|-------|------|-------------|
| `full_reset` | `bool` | is this a full reset of the map |

### player_death

a game event, name may be 32 charaters long

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | user ID who died |
| `attacker` | `player_controller_and_pawn` | user ID who killed |

### player_footstep

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_pawn` |  |

### player_hintmessage

| Field | Type | Description |
|-------|------|-------------|
| `hintmessage` | `string` | localizable string of a hint |

### break_breakable

| Field | Type | Description |
|-------|------|-------------|
| `entindex` | `long` |  |
| `userid` | `player_pawn` |  |
| `material` | `byte` | BREAK_GLASS, BREAK_WOOD, etc |

### broken_breakable

| Field | Type | Description |
|-------|------|-------------|
| `entindex` | `long` |  |
| `userid` | `player_pawn` |  |
| `material` | `byte` | BREAK_GLASS, BREAK_WOOD, etc |

### break_prop

| Field | Type | Description |
|-------|------|-------------|
| `entindex` | `long` |  |
| `userid` | `player_pawn` |  |
| `player_held` | `bool` |  |
| `player_thrown` | `bool` |  |
| `player_dropped` | `bool` |  |

### entity_killed

| Field | Type | Description |
|-------|------|-------------|
| `entindex_killed` | `long` |  |
| `entindex_attacker` | `long` |  |
| `entindex_inflictor` | `long` |  |
| `damagebits` | `long` |  |

### door_close

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_pawn` | Who closed the door |
| `checkpoint` | `bool` | Is the door a checkpoint door |

### vote_started

**Properties:** `reliable=1`

| Field | Type | Description |
|-------|------|-------------|
| `issue` | `string` |  |
| `param1` | `string` |  |
| `votedata` | `string` |  |
| `team` | `byte` |  |
| `initiator` | `long` | entity id of the player who initiated the vote |

### vote_failed

**Properties:** `reliable=1`

| Field | Type | Description |
|-------|------|-------------|
| `team` | `byte` |  |

### vote_passed

**Properties:** `reliable=1`

| Field | Type | Description |
|-------|------|-------------|
| `details` | `string` |  |
| `param1` | `string` |  |
| `team` | `byte` |  |

### vote_changed

| Field | Type | Description |
|-------|------|-------------|
| `yesVotes` | `byte` |  |
| `noVotes` | `byte` |  |
| `potentialVotes` | `byte` |  |

### vote_cast_yes

| Field | Type | Description |
|-------|------|-------------|
| `team` | `byte` |  |
| `entityid` | `long` | entity id of the voter |

### vote_cast_no

| Field | Type | Description |
|-------|------|-------------|
| `team` | `byte` |  |
| `entityid` | `long` | entity id of the voter |

### achievement_event

| Field | Type | Description |
|-------|------|-------------|
| `achievement_name` | `string` | non-localized name of achievement |
| `cur_val` | `short` | # of steps toward achievement |
| `max_val` | `short` | total # of steps in achievement |

### achievement_earned

| Field | Type | Description |
|-------|------|-------------|
| `player` | `player_controller` | entindex of the player |
| `achievement` | `short` | achievement ID |

### achievement_write_failed

*No fields — this event carries no additional data.*

### bonus_updated

| Field | Type | Description |
|-------|------|-------------|
| `numadvanced` | `short` |  |
| `numbronze` | `short` |  |
| `numsilver` | `short` |  |
| `numgold` | `short` |  |

### spec_target_updated

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | spectating player |
| `target` | `ehandle` | ehandle of the target |

### spec_mode_updated

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | spectating player |

### entity_visible

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | The player who sees the entity |
| `subject` | `long` | Entindex of the entity they see |
| `classname` | `string` | Classname of the entity they see |
| `entityname` | `string` | name of the entity they see |

### gameinstructor_draw

*No fields — this event carries no additional data.*

### gameinstructor_nodraw

*No fields — this event carries no additional data.*

### flare_ignite_npc

| Field | Type | Description |
|-------|------|-------------|
| `entindex` | `long` | entity ignited |

### helicopter_grenade_punt_miss

*No fields — this event carries no additional data.*

### physgun_pickup

| Field | Type | Description |
|-------|------|-------------|
| `target` | `ehandle` | entity picked up |

### inventory_updated

| Field | Type | Description |
|-------|------|-------------|
| `itemdef` | `short` |  |
| `itemid` | `long` |  |

### cart_updated

*No fields — this event carries no additional data.*

### store_pricesheet_updated

*No fields — this event carries no additional data.*

### item_schema_initialized

*No fields — this event carries no additional data.*

### drop_rate_modified

*No fields — this event carries no additional data.*

### event_ticket_modified

*No fields — this event carries no additional data.*

### gc_connected

*No fields — this event carries no additional data.*

### instructor_start_lesson

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | The player who this lesson is intended for |
| `hint_name` | `string` | Name of the lesson to start.  Must match instructor_lesson.txt |
| `hint_target` | `long` | entity id that the hint should display at. Leave empty if controller target |
| `vr_movement_type` | `byte` |  |
| `vr_single_controller` | `bool` |  |
| `vr_controller_type` | `byte` |  |

### instructor_close_lesson

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | The player who this lesson is intended for |
| `hint_name` | `string` | Name of the lesson to start.  Must match instructor_lesson.txt |

### instructor_server_hint_create

create a hint using data supplied entirely by the server/map. Intended for hints to smooth playtests before content is ready to make the hint unneccessary. NOT INTENDED AS A SHIPPABLE CRUTCH

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | user ID of the player that triggered the hint |
| `hint_entindex` | `long` | entity id of the env_instructor_hint that fired the event |
| `hint_name` | `string` | what to name the hint. For referencing it again later (e.g. a kill command for the hint instead of a timeout) |
| `hint_replace_key` | `string` | type name so that messages of the same type will replace each other |
| `hint_target` | `long` | entity id that the hint should display at |
| `hint_activator_userid` | `player_controller` | playerslot of the activator |
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
| `hint_allow_nodraw_target` | `bool` | if false, the hint will dissappear if the target entity is invisible |
| `hint_nooffscreen` | `bool` | if true, the hint will not show when outside the player view |
| `hint_forcecaption` | `bool` | if true, the hint caption will show even if the hint is occluded |
| `hint_local_player_only` | `bool` | if true, only the local player will see the hint |
| `hint_start_sound` | `string` | Game sound to play |
| `hint_layoutfile` | `string` | Path for Panorama layout file |
| `hint_vr_panel_type` | `short` | Attachment type for the Panorama panel |
| `hint_vr_height_offset` | `float` | Height offset for attached panels |
| `hint_vr_offset_x` | `float` | offset for attached panels |
| `hint_vr_offset_y` | `float` | offset for attached panels |
| `hint_vr_offset_z` | `float` | offset for attached panels |

### instructor_server_hint_stop

destroys a server/map created hint

| Field | Type | Description |
|-------|------|-------------|
| `hint_name` | `string` | The hint to stop. Will stop ALL hints with this name |
| `hint_entindex` | `long` | entity id of the env_instructor_hint that fired the event |

### set_instructor_group_enabled

| Field | Type | Description |
|-------|------|-------------|
| `group` | `string` |  |
| `enabled` | `short` |  |

### clientside_lesson_closed

| Field | Type | Description |
|-------|------|-------------|
| `lesson_name` | `string` |  |

### dynamic_shadow_light_changed

*No fields — this event carries no additional data.*

### bot_takeover

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `botid` | `player_controller` |  |
| `p` | `float` |  |
| `y` | `float` |  |
| `r` | `float` |  |

## Game Events

*Source: `game.gameevents`*

### player_team

player change his team

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player |
| `team` | `byte` | team id |
| `oldteam` | `byte` | old team id |
| `disconnect` | `bool` | team change because player disconnects |
| `silent` | `bool` |  |
| `isbot` | `bool` | true if player is a bot |

### player_chat

a public player chat

| Field | Type | Description |
|-------|------|-------------|
| `teamonly` | `bool` | true if team only chat |
| `userid` | `short` | chatting player |
| `text` | `string` | chat text |

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

### game_end

a game ended

| Field | Type | Description |
|-------|------|-------------|
| `winner` | `byte` | winner team/user id |

### round_announce_match_point

*No fields — this event carries no additional data.*

### round_announce_final

*No fields — this event carries no additional data.*

### round_announce_last_round_half

*No fields — this event carries no additional data.*

### round_announce_match_start

*No fields — this event carries no additional data.*

### round_announce_warmup

*No fields — this event carries no additional data.*

### warmup_end

*No fields — this event carries no additional data.*

### round_end

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

### ugc_map_info_received

| Field | Type | Description |
|-------|------|-------------|
| `published_file_id` | `uint64` |  |

### ugc_map_unsubscribed

| Field | Type | Description |
|-------|------|-------------|
| `published_file_id` | `uint64` |  |

### ugc_map_download_error

| Field | Type | Description |
|-------|------|-------------|
| `published_file_id` | `uint64` |  |
| `error_code` | `long` |  |

### ugc_file_download_finished

| Field | Type | Description |
|-------|------|-------------|
| `hcontent` | `uint64` | id of this specific content (may be image or map) |

### ugc_file_download_start

| Field | Type | Description |
|-------|------|-------------|
| `hcontent` | `uint64` | id of this specific content (may be image or map) |
| `published_file_id` | `uint64` | id of the associated content package |

### begin_new_match

*No fields — this event carries no additional data.*

### dm_bonus_weapon_start

| Field | Type | Description |
|-------|------|-------------|
| `time` | `short` | The length of time that this bonus lasts |
| `Pos` | `short` | Loadout position of the bonus weapon |

### survival_announce_phase

| Field | Type | Description |
|-------|------|-------------|
| `phase` | `short` | The phase # |

### break_prop

| Field | Type | Description |
|-------|------|-------------|
| `entindex` | `long` |  |
| `userid` | `player_pawn` |  |

### player_decal

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_pawn` |  |

### entity_visible

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | The player who sees the entity |
| `subject` | `short` | Entindex of the entity they see |
| `classname` | `string` | Classname of the entity they see |
| `entityname` | `string` | name of the entity they see |

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

### read_game_titledata

read user titledata from profile

| Field | Type | Description |
|-------|------|-------------|
| `controllerId` | `short` | Controller id of user |

### write_game_titledata

write user titledata in profile

| Field | Type | Description |
|-------|------|-------------|
| `controllerId` | `short` | Controller id of user |

### reset_game_titledata

reset user titledata; do not automatically write profile

| Field | Type | Description |
|-------|------|-------------|
| `controllerId` | `short` | Controller id of user |

### weaponhud_selection

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | Player who this event applies to |
| `mode` | `byte` | EWeaponHudSelectionMode (switch / pickup / drop) |
| `entindex` | `long` | Weapon entity index |

### vote_ended

*No fields — this event carries no additional data.*

### vote_started

| Field | Type | Description |
|-------|------|-------------|
| `issue` | `string` |  |
| `param1` | `string` |  |
| `team` | `byte` |  |
| `initiator` | `long` | entity id of the player who initiated the vote |

### vote_changed

| Field | Type | Description |
|-------|------|-------------|
| `vote_option1` | `byte` |  |
| `vote_option2` | `byte` |  |
| `vote_option3` | `byte` |  |
| `vote_option4` | `byte` |  |
| `vote_option5` | `byte` |  |
| `potentialVotes` | `byte` |  |

### vote_cast

| Field | Type | Description |
|-------|------|-------------|
| `vote_option` | `byte` | which option the player voted on |
| `team` | `short` |  |
| `userid` | `player_controller` | player who voted |

### vote_options

| Field | Type | Description |
|-------|------|-------------|
| `count` | `byte` | Number of options - up to MAX_VOTE_OPTIONS |
| `option1` | `string` |  |
| `option2` | `string` |  |
| `option3` | `string` |  |
| `option4` | `string` |  |
| `option5` | `string` |  |

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

### endmatch_cmm_start_reveal_items

*No fields — this event carries no additional data.*

### inventory_updated

*No fields — this event carries no additional data.*

### client_loadout_changed

*No fields — this event carries no additional data.*

### add_player_sonar_icon

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `pos_x` | `float` |  |
| `pos_y` | `float` |  |
| `pos_z` | `float` |  |

### door_open

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_pawn` | Who closed the door |
| `entindex` | `long` |  |

### door_closed

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_pawn` | Who closed the door |
| `entindex` | `long` |  |

### door_break

| Field | Type | Description |
|-------|------|-------------|
| `entindex` | `long` |  |
| `dmgstate` | `long` |  |

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

## CS2 (Counter-Strike) Events

*Source: `mod.gameevents`*

### player_death

a game event, name may be 32 characters long

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

### player_hurt

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

### bullet_damage

| Field | Type | Description |
|-------|------|-------------|
| `victim` | `player_controller_and_pawn` | player index who was hurt |
| `attacker` | `player_controller_and_pawn` | player index who attacked |
| `distance` | `float` | how far the bullet travelled before it hit the player |
| `damage_dir_x` | `float` | direction vector of the bullet |
| `damage_dir_y` | `float` | direction vector of the bullet |
| `damage_dir_z` | `float` | direction vector of the bullet |
| `num_penetrations` | `byte` | how many surfaces were penetrated |
| `no_scope` | `bool` | was the shooter noscoped? |
| `in_air` | `bool` | was the shooter jumping? |
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
| `recoil_index` | `float` | recoil index. Yes this is really a float. |
| `type` | `int` | lag compensation type |

### item_purchase

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `team` | `short` |  |
| `loadout` | `short` |  |
| `weapon` | `string` |  |

### bomb_beginplant

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who is planting the bomb |
| `site` | `short` | bombsite index |

### bomb_abortplant

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who is planting the bomb |
| `site` | `short` | bombsite index |

### bomb_planted

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who planted the bomb |
| `site` | `short` | bombsite index |

### bomb_defused

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who defused the bomb |
| `site` | `short` | bombsite index |

### bomb_exploded

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who planted the bomb |
| `site` | `short` | bombsite index |

### bomb_dropped

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who dropped the bomb |
| `entindex` | `long` |  |

### bomb_pickup

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_pawn` | player pawn who picked up the bomb |

### defuser_dropped

| Field | Type | Description |
|-------|------|-------------|
| `entityid` | `long` | defuser's entity ID |

### defuser_pickup

| Field | Type | Description |
|-------|------|-------------|
| `entityid` | `long` | defuser's entity ID |
| `userid` | `player_controller_and_pawn` | player who picked up the defuser |

### announce_phase_end

*No fields — this event carries no additional data.*

### cs_intermission

*No fields — this event carries no additional data.*

### bomb_begindefuse

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who is defusing |
| `haskit` | `bool` |  |

### bomb_abortdefuse

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who was defusing |

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

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who killed the hostage |
| `hostage` | `short` | hostage entity index |

### hostage_rescued

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who rescued the hostage |
| `hostage` | `short` | hostage entity index |
| `site` | `short` | rescue site index |

### hostage_stops_following

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who rescued the hostage |
| `hostage` | `short` | hostage entity index |

### hostage_rescued_all

*No fields — this event carries no additional data.*

### hostage_call_for_help

| Field | Type | Description |
|-------|------|-------------|
| `hostage` | `short` | hostage entity index |

### vip_escaped

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player who was the VIP |

### vip_killed

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player who was the VIP |
| `attacker` | `player_controller` | user ID who killed the VIP |

### player_radio

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `slot` | `short` |  |

### bomb_beep

| Field | Type | Description |
|-------|------|-------------|
| `entindex` | `long` | c4 entity |

### weapon_fire

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

### grenade_thrown

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

### silencer_detach

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### inspect_weapon

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### weapon_zoom_rifle

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### player_spawned

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `inrestart` | `bool` | true if restart is pending |

### item_pickup

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `item` | `string` | either a weapon such as 'tmp' or 'hegrenade', or an item such as 'nvgs' |
| `silent` | `bool` |  |
| `defindex` | `long` |  |

### item_pickup_slerp

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `index` | `short` |  |
| `behavior` | `short` |  |

### item_pickup_failed

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `item` | `string` |  |
| `reason` | `short` |  |
| `limit` | `short` |  |

### item_remove

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `item` | `string` | either a weapon such as 'tmp' or 'hegrenade', or an item such as 'nvgs' |
| `defindex` | `long` |  |

### ammo_pickup

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `item` | `string` | either a weapon such as 'tmp' or 'hegrenade', or an item such as 'nvgs' |
| `index` | `long` | the weapon entindex |

### item_equip

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

### enter_buyzone

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `canbuy` | `bool` |  |

### exit_buyzone

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `canbuy` | `bool` |  |

### buytime_ended

*No fields — this event carries no additional data.*

### enter_bombzone

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `hasbomb` | `bool` |  |
| `isplanted` | `bool` |  |

### exit_bombzone

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `hasbomb` | `bool` |  |
| `isplanted` | `bool` |  |

### enter_rescue_zone

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### exit_rescue_zone

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### silencer_off

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### silencer_on

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### buymenu_open

*No fields — this event carries no additional data.*

### buymenu_close

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### round_prestart

sent before all other round restart actions

*No fields — this event carries no additional data.*

### round_poststart

sent after all other round restart actions

*No fields — this event carries no additional data.*

### round_end

| Field | Type | Description |
|-------|------|-------------|
| `winner` | `byte` | winner team/user i |
| `reason` | `byte` | reson why team won |
| `message` | `string` | end round message |
| `legacy` | `byte` | server-generated legacy value |
| `player_count` | `short` | total number of players alive at the end of round, used for statistics gathering, computed on the server in the event client is in replay when receiving this message |
| `nomusic` | `byte` | if set, don't play round end music, because action is still on-going |

### grenade_bounce

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### hegrenade_detonate

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### flashbang_detonate

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### smokegrenade_detonate

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### smokegrenade_expired

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### molotov_detonate

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### decoy_detonate

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

### tagrenade_detonate

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
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

### decoy_firing

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entityid` | `short` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### bullet_impact

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### player_footstep

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |

### player_jump

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### player_blind

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `attacker` | `player_controller` | user ID who threw the flash |
| `entityid` | `short` | the flashbang going off |
| `blind_duration` | `float` |  |

### player_falldamage

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `damage` | `float` |  |

### door_moving

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `entindex` | `long` |  |

### mb_input_lock_success

*No fields — this event carries no additional data.*

### mb_input_lock_cancel

*No fields — this event carries no additional data.*

### nav_blocked

| Field | Type | Description |
|-------|------|-------------|
| `area` | `long` |  |
| `blocked` | `bool` |  |

### nav_generate

*No fields — this event carries no additional data.*

### achievement_info_loaded

*No fields — this event carries no additional data.*

### spec_mode_updated

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | entindex of the player |

### hltv_changed_mode

| Field | Type | Description |
|-------|------|-------------|
| `oldmode` | `long` |  |
| `newmode` | `long` |  |
| `obs_target` | `long` |  |

### cs_game_disconnected

*No fields — this event carries no additional data.*

### cs_round_final_beep

*No fields — this event carries no additional data.*

### cs_round_start_beep

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

### cs_win_panel_match

*No fields — this event carries no additional data.*

### cs_match_end_restart

*No fields — this event carries no additional data.*

### cs_pre_restart

*No fields — this event carries no additional data.*

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

### hide_deathpanel

*No fields — this event carries no additional data.*

### player_avenged_teammate

| Field | Type | Description |
|-------|------|-------------|
| `avenger_id` | `player_controller` |  |
| `avenged_player_id` | `player_controller` |  |

### achievement_earned_local

| Field | Type | Description |
|-------|------|-------------|
| `achievement` | `short` | achievement ID |
| `splitscreenplayer` | `short` | splitscreen ID |

### repost_xbox_achievements

| Field | Type | Description |
|-------|------|-------------|
| `splitscreenplayer` | `short` | splitscreen ID |

### match_end_conditions

| Field | Type | Description |
|-------|------|-------------|
| `frags` | `long` |  |
| `max_rounds` | `long` |  |
| `win_rounds` | `long` |  |
| `time` | `long` |  |

### round_mvp

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `reason` | `short` |  |
| `value` | `long` |  |
| `musickitmvps` | `long` |  |
| `nomusic` | `byte` |  |
| `musickitid` | `long` |  |

### show_survival_respawn_status

| Field | Type | Description |
|-------|------|-------------|
| `loc_token` | `string` |  |
| `duration` | `long` |  |
| `userid` | `player_controller_and_pawn` |  |

### client_disconnect

*No fields — this event carries no additional data.*

### gg_killed_enemy

| Field | Type | Description |
|-------|------|-------------|
| `victimid` | `player_controller` | user ID who died |
| `attackerid` | `player_controller` | user ID who killed |
| `dominated` | `short` | did killer dominate victim with this kill |
| `revenge` | `short` | did killer get revenge on victim with this kill |
| `bonus` | `bool` | did killer kill with a bonus weapon? |

### switch_team

| Field | Type | Description |
|-------|------|-------------|
| `numPlayers` | `short` | number of active players on both T and CT |
| `numSpectators` | `short` | number of spectators |
| `avg_rank` | `short` | average rank of human players |
| `numTSlotsFree` | `short` |  |
| `numCTSlotsFree` | `short` |  |

### write_profile_data

*No fields — this event carries no additional data.*

### trial_time_expired

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player whose time has expired |

### update_matchmaking_stats

*No fields — this event carries no additional data.*

### player_reset_vote

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `vote` | `bool` |  |

### enable_restart_voting

| Field | Type | Description |
|-------|------|-------------|
| `enable` | `bool` |  |

### sfuievent

| Field | Type | Description |
|-------|------|-------------|
| `action` | `string` |  |
| `data` | `string` |  |
| `slot` | `byte` |  |

### start_vote

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `type` | `byte` |  |
| `vote_parameter` | `short` |  |

### player_given_c4

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | user ID who received the c4 |

### jointeam_failed

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `reason` | `byte` | 0 = team_full |

### teamchange_pending

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `toteam` | `byte` |  |

### material_default_complete

*No fields — this event carries no additional data.*

### cs_prev_next_spectator

| Field | Type | Description |
|-------|------|-------------|
| `next` | `bool` |  |

### nextlevel_changed

a game event, name may be 32 characters long

| Field | Type | Description |
|-------|------|-------------|
| `nextlevel` | `string` |  |
| `mapgroup` | `string` |  |
| `skirmishmode` | `string` |  |

### seasoncoin_levelup

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `category` | `short` |  |
| `rank` | `short` |  |

### tournament_reward

| Field | Type | Description |
|-------|------|-------------|
| `defindex` | `long` |  |
| `totalrewards` | `long` |  |
| `accountid` | `long` |  |

### start_halftime

*No fields — this event carries no additional data.*

### ammo_refill

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `success` | `bool` |  |

### parachute_pickup

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### parachute_deploy

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### dronegun_attack

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### drone_dispatched

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `priority` | `short` |  |
| `drone_dispatched` | `short` |  |

### loot_crate_visible

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player entindex |
| `subject` | `short` | crate entindex |
| `type` | `string` | type of crate (metal, wood, or paradrop) |

### loot_crate_opened

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player entindex |
| `type` | `string` | type of crate (metal, wood, or paradrop) |

### open_crate_instr

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player entindex |
| `subject` | `short` | crate entindex |
| `type` | `string` | type of crate (metal, wood, or paradrop) |

### smoke_beacon_paradrop

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `paradrop` | `short` |  |

### survival_paradrop_spawn

| Field | Type | Description |
|-------|------|-------------|
| `entityid` | `short` |  |

### survival_paradrop_break

| Field | Type | Description |
|-------|------|-------------|
| `entityid` | `short` |  |

### drone_cargo_detached

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `cargo` | `short` |  |
| `delivered` | `bool` |  |

### drone_above_roof

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |
| `cargo` | `short` |  |

### choppers_incoming_warning

| Field | Type | Description |
|-------|------|-------------|
| `global` | `bool` |  |

### firstbombs_incoming_warning

| Field | Type | Description |
|-------|------|-------------|
| `global` | `bool` |  |

### dz_item_interaction

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` | player entindex |
| `subject` | `short` | crate entindex |
| `type` | `string` | type of crate (metal, wood, or paradrop) |

### survival_teammate_respawn

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### survival_no_respawns_warning

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### survival_no_respawns_final

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

### player_sound

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `radius` | `int` |  |
| `duration` | `float` |  |
| `step` | `bool` |  |

### guardian_wave_restart

*No fields — this event carries no additional data.*

### team_intro_start

*No fields — this event carries no additional data.*

### team_intro_end

*No fields — this event carries no additional data.*

### game_phase_changed

| Field | Type | Description |
|-------|------|-------------|
| `new_phase` | `short` |  |

### clientside_reload_custom_econ

| Field | Type | Description |
|-------|------|-------------|
| `steamid` | `string` |  |
