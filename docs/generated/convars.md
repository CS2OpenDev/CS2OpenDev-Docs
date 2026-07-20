---
layout: default
title: ConVars
nav_order: 4
---

# ConVar Reference

All console variables extracted from CS2.

| Name | Default | Flags | Description |
|------|---------|-------|-------------|
| `CS_WarnFriendlyDamageInterval` | `3` | `gamedll` `cheat` | Defines how frequently the server notifies clients that a player damaged a friend |
| `Inferno_concav_plane_threshold` | `-10.000000` | `developmentonly` `clientdll` `defensive` |  |
| `_fov` | `0` | `developmentonly` `clientdll` `defensive` | Automates fov command to server. |
| `adsp_alley_min` | `122` | `developmentonly` `defensive` |  |
| `adsp_courtyard_min` | `126` | `developmentonly` `defensive` |  |
| `adsp_debug` | `0` | `archive` |  |
| `adsp_door_height` | `112` | `developmentonly` `defensive` |  |
| `adsp_duct_min` | `106` | `developmentonly` `defensive` |  |
| `adsp_hall_min` | `110` | `developmentonly` `defensive` |  |
| `adsp_low_ceiling` | `108` | `developmentonly` `defensive` |  |
| `adsp_opencourtyard_min` | `126` | `developmentonly` `defensive` |  |
| `adsp_openspace_min` | `130` | `developmentonly` `defensive` |  |
| `adsp_openstreet_min` | `118` | `developmentonly` `defensive` |  |
| `adsp_openwall_min` | `130` | `developmentonly` `defensive` |  |
| `adsp_room_min` | `102` | `developmentonly` `defensive` |  |
| `adsp_street_min` | `118` | `developmentonly` `defensive` |  |
| `adsp_tunnel_min` | `114` | `developmentonly` `defensive` |  |
| `adsp_wall_height` | `128` | `developmentonly` `defensive` |  |
| `ag2_network_recipeshape_cache_size` | `32` | `developmentonly` `gamedll` `dontrecord` | Cache size for recently-used pose recipe shapes. |
| `ag2_preserve_params_on_reload` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` | When an animgraph is reloaded, should the underlying system restore all params? |
| `ag2_use_networked_serialization_context_demo` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `dontrecord` | Use networked compatibility serialization context in demo playback. |
| `ag2_use_networked_serialization_context_game` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` | Use networked compatibility serialization context in games. |
| `ai_debug_dyninteractions` | `0` | `gamedll` `cheat` | Debug the NPC dynamic interaction system. |
| `ai_debug_los` | `0` | `gamedll` `cheat` | NPC Line-Of-Sight debug mode. If 1, solid entities that block NPC LOC will be highlighted with white bounding boxes. If 2, it'll show non-solid entities that would do it if they were solid. |
| `ai_debug_ragdoll_magnets` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `ai_debug_scripted_sequence` | `false` | `gamedll` `cheat` |  |
| `ai_debug_shoot_positions` | `0` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ai_debug_speech` | `0` | `developmentonly` `gamedll` `defensive` |  |
| `ai_disabled` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ai_force_serverside_ragdoll` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `ai_off_nav_show_nearest` | `false` | `gamedll` `cheat` |  |
| `ai_sequence_debug` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `ai_use_visibility_cache` | `1` | `developmentonly` `gamedll` `defensive` | Sets whether or not NPCs can cache their Visibility checks against other entities. If set to 2, also tests to make sure that NPC->Target results match that of Target->NPC. |
| `ai_use_visibility_cache_reciprocation` | `true` | `developmentonly` `gamedll` `defensive` | Sets whether or not the visibility check cache should be reciprocal. |
| `always_perform_full_spatial_partition_update` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `ammo_338mag_headshot_mult` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_338mag_impulse` | `2800.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_338mag_max` | `30` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_357sig_headshot_mult` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_357sig_impulse` | `2000.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_357sig_max` | `52` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_357sig_min_max` | `12` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_357sig_p250_max` | `26` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_357sig_small_max` | `24` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_45acp_headshot_mult` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_45acp_impulse` | `2100.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_45acp_max` | `100` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_50AE_headshot_mult` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_50AE_impulse` | `2400.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_50AE_max` | `35` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_556mm_box_headshot_mult` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_556mm_box_impulse` | `2400.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_556mm_box_max` | `200` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_556mm_headshot_mult` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_556mm_impulse` | `2400.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_556mm_max` | `90` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_556mm_small_max` | `40` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_57mm_headshot_mult` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_57mm_impulse` | `2000.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_57mm_max` | `100` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_762mm_headshot_mult` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_762mm_impulse` | `2400.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_762mm_max` | `90` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_9mm_headshot_mult` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_9mm_impulse` | `2000.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_9mm_max` | `120` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_buckshot_headshot_mult` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_buckshot_impulse` | `600.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_buckshot_max` | `32` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_grenade_limit_default` | `1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `ammo_grenade_limit_flashbang` | `1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `ammo_grenade_limit_total` | `3` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `ammo_item_limit_adrenaline` | `5` | `gamedll` `clientdll` `replicated` `release` |  |
| `ammo_item_limit_healthshot` | `4` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `anim_decode_forcewritealltransforms` | `false` | `developmentonly` | Force BatchAnimationDecode to write transformations for all bones |
| `anim_disable` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `anim_resource_validate_on_load` | `true` | `release` | Validates the animation group channel list against the animations on load for every animation |
| `animated_material_attributes` | `true` | `clientdll` `cheat` |  |
| `animgraph2_enable_parallel_update` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph2_serialize_pose_recipe_in_pre_pack_entities` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_debug` | `false` | `gamedll` `clientdll` `replicated` `cheat` | Debug animation graph |
| `animgraph_debug_animevents` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` | Print info about animevents emitted by AnimGraph |
| `animgraph_debug_entindex` | `0` | `gamedll` `clientdll` `replicated` `cheat` | The entity to specifically debug |
| `animgraph_debug_filterent` | `0` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Filter setting for animgraph_debug_variables output. If set to -1, show debug for all entities. If set to 0, show debug for any NPCs that have been npc_selected. If set to >0, something other than 0, show debug for the entity with the matching entindex. |
| `animgraph_debug_max_poseop_count` | `false` | `reference` |  |
| `animgraph_debug_set_filter_params` | `` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Comma separated list of params to filter against when drawing debug text overlays |
| `animgraph_debug_set_filter_tags` | `` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Comma separated list of tags to filter against when drawing debug text overlays |
| `animgraph_debug_show_unreferenced_params` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_debug_show_unreferenced_tags` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_debug_tags` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_debug_variables` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Turn on to see animgraph variable changes for entities passing animgraph_debug_filterent. |
| `animgraph_debug_variables_ignore_missing` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | If set, animgraph_debug_variables won't show debug for warnings about sets to missing variables. |
| `animgraph_debug_variables_ignore_nonchanges` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | If set, animgraph_debug_variables won't show debug for variable sets that don't change the value. |
| `animgraph_draw_traces` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_enable` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` | Enable animation graph |
| `animgraph_enable_dirty_netvar_optimization` | `true` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_auto_ledge_detection` | `true` | `developmentonly` `replicated` `defensive` | Attempt to detect when the foot is partially hanging off a ledge and stop it tilting to reach the bottom |
| `animgraph_footlock_auto_stair_detection` | `true` | `developmentonly` `replicated` `defensive` | Attempt to detect when the foot is on a stair and will stop it from tilting to reach the next step |
| `animgraph_footlock_calculate_tilt` | `true` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_debug_foot_index` | `-1` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_debug_type` | `2` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_draw_footbase` | `false` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_enabled` | `true` | `developmentonly` `replicated` `defensive` | A master convar that effectively disables the entire footlock node. |
| `animgraph_footlock_ground_roll` | `true` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_hip_offset_enable` | `true` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_ik_enable` | `true` | `replicated` `cheat` | Enable IK. |
| `animgraph_footlock_tilt_mode` | `1` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footlock_trace_ground_enabled` | `true` | `developmentonly` `replicated` `defensive` | Convar for toggling foot lock ground tracking. |
| `animgraph_footlock_use_hip_shift` | `true` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_footstep_node_supresses_events` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_force_full_network_updates` | `false` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_ik_debug` | `false` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_motionmatching_print_compressionstats` | `false` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_network_enable` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` | Enable animation graph networking. The setting is only read at graph creation time; to use please set on the command line. |
| `animgraph_parallel_postdataupdate` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `animgraph_slope_draw_raycasts` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `animgraph_slope_enable` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `animgraph_slowdownonslopes_enabled` | `true` | `developmentonly` `replicated` `defensive` |  |
| `animgraph_trace_ignore_prop_physics` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `animgraph_trace_static_only` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `animgraph_verify_dirty_netvar_optimization` | `false` | `developmentonly` `replicated` `defensive` |  |
| `annotation_auto_load` | `false` | `clientdll` `release` `commandline_enforced` |  |
| `attached_output_stall_ms` | `250.000000` | `developmentonly` `defensive` |  |
| `audio_input_test_signal` | `false` | `developmentonly` | For testing the audio input pathway with a sine tone instead of SDL3. |
| `audio_input_use_sdl_roles` | `false` | `developmentonly` |  |
| `autosave_fully_async` | `true` | `developmentonly` `gamedll` `defensive` | Set to 1 to have autosaves execute completely on the save thread, forces 'render only' mode while the save completes |
| `bot_allow_grenades` | `true` | `gamedll` `release` | If nonzero, bots may use grenades. |
| `bot_allow_machine_guns` | `true` | `gamedll` `release` | If nonzero, bots may use the machine gun. |
| `bot_allow_pistols` | `true` | `gamedll` `release` | If nonzero, bots may use pistols. |
| `bot_allow_rifles` | `true` | `gamedll` `release` | If nonzero, bots may use rifles. |
| `bot_allow_rogues` | `true` | `gamedll` `release` `commandline_enforced` | If nonzero, bots may occasionally go 'rogue'. Rogue bots do not obey radio commands, nor pursue scenario goals. |
| `bot_allow_shotguns` | `true` | `gamedll` `release` | If nonzero, bots may use shotguns. |
| `bot_allow_snipers` | `true` | `gamedll` `release` | If nonzero, bots may use sniper rifles. |
| `bot_allow_sub_machine_guns` | `true` | `gamedll` `release` | If nonzero, bots may use sub-machine guns. |
| `bot_auto_follow` | `false` | `gamedll` `release` | If nonzero, bots with high co-op may automatically follow a nearby human player. |
| `bot_auto_vacate` | `true` | `gamedll` `release` | If nonzero, bots will automatically leave to make room for human players. |
| `bot_autodifficulty_threshold_high` | `5.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Upper bound above Average Human Contribution Score that a bot must be above to change its difficulty |
| `bot_autodifficulty_threshold_low` | `-2.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Lower bound below Average Human Contribution Score that a bot must be below to change its difficulty |
| `bot_chatter` | `normal` | `gamedll` `release` `commandline_enforced` | Control how bots talk. Allowed values: 'off', 'radio', 'minimal', or 'normal'. |
| `bot_chatter_use_rr` | `true` | `developmentonly` `gamedll` | 0 = Use old bot chatter system, 1 = Use response rules |
| `bot_controllable` | `true` | `gamedll` `release` | Determines whether bots can be controlled by players |
| `bot_coop_idle_max_vision_distance` | `1400.000000` | `gamedll` `replicated` `release` `commandline_enforced` | Max distance bots can see targets (in coop) when they are idle, dormant, hiding or asleep. |
| `bot_crouch` | `false` | `gamedll` `cheat` |  |
| `bot_debug` | `0` | `gamedll` `cheat` | For internal testing purposes. |
| `bot_debug_target` | `0` | `gamedll` `cheat` | For internal testing purposes. |
| `bot_defense_rush_chance` | `33.000000` | `gamedll` `cheat` | Are the defense bots going to rush. |
| `bot_defer_to_human_goals` | `false` | `gamedll` `release` `commandline_enforced` | If nonzero and there is a human on the team, the bots will not do the scenario tasks. |
| `bot_defer_to_human_items` | `true` | `gamedll` `release` `commandline_enforced` | If nonzero and there is a human on the team, the bots will not get scenario items. |
| `bot_difficulty` | `1` | `gamedll` `release` `commandline_enforced` | Defines the skill of bots joining the game.  Values are: 0=easy, 1=normal, 2=hard, 3=expert. |
| `bot_dont_shoot` | `false` | `gamedll` `cheat` `release` | If nonzero, bots will not fire weapons (for debugging). |
| `bot_eco_limit` | `2000.000000` | `gamedll` `release` | If nonzero, bots will not buy if their money falls below this amount. |
| `bot_flipout` | `false` | `gamedll` `release` | If nonzero, bots use no CPU for AI. Instead, they run around randomly. |
| `bot_force_duck` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `bot_freeze` | `false` | `gamedll` `cheat` |  |
| `bot_ignore_enemies` | `false` | `gamedll` `cheat` | If nonzero, bots will ignore enemies (for debugging). |
| `bot_ignore_players` | `false` | `gamedll` `cheat` | Bots will not see non-bot players. |
| `bot_join_after_player` | `true` | `gamedll` `release` | If nonzero, bots wait until a player joins before entering the game. |
| `bot_join_delay` | `0` | `developmentonly` `gamedll` `defensive` | Prevents bots from joining the server for this many seconds after a map change. |
| `bot_join_in_warmup` | `true` | `developmentonly` `gamedll` `defensive` | Prevents bots from joining the server while warmup phase is active. |
| `bot_join_team` | `any` | `gamedll` `release` | Determines the team bots will join into. Allowed values: 'any', 'T', or 'CT'. |
| `bot_loadout` | `` | `gamedll` `cheat` | bots are given these items at round start |
| `bot_max_visible_smoke_length` | `200.000000` | `gamedll` `replicated` `release` | Bots will see players through smoke clouds up to this length. |
| `bot_max_vision_distance_override` | `-1.000000` | `gamedll` `replicated` `release` `commandline_enforced` | Max distance bots can see targets. |
| `bot_mimic` | `0` | `gamedll` `clientdll` `replicated` `cheat` | Bot uses usercmd of player by index. |
| `bot_mimic_spec_buttons` | `true` | `clientdll` `cheat` | +attack, +jump etc are used for spectator control instead of being passed on to spectated bot |
| `bot_mimic_yaw_offset` | `180.000000` | `gamedll` `cheat` |  |
| `bot_prefix` | `` | `gamedll` `release` | This string is prefixed to the name of all bots that join the game.
<difficulty> will be replaced with the bot's difficulty.
<weaponclass> will be replaced with the bot's desired weapon class.
<skill> will be replaced with a 0-100 representation of the bot's skill. |
| `bot_quota` | `10` | `gamedll` `release` `commandline_enforced` | Determines the total number of bots in the game. |
| `bot_quota_mode` | `normal` | `gamedll` `release` `commandline_enforced` | Determines the type of quota.
Allowed values: 'normal', 'fill', and 'match'.
If 'fill', the server will adjust bots to keep N players in the game, where N is bot_quota.
If 'match', the server will maintain a 1:N ratio of humans to bots, where N is bot_quota. |
| `bot_randombuy` | `false` | `gamedll` `cheat` | should bots ignore their prefered weapons and just buy weapons at random? |
| `bot_show_battlefront` | `false` | `gamedll` `cheat` | Show areas where rushing players will initially meet. |
| `bot_show_nav` | `false` | `gamedll` `cheat` | For internal testing purposes. |
| `bot_show_occupy_time` | `false` | `gamedll` `cheat` | Show when each nav area can first be reached by each team. |
| `bot_stop` | `0` | `gamedll` `cheat` | bot_stop <1\|all> \| <not_bomber> \| <t> \| <ct> |
| `bot_strafe` | `0.000000` | `gamedll` `release` | Strafe left and right (interval) |
| `bot_traceview` | `0` | `gamedll` `cheat` | For internal testing purposes. |
| `bot_walk` | `false` | `gamedll` `release` | If nonzero, bots can only walk, not run. |
| `bot_zombie` | `false` | `gamedll` `cheat` | If nonzero, bots will stay in idle mode and not attack. |
| `break_damage_inherit_scale` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `break_invulnerable_spawn_duration` | `0.500000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `breakable_debug_spawn_transform_time` | `0.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | Debug draw the spawn transform location. |
| `breakable_multiplayer` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `buddha` | `false` | `gamedll` `notify` `cheat` | Player takes damage but won't die |
| `buddha_ignore_bots` | `false` | `gamedll` `notify` `cheat` | Bots always buddha 0 |
| `buddha_reset_hp` | `1` | `gamedll` `notify` `cheat` | HP to set when damaged below zero in Buddha Mode |
| `buildcubemaps_renderdoc_capture` | `-1` | `developmentonly` `clientdll` | Capture a specific cubemap with RenderDoc during buildcubemaps. |
| `c_maxdistance` | `200.000000` | `clientdll` `archive` |  |
| `c_maxpitch` | `90.000000` | `clientdll` `archive` |  |
| `c_maxyaw` | `135.000000` | `clientdll` `archive` |  |
| `c_mindistance` | `30.000000` | `clientdll` `archive` |  |
| `c_minpitch` | `0.000000` | `clientdll` `archive` |  |
| `c_minyaw` | `-135.000000` | `clientdll` `archive` |  |
| `c_orthoheight` | `100.000000` | `clientdll` `archive` |  |
| `c_orthowidth` | `100.000000` | `clientdll` `archive` |  |
| `c_thirdpersonshoulder` | `false` | `clientdll` `archive` |  |
| `c_thirdpersonshoulderaimdist` | `120.000000` | `clientdll` `archive` |  |
| `c_thirdpersonshoulderdist` | `40.000000` | `clientdll` `archive` |  |
| `c_thirdpersonshoulderheight` | `5.000000` | `clientdll` `archive` |  |
| `c_thirdpersonshoulderoffset` | `20.000000` | `clientdll` `archive` |  |
| `cachedvalue_count_partybrowser` | `0` | `clientdll` `hidden` `archive` |  |
| `cachedvalue_count_teammates` | `0` | `clientdll` `hidden` `archive` |  |
| `cam_collision` | `1` | `clientdll` `archive` | When in thirdperson and cam_collision is set to 1, an attempt is made to keep the camera from passing though walls. |
| `cam_idealdelta` | `4.000000` | `clientdll` `archive` | Controls the speed when matching offset to ideal angles in thirdperson view |
| `cam_idealdist` | `150.000000` | `clientdll` `archive` |  |
| `cam_ideallag` | `4.000000` | `clientdll` `archive` | Amount of lag used when matching offset to ideal angles in thirdperson view |
| `cam_idealpitch` | `0.000000` | `clientdll` `archive` |  |
| `cam_idealyaw` | `0.000000` | `clientdll` `archive` |  |
| `cam_showangles` | `false` | `clientdll` `cheat` | When in thirdperson, print viewangles/idealangles/cameraoffsets to the console. |
| `cam_snapto` | `false` | `clientdll` `archive` |  |
| `camera_datadriven_debug` | `false` | `developmentonly` `clientdll` `cheat` |  |
| `camera_datadriven_disable_cache` | `false` | `developmentonly` `gamedll` `cheat` |  |
| `camera_path_edit_mode` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `cash_player_bomb_defused` | `300` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_bomb_planted` | `300` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_damage_hostage` | `-30` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_drop_on_death` | `0` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_drop_on_death_stack_value` | `250` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_get_killed` | `0` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_interact_with_hostage` | `150` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_killed_enemy_default` | `300` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_killed_enemy_factor` | `1.000000` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_killed_hostage` | `-1000` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_killed_teammate` | `-300` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_rescued_hostage` | `1000` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_player_respawn_amount` | `0` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_bonus_shorthanded` | `0` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_elimination_bomb_map` | `3250` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_elimination_hostage_map_ct` | `2000` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_elimination_hostage_map_t` | `1000` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_hostage_alive` | `0` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_hostage_interaction` | `500` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_loser_bonus` | `1400` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_loser_bonus_consecutive_rounds` | `500` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_per_dead_enemy` | `50` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_planted_bomb_but_defused` | `600` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_rescued_hostage` | `0` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_terrorist_win_bomb` | `3500` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_win_by_defusing_bomb` | `3250` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_win_by_hostage_rescue` | `3500` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_win_by_time_running_out_bomb` | `3250` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_win_by_time_running_out_hostage` | `3250` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` |  |
| `cash_team_winner_bonus_consecutive_rounds` | `0` | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `cc_captiontrace` | `1` | `developmentonly` `clientdll` `defensive` | Show missing closecaptions (0 = no, 1 = devconsole, 2 = show in hud) |
| `cc_delay_time` | `0.250000` | `clientdll` `archive` | Close caption delay before showing caption. |
| `cc_force_combine_chatter` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cc_lang` | `` | `clientdll` `archive` | Current close caption language (emtpy = use game UI language) |
| `cc_linger_time` | `1.000000` | `clientdll` `archive` | Close caption linger time. |
| `cc_log` | `0` | `developmentonly` `clientdll` `defensive` | Log caption names and contents (0 = off, 1 = found captions, 2 = unfound captions, 3 = all captions) |
| `cc_spectator_only` | `false` | `clientdll` `archive` |  |
| `cc_subtitles` | `false` | `clientdll` `archive` | If set, don't show sound effect captions, just voice overs (i.e., won't help hearing impaired players). |
| `cc_vr_caption_catchup_interval` | `0.300000` | `developmentonly` `clientdll` `defensive` | Duration it takes for attached caption to ideal point |
| `cc_vr_caption_speed` | `1` | `clientdll` `archive` | 0 = slow, 1 = medium (default), 2 = fast |
| `cc_vr_debug` | `false` | `developmentonly` `clientdll` `defensive` | Debug visualization of VR closed caption placement |
| `cc_vr_depth_test` | `false` | `developmentonly` `clientdll` `defensive` | Have closed caption Panorama panel perform depth testing against the scene |
| `cc_vr_epsilon` | `2.500000` | `developmentonly` `clientdll` `defensive` | Epsilon to trigger movement of VR subtitle panel in world space |
| `cc_vr_font_size` | `1` | `clientdll` `archive` | 0 = small, 1 = med (default), 2 = large |
| `cc_vr_forward_offset` | `30.000000` | `developmentonly` `clientdll` `defensive` | Subtitle offset distance (forward, in front of player) |
| `cc_vr_vertical_offset` | `-6.500000` | `developmentonly` `clientdll` `defensive` | Subtitle vertical offset distance (positive is up) |
| `cc_vr_width` | `1` | `clientdll` `archive` | 0 = narrow, 1 = med (default), 2 = wide |
| `character_patches` | `true` | `developmentonly` `clientdll` |  |
| `check_transmit_dump_ents` | `false` | `developmentonly` `gamedll` |  |
| `chicken_stop` | `false` | `gamedll` `cheat` |  |
| `cl_ShowBoneSetupEnts` | `false` | `developmentonly` `clientdll` `defensive` | Show which entities are having their bones setup each frame. |
| `cl_access_all_missions` | `false` | `developmentonly` `clientdll` |  |
| `cl_ag2_record_entity_graph` | `` | `developmentonly` `clientdll` | Automatically start AG2 recording when an entity with this name (wildcard) or id is created. |
| `cl_aggregate_particles` | `false` | `developmentonly` `defensive` |  |
| `cl_allow_animated_avatars` | `true` | `clientdll` `archive` `release` | Whether or not to allow animated avatars |
| `cl_allow_multi_input_binds` | `false` | `clientdll` `cheat` `release` |  |
| `cl_anglespeedkey` | `0.670000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_async_client_shatter` | `true` | `developmentonly` `clientdll` | spawn client glass shards asynchronously during demos or when remotely connected. |
| `cl_async_restore_server_authoritative_state` | `false` | `developmentonly` `clientdll` |  |
| `cl_autobuy` | `` | `clientdll` `release` | The order in which autobuy will attempt to purchase items |
| `cl_autohelp` | `true` | `clientdll` `archive` `userinfo` | Auto-help |
| `cl_bake_bomb_damage_debug` | `0` | `clientdll` `cheat` |  |
| `cl_batch_entity_list_ops_during_latch` | `false` | `developmentonly` `clientdll` | Batch entity list adds / removes while latching interpolated variables to avoid mutex contention. |
| `cl_bone_cache_optimization` | `true` | `developmentonly` `clientdll` |  |
| `cl_borrow_music_from_player_slot` | `-1` | `clientdll` `release` |  |
| `cl_boxmove` | `0` | `developmentonly` `clientdll` | run in a square, # represents how many usercommands to run before turning. |
| `cl_boxmove_speed` | `1.000000` | `developmentonly` `clientdll` | how fast to run (1 to use player max run speed). |
| `cl_buymenu_ct_nextround_high` | `5000` | `clientdll` `archive` `per_user` `release` |  |
| `cl_buymenu_ct_nextround_low` | `1400` | `clientdll` `archive` `per_user` `release` |  |
| `cl_buymenu_t_nextround_high` | `5000` | `clientdll` `archive` `per_user` `release` |  |
| `cl_buymenu_t_nextround_low` | `1400` | `clientdll` `archive` `per_user` `release` |  |
| `cl_buywheel_donate_key` | `0` | `clientdll` `archive` `per_user` `release` | Set the key to use for donation in the buy menu. 0: Left Control; 1: Left Alt; 2: Left Shift. |
| `cl_buywheel_nonumberpurchasing` | `false` | `clientdll` `archive` `per_user` `release` | Set non-zero to prevent buy wheel from purchasing via number keys |
| `cl_cameraoverride_fade_in_amount` | `0.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_cameraoverride_shadow_depth_bias` | `0.006000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_cameraoverride_shadow_end` | `0.800000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_change_callback_limit` | `0.200000` | `clientdll` `release` | change callback msec warning limit |
| `cl_chat_active` | `0` | `developmentonly` `clientdll` `defensive` |  |
| `cl_clanid` | `0` | `clientdll` `hidden` `archive` `userinfo` | Current clan ID for name decoration |
| `cl_clutch_mode` | `false` | `clientdll` `release` | Silence voice and other distracting sounds until the end of round or next death. |
| `cl_color` | `1` | `clientdll` `archive` `userinfo` | Preferred teammate color |
| `cl_crosshair_drawoutline` | `true` | `clientdll` `archive` `per_user` | Draws a black outline around the crosshair for better visibility |
| `cl_crosshair_dynamic_maxdist_splitratio` | `1.000000` | `clientdll` `archive` `per_user` | If using cl_crosshairstyle 2, this is the ratio used to determine how long the inner and outer xhair pips will be. [inner = cl_crosshairsize*(1-cl_crosshair_dynamic_maxdist_splitratio), outer = cl_crosshairsize*cl_crosshair_dynamic_maxdist_splitratio]  [0 - 1] |
| `cl_crosshair_dynamic_splitalpha_innermod` | `0.000000` | `clientdll` `archive` `per_user` | If using cl_crosshairstyle 2, this is the alpha modification that will be used for the INNER crosshair pips once they've split. [0 - 1] |
| `cl_crosshair_dynamic_splitalpha_outermod` | `1.000000` | `clientdll` `archive` `per_user` | If using cl_crosshairstyle 2, this is the alpha modification that will be used for the OUTER crosshair pips once they've split. [0.3 - 1] |
| `cl_crosshair_dynamic_splitdist` | `3` | `clientdll` `archive` `per_user` | If using cl_crosshairstyle 2, this is the distance that the crosshair pips will split into 2. (default is 7) |
| `cl_crosshair_friendly_warning` | `1` | `clientdll` `archive` `release` | 0: off, 1: on |
| `cl_crosshair_outlinethickness` | `1.000000` | `clientdll` `archive` `per_user` | Set how thick you want your crosshair outline to draw (0-3) |
| `cl_crosshair_recoil` | `true` | `clientdll` `archive` `per_user` |  |
| `cl_crosshair_show_desynced_seeds_marker` | `true` | `developmentonly` `clientdll` |  |
| `cl_crosshair_sniper_width` | `1` | `clientdll` `archive` `per_user` | If >1 sniper scope cross lines gain extra width (1 for single-pixel hairline) |
| `cl_crosshair_t` | `false` | `clientdll` `archive` `per_user` | T style crosshair |
| `cl_crosshairalpha` | `200` | `clientdll` `archive` `per_user` |  |
| `cl_crosshaircolor` | `5` | `clientdll` `archive` `per_user` | Set crosshair color as defined in game_options.consoles.txt |
| `cl_crosshaircolor_b` | `0` | `clientdll` `archive` `per_user` |  |
| `cl_crosshaircolor_g` | `255` | `clientdll` `archive` `per_user` |  |
| `cl_crosshaircolor_r` | `0` | `clientdll` `archive` `per_user` |  |
| `cl_crosshairdot` | `false` | `clientdll` `archive` `per_user` |  |
| `cl_crosshairgap` | `-2.200000` | `clientdll` `archive` `per_user` |  |
| `cl_crosshairgap_useweaponvalue` | `true` | `clientdll` `archive` `per_user` | If set to 1, the gap will update dynamically based on which weapon is currently equipped |
| `cl_crosshairsize` | `3.900000` | `clientdll` `archive` `per_user` |  |
| `cl_crosshairstyle` | `2` | `clientdll` `archive` `per_user` | 0 = DEFAULT (DISABLED), 1 = DEFAULT STATIC (DISABLED), 2 = DEFAULT (accurate recoil/spread feedback with a fixed inner part), 3 = ACCURATE DYNAMIC (DISABLED) (accurate recoil/spread feedback), 4 = DEFAULT STATIC, 5 = LEGACY (fake recoil - inaccurate feedback) |
| `cl_crosshairthickness` | `0.600000` | `clientdll` `archive` `per_user` |  |
| `cl_crosshairusealpha` | `true` | `clientdll` `archive` `per_user` |  |
| `cl_csgo_shoot_debugvis_rdp_text_l` | `10` | `developmentonly` `clientdll` |  |
| `cl_csgo_shoot_debugvis_rdp_text_x` | `45` | `developmentonly` `clientdll` |  |
| `cl_csgo_shoot_debugvis_show_los` | `false` | `developmentonly` `clientdll` | Show line of last shot. |
| `cl_csgo_shoot_debugvis_show_rdp` | `false` | `developmentonly` `clientdll` |  |
| `cl_csgo_shoot_trim_input_frames` | `true` | `developmentonly` `clientdll` |  |
| `cl_deathcam_audio_mix_phase1_fade_amount` | `0.150000` | `clientdll` `release` | Sets the amount of ducking to do on death cam fade out. When set to 1, full DeathFadeLayer is applied. |
| `cl_deathcam_audio_mix_phase1_fade_time` | `2.000000` | `clientdll` `release` | Sets the amount of time we fade out over. |
| `cl_deathcam_audio_mix_phase2_fade_amount` | `0.500000` | `clientdll` `release` | Sets the amount of ducking to do on death cam fade out. When set to 1, full DeathFadeLayer is applied. |
| `cl_deathcam_audio_mix_phase2_fade_time` | `0.400000` | `clientdll` `release` | Sets the amount of time we fade out over. |
| `cl_deathcampanel_position_dynamic` | `1` | `clientdll` `archive` | Turn on/off deathcam's kill panel dynamic Y movement |
| `cl_deathnotices_show_numbers` | `0` | `clientdll` `release` | 0: default; 1: draw names as just numbers; 2: append number on killer and victim to the name |
| `cl_debounce_zoom` | `true` | `clientdll` `archive` `userinfo` `per_user` | Whether or not to disable holding secondary fire to cycle zoom levels |
| `cl_debug_force_push_to_talk` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_debug_overlay_fullposition` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_debug_precipitation_surface_graph` | `false` | `clientdll` `replicated` `cheat` | When true, use the surface graph to pass in positions for rainfall.
 |
| `cl_debug_round_stat_submission` | `false` | `developmentonly` `clientdll` |  |
| `cl_debugviewangle` | `false` | `developmentonly` `clientdll` | Plots view angles yaw at various stages of the frame/tick in Tracy. |
| `cl_demo_predict` | `1` | `clientdll` `release` | Enable 'TrueView' when watching a demo, which attempts to recreate the client's experience more accurately.  0=disable, 1=only if demo version match, 2=always |
| `cl_demo_steadycam_blendframes` | `5` | `developmentonly` `clientdll` `defensive` | blend over this many frames |
| `cl_demo_steadycam_deflection` | `5.000000` | `developmentonly` `clientdll` `defensive` | if camera orientation changes this much update orientation |
| `cl_demo_steadycam_enable` | `0` | `developmentonly` `clientdll` `defensive` | Stabilize camera orientation/position during demo playback.  1 == remove roll, 2 == steadycam |
| `cl_demo_steadycam_radius` | `16.000000` | `developmentonly` `clientdll` `defensive` | if camera moves this much from last anchor update anchor |
| `cl_demo_view_offset_left` | `0.000000` | `developmentonly` `clientdll` `defensive` | View offset during demo playback (+/- 1.25 is a good default for human average left/right eye offset) |
| `cl_demoviewoverride` | `0.000000` | `developmentonly` `clientdll` `defensive` | Override view during demo playback |
| `cl_disable_deathcam_audio_mix_fade_out` | `false` | `clientdll` `release` | When set to true, disables audio being silenced while the death cam fades out. |
| `cl_disable_postprocessing` | `false` | `clientdll` `cheat` |  |
| `cl_disable_ragdolls` | `false` | `clientdll` `cheat` |  |
| `cl_disable_round_end_report` | `false` | `clientdll` `archive` `release` |  |
| `cl_display_flashbang_values` | `false` | `developmentonly` `clientdll` |  |
| `cl_display_game_events` | `false` | `clientdll` `cheat` |  |
| `cl_display_player_visibilty` | `false` | `developmentonly` `clientdll` |  |
| `cl_dm_buyrandomweapons` | `true` | `clientdll` `archive` `release` | Player will automatically receive a random weapon on spawn in deathmatch if this is set to 1 (otherwise, they will receive the last weapon) |
| `cl_dormant_spew` | `false` | `developmentonly` `clientdll` `defensive` | Spew state on when client entities become dormant or active. |
| `cl_draw_only_deathnotices` | `false` | `clientdll` `release` | For drawing only the crosshair and death notices (used for moviemaking) |
| `cl_draw_simulating_entities` | `false` | `clientdll` `cheat` |  |
| `cl_draw_simulating_entities_distance` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_drawhud` | `true` | `clientdll` `cheat` | Enable the rendering of the hud |
| `cl_drawhud_force_deathnotices` | `0` | `clientdll` `release` | 0: default; 1: draw deathnotices even if hud disabled; -1: force no deathnotices |
| `cl_drawhud_force_radar` | `0` | `clientdll` `release` | 0: default; 1: draw radar even if hud disabled; -1: force no radar |
| `cl_drawhud_force_teamid_overhead` | `0` | `clientdll` `release` | 0: default; 1: draw teamid even if hud disabled; -1: force no teamid |
| `cl_drawhud_specvote` | `true` | `clientdll` `release` | 1: default; 0: disables vote UI for spectators |
| `cl_embedded_stream_audio_volume` | `0.000000` | `clientdll` `hidden` `archive` | Embedded stream audio volume |
| `cl_embedded_stream_audio_volume_xmaster` | `true` | `clientdll` `hidden` `archive` | Whether embedded stream audio volume gets multiplied by master volume |
| `cl_embedded_stream_video_playing` | `0.000000` | `developmentonly` `clientdll` `hidden` `defensive` | Embedded stream video playing state |
| `cl_enable_party_voice` | `true` | `clientdll` `archive` `release` |  |
| `cl_ent_attachment_filter_substrings` | `` | `clientdll` `cheat` | If an attachment's name has any of the given substrings in it, it will be displayed. Substrings can be delimited by the ',' or '\|' character. |
| `cl_ent_joint_axis_size` | `4.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_ent_joint_filter_name` | `` | `clientdll` `cheat` | If a joint's entire name matches (case insensitive), it will be displayed. |
| `cl_ent_joint_filter_substrings` | `` | `clientdll` `cheat` | If a joint's name has any of the given substrings in it, it will be displayed. Substrings can be delimited by the ',' or '\|' character. |
| `cl_ent_joint_lines` | `true` | `clientdll` `cheat` | Draw a line between a rendered joint and its parent. |
| `cl_ent_joint_names` | `true` | `clientdll` `cheat` | Draw the name of a rendered joint. |
| `cl_ent_joint_only_ik_joints` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_ent_joint_use_bind_pose` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_ent_pivot_size` | `20.000000` | `clientdll` `archive` `cheat` |  |
| `cl_ent_show_contexts` | `false` | `clientdll` `cheat` | Show entity contexts in ent_text display |
| `cl_ent_showonlyattachment` | `` | `clientdll` `cheat` |  |
| `cl_ent_showonlyhitbox` | `-1` | `clientdll` `cheat` |  |
| `cl_ent_skeleton_only_ik_joints` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_ent_text_flags_active` | `-1` | `clientdll` `archive` `cheat` |  |
| `cl_ent_text_no_name_really_i_mean_it` | `false` | `clientdll` `cheat` |  |
| `cl_error_report_time` | `0.000000` | `clientdll` `release` | Minimum time in seconds that must elapse before printing prediction error summary. 0 to disable. |
| `cl_extrapolate` | `true` | `clientdll` `cheat` | Enable/disable extrapolation if interpolation history runs out. |
| `cl_extrapolate_amount` | `0.250000` | `clientdll` `cheat` | Set how many seconds the client will extrapolate entities for. |
| `cl_fake_timeout` | `false` | `developmentonly` `clientdll` |  |
| `cl_fasttempentcollision` | `5` | `developmentonly` `clientdll` `defensive` |  |
| `cl_firstperson_legs` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_firstperson_legs_aoproxy` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_fixedcrosshairgap` | `3.000000` | `clientdll` `archive` `per_user` | For crosshair style 1: How big to make the gap between the pips in the fixed crosshair |
| `cl_force_spec_hud_color_to_team` | `true` | `clientdll` `archive` | Spec hud color setting is always team/teammate |
| `cl_frametime_summary_report_detailed` | `true` | `clientdll` `release` | When a perf report is dumped at the end of the session, should it be detailed? |
| `cl_globallight_debug` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_depth_bias` | `-999.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_expansion` | `200.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_freeze` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_orig_calc_frustum` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_shadow_mode` | `2` | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_slope_scale_depth_bias` | `-999.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_use_alt_focus_region` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_use_optimized_calc_frustum` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_use_shaadow_near_offset` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_world_bottom_height` | `0.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_globallight_world_top_height` | `4096.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_glow_brightness` | `1.000000` | `clientdll` `cheat` | Brightness of player halos |
| `cl_glow_item_far_b` | `1.000000` | `clientdll` `release` |  |
| `cl_glow_item_far_g` | `0.400000` | `clientdll` `release` |  |
| `cl_glow_item_far_r` | `0.300000` | `clientdll` `release` |  |
| `cl_graphics_driver_warning_dont_show_again` | `false` | `clientdll` `archive` `release` | Graphics driver recommendation (NVIDIA 581.80 / AMD 23.11.1) |
| `cl_grenadecrosshair_decoy` | `true` | `clientdll` `archive` `per_user` | Is the grenade crosshair enabled |
| `cl_grenadecrosshair_explosive` | `true` | `clientdll` `archive` `per_user` | Is the grenade crosshair enabled |
| `cl_grenadecrosshair_fire` | `true` | `clientdll` `archive` `per_user` | Is the grenade crosshair enabled |
| `cl_grenadecrosshair_flash` | `true` | `clientdll` `archive` `per_user` | Is the grenade crosshair enabled |
| `cl_grenadecrosshair_keepusercrosshair` | `true` | `clientdll` `archive` `per_user` | Keep the user's crosshair when the grenade crosshair is enabled |
| `cl_grenadecrosshair_smoke` | `true` | `clientdll` `archive` `per_user` | Is the grenade crosshair enabled |
| `cl_grenadecrosshair_tickinterval` | `10.000000` | `developmentonly` `clientdll` |  |
| `cl_grenadecrosshair_ticklabels` | `true` | `developmentonly` `clientdll` |  |
| `cl_grenadecrosshair_tickscaling` | `1.100000` | `developmentonly` `clientdll` |  |
| `cl_grenadecrosshairdelay_decoy` | `2.000000` | `clientdll` `archive` `per_user` | How long should the pin be pulled for before showing the grenade crosshair |
| `cl_grenadecrosshairdelay_explosive` | `2.000000` | `clientdll` `archive` `per_user` | How long should the pin be pulled for before showing the grenade crosshair |
| `cl_grenadecrosshairdelay_fire` | `2.000000` | `clientdll` `archive` `per_user` | How long should the pin be pulled for before showing the grenade crosshair |
| `cl_grenadecrosshairdelay_flash` | `2.000000` | `clientdll` `archive` `per_user` | How long should the pin be pulled for before showing the grenade crosshair |
| `cl_grenadecrosshairdelay_smoke` | `2.000000` | `clientdll` `archive` `per_user` | How long should the pin be pulled for before showing the grenade crosshair |
| `cl_hide_avatar_images` | `0` | `clientdll` `archive` | Hide avatar images for other players. 
	0 - Off.
	1 - Block All
	2 - Block all but friends |
| `cl_highlights_hud_playback` | `0` | `clientdll` `hidden` `release` | Highlights hud playback |
| `cl_hitbox_debug` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_hold_game_events_force_delay_ticks` | `0` | `developmentonly` `clientdll` `defensive` | Debugging convar to force late dispatch of game events. |
| `cl_hold_game_events_until_server_tick` | `true` | `developmentonly` `clientdll` `defensive` | Holds game events until client has received the tick the event was fired on. |
| `cl_http_log_enable` | `false` | `clientdll` `dontrecord` `release` `clientcmd_can_execute` | Allows sending HTTP log from client main menu. |
| `cl_hud_color` | `0` | `clientdll` `archive` `release` | 0 = team color, 1 =  white, 2 = bright white, 3 = light blue, 4 = blue, 5 = purple, 6 = red, 7 = orange, 8 = yellow, 9 = green, 10 = aqua, 11 = pink, 12 = teammate color. |
| `cl_hud_radar_background_alpha` | `0.627000` | `clientdll` `archive` `release` |  |
| `cl_hud_radar_blur_background` | `true` | `clientdll` `archive` `release` | Blurs the radar background. |
| `cl_hud_radar_map_additive` | `true` | `clientdll` `archive` `release` | Blend Hud radar map additively on top of background. |
| `cl_hud_radar_scale` | `1.000000` | `clientdll` `archive` `release` |  |
| `cl_hud_telemetry_frametime_poor` | `100.000000` | `clientdll` `archive` `release` | Frame time greater than this is considered 'poor'. |
| `cl_hud_telemetry_frametime_show` | `1` | `clientdll` `archive` `release` | Show frame time (FPS) in the HUD.  0=never, 1=only if poor, 2=always |
| `cl_hud_telemetry_net_detailed` | `0` | `clientdll` `archive` `release` | Show breakdown network misdelivery (loss, late delivery, and peak jitter).  0=never, 1=only in poor network conditions, 2=always |
| `cl_hud_telemetry_net_misdelivery_poor` | `2.000000` | `clientdll` `archive` `release` | Packet delivery anomaly rate (0..100) higher than this is considered 'poor'. |
| `cl_hud_telemetry_net_misdelivery_show` | `1` | `clientdll` `archive` `release` | Show percentage of user commands & server snapshots that are missed due to network conditions.  0=never, 1=only in poor conditions, 2=always |
| `cl_hud_telemetry_net_quality_graph_show` | `0` | `clientdll` `archive` `release` | Show packet jitter and netframe loss/reordering in the HUD.  0=never, 1=only in poor conditions, 2=always |
| `cl_hud_telemetry_ping_poor` | `100.000000` | `clientdll` `archive` `release` | Ping higher than this (ms) is considered 'poor'. |
| `cl_hud_telemetry_ping_show` | `1` | `clientdll` `archive` `release` | Show ping in the HUD.  0=never, 1=only in poor conditions, 2=always |
| `cl_hud_telemetry_serverrecvmargin_graph_show` | `0` | `clientdll` `archive` `release` | Show graph of the server recv margin in the HUD.  (How early/late user commands are arriving at the server before they are executed.)   0=never, 1=only when there are command queue problems, 2=always |
| `cl_import_csgo_config` | `true` | `clientdll` `archive` `release` |  |
| `cl_inferno_bodyburn` | `true` | `developmentonly` `clientdll` |  |
| `cl_instant_death_anim` | `false` | `developmentonly` `clientdll` |  |
| `cl_interp_ag2_for_non_ag2_entities` | `true` | `developmentonly` `clientdll` |  |
| `cl_interp_all` | `false` | `developmentonly` `clientdll` `defensive` | Disable interpolation list optimizations. |
| `cl_interp_animationvars` | `true` | `developmentonly` `clientdll` `defensive` | Interpolate LATCH_ANIMATION_BIT vars if interpolation interval is greater than simulation interval |
| `cl_interp_hermite` | `true` | `clientdll` `cheat` | Set to zero do disable hermite interpolation. |
| `cl_interp_npcs` | `0.000000` | `developmentonly` `clientdll` `defensive` | Interpolate NPC positions starting this many seconds in past (or the value as per cl_interp_ratio, if greater) |
| `cl_interp_parallel` | `false` | `developmentonly` `clientdll` `defensive` | Run interpolation in parallel for entities with no children. |
| `cl_interp_ratio` | `2.000000` | `clientdll` `userinfo` | Set number of client simulation interpolation ticks. |
| `cl_interp_simulationvars` | `true` | `developmentonly` `clientdll` `defensive` | Interpolate LATCH_SIMULATION_BIT vars if interpolation interval is greater than animation interval |
| `cl_interp_threadmodeticks` | `0` | `developmentonly` `clientdll` `defensive` | Additional interpolation ticks to use when interpolating with threaded engine mode set. |
| `cl_interpolate` | `true` | `developmentonly` `clientdll` `userinfo` |  |
| `cl_interpolate_report` | `false` | `clientdll` `archive` | Enable to show interpolation profile timing
 |
| `cl_inv_volatile_limits` | `0:0` | `clientdll` `archive` |  |
| `cl_inventory_debug_tooltip` | `false` | `clientdll` `release` |  |
| `cl_inventory_radial_immediate_select` | `true` | `clientdll` `archive` `per_user` | In inventory selection radials. Select weapons the moment the cursor highlights them. Otherwise, only select the selected item on exit. |
| `cl_inventory_radial_tap_to_cycle` | `true` | `clientdll` `archive` `per_user` | In inventory selection radials. Select weapons the moment the cursor highlights them. Otherwise, only select the selected item on exit. |
| `cl_inventory_saved_filter2` | `all` | `clientdll` `archive` `release` |  |
| `cl_inventory_saved_sort2` | `inv_sort_age` | `clientdll` `archive` `release` |  |
| `cl_invites_only_friends` | `false` | `clientdll` `archive` `release` | If turned on, will ignore in-game invites from recent teammates or other non-friends |
| `cl_invites_only_mainmenu` | `false` | `clientdll` `archive` `release` | If turned on, will ignore all invites when user is playing a match |
| `cl_ironsight_dot_scale` | `1.000000` | `clientdll` `archive` `per_user` | Ironsight dot scale |
| `cl_ironsight_filter_alpha` | `1.000000` | `developmentonly` `clientdll` | Ironsight filter alpha |
| `cl_ironsight_min_channel_color` | `0.300000` | `developmentonly` `clientdll` | Ironsight min channel color value |
| `cl_ironsight_usecrosshaircolor` | `false` | `clientdll` `archive` `per_user` | Should the scope dot match the user's crosshair color |
| `cl_itemimages_dynamically_generated` | `2` | `clientdll` `archive` `release` | 2: use render-targets; 0: disk assets only |
| `cl_jitter_bad_threshold_up` | `0.000000` | `reference` |  |
| `cl_lagcompensation_test_auto_target` | `false` | `developmentonly` `clientdll` | Auto-pick value of cl_lagcompensation_test_target. |
| `cl_lagcompensation_test_target` | `-1` | `developmentonly` `clientdll` | Player whose head is tracked to test lag compensation. |
| `cl_latch_report` | `false` | `clientdll` `archive` | Enable to output stats about latching |
| `cl_leveloverview` | `0.000000` | `clientdll` `cheat` |  |
| `cl_lightquery_debug` | `false` | `clientdll` `cheat` |  |
| `cl_loadout_saved_sort` | `inv_sort_age` | `clientdll` `archive` `release` |  |
| `cl_lock_camera` | `false` | `clientdll` `cheat` |  |
| `cl_low_latency_vsync_recommendation_dont_show_again` | `false` | `clientdll` `archive` `release` |  |
| `cl_major_store_watch_list` | `` | `clientdll` `archive` |  |
| `cl_map_preview_debug_jitter` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_massreport` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_matchlist_controlroom_aid` | `0` | `clientdll` `hidden` `release` |  |
| `cl_max_particle_pvs_aabb_edge_length` | `0.000000` | `release` |  |
| `cl_min_china_movie_time` | `6.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_min_movie_time` | `4.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_mute_all_but_friends_and_party` | `0` | `clientdll` `archive` | Only allow communication from friends and matchmaking party members. Set to 1 to apply the in non-competitive game modes. Set to 2 will apply the setting in all modes.
 |
| `cl_mute_enemy_team` | `false` | `clientdll` `archive` | Block all communication from players on the enemy team. |
| `cl_mute_player_after_reporting_abuse` | `true` | `developmentonly` `clientdll` | Mute players reported for abuse automatically. |
| `cl_net_buffer_ticks` | `0` | `clientdll` `archive` `release` | Number of ticks of delay for server snapshots and user commands.  This value controls the value of cl_interp_ratio, which you should not modify directly. |
| `cl_net_buffer_ticks_use_interp` | `false` | `clientdll` `release` | If false, we smooth over packet loss by adjusting the clock synchronization to buffer packets.  If true, we process packets immediately and use cl_interp to delay their effects |
| `cl_net_showeventlisteners` | `false` | `developmentonly` `clientdll` `defensive` | Show listening addition/removals |
| `cl_net_showevents` | `0` | `developmentonly` `clientdll` `defensive` | Dump game events to console (1=client only, 2=all). |
| `cl_new_user_phase` | `0` | `clientdll` `archive` `release` | 0: Not Started, 1: Needs Training, 2: Training Complete, -1: Disabled |
| `cl_obs_interp_enable` | `true` | `clientdll` `archive` | Enables interpolation between observer targets |
| `cl_obs_interp_speed` | `1.000000` | `clientdll` `archive` | Spectator camera interpolation speed |
| `cl_observed_bot_crosshair` | `2` | `clientdll` `archive` `release` | Control the crosshair shown when observing a bot. 0: Show player crosshair. 1: Show player crosshair only when bot can be taken over, otherwise show default.. 2: Always show default crosshair for bots. |
| `cl_paintkit_override` | `` | `clientdll` `cheat` `release` |  |
| `cl_panel_freeze_time_after_press` | `0.500000` | `developmentonly` `clientdll` `defensive` | time to freeze mouse/pointer motion after a mouse button press |
| `cl_particle_batch_mode` | `1` | `developmentonly` `defensive` |  |
| `cl_particle_create_duplicate_work_for_profiling` | `0` | `developmentonly` | Create and destroy N particle systems for every one created normally |
| `cl_particle_fallback_base` | `0` | `developmentonly` `defensive` | Base for falling back to cheaper effects under load. |
| `cl_particle_fallback_multiplier` | `0.000000` | `developmentonly` `defensive` | Multiplier for falling back to cheaper effects under load. |
| `cl_particle_log_creates` | `false` | `developmentonly` `defensive` | Print debug message every time a particle collection is created |
| `cl_particle_max_count` | `0` | `developmentonly` `defensive` |  |
| `cl_particle_newinit` | `true` | `developmentonly` | turn on optimized particle init |
| `cl_particle_retire_cost` | `0.000000` | `cheat` |  |
| `cl_particle_sim_fallback_base_multiplier` | `5.000000` | `developmentonly` `defensive` | How aggressive the switch to fallbacks will be depending on how far over the cl_particle_sim_fallback_threshold_ms the sim time is.  Higher numbers are more aggressive. |
| `cl_particle_sim_fallback_threshold_ms` | `6.000000` | `developmentonly` `defensive` | Amount of simulation time that can elapse before new systems start falling back to cheaper versions |
| `cl_particle_simulate` | `true` | `cheat` | Enables/Disables Particle Simulation |
| `cl_pclass` | `` | `clientdll` `cheat` | Dump entity by prediction classname. |
| `cl_pdump` | `-1` | `clientdll` `cheat` | Dump info about this entity to screen. |
| `cl_phys_animated_hierarchy` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_phys_assume_fixed_tick_interval` | `true` | `developmentonly` `clientdll` | If true, we assume the client uses a fixed tickrate like the server (which may not always be true). If false, we recalculate the number of physics substeps in each client tick based on the actual elapsed time in the tick. |
| `cl_phys_block_dist` | `1.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_phys_block_fraction` | `0.100000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_phys_debug_callback_entities` | `false` | `clientdll` `cheat` | Print all entities that get touch callbacks. Each entity is printed only once. |
| `cl_phys_enabled` | `true` | `clientdll` `cheat` | Enable all physics simulation |
| `cl_phys_networked_start_sleep` | `false` | `developmentonly` `clientdll` |  |
| `cl_phys_sleep_enable` | `true` | `clientdll` `cheat` | Enable sleeping for dynamic physics bodies. |
| `cl_phys_sound_disable_impact_sounds_under_hard_threshold` | `false` | `clientdll` `cheat` | if true, impact sounds wont play if no soft impact sound is present and the impact is below the hard velocity threshold. |
| `cl_phys_stop_at_collision` | `` | `clientdll` `cheat` |  |
| `cl_phys_timescale` | `1.000000` | `developmentonly` `clientdll` `defensive` | Scale time for physics |
| `cl_phys_visualize_awake` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_ping_fade_deadzone` | `60.000000` | `clientdll` `archive` `release` | Distance from the crosshair over which the ping is completely invisible |
| `cl_ping_fade_distance` | `300.000000` | `clientdll` `archive` `release` | Distance from the crosshair over which the ping fades |
| `cl_pitchdown` | `89.000000` | `clientdll` `cheat` |  |
| `cl_pitchspeed` | `225.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_pitchup` | `89.000000` | `clientdll` `cheat` |  |
| `cl_player_ping_mute` | `0` | `clientdll` `archive` `release` | If 1, player pinging will make a sound, if 0, pings will be silent |
| `cl_player_ragdolls_collide` | `false` | `clientdll` `cheat` `release` |  |
| `cl_player_visibility_far` | `700.000000` | `developmentonly` `clientdll` | distance at which proxy scale is maximized |
| `cl_player_visibility_far_scale` | `1.300000` | `developmentonly` `clientdll` | proxy scale multiplier at max dist (is 1.0 at mindist) |
| `cl_player_visibility_near` | `200.000000` | `developmentonly` `clientdll` | cull characters nearer than this |
| `cl_player_visibility_show_stencil_proxy` | `false` | `developmentonly` `clientdll` |  |
| `cl_player_visibility_stencil_bloat_amount` | `1.400000` | `developmentonly` `clientdll` |  |
| `cl_player_visibility_stencil_proxy_min_dist` | `3.000000` | `developmentonly` `clientdll` |  |
| `cl_player_visibility_stencil_proxy_min_dist_box` | `1.000000` | `developmentonly` `clientdll` |  |
| `cl_player_visibility_stencil_proxy_type` | `1` | `developmentonly` `clientdll` | 0 - box, 1 - dodecahedron |
| `cl_playerslot_in_names` | `false` | `clientdll` `cheat` `release` | prepend controller playerslot to names for debugging |
| `cl_pred_always_latch` | `false` | `clientdll` `release` |  |
| `cl_pred_build_verbose` | `false` | `developmentonly` `clientdll` `defensive` | Verbose spew when building prediction optimized data runs. |
| `cl_pred_checkstuck` | `false` | `developmentonly` `clientdll` | Perform the additional 'stuck' traces on the client side during prediction. |
| `cl_pred_optimize` | `true` | `developmentonly` `clientdll` `defensive` | Optimize for not repredicting if there were no errors |
| `cl_pred_parallel_postnetwork` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_pred_print_every_cmd` | `false` | `clientdll` `release` | Print something every time we predict a command |
| `cl_predict_body_shot_fx` | `false` | `clientdll` `archive` `release` |  |
| `cl_predict_bomb_defusal` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_predict_head_shot_fx` | `false` | `clientdll` `archive` `release` |  |
| `cl_predict_kill_ragdolls` | `true` | `clientdll` `archive` `release` |  |
| `cl_predict_weapon_drop` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_prediction_savedata_postentitypacketreceived` | `false` | `clientdll` `release` | Experimental optimization.  If you are reading this in 2026, please delete this convar. |
| `cl_predictioncopy_runs` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_prefer_lefthanded` | `false` | `clientdll` `archive` `userinfo` `per_user` | Left handed preference |
| `cl_promoted_settings_acknowledged` | `0:0` | `clientdll` `archive` |  |
| `cl_quickinventory_filename` | `radial_quickinventory.txt` | `clientdll` `archive` `release` |  |
| `cl_quickinventory_lastinv` | `true` | `clientdll` `archive` `release` |  |
| `cl_quickinventory_line_update_speed` | `65.000000` | `clientdll` `archive` `release` |  |
| `cl_radar_always_centered` | `true` | `clientdll` `archive` `release` | If set to 0, the radar is maximally used. Otherwise the player is always centered, even at map extents. |
| `cl_radar_fast_transforms` | `true` | `developmentonly` `clientdll` | Faster way of placing icons on the mini map. |
| `cl_radar_icon_scale_min` | `0.600000` | `clientdll` `archive` `release` | Sets the minimum icon scale. Valid values are 0.4 to 1.25. |
| `cl_radar_rotate` | `true` | `clientdll` `archive` `release` | 1 |
| `cl_radar_scale` | `0.700000` | `clientdll` `archive` `release` | Sets the radar scale. Valid values are 0.25 to 1.0. |
| `cl_radar_scale_alternate` | `1.000000` | `clientdll` `archive` `release` | Sets the alternate radar scale. Valid values are 0.25 to 1.0. |
| `cl_radar_scale_dynamic` | `false` | `clientdll` `archive` `release` | Toggles between a radar that scales dynamically to encompass all the detected elements on the map. |
| `cl_radar_show_all_players_when_spectating` | `true` | `clientdll` `archive` `release` | Set all players visible on radar when spectating, regardless of whether they have been spotted. |
| `cl_radar_square_always` | `false` | `clientdll` `archive` `release` | If set, the radar will always be square. |
| `cl_radar_square_when_spectating` | `true` | `clientdll` `archive` `release` | If set, the radar will be square when spectating. |
| `cl_radar_square_with_scoreboard` | `true` | `clientdll` `archive` `release` | If set, the radar will toggle to square when the scoreboard is visible. |
| `cl_radial_coyote_time` | `0.150000` | `developmentonly` `clientdll` | Selection lenience: How long in seconds the last selected radial segment is used if no segment is selected. |
| `cl_radial_menu_icon_radius` | `200.000000` | `developmentonly` `clientdll` |  |
| `cl_radial_menu_tap_duration` | `0.200000` | `developmentonly` `clientdll` | If nothing in a radial menu is selected, and the button engaging the radial menu is released within this duration, fallback on the radial's tap functionality |
| `cl_radial_radio_tab` | `0` | `clientdll` `release` |  |
| `cl_radial_radio_tab_0_text_1` | `#Chatwheel_quiet` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_2` | `#Chatwheel_requestecoround` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_3` | `#Chatwheel_bplan` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_4` | `#Chatwheel_requestweapon` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_5` | `#Chatwheel_midplan` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_6` | `#Chatwheel_droppedbomb` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_7` | `#Chatwheel_aplan` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_0_text_8` | `#Chatwheel_requestspend` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_1` | `#Chatwheel_bombcarrierspotted` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_2` | `#Chatwheel_requestecoround` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_3` | `#Chatwheel_multipleenemieshere` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_4` | `#Chatwheel_requestweapon` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_5` | `#Chatwheel_rotatetome` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_6` | `#Chatwheel_ihavethebomb` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_7` | `#Chatwheel_oneenemyhere` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_1_text_8` | `#Chatwheel_requestspend` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_1` | `#Chatwheel_bombcarrierspotted` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_2` | `#Chatwheel_requestecoround` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_3` | `#Chatwheel_multipleenemieshere` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_4` | `#Chatwheel_requestweapon` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_5` | `#Chatwheel_rotatetome` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_6` | `#Chatwheel_ihavethebomb` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_7` | `#Chatwheel_oneenemyhere` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tab_2_text_8` | `#Chatwheel_requestspend` | `clientdll` `archive` `release` |  |
| `cl_radial_radio_tap_to_ping` | `true` | `clientdll` `archive` `release` | When tapping the radial radio button, leave a ping if nothing is selected within the time in seconds set in cl_radial_menu_tap_duration |
| `cl_radial_radio_version_reset` | `2` | `clientdll` `archive` `release` |  |
| `cl_radialmenu_deadzone_size` | `0.400000` | `clientdll` `release` |  |
| `cl_radialmenu_deadzone_size_joystick` | `0.170000` | `clientdll` `archive` `release` |  |
| `cl_ragdoll_default_scale` | `1.000000` | `developmentonly` `clientdll` |  |
| `cl_ragdoll_limit` | `20` | `clientdll` `archive` | Maximum number of ragdolls to show (-1 disables limit) |
| `cl_ragdoll_lru_debug` | `false` | `clientdll` `replicated` `cheat` |  |
| `cl_ragdoll_physics_enable` | `1` | `developmentonly` `clientdll` `defensive` | Enable/disable ragdoll physics. |
| `cl_ragdoll_reload` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_ragdoll_workaround_threshold` | `4.000000` | `clientdll` `release` | Mainly cosmetic, client-only effect: when client doesn't know the last position of another player that spawns a ragdoll, the ragdoll creation is simplified and ragdoll is created in the right place. If you increase this significantly, ragdoll positions on your client may be dramatically wrong, but it won't affect other clients |
| `cl_random_taser_bone_y` | `-1.000000` | `developmentonly` `clientdll` `defensive` | The Y position used for the random taser force. |
| `cl_random_taser_force_y` | `-1.000000` | `developmentonly` `clientdll` `defensive` | The Y position used for the random taser force. |
| `cl_random_taser_power` | `4000.000000` | `developmentonly` `clientdll` `defensive` | Power used when applying the taser effect. |
| `cl_rebuy` | `` | `clientdll` `release` | The order in which rebuy will attempt to repurchase items |
| `cl_redemption_reset_timestamp` | `0` | `clientdll` `archive` `release` |  |
| `cl_refresh_rate_recommendation_dont_show_again` | `false` | `clientdll` `archive` `release` |  |
| `cl_retire_low_priority_lights` | `false` | `developmentonly` `clientdll` `defensive` | Low priority dlights are replaced by high priority ones |
| `cl_sanitize_muted_players` | `true` | `clientdll` `release` | Hide names and avatars of muted players. |
| `cl_sanitize_player_names` | `false` | `clientdll` `archive` | Replace names of other players with something non-offensive. |
| `cl_sceneentity_debug` | `false` | `developmentonly` `clientdll` `defensive` | Display all thinking scene entities and its data. |
| `cl_scoreboard_mouse_enable_binding` | `+attack2` | `clientdll` `archive` | Name of the binding to enable mouse selection in the scoreboard |
| `cl_scoreboard_survivors_always_on` | `false` | `clientdll` `archive` `release` |  |
| `cl_scoreboard_toggle_enable` | `false` | `developmentonly` `clientdll` |  |
| `cl_screenmessage_notifytime` | `8.000000` | `developmentonly` `clientdll` `defensive` | How long to display screen message text |
| `cl_script_attach_debugger_at_startup` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_script_break_in_native_debugger_on_error` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_search_key_token` | `` | `clientdll` `hidden` `release` | Development search key token. |
| `cl_sequence_debug` | `-1` | `developmentonly` `clientdll` `defensive` |  |
| `cl_sequence_debug2` | `-1` | `developmentonly` `clientdll` `defensive` |  |
| `cl_sequence_model_substring` | `` | `developmentonly` `clientdll` `defensive` |  |
| `cl_server_graphic1_enable` | `true` | `clientdll` `release` | When enabled, 360x60 (<16kb) image file will be displayed to on-server spectators. |
| `cl_server_graphic2_enable` | `true` | `clientdll` `release` | When enabled, 220x45 (<16kb) image file will be displayed to on-server spectators. |
| `cl_session` | `` | `reference` |  |
| `cl_show_bombs` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_show_camera_position` | `false` | `developmentonly` `clientdll` |  |
| `cl_show_clan_in_death_notice` | `true` | `clientdll` `archive` `release` | Is set, the clan name will show next to player names in the death notices. |
| `cl_show_enemy_avatar_colors` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_show_equipment_value` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_show_equipped_character_for_player_avatars` | `false` | `clientdll` `archive` |  |
| `cl_show_head_trajectory` | `0.000000` | `developmentonly` `clientdll` |  |
| `cl_show_matchmaking_stat_spew` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_show_observer_crosshair` | `2` | `clientdll` `archive` `release` | Show the crosshair of the player being observed. 0: off 1: friends and party 2: everyone  |
| `cl_show_playernames_max_chars_console` | `false` | `developmentonly` `clientdll` | Shows all player names (including bots) as 16 W's. |
| `cl_show_quest_info` | `false` | `developmentonly` `clientdll` |  |
| `cl_show_splashes` | `true` | `developmentonly` `clientdll` |  |
| `cl_showerror` | `0` | `clientdll` `release` | Show prediction errors, 2 for above plus detailed field deltas, 3 to filter out serverside known prediction errors, -entindex for specific entity. |
| `cl_showfps` | `0` | `clientdll` `release` | Draw fps meter at top of screen (1 = fps, 2 = smooth fps, 3 = server MS, 4 = Show FPS and Log to file ) |
| `cl_showframenumber` | `false` | `clientdll` `release` | Show current framenumber |
| `cl_showloadout` | `true` | `clientdll` `archive` `per_user` | Toggles display of current loadout. |
| `cl_showmem` | `0` | `clientdll` `release` | Draw approximate memory use at top of screen |
| `cl_showpos` | `0` | `clientdll` `cheat` `release` | Draw current position at top of screen |
| `cl_showtextmsg` | `true` | `developmentonly` `clientdll` `defensive` | Enable/disable text messages printing on the screen. |
| `cl_showtick` | `0` | `clientdll` `release` | Show current tick/time values.  Bitmask:  1='render time'  2='GameTime'   4=time of predicted entities  8=offset of predicted entities    (-1 means 'everything') |
| `cl_showusercmd` | `false` | `developmentonly` `clientdll` `defensive` | Show user command encoding |
| `cl_silencer_mode` | `0` | `clientdll` `archive` `userinfo` `per_user` | 0: cannot detach; 1: press secondary fire to detach |
| `cl_simulate_dormant_entities` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_skeleton_instance_smear_boneflags` | `false` | `clientdll` `cheat` | Smear boneflags across the model.  Costs computation, but tests to make sure your bone flags are consistent. |
| `cl_skip_hierarchy_update_for_unchanged_entities` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` | Skip updating hierarchy information in PostDataUpdate for entities that have not changed |
| `cl_skip_update_animations` | `false` | `developmentonly` `clientdll` | Enable to skip game animations |
| `cl_smoke_edge_feather` | `21.000000` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `cl_smoke_lower_speed` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `cl_smoke_origin_height` | `68.000000` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `cl_smoke_torus_ring_radius` | `61.000000` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `cl_smoke_torus_ring_subradius` | `88.000000` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `cl_smoke_volume_growth` | `1.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_smoke_volumeprop` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_smooth` | `true` | `developmentonly` `clientdll` `defensive` | Smooth view/eye origin after prediction errors |
| `cl_smooth_draw_debug` | `false` | `clientdll` `cheat` |  |
| `cl_smooth_root_catchup_factor` | `0.210000` | `clientdll` `cheat` |  |
| `cl_smooth_root_max_accel` | `1000.000000` | `clientdll` `cheat` |  |
| `cl_smooth_root_origin_coeff` | `100.000000` | `clientdll` `cheat` |  |
| `cl_smooth_root_timehorizon` | `0.125000` | `clientdll` `cheat` |  |
| `cl_smooth_root_velocity_coeff` | `20.000000` | `clientdll` `cheat` |  |
| `cl_smooth_targetspeed` | `150.000000` | `clientdll` `release` |  |
| `cl_smoothtime` | `0.200000` | `developmentonly` `clientdll` `defensive` | Smooth client's view after prediction error over this many seconds |
| `cl_snd_cast_clear` | `true` | `developmentonly` `defensive` |  |
| `cl_snd_cast_retrigger` | `true` | `developmentonly` `defensive` |  |
| `cl_snd_new_visualize` | `false` | `clientdll` `cheat` | Displays soundevent name played at it's 3d position |
| `cl_sniper_auto_rezoom` | `true` | `clientdll` `archive` `userinfo` `per_user` | Auto-rezoom snipers after a shot |
| `cl_sniper_delay_unscope` | `false` | `clientdll` `archive` `release` |  |
| `cl_sniper_show_inaccuracy` | `true` | `clientdll` `archive` `release` |  |
| `cl_spec_show_bindings` | `true` | `clientdll` `release` `clientcmd_can_execute` | Toggle the visibility of the spectator bindings. |
| `cl_spec_stats` | `true` | `clientdll` `release` |  |
| `cl_spec_use_tournament_content_standards` | `false` | `clientdll` `release` |  |
| `cl_streams_image_sfurl` | `img://loadjpeg:(640x360):` | `developmentonly` `clientdll` | Format of Scaleform image representing the stream |
| `cl_streams_mytwitchtv_channel` | `http://www.twitch.tv/` | `developmentonly` `clientdll` | Twitch.tv account channel URL |
| `cl_streams_mytwitchtv_nolink` | `http://www.twitch.tv/settings/connections` | `developmentonly` `clientdll` | Twitch.tv account linking URL |
| `cl_streams_refresh_interval` | `300.000000` | `developmentonly` `clientdll` | How often to refresh streams list |
| `cl_streams_request_accept` | `application/vnd.twitchtv.v5+json` | `developmentonly` `clientdll` | Header for api request |
| `cl_streams_request_url` | `https://api.twitch.tv/helix/streams?game_id=32399&first=12` | `developmentonly` `clientdll` | Number of streams requested for display |
| `cl_streams_write_response_file` | `` | `developmentonly` `clientdll` | When set will save streams info file for diagnostics |
| `cl_svc_usercmds_delta_validate` | `false` | `developmentonly` `clientdll` | Validate consistency of delta-encoded user commands.  Requires server to have sv_cq_validate_encoded_svc_usercmds enabled. |
| `cl_teamcounter_playercount_instead_of_avatars` | `false` | `clientdll` `archive` `release` |  |
| `cl_teamid_overhead_colors_show` | `true` | `clientdll` `archive` `release` | Show team overhead id in teammate color |
| `cl_teamid_overhead_fade_near_crosshair` | `0.500000` | `clientdll` `archive` `release` | The amount to fade teamid when near the crosshair. Range is 0.0-1.0. 0: off |
| `cl_teamid_overhead_maxdist` | `6000` | `clientdll` `cheat` `per_user` | max distance at which the overhead team id icons will show |
| `cl_teamid_overhead_maxdist_spec` | `4000` | `clientdll` `cheat` `per_user` | max distance at which the overhead team id icons will show when a spectator |
| `cl_teamid_overhead_mode` | `3` | `clientdll` `archive` `release` | Always show team id over teammates. 0 = off, 1 = pips; 2 = +name, 3 = +equipment |
| `cl_teammate_color_1` | `136 206 245` | `developmentonly` `clientdll` `defensive` |  |
| `cl_teammate_color_2` | `0 158 128` | `developmentonly` `clientdll` `defensive` |  |
| `cl_teammate_color_3` | `241 228 65` | `developmentonly` `clientdll` `defensive` |  |
| `cl_teammate_color_4` | `230 128 42` | `developmentonly` `clientdll` `defensive` |  |
| `cl_teammate_color_5` | `189 44 150` | `developmentonly` `clientdll` `defensive` |  |
| `cl_teammate_colors_show` | `1` | `clientdll` `archive` `release` | In competitive, 1 = show teammates as separate colors in the radar, scoreboard, etc., 2 = show colors and letters |
| `cl_tracer_frequency_override` | `1` | `developmentonly` `clientdll` | Override tracer frequency (-1 to disable) |
| `cl_tracer_whiz_distance` | `72.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_tracer_whiz_infront_distance` | `32.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_track_aim_head_log_closest` | `false` | `developmentonly` `clientdll` | Log when closest distance to head was reached and what it was |
| `cl_track_aim_head_threshold` | `0.000000` | `developmentonly` `clientdll` | Notify render device when rendering a frame with enemy head within threshold distance |
| `cl_track_render_eye_angles` | `false` | `clientdll` `cheat` | Spew render eye angles |
| `cl_trueview_show_doa_predictions` | `true` | `clientdll` `release` | If true, trueview will recreate the original player experience, including commands that were predicted clientside but never executed on the server because the player was dead when they arrived. |
| `cl_trueview_show_status` | `2` | `clientdll` `release` | 0=Never; 1=Only if there is a problem; 2=always |
| `cl_ui_particles_destroy_when_not_painting` | `true` | `developmentonly` `clientdll` |  |
| `cl_use_entity_as_targetid` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_use_last_selected_weapon_slot_position` | `false` | `clientdll` `archive` `release` | Use the last selected weapon slot position when switching back to a weapon slot. |
| `cl_use_old_wearable_shoulddraw` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cl_use_opens_buy_menu` | `false` | `clientdll` `archive` `userinfo` `per_user` | Pressing the +use key will open the buy menu if in a buy zone (just as if you pressed the 'buy' key). |
| `cl_usercmd_showsize` | `false` | `reference` |  |
| `cl_versus_intro` | `true` | `clientdll` `archive` `release` |  |
| `cl_view_near_hud_player_eye_dist` | `20.000000` | `developmentonly` `clientdll` |  |
| `cl_view_near_other_player_eye_dist` | `16.000000` | `developmentonly` `clientdll` |  |
| `cl_viewing_vanity_loadout` | `false` | `gamedll` `clientdll` `userinfo` |  |
| `cl_viewmodelsclonedasworld` | `true` | `developmentonly` `clientdll` |  |
| `cl_voiceenabled` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `cl_voip_lobby_audio_volume` | `0` | `developmentonly` `clientdll` `hidden` | Lobby voip stream audio volume |
| `cl_vrr_recommendation_dont_show_again` | `false` | `clientdll` `archive` `release` |  |
| `cl_vsnd_morph_override_ease_enabled` | `true` | `developmentonly` `clientdll` `defensive` | Controls whether the compiled in vsnd morph data ease in/out values are used or values set from the convars (cl_vsnd_morph_override_ease_in, cl_vsnd_morph_override_ease_out) are used |
| `cl_vsnd_morph_override_ease_in` | `0.200000` | `developmentonly` `clientdll` `defensive` | If cl_enable_vsnd_morph_override_ease_enabled is true, ease into vsnd morph driven animation over the specified number of seconds. |
| `cl_vsnd_morph_override_ease_out` | `0.200000` | `developmentonly` `clientdll` `defensive` | If cl_enable_vsnd_morph_override_ease_enabled is true, ease out of vsnd morph driven animation over the specified number of seconds. |
| `cl_wallbang_heavy_threshold` | `22` | `clientdll` `cheat` `release` | The Threshold where to switch from Light to Heavy Wallbang tracer |
| `cl_weapon_debug_print_accuracy` | `false` | `developmentonly` `clientdll` `replicated` |  |
| `cl_weapon_debug_show_accuracy` | `0` | `clientdll` `cheat` `release` | Draws a circle representing the effective range with every shot. |
| `cl_weapon_debug_show_accuracy_duration` | `10.000000` | `clientdll` `cheat` `release` |  |
| `cl_weapon_selection_rarity_color` | `false` | `clientdll` `archive` `release` |  |
| `cl_workshop_map_download_timeout` | `120.000000` | `developmentonly` `clientdll` `defensive` |  |
| `cl_yawspeed` | `210.000000` | `developmentonly` `clientdll` `defensive` |  |
| `clear_debug_flags_on_death` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `closecaption` | `false` | `clientdll` `archive` `userinfo` | Enable close captioning. |
| `cloth_debug_draw` | `0` | `developmentonly` `clientdll` |  |
| `cloth_filter_transform_stateless` | `false` | `developmentonly` `defensive` | Enable the new, stateless version of FilterTransform |
| `cloth_ground_plane_thickness` | `3.000000` | `developmentonly` `defensive` | Raise ground by this much for all cloth that traces the ground; should be 0 ideally |
| `cloth_hudmodel_presettle` | `0` | `developmentonly` `clientdll` |  |
| `cloth_hudmodel_presettle_log` | `false` | `developmentonly` `clientdll` |  |
| `cloth_interp_rot` | `false` | `developmentonly` `clientdll` |  |
| `cloth_iv_dump` | `4` | `developmentonly` `clientdll` `defensive` |  |
| `cloth_iv_store_back` | `false` | `developmentonly` `clientdll` `replicated` `defensive` |  |
| `cloth_sim_on_tick` | `true` | `developmentonly` `clientdll` |  |
| `cloth_smooth_motion_correct` | `false` | `developmentonly` `clientdll` |  |
| `cloth_smooth_motion_extrapolate` | `0.000000` | `developmentonly` `clientdll` |  |
| `cloth_update` | `true` | `developmentonly` `clientdll` |  |
| `cojob_lock_hold_warning_threshold_ms` | `10000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | How long in milliseconds before we warn about lock hold duration |
| `cojob_max_no_yield_time_us` | `3000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Will spew if a job takes longer than the specified number of microseconds |
| `commentary` | `false` | `gamedll` `archive` | Desired commentary mode state. |
| `commentary_available` | `false` | `developmentonly` `gamedll` `defensive` | Automatically set by the game when a commentary file is available for the current map. |
| `commentary_node_use_viewfacing` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `composite_material_cache_count_max` | `16` | `developmentonly` `clientdll` |  |
| `composite_material_dump_images` | `false` | `developmentonly` `clientdll` |  |
| `composite_material_save_to_disk` | `false` | `developmentonly` `clientdll` |  |
| `composite_material_use_bc7` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `composite_material_use_gpu` | `true` | `developmentonly` `clientdll` |  |
| `composite_material_use_gpu_endpoint_optimization` | `false` | `developmentonly` `clientdll` |  |
| `composite_material_use_gpu_perceptual_error_metric` | `true` | `developmentonly` `clientdll` |  |
| `compositematerial_showdebugwindow` | `false` | `developmentonly` `clientdll` `archive` `replicated` `cheat` `menubar_item` | Source2/Composite Material Debug |
| `connect_lobby` | `0` | `developmentonly` `clientdll` `hidden` `defensive` | Sets the lobby ID to connect to on start. |
| `contributionscore_assist` | `1` | `gamedll` `release` `commandline_enforced` | amount of contribution score added for an assist |
| `contributionscore_assist_reqs` | `0` | `gamedll` `release` `commandline_enforced` | extra requirements to earn contribution score for an assist |
| `contributionscore_bomb_defuse_major` | `3` | `gamedll` `release` `commandline_enforced` | amount of contribution score for defusing a bomb while at least one enemy remains alive |
| `contributionscore_bomb_defuse_minor` | `1` | `gamedll` `release` `commandline_enforced` | amount of contribution score for defusing a bomb after eliminating enemy team |
| `contributionscore_bomb_exploded` | `1` | `gamedll` `release` `commandline_enforced` | amount of contribution score awarded to bomb planter and terrorists remaining alive if bomb explosion wins the round |
| `contributionscore_bomb_planted` | `2` | `gamedll` `release` `commandline_enforced` | amount of contribution score for planting a bomb |
| `contributionscore_cash_bundle` | `0` | `gamedll` `release` `commandline_enforced` | amount of contribution score for picking up a cash bundle |
| `contributionscore_crate_break` | `0` | `gamedll` `release` `commandline_enforced` | amount of contribution score for breaking an item crate |
| `contributionscore_hostage_kill` | `-2` | `gamedll` `release` `commandline_enforced` | amount of contribution score for killing a hostage, normally negative |
| `contributionscore_hostage_rescue_major` | `3` | `gamedll` `release` `commandline_enforced` | amount of contribution score added to rescuer per hostage rescued |
| `contributionscore_hostage_rescue_minor` | `1` | `gamedll` `release` `commandline_enforced` | amount of contribution score added to all alive CTs per hostage rescued |
| `contributionscore_kill` | `2` | `gamedll` `release` `commandline_enforced` | amount of contribution score added for a kill |
| `contributionscore_kill_factor` | `0.000000` | `gamedll` `release` `commandline_enforced` | percentage of victim's contribution score to award to their killer as a bonus |
| `contributionscore_kill_reqs` | `0` | `gamedll` `release` `commandline_enforced` | extra requirements to earn contribution score for a kill |
| `contributionscore_objective_kill` | `3` | `gamedll` `release` `commandline_enforced` | amount of contribution score added for an objective related kill |
| `contributionscore_participation` | `0` | `gamedll` `release` `commandline_enforced` | amount of contribution score awarded to players for active participation in the round |
| `contributionscore_suicide` | `-2` | `gamedll` `release` `commandline_enforced` | amount of contribution score for a suicide, normally negative |
| `contributionscore_team_kill` | `-2` | `gamedll` `release` `commandline_enforced` | amount of contribution score for a team kill, normally negative |
| `cpu_level` | `2` | `developmentonly` `clientdll` `defensive` | CPU Level - Default: High |
| `cq_buffer_bloat_msecs_max` | `0.000000` | `reference` |  |
| `cq_debug` | `0` | `developmentonly` `gamedll` `replicated` `defensive` | Verbose command queue logging. |
| `cq_dilation_percentage` | `5.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | When speeding up slowing down, this is how much |
| `cq_enable` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Run one usercmd per server tick and maintain a buffer.  Client speeds up/slows down it's usercmd tick rate to maintain server command queue buffering. |
| `cq_fake_starve` | `0` | `developmentonly` `gamedll` | if set, starve this many commands by discarding during process usercmds. |
| `cq_logging` | `false` | `gamedll` `release` | command queue logging of events. |
| `cq_logging_interval` | `0.000000` | `gamedll` `release` | command queue logging per player stats every N seconds, 0 to disable. |
| `cq_max_starved_substitute_commands` | `4` | `gamedll` `release` | Server will stop generating substitute commands if client hasn't sent one, after N in a row |
| `cq_print_every_command` | `false` | `gamedll` `release` | print every command as we execute it |
| `cq_runtests` | `false` | `developmentonly` `gamedll` |  |
| `cq_runtests_broadcast_info` | `false` | `developmentonly` `gamedll` | send message to remote client console when tests change. |
| `cq_runtests_interval` | `30.000000` | `developmentonly` `gamedll` |  |
| `crosshair` | `true` | `clientdll` `archive` `per_user` |  |
| `cs2_bomb_damage_showdebugwindow` | `false` | `developmentonly` `clientdll` `archive` `replicated` `cheat` `menubar_item` | CSGO/Bomb Damage |
| `cs_AssistDamageThreshold` | `25` | `developmentonly` `gamedll` | cs_AssistDamageThreshold defines the amount of damage needed to score an assist |
| `cs_ShowStateTransitions` | `-2` | `gamedll` `cheat` | cs_ShowStateTransitions <ent index or -1 for all>. Show player state transitions. |
| `cs_hostage_near_rescue_music_distance` | `2000.000000` | `gamedll` `cheat` |  |
| `cs_logtouchexpansion` | `-2` | `gamedll` `cheat` | cs_logtouchexpansion <ent index or -1 for all>. Log player touch expansion component. |
| `cs_minimap_create_output_size` | `1024` | `clientdll` `release` | Size of minimap texture generated with cs_minimap_create (512 default) |
| `cs_minimap_renderdoc_capture_enabled` | `false` | `developmentonly` `clientdll` `hidden` `cheat` |  |
| `cs_minimap_rendering_msaa_mode` | `2` | `developmentonly` `clientdll` `cheat` | MSAA mode used for minimap rendering 0-none, 1-2xMSAA, 2-4xMSAA, 3-6X, 4-8X, etc |
| `cs_steamvideo_max_kills_per_multikill` | `5` | `developmentonly` `clientdll` | Max number of kills for a single multikill event |
| `cs_steamvideo_max_time_between_multikill_events` | `5.000000` | `developmentonly` `clientdll` | Maximum time in seconds between consecutive kills for them to be combined into a multikill event |
| `cs_steamvideo_multikill_padding_time` | `2.000000` | `developmentonly` `clientdll` | Time in seconds to add before the first kill and after the last kill for multikill events |
| `csgo_3d_skybox` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `csgo_demoui_playbeck_timestep_value` | `15` | `developmentonly` `clientdll` `defensive` | Number of seconds to seek when using TimeStep buttons on demo playback controller. |
| `csgo_demoui_player_death_seek_lead_up_time` | `1.000000` | `developmentonly` `clientdll` `defensive` | Seek to a moment this amount of seconds leading up to a player death instead of the exact time of the death. |
| `csgo_demoui_previous_event_search_offset` | `2.000000` | `developmentonly` `clientdll` `defensive` | Do not consider events that happened in the last specified number of seconds when a user clicks 'previous' on the UI. |
| `csgo_disable_preview_maps` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `csgo_fatdemo_enable` | `false` | `gamedll` `clientdll` `replicated` `release` |  |
| `csgo_fatdemo_output` | `test.fatdem` | `gamedll` `clientdll` `replicated` `release` |  |
| `csgo_map_preview_scale` | `0.000000` | `clientdll` `archive` |  |
| `csgo_nav_jump_link_detour_threshold` | `1500.000000` | `developmentonly` `gamedll` `replicated` `defensive` | don't traverse a jump link if there's a detour that costs less than this amount |
| `csgo_use_fullsort_for_opaque` | `true` | `clientdll` `cheat` | fullsort the opaque pass when there wasn't a depth prepass |
| `csm_bias_override_0` | `1.000000` | `clientdll` `cheat` |  |
| `csm_bias_override_1` | `1.000000` | `clientdll` `cheat` |  |
| `csm_bias_override_2` | `1.000000` | `clientdll` `cheat` |  |
| `csm_bias_override_3` | `1.000000` | `clientdll` `cheat` |  |
| `csm_cascade0_override_dist` | `-1.000000` | `clientdll` `cheat` |  |
| `csm_cascade1_override_dist` | `-1.000000` | `clientdll` `cheat` |  |
| `csm_cascade2_override_dist` | `-1.000000` | `clientdll` `cheat` |  |
| `csm_cascade3_override_dist` | `-1.000000` | `clientdll` `cheat` |  |
| `csm_cascade_viewdir_shadow_bias_scale` | `2.000000` | `clientdll` `cheat` |  |
| `csm_max_dist_between_caster_and_receiver` | `15000.000000` | `clientdll` `cheat` | default pushback |
| `csm_max_num_cascades_override` | `-1` | `developmentonly` `clientdll` `defensive` | Number of cascades in sunlight shadow |
| `csm_max_shadow_dist_override` | `-1.000000` | `developmentonly` `clientdll` `defensive` |  |
| `csm_max_visible_dist` | `7500.000000` | `clientdll` `cheat` |  |
| `csm_res_override_0` | `0` | `clientdll` `cheat` |  |
| `csm_res_override_1` | `0` | `clientdll` `cheat` |  |
| `csm_res_override_2` | `0` | `clientdll` `cheat` |  |
| `csm_res_override_3` | `0` | `clientdll` `cheat` |  |
| `csm_shadow_worldview_align_x_to_u` | `false` | `clientdll` `cheat` |  |
| `csm_shadow_worldview_shear_align_z_to_v` | `false` | `clientdll` `cheat` |  |
| `csm_sst_max_visible_dist` | `2000.000000` | `clientdll` `cheat` |  |
| `csm_sst_pushback_distance` | `1500.000000` | `clientdll` `cheat` | default pushback |
| `csm_sst_shadow_focus_region_maxz` | `2000.000000` | `clientdll` `cheat` |  |
| `csm_sst_shadow_focus_region_minz` | `-2000.000000` | `clientdll` `cheat` |  |
| `csm_sst_shadow_focus_region_thin_compensation` | `1500.000000` | `clientdll` `cheat` |  |
| `csm_viewdir_shadow_bias` | `0.000000` | `clientdll` `cheat` |  |
| `csm_viewmodel_max_shadow_dist` | `21.000000` | `clientdll` `cheat` |  |
| `csm_viewmodel_max_visible_dist` | `1000.000000` | `clientdll` `cheat` |  |
| `csm_viewmodel_nearz` | `0.500000` | `clientdll` `cheat` |  |
| `csm_viewmodel_shadows` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `cv_bot_ai_bt_debug_target` | `-1` | `gamedll` `replicated` `cheat` | Draw the behavior tree of the given bot. |
| `cv_bot_ai_bt_hiding_spot_show` | `false` | `gamedll` `replicated` `cheat` | Draw hiding spots. |
| `cv_bot_ai_bt_moveto_show_next_hiding_spot` | `false` | `gamedll` `replicated` `cheat` | Draw the hiding spot the bot will check next. |
| `damage_impact_heavy` | `40` | `developmentonly` `clientdll` `defensive` | Damage ABOVE this value is considered heavy damage |
| `damage_impact_medium` | `20` | `developmentonly` `clientdll` `defensive` | Damage BELOW this value is considered light damage |
| `death_chase_distance` | `76.000000` | `developmentonly` `clientdll` |  |
| `death_panel_delay_time` | `0.250000` | `developmentonly` `clientdll` |  |
| `death_panel_travel_time` | `0.250000` | `developmentonly` `clientdll` |  |
| `debug_aim_angle` | `0` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `debug_async_data_panel_override_state` | `-1` | `developmentonly` `clientdll` | Force ALL async data panels to be in a specific state. -1:disabled, 0:failure, 1:loading, 2:success |
| `debug_chicken` | `false` | `developmentonly` `gamedll` | Chicken debug info |
| `debug_destructible_parts` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Draw debug information for destructible parts. |
| `debug_destructible_parts_enabled` | `true` | `gamedll` `clientdll` `replicated` `cheat` | Toggle enabling/disabling the destructible parts system for debug. |
| `debug_destructible_parts_radius_damage` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `debug_destructible_parts_ttl` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | How long the debug draws stick around for, unless they're per-tick. |
| `debug_error_model` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `debug_hltv` | `0` | `developmentonly` `clientdll` `replicated` `clientcmd_can_execute` | Print out hltv events |
| `debug_overlay_fullposition` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `debug_physimpact` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `debug_radial_damage` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `debug_shared_random` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `debug_takedamage_summaries` | `false` | `gamedll` `cheat` |  |
| `debug_video_config_cvars` | `false` | `developmentonly` `clientdll` |  |
| `debug_visibility_monitor` | `0` | `gamedll` `cheat` |  |
| `debugoverlay_circle_verts` | `24` | `cheat` |  |
| `debugoverlay_enable_dotted_dashed` | `true` | `cheat` | Toggle the use of dotted/dashed debugoverlay lines to indicate source |
| `debugoverlay_force_respect_ttl` | `false` | `cheat` | Force respect TTL even when clearing scopes |
| `debugoverlay_show_text_outline` | `false` | `cheat` | Toggle display of box around text |
| `debugoverlay_text_scale` | `1.000000` | `archive` `cheat` | Scale of the text used for 3d display, but see also debug_font_{size,name} |
| `decalfrequency` | `10.000000` | `developmentonly` `gamedll` `notify` `defensive` |  |
| `default_fov` | `90.000000` | `clientdll` `cheat` |  |
| `demo_debug` | `0` | `reference` |  |
| `demo_highlight_fade_duration` | `0.250000` | `clientdll` `release` | Duration of the fade in and of the fade out transitions (fade in + fade out is 2x this value). |
| `demo_highlight_seconds_after` | `2.000000` | `clientdll` `release` | How many seconds after the actual highlight event to show when viewing highlights. |
| `demo_highlight_seconds_before` | `6.000000` | `clientdll` `release` | How many seconds before the actual highlight event to show when viewing highlights. |
| `demo_mouse_enable_binding` | `drop` | `clientdll` `archive` | Name of the binding to enable mouse on demo playback UI |
| `demo_pause_at_end` | `true` | `clientdll` `release` | Pause demo playback when the end of the file is reached, otherwise quit to main menu. |
| `demo_playback_override_settings` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `demo_skip_to_shot_seconds_before` | `2.000000` | `clientdll` `release` | How many seconds before the shot to skip to when skipping to a specific shot ID. |
| `demo_ui_mode` | `2` | `clientdll` `release` | UI mode for demo playback. 0 = disabled, 1 = minimal, 2 = full |
| `destructible_parts_destroy_parts_when_gibbing` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `dev_add_onground_on_spawn` | `false` | `gamedll` `release` | Should we mess with the ground flag when we spawn? (I don't think we should). If we don't hit the assert in CCSPlayer_MovementServices::ProcessMovement, we should remove this by Dec 2022. |
| `dev_create_bhop_reports` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Whether we should create bhop reports when you jump. Reports are created for the client and server and are numbered monotonically |
| `dev_create_move_report` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Whether we should create move reports when you push movement keys. Reports are created for the server and are numbered monotonically |
| `dev_create_sensitivity_report` | `0.000000` | `developmentonly` `clientdll` |  |
| `dev_create_smooth_motion_report` | `false` | `developmentonly` `clientdll` `replicated` `cheat` |  |
| `dev_cs_force_disable_move` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` | forcibly prevent players from moving |
| `dev_cs_frame_firing_enable` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` | Enable that firing will pretend like it's happening on frames. |
| `dev_cs_frame_firing_insert_idle_pose_now` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` | Should we insert the idle pose at this time to make the animation interpolation punchier? |
| `dev_cs_frame_firing_play_animevents` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` | Should we play the animevents that animgraph will skip over? |
| `dev_cs_frame_firing_skip_first_frame_enable` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` | Should we skip the first frame of shooting to make the animation punchier? |
| `dev_cs_frame_firing_tick_offset_enable` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` | Should we offset the current frame to the tick |
| `dev_cs_ragdoll_head_ankle_delta_z_threshold` | `35.000000` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `dev_cs_ragdoll_nudge_intensity` | `500.000000` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `dev_cs_ragdoll_nudge_max_duration` | `1.500000` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `dev_cs_ragdoll_progress_check_interval` | `0.250000` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `dev_reportmoneychanges` | `false` | `developmentonly` `gamedll` `replicated` | Displays money account changes for players in the console |
| `developer` | `0` | `reference` |  |
| `devonly_chicken_activity_debug` | `false` | `developmentonly` `gamedll` | Print chicken activity info to the console |
| `devonly_chicken_blocktimer` | `0.200000` | `developmentonly` `gamedll` | Chicken blockertimer |
| `devonly_chicken_feeler_distance` | `30.000000` | `developmentonly` `gamedll` | Chicken feeler distance |
| `devonly_chicken_feeler_height` | `5.000000` | `developmentonly` `gamedll` | Chicken feeler height |
| `devonly_chicken_feeler_pitch` | `45.000000` | `developmentonly` `gamedll` | Chicken feeler pitch |
| `diffcheck` | `true` | `developmentonly` `defensive` | Activate diffcheck system. |
| `diffcheck_playerslot` | `0` | `developmentonly` `defensive` |  |
| `diffcheck_spew` | `true` | `developmentonly` `defensive` | Actually show diffcheck results. |
| `diffcheck_spew_diff_filter` | `` | `developmentonly` `defensive` | Show diff with matching filter substring only. |
| `diffcheck_spew_diff_only` | `false` | `developmentonly` `defensive` | Show diff only. |
| `disable_dynamic_prop_loading` | `false` | `gamedll` `cheat` | If non-zero when a map loads, dynamic props won't be loaded |
| `disable_source_soundscape_trace` | `false` | `developmentonly` `gamedll` `defensive` | Bypasses lookup of soundscapes for indvidual audio sources when enabled. |
| `display_convars_onscreen_in_big_text` | `` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Display the convars on the screen in big text. Use semicolons to separate multiple convars |
| `display_game_events` | `false` | `gamedll` `cheat` |  |
| `dota_enable_spatial_audio` | `false` | `release` | Flag to enable spatial audio in Dota 2. |
| `dota_spatial_audio_mix` | `1.000000` | `release` | Mix value to blend spatial and non-spatial audio in Dota 2. |
| `dsp_automatic` | `0` | `developmentonly` `demo` `defensive` |  |
| `dsp_db_min` | `80` | `developmentonly` `demo` `defensive` |  |
| `dsp_db_mixdrop` | `0.500000` | `developmentonly` `demo` `defensive` |  |
| `dsp_dist_max` | `1440.000000` | `cheat` `demo` |  |
| `dsp_dist_min` | `0.000000` | `cheat` `demo` |  |
| `dsp_mix_max` | `0.800000` | `developmentonly` `demo` `defensive` |  |
| `dsp_mix_min` | `0.200000` | `developmentonly` `demo` `defensive` |  |
| `dsp_off` | `false` | `cheat` |  |
| `dsp_vol_2ch` | `1.000000` | `developmentonly` `demo` `defensive` |  |
| `dsp_vol_4ch` | `0.500000` | `developmentonly` `demo` `defensive` |  |
| `dsp_vol_5ch` | `0.500000` | `developmentonly` `demo` `defensive` |  |
| `dsp_volume` | `0.800000` | `archive` `demo` |  |
| `dump_audio_input` | `false` | `developmentonly` |  |
| `econ_debug_loadout_ui` | `false` | `developmentonly` `clientdll` | Show debug data when players change their loadout. |
| `econ_enable_inventory_images` | `true` | `developmentonly` `clientdll` | allow inventory image rendering for use by scaleform |
| `econ_inventory_image_pinboard` | `false` | `developmentonly` `clientdll` |  |
| `enable_boneflex` | `true` | `clientdll` `archive` |  |
| `engine_frametime_amnesty_debug` | `false` | `reference` |  |
| `engine_frametime_warnings_enable` | `false` | `reference` |  |
| `english` | `true` | `clientdll` `userinfo` | If set to 1, running the english language set of assets. |
| `ent_actornames_font` | `Consolas` | `gamedll` `clientdll` `replicated` `cheat` | ent_actornames font name |
| `ent_actornames_fontsize` | `24` | `gamedll` `clientdll` `replicated` `cheat` | ent_actornames font size |
| `ent_attachment_filter_substrings` | `` | `gamedll` `cheat` | If an attachment's name has any of the given substrings in it, it will be displayed. Substrings can be delimited by the ',' or '\|' character. |
| `ent_bitvec_enable` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `ent_debug_draw_thinkers` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `ent_joint_axis_size` | `4.000000` | `developmentonly` `gamedll` `defensive` |  |
| `ent_joint_filter_name` | `` | `gamedll` `cheat` | If a joint's entire name matches (case insensitive), it will be displayed. |
| `ent_joint_filter_substrings` | `` | `gamedll` `cheat` | If a joint's name has any of the given substrings in it, it will be displayed. Substrings can be delimited by the ',' or '\|' character. |
| `ent_joint_lines` | `true` | `gamedll` `cheat` | Draw a line between a rendered joint and its parent. |
| `ent_joint_names` | `true` | `gamedll` `cheat` | Draw the name of a rendered joint. |
| `ent_joint_only_ik_joints` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `ent_joint_use_bind_pose` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `ent_messages_draw` | `false` | `gamedll` `clientdll` `replicated` `cheat` | Visualizes all entity input/output activity. |
| `ent_pivot_size` | `20.000000` | `gamedll` `archive` `cheat` |  |
| `ent_revert_dormancy_change` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `ent_show_contexts` | `false` | `gamedll` `cheat` | Show entity contexts in ent_text display |
| `ent_showonlyattachment` | `` | `gamedll` `cheat` |  |
| `ent_skeleton_duration` | `0.000000` | `gamedll` `clientdll` `replicated` `cheat` | Duration of ent_skeleton display |
| `ent_skeleton_only_ik_joints` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `ent_skeleton_snapshot` | `false` | `developmentonly` `gamedll` |  |
| `ent_steadystate_batchsize` | `20` | `developmentonly` `gamedll` `defensive` | Max number of entities to transmit to player |
| `ent_steadystate_delay` | `5.000000` | `developmentonly` `gamedll` `defensive` | Time in seconds without network state changes until an entity is considered for trickle updates |
| `ent_steadystate_enable` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `ent_steadystate_interval` | `0.100000` | `developmentonly` `gamedll` `defensive` | Rate at which entities can be trickled to players |
| `ent_test_interpolation` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `ent_text_flags_active` | `-1` | `gamedll` `archive` `cheat` |  |
| `ent_text_no_name_really_i_mean_it` | `false` | `gamedll` `cheat` |  |
| `entity_log_load_unserialize` | `0` | `gamedll` `clientdll` `replicated` `cheat` | Output unserialization of entities on map load. 0 - off, 1 - client/server, 2 - server, 3 - client |
| `eom_local_player_defeat_anim_enabled` | `true` | `clientdll` `archive` `release` |  |
| `fade_debug_splitscreen_slot` | `-1` | `developmentonly` `clientdll` `defensive` |  |
| `ff_damage_bullet_penetration` | `0.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If friendly fire is off, this will scale the penetration power and damage a bullet does when penetrating another friendly player |
| `ff_damage_decoy_explosion` | `false` | `gamedll` `clientdll` `replicated` `release` | Enables or disables team damage from decoy detonation |
| `ff_damage_reduction_bullets` | `0.100000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How much to reduce damage done to teammates when shot.  Range is from 0 - 1 (with 1 being damage equal to what is done to an enemy) |
| `ff_damage_reduction_grenade` | `0.250000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How much to reduce damage done to teammates by a thrown grenade.  Range is from 0 - 1 (with 1 being damage equal to what is done to an enemy) |
| `ff_damage_reduction_grenade_self` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How much to damage a player does to himself with his own grenade.  Range is from 0 - 1 (with 1 being damage equal to what is done to an enemy) |
| `ff_damage_reduction_other` | `0.250000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How much to reduce damage done to teammates by things other than bullets and grenades.  Range is from 0 - 1 (with 1 being damage equal to what is done to an enemy) |
| `filter_player_simulation_time` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `fire_use_modifier` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `fish_debug` | `false` | `clientdll` `cheat` | Show debug info for fish |
| `fish_dormant` | `false` | `gamedll` `replicated` `cheat` | Turns off interactive fish behavior. Fish become immobile and unresponsive. |
| `fog_color` | `-1.000000 -1.000000 -1.000000` | `clientdll` `cheat` |  |
| `fog_colorskybox` | `-1.000000 -1.000000 -1.000000` | `clientdll` `cheat` |  |
| `fog_enable` | `true` | `clientdll` `cheat` | Enable fog |
| `fog_enableskybox` | `true` | `clientdll` `cheat` |  |
| `fog_end` | `-1.000000` | `clientdll` `cheat` |  |
| `fog_endskybox` | `-1.000000` | `clientdll` `cheat` |  |
| `fog_hdrcolorscale` | `-1.000000` | `clientdll` `cheat` |  |
| `fog_hdrcolorscaleskybox` | `-1.000000` | `clientdll` `cheat` |  |
| `fog_maxdensity` | `-1.000000` | `clientdll` `cheat` |  |
| `fog_maxdensityskybox` | `-1.000000` | `clientdll` `cheat` |  |
| `fog_override` | `0` | `clientdll` `cheat` | Overrides the map's fog settings (-1 populates fog_ vars with map's values) |
| `fog_start` | `-1.000000` | `clientdll` `cheat` |  |
| `fog_startskybox` | `-1.000000` | `clientdll` `cheat` |  |
| `fog_volume_debug` | `false` | `developmentonly` `gamedll` `defensive` | If enabled, prints diagnostic information about the current fog volume |
| `footstep_audible_threshold` | `0.550000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `footstep_debug` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `footstep_force_volume` | `-1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `force_spectator_only_tools` | `false` | `developmentonly` `clientdll` `hidden` `cheat` |  |
| `fov_cs_debug` | `0.000000` | `clientdll` `cheat` | Sets the view fov if cheats are on. |
| `fov_cs_near_z` | `6.500000` | `developmentonly` `clientdll` `cheat` |  |
| `fov_cs_super_ultrawide_near_z` | `1.000000` | `developmentonly` `clientdll` `cheat` |  |
| `fov_cs_ultrawide_near_z` | `4.000000` | `developmentonly` `clientdll` `cheat` |  |
| `fov_desired` | `75.000000` | `clientdll` `archive` `userinfo` | Sets the base field-of-view. |
| `frag_grenade_blip_frequency` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `freecamera_accel` | `5.000000` | `developmentonly` `clientdll` `defensive` | Tweak this parameter to adjust Free Camera movement acceleration. |
| `freecamera_fog_end` | `2500.000000` | `developmentonly` `clientdll` `defensive` | Fog end for Free Camera. |
| `freecamera_fog_start` | `1800.000000` | `developmentonly` `clientdll` `defensive` | Fog start for Free Camera. |
| `freecamera_max_speed` | `500.000000` | `developmentonly` `clientdll` `defensive` | Tweak this parameter to adjust Free Camera movement max speed. |
| `freecamera_rotation_multiplier` | `10.000000` | `developmentonly` `clientdll` `defensive` | Tweak this parameter to adjust Free Camera mouse rotation. |
| `freecamera_zfar` | `4500.000000` | `developmentonly` `clientdll` `defensive` | Fog start for Free Camera. |
| `func_break_max_pieces` | `15` | `gamedll` `archive` `replicated` |  |
| `func_break_reduction_factor` | `0.500000` | `developmentonly` `gamedll` `defensive` |  |
| `func_breakdmg_bullet` | `0.500000` | `developmentonly` `gamedll` `defensive` |  |
| `func_breakdmg_club` | `1.500000` | `developmentonly` `gamedll` `defensive` |  |
| `func_breakdmg_explosive` | `1.250000` | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_async_movable_navmesh_updates` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_debug` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_debug_all` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_debug_follower` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_debug_parallel` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_debug_showtext` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_debug_verbose` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_force_transition_start_direction` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_get_speed_override` | `0.000000` | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_imgui_log_count` | `30` | `developmentonly` `gamedll` `defensive` |  |
| `func_mover_run_parallel` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `func_rotator_debug` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `func_rotator_run_parallel` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `fx_drawmetalspark` | `true` | `developmentonly` `clientdll` | Draw metal spark effects. |
| `g_debug_angularsensor` | `false` | `gamedll` `cheat` |  |
| `g_debug_constraint_sounds` | `false` | `gamedll` `cheat` | Enable debug printing about constraint sounds. |
| `g_debug_doors` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `g_debug_ragdoll_visualize` | `false` | `clientdll` `cheat` |  |
| `g_debug_transitions` | `0` | `developmentonly` `gamedll` `cheat` | Set to 1 and restart the map to be warned if the map has no trigger_transition volumes. Set to 2 to see a dump of all entities & associated results during a transition. |
| `g_ragdoll_fadespeed` | `600` | `developmentonly` `clientdll` `defensive` |  |
| `g_ragdoll_important_maxcount` | `2` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `g_ragdoll_lvfadespeed` | `100` | `developmentonly` `clientdll` `defensive` |  |
| `g_ragdoll_maxcount` | `5` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `game_mode` | `0` | `reference` |  |
| `game_online` | `true` | `developmentonly` `gamedll` `clientdll` `hidden` `replicated` `defensive` | The current game is online. |
| `game_particle_manager_requeue_messages` | `true` | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `game_public` | `true` | `developmentonly` `gamedll` `clientdll` `hidden` `replicated` `defensive` | The current game is public. |
| `game_type` | `0` | `reference` |  |
| `gameinstructor_enable` | `false` | `clientdll` `release` | Display in game lessons that teach new players. |
| `gameinstructor_find_errors` | `false` | `clientdll` `cheat` | Set to 1 and the game instructor will run EVERY scripted command to uncover errors. |
| `gameinstructor_start_sound_cooldown` | `4.000000` | `developmentonly` `clientdll` `defensive` | Number of seconds forced between similar lesson start sounds. |
| `gameinstructor_verbose` | `0` | `clientdll` `cheat` | Set to 1 for standard debugging or 2 (in combo with gameinstructor_verbose_lesson) to show update actions. |
| `gameinstructor_verbose_lesson` | `` | `clientdll` `cheat` | Display more verbose information for lessons have this name. |
| `gamestats_file_output_directory` | `` | `developmentonly` `gamedll` `defensive` | When -gamestatsfileoutputonly is specified, file will be emitted here instead of to modpath
 |
| `gc_secret_key` | `` | `developmentonly` `gamedll` `protected` `defensive` | Secret key for authenticating with the GC
 |
| `gl_clear` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `glow_chickens` | `false` | `developmentonly` `gamedll` | Glow chickens with a green outline. |
| `glow_outline_width` | `6.000000` | `clientdll` `cheat` | Width of glow outline effect in screen space. |
| `glow_use_tolerance` | `0.850000` | `clientdll` `replicated` `cheat` |  |
| `gotv_theater_container` | `` | `clientdll` `release` | Enables GOTV theater mode for the specified container, setting it to 'live' will play top live matches |
| `gpu_level` | `3` | `developmentonly` `clientdll` `defensive` | GPU Level - Default: High |
| `gpu_mem_level` | `2` | `developmentonly` `clientdll` `defensive` | Memory Level - Default: High |
| `hairsim_force_fixed_timestep` | `true` | `developmentonly` `cheat` |  |
| `hairsim_reset` | `false` | `developmentonly` `cheat` |  |
| `healthshot_allow_use_at_full` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `healthshot_health` | `50` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `healthshot_healthboost_damage_multiplier` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `healthshot_healthboost_speed_multiplier` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `healthshot_healthboost_time` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `hidehud` | `0` | `clientdll` `cheat` | bitmask: 1=weapon selection, 2=flashlight, 4=all, 8=health, 16=player dead, 32=needssuit, 64=misc, 128=chat, 256=crosshair, 512=vehicle crosshair, 1024=in vehicle |
| `hinttext_displaytime` | `4.000000` | `developmentonly` `clientdll` `defensive` |  |
| `host_timescale` | `0.000000` | `reference` |  |
| `hostage_debug` | `0` | `gamedll` `clientdll` `replicated` `cheat` | Show hostage AI debug information |
| `hostage_drop_time` | `1.000000` | `developmentonly` `gamedll` | Time for the hostage before it fully drops to ground |
| `hostage_is_silent` | `false` | `gamedll` `clientdll` `replicated` `cheat` | When set, the hostage won't play any code driven response rules lines |
| `hostfile` | `host.txt` | `gamedll` `release` | The HOST file to load. |
| `hostname` | `` | `reference` |  |
| `hud_fastswitch` | `0` | `clientdll` `archive` |  |
| `hud_scaling` | `1.000000` | `clientdll` `archive` | Scales hud elements |
| `hud_showtargetid` | `true` | `clientdll` `archive` `per_user` | Enables display of target names |
| `hullivr_edge_merge_tan` | `0.020000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Should we try to straighten two faces connected to this edge? (tangent) |
| `hullivr_faceisland_merge_disp` | `0.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Should we straighten face island if the displacement is this much? (inches) |
| `hullivr_faceisland_merge_tan` | `0.040000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Should we try to straighten an island of faces deviating from their average normal (tangent)? |
| `hullivr_version` | `3` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `ik_constraints_enabled` | `true` | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_all_chains_unique_color_per_chain` | `false` | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_ccd` | `0` | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_chain_to_filter_by` | `` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ik_debug_constraints` | `-1` | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_dogleg3bone` | `0` | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_dogleg3bone_enabled` | `true` | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_fabrik_backwards_enabled` | `true` | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_fabrik_backwards_iterations` | `0` | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_fabrik_forwards_enabled` | `true` | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_fabrik_forwards_iterations` | `0` | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_groundtraces` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` | Show IK trace related details |
| `ik_debug_perlin_solver` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `ik_debug_planetilt` | `0` | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_planetilt_axis_length` | `20.000000` | `developmentonly` `replicated` `defensive` |  |
| `ik_debug_targets` | `false` | `developmentonly` `replicated` `defensive` |  |
| `ik_enable` | `true` | `replicated` `cheat` | Enable IK. |
| `ik_fabrik_align_chain` | `true` | `developmentonly` `replicated` `defensive` |  |
| `ik_fabrik_backwards_enabled` | `true` | `developmentonly` `replicated` `defensive` |  |
| `ik_fabrik_forwards_enabled` | `true` | `developmentonly` `replicated` `defensive` |  |
| `ik_fabrik_override_num_iterations` | `-1` | `developmentonly` `replicated` `defensive` |  |
| `ik_final_fixup_enable` | `true` | `developmentonly` `replicated` `defensive` |  |
| `ik_hinge_debug_bone_index` | `-1` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ik_planetilt_enable` | `true` | `developmentonly` `replicated` `defensive` |  |
| `imgui_debug_draw_dashboard_toggle_pause` | `false` | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` `menubar_item` | Dashboard/Pause Game When Activated |
| `imgui_debug_draw_dashboard_window` | `false` | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` `menubar_item` | Dashboard/Show Dashboard |
| `imgui_debug_draw_dashboard_window_toggle_focus` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Dashboard toggle focus |
| `imgui_default_font_size` | `20.000000` | `archive` `cheat` | Default imgui font size |
| `imgui_domain` | `2` | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` | 1 == client, 2 == server |
| `imgui_enable` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | if imgui should display |
| `imgui_enable_input` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | if imgui should consume input |
| `imgui_ent_text_enable` | `true` | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` `menubar_item` | Show Entity Text in Window |
| `imgui_show_bullets` | `false` | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` `menubar_item` | CSGO/Bullets |
| `imgui_show_cs2_worldmodel` | `false` | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` `menubar_item` | CSGO/WorldModel |
| `imgui_show_grenades_window` | `false` | `developmentonly` `gamedll` `clientdll` `archive` `replicated` `cheat` `menubar_item` | CSGO/Show Grenades History |
| `imgui_temp_enable` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | if imgui should display temporarily |
| `in_button_double_press_window` | `0.220000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | How short the time between presses needs to be for us to consider it a double-press |
| `in_spewbuttondelta` | `0` | `developmentonly` `gamedll` `clientdll` `replicated` | Spew button deltas, 0 = off, 1 = server, 2 = client, 3 = both |
| `in_spewbuttonhold` | `0` | `developmentonly` `gamedll` `clientdll` `replicated` | Spew button hold times, 0 = off, 1 = server, 2 = client, 3 = both |
| `in_spewent` | `-1` | `developmentonly` `gamedll` `clientdll` `replicated` | Which entity should we spew input for? (Useful for debugging bot input) |
| `in_spewinput` | `0` | `developmentonly` `gamedll` `clientdll` `replicated` | Spew input, 0 = off, 1 = server, 2 = client, 3 = both |
| `inferno_batched_rays` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `inferno_child_spawn_interval_multiplier` | `0.100000` | `gamedll` `cheat` | Amount spawn interval increases for each child |
| `inferno_child_spawn_max_depth` | `4` | `gamedll` `replicated` `release` |  |
| `inferno_ct_experiment` | `true` | `gamedll` `clientdll` `replicated` `cheat` | enable ct incendiary experiment |
| `inferno_damage` | `40.000000` | `gamedll` `cheat` | Damage per second |
| `inferno_damage_ct` | `40.000000` | `gamedll` `cheat` | Damage per second from CT inferno |
| `inferno_damage_timer` | `0.200000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | How long between times for the inferno to deal damage. |
| `inferno_debug` | `false` | `gamedll` `cheat` |  |
| `inferno_dlight_spacing` | `7200.000000` | `clientdll` `cheat` | Inferno dlights are at least this far apart |
| `inferno_dlights` | `30.000000` | `developmentonly` `clientdll` `defensive` | Min FPS at which molotov dlights will be created |
| `inferno_fire` | `2` | `developmentonly` `clientdll` `defensive` |  |
| `inferno_flame_lifetime` | `7.000000` | `gamedll` `replicated` `release` | Average lifetime of each flame in seconds |
| `inferno_flame_lifetime_incendiary` | `5.500000` | `gamedll` `replicated` `release` | Average lifetime of each flame in seconds (incgrenade) |
| `inferno_flame_spacing` | `42.000000` | `gamedll` `cheat` | Minimum distance between separate flame spawns |
| `inferno_forward_reduction_factor` | `0.900000` | `gamedll` `cheat` |  |
| `inferno_friendly_fire_duration` | `6.000000` | `gamedll` `cheat` | For this long, FF is credited back to the thrower. |
| `inferno_initial_spawn_interval` | `0.020000` | `gamedll` `cheat` | Time between spawning flames for first fire |
| `inferno_max_child_spawn_interval` | `0.500000` | `gamedll` `cheat` | Largest time interval for child flame spawning |
| `inferno_max_flames` | `16` | `gamedll` `replicated` `release` | Maximum number of flames that can be created |
| `inferno_max_range` | `150.000000` | `gamedll` `replicated` `release` | Maximum distance flames can spread from their initial ignition point |
| `inferno_max_range_ct` | `110.000000` | `gamedll` `replicated` `release` | Maximum distance flames can spread from their initial ignition point for an incendiary |
| `inferno_max_trace_per_tick` | `16` | `developmentonly` `gamedll` `defensive` |  |
| `inferno_per_flame_spawn_duration` | `3.000000` | `gamedll` `cheat` | Duration each new flame will attempt to spawn new flames |
| `inferno_smoke_volume_density` | `0.030000` | `gamedll` `cheat` |  |
| `inferno_spawn_angle` | `45.000000` | `gamedll` `cheat` | Angular change from parent |
| `inferno_spread_speed_mult` | `1.000000` | `gamedll` `replicated` `release` | Speed up the spreadrate of the Molotov until max number of nodes are created.  slowdown < 1 > Speedup |
| `inferno_spread_speed_mult_ct` | `10.000000` | `gamedll` `replicated` `release` | Speed up the spread rate of the Incendiary until max number of nodes are created. slowdown < 1 > Speedup |
| `inferno_surface_offset` | `15.000000` | `gamedll` `cheat` |  |
| `inferno_velocity_decay_factor` | `0.200000` | `gamedll` `cheat` |  |
| `inferno_velocity_factor` | `0.003000` | `gamedll` `cheat` |  |
| `inferno_velocity_factor_ct` | `0.003000` | `gamedll` `cheat` |  |
| `inferno_velocity_normal_factor` | `0.000000` | `gamedll` `cheat` |  |
| `input_downimpulsevalue` | `0.700000` | `developmentonly` `clientdll` |  |
| `input_filter_relative_analog_inputs` | `false` | `clientdll` `archive` |  |
| `input_upimpulsevalue` | `0.300000` | `developmentonly` `clientdll` |  |
| `install_dlc_workshoptools_cvar` | `-1` | `clientdll` `release` | DLC Install Status |
| `iv_debugbone` | `` | `release` | Debug bone name for interpolation spew of CAnimationState. |
| `iv_parallel_latch` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `iv_parallel_restore` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `iv_wrapped_parallel_latch` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `joy_accel_filter` | `0.200000` | `developmentonly` `clientdll` |  |
| `joy_accelmax` | `1.000000` | `developmentonly` `clientdll` |  |
| `joy_accelscale` | `0.600000` | `developmentonly` `clientdll` |  |
| `joy_advanced` | `false` | `clientdll` `archive` |  |
| `joy_advaxisr` | `0` | `clientdll` `archive` |  |
| `joy_advaxisu` | `0` | `clientdll` `archive` |  |
| `joy_advaxisv` | `0` | `clientdll` `archive` |  |
| `joy_advaxisx` | `0` | `clientdll` `archive` |  |
| `joy_advaxisy` | `0` | `clientdll` `archive` |  |
| `joy_advaxisz` | `0` | `clientdll` `archive` |  |
| `joy_autosprint` | `0.000000` | `developmentonly` `clientdll` `defensive` | Automatically sprint when moving with an analog joystick |
| `joy_circle_correct_mode` | `1` | `clientdll` `archive` `per_user` |  |
| `joy_circle_correct_mode_vehicle` | `2` | `clientdll` `archive` `per_user` |  |
| `joy_display_input` | `false` | `clientdll` `archive` |  |
| `joy_forward_sensitivity` | `1.000000` | `clientdll` `archive` `per_user` |  |
| `joy_lowend` | `1.000000` | `developmentonly` `clientdll` |  |
| `joy_lowmap` | `1.000000` | `developmentonly` `clientdll` |  |
| `joy_movement_stick` | `false` | `clientdll` `archive` `per_user` | Which stick controls movement (0 is left stick) |
| `joy_name` | `joystick` | `clientdll` `archive` |  |
| `joy_pegged` | `0.750000` | `developmentonly` `clientdll` |  |
| `joy_pitch_sensitivity` | `3.000000` | `clientdll` `archive` `per_user` |  |
| `joy_pitchsensitivity` | `1.000000` | `clientdll` `archive` `per_user` |  |
| `joy_response_look` | `0` | `clientdll` `archive` `per_user` |  |
| `joy_response_move` | `9` | `clientdll` `archive` `per_user` |  |
| `joy_response_move_vehicle` | `6` | `developmentonly` `clientdll` `defensive` |  |
| `joy_sensitive_step0` | `0.100000` | `developmentonly` `clientdll` |  |
| `joy_sensitive_step1` | `0.400000` | `developmentonly` `clientdll` |  |
| `joy_sensitive_step2` | `0.900000` | `developmentonly` `clientdll` |  |
| `joy_side_sensitivity` | `1.000000` | `clientdll` `archive` `per_user` |  |
| `joy_sidesensitivity` | `1.000000` | `clientdll` `archive` |  |
| `joy_vehicle_turn_lowend` | `0.700000` | `developmentonly` `clientdll` |  |
| `joy_vehicle_turn_lowmap` | `0.400000` | `developmentonly` `clientdll` |  |
| `joy_virtual_peg` | `0.000000` | `developmentonly` `clientdll` |  |
| `joy_xcontroller_cfg_loaded` | `false` | `developmentonly` `clientdll` `defensive` | If 0, the 360controller.cfg file will be executed on startup & option changes. |
| `joy_yaw_sensitivity` | `3.000000` | `clientdll` `archive` `per_user` |  |
| `joy_yawsensitivity` | `-1.000000` | `clientdll` `archive` `per_user` |  |
| `joystick` | `false` | `clientdll` `archive` | True if the joystick is enabled, false otherwise. |
| `key_bind_version` | `0` | `clientdll` `hidden` `archive` `release` |  |
| `keychain_animation_reactivity` | `0.250000` | `developmentonly` `clientdll` |  |
| `keychain_preview_limit_step` | `0.125000` | `developmentonly` `clientdll` |  |
| `keychain_reactivity` | `0.050000` | `developmentonly` `clientdll` |  |
| `keychain_wmul` | `2.000000` | `developmentonly` `clientdll` |  |
| `labelled_debug_helper_arc_segments` | `20` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `labelled_debug_helper_enabled` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `labelled_debug_helper_scale` | `1.000000` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `labelled_debug_helper_show_position` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `labelled_debug_helper_show_text` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `labelled_debug_helper_skeleton_show_bone_names` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `lb_allow_shadow_rotation` | `true` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Shadow Rotation |
| `lb_barnlight_shadow_use_precomputed_vis` | `true` | `developmentonly` `defensive` |  |
| `lb_barnlight_shadowmap_scale` | `1.000000` | `release` | Scale for computed barnlight shadowmap size |
| `lb_bin_slices` | `8192` | `developmentonly` `defensive` |  |
| `lb_convert_to_barn_lights_falloff_match_point` | `0.150000` | `developmentonly` `defensive` |  |
| `lb_csm_cascade_size_override` | `-1` | `developmentonly` `defensive` | Override width/height of individual cascades in the CSM |
| `lb_csm_cross_fade_override` | `-1.000000` | `developmentonly` `defensive` | Override CSM cross fade amount |
| `lb_csm_distance_fade_override` | `-1.000000` | `developmentonly` `defensive` | Override CSM distance fade |
| `lb_csm_draw_alpha_tested` | `true` | `developmentonly` `defensive` |  |
| `lb_csm_draw_translucent` | `true` | `developmentonly` `defensive` |  |
| `lb_csm_fov_override` | `-1.000000` | `developmentonly` `cheat` |  |
| `lb_csm_override_bulb_radius` | `-1.000000` | `developmentonly` `defensive` | Override bulb radius for CSM |
| `lb_csm_override_staticgeo_cascades` | `false` | `developmentonly` `defensive` | Override Cascades that will render static objects with lb_csm_override_staticgeo_cascades_value |
| `lb_csm_override_staticgeo_cascades_animated_verts` | `true` | `developmentonly` `defensive` | If lb_csm_override_staticgeo_cascades, ensure only objects without animated verts, i.e. SCENEOBJECTFLAG_CAN_RENDER_INTO_SST flag will be excluded (as opposed to all static objects). |
| `lb_csm_override_staticgeo_cascades_value` | `-1` | `developmentonly` `defensive` | If lb_csm_override_staticgeo_cascades, override value used to determine which cascades render static objects |
| `lb_csm_receiver_plane_depth_bias` | `0.000015` | `developmentonly` `defensive` | Shader depth bias applied to shadow receiver (Note this conflicts with renderstate depth bias, both now default to 0) |
| `lb_csm_receiver_plane_depth_bias_transmissive_backface` | `0.000150` | `developmentonly` `defensive` | Depth bias applied to shadow receiver for transmissive backface geo (based on renderstate depthbias being 0) |
| `lb_cubemap_normalization_max` | `32.000000` | `developmentonly` `defensive` |  |
| `lb_cubemap_normalization_roughness_begin` | `0.100000` | `developmentonly` `defensive` |  |
| `lb_debug_light_bounds` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Light Bounds |
| `lb_debug_shadow_atlas` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Shadow Atlas |
| `lb_debug_shadowtile_atlas` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug ShadowTile Atlas |
| `lb_debug_silhouette` | `` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Silhouettes |
| `lb_debug_silhouette_sum` | `1` | `developmentonly` `cheat` | If we should draw normal silhouette or minkowski sum silhouette |
| `lb_debug_tiles` | `` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Tiles |
| `lb_debug_visualize_fog_shadowed_lights` | `0` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Visualize Fog Shadowed Lights |
| `lb_debug_visualize_lights` | `0` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Visualize Lights |
| `lb_debug_visualize_shadowed_light_details` | `false` | `developmentonly` `cheat` |  |
| `lb_debug_visualize_shadowed_lights` | `0` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Debug Visualize Shadowed Lights |
| `lb_dynamic_shadow_penumbra` | `true` | `developmentonly` `defensive` | Adjust shadow penumbra based on light size |
| `lb_dynamic_shadow_resolution` | `true` | `developmentonly` `defensive` | Dynamically adjust shadow resolution |
| `lb_dynamic_shadow_resolution_base` | `1024.000000` | `developmentonly` `defensive` | Base resolution for dynamic shadowmap sizing.  Shadowmap size of a screen sized light |
| `lb_dynamic_shadow_resolution_base_cmp_shadowmapsize` | `false` | `developmentonly` | take min of lb_dynamic_shadow_resolution and barnlight shadowmapsize as base shadowmapsize |
| `lb_dynamic_shadow_resolution_delay` | `0.850000` | `developmentonly` `defensive` | Update delay for shadow size |
| `lb_dynamic_shadow_resolution_hysteresis` | `0.330000` | `developmentonly` `defensive` | Update hysteresis for shadow size |
| `lb_dynamic_shadow_resolution_quantization` | `64` | `developmentonly` `defensive` | Quantization of dynamically computed shadow size |
| `lb_enable_baked_shadows` | `true` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Enable Baked Shadows |
| `lb_enable_binning` | `true` | `developmentonly` `menubar_item` `defensive` | SceneSystem/LightBinner/Enable Binning |
| `lb_enable_dynamic_lights` | `true` | `developmentonly` `cheat` | Allows rendering dynamic lights |
| `lb_enable_envmaps` | `true` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Enable EnvMaps |
| `lb_enable_fog_mixed_shadows` | `true` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Enable Fog Mixed Shadows |
| `lb_enable_lights` | `true` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Enable Lights |
| `lb_enable_shadow_casting` | `true` | `developmentonly` `defensive` | Allow stationary/dynamic lights to cast shadows. |
| `lb_enable_stationary_lights` | `true` | `developmentonly` `cheat` | Allows rendering stationary/mixed lights |
| `lb_enable_sunlight` | `true` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Enable Sunlight |
| `lb_low_quality_shader_fade_region_rescale` | `0.000000` | `developmentonly` `cheat` | For envmaps in low quality shader mode, how much of the fade region to scale the envmap box by. |
| `lb_max_visible_barn_lights_override` | `-1` | `developmentonly` `cheat` | Override maximum visible barn lights |
| `lb_max_visible_envmaps_override` | `-1` | `developmentonly` `cheat` | Override maximum visible envmaps |
| `lb_mixed_shadows` | `true` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Enable Mixed Shadows |
| `lb_override_barn_light_fade_sizes` | `0.050000 0.025000` | `developmentonly` `cheat` |  |
| `lb_override_barn_light_fade_sizes_enable` | `false` | `developmentonly` `cheat` |  |
| `lb_override_barn_light_shadow_fade_sizes` | `0.100000 0.050000` | `developmentonly` `cheat` |  |
| `lb_precomputed_shadowmap_depth_bias` | `0.000350` | `developmentonly` |  |
| `lb_precomputed_shadowmap_enable` | `true` | `developmentonly` |  |
| `lb_shadow_map_cull_empty_mixed` | `false` | `cheat` | Don't render shadows for mixed shadowmaps with no dynamics objects in view |
| `lb_shadow_map_culling` | `true` | `cheat` |  |
| `lb_shadow_texture_height_override` | `-1` | `developmentonly` `defensive` | Override height of shadow atlas texture |
| `lb_shadow_texture_width_override` | `-1` | `developmentonly` `defensive` | Override width of shadow atlas texture |
| `lb_ssss_importance_sample` | `false` | `developmentonly` `defensive` |  |
| `lb_ssss_samples` | `11` | `developmentonly` `defensive` | Subsurface sample count |
| `lb_sun_csm_size_cull_threshold_texels` | `10.000000` | `developmentonly` `defensive` | Size, in texels, where we will cull an object in the shadowmap |
| `lb_tile_pixels` | `8` | `developmentonly` `defensive` |  |
| `lb_time_sliced_shadow_map_reallocation_age` | `0.700000` | `developmentonly` `defensive` | Age of cached allocation to be considered for re-allocation |
| `lb_time_sliced_shadow_map_reallocation_pct` | `0.200000` | `developmentonly` `defensive` | Likelyhood we'll re-allocate a timesliced shadowmap (to try to improve packing) |
| `lb_time_sliced_shadow_map_rendering_enable` | `true` | `developmentonly` `defensive` | Allow time-sliced shadow buffer rendering when enabled via gameinfo.gi |
| `lb_timesliced_shadows_dynamic_size` | `true` | `developmentonly` `defensive` |  |
| `lb_use_ellipsoid_bounds` | `true` | `developmentonly` `cheat` |  |
| `lb_use_illumination_silhouette` | `true` | `developmentonly` `cheat` `menubar_item` | SceneSystem/LightBinner/Use Illumination Bounds |
| `leaderboards_cache_duration` | `600` | `developmentonly` `clientdll` |  |
| `lightquery_debug_direct_lighting` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `lightquery_debug_indirect_lighting` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `lobby_default_privacy_bits2` | `1` | `clientdll` `archive` `release` | Lobby default permissions (0: private, 1: public) |
| `lobby_gamesearch_fake` | `0` | `developmentonly` `clientdll` |  |
| `lobby_stats_fake` | `false` | `developmentonly` `clientdll` |  |
| `locator_topdown_style` | `false` | `developmentonly` `clientdll` `defensive` | Topdown games set this to handle distance and offscreen location differently. |
| `lockMoveControllerRet` | `false` | `clientdll` `archive` |  |
| `logaddress_token_secret` | `` | `gamedll` `release` | Set a secret string that will be hashed when using logaddress with explicit token hash. |
| `logic_entity_analyzer_debug` | `false` | `gamedll` `replicated` `cheat` |  |
| `logic_npc_counter_debug` | `false` | `gamedll` `replicated` `cheat` |  |
| `lservercfgfile` | `listenserver.cfg` | `developmentonly` `gamedll` `defensive` |  |
| `m_pitch` | `0.022000` | `clientdll` `archive` `userinfo` `per_user` | Mouse pitch factor. |
| `m_yaw` | `0.022000` | `clientdll` `archive` `userinfo` `per_user` | Mouse yaw factor. |
| `mapcyclefile` | `mapcycle.txt` | `developmentonly` `gamedll` `defensive` | Name of the .txt file used to cycle the maps on multiplayer servers  |
| `mapoverview_allow_client_draw` | `false` | `clientdll` `release` | Allow a client to draw on the map overview |
| `mapoverview_icon_scale` | `1.000000` | `clientdll` `archive` `release` | Sets the icon scale multiplier for the overview map. Valid values are 0.5 to 3.0. |
| `markup_volume_ref_cone_angle` | `135.000000` | `developmentonly` `gamedll` `defensive` |  |
| `mat_colcorrection_disableentities` | `false` | `developmentonly` `clientdll` `defensive` | Disable map color-correction entities |
| `mat_colcorrection_editor` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `mat_colcorrection_forceentitiesclientside` | `false` | `clientdll` `cheat` | Forces color correction entities to be updated on the client |
| `mat_depthbias_shadowmap` | `0.000500` | `developmentonly` `clientdll` `defensive` |  |
| `mat_disable_normal_mapping` | `false` | `clientdll` `cheat` |  |
| `mat_fullbright` | `0` | `reference` |  |
| `mat_lpv_luxels` | `false` | `reference` |  |
| `mat_luxels` | `false` | `reference` |  |
| `mat_overdraw` | `0` | `reference` |  |
| `mat_shading_complexity` | `false` | `reference` |  |
| `mat_slopescaledepthbias_shadowmap` | `4.000000` | `developmentonly` `clientdll` `defensive` |  |
| `mat_tonemap_bloom_scale` | `-1.000000` | `cheat` |  |
| `mat_tonemap_bloom_start_value` | `-1.000000` | `cheat` |  |
| `mat_tonemap_debug` | `0` | `developmentonly` `defensive` |  |
| `mat_tonemap_force_accelerate_exposure_down` | `-1.000000` | `cheat` |  |
| `mat_tonemap_force_average_lum_min` | `-1.000000` | `cheat` | Override. Old default was 3.0 |
| `mat_tonemap_force_log_lum_max` | `-1.000000` | `cheat` |  |
| `mat_tonemap_force_log_lum_min` | `-1.000000` | `cheat` |  |
| `mat_tonemap_force_max` | `-1.000000` | `cheat` |  |
| `mat_tonemap_force_min` | `-1.000000` | `cheat` |  |
| `mat_tonemap_force_percent_bright_pixels` | `-1.000000` | `cheat` | Override. Old value was 1.0 |
| `mat_tonemap_force_percent_target` | `-1.000000` | `cheat` | Override. Old default was 45. |
| `mat_tonemap_force_rate` | `-1.000000` | `cheat` |  |
| `mat_tonemap_force_scale` | `0.000000` | `cheat` |  |
| `mat_tonemap_force_use_alpha` | `-1` | `cheat` |  |
| `mat_tonemap_uncap_exposure` | `0` | `cheat` |  |
| `mat_viewportscale` | `1.000000` | `developmentonly` `clientdll` `defensive` | Scale down the main viewport (to reduce GPU impact on CPU profiling) |
| `mat_wireframe` | `0` | `reference` |  |
| `mem_level` | `2` | `developmentonly` `clientdll` `defensive` | Memory Level - Default: High |
| `mesh_calculate_curvature_smooth_invert` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `mesh_calculate_curvature_smooth_pass_count` | `3` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `mesh_calculate_curvature_smooth_weight` | `1.000000` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `mic_listen_while_nonfocused` | `false` | `developmentonly` `clientdll` `defensive` | Enables the ability for the mic to remain open if the window loses focus such as when a caster tabs out to adjust settings |
| `mm_dedicated_search_maxping` | `0` | `reference` |  |
| `model_default_preview_sequence_name` | `` | `gamedll` `clientdll` `archive` `replicated` |  |
| `molotov_throw_detonate_time` | `2.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `molotov_usethrow_direction` | `false` | `gamedll` `cheat` |  |
| `motdfile` | `motd.txt` | `gamedll` `release` | The MOTD file to load. |
| `mouse_inverty` | `false` | `clientdll` `archive` `userinfo` |  |
| `movement_stats_debug_draw` | `false` | `gamedll` `cheat` |  |
| `movement_stats_force_calculate` | `false` | `gamedll` `cheat` |  |
| `mp_afterroundmoney` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | amount of money awared to every player after each round |
| `mp_allowspectators` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | toggles whether the server allows spectator mode or not |
| `mp_anyone_can_pickup_c4` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If set, everyone can pick up the c4, not just Ts. |
| `mp_autokick` | `true` | `gamedll` `replicated` `release` `commandline_enforced` | Kick idle/team-killing/team-damaging players |
| `mp_autoteambalance` | `true` | `gamedll` `notify` `release` `commandline_enforced` |  |
| `mp_backup_restore_load_autopause` | `true` | `gamedll` `release` | Whether to automatically pause the match after restoring round data from backup |
| `mp_backup_round_auto` | `true` | `gamedll` `release` | If enabled will keep in-memory backups to handle reconnecting players even if the backup files aren't written to disk |
| `mp_backup_round_file` | `backup` | `gamedll` `release` | If set then server will save all played rounds information to files filename_date_time_team1_team2_mapname_roundnum_score1_score2.txt |
| `mp_backup_round_file_last` | `` | `gamedll` `release` | Every time a backup file is written the value of this convar gets updated to hold the name of the backup file. |
| `mp_backup_round_file_pattern` | `%prefix%_round%round%.txt` | `gamedll` `release` | If set then server will save all played rounds information to files named by this pattern, e.g.'%prefix%_%date%_%time%_%team1%_%team2%_%map%_round%round%_score_%score1%_%score2%.txt' |
| `mp_bot_ai_bt` | `` | `gamedll` `release` `commandline_enforced` | Use the specified behavior tree file to drive the bot behavior. |
| `mp_buy_allow_grenades` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Whether players can purchase grenades from the buy menu or not. |
| `mp_buy_allow_guns` | `255` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Whether players can purchase guns: pistols (1), SMGs (2), rifles (4), shotguns (8), sniper rifles (16), heavy MGs (32). |
| `mp_buy_anywhere` | `0` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | When set, players can buy anywhere, not only in buyzones. 0 = default. 1 = both teams. 2 = Terrorists. 3 = Counter-Terrorists. |
| `mp_buy_during_immunity` | `0` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | When set, players can buy when immune, ignoring buytime. 0 = default. 1 = both teams. 2 = Terrorists. 3 = Counter-Terrorists. |
| `mp_buytime` | `90.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How many seconds after round start players can buy items for. |
| `mp_c4_cannot_be_defused` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If set, the planted c4 cannot be defused. |
| `mp_c4timer` | `40` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | how long from when the C4 is armed until it blows |
| `mp_chattime` | `10` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | amount of time players can chat after the game is over |
| `mp_competitive_endofmatch_extra_time` | `15.000000` | `gamedll` `release` | After a competitive match finishes rematch voting extra time is given for rankings. |
| `mp_consecutive_loss_aversion` | `1` | `gamedll` `clientdll` `replicated` `release` | How loss streak is affected with round win: 0 = win fully resets loss bonus, 1 = first win steps down loss bonus, 2 = first win holds loss bonus and step down starting with second win |
| `mp_consecutive_loss_max` | `4` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `mp_coopmission_bot_difficulty_offset` | `0` | `gamedll` `replicated` `release` `commandline_enforced` | The difficulty offset modifier for bots during coop missions. |
| `mp_ct_default_grenades` | `` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default grenades that the CTs will spawn with.	 To give multiple grenades, separate each weapon class with a space like this: 'weapon_molotov weapon_hegrenade' |
| `mp_ct_default_melee` | `weapon_knife` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default melee weapon that the CTs will spawn with.	 Even if this is blank, a knife will be given.	To give a taser, it should look like this: 'weapon_knife weapon_taser'.	 Remember to set mp_weapons_allow_zeus to 1 if you want to give a taser! |
| `mp_ct_default_primary` | `` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default primary (rifle) weapon that the CTs will spawn with |
| `mp_ct_default_secondary` | `weapon_hkp2000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default secondary (pistol) weapon that the CTs will spawn with |
| `mp_damage_headshot_only` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines whether non-headshot hits do any damage. |
| `mp_damage_scale_ct_body` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scales the damage a CT player takes by this much when they take damage in the body. (1 == 100%, 0.5 == 50%) |
| `mp_damage_scale_ct_head` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scales the damage a CT player takes by this much when they take damage in the head (1 == 100%, 0.5 == 50%).  REMEMBER! headshots do 4x the damage of the body before this scaler is applied. |
| `mp_damage_scale_t_body` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scales the damage a T player takes by this much when they take damage in the body. (1 == 100%, 0.5 == 50%) |
| `mp_damage_scale_t_head` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scales the damage a T player takes by this much when they take damage in the head (1 == 100%, 0.5 == 50%).	 REMEMBER! headshots do 4x the damage of the body before this scaler is applied. |
| `mp_damage_vampiric_amount` | `0.000000` | `gamedll` `replicated` `release` `commandline_enforced` | If Set to non-0, will determine the fraction of damage dealt that will be given to attacker. |
| `mp_death_drop_c4` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Whether c4 is droppable |
| `mp_death_drop_defuser` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Drop defuser on player death |
| `mp_death_drop_grenade` | `2` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Which grenade to drop on player death: 0=none, 1=best, 2=current or best, 3=all grenades |
| `mp_death_drop_gun` | `1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Which gun to drop on player death: 0=none, 1=best, 2=current or best |
| `mp_death_drop_healthshot` | `true` | `gamedll` `clientdll` `replicated` `release` | Drop healthshot on player death |
| `mp_death_drop_taser` | `true` | `gamedll` `clientdll` `replicated` `release` | Drop taser on player death |
| `mp_deathcam_skippable` | `true` | `gamedll` `replicated` `release` `commandline_enforced` | Determines whether a player can early-out of the deathcam. |
| `mp_default_team_winner_no_objective` | `-1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If the map doesn't define an objective (bomb, hostage, etc), the value of this convar will declare the winner when the time runs out in the round. |
| `mp_defuser_allocation` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How to allocate defusers to CTs at start or round: 0=none, 1=random, 2=everyone |
| `mp_disconnect_kills_bots` | `false` | `gamedll` `release` | When a bot disconnects, kill them first.  Requires mp_disconnect_kills_players. |
| `mp_disconnect_kills_players` | `true` | `gamedll` `release` | When a player disconnects, kill them first (triggering item drops, stats, etc.) |
| `mp_display_kill_assists` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Whether to display and score player assists |
| `mp_dm_bonus_length_max` | `30.000000` | `gamedll` `clientdll` `replicated` `release` | Maximum time the bonus time will last (in seconds) |
| `mp_dm_bonus_length_min` | `30.000000` | `gamedll` `clientdll` `replicated` `release` | Minimum time the bonus time will last (in seconds) |
| `mp_dm_bonus_percent` | `50` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Percent of points additionally awarded when someone gets a kill with the bonus weapon during the bonus period. |
| `mp_dm_bonusweapon_dogtags` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Additional dogtags to drop when making a kill with the bonus weapon |
| `mp_dm_dogtag_score` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Points to award for picking up a dogtag in deathmatch. |
| `mp_dm_healthshot_killcount` | `3` | `gamedll` `clientdll` `replicated` `release` | Grant healthshots in deathmatch after n kills |
| `mp_dm_kill_base_score` | `8` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Number of base points to award for a kill in deathmatch.  Cheaper weapons award 1 or 2 additional points. |
| `mp_dm_taser_bonus_streak_max` | `2` | `gamedll` `clientdll` `replicated` `release` | Maximum times to multiply the score for getting a streak of taser kills in a single life. |
| `mp_dm_teammode` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | In deathmatch, enables team DM visuals & scoring (0: personal, 1: team mode, 2: use team contribution score) |
| `mp_dm_teammode_bonus_score` | `1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Team deathmatch victory points to award for kill with bonus weapon |
| `mp_dm_teammode_dogtag_score` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Team deathmatch victory points to award for collecting enemy dogtags |
| `mp_dm_teammode_kill_score` | `1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Team deathmatch victory points to award for enemy kill |
| `mp_dm_time_between_bonus_max` | `40.000000` | `gamedll` `clientdll` `replicated` `release` | Maximum time a bonus time will start after the round start or after the last bonus (in seconds) |
| `mp_dm_time_between_bonus_min` | `30.000000` | `gamedll` `clientdll` `replicated` `release` | Minimum time a bonus time will start after the round start or after the last bonus (in seconds) |
| `mp_dogtag_despawn_on_killer_death` | `true` | `gamedll` `replicated` `release` `commandline_enforced` | Whether dogtags should despawn when their killer dies |
| `mp_dogtag_despawn_time` | `120.000000` | `gamedll` `replicated` `release` `commandline_enforced` | How many seconds dogtags should stay around before despawning automatically (0 = infinite) |
| `mp_dogtag_pickup_rule` | `0` | `gamedll` `replicated` `release` `commandline_enforced` | Who is eligible to pick up a dogtag (0 = killer only, 1 = killer's team, 2 = victim's team, 3 = killer & victim's team, 4 = anyone) |
| `mp_drop_grenade_enable` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Allows players to drop grenades. |
| `mp_drop_knife_enable` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Allows players to drop knives. |
| `mp_economy_reset_rounds` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Reset all player money every N rounds (0 for never) |
| `mp_endmatch_votenextleveltime` | `20.000000` | `gamedll` `release` | If mp_endmatch_votenextmap is set, players have this much time to vote on the next map at match end. |
| `mp_endmatch_votenextmap` | `true` | `gamedll` `clientdll` `replicated` `release` | Whether or not players vote for the next map at the end of the match when the final scoreboard comes up |
| `mp_endmatch_votenextmap_keepcurrent` | `true` | `gamedll` `clientdll` `replicated` `release` | If set, keeps the current map in the list of voting options.  If not set, the current map will not appear in the list of voting options. |
| `mp_endmatch_votenextmap_wargames_modes` | `` | `gamedll` `release` | Modes available for endmatch voting during War Games. Separate names with spaces. |
| `mp_endmatch_votenextmap_wargames_nummaps` | `3` | `gamedll` `release` | Maximum number of maps to include in endmatch voting during War Games |
| `mp_endmatch_votenextmap_wargames_nummodes` | `1` | `gamedll` `release` | Maximum number of other War Games to include in endmatch voting during War Games |
| `mp_endwarmup_player_count` | `0` | `gamedll` `clientdll` `replicated` `release` | Number of players required to be connected to end warmup early. 0 to require maximum players for mode. |
| `mp_equipment_reset_rounds` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Reset all player equipment every N rounds (0 for never) |
| `mp_fadetoblack` | `false` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `defensive` | fade a player's screen to black when he dies |
| `mp_flinch_punch_scale` | `3.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Scalar for first person view punch when getting hit. |
| `mp_footsteps_serverside` | `true` | `gamedll` `release` | Makes the server always play footstep sounds. Clients never calculate footstep sounds locally, instead relying on the server. |
| `mp_force_pick_time` | `15.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The amount of time a player has on the team screen to make a selection before being auto-teamed |
| `mp_forcecamera` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Restricts spectator modes for dead players |
| `mp_forcerespawn` | `true` | `developmentonly` `gamedll` `notify` `defensive` |  |
| `mp_fraglimit` | `0` | `gamedll` `notify` `release` |  |
| `mp_free_armor` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines whether kevlar (1+) and/or helmet (2+) are given automatically. |
| `mp_freezetime` | `6` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | how many seconds to keep players frozen when the round starts |
| `mp_friendlyfire` | `false` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | Allows team members to injure other members of their team |
| `mp_give_player_c4` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Whether this map should spawn a c4 bomb for a player or not. |
| `mp_global_damage_per_second` | `0.000000` | `gamedll` `replicated` `release` `commandline_enforced` | If above 0, deal non-lethal damage to players over time. |
| `mp_guardian_bomb_plant_custom_x_mark_location` | `` | `gamedll` `clientdll` `replicated` `release` | x,y,z to display an X for the bomb plant in guardian missions with custom bomb plant boundaries. |
| `mp_guardian_target_site` | `-1` | `gamedll` `release` `commandline_enforced` | If set to the index of a bombsite, will cause random spawns to be only created near that site. |
| `mp_halftime` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines whether the match switches sides in a halftime event. |
| `mp_halftime_duration` | `15.000000` | `gamedll` `clientdll` `replicated` `release` | Target number of seconds that halftime lasts; shortened if team intros are active |
| `mp_halftime_pausematch` | `0` | `gamedll` `clientdll` `replicated` `release` | Set to 1 to pause match after halftime countdown elapses. Match must be resumed by vote or admin. |
| `mp_halftime_pausetimer` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Set to 1 to stay in halftime indefinitely. Set to 0 to resume the timer. |
| `mp_hostages_max` | `2` | `gamedll` `replicated` `release` `commandline_enforced` | Maximum number of hostages to spawn. |
| `mp_hostages_rescuetime` | `1.000000` | `gamedll` `clientdll` `replicated` `release` | Additional time added to round time if a hostage is reached by a CT. |
| `mp_hostages_rescuetowin` | `1` | `developmentonly` `gamedll` `clientdll` `replicated` | 0 == all alive, any other number is the number the CT's need to rescue to win the round. |
| `mp_hostages_run_speed_modifier` | `1.000000` | `gamedll` `replicated` `release` | Default is 1.0, slow down hostages by setting this to < 1.0. |
| `mp_hostages_spawn_farthest` | `false` | `gamedll` `replicated` `release` | When enabled will consistently force the farthest hostages to spawn. |
| `mp_hostages_spawn_force_positions` | `` | `gamedll` `replicated` `release` `commandline_enforced` | Comma separated list of zero based indices to force spawn positions, e.g. '0,2' or '1,6' |
| `mp_hostages_spawn_force_positions_xyz` | `` | `gamedll` `replicated` `release` | Comma separated list of xyz locations to force spawn positions, e.g. 'x1 y1 z1,x2 y2 z2' |
| `mp_hostages_spawn_same_every_round` | `true` | `gamedll` `replicated` `release` `commandline_enforced` | 0 = spawn hostages randomly every round, 1 = same spawns for entire match. |
| `mp_hostages_takedamage` | `false` | `gamedll` `clientdll` `replicated` `release` | Whether or not hostages can be hurt. |
| `mp_humanteam` | `any` | `gamedll` `replicated` `release` | Restricts human players to a single team {any, CT, T} |
| `mp_ignore_round_win_conditions` | `false` | `gamedll` `replicated` `release` | Ignore conditions which would end the current round |
| `mp_items_prohibited` | `` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Set this convar to a comma-delimited list of definition indices of weapons that should be prohibited from use. |
| `mp_join_grace_time` | `0.000000` | `gamedll` `clientdll` `replicated` `release` | Number of seconds after round start to allow a player to join a game |
| `mp_limitteams` | `2` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | Max # of players 1 team can have over another (0 disables check) |
| `mp_logdetail` | `0` | `gamedll` `release` | Logs attacks.  Values are: 0=off, 1=enemy, 2=teammate, 3=both) |
| `mp_logdetail_items` | `false` | `gamedll` `release` | Logs a line any time a player acquires or loses an item. |
| `mp_logmoney` | `false` | `gamedll` `release` | Enables money logging.  Values are: 0=off, 1=on |
| `mp_match_can_clinch` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Can a team clinch and end the match by being so far ahead that the other team has no way to catching up? |
| `mp_match_end_changelevel` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | At the end of the match, perform a changelevel even if next map is the same |
| `mp_match_end_restart` | `false` | `gamedll` `clientdll` `replicated` `release` | At the end of the match, perform a restart instead of loading a new map |
| `mp_match_restart_delay` | `25` | `gamedll` `clientdll` `replicated` `release` | Time (in seconds) until a match restarts. |
| `mp_max_armor` | `2` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines the highest level of armor allowed to be purchased. (0) None, (1) Kevlar, (2) Helmet |
| `mp_maxmoney` | `16000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | maximum amount of money allowed in a player's account |
| `mp_maxrounds` | `0` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | max number of rounds to play before server changes maps |
| `mp_min_halftime_duration` | `8.500000` | `gamedll` `clientdll` `replicated` `release` | Minimum number of seconds that halftime lasts even if team intros are active |
| `mp_only_cts_rescue_hostages` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `mp_overtime_enable` | `false` | `gamedll` `clientdll` `replicated` `release` | If a match ends in a tie, use overtime rules to determine winner |
| `mp_overtime_halftime_pausetimer` | `0` | `gamedll` `clientdll` `replicated` `release` | If set to 1 will set mp_halftime_pausetimer to 1 before every half of overtime. Set mp_halftime_pausetimer to 0 to resume the timer. |
| `mp_overtime_limit` | `0` | `gamedll` `clientdll` `replicated` `release` | When overtime is enabled, only so many overtimes can be played |
| `mp_overtime_maxrounds` | `6` | `gamedll` `clientdll` `replicated` `release` | When overtime is enabled play additional rounds to determine winner |
| `mp_overtime_startmoney` | `10000` | `gamedll` `clientdll` `replicated` `release` | Money assigned to all players at start of every overtime half |
| `mp_plant_c4_anywhere` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `mp_playercashawards` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Players can earn money by performing in-game actions |
| `mp_playerid` | `0` | `gamedll` `clientdll` `replicated` `release` | Controls what information player see in the status bar: 0 all names; 1 team names; 2 no names |
| `mp_playerid_delay` | `0.400000` | `gamedll` `clientdll` `replicated` `release` | Number of seconds to delay showing information in the status bar |
| `mp_playerid_hold` | `0.100000` | `gamedll` `clientdll` `replicated` `release` | Number of seconds to keep showing old information in the status bar |
| `mp_promoted_item_enabled` | `false` | `gamedll` `clientdll` `notify` `replicated` `release` | Allow the purchasing of the promoted item. |
| `mp_randomspawn` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines whether players are to spawn. 0 = default; 1 = both teams; 2 = Terrorists; 3 = CTs. |
| `mp_randomspawn_dist` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If using mp_randomspawn, determines whether to test distance when selecting this spot. |
| `mp_randomspawn_los` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If using mp_randomspawn, determines whether to test Line of Sight when spawning. |
| `mp_require_gun_use_to_acquire` | `false` | `gamedll` `release` | Whether guns must be +used to acquire or default is touch-to-pickup |
| `mp_respawn_immunitytime` | `4.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How many seconds after respawn immunity lasts. Set to negative value to disable warmup immunity. |
| `mp_respawn_on_death_ct` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | When set to 1, counter-terrorists will respawn after dying. |
| `mp_respawn_on_death_t` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | When set to 1, terrorists will respawn after dying. |
| `mp_respawnwavetime_ct` | `10.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Time between respawn waves for CTs. |
| `mp_respawnwavetime_t` | `10.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Time between respawn waves for Terrorists. |
| `mp_restartgame` | `0` | `gamedll` `release` | If non-zero, game will restart in the specified number of seconds |
| `mp_retake_ct_count` | `4` | `gamedll` `clientdll` `replicated` `release` | Number of CT's when playing retakes. |
| `mp_retake_ct_loadout_bonus_card` | `#GameUI_Retake_Card_TheAWPortunity,1,1,weapon_awp` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT bonus card for full buy round when playing bomb site retake. |
| `mp_retake_ct_loadout_bonus_card_availability` | `1,2` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT bonus card availability pattern for full buy round when playing bomb site retake. |
| `mp_retake_ct_loadout_default_pistol_round` | `1|3;#GameUI_Retake_Card_4v3,1,0,secondary0|1;#GameUI_Retake_Card_FlashOut,0,0,secondary0,grenade0;#GameUI_Retake_Card_HideAndPeek,0,0,secondary0,grenade1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT Loadouts for default pistol round when playing bomb site retake. |
| `mp_retake_ct_loadout_enemy_card` | `#GameUI_Retake_Card_BehindEnemyLines,1,1,rifle1,grenade2` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT enemy card for full buy round when playing bomb site retake. |
| `mp_retake_ct_loadout_full_buy_round` | `4|2;#GameUI_Retake_Card_LightEmUp,1,1,rifle1,grenade0|2;#GameUI_Retake_Card_Kobe,1,1,rifle1,grenade2|1;#GameUI_Retake_Card_1g,1,1,rifle1,grenade3|1;#GameUI_Retake_Card_DisappearingAct,1,1,rifle1,grenade1|1;#GameUI_Retake_Card_EyesOnTarget,1,1,weapon_aug` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT Loadouts for full buy round when playing bomb site retake. |
| `mp_retake_ct_loadout_light_buy_round` | `3|2;#GameUI_Retake_Card_UmpInSmoke,1,1,weapon_ump45,grenade1|2;#GameUI_Retake_Card_FunNGun,1,1,weapon_mp9,grenade2|2;#GameUI_Retake_Card_Sharpshooter,1,1,weapon_ssg08,grenade0|2;#GameUI_Retake_Card_BurstBullpup,1,1,weapon_famas` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT Loadouts for force buy round when playing bomb site retake. |
| `mp_retake_ct_loadout_upgraded_pistol_round` | `2|2;#GameUI_Retake_Card_TakeFive,0,0,weapon_fiveseven|2;#GameUI_Retake_Card_BlindFire,1,0,weapon_p250,grenade0|2;#GameUI_Retake_Card_OnlyTakesOne,0,0,weapon_deagle|2;#GameUI_Retake_Card_SneakyBeakyLike,0,0,weapon_p250,grenade1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT Loadouts for upgraded pistol round when playing bomb site retake. |
| `mp_retake_max_consecutive_rounds_same_target_site` | `2` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Limit the number of consecutive rounds targeting the same site. |
| `mp_retake_t_count` | `3` | `gamedll` `clientdll` `replicated` `release` | Number of terrorists when playing retakes. |
| `mp_retake_t_loadout_bonus_card` | `#GameUI_Retake_Card_TheAWPortunity,1,1,weapon_awp` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T bonus card for full buy round when playing bomb site retake. |
| `mp_retake_t_loadout_bonus_card_availability` | `1,1,2` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T bonus card availability pattern for full buy round when playing bomb site retake. |
| `mp_retake_t_loadout_default_pistol_round` | `0|3;#GameUI_Retake_Card_4BadGuysLeft,1,0,secondary0|1;#GameUI_Retake_Card_LookAway,0,0,secondary0,grenade0;#GameUI_Retake_Card_WhenThereIsSmoke,0,0,secondary0,grenade1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T Loadouts for default pistol round when playing bomb site retake. |
| `mp_retake_t_loadout_enemy_card` | `#GameUI_Retake_Card_FindersKeepers,1,1,rifle1,grenade0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T enemy card for full buy round when playing bomb site retake. |
| `mp_retake_t_loadout_full_buy_round` | `0|2;#GameUI_Retake_Card_OlReliable,1,1,rifle1,grenade0|1;#GameUI_Retake_Card_SmokeShow,1,1,rifle1,grenade1|1;#GameUI_Retake_Card_HotShot,1,1,rifle1,grenade3|1;#GameUI_Retake_Card_EyeSpy,1,1,weapon_sg556,grenade2` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T Loadouts for full buy round when playing bomb site retake. |
| `mp_retake_t_loadout_light_buy_round` | `0|2;#GameUI_Retake_Card_BackInAFlash,1,1,weapon_ump45,grenade0|2;#GameUI_Retake_Card_AllIn,1,1,weapon_galilar|1;#GameUI_Retake_Card_BoomBox,1,1,weapon_mac10,grenade2,grenade1|1;#GameUI_Retake_Card_SetThemFree,1,1,weapon_ssg08,grenade0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T Loadouts for force buy round when playing bomb site retake. |
| `mp_retake_t_loadout_upgraded_pistol_round` | `0|2;#GameUI_Retake_Card_BlindFire,1,0,weapon_elite,grenade0|2;#GameUI_Retake_Card_QueOta,0,0,weapon_deagle|1;#GameUI_Retake_Card_SmokeScreen,0,0,weapon_p250,grenade1|1;#GameUI_Retake_Card_TecTecBoom,0,0,weapon_tec9,grenade2` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | T Loadouts for upgraded pistol round when playing bomb site retake. |
| `mp_round_restart_delay` | `7.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Number of seconds to delay before restarting a round after a win |
| `mp_roundtime` | `5.000000` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | How many minutes each round takes. |
| `mp_roundtime_defuse` | `0.000000` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | How many minutes each round of Bomb Defuse takes. If 0 then use mp_roundtime instead. |
| `mp_roundtime_hostage` | `0.000000` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | How many minutes each round of Hostage Rescue takes. If 0 then use mp_roundtime instead. |
| `mp_shoot_dropped_grenades` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Dropped grenades detonate when shot. |
| `mp_shorthanded_cash_bonus_ignore_kicked` | `true` | `gamedll` `clientdll` `replicated` `release` | Determines whether kicked players are included in the assessment for short-handedness |
| `mp_shorthanded_cash_bonus_round_delay` | `2` | `gamedll` `clientdll` `replicated` `release` | number of previous rounds that a team needs to have been shorthanded before they are eligible for the short-handed bonus |
| `mp_solid_enemies` | `1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How solid are enemies: 0 = transparent; 1 = fully solid |
| `mp_solid_teammates` | `1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How solid are teammates: 0 = transparent; 1 = fully solid; 2 = can stand on top of heads |
| `mp_spawnprotectiontime` | `5` | `gamedll` `replicated` `release` | Kick players who team-kill within this many seconds of a round restart. |
| `mp_spectators_max` | `2` | `gamedll` `clientdll` `replicated` `release` | How many spectators are allowed in a match. |
| `mp_starting_losses` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines what the initial loss streak is. |
| `mp_startmoney` | `800` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | amount of money each player gets when they reset |
| `mp_suicide_penalty` | `true` | `gamedll` `release` `commandline_enforced` | Punish players for suicides |
| `mp_t_default_grenades` | `` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default grenades that the Ts will spawn with.	To give multiple grenades, separate each weapon class with a space like this: 'weapon_molotov weapon_hegrenade' |
| `mp_t_default_melee` | `weapon_knife` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default melee weapon that the Ts will spawn with |
| `mp_t_default_primary` | `` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default primary (rifle) weapon that the Ts will spawn with |
| `mp_t_default_secondary` | `weapon_glock` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The default secondary (pistol) weapon that the Ts will spawn with |
| `mp_tagging_scale` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scalar for player tagging modifier when hit. Lower values for greater tagging. |
| `mp_taser_recharge_time` | `30.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines recharge time for taser. -1 = disabled. |
| `mp_td_dmgtokick` | `300` | `gamedll` `replicated` `release` | The damage threshhold players have to exceed in a match to get kicked. |
| `mp_td_dmgtowarn` | `200` | `gamedll` `replicated` `release` | The damage threshhold players have to exceed in a match to get warned that they are about to be kicked. |
| `mp_td_spawndmgthreshold` | `50` | `gamedll` `replicated` `release` | The damage threshold players have to exceed at the start of the round to be warned/kick. |
| `mp_team_intro_time` | `6.500000` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | How many seconds for team intro |
| `mp_team_timeout_max` | `1` | `gamedll` `clientdll` `replicated` `release` | Number of timeouts each team gets per match. |
| `mp_team_timeout_ot_add_each` | `0` | `gamedll` `clientdll` `replicated` `release` | Number of timeouts to add for each team when match goes to 2nd and each next overtime. |
| `mp_team_timeout_ot_add_once` | `0` | `gamedll` `clientdll` `replicated` `release` | Number of timeouts to add for each team when regulation time ends and match goes to overtime. |
| `mp_team_timeout_ot_max` | `1` | `gamedll` `clientdll` `replicated` `release` | Max number of timeouts each team can have per OT after all OT timeouts got added. |
| `mp_team_timeout_time` | `60` | `gamedll` `clientdll` `replicated` `release` | Duration of each timeout. |
| `mp_teamcashawards` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Teams can earn money by performing in-game actions |
| `mp_teamflag_1` | `` | `gamedll` `release` | Enter a country's alpha 2 code to show that flag next to team 1's name in the spectator scoreboard. |
| `mp_teamflag_2` | `` | `gamedll` `release` | Enter a country's alpha 2 code to show that flag next to team 2's name in the spectator scoreboard. |
| `mp_teamlogo_1` | `` | `gamedll` `release` | Enter a team's shorthand image name to display their logo. Images can be found here: 'resource/flash/econ/tournaments/teams' |
| `mp_teamlogo_2` | `` | `gamedll` `release` | Enter a team's shorthand image name to display their logo. Images can be found here: 'resource/flash/econ/tournaments/teams' |
| `mp_teammatchstat_1` | `` | `gamedll` `release` | A non-empty string sets first team's match stat. |
| `mp_teammatchstat_2` | `` | `gamedll` `release` | A non-empty string sets second team's match stat. |
| `mp_teammatchstat_cycletime` | `45.000000` | `gamedll` `release` | Cycle match stats after so many seconds |
| `mp_teammatchstat_holdtime` | `5.000000` | `gamedll` `release` | Decide on a match stat and hold it additionally for at least so many seconds |
| `mp_teammatchstat_txt` | `` | `gamedll` `release` | A non-empty string sets the match stat description, e.g. 'Match 2 of 3'. |
| `mp_teammates_are_enemies` | `false` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | When set, your teammates act as enemies and all players are valid targets. |
| `mp_teamname_1` | `` | `gamedll` `release` | A non-empty string overrides the first team's name. |
| `mp_teamname_2` | `` | `gamedll` `release` | A non-empty string overrides the second team's name. |
| `mp_teamplay` | `false` | `developmentonly` `gamedll` `notify` `defensive` |  |
| `mp_teamprediction_pct` | `0` | `gamedll` `release` | A value between 1 and 99 will show predictions in favor of CT team. |
| `mp_teamprediction_txt` | `#SFUIHUD_Spectate_Predictions` | `gamedll` `release` | A value between 1 and 99 will set predictions in favor of first team. |
| `mp_teamscore_1` | `0` | `gamedll` `release` | A non-empty string for best-of-N maps won by the first team. |
| `mp_teamscore_2` | `0` | `gamedll` `release` | A non-empty string for best-of-N maps won by the second team. |
| `mp_teamscore_max` | `0` | `gamedll` `release` | How many maps to win the series (bo3 max=2; bo5 max=3; bo7 max=4) |
| `mp_technical_timeout_duration_s` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How many seconds is a full technical timeout? |
| `mp_technical_timeout_per_team` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How many technical timeouts are there per team? |
| `mp_timelimit` | `0.000000` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | game time per map in minutes |
| `mp_tkpunish` | `0` | `gamedll` `replicated` `release` | Will TK'ers and team damagers be punished in the next round?  {0=no,  1=yes} |
| `mp_tournament` | `false` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `defensive` |  |
| `mp_tournament_whitelist` | `item_whitelist.txt` | `developmentonly` `gamedll` `defensive` | Specifies the item whitelist file to use. |
| `mp_use_respawn_waves` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | When set to 1, and that player's team is set to respawn, they will respawn in waves. If set to 2, teams will respawn when the whole team is dead. |
| `mp_verbose_changelevel_spew` | `1` | `gamedll` `clientdll` `replicated` `release` |  |
| `mp_warmup_items_drop_policy` | `247` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Which items can drop during warmup (bitfield, 1=gun, 2=c4, 4=nade, 8=defuser, 16=taser, 32=healthshot) |
| `mp_warmup_items_nocost` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines whether weapons are free to buy during warmup. |
| `mp_warmup_items_nocount_policy` | `42` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Which items are unlimited during warmup (bitfield, 1=gun, 2=c4, 4=nade, 8=defuser/kevlar, 16=taser, 32=healthshot) |
| `mp_warmup_jointeam_cooldown` | `2.000000` | `developmentonly` `gamedll` `defensive` |  |
| `mp_warmup_offline_enabled` | `false` | `gamedll` `clientdll` `replicated` `release` | Whether or not to do a warmup period at the start of a match in an offline (bot) match. |
| `mp_warmup_online_enabled` | `true` | `gamedll` `clientdll` `replicated` `release` | Whether or not to do a warmup period at the start of an online match. |
| `mp_warmup_pausetimer` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Set to 1 to stay in warmup indefinitely. Set to 0 to resume the timer. |
| `mp_warmuptime` | `30.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | How long the warmup period lasts. Changing this value resets warmup. |
| `mp_warmuptime_all_players_connected` | `0.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Warmup time to use when all players have connected. 0 to disable. |
| `mp_warmuptime_match_cancelled` | `5.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Warmup time to use when the match will be cancelled (eg. due to a live VAC ban). |
| `mp_weapon_next_owner_touch_time` | `1.300000` | `gamedll` `cheat` `release` |  |
| `mp_weapon_prev_owner_touch_time` | `1.500000` | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `mp_weapon_self_inflict_amount` | `0.000000` | `gamedll` `replicated` `release` `commandline_enforced` | If Set to non-0, will hurt the attacker by the specified fraction of max damage if they miss. |
| `mp_weapons_allow_heavy` | `-1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines which team, if any, can purchase Heavy guns. -1 = any; 0 = non; 2 = Ts; 3 = CTs. |
| `mp_weapons_allow_map_placed` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If this convar is set, when a match starts, the game will not delete weapons placed in the map. |
| `mp_weapons_allow_pistols` | `-1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines which team, if any, can purchase Pistols. -1 = any; 0 = non; 2 = Ts; 3 = CTs. |
| `mp_weapons_allow_rifles` | `-1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines which team, if any, can purchase Rifles. -1 = any; 0 = non; 2 = Ts; 3 = CTs. |
| `mp_weapons_allow_smgs` | `-1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines which team, if any, can purchase SMGs. -1 = any; 0 = non; 2 = Ts; 3 = CTs. |
| `mp_weapons_allow_typecount` | `5` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines how many purchases of each weapon type allowed per player per round (0 to disallow purchasing, -1 to have no limit). |
| `mp_weapons_allow_zeus` | `1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Determines how many Zeus purchases a player can make per round (0 to disallow, -1 to have no limit). |
| `mp_weapons_max_gun_purchases_per_weapon_per_match` | `-1` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Max number of times a player may purchase any weapon per match |
| `mp_weaponstay` | `false` | `developmentonly` `gamedll` `notify` `defensive` |  |
| `mp_win_panel_display_time` | `3.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | The amount of time to show the win panel between matches / halfs |
| `mp_winlimit` | `0` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `defensive` | Max score one team can reach before server changes maps |
| `muzzle_flash_debug` | `false` | `developmentonly` `clientdll` |  |
| `nav_approach_points_area_size_threshold` | `200.000000` | `developmentonly` `gamedll` `defensive` | Ignore nav areas with at least one side smaller than this amount during approach point calculation. |
| `nav_attribute_obstacle_draw` | `false` | `developmentonly` `gamedll` |  |
| `nav_attribute_obstacle_draw_attribute` | `` | `developmentonly` `gamedll` |  |
| `nav_attribute_obstacle_draw_elements` | `false` | `developmentonly` `gamedll` |  |
| `nav_bfs_debug` | `0` | `gamedll` `cheat` |  |
| `nav_create_indirect_connection_set_from` | `0.000000 0.000000 0.000000` | `gamedll` `cheat` | Set the 'from' location of an indirect connection. |
| `nav_create_indirect_connection_set_to` | `0.000000 0.000000 0.000000` | `gamedll` `cheat` | Set the 'to' location of an indirect connection. |
| `nav_curve_alt` | `false` | `gamedll` `cheat` |  |
| `nav_curve_iter` | `0` | `gamedll` `cheat` |  |
| `nav_curve_lock` | `-1` | `gamedll` `cheat` |  |
| `nav_curve_max_step` | `10.000000` | `gamedll` `cheat` |  |
| `nav_curve_set` | `-1` | `gamedll` `cheat` |  |
| `nav_curve_step` | `0.020000` | `gamedll` `cheat` |  |
| `nav_debug_blocked` | `false` | `gamedll` `cheat` |  |
| `nav_drag_selection_volume_zmax_offset` | `32` | `developmentonly` `gamedll` `replicated` `defensive` | The offset of the nav drag volume top from center |
| `nav_drag_selection_volume_zmin_offset` | `32` | `developmentonly` `gamedll` `replicated` `defensive` | The offset of the nav drag volume bottom from center |
| `nav_draw_area_connections` | `false` | `gamedll` `cheat` |  |
| `nav_draw_area_filled` | `true` | `gamedll` `cheat` |  |
| `nav_draw_area_gravity` | `false` | `gamedll` `cheat` |  |
| `nav_draw_area_ground` | `false` | `gamedll` `cheat` |  |
| `nav_draw_area_hull_support` | `false` | `gamedll` `cheat` |  |
| `nav_draw_area_ids` | `false` | `gamedll` `cheat` |  |
| `nav_draw_area_inset_margin` | `0.000000` | `gamedll` `cheat` |  |
| `nav_draw_area_normal` | `false` | `gamedll` `cheat` |  |
| `nav_draw_area_should_be_destroyed` | `false` | `gamedll` `cheat` |  |
| `nav_draw_area_split_by_obstacle_mgr` | `false` | `gamedll` `cheat` |  |
| `nav_draw_area_ztest` | `false` | `gamedll` `cheat` |  |
| `nav_draw_attribute_dynamic` | `` | `developmentonly` `gamedll` | Draw all nav areas with this dynamic attribute |
| `nav_draw_attribute_game` | `` | `developmentonly` `gamedll` | Draw all nav areas with this game attribute |
| `nav_draw_attribute_space` | `` | `developmentonly` `gamedll` | Draw only nav blocks with this attribute |
| `nav_draw_blocked` | `true` | `gamedll` `cheat` |  |
| `nav_draw_blocked_connections` | `false` | `gamedll` `cheat` |  |
| `nav_draw_boundary_areas` | `false` | `gamedll` `cheat` |  |
| `nav_draw_connected_area_radius` | `1000.000000` | `gamedll` `cheat` |  |
| `nav_draw_dangerareas` | `false` | `gamedll` `cheat` |  |
| `nav_draw_dormant_movable_meshes` | `false` | `gamedll` `cheat` | Draw dormant movable meshes. |
| `nav_draw_externally_created` | `false` | `gamedll` `cheat` |  |
| `nav_draw_flow_map` | `false` | `gamedll` `cheat` |  |
| `nav_draw_hidingspots` | `false` | `gamedll` `cheat` |  |
| `nav_draw_indirect_connections` | `false` | `gamedll` `cheat` |  |
| `nav_draw_jump_links` | `false` | `gamedll` `cheat` |  |
| `nav_draw_limit` | `300` | `gamedll` `cheat` | The maximum number of areas to draw in edit mode |
| `nav_draw_link_alignment` | `false` | `gamedll` `cheat` |  |
| `nav_draw_links` | `false` | `gamedll` `cheat` |  |
| `nav_draw_markup` | `true` | `gamedll` `cheat` |  |
| `nav_draw_mesh` | `true` | `gamedll` `cheat` |  |
| `nav_draw_mesh_grid` | `false` | `gamedll` `cheat` | Draw the mesh's spatial grid structure around the edit cursor position. |
| `nav_draw_mesh_offset` | `1.000000` | `gamedll` `cheat` | Vertical offset for drawing the mesh (useful for flat planes where the mesh is often a fixed offset from the physical ground |
| `nav_draw_space_boundary` | `0` | `developmentonly` `gamedll` | Draw the boundaries of the 3d nav space. 1 = draw flying space, 2 = draw swimming space |
| `nav_draw_space_cells` | `false` | `developmentonly` `gamedll` |  |
| `nav_draw_space_fly` | `false` | `developmentonly` `gamedll` |  |
| `nav_draw_space_neighbors` | `0` | `developmentonly` `gamedll` |  |
| `nav_draw_space_portals` | `false` | `developmentonly` `gamedll` |  |
| `nav_draw_space_radius` | `0.000000` | `developmentonly` `gamedll` |  |
| `nav_draw_space_swim` | `false` | `developmentonly` `gamedll` |  |
| `nav_draw_space_transitions` | `true` | `developmentonly` `gamedll` |  |
| `nav_edit` | `0` | `gamedll` `cheat` | Set to one to interactively edit the Navigation Mesh. Set to zero to leave edit mode. |
| `nav_edit_draw_navlinks` | `true` | `gamedll` `cheat` |  |
| `nav_edit_use_camera` | `true` | `gamedll` `cheat` |  |
| `nav_edit_validate` | `false` | `gamedll` `cheat` | Validate navmesh structures. |
| `nav_find_occluded_node_nozup_use_raycast` | `true` | `gamedll` `cheat` |  |
| `nav_flow_map_enabled` | `true` | `developmentonly` `gamedll` |  |
| `nav_gen_add_jumps` | `true` | `gamedll` `cheat` |  |
| `nav_gen_agent_radius_buffer` | `0.500000` | `gamedll` `cheat` | Buffer to add to agent radius before passing to nav gen |
| `nav_gen_clip_polys_to_clearance` | `true` | `gamedll` `cheat` |  |
| `nav_gen_clip_polys_to_clearance_debug` | `false` | `gamedll` `cheat` |  |
| `nav_gen_connect_allow_multiple` | `true` | `gamedll` `cheat` |  |
| `nav_gen_connect_angle` | `0.750000` | `gamedll` `cheat` |  |
| `nav_gen_connect_angle_ignore_z` | `true` | `gamedll` `cheat` |  |
| `nav_gen_connect_dist_a` | `1.000000` | `gamedll` `cheat` |  |
| `nav_gen_connect_dist_b` | `1.500000` | `gamedll` `cheat` |  |
| `nav_gen_connect_dist_z_mult` | `0.500000` | `gamedll` `cheat` |  |
| `nav_gen_connect_overlap` | `0.500000` | `gamedll` `cheat` |  |
| `nav_gen_degen_limit` | `0.001000` | `gamedll` `cheat` |  |
| `nav_gen_false` | `false` | `gamedll` `cheat` | Always false |
| `nav_gen_island_removal` | `false` | `gamedll` `cheat` |  |
| `nav_gen_island_removal_all_hulls` | `true` | `gamedll` `cheat` |  |
| `nav_gen_join_nonzup` | `true` | `gamedll` `cheat` |  |
| `nav_gen_jump_connection_min_overlap_ratio` | `1.000000` | `gamedll` `cheat` | Minimum edge overlap required for jump connection consideration as a percentage of agent radius |
| `nav_gen_markup_split_expand` | `2.000000` | `gamedll` `cheat` |  |
| `nav_gen_markup_split_tol_base` | `1.000000` | `gamedll` `cheat` |  |
| `nav_gen_markup_split_tol_nonav` | `1.000000` | `gamedll` `cheat` |  |
| `nav_gen_markup_split_tol_nonentity` | `8.000000` | `gamedll` `cheat` |  |
| `nav_gen_max_bottleneck_width` | `128.000000` | `gamedll` `cheat` |  |
| `nav_gen_max_bottleneck_width_do_clip` | `true` | `gamedll` `cheat` |  |
| `nav_gen_max_edge_len` | `512.000000` | `gamedll` `cheat` |  |
| `nav_gen_max_edge_len_do_clip` | `true` | `gamedll` `cheat` |  |
| `nav_gen_max_edge_len_split_tol` | `24.000000` | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads` | `true` | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_angle_limit` | `8.000000` | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_num_steps` | `6` | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_planar_deviation_limit` | `4.000000` | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_se_limit_end` | `0.100000` | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_se_limit_start` | `0.000010` | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_weld_limit_end` | `0.010000` | `gamedll` `cheat` |  |
| `nav_gen_opt_to_quads_weld_limit_start` | `0.000000` | `gamedll` `cheat` |  |
| `nav_gen_oriented_angle_tol` | `15.000000` | `gamedll` `cheat` | Max abrupt orientation difference an NPC can tolerate when moving through the mesh (degrees). |
| `nav_gen_oriented_max_region_range` | `15.000000` | `gamedll` `cheat` | Max orientation range allowed within a region before it gets further split. |
| `nav_gen_remove_vertical_polys` | `true` | `gamedll` `cheat` |  |
| `nav_gen_split_boundary_polys` | `false` | `gamedll` `cheat` |  |
| `nav_gen_split_multi_connection_polys` | `true` | `gamedll` `cheat` |  |
| `nav_gen_split_multi_connection_polys_tol` | `0.010000` | `gamedll` `cheat` |  |
| `nav_gen_true` | `true` | `gamedll` `cheat` | Always true |
| `nav_gen_vertical_limit` | `88.000000` | `gamedll` `cheat` |  |
| `nav_genrt_debug` | `false` | `gamedll` `cheat` |  |
| `nav_ignore_vpk_navdata` | `false` | `developmentonly` `gamedll` | For testing using legacy nav data |
| `nav_max_view_distance` | `0.000000` | `gamedll` `cheat` | Maximum range for precomputed nav mesh visibility (0 = default 1500 units) |
| `nav_obstacle_validate` | `false` | `gamedll` `cheat` |  |
| `nav_obstruction_async_update` | `false` | `developmentonly` `gamedll` |  |
| `nav_obstruction_draw` | `0.000000` | `gamedll` `cheat` |  |
| `nav_obstruction_draw_change` | `false` | `gamedll` `cheat` |  |
| `nav_obstruction_draw_dist` | `-1.000000` | `gamedll` `cheat` |  |
| `nav_obstruction_draw_island` | `0.000000` | `gamedll` `cheat` |  |
| `nav_obstruction_draw_island_hull` | `-1` | `gamedll` `cheat` |  |
| `nav_obstruction_draw_movefail_blocking` | `false` | `gamedll` `cheat` |  |
| `nav_path_debug` | `false` | `gamedll` `cheat` |  |
| `nav_path_draw_areas` | `false` | `gamedll` `cheat` |  |
| `nav_path_draw_arrow` | `true` | `gamedll` `cheat` |  |
| `nav_path_draw_climb_segments` | `true` | `gamedll` `cheat` |  |
| `nav_path_draw_connected_areas` | `false` | `gamedll` `cheat` |  |
| `nav_path_draw_ground_segments` | `true` | `gamedll` `cheat` |  |
| `nav_path_draw_jump_segments` | `true` | `gamedll` `cheat` |  |
| `nav_path_draw_ladder_segments` | `true` | `gamedll` `cheat` |  |
| `nav_path_draw_link_segments` | `true` | `gamedll` `cheat` |  |
| `nav_path_draw_tick` | `0.000000` | `gamedll` `cheat` |  |
| `nav_path_fixup_climb_up_segments` | `false` | `gamedll` `cheat` |  |
| `nav_path_fixup_gap_segments` | `false` | `gamedll` `cheat` |  |
| `nav_path_jump_process_debug` | `false` | `gamedll` `cheat` |  |
| `nav_path_optimize` | `true` | `gamedll` `cheat` |  |
| `nav_path_optimize_portals` | `true` | `gamedll` `cheat` |  |
| `nav_path_optimizer_debug` | `0` | `gamedll` `cheat` |  |
| `nav_pathfind_debug_log` | `0` | `gamedll` `cheat` |  |
| `nav_pathfind_draw` | `0.000000` | `gamedll` `cheat` |  |
| `nav_pathfind_draw_blocked` | `0.000000` | `gamedll` `cheat` |  |
| `nav_pathfind_draw_costs` | `false` | `gamedll` `cheat` |  |
| `nav_pathfind_draw_fail` | `0.000000` | `gamedll` `cheat` |  |
| `nav_pathfind_draw_total_costs` | `false` | `gamedll` `cheat` |  |
| `nav_pathfind_inadmissable_heuristic_factor` | `1.000000` | `gamedll` `cheat` |  |
| `nav_pathfind_multithread` | `false` | `gamedll` `cheat` |  |
| `nav_potentially_visible_dot_tolerance` | `0.980000` | `gamedll` `cheat` |  |
| `nav_recorder_enabled` | `true` | `gamedll` `cheat` |  |
| `nav_select_allow_blocked` | `true` | `gamedll` `cheat` | When selecting an area under nav_edit, allow area marked as blocked. |
| `nav_select_area_id` | `-1` | `gamedll` `cheat` | Select nav area with matching ID. |
| `nav_select_block_id` | `-1` | `gamedll` `cheat` | Select nav space block with matching ID. |
| `nav_select_hull` | `0` | `gamedll` `cheat` | Restrict area selection to areas that can support a hull of the given category |
| `nav_show_area_connections` | `true` | `gamedll` `cheat` | Show connections to selected area when true |
| `nav_show_area_verts` | `true` | `gamedll` `cheat` | Show area vertex positions |
| `nav_show_area_water_info` | `true` | `gamedll` `cheat` |  |
| `nav_show_elem_info` | `true` | `gamedll` `cheat` |  |
| `nav_show_elem_info_font` | `Consolas` | `gamedll` `cheat` |  |
| `nav_show_elem_info_font_size` | `-1.000000` | `gamedll` `cheat` |  |
| `nav_show_elem_info_font_voffset` | `-11.000000` | `gamedll` `cheat` |  |
| `nav_smooth_constrain_spline` | `true` | `gamedll` `cheat` |  |
| `nav_smooth_constrain_spline_relax` | `0.006000` | `gamedll` `cheat` |  |
| `nav_smooth_constrain_spring` | `2` | `gamedll` `cheat` |  |
| `nav_smooth_constrain_spring_relax` | `0.010000` | `gamedll` `cheat` |  |
| `nav_smooth_draw_boundary` | `0.000000` | `gamedll` `cheat` |  |
| `nav_smooth_draw_calc` | `0` | `gamedll` `cheat` |  |
| `nav_smooth_draw_constraint_spline` | `false` | `gamedll` `cheat` |  |
| `nav_smooth_draw_constraint_spring` | `0.000000` | `gamedll` `cheat` |  |
| `nav_smooth_draw_speed` | `0.000000` | `gamedll` `cheat` |  |
| `nav_smooth_enable` | `1` | `gamedll` `cheat` |  |
| `nav_smooth_push_from_walls` | `12.000000` | `developmentonly` `gamedll` |  |
| `nav_smooth_relax` | `true` | `gamedll` `cheat` |  |
| `nav_smooth_relax_use_timesteps` | `false` | `gamedll` `cheat` |  |
| `nav_smooth_spring_const_override` | `-1.000000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_enable` | `true` | `gamedll` `cheat` |  |
| `nav_smooth_spring_factor_deriv` | `0.000000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_factor_dist` | `0.000000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_factor_speed` | `0.000000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_forward_dist_base` | `50.000000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_forward_dist_time_limit` | `1.000000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_max_dist` | `36.000000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_tension_max_override` | `-1.000000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_timestep_factor_accel` | `100.000000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_timestep_factor_speed` | `100.000000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_timestep_max` | `0.500000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_timestep_min` | `0.100000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_yaw_rotation_speed` | `50.000000` | `gamedll` `cheat` |  |
| `nav_smooth_spring_yaw_threshold` | `20.000000` | `gamedll` `cheat` |  |
| `nav_space_select_dist` | `1000.000000` | `gamedll` `cheat` |  |
| `nav_split_show_line` | `false` | `gamedll` `cheat` | Show the free split line. |
| `nav_test_area_gravity` | `false` | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_dist_0` | `-1.000000` | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_dist_1` | `-1.000000` | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_dist_2` | `-1.000000` | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_hex` | `false` | `gamedll` `cheat` | Demonstrates searching hexagonal lattice over nav mesh. |
| `nav_test_bfs_lattice_mark` | `2.000000` | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_simple` | `false` | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_spacing_0` | `24.000000` | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_spacing_1` | `48.000000` | `gamedll` `cheat` |  |
| `nav_test_bfs_lattice_spacing_2` | `96.000000` | `gamedll` `cheat` |  |
| `nav_test_bfs_simple` | `false` | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_circle` | `0.000000` | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_force` | `false` | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_grid_dim` | `90.000000` | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_path` | `0.000000` | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_rays` | `100.000000` | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_rays_margin` | `-1.000000` | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_rays_random` | `false` | `gamedll` `cheat` |  |
| `nav_test_boundary_zone_sphere` | `0.000000` | `gamedll` `cheat` |  |
| `nav_test_curve_opt` | `0` | `gamedll` `cheat` |  |
| `nav_test_detour` | `false` | `gamedll` `cheat` |  |
| `nav_test_find_nearest` | `false` | `gamedll` `cheat` | Calculate the nearest point on the navmesh to the trace point.  Uses selection from nav_select_hull. |
| `nav_test_find_nearest_clear` | `false` | `gamedll` `cheat` | Calculate the nearest point on the navmesh to the trace point.  Uses selection from nav_select_hull. |
| `nav_test_find_random_connected` | `false` | `gamedll` `cheat` | Demonstrates finding random points that are connected in the nav mesh to the start point. |
| `nav_test_find_random_connected_dist_max` | `1000.000000` | `gamedll` `cheat` |  |
| `nav_test_find_random_connected_dist_min` | `100.000000` | `gamedll` `cheat` |  |
| `nav_test_find_z` | `0.000000` | `gamedll` `cheat` |  |
| `nav_test_force_npc_repath` | `false` | `gamedll` `cheat` |  |
| `nav_test_genrt` | `false` | `gamedll` `cheat` |  |
| `nav_test_genrt_place` | `false` | `gamedll` `cheat` |  |
| `nav_test_genrt_tile_removal_extent` | `50.000000` | `gamedll` `cheat` |  |
| `nav_test_genrt_tile_removal_place` | `false` | `gamedll` `cheat` |  |
| `nav_test_getareaoverlapping_gravity` | `false` | `gamedll` `cheat` |  |
| `nav_test_getnearestnav_gravity` | `false` | `gamedll` `cheat` |  |
| `nav_test_multi_connection` | `false` | `gamedll` `cheat` |  |
| `nav_test_npc_area` | `0` | `gamedll` `cheat` |  |
| `nav_test_npc_collision` | `0` | `gamedll` `cheat` |  |
| `nav_test_npc_collision_range` | `250.000000` | `gamedll` `cheat` |  |
| `nav_test_npc_collision_show_geometry` | `false` | `gamedll` `cheat` |  |
| `nav_test_path` | `false` | `gamedll` `cheat` | Calculate and draw a path from player/camera position to the test position. |
| `nav_test_path_lock_goal` | `false` | `gamedll` `cheat` | Lock the pathfinding goal to the current intersection point. |
| `nav_test_path_lock_start` | `false` | `gamedll` `cheat` | Lock the pathfinding start to the current intersection point. |
| `nav_test_path_move` | `false` | `gamedll` `cheat` |  |
| `nav_test_path_opt` | `true` | `gamedll` `cheat` | Enable path optimization for nav_edit_path paths. |
| `nav_test_path_opt_transitions` | `false` | `gamedll` `cheat` |  |
| `nav_test_path_return` | `false` | `gamedll` `cheat` | Calculate a return path from cursor position to the path calculated by nav_test_path. |
| `nav_test_path_space` | `0` | `gamedll` `cheat` | Should nav_test_path test 3d navigation?  1 = space to space, 2 = multi-modal space/ground |
| `nav_test_path_space_fly` | `true` | `gamedll` `cheat` | Test flight paths |
| `nav_test_path_space_swim` | `true` | `gamedll` `cheat` | Test swim paths |
| `nav_test_pos_name` | `` | `developmentonly` `gamedll` `defensive` |  |
| `nav_test_pos_place` | `-1` | `developmentonly` `gamedll` `defensive` |  |
| `nav_test_ray_space` | `0` | `gamedll` `cheat` |  |
| `nav_test_rays` | `false` | `gamedll` `cheat` |  |
| `nav_test_rays_use_npc_move` | `false` | `gamedll` `cheat` |  |
| `nav_test_search_on_path` | `false` | `gamedll` `cheat` | Test the 'on path' search mode for tactical searches. Requires a selected NPC with a current path. |
| `nav_test_search_on_path_boundary_edges_only` | `false` | `gamedll` `cheat` | Activate the 'boundary edges only' constraint when testing the 'on path' search mode for tactical searches. |
| `nav_test_search_on_path_setgoal` | `false` | `gamedll` `cheat` | Test the 'on path' search mode for tactical searches using SetGoal w/ possible path clipping (flips between 2 searches). Requires a selected NPC. |
| `nav_test_smooth` | `false` | `gamedll` `cheat` |  |
| `nav_test_smooth_extern_push` | `0.000000` | `gamedll` `cheat` |  |
| `nav_test_smooth_in_speed` | `120.000000` | `gamedll` `cheat` |  |
| `nav_test_smooth_in_yaw` | `0.000000` | `gamedll` `cheat` |  |
| `nav_test_smooth_path_speed` | `-1.000000` | `gamedll` `cheat` |  |
| `nav_test_smooth_separating_dist` | `-1.000000` | `gamedll` `cheat` |  |
| `nav_test_smooth_spring_const` | `-1.000000` | `gamedll` `cheat` |  |
| `nav_test_smooth_spring_tension_max` | `-1.000000` | `gamedll` `cheat` |  |
| `nav_test_spline` | `0` | `gamedll` `cheat` |  |
| `nav_test_split_obstacle` | `0` | `gamedll` `cheat` |  |
| `nav_test_split_obstacle_dirty` | `false` | `gamedll` `cheat` |  |
| `nav_test_split_obstacle_leave` | `false` | `gamedll` `cheat` |  |
| `nav_test_split_obstacle_size` | `30.000000` | `gamedll` `cheat` |  |
| `nav_test_split_obstacle_update_pos` | `true` | `gamedll` `cheat` |  |
| `nav_volume_debug` | `0` | `gamedll` `cheat` | Draw or print debug information about nav volume queries. |
| `navspace_create_water_smooth_connections` | `true` | `gamedll` `cheat` |  |
| `navspace_create_water_transition_connections` | `true` | `gamedll` `cheat` |  |
| `navspace_debug_pathfind` | `-1.000000` | `gamedll` `cheat` |  |
| `navspace_debug_stringpull` | `1.000000` | `gamedll` `cheat` |  |
| `navspace_debug_trace` | `0.000000` | `gamedll` `cheat` |  |
| `navspace_debug_transition_calc` | `0.000000` | `gamedll` `cheat` |  |
| `navspace_draw_changes_blocks` | `0.000000` | `gamedll` `cheat` | Draw blocks when they change |
| `navspace_draw_changes_waters` | `0.000000` | `gamedll` `cheat` | Draw water volumes when they change |
| `navspace_path_use_water_level_locator` | `true` | `gamedll` `cheat` |  |
| `net_async_job_random_sleep` | `0.000000` | `developmentonly` `defensive` | Sleep randomly 0..net_async_job_random_sleep ms in the parallel server jobs; sleep is per job |
| `net_client_steamdatagram_enable_override` | `0` | `clientdll` `release` | 0: Use connect method requested by GC.  >0: Always use SDR if possible.  <0: Always use direct UDP if possible |
| `net_debug_to_file` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `net_showeventlisteners` | `false` | `developmentonly` `gamedll` `defensive` | Show listening addition/removals |
| `net_showevents` | `0` | `developmentonly` `gamedll` `defensive` | Dump game events to console (1=client only, 2=all). |
| `nextlevel` | `` | `gamedll` `notify` `release` | If set to a valid map name, will trigger a changelevel to the specified map at the end of the round |
| `nextmap_print_enabled` | `false` | `gamedll` `release` | When enabled prints next map to clients |
| `nextmode` | `` | `gamedll` `notify` `replicated` `release` | Sets the game mode to be played when the next level loads |
| `noclip_fixup` | `true` | `gamedll` `cheat` |  |
| `npc_record_snapshot_data` | `false` | `developmentonly` `gamedll` |  |
| `npcsolve_attract_draw` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_constraint_nav` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_constraint_npc` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_drag_linear` | `0.000000` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_forward` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_forward_const` | `30000.000000` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_forward_dist` | `200.000000` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_forward_margin` | `5.000000` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_path_close_const` | `0.000000` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_path_close_max_tension` | `100.000000` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_path_lookahead_const` | `4.000000` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_path_lookahead_dist` | `100.000000` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_path_vel_const` | `0.000000` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_separation` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_separation_const` | `10000.000000` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_separation_dist` | `5.000000` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_separation_draw` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_separation_jitter` | `0.000000` | `developmentonly` `gamedll` `defensive` |  |
| `npcsolve_separation_r2` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `option_duck_method` | `false` | `clientdll` `archive` `userinfo` `per_user` | Input toggle control |
| `option_speed_method` | `false` | `clientdll` `archive` `userinfo` `per_user` | Input toggle control |
| `opus_decode_test_signal` | `false` | `developmentonly` |  |
| `opus_unittest_test_signal` | `false` | `developmentonly` |  |
| `panorama_async_compute_mipgen` | `true` | `developmentonly` `clientdll` | use asynchronous compute for mipmap generation. |
| `panorama_console_max_autocomplete` | `100` | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `panorama_console_max_history` | `100` | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `panorama_console_max_lines` | `2000` | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `panorama_console_position_and_size` | `` | `clientdll` `hidden` `archive` |  |
| `panorama_daisy_wheel` | `ABXY` | `developmentonly` `clientdll` `hidden` `defensive` | Daisy wheel input mode: RS \| ABXY |
| `panorama_debug_movies` | `false` | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `panorama_debug_overlay_opacity` | `0.000000` | `reference` |  |
| `panorama_debug_overlay_opacity_max` | `0.000000` | `reference` |  |
| `panorama_debug_overlay_opacity_min` | `0.000000` | `reference` |  |
| `panorama_debugger_theme` | `Light` | `clientdll` `archive` |  |
| `panorama_dragscroll_maxflickvelocity` | `8000.000000` | `developmentonly` `clientdll` `hidden` `defensive` | Maximum velocity for a drag scroll flick |
| `panorama_dragscroll_minflickvelocity` | `60.000000` | `developmentonly` `clientdll` `hidden` `defensive` | Minimum velocity that the mouse must be moving as mouse up time to qualify as a drag scroll flick |
| `panorama_focus_world_panels` | `false` | `clientdll` `archive` | when set request key focus when a world panel is enabled |
| `panorama_label_draw_rects` | `0` | `developmentonly` `clientdll` `hidden` `defensive` | When labels paint, draw the rectangles for the character ranges. 0 = none, 1 = all, 2 = text only, 3 = inline objects only |
| `panorama_label_wrap_before_shrink` | `true` | `developmentonly` `clientdll` `hidden` `defensive` | Should labels try to wrap text before using text-overflow: shrink |
| `panorama_movie_async_load_size_bytes` | `20971520` | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `panorama_movie_force_not_ready_behavior` | `-1` | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `panorama_streaming_load_local_images` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `panorama_transition_time_factor` | `0.000000` | `reference` |  |
| `panorama_worldpanel_update_cull_distance` | `1000.000000` | `developmentonly` `clientdll` `defensive` |  |
| `panorama_worldpanel_update_cull_size_threshold` | `5.000000` | `developmentonly` `clientdll` `defensive` |  |
| `panorama_worldpanel_update_culling` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `parallel_perform_invalidate_physics` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `parallel_update_surrounding_bounds_in_spatial_partition_update` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `particle_cluster_debug` | `0` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `particle_cluster_manager_search_dist` | `256.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `particle_cluster_nodraw` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `particle_cluster_use_collision_hulls` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `particle_debug_creation_filter` | `` | `developmentonly` `clientdll` `hidden` `replicated` `defensive` |  |
| `particle_layer_id_whitelist` | `` | `developmentonly` |  |
| `particle_powsimd_random_range_exp` | `true` | `developmentonly` `defensive` |  |
| `particle_profile_filter` | `` | `developmentonly` `defensive` | Profile particle filter |
| `particle_snapshot_allow_combined_models` | `false` | `developmentonly` |  |
| `particle_test_attach_attachment` | `0` | `gamedll` `cheat` | Attachment index for attachment mode |
| `particle_test_attach_mode` | `follow_attachment` | `gamedll` `cheat` | Possible Values: 'start_at_attachment', 'follow_attachment', 'start_at_origin', 'follow_origin' |
| `particle_test_file` | `` | `gamedll` `cheat` | Name of the particle system to dynamically spawn |
| `partybrowser_throttle_data` | `0.150000` | `developmentonly` `clientdll` |  |
| `partybrowser_timeout` | `15.000000` | `developmentonly` `clientdll` |  |
| `path_closest_point_debug` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `path_node_evaluation_debug` | `0.000000` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `pawn_mimic_all` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `phonemedelay` | `0.000000` | `developmentonly` `clientdll` `defensive` | Phoneme delay to account for sound system latency. |
| `phonemefilter` | `0.080000` | `developmentonly` `clientdll` `defensive` | Time duration of box filter to pass over phonemes. |
| `phonemesnap` | `2` | `developmentonly` `clientdll` `defensive` | Lod at level at which visemes stops always considering two phonemes, regardless of duration. |
| `phys_batch_ray_test` | `0` | `developmentonly` `clientdll` `defensive` |  |
| `phys_continuous_kinematic_update` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_cull_internal_mesh_contacts` | `false` | `developmentonly` `replicated` `defensive` |  |
| `phys_dynamic_scaling` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `phys_expensive_shape_threshold` | `6` | `clientdll` `cheat` |  |
| `phys_force_controller_debug` | `false` | `developmentonly` `gamedll` |  |
| `phys_headshotscale` | `1.300000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Modifier for the headshot impulse hits on players |
| `phys_impactforcescale` | `1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `phys_joint_teleport` | `true` | `gamedll` `cheat` | Teleport joint anchors if connected to world |
| `phys_length_damping_ratio` | `2.000000` | `gamedll` `cheat` | Spring damping ratio for length constraint |
| `phys_length_frequency` | `5.000000` | `gamedll` `cheat` | Spring stiffness for length constraint |
| `phys_log_updaters` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_log_updaters_exclude` | `weapon pistol rifle survivor common_male` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_log_updaters_include` | `limbs` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_min_motion_controller_count_to_run_in_job` | `8` | `developmentonly` `defensive` |  |
| `phys_multithreading_enabled` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Enable/Disable Multithreading in VPhysics |
| `phys_playerscale` | `10.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | This multiplies the bullet impact impuse on players for more dramatic results when players are shot. |
| `phys_powered_ragdoll_debug` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_pushscale` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_shoot_angular_speed` | `3600.000000` | `developmentonly` `gamedll` `defensive` |  |
| `phys_shoot_speed` | `250.000000` | `developmentonly` `gamedll` `defensive` |  |
| `phys_show_stats` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_step_threaded` | `true` | `developmentonly` |  |
| `phys_stressbodyweights` | `5.000000` | `developmentonly` `gamedll` `defensive` |  |
| `phys_threaded_cloth_bone_update` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_threaded_kinematic_bone_update` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_threaded_transform_update` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_timescale` | `1.000000` | `developmentonly` `gamedll` `defensive` | Scale time for physics |
| `phys_upimpactforcescale` | `0.375000` | `developmentonly` `gamedll` `defensive` |  |
| `phys_use_block_solver` | `true` | `gamedll` `cheat` | Use block solving for constraint entities |
| `phys_vehicleimpactforcescale` | `1.500000` | `developmentonly` `gamedll` `defensive` |  |
| `phys_visualize_awake_dynamic_only` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_visualize_awake_unattached_only` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `phys_wind_force_scale` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | Scale on the force wind applies to physics bodies |
| `pickup_check_period` | `0.250000` | `developmentonly` `gamedll` `defensive` |  |
| `player_botdifflast_s` | `2` | `clientdll` `archive` `release` |  |
| `player_competitive_maplist_2v2_10_0_D684D4E1` | `mg_de_inferno,mg_de_nuke,mg_de_vertigo,mg_de_debris,mg_de_poseidon,mg_de_eldorado,mg_de_overpass` | `clientdll` `archive` |  |
| `player_competitive_maplist_8_10_0_A062AC6A` | `mg_de_dust2,mg_de_train,mg_de_ancient,mg_de_inferno,mg_de_nuke,mg_de_vertigo,mg_de_mirage,mg_cs_office,mg_cs_italy,mg_de_cache,mg_de_boulder,mg_de_anubis,mg_lobby_mapveto,mg_de_fachwerk,mg_cs_shelter,mg_de_overpass` | `clientdll` `archive` |  |
| `player_debug_off_nav` | `false` | `gamedll` `cheat` |  |
| `player_debug_print_damage` | `false` | `gamedll` `cheat` | When true, print amount and type of all damage received by player to console. |
| `player_nevershow_communityservermessage` | `0` | `clientdll` `archive` `per_user` |  |
| `player_ping_token_cooldown` | `20.000000` | `gamedll` `cheat` `release` | Cooldown for how long it takes for a player's ping token to refresh allowing them to ping again (they get 5 tokens). |
| `player_survival_list_10_0_303` | `mg_dz_blacksite,mg_dz_sirocco,mg_dz_vineyard,mg_dz_ember` | `clientdll` `archive` |  |
| `player_teamplayedlast` | `3` | `clientdll` `archive` `per_user` |  |
| `player_use_radius` | `80.000000` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `player_wargames_list2_10_0_0` | `` | `clientdll` `archive` |  |
| `population_distribution_debug` | `0.000000` | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `pred_cloth_pos_max` | `2.000000` | `developmentonly` `clientdll` |  |
| `pred_cloth_pos_multiplier` | `0.500000` | `developmentonly` `clientdll` |  |
| `pred_cloth_pos_strength` | `0.250000` | `developmentonly` `clientdll` |  |
| `pred_cloth_rot_high` | `0.100000` | `developmentonly` `clientdll` |  |
| `pred_cloth_rot_low` | `0.010000` | `developmentonly` `clientdll` |  |
| `pred_cloth_rot_multiplier` | `0.300000` | `developmentonly` `clientdll` |  |
| `pred_cloth_smooth_motion` | `1` | `developmentonly` `clientdll` |  |
| `pred_cloth_vmax` | `2.000000` | `developmentonly` `clientdll` |  |
| `pred_cloth_vw` | `0.050000` | `developmentonly` `clientdll` |  |
| `presettle_cloth_iterations` | `30` | `developmentonly` `clientdll` `defensive` |  |
| `prop_debug_collision` | `false` | `gamedll` `cheat` | Highlights props based on their collision group: COLLISION_GROUP_PROPS(white), COLLISION_GROUP_INTERACTIVE_DEBRIS(green), COLLISION_GROUP_DEBRIS and will return to COLLISION_GROUP_INTERACTIVE_DEBRIS on sleeping(bright red), COLLISION_GROUP_DEBRIS permanently (dark red), COLLISION_GROUP_DEBRIS(blue), OTHER(grey) |
| `prop_nav_ignore_edge_len` | `-1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_ignore_mass` | `-1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_avoid_mass` | `100.099998` | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_avoid_use_connection_blocker` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_block_edge_min_` | `-1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_block_edge_min_a` | `-1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_block_edge_min_c` | `-1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_block_mass_a` | `-1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_block_mass_b` | `-1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `prop_nav_obstacle_block_mass_c` | `-1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `props_break_apply_radial_forces` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `props_break_max_pieces_perframe` | `16` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Maximum prop breakable piece count per frame (-1 = model default) |
| `props_break_radial_force_ratio` | `0.330000` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `pulse_save_execution_history` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` | Keep a history of all instructions run on a per graph basis. |
| `pulse_save_execution_history_limit` | `10000` | `developmentonly` `gamedll` `clientdll` `replicated` | Keep a history of all instructions run on a per graph basis. |
| `pvs_debugentity` | `-1` | `gamedll` `release` | Verbose spew for this entity when doing IsInPVS computation. |
| `pvs_flowtype` | `0` | `gamedll` `release` | Flow through spawn groups for vis (0 == default, 1 == always visible, 2 == never visible. |
| `pwatchent` | `-1` | `clientdll` `cheat` | Entity to watch for prediction system changes. |
| `pwatchvar` | `` | `clientdll` `cheat` | Entity variable to watch in prediction system for changes. |
| `r_AirboatViewDampenDamp` | `1.000000` | `gamedll` `clientdll` `notify` `replicated` `cheat` |  |
| `r_AirboatViewDampenFreq` | `7.000000` | `gamedll` `clientdll` `notify` `replicated` `cheat` |  |
| `r_AirboatViewZHeight` | `0.000000` | `gamedll` `clientdll` `notify` `replicated` `cheat` |  |
| `r_JeepViewDampenDamp` | `1.000000` | `gamedll` `clientdll` `notify` `replicated` `cheat` |  |
| `r_JeepViewDampenFreq` | `7.000000` | `gamedll` `clientdll` `notify` `replicated` `cheat` |  |
| `r_JeepViewZHeight` | `10.000000` | `gamedll` `clientdll` `notify` `replicated` `cheat` |  |
| `r_RainAllowInSplitScreen` | `false` | `developmentonly` `clientdll` `defensive` | Allows rain in splitscreen |
| `r_RainParticleDensity` | `1.000000` | `developmentonly` `clientdll` `defensive` | Density of Particle Rain 0-1 |
| `r_add_views_in_pre_output` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `r_allow_onesweep_gpusort` | `true` | `developmentonly` `defensive` |  |
| `r_aoproxy_cull_dist` | `12.000000` | `developmentonly` `defensive` | Distance to cull the AO proxy as a factor of size |
| `r_aoproxy_debug` | `false` | `clientdll` `cheat` |  |
| `r_aoproxy_default_ambient_strength` | `1.000000` | `developmentonly` `defensive` |  |
| `r_aoproxy_default_light_cone_angles` | `0.300000 0.300000 0.300000 1.000000` | `developmentonly` `defensive` |  |
| `r_aoproxy_default_light_cone_strengths` | `3.000000 8.000000 1.000000 4.000000` | `developmentonly` `defensive` |  |
| `r_aoproxy_default_light_position_0` | `0.816497 0.000000 0.577350` | `developmentonly` `defensive` |  |
| `r_aoproxy_default_light_position_1` | `-0.408248 0.707107 0.577350` | `developmentonly` `defensive` |  |
| `r_aoproxy_default_light_position_2` | `-0.408248 -0.707107 0.577350` | `developmentonly` `defensive` |  |
| `r_aoproxy_default_light_position_3` | `0.000000 0.000000 1.000000` | `developmentonly` `defensive` |  |
| `r_aoproxy_enable` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_aoproxy_min_dist` | `3.000000` | `developmentonly` `defensive` |  |
| `r_aoproxy_min_dist_box` | `1.000000` | `developmentonly` `defensive` |  |
| `r_aoproxy_show` | `false` | `clientdll` `cheat` |  |
| `r_bloom_tent_filter_radius` | `3.100000` | `developmentonly` `clientdll` `cheat` | bloom mip up-sample filtering radius (using 3x3 tent filter, radius in mip level texels), 0.0 radius => box (2x2) filter with (fixed) 1.0 radius |
| `r_character_decal_monitor_draw_frustum` | `false` | `developmentonly` |  |
| `r_character_decal_monitor_emissive` | `false` | `developmentonly` |  |
| `r_character_decal_monitor_render_res` | `512` | `developmentonly` |  |
| `r_character_decal_renderdoc_capture` | `false` | `developmentonly` |  |
| `r_character_decal_resolution` | `1024` | `developmentonly` `defensive` | Resolution of character decal texture. |
| `r_cs2_show_icon_editor` | `false` | `developmentonly` `clientdll` `replicated` `cheat` `menubar_item` | CSGO/Icon Editor |
| `r_csgo_bloom_threshold_all_samples` | `true` | `developmentonly` `clientdll` | Execute bloom threshold once per sample during downsample (default enabled, higher quality, less bloom aliasing) |
| `r_csgo_bloom_threshold_downsample_jimenez` | `true` | `developmentonly` `clientdll` | Custom downsample based on Jimenez14, (default enabled, higher quality, decreases bloom aliasing further) |
| `r_csgo_cable_pixel_radius_clamp` | `1.200000` | `developmentonly` `clientdll` | Minimum clamped size in pixels of a cable (if using F_CLAMP_MIN_RADIUS 1 in cable material) |
| `r_csgo_cmaa_debug_edges` | `false` | `developmentonly` `clientdll` | debug visualize edges |
| `r_csgo_cmaa_enable` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `r_csgo_cmaa_extra_sharp` | `false` | `developmentonly` `clientdll` `defensive` | trade more sharpness for reduced antialiasing |
| `r_csgo_cmaa_quality` | `3` | `developmentonly` `clientdll` `defensive` | 0=low, 1=medium, 2=high, 3=ultra |
| `r_csgo_csm_max_visible_distance` | `7500.000000` | `developmentonly` `clientdll` |  |
| `r_csgo_csm_max_visible_distance_preview` | `2000.000000` | `developmentonly` `clientdll` |  |
| `r_csgo_csm_override_staticgeo_cascades_alphatest` | `false` | `developmentonly` `clientdll` `defensive` | If lb_csm_override_staticgeo_cascades true, ensure objects with SCENEOBJECTFLAG_ALPHA_TESTED flag will be rendered into cascade. |
| `r_csgo_csm_pushback_distance` | `7000.000000` | `developmentonly` `clientdll` |  |
| `r_csgo_csm_pushback_distance_preview` | `1500.000000` | `developmentonly` `clientdll` |  |
| `r_csgo_cubemap_normalization` | `true` | `clientdll` `cheat` |  |
| `r_csgo_decal_debug` | `false` | `clientdll` `cheat` |  |
| `r_csgo_decals_use_msaa` | `false` | `developmentonly` `clientdll` |  |
| `r_csgo_depth_prepass` | `true` | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_cull_threshold` | `60.000000` | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_skybox_alpha_tested` | `true` | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_skybox_large` | `false` | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_skybox_small` | `false` | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_skybox_small_cull_threshold` | `5.000000` | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_small_cull_threshold` | `10.000000` | `clientdll` `cheat` |  |
| `r_csgo_depth_prepass_viewmodel` | `true` | `clientdll` `cheat` |  |
| `r_csgo_directional_lightmaps` | `true` | `clientdll` `cheat` |  |
| `r_csgo_effects_bloom` | `true` | `clientdll` `cheat` |  |
| `r_csgo_effects_bloom_when_smoked` | `false` | `clientdll` `cheat` |  |
| `r_csgo_enable_cubemap_fog` | `true` | `developmentonly` `clientdll` |  |
| `r_csgo_enable_glows` | `true` | `clientdll` `cheat` |  |
| `r_csgo_enable_gradient_fog` | `true` | `developmentonly` `clientdll` |  |
| `r_csgo_enable_high_precision_lighting` | `true` | `clientdll` `cheat` |  |
| `r_csgo_enable_sunlight_check` | `true` | `developmentonly` `clientdll` `defensive` | Enable vis tests for sunlight. |
| `r_csgo_enable_tonemapping` | `true` | `clientdll` `cheat` |  |
| `r_csgo_enable_translucent_screen_space` | `true` | `clientdll` `cheat` |  |
| `r_csgo_enable_volume_fog` | `false` | `developmentonly` `clientdll` |  |
| `r_csgo_firstpersonlegs_nearz_offset` | `0.100000` | `developmentonly` `clientdll` |  |
| `r_csgo_fsr_enable_mip_bias` | `true` | `developmentonly` `clientdll` `defensive` | Apply negative mip bias when rendering with FSR. |
| `r_csgo_fsr_rcas_sharpness` | `0.250000` | `developmentonly` `clientdll` `defensive` | RCAS sharpness when using FSR + RCAS upsample. |
| `r_csgo_fsr_upsample` | `0` | `developmentonly` `clientdll` `defensive` | 0 == bilinear upsampe, 1 == FSR upsample, 2 == FSR + RCAS upsample |
| `r_csgo_gpu_culling` | `true` | `developmentonly` `clientdll` `menubar_item` `defensive` | CSGO/Graphics/GPU Culling |
| `r_csgo_gpu_culling_camera_offset` | `0.000000` | `developmentonly` `clientdll` |  |
| `r_csgo_gpu_culling_shadows` | `false` | `developmentonly` `clientdll` `menubar_item` `defensive` | CSGO/Graphics/GPU Cull Shadow Views |
| `r_csgo_gpu_culling_shadows_min_cascade` | `1` | `developmentonly` `clientdll` | If r_csgo_gpu_culling_shadows is true, this defines min cascade for which gpu culling is used |
| `r_csgo_gpu_culling_two_pass` | `false` | `developmentonly` `clientdll` `menubar_item` `defensive` | CSGO/Graphics/GPU Culling (Two Pass) |
| `r_csgo_gpu_debug_draw` | `false` | `developmentonly` `clientdll` |  |
| `r_csgo_gpu_opt_downsample_depth_using_resolved_depth` | `true` | `developmentonly` `clientdll` | use already resolved depth as input to downsample depth layer |
| `r_csgo_gpu_opt_firstpersonlegs_visible_angle` | `40.000000` | `developmentonly` `clientdll` | avoid overhead of firstpersonlegs layers if not looking down enough to see them |
| `r_csgo_gpu_opt_prepass_characters` | `true` | `developmentonly` `clientdll` | only depth prepass nearby characters (see r_csgo_gpu_opt_prepass_characters_cull_threshold to control threshold) |
| `r_csgo_gpu_opt_prepass_characters_cull_threshold` | `15.000000` | `developmentonly` `clientdll` | use with r_csgo_gpu_opt_prepass_characters |
| `r_csgo_gpu_opt_resolve_depth_for_decals_on_translucent` | `true` | `developmentonly` `clientdll` | optimize layers for decals on translucent geo, avoid one resolve and some fullscreen passes |
| `r_csgo_gpu_opt_resolve_depth_no_characters` | `true` | `developmentonly` `clientdll` | remove unused resolve |
| `r_csgo_gpu_opt_use_aoproxy_depth_for_depth_pyramid` | `true` | `developmentonly` `clientdll` | if ao proxies enabled, use ao proxy downsampled depth as input to generate the depth pyramid for gpu culling |
| `r_csgo_gpu_opt_viewmodel_stencil` | `true` | `developmentonly` `clientdll` |  |
| `r_csgo_gpu_opt_water_refraction_resolve` | `true` | `developmentonly` `clientdll` | copy already resolved depth for use by waterrefraction layers, instead of resolving main depth again (avoids msaa samples) |
| `r_csgo_gpu_optimizations` | `true` | `developmentonly` `clientdll` | temporary cvar to control new GPU optimzations (depth resolves, etc) |
| `r_csgo_joint_upscale_sigma` | `0.002000` | `developmentonly` `clientdll` |  |
| `r_csgo_max_barnlight_shadow_scale_preview` | `4.000000` | `developmentonly` `clientdll` |  |
| `r_csgo_mboit` | `true` | `clientdll` `cheat` |  |
| `r_csgo_mboit_bias` | `0.000005` | `clientdll` `cheat` |  |
| `r_csgo_mboit_debug` | `false` | `clientdll` `cheat` |  |
| `r_csgo_mboit_force_mixed_resolution` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `r_csgo_mboit_overestimation` | `0.010000` | `clientdll` `cheat` |  |
| `r_csgo_mboit_upscale_cs` | `false` | `clientdll` `cheat` |  |
| `r_csgo_mboit_use_4_moments` | `false` | `clientdll` `cheat` |  |
| `r_csgo_merge_resolve_with_histogram` | `true` | `clientdll` `cheat` |  |
| `r_csgo_microshadowing` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_csgo_mixed_resolution_color_slices` | `false` | `clientdll` `cheat` |  |
| `r_csgo_mixed_resolution_particles` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_csgo_mixed_resolution_particles_minmax` | `false` | `clientdll` `cheat` |  |
| `r_csgo_mixed_resolution_particles_scale` | `2` | `clientdll` `cheat` |  |
| `r_csgo_mouse_trace_coord` | `true` | `clientdll` `cheat` |  |
| `r_csgo_msaa_resolve_apply_exposure_scale` | `true` | `developmentonly` `clientdll` | 0 - before, 1 - after fix for a2c fringing |
| `r_csgo_multiscattering` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_csgo_no_shader_resolve` | `false` | `clientdll` `cheat` |  |
| `r_csgo_opaquerefract_viewmodel_depthcopy` | `false` | `developmentonly` `clientdll` | Copy depth in viewmodel for opaquerefract  |
| `r_csgo_opaquerefract_viewmodel_quality` | `1` | `developmentonly` `clientdll` | Opaque refract quality in viewmodel: 0 = no background copy, no depth, 1= background copy, depth if enabled  |
| `r_csgo_outline_glow_scaledenom` | `1` | `developmentonly` `clientdll` `cheat` |  |
| `r_csgo_player_occlusion_query` | `true` | `developmentonly` `clientdll` |  |
| `r_csgo_player_occlusion_query_debug` | `false` | `developmentonly` `clientdll` |  |
| `r_csgo_postprocess_enable` | `true` | `clientdll` `cheat` |  |
| `r_csgo_r11g11b10_dither_mode` | `2` | `developmentonly` `clientdll` | 0 - disabled, 1 - regular dither noise, 2 - blue noise dither |
| `r_csgo_readonly_depth_stencil_enable` | `true` | `clientdll` `cheat` |  |
| `r_csgo_reconstruct_normals` | `false` | `clientdll` `cheat` |  |
| `r_csgo_reconstruct_normals_method` | `0` | `clientdll` `cheat` |  |
| `r_csgo_render_decals` | `true` | `clientdll` `cheat` |  |
| `r_csgo_render_decals_on_translucent` | `true` | `clientdll` `cheat` |  |
| `r_csgo_render_dither_scale` | `1.000000` | `clientdll` `cheat` |  |
| `r_csgo_render_dynamic_objects` | `true` | `clientdll` `cheat` |  |
| `r_csgo_render_inferno_decals` | `true` | `clientdll` `cheat` |  |
| `r_csgo_render_opaque` | `true` | `clientdll` `cheat` |  |
| `r_csgo_render_overlays` | `true` | `clientdll` `cheat` |  |
| `r_csgo_render_post_bloom` | `1` | `clientdll` `cheat` |  |
| `r_csgo_render_post_bloom_strength` | `-1.000000` | `clientdll` `cheat` |  |
| `r_csgo_render_post_colorcorrection` | `0` | `clientdll` `cheat` |  |
| `r_csgo_render_post_film_grain` | `0` | `clientdll` `cheat` |  |
| `r_csgo_render_post_fxaa` | `0` | `developmentonly` `clientdll` `defensive` |  |
| `r_csgo_render_post_local_contrast` | `true` | `clientdll` `cheat` |  |
| `r_csgo_render_post_mirror_horizontal` | `0` | `clientdll` `cheat` |  |
| `r_csgo_render_post_mirror_vertical` | `0` | `clientdll` `cheat` |  |
| `r_csgo_render_translucent` | `true` | `clientdll` `cheat` |  |
| `r_csgo_resolve_dither_bluenoise_amount` | `4.000000` | `developmentonly` `clientdll` | Equivalent to r_csgo_render_dither_scale, but purely to control bluenoise for R11G11B10 downsample dither (if r_csgo_r11g11b10_dither_mode = 2) |
| `r_csgo_resolve_dither_noise_amount` | `0.200000` | `developmentonly` `clientdll` | Amount of screen space dither noise to apply during resolve (used/essential with R11G11B10_FLOAT RT) |
| `r_csgo_shader_feature_test_value` | `0.000000` | `developmentonly` `clientdll` |  |
| `r_csgo_shader_perf_test` | `false` | `developmentonly` `clientdll` |  |
| `r_csgo_shadow_map_allocation_failure_policy` | `1` | `developmentonly` `clientdll` `cheat` | What happens when a shadow map fails allocation? 0 = don't render, 1 = render unshadowed |
| `r_csgo_shadows_debug` | `0` | `clientdll` `cheat` |  |
| `r_csgo_smoke_avoid_flat` | `true` | `developmentonly` `clientdll` |  |
| `r_csgo_smoke_clip_sniper` | `true` | `developmentonly` `clientdll` |  |
| `r_csgo_smoke_fullres_enhance` | `false` | `developmentonly` `clientdll` | Enhance edges of smokes to eliminate bad pixels |
| `r_csgo_smoke_fullres_pass` | `true` | `developmentonly` `clientdll` | Does a full res pass to cover holes and artifacts in smoke low res |
| `r_csgo_smoke_overlay_min_dt` | `0.015686` | `developmentonly` `clientdll` |  |
| `r_csgo_smoke_shadow` | `true` | `developmentonly` `clientdll` |  |
| `r_csgo_smoke_upscale_discard_pixels_behind` | `false` | `developmentonly` `clientdll` | When upsampling smoke discard pixels behind solid depth to avoid pixelated artifacts |
| `r_csgo_stencil_sniper_zoom` | `true` | `developmentonly` `clientdll` |  |
| `r_csgo_test1` | `false` | `clientdll` `release` |  |
| `r_csgo_tools_vis_cubemap_roughness` | `0.000100` | `developmentonly` `clientdll` `cheat` |  |
| `r_csgo_upscale_depth_threshold` | `3.000000` | `developmentonly` `clientdll` |  |
| `r_csgo_use_compute_bloom` | `false` | `developmentonly` `clientdll` |  |
| `r_csgo_viewmodel_csm_pushback_distance` | `1500.000000` | `developmentonly` `clientdll` |  |
| `r_csgo_viewmodel_envmap_position_bias` | `0.850000` | `developmentonly` `clientdll` `cheat` |  |
| `r_csgo_viewmodel_far_plane` | `100.000000` | `developmentonly` `clientdll` |  |
| `r_csgo_viewmodel_near_plane` | `1.000000` | `developmentonly` `clientdll` |  |
| `r_csgo_viewmodel_probe_clamp_plane_distance` | `16.000000` | `developmentonly` `clientdll` `cheat` |  |
| `r_csgo_volume_mboit_optimization` | `true` | `clientdll` `cheat` |  |
| `r_csgo_water_effects` | `true` | `clientdll` `cheat` |  |
| `r_csgo_water_refraction` | `true` | `clientdll` `cheat` |  |
| `r_csgo_water_skybox_depth` | `true` | `developmentonly` `clientdll` |  |
| `r_cubemap_debug_colors` | `0` | `cheat` |  |
| `r_dashboard_render_quality` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_debug_depth_holes` | `false` | `clientdll` `cheat` |  |
| `r_debug_particle_shadows` | `false` | `clientdll` `cheat` |  |
| `r_debug_precipitation` | `false` | `clientdll` `cheat` | Show precipitation volumes |
| `r_decal_hit_confirmation` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `r_decals` | `2048` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_decals_additional_offset` | `0.010000` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `r_decals_default_fade_duration` | `3.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_decals_default_start_fade` | `30.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_decals_max_on_deformables` | `512` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_decals_overide_fadestarttime_params` | `-1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `commandline_enforced` `defensive` |  |
| `r_decals_overlap_threshold` | `6` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_depth_of_field` | `1` | `developmentonly` `clientdll` | 0 = off, 1 = enabled (high quality, circular bokeh, HDR) |
| `r_directional_lightmaps` | `true` | `developmentonly` `defensive` |  |
| `r_directlighting` | `false` | `reference` |  |
| `r_dof2_maxblursize` | `5.000000` | `developmentonly` `clientdll` |  |
| `r_dof2_radiusscale` | `0.250000` | `developmentonly` `clientdll` |  |
| `r_dopixelvisibility` | `true` | `cheat` |  |
| `r_draw3dskybox` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_draw_overlays` | `true` | `developmentonly` `defensive` |  |
| `r_draw_particle_children_with_parents` | `-1` | `cheat` | Draw particle children with parents (-1=use gameinfo, 0=no, 1=yes) |
| `r_drawchickens` | `true` | `clientdll` `cheat` | Render chickens |
| `r_drawcsplayers` | `true` | `clientdll` `cheat` | Render CS players |
| `r_drawdecals` | `false` | `reference` |  |
| `r_drawdevvisualizers` | `false` | `clientdll` `cheat` | Render dev visualizers |
| `r_drawparticles` | `true` | `cheat` `menubar_item` | SceneSystem/Particles/Draw Particles |
| `r_drawpixelvisibility` | `false` | `developmentonly` `defensive` | Show the occlusion proxies |
| `r_drawropes` | `true` | `clientdll` `cheat` |  |
| `r_drawtracers` | `true` | `clientdll` `cheat` |  |
| `r_drawtracers_firstperson` | `true` | `clientdll` `archive` `release` | Toggle visibility of first person weapon tracers |
| `r_drawviewmodel` | `true` | `clientdll` `cheat` | Render view model |
| `r_enable_rigid_animation` | `false` | `developmentonly` `clientdll` |  |
| `r_extra_render_frames` | `0` | `reference` |  |
| `r_fallback_texture_lod_scale` | `2.000000` | `cheat` | Scale factor for requested texture size (texture streaming) - used for geo that doesn't have a precomputed UV density measure |
| `r_farz` | `-1.000000` | `clientdll` `cheat` | Override the far clipping plane. -1 means to use the value in env_fog_controller. |
| `r_flashlightambient` | `0.000000` | `clientdll` `cheat` |  |
| `r_flashlightbacktraceoffset` | `0.400000` | `clientdll` `cheat` |  |
| `r_flashlightbrightness` | `1.000000` | `clientdll` `replicated` `cheat` |  |
| `r_flashlightconstant` | `0.000000` | `clientdll` `replicated` `cheat` |  |
| `r_flashlightfar` | `1500.000000` | `clientdll` `replicated` `cheat` |  |
| `r_flashlightfov` | `53.000000` | `clientdll` `replicated` `cheat` |  |
| `r_flashlightladderdist` | `40.000000` | `clientdll` `cheat` |  |
| `r_flashlightlinear` | `100.000000` | `clientdll` `replicated` `cheat` |  |
| `r_flashlightlockposition` | `false` | `clientdll` `cheat` |  |
| `r_flashlightmuzzleflashfov` | `120.000000` | `clientdll` `cheat` |  |
| `r_flashlightnear` | `4.000000` | `clientdll` `replicated` `cheat` |  |
| `r_flashlightnearoffsetscale` | `1.000000` | `clientdll` `cheat` |  |
| `r_flashlightoffsetforward` | `0.000000` | `clientdll` `replicated` `cheat` |  |
| `r_flashlightoffsetright` | `5.000000` | `clientdll` `replicated` `cheat` |  |
| `r_flashlightoffsetup` | `-5.000000` | `clientdll` `replicated` `cheat` |  |
| `r_flashlightquadratic` | `0.000000` | `clientdll` `replicated` `cheat` |  |
| `r_flashlightshadowatten` | `0.350000` | `clientdll` `cheat` |  |
| `r_flashlighttracedistcutoff` | `128.000000` | `clientdll` `cheat` |  |
| `r_flashlighttracedistwatercutoff` | `80.000000` | `clientdll` `cheat` |  |
| `r_flashlightvisualizetrace` | `false` | `clientdll` `cheat` |  |
| `r_force_thick_hair` | `false` | `developmentonly` `cheat` |  |
| `r_freeze_sceneobjects` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `r_freezeparticles` | `false` | `cheat` | Pause particle simulation |
| `r_fullscreen_gamma` | `0.000000` | `reference` |  |
| `r_fullscreen_quad_single_triangle` | `true` | `developmentonly` |  |
| `r_gpu_debug_draw_freeze` | `false` | `developmentonly` `clientdll` |  |
| `r_hair_ao` | `true` | `developmentonly` `defensive` |  |
| `r_hair_debug_guides` | `0` | `developmentonly` `cheat` | 1: Highlight guide hairs, 2: draw only guide hairs |
| `r_hair_indirect_transmittance` | `true` | `developmentonly` `defensive` |  |
| `r_hair_meshshader` | `0` | `developmentonly` `defensive` |  |
| `r_hair_shadowtile` | `true` | `developmentonly` `defensive` |  |
| `r_hair_voxels` | `-1` | `developmentonly` `cheat` |  |
| `r_hair_wind_global_scale` | `0.300000` | `developmentonly` `defensive` |  |
| `r_hair_wind_min_noise_speed` | `20.000000` | `developmentonly` `defensive` |  |
| `r_hair_wind_motion_scale` | `0.070000` | `developmentonly` `defensive` |  |
| `r_hair_wind_noise` | `0.200000` | `developmentonly` `defensive` |  |
| `r_hair_wind_noise_occlusion` | `1.000000` | `developmentonly` `defensive` |  |
| `r_hair_wind_noise_size` | `10.000000` | `developmentonly` `defensive` |  |
| `r_hair_wind_occlusion` | `2.000000` | `developmentonly` `defensive` |  |
| `r_haircull_percent` | `-1.000000` | `developmentonly` `cheat` |  |
| `r_hairsort` | `true` | `developmentonly` `cheat` |  |
| `r_icon_csm_pushback_distance` | `-1.000000` | `developmentonly` `clientdll` `cheat` | csm pushback distance, should be much shorter/disabled for icon rendering |
| `r_icon_custommaterial_maxres` | `512` | `developmentonly` `clientdll` `cheat` | maxres for custommaterials when rendering icons |
| `r_icon_generate_offline_mips` | `false` | `developmentonly` `clientdll` `cheat` | generate mips via sidecar file for offline |
| `r_icon_generate_runtime_mips` | `true` | `developmentonly` `clientdll` `cheat` | generate mips for runtime |
| `r_icon_highcontrast_postprocessing_weight` | `0.375000` | `developmentonly` `clientdll` `cheat` | if using high contrast postprocessing, use this weight (weight = 1.0 for characters) |
| `r_icon_image_cache_to_disk` | `true` | `clientdll` `archive` `release` | 1 |
| `r_icon_max_mip_width` | `128` | `developmentonly` `clientdll` `cheat` | r_icon_max_mip_width |
| `r_icon_player_equip_gloves_from_loadout` | `false` | `developmentonly` `clientdll` `cheat` | equip gloves on player for icon rendering from loadout, or use default gloves |
| `r_icon_rendering_height` | `384` | `developmentonly` `clientdll` `hidden` `cheat` | icon rendering height |
| `r_icon_rendering_width` | `512` | `developmentonly` `clientdll` `hidden` `cheat` | icon rendering width |
| `r_icon_show_timing` | `false` | `developmentonly` `clientdll` `cheat` | show timing in output |
| `r_icon_use_kv3_camera` | `false` | `developmentonly` `clientdll` `cheat` | use test kv3 data for camera |
| `r_impact_ricochet_chance` | `0.300000` | `developmentonly` `clientdll` `defensive` |  |
| `r_impacts_alt_orientation` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_impacts_decal_grazing_incidence_cutoff` | `0.550000` | `developmentonly` `clientdll` `defensive` |  |
| `r_impacts_decal_grazing_incidence_variance` | `0.100000` | `developmentonly` `clientdll` `defensive` |  |
| `r_indirectlighting` | `false` | `reference` |  |
| `r_late_particle_job_sync` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `r_light_flickering_enabled` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_light_probe_volume_debug_colors` | `false` | `cheat` |  |
| `r_light_probe_volume_debug_grid` | `0` | `cheat` | Show LPV debug grid, 0: off, 1: closest only 2: closest and keep 3: all |
| `r_light_probe_volume_debug_grid_albedo` | `128 128 128` | `cheat` | albedo for LPV debug grid |
| `r_light_probe_volume_debug_grid_bbox` | `true` | `cheat` | Show LPV bounding box when debug grid is on, 0: off, 1: on |
| `r_light_probe_volume_debug_grid_metalness` | `0.000000` | `cheat` | metalness for LPV debug grid |
| `r_light_probe_volume_debug_grid_prim` | `0` | `cheat` | 0: spheres, 1: cubes |
| `r_light_probe_volume_debug_grid_roughness` | `0.500000` | `cheat` | roughness for LPV debug grid |
| `r_light_probe_volume_debug_grid_samplesize` | `4.000000` | `cheat` | sphere radius (world) for LPV debug grid |
| `r_lightmap_size` | `0` | `reference` |  |
| `r_limit_particle_job_duration` | `false` | `developmentonly` `defensive` |  |
| `r_mapextents` | `16384.000000` | `clientdll` `cheat` | Set the max dimension for the map.  This determines the far clipping plane |
| `r_mixed_shadows_fade_in_time` | `0.500000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_mixed_shadows_fade_out_time` | `0.500000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `r_monitor_3dskybox` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_morphing_enabled` | `true` | `cheat` |  |
| `r_muzzleflashbrightness` | `0.400000` | `clientdll` `replicated` `cheat` |  |
| `r_muzzleflashlinear` | `0.050000` | `clientdll` `replicated` `cheat` |  |
| `r_nearz` | `-1.000000` | `clientdll` `cheat` | Override the near clipping plane. -1 means use the default. |
| `r_particle_allowprerender` | `true` | `developmentonly` |  |
| `r_particle_batch_collections` | `false` | `developmentonly` |  |
| `r_particle_batch_in_fullsort` | `false` | `developmentonly` |  |
| `r_particle_cables_cast_shadows` | `true` | `developmentonly` `defensive` |  |
| `r_particle_cables_culling` | `1` | `developmentonly` `defensive` |  |
| `r_particle_cables_culling_bounds_scale` | `1.200000` | `developmentonly` `defensive` |  |
| `r_particle_cables_dynamic_roundness` | `false` | `developmentonly` `defensive` |  |
| `r_particle_cables_dynamic_roundness_threshold` | `20` | `developmentonly` `defensive` |  |
| `r_particle_cables_render` | `true` | `developmentonly` `defensive` |  |
| `r_particle_cables_render_meshlets` | `true` | `developmentonly` `defensive` |  |
| `r_particle_cables_visualize_roundness` | `false` | `developmentonly` `defensive` |  |
| `r_particle_debug_filter` | `` | `developmentonly` `defensive` | Limit debug visualizations to substring match of effect name |
| `r_particle_debug_force_simulation` | `0` | `developmentonly` `defensive` | -1 for all asleep, 1 for all awake |
| `r_particle_debug_randomseeds` | `false` | `developmentonly` `defensive` | Use random seeds in debug |
| `r_particle_debug_show_attribute` | `-1` | `developmentonly` | Show specific attribute when debugging particle systems |
| `r_particle_debug_show_control_points` | `false` | `developmentonly` | Show all used controlpoints |
| `r_particle_debug_show_rope_segments` | `0` | `developmentonly` | Show rope segments when debugging particle systems - specify a number to isolate to that segment id |
| `r_particle_debug_show_sort_position` | `false` | `developmentonly` | Show the sorting position when debugging particle systems |
| `r_particle_enable_fastpath` | `true` | `developmentonly` |  |
| `r_particle_explicit_fetch` | `false` | `developmentonly` |  |
| `r_particle_fixedrandomseeds` | `false` | `developmentonly` | Use fixed seeds for easier debugging |
| `r_particle_gpu_implicit` | `true` | `developmentonly` `defensive` |  |
| `r_particle_gpu_implicit_cull_columns` | `true` | `developmentonly` |  |
| `r_particle_gpu_implicit_debug_bricks` | `false` | `developmentonly` |  |
| `r_particle_gpu_implicit_debug_stats` | `false` | `developmentonly` |  |
| `r_particle_gpu_implicit_debug_wireframe` | `false` | `developmentonly` |  |
| `r_particle_gpu_implicit_lds_cache` | `false` | `developmentonly` |  |
| `r_particle_max_detail_level` | `3` | `developmentonly` `defensive` | The maximum detail level of particle to create |
| `r_particle_max_draw_distance` | `1000000.000000` | `cheat` | The maximum distance that particles will render |
| `r_particle_max_size_cull` | `1200.000000` | `developmentonly` `defensive` | Particle systems larger than this in every dimension skip culling to save CPU.  They will be drawn anyway. |
| `r_particle_max_texture_layers` | `-1` | `developmentonly` `defensive` |  |
| `r_particle_min_timestep` | `0.000000` | `developmentonly` `defensive` | A minimum on particle simulation time, particle simulation happening more frequently than this will lerp. |
| `r_particle_mixed_resolution_viewstart` | `500.000000` | `developmentonly` |  |
| `r_particle_model_new` | `false` | `developmentonly` |  |
| `r_particle_model_new8` | `true` | `developmentonly` |  |
| `r_particle_model_per_thread_count` | `32` | `developmentonly` |  |
| `r_particle_multiplier` | `1` | `cheat` | Render each particle system N times for perf testing |
| `r_particle_newinput` | `false` | `developmentonly` | Enable input path in particle ops |
| `r_particle_render_refreshes_sleep_timer` | `true` | `developmentonly` | Disable to get a better look at what's happening offscreen |
| `r_particle_render_sprites_issue_vizquery` | `true` | `developmentonly` |  |
| `r_particle_render_test` | `false` | `developmentonly` `defensive` | render particles 100 times and show perf |
| `r_particle_shadow_map_texture_size` | `1536` | `developmentonly` `clientdll` `defensive` |  |
| `r_particle_shadows` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_particle_shadows_cast_on_particles` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_particle_shadows_cast_on_particles_scale` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_particle_shadows_cast_on_world` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_particle_shadows_compute` | `true` | `clientdll` `release` |  |
| `r_particle_skip_postsim` | `false` | `developmentonly` |  |
| `r_particle_testbuffers` | `false` | `developmentonly` `defensive` |  |
| `r_particle_timescale` | `1.000000` | `developmentonly` `defensive` |  |
| `r_particle_warn_threshold_ms` | `0.000000` | `developmentonly` `defensive` | Threshold to warn about when rendering particles. |
| `r_particles_memset_at_init` | `1` | `developmentonly` | 0=don't clear particle attrs at init 1=clear to zero 2=clear to 0xdb -1=clear to zero at first sim |
| `r_physics_particle_op_spawn_scale` | `1.000000` | `developmentonly` |  |
| `r_pixelvisibility_partial` | `true` | `cheat` |  |
| `r_pixelvisibility_spew` | `false` | `cheat` |  |
| `r_player_fog_distance_multiplier` | `1.700000` | `developmentonly` `clientdll` `cheat` |  |
| `r_player_fog_maxdensity_multiplier` | `0.600000` | `developmentonly` `clientdll` `cheat` |  |
| `r_player_visibility_mode` | `1` | `clientdll` `archive` `release` |  |
| `r_player_visibility_stencil` | `true` | `developmentonly` `clientdll` `cheat` |  |
| `r_player_visibility_strength` | `1.100000` | `developmentonly` `clientdll` `cheat` |  |
| `r_post_bloom_debug` | `0` | `developmentonly` `clientdll` | 1 = bloom output (before thresholding), 2 = quarter res downsample, 3 = quarter res effects bloom 4 = quarter res effects raw |
| `r_propsmaxdist` | `1200.000000` | `developmentonly` `clientdll` `defensive` | Maximum visible distance |
| `r_render_hair` | `true` | `developmentonly` `cheat` |  |
| `r_render_to_cubemap_begin_mixing_roughness` | `0.250000` | `developmentonly` `clientdll` `defensive` |  |
| `r_render_to_cubemap_debug` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `r_replay_post_effect` | `-1` | `clientdll` `cheat` |  |
| `r_reset_character_decals` | `false` | `developmentonly` `defensive` |  |
| `r_ropetranslucent` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_screen_size_expansion` | `0` | `developmentonly` `clientdll` `defensive` |  |
| `r_shadows` | `true` | `cheat` |  |
| `r_shadowtile_waveops` | `false` | `reference` |  |
| `r_show_build_info` | `true` | `clientdll` `archive` `release` | Build information. Leave this enabled when submitting bug screenshots and videos, please! |
| `r_show_time_info` | `false` | `clientdll` `release` | Show real time, large. |
| `r_showdebugoverlays` | `false` | `reference` |  |
| `r_showsceneobjectbounds` | `false` | `reference` |  |
| `r_size_cull_threshold_fade` | `0.000000` | `reference` |  |
| `r_size_cull_threshold_shadow` | `0.000000` | `reference` |  |
| `r_skinning_enabled` | `true` | `cheat` |  |
| `r_smooth_morph_normals` | `true` | `release` |  |
| `r_spectator_flashbang_opacity` | `0.600000` | `clientdll` `archive` | Spectator flash opacity |
| `r_ssao` | `false` | `reference` |  |
| `r_ssao_bias` | `0.500000` | `developmentonly` `defensive` |  |
| `r_ssao_blur` | `true` | `developmentonly` `defensive` |  |
| `r_ssao_radius` | `30.000000` | `developmentonly` `defensive` |  |
| `r_ssao_strength` | `1.200000` | `developmentonly` `defensive` |  |
| `r_strip_invisible_during_sceneobject_update` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `r_test1_maximum_wait_ms` | `10.000000` | `clientdll` `release` |  |
| `r_texture_lod_scale` | `1.000000` | `cheat` | Scale factor for requested texture size (texture streaming) |
| `r_threaded_particle_creation` | `true` | `developmentonly` `defensive` |  |
| `r_threaded_particles` | `true` | `developmentonly` `defensive` |  |
| `r_threaded_scene_object_update` | `true` | `developmentonly` `clientdll` `defensive` |  |
| `r_ui_update_parallel_with_server` | `false` | `reference` |  |
| `r_update_particles_on_render_only_frames` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `radarvisdistance` | `1000.000000` | `gamedll` `cheat` | at this distance and beyond you need to be point right at someone to see them |
| `radarvismaxdot` | `0.996000` | `gamedll` `cheat` | how closely you have to point at someone to see them beyond max distance |
| `radarvismethod` | `1` | `gamedll` `cheat` | 0 for traditional method, 1 for more realistic method |
| `radarvispow` | `0.400000` | `gamedll` `cheat` | the degree to which you can point away from a target, and still see them on radar. |
| `ragdoll_debug_item_detachment` | `false` | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `ragdoll_fixup_joint_limits` | `true` | `developmentonly` `gamedll` `replicated` | Adjusts bone transforms so that physics joints don't appear violated (limits) |
| `ragdoll_fixup_joint_limits_max_height` | `1` | `developmentonly` `gamedll` `replicated` | Disable ragdoll_fixup_joint_limits on joints too high in the hierarchy because long chains tend to depend on violating limits |
| `ragdoll_fixup_joint_orientation` | `true` | `developmentonly` `gamedll` `replicated` | Adjusts bone transforms so that physics joints don't appear violated (orientation) |
| `ragdoll_fixup_joint_orientation_max_height` | `10` | `developmentonly` `gamedll` `replicated` | Disable ragdoll_fixup_joint_orientation on joints too high in the hierarchy because small differences can massively accumulate (e.g. long chains) |
| `ragdoll_fixup_joint_translation` | `true` | `developmentonly` `gamedll` `replicated` | Adjusts bone transforms so that physics joints don't appear violated (translation) |
| `ragdoll_friction_scale` | `0.600000` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_gravity_scale` | `1.000000` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_impact_strength` | `500.000000` | `developmentonly` `clientdll` `defensive` |  |
| `ragdoll_lru_debug_removal` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_lru_min_age` | `10.000000` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_move_entity` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_override_root_orientation` | `true` | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `ragdoll_parallel_pose_control` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `ragdoll_prop_settle` | `true` | `developmentonly` `gamedll` `replicated` `defensive` | Enable more aggressive ragdoll settling |
| `ragdoll_prop_sleepaftertime` | `4.000000` | `developmentonly` `gamedll` `replicated` `defensive` | After this many seconds of being basically stationary, the ragdoll will go to sleep. |
| `ragdoll_prop_sleepdisabletime` | `1.500000` | `developmentonly` `gamedll` `replicated` `defensive` | Ragdoll is not allowed to physically sleep until this timer has elapsed. |
| `ragdoll_resolve_initial_conflict` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_resolve_separation` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_scale_sleep_tolerance` | `true` | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `ragdoll_update_from_weights` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `ragdoll_visualize_creation_skeleton` | `false` | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `ragdoll_vphysics_scale` | `0.500000` | `developmentonly` `gamedll` `replicated` `defensive` | How much we scale physics impacts against the ragdoll. |
| `recast_mark_overhang` | `false` | `gamedll` `replicated` `cheat` | Enable/disable overhang detection |
| `recast_partitioning` | `0` | `gamedll` `replicated` `cheat` | 0 = watershed, 1 = monotone, 2 = layers |
| `report_cliententitysim` | `false` | `clientdll` `cheat` | List all clientside simulations and time - will report and turn itself off. |
| `report_clientthinklist` | `false` | `clientdll` `cheat` | List all clientside entities thinking and time - will report and turn itself off. |
| `rope_averagelight` | `true` | `developmentonly` `clientdll` `defensive` | Makes ropes use average of cubemap lighting instead of max intensity. |
| `rope_collide` | `1` | `developmentonly` `clientdll` `defensive` | Collide rope with the world |
| `rope_shake` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `rope_smooth_enlarge` | `1.400000` | `developmentonly` `clientdll` `defensive` | How much to enlarge ropes in screen space for antialiasing effect |
| `rope_smooth_maxalpha` | `0.500000` | `developmentonly` `clientdll` `defensive` | Alpha for rope antialiasing effect |
| `rope_smooth_maxalphawidth` | `1.750000` | `developmentonly` `clientdll` `defensive` |  |
| `rope_smooth_minalpha` | `0.200000` | `developmentonly` `clientdll` `defensive` | Alpha for rope antialiasing effect |
| `rope_smooth_minwidth` | `0.300000` | `developmentonly` `clientdll` `defensive` | When using smoothing, this is the min screenspace width it lets a rope shrink to |
| `rope_subdiv` | `2` | `developmentonly` `clientdll` `defensive` | Rope subdivision amount |
| `rope_wind_dist` | `1000.000000` | `developmentonly` `clientdll` `defensive` | Don't use CPU applying small wind gusts to ropes when they're past this distance. |
| `rr_debugclassname` | `` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | If set, rr_debugclassname will print only response tests where 'classname' corresponds to this variable. Use to filter for a specific character. |
| `rr_debugresponseconcept` | `` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | If set, rr_debugresponseconcept will print only responses testing for the specified concept |
| `rr_debugresponses` | `0` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Show verbose matching output (1 for simple, 2 for rule scoring, 3 for noisy). If set to 4, it will only show response success/failure for npc_selected NPCs. |
| `rr_debugrule` | `` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | If set to the name of the rule, that rule's score will be shown whenever a concept is passed into the response rules system. |
| `rr_followup_maxdist` | `1800.000000` | `gamedll` `cheat` | 'then ANY' or 'then ALL' response followups will be dispatched only to characters within this distance. |
| `rr_thenany_score_slop` | `0.000000` | `gamedll` `archive` `cheat` | When computing respondents for a 'THEN ANY' rule, all rule-matching scores within this much of the best score will be considered. |
| `rtx_dynamic_blas` | `true` | `developmentonly` `defensive` | Allow dynamic BLAS creation for geometry going through the compute shader skinning path. |
| `rtx_dynamic_blas_caching` | `true` | `developmentonly` `defensive` | Cache dynamic BLAS if geometry has not changed |
| `rtx_force_default_hitgroup` | `false` | `developmentonly` `defensive` | Forces all ray traced geometry to use default hit shaders instead of specialized ones. |
| `rtx_texture_resolution` | `512` | `developmentonly` `defensive` | Sets the texture resolution the raytracer will mark to stream in |
| `run_voicecontainer_async` | `false` | `developmentonly` |  |
| `safezonex` | `1.000000` | `clientdll` `archive` | The percentage of the screen width that is considered safe from overscan. Cannot result in a width less than the height. |
| `safezoney` | `1.000000` | `clientdll` `archive` | The percentage of the screen height that is considered safe from overscan |
| `save_async` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `save_debug_snapshots` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Save/Load debug snapshot data |
| `save_fake_hitch` | `0` | `developmentonly` `gamedll` `defensive` | Force a busy wait for the specified number of milliseconds during save to simulate a hitch |
| `save_history_count` | `1` | `developmentonly` `gamedll` `defensive` | Keep this many old copies in history of autosaves and quicksaves. |
| `save_maxarray_spew` | `10` | `gamedll` `release` | Max number of array entries to spew when using SaveRestoreIO spewing. |
| `save_parallel` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `save_screenshot` | `2` | `developmentonly` `gamedll` `defensive` | 0 = none, 1 = non-autosave, 2 = always, 3 = bug_only |
| `save_spew` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `save_write_kv3` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Write the KV3 entity data as a text file in the save directory |
| `saving_enabled` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sc_aggregate_bvh` | `true` | `developmentonly` |  |
| `sc_aggregate_bvh_threshold` | `128` | `developmentonly` |  |
| `sc_aggregate_debug_draw_meshlets` | `0` | `developmentonly` `menubar_item` | SceneSystem/Aggregates/Visualize Meshlets |
| `sc_aggregate_debug_draw_meshlets_bounds` | `false` | `developmentonly` | Visualize meshlet bounds and cone axis. Mesh shader only. |
| `sc_aggregate_debug_visualizer` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/Aggregates/Debug Visualizer |
| `sc_aggregate_fragment_merging` | `true` | `developmentonly` |  |
| `sc_aggregate_gpu_culling` | `true` | `developmentonly` `defensive` | Toggles GPU culling of aggregate meshes |
| `sc_aggregate_gpu_culling_conservative_bounds` | `false` | `developmentonly` |  |
| `sc_aggregate_gpu_culling_show_culled` | `false` | `developmentonly` `menubar_item` | SceneSystem/Aggregates/Show GPU Culled Meshes |
| `sc_aggregate_gpu_occlusion_culling` | `true` | `developmentonly` `defensive` |  |
| `sc_aggregate_indirect_draw_compaction` | `true` | `release` | Use multidrawindirect...count if the driver/hardware supports it |
| `sc_aggregate_indirect_draw_compaction_threshold` | `8` | `release` | Threshold of indirect draws when we will do compaction |
| `sc_aggregate_instance_streams` | `true` | `developmentonly` | Enable instance streams |
| `sc_aggregate_material_solo` | `` | `developmentonly` `cheat` |  |
| `sc_aggregate_render_mesh_shader` | `true` | `developmentonly` | Using mesh shaders if available instead of drawcalls |
| `sc_aggregate_rtproxy_debug_visualizer` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/Aggregates/RT Proxy Debug Visualizer |
| `sc_aggregate_rtproxy_instanced_geo` | `true` | `developmentonly` `cheat` |  |
| `sc_aggregate_rtproxy_unique_geo` | `true` | `developmentonly` `cheat` |  |
| `sc_aggregate_rtproxy_visualize` | `false` | `developmentonly` `cheat` |  |
| `sc_aggregate_show_outside_vis` | `false` | `developmentonly` |  |
| `sc_allow_dithered_lod` | `true` | `developmentonly` `defensive` | Allow use of dithered lod transitions |
| `sc_allow_dynamic_constant_batching` | `true` | `developmentonly` `defensive` |  |
| `sc_allow_write_depth_before_blend` | `true` | `developmentonly` `defensive` |  |
| `sc_barnlight_enable_precomputed_vis` | `true` | `developmentonly` `defensive` | Enable use of precomputed vis membership for lights (requires map restart) |
| `sc_batch_layer_cb_updates` | `true` | `developmentonly` `defensive` |  |
| `sc_cache_envmap_lpv_lookup` | `true` | `developmentonly` `defensive` |  |
| `sc_clutter_density_full_size` | `0.007500` | `developmentonly` `defensive` | Screen-size where clutter will be full density |
| `sc_clutter_density_none_size` | `0.003500` | `developmentonly` `defensive` | Screen-size where clutter will be gone |
| `sc_clutter_desity_override` | `false` | `developmentonly` |  |
| `sc_clutter_enable` | `true` | `developmentonly` `menubar_item` | SceneSystem/Clutter/Draw Clutter |
| `sc_disableThreading` | `false` | `cheat` |  |
| `sc_disable_baked_lighting` | `false` | `developmentonly` `defensive` |  |
| `sc_disable_culling_boxes` | `false` | `cheat` |  |
| `sc_disable_procedural_layer_rendering` | `false` | `cheat` |  |
| `sc_disable_shadow_fastpath` | `false` | `cheat` |  |
| `sc_disable_spotlight_shadows` | `false` | `cheat` |  |
| `sc_disable_world_materials` | `false` | `cheat` |  |
| `sc_distancefield_visualize_atlas` | `false` | `developmentonly` `defensive` |  |
| `sc_dithered_lod_transition_amt` | `0.075000` | `developmentonly` `defensive` | Percentage of the transition between two lods we will apply a dither |
| `sc_draw_aggregate_meshes` | `true` | `developmentonly` `menubar_item` | SceneSystem/Aggregates/Draw Aggregates |
| `sc_dump_lists` | `` | `cheat` |  |
| `sc_enable_discard` | `true` | `developmentonly` `defensive` |  |
| `sc_extended_stats` | `false` | `cheat` |  |
| `sc_fade_distance_scale_override` | `-1.000000` | `cheat` |  |
| `sc_force_lod_level` | `-1` | `cheat` |  |
| `sc_force_materials_batchable` | `false` | `cheat` |  |
| `sc_force_single_display_list_per_layer` | `false` | `developmentonly` `defensive` |  |
| `sc_force_translation_in_projection` | `false` | `cheat` | If enabled, the camera's translation will be included in the projection matrix. |
| `sc_hdr_enabled_override` | `-1` | `developmentonly` `performing_callbacks` `defensive` | Override default setting for HDR rendering. -1 default, 0 NoHdr, 1 Hdr, 2 Hdr 1010102 3 Hdr 111110 |
| `sc_imgui_show_debug_log` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/Imgui/Show Debug Log |
| `sc_imgui_show_id_stack` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/Imgui/Show ID Stack Tool |
| `sc_imgui_show_metrics` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/Imgui/Show Metrics |
| `sc_instanced_debug_visualizer` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/Instanced/Debug Visualizer |
| `sc_instanced_gpu_culling_show_culled` | `false` | `developmentonly` `menubar_item` | SceneSystem/Instanced/Show GPU Culled Meshlets |
| `sc_instanced_material_solo` | `` | `developmentonly` `cheat` |  |
| `sc_instanced_mesh_enable` | `true` | `developmentonly` `cheat` `menubar_item` | SceneSystem/Instanced/Draw Instanced |
| `sc_instanced_mesh_gpu_culling` | `true` | `developmentonly` `defensive` | Toggles GPU culling of instanced meshes |
| `sc_instanced_mesh_gpu_density_culling` | `true` | `developmentonly` `defensive` | Toggles density culling (if enabled) |
| `sc_instanced_mesh_gpu_occlusion_culling` | `true` | `developmentonly` `defensive` | Toggles GPU occlusion of instanced meshes |
| `sc_instanced_mesh_gpu_vis_culling` | `true` | `developmentonly` `defensive` | Toggles GPU vis of instanced meshes |
| `sc_instanced_mesh_lod_bias` | `1.250000` | `developmentonly` `defensive` | Bias for LOD selection of instanced meshes |
| `sc_instanced_mesh_lod_bias_shadow` | `1.750000` | `developmentonly` `defensive` | Bias for LOD selection of instanced meshes in shadowmaps |
| `sc_instanced_mesh_motion_vectors` | `true` | `developmentonly` `defensive` | Toggles motion vector support for instanced meshes |
| `sc_instanced_mesh_opaque_fade` | `true` | `developmentonly` `defensive` | Toggles fade support for instanced meshes |
| `sc_instanced_mesh_size_cull_bias` | `1.500000` | `developmentonly` `defensive` | Bias for size culling of instanced meshes |
| `sc_instanced_mesh_size_cull_bias_shadow` | `2.000000` | `developmentonly` `defensive` | Bias for size culling instanced meshes in shadowmaps |
| `sc_instanced_mesh_solo` | `` | `developmentonly` `cheat` |  |
| `sc_keep_all_layers` | `false` | `developmentonly` `defensive` |  |
| `sc_layer_batch_threshold` | `128` | `developmentonly` `defensive` |  |
| `sc_layer_batch_threshold_fullsort` | `80` | `developmentonly` `defensive` |  |
| `sc_max_framebuffer_copies_per_layer` | `1` | `developmentonly` `defensive` |  |
| `sc_mesh_backface_culling` | `true` | `developmentonly` `defensive` |  |
| `sc_mesh_gpu_occlusion_culling` | `true` | `developmentonly` `defensive` |  |
| `sc_mesh_gpu_volume_culling` | `true` | `developmentonly` `defensive` |  |
| `sc_mesh_mesh_shaders` | `false` | `developmentonly` `defensive` |  |
| `sc_mesh_shadows_batch_across_materials` | `true` | `developmentonly` `defensive` |  |
| `sc_mesh_use_pmb` | `false` | `developmentonly` `defensive` |  |
| `sc_no_cull` | `false` | `developmentonly` `defensive` |  |
| `sc_no_vis` | `false` | `developmentonly` `defensive` |  |
| `sc_only_render_opaque` | `false` | `cheat` |  |
| `sc_only_render_shadowcasters` | `false` | `cheat` |  |
| `sc_particle_debug_visualizer` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/Particles/Debug Visualizer |
| `sc_reject_all_objects` | `false` | `cheat` |  |
| `sc_rendergraph_debug_visualizer` | `false` | `developmentonly` `menubar_item` | SceneSystem/RenderGraph Visualizer |
| `sc_screen_size_lod_scale_override` | `-1.000000` | `cheat` |  |
| `sc_shadow_depth_bias` | `256` | `developmentonly` `defensive` |  |
| `sc_shadow_depth_bias_clamp` | `0.000000` | `developmentonly` `defensive` |  |
| `sc_shadow_depth_bias_state_override` | `false` | `developmentonly` `defensive` |  |
| `sc_shadow_slopescale_depth_bias` | `2.130000` | `developmentonly` `defensive` |  |
| `sc_show_cs_skinning_stats` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/Compute Skinning Stats |
| `sc_show_gpu_profiler` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/GPU Profiler |
| `sc_show_hair_debug_ui` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/Hair Debug UI |
| `sc_show_object_browser` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/SceneObject Browser |
| `sc_show_texture_visualizer` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/Texture Visualizer |
| `sc_show_view_profiler` | `false` | `developmentonly` `cheat` `menubar_item` | SceneSystem/View Profiler |
| `sc_skip_traversal` | `false` | `cheat` |  |
| `sc_spew_cmt_usage` | `false` | `developmentonly` `defensive` |  |
| `sc_throw_away_all_layers` | `false` | `developmentonly` `defensive` |  |
| `sc_use_clear_subrect` | `false` | `developmentonly` `defensive` |  |
| `sc_view_profiler_frame_averaging` | `10` | `developmentonly` `defensive` |  |
| `sc_visualize_batches` | `0` | `developmentonly` `defensive` | color per batch |
| `sc_visualize_sceneobjects` | `SCENEOBJECT_VIS_NONE` | `developmentonly` `menubar_item` `defensive` | SceneSystem/Visualize SceneObject Mode |
| `sc_visualize_sceneobjects_meshlets` | `SCENEOBJECT_MESHLET_VIS_NONE` | `developmentonly` `menubar_item` | SceneSystem/Visualize Base SceneObject Meshlets |
| `scene_clientflex` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Do client side flex animation. |
| `scene_print` | `0` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | When playing back a scene, print timing and event info to console. |
| `scene_vcdautosave` | `false` | `developmentonly` `clientdll` `defensive` | Create a savegame before VCD playback |
| `screenmessage_notifytime` | `8.000000` | `developmentonly` `gamedll` `defensive` | How long to display screen message text |
| `screenmessage_show` | `-1` | `cheat` | Enable display of console messages on screen. 1 = Enabled, 0 = Disabled, -1 = Enabled if vgui is not present |
| `script_attach_debugger_at_startup` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `script_break_in_native_debugger_on_error` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `sensitivity` | `1.250000` | `clientdll` `archive` `userinfo` `per_user` | Mouse sensitivity. |
| `sensitivity_y_scale` | `1.000000` | `clientdll` `archive` `userinfo` `per_user` | Multiplies the mouse Y axis for finer pitch vs yaw aim |
| `servercfgfile` | `server.cfg` | `gamedll` `release` |  |
| `shake_show` | `false` | `developmentonly` `clientdll` `defensive` | Displays a list of the active screen shakes. |
| `shatterglass_cleanup` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `shatterglass_cleanup_max` | `200` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `shatterglass_debug` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `shatterglass_hit_tolerance` | `2.000000` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `shatterglass_shard_lifetime` | `15.000000` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `show_visibility_boxes` | `false` | `clientdll` `cheat` | Enable or Disable debug display of visibility boxes |
| `silence_dsp` | `false` | `cheat` | When on, silences all DSP mixes. |
| `sk_autoaim_mode` | `1` | `gamedll` `clientdll` `archive` `replicated` |  |
| `sk_player_arm` | `1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `sk_player_chest` | `1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `sk_player_head` | `2.000000` | `developmentonly` `gamedll` `defensive` |  |
| `sk_player_leg` | `1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `sk_player_stomach` | `1.000000` | `developmentonly` `gamedll` `defensive` |  |
| `skel_constraints_enable` | `true` | `replicated` `cheat` |  |
| `skel_debug` | `` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `skeleton_instance_debug_bodygroups` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Debug bodygroups |
| `skeleton_instance_lod_optimization` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` | Compute LOD mask internally like since 2016, i.e. force all LOD groups' bones to compute |
| `skeleton_instance_scaleset_enable` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `skeleton_instance_smear_boneflags` | `false` | `gamedll` `cheat` | Smear boneflags across the model.  Costs computation, but tests to make sure your bone flags are consistent. |
| `skeleton_physics_joint_fixup` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` |  |
| `skill` | `1` | `gamedll` `clientdll` `archive` `replicated` `per_user` | Game skill level. |
| `slope_drop_enable` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Toggles a test dropping the view offset based on the slope |
| `slope_drop_max_offset` | `16.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | The maximum distance to adjust the view height |
| `slope_drop_off_ground_blend_speed` | `160.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | The speed with which the slope drop is blended out when the entity leaves the ground |
| `smoke_grenade_ct_color` | `75.000000 127.000000 155.000000` | `developmentonly` `gamedll` `cheat` |  |
| `smoke_grenade_t_color` | `180.000000 129.000000 50.000000` | `developmentonly` `gamedll` `cheat` |  |
| `smoke_param1` | `6.260000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `smoke_param2` | `8.270000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `smoke_param3` | `0.130000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `smoke_param4` | `0.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `smoke_param5` | `0` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `smoke_use_noise_texture` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `smoke_volume_lod_ratio_change` | `0.600000` | `developmentonly` `clientdll` |  |
| `smoothstairs` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Smooth player eye z coordinate when traversing stairs. |
| `snd_async_spew_blocking` | `0` | `developmentonly` `defensive` | Spew message to console any time async sound loading blocks on file i/o. |
| `snd_autodetect_latency` | `true` | `archive` |  |
| `snd_beatpattern_show_bpm` | `false` | `cheat` |  |
| `snd_beatpattern_show_events` | `false` | `cheat` |  |
| `snd_beatpattern_show_quantize_queue` | `false` | `cheat` |  |
| `snd_beatpattern_use_lookahead` | `false` | `cheat` |  |
| `snd_boxverb_simd` | `true` | `developmentonly` `defensive` | Enable SIMD code path for shoebox reverb processor. |
| `snd_boxverb_simd_svf` | `1` | `developmentonly` `defensive` | 0 = use biquad instead of svf, 1 = use vectorized svf, 2 = use scalar svf |
| `snd_break_on_start_soundevent` | `` | `gamedll` `clientdll` `replicated` `cheat` | Use to debug break on any soundevent that is started matching this name |
| `snd_compare_KV_convert` | `false` | `developmentonly` `defensive` |  |
| `snd_deathcamera_volume` | `0.160000` | `clientdll` `archive` `release` | Volume of Deathcam Timers |
| `snd_delay_sound_ms_max` | `250.000000` | `developmentonly` `defensive` | Sound device synchronization max delay (ms) |
| `snd_delay_sound_ms_shift` | `23.000000` | `developmentonly` `defensive` | Sound device synchronization shift (ms) |
| `snd_diffusor_simd` | `false` | `developmentonly` `defensive` | Enable SIMD code path for diffusor processor. |
| `snd_disable_mixer_duck` | `false` | `cheat` |  |
| `snd_disable_mixer_solo` | `false` | `cheat` |  |
| `snd_disable_radar_visualize` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_dsp_distance_max` | `2000.000000` | `cheat` |  |
| `snd_dsp_distance_min` | `20.000000` | `cheat` |  |
| `snd_duckerattacktime` | `0.500000` | `archive` |  |
| `snd_duckerreleasetime` | `2.500000` | `archive` |  |
| `snd_duckerthreshold` | `0.150000` | `archive` |  |
| `snd_ducktovolume` | `0.550000` | `archive` |  |
| `snd_enable_imgui` | `false` | `developmentonly` `archive` `cheat` `menubar_item` | Game/Sound System Debugger |
| `snd_enable_subgraph_corenull_passthrough` | `true` | `developmentonly` `defensive` |  |
| `snd_enable_subgraph_log` | `false` | `developmentonly` `defensive` |  |
| `snd_envelope_rate` | `0.900000` | `cheat` |  |
| `snd_eq_arms_race` | `-1` | `developmentonly` `clientdll` `archive` |  |
| `snd_eq_casual` | `-1` | `developmentonly` `clientdll` `archive` |  |
| `snd_eq_competitive` | `-1` | `developmentonly` `clientdll` `archive` |  |
| `snd_eq_deathmatch` | `-1` | `developmentonly` `clientdll` `archive` |  |
| `snd_eq_spectator` | `-1` | `developmentonly` `clientdll` `archive` |  |
| `snd_eq_warmup` | `-1` | `developmentonly` `clientdll` `archive` |  |
| `snd_event_cone_debug` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` |  |
| `snd_event_oriented_box_debug` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` |  |
| `snd_event_oriented_lerp_max_distance` | `64.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` |  |
| `snd_event_oriented_lerp_min_distance` | `24.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` |  |
| `snd_filter` | `` | `cheat` |  |
| `snd_foliage_db_loss` | `4.000000` | `gamedll` `cheat` | foliage dB loss per 1200 units |
| `snd_gain` | `1.000000` | `archive` |  |
| `snd_gain_max` | `1.000000` | `cheat` |  |
| `snd_gain_min` | `0.010000` | `cheat` |  |
| `snd_gamevoicevolume` | `1.000000` | `archive` | Game v.o. volume |
| `snd_gamevolume` | `1.000000` | `archive` | Game volume |
| `snd_group_cluster_debug` | `false` | `replicated` `cheat` |  |
| `snd_group_occlusion_debug` | `false` | `developmentonly` |  |
| `snd_group_priority_debug` | `false` | `replicated` `cheat` |  |
| `snd_group_priority_max_tolerance` | `0.050000` | `replicated` `cheat` |  |
| `snd_headphone_eq` | `0` | `clientdll` `archive` `clientcmd_can_execute` | Select Headphone EQ Preset |
| `snd_headphone_eq_active` | `0` | `clientdll` `clientcmd_can_execute` | Select Headphone EQ Preset |
| `snd_hrtf_distance_behind` | `0.000000` | `developmentonly` `defensive` | HRTF calculations will calculate the player as being this far behind the camera. |
| `snd_list` | `` | `cheat` |  |
| `snd_log_empty_event_entities` | `false` | `clientdll` `cheat` | Logs the sound event entities that have empty names. |
| `snd_mainmenu_music_break_time_max` | `0` | `clientdll` `cheat` | Maximum amount of time to pause between playing main menu music |
| `snd_mainmenu_music_break_time_min` | `0` | `clientdll` `cheat` | Minimum amount of time to pause between playing main menu music |
| `snd_mapobjective_volume` | `0.040000` | `clientdll` `archive` `release` | Volume of Map Objective Music |
| `snd_max_pitch_shift_inaccuracy` | `0.080000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_menumap_volume` | `1.000000` | `clientdll` `archive` `release` | Volume of background sounds for maps |
| `snd_menumusic_volume` | `0.040000` | `clientdll` `archive` `release` | Volume of Menu / Non-gameplay music |
| `snd_mergemethod` | `1` | `developmentonly` `defensive` | Sound merge method (0 == sum and clip, 1 == max, 2 == avg). |
| `snd_min_latency` | `false` | `developmentonly` `cheat` |  |
| `snd_mix_async` | `true` | `developmentonly` `cheat` |  |
| `snd_mixahead` | `0.001000` | `archive` |  |
| `snd_mixer_master_dsp` | `1.000000` | `cheat` |  |
| `snd_mixer_master_level` | `1.000000` | `cheat` |  |
| `snd_musicvolume` | `1.000000` | `archive` | Music volume |
| `snd_mute_mvp_music_live_players` | `false` | `clientdll` `archive` `release` | If set, MVP music is muted if players from both teams are still alive. |
| `snd_mvp_volume` | `0.160000` | `clientdll` `archive` `release` | Volume of MVP Music |
| `snd_new_visualize` | `false` | `gamedll` `cheat` | Displays soundevent name played at it's 3d position |
| `snd_occlusion_bounces` | `1` | `replicated` `cheat` |  |
| `snd_occlusion_debug` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `snd_occlusion_debug_listener_pos` | `` | `developmentonly` `cheat` |  |
| `snd_occlusion_indirect_max` | `0.700000` | `developmentonly` `cheat` |  |
| `snd_occlusion_indirect_min` | `0.010000` | `developmentonly` `cheat` |  |
| `snd_occlusion_indirect_radius` | `120.000000` | `developmentonly` `cheat` |  |
| `snd_occlusion_min_wall_thickness` | `4.000000` | `replicated` `cheat` |  |
| `snd_occlusion_override` | `-1.000000` | `developmentonly` `replicated` `cheat` |  |
| `snd_occlusion_rays` | `4` | `replicated` `cheat` |  |
| `snd_occlusion_report` | `false` | `developmentonly` `cheat` |  |
| `snd_occlusion_visualize` | `false` | `developmentonly` `cheat` |  |
| `snd_op_test_convar` | `720.000000` | `cheat` |  |
| `snd_opvar_set_point_debug` | `false` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `snd_opvar_set_point_update_interval` | `0.200000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_opvar_set_point_update_interval_fast` | `0.033300` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_rear_stereo_scale` | `1.000000` | `replicated` `cheat` |  |
| `snd_refdb` | `60.000000` | `cheat` | Reference dB at snd_refdist |
| `snd_refdist` | `36.000000` | `cheat` | Reference distance for snd_refdb |
| `snd_report_audio_nan` | `false` | `release` |  |
| `snd_report_c4_sounds` | `false` | `developmentonly` `clientdll` `cheat` |  |
| `snd_report_verbose_error` | `false` | `cheat` | If set to 1, report more error found when playing sounds.
 |
| `snd_roundaction_volume` | `0.000000` | `clientdll` `archive` `release` | Volume of Move Action Music |
| `snd_roundend_volume` | `0.160000` | `clientdll` `archive` `release` | Volume of Won/Lost Music |
| `snd_roundstart_volume` | `0.000000` | `clientdll` `archive` `release` | Volume of Round Start Music |
| `snd_showclassname` | `0` | `cheat` |  |
| `snd_showstart` | `0` | `cheat` |  |
| `snd_sos_beatpattern_show_operator_updates` | `false` | `developmentonly` `defensive` |  |
| `snd_sos_block_global_stack` | `false` | `cheat` |  |
| `snd_sos_block_stop_global_stack` | `true` | `cheat` |  |
| `snd_sos_calc_angle_debug` | `false` | `replicated` `cheat` |  |
| `snd_sos_debug_trigger_opvar` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `snd_sos_enable_nan_check` | `false` | `developmentonly` |  |
| `snd_sos_hide_simple_parameter_overwrite_warnings` | `true` | `developmentonly` `defensive` |  |
| `snd_sos_ingame_debug` | `false` | `cheat` |  |
| `snd_sos_limit_self` | `false` | `developmentonly` |  |
| `snd_sos_list_operator_updates` | `false` | `cheat` |  |
| `snd_sos_max_event_base_depth` | `4` | `developmentonly` `defensive` |  |
| `snd_sos_opvar_debug` | `false` | `cheat` |  |
| `snd_sos_pause_system` | `false` | `cheat` |  |
| `snd_sos_print_addfield_dupes` | `false` | `cheat` |  |
| `snd_sos_print_field_references` | `false` | `cheat` |  |
| `snd_sos_print_fps` | `false` | `cheat` |  |
| `snd_sos_print_frametime` | `false` | `cheat` |  |
| `snd_sos_print_full_field_info` | `false` | `cheat` |  |
| `snd_sos_print_table_arrays` | `false` | `cheat` |  |
| `snd_sos_report_entity_deleted` | `false` | `developmentonly` `defensive` |  |
| `snd_sos_show_block_debug` | `false` | `cheat` | Spew data about the list of block entries. |
| `snd_sos_show_entry_match_free` | `false` | `developmentonly` `defensive` |  |
| `snd_sos_show_mixgroup_path_errors` | `false` | `developmentonly` `defensive` |  |
| `snd_sos_show_operator_event_and_stack` | `true` | `cheat` |  |
| `snd_sos_show_operator_event_filter` | `` | `cheat` |  |
| `snd_sos_show_operator_field_filter` | `` | `cheat` |  |
| `snd_sos_show_operator_init` | `false` | `cheat` |  |
| `snd_sos_show_operator_not_executing` | `true` | `cheat` |  |
| `snd_sos_show_operator_operator_filter` | `` | `cheat` |  |
| `snd_sos_show_operator_pause_entry` | `false` | `cheat` |  |
| `snd_sos_show_operator_shutdown` | `false` | `cheat` |  |
| `snd_sos_show_operator_stop_entry` | `false` | `cheat` |  |
| `snd_sos_show_operator_updates` | `false` | `cheat` |  |
| `snd_sos_show_opfield_cache_updates` | `false` | `cheat` |  |
| `snd_sos_show_opvar_updates` | `false` | `cheat` |  |
| `snd_sos_show_opvar_updates_filter` | `` | `cheat` |  |
| `snd_sos_show_parameter_overwrite_value_comparisons` | `false` | `developmentonly` `defensive` |  |
| `snd_sos_show_parameter_overwrite_warnings` | `false` | `developmentonly` `defensive` |  |
| `snd_sos_show_queuetotrack` | `false` | `cheat` |  |
| `snd_sos_show_soundevent_overwrites` | `false` | `developmentonly` `defensive` |  |
| `snd_sos_show_soundevent_param_overwrite` | `false` | `cheat` |  |
| `snd_sos_show_soundevent_start` | `false` | `cheat` |  |
| `snd_sos_show_track_list` | `false` | `developmentonly` `defensive` |  |
| `snd_sos_show_voice_elapsed_time` | `false` | `developmentonly` `defensive` |  |
| `snd_sos_soundevent_constellation_debug` | `false` | `developmentonly` `replicated` `cheat` |  |
| `snd_sos_soundevent_constellation_replenish_max_fraction` | `0.300000` | `developmentonly` `replicated` `cheat` |  |
| `snd_sos_soundevent_deferred_interval_time` | `0.100000` | `developmentonly` `defensive` |  |
| `snd_sos_soundevent_filter` | `` | `cheat` |  |
| `snd_sos_soundevent_max_deferred_time` | `5.000000` | `developmentonly` `defensive` |  |
| `snd_sos_soundevent_show_deferral_warning` | `false` | `developmentonly` `defensive` |  |
| `snd_sos_tools_detailed_debugging` | `true` | `developmentonly` `archive` |  |
| `snd_sound_areas_debug` | `false` | `clientdll` `replicated` `cheat` |  |
| `snd_sound_areas_debug_interval` | `0.200000` | `clientdll` `replicated` `cheat` |  |
| `snd_soundmixer` | `Default_Mix` | `developmentonly` `defensive` |  |
| `snd_soundmixer_update_maximum_frame_rate` | `10` | `cheat` |  |
| `snd_soundmixer_version` | `2` | `developmentonly` `defensive` |  |
| `snd_spatialize_lerp` | `0.000000` | `archive` `release` |  |
| `snd_steamaudio_display_dimension_data_inside` | `true` | `developmentonly` `defensive` | When visualizing dimensions data at runtime, draw the inside direction. |
| `snd_steamaudio_display_dimension_data_outside` | `true` | `developmentonly` `defensive` | When visualizing dimensions data at runtime, draw the outisde direction. |
| `snd_steamaudio_display_dimension_data_size` | `true` | `developmentonly` `defensive` | When visualizing dimensions data at runtime, draw the size of the space. |
| `snd_steamaudio_dynamicpathing_max_samples` | `16` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_steamaudio_enable_reverb` | `0.000000` | `release` | Enable Steam Audio Reverb processor. |
| `snd_steamaudio_pathing_caching_threshold` | `5.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_steamaudio_pathing_enable_caching` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `snd_steamaudio_perspective_correction_front_only` | `true` | `developmentonly` | Use perspective correction for 3D audio only in the frontal directions. |
| `snd_steamaudio_reverb_level_db` | `-3.000000` | `release` | Adjust overall volume (dB) of the output from Steam Audio Reverb processor. |
| `snd_steamaudio_source_pathing_debug` | `false` | `archive` | Enable path visualization for steam_audio_source operator. |
| `snd_steamaudio_source_pathing_debug_duration` | `0.010000` | `developmentonly` `defensive` | Duration for which path remains visible. Should be close to update rate of the sound operator stack. |
| `snd_steamaudio_source_pathing_enable_validation` | `false` | `developmentonly` `defensive` | Enable real-time pathing validation against dynamic geometry. |
| `snd_surf_volume_inair` | `0.500000` | `clientdll` `archive` `release` | The volume of the wind when surfing. |
| `snd_surf_volume_map` | `0.300000` | `clientdll` `archive` `release` | The volume of ambient sounds when surfing is enabled. |
| `snd_surf_volume_slide` | `0.500000` | `clientdll` `archive` `release` | The volume of sliding along surfaces when surfing. |
| `snd_tensecondwarning_volume` | `0.040000` | `clientdll` `archive` `release` | Volume of Ten Second Warnings |
| `snd_toolvolume` | `1.000000` | `archive` | Volume of sounds in tools (e.g. Hammer, SFM) |
| `snd_use_baked_occlusion` | `0.000000` | `replicated` `cheat` `release` |  |
| `snd_vmix_override_mix_decay_time` | `-1.000000` | `cheat` | If set > 0, overrides how long the decay time is on all mix graphs (in seconds).
 |
| `snd_voipvolume` | `1.000000` | `archive` | Voice volume |
| `snd_vol_arms_race` | `1.000000` | `developmentonly` `clientdll` `archive` |  |
| `snd_vol_casual` | `1.000000` | `developmentonly` `clientdll` `archive` |  |
| `snd_vol_competitive` | `1.000000` | `developmentonly` `clientdll` `archive` |  |
| `snd_vol_deathmatch` | `1.000000` | `developmentonly` `clientdll` `archive` |  |
| `snd_vol_per_game_mode` | `true` | `developmentonly` `clientdll` `archive` |  |
| `snd_vol_spectator` | `1.000000` | `developmentonly` `clientdll` `archive` |  |
| `snd_vol_warmup` | `1.000000` | `developmentonly` `clientdll` `archive` |  |
| `sos_debug_emit` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sos_use_guid_filter` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sound_device_override` | `` | `archive` `release` | ID of the sound device to use |
| `soundevent_check_networked_entity` | `false` | `developmentonly` `gamedll` |  |
| `soundpatch_captionlength` | `2.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | How long looping soundpatch captions should display for. |
| `soundscape_debug` | `false` | `gamedll` `cheat` | When on, draws lines to all env_soundscape entities. Green lines show the active soundscape, red lines show soundscapes that aren't in range, and white lines show soundscapes that are in range, but not the active soundscape. |
| `soundscape_fadetime` | `3.000000` | `clientdll` `cheat` | Time to crossfade sound effects between soundscapes |
| `soundscape_message` | `false` | `developmentonly` `clientdll` `defensive` |  |
| `soundscape_radius_debug` | `false` | `clientdll` `cheat` | Prints current volume of radius sounds |
| `soundscape_update_include_bots` | `false` | `developmentonly` `gamedll` `cheat` | Enable to calculate soundscape audio params for bots. |
| `soundsystem_device_used` | `` | `developmentonly` `defensive` | Sound device in use (changing this does not change the soundsystem). |
| `sparseshadowtree_cascade_mask` | `4` | `developmentonly` | Bitfield describing which cascades to generate/use SST for. (OR'd 1UL<<cascadeIndex, default is 1UL<<2 only, i.e. just cascade 2) |
| `sparseshadowtree_copy_to_shadow_atlas_ps` | `true` | `developmentonly` | Copy layer from CS output to shadow atlas uses PS copy (vs CopyTexture). |
| `sparseshadowtree_cs_debug_colors` | `false` | `developmentonly` | Output debug colors for SST CS. |
| `sparseshadowtree_cs_exclude_next_cascade_region` | `true` | `developmentonly` | Exclude the inner region of a cascade during CS unpack if there is a higher resolution cascade that will cover that area. |
| `sparseshadowtree_cs_unpack_mode` | `1` | `developmentonly` | Unpack mode in cs, 0 - one leaf per thread (16 output pixels), 1 (default) - one leaf row per thread (4 output pixels), 2 - one pixel out per thread. |
| `sparseshadowtree_debug_tile_range_xmax` | `1` | `developmentonly` | SST Tile range for renderdoc/debug capturing. |
| `sparseshadowtree_debug_tile_range_xmin` | `0` | `developmentonly` | SST Tile range for renderdoc/debug capturing. |
| `sparseshadowtree_debug_tile_range_ymax` | `1` | `developmentonly` | SST Tile range for renderdoc/debug capturing. |
| `sparseshadowtree_debug_tile_range_ymin` | `0` | `developmentonly` | SST Tile range for renderdoc/debug capturing. |
| `sparseshadowtree_disable_add_layers` | `false` | `developmentonly` | Disable SST runtime layers, for debugging (will exclude geo that CAN render into SST if SST otherwise enabled) |
| `sparseshadowtree_disable_for_viewmodel` | `true` | `developmentonly` | Disable SST generation and runtime for viewmodel (use original CSM rendering). |
| `sparseshadowtree_enable_rendering` | `true` | `developmentonly` | Enable use of SST at runtime (static geo rendered into cascades via SST). |
| `sparseshadowtree_leaf_compress_scaleoffset` | `true` | `developmentonly` | Compress leaf node depths using scale & offset. |
| `sparseshadowtree_leaf_precision` | `0.000400` | `developmentonly` | precision for depth compression at SST leaf nodes. |
| `sparseshadowtree_leaf_precision_viewmodel` | `0.000500` | `developmentonly` | (viewmodel) precision for depth compression at SST leaf nodes. |
| `sparseshadowtree_parallel_generation` | `2` | `developmentonly` | Split SST tile generation into threadjobs (0 - disabled, 1 - wait on readpixels for job batch, 2 - async readpixels). |
| `sparseshadowtree_plane_incr_per_step` | `0.000100` | `developmentonly` | depth to increment candidate plane values per iteration to satisfy selection. |
| `sparseshadowtree_plane_incr_per_step_viewmodel` | `0.002500` | `developmentonly` | (viewmodel) depth to increment candidate plane values per iteration to satisfy selection. |
| `sparseshadowtree_plane_max_error` | `0.000400` | `developmentonly` | max error (distance away in depth) candidate plane is allowed before rejecting. |
| `sparseshadowtree_plane_max_error_viewmodel` | `0.010000` | `developmentonly` | (viewmodel) max error (distance away in depth) candidate plane is allowed before rejecting. |
| `sparseshadowtree_plane_num_iter` | `5` | `developmentonly` | number of steps to push candidate plane behind depths. |
| `sparseshadowtree_render_cables` | `false` | `developmentonly` | Render cables into SST. |
| `sparseshadowtree_renderdoc_capture_generation` | `false` | `developmentonly` | Capture dual shadow maps during sparseshadowtree generation. |
| `sparseshadowtree_unpack_direct_to_shadow_atlas` | `false` | `developmentonly` | unpack SST directly into shadow atlas cascade vs via staging texture PS copy (NOTE - rendersystem fix reqd for AMD + driver fix required for NV + VK only. |
| `sparseshadowtree_uv_frac_offset_x` | `0.000000` | `developmentonly` | uv x offset during copy to cascade. |
| `sparseshadowtree_uv_frac_offset_y` | `0.000000` | `developmentonly` | uv y offset during copy to cascade. |
| `speaker_config` | `-1` | `archive` |  |
| `spec_autodirector` | `true` | `clientdll` `clientcmd_can_execute` | Auto-director chooses best view modes while spectating |
| `spec_autodirector_cameraman` | `-1` | `developmentonly` `clientdll` |  |
| `spec_centerchasecam` | `false` | `clientdll` `archive` | Looks at the target player's center, instead of his eye position, in chase came mode |
| `spec_chasedistance` | `96.000000` | `developmentonly` `clientdll` `defensive` | Chase cam's ideal distance from target |
| `spec_chasedistancespeed` | `144.000000` | `developmentonly` `clientdll` `defensive` | Chase cam's ideal distance from target |
| `spec_death_panel_replay_position` | `0.750000` | `developmentonly` `clientdll` `defensive` |  |
| `spec_freeze_deathanim_time` | `0.800000` | `gamedll` `clientdll` `replicated` `release` | The time that the death cam will spend watching the player's ragdoll before going into the freeze death cam. |
| `spec_freeze_time` | `3.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Time spend frozen in observer freeze cam. |
| `spec_freeze_time_lock` | `1.000000` | `gamedll` `clientdll` `replicated` `release` | Time players are prevented from skipping the freeze cam |
| `spec_freeze_traveltime` | `0.300000` | `gamedll` `clientdll` `replicated` `release` | Time taken to zoom in to frame a target in observer freeze cam. |
| `spec_glow_decay_time` | `2.000000` | `clientdll` `release` | Time to decay glow from 1.0 to spec_glow_silent_factor after spec_glow_full_time. |
| `spec_glow_full_time` | `1.000000` | `clientdll` `release` | Noisy players stay at full brightness for this long. |
| `spec_glow_silent_factor` | `0.400000` | `clientdll` `release` | Lurking player xray glow scaling. |
| `spec_glow_spike_factor` | `1.200000` | `clientdll` `release` | Noisy player xray glow scaling (pop when noise is made).  Make >1 to add a 'spike' to noise-making players |
| `spec_glow_spike_time` | `0.000000` | `clientdll` `release` | Time for noisy player glow 'spike' to show that they made noise very recently. |
| `spec_lock_to_accountid` | `0` | `developmentonly` `clientdll` | As an observer, lock the spectator target to the given accountid. |
| `spec_replay_autostart` | `true` | `clientdll` `archive` | Auto-start Killer Replay when available |
| `spec_replay_bot` | `false` | `gamedll` `release` | Enable Spectator Hltv Replay when killed by bot |
| `spec_replay_cache_ragdolls` | `true` | `developmentonly` `clientdll` `defensive` | when set to 0, ragdolls will settle dynamically before and after Killer Replay |
| `spec_replay_colorcorrection` | `0.500000` | `developmentonly` `clientdll` `defensive` | Amount of color correction in deathcam replay |
| `spec_replay_enable` | `0` | `reference` |  |
| `spec_replay_fadein` | `0.750000` | `developmentonly` `clientdll` `defensive` | Amount of time in seconds it takes to visually fade into replay, or into real-time after replay |
| `spec_replay_fadeout` | `0.750000` | `developmentonly` `clientdll` `defensive` | Amount of time in seconds it takes to visually fade out of replay, or out of real-time before replay |
| `spec_replay_leadup_time` | `0.000000` | `reference` |  |
| `spec_replay_others_experimental` | `false` | `developmentonly` `clientdll` `defensive` | Replay the last death of the round, if possible. Disabled on official servers by default. Experimental. |
| `spec_replay_outline` | `1` | `developmentonly` `clientdll` `defensive` | Enable outline selecting victim in hltv replay: 0 - none; 1 - ouline YOU; 2 - outline YOU, with red ragdoll outline; 3 - normal spectator outlines |
| `spec_replay_rate_slowdown` | `1.000000` | `developmentonly` `clientdll` `defensive` | The part of Killer Replay right before death is played at this rate |
| `spec_replay_rate_slowdown_length` | `0.500000` | `developmentonly` `clientdll` `defensive` | The part of Killer Replay right before death is played at this rate |
| `spec_replay_review_sound` | `true` | `developmentonly` `clientdll` `defensive` | When set to non-0, a sound effect is played during Killer Replay |
| `spec_replay_round_delay` | `0.000000` | `gamedll` `release` | Round can be delayed by this much due to someone watching a replay; must be at least 3-4 seconds, otherwise the last replay will always be interrupted by round start, assuming normal pause between round_end and round_start events (7 seconds) and freezecam delay (2 seconds) and 7.4 second full replay (5.4 second pre-death and ~2 seconds post-death) and replay in/out switching (up to a second) |
| `spec_replay_sound_fadein` | `0.050000` | `developmentonly` `clientdll` `defensive` | Amount of time in seconds it takes to fade in the audio before or after replay |
| `spec_replay_sound_fadeout` | `0.000000` | `developmentonly` `clientdll` `defensive` | Amount of time in seconds it takes to fade out the audio before or after replay |
| `spec_replay_victim_pov` | `false` | `developmentonly` `clientdll` `defensive` | Killer Replay - replay from victim's point of view (1); the default is killer's (0). Experimental. |
| `spec_replay_winddown_time` | `2.000000` | `gamedll` `release` | The trailing time, in seconds, of replay past the event, including fade-out |
| `spec_show_xray` | `1` | `clientdll` `archive` `release` | If set to 1, you can see player outlines and name IDs through walls - who you can see depends on your team and mode |
| `spec_track` | `0` | `developmentonly` `clientdll` `defensive` | Tracks an entity in spec mode |
| `spec_usenumberkeys_nobinds` | `true` | `clientdll` `archive` | If set to 1, map voting and spectator view use the raw number keys instead of the weapon binds (slot1, slot2, etc). |
| `ss_mimic` | `0` | `developmentonly` `clientdll` `cheat` | Split screen users mimic base player's CUserCmds |
| `stats_display` | `0` | `reference` |  |
| `stats_highlight_interval` | `10.000000` | `developmentonly` `clientdll` `defensive` | Interval between hightlight screens in the transition stats panel |
| `steam_controller_haptics` | `true` | `clientdll` `release` |  |
| `steamworks_sessionid_client` | `0` | `clientdll` `hidden` `userinfo` | The client session ID for the new steamworks gamestats. |
| `steamworks_sessionid_server` | `0` | `developmentonly` `gamedll` `clientdll` `hidden` `replicated` `defensive` | The server session ID for the new steamworks gamestats. |
| `sticky_tooltips` | `false` | `developmentonly` `clientdll` `hidden` `defensive` | Don't ever hide tooltips. Helpful when debugging complicated tooltip layouts. |
| `surf_speed_fast` | `3000.000000` | `gamedll` `clientdll` `replicated` `release` | Speed above which a player is considered to be going fast. |
| `surf_speed_med` | `2000.000000` | `gamedll` `clientdll` `replicated` `release` | Speed above which a player is considered to be going medium. |
| `surf_speed_slow` | `50.000000` | `gamedll` `clientdll` `replicated` `release` | Speed above which a player is considered to be going slow. |
| `suspicious_hit_odds_threshold` | `0.010000` | `gamedll` `release` |  |
| `suspicious_hit_player_radius` | `8.000000` | `gamedll` `release` |  |
| `suspicious_hit_strategy` | `0` | `gamedll` `release` | What to do about suspicious hits. 0: Nothing. 1: Skip the bullet. 2: Skip the bullet and re-roll a new bullet. |
| `sv_accelerate` | `5.500000` | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_accelerate_debug_speed` | `false` | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_accelerate_use_weapon_speed` | `true` | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_ag2_record_entity_graph` | `` | `developmentonly` `gamedll` | Automatically start AG2 recording when an entity with this name (wildcard) or id is created. |
| `sv_air_max_wishspeed` | `30.000000` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_airaccelerate` | `12.000000` | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_allchat` | `true` | `gamedll` `notify` `release` | Players can receive all other players' text chat, no death restrictions |
| `sv_allow_annotations_access_level` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | 0:off \| 1: view-only \| 2: edit. |
| `sv_allow_ground_weapon_pickup` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_allow_switching_weapon_handedness` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_allow_votes` | `true` | `gamedll` `release` `commandline_enforced` | Allow voting? |
| `sv_alltalk` | `false` | `gamedll` `notify` `release` `commandline_enforced` | Players can hear all other players' voice communication, no team restrictions |
| `sv_annotation_limits_max_rounds_per_half` | `5` | `gamedll` `clientdll` `replicated` `release` | Hard limit on maximum number of rounds (per half) that annotations can be seen in a live match |
| `sv_auto_adjust_bot_difficulty` | `true` | `gamedll` `release` `commandline_enforced` | Adjust the difficulty of bots each round based on contribution score. |
| `sv_auto_cstrafe_attempt_window` | `1` | `gamedll` `release` | The length of the window of trailing counter-strafe attempts considered during input automation detection. |
| `sv_auto_cstrafe_kick` | `false` | `gamedll` `release` | Whether or not to kick players when counter-strafe input automation is detected. |
| `sv_auto_cstrafe_logging` | `0` | `gamedll` `release` | 0: never, 1: every time counter-strafe input automation is detected, 2: every counter-strafe |
| `sv_auto_cstrafe_lower_overlap_pct_threshold` | `0.000000` | `gamedll` `release` | The percentage of overlapping attempts in the attempt window below which input automation detection is triggered at the success threshold. |
| `sv_auto_cstrafe_min_attempts` | `1` | `gamedll` `release` | The minimum number of counter-strafe attempts required for input automation detection. The player must be moving more than 135.2 units/s for their counter-strafe to be considered an attempt. An attempt is either considered a success (counter-strafing took place within a single tick), an overlap (both directions were held for 1+ ticks) or an underlap (neither direction was held for 1+ ticks). |
| `sv_auto_cstrafe_sequence_length` | `1` | `gamedll` `release` | The length of sequential counter-strafe attempts evaluated relative to the success threshold. Input automation detection considers the best sequence within the larger attempt window. |
| `sv_auto_cstrafe_success_threshold` | `1` | `gamedll` `release` | The minimum number of successful counter-strafes within a best sequence that will trigger input automation detection. The number of successes that trigger input automation detection is interpolated between the success threshold and a 'perfect' sequence (all counter-strafes in a sequence are successes), depending on the player's percentage of overlapping counter-strafe attempts. |
| `sv_auto_cstrafe_upper_overlap_pct_threshold` | `0.000000` | `gamedll` `release` | The percentage of overlapping attempts in the attempt window below which input automation detection is triggered when all counter-strafes in a sequence are successes. |
| `sv_auto_full_alltalk_during_warmup_half_end` | `true` | `gamedll` `release` `commandline_enforced` | When enabled will automatically turn on full all talk mode in warmup, at halftime and at the end of the match |
| `sv_autobunnyhopping` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Players automatically re-jump while holding jump button |
| `sv_autobuyammo` | `false` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | Enable automatic ammo purchase when inside buy zones during buy periods |
| `sv_autoexec_mapname_cfg` | `false` | `gamedll` `release` | Execute a mapname cfg file on the server automatically in custom game modes that require it. |
| `sv_autosave` | `true` | `developmentonly` `gamedll` `replicated` `defensive` | Set to 1 to autosave game on level transition. Does not affect autosave triggers. |
| `sv_backspeed` | `0.600000` | `developmentonly` `gamedll` `clientdll` `replicated` | How much to slow down backwards motion |
| `sv_bhop_time_window` | `0.007812` | `gamedll` `clientdll` `replicated` `release` | sv_legacy_jump disabled only: The time window (in seconds) around landing where a jump press is considered a bhop attempt. |
| `sv_bot_buy_decoy_weight` | `1.000000` | `gamedll` `release` | Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars. |
| `sv_bot_buy_flash_weight` | `1.000000` | `gamedll` `release` | Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars. |
| `sv_bot_buy_grenade_chance` | `33.000000` | `gamedll` `release` `commandline_enforced` | Chance bots will buy a grenade with leftover money (after prim, sec and armor). Input as percent (0-100.0) |
| `sv_bot_buy_hegrenade_weight` | `6.000000` | `gamedll` `release` | Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars. |
| `sv_bot_buy_molotov_weight` | `1.000000` | `gamedll` `release` | Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars. |
| `sv_bot_buy_smoke_weight` | `1.000000` | `gamedll` `release` | Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars. |
| `sv_bot_difficulty_kbm` | `0.000000` | `developmentonly` `gamedll` `clientdll` `hidden` `replicated` `defensive` | Bot difficulty while playing with Keyboard/Mouse device |
| `sv_bot_parallel_threat_detection` | `true` | `developmentonly` `gamedll` `defensive` | Perform bot threat detection in parallel |
| `sv_bots_get_easier_each_win` | `0` | `gamedll` `release` `commandline_enforced` | If > 0, some # of bots will lower thier difficulty each time they win. The argument defines how many will lower their difficulty each time. |
| `sv_bounce` | `0.000000` | `gamedll` `clientdll` `notify` `replicated` `release` | Bounce multiplier for when physically simulated objects collide with other objects. |
| `sv_buy_status_override` | `-1` | `gamedll` `replicated` `release` `commandline_enforced` | Override for buy status map info. 0 = everyone can buy, 1 = ct only, 2 = t only 3 = nobody |
| `sv_buymenu_open_prevents_opportunistic_pickup` | `false` | `gamedll` `release` |  |
| `sv_c4_upright_constraint_damping` | `0.500000` | `developmentonly` `gamedll` `defensive` | Controls how much velocity is damped on the constraint. 0 = undamped wobbly spring, 1 = critically damped no wobble fast converge, >1 = over damped |
| `sv_c4_upright_constraint_enabled` | `true` | `developmentonly` `gamedll` `defensive` | Use a constraint to keep C4 pointed upright when thrown |
| `sv_c4_upright_constraint_strength` | `0.600000` | `developmentonly` `gamedll` `defensive` | How quickly the constraint converges |
| `sv_chat_proximity` | `-1.000000` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_cheats` | `false` | `reference` |  |
| `sv_client_max_interp_ratio` | `5.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | This can be used to limit the value of cl_interp_ratio for connected clients (only while they are connected). |
| `sv_client_min_interp_ratio` | `0.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | This can be used to limit the value of cl_interp_ratio for connected clients (only while they are connected).
 |
| `sv_clip_penetration_traces_to_players` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sv_clockcorrection_msecs` | `30.000000` | `gamedll` `release` | The server tries to keep each player's m_nTickBase withing this many msecs of the server absolute tickcount |
| `sv_cloth_interp_rot` | `false` | `developmentonly` `gamedll` |  |
| `sv_coaching_enabled` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `release` | Allows spectating and communicating with a team ( 'coach t' or 'coach ct' ) |
| `sv_competitive_minspec` | `true` | `gamedll` `clientdll` `notify` `replicated` `release` | Enable to force certain client convars to minimum/maximum values to help prevent competitive advantages. |
| `sv_compute_per_bot_difficulty` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` | 0 = compute all bot difficulties equally, 1 = compute unique bot difficulty for each bot  |
| `sv_condense_late_buttons` | `true` | `developmentonly` `gamedll` `defensive` | When condensing late commands. Should we compress multiple moves of button presses into the target move? |
| `sv_cq_delta_encode_svc_usercmds` | `true` | `developmentonly` `gamedll` | Delta encode svc_UserCmds message |
| `sv_cq_min_queue` | `0` | `reference` |  |
| `sv_cq_trim_bloat_remainder` | `1` | `gamedll` `release` | When trimming a bloated CQ, leave at least N more commands than the minimum |
| `sv_cq_trim_bloat_space` | `0` | `gamedll` `release` | When trimming a bloated CQ, try to leave room for N more commands to be added.  0 will trim only what is needed to remove the immediate bloat, a very large value will reset the whole queue. |
| `sv_cq_trim_catchup_remainder` | `1` | `gamedll` `release` | When trimming an overful CQ due to app 'catchup' request, leave at least N more commands than the minimum |
| `sv_cq_validate_encoded_svc_usercmds` | `false` | `developmentonly` `gamedll` | VERY EXPENSIVE: serialize non-delta-encoded commands along with delta-encoded for validation |
| `sv_cs_player_speed_has_hostage` | `200.000000` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_csgo_gpu_culling_skybox` | `false` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_csgo_shoot_assert_lagcompensation_error` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_force_full_interp` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_force_use_target_time` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_lagcompensation_max_error` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | Warn if lag compensated head hitbox position doesn't match that on client. |
| `sv_csgo_shoot_log` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_log_attack_cmds_only` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_use_full_interp` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_verify` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_csgo_shoot_verify_on_attack_only` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` | Only run lag compensation error check when primary attack goes down. |
| `sv_damage_prediction_allowed` | `true` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_deadtalk` | `false` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | Dead players can speak (voice, text) to the living |
| `sv_debug_client_not_in_pvs` | `false` | `gamedll` `cheat` | If set, draw failed client PVS checks with red box |
| `sv_debug_player_use` | `0` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Visualizes +use logic. Green cross=trace success, Red cross=trace too far, Green box=radius success |
| `sv_debugroundstats` | `false` | `developmentonly` `gamedll` |  |
| `sv_dev_damage_use_netvars` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` | Whether we should use network vars (true) or legacy messages (false). |
| `sv_disable_immunity_alpha` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If set, clients won't slam the player model render settings each frame for immunity [mod authors use this] |
| `sv_disable_networkable_loadouts` | `false` | `developmentonly` `gamedll` `clientdll` `hidden` `replicated` `defensive` |  |
| `sv_disable_observer_interpolation` | `false` | `gamedll` `clientdll` `replicated` `release` | Disallow interpolating between observer targets on this server. |
| `sv_disable_querycache` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | debug - disable trace query cache |
| `sv_disable_radar` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | 0: regular radar; 1: always disabled; 2: disabled in warmup |
| `sv_disable_teamselect_menu` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Disable teamselect menu on clients |
| `sv_disconnected_player_data_hold_time` | `60` | `gamedll` `clientdll` `replicated` `release` | Duration, in seconds, to hold onto the data of disconnected players, for scoreboard display. |
| `sv_disconnected_players_cleanup_delay` | `0` | `gamedll` `release` `commandline_enforced` | Delay between player disconnecting and their corpse getting cleaned up. |
| `sv_early_network_message_processing` | `false` | `developmentonly` `gamedll` | Processes network messages on the server before entities think, instead of at the end of the tick. |
| `sv_enablebunnyhopping` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Allow jump speed to exceed 1.1x max speed |
| `sv_endmatch_item_drop_interval` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | The time between drops on the end match scoreboard  |
| `sv_endmatch_item_drop_interval_ancient` | `3.500000` | `developmentonly` `gamedll` `clientdll` `replicated` | The time between drops on the end match scoreboard for ancient items  |
| `sv_endmatch_item_drop_interval_legendary` | `2.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | The time between drops on the end match scoreboard for legendary items  |
| `sv_endmatch_item_drop_interval_mythical` | `1.250000` | `developmentonly` `gamedll` `clientdll` `replicated` | The time between drops on the end match scoreboard for mythical items  |
| `sv_endmatch_item_drop_interval_rare` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | The time between drops on the end match scoreboard for rare items  |
| `sv_ent_showonlyhitbox` | `-1` | `gamedll` `cheat` |  |
| `sv_extract_ammo_from_dropped_weapons` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_extreme_strafe_accuracy_fishtail` | `0.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | Number of degrees of aim 'fishtail' when making an extreme strafe direction change |
| `sv_fade_player_visibility_farz` | `false` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_falldamage_scale` | `1.000000` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_falldamage_to_below_player_multiplier` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scale damage when distributed across two players |
| `sv_falldamage_to_below_player_ratio` | `0.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Landing on a another player's head gives them this ratio of the damage. |
| `sv_flashed_amount_for_blind_kill` | `0.700000` | `gamedll` `release` | Minimum flashed alpha value for a player to be awarded a blind kill on the kill feed. |
| `sv_footsteps` | `1.000000` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` | Play footstep sound for players |
| `sv_force_team_intro_random` | `0` | `developmentonly` `gamedll` |  |
| `sv_force_team_intro_variant` | `0` | `developmentonly` `gamedll` |  |
| `sv_force_transmit_ents` | `false` | `developmentonly` `gamedll` | Will transmit all entities to client, regardless of PVS conditions (will still skip based on transmit flags, however). |
| `sv_freeze_camera_angles` | `0.000000 0.000000 0.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_freeze_camera_enabled` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_freeze_camera_min_remaining` | `3` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_freeze_camera_position` | `0.000000 0.000000 0.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_friction` | `5.200000` | `gamedll` `clientdll` `notify` `replicated` `release` | World friction. |
| `sv_full_alltalk` | `false` | `gamedll` `clientdll` `replicated` `release` | Any player (including Spectator team) can speak to any other player |
| `sv_game_mode_flags` | `0` | `gamedll` `release` | Dedicated server game mode flags to run |
| `sv_gameinstructor_disable` | `false` | `gamedll` `clientdll` `replicated` `release` | Force all clients to disable their game instructors. |
| `sv_gameinstructor_enable` | `false` | `clientdll` `replicated` `release` | Force all clients to enable their game instructors. |
| `sv_give_item` | `` | `gamedll` `hidden` `replicated` `cheat` `release` `commandline_enforced` | Player's extra item to give |
| `sv_gravity` | `800.000000` | `gamedll` `clientdll` `notify` `replicated` `release` | World gravity. |
| `sv_grenade_collision_sphere` | `false` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_grenade_collision_sphere_radius` | `2.000000` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_grenade_trajectory_prac_pipreview` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Shows grenade trajectory practice picture-in-picture preview. |
| `sv_grenade_trajectory_prac_trailtime` | `0.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Shows grenade trajectory practice visualization for this number of seconds. |
| `sv_grenade_trajectory_time_spectator` | `0.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Length of time grenade trajectory remains visible as a spectator. |
| `sv_guardian_extra_equipment_ct` | `` | `gamedll` `release` `commandline_enforced` | Extra starting equipment for CT players in guardian modes |
| `sv_guardian_extra_equipment_t` | `` | `gamedll` `release` `commandline_enforced` | Extra starting equipment for Terrorist players in guardian modes |
| `sv_guardian_refresh_ammo_for_items_on_waves` | `` | `gamedll` `release` `commandline_enforced` | List of additional weapons to refill ammo on waves. |
| `sv_guardian_spawn_health_ct` | `100` | `gamedll` `release` `commandline_enforced` | Starting health in guardian modes. |
| `sv_guardian_spawn_health_t` | `100` | `gamedll` `release` `commandline_enforced` | Starting health in guardian modes. |
| `sv_health_approach_enabled` | `true` | `gamedll` `replicated` `release` `commandline_enforced` |  |
| `sv_health_approach_speed` | `10.000000` | `gamedll` `replicated` `release` `commandline_enforced` |  |
| `sv_hegrenade_damage_multiplier` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_hegrenade_radius_multiplier` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_hide_ent_in_pvs` | `-1` | `developmentonly` `gamedll` |  |
| `sv_hide_roundtime_until_seconds` | `0` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_highlight_distance` | `500.000000` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_highlight_duration` | `3.500000` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_hitbox_debug` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `sv_human_autojoin_team` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Force human players on to a team. 0 to disable. |
| `sv_ignoregrenaderadio` | `false` | `gamedll` `release` `commandline_enforced` | Turn off Fire in the hole messages |
| `sv_infinite_ammo` | `0` | `gamedll` `clientdll` `replicated` `cheat` `release` `commandline_enforced` | Player's active weapon will never run out of ammo |
| `sv_invites_only_mainmenu` | `false` | `gamedll` `clientdll` `replicated` `release` | If turned on, will ignore all invites when user is playing a match |
| `sv_jump_impulse` | `301.993378` | `gamedll` `clientdll` `replicated` `release` | Initial upward velocity for player jumps; sqrt(2*gravity*height). |
| `sv_jump_precision_enable` | `true` | `gamedll` `clientdll` `replicated` `release` | Enable jump precision. Some game modes benefit from being able to turn this off. |
| `sv_jump_spam_penalty_time` | `0.015625` | `gamedll` `clientdll` `replicated` `release` | For subtick jumps, if this much time or less has elapsed since the last time the user has pressed the jump key, pretend they hadn't. Lowering this makes bunnyhopping easier. |
| `sv_kick_ban_duration` | `15.000000` | `gamedll` `clientdll` `notify` `replicated` `release` | How long should a kick ban from the server should last (in minutes) |
| `sv_kick_players_with_cooldown` | `1` | `gamedll` `replicated` `release` | (0: do not kick on insecure servers; 1: kick players with Untrusted status or convicted by Overwatch; 2: kick players with any cooldown) |
| `sv_kill_players_at_coord_min` | `true` | `gamedll` `release` | Kill players with fall damage at negative coord min |
| `sv_ladder_angle` | `-0.707000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Cos of angle of incidence to ladder perpendicular for applying ladder_dampen |
| `sv_ladder_dampen` | `0.200000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Amount to dampen perpendicular movement on a ladder |
| `sv_ladder_scale_speed` | `0.780000` | `gamedll` `clientdll` `replicated` `release` | Scale top speed on ladders |
| `sv_ladder_slack_z_mult` | `0.026000` | `gamedll` `clientdll` `replicated` `cheat` | Difference in Z increases toward the middle of the slack ladder.
 |
| `sv_lagcomp_filterbyviewangle` | `true` | `gamedll` `cheat` | If true, player pawn will filter lag compensation targets by their view angle. |
| `sv_lagcompensationforcerestore` | `true` | `gamedll` `cheat` | Don't test validity of a lag comp restore, just do it. |
| `sv_late_commands_allowed` | `5` | `gamedll` `release` | Allow N late commands to run at 0 timescale prior to running an on-time command. Negative values for network round trip based calculation with a hard cap of the of absolute value |
| `sv_legacy_jump` | `false` | `gamedll` `clientdll` `replicated` `release` | Whether or not to use the pre-2026 jump code. |
| `sv_lightquery_debug` | `false` | `gamedll` `cheat` |  |
| `sv_limit_buyrandom_per_life` | `true` | `gamedll` `release` | Enable to limit buyrandom command to only run once per player life |
| `sv_log_http_record_before_any_listeners` | `false` | `gamedll` `release` |  |
| `sv_log_roundstats` | `true` | `gamedll` `release` |  |
| `sv_mapvetopickvote_maps` | `de_cache,de_anubis,de_inferno,de_mirage,de_dust2,de_nuke,de_ancient` | `gamedll` `release` | Which maps are used for map veto pick sequence |
| `sv_mapvetopickvote_phase_duration` | `[1:5][2:15][3:20][4:10][5:10][6:5]` | `gamedll` `release` | How many seconds each phase lasts |
| `sv_mapvetopickvote_rnd` | `false` | `gamedll` `release` | When enabled will shuffle veto pick maps list order every time |
| `sv_massreport` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `sv_matchend_drops_enabled` | `true` | `gamedll` `release` | Rewards gameplay time is always accumulated for players, but drops at the end of the match can be prevented |
| `sv_matchpause_auto_5v5` | `false` | `gamedll` `clientdll` `replicated` `release` | When enabled will automatically pause the match at next freeze time if less than 5 players are connected on each team. |
| `sv_matchperfstats_maxclientperfsamples` | `100` | `developmentonly` `gamedll` `defensive` | Don't retain more than N perf samples for any given client |
| `sv_max_deathmatch_respawns_per_tick` | `0` | `gamedll` `release` `commandline_enforced` |  |
| `sv_max_distance_transmit_footsteps` | `1250.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Maximum distance to transmit footstep sound effects. |
| `sv_maxspeed` | `320.000000` | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_maxunlag` | `1.000000` | `gamedll` `clientdll` `replicated` `release` | Maximum lag compensation in seconds |
| `sv_maxunlag_player` | `-1.000000` | `gamedll` `release` | If >0, maximumum lag compensation used for other human pawns. Applied after sv_maxunlag! |
| `sv_maxuptimelimit` | `0.000000` | `gamedll` `release` | Number of hours to operate before trying sv_shutdown. |
| `sv_maxvelocity` | `3500.000000` | `gamedll` `clientdll` `replicated` `release` | Maximum speed any ballistically moving object is allowed to attain per axis. |
| `sv_min_jump_landing_sound` | `260.000000` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_minimum_desired_chicken_count` | `0` | `gamedll` `replicated` `release` | Minimum number of chickens to attempt to spawn in the map |
| `sv_mover_maxslope` | `0.700000` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `defensive` | The maximum slope the player can overcome [-] |
| `sv_mover_pogodampingratio` | `1.000000` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `defensive` | The capsule pogo stick damping ratio [-] |
| `sv_mover_pogofrequency` | `10.000000` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` `defensive` | The capsule pogo stick frequency [hz]. |
| `sv_mute_players_with_social_penalties` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `sv_networkvar_log_fullchanges` | `false` | `developmentonly` `gamedll` | Log FUL_FULL_EDICT_CHANGED calls. |
| `sv_no_navmesh` | `false` | `developmentonly` `gamedll` `cheat` | Block loading of the navmesh. Unplayable, only used for memory sampling. |
| `sv_noclipaccelerate` | `5.000000` | `gamedll` `clientdll` `archive` `notify` `replicated` |  |
| `sv_noclipduringpause` | `false` | `gamedll` `clientdll` `replicated` `cheat` | If cheats are enabled, then you can noclip with the game paused (for doing screenshots, etc.). |
| `sv_noclipfriction` | `4.000000` | `gamedll` `clientdll` `archive` `notify` `replicated` | Friction during noclip move. |
| `sv_noclipspeed` | `1200.000000` | `gamedll` `clientdll` `archive` `notify` `replicated` |  |
| `sv_noclipspeedscaleonshift` | `0.500000` | `gamedll` `clientdll` `archive` `notify` `replicated` |  |
| `sv_nomvp` | `false` | `developmentonly` `gamedll` `defensive` | Disable MVP awards. |
| `sv_nonemesis` | `true` | `developmentonly` `gamedll` `defensive` | Disable nemesis and revenge. |
| `sv_nowinpanel` | `false` | `developmentonly` `gamedll` `defensive` | Turn on/off win panel on server |
| `sv_optimizedmovement` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `sv_outofammo_indicator` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` |  |
| `sv_override_max_health` | `0` | `gamedll` `release` |  |
| `sv_parallel_checktransmit` | `0` | `gamedll` `release` | Set to 1 to use threaded checkentities for transmit/pvs on listen servers, 2 for dedicated servers. |
| `sv_party_mode` | `false` | `gamedll` `clientdll` `replicated` `release` | Party!! |
| `sv_pause_on_tick` | `0` | `developmentonly` `gamedll` `replicated` `cheat` | Tick count to pause on |
| `sv_phys_animated_hierarchy` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `sv_phys_async_buoyancy_update` | `false` | `developmentonly` `gamedll` `replicated` `defensive` | If true, server buoyancy motion controllers are updated in an async job after the tick has completed. |
| `sv_phys_debug_callback_entities` | `false` | `gamedll` `cheat` | Print all entities that get touch callbacks. Each entity is printed only once. |
| `sv_phys_enabled` | `true` | `gamedll` `cheat` | Enable all physics simulation |
| `sv_phys_sleep_enable` | `true` | `gamedll` `cheat` | Enable sleeping for dynamic physics bodies. |
| `sv_phys_sound_disable_impact_sounds_under_hard_threshold` | `false` | `gamedll` `cheat` | if true, impact sounds wont play if no soft impact sound is present and the impact is below the hard velocity threshold. |
| `sv_phys_stop_at_collision` | `` | `gamedll` `cheat` |  |
| `sv_phys_visualize_awake` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `sv_player_search_range` | `64.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sv_playerradio_use_allowlist` | `true` | `gamedll` `release` | playerradio commands may only use responses from an allow list of commands. |
| `sv_predictable_damage_tag_ticks` | `2` | `gamedll` `release` | Delay player slowdown when damaged by # ticks to reduce misprediction effects |
| `sv_prime_accounts_only` | `false` | `gamedll` `release` | When this setting is enabled only prime users can connect to this game server. |
| `sv_pushaway_clientside` | `0` | `developmentonly` `gamedll` `clientdll` `replicated` | Clientside physics push away (0=off, 1=only localplayer, 1=all players) |
| `sv_pushaway_clientside_size` | `15.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | Minimum size of pushback objects |
| `sv_pushaway_force` | `300000.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | How hard physics objects are pushed away from the players on the server. |
| `sv_pushaway_hostage_force` | `20000.000000` | `gamedll` `replicated` `cheat` | How hard the hostage is pushed away from physics objects (falls off with inverse square of distance). |
| `sv_pushaway_max_force` | `2000.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | Maximum amount of force applied to physics objects by players. |
| `sv_pushaway_max_hostage_force` | `1000.000000` | `gamedll` `replicated` `cheat` | Maximum of how hard the hostage is pushed away from physics objects. |
| `sv_pushaway_max_player_force` | `20.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Maximum of how hard the player is pushed away from physics objects. |
| `sv_pushaway_min_player_speed` | `75.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | If a player is moving slower than this, don't push away physics objects (enables ducking behind things). |
| `sv_pushaway_player_force` | `450.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | How hard the player is pushed away from physics objects (falls off with inverse square of distance). |
| `sv_pvs_cache_query_inflate_amount` | `0` | `developmentonly` `gamedll` |  |
| `sv_pvs_entity` | `-1` | `developmentonly` `gamedll` `defensive` | If set, only allows this ent index to network (other than players and things that force sending). |
| `sv_pvs_max_distance` | `0.000000` | `reference` |  |
| `sv_pvs_random` | `false` | `developmentonly` `gamedll` `defensive` | If set, objects blink in/out of pvs randomly. |
| `sv_pvs_shadows_include_env` | `false` | `gamedll` `replicated` `release` |  |
| `sv_quantize_movement_input` | `true` | `gamedll` `clientdll` `replicated` `release` | Quantize movement input values. Enabling this restricts players from using analog input to move at fractional speeds normally impossible with digital button input. |
| `sv_radio_throttle_window` | `10.000000` | `gamedll` `release` | The number of seconds before radio command tokens refresh. |
| `sv_ragdoll_lru_debug` | `false` | `gamedll` `replicated` `cheat` |  |
| `sv_record_item_time_data` | `false` | `gamedll` `release` | Turn on recording of per player item time data into the server log. |
| `sv_regeneration_force_on` | `false` | `gamedll` `cheat` | Cheat to test regenerative health systems |
| `sv_regeneration_wait_time` | `1.000000` | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `sv_reliableavatardata` | `false` | `gamedll` `clientdll` `replicated` `release` | Use server overrides for steam avatars |
| `sv_remapper_loopsoundfix` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sv_remapper_range_multiplier` | `1.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sv_remove_ent_from_pvs` | `0` | `developmentonly` `gamedll` |  |
| `sv_rollangle` | `0.000000` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` | Max view roll angle |
| `sv_rollspeed` | `200.000000` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` |  |
| `sv_runcmds` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `sv_script_think_interval` | `0.100000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `sv_sellback_enabled` | `true` | `gamedll` `clientdll` `replicated` `release` | Determines whether players can undo purchases in the buy menu |
| `sv_sequence_debug` | `-1` | `developmentonly` `gamedll` `defensive` |  |
| `sv_sequence_debug2` | `-1` | `developmentonly` `gamedll` `defensive` |  |
| `sv_sequence_model_substring` | `` | `developmentonly` `gamedll` `defensive` |  |
| `sv_server_graphic1` | `` | `gamedll` `clientdll` `replicated` `release` | A 360x60 (<16kb) image file in /csgo/ that will be displayed to spectators. |
| `sv_server_graphic2` | `` | `gamedll` `clientdll` `replicated` `release` | A 220x45 (<16kb) image file in /csgo/ that will be displayed to spectators. |
| `sv_server_verify_blood_on_player` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `sv_shared_team_pvs` | `false` | `developmentonly` `gamedll` `defensive` | PVS is shared between teams |
| `sv_show_bot_difficulty_in_name` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | 0 = hide bot difficulty in bot name, 1 = show bot difficulty in bot name |
| `sv_show_move_collisions` | `false` | `gamedll` `clientdll` `replicated` `cheat` | Enable this to visualize collisions between player and geometry. |
| `sv_show_team_equipment_force_on` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Force on if not prohibited |
| `sv_show_team_equipment_prohibit` | `false` | `gamedll` `clientdll` `notify` `replicated` `release` | Determines whether +cl_show_team_equipment is prohibited. |
| `sv_show_teammate_death_notification` | `false` | `gamedll` `release` | Show chat notification upon teammate death |
| `sv_show_voip_indicator_for_enemies` | `false` | `gamedll` `replicated` `release` | Makes it so the voip icon is shown over enemies as well as allies when they are talking |
| `sv_showbullethits` | `0` | `gamedll` `clientdll` `replicated` `release` | 1=show hits and near misses, 2=show hits only |
| `sv_showhitregistration` | `0` | `gamedll` `clientdll` `replicated` `cheat` | Display lag_compensated hitboxes. 0 = off, 1 = server only, 2 = client only, 3 = both server and client |
| `sv_showimpacts` | `0` | `gamedll` `clientdll` `replicated` `release` | Shows client (red) and server (blue) bullet impact point (1=both, 2=client-only, 3=server-only) |
| `sv_showimpacts_penetration` | `0` | `gamedll` `clientdll` `replicated` `release` | Shows extra data when bullets penetrate. (use sv_showimpacts_time to increase time shown) |
| `sv_showimpacts_time` | `4.000000` | `gamedll` `clientdll` `replicated` `release` | Duration bullet impact indicators remain before disappearing |
| `sv_showladders` | `false` | `developmentonly` `gamedll` `defensive` | Show bbox and dismount points for all ladders (must be set before level load.)
 |
| `sv_showlagcompensation_rec` | `0.000000` | `developmentonly` `gamedll` | If > 0, show lag compensation hitboxes as they're recorded. Value is for how long. |
| `sv_showplayerhitboxes` | `0` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Show lag compensated hitboxes for the specified player index whenever a player fires. |
| `sv_skel_constraints_enable` | `false` | `replicated` `cheat` |  |
| `sv_skip_update_animations` | `false` | `developmentonly` `gamedll` | Enable to skip game animations |
| `sv_skirmish_id` | `0` | `gamedll` `clientdll` `replicated` `release` | Dedicated server skirmish id to run |
| `sv_skyname` | `sky_urb01` | `gamedll` `clientdll` `archive` `replicated` | Current name of the skybox texture |
| `sv_smoke_volume_blind_start` | `0.200000` | `developmentonly` `clientdll` |  |
| `sv_sniper_tracer_innacuracy` | `0.085000` | `developmentonly` `gamedll` `clientdll` `replicated` | How inaccurate a sniper shot can be before we trip sv_sniper_tracer_mode behavior. |
| `sv_sniper_tracer_innacuracy_length` | `200.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | How far should the tracer draw if we trip sv_sniper_tracer_mode behavior. |
| `sv_sniper_tracer_mode` | `1` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Mode for sniper tracers. 0: legacy, 1: hide when more than sv_sniper_tracer_innacuracy inaccurate. |
| `sv_spawn_afk_bomb_drop_time` | `15.000000` | `gamedll` `replicated` `release` | Players that have never moved since they spawned will drop the bomb after this amount of time. |
| `sv_spec_hear` | `3` | `gamedll` `clientdll` `notify` `replicated` `release` | Determines who spectators can hear: 0: only spectators; 1: all players; 2: spectated team; 3: self only; 4: nobody |
| `sv_spec_use_tournament_content_standards` | `false` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_specaccelerate` | `5.000000` | `gamedll` `clientdll` `archive` `notify` `replicated` |  |
| `sv_specnoclip` | `true` | `gamedll` `clientdll` `archive` `notify` `replicated` |  |
| `sv_specspeed` | `1200.000000` | `gamedll` `clientdll` `archive` `notify` `replicated` |  |
| `sv_staminajumpcost` | `0.080000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | sv_legacy_jump only: Stamina penalty for jumping |
| `sv_staminalandcost` | `0.050000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | sv_legacy_jump only: Stamina penalty for landing |
| `sv_staminamax` | `80.000000` | `gamedll` `clientdll` `replicated` `release` | Maximum stamina penalty |
| `sv_staminarecoveryrate` | `60.000000` | `gamedll` `clientdll` `replicated` `release` | Rate at which stamina recovers (units/sec) |
| `sv_standable_normal` | `0.700000` | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_step_move_vel_min` | `64.000000` | `gamedll` `clientdll` `replicated` `cheat` | Min velocity for step move. |
| `sv_stepsize` | `18.000000` | `developmentonly` `gamedll` `clientdll` `notify` `replicated` |  |
| `sv_stopspeed` | `80.000000` | `gamedll` `clientdll` `notify` `replicated` `release` | Minimum stopping speed when on ground. |
| `sv_strafing_inaccuracy_bias` | `0.500000` | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_strafing_inaccuracy_enabled` | `false` | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_strafing_inaccuracy_scale` | `0.100000` | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_strict_notarget` | `false` | `developmentonly` `gamedll` `defensive` | If set, notarget will cause entities to never think they are in the pvs |
| `sv_subtick_movement_view_angles` | `true` | `gamedll` `clientdll` `replicated` `release` | Whether or not subtick view angles are taken into account during movement. |
| `sv_suppress_friendlyfire_decals` | `true` | `developmentonly` `gamedll` |  |
| `sv_suppress_viewpunch` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` |  |
| `sv_surf_sounds` | `false` | `gamedll` `clientdll` `replicated` `release` | Should we try to play sounds for surf? |
| `sv_talk_after_dying_time` | `0.000000` | `gamedll` `clientdll` `replicated` `release` | The number of seconds a player can continue talking after dying as if they were still alive |
| `sv_talk_enemy_dead` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Dead players can hear all dead enemy communication (voice, chat) |
| `sv_talk_enemy_living` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Living players can hear all living enemy communication (voice, chat) |
| `sv_teamid_overhead` | `true` | `gamedll` `clientdll` `notify` `replicated` `release` | Shows teamID over player's heads.  0 = off, 1 = on |
| `sv_teamid_overhead_always_prohibit` | `false` | `gamedll` `clientdll` `notify` `replicated` `release` | Determines whether cl_teamid_overhead_always is prohibited. |
| `sv_teamid_overhead_maxdist` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If >0, server will override cl_teamid_overhead_maxdist |
| `sv_teamid_overhead_maxdist_spec` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If >0, server will override cl_teamid_overhead_maxdist_spec |
| `sv_tick_parallel_with_client` | `false` | `reference` |  |
| `sv_timebetweenducks` | `0.400000` | `gamedll` `clientdll` `replicated` `release` | Minimum time before recognizing consecutive duck key |
| `sv_turbophysics` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Turns on turbo physics |
| `sv_turning_inaccuracy_angle_min` | `4.000000` | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_turning_inaccuracy_decay` | `0.800000` | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_turning_inaccuracy_enabled` | `false` | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_unlag` | `true` | `developmentonly` `gamedll` | Enables player lag compensation |
| `sv_unlag_debug` | `false` | `developmentonly` `gamedll` |  |
| `sv_unlag_fixstuck` | `false` | `developmentonly` `gamedll` | Disallow backtracking a player for lag compensation if it will cause them to become stuck |
| `sv_use_hi_pri_context_switch_time` | `1.000000` | `gamedll` `clientdll` `replicated` `release` | +use search behaves as though high priority items are usable for this long after they become unusable to avoid players accidentally performing a different action. |
| `sv_use_playercache` | `true` | `gamedll` `clientdll` `replicated` `cheat` | Cache off player bounds for traces. |
| `sv_use_pvs_cache` | `false` | `developmentonly` `gamedll` |  |
| `sv_usercmd_custom_random_seed` | `false` | `gamedll` `release` | When enabled server will populate an additional random seed independent of the client |
| `sv_usercmd_execute_warning_ms` | `5.000000` | `gamedll` `archive` | Emit a warning if we spend more than N ms executing user commands for a single player |
| `sv_vac_webapi_auth_key` | `` | `gamedll` `release` | Key for when posting to vac related webapis. |
| `sv_versus_screen_scene_id` | `0` | `gamedll` `release` `commandline_enforced` | Determines which scene is used for the versus screen. |
| `sv_voice_proximity` | `-1.000000` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_vote_allow_in_warmup` | `false` | `gamedll` `release` | Allow voting during warmup? |
| `sv_vote_allow_spectators` | `false` | `gamedll` `release` | Allow spectators to initiate votes? |
| `sv_vote_command_delay` | `2.000000` | `gamedll` `release` | How long after a vote passes until the action happens |
| `sv_vote_count_spectator_votes` | `false` | `gamedll` `release` | Allow spectators to vote on issues? |
| `sv_vote_creation_timer` | `120.000000` | `gamedll` `release` | How often someone can individually call a vote. |
| `sv_vote_disallow_kick_on_match_point` | `false` | `gamedll` `release` | Disallow vote kicking on the match point round. |
| `sv_vote_failure_timer` | `300.000000` | `gamedll` `release` | A vote that fails cannot be re-submitted for this long |
| `sv_vote_issue_changelevel_allowed` | `true` | `developmentonly` `gamedll` `defensive` | Can people hold votes to change levels? |
| `sv_vote_issue_kick_allowed` | `true` | `gamedll` `notify` `replicated` `release` | Can people hold votes to kick players from the server? |
| `sv_vote_issue_loadbackup_allowed` | `true` | `gamedll` `notify` `replicated` `release` | Can people hold votes to load match from backup? |
| `sv_vote_issue_loadbackup_spec_authoritative` | `false` | `gamedll` `release` | When enabled, admins load match from backup without players vote |
| `sv_vote_issue_loadbackup_spec_only` | `false` | `gamedll` `notify` `replicated` `release` | When enabled, only admins load match from backup |
| `sv_vote_issue_loadbackup_spec_safe` | `true` | `gamedll` `release` | When enabled, admins load match from backup in safe time of the round only |
| `sv_vote_issue_matchready_allowed` | `true` | `developmentonly` `gamedll` `defensive` | Can people hold votes to ready/unready the match? |
| `sv_vote_issue_nextlevel_allowed` | `true` | `developmentonly` `gamedll` `defensive` | Can people hold votes to set the next level? |
| `sv_vote_issue_nextlevel_allowextend` | `true` | `developmentonly` `gamedll` `defensive` | Allow players to extend the current map? |
| `sv_vote_issue_nextlevel_choicesmode` | `true` | `developmentonly` `gamedll` `defensive` | Present players with a list of lowest playtime maps to choose from? |
| `sv_vote_issue_nextlevel_prevent_change` | `true` | `developmentonly` `gamedll` `defensive` | Not allowed to vote for a nextlevel if one has already been set. |
| `sv_vote_issue_pause_match_allowed` | `true` | `developmentonly` `gamedll` `defensive` | Can people hold votes to pause/unpause the match? |
| `sv_vote_issue_pause_match_spec_only` | `false` | `gamedll` `notify` `replicated` `release` | When enabled, only admins start technical pause |
| `sv_vote_issue_restart_game_allowed` | `false` | `gamedll` `release` | Can people hold votes to restart the game? |
| `sv_vote_issue_scramble_teams_allowed` | `false` | `developmentonly` `gamedll` `defensive` | Can people hold votes to scramble the teams? |
| `sv_vote_issue_surrrender_allowed` | `true` | `developmentonly` `gamedll` `defensive` | Can people hold votes to surrender? |
| `sv_vote_issue_swap_teams_allowed` | `false` | `developmentonly` `gamedll` `defensive` | Can people hold votes to swap the teams? |
| `sv_vote_issue_timeout_allowed` | `true` | `developmentonly` `gamedll` `defensive` | Can people hold votes to time out? |
| `sv_vote_kick_ban_duration` | `15.000000` | `gamedll` `notify` `replicated` `release` | How long should a kick vote ban someone from the server? (in minutes) |
| `sv_vote_quorum_ratio` | `0.501000` | `gamedll` `release` | The minimum ratio of players needed to vote on an issue to resolve it. |
| `sv_vote_timer_duration` | `15.000000` | `gamedll` `release` | How long to allow voting on an issue |
| `sv_vote_to_changelevel_before_match_point` | `false` | `gamedll` `replicated` `release` `commandline_enforced` | Restricts vote to change level to rounds prior to match point (default 0, vote is never disallowed) |
| `sv_vote_to_changelevel_rndmin` | `0` | `gamedll` `replicated` `release` `commandline_enforced` | When non-zero, restricts vote to change level to this many first rounds or minutes of the match (default 0, vote is not disallowed) |
| `sv_walkable_normal` | `0.700000` | `gamedll` `clientdll` `replicated` `cheat` `release` |  |
| `sv_warmup_to_freezetime_delay` | `4` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Delay between end of warmup and start of match. |
| `sv_water_slow_amount` | `0.900000` | `gamedll` `clientdll` `replicated` `release` |  |
| `sv_wateraccelerate` | `10.000000` | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_waterdist` | `12.000000` | `developmentonly` `gamedll` `clientdll` `replicated` | Vertical view fixup when eyes are near water plane. |
| `sv_waterfriction` | `1.000000` | `gamedll` `clientdll` `notify` `replicated` `release` |  |
| `sv_weapon_require_use_grace_period` | `1.000000` | `gamedll` `release` |  |
| `sv_weapon_swap_difficulty_near_hi_pri` | `2` | `gamedll` `clientdll` `replicated` `release` | 0 = Cone searches easily reach past high priority items to swap weapons. 1 = Cone searches are narrowed and require that the weapon is strictly closer. 2 = cone searches are disabled near high priority items |
| `sv_workshop_allow_other_maps` | `true` | `gamedll` `release` | When hosting a workshop collection, users can play other workshop map on this server when it is empty and then mapcycle into this server collection. |
| `sv_workshop_map_save_data_max_filesize_mb` | `1` | `gamedll` `release` `commandline_enforced` |  |
| `target_scan_use_query_cache` | `true` | `developmentonly` `gamedll` `defensive` |  |
| `teleport_trigger_debug` | `false` | `developmentonly` `gamedll` |  |
| `testscript_debug` | `false` | `developmentonly` `defensive` | Debug test scripts. |
| `think_limit` | `10.000000` | `gamedll` `clientdll` `replicated` `release` | Maximum think time in milliseconds, warning is printed if this is exceeded. |
| `throttle_expensive_ai` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `toast_manager_override_duration` | `-1.000000` | `developmentonly` `clientdll` |  |
| `tool_spawned_model_scales` | `1.000000 1.000000 1.000000` | `developmentonly` `gamedll` `replicated` |  |
| `tools_stall_monitor_break_on_unknown_cause` | `false` | `developmentonly` | Break on unknown stall cause |
| `trigger_fan_debug` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `trigger_fan_player_windblock_debug` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `trusted_launch` | `0` | `clientdll` `archive` | Trusted launch status |
| `tv_advertise_watchable` | `false` | `reference` |  |
| `tv_allow_autorecording_index` | `-1` | `gamedll` `release` | When >=0 restricts autorecording only to the specified TV index |
| `tv_allow_camera_man` | `true` | `developmentonly` `gamedll` `defensive` | Auto director allows spectators to become camera man |
| `tv_allow_camera_man_steamid` | `0` | `gamedll` `release` | Allows tournament production cameraman to run csgo.exe -interactivecaster on SteamID 7650123456XXX and be the camera man. |
| `tv_allow_camera_man_steamid2` | `0` | `gamedll` `release` | Allows tournament production tv cameraman to run csgo.exe -interactivecaster on SteamID 7650123456XXX and be the tv camera man. |
| `tv_allow_static_shots` | `true` | `gamedll` `release` | Auto director uses fixed level cameras for shots |
| `tv_delay` | `120` | `gamedll` `release` `commandline_enforced` | SourceTV broadcast delay in seconds |
| `tv_delay1` | `15` | `gamedll` `release` `commandline_enforced` | SourceTV[instance 1] broadcast delay in seconds |
| `tv_delaymapchange` | `true` | `gamedll` `release` | Delays map change until broadcast is complete |
| `tv_include_usercommands` | `true` | `gamedll` `release` | HLTV streams will include player usercommands each tick |
| `tv_listen_voice_indices` | `0` | `clientdll` `userinfo` | Bitfield of playerslots to listen to voice messages from when connected to SourceTV, default is none |
| `tv_listen_voice_indices_h` | `0` | `clientdll` `userinfo` | High 32 bits of bitfield of playerslots to listen to voice messages from when connected to SourceTV, default is none |
| `tv_log_director_events` | `false` | `developmentonly` `gamedll` `defensive` | Log game events being considered by the director |
| `tv_nochat` | `false` | `reference` |  |
| `tv_relayradio` | `false` | `gamedll` `release` | Relay team radio commands to TV: 0=off, 1=on |
| `tv_show_allchat` | `true` | `gamedll` `release` |  |
| `tv_spectator_port_offset` | `0` | `clientdll` `release` |  |
| `tv_transmitall` | `false` | `reference` |  |
| `ui_deepstats_radio_heat_figurine` | `0` | `clientdll` `archive` `release` |  |
| `ui_deepstats_radio_heat_tab` | `0` | `clientdll` `archive` `release` |  |
| `ui_deepstats_radio_heat_team` | `0` | `clientdll` `archive` `release` |  |
| `ui_deepstats_toplevel_mode` | `0` | `clientdll` `archive` `release` |  |
| `ui_hud_dist` | `24.000000` | `developmentonly` `clientdll` `replicated` `defensive` | distance from the player to the hud |
| `ui_inspect_bkgnd_map_C2AEBB5E` | `warehouse` | `clientdll` `archive` `release` | Inspect background map |
| `ui_inventorysettings_recently_acknowledged` | `` | `clientdll` `archive` `release` |  |
| `ui_leaderboards_top_public_appid` | `730` | `clientdll` `hidden` `release` |  |
| `ui_lobby_draft_enabled` | `false` | `clientdll` `release` |  |
| `ui_mainmenu_bkgnd_movie_C2AEBB5E` | `de_cache` | `clientdll` `archive` `release` | Main menu background movie |
| `ui_nearbylobbies_filter3` | `competitive` | `clientdll` `archive` `release` |  |
| `ui_news_last_read_link` | `` | `clientdll` `archive` `release` |  |
| `ui_news_last_read_link2` | `` | `clientdll` `archive` `release` |  |
| `ui_notification_tb_snooze` | `` | `clientdll` `archive` `release` |  |
| `ui_party_msg_sound_enabled` | `true` | `clientdll` `release` | When enabled, lobby messages will play a short sound |
| `ui_playsettings_custom_preset` | `` | `clientdll` `archive` `release` |  |
| `ui_playsettings_directchallengekey` | `` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_casual` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_competitive` | `16` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_cooperative` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_deathmatch` | `32` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_retakes` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_scrimcomp2v2` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_skirmish` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_listen_survival` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_casual` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_competitive` | `16` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_cooperative` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_deathmatch` | `32` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_retakes` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_scrimcomp2v2` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_skirmish` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_flags_official_survival` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_listen_annotations` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_listen_grenades` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_listen_infammo` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_listen_infwarmup` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_listen_casual` | `mg_de_dust2` | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_listen_competitive` | `mg_de_dust2` | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_listen_deathmatch` | `mg_de_dust2` | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_listen_gungameprogressive` | `mg_ar_baggage` | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_listen_retakes` | `mg_de_dust2` | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_listen_scrimcomp2v2` | `mg_de_inferno` | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_official_casual` | `mg_casualalpha` | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_official_deathmatch` | `mg_casualalpha` | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_official_gungameprogressive` | `mg_armsrace` | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_official_retakes` | `mg_casualalpha` | `clientdll` `archive` `release` |  |
| `ui_playsettings_maps_workshop` | `` | `clientdll` `archive` `release` |  |
| `ui_playsettings_mode_listen` | `deathmatch` | `clientdll` `archive` `release` |  |
| `ui_playsettings_mode_official_v20` | `deathmatch` | `clientdll` `archive` `release` |  |
| `ui_playsettings_survival_solo` | `0` | `clientdll` `archive` `release` |  |
| `ui_playsettings_warmup_map_name` | `de_mirage` | `clientdll` `archive` `release` |  |
| `ui_popup_weaponupdate_version` | `0` | `clientdll` `archive` `release` |  |
| `ui_render_task_clips_label` | `dealt_damage` | `clientdll` `release` |  |
| `ui_render_task_file` | `rendertask` | `clientdll` `release` |  |
| `ui_render_task_fps` | `60` | `clientdll` `release` |  |
| `ui_render_task_generate_clips` | `false` | `clientdll` `release` |  |
| `ui_setting_advertiseforhire_auto` | `1` | `clientdll` `archive` `release` | Whether users will automatically advertise for invites (0: off; 1: last; 2: auto) |
| `ui_setting_advertiseforhire_auto_last` | `/competitive` | `clientdll` `archive` `release` | Which game mode users last used to advertise for invites |
| `ui_show_subscription_alert` | `0` | `clientdll` `archive` `release` |  |
| `ui_show_unlock_competitive_alert` | `` | `clientdll` `archive` `release` |  |
| `ui_steam_overlay_notification_position` | `bottomleft` | `clientdll` `archive` | Steam overlay notification position |
| `ui_steam_overlay_notification_position_horz` | `0` | `clientdll` `archive` | Steam overlay notification position horizontal offset |
| `ui_steam_overlay_notification_position_vert` | `0` | `clientdll` `archive` | Steam overlay notification position vertical offset |
| `ui_vanitysetting_loadoutslot_ct` | `` | `clientdll` `archive` `release` |  |
| `ui_vanitysetting_loadoutslot_t` | `` | `clientdll` `archive` `release` |  |
| `ui_vanitysetting_team` | `` | `clientdll` `archive` `release` |  |
| `update_all_keyframed_in_spatial_partition_update` | `true` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `update_voices_low_priority` | `false` | `developmentonly` `defensive` |  |
| `vehicle_debug_impact_damage` | `false` | `developmentonly` `gamedll` |  |
| `videocfg_ao_detail` | `0` | `developmentonly` `clientdll` `defensive` |  |
| `videocfg_fsr_detail` | `0` | `developmentonly` `clientdll` `defensive` |  |
| `videocfg_hdr_detail` | `-1` | `developmentonly` `clientdll` `defensive` |  |
| `videocfg_particle_detail` | `1` | `developmentonly` `clientdll` `defensive` |  |
| `videocfg_shadow_quality` | `1` | `developmentonly` `clientdll` `defensive` |  |
| `videocfg_texture_detail` | `1` | `developmentonly` `clientdll` `defensive` |  |
| `view_punch_decay` | `18.000000` | `gamedll` `clientdll` `replicated` `cheat` `release` | Decay factor exponent for view punch |
| `viewmodel_fov` | `60.000000` | `clientdll` `archive` `userinfo` `per_user` | Viewmodel FOV |
| `viewmodel_offset_x` | `1.000000` | `clientdll` `archive` `userinfo` `per_user` | viewmodel_offset_x |
| `viewmodel_offset_y` | `1.000000` | `clientdll` `archive` `userinfo` `per_user` | viewmodel_offset_y |
| `viewmodel_offset_z` | `-1.000000` | `clientdll` `archive` `userinfo` `per_user` | viewmodel_offset_z |
| `viewmodel_presetpos` | `1` | `clientdll` `archive` | 1:"Desktop", 2:"Classic"  |
| `violence_ablood` | `false` | `reference` |  |
| `violence_agibs` | `false` | `reference` |  |
| `violence_hblood` | `false` | `reference` |  |
| `violence_hgibs` | `false` | `reference` |  |
| `vis_force` | `false` | `gamedll` `cheat` |  |
| `vismon_poll_frequency` | `0.500000` | `gamedll` `cheat` |  |
| `vismon_trace_limit` | `12` | `gamedll` `cheat` |  |
| `voice_all_icons` | `false` | `developmentonly` `clientdll` `defensive` | Draw all players' voice icons |
| `voice_clientdebug` | `0` | `developmentonly` `clientdll` `defensive` |  |
| `voice_fadeouttime` | `0.005000` | `developmentonly` `defensive` |  |
| `voice_initial_buffer_ms` | `200` | `developmentonly` `defensive` |  |
| `voice_loopback` | `false` | `userinfo` |  |
| `voice_loopback_no_networking` | `false` | `reference` |  |
| `voice_min_buffer_ms` | `100` | `developmentonly` `defensive` |  |
| `voice_modenable` | `true` | `clientdll` `archive` `release` `clientcmd_can_execute` | Enable/disable voice in this mod. |
| `voice_player_speaking_delay_threshold` | `0.500000` | `gamedll` `cheat` |  |
| `voice_serverdebug` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `voice_stall_ms` | `250.000000` | `developmentonly` `defensive` |  |
| `voice_threshold` | `0.000000` | `reference` |  |
| `voice_threshold_delay` | `0.000000` | `reference` |  |
| `voice_vox` | `0` | `clientdll` `archive` `per_user` | Voice chat uses a vox-style always on |
| `voice_vox_current_peak` | `0.000000` | `developmentonly` `clientdll` `defensive` | Current peak value (out of 64k) of the incoming voice stream |
| `volume` | `1.000000` | `archive` | Sound volume |
| `volume_fog_debug_volumes` | `false` | `cheat` |  |
| `volume_fog_density_scale` | `1.000000` | `developmentonly` `cheat` | Scale global volume fog density |
| `volume_fog_depth` | `128` | `developmentonly` `defensive` | Depth of volume fog texture |
| `volume_fog_depth_warp` | `7.000000` | `developmentonly` `defensive` |  |
| `volume_fog_depth_warp_debug` | `false` | `developmentonly` `defensive` |  |
| `volume_fog_dither_scale` | `1.000000` | `cheat` |  |
| `volume_fog_enable_jitter` | `true` | `cheat` |  |
| `volume_fog_height` | `160` | `developmentonly` `defensive` | Height of volume fog texture |
| `volume_fog_intermediate_textures_hdr` | `true` | `developmentonly` `defensive` |  |
| `volume_fog_shadow_penumbra_multiplier` | `3.000000` | `developmentonly` `defensive` | Penumbra size multiplier for shadow sampling, reduces fog shadow aliasing |
| `volume_fog_temporal_filter` | `true` | `developmentonly` `defensive` |  |
| `volume_fog_temporal_weight` | `0.900000` | `developmentonly` `defensive` | Temporal filtering weight |
| `volume_fog_width` | `240` | `developmentonly` `defensive` | Width of volume fog texture |
| `vprof_scope_entity_clientthink` | `false` | `developmentonly` `clientdll` `hidden` `defensive` | Does nothing whatsoever. |
| `vprof_scope_entity_thinks` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` |  |
| `vprof_think_limit` | `false` | `developmentonly` `gamedll` `defensive` |  |
| `vt_sim_streaming_delay_ms` | `500.000000` | `developmentonly` `defensive` |  |
| `weapon_accuracy_forcespread` | `0.000000` | `gamedll` `clientdll` `replicated` `release` | Force spread to the specified value. |
| `weapon_accuracy_logging` | `false` | `developmentonly` `gamedll` `clientdll` `archive` `replicated` |  |
| `weapon_accuracy_nospread` | `false` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Disable weapon inaccuracy spread |
| `weapon_accuracy_reset_on_deploy` | `false` | `gamedll` `clientdll` `replicated` `cheat` `release` | On deploy, forcibly reset weapon accuracy to zero. |
| `weapon_accuracy_shotgun_spread_patterns` | `true` | `gamedll` `clientdll` `replicated` `release` |  |
| `weapon_accuracy_stack_boost_limit` | `2` | `gamedll` `clientdll` `replicated` `release` | Apply ladder inaccuracy to players boosted by a stack of this many (or more) players |
| `weapon_air_spread_scale` | `1.000000` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | Scale factor for jumping inaccuracy, set to 0 to make jumping accuracy equal to standing |
| `weapon_all_nametag` | `false` | `developmentonly` `clientdll` |  |
| `weapon_all_stattrak` | `false` | `developmentonly` `clientdll` |  |
| `weapon_auto_cleanup_time` | `0.000000` | `gamedll` `clientdll` `replicated` `release` | If set to non-zero, weapons will delete themselves after the specified time (in seconds) if no players are near. |
| `weapon_debug_inaccuracy_only_up` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Force weapon inaccuracy to be in exactly the up direction |
| `weapon_debug_max_inaccuracy` | `false` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | Force all shots to have maximum inaccuracy |
| `weapon_debug_spread_gap` | `0.670000` | `clientdll` `cheat` `per_user` |  |
| `weapon_debug_spread_show` | `0` | `clientdll` `cheat` `per_user` | Enables display of weapon accuracy; 1: show accuracy box, 3: show accuracy with dynamic crosshair |
| `weapon_land_dip_amt` | `20.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `cheat` | The amount the gun should dip when the player lands after a jump. |
| `weapon_max_before_cleanup` | `0` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | If set to non-zero, will remove the oldest dropped weapon to maintain the specified number of dropped weapons in the world. |
| `weapon_molotov_maxdetonateslope` | `30.000000` | `developmentonly` `gamedll` `clientdll` `replicated` `defensive` | Maximum angle of slope on which the molotov will detonate |
| `weapon_near_empty_sound` | `true` | `gamedll` `clientdll` `replicated` `cheat` |  |
| `weapon_random_stickers` | `false` | `developmentonly` `clientdll` |  |
| `weapon_reticle_knife_show` | `true` | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | When enabled will show knife reticle on clients. Used for game modes requiring target id display when holding a knife. |
| `weapon_skin_force_legacy` | `-1` | `developmentonly` `gamedll` `clientdll` `replicated` |  |
| `weapon_skins` | `true` | `developmentonly` `clientdll` |  |
| `weapon_skins_on_default` | `false` | `developmentonly` `clientdll` |  |
| `weapon_sound_falloff_multiplier` | `1.000000` | `gamedll` `clientdll` `replicated` `cheat` `release` `commandline_enforced` | Scaling for falloff of weapon firing sounds |
| `webapi_values_init_buffer_size` | `65536` | `developmentonly` `clientdll` `defensive` | Initial buffer size for buffers in the WebAPIValues buffer pool |
| `webapi_values_max_pool_size_mb` | `400` | `developmentonly` `clientdll` `defensive` | Maximum size in bytes of the WebAPIValues buffer pool |
| `wind_system_debug_volumes` | `false` | `developmentonly` `defensive` |  |
| `wind_system_default_resolution_xy` | `256` | `developmentonly` `defensive` |  |
| `wind_system_default_resolution_z` | `32` | `developmentonly` `defensive` |  |
| `wind_system_default_sample_min_spacing` | `12.000000` | `developmentonly` `defensive` |  |
| `wind_system_temporal_smoothing` | `true` | `developmentonly` `defensive` |  |
| `zoom_sensitivity_ratio` | `1.000000` | `clientdll` `archive` `per_user` | Additional mouse sensitivity scale factor applied when FOV is zoomed in. |
