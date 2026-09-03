---
title: ConVars
---

# ConVar Reference

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

All console variables extracted from CS2, with the value type and the bounds the engine enforces where it declares them.

| Name | Type | Default | Range | Flags | Description |
|------|------|---------|-------|-------|-------------|
| `CS_WarnFriendlyDamageInterval` | `Int32` | `3` |  | `gamedll` `cheat` | Defines how frequently the server notifies clients that a player damaged a friend |
| `Inferno_concav_plane_threshold` | `Float32` | `-10.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `_fov` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` | Automates fov command to server. |
| `adsp_alley_min` | `Int32` | `122` |  | `developmentonly` `defensive` |  |
| `adsp_courtyard_min` | `Int32` | `126` |  | `developmentonly` `defensive` |  |
| `adsp_debug` | `Int32` | `0` |  | `archive` |  |
| `adsp_door_height` | `Int32` | `112` |  | `developmentonly` `defensive` |  |
| `adsp_duct_min` | `Int32` | `106` |  | `developmentonly` `defensive` |  |
| `adsp_hall_min` | `Int32` | `110` |  | `developmentonly` `defensive` |  |
| `adsp_low_ceiling` | `Int32` | `108` |  | `developmentonly` `defensive` |  |
| `adsp_opencourtyard_min` | `Int32` | `126` |  | `developmentonly` `defensive` |  |
| `adsp_openspace_min` | `Int32` | `130` |  | `developmentonly` `defensive` |  |
| `adsp_openstreet_min` | `Int32` | `118` |  | `developmentonly` `defensive` |  |
| `adsp_openwall_min` | `Int32` | `130` |  | `developmentonly` `defensive` |  |
| `adsp_room_min` | `Int32` | `102` |  | `developmentonly` `defensive` |  |
| `adsp_street_min` | `Int32` | `118` |  | `developmentonly` `defensive` |  |
| `adsp_tunnel_min` | `Int32` | `114` |  | `developmentonly` `defensive` |  |
| `adsp_wall_height` | `Int32` | `128` |  | `developmentonly` `defensive` |  |
| `ag2_network_recipeshape_cache_size` | `Int32` | `32` | `1 .. 1024` | `developmentonly` `gamedll` `dontrecord` | Cache size for recently-used pose recipe shapes. |
| `ag2_preserve_params_on_reload` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` | When an animgraph is reloaded, should the underlying system restore all params? |
| `ag2_use_networked_serialization_context_demo` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `dontrecord` | Use networked compatibility serialization context in demo playback. |
| `ag2_use_networked_serialization_context_game` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Use networked compatibility serialization context in games. |
| `ai_debug_dyninteractions` | `Int32` | `0` |  | `gamedll` `cheat` | Debug the NPC dynamic interaction system. |
| `ai_debug_los` | `Int32` | `0` |  | `gamedll` `cheat` | NPC Line-Of-Sight debug mode. If 1, solid entities that block NPC LOC will be highlighted with white bounding boxes. If 2, it'll show non-solid entities that would do it if they were solid. |
| `ai_debug_ragdoll_magnets` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `ai_debug_scripted_sequence` | `String` | `false` |  | `gamedll` `cheat` |  |
| `ai_debug_shoot_positions` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ai_debug_speech` | `Int32` | `0` |  | `developmentonly` `gamedll` `defensive` |  |
| `ai_disabled` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ai_force_serverside_ragdoll` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `ai_off_nav_show_nearest` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `ai_sequence_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `ai_use_visibility_cache` | `Int32` | `1` |  | `developmentonly` `gamedll` `defensive` | Sets whether or not NPCs can cache their Visibility checks against other entities. If set to 2, also tests to make sure that NPC-&gt;Target results match that of Target-&gt;NPC. |
| `ai_use_visibility_cache_reciprocation` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Sets whether or not the visibility check cache should be reciprocal. |
| `always_perform_full_spatial_partition_update` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `ammo_338mag_headshot_mult` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_338mag_impulse` | `Float32` | `2800.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_338mag_max` | `Int32` | `30` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_357sig_headshot_mult` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_357sig_impulse` | `Float32` | `2000.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_357sig_max` | `Int32` | `52` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_357sig_min_max` | `Int32` | `12` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_357sig_p250_max` | `Int32` | `26` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_357sig_small_max` | `Int32` | `24` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_45acp_headshot_mult` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_45acp_impulse` | `Float32` | `2100.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_45acp_max` | `Int32` | `100` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_50AE_headshot_mult` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_50AE_impulse` | `Float32` | `2400.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_50AE_max` | `Int32` | `35` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_556mm_box_headshot_mult` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_556mm_box_impulse` | `Float32` | `2400.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_556mm_box_max` | `Int32` | `200` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_556mm_headshot_mult` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_556mm_impulse` | `Float32` | `2400.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_556mm_max` | `Int32` | `90` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_556mm_small_max` | `Int32` | `40` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_57mm_headshot_mult` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_57mm_impulse` | `Float32` | `2000.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_57mm_max` | `Int32` | `100` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_762mm_headshot_mult` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_762mm_impulse` | `Float32` | `2400.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_762mm_max` | `Int32` | `90` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_9mm_headshot_mult` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_9mm_impulse` | `Float32` | `2000.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_9mm_max` | `Int32` | `120` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_buckshot_headshot_mult` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_buckshot_impulse` | `Float32` | `600.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_buckshot_max` | `Int32` | `32` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_grenade_limit_default` | `Int32` | `1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `ammo_grenade_limit_flashbang` | `Int32` | `1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `ammo_grenade_limit_total` | `Int32` | `3` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `ammo_item_limit_adrenaline` | `Int32` | `5` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_item_limit_healthshot` | `Int32` | `4` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `anim_decode_forcewritealltransforms` | `Bool` | `false` |  | `developmentonly` | Force BatchAnimationDecode to write transformations for all bones |
| `anim_disable` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `anim_resource_validate_on_load` | `Bool` | `true` |  | `release` | Validates the animation group channel list against the animations on load for every animation |
| `animated_material_attributes` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `animgraph2_enable_parallel_update` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph2_serialize_pose_recipe_in_pre_pack_entities` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_debug` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` | Debug animation graph |
| `animgraph_debug_animevents` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Print info about animevents emitted by AnimGraph |
| `animgraph_debug_entindex` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `cheat` | The entity to specifically debug |
| `animgraph_debug_filterent` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Filter setting for animgraph_debug_variables output. If set to -1, show debug for all entities. If set to 0, show debug for any NPCs that have been npc_selected. If set to &gt;0, something other than 0, show debug for the entity with the matching entindex. |
| `animgraph_debug_max_poseop_count` | `Bool` | `false` |  | `reference` |  |
| `animgraph_debug_set_filter_params` | `String` |  |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Comma separated list of params to filter against when drawing debug text overlays |
| `animgraph_debug_set_filter_tags` | `String` |  |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Comma separated list of tags to filter against when drawing debug text overlays |
| `animgraph_debug_show_unreferenced_params` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_debug_show_unreferenced_tags` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_debug_tags` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_debug_variables` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Turn on to see animgraph variable changes for entities passing animgraph_debug_filterent. |
| `animgraph_debug_variables_ignore_missing` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | If set, animgraph_debug_variables won't show debug for warnings about sets to missing variables. |
| `animgraph_debug_variables_ignore_nonchanges` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | If set, animgraph_debug_variables won't show debug for variable sets that don't change the value. |
| `animgraph_draw_traces` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_enable` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Enable animation graph |
| `animgraph_enable_dirty_netvar_optimization` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_auto_ledge_detection` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` | Attempt to detect when the foot is partially hanging off a ledge and stop it tilting to reach the bottom |
| `animgraph_footlock_auto_stair_detection` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` | Attempt to detect when the foot is on a stair and will stop it from tilting to reach the next step |
| `animgraph_footlock_calculate_tilt` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_debug_foot_index` | `Int32` | `-1` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_debug_type` | `Int32` | `2` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_draw_footbase` | `Bool` | `false` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_enabled` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` | A master convar that effectively disables the entire footlock node. |
| `animgraph_footlock_ground_roll` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_hip_offset_enable` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_ik_enable` | `Bool` | `true` |  | `replicated` `cheat` | Enable IK. |
| `animgraph_footlock_tilt_mode` | `Int32` | `1` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_trace_ground_enabled` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` | Convar for toggling foot lock ground tracking. |
| `animgraph_footlock_use_hip_shift` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footstep_node_supresses_events` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_force_full_network_updates` | `Bool` | `false` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_ik_debug` | `Bool` | `false` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_motionmatching_print_compressionstats` | `Bool` | `false` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_network_enable` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Enable animation graph networking. The setting is only read at graph creation time; to use please set on the command line. |
| `animgraph_parallel_postdataupdate` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `animgraph_slope_draw_raycasts` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `animgraph_slope_enable` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `animgraph_slowdownonslopes_enabled` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `animgraph_trace_ignore_prop_physics` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_trace_static_only` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `animgraph_verify_dirty_netvar_optimization` | `Bool` | `false` |  | `developmentonly` `replicated` `defensive` |  |
| `annotation_auto_load` | `Bool` | `false` |  | `clientdll` `release` `commandline_enforced` |  |
| `attached_output_stall_ms` | `Float32` | `250.000000` |  | `developmentonly` `defensive` |  |
| `audio_input_test_signal` | `Bool` | `false` |  | `developmentonly` | For testing the audio input pathway with a sine tone instead of SDL3. |
| `audio_input_use_sdl_roles` | `Bool` | `false` |  | `developmentonly` |  |
| `autosave_fully_async` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Set to 1 to have autosaves execute completely on the save thread, forces 'render only' mode while the save completes |
| `battery_saver` | `Bool` | `false` |  | `archive` | OBSOLETE replaced by mobile_fps_* - Battery saver mode. 0=off, 1=on |
| `bot_allow_grenades` | `Bool` | `true` |  | `gamedll` `release` | If nonzero, bots may use grenades. |
| `bot_allow_machine_guns` | `Bool` | `true` |  | `gamedll` `release` | If nonzero, bots may use the machine gun. |
| `bot_allow_pistols` | `Bool` | `true` |  | `gamedll` `release` | If nonzero, bots may use pistols. |
| `bot_allow_rifles` | `Bool` | `true` |  | `gamedll` `release` | If nonzero, bots may use rifles. |
| `bot_allow_rogues` | `Bool` | `true` |  | `gamedll` `release` `commandline_enforced` | If nonzero, bots may occasionally go 'rogue'. Rogue bots do not obey radio commands, nor pursue scenario goals. |
| `bot_allow_shotguns` | `Bool` | `true` |  | `gamedll` `release` | If nonzero, bots may use shotguns. |
| `bot_allow_snipers` | `Bool` | `true` |  | `gamedll` `release` | If nonzero, bots may use sniper rifles. |
| `bot_allow_sub_machine_guns` | `Bool` | `true` |  | `gamedll` `release` | If nonzero, bots may use sub-machine guns. |
| `bot_auto_follow` | `Bool` | `false` |  | `gamedll` `release` | If nonzero, bots with high co-op may automatically follow a nearby human player. |
| `bot_auto_vacate` | `Bool` | `true` |  | `gamedll` `release` | If nonzero, bots will automatically leave to make room for human players. |
| `bot_autodifficulty_threshold_high` | `Float32` | `5.000000` | `-20.000000 .. 20.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Upper bound above Average Human Contribution Score that a bot must be above to change its difficulty |
| `bot_autodifficulty_threshold_low` | `Float32` | `-2.000000` | `-20.000000 .. 20.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Lower bound below Average Human Contribution Score that a bot must be below to change its difficulty |
| `bot_chatter` | `String` | `normal` |  | `gamedll` `release` `commandline_enforced` | Control how bots talk. Allowed values: 'off', 'radio', 'minimal', or 'normal'. |
| `bot_chatter_use_rr` | `Bool` | `true` |  | `developmentonly` `gamedll` | 0 = Use old bot chatter system, 1 = Use response rules |
| `bot_controllable` | `Bool` | `true` |  | `gamedll` `release` | Determines whether bots can be controlled by players |
| `bot_coop_idle_max_vision_distance` | `Float32` | `1400.000000` | `>= -1.000000` | `gamedll` `replicated` `release` `commandline_enforced` | Max distance bots can see targets (in coop) when they are idle, dormant, hiding or asleep. |
| `bot_crouch` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `bot_debug` | `Int32` | `0` |  | `gamedll` `cheat` | For internal testing purposes. |
| `bot_debug_target` | `Int32` | `0` |  | `gamedll` `cheat` | For internal testing purposes. |
| `bot_defense_rush_chance` | `Float32` | `33.000000` |  | `gamedll` `cheat` | Are the defense bots going to rush. |
| `bot_defer_to_human_goals` | `Bool` | `false` |  | `gamedll` `release` `commandline_enforced` | If nonzero and there is a human on the team, the bots will not do the scenario tasks. |
| `bot_defer_to_human_items` | `Bool` | `true` |  | `gamedll` `release` `commandline_enforced` | If nonzero and there is a human on the team, the bots will not get scenario items. |
| `bot_difficulty` | `Int32` | `1` |  | `gamedll` `release` `commandline_enforced` | Defines the skill of bots joining the game.  Values are: 0=easy, 1=normal, 2=hard, 3=expert. |
| `bot_dont_shoot` | `Bool` | `false` |  | `gamedll` `cheat` `release` | If nonzero, bots will not fire weapons (for debugging). |
| `bot_eco_limit` | `Float32` | `2000.000000` |  | `gamedll` `release` | If nonzero, bots will not buy if their money falls below this amount. |
| `bot_flipout` | `Bool` | `false` |  | `gamedll` `release` | If nonzero, bots use no CPU for AI. Instead, they run around randomly. |
| `bot_force_duck` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `bot_freeze` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `bot_ignore_enemies` | `Bool` | `false` |  | `gamedll` `cheat` | If nonzero, bots will ignore enemies (for debugging). |
| `bot_ignore_players` | `Bool` | `false` |  | `gamedll` `cheat` | Bots will not see non-bot players. |
| `bot_join_after_player` | `Bool` | `true` |  | `gamedll` `release` | If nonzero, bots wait until a player joins before entering the game. |
| `bot_join_delay` | `Int32` | `0` |  | `developmentonly` `gamedll` `defensive` | Prevents bots from joining the server for this many seconds after a map change. |
| `bot_join_in_warmup` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Prevents bots from joining the server while warmup phase is active. |
| `bot_join_team` | `String` | `any` |  | `gamedll` `release` | Determines the team bots will join into. Allowed values: 'any', 'T', or 'CT'. |
| `bot_loadout` | `String` |  |  | `gamedll` `cheat` | bots are given these items at round start |
| `bot_max_visible_smoke_length` | `Float32` | `200.000000` |  | `gamedll` `replicated` `release` | Bots will see players through smoke clouds up to this length. |
| `bot_max_vision_distance_override` | `Float32` | `-1.000000` | `>= -1.000000` | `gamedll` `replicated` `release` `commandline_enforced` | Max distance bots can see targets. |
| `bot_mimic` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `cheat` | Bot uses usercmd of player by index. |
| `bot_mimic_spec_buttons` | `Bool` | `true` |  | `clientdll` `cheat` | +attack, +jump etc are used for spectator control instead of being passed on to spectated bot |
| `bot_mimic_yaw_offset` | `Float32` | `180.000000` |  | `gamedll` `cheat` |  |
| `bot_prefix` | `String` |  |  | `gamedll` `release` | This string is prefixed to the name of all bots that join the game.<br>&lt;difficulty&gt; will be replaced with the bot's difficulty.<br>&lt;weaponclass&gt; will be replaced with the bot's desired weapon class.<br>&lt;skill&gt; will be replaced with a 0-100 representation of the bot's skill. |
| `bot_quota` | `Int32` | `10` |  | `gamedll` `release` `commandline_enforced` | Determines the total number of bots in the game. |
| `bot_quota_mode` | `String` | `normal` |  | `gamedll` `release` `commandline_enforced` | Determines the type of quota.<br>Allowed values: 'normal', 'fill', and 'match'.<br>If 'fill', the server will adjust bots to keep N players in the game, where N is bot_quota.<br>If 'match', the server will maintain a 1:N ratio of humans to bots, where N is bot_quota. |
| `bot_randombuy` | `Bool` | `false` |  | `gamedll` `cheat` | should bots ignore their prefered weapons and just buy weapons at random? |
| `bot_show_battlefront` | `Bool` | `false` |  | `gamedll` `cheat` | Show areas where rushing players will initially meet. |
| `bot_show_nav` | `Bool` | `false` |  | `gamedll` `cheat` | For internal testing purposes. |
| `bot_show_occupy_time` | `Bool` | `false` |  | `gamedll` `cheat` | Show when each nav area can first be reached by each team. |
| `bot_stop` | `String` | `0` |  | `gamedll` `cheat` | bot_stop &lt;1\|all&gt; \| &lt;not_bomber&gt; \| &lt;t&gt; \| &lt;ct&gt; |
| `bot_strafe` | `Float32` | `0.000000` |  | `gamedll` `release` | Strafe left and right (interval) |
| `bot_traceview` | `Int32` | `0` |  | `gamedll` `cheat` | For internal testing purposes. |
| `bot_walk` | `Bool` | `false` |  | `gamedll` `release` | If nonzero, bots can only walk, not run. |
| `bot_zombie` | `Bool` | `false` |  | `gamedll` `cheat` | If nonzero, bots will stay in idle mode and not attack. |
| `break_damage_inherit_scale` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `break_invulnerable_spawn_duration` | `Float32` | `0.500000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `breakable_debug_spawn_transform_time` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Debug draw the spawn transform location. |
| `breakable_multiplayer` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `buddha` | `Bool` | `false` |  | `gamedll` `notify` `cheat` | Player takes damage but won't die |
| `buddha_ignore_bots` | `Bool` | `false` |  | `gamedll` `notify` `cheat` | Bots always buddha 0 |
| `buddha_reset_hp` | `Int32` | `1` |  | `gamedll` `notify` `cheat` | HP to set when damaged below zero in Buddha Mode |
| `bug_submitter_override` | `String` |  |  | `archive` |  |
| `buildcubemaps_renderdoc_capture` | `Int32` | `-1` |  | `developmentonly` `clientdll` | Capture a specific cubemap with RenderDoc during buildcubemaps. |
| `c_maxdistance` | `Float32` | `200.000000` |  | `clientdll` `archive` |  |
| `c_maxpitch` | `Float32` | `90.000000` |  | `clientdll` `archive` |  |
| `c_maxyaw` | `Float32` | `135.000000` |  | `clientdll` `archive` |  |
| `c_mindistance` | `Float32` | `30.000000` |  | `clientdll` `archive` |  |
| `c_minpitch` | `Float32` | `0.000000` |  | `clientdll` `archive` |  |
| `c_minyaw` | `Float32` | `-135.000000` |  | `clientdll` `archive` |  |
| `c_orthoheight` | `Float32` | `100.000000` |  | `clientdll` `archive` |  |
| `c_orthowidth` | `Float32` | `100.000000` |  | `clientdll` `archive` |  |
| `c_thirdpersonshoulder` | `Bool` | `false` |  | `clientdll` `archive` |  |
| `c_thirdpersonshoulderaimdist` | `Float32` | `120.000000` |  | `clientdll` `archive` |  |
| `c_thirdpersonshoulderdist` | `Float32` | `40.000000` |  | `clientdll` `archive` |  |
| `c_thirdpersonshoulderheight` | `Float32` | `5.000000` |  | `clientdll` `archive` |  |
| `c_thirdpersonshoulderoffset` | `Float32` | `20.000000` |  | `clientdll` `archive` |  |
| `cachedvalue_count_partybrowser` | `Int32` | `0` |  | `clientdll` `hidden` `archive` |  |
| `cachedvalue_count_teammates` | `Int32` | `0` |  | `clientdll` `hidden` `archive` |  |
| `cam_collision` | `Int32` | `1` |  | `clientdll` `archive` | When in thirdperson and cam_collision is set to 1, an attempt is made to keep the camera from passing though walls. |
| `cam_idealdelta` | `Float32` | `4.000000` |  | `clientdll` `archive` | Controls the speed when matching offset to ideal angles in thirdperson view |
| `cam_idealdist` | `Float32` | `150.000000` |  | `clientdll` `archive` |  |
| `cam_ideallag` | `Float32` | `4.000000` |  | `clientdll` `archive` | Amount of lag used when matching offset to ideal angles in thirdperson view |
| `cam_idealpitch` | `Float32` | `0.000000` |  | `clientdll` `archive` |  |
| `cam_idealyaw` | `Float32` | `0.000000` |  | `clientdll` `archive` |  |
| `cam_showangles` | `Bool` | `false` |  | `clientdll` `cheat` | When in thirdperson, print viewangles/idealangles/cameraoffsets to the console. |
| `cam_snapto` | `Bool` | `false` |  | `clientdll` `archive` |  |
| `camera_datadriven_debug` | `Bool` | `false` |  | `developmentonly` `clientdll` `cheat` |  |
| `camera_datadriven_disable_cache` | `Bool` | `false` |  | `developmentonly` `gamedll` `cheat` |  |
| `camera_path_edit_mode` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `cash_player_bomb_defused` | `Int32` | `300` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_bomb_planted` | `Int32` | `300` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_damage_hostage` | `Int32` | `-30` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_drop_on_death` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_drop_on_death_stack_value` | `Int32` | `250` |  | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_get_killed` | `Int32` | `0` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_interact_with_hostage` | `Int32` | `150` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_killed_enemy_default` | `Int32` | `300` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_killed_enemy_factor` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_killed_hostage` | `Int32` | `-1000` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_killed_teammate` | `Int32` | `-300` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_rescued_hostage` | `Int32` | `1000` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_respawn_amount` | `Int32` | `0` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_bonus_shorthanded` | `Int32` | `0` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_elimination_bomb_map` | `Int32` | `3250` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_elimination_hostage_map_ct` | `Int32` | `2000` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_elimination_hostage_map_t` | `Int32` | `1000` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_hostage_alive` | `Int32` | `0` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_hostage_interaction` | `Int32` | `500` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_loser_bonus` | `Int32` | `1400` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_loser_bonus_consecutive_rounds` | `Int32` | `500` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_per_dead_enemy` | `Int32` | `50` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_planted_bomb_but_defused` | `Int32` | `600` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_rescued_hostage` | `Int32` | `0` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_terrorist_win_bomb` | `Int32` | `3500` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_win_by_defusing_bomb` | `Int32` | `3250` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_win_by_hostage_rescue` | `Int32` | `3500` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_win_by_time_running_out_bomb` | `Int32` | `3250` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_win_by_time_running_out_hostage` | `Int32` | `3250` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_winner_bonus_consecutive_rounds` | `Int32` | `0` |  | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `cc_captiontrace` | `Int32` | `1` |  | `developmentonly` `clientdll` `defensive` | Show missing closecaptions (0 = no, 1 = devconsole, 2 = show in hud) |
| `cc_delay_time` | `Float32` | `0.250000` |  | `clientdll` `archive` | Close caption delay before showing caption. |
| `cc_force_combine_chatter` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cc_lang` | `String` |  |  | `clientdll` `archive` | Current close caption language (emtpy = use game UI language) |
| `cc_linger_time` | `Float32` | `1.000000` |  | `clientdll` `archive` | Close caption linger time. |
| `cc_log` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` | Log caption names and contents (0 = off, 1 = found captions, 2 = unfound captions, 3 = all captions) |
| `cc_spectator_only` | `Bool` | `false` |  | `clientdll` `archive` |  |
| `cc_subtitles` | `Bool` | `false` |  | `clientdll` `archive` | If set, don't show sound effect captions, just voice overs (i.e., won't help hearing impaired players). |
| `cc_vr_caption_catchup_interval` | `Float32` | `0.300000` | `>= 0.010000` | `developmentonly` `clientdll` `defensive` | Duration it takes for attached caption to ideal point |
| `cc_vr_caption_speed` | `Int32` | `1` | `0 .. 2` | `clientdll` `archive` | 0 = slow, 1 = medium (default), 2 = fast |
| `cc_vr_debug` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Debug visualization of VR closed caption placement |
| `cc_vr_depth_test` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Have closed caption Panorama panel perform depth testing against the scene |
| `cc_vr_epsilon` | `Float32` | `2.500000` |  | `developmentonly` `clientdll` `defensive` | Epsilon to trigger movement of VR subtitle panel in world space |
| `cc_vr_font_size` | `Int32` | `1` | `0 .. 2` | `clientdll` `archive` | 0 = small, 1 = med (default), 2 = large |
| `cc_vr_forward_offset` | `Float32` | `30.000000` |  | `developmentonly` `clientdll` `defensive` | Subtitle offset distance (forward, in front of player) |
| `cc_vr_vertical_offset` | `Float32` | `-6.500000` |  | `developmentonly` `clientdll` `defensive` | Subtitle vertical offset distance (positive is up) |
| `cc_vr_width` | `Int32` | `1` | `0 .. 2` | `clientdll` `archive` | 0 = narrow, 1 = med (default), 2 = wide |
| `character_patches` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `check_transmit_dump_ents` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `chicken_stop` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `cl_ShowBoneSetupEnts` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Show which entities are having their bones setup each frame. |
| `cl_access_all_missions` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_ag2_record_entity_graph` | `String` |  |  | `developmentonly` `clientdll` | Automatically start AG2 recording when an entity with this name (wildcard) or id is created. |
| `cl_aggregate_particles` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `cl_allow_animated_avatars` | `Bool` | `true` |  | `clientdll` `archive` `release` | Whether or not to allow animated avatars |
| `cl_allow_multi_input_binds` | `Bool` | `false` |  | `clientdll` `cheat` `release` |  |
| `cl_anglespeedkey` | `Float32` | `0.670000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_async_client_shatter` | `Bool` | `true` |  | `developmentonly` `clientdll` | spawn client glass shards asynchronously during demos or when remotely connected. |
| `cl_async_restore_server_authoritative_state` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_async_usercmd_send` | `Bool` | `true` |  | `developmentonly` |  |
| `cl_async_usercmd_send_recvmargin_min` | `Float32` | `1.000000` |  | `developmentonly` `defensive` | Min size of the recv margin queue when async usercmd send is disabled |
| `cl_auto_cursor_scale` | `Bool` | `true` |  | `archive` | Automatic cursor size scaling. |
| `cl_autobuy` | `String` |  |  | `clientdll` `release` | The order in which autobuy will attempt to purchase items |
| `cl_autohelp` | `Bool` | `true` |  | `clientdll` `archive` `userinfo` | Auto-help |
| `cl_bake_bomb_damage_debug` | `Int32` | `0` |  | `clientdll` `cheat` |  |
| `cl_batch_entity_list_ops_during_latch` | `Bool` | `false` |  | `developmentonly` `clientdll` | Batch entity list adds / removes while latching interpolated variables to avoid mutex contention. |
| `cl_bone_cache_optimization` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `cl_borrow_music_from_player_slot` | `Int32` | `-1` |  | `clientdll` `release` |  |
| `cl_boxmove` | `Int32` | `0` |  | `developmentonly` `clientdll` | run in a square, # represents how many usercommands to run before turning. |
| `cl_boxmove_speed` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` | how fast to run (1 to use player max run speed). |
| `cl_buffer_incoming_net_messages` | `Bool` | `true` |  | `release` |  |
| `cl_buymenu_ct_nextround_high` | `Int32` | `5000` |  | `clientdll` `archive` `per_user` `release` |  |
| `cl_buymenu_ct_nextround_low` | `Int32` | `1400` |  | `clientdll` `archive` `per_user` `release` |  |
| `cl_buymenu_t_nextround_high` | `Int32` | `5000` |  | `clientdll` `archive` `per_user` `release` |  |
| `cl_buymenu_t_nextround_low` | `Int32` | `1400` |  | `clientdll` `archive` `per_user` `release` |  |
| `cl_buywheel_donate_key` | `Int32` | `0` |  | `clientdll` `archive` `per_user` `release` | Set the key to use for donation in the buy menu. 0: Left Control; 1: Left Alt; 2: Left Shift. |
| `cl_buywheel_nonumberpurchasing` | `Bool` | `false` |  | `clientdll` `archive` `per_user` `release` | Set non-zero to prevent buy wheel from purchasing via number keys |
| `cl_cache_sendtable` | `Bool` | `true` |  | `developmentonly` `defensive` | Cache sendtables |
| `cl_cameraoverride_fade_in_amount` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_cameraoverride_shadow_depth_bias` | `Float32` | `0.006000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_cameraoverride_shadow_end` | `Float32` | `0.800000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_change_callback_limit` | `Float32` | `0.200000` |  | `clientdll` `release` | change callback msec warning limit |
| `cl_chat_active` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_clanid` | `String` | `0` |  | `clientdll` `hidden` `archive` `userinfo` | Current clan ID for name decoration |
| `cl_clock_buffer_ticks` | `Float32` | `0.000000` |  | `developmentonly` | Clock sync will try to maintain an additional margin of N ticks.  This is intended to smooth over packet loss, and is a replacement for cl_interp_ratio / cl_interp.  This value is simply added to cl_clock_recvmargin_desired |
| `cl_clock_buffer_ticks_spectator` | `Float32` | `2.000000` |  | `developmentonly` | Additional margin (in ticks) to apply when spectating. |
| `cl_clock_correction` | `Bool` | `true` |  | `cheat` | Enable/disable clock correction on the client. |
| `cl_clock_recvmargin_adjust_limit_slowdown` | `Float32` | `93.000000` | `66.000000 .. 100.000000` | `developmentonly` | Clock sync will not slow down time slower than N% |
| `cl_clock_recvmargin_adjust_limit_speedup` | `Float32` | `106.000000` | `100.000000 .. 150.000000` | `developmentonly` | Clock sync will not speed up time faster than N% |
| `cl_clock_recvmargin_desired` | `Float32` | `5.000000` |  | `developmentonly` | Clock sync will try to maintain N ms margin between tick arrival and polling network.  The effective value is the sum of this and the time implied by cl_clock_buffer_ticks |
| `cl_clock_recvmargin_spew_interval` | `Int32` | `0` |  | `release` |  |
| `cl_clock_recvmargin_timeconstant_slowdown` | `Float32` | `0.300000` |  | `developmentonly` | Clock sync will remove 63.2% of the error in N seconds |
| `cl_clock_recvmargin_timeconstant_speedup` | `Float32` | `0.600000` |  | `developmentonly` | Clock sync will remove 63.2% of the error in N seconds |
| `cl_clock_recvmargin_window` | `Float32` | `4.000000` |  | `developmentonly` | Clock sync will use past N seconds |
| `cl_clockdbg` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `cl_clockdrift_max_ticks` | `Int32` | `3` | `>= 0` | `hidden` `release` | Maximum number of ticks the clock is allowed to drift before the client snaps its clock to the server's. |
| `cl_clutch_mode` | `Bool` | `false` |  | `clientdll` `release` | Silence voice and other distracting sounds until the end of round or next death. |
| `cl_color` | `Int32` | `1` | `0 .. 4` | `clientdll` `archive` `userinfo` | Preferred teammate color |
| `cl_connectionretrytime_p2p` | `Float32` | `20.000000` |  | `release` | Number of seconds over which to spread retry attempts for P2P. |
| `cl_cq_min_queue` | `Int32` | `0` |  | `userinfo` | Used by the client to inform the server of their desired queue length.  Derived from cl_tickpacket_recvmargin_desired and cl_tickpacket_desired_queuelength |
| `cl_crosshair_drawoutline` | `Bool` | `true` |  | `clientdll` `archive` `per_user` | Draws a black outline around the crosshair for better visibility |
| `cl_crosshair_dynamic_maxdist_splitratio` | `Float32` | `1.000000` | `0.000000 .. 1.000000` | `clientdll` `archive` `per_user` | If using cl_crosshairstyle 2, this is the ratio used to determine how long the inner and outer xhair pips will be. [inner = cl_crosshairsize*(1-cl_crosshair_dynamic_maxdist_splitratio), outer = cl_crosshairsize*cl_crosshair_dynamic_maxdist_splitratio]  [0 - 1] |
| `cl_crosshair_dynamic_splitalpha_innermod` | `Float32` | `0.000000` | `0.000000 .. 1.000000` | `clientdll` `archive` `per_user` | If using cl_crosshairstyle 2, this is the alpha modification that will be used for the INNER crosshair pips once they've split. [0 - 1] |
| `cl_crosshair_dynamic_splitalpha_outermod` | `Float32` | `1.000000` | `0.300000 .. 1.000000` | `clientdll` `archive` `per_user` | If using cl_crosshairstyle 2, this is the alpha modification that will be used for the OUTER crosshair pips once they've split. [0.3 - 1] |
| `cl_crosshair_dynamic_splitdist` | `Int32` | `3` |  | `clientdll` `archive` `per_user` | If using cl_crosshairstyle 2, this is the distance that the crosshair pips will split into 2. (default is 7) |
| `cl_crosshair_friendly_warning` | `Int32` | `1` | `0 .. 1` | `clientdll` `archive` `release` | 0: off, 1: on |
| `cl_crosshair_outlinethickness` | `Float32` | `1.000000` | `0.000000 .. 3.000000` | `clientdll` `archive` `per_user` | Set how thick you want your crosshair outline to draw (0-3) |
| `cl_crosshair_recoil` | `Bool` | `true` |  | `clientdll` `archive` `per_user` |  |
| `cl_crosshair_show_desynced_seeds_marker` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `cl_crosshair_sniper_width` | `Int32` | `1` |  | `clientdll` `archive` `per_user` | If &gt;1 sniper scope cross lines gain extra width (1 for single-pixel hairline) |
| `cl_crosshair_t` | `Bool` | `false` |  | `clientdll` `archive` `per_user` | T style crosshair |
| `cl_crosshairalpha` | `Int32` | `200` | `0 .. 255` | `clientdll` `archive` `per_user` |  |
| `cl_crosshaircolor` | `Int32` | `5` |  | `clientdll` `archive` `per_user` | Set crosshair color as defined in game_options.consoles.txt |
| `cl_crosshaircolor_b` | `Int32` | `0` | `0 .. 255` | `clientdll` `archive` `per_user` |  |
| `cl_crosshaircolor_g` | `Int32` | `255` | `0 .. 255` | `clientdll` `archive` `per_user` |  |
| `cl_crosshaircolor_r` | `Int32` | `0` | `0 .. 255` | `clientdll` `archive` `per_user` |  |
| `cl_crosshairdot` | `Bool` | `false` |  | `clientdll` `archive` `per_user` |  |
| `cl_crosshairgap` | `Float32` | `-2.200000` |  | `clientdll` `archive` `per_user` |  |
| `cl_crosshairgap_useweaponvalue` | `Bool` | `true` |  | `clientdll` `archive` `per_user` | If set to 1, the gap will update dynamically based on which weapon is currently equipped |
| `cl_crosshairsize` | `Float32` | `3.900000` |  | `clientdll` `archive` `per_user` |  |
| `cl_crosshairstyle` | `Int32` | `2` |  | `clientdll` `archive` `per_user` | 0 = DEFAULT (DISABLED), 1 = DEFAULT STATIC (DISABLED), 2 = DEFAULT (accurate recoil/spread feedback with a fixed inner part), 3 = ACCURATE DYNAMIC (DISABLED) (accurate recoil/spread feedback), 4 = DEFAULT STATIC, 5 = LEGACY (fake recoil - inaccurate feedback) |
| `cl_crosshairthickness` | `Float32` | `0.600000` |  | `clientdll` `archive` `per_user` |  |
| `cl_crosshairusealpha` | `Bool` | `true` |  | `clientdll` `archive` `per_user` |  |
| `cl_csgo_shoot_debugvis_rdp_text_l` | `Int32` | `10` |  | `developmentonly` `clientdll` |  |
| `cl_csgo_shoot_debugvis_rdp_text_x` | `Int32` | `45` |  | `developmentonly` `clientdll` |  |
| `cl_csgo_shoot_debugvis_show_los` | `Bool` | `false` |  | `developmentonly` `clientdll` | Show line of last shot. |
| `cl_csgo_shoot_debugvis_show_rdp` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_csgo_shoot_trim_input_frames` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `cl_cursor_scale` | `Float32` | `1.000000` |  | `archive` | Cursor size scaling factor. |
| `cl_deathcam_audio_mix_phase1_fade_amount` | `Float32` | `0.150000` |  | `clientdll` `release` | Sets the amount of ducking to do on death cam fade out. When set to 1, full DeathFadeLayer is applied. |
| `cl_deathcam_audio_mix_phase1_fade_time` | `Float32` | `2.000000` |  | `clientdll` `release` | Sets the amount of time we fade out over. |
| `cl_deathcam_audio_mix_phase2_fade_amount` | `Float32` | `0.500000` |  | `clientdll` `release` | Sets the amount of ducking to do on death cam fade out. When set to 1, full DeathFadeLayer is applied. |
| `cl_deathcam_audio_mix_phase2_fade_time` | `Float32` | `0.400000` |  | `clientdll` `release` | Sets the amount of time we fade out over. |
| `cl_deathcampanel_position_dynamic` | `Int32` | `1` |  | `clientdll` `archive` | Turn on/off deathcam's kill panel dynamic Y movement |
| `cl_deathnotices_show_numbers` | `Int32` | `0` |  | `clientdll` `release` | 0: default; 1: draw names as just numbers; 2: append number on killer and victim to the name |
| `cl_debounce_zoom` | `Bool` | `true` |  | `clientdll` `archive` `userinfo` `per_user` | Whether or not to disable holding secondary fire to cycle zoom levels |
| `cl_debug_build_recvmargin_min` | `Float32` | `2.000000` |  | `developmentonly` `defensive` | Min size of the recv margin queue when in tools/debug mode |
| `cl_debug_force_push_to_talk` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_debug_overlay_fullposition` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_debug_overlays_broadcast` | `Bool` | `false` |  | `release` | Render debug overlays from server. |
| `cl_debug_precipitation_surface_graph` | `Bool` | `false` |  | `clientdll` `replicated` `cheat` | When true, use the surface graph to pass in positions for rainfall. |
| `cl_debug_round_stat_submission` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_debugviewangle` | `Bool` | `false` |  | `developmentonly` `clientdll` | Plots view angles yaw at various stages of the frame/tick in Tracy. |
| `cl_demo_predict` | `Int32` | `1` |  | `clientdll` `release` | Enable 'TrueView' when watching a demo, which attempts to recreate the client's experience more accurately.  0=disable, 1=only if demo version match, 2=always |
| `cl_demo_steadycam_blendframes` | `Int32` | `5` |  | `developmentonly` `clientdll` `defensive` | blend over this many frames |
| `cl_demo_steadycam_deflection` | `Float32` | `5.000000` |  | `developmentonly` `clientdll` `defensive` | if camera orientation changes this much update orientation |
| `cl_demo_steadycam_enable` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` | Stabilize camera orientation/position during demo playback.  1 == remove roll, 2 == steadycam |
| `cl_demo_steadycam_radius` | `Float32` | `16.000000` |  | `developmentonly` `clientdll` `defensive` | if camera moves this much from last anchor update anchor |
| `cl_demo_view_offset_left` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` `defensive` | View offset during demo playback (+/- 1.25 is a good default for human average left/right eye offset) |
| `cl_demoviewoverride` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` `defensive` | Override view during demo playback |
| `cl_disable_deathcam_audio_mix_fade_out` | `Bool` | `false` |  | `clientdll` `release` | When set to true, disables audio being silenced while the death cam fades out. |
| `cl_disable_postprocessing` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `cl_disable_ragdolls` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `cl_disable_round_end_report` | `Bool` | `false` |  | `clientdll` `archive` `release` |  |
| `cl_disconnect_soundevent` | `String` | `core.stop_all_soundevents` |  | `developmentonly` `defensive` | This soundevent is called to stop the desired soundevents when the game is disconnected. |
| `cl_disconnect_voice_fade` | `Float32` | `2.000000` |  | `developmentonly` `defensive` | This is a fade of current voices that is called when the game is disconnected. -1.f for no fade on disconnect |
| `cl_display_flashbang_values` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_display_game_events` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `cl_display_player_visibilty` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_dm_buyrandomweapons` | `Bool` | `true` |  | `clientdll` `archive` `release` | Player will automatically receive a random weapon on spawn in deathmatch if this is set to 1 (otherwise, they will receive the last weapon) |
| `cl_dormant_spew` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Spew state on when client entities become dormant or active. |
| `cl_draw_only_deathnotices` | `Bool` | `false` |  | `clientdll` `release` | For drawing only the crosshair and death notices (used for moviemaking) |
| `cl_draw_simulating_entities` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `cl_draw_simulating_entities_distance` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_drawhud` | `Bool` | `true` |  | `clientdll` `cheat` | Enable the rendering of the hud |
| `cl_drawhud_force_deathnotices` | `Int32` | `0` |  | `clientdll` `release` | 0: default; 1: draw deathnotices even if hud disabled; -1: force no deathnotices |
| `cl_drawhud_force_radar` | `Int32` | `0` |  | `clientdll` `release` | 0: default; 1: draw radar even if hud disabled; -1: force no radar |
| `cl_drawhud_force_teamid_overhead` | `Int32` | `0` |  | `clientdll` `release` | 0: default; 1: draw teamid even if hud disabled; -1: force no teamid |
| `cl_drawhud_specvote` | `Bool` | `true` |  | `clientdll` `release` | 1: default; 0: disables vote UI for spectators |
| `cl_embedded_stream_audio_volume` | `Float32` | `0.000000` | `0.000000 .. 100.000000` | `clientdll` `hidden` `archive` | Embedded stream audio volume |
| `cl_embedded_stream_audio_volume_xmaster` | `Bool` | `true` |  | `clientdll` `hidden` `archive` | Whether embedded stream audio volume gets multiplied by master volume |
| `cl_embedded_stream_video_playing` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` `hidden` `defensive` | Embedded stream video playing state |
| `cl_enable_party_voice` | `Bool` | `true` |  | `clientdll` `archive` `release` |  |
| `cl_ent_attachment_filter_substrings` | `String` |  |  | `clientdll` `cheat` | If an attachment's name has any of the given substrings in it, it will be displayed. Substrings can be delimited by the ',' or '\|' character. |
| `cl_ent_joint_axis_size` | `Float32` | `4.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_ent_joint_filter_name` | `String` |  |  | `clientdll` `cheat` | If a joint's entire name matches (case insensitive), it will be displayed. |
| `cl_ent_joint_filter_substrings` | `String` |  |  | `clientdll` `cheat` | If a joint's name has any of the given substrings in it, it will be displayed. Substrings can be delimited by the ',' or '\|' character. |
| `cl_ent_joint_lines` | `Bool` | `true` |  | `clientdll` `cheat` | Draw a line between a rendered joint and its parent. |
| `cl_ent_joint_names` | `Bool` | `true` |  | `clientdll` `cheat` | Draw the name of a rendered joint. |
| `cl_ent_joint_only_ik_joints` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_ent_joint_use_bind_pose` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_ent_pivot_size` | `Float32` | `20.000000` |  | `clientdll` `archive` `cheat` |  |
| `cl_ent_show_contexts` | `Bool` | `false` |  | `clientdll` `cheat` | Show entity contexts in ent_text display |
| `cl_ent_showonlyattachment` | `String` |  |  | `clientdll` `cheat` |  |
| `cl_ent_showonlyhitbox` | `Int32` | `-1` |  | `clientdll` `cheat` |  |
| `cl_ent_skeleton_only_ik_joints` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_ent_text_flags_active` | `Int32` | `-1` |  | `clientdll` `archive` `cheat` |  |
| `cl_ent_text_no_name_really_i_mean_it` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `cl_error_report_time` | `Float32` | `0.000000` |  | `clientdll` `release` | Minimum time in seconds that must elapse before printing prediction error summary. 0 to disable. |
| `cl_extrapolate` | `Bool` | `true` |  | `clientdll` `cheat` | Enable/disable extrapolation if interpolation history runs out. |
| `cl_extrapolate_amount` | `Float32` | `0.250000` |  | `clientdll` `cheat` | Set how many seconds the client will extrapolate entities for. |
| `cl_fake_timeout` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_fasttempentcollision` | `Int32` | `5` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_firstperson_legs` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_firstperson_legs_aoproxy` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_fixedcrosshairgap` | `Float32` | `3.000000` |  | `clientdll` `archive` `per_user` | For crosshair style 1: How big to make the gap between the pips in the fixed crosshair |
| `cl_flushentitypacket` | `Int32` | `0` |  | `cheat` | For debugging. Force the engine to flush an entity packet. |
| `cl_force_next_signon_to_reset` | `Bool` | `false` |  | `developmentonly` |  |
| `cl_force_spec_hud_color_to_team` | `Bool` | `true` |  | `clientdll` `archive` | Spec hud color setting is always team/teammate |
| `cl_frametime_summary_report_detailed` | `Bool` | `true` |  | `clientdll` `release` | When a perf report is dumped at the end of the session, should it be detailed? |
| `cl_generate_postdataupdatepreserved` | `Bool` | `true` |  | `developmentonly` | Do we invoke PostDataUpdatePreserved callbacks for entities that had no changes but are still in the PVS? |
| `cl_globallight_debug` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_depth_bias` | `Float32` | `-999.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_expansion` | `Float32` | `200.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_freeze` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_orig_calc_frustum` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_shadow_mode` | `Int32` | `2` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_slope_scale_depth_bias` | `Float32` | `-999.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_use_alt_focus_region` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_use_optimized_calc_frustum` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_use_shaadow_near_offset` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_world_bottom_height` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_world_top_height` | `Float32` | `4096.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_glow_brightness` | `Float32` | `1.000000` |  | `clientdll` `cheat` | Brightness of player halos |
| `cl_glow_item_far_b` | `Float32` | `1.000000` |  | `clientdll` `release` |  |
| `cl_glow_item_far_g` | `Float32` | `0.400000` |  | `clientdll` `release` |  |
| `cl_glow_item_far_r` | `Float32` | `0.300000` |  | `clientdll` `release` |  |
| `cl_graphics_driver_warning_dont_show_again` | `Bool` | `false` |  | `clientdll` `archive` `release` | Graphics driver recommendation (NVIDIA 581.80 / AMD 23.11.1) |
| `cl_grenadecrosshair_decoy` | `Bool` | `true` |  | `clientdll` `archive` `per_user` | Is the grenade crosshair enabled |
| `cl_grenadecrosshair_explosive` | `Bool` | `true` |  | `clientdll` `archive` `per_user` | Is the grenade crosshair enabled |
| `cl_grenadecrosshair_fire` | `Bool` | `true` |  | `clientdll` `archive` `per_user` | Is the grenade crosshair enabled |
| `cl_grenadecrosshair_flash` | `Bool` | `true` |  | `clientdll` `archive` `per_user` | Is the grenade crosshair enabled |
| `cl_grenadecrosshair_keepusercrosshair` | `Bool` | `true` |  | `clientdll` `archive` `per_user` | Keep the user's crosshair when the grenade crosshair is enabled |
| `cl_grenadecrosshair_smoke` | `Bool` | `true` |  | `clientdll` `archive` `per_user` | Is the grenade crosshair enabled |
| `cl_grenadecrosshair_tickinterval` | `Float32` | `10.000000` | `1.000000 .. 45.000000` | `developmentonly` `clientdll` |  |
| `cl_grenadecrosshair_ticklabels` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `cl_grenadecrosshair_tickscaling` | `Float32` | `1.100000` | `0.500000 .. 2.000000` | `developmentonly` `clientdll` |  |
| `cl_grenadecrosshairdelay_decoy` | `Float32` | `2.000000` |  | `clientdll` `archive` `per_user` | How long should the pin be pulled for before showing the grenade crosshair |
| `cl_grenadecrosshairdelay_explosive` | `Float32` | `2.000000` |  | `clientdll` `archive` `per_user` | How long should the pin be pulled for before showing the grenade crosshair |
| `cl_grenadecrosshairdelay_fire` | `Float32` | `2.000000` |  | `clientdll` `archive` `per_user` | How long should the pin be pulled for before showing the grenade crosshair |
| `cl_grenadecrosshairdelay_flash` | `Float32` | `2.000000` |  | `clientdll` `archive` `per_user` | How long should the pin be pulled for before showing the grenade crosshair |
| `cl_grenadecrosshairdelay_smoke` | `Float32` | `2.000000` |  | `clientdll` `archive` `per_user` | How long should the pin be pulled for before showing the grenade crosshair |
| `cl_hide_avatar_images` | `Int32` | `0` |  | `clientdll` `archive` | Hide avatar images for other players.<br>0 - Off.<br>1 - Block All<br>2 - Block all but friends |
| `cl_highlights_hud_playback` | `Int32` | `0` |  | `clientdll` `hidden` `release` | Highlights hud playback |
| `cl_hitbox_debug` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_hold_game_events_force_delay_ticks` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` | Debugging convar to force late dispatch of game events. |
| `cl_hold_game_events_until_server_tick` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` | Holds game events until client has received the tick the event was fired on. |
| `cl_http_log_enable` | `Bool` | `false` |  | `clientdll` `dontrecord` `release` `clientcmd_can_execute` | Allows sending HTTP log from client main menu. |
| `cl_hud_color` | `Int32` | `0` |  | `clientdll` `archive` `release` | 0 = team color, 1 =  white, 2 = bright white, 3 = light blue, 4 = blue, 5 = purple, 6 = red, 7 = orange, 8 = yellow, 9 = green, 10 = aqua, 11 = pink, 12 = teammate color. |
| `cl_hud_radar_background_alpha` | `Float32` | `0.627000` | `0.000000 .. 1.000000` | `clientdll` `archive` `release` |  |
| `cl_hud_radar_blur_background` | `Bool` | `true` |  | `clientdll` `archive` `release` | Blurs the radar background. |
| `cl_hud_radar_map_additive` | `Bool` | `true` |  | `clientdll` `archive` `release` | Blend Hud radar map additively on top of background. |
| `cl_hud_radar_scale` | `Float32` | `1.000000` | `0.800000 .. 1.300000` | `clientdll` `archive` `release` |  |
| `cl_hud_telemetry_frametime_poor` | `Float32` | `100.000000` | `1.000000 .. 100.000000` | `clientdll` `archive` `release` | Frame time greater than this is considered 'poor'. |
| `cl_hud_telemetry_frametime_show` | `Int32` | `1` |  | `clientdll` `archive` `release` | Show frame time (FPS) in the HUD.  0=never, 1=only if poor, 2=always |
| `cl_hud_telemetry_net_detailed` | `Int32` | `0` |  | `clientdll` `archive` `release` | Show breakdown network misdelivery (loss, late delivery, and peak jitter).  0=never, 1=only in poor network conditions, 2=always |
| `cl_hud_telemetry_net_misdelivery_poor` | `Float32` | `2.000000` |  | `clientdll` `archive` `release` | Packet delivery anomaly rate (0..100) higher than this is considered 'poor'. |
| `cl_hud_telemetry_net_misdelivery_show` | `Int32` | `1` |  | `clientdll` `archive` `release` | Show percentage of user commands &amp; server snapshots that are missed due to network conditions.  0=never, 1=only in poor conditions, 2=always |
| `cl_hud_telemetry_net_quality_graph_show` | `Int32` | `0` |  | `clientdll` `archive` `release` | Show packet jitter and netframe loss/reordering in the HUD.  0=never, 1=only in poor conditions, 2=always |
| `cl_hud_telemetry_ping_poor` | `Float32` | `100.000000` |  | `clientdll` `archive` `release` | Ping higher than this (ms) is considered 'poor'. |
| `cl_hud_telemetry_ping_show` | `Int32` | `1` |  | `clientdll` `archive` `release` | Show ping in the HUD.  0=never, 1=only in poor conditions, 2=always |
| `cl_hud_telemetry_serverrecvmargin_graph_show` | `Int32` | `0` |  | `clientdll` `archive` `release` | Show graph of the server recv margin in the HUD.  (How early/late user commands are arriving at the server before they are executed.)   0=never, 1=only when there are command queue problems, 2=always |
| `cl_ignorepackets` | `Bool` | `false` |  | `cheat` | Force client to ignore packets (for debugging). |
| `cl_import_csgo_config` | `Bool` | `true` |  | `clientdll` `archive` `release` |  |
| `cl_inferno_bodyburn` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `cl_input_enable_raw_keyboard` | `Bool` | `false` |  | `release` | Enable raw keyboard input |
| `cl_instant_death_anim` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_interp_ag2_for_non_ag2_entities` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `cl_interp_all` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Disable interpolation list optimizations. |
| `cl_interp_animationvars` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` | Interpolate LATCH_ANIMATION_BIT vars if interpolation interval is greater than simulation interval |
| `cl_interp_hermite` | `Bool` | `true` |  | `clientdll` `cheat` | Set to zero do disable hermite interpolation. |
| `cl_interp_npcs` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` `defensive` | Interpolate NPC positions starting this many seconds in past (or the value as per cl_interp_ratio, if greater) |
| `cl_interp_parallel` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Run interpolation in parallel for entities with no children. |
| `cl_interp_ratio` | `Float32` | `2.000000` | `0.000000 .. 19.000000` | `clientdll` `userinfo` | Set number of client simulation interpolation ticks. |
| `cl_interp_simulationvars` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` | Interpolate LATCH_SIMULATION_BIT vars if interpolation interval is greater than animation interval |
| `cl_interp_threadmodeticks` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` | Additional interpolation ticks to use when interpolating with threaded engine mode set. |
| `cl_interpolate` | `Bool` | `true` |  | `developmentonly` `clientdll` `userinfo` | Interpolate entities on the client. |
| `cl_interpolate_report` | `Bool` | `false` |  | `clientdll` `archive` | Enable to show interpolation profile timing |
| `cl_inv_volatile_limits` | `String` | `0:0` |  | `clientdll` `archive` |  |
| `cl_inventory_debug_tooltip` | `Bool` | `false` |  | `clientdll` `release` |  |
| `cl_inventory_radial_immediate_select` | `Bool` | `true` |  | `clientdll` `archive` `per_user` | In inventory selection radials. Select weapons the moment the cursor highlights them. Otherwise, only select the selected item on exit. |
| `cl_inventory_radial_tap_to_cycle` | `Bool` | `true` |  | `clientdll` `archive` `per_user` | In inventory selection radials. Select weapons the moment the cursor highlights them. Otherwise, only select the selected item on exit. |
| `cl_inventory_saved_filter2` | `String` | `all` |  | `clientdll` `archive` `release` |  |
| `cl_inventory_saved_sort2` | `String` | `inv_sort_age` |  | `clientdll` `archive` `release` |  |
| `cl_invites_only_friends` | `Bool` | `false` |  | `clientdll` `archive` `release` | If turned on, will ignore in-game invites from recent teammates or other non-friends |
| `cl_invites_only_mainmenu` | `Bool` | `false` |  | `clientdll` `archive` `release` | If turned on, will ignore all invites when user is playing a match |
| `cl_ironsight_dot_scale` | `Float32` | `1.000000` | `0.100000 .. 2.000000` | `clientdll` `archive` `per_user` | Ironsight dot scale |
| `cl_ironsight_filter_alpha` | `Float32` | `1.000000` | `0.000000 .. 1.000000` | `developmentonly` `clientdll` | Ironsight filter alpha |
| `cl_ironsight_min_channel_color` | `Float32` | `0.300000` | `0.000000 .. 1.000000` | `developmentonly` `clientdll` | Ironsight min channel color value |
| `cl_ironsight_usecrosshaircolor` | `Bool` | `false` |  | `clientdll` `archive` `per_user` | Should the scope dot match the user's crosshair color |
| `cl_itemimages_dynamically_generated` | `UInt32` | `2` |  | `clientdll` `archive` `release` | 2: use render-targets; 0: disk assets only |
| `cl_jitter_bad_threshold_up` | `Float32` | `20.000000` | `1.000000 .. 100.000000` | `userinfo` | When upstream packet jitter in a frame exceeds this threshold (ms), the frame is considered to have 'irregular delivery'.  This is a derived value and should not be modified manually |
| `cl_joystick_enabled` | `Bool` | `true` |  | `archive` | Enable joystick input |
| `cl_lagcompensation_test_auto_target` | `Bool` | `false` |  | `developmentonly` `clientdll` | Auto-pick value of cl_lagcompensation_test_target. |
| `cl_lagcompensation_test_target` | `Int32` | `-1` |  | `developmentonly` `clientdll` | Player whose head is tracked to test lag compensation. |
| `cl_language` | `String` | `english` |  | `developmentonly` `defensive` | Language |
| `cl_latch_report` | `Bool` | `false` |  | `clientdll` `archive` | Enable to output stats about latching |
| `cl_leveloverview` | `Float32` | `0.000000` |  | `clientdll` `cheat` |  |
| `cl_lightquery_debug` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `cl_loadout_saved_sort` | `String` | `inv_sort_age` |  | `clientdll` `archive` `release` |  |
| `cl_lock_camera` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `cl_log_tick` | `Bool` | `false` |  | `developmentonly` `defensive` | Log when a tick is received |
| `cl_log_tick_skips` | `Int32` | `0` |  | `developmentonly` `defensive` | Log when the tick delta &gt;= this |
| `cl_low_latency_vsync_recommendation_dont_show_again` | `Bool` | `false` |  | `clientdll` `archive` `release` |  |
| `cl_major_store_watch_list` | `String` |  |  | `clientdll` `archive` |  |
| `cl_map_preview_debug_jitter` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_massreport` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_matchlist_controlroom_aid` | `Int32` | `0` |  | `clientdll` `hidden` `release` |  |
| `cl_max_particle_pvs_aabb_edge_length` | `Float32` | `0.000000` |  | `release` |  |
| `cl_min_china_movie_time` | `Float32` | `6.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_min_movie_time` | `Float32` | `4.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_mute_all_but_friends_and_party` | `Int32` | `0` |  | `clientdll` `archive` | Only allow communication from friends and matchmaking party members. Set to 1 to apply the in non-competitive game modes. Set to 2 will apply the setting in all modes. |
| `cl_mute_enemy_team` | `Bool` | `false` |  | `clientdll` `archive` | Block all communication from players on the enemy team. |
| `cl_mute_player_after_reporting_abuse` | `Bool` | `true` |  | `developmentonly` `clientdll` | Mute players reported for abuse automatically. |
| `cl_names_debug` | `Bool` | `false` |  | `developmentonly` |  |
| `cl_net_buffer_ticks` | `Int32` | `0` | `0 .. 2` | `clientdll` `archive` `release` | Number of ticks of delay for server snapshots and user commands.  This value controls the value of cl_interp_ratio, which you should not modify directly. |
| `cl_net_buffer_ticks_use_interp` | `Bool` | `false` |  | `clientdll` `release` | If false, we smooth over packet loss by adjusting the clock synchronization to buffer packets.  If true, we process packets immediately and use cl_interp to delay their effects |
| `cl_net_showeventlisteners` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Show listening addition/removals |
| `cl_net_showevents` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` | Dump game events to console (1=client only, 2=all). |
| `cl_new_user_phase` | `Int32` | `0` |  | `clientdll` `archive` `release` | 0: Not Started, 1: Needs Training, 2: Training Complete, -1: Disabled |
| `cl_obs_interp_enable` | `Bool` | `true` |  | `clientdll` `archive` | Enables interpolation between observer targets |
| `cl_obs_interp_speed` | `Float32` | `1.000000` | `0.250000 .. 2.500000` | `clientdll` `archive` | Spectator camera interpolation speed |
| `cl_observed_bot_crosshair` | `Int32` | `2` |  | `clientdll` `archive` `release` | Control the crosshair shown when observing a bot. 0: Show player crosshair. 1: Show player crosshair only when bot can be taken over, otherwise show default.. 2: Always show default crosshair for bots. |
| `cl_paintkit_override` | `String` |  |  | `clientdll` `cheat` `release` |  |
| `cl_panel_freeze_time_after_press` | `Float32` | `0.500000` |  | `developmentonly` `clientdll` `defensive` | time to freeze mouse/pointer motion after a mouse button press |
| `cl_parallel_readpacketentities` | `Bool` | `true` |  | `developmentonly` `defensive` | Set to 1 to use threading snapshot reading (if game supports and server is sending bitcounts). |
| `cl_parallel_readpacketentities_threshold` | `Int32` | `2` |  | `developmentonly` `defensive` | Use parallel processing of snapshot reading if above this many entries. |
| `cl_particle_batch_mode` | `Int32` | `1` |  | `developmentonly` `defensive` |  |
| `cl_particle_create_duplicate_work_for_profiling` | `Int32` | `0` |  | `developmentonly` | Create and destroy N particle systems for every one created normally |
| `cl_particle_fallback_base` | `Int32` | `0` |  | `developmentonly` `defensive` | Base for falling back to cheaper effects under load. |
| `cl_particle_fallback_multiplier` | `Float32` | `0.000000` |  | `developmentonly` `defensive` | Multiplier for falling back to cheaper effects under load. |
| `cl_particle_log_creates` | `Bool` | `false` |  | `developmentonly` `defensive` | Print debug message every time a particle collection is created |
| `cl_particle_max_count` | `Int32` | `0` |  | `developmentonly` `defensive` |  |
| `cl_particle_newinit` | `Bool` | `true` |  | `developmentonly` | turn on optimized particle init |
| `cl_particle_retire_cost` | `Float32` | `0.000000` |  | `cheat` |  |
| `cl_particle_sim_fallback_base_multiplier` | `Float32` | `5.000000` |  | `developmentonly` `defensive` | How aggressive the switch to fallbacks will be depending on how far over the cl_particle_sim_fallback_threshold_ms the sim time is.  Higher numbers are more aggressive. |
| `cl_particle_sim_fallback_threshold_ms` | `Float32` | `6.000000` |  | `developmentonly` `defensive` | Amount of simulation time that can elapse before new systems start falling back to cheaper versions |
| `cl_particle_simulate` | `Bool` | `true` |  | `cheat` | Enables/Disables Particle Simulation |
| `cl_pclass` | `String` |  |  | `clientdll` `cheat` | Dump entity by prediction classname. |
| `cl_pdump` | `Int32` | `-1` |  | `clientdll` `cheat` | Dump info about this entity to screen. |
| `cl_phys_animated_hierarchy` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_phys_assume_fixed_tick_interval` | `Bool` | `true` |  | `developmentonly` `clientdll` | If true, we assume the client uses a fixed tickrate like the server (which may not always be true). If false, we recalculate the number of physics substeps in each client tick based on the actual elapsed time in the tick. |
| `cl_phys_block_dist` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_phys_block_fraction` | `Float32` | `0.100000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_phys_debug_callback_entities` | `Bool` | `false` |  | `clientdll` `cheat` | Print all entities that get touch callbacks. Each entity is printed only once. |
| `cl_phys_enabled` | `Bool` | `true` |  | `clientdll` `cheat` | Enable all physics simulation |
| `cl_phys_networked_start_sleep` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_phys_sleep_enable` | `Bool` | `true` |  | `clientdll` `cheat` | Enable sleeping for dynamic physics bodies. |
| `cl_phys_sound_disable_impact_sounds_under_hard_threshold` | `Bool` | `false` |  | `clientdll` `cheat` | if true, impact sounds wont play if no soft impact sound is present and the impact is below the hard velocity threshold. |
| `cl_phys_stop_at_collision` | `String` |  |  | `clientdll` `cheat` |  |
| `cl_phys_timescale` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `defensive` | Scale time for physics |
| `cl_phys_visualize_awake` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_ping_fade_deadzone` | `Float32` | `60.000000` |  | `clientdll` `archive` `release` | Distance from the crosshair over which the ping is completely invisible |
| `cl_ping_fade_distance` | `Float32` | `300.000000` |  | `clientdll` `archive` `release` | Distance from the crosshair over which the ping fades |
| `cl_pitchdown` | `Float32` | `89.000000` |  | `clientdll` `cheat` |  |
| `cl_pitchspeed` | `Float32` | `225.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_pitchup` | `Float32` | `89.000000` |  | `clientdll` `cheat` |  |
| `cl_playback_screenshots` | `Bool` | `false` |  | `developmentonly` `defensive` | Allows the client to playback screenshot and jpeg commands in demos. |
| `cl_player_ping_mute` | `Int32` | `0` |  | `clientdll` `archive` `release` | If 1, player pinging will make a sound, if 0, pings will be silent |
| `cl_player_ragdolls_collide` | `Bool` | `false` |  | `clientdll` `cheat` `release` |  |
| `cl_player_visibility_far` | `Float32` | `700.000000` |  | `developmentonly` `clientdll` | distance at which proxy scale is maximized |
| `cl_player_visibility_far_scale` | `Float32` | `1.300000` |  | `developmentonly` `clientdll` | proxy scale multiplier at max dist (is 1.0 at mindist) |
| `cl_player_visibility_near` | `Float32` | `200.000000` |  | `developmentonly` `clientdll` | cull characters nearer than this |
| `cl_player_visibility_show_stencil_proxy` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_player_visibility_stencil_bloat_amount` | `Float32` | `1.400000` |  | `developmentonly` `clientdll` |  |
| `cl_player_visibility_stencil_proxy_min_dist` | `Float32` | `3.000000` |  | `developmentonly` `clientdll` |  |
| `cl_player_visibility_stencil_proxy_min_dist_box` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` |  |
| `cl_player_visibility_stencil_proxy_type` | `Int32` | `1` |  | `developmentonly` `clientdll` | 0 - box, 1 - dodecahedron |
| `cl_playerslot_in_names` | `Bool` | `false` |  | `clientdll` `cheat` `release` | prepend controller playerslot to names for debugging |
| `cl_poll_network_early` | `Bool` | `true` |  | `release` | Enable polling for network messages every frame, instead of every tick |
| `cl_pred_always_latch` | `Bool` | `false` |  | `clientdll` `release` |  |
| `cl_pred_build_verbose` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Verbose spew when building prediction optimized data runs. |
| `cl_pred_checkstuck` | `Bool` | `false` |  | `developmentonly` `clientdll` | Perform the additional 'stuck' traces on the client side during prediction. |
| `cl_pred_optimize` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` | Optimize for not repredicting if there were no errors |
| `cl_pred_parallel_postnetwork` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_pred_print_every_cmd` | `Bool` | `false` |  | `clientdll` `release` | Print something every time we predict a command |
| `cl_predict_body_shot_fx` | `Bool` | `false` |  | `clientdll` `archive` `release` |  |
| `cl_predict_bomb_defusal` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_predict_head_shot_fx` | `Bool` | `false` |  | `clientdll` `archive` `release` |  |
| `cl_predict_kill_ragdolls` | `Bool` | `true` |  | `clientdll` `archive` `release` |  |
| `cl_predict_weapon_drop` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_prediction_savedata_postentitypacketreceived` | `Bool` | `false` |  | `clientdll` `release` | Experimental optimization.  If you are reading this in 2026, please delete this convar. |
| `cl_predictioncopy_runs` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_prefer_lefthanded` | `Bool` | `false` |  | `clientdll` `archive` `userinfo` `per_user` | Left handed preference |
| `cl_promoted_settings_acknowledged` | `String` | `0:0` |  | `clientdll` `archive` |  |
| `cl_quickinventory_filename` | `String` | `radial_quickinventory.txt` |  | `clientdll` `archive` `release` |  |
| `cl_quickinventory_lastinv` | `Bool` | `true` |  | `clientdll` `archive` `release` |  |
| `cl_quickinventory_line_update_speed` | `Float32` | `65.000000` |  | `clientdll` `archive` `release` |  |
| `cl_radar_always_centered` | `Bool` | `true` |  | `clientdll` `archive` `release` | If set to 0, the radar is maximally used. Otherwise the player is always centered, even at map extents. |
| `cl_radar_fast_transforms` | `Bool` | `true` |  | `developmentonly` `clientdll` | Faster way of placing icons on the mini map. |
| `cl_radar_icon_scale_min` | `Float32` | `0.600000` | `0.400000 .. 1.250000` | `clientdll` `archive` `release` | Sets the minimum icon scale. Valid values are 0.4 to 1.25. |
| `cl_radar_rotate` | `Bool` | `true` |  | `clientdll` `archive` `release` | 1 |
| `cl_radar_scale` | `Float32` | `0.700000` | `0.250000 .. 1.000000` | `clientdll` `archive` `release` | Sets the radar scale. Valid values are 0.25 to 1.0. |
| `cl_radar_scale_alternate` | `Float32` | `1.000000` | `0.250000 .. 1.000000` | `clientdll` `archive` `release` | Sets the alternate radar scale. Valid values are 0.25 to 1.0. |
| `cl_radar_scale_dynamic` | `Bool` | `false` |  | `clientdll` `archive` `release` | Toggles between a radar that scales dynamically to encompass all the detected elements on the map. |
| `cl_radar_show_all_players_when_spectating` | `Bool` | `true` |  | `clientdll` `archive` `release` | Set all players visible on radar when spectating, regardless of whether they have been spotted. |
| `cl_radar_square_always` | `Bool` | `false` |  | `clientdll` `archive` `release` | If set, the radar will always be square. |
| `cl_radar_square_when_spectating` | `Bool` | `true` |  | `clientdll` `archive` `release` | If set, the radar will be square when spectating. |
| `cl_radar_square_with_scoreboard` | `Bool` | `true` |  | `clientdll` `archive` `release` | If set, the radar will toggle to square when the scoreboard is visible. |
| `cl_radial_coyote_time` | `Float32` | `0.150000` |  | `developmentonly` `clientdll` | Selection lenience: How long in seconds the last selected radial segment is used if no segment is selected. |
| `cl_radial_menu_icon_radius` | `Float32` | `200.000000` |  | `developmentonly` `clientdll` |  |
| `cl_radial_menu_tap_duration` | `Float32` | `0.200000` |  | `developmentonly` `clientdll` | If nothing in a radial menu is selected, and the button engaging the radial menu is released within this duration, fallback on the radial's tap functionality |
| `cl_radial_radio_tab` | `Int32` | `0` |  | `clientdll` `release` |  |
| `cl_radial_radio_tab_0_text_1` | `String` | `#Chatwheel_quiet` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_2` | `String` | `#Chatwheel_requestecoround` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_3` | `String` | `#Chatwheel_bplan` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_4` | `String` | `#Chatwheel_requestweapon` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_5` | `String` | `#Chatwheel_midplan` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_6` | `String` | `#Chatwheel_droppedbomb` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_7` | `String` | `#Chatwheel_aplan` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_8` | `String` | `#Chatwheel_requestspend` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_1` | `String` | `#Chatwheel_bombcarrierspotted` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_2` | `String` | `#Chatwheel_requestecoround` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_3` | `String` | `#Chatwheel_multipleenemieshere` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_4` | `String` | `#Chatwheel_requestweapon` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_5` | `String` | `#Chatwheel_rotatetome` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_6` | `String` | `#Chatwheel_ihavethebomb` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_7` | `String` | `#Chatwheel_oneenemyhere` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_8` | `String` | `#Chatwheel_requestspend` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_1` | `String` | `#Chatwheel_bombcarrierspotted` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_2` | `String` | `#Chatwheel_requestecoround` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_3` | `String` | `#Chatwheel_multipleenemieshere` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_4` | `String` | `#Chatwheel_requestweapon` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_5` | `String` | `#Chatwheel_rotatetome` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_6` | `String` | `#Chatwheel_ihavethebomb` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_7` | `String` | `#Chatwheel_oneenemyhere` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_8` | `String` | `#Chatwheel_requestspend` |  | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tap_to_ping` | `Bool` | `true` |  | `clientdll` `archive` `release` | When tapping the radial radio button, leave a ping if nothing is selected within the time in seconds set in cl_radial_menu_tap_duration |
| `cl_radial_radio_version_reset` | `Int32` | `2` |  | `clientdll` `archive` `release` |  |
| `cl_radialmenu_deadzone_size` | `Float32` | `0.400000` | `0.000000 .. 1.000000` | `clientdll` `release` |  |
| `cl_radialmenu_deadzone_size_joystick` | `Float32` | `0.170000` | `0.000000 .. 1.000000` | `clientdll` `archive` `release` |  |
| `cl_ragdoll_default_scale` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` |  |
| `cl_ragdoll_limit` | `Int32` | `20` |  | `clientdll` `archive` | Maximum number of ragdolls to show (-1 disables limit) |
| `cl_ragdoll_lru_debug` | `Bool` | `false` |  | `clientdll` `replicated` `cheat` |  |
| `cl_ragdoll_physics_enable` | `Int32` | `1` |  | `developmentonly` `clientdll` `defensive` | Enable/disable ragdoll physics. |
| `cl_ragdoll_reload` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_ragdoll_workaround_threshold` | `Float32` | `4.000000` |  | `clientdll` `release` | Mainly cosmetic, client-only effect: when client doesn't know the last position of another player that spawns a ragdoll, the ragdoll creation is simplified and ragdoll is created in the right place. If you increase this significantly, ragdoll positions on your client may be dramatically wrong, but it won't affect other clients |
| `cl_random_taser_bone_y` | `Float32` | `-1.000000` |  | `developmentonly` `clientdll` `defensive` | The Y position used for the random taser force. |
| `cl_random_taser_force_y` | `Float32` | `-1.000000` |  | `developmentonly` `clientdll` `defensive` | The Y position used for the random taser force. |
| `cl_random_taser_power` | `Float32` | `4000.000000` |  | `developmentonly` `clientdll` `defensive` | Power used when applying the taser effect. |
| `cl_rebuy` | `String` |  |  | `clientdll` `release` | The order in which rebuy will attempt to repurchase items |
| `cl_redemption_reset_timestamp` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `cl_refresh_rate_recommendation_dont_show_again` | `Bool` | `false` |  | `clientdll` `archive` `release` |  |
| `cl_resend` | `Float32` | `0.500000` | `0.100000 .. 2.000000` | `release` | Delay in seconds before the client will resend the 'connect' attempt |
| `cl_retire_low_priority_lights` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Low priority dlights are replaced by high priority ones |
| `cl_sanitize_muted_players` | `Bool` | `true` |  | `clientdll` `release` | Hide names and avatars of muted players. |
| `cl_sanitize_player_names` | `Bool` | `false` |  | `clientdll` `archive` | Replace names of other players with something non-offensive. |
| `cl_sceneentity_debug` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Display all thinking scene entities and its data. |
| `cl_scoreboard_mouse_enable_binding` | `String` | `+attack2` |  | `clientdll` `archive` | Name of the binding to enable mouse selection in the scoreboard |
| `cl_scoreboard_survivors_always_on` | `Bool` | `false` |  | `clientdll` `archive` `release` |  |
| `cl_scoreboard_toggle_enable` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_screenmessage_notifytime` | `Float32` | `8.000000` |  | `developmentonly` `clientdll` `defensive` | How long to display screen message text |
| `cl_script_attach_debugger_at_startup` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_script_break_in_native_debugger_on_error` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_search_key_token` | `String` |  |  | `clientdll` `hidden` `release` | Development search key token. |
| `cl_sendtable_cache_filename` | `String` | `sendtables.bin` |  | `developmentonly` `defensive` | Send tables cache file |
| `cl_sequence_debug` | `Int32` | `-1` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_sequence_debug2` | `Int32` | `-1` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_sequence_model_substring` | `String` |  |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_server_graphic1_enable` | `Bool` | `true` |  | `clientdll` `release` | When enabled, 360x60 (&lt;16kb) image file will be displayed to on-server spectators. |
| `cl_server_graphic2_enable` | `Bool` | `true` |  | `clientdll` `release` | When enabled, 220x45 (&lt;16kb) image file will be displayed to on-server spectators. |
| `cl_session` | `String` |  |  | `developmentonly` `hidden` `server_can_execute` |  |
| `cl_show_bombs` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_show_camera_position` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_show_clan_in_death_notice` | `Bool` | `true` |  | `clientdll` `archive` `release` | Is set, the clan name will show next to player names in the death notices. |
| `cl_show_enemy_avatar_colors` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_show_equipment_value` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_show_equipped_character_for_player_avatars` | `Bool` | `false` |  | `clientdll` `archive` |  |
| `cl_show_head_trajectory` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` |  |
| `cl_show_matchmaking_stat_spew` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_show_observer_crosshair` | `Int32` | `2` |  | `clientdll` `archive` `release` | Show the crosshair of the player being observed. 0: off 1: friends and party 2: everyone |
| `cl_show_playernames_max_chars_console` | `Bool` | `false` |  | `developmentonly` `clientdll` | Shows all player names (including bots) as 16 W's. |
| `cl_show_quest_info` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cl_show_splashes` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `cl_showdemooverlay` | `Float32` | `0.000000` |  | `developmentonly` `defensive` | How often to flash demo recording/playback overlay (0 - disable overlay, -1 - show always) |
| `cl_showerror` | `Int32` | `0` |  | `clientdll` `release` | Show prediction errors, 2 for above plus detailed field deltas, 3 to filter out serverside known prediction errors, -entindex for specific entity. |
| `cl_showfps` | `Int32` | `0` |  | `clientdll` `release` | Draw fps meter at top of screen (1 = fps, 2 = smooth fps, 3 = server MS, 4 = Show FPS and Log to file ) |
| `cl_showframenumber` | `Bool` | `false` |  | `clientdll` `release` | Show current framenumber |
| `cl_showloadout` | `Bool` | `true` |  | `clientdll` `archive` `per_user` | Toggles display of current loadout. |
| `cl_showmem` | `Int32` | `0` |  | `clientdll` `release` | Draw approximate memory use at top of screen |
| `cl_showpos` | `Int32` | `0` |  | `clientdll` `cheat` `release` | Draw current position at top of screen |
| `cl_showtextmsg` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` | Enable/disable text messages printing on the screen. |
| `cl_showtick` | `Int32` | `0` |  | `clientdll` `release` | Show current tick/time values.  Bitmask:  1='render time'  2='GameTime'   4=time of predicted entities  8=offset of predicted entities    (-1 means 'everything') |
| `cl_showusercmd` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Show user command encoding |
| `cl_silencer_mode` | `Int32` | `0` |  | `clientdll` `archive` `userinfo` `per_user` | 0: cannot detach; 1: press secondary fire to detach |
| `cl_simulate_dormant_entities` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_skeleton_instance_smear_boneflags` | `Bool` | `false` |  | `clientdll` `cheat` | Smear boneflags across the model.  Costs computation, but tests to make sure your bone flags are consistent. |
| `cl_skip_hierarchy_update_for_unchanged_entities` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Skip updating hierarchy information in PostDataUpdate for entities that have not changed |
| `cl_skip_update_animations` | `Bool` | `false` |  | `developmentonly` `clientdll` | Enable to skip game animations |
| `cl_smoke_edge_feather` | `Float32` | `21.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `cl_smoke_lower_speed` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `cl_smoke_origin_height` | `Float32` | `68.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `cl_smoke_torus_ring_radius` | `Float32` | `61.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `cl_smoke_torus_ring_subradius` | `Float32` | `88.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `cl_smoke_volume_growth` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_smoke_volumeprop` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_smooth` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` | Smooth view/eye origin after prediction errors |
| `cl_smooth_draw_debug` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `cl_smooth_root_catchup_factor` | `Float32` | `0.210000` |  | `clientdll` `cheat` |  |
| `cl_smooth_root_max_accel` | `Float32` | `1000.000000` |  | `clientdll` `cheat` |  |
| `cl_smooth_root_origin_coeff` | `Float32` | `100.000000` |  | `clientdll` `cheat` |  |
| `cl_smooth_root_timehorizon` | `Float32` | `0.125000` |  | `clientdll` `cheat` |  |
| `cl_smooth_root_velocity_coeff` | `Float32` | `20.000000` |  | `clientdll` `cheat` |  |
| `cl_smooth_targetspeed` | `Float32` | `150.000000` |  | `clientdll` `release` |  |
| `cl_smoothtime` | `Float32` | `0.200000` | `0.010000 .. 2.000000` | `developmentonly` `clientdll` `defensive` | Smooth client's view after prediction error over this many seconds |
| `cl_snd_cast_clear` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `cl_snd_cast_retrigger` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `cl_snd_new_visualize` | `Bool` | `false` |  | `clientdll` `cheat` | Displays soundevent name played at it's 3d position |
| `cl_sniper_auto_rezoom` | `Bool` | `true` |  | `clientdll` `archive` `userinfo` `per_user` | Auto-rezoom snipers after a shot |
| `cl_sniper_delay_unscope` | `Bool` | `false` |  | `clientdll` `archive` `release` |  |
| `cl_sniper_show_inaccuracy` | `Bool` | `true` |  | `clientdll` `archive` `release` |  |
| `cl_spawngroup_log` | `Bool` | `false` |  | `developmentonly` | Dump the contents of the next spawngroup manifest to file. |
| `cl_spawngroup_spewresources` | `Bool` | `false` |  | `developmentonly` | Spew all manifest add/updates. |
| `cl_spec_show_bindings` | `Bool` | `true` |  | `clientdll` `release` `clientcmd_can_execute` | Toggle the visibility of the spectator bindings. |
| `cl_spec_stats` | `Bool` | `true` |  | `clientdll` `release` |  |
| `cl_spec_use_tournament_content_standards` | `Bool` | `false` |  | `clientdll` `release` |  |
| `cl_streams_image_sfurl` | `String` | `img://loadjpeg:(640x360):` |  | `developmentonly` `clientdll` | Format of Scaleform image representing the stream |
| `cl_streams_mytwitchtv_channel` | `String` | `http://www.twitch.tv/` |  | `developmentonly` `clientdll` | Twitch.tv account channel URL |
| `cl_streams_mytwitchtv_nolink` | `String` | `http://www.twitch.tv/settings/connections` |  | `developmentonly` `clientdll` | Twitch.tv account linking URL |
| `cl_streams_refresh_interval` | `Float32` | `300.000000` |  | `developmentonly` `clientdll` | How often to refresh streams list |
| `cl_streams_request_accept` | `String` | `application/vnd.twitchtv.v5+json` |  | `developmentonly` `clientdll` | Header for api request |
| `cl_streams_request_url` | `String` | `https://api.twitch.tv/helix/streams?game_id=32399&first=12` |  | `developmentonly` `clientdll` | Number of streams requested for display |
| `cl_streams_write_response_file` | `String` |  |  | `developmentonly` `clientdll` | When set will save streams info file for diagnostics |
| `cl_svc_usercmds_delta_validate` | `Bool` | `false` |  | `developmentonly` `clientdll` | Validate consistency of delta-encoded user commands.  Requires server to have sv_cq_validate_encoded_svc_usercmds enabled. |
| `cl_teamcounter_playercount_instead_of_avatars` | `Bool` | `false` |  | `clientdll` `archive` `release` |  |
| `cl_teamid_overhead_colors_show` | `Bool` | `true` |  | `clientdll` `archive` `release` | Show team overhead id in teammate color |
| `cl_teamid_overhead_fade_near_crosshair` | `Float32` | `0.500000` |  | `clientdll` `archive` `release` | The amount to fade teamid when near the crosshair. Range is 0.0-1.0. 0: off |
| `cl_teamid_overhead_maxdist` | `Int32` | `6000` |  | `clientdll` `cheat` `per_user` | max distance at which the overhead team id icons will show |
| `cl_teamid_overhead_maxdist_spec` | `Int32` | `4000` |  | `clientdll` `cheat` `per_user` | max distance at which the overhead team id icons will show when a spectator |
| `cl_teamid_overhead_mode` | `Int32` | `3` |  | `clientdll` `archive` `release` | Always show team id over teammates. 0 = off, 1 = pips; 2 = +name, 3 = +equipment |
| `cl_teammate_color_1` | `Color` | `136 206 245` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_teammate_color_2` | `Color` | `0 158 128` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_teammate_color_3` | `Color` | `241 228 65` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_teammate_color_4` | `Color` | `230 128 42` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_teammate_color_5` | `Color` | `189 44 150` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_teammate_colors_show` | `Int32` | `1` |  | `clientdll` `archive` `release` | In competitive, 1 = show teammates as separate colors in the radar, scoreboard, etc., 2 = show colors and letters |
| `cl_tickpacket_desired_queuelength` | `Float32` | `0.000000` | `0.000000 .. 5.000000` | `userinfo` | This value, multiplied by the tick interval, is added to cl_tickpacket_recvmargin_desired to obtain the effective desired recv margin. |
| `cl_tickpacket_recvmargin_adjust_limit` | `Float32` | `5.000000` |  | `developmentonly` | Recvmargin-based usercommand pacing will not speed up or slow down command pacing by more than N% compared to realtime |
| `cl_tickpacket_recvmargin_desired` | `Float32` | `5.000000` |  | `developmentonly` | Recvmargin-based usercommand pacing will try to maintain N ms margin between user command arriving at the server and the server needing that user command.  See also cl_tickpacket_desired_queuelength. |
| `cl_tickpacket_recvmargin_minsamples` | `Int32` | `10` |  | `developmentonly` | Recvmargin-based usercommand pacing will not take action unless we have N samples |
| `cl_tickpacket_recvmargin_spew_interval` | `Int32` | `0` |  | `release` |  |
| `cl_tickpacket_recvmargin_timeconstant` | `Float32` | `0.400000` |  | `developmentonly` | Recvmargin-based usercommand pacing will remove 63.2% of the error in N seconds |
| `cl_tickpacket_recvmargin_window` | `Float32` | `4.000000` |  | `developmentonly` | Recvmargin-based usercommand pacing will use past N seconds |
| `cl_ticks_net_print_threshold` | `Float32` | `2.000000` |  | `release` | Print a message if network issues cause problems with server snapshots of user commands not being available when needed, if the percentage (0...100) exceeds this value.  A value of 0 will cause the message to always print each time it is calculated |
| `cl_ticks_warning_level` | `Int32` | `0` |  | `release` | Print a message about problems with ticks and interpolation.  0=never, 1=warnings, 2=all, even if hidden by interpolation |
| `cl_timeout` | `Float32` | `30.000000` |  | `archive` | After this many seconds without receiving a packet from the server, the client will disconnect itself |
| `cl_tracer_frequency_override` | `Int32` | `1` |  | `developmentonly` `clientdll` | Override tracer frequency (-1 to disable) |
| `cl_tracer_whiz_distance` | `Float32` | `72.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_tracer_whiz_infront_distance` | `Float32` | `32.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_track_aim_head_log_closest` | `Bool` | `false` |  | `developmentonly` `clientdll` | Log when closest distance to head was reached and what it was |
| `cl_track_aim_head_threshold` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` | Notify render device when rendering a frame with enemy head within threshold distance |
| `cl_track_render_eye_angles` | `Bool` | `false` |  | `clientdll` `cheat` | Spew render eye angles |
| `cl_trueview_show_doa_predictions` | `Bool` | `true` |  | `clientdll` `release` | If true, trueview will recreate the original player experience, including commands that were predicted clientside but never executed on the server because the player was dead when they arrived. |
| `cl_trueview_show_status` | `Int32` | `2` |  | `clientdll` `release` | 0=Never; 1=Only if there is a problem; 2=always |
| `cl_ui_particles_destroy_when_not_painting` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `cl_use_entity_as_targetid` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_use_last_selected_weapon_slot_position` | `Bool` | `false` |  | `clientdll` `archive` `release` | Use the last selected weapon slot position when switching back to a weapon slot. |
| `cl_use_old_wearable_shoulddraw` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_use_opens_buy_menu` | `Bool` | `false` |  | `clientdll` `archive` `userinfo` `per_user` | Pressing the +use key will open the buy menu if in a buy zone (just as if you pressed the 'buy' key). |
| `cl_usercmd_dbg` | `Int32` | `0` |  | `developmentonly` | show usercmd payload sizing info for packets with more than this many usercmds |
| `cl_usercmd_max_per_movemsg` | `Int32` | `4` | `>= 4` | `release` | max number of CUserCmds to send in one client move message |
| `cl_usercmd_showsize` | `Bool` | `false` |  | `developmentonly` |  |
| `cl_usesocketsforloopback` | `Bool` | `false` |  | `developmentonly` `defensive` | When connecting to local listen server (for example, using the 'map' command), default to loopback=false, which connects to '127.0.0.1' instead of 'loopback'.  This uses the network stack so that fake lag/loss can be simulated. |
| `cl_versus_intro` | `Bool` | `true` |  | `clientdll` `archive` `release` |  |
| `cl_view_near_hud_player_eye_dist` | `Float32` | `20.000000` |  | `developmentonly` `clientdll` |  |
| `cl_view_near_other_player_eye_dist` | `Float32` | `16.000000` |  | `developmentonly` `clientdll` |  |
| `cl_viewing_vanity_loadout` | `Bool` | `false` |  | `gamedll` `clientdll` `userinfo` |  |
| `cl_viewmodelsclonedasworld` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `cl_voiceenabled` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_voip_lobby_audio_volume` | `Int32` | `0` | `0 .. 100` | `developmentonly` `clientdll` `hidden` | Lobby voip stream audio volume |
| `cl_vrr_recommendation_dont_show_again` | `Bool` | `false` |  | `clientdll` `archive` `release` |  |
| `cl_vsnd_morph_override_ease_enabled` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` | Controls whether the compiled in vsnd morph data ease in/out values are used or values set from the convars (cl_vsnd_morph_override_ease_in, cl_vsnd_morph_override_ease_out) are used |
| `cl_vsnd_morph_override_ease_in` | `Float32` | `0.200000` |  | `developmentonly` `clientdll` `defensive` | If cl_enable_vsnd_morph_override_ease_enabled is true, ease into vsnd morph driven animation over the specified number of seconds. |
| `cl_vsnd_morph_override_ease_out` | `Float32` | `0.200000` |  | `developmentonly` `clientdll` `defensive` | If cl_enable_vsnd_morph_override_ease_enabled is true, ease out of vsnd morph driven animation over the specified number of seconds. |
| `cl_wallbang_heavy_threshold` | `Int32` | `22` |  | `clientdll` `cheat` `release` | The Threshold where to switch from Light to Heavy Wallbang tracer |
| `cl_weapon_debug_print_accuracy` | `Bool` | `false` |  | `developmentonly` `clientdll` `replicated` |  |
| `cl_weapon_debug_show_accuracy` | `Int32` | `0` |  | `clientdll` `cheat` `release` | Draws a circle representing the effective range with every shot. |
| `cl_weapon_debug_show_accuracy_duration` | `Float32` | `10.000000` |  | `clientdll` `cheat` `release` |  |
| `cl_weapon_selection_rarity_color` | `Bool` | `false` |  | `clientdll` `archive` `release` |  |
| `cl_workshop_map_download_timeout` | `Float32` | `120.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `cl_yawspeed` | `Float32` | `210.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `clear_debug_flags_on_death` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `clientport` | `Int32` | `0` |  | `release` | If non-zero, client binds port to specific address.  Usually you should leave this blank to use a different random system-assigned port for each connection. |
| `closecaption` | `Bool` | `false` |  | `clientdll` `archive` `userinfo` | Enable close captioning. |
| `cloth_debug_draw` | `Int32` | `0` |  | `developmentonly` `clientdll` |  |
| `cloth_filter_transform_stateless` | `Bool` | `false` |  | `developmentonly` `defensive` | Enable the new, stateless version of FilterTransform |
| `cloth_ground_plane_thickness` | `Float32` | `3.000000` |  | `developmentonly` `defensive` | Raise ground by this much for all cloth that traces the ground; should be 0 ideally |
| `cloth_hudmodel_presettle` | `Int32` | `0` |  | `developmentonly` `clientdll` |  |
| `cloth_hudmodel_presettle_log` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cloth_interp_rot` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cloth_iv_dump` | `Int32` | `4` |  | `developmentonly` `clientdll` `defensive` |  |
| `cloth_iv_store_back` | `Bool` | `false` |  | `developmentonly` `clientdll` `replicated` `defensive` |  |
| `cloth_sim_on_tick` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `cloth_smooth_motion_correct` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `cloth_smooth_motion_extrapolate` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` |  |
| `cloth_update` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `cojob_lock_hold_warning_threshold_ms` | `Int32` | `10000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | How long in milliseconds before we warn about lock hold duration |
| `cojob_max_no_yield_time_us` | `UInt32` | `3000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Will spew if a job takes longer than the specified number of microseconds |
| `commentary` | `Bool` | `false` |  | `gamedll` `archive` | Desired commentary mode state. |
| `commentary_available` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | Automatically set by the game when a commentary file is available for the current map. |
| `commentary_node_use_viewfacing` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `composite_material_cache_count_max` | `Int32` | `24` |  | `developmentonly` `clientdll` |  |
| `composite_material_dump_images` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `composite_material_save_to_disk` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `composite_material_use_bc7` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `composite_material_use_gpu` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `composite_material_use_gpu_endpoint_optimization` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `composite_material_use_gpu_perceptual_error_metric` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `compositematerial_showdebugwindow` | `Bool` | `false` |  | `developmentonly` `clientdll` `archive` `replicated` `cheat` `menubar_item` | Source2/Composite Material Debug |
| `con_enable` | `Bool` | `false` |  | `archive` `per_user` | Allows the console to be activated. |
| `con_logfile_suffix` | `String` |  |  | `developmentonly` `defensive` | Suffix to append to the console log, may be changed to reopen the log |
| `connect_lobby` | `UInt64` | `0` |  | `developmentonly` `clientdll` `hidden` `defensive` | Sets the lobby ID to connect to on start. |
| `contributionscore_assist` | `Int32` | `1` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score added for an assist |
| `contributionscore_assist_reqs` | `Int32` | `0` |  | `gamedll` `release` `commandline_enforced` | extra requirements to earn contribution score for an assist |
| `contributionscore_bomb_defuse_major` | `Int32` | `3` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score for defusing a bomb while at least one enemy remains alive |
| `contributionscore_bomb_defuse_minor` | `Int32` | `1` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score for defusing a bomb after eliminating enemy team |
| `contributionscore_bomb_exploded` | `Int32` | `1` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score awarded to bomb planter and terrorists remaining alive if bomb explosion wins the round |
| `contributionscore_bomb_planted` | `Int32` | `2` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score for planting a bomb |
| `contributionscore_cash_bundle` | `Int32` | `0` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score for picking up a cash bundle |
| `contributionscore_crate_break` | `Int32` | `0` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score for breaking an item crate |
| `contributionscore_hostage_kill` | `Int32` | `-2` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score for killing a hostage, normally negative |
| `contributionscore_hostage_rescue_major` | `Int32` | `3` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score added to rescuer per hostage rescued |
| `contributionscore_hostage_rescue_minor` | `Int32` | `1` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score added to all alive CTs per hostage rescued |
| `contributionscore_kill` | `Int32` | `2` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score added for a kill |
| `contributionscore_kill_factor` | `Float32` | `0.000000` |  | `gamedll` `release` `commandline_enforced` | percentage of victim's contribution score to award to their killer as a bonus |
| `contributionscore_kill_reqs` | `Int32` | `0` |  | `gamedll` `release` `commandline_enforced` | extra requirements to earn contribution score for a kill |
| `contributionscore_objective_kill` | `Int32` | `3` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score added for an objective related kill |
| `contributionscore_participation` | `Int32` | `0` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score awarded to players for active participation in the round |
| `contributionscore_suicide` | `Int32` | `-2` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score for a suicide, normally negative |
| `contributionscore_team_kill` | `Int32` | `-2` |  | `gamedll` `release` `commandline_enforced` | amount of contribution score for a team kill, normally negative |
| `convars_echo_toggle_changes` | `Bool` | `true` |  | `developmentonly` `defensive` | Echo to the console changes caused by toggling. |
| `cpu_level` | `Int32` | `2` |  | `developmentonly` `clientdll` `defensive` | CPU Level - Default: High |
| `cq_buffer_bloat_msecs_max` | `Float32` | `150.000000` |  | `replicated` `release` | Server will not allow the client to buffer up more than N ms of commands. |
| `cq_debug` | `Int32` | `0` |  | `developmentonly` `gamedll` `replicated` `defensive` | Verbose command queue logging. |
| `cq_dilation_percentage` | `Float32` | `5.000000` | `0.100000 .. 10.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | When speeding up slowing down, this is how much |
| `cq_enable` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Run one usercmd per server tick and maintain a buffer.  Client speeds up/slows down it's usercmd tick rate to maintain server command queue buffering. |
| `cq_fake_starve` | `Int32` | `0` |  | `developmentonly` `gamedll` | if set, starve this many commands by discarding during process usercmds. |
| `cq_logging` | `Bool` | `false` |  | `gamedll` `release` | command queue logging of events. |
| `cq_logging_interval` | `Float32` | `0.000000` |  | `gamedll` `release` | command queue logging per player stats every N seconds, 0 to disable. |
| `cq_max_starved_substitute_commands` | `Int32` | `4` |  | `gamedll` `release` | Server will stop generating substitute commands if client hasn't sent one, after N in a row |
| `cq_print_every_command` | `Bool` | `false` |  | `gamedll` `release` | print every command as we execute it |
| `cq_runtests` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `cq_runtests_broadcast_info` | `Bool` | `false` |  | `developmentonly` `gamedll` | send message to remote client console when tests change. |
| `cq_runtests_interval` | `Float32` | `30.000000` |  | `developmentonly` `gamedll` |  |
| `crosshair` | `Bool` | `true` |  | `clientdll` `archive` `per_user` |  |
| `cs2_bomb_damage_showdebugwindow` | `Bool` | `false` |  | `developmentonly` `clientdll` `archive` `replicated` `cheat` `menubar_item` | CSGO/Bomb Damage |
| `cs_AssistDamageThreshold` | `Int32` | `25` |  | `developmentonly` `gamedll` | cs_AssistDamageThreshold defines the amount of damage needed to score an assist |
| `cs_ShowStateTransitions` | `Int32` | `-2` |  | `gamedll` `cheat` | cs_ShowStateTransitions &lt;ent index or -1 for all&gt;. Show player state transitions. |
| `cs_hostage_near_rescue_music_distance` | `Float32` | `2000.000000` |  | `gamedll` `cheat` |  |
| `cs_logtouchexpansion` | `Int32` | `-2` |  | `gamedll` `cheat` | cs_logtouchexpansion &lt;ent index or -1 for all&gt;. Log player touch expansion component. |
| `cs_minimap_create_output_size` | `Int32` | `1024` |  | `clientdll` `release` | Size of minimap texture generated with cs_minimap_create (512 default) |
| `cs_minimap_renderdoc_capture_enabled` | `Bool` | `false` |  | `developmentonly` `clientdll` `hidden` `cheat` |  |
| `cs_minimap_rendering_msaa_mode` | `Int32` | `2` |  | `developmentonly` `clientdll` `cheat` | MSAA mode used for minimap rendering 0-none, 1-2xMSAA, 2-4xMSAA, 3-6X, 4-8X, etc |
| `cs_steamvideo_max_kills_per_multikill` | `Int32` | `5` |  | `developmentonly` `clientdll` | Max number of kills for a single multikill event |
| `cs_steamvideo_max_time_between_multikill_events` | `Float32` | `5.000000` |  | `developmentonly` `clientdll` | Maximum time in seconds between consecutive kills for them to be combined into a multikill event |
| `cs_steamvideo_multikill_padding_time` | `Float32` | `2.000000` |  | `developmentonly` `clientdll` | Time in seconds to add before the first kill and after the last kill for multikill events |
| `csgo_3d_skybox` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `csgo_demoui_playbeck_timestep_value` | `Int32` | `15` |  | `developmentonly` `clientdll` `defensive` | Number of seconds to seek when using TimeStep buttons on demo playback controller. |
| `csgo_demoui_player_death_seek_lead_up_time` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `defensive` | Seek to a moment this amount of seconds leading up to a player death instead of the exact time of the death. |
| `csgo_demoui_previous_event_search_offset` | `Float32` | `2.000000` |  | `developmentonly` `clientdll` `defensive` | Do not consider events that happened in the last specified number of seconds when a user clicks 'previous' on the UI. |
| `csgo_disable_preview_maps` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `csgo_fatdemo_enable` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `csgo_fatdemo_output` | `String` | `test.fatdem` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `csgo_map_preview_scale` | `Float32` | `0.000000` |  | `clientdll` `archive` |  |
| `csgo_nav_jump_link_detour_threshold` | `Float32` | `1500.000000` |  | `developmentonly` `gamedll` `replicated` `defensive` | don't traverse a jump link if there's a detour that costs less than this amount |
| `csgo_use_fullsort_for_opaque` | `Bool` | `true` |  | `clientdll` `cheat` | fullsort the opaque pass when there wasn't a depth prepass |
| `csm_bias_override_0` | `Float32` | `1.000000` |  | `clientdll` `cheat` |  |
| `csm_bias_override_1` | `Float32` | `1.000000` |  | `clientdll` `cheat` |  |
| `csm_bias_override_2` | `Float32` | `1.000000` |  | `clientdll` `cheat` |  |
| `csm_bias_override_3` | `Float32` | `1.000000` |  | `clientdll` `cheat` |  |
| `csm_cascade0_override_dist` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `csm_cascade1_override_dist` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `csm_cascade2_override_dist` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `csm_cascade3_override_dist` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `csm_cascade_viewdir_shadow_bias_scale` | `Float32` | `2.000000` |  | `clientdll` `cheat` |  |
| `csm_max_dist_between_caster_and_receiver` | `Float32` | `15000.000000` |  | `clientdll` `cheat` | default pushback |
| `csm_max_num_cascades_override` | `Int32` | `-1` |  | `developmentonly` `clientdll` `defensive` | Number of cascades in sunlight shadow |
| `csm_max_shadow_dist_override` | `Float32` | `-1.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `csm_max_visible_dist` | `Float32` | `7500.000000` |  | `clientdll` `cheat` |  |
| `csm_res_override_0` | `UInt32` | `0` |  | `clientdll` `cheat` |  |
| `csm_res_override_1` | `UInt32` | `0` |  | `clientdll` `cheat` |  |
| `csm_res_override_2` | `UInt32` | `0` |  | `clientdll` `cheat` |  |
| `csm_res_override_3` | `UInt32` | `0` |  | `clientdll` `cheat` |  |
| `csm_shadow_worldview_align_x_to_u` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `csm_shadow_worldview_shear_align_z_to_v` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `csm_sst_max_visible_dist` | `Float32` | `2000.000000` |  | `clientdll` `cheat` |  |
| `csm_sst_pushback_distance` | `Float32` | `1500.000000` |  | `clientdll` `cheat` | default pushback |
| `csm_sst_shadow_focus_region_maxz` | `Float32` | `2000.000000` |  | `clientdll` `cheat` |  |
| `csm_sst_shadow_focus_region_minz` | `Float32` | `-2000.000000` |  | `clientdll` `cheat` |  |
| `csm_sst_shadow_focus_region_thin_compensation` | `Float32` | `1500.000000` |  | `clientdll` `cheat` |  |
| `csm_viewdir_shadow_bias` | `Float32` | `0.000000` |  | `clientdll` `cheat` |  |
| `csm_viewmodel_max_shadow_dist` | `Float32` | `21.000000` |  | `clientdll` `cheat` |  |
| `csm_viewmodel_max_visible_dist` | `Float32` | `1000.000000` |  | `clientdll` `cheat` |  |
| `csm_viewmodel_nearz` | `Float32` | `0.500000` |  | `clientdll` `cheat` |  |
| `csm_viewmodel_shadows` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `custom_bot_difficulty` | `Int32` | `2` |  | `gamedll` `clientdll` `replicated` `release` | Bot difficulty for offline play. |
| `cv_bot_ai_bt_debug_target` | `Int32` | `-1` |  | `gamedll` `replicated` `cheat` | Draw the behavior tree of the given bot. |
| `cv_bot_ai_bt_hiding_spot_show` | `Bool` | `false` |  | `gamedll` `replicated` `cheat` | Draw hiding spots. |
| `cv_bot_ai_bt_moveto_show_next_hiding_spot` | `Bool` | `false` |  | `gamedll` `replicated` `cheat` | Draw the hiding spot the bot will check next. |
| `damage_impact_heavy` | `Int32` | `40` |  | `developmentonly` `clientdll` `defensive` | Damage ABOVE this value is considered heavy damage |
| `damage_impact_medium` | `Int32` | `20` |  | `developmentonly` `clientdll` `defensive` | Damage BELOW this value is considered light damage |
| `death_chase_distance` | `Float32` | `76.000000` |  | `developmentonly` `clientdll` |  |
| `death_panel_delay_time` | `Float32` | `0.250000` |  | `developmentonly` `clientdll` |  |
| `death_panel_travel_time` | `Float32` | `0.250000` |  | `developmentonly` `clientdll` |  |
| `debug_aim_angle` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `debug_async_data_panel_override_state` | `Int32` | `-1` |  | `developmentonly` `clientdll` | Force ALL async data panels to be in a specific state. -1:disabled, 0:failure, 1:loading, 2:success |
| `debug_chicken` | `Bool` | `false` |  | `developmentonly` `gamedll` | Chicken debug info |
| `debug_destructible_parts` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Draw debug information for destructible parts. |
| `debug_destructible_parts_enabled` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` | Toggle enabling/disabling the destructible parts system for debug. |
| `debug_destructible_parts_radius_damage` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `debug_destructible_parts_ttl` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | How long the debug draws stick around for, unless they're per-tick. |
| `debug_draw_enable` | `Bool` | `true` |  | `developmentonly` `replicated` |  |
| `debug_error_model` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `debug_font_name` | `String` | `Courier New` |  | `developmentonly` `defensive` | Debug font name |
| `debug_font_size` | `Int32` | `14` |  | `developmentonly` `defensive` | Font size for the debug font |
| `debug_hltv` | `Int32` | `0` |  | `developmentonly` `clientdll` `replicated` `clientcmd_can_execute` | Print out hltv events |
| `debug_overlay_fullposition` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `debug_physimpact` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `debug_radial_damage` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `debug_shared_random` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `debug_takedamage_summaries` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `debug_video_config_cvars` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `debug_visibility_monitor` | `Int32` | `0` |  | `gamedll` `cheat` |  |
| `debugoverlay_circle_verts` | `Int32` | `24` |  | `cheat` |  |
| `debugoverlay_enable_dotted_dashed` | `Bool` | `true` |  | `cheat` | Toggle the use of dotted/dashed debugoverlay lines to indicate source |
| `debugoverlay_force_respect_ttl` | `Bool` | `false` |  | `cheat` | Force respect TTL even when clearing scopes |
| `debugoverlay_show_text_outline` | `Bool` | `false` |  | `cheat` | Toggle display of box around text |
| `debugoverlay_text_scale` | `Float32` | `1.000000` |  | `archive` `cheat` | Scale of the text used for 3d display, but see also debug_font_{size,name} |
| `decalfrequency` | `Float32` | `10.000000` |  | `developmentonly` `gamedll` `notify` `defensive` |  |
| `default_fov` | `Float32` | `90.000000` |  | `clientdll` `cheat` |  |
| `demo_allow_game_mismatch` | `Bool` | `false` |  | `developmentonly` `defensive` | Allow playback of demo even if game directories are not matched [may crash or fail to load]. |
| `demo_debug` | `Int32` | `0` |  | `developmentonly` | Turn on demo debug spew. |
| `demo_flush` | `Bool` | `false` |  | `archive` | Flush writing the demo file every network update |
| `demo_highlight_fade_duration` | `Float32` | `0.250000` |  | `clientdll` `release` | Duration of the fade in and of the fade out transitions (fade in + fade out is 2x this value). |
| `demo_highlight_seconds_after` | `Float32` | `2.000000` |  | `clientdll` `release` | How many seconds after the actual highlight event to show when viewing highlights. |
| `demo_highlight_seconds_before` | `Float32` | `6.000000` |  | `clientdll` `release` | How many seconds before the actual highlight event to show when viewing highlights. |
| `demo_max_consecutive_skip_packets` | `Int32` | `100` |  | `developmentonly` `defensive` | Don't skip more than N messages in a row when skipping in a demo file. |
| `demo_mouse_enable_binding` | `String` | `drop` |  | `clientdll` `archive` | Name of the binding to enable mouse on demo playback UI |
| `demo_pause_at_end` | `Bool` | `true` |  | `clientdll` `release` | Pause demo playback when the end of the file is reached, otherwise quit to main menu. |
| `demo_playback_override_settings` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `demo_quitafterplayback` | `Bool` | `false` |  | `release` | Quits game after demo playback. |
| `demo_recordcommands` | `Bool` | `true` |  | `cheat` | Record commands typed at console into .dem files. |
| `demo_skip_to_shot_seconds_before` | `Float32` | `2.000000` |  | `clientdll` `release` | How many seconds before the shot to skip to when skipping to a specific shot ID. |
| `demo_ui_mode` | `Int32` | `2` |  | `clientdll` `release` | UI mode for demo playback. 0 = disabled, 1 = minimal, 2 = full |
| `demo_usefastgoto` | `Bool` | `true` |  | `developmentonly` `defensive` | Use fast frame skipping when available for demo_goto commands. |
| `demo_writefullupdate_rate` | `Int32` | `60` |  | `developmentonly` `defensive` | Interval time in seconds to write full updates to demo. |
| `destructible_parts_destroy_parts_when_gibbing` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `dev_add_onground_on_spawn` | `Bool` | `false` |  | `gamedll` `release` | Should we mess with the ground flag when we spawn? (I don't think we should). If we don't hit the assert in CCSPlayer_MovementServices::ProcessMovement, we should remove this by Dec 2022. |
| `dev_create_bhop_reports` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Whether we should create bhop reports when you jump. Reports are created for the client and server and are numbered monotonically |
| `dev_create_move_report` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Whether we should create move reports when you push movement keys. Reports are created for the server and are numbered monotonically |
| `dev_create_sensitivity_report` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` |  |
| `dev_create_smooth_motion_report` | `Bool` | `false` |  | `developmentonly` `clientdll` `replicated` `cheat` |  |
| `dev_cs_force_disable_move` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` | forcibly prevent players from moving |
| `dev_cs_frame_firing_enable` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Enable that firing will pretend like it's happening on frames. |
| `dev_cs_frame_firing_insert_idle_pose_now` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Should we insert the idle pose at this time to make the animation interpolation punchier? |
| `dev_cs_frame_firing_play_animevents` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Should we play the animevents that animgraph will skip over? |
| `dev_cs_frame_firing_skip_first_frame_enable` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Should we skip the first frame of shooting to make the animation punchier? |
| `dev_cs_frame_firing_tick_offset_enable` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Should we offset the current frame to the tick |
| `dev_cs_ragdoll_head_ankle_delta_z_threshold` | `Float32` | `35.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `dev_cs_ragdoll_nudge_intensity` | `Float32` | `500.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `dev_cs_ragdoll_nudge_max_duration` | `Float32` | `1.500000` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `dev_cs_ragdoll_progress_check_interval` | `Float32` | `0.250000` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `dev_reportmoneychanges` | `Bool` | `false` |  | `developmentonly` `gamedll` `replicated` | Displays money account changes for players in the console |
| `developer` | `Int32` | `0` |  | `release` | Set developer message level. |
| `devonly_chicken_activity_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` | Print chicken activity info to the console |
| `devonly_chicken_blocktimer` | `Float32` | `0.200000` |  | `developmentonly` `gamedll` | Chicken blockertimer |
| `devonly_chicken_feeler_distance` | `Float32` | `30.000000` |  | `developmentonly` `gamedll` | Chicken feeler distance |
| `devonly_chicken_feeler_height` | `Float32` | `5.000000` |  | `developmentonly` `gamedll` | Chicken feeler height |
| `devonly_chicken_feeler_pitch` | `Float32` | `45.000000` |  | `developmentonly` `gamedll` | Chicken feeler pitch |
| `diffcheck` | `Bool` | `true` |  | `developmentonly` `defensive` | Activate diffcheck system. |
| `diffcheck_playerslot` | `Int32` | `0` |  | `developmentonly` `defensive` |  |
| `diffcheck_spew` | `Bool` | `true` |  | `developmentonly` `defensive` | Actually show diffcheck results. |
| `diffcheck_spew_diff_filter` | `String` |  |  | `developmentonly` `defensive` | Show diff with matching filter substring only. |
| `diffcheck_spew_diff_only` | `Bool` | `false` |  | `developmentonly` `defensive` | Show diff only. |
| `disable_dynamic_prop_loading` | `Bool` | `false` |  | `gamedll` `cheat` | If non-zero when a map loads, dynamic props won't be loaded |
| `disable_source_soundscape_trace` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | Bypasses lookup of soundscapes for indvidual audio sources when enabled. |
| `display_convars_onscreen_in_big_text` | `String` |  |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Display the convars on the screen in big text. Use semicolons to separate multiple convars |
| `display_game_events` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `dota_enable_spatial_audio` | `Bool` | `false` |  | `release` | Flag to enable spatial audio in Dota 2. |
| `dota_spatial_audio_mix` | `Float32` | `1.000000` |  | `release` | Mix value to blend spatial and non-spatial audio in Dota 2. |
| `dsp_automatic` | `Int32` | `0` |  | `developmentonly` `demo` `defensive` |  |
| `dsp_db_min` | `Int32` | `80` |  | `developmentonly` `demo` `defensive` |  |
| `dsp_db_mixdrop` | `Float32` | `0.500000` |  | `developmentonly` `demo` `defensive` |  |
| `dsp_dist_max` | `Float32` | `1440.000000` |  | `cheat` `demo` |  |
| `dsp_dist_min` | `Float32` | `0.000000` |  | `cheat` `demo` |  |
| `dsp_mix_max` | `Float32` | `0.800000` |  | `developmentonly` `demo` `defensive` |  |
| `dsp_mix_min` | `Float32` | `0.200000` |  | `developmentonly` `demo` `defensive` |  |
| `dsp_off` | `Bool` | `false` |  | `cheat` |  |
| `dsp_vol_2ch` | `Float32` | `1.000000` |  | `developmentonly` `demo` `defensive` |  |
| `dsp_vol_4ch` | `Float32` | `0.500000` |  | `developmentonly` `demo` `defensive` |  |
| `dsp_vol_5ch` | `Float32` | `0.500000` |  | `developmentonly` `demo` `defensive` |  |
| `dsp_volume` | `Float32` | `0.800000` |  | `archive` `demo` |  |
| `dump_audio_input` | `Bool` | `false` |  | `developmentonly` |  |
| `econ_debug_loadout_ui` | `Bool` | `false` |  | `developmentonly` `clientdll` | Show debug data when players change their loadout. |
| `econ_enable_inventory_images` | `Bool` | `true` |  | `developmentonly` `clientdll` | allow inventory image rendering for use by scaleform |
| `econ_inventory_image_pinboard` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `enable_boneflex` | `Bool` | `true` |  | `clientdll` `archive` |  |
| `engine_accurate_input_processing_delta_time` | `Bool` | `false` |  | `developmentonly` `defensive` | When true, elapsed time given to the input processing will be the time elapsed since the last input processing. This is only relevant when input is processed multiple times per frame ( i.e. multiple ticks per frame) |
| `engine_allow_multiple_simulates_per_frame` | `Bool` | `false` |  | `developmentonly` `defensive` | When the client is catching up in low frame rate situations, should we run client simulate more than once a frame? |
| `engine_allow_multiple_ticks_per_frame` | `Bool` | `true` |  | `developmentonly` `defensive` | When the client is catching up in low frame rate situations, should we run tick more than once a frame? |
| `engine_client_tick_pad_enable` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `engine_cpu_info_extended` | `String` |  |  | `developmentonly` `defensive` | CPU the engine is running on. |
| `engine_frametime_amnesty_debug` | `Bool` | `false` |  | `developmentonly` `defensive` | Enable logging about events that disable frame time warnings |
| `engine_frametime_warnings_enable` | `Bool` | `true` |  | `developmentonly` `defensive` | Enable framerate-related warnings, such as sv_long_frame_ms.  Disabling warnings is useful when running in situations such a debug where a slow frame rate is expected |
| `engine_low_latency_sleep_after_client_tick` | `Bool` | `false` |  | `release` | When r_low_latency is enabled, this moves the low latency sleep on tick frames to happen after client simulation. |
| `engine_max_resource_system_update_time` | `Int32` | `5` |  | `developmentonly` `defensive` |  |
| `engine_max_ticks_to_simulate` | `Int32` | `-1` |  | `developmentonly` `defensive` | Max number of ticks to simulate per frame, after which simulation will start to slow down compared to real time. |
| `engine_no_focus_sleep` | `Int32` | `20` |  | `archive` |  |
| `engine_no_focus_sleep_vconsole_suppress` | `Bool` | `true` |  | `developmentonly` `defensive` | When VConsole is in the foreground, don't trigger engine_no_focus_sleep behavior |
| `engine_ostype` | `String` |  |  | `developmentonly` `defensive` | OS type the engine is running on. |
| `engine_phys_debug_limit_ticks` | `Bool` | `true` |  | `developmentonly` |  |
| `engine_platform_name_extended` | `String` |  |  | `developmentonly` `defensive` | Platform the engine is running on. |
| `engine_relaunch_app_before_exiting` | `Bool` | `false` |  | `hidden` `release` | Use this to tell Steam to relaunch the app right after existing |
| `engine_render_only` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `engine_rendersystem_init` | `String` |  |  | `developmentonly` `defensive` | Rendersystem option requested (changing this does not change the rendersystem). |
| `engine_rendersystem_shader_model` | `Int32` | `0` |  | `developmentonly` `defensive` | Rendersystem shader model in use (changing this does not change the shader model). |
| `engine_rendersystem_used` | `String` |  |  | `developmentonly` `defensive` | Rendersystem option in use (changing this does not change the rendersystem). |
| `engine_show_frame_dispatch` | `Bool` | `false` |  | `developmentonly` | show frame dispatch names. |
| `engine_show_frame_pacing` | `Bool` | `false` |  | `release` |  |
| `engine_show_frame_ticks` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `engine_sse42` | `Bool` | `true` |  | `developmentonly` `defensive` | turn on sse4.2 optimizations in the engine |
| `engine_update_resource_system_during_low_latency_sleep` | `Bool` | `true` |  | `developmentonly` |  |
| `english` | `Bool` | `true` |  | `clientdll` `userinfo` | If set to 1, running the english language set of assets. |
| `ent_actornames_font` | `String` | `Consolas` |  | `gamedll` `clientdll` `replicated` `cheat` | ent_actornames font name |
| `ent_actornames_fontsize` | `Int32` | `24` |  | `gamedll` `clientdll` `replicated` `cheat` | ent_actornames font size |
| `ent_attachment_filter_substrings` | `String` |  |  | `gamedll` `cheat` | If an attachment's name has any of the given substrings in it, it will be displayed. Substrings can be delimited by the ',' or '\|' character. |
| `ent_bitvec_enable` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `ent_debug_draw_thinkers` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `ent_joint_axis_size` | `Float32` | `4.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `ent_joint_filter_name` | `String` |  |  | `gamedll` `cheat` | If a joint's entire name matches (case insensitive), it will be displayed. |
| `ent_joint_filter_substrings` | `String` |  |  | `gamedll` `cheat` | If a joint's name has any of the given substrings in it, it will be displayed. Substrings can be delimited by the ',' or '\|' character. |
| `ent_joint_lines` | `Bool` | `true` |  | `gamedll` `cheat` | Draw a line between a rendered joint and its parent. |
| `ent_joint_names` | `Bool` | `true` |  | `gamedll` `cheat` | Draw the name of a rendered joint. |
| `ent_joint_only_ik_joints` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `ent_joint_use_bind_pose` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `ent_messages_draw` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` | Visualizes all entity input/output activity. |
| `ent_pivot_size` | `Float32` | `20.000000` |  | `gamedll` `archive` `cheat` |  |
| `ent_revert_dormancy_change` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `ent_show_contexts` | `Bool` | `false` |  | `gamedll` `cheat` | Show entity contexts in ent_text display |
| `ent_showonlyattachment` | `String` |  |  | `gamedll` `cheat` |  |
| `ent_skeleton_duration` | `Float32` | `0.000000` |  | `gamedll` `clientdll` `replicated` `cheat` | Duration of ent_skeleton display |
| `ent_skeleton_only_ik_joints` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `ent_skeleton_snapshot` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `ent_steadystate_batchsize` | `Int32` | `20` |  | `developmentonly` `gamedll` `defensive` | Max number of entities to transmit to player |
| `ent_steadystate_delay` | `Float32` | `5.000000` |  | `developmentonly` `gamedll` `defensive` | Time in seconds without network state changes until an entity is considered for trickle updates |
| `ent_steadystate_enable` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `ent_steadystate_interval` | `Float32` | `0.100000` |  | `developmentonly` `gamedll` `defensive` | Rate at which entities can be trickled to players |
| `ent_test_interpolation` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `ent_text_flags_active` | `Int32` | `-1` |  | `gamedll` `archive` `cheat` |  |
| `ent_text_no_name_really_i_mean_it` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `entity_log_load_unserialize` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `cheat` | Output unserialization of entities on map load. 0 - off, 1 - client/server, 2 - server, 3 - client |
| `eom_local_player_defeat_anim_enabled` | `Bool` | `true` |  | `clientdll` `archive` `release` |  |
| `execute_command_every_frame` | `String` |  |  | `cheat` |  |
| `fade_debug_splitscreen_slot` | `Int32` | `-1` |  | `developmentonly` `clientdll` `defensive` |  |
| `ff_damage_bullet_penetration` | `Float32` | `0.000000` | `0.000000 .. 1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If friendly fire is off, this will scale the penetration power and damage a bullet does when penetrating another friendly player |
| `ff_damage_decoy_explosion` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | Enables or disables team damage from decoy detonation |
| `ff_damage_reduction_bullets` | `Float32` | `0.100000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How much to reduce damage done to teammates when shot.  Range is from 0 - 1 (with 1 being damage equal to what is done to an enemy) |
| `ff_damage_reduction_grenade` | `Float32` | `0.250000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How much to reduce damage done to teammates by a thrown grenade.  Range is from 0 - 1 (with 1 being damage equal to what is done to an enemy) |
| `ff_damage_reduction_grenade_self` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How much to damage a player does to himself with his own grenade.  Range is from 0 - 1 (with 1 being damage equal to what is done to an enemy) |
| `ff_damage_reduction_other` | `Float32` | `0.250000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How much to reduce damage done to teammates by things other than bullets and grenades.  Range is from 0 - 1 (with 1 being damage equal to what is done to an enemy) |
| `filesystem_buffer_size` | `Int32` | `0` |  | `developmentonly` `defensive` | Size of per file buffers. 0 for none |
| `filesystem_fake_latency` | `Int32` | `0` |  | `developmentonly` `defensive` |  |
| `filesystem_max_stdio_read` | `Int32` | `16` |  | `developmentonly` `defensive` |  |
| `filesystem_native` | `Bool` | `true` |  | `developmentonly` `defensive` | Use native FS or STDIO |
| `filesystem_report_buffered_io` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `filesystem_unbuffered_io` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `filter_player_simulation_time` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `fire_use_modifier` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `fish_debug` | `Bool` | `false` |  | `clientdll` `cheat` | Show debug info for fish |
| `fish_dormant` | `Bool` | `false` |  | `gamedll` `replicated` `cheat` | Turns off interactive fish behavior. Fish become immobile and unresponsive. |
| `fog_color` | `Vector3` | `-1.000000 -1.000000 -1.000000` |  | `clientdll` `cheat` |  |
| `fog_colorskybox` | `Vector3` | `-1.000000 -1.000000 -1.000000` |  | `clientdll` `cheat` |  |
| `fog_enable` | `Bool` | `true` |  | `clientdll` `cheat` | Enable fog |
| `fog_enableskybox` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `fog_end` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `fog_endskybox` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `fog_hdrcolorscale` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `fog_hdrcolorscaleskybox` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `fog_maxdensity` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `fog_maxdensityskybox` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `fog_override` | `Int32` | `0` |  | `clientdll` `cheat` | Overrides the map's fog settings (-1 populates fog_ vars with map's values) |
| `fog_override_enable` | `Bool` | `false` |  | `cheat` | Use fog_override convars instead of world fog data |
| `fog_override_end` | `Float32` | `3500.000000` |  | `cheat` |  |
| `fog_override_exponent` | `Float32` | `2.000000` |  | `cheat` |  |
| `fog_override_max_density` | `Float32` | `0.400000` |  | `cheat` |  |
| `fog_override_start` | `Float32` | `1000.000000` |  | `cheat` |  |
| `fog_start` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `fog_startskybox` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `fog_volume_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | If enabled, prints diagnostic information about the current fog volume |
| `font_show_glyph_miss` | `Bool` | `false` |  | `developmentonly` |  |
| `footstep_audible_threshold` | `Float32` | `0.550000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `footstep_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `footstep_force_volume` | `Float32` | `-1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `force_spectator_only_tools` | `Bool` | `false` |  | `developmentonly` `clientdll` `hidden` `cheat` |  |
| `fov_cs_debug` | `Float32` | `0.000000` |  | `clientdll` `cheat` | Sets the view fov if cheats are on. |
| `fov_cs_near_z` | `Float32` | `6.500000` |  | `developmentonly` `clientdll` `cheat` |  |
| `fov_cs_super_ultrawide_near_z` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `cheat` |  |
| `fov_cs_ultrawide_near_z` | `Float32` | `4.000000` |  | `developmentonly` `clientdll` `cheat` |  |
| `fov_desired` | `Float32` | `75.000000` | `1.000000 .. 135.000000` | `clientdll` `archive` `userinfo` | Sets the base field-of-view. |
| `fps_max` | `Float32` | `120.000000` |  | `archive` `release` | Frame rate limiter.  0=no limit.  Does not apply to dedicated server. |
| `fps_max_tools` | `Float32` | `120.000000` |  | `archive` | Additional frame rate limit while in tools mode and a window other than the game window has focus. Note that fps_max still applies, this only allows the maximum frame rate for tools mode to be lower. 0=no tools specific limit. |
| `fps_max_ui` | `Float32` | `0.000000` |  | `archive` | Frame rate limiter while the game UI is displayed.  0=no limit.  Does not apply to dedicated server. |
| `frag_grenade_blip_frequency` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `freecamera_accel` | `Float32` | `5.000000` |  | `developmentonly` `clientdll` `defensive` | Tweak this parameter to adjust Free Camera movement acceleration. |
| `freecamera_fog_end` | `Float32` | `2500.000000` |  | `developmentonly` `clientdll` `defensive` | Fog end for Free Camera. |
| `freecamera_fog_start` | `Float32` | `1800.000000` |  | `developmentonly` `clientdll` `defensive` | Fog start for Free Camera. |
| `freecamera_max_speed` | `Float32` | `500.000000` |  | `developmentonly` `clientdll` `defensive` | Tweak this parameter to adjust Free Camera movement max speed. |
| `freecamera_rotation_multiplier` | `Float32` | `10.000000` |  | `developmentonly` `clientdll` `defensive` | Tweak this parameter to adjust Free Camera mouse rotation. |
| `freecamera_zfar` | `Float32` | `4500.000000` |  | `developmentonly` `clientdll` `defensive` | Fog start for Free Camera. |
| `fs_async_threads` | `Int32` | `-1` |  | `developmentonly` `defensive` | Number of IO threads in async filesystem (-1 == auto) |
| `fs_fake_read_delay_ms` | `Int32` | `0` |  | `release` | Add N ms of delay to every low-level read operation, to simulate a slow disk |
| `fs_report_async_io` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `fs_report_long_reads` | `Int32` | `0` |  | `developmentonly` `defensive` | 0:Off, 1:All (for tracking accumulated duplicate read times), &gt;1:Microsecond threashold |
| `fs_report_sync_opens` | `Int32` | `0` |  | `release` | 0:Off, 1:Always, 2:Not during load |
| `fs_warning_mode` | `Int32` | `0` |  | `developmentonly` `defensive` | 0:Off, 1:Warn main thread, 2:Warn other threads |
| `func_break_max_pieces` | `Int32` | `15` |  | `gamedll` `archive` `replicated` |  |
| `func_break_reduction_factor` | `Float32` | `0.500000` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_breakdmg_bullet` | `Float32` | `0.500000` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_breakdmg_club` | `Float32` | `1.500000` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_breakdmg_explosive` | `Float32` | `1.250000` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_async_movable_navmesh_updates` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_debug_all` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_debug_follower` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_debug_parallel` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_debug_showtext` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_debug_verbose` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_force_transition_start_direction` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_get_speed_override` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_imgui_log_count` | `Int32` | `30` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_run_parallel` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_rotator_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `func_rotator_run_parallel` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `fx_drawmetalspark` | `Bool` | `true` |  | `developmentonly` `clientdll` | Draw metal spark effects. |
| `g_debug_angularsensor` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `g_debug_constraint_sounds` | `Bool` | `false` |  | `gamedll` `cheat` | Enable debug printing about constraint sounds. |
| `g_debug_doors` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `g_debug_ragdoll_visualize` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `g_debug_transitions` | `Int32` | `0` |  | `developmentonly` `gamedll` `cheat` | Set to 1 and restart the map to be warned if the map has no trigger_transition volumes. Set to 2 to see a dump of all entities &amp; associated results during a transition. |
| `g_ragdoll_fadespeed` | `Int32` | `600` |  | `developmentonly` `clientdll` `defensive` |  |
| `g_ragdoll_important_maxcount` | `Int32` | `2` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `g_ragdoll_lvfadespeed` | `Int32` | `100` |  | `developmentonly` `clientdll` `defensive` |  |
| `g_ragdoll_maxcount` | `Int32` | `5` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `game_mode` | `Int32` | `1` |  | `gamedll` `clientdll` `replicated` `release` | The current game mode (based on game type). See GameModes.txt. |
| `game_online` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `hidden` `replicated` `defensive` | The current game is online. |
| `game_particle_manager_requeue_messages` | `Bool` | `true` |  | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `game_public` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `hidden` `replicated` `defensive` | The current game is public. |
| `game_type` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` | The current game type. See GameModes.txt. |
| `gameevents_showeventlisteners` | `Bool` | `false` |  | `developmentonly` `defensive` | Show listening addition/removals |
| `gameevents_showevents` | `Int32` | `0` |  | `developmentonly` `defensive` | Dump game events to console. (1 = Show Signaling, 2 = Show Posting also). |
| `gameinstructor_enable` | `Bool` | `false` |  | `clientdll` `release` | Display in game lessons that teach new players. |
| `gameinstructor_find_errors` | `Bool` | `false` |  | `clientdll` `cheat` | Set to 1 and the game instructor will run EVERY scripted command to uncover errors. |
| `gameinstructor_start_sound_cooldown` | `Float32` | `4.000000` |  | `developmentonly` `clientdll` `defensive` | Number of seconds forced between similar lesson start sounds. |
| `gameinstructor_verbose` | `Int32` | `0` |  | `clientdll` `cheat` | Set to 1 for standard debugging or 2 (in combo with gameinstructor_verbose_lesson) to show update actions. |
| `gameinstructor_verbose_lesson` | `String` |  |  | `clientdll` `cheat` | Display more verbose information for lessons have this name. |
| `gamestats_file_output_directory` | `String` |  |  | `developmentonly` `gamedll` `defensive` | When -gamestatsfileoutputonly is specified, file will be emitted here instead of to modpath |
| `gc_secret_key` | `String` |  |  | `developmentonly` `gamedll` `protected` `defensive` | Secret key for authenticating with the GC |
| `gl_clear` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `glow_chickens` | `Bool` | `false` |  | `developmentonly` `gamedll` | Glow chickens with a green outline. |
| `glow_outline_width` | `Float32` | `6.000000` |  | `clientdll` `cheat` | Width of glow outline effect in screen space. |
| `glow_use_tolerance` | `Float32` | `0.850000` |  | `clientdll` `replicated` `cheat` |  |
| `gotv_theater_container` | `String` |  |  | `clientdll` `release` | Enables GOTV theater mode for the specified container, setting it to 'live' will play top live matches |
| `gpu_level` | `Int32` | `3` |  | `developmentonly` `clientdll` `defensive` | GPU Level - Default: High |
| `gpu_mem_level` | `Int32` | `2` |  | `developmentonly` `clientdll` `defensive` | Memory Level - Default: High |
| `hairsim_force_fixed_timestep` | `Bool` | `true` |  | `developmentonly` `cheat` |  |
| `hairsim_reset` | `Bool` | `false` |  | `developmentonly` `cheat` |  |
| `healthshot_allow_use_at_full` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `healthshot_health` | `Int32` | `50` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `healthshot_healthboost_damage_multiplier` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `healthshot_healthboost_speed_multiplier` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `healthshot_healthboost_time` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `hidehud` | `Int32` | `0` |  | `clientdll` `cheat` | bitmask: 1=weapon selection, 2=flashlight, 4=all, 8=health, 16=player dead, 32=needssuit, 64=misc, 128=chat, 256=crosshair, 512=vehicle crosshair, 1024=in vehicle |
| `hinttext_displaytime` | `Float32` | `4.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `host_force_frametime_to_equal_tick_interval` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `host_force_max_frametime_to_tick_interval` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `host_framerate` | `Float32` | `0.000000` |  | `release` | Set to lock per-frame time elapse. |
| `host_readconfig_ignore_userconfig` | `Bool` | `false` |  | `cheat` | Whether we should ignore the user config file for reading/writing. |
| `host_timescale` | `Float32` | `1.000000` |  | `replicated` `cheat` | Prescale the clock by this amount. |
| `hostage_debug` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `cheat` | Show hostage AI debug information |
| `hostage_drop_time` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` | Time for the hostage before it fully drops to ground |
| `hostage_is_silent` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` | When set, the hostage won't play any code driven response rules lines |
| `hostfile` | `String` | `host.txt` |  | `gamedll` `release` | The HOST file to load. |
| `hostname` | `String` |  |  | `release` | Hostname for server. |
| `hostname_in_client_status` | `Bool` | `false` |  | `release` | Show server hostname in client status. |
| `hostport` | `Int32` | `27015` |  | `release` | Host game server port |
| `hud_fastswitch` | `Int32` | `0` |  | `clientdll` `archive` |  |
| `hud_scaling` | `Float32` | `1.000000` | `0.900000 .. 1.100000` | `clientdll` `archive` | Scales hud elements |
| `hud_showtargetid` | `Bool` | `true` |  | `clientdll` `archive` `per_user` | Enables display of target names |
| `hullivr_edge_merge_tan` | `Float32` | `0.020000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Should we try to straighten two faces connected to this edge? (tangent) |
| `hullivr_faceisland_merge_disp` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Should we straighten face island if the displacement is this much? (inches) |
| `hullivr_faceisland_merge_tan` | `Float32` | `0.040000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Should we try to straighten an island of faces deviating from their average normal (tangent)? |
| `hullivr_version` | `Int32` | `3` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `ik_constraints_enabled` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_all_chains_unique_color_per_chain` | `Bool` | `false` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_ccd` | `Int32` | `0` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_chain_to_filter_by` | `String` |  |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ik_debug_constraints` | `Int32` | `-1` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_dogleg3bone` | `Int32` | `0` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_dogleg3bone_enabled` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_fabrik_backwards_enabled` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_fabrik_backwards_iterations` | `Int32` | `0` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_fabrik_forwards_enabled` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_fabrik_forwards_iterations` | `Int32` | `0` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_groundtraces` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Show IK trace related details |
| `ik_debug_perlin_solver` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `ik_debug_planetilt` | `Int32` | `0` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_planetilt_axis_length` | `Float32` | `20.000000` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_targets` | `Bool` | `false` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_enable` | `Bool` | `true` |  | `replicated` `cheat` | Enable IK. |
| `ik_fabrik_align_chain` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_fabrik_backwards_enabled` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_fabrik_forwards_enabled` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_fabrik_override_num_iterations` | `Int32` | `-1` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_final_fixup_enable` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `ik_hinge_debug_bone_index` | `Int32` | `-1` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ik_planetilt_enable` | `Bool` | `true` |  | `developmentonly` `replicated` `defensive` |  |
| `imgui_debug_draw_dashboard_toggle_pause` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` `menubar_item` | Dashboard/Pause Game When Activated |
| `imgui_debug_draw_dashboard_window` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` `menubar_item` | Dashboard/Show Dashboard |
| `imgui_debug_draw_dashboard_window_toggle_focus` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Dashboard toggle focus |
| `imgui_default_font_size` | `Float32` | `20.000000` |  | `archive` `cheat` | Default imgui font size |
| `imgui_domain` | `Int32` | `2` |  | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` | 1 == client, 2 == server |
| `imgui_enable` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | if imgui should display |
| `imgui_enable_input` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | if imgui should consume input |
| `imgui_ent_text_enable` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` `menubar_item` | Show Entity Text in Window |
| `imgui_show_bullets` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` `menubar_item` | CSGO/Bullets |
| `imgui_show_cs2_worldmodel` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` `menubar_item` | CSGO/WorldModel |
| `imgui_show_grenades_window` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` `menubar_item` | CSGO/Show Grenades History |
| `imgui_temp_enable` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | if imgui should display temporarily |
| `in_button_double_press_window` | `Float32` | `0.220000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | How short the time between presses needs to be for us to consider it a double-press |
| `in_spewbuttondelta` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Spew button deltas, 0 = off, 1 = server, 2 = client, 3 = both |
| `in_spewbuttonhold` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Spew button hold times, 0 = off, 1 = server, 2 = client, 3 = both |
| `in_spewent` | `Int32` | `-1` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Which entity should we spew input for? (Useful for debugging bot input) |
| `in_spewinput` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Spew input, 0 = off, 1 = server, 2 = client, 3 = both |
| `inferno_batched_rays` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `inferno_child_spawn_interval_multiplier` | `Float32` | `0.100000` |  | `gamedll` `cheat` | Amount spawn interval increases for each child |
| `inferno_child_spawn_max_depth` | `Int32` | `4` |  | `gamedll` `replicated` `release` |  |
| `inferno_ct_experiment` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` | enable ct incendiary experiment |
| `inferno_damage` | `Float32` | `40.000000` |  | `gamedll` `cheat` | Damage per second |
| `inferno_damage_ct` | `Float32` | `40.000000` |  | `gamedll` `cheat` | Damage per second from CT inferno |
| `inferno_damage_timer` | `Float32` | `0.200000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | How long between times for the inferno to deal damage. |
| `inferno_debug` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `inferno_dlight_spacing` | `Float32` | `7200.000000` |  | `clientdll` `cheat` | Inferno dlights are at least this far apart |
| `inferno_dlights` | `Float32` | `30.000000` |  | `developmentonly` `clientdll` `defensive` | Min FPS at which molotov dlights will be created |
| `inferno_fire` | `Int32` | `2` |  | `developmentonly` `clientdll` `defensive` |  |
| `inferno_flame_lifetime` | `Float32` | `7.000000` |  | `gamedll` `replicated` `release` | Average lifetime of each flame in seconds |
| `inferno_flame_lifetime_incendiary` | `Float32` | `5.500000` |  | `gamedll` `replicated` `release` | Average lifetime of each flame in seconds (incgrenade) |
| `inferno_flame_spacing` | `Float32` | `42.000000` |  | `gamedll` `cheat` | Minimum distance between separate flame spawns |
| `inferno_forward_reduction_factor` | `Float32` | `0.900000` |  | `gamedll` `cheat` |  |
| `inferno_friendly_fire_duration` | `Float32` | `6.000000` |  | `gamedll` `cheat` | For this long, FF is credited back to the thrower. |
| `inferno_initial_spawn_interval` | `Float32` | `0.020000` |  | `gamedll` `cheat` | Time between spawning flames for first fire |
| `inferno_max_child_spawn_interval` | `Float32` | `0.500000` |  | `gamedll` `cheat` | Largest time interval for child flame spawning |
| `inferno_max_flames` | `Int32` | `16` |  | `gamedll` `replicated` `release` | Maximum number of flames that can be created |
| `inferno_max_range` | `Float32` | `150.000000` |  | `gamedll` `replicated` `release` | Maximum distance flames can spread from their initial ignition point |
| `inferno_max_range_ct` | `Float32` | `110.000000` |  | `gamedll` `replicated` `release` | Maximum distance flames can spread from their initial ignition point for an incendiary |
| `inferno_max_trace_per_tick` | `Int32` | `16` |  | `developmentonly` `gamedll` `defensive` |  |
| `inferno_per_flame_spawn_duration` | `Float32` | `3.000000` |  | `gamedll` `cheat` | Duration each new flame will attempt to spawn new flames |
| `inferno_smoke_volume_density` | `Float32` | `0.030000` |  | `gamedll` `cheat` |  |
| `inferno_spawn_angle` | `Float32` | `45.000000` |  | `gamedll` `cheat` | Angular change from parent |
| `inferno_spread_speed_mult` | `Float32` | `1.000000` |  | `gamedll` `replicated` `release` | Speed up the spreadrate of the Molotov until max number of nodes are created.  slowdown &lt; 1 &gt; Speedup |
| `inferno_spread_speed_mult_ct` | `Float32` | `10.000000` |  | `gamedll` `replicated` `release` | Speed up the spread rate of the Incendiary until max number of nodes are created. slowdown &lt; 1 &gt; Speedup |
| `inferno_surface_offset` | `Float32` | `15.000000` |  | `gamedll` `cheat` |  |
| `inferno_velocity_decay_factor` | `Float32` | `0.200000` |  | `gamedll` `cheat` |  |
| `inferno_velocity_factor` | `Float32` | `0.003000` |  | `gamedll` `cheat` |  |
| `inferno_velocity_factor_ct` | `Float32` | `0.003000` |  | `gamedll` `cheat` |  |
| `inferno_velocity_normal_factor` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `input_button_code_is_scan_code_scd` | `Bool` | `true` |  | `archive` `per_user` | Bind keys based on keyboard position instead of key name |
| `input_downimpulsevalue` | `Float32` | `0.700000` |  | `developmentonly` `clientdll` |  |
| `input_filter_relative_analog_inputs` | `Bool` | `false` |  | `clientdll` `archive` |  |
| `input_forceuser` | `Int32` | `-1` |  | `cheat` | Force user input to this split screen player. |
| `input_upimpulsevalue` | `Float32` | `0.300000` |  | `developmentonly` `clientdll` |  |
| `install_dlc_workshoptools_cvar` | `String` | `-1` |  | `clientdll` `release` | DLC Install Status |
| `instant_replay` | `Bool` | `true` |  | `developmentonly` `defensive` | Enable instant replay recording. |
| `instant_replay_history_limit` | `Int32` | `120` |  | `developmentonly` `defensive` | Maximum amount of minutes to save history (0 is unlimited). |
| `iv_debugbone` | `String` |  |  | `release` | Debug bone name for interpolation spew of CAnimationState. |
| `iv_parallel_latch` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `iv_parallel_restore` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `iv_wrapped_parallel_latch` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `joy_accel_filter` | `Float32` | `0.200000` |  | `developmentonly` `clientdll` |  |
| `joy_accelmax` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` |  |
| `joy_accelscale` | `Float32` | `0.600000` |  | `developmentonly` `clientdll` |  |
| `joy_advanced` | `Bool` | `false` |  | `clientdll` `archive` |  |
| `joy_advaxisr` | `Int32` | `0` |  | `clientdll` `archive` |  |
| `joy_advaxisu` | `Int32` | `0` |  | `clientdll` `archive` |  |
| `joy_advaxisv` | `Int32` | `0` |  | `clientdll` `archive` |  |
| `joy_advaxisx` | `Int32` | `0` |  | `clientdll` `archive` |  |
| `joy_advaxisy` | `Int32` | `0` |  | `clientdll` `archive` |  |
| `joy_advaxisz` | `Int32` | `0` |  | `clientdll` `archive` |  |
| `joy_autosprint` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` `defensive` | Automatically sprint when moving with an analog joystick |
| `joy_axisbutton_threshold` | `Float32` | `0.300000` |  | `archive` | Analog axis range before a button press is registered. |
| `joy_axisr_deadzone` | `Float32` | `0.150000` |  | `archive` `per_user` |  |
| `joy_axisr_relative` | `Bool` | `false` |  | `archive` `per_user` |  |
| `joy_axisu_deadzone` | `Float32` | `0.150000` |  | `archive` `per_user` |  |
| `joy_axisu_relative` | `Bool` | `false` |  | `archive` `per_user` |  |
| `joy_axisv_deadzone` | `Float32` | `0.150000` |  | `archive` `per_user` |  |
| `joy_axisv_relative` | `Bool` | `false` |  | `archive` `per_user` |  |
| `joy_axisx_deadzone` | `Float32` | `0.150000` |  | `archive` `per_user` |  |
| `joy_axisx_relative` | `Bool` | `false` |  | `archive` `per_user` |  |
| `joy_axisy_deadzone` | `Float32` | `0.150000` |  | `archive` `per_user` |  |
| `joy_axisy_relative` | `Bool` | `false` |  | `archive` `per_user` |  |
| `joy_axisz_deadzone` | `Float32` | `0.150000` |  | `archive` `per_user` |  |
| `joy_axisz_relative` | `Bool` | `false` |  | `archive` `per_user` |  |
| `joy_circle_correct_mode` | `Int32` | `1` |  | `clientdll` `archive` `per_user` |  |
| `joy_circle_correct_mode_vehicle` | `Int32` | `2` |  | `clientdll` `archive` `per_user` |  |
| `joy_display_input` | `Bool` | `false` |  | `clientdll` `archive` |  |
| `joy_forward_sensitivity` | `Float32` | `1.000000` |  | `clientdll` `archive` `per_user` |  |
| `joy_lowend` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` |  |
| `joy_lowmap` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` |  |
| `joy_movement_stick` | `Bool` | `false` |  | `clientdll` `archive` `per_user` | Which stick controls movement (0 is left stick) |
| `joy_name` | `String` | `joystick` |  | `clientdll` `archive` |  |
| `joy_pegged` | `Float32` | `0.750000` |  | `developmentonly` `clientdll` |  |
| `joy_pitch_sensitivity` | `Float32` | `3.000000` |  | `clientdll` `archive` `per_user` |  |
| `joy_pitchsensitivity` | `Float32` | `1.000000` |  | `clientdll` `archive` `per_user` |  |
| `joy_response_look` | `Int32` | `0` |  | `clientdll` `archive` `per_user` |  |
| `joy_response_move` | `Int32` | `9` |  | `clientdll` `archive` `per_user` |  |
| `joy_response_move_vehicle` | `Int32` | `6` |  | `developmentonly` `clientdll` `defensive` |  |
| `joy_sensitive_step0` | `Float32` | `0.100000` |  | `developmentonly` `clientdll` |  |
| `joy_sensitive_step1` | `Float32` | `0.400000` |  | `developmentonly` `clientdll` |  |
| `joy_sensitive_step2` | `Float32` | `0.900000` |  | `developmentonly` `clientdll` |  |
| `joy_side_sensitivity` | `Float32` | `1.000000` |  | `clientdll` `archive` `per_user` |  |
| `joy_sidesensitivity` | `Float32` | `1.000000` |  | `clientdll` `archive` |  |
| `joy_vehicle_turn_lowend` | `Float32` | `0.700000` |  | `developmentonly` `clientdll` |  |
| `joy_vehicle_turn_lowmap` | `Float32` | `0.400000` |  | `developmentonly` `clientdll` |  |
| `joy_virtual_peg` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` |  |
| `joy_xcontroller_cfg_loaded` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | If 0, the 360controller.cfg file will be executed on startup &amp; option changes. |
| `joy_yaw_sensitivity` | `Float32` | `3.000000` |  | `clientdll` `archive` `per_user` |  |
| `joy_yawsensitivity` | `Float32` | `-1.000000` |  | `clientdll` `archive` `per_user` |  |
| `joystick` | `Bool` | `false` |  | `clientdll` `archive` | True if the joystick is enabled, false otherwise. |
| `jpeg_quality` | `Int32` | `90` | `1 .. 100` | `developmentonly` `defensive` | Set jpeg screenshot quality. [1..100] |
| `key_bind_version` | `Int32` | `0` |  | `clientdll` `hidden` `archive` `release` |  |
| `keychain_animation_reactivity` | `Float32` | `0.250000` |  | `developmentonly` `clientdll` |  |
| `keychain_preview_limit_step` | `Float32` | `0.125000` |  | `developmentonly` `clientdll` |  |
| `keychain_reactivity` | `Float32` | `0.050000` |  | `developmentonly` `clientdll` |  |
| `keychain_wmul` | `Float32` | `2.000000` |  | `developmentonly` `clientdll` |  |
| `labelled_debug_helper_arc_segments` | `Int32` | `20` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `labelled_debug_helper_enabled` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `labelled_debug_helper_scale` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `labelled_debug_helper_show_position` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `labelled_debug_helper_show_text` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `labelled_debug_helper_skeleton_show_bone_names` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `lb_allow_shadow_rotation` | `Bool` | `true` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Shadow Rotation |
| `lb_barnlight_shadow_use_precomputed_vis` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `lb_barnlight_shadowmap_scale` | `Float32` | `1.000000` |  | `release` | Scale for computed barnlight shadowmap size |
| `lb_bin_slices` | `Int32` | `8192` |  | `developmentonly` `defensive` |  |
| `lb_convert_to_barn_lights_falloff_match_point` | `Float32` | `0.150000` |  | `developmentonly` `defensive` |  |
| `lb_csm_cascade_size_override` | `Int32` | `-1` |  | `developmentonly` `defensive` | Override width/height of individual cascades in the CSM |
| `lb_csm_cross_fade_override` | `Float32` | `-1.000000` |  | `developmentonly` `defensive` | Override CSM cross fade amount |
| `lb_csm_distance_fade_override` | `Float32` | `-1.000000` |  | `developmentonly` `defensive` | Override CSM distance fade |
| `lb_csm_draw_alpha_tested` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `lb_csm_draw_translucent` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `lb_csm_fov_override` | `Float32` | `-1.000000` |  | `developmentonly` `cheat` |  |
| `lb_csm_override_bulb_radius` | `Float32` | `-1.000000` |  | `developmentonly` `defensive` | Override bulb radius for CSM |
| `lb_csm_override_staticgeo_cascades` | `Bool` | `false` |  | `developmentonly` `defensive` | Override Cascades that will render static objects with lb_csm_override_staticgeo_cascades_value |
| `lb_csm_override_staticgeo_cascades_animated_verts` | `Bool` | `true` |  | `developmentonly` `defensive` | If lb_csm_override_staticgeo_cascades, ensure only objects without animated verts, i.e. SCENEOBJECTFLAG_CAN_RENDER_INTO_SST flag will be excluded (as opposed to all static objects). |
| `lb_csm_override_staticgeo_cascades_value` | `Int32` | `-1` |  | `developmentonly` `defensive` | If lb_csm_override_staticgeo_cascades, override value used to determine which cascades render static objects |
| `lb_csm_receiver_plane_depth_bias` | `Float32` | `0.000015` |  | `developmentonly` `defensive` | Shader depth bias applied to shadow receiver (Note this conflicts with renderstate depth bias, both now default to 0) |
| `lb_csm_receiver_plane_depth_bias_transmissive_backface` | `Float32` | `0.000150` |  | `developmentonly` `defensive` | Depth bias applied to shadow receiver for transmissive backface geo (based on renderstate depthbias being 0) |
| `lb_cubemap_normalization_max` | `Float32` | `32.000000` |  | `developmentonly` `defensive` |  |
| `lb_cubemap_normalization_roughness_begin` | `Float32` | `0.100000` |  | `developmentonly` `defensive` |  |
| `lb_debug_light_bounds` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Light Bounds |
| `lb_debug_shadow_atlas` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Shadow Atlas |
| `lb_debug_shadowtile_atlas` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug ShadowTile Atlas |
| `lb_debug_silhouette` | `String` |  |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Silhouettes |
| `lb_debug_silhouette_sum` | `UInt32` | `1` | `1 .. 3` | `developmentonly` `cheat` | If we should draw normal silhouette or minkowski sum silhouette |
| `lb_debug_tiles` | `String` |  |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Tiles |
| `lb_debug_visualize_fog_shadowed_lights` | `Int32` | `0` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Visualize Fog Shadowed Lights |
| `lb_debug_visualize_lights` | `Int32` | `0` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Visualize Lights |
| `lb_debug_visualize_shadowed_light_details` | `Bool` | `false` |  | `developmentonly` `cheat` |  |
| `lb_debug_visualize_shadowed_lights` | `Int32` | `0` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Visualize Shadowed Lights |
| `lb_dynamic_shadow_penumbra` | `Bool` | `true` |  | `developmentonly` `defensive` | Adjust shadow penumbra based on light size |
| `lb_dynamic_shadow_resolution` | `Bool` | `true` |  | `developmentonly` `defensive` | Dynamically adjust shadow resolution |
| `lb_dynamic_shadow_resolution_base` | `Float32` | `1024.000000` | `128.000000 .. 2048.000000` | `developmentonly` `defensive` | Base resolution for dynamic shadowmap sizing.  Shadowmap size of a screen sized light |
| `lb_dynamic_shadow_resolution_base_cmp_shadowmapsize` | `Bool` | `false` |  | `developmentonly` | take min of lb_dynamic_shadow_resolution and barnlight shadowmapsize as base shadowmapsize |
| `lb_dynamic_shadow_resolution_delay` | `Float32` | `0.850000` | `0.100000 .. 3.000000` | `developmentonly` `defensive` | Update delay for shadow size |
| `lb_dynamic_shadow_resolution_hysteresis` | `Float32` | `0.330000` | `0.010000 .. 1.000000` | `developmentonly` `defensive` | Update hysteresis for shadow size |
| `lb_dynamic_shadow_resolution_quantization` | `UInt32` | `64` | `8 .. 128` | `developmentonly` `defensive` | Quantization of dynamically computed shadow size |
| `lb_enable_baked_shadows` | `Bool` | `true` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Enable Baked Shadows |
| `lb_enable_binning` | `Bool` | `true` |  | `developmentonly` `menubar_item` `defensive` | SceneSystem/LightBinner/Enable Binning |
| `lb_enable_dynamic_lights` | `Bool` | `true` |  | `developmentonly` `cheat` | Allows rendering dynamic lights |
| `lb_enable_envmaps` | `Bool` | `true` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Enable EnvMaps |
| `lb_enable_fog_mixed_shadows` | `Bool` | `true` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Enable Fog Mixed Shadows |
| `lb_enable_lights` | `Bool` | `true` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Enable Lights |
| `lb_enable_shadow_casting` | `Bool` | `true` |  | `developmentonly` `defensive` | Allow stationary/dynamic lights to cast shadows. |
| `lb_enable_stationary_lights` | `Bool` | `true` |  | `developmentonly` `cheat` | Allows rendering stationary/mixed lights |
| `lb_enable_sunlight` | `Bool` | `true` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Enable Sunlight |
| `lb_low_quality_shader_fade_region_rescale` | `Float32` | `0.000000` |  | `developmentonly` `cheat` | For envmaps in low quality shader mode, how much of the fade region to scale the envmap box by. |
| `lb_max_visible_barn_lights_override` | `Int32` | `-1` |  | `developmentonly` `cheat` | Override maximum visible barn lights |
| `lb_max_visible_envmaps_override` | `Int32` | `-1` |  | `developmentonly` `cheat` | Override maximum visible envmaps |
| `lb_mixed_shadows` | `Bool` | `true` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Enable Mixed Shadows |
| `lb_override_barn_light_fade_sizes` | `Vector2` | `0.050000 0.025000` |  | `developmentonly` `cheat` |  |
| `lb_override_barn_light_fade_sizes_enable` | `Bool` | `false` |  | `developmentonly` `cheat` |  |
| `lb_override_barn_light_shadow_fade_sizes` | `Vector2` | `0.100000 0.050000` |  | `developmentonly` `cheat` |  |
| `lb_precomputed_shadowmap_depth_bias` | `Float32` | `0.000350` |  | `developmentonly` |  |
| `lb_precomputed_shadowmap_enable` | `Bool` | `true` |  | `developmentonly` |  |
| `lb_shadow_map_cull_empty_mixed` | `Bool` | `false` |  | `cheat` | Don't render shadows for mixed shadowmaps with no dynamics objects in view |
| `lb_shadow_map_culling` | `Bool` | `true` |  | `cheat` |  |
| `lb_shadow_texture_height_override` | `Int32` | `-1` |  | `developmentonly` `defensive` | Override height of shadow atlas texture |
| `lb_shadow_texture_width_override` | `Int32` | `-1` |  | `developmentonly` `defensive` | Override width of shadow atlas texture |
| `lb_ssss_importance_sample` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `lb_ssss_samples` | `Int32` | `11` | `3 .. 15` | `developmentonly` `defensive` | Subsurface sample count |
| `lb_sun_csm_size_cull_threshold_texels` | `Float32` | `10.000000` |  | `developmentonly` `defensive` | Size, in texels, where we will cull an object in the shadowmap |
| `lb_tile_pixels` | `Int32` | `8` |  | `developmentonly` `defensive` |  |
| `lb_time_sliced_shadow_map_reallocation_age` | `Float32` | `0.700000` |  | `developmentonly` `defensive` | Age of cached allocation to be considered for re-allocation |
| `lb_time_sliced_shadow_map_reallocation_pct` | `Float32` | `0.200000` |  | `developmentonly` `defensive` | Likelyhood we'll re-allocate a timesliced shadowmap (to try to improve packing) |
| `lb_time_sliced_shadow_map_rendering_enable` | `Bool` | `true` |  | `developmentonly` `defensive` | Allow time-sliced shadow buffer rendering when enabled via gameinfo.gi |
| `lb_timesliced_shadows_dynamic_size` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `lb_use_ellipsoid_bounds` | `Bool` | `true` |  | `developmentonly` `cheat` |  |
| `lb_use_illumination_silhouette` | `Bool` | `true` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Use Illumination Bounds |
| `leaderboards_cache_duration` | `Int32` | `600` |  | `developmentonly` `clientdll` |  |
| `lightquery_debug_direct_lighting` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `lightquery_debug_indirect_lighting` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `lobby_default_privacy_bits2` | `String` | `1` |  | `clientdll` `archive` `release` | Lobby default permissions (0: private, 1: public) |
| `lobby_gamesearch_fake` | `Int32` | `0` |  | `developmentonly` `clientdll` |  |
| `lobby_stats_fake` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `locator_topdown_style` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Topdown games set this to handle distance and offscreen location differently. |
| `lockMoveControllerRet` | `Bool` | `false` |  | `clientdll` `archive` |  |
| `logaddress_token_secret` | `String` |  |  | `gamedll` `release` | Set a secret string that will be hashed when using logaddress with explicit token hash. |
| `logic_entity_analyzer_debug` | `Bool` | `false` |  | `gamedll` `replicated` `cheat` |  |
| `logic_npc_counter_debug` | `Bool` | `false` |  | `gamedll` `replicated` `cheat` |  |
| `lservercfgfile` | `String` | `listenserver.cfg` |  | `developmentonly` `gamedll` `defensive` |  |
| `m_pitch` | `Float32` | `0.022000` |  | `clientdll` `archive` `userinfo` `per_user` | Mouse pitch factor. |
| `m_yaw` | `Float32` | `0.022000` |  | `clientdll` `archive` `userinfo` `per_user` | Mouse yaw factor. |
| `mapcyclefile` | `String` | `mapcycle.txt` |  | `developmentonly` `gamedll` `defensive` | Name of the .txt file used to cycle the maps on multiplayer servers |
| `mapoverview_allow_client_draw` | `Bool` | `false` |  | `clientdll` `release` | Allow a client to draw on the map overview |
| `mapoverview_icon_scale` | `Float32` | `1.000000` | `0.500000 .. 3.000000` | `clientdll` `archive` `release` | Sets the icon scale multiplier for the overview map. Valid values are 0.5 to 3.0. |
| `markup_volume_ref_cone_angle` | `Float32` | `135.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `mat_assert_on_error_shader_use` | `Bool` | `false` |  | `developmentonly` |  |
| `mat_cache_and_skip_commandbuffers` | `Bool` | `true` |  | `developmentonly` |  |
| `mat_cache_renderablepasses` | `Bool` | `true` |  | `developmentonly` |  |
| `mat_colcorrection_disableentities` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Disable map color-correction entities |
| `mat_colcorrection_editor` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `mat_colcorrection_forceentitiesclientside` | `Bool` | `false` |  | `clientdll` `cheat` | Forces color correction entities to be updated on the client |
| `mat_colorcorrection` | `Bool` | `true` |  | `developmentonly` |  |
| `mat_depthbias_shadowmap` | `Float32` | `0.000500` |  | `developmentonly` `clientdll` `defensive` |  |
| `mat_disable_normal_mapping` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `mat_execute_skipbuffers` | `Bool` | `true` |  | `developmentonly` |  |
| `mat_fullbright` | `Int32` | `0` |  | `cheat` | Debug rendering modes |
| `mat_hide_error_shader` | `Bool` | `false` |  | `developmentonly` |  |
| `mat_lpv_luxels` | `Bool` | `false` |  | `cheat` |  |
| `mat_luxels` | `Bool` | `false` |  | `cheat` |  |
| `mat_max_lighting_complexity` | `Float32` | `8.000000` |  | `cheat` |  |
| `mat_overdraw` | `Int32` | `0` |  | `cheat` | Visualize overdraw |
| `mat_overdraw_color` | `Vector3` | `0.075000 0.150000 0.300000` |  | `cheat` |  |
| `mat_shader_cache` | `Bool` | `true` |  | `developmentonly` |  |
| `mat_shading_complexity` | `Bool` | `false` |  | `cheat` | Visualize shading complexity |
| `mat_shading_complexity_color` | `Vector3` | `1.000000 0.500000 0.250000` |  | `cheat` |  |
| `mat_shading_complexity_max_instruction_count` | `Float32` | `1024.000000` |  | `cheat` |  |
| `mat_shading_complexity_max_register_count` | `Float32` | `128.000000` |  | `cheat` |  |
| `mat_shadowmap_luxels` | `Bool` | `false` |  | `cheat` |  |
| `mat_show_distance_field` | `Int32` | `0` |  | `cheat` | 0=Off, 1=Visualize trace from camera, 2=Visualize occlusion, 3=Visualize far field trace from camera |
| `mat_skip_static_const_eval` | `Bool` | `true` |  | `developmentonly` |  |
| `mat_slopescaledepthbias_shadowmap` | `Float32` | `4.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `mat_tonemap_bloom_scale` | `Float32` | `-1.000000` |  | `cheat` |  |
| `mat_tonemap_bloom_start_value` | `Float32` | `-1.000000` |  | `cheat` |  |
| `mat_tonemap_debug` | `Int32` | `0` |  | `developmentonly` `defensive` |  |
| `mat_tonemap_force_accelerate_exposure_down` | `Float32` | `-1.000000` |  | `cheat` |  |
| `mat_tonemap_force_average_lum_min` | `Float32` | `-1.000000` |  | `cheat` | Override. Old default was 3.0 |
| `mat_tonemap_force_log_lum_max` | `Float32` | `-1.000000` |  | `cheat` |  |
| `mat_tonemap_force_log_lum_min` | `Float32` | `-1.000000` |  | `cheat` |  |
| `mat_tonemap_force_max` | `Float32` | `-1.000000` |  | `cheat` |  |
| `mat_tonemap_force_min` | `Float32` | `-1.000000` |  | `cheat` |  |
| `mat_tonemap_force_percent_bright_pixels` | `Float32` | `-1.000000` |  | `cheat` | Override. Old value was 1.0 |
| `mat_tonemap_force_percent_target` | `Float32` | `-1.000000` |  | `cheat` | Override. Old default was 45. |
| `mat_tonemap_force_rate` | `Float32` | `-1.000000` |  | `cheat` |  |
| `mat_tonemap_force_scale` | `Float32` | `0.000000` |  | `cheat` |  |
| `mat_tonemap_force_use_alpha` | `Int32` | `-1` |  | `cheat` |  |
| `mat_tonemap_uncap_exposure` | `Int32` | `0` |  | `cheat` |  |
| `mat_viewportscale` | `Float32` | `1.000000` | `0.001563 .. 1.000000` | `developmentonly` `clientdll` `defensive` | Scale down the main viewport (to reduce GPU impact on CPU profiling) |
| `mat_warn_bad_modes` | `Bool` | `false` |  | `developmentonly` |  |
| `mat_wireframe` | `Int32` | `0` |  | `cheat` | 0=Off, 1=Surface Wireframe, 2=Transparent Wireframe |
| `mem_level` | `Int32` | `2` |  | `developmentonly` `clientdll` `defensive` | Memory Level - Default: High |
| `mem_test_each_frame` | `Bool` | `false` |  | `developmentonly` `defensive` | Run heap check at end of every frame |
| `mem_test_every_n_seconds` | `Int32` | `0` |  | `developmentonly` `defensive` | Run heap check at a specified interval |
| `mem_test_quiet` | `Bool` | `false` |  | `developmentonly` `defensive` | Don't print stats when memtesting |
| `mesh_calculate_curvature_smooth_invert` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `mesh_calculate_curvature_smooth_pass_count` | `Int32` | `3` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `mesh_calculate_curvature_smooth_weight` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `mic_listen_while_nonfocused` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Enables the ability for the mic to remain open if the window loses focus such as when a caster tabs out to adjust settings |
| `mm_csgo_community_search_players_min` | `Int32` | `3` |  | `archive` `release` | When performing CSGO community matchmaking look for servers with at least so many human players |
| `mm_debug_friend_rp` | `UInt32` | `0` |  | `developmentonly` |  |
| `mm_dedicated_allow` | `Bool` | `true` |  | `developmentonly` | 1 = allow searches for dedicated servers |
| `mm_dedicated_fake` | `Bool` | `false` |  | `developmentonly` | 1 = pretend like search is going, but abort after some time |
| `mm_dedicated_force_servers` | `String` |  |  | `release` | Comma delimited list of ip:port of servers used to search for dedicated servers instead of searching for public servers.<br>Use syntax `publicip1:port\|privateip1:port,publicip2:port\|privateip2:port` if your server is behind NAT.<br>If the server is behind NAT, you can specify `0.0.0.0\|privateip:port` and if server port is in the list of `mm_server_search_lan_ports` its public address should be automatically detected. |
| `mm_dedicated_ip` | `String` |  |  | `developmentonly` | IP address of dedicated servers to consider available |
| `mm_dedicated_search_maxping` | `Int32` | `150` | `25 .. 350` | `archive` | Longest preferred ping to dedicated servers for games |
| `mm_dedicated_search_maxresults` | `Int32` | `75` |  | `developmentonly` |  |
| `mm_dedicated_timeout_request` | `Float32` | `20.000000` |  | `developmentonly` |  |
| `mm_dlcs_mask_extras` | `UInt32` | `0` |  | `developmentonly` `defensive` |  |
| `mm_dlcs_mask_fake` | `String` |  |  | `developmentonly` `defensive` |  |
| `mm_events_listeners_validation` | `Bool` | `false` |  | `developmentonly` |  |
| `mm_ignored_sessions_forget_pass` | `Int32` | `5` |  | `developmentonly` |  |
| `mm_ignored_sessions_forget_time` | `Float32` | `600.000000` |  | `developmentonly` |  |
| `mm_player_search_count` | `Int32` | `5` |  | `developmentonly` |  |
| `mm_player_search_lan_ping_duration` | `Float32` | `3.500000` |  | `developmentonly` | Duration of LAN discovery ping phase. |
| `mm_player_search_lan_ping_interval` | `Float32` | `0.500000` |  | `developmentonly` | Interval between LAN discovery pings. |
| `mm_player_search_requests_limit` | `Int32` | `-1` |  | `developmentonly` | How many friend requests are displayed. |
| `mm_player_search_update_interval` | `Float32` | `10.000000` |  | `developmentonly` | Interval between players searches. |
| `mm_session_search_num_results` | `Int32` | `10` |  | `developmentonly` |  |
| `mm_session_search_qos_timeout` | `Float32` | `15.000000` |  | `release` |  |
| `mm_session_sys_connect_timeout` | `Float32` | `8.000000` |  | `developmentonly` |  |
| `mm_session_sys_delay_create` | `Float32` | `0.000000` |  | `developmentonly` |  |
| `mm_session_sys_delay_create_host` | `Float32` | `1.200000` |  | `developmentonly` |  |
| `mm_session_sys_kick_ban_duration` | `Float32` | `180.000000` |  | `release` |  |
| `mm_session_sys_pkey` | `String` |  |  | `release` |  |
| `mm_session_sys_ranking_timeout` | `Float32` | `12.000000` |  | `developmentonly` |  |
| `mm_session_sys_slots_guaranteed` | `Int32` | `10` |  | `developmentonly` |  |
| `mm_session_team_res_timeout` | `Float32` | `30.000000` |  | `developmentonly` |  |
| `mm_session_voice_loading` | `Bool` | `false` |  | `developmentonly` |  |
| `mm_sv_load_test` | `Bool` | `false` |  | `developmentonly` |  |
| `mm_teamsearch_errortime` | `Float32` | `3.000000` |  | `developmentonly` | Time team search is in error state until it self-cancels |
| `mm_teamsearch_nostart` | `Bool` | `false` |  | `developmentonly` | Team search will fake cancel before searching for server |
| `mm_title_debug_version` | `Int32` | `0` |  | `developmentonly` | This matchmaking version will override .res file version for isolating matchmaking |
| `mm_tu_string` | `String` | `00000000` |  | `developmentonly` `defensive` |  |
| `mm_use_p2p_for_listen_server` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `mobile_fps_increase_during_charging` | `Bool` | `false` |  | `archive` | MOBILE_FPS_CONTROL: If true we increase framerate limit while charging |
| `mobile_fps_increase_during_hfr_animations` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` | MOBILE_FPS_CONTROL: If true we increase framerate limit during HFR-tagged animations and transitions. |
| `mobile_fps_increase_during_touch` | `Bool` | `true` |  | `archive` | MOBILE_FPS_CONTROL: If true we increase framerate limit during touch |
| `mobile_fps_limit` | `Float32` | `30.000000` |  | `archive` | MOBILE_FPS_CONTROL: Mobile FPS limit - 15, 30, 60 |
| `model_default_preview_sequence_name` | `String` |  |  | `gamedll` `clientdll` `archive` `replicated` |  |
| `molotov_throw_detonate_time` | `Float32` | `2.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `molotov_usethrow_direction` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `motdfile` | `String` | `motd.txt` |  | `gamedll` `release` | The MOTD file to load. |
| `mouse_disableinput` | `Bool` | `false` |  | `developmentonly` `defensive` | Set to disable mouse input |
| `mouse_inverty` | `Bool` | `false` |  | `clientdll` `archive` `userinfo` |  |
| `movement_stats_debug_draw` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `movement_stats_force_calculate` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `mp_afterroundmoney` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | amount of money awared to every player after each round |
| `mp_allowspectators` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | toggles whether the server allows spectator mode or not |
| `mp_anyone_can_pickup_c4` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If set, everyone can pick up the c4, not just Ts. |
| `mp_autokick` | `Bool` | `true` |  | `gamedll` `replicated` `release` `commandline_enforced` | Kick idle/team-killing/team-damaging players |
| `mp_autoteambalance` | `Bool` | `true` |  | `gamedll` `notify` `release` `commandline_enforced` |  |
| `mp_backup_restore_load_autopause` | `Bool` | `true` |  | `gamedll` `release` | Whether to automatically pause the match after restoring round data from backup |
| `mp_backup_round_auto` | `Bool` | `true` |  | `gamedll` `release` | If enabled will keep in-memory backups to handle reconnecting players even if the backup files aren't written to disk |
| `mp_backup_round_file` | `String` | `backup` |  | `gamedll` `release` | If set then server will save all played rounds information to files filename_date_time_team1_team2_mapname_roundnum_score1_score2.txt |
| `mp_backup_round_file_last` | `String` |  |  | `gamedll` `release` | Every time a backup file is written the value of this convar gets updated to hold the name of the backup file. |
| `mp_backup_round_file_pattern` | `String` | `%prefix%_round%round%.txt` |  | `gamedll` `release` | If set then server will save all played rounds information to files named by this pattern, e.g.'%prefix%_%date%_%time%_%team1%_%team2%_%map%_round%round%_score_%score1%_%score2%.txt' |
| `mp_bot_ai_bt` | `String` |  |  | `gamedll` `release` `commandline_enforced` | Use the specified behavior tree file to drive the bot behavior. |
| `mp_buy_allow_grenades` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Whether players can purchase grenades from the buy menu or not. |
| `mp_buy_allow_guns` | `Int32` | `255` | `0 .. 255` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Whether players can purchase guns: pistols (1), SMGs (2), rifles (4), shotguns (8), sniper rifles (16), heavy MGs (32). |
| `mp_buy_anywhere` | `Int32` | `0` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | When set, players can buy anywhere, not only in buyzones. 0 = default. 1 = both teams. 2 = Terrorists. 3 = Counter-Terrorists. |
| `mp_buy_during_immunity` | `Int32` | `0` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | When set, players can buy when immune, ignoring buytime. 0 = default. 1 = both teams. 2 = Terrorists. 3 = Counter-Terrorists. |
| `mp_buytime` | `Float32` | `90.000000` | `>= 0.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How many seconds after round start players can buy items for. |
| `mp_c4_cannot_be_defused` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If set, the planted c4 cannot be defused. |
| `mp_c4timer` | `Int32` | `40` | `>= 10` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | how long from when the C4 is armed until it blows |
| `mp_chattime` | `Int32` | `10` | `1 .. 120` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | amount of time players can chat after the game is over |
| `mp_competitive_endofmatch_extra_time` | `Float32` | `15.000000` |  | `gamedll` `release` | After a competitive match finishes rematch voting extra time is given for rankings. |
| `mp_consecutive_loss_aversion` | `Int32` | `1` | `>= 0` | `gamedll` `clientdll` `replicated` `release` | How loss streak is affected with round win: 0 = win fully resets loss bonus, 1 = first win steps down loss bonus, 2 = first win holds loss bonus and step down starting with second win |
| `mp_consecutive_loss_max` | `Int32` | `4` | `>= 0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `mp_coopmission_bot_difficulty_offset` | `Int32` | `0` |  | `gamedll` `replicated` `release` `commandline_enforced` | The difficulty offset modifier for bots during coop missions. |
| `mp_ct_default_grenades` | `String` |  |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default grenades that the CTs will spawn with.	 To give multiple grenades, separate each weapon class with a space like this: 'weapon_molotov weapon_hegrenade' |
| `mp_ct_default_melee` | `String` | `weapon_knife` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default melee weapon that the CTs will spawn with.	 Even if this is blank, a knife will be given.	To give a taser, it should look like this: 'weapon_knife weapon_taser'.	 Remember to set mp_weapons_allow_zeus to 1 if you want to give a taser! |
| `mp_ct_default_primary` | `String` |  |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default primary (rifle) weapon that the CTs will spawn with |
| `mp_ct_default_secondary` | `String` | `weapon_hkp2000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default secondary (pistol) weapon that the CTs will spawn with |
| `mp_damage_headshot_only` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines whether non-headshot hits do any damage. |
| `mp_damage_scale_ct_body` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scales the damage a CT player takes by this much when they take damage in the body. (1 == 100%, 0.5 == 50%) |
| `mp_damage_scale_ct_head` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scales the damage a CT player takes by this much when they take damage in the head (1 == 100%, 0.5 == 50%).  REMEMBER! headshots do 4x the damage of the body before this scaler is applied. |
| `mp_damage_scale_t_body` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scales the damage a T player takes by this much when they take damage in the body. (1 == 100%, 0.5 == 50%) |
| `mp_damage_scale_t_head` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scales the damage a T player takes by this much when they take damage in the head (1 == 100%, 0.5 == 50%).	 REMEMBER! headshots do 4x the damage of the body before this scaler is applied. |
| `mp_damage_vampiric_amount` | `Float32` | `0.000000` |  | `gamedll` `replicated` `release` `commandline_enforced` | If Set to non-0, will determine the fraction of damage dealt that will be given to attacker. |
| `mp_death_drop_c4` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Whether c4 is droppable |
| `mp_death_drop_defuser` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Drop defuser on player death |
| `mp_death_drop_grenade` | `Int32` | `2` | `0 .. 2` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Which grenade to drop on player death: 0=none, 1=best, 2=current or best, 3=all grenades |
| `mp_death_drop_gun` | `Int32` | `1` | `0 .. 2` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Which gun to drop on player death: 0=none, 1=best, 2=current or best |
| `mp_death_drop_healthshot` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` | Drop healthshot on player death |
| `mp_death_drop_taser` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` | Drop taser on player death |
| `mp_deathcam_skippable` | `Bool` | `true` |  | `gamedll` `replicated` `release` `commandline_enforced` | Determines whether a player can early-out of the deathcam. |
| `mp_default_team_winner_no_objective` | `Int32` | `-1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If the map doesn't define an objective (bomb, hostage, etc), the value of this convar will declare the winner when the time runs out in the round. |
| `mp_defuser_allocation` | `Int32` | `0` | `0 .. 2` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How to allocate defusers to CTs at start or round: 0=none, 1=random, 2=everyone |
| `mp_disconnect_kills_bots` | `Bool` | `false` |  | `gamedll` `release` | When a bot disconnects, kill them first.  Requires mp_disconnect_kills_players. |
| `mp_disconnect_kills_players` | `Bool` | `true` |  | `gamedll` `release` | When a player disconnects, kill them first (triggering item drops, stats, etc.) |
| `mp_display_kill_assists` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Whether to display and score player assists |
| `mp_dm_bonus_length_max` | `Float32` | `30.000000` |  | `gamedll` `clientdll` `replicated` `release` | Maximum time the bonus time will last (in seconds) |
| `mp_dm_bonus_length_min` | `Float32` | `30.000000` |  | `gamedll` `clientdll` `replicated` `release` | Minimum time the bonus time will last (in seconds) |
| `mp_dm_bonus_percent` | `Int32` | `50` | `>= 0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Percent of points additionally awarded when someone gets a kill with the bonus weapon during the bonus period. |
| `mp_dm_bonusweapon_dogtags` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Additional dogtags to drop when making a kill with the bonus weapon |
| `mp_dm_dogtag_score` | `Int32` | `0` | `>= 0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Points to award for picking up a dogtag in deathmatch. |
| `mp_dm_healthshot_killcount` | `Int32` | `3` |  | `gamedll` `clientdll` `replicated` `release` | Grant healthshots in deathmatch after n kills |
| `mp_dm_kill_base_score` | `Int32` | `8` | `>= 0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Number of base points to award for a kill in deathmatch.  Cheaper weapons award 1 or 2 additional points. |
| `mp_dm_taser_bonus_streak_max` | `Int32` | `2` | `>= 0` | `gamedll` `clientdll` `replicated` `release` | Maximum times to multiply the score for getting a streak of taser kills in a single life. |
| `mp_dm_teammode` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | In deathmatch, enables team DM visuals &amp; scoring (0: personal, 1: team mode, 2: use team contribution score) |
| `mp_dm_teammode_bonus_score` | `Int32` | `1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Team deathmatch victory points to award for kill with bonus weapon |
| `mp_dm_teammode_dogtag_score` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Team deathmatch victory points to award for collecting enemy dogtags |
| `mp_dm_teammode_kill_score` | `Int32` | `1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Team deathmatch victory points to award for enemy kill |
| `mp_dm_time_between_bonus_max` | `Float32` | `40.000000` |  | `gamedll` `clientdll` `replicated` `release` | Maximum time a bonus time will start after the round start or after the last bonus (in seconds) |
| `mp_dm_time_between_bonus_min` | `Float32` | `30.000000` |  | `gamedll` `clientdll` `replicated` `release` | Minimum time a bonus time will start after the round start or after the last bonus (in seconds) |
| `mp_dogtag_despawn_on_killer_death` | `Bool` | `true` |  | `gamedll` `replicated` `release` `commandline_enforced` | Whether dogtags should despawn when their killer dies |
| `mp_dogtag_despawn_time` | `Float32` | `120.000000` | `>= 0.000000` | `gamedll` `replicated` `release` `commandline_enforced` | How many seconds dogtags should stay around before despawning automatically (0 = infinite) |
| `mp_dogtag_pickup_rule` | `Int32` | `0` |  | `gamedll` `replicated` `release` `commandline_enforced` | Who is eligible to pick up a dogtag (0 = killer only, 1 = killer's team, 2 = victim's team, 3 = killer &amp; victim's team, 4 = anyone) |
| `mp_drop_grenade_enable` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Allows players to drop grenades. |
| `mp_drop_knife_enable` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Allows players to drop knives. |
| `mp_economy_reset_rounds` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Reset all player money every N rounds (0 for never) |
| `mp_endmatch_votenextleveltime` | `Float32` | `20.000000` |  | `gamedll` `release` | If mp_endmatch_votenextmap is set, players have this much time to vote on the next map at match end. |
| `mp_endmatch_votenextmap` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` | Whether or not players vote for the next map at the end of the match when the final scoreboard comes up |
| `mp_endmatch_votenextmap_keepcurrent` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` | If set, keeps the current map in the list of voting options.  If not set, the current map will not appear in the list of voting options. |
| `mp_endmatch_votenextmap_wargames_modes` | `String` |  |  | `gamedll` `release` | Modes available for endmatch voting during War Games. Separate names with spaces. |
| `mp_endmatch_votenextmap_wargames_nummaps` | `Int32` | `3` |  | `gamedll` `release` | Maximum number of maps to include in endmatch voting during War Games |
| `mp_endmatch_votenextmap_wargames_nummodes` | `Int32` | `1` |  | `gamedll` `release` | Maximum number of other War Games to include in endmatch voting during War Games |
| `mp_endwarmup_player_count` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` | Number of players required to be connected to end warmup early. 0 to require maximum players for mode. |
| `mp_equipment_reset_rounds` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Reset all player equipment every N rounds (0 for never) |
| `mp_fadetoblack` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `defensive` | fade a player's screen to black when he dies |
| `mp_flinch_punch_scale` | `Float32` | `3.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Scalar for first person view punch when getting hit. |
| `mp_footsteps_serverside` | `Bool` | `true` |  | `gamedll` `release` | Makes the server always play footstep sounds. Clients never calculate footstep sounds locally, instead relying on the server. |
| `mp_force_pick_time` | `Float32` | `15.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The amount of time a player has on the team screen to make a selection before being auto-teamed |
| `mp_forcecamera` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Restricts spectator modes for dead players |
| `mp_forcerespawn` | `Bool` | `true` |  | `developmentonly` `gamedll` `notify` `defensive` |  |
| `mp_fraglimit` | `Int32` | `0` |  | `gamedll` `notify` `release` |  |
| `mp_free_armor` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines whether kevlar (1+) and/or helmet (2+) are given automatically. |
| `mp_freezetime` | `Int32` | `6` | `0 .. 60` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | how many seconds to keep players frozen when the round starts |
| `mp_friendlyfire` | `Bool` | `false` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | Allows team members to injure other members of their team |
| `mp_give_player_c4` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Whether this map should spawn a c4 bomb for a player or not. |
| `mp_global_damage_per_second` | `Float32` | `0.000000` | `>= 0.000000` | `gamedll` `replicated` `release` `commandline_enforced` | If above 0, deal non-lethal damage to players over time. |
| `mp_guardian_bomb_plant_custom_x_mark_location` | `String` |  |  | `gamedll` `clientdll` `replicated` `release` | x,y,z to display an X for the bomb plant in guardian missions with custom bomb plant boundaries. |
| `mp_guardian_target_site` | `Int32` | `-1` |  | `gamedll` `release` `commandline_enforced` | If set to the index of a bombsite, will cause random spawns to be only created near that site. |
| `mp_halftime` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines whether the match switches sides in a halftime event. |
| `mp_halftime_duration` | `Float32` | `15.000000` | `0.000000 .. 300.000000` | `gamedll` `clientdll` `replicated` `release` | Target number of seconds that halftime lasts; shortened if team intros are active |
| `mp_halftime_pausematch` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` | Set to 1 to pause match after halftime countdown elapses. Match must be resumed by vote or admin. |
| `mp_halftime_pausetimer` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Set to 1 to stay in halftime indefinitely. Set to 0 to resume the timer. |
| `mp_hostages_max` | `Int32` | `2` |  | `gamedll` `replicated` `release` `commandline_enforced` | Maximum number of hostages to spawn. |
| `mp_hostages_rescuetime` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` | Additional time added to round time if a hostage is reached by a CT. |
| `mp_hostages_rescuetowin` | `Int32` | `1` |  | `developmentonly` `gamedll` `clientdll` `replicated` | 0 == all alive, any other number is the number the CT's need to rescue to win the round. |
| `mp_hostages_run_speed_modifier` | `Float32` | `1.000000` | `0.100000 .. 1.500000` | `gamedll` `replicated` `release` | Default is 1.0, slow down hostages by setting this to &lt; 1.0. |
| `mp_hostages_spawn_farthest` | `Bool` | `false` |  | `gamedll` `replicated` `release` | When enabled will consistently force the farthest hostages to spawn. |
| `mp_hostages_spawn_force_positions` | `String` |  |  | `gamedll` `replicated` `release` `commandline_enforced` | Comma separated list of zero based indices to force spawn positions, e.g. '0,2' or '1,6' |
| `mp_hostages_spawn_force_positions_xyz` | `String` |  |  | `gamedll` `replicated` `release` | Comma separated list of xyz locations to force spawn positions, e.g. 'x1 y1 z1,x2 y2 z2' |
| `mp_hostages_spawn_same_every_round` | `Bool` | `true` |  | `gamedll` `replicated` `release` `commandline_enforced` | 0 = spawn hostages randomly every round, 1 = same spawns for entire match. |
| `mp_hostages_takedamage` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | Whether or not hostages can be hurt. |
| `mp_humanteam` | `String` | `any` |  | `gamedll` `replicated` `release` | Restricts human players to a single team {any, CT, T} |
| `mp_ignore_round_win_conditions` | `Bool` | `false` |  | `gamedll` `replicated` `release` | Ignore conditions which would end the current round |
| `mp_items_prohibited` | `String` |  |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Set this convar to a comma-delimited list of definition indices of weapons that should be prohibited from use. |
| `mp_join_grace_time` | `Float32` | `0.000000` | `0.000000 .. 30.000000` | `gamedll` `clientdll` `replicated` `release` | Number of seconds after round start to allow a player to join a game |
| `mp_limitteams` | `Int32` | `2` | `0 .. 30` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | Max # of players 1 team can have over another (0 disables check) |
| `mp_logdetail` | `Int32` | `0` | `0 .. 3` | `gamedll` `release` | Logs attacks.  Values are: 0=off, 1=enemy, 2=teammate, 3=both) |
| `mp_logdetail_items` | `Bool` | `false` |  | `gamedll` `release` | Logs a line any time a player acquires or loses an item. |
| `mp_logmoney` | `Bool` | `false` |  | `gamedll` `release` | Enables money logging.  Values are: 0=off, 1=on |
| `mp_match_can_clinch` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Can a team clinch and end the match by being so far ahead that the other team has no way to catching up? |
| `mp_match_end_changelevel` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | At the end of the match, perform a changelevel even if next map is the same |
| `mp_match_end_restart` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | At the end of the match, perform a restart instead of loading a new map |
| `mp_match_restart_delay` | `Int32` | `25` | `1 .. 9999` | `gamedll` `clientdll` `replicated` `release` | Time (in seconds) until a match restarts. |
| `mp_max_armor` | `Int32` | `2` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines the highest level of armor allowed to be purchased. (0) None, (1) Kevlar, (2) Helmet |
| `mp_maxmoney` | `Int32` | `16000` | `>= 0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | maximum amount of money allowed in a player's account |
| `mp_maxrounds` | `Int32` | `0` | `>= 0` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | max number of rounds to play before server changes maps |
| `mp_min_halftime_duration` | `Float32` | `8.500000` | `0.000000 .. 300.000000` | `gamedll` `clientdll` `replicated` `release` | Minimum number of seconds that halftime lasts even if team intros are active |
| `mp_only_cts_rescue_hostages` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `mp_overtime_enable` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | If a match ends in a tie, use overtime rules to determine winner |
| `mp_overtime_halftime_pausetimer` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` | If set to 1 will set mp_halftime_pausetimer to 1 before every half of overtime. Set mp_halftime_pausetimer to 0 to resume the timer. |
| `mp_overtime_limit` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` | When overtime is enabled, only so many overtimes can be played |
| `mp_overtime_maxrounds` | `Int32` | `6` |  | `gamedll` `clientdll` `replicated` `release` | When overtime is enabled play additional rounds to determine winner |
| `mp_overtime_startmoney` | `Int32` | `10000` |  | `gamedll` `clientdll` `replicated` `release` | Money assigned to all players at start of every overtime half |
| `mp_plant_c4_anywhere` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `mp_playercashawards` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Players can earn money by performing in-game actions |
| `mp_playerid` | `Int32` | `0` | `0 .. 2` | `gamedll` `clientdll` `replicated` `release` | Controls what information player see in the status bar: 0 all names; 1 team names; 2 no names |
| `mp_playerid_delay` | `Float32` | `0.400000` | `0.000000 .. 1.000000` | `gamedll` `clientdll` `replicated` `release` | Number of seconds to delay showing information in the status bar |
| `mp_playerid_hold` | `Float32` | `0.100000` | `0.000000 .. 1.000000` | `gamedll` `clientdll` `replicated` `release` | Number of seconds to keep showing old information in the status bar |
| `mp_promoted_item_enabled` | `Bool` | `false` |  | `gamedll` `clientdll` `notify` `replicated` `release` | Allow the purchasing of the promoted item. |
| `mp_randomspawn` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines whether players are to spawn. 0 = default; 1 = both teams; 2 = Terrorists; 3 = CTs. |
| `mp_randomspawn_dist` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If using mp_randomspawn, determines whether to test distance when selecting this spot. |
| `mp_randomspawn_los` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If using mp_randomspawn, determines whether to test Line of Sight when spawning. |
| `mp_require_gun_use_to_acquire` | `Bool` | `false` |  | `gamedll` `release` | Whether guns must be +used to acquire or default is touch-to-pickup |
| `mp_respawn_immunitytime` | `Float32` | `4.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How many seconds after respawn immunity lasts. Set to negative value to disable warmup immunity. |
| `mp_respawn_on_death_ct` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | When set to 1, counter-terrorists will respawn after dying. |
| `mp_respawn_on_death_t` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | When set to 1, terrorists will respawn after dying. |
| `mp_respawnwavetime_ct` | `Float32` | `10.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Time between respawn waves for CTs. |
| `mp_respawnwavetime_t` | `Float32` | `10.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Time between respawn waves for Terrorists. |
| `mp_restartgame` | `Int32` | `0` |  | `gamedll` `release` | If non-zero, game will restart in the specified number of seconds |
| `mp_retake_ct_count` | `Int32` | `4` |  | `gamedll` `clientdll` `replicated` `release` | Number of CT's when playing retakes. |
| `mp_retake_ct_loadout_bonus_card` | `String` | `#GameUI_Retake_Card_TheAWPortunity,1,1,weapon_awp` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT bonus card for full buy round when playing bomb site retake. |
| `mp_retake_ct_loadout_bonus_card_availability` | `String` | `1,2` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT bonus card availability pattern for full buy round when playing bomb site retake. |
| `mp_retake_ct_loadout_default_pistol_round` | `String` | `1&#124;3;#GameUI_Retake_Card_4v3,1,0,secondary0&#124;1;#GameUI_Retake_Card_FlashOut,0,0,secondary0,grenade0;#GameUI_Retake_Card_HideAndPeek,0,0,secondary0,grenade1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT Loadouts for default pistol round when playing bomb site retake. |
| `mp_retake_ct_loadout_enemy_card` | `String` | `#GameUI_Retake_Card_BehindEnemyLines,1,1,rifle1,grenade2` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT enemy card for full buy round when playing bomb site retake. |
| `mp_retake_ct_loadout_full_buy_round` | `String` | `4&#124;2;#GameUI_Retake_Card_LightEmUp,1,1,rifle1,grenade0&#124;2;#GameUI_Retake_Card_Kobe,1,1,rifle1,grenade2&#124;1;#GameUI_Retake_Card_1g,1,1,rifle1,grenade3&#124;1;#GameUI_Retake_Card_DisappearingAct,1,1,rifle1,grenade1&#124;1;#GameUI_Retake_Card_EyesOnTarget,1,1,weapon_aug` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT Loadouts for full buy round when playing bomb site retake. |
| `mp_retake_ct_loadout_light_buy_round` | `String` | `3&#124;2;#GameUI_Retake_Card_UmpInSmoke,1,1,weapon_ump45,grenade1&#124;2;#GameUI_Retake_Card_FunNGun,1,1,weapon_mp9,grenade2&#124;2;#GameUI_Retake_Card_Sharpshooter,1,1,weapon_ssg08,grenade0&#124;2;#GameUI_Retake_Card_BurstBullpup,1,1,weapon_famas` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT Loadouts for force buy round when playing bomb site retake. |
| `mp_retake_ct_loadout_upgraded_pistol_round` | `String` | `2&#124;2;#GameUI_Retake_Card_TakeFive,0,0,weapon_fiveseven&#124;2;#GameUI_Retake_Card_BlindFire,1,0,weapon_p250,grenade0&#124;2;#GameUI_Retake_Card_OnlyTakesOne,0,0,weapon_deagle&#124;2;#GameUI_Retake_Card_SneakyBeakyLike,0,0,weapon_p250,grenade1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT Loadouts for upgraded pistol round when playing bomb site retake. |
| `mp_retake_max_consecutive_rounds_same_target_site` | `Int32` | `2` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Limit the number of consecutive rounds targeting the same site. |
| `mp_retake_t_count` | `Int32` | `3` |  | `gamedll` `clientdll` `replicated` `release` | Number of terrorists when playing retakes. |
| `mp_retake_t_loadout_bonus_card` | `String` | `#GameUI_Retake_Card_TheAWPortunity,1,1,weapon_awp` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T bonus card for full buy round when playing bomb site retake. |
| `mp_retake_t_loadout_bonus_card_availability` | `String` | `1,1,2` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T bonus card availability pattern for full buy round when playing bomb site retake. |
| `mp_retake_t_loadout_default_pistol_round` | `String` | `0&#124;3;#GameUI_Retake_Card_4BadGuysLeft,1,0,secondary0&#124;1;#GameUI_Retake_Card_LookAway,0,0,secondary0,grenade0;#GameUI_Retake_Card_WhenThereIsSmoke,0,0,secondary0,grenade1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T Loadouts for default pistol round when playing bomb site retake. |
| `mp_retake_t_loadout_enemy_card` | `String` | `#GameUI_Retake_Card_FindersKeepers,1,1,rifle1,grenade0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T enemy card for full buy round when playing bomb site retake. |
| `mp_retake_t_loadout_full_buy_round` | `String` | `0&#124;2;#GameUI_Retake_Card_OlReliable,1,1,rifle1,grenade0&#124;1;#GameUI_Retake_Card_SmokeShow,1,1,rifle1,grenade1&#124;1;#GameUI_Retake_Card_HotShot,1,1,rifle1,grenade3&#124;1;#GameUI_Retake_Card_EyeSpy,1,1,weapon_sg556,grenade2` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T Loadouts for full buy round when playing bomb site retake. |
| `mp_retake_t_loadout_light_buy_round` | `String` | `0&#124;2;#GameUI_Retake_Card_BackInAFlash,1,1,weapon_ump45,grenade0&#124;2;#GameUI_Retake_Card_AllIn,1,1,weapon_galilar&#124;1;#GameUI_Retake_Card_BoomBox,1,1,weapon_mac10,grenade2,grenade1&#124;1;#GameUI_Retake_Card_SetThemFree,1,1,weapon_ssg08,grenade0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T Loadouts for force buy round when playing bomb site retake. |
| `mp_retake_t_loadout_upgraded_pistol_round` | `String` | `0&#124;2;#GameUI_Retake_Card_BlindFire,1,0,weapon_elite,grenade0&#124;2;#GameUI_Retake_Card_QueOta,0,0,weapon_deagle&#124;1;#GameUI_Retake_Card_SmokeScreen,0,0,weapon_p250,grenade1&#124;1;#GameUI_Retake_Card_TecTecBoom,0,0,weapon_tec9,grenade2` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T Loadouts for upgraded pistol round when playing bomb site retake. |
| `mp_round_restart_delay` | `Float32` | `7.000000` | `>= 0.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Number of seconds to delay before restarting a round after a win |
| `mp_roundtime` | `Float32` | `5.000000` | `0.100000 .. 60.000000` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | How many minutes each round takes. |
| `mp_roundtime_defuse` | `Float32` | `0.000000` | `0.000000 .. 60.000000` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | How many minutes each round of Bomb Defuse takes. If 0 then use mp_roundtime instead. |
| `mp_roundtime_hostage` | `Float32` | `0.000000` | `0.000000 .. 60.000000` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | How many minutes each round of Hostage Rescue takes. If 0 then use mp_roundtime instead. |
| `mp_shoot_dropped_grenades` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Dropped grenades detonate when shot. |
| `mp_shorthanded_cash_bonus_ignore_kicked` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` | Determines whether kicked players are included in the assessment for short-handedness |
| `mp_shorthanded_cash_bonus_round_delay` | `Int32` | `2` |  | `gamedll` `clientdll` `replicated` `release` | number of previous rounds that a team needs to have been shorthanded before they are eligible for the short-handed bonus |
| `mp_solid_enemies` | `Int32` | `1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How solid are enemies: 0 = transparent; 1 = fully solid |
| `mp_solid_teammates` | `Int32` | `1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How solid are teammates: 0 = transparent; 1 = fully solid; 2 = can stand on top of heads |
| `mp_spawnprotectiontime` | `Int32` | `5` |  | `gamedll` `replicated` `release` | Kick players who team-kill within this many seconds of a round restart. |
| `mp_spectators_max` | `Int32` | `2` | `>= 0` | `gamedll` `clientdll` `replicated` `release` | How many spectators are allowed in a match. |
| `mp_starting_losses` | `Int32` | `0` | `>= 0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines what the initial loss streak is. |
| `mp_startmoney` | `Int32` | `800` | `>= 0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | amount of money each player gets when they reset |
| `mp_suicide_penalty` | `Bool` | `true` |  | `gamedll` `release` `commandline_enforced` | Punish players for suicides |
| `mp_t_default_grenades` | `String` |  |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default grenades that the Ts will spawn with.	To give multiple grenades, separate each weapon class with a space like this: 'weapon_molotov weapon_hegrenade' |
| `mp_t_default_melee` | `String` | `weapon_knife` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default melee weapon that the Ts will spawn with |
| `mp_t_default_primary` | `String` |  |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default primary (rifle) weapon that the Ts will spawn with |
| `mp_t_default_secondary` | `String` | `weapon_glock` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default secondary (pistol) weapon that the Ts will spawn with |
| `mp_tagging_scale` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scalar for player tagging modifier when hit. Lower values for greater tagging. |
| `mp_taser_recharge_time` | `Float32` | `30.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines recharge time for taser. -1 = disabled. |
| `mp_td_dmgtokick` | `Int32` | `300` |  | `gamedll` `replicated` `release` | The damage threshhold players have to exceed in a match to get kicked. |
| `mp_td_dmgtowarn` | `Int32` | `200` |  | `gamedll` `replicated` `release` | The damage threshhold players have to exceed in a match to get warned that they are about to be kicked. |
| `mp_td_spawndmgthreshold` | `Int32` | `50` |  | `gamedll` `replicated` `release` | The damage threshold players have to exceed at the start of the round to be warned/kick. |
| `mp_team_intro_time` | `Float32` | `6.500000` | `>= 0.000000` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | How many seconds for team intro |
| `mp_team_timeout_max` | `Int32` | `1` |  | `gamedll` `clientdll` `replicated` `release` | Number of timeouts each team gets per match. |
| `mp_team_timeout_ot_add_each` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` | Number of timeouts to add for each team when match goes to 2nd and each next overtime. |
| `mp_team_timeout_ot_add_once` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` | Number of timeouts to add for each team when regulation time ends and match goes to overtime. |
| `mp_team_timeout_ot_max` | `Int32` | `1` |  | `gamedll` `clientdll` `replicated` `release` | Max number of timeouts each team can have per OT after all OT timeouts got added. |
| `mp_team_timeout_time` | `Int32` | `60` |  | `gamedll` `clientdll` `replicated` `release` | Duration of each timeout. |
| `mp_teamcashawards` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Teams can earn money by performing in-game actions |
| `mp_teamflag_1` | `String` |  |  | `gamedll` `release` | Enter a country's alpha 2 code to show that flag next to team 1's name in the spectator scoreboard. |
| `mp_teamflag_2` | `String` |  |  | `gamedll` `release` | Enter a country's alpha 2 code to show that flag next to team 2's name in the spectator scoreboard. |
| `mp_teamlogo_1` | `String` |  |  | `gamedll` `release` | Enter a team's shorthand image name to display their logo. Images can be found here: 'resource/flash/econ/tournaments/teams' |
| `mp_teamlogo_2` | `String` |  |  | `gamedll` `release` | Enter a team's shorthand image name to display their logo. Images can be found here: 'resource/flash/econ/tournaments/teams' |
| `mp_teammatchstat_1` | `String` |  |  | `gamedll` `release` | A non-empty string sets first team's match stat. |
| `mp_teammatchstat_2` | `String` |  |  | `gamedll` `release` | A non-empty string sets second team's match stat. |
| `mp_teammatchstat_cycletime` | `Float32` | `45.000000` |  | `gamedll` `release` | Cycle match stats after so many seconds |
| `mp_teammatchstat_holdtime` | `Float32` | `5.000000` |  | `gamedll` `release` | Decide on a match stat and hold it additionally for at least so many seconds |
| `mp_teammatchstat_txt` | `String` |  |  | `gamedll` `release` | A non-empty string sets the match stat description, e.g. 'Match 2 of 3'. |
| `mp_teammates_are_enemies` | `Bool` | `false` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | When set, your teammates act as enemies and all players are valid targets. |
| `mp_teamname_1` | `String` |  |  | `gamedll` `release` | A non-empty string overrides the first team's name. |
| `mp_teamname_2` | `String` |  |  | `gamedll` `release` | A non-empty string overrides the second team's name. |
| `mp_teamplay` | `Bool` | `false` |  | `developmentonly` `gamedll` `notify` `defensive` |  |
| `mp_teamprediction_pct` | `Int32` | `0` |  | `gamedll` `release` | A value between 1 and 99 will show predictions in favor of CT team. |
| `mp_teamprediction_txt` | `String` | `#SFUIHUD_Spectate_Predictions` |  | `gamedll` `release` | A value between 1 and 99 will set predictions in favor of first team. |
| `mp_teamscore_1` | `Int32` | `0` |  | `gamedll` `release` | A non-empty string for best-of-N maps won by the first team. |
| `mp_teamscore_2` | `Int32` | `0` |  | `gamedll` `release` | A non-empty string for best-of-N maps won by the second team. |
| `mp_teamscore_max` | `Int32` | `0` | `0 .. 7` | `gamedll` `release` | How many maps to win the series (bo3 max=2; bo5 max=3; bo7 max=4) |
| `mp_technical_timeout_duration_s` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How many seconds is a full technical timeout? |
| `mp_technical_timeout_per_team` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How many technical timeouts are there per team? |
| `mp_timelimit` | `Float32` | `0.000000` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | game time per map in minutes |
| `mp_tkpunish` | `Int32` | `0` |  | `gamedll` `replicated` `release` | Will TK'ers and team damagers be punished in the next round?  {0=no,  1=yes} |
| `mp_tournament` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `defensive` |  |
| `mp_tournament_whitelist` | `String` | `item_whitelist.txt` |  | `developmentonly` `gamedll` `defensive` | Specifies the item whitelist file to use. |
| `mp_use_respawn_waves` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | When set to 1, and that player's team is set to respawn, they will respawn in waves. If set to 2, teams will respawn when the whole team is dead. |
| `mp_verbose_changelevel_spew` | `Int32` | `1` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `mp_warmup_items_drop_policy` | `Int32` | `247` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Which items can drop during warmup (bitfield, 1=gun, 2=c4, 4=nade, 8=defuser, 16=taser, 32=healthshot) |
| `mp_warmup_items_nocost` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines whether weapons are free to buy during warmup. |
| `mp_warmup_items_nocount_policy` | `Int32` | `42` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Which items are unlimited during warmup (bitfield, 1=gun, 2=c4, 4=nade, 8=defuser/kevlar, 16=taser, 32=healthshot) |
| `mp_warmup_jointeam_cooldown` | `Float32` | `2.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `mp_warmup_offline_enabled` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | Whether or not to do a warmup period at the start of a match in an offline (bot) match. |
| `mp_warmup_online_enabled` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` | Whether or not to do a warmup period at the start of an online match. |
| `mp_warmup_pausetimer` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Set to 1 to stay in warmup indefinitely. Set to 0 to resume the timer. |
| `mp_warmuptime` | `Float32` | `30.000000` | `>= 5.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How long the warmup period lasts. Changing this value resets warmup. |
| `mp_warmuptime_all_players_connected` | `Float32` | `0.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Warmup time to use when all players have connected. 0 to disable. |
| `mp_warmuptime_match_cancelled` | `Float32` | `5.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Warmup time to use when the match will be cancelled (eg. due to a live VAC ban). |
| `mp_weapon_next_owner_touch_time` | `Float32` | `1.300000` |  | `gamedll` `cheat` `release` |  |
| `mp_weapon_prev_owner_touch_time` | `Float32` | `1.500000` |  | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `mp_weapon_self_inflict_amount` | `Float32` | `0.000000` |  | `gamedll` `replicated` `release` `commandline_enforced` | If Set to non-0, will hurt the attacker by the specified fraction of max damage if they miss. |
| `mp_weapons_allow_heavy` | `Int32` | `-1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines which team, if any, can purchase Heavy guns. -1 = any; 0 = non; 2 = Ts; 3 = CTs. |
| `mp_weapons_allow_map_placed` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If this convar is set, when a match starts, the game will not delete weapons placed in the map. |
| `mp_weapons_allow_pistols` | `Int32` | `-1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines which team, if any, can purchase Pistols. -1 = any; 0 = non; 2 = Ts; 3 = CTs. |
| `mp_weapons_allow_rifles` | `Int32` | `-1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines which team, if any, can purchase Rifles. -1 = any; 0 = non; 2 = Ts; 3 = CTs. |
| `mp_weapons_allow_smgs` | `Int32` | `-1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines which team, if any, can purchase SMGs. -1 = any; 0 = non; 2 = Ts; 3 = CTs. |
| `mp_weapons_allow_typecount` | `Int32` | `5` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines how many purchases of each weapon type allowed per player per round (0 to disallow purchasing, -1 to have no limit). |
| `mp_weapons_allow_zeus` | `Int32` | `1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines how many Zeus purchases a player can make per round (0 to disallow, -1 to have no limit). |
| `mp_weapons_max_gun_purchases_per_weapon_per_match` | `Int32` | `-1` | `-1 .. 1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Max number of times a player may purchase any weapon per match |
| `mp_weaponstay` | `Bool` | `false` |  | `developmentonly` `gamedll` `notify` `defensive` |  |
| `mp_win_panel_display_time` | `Float32` | `3.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The amount of time to show the win panel between matches / halfs |
| `mp_winlimit` | `Int32` | `0` | `>= 0` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `defensive` | Max score one team can reach before server changes maps |
| `multigpu_skip_semaphores` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `multigpu_skip_transfers` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `muzzle_flash_debug` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `name` | `String` | `unnamed` |  | `archive` `per_user` |  |
| `nav_approach_points_area_size_threshold` | `Float32` | `200.000000` |  | `developmentonly` `gamedll` `defensive` | Ignore nav areas with at least one side smaller than this amount during approach point calculation. |
| `nav_attribute_obstacle_draw` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `nav_attribute_obstacle_draw_attribute` | `String` |  |  | `developmentonly` `gamedll` |  |
| `nav_attribute_obstacle_draw_elements` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `nav_bfs_debug` | `Int32` | `0` |  | `gamedll` `cheat` |  |
| `nav_create_indirect_connection_set_from` | `Vector3` | `0.000000 0.000000 0.000000` |  | `gamedll` `cheat` | Set the 'from' location of an indirect connection. |
| `nav_create_indirect_connection_set_to` | `Vector3` | `0.000000 0.000000 0.000000` |  | `gamedll` `cheat` | Set the 'to' location of an indirect connection. |
| `nav_curve_alt` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_curve_iter` | `Int32` | `0` |  | `gamedll` `cheat` |  |
| `nav_curve_lock` | `Int32` | `-1` |  | `gamedll` `cheat` |  |
| `nav_curve_max_step` | `Float32` | `10.000000` |  | `gamedll` `cheat` |  |
| `nav_curve_set` | `Int32` | `-1` |  | `gamedll` `cheat` |  |
| `nav_curve_step` | `Float32` | `0.020000` |  | `gamedll` `cheat` |  |
| `nav_debug_blocked` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_drag_selection_volume_zmax_offset` | `Int32` | `32` |  | `developmentonly` `gamedll` `replicated` `defensive` | The offset of the nav drag volume top from center |
| `nav_drag_selection_volume_zmin_offset` | `Int32` | `32` |  | `developmentonly` `gamedll` `replicated` `defensive` | The offset of the nav drag volume bottom from center |
| `nav_draw_area_connections` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_area_filled` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_draw_area_gravity` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_area_ground` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_area_hull_support` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_area_ids` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_area_inset_margin` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_draw_area_normal` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_area_should_be_destroyed` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_area_split_by_obstacle_mgr` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_area_ztest` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_attribute_dynamic` | `String` |  |  | `developmentonly` `gamedll` | Draw all nav areas with this dynamic attribute |
| `nav_draw_attribute_game` | `String` |  |  | `developmentonly` `gamedll` | Draw all nav areas with this game attribute |
| `nav_draw_attribute_space` | `String` |  |  | `developmentonly` `gamedll` | Draw only nav blocks with this attribute |
| `nav_draw_blocked` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_draw_blocked_connections` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_boundary_areas` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_connected_area_radius` | `Float32` | `1000.000000` |  | `gamedll` `cheat` |  |
| `nav_draw_dangerareas` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_dormant_movable_meshes` | `Bool` | `false` |  | `gamedll` `cheat` | Draw dormant movable meshes. |
| `nav_draw_externally_created` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_flow_map` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_hidingspots` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_indirect_connections` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_jump_links` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_limit` | `Int32` | `300` |  | `gamedll` `cheat` | The maximum number of areas to draw in edit mode |
| `nav_draw_link_alignment` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_links` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_draw_markup` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_draw_mesh` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_draw_mesh_grid` | `Bool` | `false` |  | `gamedll` `cheat` | Draw the mesh's spatial grid structure around the edit cursor position. |
| `nav_draw_mesh_offset` | `Float32` | `1.000000` |  | `gamedll` `cheat` | Vertical offset for drawing the mesh (useful for flat planes where the mesh is often a fixed offset from the physical ground |
| `nav_draw_space_boundary` | `Int32` | `0` |  | `developmentonly` `gamedll` | Draw the boundaries of the 3d nav space. 1 = draw flying space, 2 = draw swimming space |
| `nav_draw_space_cells` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `nav_draw_space_fly` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `nav_draw_space_neighbors` | `Int32` | `0` |  | `developmentonly` `gamedll` |  |
| `nav_draw_space_portals` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `nav_draw_space_radius` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` |  |
| `nav_draw_space_swim` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `nav_draw_space_transitions` | `Bool` | `true` |  | `developmentonly` `gamedll` |  |
| `nav_edit` | `Int32` | `0` |  | `gamedll` `cheat` | Set to one to interactively edit the Navigation Mesh. Set to zero to leave edit mode. |
| `nav_edit_draw_navlinks` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_edit_use_camera` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_edit_validate` | `Bool` | `false` |  | `gamedll` `cheat` | Validate navmesh structures. |
| `nav_find_occluded_node_nozup_use_raycast` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_flow_map_enabled` | `Bool` | `true` |  | `developmentonly` `gamedll` |  |
| `nav_gen_add_jumps` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_gen_agent_radius_buffer` | `Float32` | `0.500000` |  | `gamedll` `cheat` | Buffer to add to agent radius before passing to nav gen |
| `nav_gen_clip_polys_to_clearance` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_gen_clip_polys_to_clearance_debug` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_gen_connect_allow_multiple` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_gen_connect_angle` | `Float32` | `0.750000` |  | `gamedll` `cheat` |  |
| `nav_gen_connect_angle_ignore_z` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_gen_connect_dist_a` | `Float32` | `1.000000` |  | `gamedll` `cheat` |  |
| `nav_gen_connect_dist_b` | `Float32` | `1.500000` |  | `gamedll` `cheat` |  |
| `nav_gen_connect_dist_z_mult` | `Float32` | `0.500000` |  | `gamedll` `cheat` |  |
| `nav_gen_connect_overlap` | `Float32` | `0.500000` |  | `gamedll` `cheat` |  |
| `nav_gen_degen_limit` | `Float32` | `0.001000` |  | `gamedll` `cheat` |  |
| `nav_gen_false` | `Bool` | `false` |  | `gamedll` `cheat` | Always false |
| `nav_gen_island_removal` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_gen_island_removal_all_hulls` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_gen_join_nonzup` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_gen_jump_connection_min_overlap_ratio` | `Float32` | `1.000000` |  | `gamedll` `cheat` | Minimum edge overlap required for jump connection consideration as a percentage of agent radius |
| `nav_gen_markup_split_expand` | `Float32` | `2.000000` |  | `gamedll` `cheat` |  |
| `nav_gen_markup_split_tol_base` | `Float32` | `1.000000` |  | `gamedll` `cheat` |  |
| `nav_gen_markup_split_tol_nonav` | `Float32` | `1.000000` |  | `gamedll` `cheat` |  |
| `nav_gen_markup_split_tol_nonentity` | `Float32` | `8.000000` |  | `gamedll` `cheat` |  |
| `nav_gen_max_bottleneck_width` | `Float32` | `128.000000` |  | `gamedll` `cheat` |  |
| `nav_gen_max_bottleneck_width_do_clip` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_gen_max_edge_len` | `Float32` | `512.000000` |  | `gamedll` `cheat` |  |
| `nav_gen_max_edge_len_do_clip` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_gen_max_edge_len_split_tol` | `Float32` | `24.000000` |  | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_angle_limit` | `Float32` | `8.000000` |  | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_num_steps` | `Int32` | `6` |  | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_planar_deviation_limit` | `Float32` | `4.000000` |  | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_se_limit_end` | `Float32` | `0.100000` |  | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_se_limit_start` | `Float32` | `0.000010` |  | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_weld_limit_end` | `Float32` | `0.010000` |  | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_weld_limit_start` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_gen_oriented_angle_tol` | `Float32` | `15.000000` |  | `gamedll` `cheat` | Max abrupt orientation difference an NPC can tolerate when moving through the mesh (degrees). |
| `nav_gen_oriented_max_region_range` | `Float32` | `15.000000` |  | `gamedll` `cheat` | Max orientation range allowed within a region before it gets further split. |
| `nav_gen_remove_vertical_polys` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_gen_split_boundary_polys` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_gen_split_multi_connection_polys` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_gen_split_multi_connection_polys_tol` | `Float32` | `0.010000` |  | `gamedll` `cheat` |  |
| `nav_gen_true` | `Bool` | `true` |  | `gamedll` `cheat` | Always true |
| `nav_gen_vertical_limit` | `Float32` | `88.000000` |  | `gamedll` `cheat` |  |
| `nav_genrt_debug` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_ignore_vpk_navdata` | `Bool` | `false` |  | `developmentonly` `gamedll` | For testing using legacy nav data |
| `nav_max_view_distance` | `Float32` | `0.000000` |  | `gamedll` `cheat` | Maximum range for precomputed nav mesh visibility (0 = default 1500 units) |
| `nav_obstacle_validate` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_obstruction_async_update` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `nav_obstruction_draw` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_obstruction_draw_change` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_obstruction_draw_dist` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `nav_obstruction_draw_island` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_obstruction_draw_island_hull` | `Int32` | `-1` |  | `gamedll` `cheat` |  |
| `nav_obstruction_draw_movefail_blocking` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_path_debug` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_path_draw_areas` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_path_draw_arrow` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_path_draw_climb_segments` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_path_draw_connected_areas` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_path_draw_ground_segments` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_path_draw_jump_segments` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_path_draw_ladder_segments` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_path_draw_link_segments` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_path_draw_tick` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_path_fixup_climb_up_segments` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_path_fixup_gap_segments` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_path_jump_process_debug` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_path_optimize` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_path_optimize_portals` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_path_optimizer_debug` | `Int32` | `0` |  | `gamedll` `cheat` |  |
| `nav_pathfind_debug_log` | `Int32` | `0` |  | `gamedll` `cheat` |  |
| `nav_pathfind_draw` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_pathfind_draw_blocked` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_pathfind_draw_costs` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_pathfind_draw_fail` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_pathfind_draw_total_costs` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_pathfind_inadmissable_heuristic_factor` | `Float32` | `1.000000` |  | `gamedll` `cheat` |  |
| `nav_pathfind_multithread` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_potentially_visible_dot_tolerance` | `Float32` | `0.980000` |  | `gamedll` `cheat` |  |
| `nav_recorder_enabled` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_select_allow_blocked` | `Bool` | `true` |  | `gamedll` `cheat` | When selecting an area under nav_edit, allow area marked as blocked. |
| `nav_select_area_id` | `Int32` | `-1` |  | `gamedll` `cheat` | Select nav area with matching ID. |
| `nav_select_block_id` | `Int32` | `-1` |  | `gamedll` `cheat` | Select nav space block with matching ID. |
| `nav_select_hull` | `Int32` | `0` |  | `gamedll` `cheat` | Restrict area selection to areas that can support a hull of the given category |
| `nav_show_area_connections` | `Bool` | `true` |  | `gamedll` `cheat` | Show connections to selected area when true |
| `nav_show_area_verts` | `Bool` | `true` |  | `gamedll` `cheat` | Show area vertex positions |
| `nav_show_area_water_info` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_show_elem_info` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_show_elem_info_font` | `String` | `Consolas` |  | `gamedll` `cheat` |  |
| `nav_show_elem_info_font_size` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `nav_show_elem_info_font_voffset` | `Float32` | `-11.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_constrain_spline` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_smooth_constrain_spline_relax` | `Float32` | `0.006000` |  | `gamedll` `cheat` |  |
| `nav_smooth_constrain_spring` | `Int32` | `2` |  | `gamedll` `cheat` |  |
| `nav_smooth_constrain_spring_relax` | `Float32` | `0.010000` |  | `gamedll` `cheat` |  |
| `nav_smooth_draw_boundary` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_draw_calc` | `Int32` | `0` |  | `gamedll` `cheat` |  |
| `nav_smooth_draw_constraint_spline` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_smooth_draw_constraint_spring` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_draw_speed` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_enable` | `Int32` | `1` |  | `gamedll` `cheat` |  |
| `nav_smooth_push_from_walls` | `Float32` | `12.000000` |  | `developmentonly` `gamedll` |  |
| `nav_smooth_relax` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_smooth_relax_use_timesteps` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_const_override` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_enable` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_factor_deriv` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_factor_dist` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_factor_speed` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_forward_dist_base` | `Float32` | `50.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_forward_dist_time_limit` | `Float32` | `1.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_max_dist` | `Float32` | `36.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_tension_max_override` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_timestep_factor_accel` | `Float32` | `100.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_timestep_factor_speed` | `Float32` | `100.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_timestep_max` | `Float32` | `0.500000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_timestep_min` | `Float32` | `0.100000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_yaw_rotation_speed` | `Float32` | `50.000000` |  | `gamedll` `cheat` |  |
| `nav_smooth_spring_yaw_threshold` | `Float32` | `20.000000` |  | `gamedll` `cheat` |  |
| `nav_space_select_dist` | `Float32` | `1000.000000` |  | `gamedll` `cheat` |  |
| `nav_split_show_line` | `Bool` | `false` |  | `gamedll` `cheat` | Show the free split line. |
| `nav_test_area_gravity` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_dist_0` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_dist_1` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_dist_2` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_hex` | `Bool` | `false` |  | `gamedll` `cheat` | Demonstrates searching hexagonal lattice over nav mesh. |
| `nav_test_bfs_lattice_mark` | `Float32` | `2.000000` |  | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_simple` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_spacing_0` | `Float32` | `24.000000` |  | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_spacing_1` | `Float32` | `48.000000` |  | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_spacing_2` | `Float32` | `96.000000` |  | `gamedll` `cheat` |  |
| `nav_test_bfs_simple` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_circle` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_force` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_grid_dim` | `Float32` | `90.000000` |  | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_path` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_rays` | `Float32` | `100.000000` |  | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_rays_margin` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_rays_random` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_sphere` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_test_curve_opt` | `Int32` | `0` |  | `gamedll` `cheat` |  |
| `nav_test_detour` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_find_nearest` | `Bool` | `false` |  | `gamedll` `cheat` | Calculate the nearest point on the navmesh to the trace point.  Uses selection from nav_select_hull. |
| `nav_test_find_nearest_clear` | `Bool` | `false` |  | `gamedll` `cheat` | Calculate the nearest point on the navmesh to the trace point.  Uses selection from nav_select_hull. |
| `nav_test_find_random_connected` | `Bool` | `false` |  | `gamedll` `cheat` | Demonstrates finding random points that are connected in the nav mesh to the start point. |
| `nav_test_find_random_connected_dist_max` | `Float32` | `1000.000000` |  | `gamedll` `cheat` |  |
| `nav_test_find_random_connected_dist_min` | `Float32` | `100.000000` |  | `gamedll` `cheat` |  |
| `nav_test_find_z` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_test_force_npc_repath` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_genrt` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_genrt_place` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_genrt_tile_removal_extent` | `Float32` | `50.000000` |  | `gamedll` `cheat` |  |
| `nav_test_genrt_tile_removal_place` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_getareaoverlapping_gravity` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_getnearestnav_gravity` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_multi_connection` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_npc_area` | `Int32` | `0` |  | `gamedll` `cheat` |  |
| `nav_test_npc_collision` | `Int32` | `0` |  | `gamedll` `cheat` |  |
| `nav_test_npc_collision_range` | `Float32` | `250.000000` |  | `gamedll` `cheat` |  |
| `nav_test_npc_collision_show_geometry` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_path` | `Bool` | `false` |  | `gamedll` `cheat` | Calculate and draw a path from player/camera position to the test position. |
| `nav_test_path_lock_goal` | `Bool` | `false` |  | `gamedll` `cheat` | Lock the pathfinding goal to the current intersection point. |
| `nav_test_path_lock_start` | `Bool` | `false` |  | `gamedll` `cheat` | Lock the pathfinding start to the current intersection point. |
| `nav_test_path_move` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_path_opt` | `Bool` | `true` |  | `gamedll` `cheat` | Enable path optimization for nav_edit_path paths. |
| `nav_test_path_opt_transitions` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_path_return` | `Bool` | `false` |  | `gamedll` `cheat` | Calculate a return path from cursor position to the path calculated by nav_test_path. |
| `nav_test_path_space` | `Int32` | `0` |  | `gamedll` `cheat` | Should nav_test_path test 3d navigation?  1 = space to space, 2 = multi-modal space/ground |
| `nav_test_path_space_fly` | `Bool` | `true` |  | `gamedll` `cheat` | Test flight paths |
| `nav_test_path_space_swim` | `Bool` | `true` |  | `gamedll` `cheat` | Test swim paths |
| `nav_test_pos_name` | `String` |  |  | `developmentonly` `gamedll` `defensive` |  |
| `nav_test_pos_place` | `Int32` | `-1` |  | `developmentonly` `gamedll` `defensive` |  |
| `nav_test_ray_space` | `Int32` | `0` |  | `gamedll` `cheat` |  |
| `nav_test_rays` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_rays_use_npc_move` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_search_on_path` | `Bool` | `false` |  | `gamedll` `cheat` | Test the 'on path' search mode for tactical searches. Requires a selected NPC with a current path. |
| `nav_test_search_on_path_boundary_edges_only` | `Bool` | `false` |  | `gamedll` `cheat` | Activate the 'boundary edges only' constraint when testing the 'on path' search mode for tactical searches. |
| `nav_test_search_on_path_setgoal` | `Bool` | `false` |  | `gamedll` `cheat` | Test the 'on path' search mode for tactical searches using SetGoal w/ possible path clipping (flips between 2 searches). Requires a selected NPC. |
| `nav_test_smooth` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_smooth_extern_push` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_test_smooth_in_speed` | `Float32` | `120.000000` |  | `gamedll` `cheat` |  |
| `nav_test_smooth_in_yaw` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `nav_test_smooth_path_speed` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `nav_test_smooth_separating_dist` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `nav_test_smooth_spring_const` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `nav_test_smooth_spring_tension_max` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `nav_test_spline` | `Int32` | `0` |  | `gamedll` `cheat` |  |
| `nav_test_split_obstacle` | `Int32` | `0` |  | `gamedll` `cheat` |  |
| `nav_test_split_obstacle_dirty` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_split_obstacle_leave` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `nav_test_split_obstacle_size` | `Float32` | `30.000000` |  | `gamedll` `cheat` |  |
| `nav_test_split_obstacle_update_pos` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `nav_volume_debug` | `Int32` | `0` |  | `gamedll` `cheat` | Draw or print debug information about nav volume queries. |
| `navspace_create_water_smooth_connections` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `navspace_create_water_transition_connections` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `navspace_debug_pathfind` | `Float32` | `-1.000000` |  | `gamedll` `cheat` |  |
| `navspace_debug_stringpull` | `Float32` | `1.000000` |  | `gamedll` `cheat` |  |
| `navspace_debug_trace` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `navspace_debug_transition_calc` | `Float32` | `0.000000` |  | `gamedll` `cheat` |  |
| `navspace_draw_changes_blocks` | `Float32` | `0.000000` |  | `gamedll` `cheat` | Draw blocks when they change |
| `navspace_draw_changes_waters` | `Float32` | `0.000000` |  | `gamedll` `cheat` | Draw water volumes when they change |
| `navspace_path_use_water_level_locator` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `net_async_clientconnect` | `Bool` | `true` |  | `developmentonly` `defensive` | Enable async client connect optimization |
| `net_async_job_random_sleep` | `Float32` | `0.000000` |  | `developmentonly` `defensive` | Sleep randomly 0..net_async_job_random_sleep ms in the parallel server jobs; sleep is per job |
| `net_client_steamdatagram_enable_override` | `Int32` | `0` |  | `clientdll` `release` | 0: Use connect method requested by GC.  &gt;0: Always use SDR if possible.  &lt;0: Always use direct UDP if possible |
| `net_debug_to_file` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `net_showeventlisteners` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | Show listening addition/removals |
| `net_showevents` | `Int32` | `0` |  | `developmentonly` `gamedll` `defensive` | Dump game events to console (1=client only, 2=all). |
| `nextlevel` | `String` |  |  | `gamedll` `notify` `release` | If set to a valid map name, will trigger a changelevel to the specified map at the end of the round |
| `nextmap_print_enabled` | `Bool` | `false` |  | `gamedll` `release` | When enabled prints next map to clients |
| `nextmode` | `String` |  |  | `gamedll` `notify` `replicated` `release` | Sets the game mode to be played when the next level loads |
| `noclip_fixup` | `Bool` | `true` |  | `gamedll` `cheat` |  |
| `npc_record_snapshot_data` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `npcsolve_attract_draw` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_constraint_nav` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_constraint_npc` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_drag_linear` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_forward` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_forward_const` | `Float32` | `30000.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_forward_dist` | `Float32` | `200.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_forward_margin` | `Float32` | `5.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_path_close_const` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_path_close_max_tension` | `Float32` | `100.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_path_lookahead_const` | `Float32` | `4.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_path_lookahead_dist` | `Float32` | `100.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_path_vel_const` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_separation` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_separation_const` | `Float32` | `10000.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_separation_dist` | `Float32` | `5.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_separation_draw` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_separation_jitter` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_separation_r2` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `option_duck_method` | `Bool` | `false` |  | `clientdll` `archive` `userinfo` `per_user` | Input toggle control |
| `option_speed_method` | `Bool` | `false` |  | `clientdll` `archive` `userinfo` `per_user` | Input toggle control |
| `opus_decode_test_signal` | `Bool` | `false` |  | `developmentonly` |  |
| `opus_encode_test_signal` | `Bool` | `false` |  | `developmentonly` |  |
| `opus_unittest_test_signal` | `Bool` | `false` |  | `developmentonly` |  |
| `panorama_2d_translate_no_comp_layer` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_alignment_fixes` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` | Fix alignment issues |
| `panorama_allow_texture_composition_layer_fast_path` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_allow_transitions` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_apply_styles_for_invisible_parents` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` | Specifies whether to short circuit applying styles when a parent is invisible. |
| `panorama_assert_loading_panel_type` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` | Force style invalidation of the entire panel subtree when adding / removing classes. |
| `panorama_async_compute_mipgen` | `Bool` | `true` |  | `developmentonly` `clientdll` | use asynchronous compute for mipmap generation. |
| `panorama_box_shadow_no_comp_layer` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_cache_command_list_repaint_threshold` | `Float32` | `0.250000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_cache_command_list_size_threshold` | `UInt32` | `384` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_classes_force_invalidate` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` | Force style invalidation of the entire panel subtree when adding / removing classes. |
| `panorama_clear_frames_on_device_restore` | `Int32` | `2` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_comp_layer_lru_lifetime` | `Float32` | `1.000000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_composition_atlas` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_console_max_autocomplete` | `Int32` | `100` |  | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `panorama_console_max_history` | `Int32` | `100` |  | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `panorama_console_max_lines` | `Int32` | `2000` |  | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `panorama_console_position_and_size` | `String` |  |  | `clientdll` `hidden` `archive` |  |
| `panorama_content_size_fixes` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` | Fix content size issues |
| `panorama_daisy_wheel` | `String` | `ABXY` |  | `developmentonly` `clientdll` `hidden` `defensive` | Daisy wheel input mode: RS \| ABXY |
| `panorama_dash_gap_ratio` | `Float32` | `0.500000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_dash_len` | `Float32` | `20.000000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_debug_movies` | `Bool` | `false` |  | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `panorama_debug_overlay_opacity` | `Float32` | `0.250000` |  | `hidden` `archive` |  |
| `panorama_debug_overlay_opacity_max` | `Float32` | `0.250000` |  | `hidden` `archive` |  |
| `panorama_debug_overlay_opacity_min` | `Float32` | `0.010000` |  | `hidden` `archive` |  |
| `panorama_debug_ready_for_display` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_debug_treat_all_addons_as_untrusted` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_debugger_theme` | `String` | `Light` |  | `clientdll` `archive` |  |
| `panorama_disable_blur` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_disable_box_shadow` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_disable_descendant_filtering` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` | Disable descendant selector filtering |
| `panorama_disable_draw_fancy_quad` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_disable_draw_text` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_disable_draw_text_shadow` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_disable_layer_cache` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_disable_layer_clear` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_disable_render_callbacks` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_disable_render_target_cache` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_disallow_hover_styles` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_dragscroll_affordance` | `Int32` | `20` |  | `developmentonly` `hidden` `defensive` | Minimum mouse movement in pixels before a move is treated as a drag scroll |
| `panorama_dragscroll_maxflickvelocity` | `Float32` | `8000.000000` |  | `developmentonly` `clientdll` `hidden` `defensive` | Maximum velocity for a drag scroll flick |
| `panorama_dragscroll_minflickvelocity` | `Float32` | `60.000000` |  | `developmentonly` `clientdll` `hidden` `defensive` | Minimum velocity that the mouse must be moving as mouse up time to qualify as a drag scroll flick |
| `panorama_dragscroll_mintime` | `Float32` | `0.020000` |  | `developmentonly` `hidden` `defensive` | Minimum time that the mouse button must be down before a move is treated as a drag scroll |
| `panorama_dragscroll_velocitymultiplier` | `Float32` | `0.500000` |  | `developmentonly` `hidden` `defensive` | Multiplier for flick velocity off of actual measured velocity |
| `panorama_draw_fast_path_img_shadow` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_draw_text_fast_path` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_draw_text_fast_path_text_shadow` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_enable_secondary_layout_pass` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_focus_world_panels` | `Bool` | `false` |  | `clientdll` `archive` | when set request key focus when a world panel is enabled |
| `panorama_force_active_controller_type` | `Int32` | `-1` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_force_desired_layout_traverse` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` | Force desired layout traverse, even if the cached values are up to date. |
| `panorama_highlight_bad_opacity_masks` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_highlight_composition_layers` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_highlight_slow_operations` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_hsbc_through_fast_path` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_joystick_axis_repeat_curve_time` | `Float32` | `1.000000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_joystick_axis_repeat_interval_end` | `Float32` | `0.050000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_joystick_axis_repeat_interval_start` | `Float32` | `0.220000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_joystick_button_repeat_curve_time` | `Float32` | `1.200000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_joystick_button_repeat_interval_end` | `Float32` | `0.100000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_joystick_button_repeat_interval_start` | `Float32` | `0.480000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_joystick_enabled` | `Bool` | `true` |  | `archive` | Enable panorama joystick input |
| `panorama_js_minidumps` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` | Enable sending minidumps on JS Exceptions. |
| `panorama_label_draw_rects` | `Int32` | `0` |  | `developmentonly` `clientdll` `hidden` `defensive` | When labels paint, draw the rectangles for the character ranges. 0 = none, 1 = all, 2 = text only, 3 = inline objects only |
| `panorama_label_wrap_before_shrink` | `Bool` | `true` |  | `developmentonly` `clientdll` `hidden` `defensive` | Should labels try to wrap text before using text-overflow: shrink |
| `panorama_large_dispatch_event_queue` | `Int32` | `0` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_max_text_shadow_strength` | `Float32` | `10.000000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_might_scroll_no_comp_layer` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_min_comp_layer_cache_cost` | `Int32` | `4096` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_movie_async_load_size_bytes` | `Int32` | `20971520` |  | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `panorama_movie_force_not_ready_behavior` | `Int32` | `-1` |  | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `panorama_panel_occlusion` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_print_render_tree` | `String` |  |  | `developmentonly` `hidden` `defensive` | Print the RenderOperation_t tree for the given root window; set to * to print all |
| `panorama_reload_animations` | `Int32` | `2` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_render_target_cache_max_size` | `Int32` | `31457280` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_script_cache_enabled` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` | Enable script caching to speed up recompiling scripts multiple times. |
| `panorama_show_fps` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `panorama_show_fps_scale` | `Float32` | `1.000000` |  | `developmentonly` `defensive` |  |
| `panorama_simple_borders_no_comp_layer` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_skip_composition_layer_content_paint` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_skip_composition_layer_content_paint_tint` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_spew_async_event_substring` | `String` |  |  | `developmentonly` `hidden` `defensive` | If non-empty, print debug info about async event queue and dispatch behavior for events containing the substring. |
| `panorama_spew_layout_invalidates` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_stats_log_time` | `Float32` | `0.000000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_streaming_load_local_images` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `panorama_style_flag_force_invalidate` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` | Force style invalidation of the entire panel subtree when adding / removing style flags. |
| `panorama_suspend_animation` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_suspend_paint` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_temp_comp_layer_min_dimension` | `Float32` | `512.000000` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_toggledebugger_mode` | `Int32` | `0` | `0 .. 1` | `hidden` `archive` | Toggledebugger key operation : 0 = open/inspect, 1 = open/close |
| `panorama_track_render_commands` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_transform_parents_no_layer_for_perspective` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_transforms_no_comp_layer` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_transition_time_factor` | `Float32` | `1.000000` |  | `developmentonly` `hidden` `defensive` | A float representing a scale factor for transitions. 1.0 is normal, 2.0 would be twice as fast as normal, 0.5 half as fast |
| `panorama_unlink_from_render_tree` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_use_backbuffer_directly` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_use_composite_cmd_for_cached_layers` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_use_new_occlusion_invalidation` | `Bool` | `true` |  | `developmentonly` `hidden` `defensive` |  |
| `panorama_worldpanel_update_cull_distance` | `Float32` | `1000.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `panorama_worldpanel_update_cull_size_threshold` | `Float32` | `5.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `panorama_worldpanel_update_culling` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `parallel_perform_invalidate_physics` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `parallel_update_surrounding_bounds_in_spatial_partition_update` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `particle_cluster_debug` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `particle_cluster_manager_search_dist` | `Float32` | `256.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `particle_cluster_nodraw` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `particle_cluster_use_collision_hulls` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `particle_debug_creation_filter` | `String` |  |  | `developmentonly` `clientdll` `hidden` `replicated` `defensive` |  |
| `particle_layer_id_whitelist` | `String` |  |  | `developmentonly` |  |
| `particle_powsimd_random_range_exp` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `particle_profile_filter` | `String` |  |  | `developmentonly` `defensive` | Profile particle filter |
| `particle_snapshot_allow_combined_models` | `Bool` | `false` |  | `developmentonly` |  |
| `particle_test_attach_attachment` | `Int32` | `0` |  | `gamedll` `cheat` | Attachment index for attachment mode |
| `particle_test_attach_mode` | `String` | `follow_attachment` |  | `gamedll` `cheat` | Possible Values: 'start_at_attachment', 'follow_attachment', 'start_at_origin', 'follow_origin' |
| `particle_test_file` | `String` |  |  | `gamedll` `cheat` | Name of the particle system to dynamically spawn |
| `partybrowser_throttle_data` | `Float32` | `0.150000` |  | `developmentonly` `clientdll` |  |
| `partybrowser_timeout` | `Float32` | `15.000000` |  | `developmentonly` `clientdll` |  |
| `password` | `String` |  |  | `archive` `dontrecord` `server_cannot_query` | Current server access password |
| `path_closest_point_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `path_node_evaluation_debug` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `pawn_mimic_all` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `phonemedelay` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` `defensive` | Phoneme delay to account for sound system latency. |
| `phonemefilter` | `Float32` | `0.080000` |  | `developmentonly` `clientdll` `defensive` | Time duration of box filter to pass over phonemes. |
| `phonemesnap` | `Int32` | `2` |  | `developmentonly` `clientdll` `defensive` | Lod at level at which visemes stops always considering two phonemes, regardless of duration. |
| `phys_batch_ray_test` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` |  |
| `phys_continuous_kinematic_update` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_cull_internal_mesh_contacts` | `Bool` | `false` |  | `developmentonly` `replicated` `defensive` |  |
| `phys_dynamic_scaling` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `phys_expensive_shape_threshold` | `Int32` | `6` |  | `clientdll` `cheat` |  |
| `phys_force_controller_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `phys_headshotscale` | `Float32` | `1.300000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Modifier for the headshot impulse hits on players |
| `phys_highlight_expensive_objects` | `Bool` | `false` |  | `cheat` | Highlight expensive physics objects |
| `phys_highlight_expensive_objects_strength` | `Float32` | `0.020000` |  | `cheat` | Highlight expensive physics objects strength |
| `phys_impactforcescale` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `phys_joint_teleport` | `Bool` | `true` |  | `gamedll` `cheat` | Teleport joint anchors if connected to world |
| `phys_length_damping_ratio` | `Float32` | `2.000000` |  | `gamedll` `cheat` | Spring damping ratio for length constraint |
| `phys_length_frequency` | `Float32` | `5.000000` |  | `gamedll` `cheat` | Spring stiffness for length constraint |
| `phys_log_updaters` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_log_updaters_exclude` | `String` | `weapon pistol rifle survivor common_male` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_log_updaters_include` | `String` | `limbs` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_min_motion_controller_count_to_run_in_job` | `Int32` | `8` |  | `developmentonly` `defensive` |  |
| `phys_multithreading_enabled` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Enable/Disable Multithreading in VPhysics |
| `phys_playerscale` | `Float32` | `10.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | This multiplies the bullet impact impuse on players for more dramatic results when players are shot. |
| `phys_powered_ragdoll_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_pushscale` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_shoot_angular_speed` | `Float32` | `3600.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `phys_shoot_speed` | `Float32` | `250.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `phys_show_stats` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_step_threaded` | `Bool` | `true` |  | `developmentonly` |  |
| `phys_stressbodyweights` | `Float32` | `5.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `phys_threaded_cloth_bone_update` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_threaded_kinematic_bone_update` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_threaded_transform_update` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_timescale` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `defensive` | Scale time for physics |
| `phys_upimpactforcescale` | `Float32` | `0.375000` |  | `developmentonly` `gamedll` `defensive` |  |
| `phys_use_block_solver` | `Bool` | `true` |  | `gamedll` `cheat` | Use block solving for constraint entities |
| `phys_vehicleimpactforcescale` | `Float32` | `1.500000` |  | `developmentonly` `gamedll` `defensive` |  |
| `phys_visualize_awake_dynamic_only` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_visualize_awake_unattached_only` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_wind_force_scale` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Scale on the force wind applies to physics bodies |
| `pickup_check_period` | `Float32` | `0.250000` |  | `developmentonly` `gamedll` `defensive` |  |
| `player0_using_joystick` | `Bool` | `false` |  | `archive` |  |
| `player_botdifflast_s` | `String` | `2` |  | `clientdll` `archive` `release` |  |
| `player_competitive_maplist_2v2_10_0_D684D4E1` | `String` | `mg_de_inferno,mg_de_nuke,mg_de_vertigo,mg_de_debris,mg_de_poseidon,mg_de_eldorado,mg_de_overpass` |  | `clientdll` `archive` |  |
| `player_competitive_maplist_8_10_0_A062AC6A` | `String` | `mg_de_dust2,mg_de_train,mg_de_ancient,mg_de_inferno,mg_de_nuke,mg_de_vertigo,mg_de_mirage,mg_cs_office,mg_cs_italy,mg_de_cache,mg_de_boulder,mg_de_anubis,mg_lobby_mapveto,mg_de_fachwerk,mg_cs_shelter,mg_de_overpass` |  | `clientdll` `archive` |  |
| `player_debug_off_nav` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `player_debug_print_damage` | `Bool` | `false` |  | `gamedll` `cheat` | When true, print amount and type of all damage received by player to console. |
| `player_nevershow_communityservermessage` | `String` | `0` |  | `clientdll` `archive` `per_user` |  |
| `player_ping_token_cooldown` | `Float32` | `20.000000` |  | `gamedll` `cheat` `release` | Cooldown for how long it takes for a player's ping token to refresh allowing them to ping again (they get 5 tokens). |
| `player_survival_list_10_0_303` | `String` | `mg_dz_blacksite,mg_dz_sirocco,mg_dz_vineyard,mg_dz_ember` |  | `clientdll` `archive` |  |
| `player_teamplayedlast` | `Int32` | `3` |  | `clientdll` `archive` `per_user` |  |
| `player_use_radius` | `Float32` | `80.000000` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `player_wargames_list2_10_0_0` | `String` |  |  | `clientdll` `archive` |  |
| `population_distribution_debug` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `pred_cloth_pos_max` | `Float32` | `2.000000` |  | `developmentonly` `clientdll` |  |
| `pred_cloth_pos_multiplier` | `Float32` | `0.500000` |  | `developmentonly` `clientdll` |  |
| `pred_cloth_pos_strength` | `Float32` | `0.250000` |  | `developmentonly` `clientdll` |  |
| `pred_cloth_rot_high` | `Float32` | `0.100000` |  | `developmentonly` `clientdll` |  |
| `pred_cloth_rot_low` | `Float32` | `0.010000` |  | `developmentonly` `clientdll` |  |
| `pred_cloth_rot_multiplier` | `Float32` | `0.300000` |  | `developmentonly` `clientdll` |  |
| `pred_cloth_smooth_motion` | `Int32` | `1` |  | `developmentonly` `clientdll` |  |
| `pred_cloth_vmax` | `Float32` | `2.000000` |  | `developmentonly` `clientdll` |  |
| `pred_cloth_vw` | `Float32` | `0.050000` |  | `developmentonly` `clientdll` |  |
| `presettle_cloth_iterations` | `Int32` | `30` |  | `developmentonly` `clientdll` `defensive` |  |
| `prop_debug_collision` | `Bool` | `false` |  | `gamedll` `cheat` | Highlights props based on their collision group: COLLISION_GROUP_PROPS(white), COLLISION_GROUP_INTERACTIVE_DEBRIS(green), COLLISION_GROUP_DEBRIS and will return to COLLISION_GROUP_INTERACTIVE_DEBRIS on sleeping(bright red), COLLISION_GROUP_DEBRIS permanently (dark red), COLLISION_GROUP_DEBRIS(blue), OTHER(grey) |
| `prop_nav_ignore_edge_len` | `Float32` | `-1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_ignore_mass` | `Float32` | `-1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_avoid_mass` | `Float32` | `100.099998` |  | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_avoid_use_connection_blocker` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_block_edge_min_` | `Float32` | `-1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_block_edge_min_a` | `Float32` | `-1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_block_edge_min_c` | `Float32` | `-1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_block_mass_a` | `Float32` | `-1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_block_mass_b` | `Float32` | `-1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_block_mass_c` | `Float32` | `-1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `props_break_apply_radial_forces` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `props_break_max_pieces_perframe` | `Int32` | `16` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Maximum prop breakable piece count per frame (-1 = model default) |
| `props_break_radial_force_ratio` | `Float32` | `0.330000` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `pulse_save_execution_history` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Keep a history of all instructions run on a per graph basis. |
| `pulse_save_execution_history_limit` | `Int32` | `10000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Keep a history of all instructions run on a per graph basis. |
| `pvs_debugentity` | `Int32` | `-1` |  | `gamedll` `release` | Verbose spew for this entity when doing IsInPVS computation. |
| `pvs_flowtype` | `Int32` | `0` |  | `gamedll` `release` | Flow through spawn groups for vis (0 == default, 1 == always visible, 2 == never visible. |
| `pwatchent` | `Int32` | `-1` |  | `clientdll` `cheat` | Entity to watch for prediction system changes. |
| `pwatchvar` | `String` |  |  | `clientdll` `cheat` | Entity variable to watch in prediction system for changes. |
| `r_AirboatViewDampenDamp` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `notify` `replicated` `cheat` |  |
| `r_AirboatViewDampenFreq` | `Float32` | `7.000000` |  | `gamedll` `clientdll` `notify` `replicated` `cheat` |  |
| `r_AirboatViewZHeight` | `Float32` | `0.000000` |  | `gamedll` `clientdll` `notify` `replicated` `cheat` |  |
| `r_JeepViewDampenDamp` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `notify` `replicated` `cheat` |  |
| `r_JeepViewDampenFreq` | `Float32` | `7.000000` |  | `gamedll` `clientdll` `notify` `replicated` `cheat` |  |
| `r_JeepViewZHeight` | `Float32` | `10.000000` |  | `gamedll` `clientdll` `notify` `replicated` `cheat` |  |
| `r_RainAllowInSplitScreen` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Allows rain in splitscreen |
| `r_RainParticleDensity` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `defensive` | Density of Particle Rain 0-1 |
| `r_add_views_in_pre_output` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_allow_low_gpu_memory_mode` | `Bool` | `true` |  | `release` | Allow Low GPU Memory mode (i.e. when building maps). |
| `r_allow_onesweep_gpusort` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_always_render_all_windows` | `Bool` | `false` |  | `developmentonly` `defensive` | Always force all engine &amp; tools to render |
| `r_aoproxy_cull_dist` | `Float32` | `12.000000` |  | `developmentonly` `defensive` | Distance to cull the AO proxy as a factor of size |
| `r_aoproxy_debug` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_aoproxy_default_ambient_strength` | `Float32` | `1.000000` |  | `developmentonly` `defensive` |  |
| `r_aoproxy_default_light_cone_angles` | `Vector4` | `0.300000 0.300000 0.300000 1.000000` |  | `developmentonly` `defensive` |  |
| `r_aoproxy_default_light_cone_strengths` | `Vector4` | `3.000000 8.000000 1.000000 4.000000` |  | `developmentonly` `defensive` |  |
| `r_aoproxy_default_light_position_0` | `Vector3` | `0.816497 0.000000 0.577350` |  | `developmentonly` `defensive` |  |
| `r_aoproxy_default_light_position_1` | `Vector3` | `-0.408248 0.707107 0.577350` |  | `developmentonly` `defensive` |  |
| `r_aoproxy_default_light_position_2` | `Vector3` | `-0.408248 -0.707107 0.577350` |  | `developmentonly` `defensive` |  |
| `r_aoproxy_default_light_position_3` | `Vector3` | `0.000000 0.000000 1.000000` |  | `developmentonly` `defensive` |  |
| `r_aoproxy_enable` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_aoproxy_min_dist` | `Float32` | `3.000000` |  | `developmentonly` `defensive` |  |
| `r_aoproxy_min_dist_box` | `Float32` | `1.000000` |  | `developmentonly` `defensive` |  |
| `r_aoproxy_show` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_aspectratio` | `Float32` | `0.000000` |  | `developmentonly` `defensive` |  |
| `r_async_shader_compile_notify_frequency` | `Int32` | `10` |  | `developmentonly` |  |
| `r_bloom_tent_filter_radius` | `Float32` | `3.100000` |  | `developmentonly` `clientdll` `cheat` | bloom mip up-sample filtering radius (using 3x3 tent filter, radius in mip level texels), 0.0 radius =&gt; box (2x2) filter with (fixed) 1.0 radius |
| `r_cache_pool_allocations` | `Bool` | `true` |  | `developmentonly` |  |
| `r_character_decal_monitor_draw_frustum` | `Bool` | `false` |  | `developmentonly` |  |
| `r_character_decal_monitor_emissive` | `Bool` | `false` |  | `developmentonly` |  |
| `r_character_decal_monitor_render_res` | `Int32` | `512` |  | `developmentonly` |  |
| `r_character_decal_renderdoc_capture` | `Bool` | `false` |  | `developmentonly` |  |
| `r_character_decal_resolution` | `Int32` | `1024` | `>= 256` | `developmentonly` `defensive` | Resolution of character decal texture. |
| `r_cs2_show_icon_editor` | `Bool` | `false` |  | `developmentonly` `clientdll` `replicated` `cheat` `menubar_item` | CSGO/Icon Editor |
| `r_csgo_bloom_threshold_all_samples` | `Bool` | `true` |  | `developmentonly` `clientdll` | Execute bloom threshold once per sample during downsample (default enabled, higher quality, less bloom aliasing) |
| `r_csgo_bloom_threshold_downsample_jimenez` | `Bool` | `true` |  | `developmentonly` `clientdll` | Custom downsample based on Jimenez14, (default enabled, higher quality, decreases bloom aliasing further) |
| `r_csgo_cable_pixel_radius_clamp` | `Float32` | `1.200000` |  | `developmentonly` `clientdll` | Minimum clamped size in pixels of a cable (if using F_CLAMP_MIN_RADIUS 1 in cable material) |
| `r_csgo_cmaa_debug_edges` | `Bool` | `false` |  | `developmentonly` `clientdll` | debug visualize edges |
| `r_csgo_cmaa_enable` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_csgo_cmaa_extra_sharp` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | trade more sharpness for reduced antialiasing |
| `r_csgo_cmaa_quality` | `Int32` | `3` |  | `developmentonly` `clientdll` `defensive` | 0=low, 1=medium, 2=high, 3=ultra |
| `r_csgo_csm_max_visible_distance` | `Float32` | `7500.000000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_csm_max_visible_distance_preview` | `Float32` | `2000.000000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_csm_override_staticgeo_cascades_alphatest` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | If lb_csm_override_staticgeo_cascades true, ensure objects with SCENEOBJECTFLAG_ALPHA_TESTED flag will be rendered into cascade. |
| `r_csgo_csm_pushback_distance` | `Float32` | `7000.000000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_csm_pushback_distance_preview` | `Float32` | `1500.000000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_cubemap_normalization` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_decal_debug` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_csgo_decals_use_msaa` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `r_csgo_depth_prepass` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_cull_threshold` | `Float32` | `60.000000` |  | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_skybox_alpha_tested` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_skybox_large` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_skybox_small` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_skybox_small_cull_threshold` | `Float32` | `5.000000` |  | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_small_cull_threshold` | `Float32` | `10.000000` |  | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_viewmodel` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_directional_lightmaps` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_effects_bloom` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_effects_bloom_when_smoked` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_csgo_enable_cubemap_fog` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `r_csgo_enable_glows` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_enable_gradient_fog` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `r_csgo_enable_high_precision_lighting` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_enable_sunlight_check` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` | Enable vis tests for sunlight. |
| `r_csgo_enable_tonemapping` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_enable_translucent_screen_space` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_enable_volume_fog` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `r_csgo_firstpersonlegs_nearz_offset` | `Float32` | `0.100000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_fsr_enable_mip_bias` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` | Apply negative mip bias when rendering with FSR. |
| `r_csgo_fsr_rcas_sharpness` | `Float32` | `0.250000` |  | `developmentonly` `clientdll` `defensive` | RCAS sharpness when using FSR + RCAS upsample. |
| `r_csgo_fsr_upsample` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` | 0 == bilinear upsampe, 1 == FSR upsample, 2 == FSR + RCAS upsample |
| `r_csgo_gpu_culling` | `Bool` | `true` |  | `developmentonly` `clientdll` `menubar_item` `defensive` | CSGO/Graphics/GPU Culling |
| `r_csgo_gpu_culling_camera_offset` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_gpu_culling_shadows` | `Bool` | `false` |  | `developmentonly` `clientdll` `menubar_item` `defensive` | CSGO/Graphics/GPU Cull Shadow Views |
| `r_csgo_gpu_culling_shadows_min_cascade` | `Int32` | `1` |  | `developmentonly` `clientdll` | If r_csgo_gpu_culling_shadows is true, this defines min cascade for which gpu culling is used |
| `r_csgo_gpu_culling_two_pass` | `Bool` | `false` |  | `developmentonly` `clientdll` `menubar_item` `defensive` | CSGO/Graphics/GPU Culling (Two Pass) |
| `r_csgo_gpu_debug_draw` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `r_csgo_gpu_opt_downsample_depth_using_resolved_depth` | `Bool` | `true` |  | `developmentonly` `clientdll` | use already resolved depth as input to downsample depth layer |
| `r_csgo_gpu_opt_firstpersonlegs_visible_angle` | `Float32` | `40.000000` |  | `developmentonly` `clientdll` | avoid overhead of firstpersonlegs layers if not looking down enough to see them |
| `r_csgo_gpu_opt_prepass_characters` | `Bool` | `true` |  | `developmentonly` `clientdll` | only depth prepass nearby characters (see r_csgo_gpu_opt_prepass_characters_cull_threshold to control threshold) |
| `r_csgo_gpu_opt_prepass_characters_cull_threshold` | `Float32` | `15.000000` |  | `developmentonly` `clientdll` | use with r_csgo_gpu_opt_prepass_characters |
| `r_csgo_gpu_opt_resolve_depth_for_decals_on_translucent` | `Bool` | `true` |  | `developmentonly` `clientdll` | optimize layers for decals on translucent geo, avoid one resolve and some fullscreen passes |
| `r_csgo_gpu_opt_resolve_depth_no_characters` | `Bool` | `true` |  | `developmentonly` `clientdll` | remove unused resolve |
| `r_csgo_gpu_opt_use_aoproxy_depth_for_depth_pyramid` | `Bool` | `true` |  | `developmentonly` `clientdll` | if ao proxies enabled, use ao proxy downsampled depth as input to generate the depth pyramid for gpu culling |
| `r_csgo_gpu_opt_viewmodel_stencil` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `r_csgo_gpu_opt_water_refraction_resolve` | `Bool` | `true` |  | `developmentonly` `clientdll` | copy already resolved depth for use by waterrefraction layers, instead of resolving main depth again (avoids msaa samples) |
| `r_csgo_gpu_optimizations` | `Bool` | `true` |  | `developmentonly` `clientdll` | temporary cvar to control new GPU optimzations (depth resolves, etc) |
| `r_csgo_joint_upscale_sigma` | `Float32` | `0.002000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_max_barnlight_shadow_scale_preview` | `Float32` | `4.000000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_mboit` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_mboit_bias` | `Float32` | `0.000005` |  | `clientdll` `cheat` |  |
| `r_csgo_mboit_debug` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_csgo_mboit_force_mixed_resolution` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_csgo_mboit_overestimation` | `Float32` | `0.010000` |  | `clientdll` `cheat` |  |
| `r_csgo_mboit_upscale_cs` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_csgo_mboit_use_4_moments` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_csgo_merge_resolve_with_histogram` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_microshadowing` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_csgo_mixed_resolution_color_slices` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_csgo_mixed_resolution_particles` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_csgo_mixed_resolution_particles_minmax` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_csgo_mixed_resolution_particles_scale` | `Int32` | `2` |  | `clientdll` `cheat` |  |
| `r_csgo_mouse_trace_coord` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_msaa_resolve_apply_exposure_scale` | `Bool` | `true` |  | `developmentonly` `clientdll` | 0 - before, 1 - after fix for a2c fringing |
| `r_csgo_multiscattering` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_csgo_no_shader_resolve` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_csgo_opaquerefract_viewmodel_depthcopy` | `Bool` | `false` |  | `developmentonly` `clientdll` | Copy depth in viewmodel for opaquerefract |
| `r_csgo_opaquerefract_viewmodel_quality` | `Int32` | `1` |  | `developmentonly` `clientdll` | Opaque refract quality in viewmodel: 0 = no background copy, no depth, 1= background copy, depth if enabled |
| `r_csgo_outline_glow_scaledenom` | `Int32` | `1` |  | `developmentonly` `clientdll` `cheat` |  |
| `r_csgo_player_occlusion_query` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `r_csgo_player_occlusion_query_debug` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `r_csgo_postprocess_enable` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_r11g11b10_dither_mode` | `Int32` | `2` |  | `developmentonly` `clientdll` | 0 - disabled, 1 - regular dither noise, 2 - blue noise dither |
| `r_csgo_readonly_depth_stencil_enable` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_reconstruct_normals` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_csgo_reconstruct_normals_method` | `Int32` | `0` |  | `clientdll` `cheat` |  |
| `r_csgo_render_decals` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_render_decals_on_translucent` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_render_dither_scale` | `Float32` | `1.000000` |  | `clientdll` `cheat` |  |
| `r_csgo_render_dynamic_objects` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_render_inferno_decals` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_render_opaque` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_render_overlays` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_render_post_bloom` | `Int32` | `1` |  | `clientdll` `cheat` |  |
| `r_csgo_render_post_bloom_strength` | `Float32` | `-1.000000` |  | `clientdll` `cheat` |  |
| `r_csgo_render_post_colorcorrection` | `Int32` | `0` |  | `clientdll` `cheat` |  |
| `r_csgo_render_post_film_grain` | `Int32` | `0` |  | `clientdll` `cheat` |  |
| `r_csgo_render_post_fxaa` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_csgo_render_post_local_contrast` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_render_post_mirror_horizontal` | `Int32` | `0` |  | `clientdll` `cheat` |  |
| `r_csgo_render_post_mirror_vertical` | `Int32` | `0` |  | `clientdll` `cheat` |  |
| `r_csgo_render_translucent` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_resolve_dither_bluenoise_amount` | `Float32` | `4.000000` |  | `developmentonly` `clientdll` | Equivalent to r_csgo_render_dither_scale, but purely to control bluenoise for R11G11B10 downsample dither (if r_csgo_r11g11b10_dither_mode = 2) |
| `r_csgo_resolve_dither_noise_amount` | `Float32` | `0.200000` |  | `developmentonly` `clientdll` | Amount of screen space dither noise to apply during resolve (used/essential with R11G11B10_FLOAT RT) |
| `r_csgo_shader_feature_test_value` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_shader_perf_test` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `r_csgo_shadow_map_allocation_failure_policy` | `Int32` | `1` |  | `developmentonly` `clientdll` `cheat` | What happens when a shadow map fails allocation? 0 = don't render, 1 = render unshadowed |
| `r_csgo_shadows_debug` | `Int32` | `0` |  | `clientdll` `cheat` |  |
| `r_csgo_smoke_avoid_flat` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `r_csgo_smoke_clip_sniper` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `r_csgo_smoke_fullres_enhance` | `Bool` | `false` |  | `developmentonly` `clientdll` | Enhance edges of smokes to eliminate bad pixels |
| `r_csgo_smoke_fullres_pass` | `Bool` | `true` |  | `developmentonly` `clientdll` | Does a full res pass to cover holes and artifacts in smoke low res |
| `r_csgo_smoke_overlay_min_dt` | `Float32` | `0.015686` |  | `developmentonly` `clientdll` |  |
| `r_csgo_smoke_shadow` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `r_csgo_smoke_upscale_discard_pixels_behind` | `Bool` | `false` |  | `developmentonly` `clientdll` | When upsampling smoke discard pixels behind solid depth to avoid pixelated artifacts |
| `r_csgo_stencil_sniper_zoom` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `r_csgo_test1` | `Bool` | `false` |  | `clientdll` `release` |  |
| `r_csgo_tools_vis_cubemap_roughness` | `Float32` | `0.000100` |  | `developmentonly` `clientdll` `cheat` |  |
| `r_csgo_upscale_depth_threshold` | `Float32` | `3.000000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_use_compute_bloom` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `r_csgo_viewmodel_csm_pushback_distance` | `Float32` | `1500.000000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_viewmodel_envmap_position_bias` | `Float32` | `0.850000` |  | `developmentonly` `clientdll` `cheat` |  |
| `r_csgo_viewmodel_far_plane` | `Float32` | `100.000000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_viewmodel_near_plane` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` |  |
| `r_csgo_viewmodel_probe_clamp_plane_distance` | `Float32` | `16.000000` |  | `developmentonly` `clientdll` `cheat` |  |
| `r_csgo_volume_mboit_optimization` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_water_effects` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_water_refraction` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_csgo_water_skybox_depth` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `r_cubemap_debug_colors` | `Int32` | `0` |  | `cheat` |  |
| `r_dashboard_render_quality` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_debug_depth_holes` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_debug_draw_safe_area_insets` | `Bool` | `false` |  | `developmentonly` | Render safe area insets as wireframe. |
| `r_debug_particle_shadows` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_debug_precipitation` | `Bool` | `false` |  | `clientdll` `cheat` | Show precipitation volumes |
| `r_decal_hit_confirmation` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `r_decals` | `Int32` | `2048` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_decals_additional_offset` | `Float32` | `0.010000` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `r_decals_default_fade_duration` | `Float32` | `3.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_decals_default_start_fade` | `Float32` | `30.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_decals_max_on_deformables` | `Int32` | `512` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_decals_overide_fadestarttime_params` | `Float32` | `-1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `commandline_enforced` `defensive` |  |
| `r_decals_overlap_threshold` | `Int32` | `6` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_depth_of_field` | `Int32` | `1` |  | `developmentonly` `clientdll` | 0 = off, 1 = enabled (high quality, circular bokeh, HDR) |
| `r_directional_lightmaps` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_directlighting` | `Bool` | `true` |  | `cheat` | Set to use direct lighting |
| `r_dlss_preset` | `Int32` | `5` |  | `developmentonly` `defensive` |  |
| `r_dof2_maxblursize` | `Float32` | `5.000000` |  | `developmentonly` `clientdll` |  |
| `r_dof2_radiusscale` | `Float32` | `0.250000` |  | `developmentonly` `clientdll` |  |
| `r_dof_override` | `Bool` | `false` |  | `cheat` |  |
| `r_dof_override_far_blurry` | `Float32` | `2000.000000` |  | `cheat` |  |
| `r_dof_override_far_crisp` | `Float32` | `180.000000` |  | `cheat` |  |
| `r_dof_override_near_blurry` | `Float32` | `-100.000000` |  | `cheat` |  |
| `r_dof_override_near_crisp` | `Float32` | `0.000000` |  | `cheat` |  |
| `r_dof_override_tilt_to_ground` | `Float32` | `0.500000` |  | `cheat` |  |
| `r_dopixelvisibility` | `Bool` | `true` |  | `cheat` |  |
| `r_draw3dskybox` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_draw_first_tri_only` | `Bool` | `false` |  | `cheat` |  |
| `r_draw_instances` | `Bool` | `true` |  | `cheat` |  |
| `r_draw_overlays` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_draw_particle_children_with_parents` | `Int32` | `-1` |  | `cheat` | Draw particle children with parents (-1=use gameinfo, 0=no, 1=yes) |
| `r_drawblankworld` | `Bool` | `false` |  | `cheat` | Render blank instead of the game world |
| `r_drawchickens` | `Bool` | `true` |  | `clientdll` `cheat` | Render chickens |
| `r_drawcsplayers` | `Bool` | `true` |  | `clientdll` `cheat` | Render CS players |
| `r_drawdecals` | `Bool` | `true` |  | `cheat` | Set to render decals |
| `r_drawdevvisualizers` | `Bool` | `false` |  | `clientdll` `cheat` | Render dev visualizers |
| `r_drawpanorama` | `Bool` | `true` |  | `cheat` | Enable the rendering of panorama UI |
| `r_drawparticles` | `Bool` | `true` |  | `cheat` `menubar_item` | SceneSystem/Particles/Draw Particles |
| `r_drawpixelvisibility` | `Bool` | `false` |  | `developmentonly` `defensive` | Show the occlusion proxies |
| `r_drawropes` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_drawskybox` | `Bool` | `true` |  | `cheat` | Render the 2d skybox. |
| `r_drawtracers` | `Bool` | `true` |  | `clientdll` `cheat` |  |
| `r_drawtracers_firstperson` | `Bool` | `true` |  | `clientdll` `archive` `release` | Toggle visibility of first person weapon tracers |
| `r_drawviewmodel` | `Bool` | `true` |  | `clientdll` `cheat` | Render view model |
| `r_drawworld` | `Bool` | `true` |  | `cheat` | Render the world. |
| `r_dx11_debug_clean` | `Bool` | `false` |  | `release` | Aggressively unbind bound resources to cleanup DX11 debug warnings. |
| `r_dx11_software_cmd_lists` | `Bool` | `true` |  | `developmentonly` `defensive` | Enable Software Command lists for DX11 (Avoid using deferred contexts) |
| `r_enable_rigid_animation` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `r_experimental_lag_limiter` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `r_extra_render_frames` | `Int32` | `0` |  | `cheat` |  |
| `r_fallback_texture_lod_scale` | `Float32` | `2.000000` |  | `cheat` | Scale factor for requested texture size (texture streaming) - used for geo that doesn't have a precomputed UV density measure |
| `r_farz` | `Float32` | `-1.000000` |  | `clientdll` `cheat` | Override the far clipping plane. -1 means to use the value in env_fog_controller. |
| `r_flashlightambient` | `Float32` | `0.000000` |  | `clientdll` `cheat` |  |
| `r_flashlightbacktraceoffset` | `Float32` | `0.400000` |  | `clientdll` `cheat` |  |
| `r_flashlightbrightness` | `Float32` | `1.000000` |  | `clientdll` `replicated` `cheat` |  |
| `r_flashlightconstant` | `Float32` | `0.000000` |  | `clientdll` `replicated` `cheat` |  |
| `r_flashlightfar` | `Float32` | `1500.000000` |  | `clientdll` `replicated` `cheat` |  |
| `r_flashlightfov` | `Float32` | `53.000000` |  | `clientdll` `replicated` `cheat` |  |
| `r_flashlightladderdist` | `Float32` | `40.000000` |  | `clientdll` `cheat` |  |
| `r_flashlightlinear` | `Float32` | `100.000000` |  | `clientdll` `replicated` `cheat` |  |
| `r_flashlightlockposition` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_flashlightmuzzleflashfov` | `Float32` | `120.000000` |  | `clientdll` `cheat` |  |
| `r_flashlightnear` | `Float32` | `4.000000` |  | `clientdll` `replicated` `cheat` |  |
| `r_flashlightnearoffsetscale` | `Float32` | `1.000000` |  | `clientdll` `cheat` |  |
| `r_flashlightoffsetforward` | `Float32` | `0.000000` |  | `clientdll` `replicated` `cheat` |  |
| `r_flashlightoffsetright` | `Float32` | `5.000000` |  | `clientdll` `replicated` `cheat` |  |
| `r_flashlightoffsetup` | `Float32` | `-5.000000` |  | `clientdll` `replicated` `cheat` |  |
| `r_flashlightquadratic` | `Float32` | `0.000000` |  | `clientdll` `replicated` `cheat` |  |
| `r_flashlightshadowatten` | `Float32` | `0.350000` |  | `clientdll` `cheat` |  |
| `r_flashlighttracedistcutoff` | `Float32` | `128.000000` |  | `clientdll` `cheat` |  |
| `r_flashlighttracedistwatercutoff` | `Float32` | `80.000000` |  | `clientdll` `cheat` |  |
| `r_flashlightvisualizetrace` | `Bool` | `false` |  | `clientdll` `cheat` |  |
| `r_force_no_present` | `Bool` | `false` |  | `cheat` | Force the render device to not present frames. |
| `r_force_render_frame_count` | `Int32` | `5` |  | `developmentonly` | The number of frames to render when a |
| `r_force_thick_hair` | `Bool` | `false` |  | `developmentonly` `cheat` |  |
| `r_frame_sync_enable` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_freeze_sceneobjects` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_freezeparticles` | `Bool` | `false` |  | `cheat` | Pause particle simulation |
| `r_fullscreen_gamma` | `Float32` | `2.200000` | `1.000000 .. 4.000000` | `archive` | Screen Gamma (only in fullscreen modes) |
| `r_fullscreen_quad_single_triangle` | `Bool` | `true` |  | `developmentonly` |  |
| `r_gpu_debug_draw_freeze` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `r_grass_allow_flattening` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `r_grass_alpha_test` | `Int32` | `0` |  | `developmentonly` `defensive` |  |
| `r_grass_density_mode` | `Int32` | `0` |  | `developmentonly` `defensive` | 0 = Density corresponds to blade existance, 1 = Density corresponds to blade height, 2 = Both 0 and 1 |
| `r_grass_end_fade` | `Float32` | `3000.000000` |  | `developmentonly` `defensive` |  |
| `r_grass_max_brightness_change` | `Float32` | `75.000000` |  | `developmentonly` `defensive` |  |
| `r_grass_quality` | `Int32` | `2` |  | `developmentonly` `defensive` | 0 = Off, 1 = Low, 2 = Med, 3 = high, 4 = ultra |
| `r_grass_start_fade` | `Float32` | `2000.000000` |  | `developmentonly` `defensive` |  |
| `r_grass_vertex_lighting` | `Int32` | `0` |  | `developmentonly` `defensive` |  |
| `r_hair_ao` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_hair_debug_guides` | `Int32` | `0` |  | `developmentonly` `cheat` | 1: Highlight guide hairs, 2: draw only guide hairs |
| `r_hair_indirect_transmittance` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_hair_meshshader` | `Int32` | `0` |  | `developmentonly` `defensive` |  |
| `r_hair_shadowtile` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_hair_voxels` | `Int32` | `-1` |  | `developmentonly` `cheat` |  |
| `r_hair_wind_global_scale` | `Float32` | `0.300000` |  | `developmentonly` `defensive` |  |
| `r_hair_wind_min_noise_speed` | `Float32` | `20.000000` |  | `developmentonly` `defensive` |  |
| `r_hair_wind_motion_scale` | `Float32` | `0.070000` |  | `developmentonly` `defensive` |  |
| `r_hair_wind_noise` | `Float32` | `0.200000` |  | `developmentonly` `defensive` |  |
| `r_hair_wind_noise_occlusion` | `Float32` | `1.000000` |  | `developmentonly` `defensive` |  |
| `r_hair_wind_noise_size` | `Float32` | `10.000000` |  | `developmentonly` `defensive` |  |
| `r_hair_wind_occlusion` | `Float32` | `2.000000` |  | `developmentonly` `defensive` |  |
| `r_haircull_percent` | `Float32` | `-1.000000` |  | `developmentonly` `cheat` |  |
| `r_hairsort` | `Bool` | `true` |  | `developmentonly` `cheat` |  |
| `r_icon_csm_pushback_distance` | `Float32` | `-1.000000` |  | `developmentonly` `clientdll` `cheat` | csm pushback distance, should be much shorter/disabled for icon rendering |
| `r_icon_custommaterial_maxres` | `Int32` | `512` |  | `developmentonly` `clientdll` `cheat` | maxres for custommaterials when rendering icons |
| `r_icon_generate_offline_mips` | `Bool` | `false` |  | `developmentonly` `clientdll` `cheat` | generate mips via sidecar file for offline |
| `r_icon_generate_runtime_mips` | `Bool` | `true` |  | `developmentonly` `clientdll` `cheat` | generate mips for runtime |
| `r_icon_highcontrast_postprocessing_weight` | `Float32` | `0.375000` | `0.000000 .. 1.000000` | `developmentonly` `clientdll` `cheat` | if using high contrast postprocessing, use this weight (weight = 1.0 for characters) |
| `r_icon_image_cache_to_disk` | `Bool` | `true` |  | `clientdll` `archive` `release` | 1 |
| `r_icon_max_mip_width` | `Int32` | `128` |  | `developmentonly` `clientdll` `cheat` | r_icon_max_mip_width |
| `r_icon_player_equip_gloves_from_loadout` | `Bool` | `false` |  | `developmentonly` `clientdll` `cheat` | equip gloves on player for icon rendering from loadout, or use default gloves |
| `r_icon_rendering_height` | `Int32` | `384` |  | `developmentonly` `clientdll` `hidden` `cheat` | icon rendering height |
| `r_icon_rendering_width` | `Int32` | `512` |  | `developmentonly` `clientdll` `hidden` `cheat` | icon rendering width |
| `r_icon_show_timing` | `Bool` | `false` |  | `developmentonly` `clientdll` `cheat` | show timing in output |
| `r_icon_use_kv3_camera` | `Bool` | `false` |  | `developmentonly` `clientdll` `cheat` | use test kv3 data for camera |
| `r_impact_ricochet_chance` | `Float32` | `0.300000` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_impacts_alt_orientation` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_impacts_decal_grazing_incidence_cutoff` | `Float32` | `0.550000` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_impacts_decal_grazing_incidence_variance` | `Float32` | `0.100000` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_indirectlighting` | `Bool` | `true` |  | `cheat` | Set to use indirect lighting |
| `r_late_particle_job_sync` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_legacy_vsync` | `Bool` | `false` |  | `developmentonly` `hidden` `defensive` | Use legacy vsync mode -- for testing for a couple user machines. |
| `r_light_flickering_enabled` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_light_probe_volume_debug_colors` | `Bool` | `false` |  | `cheat` |  |
| `r_light_probe_volume_debug_grid` | `Int32` | `0` |  | `cheat` | Show LPV debug grid, 0: off, 1: closest only 2: closest and keep 3: all |
| `r_light_probe_volume_debug_grid_albedo` | `Color` | `128 128 128` |  | `cheat` | albedo for LPV debug grid |
| `r_light_probe_volume_debug_grid_bbox` | `Bool` | `true` |  | `cheat` | Show LPV bounding box when debug grid is on, 0: off, 1: on |
| `r_light_probe_volume_debug_grid_metalness` | `Float32` | `0.000000` |  | `cheat` | metalness for LPV debug grid |
| `r_light_probe_volume_debug_grid_prim` | `Int32` | `0` |  | `cheat` | 0: spheres, 1: cubes |
| `r_light_probe_volume_debug_grid_roughness` | `Float32` | `0.500000` |  | `cheat` | roughness for LPV debug grid |
| `r_light_probe_volume_debug_grid_samplesize` | `Float32` | `4.000000` |  | `cheat` | sphere radius (world) for LPV debug grid |
| `r_lightmap_set` | `String` | `lightmaps` |  | `cheat` | Lightmap set to use, only works on map load |
| `r_lightmap_size` | `Int32` | `65536` |  | `developmentonly` `defensive` | Maximum lightmap resolution. |
| `r_lightmap_size_directional_irradiance` | `Int32` | `-1` |  | `developmentonly` `defensive` | Maximum lightmap resolution for directional_irradiance channel. -1 = use value of r_lightmap_size |
| `r_limit_particle_job_duration` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `r_low_latency` | `Int32` | `1` |  | `developmentonly` `defensive` | NVIDIA Low Latency/AMD Anti-Lag 2 (0 = off, 1 = on, 2 = NV-only, on + boost) |
| `r_low_latency_trigger_flash` | `Bool` | `true` |  | `developmentonly` `defensive` | NVIDIA Low Latency Trigger Flash |
| `r_mapextents` | `Float32` | `16384.000000` |  | `clientdll` `cheat` | Set the max dimension for the map.  This determines the far clipping plane |
| `r_max_texture_pool_size` | `Int32` | `0` |  | `developmentonly` `defensive` | Upper limit on texture pool size. |
| `r_memory_aliasing` | `Bool` | `true` |  | `developmentonly` | Allow disabling memory aliasing in the device memory pool.  This is just intended for testing/ruling out aliasing issues. |
| `r_mipgen_compute_shader` | `Bool` | `true` |  | `developmentonly` `defensive` | Use compute shader for mipgen. |
| `r_mixed_shadows_fade_in_time` | `Float32` | `0.500000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_mixed_shadows_fade_out_time` | `Float32` | `0.500000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_monitor_3dskybox` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_morphing_enabled` | `Bool` | `true` |  | `cheat` |  |
| `r_multigpu_num_gpus_found` | `Int32` | `1` |  | `developmentonly` `defensive` |  |
| `r_multigpu_num_gpus_used` | `Int32` | `1` |  | `developmentonly` `defensive` |  |
| `r_muzzleflashbrightness` | `Float32` | `0.400000` |  | `clientdll` `replicated` `cheat` |  |
| `r_muzzleflashlinear` | `Float32` | `0.050000` |  | `clientdll` `replicated` `cheat` |  |
| `r_nearz` | `Float32` | `-1.000000` |  | `clientdll` `cheat` | Override the near clipping plane. -1 means use the default. |
| `r_particle_allowprerender` | `Bool` | `true` |  | `developmentonly` |  |
| `r_particle_batch_collections` | `Bool` | `false` |  | `developmentonly` |  |
| `r_particle_batch_in_fullsort` | `Bool` | `false` |  | `developmentonly` |  |
| `r_particle_cables_cast_shadows` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_particle_cables_culling` | `Int32` | `1` |  | `developmentonly` `defensive` |  |
| `r_particle_cables_culling_bounds_scale` | `Float32` | `1.200000` |  | `developmentonly` `defensive` |  |
| `r_particle_cables_dynamic_roundness` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `r_particle_cables_dynamic_roundness_threshold` | `Int32` | `20` |  | `developmentonly` `defensive` |  |
| `r_particle_cables_render` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_particle_cables_render_meshlets` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_particle_cables_visualize_roundness` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `r_particle_debug_filter` | `String` |  |  | `developmentonly` `defensive` | Limit debug visualizations to substring match of effect name |
| `r_particle_debug_force_simulation` | `Int32` | `0` |  | `developmentonly` `defensive` | -1 for all asleep, 1 for all awake |
| `r_particle_debug_randomseeds` | `Bool` | `false` |  | `developmentonly` `defensive` | Use random seeds in debug |
| `r_particle_debug_show_attribute` | `Int32` | `-1` |  | `developmentonly` | Show specific attribute when debugging particle systems |
| `r_particle_debug_show_control_points` | `Bool` | `false` |  | `developmentonly` | Show all used controlpoints |
| `r_particle_debug_show_rope_segments` | `Int32` | `0` |  | `developmentonly` | Show rope segments when debugging particle systems - specify a number to isolate to that segment id |
| `r_particle_debug_show_sort_position` | `Bool` | `false` |  | `developmentonly` | Show the sorting position when debugging particle systems |
| `r_particle_enable_fastpath` | `Bool` | `true` |  | `developmentonly` |  |
| `r_particle_explicit_fetch` | `Bool` | `false` |  | `developmentonly` |  |
| `r_particle_fixedrandomseeds` | `Bool` | `false` |  | `developmentonly` | Use fixed seeds for easier debugging |
| `r_particle_gpu_implicit` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_particle_gpu_implicit_cull_columns` | `Bool` | `true` |  | `developmentonly` |  |
| `r_particle_gpu_implicit_debug_bricks` | `Bool` | `false` |  | `developmentonly` |  |
| `r_particle_gpu_implicit_debug_stats` | `Bool` | `false` |  | `developmentonly` |  |
| `r_particle_gpu_implicit_debug_wireframe` | `Bool` | `false` |  | `developmentonly` |  |
| `r_particle_gpu_implicit_lds_cache` | `Bool` | `false` |  | `developmentonly` |  |
| `r_particle_max_detail_level` | `Int32` | `3` |  | `developmentonly` `defensive` | The maximum detail level of particle to create |
| `r_particle_max_draw_distance` | `Float32` | `1000000.000000` |  | `cheat` | The maximum distance that particles will render |
| `r_particle_max_size_cull` | `Float32` | `1200.000000` |  | `developmentonly` `defensive` | Particle systems larger than this in every dimension skip culling to save CPU.  They will be drawn anyway. |
| `r_particle_max_texture_layers` | `Int32` | `-1` |  | `developmentonly` `defensive` |  |
| `r_particle_min_timestep` | `Float32` | `0.000000` |  | `developmentonly` `defensive` | A minimum on particle simulation time, particle simulation happening more frequently than this will lerp. |
| `r_particle_mixed_resolution_viewstart` | `Float32` | `500.000000` |  | `developmentonly` |  |
| `r_particle_model_new` | `Bool` | `false` |  | `developmentonly` |  |
| `r_particle_model_new8` | `Bool` | `true` |  | `developmentonly` |  |
| `r_particle_model_per_thread_count` | `Int32` | `32` |  | `developmentonly` |  |
| `r_particle_multiplier` | `Int32` | `1` |  | `cheat` | Render each particle system N times for perf testing |
| `r_particle_newinput` | `Bool` | `false` |  | `developmentonly` | Enable input path in particle ops |
| `r_particle_render_refreshes_sleep_timer` | `Bool` | `true` |  | `developmentonly` | Disable to get a better look at what's happening offscreen |
| `r_particle_render_sprites_issue_vizquery` | `Bool` | `true` |  | `developmentonly` |  |
| `r_particle_render_test` | `Bool` | `false` |  | `developmentonly` `defensive` | render particles 100 times and show perf |
| `r_particle_shadow_map_texture_size` | `Int32` | `1536` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_particle_shadows` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_particle_shadows_cast_on_particles` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_particle_shadows_cast_on_particles_scale` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_particle_shadows_cast_on_world` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_particle_shadows_compute` | `Bool` | `true` |  | `clientdll` `release` |  |
| `r_particle_skip_postsim` | `Bool` | `false` |  | `developmentonly` |  |
| `r_particle_testbuffers` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `r_particle_timescale` | `Float32` | `1.000000` |  | `developmentonly` `defensive` |  |
| `r_particle_warn_threshold_ms` | `Float32` | `0.000000` |  | `developmentonly` `defensive` | Threshold to warn about when rendering particles. |
| `r_particles_memset_at_init` | `Int32` | `1` |  | `developmentonly` | 0=don't clear particle attrs at init 1=clear to zero 2=clear to 0xdb -1=clear to zero at first sim |
| `r_physics_particle_op_spawn_scale` | `Float32` | `1.000000` |  | `developmentonly` |  |
| `r_pipeline_stats_command_flush` | `Bool` | `false` |  | `developmentonly` `defensive` | Experimental: Set to 1 to enable full GPU pipeline flushing after each command list. |
| `r_pipeline_stats_flush_before_sleeping` | `Bool` | `false` |  | `developmentonly` `defensive` | Experimental: Set to 1 to enable GPU pipeline flushes right before the render thread sleeps to wait for more work. |
| `r_pipeline_stats_present_flush` | `Bool` | `false` |  | `developmentonly` `defensive` | Experimental: Set to 1 to enable full GPU pipeline flushing after each present. |
| `r_pipeline_stats_use_flush_api` | `Bool` | `true` |  | `developmentonly` `defensive` | Experimental: Set to 1 to use the ID3D11DeviceContext11::Flush() to flush the GPU pipeline instead of queries. |
| `r_pixelvisibility_partial` | `Bool` | `true` |  | `cheat` |  |
| `r_pixelvisibility_spew` | `Bool` | `false` |  | `cheat` |  |
| `r_player_fog_distance_multiplier` | `Float32` | `1.700000` |  | `developmentonly` `clientdll` `cheat` |  |
| `r_player_fog_maxdensity_multiplier` | `Float32` | `0.600000` |  | `developmentonly` `clientdll` `cheat` |  |
| `r_player_visibility_mode` | `Int32` | `1` |  | `clientdll` `archive` `release` |  |
| `r_player_visibility_stencil` | `Bool` | `true` |  | `developmentonly` `clientdll` `cheat` |  |
| `r_player_visibility_strength` | `Float32` | `1.100000` |  | `developmentonly` `clientdll` `cheat` |  |
| `r_post_bloom_debug` | `Int32` | `0` |  | `developmentonly` `clientdll` | 1 = bloom output (before thresholding), 2 = quarter res downsample, 3 = quarter res effects bloom 4 = quarter res effects raw |
| `r_prefer_loop_unrolling` | `Bool` | `true` |  | `developmentonly` `defensive` | Prefer shader loop unrolling. |
| `r_propsmaxdist` | `Float32` | `1200.000000` |  | `developmentonly` `clientdll` `defensive` | Maximum visible distance |
| `r_render_hair` | `Bool` | `true` |  | `developmentonly` `cheat` |  |
| `r_render_to_cubemap_begin_mixing_roughness` | `Float32` | `0.250000` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_render_to_cubemap_debug` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_render_world_node_bounds` | `Bool` | `false` |  | `cheat` | Render world node bounds |
| `r_renderdoc_auto_shader_pdbs` | `Bool` | `true` |  | `developmentonly` `defensive` | Automatically generate shader debug info on capture |
| `r_renderdoc_open_captures` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_renderdoc_validation_error_capture_limit` | `Int32` | `5` |  | `developmentonly` `defensive` |  |
| `r_rendersun` | `Bool` | `true` |  | `cheat` | Render sun lighting |
| `r_replay_post_effect` | `Int32` | `-1` |  | `clientdll` `cheat` |  |
| `r_reset_character_decals` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `r_ropetranslucent` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_screen_size_expansion` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_shadows` | `Bool` | `true` |  | `cheat` |  |
| `r_shadowtile_waveops` | `Bool` | `false` |  | `reference` |  |
| `r_show_build_info` | `Bool` | `true` |  | `clientdll` `archive` `release` | Build information. Leave this enabled when submitting bug screenshots and videos, please! |
| `r_show_gpu_memory_visualizer` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/Vulkan GPU Memory Visualizer |
| `r_show_time_info` | `Bool` | `false` |  | `clientdll` `release` | Show real time, large. |
| `r_showdebugoverlays` | `Bool` | `false` |  | `cheat` | Set to render debug overlays |
| `r_showsceneobjectbounds` | `Bool` | `false` |  | `cheat` | Show scenesystem object bounding boxes |
| `r_size_cull_threshold` | `Float32` | `0.800000` |  | `developmentonly` | Threshold of screen size percentage below which objects get culled |
| `r_size_cull_threshold_fade` | `Float32` | `0.000000` |  | `developmentonly` | % above the screen size percentage where we will start fading out (==0 will disable fading). |
| `r_size_cull_threshold_shadow` | `Float32` | `0.200000` |  | `cheat` | Threshold of shadow map size percentage below which objects get culled |
| `r_skinning_enabled` | `Bool` | `true` |  | `cheat` |  |
| `r_skip_precache_validation_check` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `r_smooth_morph_normals` | `Bool` | `true` |  | `release` |  |
| `r_spectator_flashbang_opacity` | `Float32` | `0.600000` | `0.200000 .. 1.000000` | `clientdll` `archive` | Spectator flash opacity |
| `r_ssao` | `Bool` | `true` |  | `developmentonly` `defensive` | Set to use screen-space ambient occlusion |
| `r_ssao_bias` | `Float32` | `0.500000` |  | `developmentonly` `defensive` |  |
| `r_ssao_blur` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_ssao_radius` | `Float32` | `30.000000` |  | `developmentonly` `defensive` |  |
| `r_ssao_strength` | `Float32` | `1.200000` |  | `developmentonly` `defensive` |  |
| `r_strip_invisible_during_sceneobject_update` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_test1_maximum_wait_ms` | `Float32` | `10.000000` |  | `clientdll` `release` |  |
| `r_texture_budget_dynamic` | `Bool` | `true` |  | `developmentonly` `defensive` | Dynamically adjust texture streaming budget based on GPU memory usage. |
| `r_texture_budget_threshold` | `Float32` | `0.900000` |  | `developmentonly` `defensive` | Reduce texture memory pool size when this percentage of the budget is full. |
| `r_texture_budget_update_period` | `Float32` | `0.100000` |  | `developmentonly` `defensive` | Time (in seconds) between updating texture memory budget. |
| `r_texture_eager_eviction` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `r_texture_hookup_uses_threadpool` | `Bool` | `true` |  | `developmentonly` `defensive` | Async Texture hookup uses its own threadpool instead of the global pool. |
| `r_texture_lod_scale` | `Float32` | `1.000000` |  | `cheat` | Scale factor for requested texture size (texture streaming) |
| `r_texture_nonstreaming_load` | `Bool` | `true` |  | `developmentonly` `defensive` | Allow immediately loading mips of textures (when possible) when their headers are loaded, saving IO &amp; reducing latency. |
| `r_texture_pool_increase_rate` | `Float32` | `64.000000` |  | `developmentonly` `defensive` | Increase texture memory pool size by this many MB / s when under budget. |
| `r_texture_pool_reduce_rate` | `Float32` | `256.000000` |  | `developmentonly` `defensive` | Reduce texture memory pool size by this many MB / s when over budget. |
| `r_texture_pool_size` | `Int32` | `1600` |  | `developmentonly` `defensive` | Total size of the texture pool in MB |
| `r_texture_stream_max_resolution` | `Int32` | `2147483647` | `>= 512` | `developmentonly` `defensive` | Maximum resolution for top mip level in streaming textures |
| `r_texture_stream_mip_bias` | `Int32` | `0` |  | `developmentonly` `defensive` | Biases the mip level the texture streaming system choses to stream for each texture. |
| `r_texture_stream_resolution_bias_decrease_rate` | `Float32` | `0.100000` |  | `developmentonly` `defensive` |  |
| `r_texture_stream_resolution_bias_increase_rate` | `Float32` | `0.050000` |  | `developmentonly` `defensive` |  |
| `r_texture_stream_resolution_bias_min` | `Float32` | `1.000000` |  | `developmentonly` `defensive` |  |
| `r_texture_stream_resolution_bias_update_period` | `Float32` | `0.500000` |  | `developmentonly` `defensive` |  |
| `r_texture_stream_throttle_amount` | `Float32` | `10.000000` |  | `developmentonly` `defensive` |  |
| `r_texture_stream_throttle_count` | `Int32` | `3` |  | `developmentonly` `defensive` |  |
| `r_texture_stream_throttle_count_over_budget` | `Int32` | `1` |  | `developmentonly` `defensive` |  |
| `r_texture_streaming_timesliced` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_texture_streamout_unthrottle_ms` | `Float32` | `0.200000` |  | `developmentonly` `defensive` | After hitting throttling limits for streamout, allow it to continue up to this number of milliseconds. |
| `r_texturefilteringquality` | `Int32` | `1` |  | `developmentonly` `defensive` | 0: Bilinear, 1: Trilinear, 2: Aniso 2x, 3: Aniso 4x, 4: Aniso 8x, 5: Aniso 16x |
| `r_threaded_particle_creation` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_threaded_particles` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `r_threaded_scene_object_update` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_timestamp_query_multiplier` | `Float32` | `1.000000` |  | `developmentonly` `defensive` | Set the TIMESTAMP query cycle multiplier, for drivers that lie |
| `r_translucent` | `Bool` | `true` |  | `cheat` | Enable rendering of translucent geometry |
| `r_ui_update_parallel_with_server` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `r_update_particles_on_render_only_frames` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `r_use_memory_budget_model` | `Bool` | `false` |  | `developmentonly` `defensive` | Use a model of GPU memory use to determine budget rather than querying the OS. |
| `r_validate_texture_streaming` | `Bool` | `false` |  | `developmentonly` `defensive` | Dumps state of texture streaming at the next frame boundary. |
| `r_vconsole_foregroundforcerender` | `Bool` | `true` |  | `developmentonly` `defensive` | When VConsole is in the foreground, force all engine &amp; tools to render |
| `r_vma_defrag_algorithm` | `Int32` | `1` |  | `developmentonly` | Defrag algorithm 0=Fast 1=Balanced 2=full 3=Extensive |
| `r_vma_defrag_enabled` | `Bool` | `true` |  | `developmentonly` |  |
| `r_vma_defrag_max_allocation_count_per_pass` | `Int32` | `256` |  | `developmentonly` | During a VMA defrag, number of moves per pass. |
| `r_vma_defrag_max_allocation_size_per_pass` | `Int32` | `32` |  | `developmentonly` | During a VMA defrag, number of MB in moves per pass. |
| `r_vma_defrag_moves_per_frame` | `Int32` | `20` |  | `developmentonly` | During a VMA defrag, number of moves to process for a pass in a single frame update. |
| `r_vma_defrag_threshold_mb` | `Int32` | `256` |  | `release` |  |
| `r_vulkan_force_sync1` | `Bool` | `false` |  | `developmentonly` |  |
| `r_vulkan_sw_cmd_lists` | `Bool` | `true` |  | `release` | Enable Software Command lists for Vulkan |
| `r_vulkan_validation_filter_in` | `String` |  |  | `developmentonly` | Comma delimited list of stristr filters for including validation messages.  Only messages matching filter will be included. |
| `r_vulkan_validation_filter_out` | `String` |  |  | `developmentonly` | Comma delimited list of stristr filters for excluding validation messages.  Any messages matching filter will be excluded. |
| `r_wait_on_present` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `r_world_frame_load_threshold_ms` | `Float32` | `10.000000` |  | `developmentonly` `defensive` |  |
| `r_world_wind_dir` | `Vector3` | `0.707000 0.707000 0.000000` |  | `developmentonly` `defensive` |  |
| `r_world_wind_frequency_grass` | `Float32` | `0.030000` |  | `developmentonly` `defensive` |  |
| `r_world_wind_frequency_trees` | `Float32` | `0.003000` |  | `developmentonly` `defensive` |  |
| `r_world_wind_offset_speed` | `Vector3` | `0.250000 0.300000 0.200000` |  | `developmentonly` `defensive` |  |
| `r_world_wind_smooth_time` | `Float32` | `2.000000` |  | `developmentonly` `defensive` |  |
| `r_world_wind_strength` | `Float32` | `40.000000` |  | `developmentonly` `defensive` |  |
| `radarvisdistance` | `Float32` | `1000.000000` | `>= 10.000000` | `gamedll` `cheat` | at this distance and beyond you need to be point right at someone to see them |
| `radarvismaxdot` | `Float32` | `0.996000` | `0.000000 .. 1.000000` | `gamedll` `cheat` | how closely you have to point at someone to see them beyond max distance |
| `radarvismethod` | `Int32` | `1` | `0 .. 1` | `gamedll` `cheat` | 0 for traditional method, 1 for more realistic method |
| `radarvispow` | `Float32` | `0.400000` |  | `gamedll` `cheat` | the degree to which you can point away from a target, and still see them on radar. |
| `ragdoll_debug_item_detachment` | `Bool` | `false` |  | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `ragdoll_fixup_joint_limits` | `Bool` | `true` |  | `developmentonly` `gamedll` `replicated` | Adjusts bone transforms so that physics joints don't appear violated (limits) |
| `ragdoll_fixup_joint_limits_max_height` | `Int32` | `1` |  | `developmentonly` `gamedll` `replicated` | Disable ragdoll_fixup_joint_limits on joints too high in the hierarchy because long chains tend to depend on violating limits |
| `ragdoll_fixup_joint_orientation` | `Bool` | `true` |  | `developmentonly` `gamedll` `replicated` | Adjusts bone transforms so that physics joints don't appear violated (orientation) |
| `ragdoll_fixup_joint_orientation_max_height` | `Int32` | `10` |  | `developmentonly` `gamedll` `replicated` | Disable ragdoll_fixup_joint_orientation on joints too high in the hierarchy because small differences can massively accumulate (e.g. long chains) |
| `ragdoll_fixup_joint_translation` | `Bool` | `true` |  | `developmentonly` `gamedll` `replicated` | Adjusts bone transforms so that physics joints don't appear violated (translation) |
| `ragdoll_friction_scale` | `Float32` | `0.600000` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_gravity_scale` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_impact_strength` | `Float32` | `500.000000` |  | `developmentonly` `clientdll` `defensive` |  |
| `ragdoll_lru_debug_removal` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_lru_min_age` | `Float32` | `10.000000` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_move_entity` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_override_root_orientation` | `Bool` | `true` |  | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `ragdoll_parallel_pose_control` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `ragdoll_prop_settle` | `Bool` | `true` |  | `developmentonly` `gamedll` `replicated` `defensive` | Enable more aggressive ragdoll settling |
| `ragdoll_prop_sleepaftertime` | `Float32` | `4.000000` |  | `developmentonly` `gamedll` `replicated` `defensive` | After this many seconds of being basically stationary, the ragdoll will go to sleep. |
| `ragdoll_prop_sleepdisabletime` | `Float32` | `1.500000` |  | `developmentonly` `gamedll` `replicated` `defensive` | Ragdoll is not allowed to physically sleep until this timer has elapsed. |
| `ragdoll_resolve_initial_conflict` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_resolve_separation` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_scale_sleep_tolerance` | `Bool` | `true` |  | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `ragdoll_update_from_weights` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_visualize_creation_skeleton` | `Bool` | `false` |  | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `ragdoll_vphysics_scale` | `Float32` | `0.500000` |  | `developmentonly` `gamedll` `replicated` `defensive` | How much we scale physics impacts against the ragdoll. |
| `rate` | `Int32` | `80000` |  | `archive` `userinfo` | Min bytes/sec the host can receive data |
| `rcon_address` | `String` |  |  | `dontrecord` `release` `server_cannot_query` | Address of remote server if sending unconnected rcon commands (format x.x.x.x:p) |
| `rcon_connected_clients_allow` | `Bool` | `true` |  | `replicated` `release` | Allow clients to use rcon commands on server. |
| `rcon_password` | `String` |  |  | `dontrecord` `release` `server_cannot_query` | remote console password. |
| `recast_mark_overhang` | `Bool` | `false` |  | `gamedll` `replicated` `cheat` | Enable/disable overhang detection |
| `recast_partitioning` | `Int32` | `0` |  | `gamedll` `replicated` `cheat` | 0 = watershed, 1 = monotone, 2 = layers |
| `replay_debug` | `Int32` | `0` |  | `replicated` `release` |  |
| `report_cliententitysim` | `Bool` | `false` |  | `clientdll` `cheat` | List all clientside simulations and time - will report and turn itself off. |
| `report_clientthinklist` | `Bool` | `false` |  | `clientdll` `cheat` | List all clientside entities thinking and time - will report and turn itself off. |
| `report_connection_failure_percentage` | `Float32` | `0.000000` |  | `developmentonly` `defensive` |  |
| `reset_voice_on_input_stallout` | `Bool` | `false` |  | `userinfo` | If true, resets the input device when there was a long enough hitch between callbacks. |
| `rope_averagelight` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` | Makes ropes use average of cubemap lighting instead of max intensity. |
| `rope_collide` | `Int32` | `1` |  | `developmentonly` `clientdll` `defensive` | Collide rope with the world |
| `rope_shake` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `rope_smooth_enlarge` | `Float32` | `1.400000` |  | `developmentonly` `clientdll` `defensive` | How much to enlarge ropes in screen space for antialiasing effect |
| `rope_smooth_maxalpha` | `Float32` | `0.500000` |  | `developmentonly` `clientdll` `defensive` | Alpha for rope antialiasing effect |
| `rope_smooth_maxalphawidth` | `Float32` | `1.750000` |  | `developmentonly` `clientdll` `defensive` |  |
| `rope_smooth_minalpha` | `Float32` | `0.200000` |  | `developmentonly` `clientdll` `defensive` | Alpha for rope antialiasing effect |
| `rope_smooth_minwidth` | `Float32` | `0.300000` |  | `developmentonly` `clientdll` `defensive` | When using smoothing, this is the min screenspace width it lets a rope shrink to |
| `rope_subdiv` | `Int32` | `2` | `0 .. 8` | `developmentonly` `clientdll` `defensive` | Rope subdivision amount |
| `rope_wind_dist` | `Float32` | `1000.000000` |  | `developmentonly` `clientdll` `defensive` | Don't use CPU applying small wind gusts to ropes when they're past this distance. |
| `rr_debugclassname` | `String` |  |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | If set, rr_debugclassname will print only response tests where 'classname' corresponds to this variable. Use to filter for a specific character. |
| `rr_debugresponseconcept` | `String` |  |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | If set, rr_debugresponseconcept will print only responses testing for the specified concept |
| `rr_debugresponses` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Show verbose matching output (1 for simple, 2 for rule scoring, 3 for noisy). If set to 4, it will only show response success/failure for npc_selected NPCs. |
| `rr_debugrule` | `String` |  |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | If set to the name of the rule, that rule's score will be shown whenever a concept is passed into the response rules system. |
| `rr_followup_maxdist` | `Float32` | `1800.000000` |  | `gamedll` `cheat` | 'then ANY' or 'then ALL' response followups will be dispatched only to characters within this distance. |
| `rr_thenany_score_slop` | `Float32` | `0.000000` |  | `gamedll` `archive` `cheat` | When computing respondents for a 'THEN ANY' rule, all rule-matching scores within this much of the best score will be considered. |
| `rtx_allow_blas_compact` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `rtx_allow_blas_create` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `rtx_dynamic_blas` | `Bool` | `true` |  | `developmentonly` `defensive` | Allow dynamic BLAS creation for geometry going through the compute shader skinning path. |
| `rtx_dynamic_blas_caching` | `Bool` | `true` |  | `developmentonly` `defensive` | Cache dynamic BLAS if geometry has not changed |
| `rtx_force_default_hitgroup` | `Bool` | `false` |  | `developmentonly` `defensive` | Forces all ray traced geometry to use default hit shaders instead of specialized ones. |
| `rtx_texture_resolution` | `UInt32` | `512` | `64 .. 2048` | `developmentonly` `defensive` | Sets the texture resolution the raytracer will mark to stream in |
| `run_voicecontainer_async` | `Bool` | `false` |  | `developmentonly` |  |
| `safezonex` | `Float32` | `1.000000` | `0.000000 .. 1.000000` | `clientdll` `archive` | The percentage of the screen width that is considered safe from overscan. Cannot result in a width less than the height. |
| `safezoney` | `Float32` | `1.000000` | `0.800000 .. 1.000000` | `clientdll` `archive` | The percentage of the screen height that is considered safe from overscan |
| `save_async` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `save_debug_snapshots` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Save/Load debug snapshot data |
| `save_fake_hitch` | `Int32` | `0` |  | `developmentonly` `gamedll` `defensive` | Force a busy wait for the specified number of milliseconds during save to simulate a hitch |
| `save_history_count` | `Int32` | `1` |  | `developmentonly` `gamedll` `defensive` | Keep this many old copies in history of autosaves and quicksaves. |
| `save_maxarray_spew` | `Int32` | `10` |  | `gamedll` `release` | Max number of array entries to spew when using SaveRestoreIO spewing. |
| `save_parallel` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `save_screenshot` | `Int32` | `2` |  | `developmentonly` `gamedll` `defensive` | 0 = none, 1 = non-autosave, 2 = always, 3 = bug_only |
| `save_spew` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `save_write_kv3` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Write the KV3 entity data as a text file in the save directory |
| `saving_enabled` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sc_aggregate_bvh` | `Bool` | `true` |  | `developmentonly` |  |
| `sc_aggregate_bvh_threshold` | `UInt32` | `128` |  | `developmentonly` |  |
| `sc_aggregate_debug_draw_meshlets` | `UInt32` | `0` |  | `developmentonly` `menubar_item` | SceneSystem/Aggregates/Visualize Meshlets |
| `sc_aggregate_debug_draw_meshlets_bounds` | `Bool` | `false` |  | `developmentonly` | Visualize meshlet bounds and cone axis. Mesh shader only. |
| `sc_aggregate_debug_visualizer` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/Aggregates/Debug Visualizer |
| `sc_aggregate_fragment_merging` | `Bool` | `true` |  | `developmentonly` |  |
| `sc_aggregate_gpu_culling` | `Bool` | `true` |  | `developmentonly` `defensive` | Toggles GPU culling of aggregate meshes |
| `sc_aggregate_gpu_culling_conservative_bounds` | `Bool` | `false` |  | `developmentonly` |  |
| `sc_aggregate_gpu_culling_show_culled` | `Bool` | `false` |  | `developmentonly` `menubar_item` | SceneSystem/Aggregates/Show GPU Culled Meshes |
| `sc_aggregate_gpu_occlusion_culling` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sc_aggregate_indirect_draw_compaction` | `Bool` | `true` |  | `release` | Use multidrawindirect...count if the driver/hardware supports it |
| `sc_aggregate_indirect_draw_compaction_threshold` | `UInt32` | `8` | `>= 1` | `release` | Threshold of indirect draws when we will do compaction |
| `sc_aggregate_instance_streams` | `Bool` | `true` |  | `developmentonly` | Enable instance streams |
| `sc_aggregate_material_solo` | `String` |  |  | `developmentonly` `cheat` |  |
| `sc_aggregate_render_mesh_shader` | `Bool` | `true` |  | `developmentonly` | Using mesh shaders if available instead of drawcalls |
| `sc_aggregate_rtproxy_debug_visualizer` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/Aggregates/RT Proxy Debug Visualizer |
| `sc_aggregate_rtproxy_instanced_geo` | `Bool` | `true` |  | `developmentonly` `cheat` |  |
| `sc_aggregate_rtproxy_unique_geo` | `Bool` | `true` |  | `developmentonly` `cheat` |  |
| `sc_aggregate_rtproxy_visualize` | `Bool` | `false` |  | `developmentonly` `cheat` |  |
| `sc_aggregate_show_outside_vis` | `Bool` | `false` |  | `developmentonly` |  |
| `sc_allow_dithered_lod` | `Bool` | `true` |  | `developmentonly` `defensive` | Allow use of dithered lod transitions |
| `sc_allow_dynamic_constant_batching` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sc_allow_precomputed_vismembers` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sc_allow_write_depth_before_blend` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sc_barnlight_enable_precomputed_vis` | `Bool` | `true` |  | `developmentonly` `defensive` | Enable use of precomputed vis membership for lights (requires map restart) |
| `sc_batch_layer_cb_updates` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sc_cache_envmap_lpv_lookup` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sc_clutter_density_full_size` | `Float32` | `0.007500` |  | `developmentonly` `defensive` | Screen-size where clutter will be full density |
| `sc_clutter_density_none_size` | `Float32` | `0.003500` |  | `developmentonly` `defensive` | Screen-size where clutter will be gone |
| `sc_clutter_desity_override` | `Bool` | `false` |  | `developmentonly` |  |
| `sc_clutter_enable` | `Bool` | `true` |  | `developmentonly` `menubar_item` | SceneSystem/Clutter/Draw Clutter |
| `sc_disableThreading` | `Bool` | `false` |  | `cheat` |  |
| `sc_disable_baked_lighting` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `sc_disable_culling_boxes` | `Bool` | `false` |  | `cheat` |  |
| `sc_disable_procedural_layer_rendering` | `Bool` | `false` |  | `cheat` |  |
| `sc_disable_shadow_fastpath` | `Bool` | `false` |  | `cheat` |  |
| `sc_disable_spotlight_shadows` | `Bool` | `false` |  | `cheat` |  |
| `sc_disable_world_materials` | `Bool` | `false` |  | `cheat` |  |
| `sc_distancefield_visualize_atlas` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `sc_dithered_lod_transition_amt` | `Float32` | `0.075000` | `0.000000 .. 0.200000` | `developmentonly` `defensive` | Percentage of the transition between two lods we will apply a dither |
| `sc_draw_aggregate_meshes` | `Bool` | `true` |  | `developmentonly` `menubar_item` | SceneSystem/Aggregates/Draw Aggregates |
| `sc_dump_lists` | `String` |  |  | `cheat` |  |
| `sc_enable_discard` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sc_extended_stats` | `Bool` | `false` |  | `cheat` |  |
| `sc_fade_distance_scale_override` | `Float32` | `-1.000000` |  | `cheat` |  |
| `sc_force_lod_level` | `Int32` | `-1` |  | `cheat` |  |
| `sc_force_materials_batchable` | `Bool` | `false` |  | `cheat` |  |
| `sc_force_single_display_list_per_layer` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `sc_force_translation_in_projection` | `Bool` | `false` |  | `cheat` | If enabled, the camera's translation will be included in the projection matrix. |
| `sc_hdr_enabled_override` | `Int32` | `-1` |  | `developmentonly` `performing_callbacks` `defensive` | Override default setting for HDR rendering. -1 default, 0 NoHdr, 1 Hdr, 2 Hdr 1010102 3 Hdr 111110 |
| `sc_imgui_show_debug_log` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/Imgui/Show Debug Log |
| `sc_imgui_show_id_stack` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/Imgui/Show ID Stack Tool |
| `sc_imgui_show_metrics` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/Imgui/Show Metrics |
| `sc_instanced_debug_visualizer` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/Instanced/Debug Visualizer |
| `sc_instanced_gpu_culling_show_culled` | `Bool` | `false` |  | `developmentonly` `menubar_item` | SceneSystem/Instanced/Show GPU Culled Meshlets |
| `sc_instanced_material_solo` | `String` |  |  | `developmentonly` `cheat` |  |
| `sc_instanced_mesh_enable` | `Bool` | `true` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/Instanced/Draw Instanced |
| `sc_instanced_mesh_gpu_culling` | `Bool` | `true` |  | `developmentonly` `defensive` | Toggles GPU culling of instanced meshes |
| `sc_instanced_mesh_gpu_density_culling` | `Bool` | `true` |  | `developmentonly` `defensive` | Toggles density culling (if enabled) |
| `sc_instanced_mesh_gpu_occlusion_culling` | `Bool` | `true` |  | `developmentonly` `defensive` | Toggles GPU occlusion of instanced meshes |
| `sc_instanced_mesh_gpu_vis_culling` | `Bool` | `true` |  | `developmentonly` `defensive` | Toggles GPU vis of instanced meshes |
| `sc_instanced_mesh_lod_bias` | `Float32` | `1.250000` |  | `developmentonly` `defensive` | Bias for LOD selection of instanced meshes |
| `sc_instanced_mesh_lod_bias_shadow` | `Float32` | `1.750000` |  | `developmentonly` `defensive` | Bias for LOD selection of instanced meshes in shadowmaps |
| `sc_instanced_mesh_motion_vectors` | `Bool` | `true` |  | `developmentonly` `defensive` | Toggles motion vector support for instanced meshes |
| `sc_instanced_mesh_opaque_fade` | `Bool` | `true` |  | `developmentonly` `defensive` | Toggles fade support for instanced meshes |
| `sc_instanced_mesh_size_cull_bias` | `Float32` | `1.500000` |  | `developmentonly` `defensive` | Bias for size culling of instanced meshes |
| `sc_instanced_mesh_size_cull_bias_shadow` | `Float32` | `2.000000` |  | `developmentonly` `defensive` | Bias for size culling instanced meshes in shadowmaps |
| `sc_instanced_mesh_solo` | `String` |  |  | `developmentonly` `cheat` |  |
| `sc_keep_all_layers` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `sc_layer_batch_threshold` | `Int32` | `128` |  | `developmentonly` `defensive` |  |
| `sc_layer_batch_threshold_fullsort` | `Int32` | `80` |  | `developmentonly` `defensive` |  |
| `sc_max_framebuffer_copies_per_layer` | `Int32` | `1` |  | `developmentonly` `defensive` |  |
| `sc_mesh_backface_culling` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sc_mesh_gpu_occlusion_culling` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sc_mesh_gpu_volume_culling` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sc_mesh_mesh_shaders` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `sc_mesh_shadows_batch_across_materials` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sc_mesh_use_pmb` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `sc_no_cull` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `sc_no_vis` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `sc_only_render_opaque` | `Bool` | `false` |  | `cheat` |  |
| `sc_only_render_shadowcasters` | `Bool` | `false` |  | `cheat` |  |
| `sc_particle_debug_visualizer` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/Particles/Debug Visualizer |
| `sc_reject_all_objects` | `Bool` | `false` |  | `cheat` |  |
| `sc_rendergraph_debug_visualizer` | `Bool` | `false` |  | `developmentonly` `menubar_item` | SceneSystem/RenderGraph Visualizer |
| `sc_screen_size_lod_scale_override` | `Float32` | `-1.000000` |  | `cheat` |  |
| `sc_shadow_depth_bias` | `Int32` | `256` |  | `developmentonly` `defensive` |  |
| `sc_shadow_depth_bias_clamp` | `Float32` | `0.000000` |  | `developmentonly` `defensive` |  |
| `sc_shadow_depth_bias_state_override` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `sc_shadow_slopescale_depth_bias` | `Float32` | `2.130000` |  | `developmentonly` `defensive` |  |
| `sc_show_cs_skinning_stats` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/Compute Skinning Stats |
| `sc_show_gpu_profiler` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/GPU Profiler |
| `sc_show_hair_debug_ui` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/Hair Debug UI |
| `sc_show_object_browser` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/SceneObject Browser |
| `sc_show_texture_visualizer` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/Texture Visualizer |
| `sc_show_view_profiler` | `Bool` | `false` |  | `developmentonly` `cheat` `menubar_item` | SceneSystem/View Profiler |
| `sc_skip_traversal` | `Bool` | `false` |  | `cheat` |  |
| `sc_spew_cmt_usage` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `sc_throw_away_all_layers` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `sc_use_clear_subrect` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `sc_view_profiler_frame_averaging` | `Int32` | `10` |  | `developmentonly` `defensive` |  |
| `sc_visualize_batches` | `Int32` | `0` |  | `developmentonly` `defensive` | color per batch |
| `sc_visualize_sceneobjects` | `String` | `SCENEOBJECT_VIS_NONE` |  | `developmentonly` `menubar_item` `defensive` | SceneSystem/Visualize SceneObject Mode |
| `sc_visualize_sceneobjects_meshlets` | `String` | `SCENEOBJECT_MESHLET_VIS_NONE` |  | `developmentonly` `menubar_item` | SceneSystem/Visualize Base SceneObject Meshlets |
| `scene_clientflex` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Do client side flex animation. |
| `scene_print` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | When playing back a scene, print timing and event info to console. |
| `scene_vcdautosave` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Create a savegame before VCD playback |
| `screenmessage_notifytime` | `Float32` | `8.000000` |  | `developmentonly` `gamedll` `defensive` | How long to display screen message text |
| `screenmessage_show` | `Int32` | `-1` |  | `cheat` | Enable display of console messages on screen. 1 = Enabled, 0 = Disabled, -1 = Enabled if vgui is not present |
| `screenshot_height` | `Int32` | `-1` |  | `developmentonly` `defensive` | Screenshot height. -1 for screen height. |
| `screenshot_prefix` | `String` | `shot` |  | `developmentonly` `defensive` | Set the screenshot auto naming prefix. |
| `screenshot_subdir` | `String` | `screenshots` |  | `developmentonly` `defensive` | Set the screenshot directory. |
| `screenshot_width` | `Int32` | `-1` |  | `developmentonly` `defensive` | Screenshot width. -1 for screen width. |
| `script_attach_debugger_at_startup` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `script_break_in_native_debugger_on_error` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `sensitivity` | `Float32` | `1.250000` | `0.000100 .. 8.000000` | `clientdll` `archive` `userinfo` `per_user` | Mouse sensitivity. |
| `sensitivity_y_scale` | `Float32` | `1.000000` | `0.000000 .. 2.000000` | `clientdll` `archive` `userinfo` `per_user` | Multiplies the mouse Y axis for finer pitch vs yaw aim |
| `servercfgfile` | `String` | `server.cfg` |  | `gamedll` `release` |  |
| `shake_show` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Displays a list of the active screen shakes. |
| `shatterglass_cleanup` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `shatterglass_cleanup_max` | `Int32` | `200` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `shatterglass_debug` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `shatterglass_hit_tolerance` | `Float32` | `2.000000` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `shatterglass_shard_lifetime` | `Float32` | `15.000000` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `show_visibility_boxes` | `Bool` | `false` |  | `clientdll` `cheat` | Enable or Disable debug display of visibility boxes |
| `silence_dsp` | `Bool` | `false` |  | `cheat` | When on, silences all DSP mixes. |
| `sk_autoaim_mode` | `Int32` | `1` |  | `gamedll` `clientdll` `archive` `replicated` |  |
| `sk_player_arm` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `sk_player_chest` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `sk_player_head` | `Float32` | `2.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `sk_player_leg` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `sk_player_stomach` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `defensive` |  |
| `skel_constraints_enable` | `Bool` | `true` |  | `replicated` `cheat` |  |
| `skel_debug` | `String` |  |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `skeleton_instance_debug_bodygroups` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Debug bodygroups |
| `skeleton_instance_lod_optimization` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Compute LOD mask internally like since 2016, i.e. force all LOD groups' bones to compute |
| `skeleton_instance_scaleset_enable` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `skeleton_instance_smear_boneflags` | `Bool` | `false` |  | `gamedll` `cheat` | Smear boneflags across the model.  Costs computation, but tests to make sure your bone flags are consistent. |
| `skeleton_physics_joint_fixup` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` |  |
| `skill` | `Int32` | `1` | `1 .. 3` | `gamedll` `clientdll` `archive` `replicated` `per_user` | Game skill level. |
| `slope_drop_enable` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Toggles a test dropping the view offset based on the slope |
| `slope_drop_max_offset` | `Float32` | `16.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | The maximum distance to adjust the view height |
| `slope_drop_off_ground_blend_speed` | `Float32` | `160.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | The speed with which the slope drop is blended out when the entity leaves the ground |
| `smoke_grenade_ct_color` | `Vector3` | `75.000000 127.000000 155.000000` |  | `developmentonly` `gamedll` `cheat` |  |
| `smoke_grenade_t_color` | `Vector3` | `180.000000 129.000000 50.000000` |  | `developmentonly` `gamedll` `cheat` |  |
| `smoke_param1` | `Float32` | `6.260000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `smoke_param2` | `Float32` | `8.270000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `smoke_param3` | `Float32` | `0.130000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `smoke_param4` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `smoke_param5` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `smoke_use_noise_texture` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `smoke_volume_lod_ratio_change` | `Float32` | `0.600000` |  | `developmentonly` `clientdll` |  |
| `smoothstairs` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Smooth player eye z coordinate when traversing stairs. |
| `snd_async_spew_blocking` | `Int32` | `0` |  | `developmentonly` `defensive` | Spew message to console any time async sound loading blocks on file i/o. |
| `snd_autodetect_latency` | `Bool` | `true` |  | `archive` |  |
| `snd_beatpattern_show_bpm` | `Bool` | `false` |  | `cheat` |  |
| `snd_beatpattern_show_events` | `Bool` | `false` |  | `cheat` |  |
| `snd_beatpattern_show_quantize_queue` | `Bool` | `false` |  | `cheat` |  |
| `snd_beatpattern_use_lookahead` | `Bool` | `false` |  | `cheat` |  |
| `snd_boxverb_simd` | `Bool` | `true` |  | `developmentonly` `defensive` | Enable SIMD code path for shoebox reverb processor. |
| `snd_boxverb_simd_svf` | `Int32` | `1` |  | `developmentonly` `defensive` | 0 = use biquad instead of svf, 1 = use vectorized svf, 2 = use scalar svf |
| `snd_break_on_start_soundevent` | `String` |  |  | `gamedll` `clientdll` `replicated` `cheat` | Use to debug break on any soundevent that is started matching this name |
| `snd_compare_KV_convert` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `snd_deathcamera_volume` | `Float32` | `0.160000` | `0.000000 .. 1.000000` | `clientdll` `archive` `release` | Volume of Deathcam Timers |
| `snd_delay_sound_ms_max` | `Float32` | `250.000000` | `0.000000 .. 250.000000` | `developmentonly` `defensive` | Sound device synchronization max delay (ms) |
| `snd_delay_sound_ms_shift` | `Float32` | `23.000000` | `0.000000 .. 50.000000` | `developmentonly` `defensive` | Sound device synchronization shift (ms) |
| `snd_diffusor_simd` | `Bool` | `false` |  | `developmentonly` `defensive` | Enable SIMD code path for diffusor processor. |
| `snd_disable_mixer_duck` | `Bool` | `false` |  | `cheat` |  |
| `snd_disable_mixer_solo` | `Bool` | `false` |  | `cheat` |  |
| `snd_disable_radar_visualize` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_dsp_distance_max` | `Float32` | `2000.000000` |  | `cheat` |  |
| `snd_dsp_distance_min` | `Float32` | `20.000000` |  | `cheat` |  |
| `snd_duckerattacktime` | `Float32` | `0.500000` |  | `archive` |  |
| `snd_duckerreleasetime` | `Float32` | `2.500000` |  | `archive` |  |
| `snd_duckerthreshold` | `Float32` | `0.150000` |  | `archive` |  |
| `snd_ducktovolume` | `Float32` | `0.550000` |  | `archive` |  |
| `snd_enable_imgui` | `Bool` | `false` |  | `developmentonly` `archive` `cheat` `menubar_item` | Game/Sound System Debugger |
| `snd_enable_subgraph_corenull_passthrough` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `snd_enable_subgraph_log` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `snd_envelope_rate` | `Float32` | `0.900000` |  | `cheat` |  |
| `snd_eq_arms_race` | `Int32` | `-1` |  | `developmentonly` `clientdll` `archive` |  |
| `snd_eq_casual` | `Int32` | `-1` |  | `developmentonly` `clientdll` `archive` |  |
| `snd_eq_competitive` | `Int32` | `-1` |  | `developmentonly` `clientdll` `archive` |  |
| `snd_eq_deathmatch` | `Int32` | `-1` |  | `developmentonly` `clientdll` `archive` |  |
| `snd_eq_spectator` | `Int32` | `-1` |  | `developmentonly` `clientdll` `archive` |  |
| `snd_eq_warmup` | `Int32` | `-1` |  | `developmentonly` `clientdll` `archive` |  |
| `snd_event_cone_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` |  |
| `snd_event_oriented_box_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` |  |
| `snd_event_oriented_lerp_max_distance` | `Float32` | `64.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` |  |
| `snd_event_oriented_lerp_min_distance` | `Float32` | `24.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` |  |
| `snd_filter` | `String` |  |  | `cheat` |  |
| `snd_foliage_db_loss` | `Float32` | `4.000000` |  | `gamedll` `cheat` | foliage dB loss per 1200 units |
| `snd_gain` | `Float32` | `1.000000` |  | `archive` |  |
| `snd_gain_max` | `Float32` | `1.000000` |  | `cheat` |  |
| `snd_gain_min` | `Float32` | `0.010000` |  | `cheat` |  |
| `snd_gamevoicevolume` | `Float32` | `1.000000` | `0.000000 .. 1.000000` | `archive` | Game v.o. volume |
| `snd_gamevolume` | `Float32` | `1.000000` | `0.000000 .. 1.000000` | `archive` | Game volume |
| `snd_group_cluster_debug` | `Bool` | `false` |  | `replicated` `cheat` |  |
| `snd_group_occlusion_debug` | `Bool` | `false` |  | `developmentonly` |  |
| `snd_group_priority_debug` | `Bool` | `false` |  | `replicated` `cheat` |  |
| `snd_group_priority_max_tolerance` | `Float32` | `0.050000` |  | `replicated` `cheat` |  |
| `snd_headphone_eq` | `Int32` | `0` |  | `clientdll` `archive` `clientcmd_can_execute` | Select Headphone EQ Preset |
| `snd_headphone_eq_active` | `Int32` | `0` |  | `clientdll` `clientcmd_can_execute` | Select Headphone EQ Preset |
| `snd_hrtf_distance_behind` | `Float32` | `0.000000` |  | `developmentonly` `defensive` | HRTF calculations will calculate the player as being this far behind the camera. |
| `snd_list` | `String` |  |  | `cheat` |  |
| `snd_log_empty_event_entities` | `Bool` | `false` |  | `clientdll` `cheat` | Logs the sound event entities that have empty names. |
| `snd_mainmenu_music_break_time_max` | `Int32` | `0` |  | `clientdll` `cheat` | Maximum amount of time to pause between playing main menu music |
| `snd_mainmenu_music_break_time_min` | `Int32` | `0` |  | `clientdll` `cheat` | Minimum amount of time to pause between playing main menu music |
| `snd_mapobjective_volume` | `Float32` | `0.040000` | `0.000000 .. 1.000000` | `clientdll` `archive` `release` | Volume of Map Objective Music |
| `snd_max_pitch_shift_inaccuracy` | `Float32` | `0.080000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_menumap_volume` | `Float32` | `1.000000` | `0.000000 .. 1.000000` | `clientdll` `archive` `release` | Volume of background sounds for maps |
| `snd_menumusic_volume` | `Float32` | `0.040000` | `0.000000 .. 1.000000` | `clientdll` `archive` `release` | Volume of Menu / Non-gameplay music |
| `snd_mergemethod` | `Int32` | `1` |  | `developmentonly` `defensive` | Sound merge method (0 == sum and clip, 1 == max, 2 == avg). |
| `snd_min_latency` | `Bool` | `false` |  | `developmentonly` `cheat` |  |
| `snd_mix_async` | `Bool` | `true` |  | `developmentonly` `cheat` |  |
| `snd_mixahead` | `Float32` | `0.001000` |  | `archive` |  |
| `snd_mixer_master_dsp` | `Float32` | `1.000000` |  | `cheat` |  |
| `snd_mixer_master_level` | `Float32` | `1.000000` |  | `cheat` |  |
| `snd_musicvolume` | `Float32` | `1.000000` | `0.000000 .. 1.000000` | `archive` | Music volume |
| `snd_mute_losefocus` | `Bool` | `true` |  | `archive` |  |
| `snd_mute_mvp_music_live_players` | `Bool` | `false` |  | `clientdll` `archive` `release` | If set, MVP music is muted if players from both teams are still alive. |
| `snd_mvp_volume` | `Float32` | `0.160000` | `0.000000 .. 1.000000` | `clientdll` `archive` `release` | Volume of MVP Music |
| `snd_new_visualize` | `Bool` | `false` |  | `gamedll` `cheat` | Displays soundevent name played at it's 3d position |
| `snd_occlusion_bounces` | `Int32` | `1` |  | `replicated` `cheat` |  |
| `snd_occlusion_debug` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `snd_occlusion_debug_listener_pos` | `String` |  |  | `developmentonly` `cheat` |  |
| `snd_occlusion_indirect_max` | `Float32` | `0.700000` |  | `developmentonly` `cheat` |  |
| `snd_occlusion_indirect_min` | `Float32` | `0.010000` |  | `developmentonly` `cheat` |  |
| `snd_occlusion_indirect_radius` | `Float32` | `120.000000` |  | `developmentonly` `cheat` |  |
| `snd_occlusion_min_wall_thickness` | `Float32` | `4.000000` |  | `replicated` `cheat` |  |
| `snd_occlusion_override` | `Float32` | `-1.000000` |  | `developmentonly` `replicated` `cheat` |  |
| `snd_occlusion_rays` | `Int32` | `4` |  | `replicated` `cheat` |  |
| `snd_occlusion_report` | `Bool` | `false` |  | `developmentonly` `cheat` |  |
| `snd_occlusion_visualize` | `Bool` | `false` |  | `developmentonly` `cheat` |  |
| `snd_op_test_convar` | `Float32` | `720.000000` |  | `cheat` |  |
| `snd_opvar_set_point_debug` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `snd_opvar_set_point_update_interval` | `Float32` | `0.200000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_opvar_set_point_update_interval_fast` | `Float32` | `0.033300` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_rear_stereo_scale` | `Float32` | `1.000000` |  | `replicated` `cheat` |  |
| `snd_refdb` | `Float32` | `60.000000` |  | `cheat` | Reference dB at snd_refdist |
| `snd_refdist` | `Float32` | `36.000000` |  | `cheat` | Reference distance for snd_refdb |
| `snd_report_audio_nan` | `Bool` | `false` |  | `release` |  |
| `snd_report_c4_sounds` | `Bool` | `false` |  | `developmentonly` `clientdll` `cheat` |  |
| `snd_report_verbose_error` | `Bool` | `false` |  | `cheat` | If set to 1, report more error found when playing sounds. |
| `snd_roundaction_volume` | `Float32` | `0.000000` | `0.000000 .. 1.000000` | `clientdll` `archive` `release` | Volume of Move Action Music |
| `snd_roundend_volume` | `Float32` | `0.160000` | `0.000000 .. 1.000000` | `clientdll` `archive` `release` | Volume of Won/Lost Music |
| `snd_roundstart_volume` | `Float32` | `0.000000` | `0.000000 .. 1.000000` | `clientdll` `archive` `release` | Volume of Round Start Music |
| `snd_showclassname` | `Int32` | `0` |  | `cheat` |  |
| `snd_showstart` | `Int32` | `0` |  | `cheat` |  |
| `snd_sos_beatpattern_show_operator_updates` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `snd_sos_block_global_stack` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_block_stop_global_stack` | `Bool` | `true` |  | `cheat` |  |
| `snd_sos_calc_angle_debug` | `Bool` | `false` |  | `replicated` `cheat` |  |
| `snd_sos_debug_trigger_opvar` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `snd_sos_enable_nan_check` | `Bool` | `false` |  | `developmentonly` |  |
| `snd_sos_hide_simple_parameter_overwrite_warnings` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `snd_sos_ingame_debug` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_limit_self` | `Bool` | `false` |  | `developmentonly` |  |
| `snd_sos_list_operator_updates` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_max_event_base_depth` | `Int32` | `4` |  | `developmentonly` `defensive` |  |
| `snd_sos_opvar_debug` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_pause_system` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_print_addfield_dupes` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_print_field_references` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_print_fps` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_print_frametime` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_print_full_field_info` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_print_table_arrays` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_report_entity_deleted` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `snd_sos_show_block_debug` | `Bool` | `false` |  | `cheat` | Spew data about the list of block entries. |
| `snd_sos_show_entry_match_free` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `snd_sos_show_mixgroup_path_errors` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `snd_sos_show_operator_event_and_stack` | `Bool` | `true` |  | `cheat` |  |
| `snd_sos_show_operator_event_filter` | `String` |  |  | `cheat` |  |
| `snd_sos_show_operator_field_filter` | `String` |  |  | `cheat` |  |
| `snd_sos_show_operator_init` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_show_operator_not_executing` | `Bool` | `true` |  | `cheat` |  |
| `snd_sos_show_operator_operator_filter` | `String` |  |  | `cheat` |  |
| `snd_sos_show_operator_pause_entry` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_show_operator_shutdown` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_show_operator_stop_entry` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_show_operator_updates` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_show_opfield_cache_updates` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_show_opvar_updates` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_show_opvar_updates_filter` | `String` |  |  | `cheat` |  |
| `snd_sos_show_parameter_overwrite_value_comparisons` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `snd_sos_show_parameter_overwrite_warnings` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `snd_sos_show_queuetotrack` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_show_soundevent_overwrites` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `snd_sos_show_soundevent_param_overwrite` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_show_soundevent_start` | `Bool` | `false` |  | `cheat` |  |
| `snd_sos_show_track_list` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `snd_sos_show_voice_elapsed_time` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `snd_sos_soundevent_constellation_debug` | `Bool` | `false` |  | `developmentonly` `replicated` `cheat` |  |
| `snd_sos_soundevent_constellation_replenish_max_fraction` | `Float32` | `0.300000` |  | `developmentonly` `replicated` `cheat` |  |
| `snd_sos_soundevent_deferred_interval_time` | `Float32` | `0.100000` |  | `developmentonly` `defensive` |  |
| `snd_sos_soundevent_filter` | `String` |  |  | `cheat` |  |
| `snd_sos_soundevent_max_deferred_time` | `Float32` | `5.000000` |  | `developmentonly` `defensive` |  |
| `snd_sos_soundevent_show_deferral_warning` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `snd_sos_tools_detailed_debugging` | `Bool` | `true` |  | `developmentonly` `archive` |  |
| `snd_sound_areas_debug` | `Bool` | `false` |  | `clientdll` `replicated` `cheat` |  |
| `snd_sound_areas_debug_interval` | `Float32` | `0.200000` |  | `clientdll` `replicated` `cheat` |  |
| `snd_soundmixer` | `String` | `Default_Mix` |  | `developmentonly` `defensive` |  |
| `snd_soundmixer_update_maximum_frame_rate` | `Int32` | `10` |  | `cheat` |  |
| `snd_soundmixer_version` | `Int32` | `2` |  | `developmentonly` `defensive` |  |
| `snd_spatialize_lerp` | `Float32` | `0.000000` |  | `archive` `release` |  |
| `snd_steamaudio_display_dimension_data_inside` | `Bool` | `true` |  | `developmentonly` `defensive` | When visualizing dimensions data at runtime, draw the inside direction. |
| `snd_steamaudio_display_dimension_data_outside` | `Bool` | `true` |  | `developmentonly` `defensive` | When visualizing dimensions data at runtime, draw the outisde direction. |
| `snd_steamaudio_display_dimension_data_size` | `Bool` | `true` |  | `developmentonly` `defensive` | When visualizing dimensions data at runtime, draw the size of the space. |
| `snd_steamaudio_dynamicpathing_max_samples` | `Int32` | `16` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_steamaudio_enable_reverb` | `Float32` | `0.000000` |  | `release` | Enable Steam Audio Reverb processor. |
| `snd_steamaudio_pathing_caching_threshold` | `Float32` | `5.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_steamaudio_pathing_enable_caching` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_steamaudio_perspective_correction_front_only` | `Bool` | `true` |  | `developmentonly` | Use perspective correction for 3D audio only in the frontal directions. |
| `snd_steamaudio_reverb_level_db` | `Float32` | `-3.000000` |  | `release` | Adjust overall volume (dB) of the output from Steam Audio Reverb processor. |
| `snd_steamaudio_source_pathing_debug` | `Bool` | `false` |  | `archive` | Enable path visualization for steam_audio_source operator. |
| `snd_steamaudio_source_pathing_debug_duration` | `Float32` | `0.010000` |  | `developmentonly` `defensive` | Duration for which path remains visible. Should be close to update rate of the sound operator stack. |
| `snd_steamaudio_source_pathing_enable_validation` | `Bool` | `false` |  | `developmentonly` `defensive` | Enable real-time pathing validation against dynamic geometry. |
| `snd_surf_volume_inair` | `Float32` | `0.500000` |  | `clientdll` `archive` `release` | The volume of the wind when surfing. |
| `snd_surf_volume_map` | `Float32` | `0.300000` |  | `clientdll` `archive` `release` | The volume of ambient sounds when surfing is enabled. |
| `snd_surf_volume_slide` | `Float32` | `0.500000` |  | `clientdll` `archive` `release` | The volume of sliding along surfaces when surfing. |
| `snd_tensecondwarning_volume` | `Float32` | `0.040000` | `0.000000 .. 1.000000` | `clientdll` `archive` `release` | Volume of Ten Second Warnings |
| `snd_toolvolume` | `Float32` | `1.000000` | `0.000000 .. 1.000000` | `archive` | Volume of sounds in tools (e.g. Hammer, SFM) |
| `snd_ui_positional` | `Bool` | `false` |  | `developmentonly` `cheat` |  |
| `snd_ui_spatialization_spread` | `Float32` | `1.000000` |  | `developmentonly` `cheat` |  |
| `snd_use_baked_occlusion` | `Float32` | `0.000000` |  | `replicated` `cheat` `release` |  |
| `snd_vmix_override_mix_decay_time` | `Float32` | `-1.000000` |  | `cheat` | If set &gt; 0, overrides how long the decay time is on all mix graphs (in seconds). |
| `snd_voipvolume` | `Float32` | `1.000000` | `0.000000 .. 2.000000` | `archive` | Voice volume |
| `snd_vol_arms_race` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `archive` |  |
| `snd_vol_casual` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `archive` |  |
| `snd_vol_competitive` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `archive` |  |
| `snd_vol_deathmatch` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `archive` |  |
| `snd_vol_per_game_mode` | `Bool` | `true` |  | `developmentonly` `clientdll` `archive` |  |
| `snd_vol_spectator` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `archive` |  |
| `snd_vol_warmup` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `archive` |  |
| `sos_debug_emit` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sos_use_guid_filter` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sound_device_override` | `String` |  |  | `archive` `release` | ID of the sound device to use |
| `soundevent_check_networked_entity` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `soundpatch_captionlength` | `Float32` | `2.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | How long looping soundpatch captions should display for. |
| `soundscape_debug` | `Bool` | `false` |  | `gamedll` `cheat` | When on, draws lines to all env_soundscape entities. Green lines show the active soundscape, red lines show soundscapes that aren't in range, and white lines show soundscapes that are in range, but not the active soundscape. |
| `soundscape_fadetime` | `Float32` | `3.000000` |  | `clientdll` `cheat` | Time to crossfade sound effects between soundscapes |
| `soundscape_message` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` |  |
| `soundscape_radius_debug` | `Bool` | `false` |  | `clientdll` `cheat` | Prints current volume of radius sounds |
| `soundscape_update_include_bots` | `Bool` | `false` |  | `developmentonly` `gamedll` `cheat` | Enable to calculate soundscape audio params for bots. |
| `soundsystem_device_used` | `String` |  |  | `developmentonly` `defensive` | Sound device in use (changing this does not change the soundsystem). |
| `soundsystem_update_async` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sparseshadowtree_cascade_mask` | `Int32` | `4` |  | `developmentonly` | Bitfield describing which cascades to generate/use SST for. (OR'd 1UL&lt;&lt;cascadeIndex, default is 1UL&lt;&lt;2 only, i.e. just cascade 2) |
| `sparseshadowtree_copy_to_shadow_atlas_ps` | `Bool` | `true` |  | `developmentonly` | Copy layer from CS output to shadow atlas uses PS copy (vs CopyTexture). |
| `sparseshadowtree_cs_debug_colors` | `Bool` | `false` |  | `developmentonly` | Output debug colors for SST CS. |
| `sparseshadowtree_cs_exclude_next_cascade_region` | `Bool` | `true` |  | `developmentonly` | Exclude the inner region of a cascade during CS unpack if there is a higher resolution cascade that will cover that area. |
| `sparseshadowtree_cs_unpack_mode` | `Int32` | `1` | `0 .. 2` | `developmentonly` | Unpack mode in cs, 0 - one leaf per thread (16 output pixels), 1 (default) - one leaf row per thread (4 output pixels), 2 - one pixel out per thread. |
| `sparseshadowtree_debug_tile_range_xmax` | `Int32` | `1` |  | `developmentonly` | SST Tile range for renderdoc/debug capturing. |
| `sparseshadowtree_debug_tile_range_xmin` | `Int32` | `0` |  | `developmentonly` | SST Tile range for renderdoc/debug capturing. |
| `sparseshadowtree_debug_tile_range_ymax` | `Int32` | `1` |  | `developmentonly` | SST Tile range for renderdoc/debug capturing. |
| `sparseshadowtree_debug_tile_range_ymin` | `Int32` | `0` |  | `developmentonly` | SST Tile range for renderdoc/debug capturing. |
| `sparseshadowtree_disable_add_layers` | `Bool` | `false` |  | `developmentonly` | Disable SST runtime layers, for debugging (will exclude geo that CAN render into SST if SST otherwise enabled) |
| `sparseshadowtree_disable_for_viewmodel` | `Bool` | `true` |  | `developmentonly` | Disable SST generation and runtime for viewmodel (use original CSM rendering). |
| `sparseshadowtree_enable_rendering` | `Bool` | `true` |  | `developmentonly` | Enable use of SST at runtime (static geo rendered into cascades via SST). |
| `sparseshadowtree_leaf_compress_scaleoffset` | `Bool` | `true` |  | `developmentonly` | Compress leaf node depths using scale &amp; offset. |
| `sparseshadowtree_leaf_precision` | `Float32` | `0.000400` |  | `developmentonly` | precision for depth compression at SST leaf nodes. |
| `sparseshadowtree_leaf_precision_viewmodel` | `Float32` | `0.000500` |  | `developmentonly` | (viewmodel) precision for depth compression at SST leaf nodes. |
| `sparseshadowtree_parallel_generation` | `Int32` | `2` |  | `developmentonly` | Split SST tile generation into threadjobs (0 - disabled, 1 - wait on readpixels for job batch, 2 - async readpixels). |
| `sparseshadowtree_plane_incr_per_step` | `Float32` | `0.000100` |  | `developmentonly` | depth to increment candidate plane values per iteration to satisfy selection. |
| `sparseshadowtree_plane_incr_per_step_viewmodel` | `Float32` | `0.002500` |  | `developmentonly` | (viewmodel) depth to increment candidate plane values per iteration to satisfy selection. |
| `sparseshadowtree_plane_max_error` | `Float32` | `0.000400` |  | `developmentonly` | max error (distance away in depth) candidate plane is allowed before rejecting. |
| `sparseshadowtree_plane_max_error_viewmodel` | `Float32` | `0.010000` |  | `developmentonly` | (viewmodel) max error (distance away in depth) candidate plane is allowed before rejecting. |
| `sparseshadowtree_plane_num_iter` | `Int32` | `5` |  | `developmentonly` | number of steps to push candidate plane behind depths. |
| `sparseshadowtree_render_cables` | `Bool` | `false` |  | `developmentonly` | Render cables into SST. |
| `sparseshadowtree_renderdoc_capture_generation` | `Bool` | `false` |  | `developmentonly` | Capture dual shadow maps during sparseshadowtree generation. |
| `sparseshadowtree_unpack_direct_to_shadow_atlas` | `Bool` | `false` |  | `developmentonly` | unpack SST directly into shadow atlas cascade vs via staging texture PS copy (NOTE - rendersystem fix reqd for AMD + driver fix required for NV + VK only. |
| `sparseshadowtree_uv_frac_offset_x` | `Float32` | `0.000000` |  | `developmentonly` | uv x offset during copy to cascade. |
| `sparseshadowtree_uv_frac_offset_y` | `Float32` | `0.000000` |  | `developmentonly` | uv y offset during copy to cascade. |
| `spawngroup_ignore_timeouts` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `speaker_config` | `Int32` | `-1` |  | `archive` |  |
| `spec_autodirector` | `Bool` | `true` |  | `clientdll` `clientcmd_can_execute` | Auto-director chooses best view modes while spectating |
| `spec_autodirector_cameraman` | `Int32` | `-1` |  | `developmentonly` `clientdll` |  |
| `spec_centerchasecam` | `Bool` | `false` |  | `clientdll` `archive` | Looks at the target player's center, instead of his eye position, in chase came mode |
| `spec_chasedistance` | `Float32` | `96.000000` | `16.000000 .. 296.000000` | `developmentonly` `clientdll` `defensive` | Chase cam's ideal distance from target |
| `spec_chasedistancespeed` | `Float32` | `144.000000` | `>= 48.000000` | `developmentonly` `clientdll` `defensive` | Chase cam's ideal distance from target |
| `spec_death_panel_replay_position` | `Float32` | `0.750000` |  | `developmentonly` `clientdll` `defensive` |  |
| `spec_freeze_deathanim_time` | `Float32` | `0.800000` |  | `gamedll` `clientdll` `replicated` `release` | The time that the death cam will spend watching the player's ragdoll before going into the freeze death cam. |
| `spec_freeze_time` | `Float32` | `3.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Time spend frozen in observer freeze cam. |
| `spec_freeze_time_lock` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` | Time players are prevented from skipping the freeze cam |
| `spec_freeze_traveltime` | `Float32` | `0.300000` |  | `gamedll` `clientdll` `replicated` `release` | Time taken to zoom in to frame a target in observer freeze cam. |
| `spec_glow_decay_time` | `Float32` | `2.000000` | `>= 0.000000` | `clientdll` `release` | Time to decay glow from 1.0 to spec_glow_silent_factor after spec_glow_full_time. |
| `spec_glow_full_time` | `Float32` | `1.000000` | `>= 0.000000` | `clientdll` `release` | Noisy players stay at full brightness for this long. |
| `spec_glow_silent_factor` | `Float32` | `0.400000` | `0.000000 .. 1.000000` | `clientdll` `release` | Lurking player xray glow scaling. |
| `spec_glow_spike_factor` | `Float32` | `1.200000` | `1.000000 .. 3.000000` | `clientdll` `release` | Noisy player xray glow scaling (pop when noise is made).  Make &gt;1 to add a 'spike' to noise-making players |
| `spec_glow_spike_time` | `Float32` | `0.000000` | `>= 0.000000` | `clientdll` `release` | Time for noisy player glow 'spike' to show that they made noise very recently. |
| `spec_lock_to_accountid` | `UInt32` | `0` |  | `developmentonly` `clientdll` | As an observer, lock the spectator target to the given accountid. |
| `spec_replay_autostart` | `Bool` | `true` |  | `clientdll` `archive` | Auto-start Killer Replay when available |
| `spec_replay_bot` | `Bool` | `false` |  | `gamedll` `release` | Enable Spectator Hltv Replay when killed by bot |
| `spec_replay_cache_ragdolls` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` | when set to 0, ragdolls will settle dynamically before and after Killer Replay |
| `spec_replay_colorcorrection` | `Float32` | `0.500000` |  | `developmentonly` `clientdll` `defensive` | Amount of color correction in deathcam replay |
| `spec_replay_enable` | `Int32` | `0` |  | `replicated` `release` `commandline_enforced` | Enable Killer Replay, requires hltv server running (0:off, 1:default, 2:force) |
| `spec_replay_fadein` | `Float32` | `0.750000` |  | `developmentonly` `clientdll` `defensive` | Amount of time in seconds it takes to visually fade into replay, or into real-time after replay |
| `spec_replay_fadeout` | `Float32` | `0.750000` |  | `developmentonly` `clientdll` `defensive` | Amount of time in seconds it takes to visually fade out of replay, or out of real-time before replay |
| `spec_replay_fullframe` | `Bool` | `true` |  | `developmentonly` `defensive` | Send full frame on every hltv replay transition |
| `spec_replay_leadup_time` | `Float32` | `5.343800` |  | `replicated` `release` | Replay time in seconds before the highlighted event |
| `spec_replay_message_time` | `Float32` | `9.500000` |  | `replicated` `release` | How long to show the message about Killer Replay after death. The best setting is a bit shorter than spec_replay_autostart_delay + spec_replay_leadup_time + spec_replay_winddown_time |
| `spec_replay_on_death` | `Bool` | `false` |  | `replicated` `release` | When &gt; 0, sets the mode whereas players see delayed replay, and are segregated into a domain of chat and voice separate from the alive players |
| `spec_replay_others_experimental` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Replay the last death of the round, if possible. Disabled on official servers by default. Experimental. |
| `spec_replay_outline` | `Int32` | `1` |  | `developmentonly` `clientdll` `defensive` | Enable outline selecting victim in hltv replay: 0 - none; 1 - ouline YOU; 2 - outline YOU, with red ragdoll outline; 3 - normal spectator outlines |
| `spec_replay_rate_base` | `Float32` | `1.000000` |  | `replicated` `release` | Base time scale of Killer Replay.Experimental. |
| `spec_replay_rate_limit` | `Float32` | `3.000000` |  | `replicated` `release` | Minimum allowable pause between replay requests in seconds |
| `spec_replay_rate_slowdown` | `Float32` | `1.000000` |  | `developmentonly` `clientdll` `defensive` | The part of Killer Replay right before death is played at this rate |
| `spec_replay_rate_slowdown_length` | `Float32` | `0.500000` |  | `developmentonly` `clientdll` `defensive` | The part of Killer Replay right before death is played at this rate |
| `spec_replay_review_sound` | `Bool` | `true` |  | `developmentonly` `clientdll` `defensive` | When set to non-0, a sound effect is played during Killer Replay |
| `spec_replay_round_delay` | `Float32` | `0.000000` |  | `gamedll` `release` | Round can be delayed by this much due to someone watching a replay; must be at least 3-4 seconds, otherwise the last replay will always be interrupted by round start, assuming normal pause between round_end and round_start events (7 seconds) and freezecam delay (2 seconds) and 7.4 second full replay (5.4 second pre-death and ~2 seconds post-death) and replay in/out switching (up to a second) |
| `spec_replay_sound_fadein` | `Float32` | `0.050000` |  | `developmentonly` `clientdll` `defensive` | Amount of time in seconds it takes to fade in the audio before or after replay |
| `spec_replay_sound_fadeout` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` `defensive` | Amount of time in seconds it takes to fade out the audio before or after replay |
| `spec_replay_victim_pov` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Killer Replay - replay from victim's point of view (1); the default is killer's (0). Experimental. |
| `spec_replay_winddown_time` | `Float32` | `2.000000` |  | `gamedll` `release` | The trailing time, in seconds, of replay past the event, including fade-out |
| `spec_show_xray` | `Int32` | `1` |  | `clientdll` `archive` `release` | If set to 1, you can see player outlines and name IDs through walls - who you can see depends on your team and mode |
| `spec_track` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` | Tracks an entity in spec mode |
| `spec_usenumberkeys_nobinds` | `Bool` | `true` |  | `clientdll` `archive` | If set to 1, map voting and spectator view use the raw number keys instead of the weapon binds (slot1, slot2, etc). |
| `splitscreen_mode` | `Int32` | `0` |  | `archive` `cheat` |  |
| `ss_mimic` | `Int32` | `0` |  | `developmentonly` `clientdll` `cheat` | Split screen users mimic base player's CUserCmds |
| `ss_voice_hearpartner` | `Bool` | `false` |  | `developmentonly` `defensive` | Route voice between splitscreen players on same system. |
| `stats_collect_gpu` | `Bool` | `false` |  | `developmentonly` `defensive` | While doing stats_display, collect GPU perf counters. Used for stats_print_gpu. |
| `stats_display` | `Int32` | `0` |  | `developmentonly` `defensive` | Displays perf statistics information |
| `stats_highlight_interval` | `Float32` | `10.000000` |  | `developmentonly` `clientdll` `defensive` | Interval between hightlight screens in the transition stats panel |
| `steam_controller_haptics` | `Bool` | `true` |  | `clientdll` `release` |  |
| `steamworks_sessionid_client` | `String` | `0` |  | `clientdll` `hidden` `userinfo` | The client session ID for the new steamworks gamestats. |
| `steamworks_sessionid_server` | `String` | `0` |  | `developmentonly` `gamedll` `clientdll` `hidden` `replicated` `defensive` | The server session ID for the new steamworks gamestats. |
| `sticky_tooltips` | `Bool` | `false` |  | `developmentonly` `clientdll` `hidden` `defensive` | Don't ever hide tooltips. Helpful when debugging complicated tooltip layouts. |
| `surf_speed_fast` | `Float32` | `3000.000000` |  | `gamedll` `clientdll` `replicated` `release` | Speed above which a player is considered to be going fast. |
| `surf_speed_med` | `Float32` | `2000.000000` |  | `gamedll` `clientdll` `replicated` `release` | Speed above which a player is considered to be going medium. |
| `surf_speed_slow` | `Float32` | `50.000000` |  | `gamedll` `clientdll` `replicated` `release` | Speed above which a player is considered to be going slow. |
| `suspicious_hit_odds_threshold` | `Float32` | `0.010000` |  | `gamedll` `release` |  |
| `suspicious_hit_player_radius` | `Float32` | `8.000000` |  | `gamedll` `release` |  |
| `suspicious_hit_strategy` | `UInt32` | `0` |  | `gamedll` `release` | What to do about suspicious hits. 0: Nothing. 1: Skip the bullet. 2: Skip the bullet and re-roll a new bullet. |
| `sv_accelerate` | `Float32` | `5.500000` |  | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_accelerate_debug_speed` | `Bool` | `false` |  | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_accelerate_use_weapon_speed` | `Bool` | `true` |  | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_ag2_record_entity_graph` | `String` |  |  | `developmentonly` `gamedll` | Automatically start AG2 recording when an entity with this name (wildcard) or id is created. |
| `sv_air_max_wishspeed` | `Float32` | `30.000000` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_airaccelerate` | `Float32` | `12.000000` |  | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_allchat` | `Bool` | `true` |  | `gamedll` `notify` `release` | Players can receive all other players' text chat, no death restrictions |
| `sv_allow_annotations_access_level` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | 0:off \| 1: view-only \| 2: edit. |
| `sv_allow_ground_weapon_pickup` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_allow_switching_weapon_handedness` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_allow_votes` | `Bool` | `true` |  | `gamedll` `release` `commandline_enforced` | Allow voting? |
| `sv_alltalk` | `Bool` | `false` |  | `gamedll` `notify` `release` `commandline_enforced` | Players can hear all other players' voice communication, no team restrictions |
| `sv_annotation_limits_max_rounds_per_half` | `Int32` | `5` | `>= -1` | `gamedll` `clientdll` `replicated` `release` | Hard limit on maximum number of rounds (per half) that annotations can be seen in a live match |
| `sv_auto_adjust_bot_difficulty` | `Bool` | `true` |  | `gamedll` `release` `commandline_enforced` | Adjust the difficulty of bots each round based on contribution score. |
| `sv_auto_cstrafe_attempt_window` | `Int32` | `1` | `1 .. 1000` | `gamedll` `release` | The length of the window of trailing counter-strafe attempts considered during input automation detection. |
| `sv_auto_cstrafe_kick` | `Bool` | `false` |  | `gamedll` `release` | Whether or not to kick players when counter-strafe input automation is detected. |
| `sv_auto_cstrafe_logging` | `Int32` | `0` | `0 .. 2` | `gamedll` `release` | 0: never, 1: every time counter-strafe input automation is detected, 2: every counter-strafe |
| `sv_auto_cstrafe_lower_overlap_pct_threshold` | `Float32` | `0.000000` | `0.000000 .. 100.000000` | `gamedll` `release` | The percentage of overlapping attempts in the attempt window below which input automation detection is triggered at the success threshold. |
| `sv_auto_cstrafe_min_attempts` | `Int32` | `1` | `1 .. 1000` | `gamedll` `release` | The minimum number of counter-strafe attempts required for input automation detection. The player must be moving more than 135.2 units/s for their counter-strafe to be considered an attempt. An attempt is either considered a success (counter-strafing took place within a single tick), an overlap (both directions were held for 1+ ticks) or an underlap (neither direction was held for 1+ ticks). |
| `sv_auto_cstrafe_sequence_length` | `Int32` | `1` | `1 .. 1000` | `gamedll` `release` | The length of sequential counter-strafe attempts evaluated relative to the success threshold. Input automation detection considers the best sequence within the larger attempt window. |
| `sv_auto_cstrafe_success_threshold` | `Int32` | `1` | `1 .. 1000` | `gamedll` `release` | The minimum number of successful counter-strafes within a best sequence that will trigger input automation detection. The number of successes that trigger input automation detection is interpolated between the success threshold and a 'perfect' sequence (all counter-strafes in a sequence are successes), depending on the player's percentage of overlapping counter-strafe attempts. |
| `sv_auto_cstrafe_upper_overlap_pct_threshold` | `Float32` | `0.000000` | `0.000000 .. 100.000000` | `gamedll` `release` | The percentage of overlapping attempts in the attempt window below which input automation detection is triggered when all counter-strafes in a sequence are successes. |
| `sv_auto_full_alltalk_during_warmup_half_end` | `Bool` | `true` |  | `gamedll` `release` `commandline_enforced` | When enabled will automatically turn on full all talk mode in warmup, at halftime and at the end of the match |
| `sv_autobunnyhopping` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Players automatically re-jump while holding jump button |
| `sv_autobuyammo` | `Bool` | `false` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | Enable automatic ammo purchase when inside buy zones during buy periods |
| `sv_autoexec_mapname_cfg` | `Bool` | `false` |  | `gamedll` `release` | Execute a mapname cfg file on the server automatically in custom game modes that require it. |
| `sv_autosave` | `Bool` | `true` |  | `developmentonly` `gamedll` `replicated` `defensive` | Set to 1 to autosave game on level transition. Does not affect autosave triggers. |
| `sv_backspeed` | `Float32` | `0.600000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | How much to slow down backwards motion |
| `sv_banid_enabled` | `Bool` | `true` |  | `release` | Whether server supports banid command |
| `sv_bhop_time_window` | `Float32` | `0.007812` | `>= 0.000000` | `gamedll` `clientdll` `replicated` `release` | sv_legacy_jump disabled only: The time window (in seconds) around landing where a jump press is considered a bhop attempt. |
| `sv_bot_buy_decoy_weight` | `Float32` | `1.000000` | `>= 0.000000` | `gamedll` `release` | Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars. |
| `sv_bot_buy_flash_weight` | `Float32` | `1.000000` | `>= 0.000000` | `gamedll` `release` | Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars. |
| `sv_bot_buy_grenade_chance` | `Float32` | `33.000000` | `0.000000 .. 100.000000` | `gamedll` `release` `commandline_enforced` | Chance bots will buy a grenade with leftover money (after prim, sec and armor). Input as percent (0-100.0) |
| `sv_bot_buy_hegrenade_weight` | `Float32` | `6.000000` | `>= 0.000000` | `gamedll` `release` | Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars. |
| `sv_bot_buy_molotov_weight` | `Float32` | `1.000000` | `>= 0.000000` | `gamedll` `release` | Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars. |
| `sv_bot_buy_smoke_weight` | `Float32` | `1.000000` | `>= 0.000000` | `gamedll` `release` | Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars. |
| `sv_bot_difficulty_kbm` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` `clientdll` `hidden` `replicated` `defensive` | Bot difficulty while playing with Keyboard/Mouse device |
| `sv_bot_parallel_threat_detection` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Perform bot threat detection in parallel |
| `sv_bots_get_easier_each_win` | `Int32` | `0` |  | `gamedll` `release` `commandline_enforced` | If &gt; 0, some # of bots will lower thier difficulty each time they win. The argument defines how many will lower their difficulty each time. |
| `sv_bounce` | `Float32` | `0.000000` |  | `gamedll` `clientdll` `notify` `replicated` `release` | Bounce multiplier for when physically simulated objects collide with other objects. |
| `sv_buy_status_override` | `Int32` | `-1` |  | `gamedll` `replicated` `release` `commandline_enforced` | Override for buy status map info. 0 = everyone can buy, 1 = ct only, 2 = t only 3 = nobody |
| `sv_buymenu_open_prevents_opportunistic_pickup` | `Bool` | `false` |  | `gamedll` `release` |  |
| `sv_c4_upright_constraint_damping` | `Float32` | `0.500000` |  | `developmentonly` `gamedll` `defensive` | Controls how much velocity is damped on the constraint. 0 = undamped wobbly spring, 1 = critically damped no wobble fast converge, &gt;1 = over damped |
| `sv_c4_upright_constraint_enabled` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Use a constraint to keep C4 pointed upright when thrown |
| `sv_c4_upright_constraint_strength` | `Float32` | `0.600000` |  | `developmentonly` `gamedll` `defensive` | How quickly the constraint converges |
| `sv_chat_proximity` | `Float32` | `-1.000000` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_cheats` | `Bool` | `false` |  | `notify` `replicated` `release` | Allow cheats on server |
| `sv_client_max_interp_ratio` | `Float32` | `5.000000` | `0.000000 .. 19.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | This can be used to limit the value of cl_interp_ratio for connected clients (only while they are connected). |
| `sv_client_min_interp_ratio` | `Float32` | `0.000000` | `0.000000 .. 19.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | This can be used to limit the value of cl_interp_ratio for connected clients (only while they are connected). |
| `sv_clip_penetration_traces_to_players` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sv_clockcorrection_msecs` | `Float32` | `30.000000` |  | `gamedll` `release` | The server tries to keep each player's m_nTickBase withing this many msecs of the server absolute tickcount |
| `sv_clockdbg` | `Bool` | `false` |  | `developmentonly` | Print spew related to server clock and ticking |
| `sv_cloth_interp_rot` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `sv_cluster` | `Int32` | `0` |  | `release` | Data center cluster this server lives in. |
| `sv_coaching_enabled` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `release` | Allows spectating and communicating with a team ( 'coach t' or 'coach ct' ) |
| `sv_competitive_minspec` | `Bool` | `true` |  | `gamedll` `clientdll` `notify` `replicated` `release` | Enable to force certain client convars to minimum/maximum values to help prevent competitive advantages. |
| `sv_compute_per_bot_difficulty` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` | 0 = compute all bot difficulties equally, 1 = compute unique bot difficulty for each bot |
| `sv_condense_late_buttons` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | When condensing late commands. Should we compress multiple moves of button presses into the target move? |
| `sv_cq_delta_encode_svc_usercmds` | `Bool` | `true` |  | `developmentonly` `gamedll` | Delta encode svc_UserCmds message |
| `sv_cq_min_queue` | `Int32` | `0` | `>= 0` | `developmentonly` `replicated` `defensive` | Server min buffer size. |
| `sv_cq_trim_bloat_remainder` | `Int32` | `1` |  | `gamedll` `release` | When trimming a bloated CQ, leave at least N more commands than the minimum |
| `sv_cq_trim_bloat_space` | `Int32` | `0` |  | `gamedll` `release` | When trimming a bloated CQ, try to leave room for N more commands to be added.  0 will trim only what is needed to remove the immediate bloat, a very large value will reset the whole queue. |
| `sv_cq_trim_catchup_remainder` | `Int32` | `1` |  | `gamedll` `release` | When trimming an overful CQ due to app 'catchup' request, leave at least N more commands than the minimum |
| `sv_cq_validate_encoded_svc_usercmds` | `Bool` | `false` |  | `developmentonly` `gamedll` | VERY EXPENSIVE: serialize non-delta-encoded commands along with delta-encoded for validation |
| `sv_cs_player_speed_has_hostage` | `Float32` | `200.000000` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_csgo_gpu_culling_skybox` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_csgo_shoot_assert_lagcompensation_error` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_force_full_interp` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_force_use_target_time` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_lagcompensation_max_error` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Warn if lag compensated head hitbox position doesn't match that on client. |
| `sv_csgo_shoot_log` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_log_attack_cmds_only` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_use_full_interp` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_verify` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_verify_on_attack_only` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Only run lag compensation error check when primary attack goes down. |
| `sv_damage_prediction_allowed` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_deadtalk` | `Bool` | `false` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | Dead players can speak (voice, text) to the living |
| `sv_debug_client_not_in_pvs` | `Bool` | `false` |  | `gamedll` `cheat` | If set, draw failed client PVS checks with red box |
| `sv_debug_overlays_bandwidth` | `Int32` | `65536` |  | `release` | Broadcast server debug overlays traffic |
| `sv_debug_overlays_broadcast` | `Bool` | `false` |  | `notify` `cheat` `release` | Broadcast server debug overlays |
| `sv_debug_player_use` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Visualizes +use logic. Green cross=trace success, Red cross=trace too far, Green box=radius success |
| `sv_debugroundstats` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `sv_deltaticks_enforce` | `Int32` | `2` |  | `release` | By default, player must ack delta ticks in order. How to enforce it: 2 = kick all clients, 1 = kick only TV clients, 0 = do not kick. |
| `sv_deltaticks_log` | `Int32` | `2` |  | `release` | Whether diagnostic logging is enabled when clients ack delta ticks out of order. Policy: 2 = log all out of order acks, 1 = log only when disconnect is triggered, 0 = do not log. |
| `sv_dev_damage_use_netvars` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Whether we should use network vars (true) or legacy messages (false). |
| `sv_dev_entitydeltapadding_extra_max` | `Int32` | `0` |  | `developmentonly` `defensive` | When encoding entity deltas, append on a random number of extra bytes.  This happens after sv_dev_entitydeltapadding_min_size. |
| `sv_dev_entitydeltapadding_extra_min` | `Int32` | `0` |  | `developmentonly` `defensive` | When encoding entity deltas, append on a random number of extra bytes.  This happens after sv_dev_entitydeltapadding_min_size. |
| `sv_dev_entitydeltapadding_min_size` | `Int32` | `0` |  | `developmentonly` `defensive` | When encoding entity deltas, if the delta size is &lt; N bytes, then shove in N dummy bytes.  This happens before sv_dev_entitydeltapadding_extra_min/sv_dev_entitydeltapadding_extra_max |
| `sv_disable_immunity_alpha` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If set, clients won't slam the player model render settings each frame for immunity [mod authors use this] |
| `sv_disable_networkable_loadouts` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `hidden` `replicated` `defensive` |  |
| `sv_disable_observer_interpolation` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | Disallow interpolating between observer targets on this server. |
| `sv_disable_querycache` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | debug - disable trace query cache |
| `sv_disable_radar` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | 0: regular radar; 1: always disabled; 2: disabled in warmup |
| `sv_disable_reliable_delta_retransmit` | `Bool` | `true` |  | `developmentonly` `defensive` | Assume that a reliable entity delta will be ack'ed and send future deltas relative to the last reliable delta. |
| `sv_disable_teamselect_menu` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Disable teamselect menu on clients |
| `sv_disconnected_player_data_hold_time` | `Int32` | `60` |  | `gamedll` `clientdll` `replicated` `release` | Duration, in seconds, to hold onto the data of disconnected players, for scoreboard display. |
| `sv_disconnected_players_cleanup_delay` | `Int32` | `0` | `0 .. 300` | `gamedll` `release` `commandline_enforced` | Delay between player disconnecting and their corpse getting cleaned up. |
| `sv_early_network_message_processing` | `Bool` | `false` |  | `developmentonly` `gamedll` | Processes network messages on the server before entities think, instead of at the end of the tick. |
| `sv_enable_alternate_baselines` | `Int32` | `1` |  | `release` | Allow alternate baseline system, set to 2 for debugging spew. |
| `sv_enable_donttransmit` | `Bool` | `true` |  | `developmentonly` | When encoding entity deltas, instead of unreliably deducing explicit deletions, actually send list of existing but not networked entities (dont_transmit list) to each client. |
| `sv_enable_removearrayelementsoutsidemetadatabounds` | `Bool` | `false` |  | `release` |  |
| `sv_enablebunnyhopping` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Allow jump speed to exceed 1.1x max speed |
| `sv_endmatch_item_drop_interval` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | The time between drops on the end match scoreboard |
| `sv_endmatch_item_drop_interval_ancient` | `Float32` | `3.500000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | The time between drops on the end match scoreboard for ancient items |
| `sv_endmatch_item_drop_interval_legendary` | `Float32` | `2.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | The time between drops on the end match scoreboard for legendary items |
| `sv_endmatch_item_drop_interval_mythical` | `Float32` | `1.250000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | The time between drops on the end match scoreboard for mythical items |
| `sv_endmatch_item_drop_interval_rare` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | The time between drops on the end match scoreboard for rare items |
| `sv_ent_showonlyhitbox` | `Int32` | `-1` |  | `gamedll` `cheat` |  |
| `sv_extra_client_connect_time` | `Float32` | `15.000000` |  | `developmentonly` `defensive` | Seconds after client connect during which extra frames are buffered to prevent non-delta'd update |
| `sv_extract_ammo_from_dropped_weapons` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_extreme_strafe_accuracy_fishtail` | `Float32` | `0.000000` | `-5.000000 .. 5.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | Number of degrees of aim 'fishtail' when making an extreme strafe direction change |
| `sv_fade_player_visibility_farz` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_falldamage_scale` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_falldamage_to_below_player_multiplier` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scale damage when distributed across two players |
| `sv_falldamage_to_below_player_ratio` | `Float32` | `0.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Landing on a another player's head gives them this ratio of the damage. |
| `sv_filterban` | `Int32` | `1` |  | `developmentonly` `defensive` | Set packet filtering by IP mode |
| `sv_flashed_amount_for_blind_kill` | `Float32` | `0.700000` |  | `gamedll` `release` | Minimum flashed alpha value for a player to be awarded a blind kill on the kill feed. |
| `sv_footsteps` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `notify` `replicated` | Play footstep sound for players |
| `sv_force_team_intro_random` | `Int32` | `0` |  | `developmentonly` `gamedll` |  |
| `sv_force_team_intro_variant` | `Int32` | `0` |  | `developmentonly` `gamedll` |  |
| `sv_force_transmit_ents` | `Bool` | `false` |  | `developmentonly` `gamedll` | Will transmit all entities to client, regardless of PVS conditions (will still skip based on transmit flags, however). |
| `sv_fps_max` | `Float32` | `0.000000` |  | `developmentonly` `hidden` `defensive` | Dedicated server frame rate limiter. 0=tick rate. Only applies to the dedicated server. |
| `sv_freeze_camera_angles` | `Vector3` | `0.000000 0.000000 0.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_freeze_camera_enabled` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_freeze_camera_min_remaining` | `Int32` | `3` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_freeze_camera_position` | `Vector3` | `0.000000 0.000000 0.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_friction` | `Float32` | `5.200000` |  | `gamedll` `clientdll` `notify` `replicated` `release` | World friction. |
| `sv_full_alltalk` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | Any player (including Spectator team) can speak to any other player |
| `sv_game_mode_flags` | `Int32` | `0` |  | `gamedll` `release` | Dedicated server game mode flags to run |
| `sv_gameinstructor_disable` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | Force all clients to disable their game instructors. |
| `sv_gameinstructor_enable` | `Bool` | `false` |  | `clientdll` `replicated` `release` | Force all clients to enable their game instructors. |
| `sv_give_item` | `String` |  |  | `gamedll` `hidden` `replicated` `cheat` `release` `commandline_enforced` | Player's extra item to give |
| `sv_gravity` | `Float32` | `800.000000` |  | `gamedll` `clientdll` `notify` `replicated` `release` | World gravity. |
| `sv_grenade_collision_sphere` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_grenade_collision_sphere_radius` | `Float32` | `2.000000` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_grenade_trajectory_prac_pipreview` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Shows grenade trajectory practice picture-in-picture preview. |
| `sv_grenade_trajectory_prac_trailtime` | `Float32` | `0.000000` | `0.000000 .. 8.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Shows grenade trajectory practice visualization for this number of seconds. |
| `sv_grenade_trajectory_time_spectator` | `Float32` | `0.000000` | `0.000000 .. 8.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Length of time grenade trajectory remains visible as a spectator. |
| `sv_guardian_extra_equipment_ct` | `String` |  |  | `gamedll` `release` `commandline_enforced` | Extra starting equipment for CT players in guardian modes |
| `sv_guardian_extra_equipment_t` | `String` |  |  | `gamedll` `release` `commandline_enforced` | Extra starting equipment for Terrorist players in guardian modes |
| `sv_guardian_refresh_ammo_for_items_on_waves` | `String` |  |  | `gamedll` `release` `commandline_enforced` | List of additional weapons to refill ammo on waves. |
| `sv_guardian_spawn_health_ct` | `Int32` | `100` |  | `gamedll` `release` `commandline_enforced` | Starting health in guardian modes. |
| `sv_guardian_spawn_health_t` | `Int32` | `100` |  | `gamedll` `release` `commandline_enforced` | Starting health in guardian modes. |
| `sv_health_approach_enabled` | `Bool` | `true` |  | `gamedll` `replicated` `release` `commandline_enforced` |  |
| `sv_health_approach_speed` | `Float32` | `10.000000` |  | `gamedll` `replicated` `release` `commandline_enforced` |  |
| `sv_hegrenade_damage_multiplier` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_hegrenade_radius_multiplier` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_hibernate_postgame_delay` | `Float32` | `5.000000` |  | `release` | # of seconds to wait after final client leaves before hibernating. |
| `sv_hibernate_when_empty` | `Bool` | `true` |  | `release` | Puts the server into extremely low CPU usage mode when no clients connected |
| `sv_hide_ent_in_pvs` | `Int32` | `-1` |  | `developmentonly` `gamedll` |  |
| `sv_hide_roundtime_until_seconds` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_highlight_distance` | `Float32` | `500.000000` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_highlight_duration` | `Float32` | `3.500000` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_hitbox_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `sv_hosting_lobby` | `Bool` | `false` |  | `developmentonly` `replicated` |  |
| `sv_hoststate_quit_syscall` | `Bool` | `false` |  | `release` | When enabled, game server will quit immediately via syscall instead of running host states shutdown sequence |
| `sv_human_autojoin_team` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Force human players on to a team. 0 to disable. |
| `sv_ignoregrenaderadio` | `Bool` | `false` |  | `gamedll` `release` `commandline_enforced` | Turn off Fire in the hole messages |
| `sv_infinite_ammo` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `cheat` `release` `commandline_enforced` | Player's active weapon will never run out of ammo |
| `sv_instancebaselines` | `Bool` | `true` |  | `developmentonly` | Enable instanced baselines. Saves network overhead. |
| `sv_invites_only_mainmenu` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | If turned on, will ignore all invites when user is playing a match |
| `sv_jump_impulse` | `Float32` | `301.993378` | `>= 0.000000` | `gamedll` `clientdll` `replicated` `release` | Initial upward velocity for player jumps; sqrt(2*gravity*height). |
| `sv_jump_precision_enable` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` | Enable jump precision. Some game modes benefit from being able to turn this off. |
| `sv_jump_spam_penalty_time` | `Float32` | `0.015625` |  | `gamedll` `clientdll` `replicated` `release` | For subtick jumps, if this much time or less has elapsed since the last time the user has pressed the jump key, pretend they hadn't. Lowering this makes bunnyhopping easier. |
| `sv_kick_ban_duration` | `Float32` | `15.000000` |  | `gamedll` `clientdll` `notify` `replicated` `release` | How long should a kick ban from the server should last (in minutes) |
| `sv_kick_players_with_cooldown` | `Int32` | `1` |  | `gamedll` `replicated` `release` | (0: do not kick on insecure servers; 1: kick players with Untrusted status or convicted by Overwatch; 2: kick players with any cooldown) |
| `sv_kill_players_at_coord_min` | `Bool` | `true` |  | `gamedll` `release` | Kill players with fall damage at negative coord min |
| `sv_ladder_angle` | `Float32` | `-0.707000` | `-1.000000 .. 1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Cos of angle of incidence to ladder perpendicular for applying ladder_dampen |
| `sv_ladder_dampen` | `Float32` | `0.200000` | `0.000000 .. 1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Amount to dampen perpendicular movement on a ladder |
| `sv_ladder_scale_speed` | `Float32` | `0.780000` | `0.000000 .. 1.000000` | `gamedll` `clientdll` `replicated` `release` | Scale top speed on ladders |
| `sv_ladder_slack_z_mult` | `Float32` | `0.026000` |  | `gamedll` `clientdll` `replicated` `cheat` | Difference in Z increases toward the middle of the slack ladder. |
| `sv_lagcomp_filterbyviewangle` | `Bool` | `true` |  | `gamedll` `cheat` | If true, player pawn will filter lag compensation targets by their view angle. |
| `sv_lagcompensationforcerestore` | `Bool` | `true` |  | `gamedll` `cheat` | Don't test validity of a lag comp restore, just do it. |
| `sv_lan` | `Bool` | `false` |  | `release` | Server is a lan server ( no heartbeat, no authentication, no non-class C addresses ) |
| `sv_late_commands_allowed` | `Int32` | `5` |  | `gamedll` `release` | Allow N late commands to run at 0 timescale prior to running an on-time command. Negative values for network round trip based calculation with a hard cap of the of absolute value |
| `sv_legacy_jump` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | Whether or not to use the pre-2026 jump code. |
| `sv_lightquery_debug` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `sv_limit_buyrandom_per_life` | `Bool` | `true` |  | `gamedll` `release` | Enable to limit buyrandom command to only run once per player life |
| `sv_log_http_record_before_any_listeners` | `Bool` | `false` |  | `gamedll` `release` |  |
| `sv_log_onefile` | `Bool` | `false` |  | `archive` `release` | Log server information to only one file. |
| `sv_log_roundstats` | `Bool` | `true` |  | `gamedll` `release` |  |
| `sv_logbans` | `Bool` | `false` |  | `archive` `release` | Log server bans in the server logs. |
| `sv_logblocks` | `Bool` | `false` |  | `release` | If true when log when a query is blocked (can cause very large log files) |
| `sv_logecho` | `Bool` | `true` |  | `archive` `release` | Echo log information to the console. |
| `sv_logfile` | `Bool` | `false` |  | `archive` `release` | Log server information in the log file. |
| `sv_logflush` | `Bool` | `false` |  | `archive` `release` | Flush the log file to disk on each write (slow). |
| `sv_logsdir` | `String` | `logs` |  | `archive` `release` | Folder in the game directory where server logs will be stored. |
| `sv_long_frame_ms` | `Float32` | `0.000000` |  | `developmentonly` `defensive` | If a server frame takes longer than N ms, complain about it.  (Dedicated server only.)  See also engine_frametime_warnings_enable. |
| `sv_mapvetopickvote_maps` | `String` | `de_cache,de_anubis,de_inferno,de_mirage,de_dust2,de_nuke,de_ancient` |  | `gamedll` `release` | Which maps are used for map veto pick sequence |
| `sv_mapvetopickvote_phase_duration` | `String` | `[1:5][2:15][3:20][4:10][5:10][6:5]` |  | `gamedll` `release` | How many seconds each phase lasts |
| `sv_mapvetopickvote_rnd` | `Bool` | `false` |  | `gamedll` `release` | When enabled will shuffle veto pick maps list order every time |
| `sv_massreport` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `sv_matchend_drops_enabled` | `Bool` | `true` |  | `gamedll` `release` | Rewards gameplay time is always accumulated for players, but drops at the end of the match can be prevented |
| `sv_matchpause_auto_5v5` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | When enabled will automatically pause the match at next freeze time if less than 5 players are connected on each team. |
| `sv_matchperfstats_maxclientperfsamples` | `Int32` | `100` |  | `developmentonly` `gamedll` `defensive` | Don't retain more than N perf samples for any given client |
| `sv_max_deathmatch_respawns_per_tick` | `Int32` | `0` |  | `gamedll` `release` `commandline_enforced` |  |
| `sv_max_distance_transmit_footsteps` | `Float32` | `1250.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Maximum distance to transmit footstep sound effects. |
| `sv_max_queries_sec` | `Float32` | `3.000000` |  | `release` | Maximum queries per second to respond to from a single IP address. |
| `sv_max_queries_sec_global` | `Float32` | `60.000000` |  | `release` | Maximum queries per second to respond to from anywhere. |
| `sv_max_queries_window` | `Float32` | `30.000000` |  | `release` | Window over which to average queries per second averages. |
| `sv_max_unreliable_delta_size` | `Int32` | `4096` |  | `developmentonly` `defensive` | Maximum allowable entity delta size over unreliable delivery. |
| `sv_maxclientframes` | `Int32` | `128` |  | `developmentonly` `defensive` |  |
| `sv_maxrate` | `Int32` | `0` | `0 .. 1000000` | `replicated` `release` | Max bandwidth rate allowed on server, 0 == unlimited |
| `sv_maxreplay` | `Float32` | `0.000000` | `0.000000 .. 15.000000` | `developmentonly` `defensive` | Maximum replay time in seconds |
| `sv_maxspeed` | `Float32` | `320.000000` |  | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_maxunlag` | `Float32` | `1.000000` | `0.000000 .. 1.000000` | `gamedll` `clientdll` `replicated` `release` | Maximum lag compensation in seconds |
| `sv_maxunlag_player` | `Float32` | `-1.000000` | `<= 1.000000` | `gamedll` `release` | If &gt;0, maximumum lag compensation used for other human pawns. Applied after sv_maxunlag! |
| `sv_maxuptimelimit` | `Float32` | `0.000000` |  | `gamedll` `release` | Number of hours to operate before trying sv_shutdown. |
| `sv_maxvelocity` | `Float32` | `3500.000000` |  | `gamedll` `clientdll` `replicated` `release` | Maximum speed any ballistically moving object is allowed to attain per axis. |
| `sv_memlimit` | `Int32` | `0` |  | `cheat` `release` | If set, whenever a game ends, if the total memory used by the server is greater than this # of megabytes, the server will exit. |
| `sv_merge_changes_after_tick_with_calcdelta` | `Int32` | `1` |  | `release` | This fixes bugs where pure calcdelta is used due to recipient changing but it doesn't pick up a field change where the value was changed back to same value as the from snapshot even though the destination fields change list does note the change. Set to 2 to spew any changes merged in by this fix. |
| `sv_min_jump_landing_sound` | `Float32` | `260.000000` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_minimum_desired_chicken_count` | `Int32` | `0` |  | `gamedll` `replicated` `release` | Minimum number of chickens to attempt to spawn in the map |
| `sv_minrate` | `Int32` | `5000` | `0 .. 1000000` | `replicated` `release` | Min bandwidth rate allowed on server, 0 == unlimited |
| `sv_mmqueue_reservation` | `String` |  |  | `developmentonly` `dontrecord` | Server queue reservation |
| `sv_mmqueue_reservation_extended_timeout` | `Int32` | `21` | `5 .. 180` | `developmentonly` | Extended time in seconds before mmqueue reservation expires. |
| `sv_mmqueue_reservation_timeout` | `Int32` | `21` | `5 .. 180` | `developmentonly` | Time in seconds before mmqueue reservation expires. |
| `sv_mover_maxslope` | `Float32` | `0.700000` |  | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `defensive` | The maximum slope the player can overcome [-] |
| `sv_mover_pogodampingratio` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `defensive` | The capsule pogo stick damping ratio [-] |
| `sv_mover_pogofrequency` | `Float32` | `10.000000` |  | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `defensive` | The capsule pogo stick frequency [hz]. |
| `sv_mute_players_with_social_penalties` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `sv_networkvar_log_fullchanges` | `Bool` | `false` |  | `developmentonly` `gamedll` | Log FUL_FULL_EDICT_CHANGED calls. |
| `sv_networkvar_perfieldtracking` | `Bool` | `true` |  | `release` | Track individual field offset changes, rather than a single dirty flag for the whole entity. |
| `sv_no_navmesh` | `Bool` | `false` |  | `developmentonly` `gamedll` `cheat` | Block loading of the navmesh. Unplayable, only used for memory sampling. |
| `sv_noclipaccelerate` | `Float32` | `5.000000` |  | `gamedll` `clientdll` `archive` `notify` `replicated` |  |
| `sv_noclipduringpause` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` | If cheats are enabled, then you can noclip with the game paused (for doing screenshots, etc.). |
| `sv_noclipfriction` | `Float32` | `4.000000` |  | `gamedll` `clientdll` `archive` `notify` `replicated` | Friction during noclip move. |
| `sv_noclipspeed` | `Float32` | `1200.000000` |  | `gamedll` `clientdll` `archive` `notify` `replicated` |  |
| `sv_noclipspeedscaleonshift` | `Float32` | `0.500000` |  | `gamedll` `clientdll` `archive` `notify` `replicated` |  |
| `sv_nomvp` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | Disable MVP awards. |
| `sv_nonemesis` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Disable nemesis and revenge. |
| `sv_nowinpanel` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | Turn on/off win panel on server |
| `sv_optimizedmovement` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_outofammo_indicator` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_outofpvsentityupdates` | `Bool` | `false` |  | `developmentonly` |  |
| `sv_override_max_health` | `Int32` | `0` |  | `gamedll` `release` |  |
| `sv_parallel_checktransmit` | `Int32` | `0` |  | `gamedll` `release` | Set to 1 to use threaded checkentities for transmit/pvs on listen servers, 2 for dedicated servers. |
| `sv_parallel_packentities` | `Int32` | `2` |  | `release` | Set to 1 to use threaded snapshot sending on listen servers, 2 for dedicated servers. |
| `sv_parallel_prepare_client_updates` | `Bool` | `false` |  | `developmentonly` |  |
| `sv_parallel_sendsnapshot` | `Int32` | `2` |  | `release` | 0: run all send jobs on main thread; 1: send jobs run asynchronously (except on dedicated server); 2: send jobs asynchronously; 3: send jobs run in parallel but block to not overlap the next tick; 4: main server clients' send jobs run in parallel, then HLTV server jobs; this approximately matches pre-async profile for a single HLTV server configuration |
| `sv_party_mode` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | Party!! |
| `sv_password` | `String` |  |  | `protected` `notify` `dontrecord` `release` | Server password for entry into multiplayer games |
| `sv_pausable` | `Int32` | `0` |  | `release` | Is the server pausable. |
| `sv_pausable_dev` | `Bool` | `true` |  | `developmentonly` | Whether listen server is pausable when running -dev and playing solo against bots |
| `sv_pausable_dev_ds` | `Bool` | `false` |  | `developmentonly` | Whether dedicated server is pausable when running -dev and playing solo against bots |
| `sv_pause_on_console_open` | `Bool` | `false` |  | `archive` | 1 = Pause the game when pressing ~ to open the console. CTRL+~ opens the console without pause. |
| `sv_pause_on_tick` | `Int32` | `0` |  | `developmentonly` `gamedll` `replicated` `cheat` | Tick count to pause on |
| `sv_phys_animated_hierarchy` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `sv_phys_async_buoyancy_update` | `Bool` | `false` |  | `developmentonly` `gamedll` `replicated` `defensive` | If true, server buoyancy motion controllers are updated in an async job after the tick has completed. |
| `sv_phys_debug_callback_entities` | `Bool` | `false` |  | `gamedll` `cheat` | Print all entities that get touch callbacks. Each entity is printed only once. |
| `sv_phys_enabled` | `Bool` | `true` |  | `gamedll` `cheat` | Enable all physics simulation |
| `sv_phys_sleep_enable` | `Bool` | `true` |  | `gamedll` `cheat` | Enable sleeping for dynamic physics bodies. |
| `sv_phys_sound_disable_impact_sounds_under_hard_threshold` | `Bool` | `false` |  | `gamedll` `cheat` | if true, impact sounds wont play if no soft impact sound is present and the impact is below the hard velocity threshold. |
| `sv_phys_stop_at_collision` | `String` |  |  | `gamedll` `cheat` |  |
| `sv_phys_visualize_awake` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `sv_player_search_range` | `Float32` | `64.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sv_playerradio_use_allowlist` | `Bool` | `true` |  | `gamedll` `release` | playerradio commands may only use responses from an allow list of commands. |
| `sv_predictable_damage_tag_ticks` | `Int32` | `2` |  | `gamedll` `release` | Delay player slowdown when damaged by # ticks to reduce misprediction effects |
| `sv_prime_accounts_only` | `Bool` | `false` |  | `gamedll` `release` | When this setting is enabled only prime users can connect to this game server. |
| `sv_pushaway_clientside` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Clientside physics push away (0=off, 1=only localplayer, 1=all players) |
| `sv_pushaway_clientside_size` | `Float32` | `15.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Minimum size of pushback objects |
| `sv_pushaway_force` | `Float32` | `300000.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | How hard physics objects are pushed away from the players on the server. |
| `sv_pushaway_hostage_force` | `Float32` | `20000.000000` |  | `gamedll` `replicated` `cheat` | How hard the hostage is pushed away from physics objects (falls off with inverse square of distance). |
| `sv_pushaway_max_force` | `Float32` | `2000.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Maximum amount of force applied to physics objects by players. |
| `sv_pushaway_max_hostage_force` | `Float32` | `1000.000000` |  | `gamedll` `replicated` `cheat` | Maximum of how hard the hostage is pushed away from physics objects. |
| `sv_pushaway_max_player_force` | `Float32` | `20.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Maximum of how hard the player is pushed away from physics objects. |
| `sv_pushaway_min_player_speed` | `Float32` | `75.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | If a player is moving slower than this, don't push away physics objects (enables ducking behind things). |
| `sv_pushaway_player_force` | `Float32` | `450.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | How hard the player is pushed away from physics objects (falls off with inverse square of distance). |
| `sv_pvs_cache_query_inflate_amount` | `Int32` | `0` |  | `developmentonly` `gamedll` |  |
| `sv_pvs_entity` | `Int32` | `-1` |  | `developmentonly` `gamedll` `defensive` | If set, only allows this ent index to network (other than players and things that force sending). |
| `sv_pvs_max_distance` | `Float32` | `0.000000` |  | `replicated` `release` | if set, adds a maximum range to PVS/PAS checks |
| `sv_pvs_random` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | If set, objects blink in/out of pvs randomly. |
| `sv_pvs_shadows_include_env` | `Bool` | `false` |  | `gamedll` `replicated` `release` |  |
| `sv_quantize_movement_input` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` | Quantize movement input values. Enabling this restricts players from using analog input to move at fractional speeds normally impossible with digital button input. |
| `sv_radio_throttle_window` | `Float32` | `10.000000` |  | `gamedll` `release` | The number of seconds before radio command tokens refresh. |
| `sv_ragdoll_lru_debug` | `Bool` | `false` |  | `gamedll` `replicated` `cheat` |  |
| `sv_rcon_banpenalty` | `Int32` | `0` | `>= 0` | `developmentonly` `defensive` | Number of minutes to ban users who fail rcon authentication |
| `sv_rcon_log` | `Bool` | `true` |  | `developmentonly` `defensive` | Enable/disable rcon logging. |
| `sv_rcon_maxfailures` | `Int32` | `10` | `1 .. 20` | `developmentonly` `defensive` | Max number of times a user can fail rcon authentication before being banned |
| `sv_rcon_minfailures` | `Int32` | `5` | `1 .. 20` | `developmentonly` `defensive` | Number of times a user can fail rcon authentication in sv_rcon_minfailuretime before being banned |
| `sv_rcon_minfailuretime` | `Float32` | `30.000000` | `>= 1.000000` | `developmentonly` `defensive` | Number of seconds to track failed rcon authentications |
| `sv_record_item_time_data` | `Bool` | `false` |  | `gamedll` `release` | Turn on recording of per player item time data into the server log. |
| `sv_recvbuf_messages` | `Int32` | `1024` |  | `developmentonly` `defensive` | Max number of messages that can be queued in a netchan receive buffer for an ordinary connection from a client. |
| `sv_regeneration_force_on` | `Bool` | `false` |  | `gamedll` `cheat` | Cheat to test regenerative health systems |
| `sv_regeneration_wait_time` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `sv_region` | `Int32` | `-1` |  | `release` | The region of the world to report this server in. |
| `sv_reliableavatardata` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | Use server overrides for steam avatars |
| `sv_remapper_loopsoundfix` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sv_remapper_range_multiplier` | `Float32` | `1.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sv_remove_ent_from_pvs` | `Int32` | `0` |  | `developmentonly` `gamedll` |  |
| `sv_replay_group_id` | `Int32` | `0` |  | `release` | The replay group that this server will be uploading files to |
| `sv_replaysdir` | `String` | `replays` |  | `developmentonly` `defensive` | Directory to store replays in |
| `sv_reserve_slots_for_reconnecting_players_kick_prior` | `Bool` | `true` |  | `developmentonly` `defensive` | Kick a previously connected player with the same steamID if a replacement comes along |
| `sv_rollangle` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` `clientdll` `notify` `replicated` | Max view roll angle |
| `sv_rollspeed` | `Float32` | `200.000000` |  | `developmentonly` `gamedll` `clientdll` `notify` `replicated` |  |
| `sv_runcmds` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `sv_script_think_interval` | `Float32` | `0.100000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sv_search_key` | `String` |  |  | `release` |  |
| `sv_search_team_key` | `String` | `public` |  | `release` | When initiating team search, set this key to match with known opponents team |
| `sv_sellback_enabled` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` | Determines whether players can undo purchases in the buy menu |
| `sv_sendtables` | `Int32` | `1` |  | `developmentonly` | Force full sendtable sending path. |
| `sv_sequence_debug` | `Int32` | `-1` |  | `developmentonly` `gamedll` `defensive` |  |
| `sv_sequence_debug2` | `Int32` | `-1` |  | `developmentonly` `gamedll` `defensive` |  |
| `sv_sequence_model_substring` | `String` |  |  | `developmentonly` `gamedll` `defensive` |  |
| `sv_server_graphic1` | `String` |  |  | `gamedll` `clientdll` `replicated` `release` | A 360x60 (&lt;16kb) image file in /csgo/ that will be displayed to spectators. |
| `sv_server_graphic2` | `String` |  |  | `gamedll` `clientdll` `replicated` `release` | A 220x45 (&lt;16kb) image file in /csgo/ that will be displayed to spectators. |
| `sv_server_verify_blood_on_player` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `sv_shared_team_pvs` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | PVS is shared between teams |
| `sv_show_bot_difficulty_in_name` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | 0 = hide bot difficulty in bot name, 1 = show bot difficulty in bot name |
| `sv_show_move_collisions` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` | Enable this to visualize collisions between player and geometry. |
| `sv_show_team_equipment_force_on` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Force on if not prohibited |
| `sv_show_team_equipment_prohibit` | `Bool` | `false` |  | `gamedll` `clientdll` `notify` `replicated` `release` | Determines whether +cl_show_team_equipment is prohibited. |
| `sv_show_teammate_death_notification` | `Bool` | `false` |  | `gamedll` `release` | Show chat notification upon teammate death |
| `sv_show_voip_indicator_for_enemies` | `Bool` | `false` |  | `gamedll` `replicated` `release` | Makes it so the voip icon is shown over enemies as well as allies when they are talking |
| `sv_showbullethits` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` | 1=show hits and near misses, 2=show hits only |
| `sv_showhitregistration` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `cheat` | Display lag_compensated hitboxes. 0 = off, 1 = server only, 2 = client only, 3 = both server and client |
| `sv_showimpacts` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` | Shows client (red) and server (blue) bullet impact point (1=both, 2=client-only, 3=server-only) |
| `sv_showimpacts_penetration` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` | Shows extra data when bullets penetrate. (use sv_showimpacts_time to increase time shown) |
| `sv_showimpacts_time` | `Float32` | `4.000000` | `0.000000 .. 10.000000` | `gamedll` `clientdll` `replicated` `release` | Duration bullet impact indicators remain before disappearing |
| `sv_showladders` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | Show bbox and dismount points for all ladders (must be set before level load.) |
| `sv_showlagcompensation_rec` | `Float32` | `0.000000` |  | `developmentonly` `gamedll` | If &gt; 0, show lag compensation hitboxes as they're recorded. Value is for how long. |
| `sv_showplayerhitboxes` | `Int32` | `0` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Show lag compensated hitboxes for the specified player index whenever a player fires. |
| `sv_shutdown_immediately_on_request` | `Bool` | `false` |  | `developmentonly` `defensive` | The server will always shutdown on receiving the shutdown request, even if not hibernating |
| `sv_skel_constraints_enable` | `Bool` | `false` |  | `replicated` `cheat` |  |
| `sv_skip_update_animations` | `Bool` | `false` |  | `developmentonly` `gamedll` | Enable to skip game animations |
| `sv_skirmish_id` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` | Dedicated server skirmish id to run |
| `sv_skyname` | `String` | `sky_urb01` |  | `gamedll` `clientdll` `archive` `replicated` | Current name of the skybox texture |
| `sv_smoke_volume_blind_start` | `Float32` | `0.200000` |  | `developmentonly` `clientdll` |  |
| `sv_snapshot_unlimited` | `Bool` | `false` |  | `replicated` `release` | For debugging, don't throw away old snapshots so that if you break in debugger (on remote client or server) it won't require an uncompressed update to resume.  You may run out of memory of course... |
| `sv_sniper_tracer_innacuracy` | `Float32` | `0.085000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | How inaccurate a sniper shot can be before we trip sv_sniper_tracer_mode behavior. |
| `sv_sniper_tracer_innacuracy_length` | `Float32` | `200.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | How far should the tracer draw if we trip sv_sniper_tracer_mode behavior. |
| `sv_sniper_tracer_mode` | `Int32` | `1` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Mode for sniper tracers. 0: legacy, 1: hide when more than sv_sniper_tracer_innacuracy inaccurate. |
| `sv_spawn_afk_bomb_drop_time` | `Float32` | `15.000000` |  | `gamedll` `replicated` `release` | Players that have never moved since they spawned will drop the bomb after this amount of time. |
| `sv_spec_hear` | `Int32` | `3` |  | `gamedll` `clientdll` `notify` `replicated` `release` | Determines who spectators can hear: 0: only spectators; 1: all players; 2: spectated team; 3: self only; 4: nobody |
| `sv_spec_use_tournament_content_standards` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_specaccelerate` | `Float32` | `5.000000` |  | `gamedll` `clientdll` `archive` `notify` `replicated` |  |
| `sv_specnoclip` | `Bool` | `true` |  | `gamedll` `clientdll` `archive` `notify` `replicated` |  |
| `sv_specspeed` | `Float32` | `1200.000000` |  | `gamedll` `clientdll` `archive` `notify` `replicated` |  |
| `sv_staminajumpcost` | `Float32` | `0.080000` | `>= 0.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | sv_legacy_jump only: Stamina penalty for jumping |
| `sv_staminalandcost` | `Float32` | `0.050000` | `>= 0.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | sv_legacy_jump only: Stamina penalty for landing |
| `sv_staminamax` | `Float32` | `80.000000` | `0.000000 .. 100.000000` | `gamedll` `clientdll` `replicated` `release` | Maximum stamina penalty |
| `sv_staminarecoveryrate` | `Float32` | `60.000000` | `>= 0.000000` | `gamedll` `clientdll` `replicated` `release` | Rate at which stamina recovers (units/sec) |
| `sv_standable_normal` | `Float32` | `0.700000` |  | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_stats` | `Bool` | `true` |  | `developmentonly` `defensive` | Collect CPU usage stats |
| `sv_steamauth_correct` | `Bool` | `false` |  | `release` | Correct behavior |
| `sv_steamauth_enforce` | `Int32` | `2` |  | `release` | By default, player must maintain a reliable connection to Steam servers. When player Steam session drops, enforce it: 2 = instantly kick, 1 = kick at next spawn, 0 = do not kick. |
| `sv_steamauth_ignore_localhost` | `Bool` | `true` |  | `release` | Ignore VAC and auth errors for client connected via localhost address or in-engine loopback |
| `sv_steamgroup` | `String` |  |  | `notify` `release` | The ID of the steam group that this server belongs to. You can find your group's ID on the admin profile page in the steam community. |
| `sv_steamgroup_exclusive` | `Bool` | `false` |  | `release` | If set, only members of Steam group will be able to join the server when it's empty, public people will be able to join the server only if it has players. |
| `sv_step_move_vel_min` | `Float32` | `64.000000` |  | `gamedll` `clientdll` `replicated` `cheat` | Min velocity for step move. |
| `sv_stepsize` | `Float32` | `18.000000` |  | `developmentonly` `gamedll` `clientdll` `notify` `replicated` |  |
| `sv_stopspeed` | `Float32` | `80.000000` |  | `gamedll` `clientdll` `notify` `replicated` `release` | Minimum stopping speed when on ground. |
| `sv_strafing_inaccuracy_bias` | `Float32` | `0.500000` |  | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_strafing_inaccuracy_enabled` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_strafing_inaccuracy_scale` | `Float32` | `0.100000` |  | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_stressbots` | `Bool` | `false` |  | `release` | If set to 1, the server calculates data and fills packets to bots. Used for perf testing. |
| `sv_strict_notarget` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | If set, notarget will cause entities to never think they are in the pvs |
| `sv_subtick_movement_view_angles` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` | Whether or not subtick view angles are taken into account during movement. |
| `sv_suppress_friendlyfire_decals` | `Bool` | `true` |  | `developmentonly` `gamedll` |  |
| `sv_suppress_viewpunch` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` |  |
| `sv_surf_sounds` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` | Should we try to play sounds for surf? |
| `sv_tags` | `String` |  |  | `notify` `release` | Server tags. Used to provide extra information to clients when they're browsing for servers. Separate tags with a comma. |
| `sv_talk_after_dying_time` | `Float32` | `0.000000` |  | `gamedll` `clientdll` `replicated` `release` | The number of seconds a player can continue talking after dying as if they were still alive |
| `sv_talk_enemy_dead` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Dead players can hear all dead enemy communication (voice, chat) |
| `sv_talk_enemy_living` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Living players can hear all living enemy communication (voice, chat) |
| `sv_teamid_overhead` | `Bool` | `true` |  | `gamedll` `clientdll` `notify` `replicated` `release` | Shows teamID over player's heads.  0 = off, 1 = on |
| `sv_teamid_overhead_always_prohibit` | `Bool` | `false` |  | `gamedll` `clientdll` `notify` `replicated` `release` | Determines whether cl_teamid_overhead_always is prohibited. |
| `sv_teamid_overhead_maxdist` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If &gt;0, server will override cl_teamid_overhead_maxdist |
| `sv_teamid_overhead_maxdist_spec` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If &gt;0, server will override cl_teamid_overhead_maxdist_spec |
| `sv_temp_baseline_string_table_buffer_size` | `Int32` | `524288` |  | `developmentonly` `defensive` | Buffer size for writing string table baselines |
| `sv_tick_parallel_with_client` | `Bool` | `false` |  | `developmentonly` | Runs the final server tick of the frame in parallel with client work |
| `sv_tick_snapshot_sort_entities` | `Bool` | `true` |  | `developmentonly` |  |
| `sv_timebetweenducks` | `Float32` | `0.400000` | `0.000000 .. 2.000000` | `gamedll` `clientdll` `replicated` `release` | Minimum time before recognizing consecutive duck key |
| `sv_timeout` | `Float32` | `20.000000` |  | `developmentonly` `defensive` | After this many seconds without a message from fully connected client, the client is dropped |
| `sv_turbophysics` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Turns on turbo physics |
| `sv_turning_inaccuracy_angle_min` | `Float32` | `4.000000` |  | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_turning_inaccuracy_decay` | `Float32` | `0.800000` |  | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_turning_inaccuracy_enabled` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_unlag` | `Bool` | `true` |  | `developmentonly` `gamedll` | Enables player lag compensation |
| `sv_unlag_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `sv_unlag_fixstuck` | `Bool` | `false` |  | `developmentonly` `gamedll` | Disallow backtracking a player for lag compensation if it will cause them to become stuck |
| `sv_unlockedchapters` | `Int32` | `1` |  | `archive` | Highest unlocked game chapter. |
| `sv_unpause_on_console_close` | `Bool` | `false` |  | `archive` | 1 = Unpause the game when pressing ~ to close the console. 0 = Leave the game paused. |
| `sv_use_hi_pri_context_switch_time` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `release` | +use search behaves as though high priority items are usable for this long after they become unusable to avoid players accidentally performing a different action. |
| `sv_use_playercache` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` | Cache off player bounds for traces. |
| `sv_use_pvs_cache` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `sv_usenetworkvars` | `Bool` | `true` |  | `developmentonly` `defensive` | Use networkvar system. |
| `sv_usercmd_custom_random_seed` | `Bool` | `false` |  | `gamedll` `release` | When enabled server will populate an additional random seed independent of the client |
| `sv_usercmd_execute_warning_ms` | `Float32` | `5.000000` |  | `gamedll` `archive` | Emit a warning if we spend more than N ms executing user commands for a single player |
| `sv_vac_webapi_auth_key` | `String` |  |  | `gamedll` `release` | Key for when posting to vac related webapis. |
| `sv_versus_screen_scene_id` | `Int32` | `0` |  | `gamedll` `release` `commandline_enforced` | Determines which scene is used for the versus screen. |
| `sv_visiblemaxplayers` | `Int32` | `-1` |  | `release` | Overrides the max players reported to prospective clients |
| `sv_voice_proximity` | `Float32` | `-1.000000` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_voicecodec` | `String` | `vaudio_speex` |  | `release` | Specifies which voice codec DLL to use in a game. Set to the name of the DLL without the extension. |
| `sv_voiceenable` | `Bool` | `true` |  | `archive` `notify` `release` |  |
| `sv_vote_allow_in_warmup` | `Bool` | `false` |  | `gamedll` `release` | Allow voting during warmup? |
| `sv_vote_allow_spectators` | `Bool` | `false` |  | `gamedll` `release` | Allow spectators to initiate votes? |
| `sv_vote_command_delay` | `Float32` | `2.000000` | `<= 4.500000` | `gamedll` `release` | How long after a vote passes until the action happens |
| `sv_vote_count_spectator_votes` | `Bool` | `false` |  | `gamedll` `release` | Allow spectators to vote on issues? |
| `sv_vote_creation_timer` | `Float32` | `120.000000` |  | `gamedll` `release` | How often someone can individually call a vote. |
| `sv_vote_disallow_kick_on_match_point` | `Bool` | `false` |  | `gamedll` `release` | Disallow vote kicking on the match point round. |
| `sv_vote_failure_timer` | `Float32` | `300.000000` |  | `gamedll` `release` | A vote that fails cannot be re-submitted for this long |
| `sv_vote_issue_changelevel_allowed` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Can people hold votes to change levels? |
| `sv_vote_issue_kick_allowed` | `Bool` | `true` |  | `gamedll` `notify` `replicated` `release` | Can people hold votes to kick players from the server? |
| `sv_vote_issue_loadbackup_allowed` | `Bool` | `true` |  | `gamedll` `notify` `replicated` `release` | Can people hold votes to load match from backup? |
| `sv_vote_issue_loadbackup_spec_authoritative` | `Bool` | `false` |  | `gamedll` `release` | When enabled, admins load match from backup without players vote |
| `sv_vote_issue_loadbackup_spec_only` | `Bool` | `false` |  | `gamedll` `notify` `replicated` `release` | When enabled, only admins load match from backup |
| `sv_vote_issue_loadbackup_spec_safe` | `Bool` | `true` |  | `gamedll` `release` | When enabled, admins load match from backup in safe time of the round only |
| `sv_vote_issue_matchready_allowed` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Can people hold votes to ready/unready the match? |
| `sv_vote_issue_nextlevel_allowed` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Can people hold votes to set the next level? |
| `sv_vote_issue_nextlevel_allowextend` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Allow players to extend the current map? |
| `sv_vote_issue_nextlevel_choicesmode` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Present players with a list of lowest playtime maps to choose from? |
| `sv_vote_issue_nextlevel_prevent_change` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Not allowed to vote for a nextlevel if one has already been set. |
| `sv_vote_issue_pause_match_allowed` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Can people hold votes to pause/unpause the match? |
| `sv_vote_issue_pause_match_spec_only` | `Bool` | `false` |  | `gamedll` `notify` `replicated` `release` | When enabled, only admins start technical pause |
| `sv_vote_issue_restart_game_allowed` | `Bool` | `false` |  | `gamedll` `release` | Can people hold votes to restart the game? |
| `sv_vote_issue_scramble_teams_allowed` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | Can people hold votes to scramble the teams? |
| `sv_vote_issue_surrrender_allowed` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Can people hold votes to surrender? |
| `sv_vote_issue_swap_teams_allowed` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | Can people hold votes to swap the teams? |
| `sv_vote_issue_timeout_allowed` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Can people hold votes to time out? |
| `sv_vote_kick_ban_duration` | `Float32` | `15.000000` |  | `gamedll` `notify` `replicated` `release` | How long should a kick vote ban someone from the server? (in minutes) |
| `sv_vote_quorum_ratio` | `Float32` | `0.501000` | `0.010000 .. 1.000000` | `gamedll` `release` | The minimum ratio of players needed to vote on an issue to resolve it. |
| `sv_vote_timer_duration` | `Float32` | `15.000000` |  | `gamedll` `release` | How long to allow voting on an issue |
| `sv_vote_to_changelevel_before_match_point` | `Bool` | `false` |  | `gamedll` `replicated` `release` `commandline_enforced` | Restricts vote to change level to rounds prior to match point (default 0, vote is never disallowed) |
| `sv_vote_to_changelevel_rndmin` | `Int32` | `0` |  | `gamedll` `replicated` `release` `commandline_enforced` | When non-zero, restricts vote to change level to this many first rounds or minutes of the match (default 0, vote is not disallowed) |
| `sv_walkable_normal` | `Float32` | `0.700000` |  | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_warmup_to_freezetime_delay` | `Int32` | `4` | `3 .. 20` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Delay between end of warmup and start of match. |
| `sv_water_slow_amount` | `Float32` | `0.900000` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_wateraccelerate` | `Float32` | `10.000000` |  | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_waterdist` | `Float32` | `12.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` | Vertical view fixup when eyes are near water plane. |
| `sv_waterfriction` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_weapon_require_use_grace_period` | `Float32` | `1.000000` |  | `gamedll` `release` |  |
| `sv_weapon_swap_difficulty_near_hi_pri` | `Int32` | `2` |  | `gamedll` `clientdll` `replicated` `release` | 0 = Cone searches easily reach past high priority items to swap weapons. 1 = Cone searches are narrowed and require that the weapon is strictly closer. 2 = cone searches are disabled near high priority items |
| `sv_workshop_allow_other_maps` | `Bool` | `true` |  | `gamedll` `release` | When hosting a workshop collection, users can play other workshop map on this server when it is empty and then mapcycle into this server collection. |
| `sv_workshop_map_save_data_max_filesize_mb` | `Int32` | `1` |  | `gamedll` `release` `commandline_enforced` |  |
| `sys_minidumpexpandedspew` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `sys_minidumpspewlines` | `Int32` | `2000` |  | `release` | Lines of crash dump console spew to keep. |
| `target_scan_use_query_cache` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` |  |
| `teleport_trigger_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `testscript_debug` | `Bool` | `false` |  | `developmentonly` `defensive` | Debug test scripts. |
| `think_limit` | `Float32` | `10.000000` |  | `gamedll` `clientdll` `replicated` `release` | Maximum think time in milliseconds, warning is printed if this is exceeded. |
| `thread_pool_option` | `Int32` | `-1` |  | `hidden` `release` | Thread pool option |
| `throttle_expensive_ai` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `timedemo_end` | `String` | `-1` |  | `release` | Ends timedemo on given tick. |
| `timedemo_start` | `String` | `-1` |  | `release` | Starts timedemo on given tick. |
| `toast_manager_override_duration` | `Float32` | `-1.000000` |  | `developmentonly` `clientdll` |  |
| `tool_spawned_model_scales` | `Vector3` | `1.000000 1.000000 1.000000` |  | `developmentonly` `gamedll` `replicated` |  |
| `tools_stall_monitor_break_on_unknown_cause` | `Bool` | `false` |  | `developmentonly` | Break on unknown stall cause |
| `trigger_fan_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `trigger_fan_player_windblock_debug` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `trusted_launch` | `Int32` | `0` |  | `clientdll` `archive` | Trusted launch status |
| `tv_advertise_watchable` | `Bool` | `false` |  | `protected` `notify` `dontrecord` `release` | GOTV advertises the match as watchable via game UI, clients watching via UI will not need to type password |
| `tv_allow_autorecording_index` | `Int32` | `-1` |  | `gamedll` `release` | When &gt;=0 restricts autorecording only to the specified TV index |
| `tv_allow_camera_man` | `Bool` | `true` |  | `developmentonly` `gamedll` `defensive` | Auto director allows spectators to become camera man |
| `tv_allow_camera_man_steamid` | `UInt64` | `0` |  | `gamedll` `release` | Allows tournament production cameraman to run csgo.exe -interactivecaster on SteamID 7650123456XXX and be the camera man. |
| `tv_allow_camera_man_steamid2` | `UInt64` | `0` |  | `gamedll` `release` | Allows tournament production tv cameraman to run csgo.exe -interactivecaster on SteamID 7650123456XXX and be the tv camera man. |
| `tv_allow_static_shots` | `Bool` | `true` |  | `gamedll` `release` | Auto director uses fixed level cameras for shots |
| `tv_autorecord` | `Bool` | `false` |  | `release` | Automatically records all games as SourceTV demos. |
| `tv_autoretry` | `Bool` | `true` |  | `release` | Relay proxies retry connection after network timeout |
| `tv_broadcast` | `Bool` | `false` |  | `release` | Automatically broadcasts all games as GOTV demos through Steam. |
| `tv_broadcast1` | `Bool` | `false` |  | `release` | Automatically broadcasts all games as GOTV[1] demos through Steam. |
| `tv_broadcast_drop_fragments` | `Int32` | `0` |  | `hidden` `release` | Drop every Nth fragment |
| `tv_broadcast_keyframe_interval` | `Float32` | `3.000000` |  | `release` | The frequency, in seconds, of sending keyframes and delta fragments to the broadcast relay server |
| `tv_broadcast_keyframe_interval1` | `Float32` | `3.000000` |  | `release` | The frequency, in seconds, of sending keyframes and delta fragments to the broadcast1 relay server |
| `tv_broadcast_max_requests` | `Int32` | `20` |  | `release` | Max number of broadcast http requests in flight. If there is a network issue, the requests may start piling up, degrading server performance. If more than the specified number of requests are in flight, the new requests are dropped. |
| `tv_broadcast_max_requests1` | `Int32` | `20` |  | `release` | Max number of broadcast1 http requests in flight. If there is a network issue, the requests may start piling up, degrading server performance. If more than the specified number of requests are in flight, the new requests are dropped. |
| `tv_broadcast_origin_auth` | `String` | `gocastauth` |  | `hidden` `release` | X-Origin-Auth header of the broadcast POSTs |
| `tv_broadcast_origin_auth1` | `String` | `gocastauth` |  | `hidden` `release` | X-Origin-Auth header of the broadcast1 POSTs |
| `tv_broadcast_origin_delay` | `Float32` | `0.000000` |  | `hidden` `release` | Injection delay request for CDN rebroadcast frameworks, seconds |
| `tv_broadcast_spew_threshold` | `Float32` | `0.100000` |  | `release` | The threshold, in seconds, that we'll spew about the snapshot tick |
| `tv_broadcast_startup_resend_interval` | `Float32` | `10.000000` |  | `release` | The interval, in seconds, of re-sending startup data to the broadcast relay server (useful in case relay crashes, restarts or startup data http request fails) |
| `tv_broadcast_terminate` | `Bool` | `true` |  | `hidden` `release` | Terminate every broadcast with a stop command |
| `tv_broadcast_url` | `String` | `http://localhost:8080` |  | `release` | URL of the broadcast relay |
| `tv_broadcast_url1` | `String` | `http://localhost:8080` |  | `release` | URL of the broadcast relay1 |
| `tv_chatgroupsize` | `Int32` | `0` |  | `release` | Set the default chat group size |
| `tv_chattimelimit` | `Float32` | `0.200000` |  | `release` | Limits spectators to chat only every n seconds |
| `tv_debug` | `Int32` | `0` |  | `release` | SourceTV debug info. |
| `tv_delay` | `Int32` | `120` | `0 .. 960` | `gamedll` `release` `commandline_enforced` | SourceTV broadcast delay in seconds |
| `tv_delay1` | `Int32` | `15` | `0 .. 960` | `gamedll` `release` `commandline_enforced` | SourceTV[instance 1] broadcast delay in seconds |
| `tv_delaymapchange` | `Bool` | `true` |  | `gamedll` `release` | Delays map change until broadcast is complete |
| `tv_deltacache` | `Int32` | `2` |  | `release` | Enable delta entity bit stream cache |
| `tv_demo_starttick` | `Int32` | `0` |  | `developmentonly` `defensive` |  |
| `tv_dispatchmode` | `Int32` | `1` |  | `release` | Dispatch clients to relay proxies: 0=never, 1=if appropriate, 2=always |
| `tv_enable` | `Bool` | `false` |  | `notify` `release` | Activates SourceTV on server. |
| `tv_enable1` | `Bool` | `false` |  | `notify` `release` | Activates SourceTV[1] on server. |
| `tv_enable_delta_frames` | `Bool` | `true` |  | `release` | Indicates whether or not the tv should use delta frames for storage of intermediate frames. This takes more CPU but significantly less memory. |
| `tv_enable_dynamic` | `Bool` | `false` |  | `notify` `release` | When enabled, changes in tv_enable convars cause immediate startup or shutdown of hltv server |
| `tv_extended_logging` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `tv_grouprelaydatareliable` | `Bool` | `false` |  | `developmentonly` `defensive` | When enabled, this will collect all information for relay sending into a single datagram to ensure that the data stays together through a potentially large number of relays |
| `tv_grouprelaydataunreliable` | `Bool` | `false` |  | `developmentonly` `defensive` | When enabled, this will collect all information for relay sending into a single datagram to ensure that the data stays together through a potentially large number of relays |
| `tv_grouprelaydatavoice` | `Bool` | `false` |  | `developmentonly` `defensive` | Similar to tv_grouprelaydata, but controls whether or not the voice channels should be routed into the grouped data for the relays |
| `tv_include_usercommands` | `Bool` | `true` |  | `gamedll` `release` | HLTV streams will include player usercommands each tick |
| `tv_instant_replay_full_frame` | `Bool` | `true` |  | `developmentonly` `defensive` | Send embedded full frames |
| `tv_instant_replay_full_frame_build_threaded` | `Bool` | `false` |  | `developmentonly` `defensive` | Build the full frames on a seperate job thread |
| `tv_instant_replay_full_frame_time` | `Int32` | `30` |  | `developmentonly` `defensive` | Seconds between full frame embeddeds |
| `tv_listen_voice_indices` | `Int32` | `0` |  | `clientdll` `userinfo` | Bitfield of playerslots to listen to voice messages from when connected to SourceTV, default is none |
| `tv_listen_voice_indices_h` | `Int32` | `0` |  | `clientdll` `userinfo` | High 32 bits of bitfield of playerslots to listen to voice messages from when connected to SourceTV, default is none |
| `tv_log_director_events` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` | Log game events being considered by the director |
| `tv_maxclients` | `Int32` | `128` | `0 .. 255` | `release` | Maximum client number on SourceTV server. |
| `tv_maxclients_relayreserved` | `Int32` | `0` | `0 .. 255` | `release` | This number of relay client connections are reserved for SourceTV relays. |
| `tv_maxrate` | `Int32` | `0` |  | `release` | Max SourceTV spectator bandwidth rate allowed, 0 == unlimited |
| `tv_name` | `String` | `SourceTV` |  | `release` | SourceTV host name |
| `tv_nochat` | `Bool` | `false` |  | `archive` `userinfo` | Don't receive chat messages from other SourceTV spectators |
| `tv_overridemaster` | `Bool` | `false` |  | `release` | Overrides the SourceTV master root address. |
| `tv_password` | `String` |  |  | `protected` `notify` `dontrecord` `release` | SourceTV password for all clients of CSTV[0] |
| `tv_password1` | `String` |  |  | `protected` `notify` `dontrecord` `release` | SourceTV password for all clients of CSTV[1]. If empty, tv_password is used |
| `tv_playcast_delay_prediction` | `Bool` | `true` |  | `release` |  |
| `tv_playcast_delay_resync` | `Float32` | `0.000000` |  | `release` | To alleviate intermittent network connectivity problems, this is the number of seconds to wait before actually re-syncing the stream after failure |
| `tv_playcast_fragment_cache_history_length` | `Float32` | `120.000000` |  | `release` | How far back before our current playback head in seconds to hold onto fragments. |
| `tv_playcast_http_delta_fragment_timeout_s` | `Int32` | `3` |  | `hidden` `release` |  |
| `tv_playcast_max_rcvage` | `Float32` | `15.000000` |  | `hidden` `release` |  |
| `tv_playcast_max_rtdelay` | `Float32` | `300.000000` |  | `hidden` `release` |  |
| `tv_playcast_origin_auth` | `String` |  |  | `hidden` `release` | Get request X-Origin-Auth string |
| `tv_playcast_retry_timeout` | `Float32` | `25.000000` |  | `release` | In case of intermittent network problems, how long should playcast retry fragment retrieval before resorting to resync |
| `tv_playcast_showerrors` | `String` |  |  | `hidden` `release` | Set to display headers upon error (e.g. "CF-Ray,CF-Cache-Status,Body" ) |
| `tv_playcast_slow_playback_when_fragment_requests_fail` | `Bool` | `true` |  | `hidden` `release` | Whether or not we slow playback rate if we start running out of buffered stream fragments. |
| `tv_port` | `Int32` | `27020` |  | `release` | Host SourceTV[0] port |
| `tv_port1` | `Int32` | `27021` |  | `release` | Host SourceTV[1] port |
| `tv_rate_multiplier` | `Float32` | `2.000000` |  | `developmentonly` `defensive` | Multiply requested rate by this value to adjust Dota TV send rate |
| `tv_record_immediate` | `Int32` | `0` |  | `release` | tv_record starting the moment tv_record was executed, not tv_delay earlier |
| `tv_relay_hard_shutdown` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `tv_relay_quit_after_game` | `Bool` | `true` |  | `developmentonly` `defensive` | Quit after a game has been relayed, do not hibernate |
| `tv_relay_rate` | `Int32` | `500000` |  | `developmentonly` `defensive` | default rate for relays |
| `tv_relay_secret_code` | `Bool` | `true` |  | `developmentonly` `defensive` | When enabled, this will use a uniquely generated server code to authenticate relay to relay connections. This code is coordinated via the GC or some external means rather than by clients directly |
| `tv_relaypassword` | `String` |  |  | `protected` `notify` `dontrecord` `release` | SourceTV password for relay proxies |
| `tv_relayradio` | `Bool` | `false` |  | `gamedll` `release` | Relay team radio commands to TV: 0=off, 1=on |
| `tv_relayvoice` | `Bool` | `true` |  | `release` | Relay voice data: 0=off, 1=on |
| `tv_secret_code` | `Bool` | `true` |  | `developmentonly` `defensive` | When enabled, this will use a uniquely generated server code to authenticate relay connections. This code is coordinated via the GC or some external means rather than by clients directly |
| `tv_secure_bypass` | `Bool` | `false` |  | `release` | Bypass secure challenge on TV port |
| `tv_show_allchat` | `Bool` | `true` |  | `gamedll` `release` |  |
| `tv_spectator_port_offset` | `Int32` | `0` |  | `clientdll` `release` |  |
| `tv_threaded_merge_entity_deltas` | `Bool` | `true` |  | `developmentonly` `defensive` | Enable SourceTV threading of delta merging |
| `tv_timeout` | `Float32` | `20.000000` |  | `release` | SourceTV connection timeout in seconds. |
| `tv_title` | `String` | `SourceTV` |  | `release` | Set title for SourceTV spectator UI |
| `tv_transmitall` | `Bool` | `false` |  | `replicated` `release` | Transmit all entities (not only director view) |
| `tv_update_hibernation_enabled` | `Bool` | `true` |  | `developmentonly` `defensive` | Allow SourceTV to control server hibernation state. |
| `tv_window_size` | `Float32` | `16.000000` |  | `release` | Specifies the number of seconds worth of frames that the tv replay system should keep in memory. Increasing this greatly increases the amount of memory consumed by the TV system |
| `ui_deepstats_radio_heat_figurine` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_deepstats_radio_heat_tab` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_deepstats_radio_heat_team` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_deepstats_toplevel_mode` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_hud_dist` | `Float32` | `24.000000` |  | `developmentonly` `clientdll` `replicated` `defensive` | distance from the player to the hud |
| `ui_inspect_bkgnd_map_C2AEBB5E` | `String` | `warehouse` |  | `clientdll` `archive` `release` | Inspect background map |
| `ui_inventorysettings_recently_acknowledged` | `String` |  |  | `clientdll` `archive` `release` |  |
| `ui_leaderboards_top_public_appid` | `Int32` | `730` |  | `clientdll` `hidden` `release` |  |
| `ui_lobby_draft_enabled` | `Bool` | `false` |  | `clientdll` `release` |  |
| `ui_mainmenu_bkgnd_movie_C2AEBB5E` | `String` | `de_cache` |  | `clientdll` `archive` `release` | Main menu background movie |
| `ui_nearbylobbies_filter3` | `String` | `competitive` |  | `clientdll` `archive` `release` |  |
| `ui_news_last_read_link` | `String` |  |  | `clientdll` `archive` `release` |  |
| `ui_news_last_read_link2` | `String` |  |  | `clientdll` `archive` `release` |  |
| `ui_notification_tb_snooze` | `String` |  |  | `clientdll` `archive` `release` |  |
| `ui_party_msg_sound_enabled` | `Bool` | `true` |  | `clientdll` `release` | When enabled, lobby messages will play a short sound |
| `ui_playsettings_custom_preset` | `String` |  |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_directchallengekey` | `String` |  |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_casual` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_competitive` | `String` | `16` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_cooperative` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_deathmatch` | `String` | `32` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_retakes` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_scrimcomp2v2` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_skirmish` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_survival` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_casual` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_competitive` | `String` | `16` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_cooperative` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_deathmatch` | `String` | `32` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_retakes` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_scrimcomp2v2` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_skirmish` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_survival` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_listen_annotations` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_listen_grenades` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_listen_infammo` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_listen_infwarmup` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_listen_casual` | `String` | `mg_de_dust2` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_listen_competitive` | `String` | `mg_de_dust2` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_listen_deathmatch` | `String` | `mg_de_dust2` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_listen_gungameprogressive` | `String` | `mg_ar_baggage` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_listen_retakes` | `String` | `mg_de_dust2` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_listen_scrimcomp2v2` | `String` | `mg_de_inferno` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_official_casual` | `String` | `mg_casualalpha` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_official_deathmatch` | `String` | `mg_casualalpha` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_official_gungameprogressive` | `String` | `mg_armsrace` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_official_retakes` | `String` | `mg_casualalpha` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_workshop` | `String` |  |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_mode_listen` | `String` | `deathmatch` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_mode_official_v20` | `String` | `deathmatch` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_survival_solo` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_playsettings_warmup_map_name` | `String` | `de_mirage` |  | `clientdll` `archive` `release` |  |
| `ui_popup_weaponupdate_version` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_render_task_clips_label` | `String` | `dealt_damage` |  | `clientdll` `release` |  |
| `ui_render_task_file` | `String` | `rendertask` |  | `clientdll` `release` |  |
| `ui_render_task_fps` | `Int32` | `60` |  | `clientdll` `release` |  |
| `ui_render_task_generate_clips` | `Bool` | `false` |  | `clientdll` `release` |  |
| `ui_setting_advertiseforhire_auto` | `Int32` | `1` |  | `clientdll` `archive` `release` | Whether users will automatically advertise for invites (0: off; 1: last; 2: auto) |
| `ui_setting_advertiseforhire_auto_last` | `String` | `/competitive` |  | `clientdll` `archive` `release` | Which game mode users last used to advertise for invites |
| `ui_show_subscription_alert` | `String` | `0` |  | `clientdll` `archive` `release` |  |
| `ui_show_unlock_competitive_alert` | `String` |  |  | `clientdll` `archive` `release` |  |
| `ui_steam_overlay_notification_position` | `String` | `bottomleft` |  | `clientdll` `archive` | Steam overlay notification position |
| `ui_steam_overlay_notification_position_horz` | `Int32` | `0` | `0 .. 100` | `clientdll` `archive` | Steam overlay notification position horizontal offset |
| `ui_steam_overlay_notification_position_vert` | `Int32` | `0` | `0 .. 100` | `clientdll` `archive` | Steam overlay notification position vertical offset |
| `ui_vanitysetting_loadoutslot_ct` | `String` |  |  | `clientdll` `archive` `release` |  |
| `ui_vanitysetting_loadoutslot_t` | `String` |  |  | `clientdll` `archive` `release` |  |
| `ui_vanitysetting_team` | `String` |  |  | `clientdll` `archive` `release` |  |
| `update_all_keyframed_in_spatial_partition_update` | `Bool` | `true` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `update_voices_low_priority` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `vconsole_rcon_server_details` | `String` |  |  | `dontrecord` `release` `server_cannot_query` | when non-empty allows for easy vconsole connection to the dedicated server. |
| `vehicle_debug_impact_damage` | `Bool` | `false` |  | `developmentonly` `gamedll` |  |
| `videocfg_ao_detail` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` |  |
| `videocfg_fsr_detail` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` |  |
| `videocfg_hdr_detail` | `Int32` | `-1` |  | `developmentonly` `clientdll` `defensive` |  |
| `videocfg_particle_detail` | `Int32` | `1` |  | `developmentonly` `clientdll` `defensive` |  |
| `videocfg_shadow_quality` | `Int32` | `1` |  | `developmentonly` `clientdll` `defensive` |  |
| `videocfg_texture_detail` | `Int32` | `1` |  | `developmentonly` `clientdll` `defensive` |  |
| `view_punch_decay` | `Float32` | `18.000000` |  | `gamedll` `clientdll` `replicated` `cheat` `release` | Decay factor exponent for view punch |
| `viewmodel_fov` | `Float32` | `60.000000` | `60.000000 .. 68.000000` | `clientdll` `archive` `userinfo` `per_user` | Viewmodel FOV |
| `viewmodel_offset_x` | `Float32` | `1.000000` | `-2.000000 .. 2.500000` | `clientdll` `archive` `userinfo` `per_user` | viewmodel_offset_x |
| `viewmodel_offset_y` | `Float32` | `1.000000` | `-2.000000 .. 2.000000` | `clientdll` `archive` `userinfo` `per_user` | viewmodel_offset_y |
| `viewmodel_offset_z` | `Float32` | `-1.000000` | `-2.000000 .. 2.000000` | `clientdll` `archive` `userinfo` `per_user` | viewmodel_offset_z |
| `viewmodel_presetpos` | `Int32` | `1` |  | `clientdll` `archive` | 1:"Desktop", 2:"Classic" |
| `violence_ablood` | `Bool` | `true` |  | `archive` | Draw alien blood |
| `violence_agibs` | `Bool` | `true` |  | `archive` | Show alien gib entities |
| `violence_hblood` | `Bool` | `true` |  | `archive` | Draw human blood |
| `violence_hgibs` | `Bool` | `true` |  | `archive` | Show human gib entities |
| `vis_enable` | `Bool` | `true` |  | `developmentonly` `defensive` | Enable precomputed visibility when true |
| `vis_force` | `Bool` | `false` |  | `gamedll` `cheat` |  |
| `vis_sunlight_enable` | `Bool` | `true` |  | `developmentonly` `cheat` | Toggle whether to use sunlight PVS for sunlight views (0 = sky PVS, 1 = sunlight PVS) |
| `vismon_poll_frequency` | `Float32` | `0.500000` |  | `gamedll` `cheat` |  |
| `vismon_trace_limit` | `Int32` | `12` |  | `gamedll` `cheat` |  |
| `voice_all_icons` | `Bool` | `false` |  | `developmentonly` `clientdll` `defensive` | Draw all players' voice icons |
| `voice_always_sample_mic` | `Bool` | `false` |  | `archive` | When enabled, open the voip audio input stream when the application launches. |
| `voice_bypass_noise_gate` | `Bool` | `false` |  | `developmentonly` |  |
| `voice_clientdebug` | `Int32` | `0` |  | `developmentonly` `clientdll` `defensive` |  |
| `voice_debugfeedbackfrom` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `voice_device_override` | `String` |  |  | `archive` `release` | Default device used for voice capture. |
| `voice_fadeouttime` | `Float32` | `0.005000` |  | `developmentonly` `defensive` |  |
| `voice_in_process` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `voice_initial_buffer_ms` | `Int32` | `200` |  | `developmentonly` `defensive` |  |
| `voice_input_stallout` | `Float32` | `2.000000` |  | `userinfo` | Time before we consider a mic stalled out and need to reset it. |
| `voice_loopback` | `Bool` | `false` |  | `userinfo` |  |
| `voice_loopback_no_networking` | `Bool` | `false` |  | `userinfo` |  |
| `voice_min_buffer_ms` | `Int32` | `100` |  | `developmentonly` `defensive` |  |
| `voice_modenable` | `Bool` | `true` |  | `clientdll` `archive` `release` `clientcmd_can_execute` | Enable/disable voice in this mod. |
| `voice_noise_supression` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `voice_player_speaking_delay_threshold` | `Float32` | `0.500000` |  | `gamedll` `cheat` |  |
| `voice_sequence_maximum_wait_time` | `Float32` | `0.500000` |  | `developmentonly` `defensive` | When receiving packets out of sequence, wait this many seconds for missing sequences to arrive |
| `voice_serverdebug` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `voice_stall_ms` | `Float32` | `250.000000` |  | `developmentonly` `defensive` |  |
| `voice_test_log_send` | `Bool` | `false` |  | `release` |  |
| `voice_threshold` | `Float32` | `-120.000000` |  | `clientdll` `archive` | decibel threshold for how loud the talker's input signal is before we think they are talking. |
| `voice_threshold_attack` | `Float32` | `0.300000` |  | `developmentonly` | Amount of time we buffer outgoing audio to detect an onset. |
| `voice_threshold_delay` | `Float32` | `0.700000` |  | `developmentonly` | Amount of time the talker is silent before we infer that they are no longer talking. |
| `voice_threshold_hold` | `Float32` | `0.200000` |  | `developmentonly` | Amount of time after the talker starts talking we should keep listening regardless of how loud they are speaking. |
| `voice_threshold_ramp_min_db` | `Float32` | `-60.000000` |  | `developmentonly` | A dB floor of when to stop transmitting packets, the volume between this and voice_threshold will still transmit packets to allow for volume ramping. |
| `voice_vox` | `Int32` | `0` |  | `clientdll` `archive` `per_user` | Voice chat uses a vox-style always on |
| `voice_vox_current_peak` | `Float32` | `0.000000` |  | `developmentonly` `clientdll` `defensive` | Current peak value (out of 64k) of the incoming voice stream |
| `volume` | `Float32` | `1.000000` | `0.000000 .. 1.000000` | `archive` | Sound volume |
| `volume_fog_debug_volumes` | `Bool` | `false` |  | `cheat` |  |
| `volume_fog_density_scale` | `Float32` | `1.000000` |  | `developmentonly` `cheat` | Scale global volume fog density |
| `volume_fog_depth` | `Int32` | `128` | `48 .. 1024` | `developmentonly` `defensive` | Depth of volume fog texture |
| `volume_fog_depth_warp` | `Float32` | `7.000000` |  | `developmentonly` `defensive` |  |
| `volume_fog_depth_warp_debug` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `volume_fog_dither_scale` | `Float32` | `1.000000` |  | `cheat` |  |
| `volume_fog_enable_jitter` | `Bool` | `true` |  | `cheat` |  |
| `volume_fog_height` | `Int32` | `160` | `64 .. 1024` | `developmentonly` `defensive` | Height of volume fog texture |
| `volume_fog_intermediate_textures_hdr` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `volume_fog_shadow_penumbra_multiplier` | `Float32` | `3.000000` |  | `developmentonly` `defensive` | Penumbra size multiplier for shadow sampling, reduces fog shadow aliasing |
| `volume_fog_temporal_filter` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `volume_fog_temporal_weight` | `Float32` | `0.900000` | `0.100000 .. 0.990000` | `developmentonly` `defensive` | Temporal filtering weight |
| `volume_fog_width` | `Int32` | `240` | `64 .. 1024` | `developmentonly` `defensive` | Width of volume fog texture |
| `vprof_counters` | `Int32` | `0` |  | `developmentonly` `defensive` |  |
| `vprof_counters_show_minmax` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `vprof_scope_entity_clientthink` | `Bool` | `false` |  | `developmentonly` `clientdll` `hidden` `defensive` | Does nothing whatsoever. |
| `vprof_scope_entity_thinks` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `vprof_think_limit` | `Bool` | `false` |  | `developmentonly` `gamedll` `defensive` |  |
| `vt_sim_streaming_delay_ms` | `Float32` | `500.000000` |  | `developmentonly` `defensive` |  |
| `vulkan_batch_size` | `Int32` | `500` |  | `developmentonly` `defensive` |  |
| `vulkan_batch_submits` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `vulkan_dedicated_allocation_threshold` | `UInt64` | `512` |  | `developmentonly` `defensive` | Size (in KBs) above which textures should be allocated in dedicated memory (NV-only). |
| `vulkan_link_time_optimize_libraries` | `Bool` | `true` |  | `release` |  |
| `vulkan_pipeline_compile_spew` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `vulkan_pipeline_compile_throttle_ms` | `Float32` | `0.000000` |  | `developmentonly` `defensive` |  |
| `vulkan_unpause_workers_after_each_texture_deallocation` | `Bool` | `false` |  | `developmentonly` | If true, the main thread pauses and unpauses the Vulkan worker threads around each texture deallocation, which allows the workers to make a little bit of progress but results in main thread stalls. If false, we keep the workers paused until all deallocations are done, allowing the deallocations to complete significantly faster. |
| `weapon_accuracy_forcespread` | `Float32` | `0.000000` |  | `gamedll` `clientdll` `replicated` `release` | Force spread to the specified value. |
| `weapon_accuracy_logging` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `archive` `replicated` |  |
| `weapon_accuracy_nospread` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Disable weapon inaccuracy spread |
| `weapon_accuracy_reset_on_deploy` | `Bool` | `false` |  | `gamedll` `clientdll` `replicated` `cheat` `release` | On deploy, forcibly reset weapon accuracy to zero. |
| `weapon_accuracy_shotgun_spread_patterns` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` |  |
| `weapon_accuracy_stack_boost_limit` | `Int32` | `2` |  | `gamedll` `clientdll` `replicated` `release` | Apply ladder inaccuracy to players boosted by a stack of this many (or more) players |
| `weapon_air_spread_scale` | `Float32` | `1.000000` | `>= 0.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scale factor for jumping inaccuracy, set to 0 to make jumping accuracy equal to standing |
| `weapon_all_nametag` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `weapon_all_stattrak` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `weapon_auto_cleanup_time` | `Float32` | `0.000000` |  | `gamedll` `clientdll` `replicated` `release` | If set to non-zero, weapons will delete themselves after the specified time (in seconds) if no players are near. |
| `weapon_debug_inaccuracy_only_up` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Force weapon inaccuracy to be in exactly the up direction |
| `weapon_debug_max_inaccuracy` | `Bool` | `false` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Force all shots to have maximum inaccuracy |
| `weapon_debug_spread_gap` | `Float32` | `0.670000` |  | `clientdll` `cheat` `per_user` |  |
| `weapon_debug_spread_show` | `Int32` | `0` |  | `clientdll` `cheat` `per_user` | Enables display of weapon accuracy; 1: show accuracy box, 3: show accuracy with dynamic crosshair |
| `weapon_land_dip_amt` | `Float32` | `20.000000` |  | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | The amount the gun should dip when the player lands after a jump. |
| `weapon_max_before_cleanup` | `Int32` | `0` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If set to non-zero, will remove the oldest dropped weapon to maintain the specified number of dropped weapons in the world. |
| `weapon_molotov_maxdetonateslope` | `Float32` | `30.000000` | `0.000000 .. 90.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Maximum angle of slope on which the molotov will detonate |
| `weapon_near_empty_sound` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `cheat` |  |
| `weapon_random_stickers` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `weapon_reticle_knife_show` | `Bool` | `true` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | When enabled will show knife reticle on clients. Used for game modes requiring target id display when holding a knife. |
| `weapon_skin_force_legacy` | `Int32` | `-1` |  | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `weapon_skins` | `Bool` | `true` |  | `developmentonly` `clientdll` |  |
| `weapon_skins_on_default` | `Bool` | `false` |  | `developmentonly` `clientdll` |  |
| `weapon_sound_falloff_multiplier` | `Float32` | `1.000000` |  | `gamedll` `clientdll` `replicated` `cheat` `release` `commandline_enforced` | Scaling for falloff of weapon firing sounds |
| `webapi_values_init_buffer_size` | `Int32` | `65536` |  | `developmentonly` `clientdll` `defensive` | Initial buffer size for buffers in the WebAPIValues buffer pool |
| `webapi_values_max_pool_size_mb` | `UInt32` | `400` |  | `developmentonly` `clientdll` `defensive` | Maximum size in bytes of the WebAPIValues buffer pool |
| `wind_system_debug_volumes` | `Bool` | `false` |  | `developmentonly` `defensive` |  |
| `wind_system_default_resolution_xy` | `Int32` | `256` |  | `developmentonly` `defensive` |  |
| `wind_system_default_resolution_z` | `Int32` | `32` |  | `developmentonly` `defensive` |  |
| `wind_system_default_sample_min_spacing` | `Float32` | `12.000000` |  | `developmentonly` `defensive` |  |
| `wind_system_temporal_smoothing` | `Bool` | `true` |  | `developmentonly` `defensive` |  |
| `zoom_sensitivity_ratio` | `Float32` | `1.000000` | `0.010000 .. 3.000000` | `clientdll` `archive` `per_user` | Additional mouse sensitivity scale factor applied when FOV is zoomed in. |
