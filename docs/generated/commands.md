---
layout: default
title: Commands
nav_order: 5
---

# Console Commands

All console commands extracted from CS2.

| Command | Flags | Description |
|---------|-------|-------------|
| `+camdistance` | `developmentonly` `clientdll` `defensive` |  |
| `+cammousemove` | `developmentonly` `clientdll` `defensive` |  |
| `+cl_show_team_equipment` | `clientdll` `release` |  |
| `+lookatweapon` | `clientdll` `release` |  |
| `+quickbuyradial` | `clientdll` `release` |  |
| `+quickgearradial` | `developmentonly` `clientdll` `defensive` |  |
| `+quickgrenaderadial` | `clientdll` `release` |  |
| `+quickinv` | `clientdll` `release` |  |
| `+radialradio` | `clientdll` `release` |  |
| `+radialradio2` | `clientdll` `release` |  |
| `+radialradio3` | `clientdll` `release` |  |
| `+spray_menu` | `clientdll` `release` |  |
| `-camdistance` | `developmentonly` `clientdll` `defensive` |  |
| `-cammousemove` | `developmentonly` `clientdll` `defensive` |  |
| `-cl_show_team_equipment` | `clientdll` `release` |  |
| `-lookatweapon` | `clientdll` `release` |  |
| `-quickbuyradial` | `clientdll` `release` |  |
| `-quickgearradial` | `developmentonly` `clientdll` `defensive` |  |
| `-quickgrenaderadial` | `clientdll` `release` |  |
| `-quickinv` | `clientdll` `release` |  |
| `-radialradio` | `clientdll` `release` |  |
| `-radialradio2` | `clientdll` `release` |  |
| `-radialradio3` | `clientdll` `release` |  |
| `-spray_menu` | `clientdll` `release` |  |
| `ShowSteamStatsSessionID` | `developmentonly` `clientdll` | Prints out the game stats session ID's (developer convar must be set to non-zero). |
| `Test_Checkpoint` | `developmentonly` `defensive` | Indicate to a test script that a checkpoint has been reached |
| `Test_CreateEntity` | `gamedll` `cheat` |  |
| `Test_EHandle` | `gamedll` `cheat` |  |
| `Test_ExitProcess` | `cheat` | Test_ExitProcess <exit code> - immediately kill the process. |
| `Test_Loop` | `developmentonly` `defensive` | Test_Loop <loop name> - loop back to the specified loop start point unconditionally. |
| `Test_LoopCount` | `developmentonly` `defensive` | Test_LoopCount <loop name> <count> - loop back to the specified loop start point the specified # of times. |
| `Test_LoopForNumSeconds` | `developmentonly` `defensive` | Test_LoopForNumSeconds <loop name> <time> - loop back to the specified start point for the specified # of seconds. |
| `Test_RandomChance` | `developmentonly` `defensive` | Test_RandomChance <percent chance, 0-100> <token1> <token2...> - Roll the dice and maybe run the command following the percentage chance. |
| `Test_RandomPlayerPosition` | `gamedll` `cheat` |  |
| `Test_StartLoop` | `developmentonly` `defensive` | Test_StartLoop <loop name> - Denote the start of a loop. Really just defines a named point you can jump to. |
| `Test_StartScript` | `developmentonly` `defensive` | Start a test script running.. |
| `_resetgamestats` | `developmentonly` `gamedll` `defensive` | Erases current game stats and writes out a blank stats file |
| `adjacent_levels` | `developmentonly` `gamedll` | List adjacent levels |
| `adjacent_preload` | `developmentonly` `gamedll` | Preload adjacennt level data - will override regular changelevel code -- PROTOTYPE/WIP |
| `anim_eval_stats` | `developmentonly` `gamedll` | Displays stats about how many EvaluatePose calls are unused |
| `animevents_dump` | `gamedll` `cheat` | List all the currently registered anim events.
 |
| `animgraph_dump_update_list` | `developmentonly` `gamedll` | Displays stats about which animations are updating |
| `annotation_append` | `clientdll` `release` | Load annotation to a file without clearing existing annotations |
| `annotation_clear` | `clientdll` `release` | Clear all annotation |
| `annotation_create` | `clientdll` `release` | Creates an annotation |
| `annotation_delete_previous_node_set` | `clientdll` `release` | Delete the last node set created |
| `annotation_load` | `clientdll` `release` | Load annotation to a file after first clearing existing annotations |
| `annotation_reload` | `clientdll` `release` | Reload the annotation file |
| `annotation_reload_language_file` | `clientdll` `release` | Creates an annotation |
| `annotation_save` | `clientdll` `release` | Save annotation to a file |
| `apply_crosshair_code` | `developmentonly` `clientdll` `defensive` | Apply a crosshair code to the current crosshair settings. |
| `autobuy` | `clientdll` `clientcmd_can_execute` | Attempt to purchase items with the order listed in cl_autobuy |
| `autosave` | `developmentonly` `gamedll` `defensive` | Autosave |
| `autosavedangerous` | `developmentonly` `gamedll` `defensive` | AutoSaveDangerous |
| `autosavedangerousissafe` | `developmentonly` `gamedll` `defensive` |  |
| `axis` | `gamedll` `cheat` | Draw an axis
	Arguments:  x y z pitch yaw roll <lifetime = 10.0> <r g b a>
 |
| `bake_bomb_damage_render_visualization` | `clientdll` `cheat` |  |
| `bot_add` | `gamedll` `release` | bot_add <t\|ct> <type> <difficulty> <name> - Adds a bot matching the given criteria. |
| `bot_add_ct` | `gamedll` `release` | bot_add_ct <type> <difficulty> <name> - Adds a Counter-Terrorist bot matching the given criteria. |
| `bot_add_t` | `gamedll` `release` | bot_add_t <type> <difficulty> <name> - Adds a terrorist bot matching the given criteria. |
| `bot_all_weapons` | `gamedll` `release` | Allows the bots to use all weapons |
| `bot_goto_mark` | `gamedll` `cheat` | Sends a bot to the marked nav area (useful for testing navigation meshes) |
| `bot_goto_selected` | `gamedll` `cheat` | Sends a bot to the selected nav area (useful for testing navigation meshes) |
| `bot_hurt` | `gamedll` `cheat` |  |
| `bot_kick` | `gamedll` `release` | bot_kick <all> <t\|ct> <type> <difficulty> <name> - Kicks a specific bot, or all bots, matching the given criteria. |
| `bot_kill` | `gamedll` `cheat` | bot_kill <all> <t\|ct> <type> <difficulty> <name> - Kills a specific bot, or all bots, matching the given criteria. |
| `bot_knives_only` | `gamedll` `release` | Restricts the bots to only using knives |
| `bot_path` | `gamedll` `cheat` | bot_path <all> <t\|ct> <type> <difficulty> <name> - Tells a specific bot to follow a human path, matching the given criteria. |
| `bot_pistols_only` | `gamedll` `release` | Restricts the bots to only using pistols |
| `bot_place` | `gamedll` `cheat` | bot_place - Places a bot from the map at where the local player is pointing. |
| `bot_snipers_only` | `gamedll` `release` | Restricts the bots to only using sniper rifles |
| `box` | `gamedll` `cheat` | Draw a bbox
	Arguments:  minx miny miny maxx maxy maxz <lifetime = 10.0> <r g b a>
 |
| `breakable_force_break` | `developmentonly` `gamedll` `defensive` | Force a breakable to break |
| `bugbug` | `clientdll` `release` | bugbug |
| `buildcubemaps` | `developmentonly` `clientdll` `defensive` | Build Cubemaps |
| `buildsparseshadowtree` | `developmentonly` `clientdll` `hidden` | Build Sparse Shadow Tree |
| `buymenu` | `clientdll` `server_can_execute` | Show or hide main buy menu |
| `buyrandom` | `gamedll` `client_can_execute` | Buy random primary and secondary. Primarily for deathmatch where cost is not an issue. |
| `callvote` | `gamedll` `client_can_execute` | Start a vote on an issue. |
| `cam_command` | `clientdll` `cheat` | Tells camera to change modes |
| `camera_cut_to_datadriven_camera` | `developmentonly` `clientdll` `hidden` `defensive` |  |
| `camera_path_add` | `clientdll` `cheat` |  |
| `camera_path_clear_all` | `clientdll` `cheat` |  |
| `camera_path_delete` | `clientdll` `cheat` |  |
| `camera_path_demo` | `clientdll` `cheat` |  |
| `camera_path_load` | `clientdll` `cheat` |  |
| `camera_path_save` | `clientdll` `cheat` |  |
| `camerazoomin` | `developmentonly` `clientdll` `defensive` |  |
| `camerazoomout` | `developmentonly` `clientdll` `defensive` |  |
| `camortho` | `clientdll` `cheat` | Switch to orthographic camera. |
| `cancelselect` | `clientdll` `server_can_execute` |  |
| `capturecubemap` | `developmentonly` `clientdll` `defensive` | Capture Cubemap |
| `cast_aabb` | `gamedll` `cheat` | Tests box collision detection |
| `cast_bullet` | `gamedll` `cheat` | Tests bullet cast |
| `cast_capsule` | `gamedll` `cheat` | Tests capsule collision detection |
| `cast_convex` | `gamedll` `cheat` | Tests convex hull collision detection |
| `cast_cylinder` | `gamedll` `cheat` | Tests cylinder collision detection |
| `cast_intervals` | `gamedll` `cheat` | Tests interval ray cast |
| `cast_obb` | `gamedll` `cheat` | Tests cylinder collision detection |
| `cast_physics` | `gamedll` `cheat` | Tests physics shape collision detection |
| `cast_ray` | `gamedll` `cheat` | Tests ray cast |
| `cast_sphere` | `gamedll` `cheat` | Tests sphere cast |
| `cc_emit` | `developmentonly` `clientdll` `defensive` | Emits a closed caption |
| `check_nofilefd` | `developmentonly` `defensive` | Print the current number of FDs reported by getrlimit |
| `cl_anim_eval_stats` | `developmentonly` `clientdll` | Displays stats about how many EvaluatePose calls are unused |
| `cl_animgraph_dump_update_list` | `developmentonly` `clientdll` | Displays stats about which animations are updating |
| `cl_avatar_convert_png` | `clientdll` `cheat` `release` | Converts all rgb avatars in the avatars directory to png |
| `cl_avatar_convert_rgb` | `clientdll` `cheat` `release` | Converts all png avatars in the avatars directory to rgb |
| `cl_axis` | `clientdll` `cheat` | Draw an axis
	Arguments:  x y z pitch yaw roll <lifetime = 10.0> <r g b a>
 |
| `cl_box` | `clientdll` `cheat` | Draw a bbox
	Arguments:  minx miny miny maxx maxy maxz <lifetime = 10.0> <r g b a>
 |
| `cl_cs_dump_econ_item_stringtable` | `developmentonly` `clientdll` `defensive` | cl_cs_dump_econ_item_stringtable |
| `cl_debugoverlay_cycle_domain` | `clientdll` `cheat` | Toggles visibility of the debug overlay system. |
| `cl_debugoverlay_cycle_state` | `clientdll` `cheat` | Toggles visibility of the debug overlay system. |
| `cl_debugoverlay_dashboard` | `clientdll` `cheat` | Makes the debug overlay dashboard visible. |
| `cl_debugoverlay_hide_imgui` | `clientdll` `cheat` | Hides the overlay. |
| `cl_debugoverlay_toggle` | `clientdll` `cheat` | Toggles visibility of the debug overlay system. |
| `cl_destroy_ragdolls` | `developmentonly` `clientdll` `defensive` | Destroys all client-side ragdolls |
| `cl_dev_decaltrace_blood` | `developmentonly` `clientdll` `cheat` | Shoot out a decal spray that shoots blood. |
| `cl_drawcross` | `clientdll` `cheat` | Draws a cross at the given location
	Arguments: x y z |
| `cl_drawline` | `clientdll` `cheat` | Draws line between two 3D Points.
	Green if no collision
	Red is collides with something
	Arguments: x1 y1 z1 x2 y2 z2 |
| `cl_dump_projected_texture_count` | `developmentonly` `clientdll` `defensive` | Print out number of active projected textures |
| `cl_dump_response_symbols` | `developmentonly` `clientdll` `defensive` | print all response symbols to the console |
| `cl_dumpentity` | `clientdll` `cheat` | Dumps info about an entity |
| `cl_dumpsplithacks` | `developmentonly` `clientdll` `defensive` | Dump split screen workarounds. |
| `cl_ent_absbox` | `clientdll` `cheat` | Displays the total bounding box for the given entity(s) in green.  Some entites will also display entity specific overlays.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_actornames` | `clientdll` `cheat` | Displays the entity name for all entities that have ShouldDisplayInActorNames true in code |
| `cl_ent_animgraph2_open_graph` | `clientdll` `cheat` | Opens the graph and starts live debugging the AG2 graph for a given entity
	Arguments: entityName
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_animgraph2_record` | `clientdll` `cheat` | Starts live debugging & recording the AG2 graph for a given entity
	Arguments: entityName
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_animgraph_debug` | `clientdll` `cheat` | Displays debug draws about the given entity(ies) animgraph
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_attachments` | `clientdll` `cheat` | Displays the attachment points on an entity.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_bbox` | `clientdll` `cheat` | Displays the movement bounding box for the given entity(ies) in orange.  Some entites will also display entity specific overlays.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_call` | `clientdll` `cheat` | ent_call <funcname> <option:entname> calls function on current look target or filtername, checks on ent, then root, then mode, then map scope |
| `cl_ent_clear_debug_overlays` | `clientdll` `cheat` | Clears all debug overlays |
| `cl_ent_find` | `clientdll` `cheat` | Find and list all entities with classnames or targetnames that contain the specified substrings.
Format: find_ent <substring>
 |
| `cl_ent_find_index` | `clientdll` `cheat` | Display data for entity matching specified index.
Format: find_ent_index <index>
 |
| `cl_ent_grab` | `clientdll` `cheat` | grabs the object in front of the player. Options: -loose -multiple -toggle |
| `cl_ent_hierarchy` | `clientdll` `cheat` | Prints the entity hierarchy tree rooted at the specified ent(s) |
| `cl_ent_hitbox` | `clientdll` `cheat` | Displays the hitboxes for the given entity(ies).
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_joints` | `clientdll` `cheat` | Displays the joint names + axes an entity.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_messages` | `clientdll` `cheat` | Toggles input/output message display for the selected entity(ies).  The name of the entity will be displayed as well as any messages that it sends or receives.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_name` | `clientdll` `cheat` | Displays the entity name |
| `cl_ent_picker` | `clientdll` `cheat` | Toggles 'picker' mode.  When picker is on, the bounding box, pivot and debugging text is displayed for whatever entity the player is looking at.
	Arguments:	full - enables all debug information |
| `cl_ent_pivot` | `clientdll` `cheat` | Displays the pivot for the given entity(ies).
	(y=up=green, z=forward=blue, x=left=red). 
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_remove` | `clientdll` `cheat` | Removes the given entity(s)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_remove_all` | `clientdll` `cheat` | Removes all entities of the specified type
	Arguments:   	{entity_name} / {class_name}  |
| `cl_ent_scale` | `clientdll` `cheat` | Scales entities.	Arguments: <scale factor> <{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at}> |
| `cl_ent_scenehierarchy` | `clientdll` `cheat` | Prints the entity scenenode hierarchy tree rooted at the specified ent(s) |
| `cl_ent_script_dump` | `clientdll` `cheat` | Dumps the names and values of this entity's script scope to the console
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_select` | `clientdll` `cheat` | Select or deselects the given entities(s) for later manipulation
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_setang` | `clientdll` `cheat` `client_can_execute` | Set entity angles |
| `cl_ent_setname` | `clientdll` `cheat` | Sets the targetname of the given entity(s)
	Arguments:   	<new entity name> <{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at}> |
| `cl_ent_setpos` | `clientdll` `cheat` `client_can_execute` | Move entity to position |
| `cl_ent_show_damage` | `clientdll` `cheat` | Sets damage display mode.  When on, you will see the amount of damage dealt over the target's head. |
| `cl_ent_skeleton` | `clientdll` `cheat` | Displays the skeleton for the given entity(ies).
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_spew_derived_classes` | `developmentonly` `clientdll` | Prints out all entity classes which inherit from a specified base class |
| `cl_ent_text` | `clientdll` `cheat` `vconsole_fuzzy_matching` | Displays text debugging information about the given entity(ies) on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_text256` | `clientdll` `cheat` | Displays text debugging information about the given entity(ies) [within 256 units of the player] on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_text_clear` | `clientdll` `cheat` | Hide text debugging information about the given entity(ies) on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_text_filter` | `clientdll` `cheat` | Set which ent_text filters you want:  |
| `cl_ent_text_radius` | `clientdll` `cheat` | Displays text debugging information about the given entity(ies) [near the player] on top of the entity (See Overlay Text)
	2 Arguments:   	<Radius> <{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at}> |
| `cl_ent_text_sticky_add` | `clientdll` `cheat` | Adds to list of names to display text debugging information about the given entity(ies) on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_text_sticky_clear` | `clientdll` `cheat` | Clears the list of names to display text debugging information about the given entity(ies) on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_text_sticky_dump` | `clientdll` `cheat` | Spews the list of names to display text debugging information about the given entity(ies) on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_text_sticky_remove` | `clientdll` `cheat` | Removes from the list of names to display text debugging information about the given entity(ies) on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_ungrab` | `clientdll` `cheat` | un-grabs all objects |
| `cl_ent_vcollide_wireframe` | `clientdll` `cheat` | Displays the interpolated vcollide wireframe pm am entity.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_viewoffset` | `clientdll` `cheat` | Displays the eye position for the given entity(ies) in red.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ent_visibility_traces` | `clientdll` `cheat` `vconsole_fuzzy_matching` | Displays visibility traces for the given entity
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_ents` | `developmentonly` `clientdll` `defensive` | List client entities, sorted by spawn group |
| `cl_game_mode_convars` | `developmentonly` `clientdll` `defensive` | Display the values of the convars for the current game_mode. |
| `cl_imgui_debug_entity` | `clientdll` `cheat` | Shows the entity browser, focused on the entity you specify.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cl_imgui_set_selection` | `clientdll` `cheat` | Sets ImGui selection |
| `cl_imgui_set_status_text` | `clientdll` `cheat` | Sets ImGui header status text |
| `cl_in_forcebuttonstate` | `developmentonly` `clientdll` `vconsole_fuzzy_matching` | Forces a button to be a particular state - WHEN PROCESSING USERCOMMANDS |
| `cl_interp` | `clientdll` `release` | Read the effective client simulation interpolation amount in terms of time. |
| `cl_mainmenu_hide_blog` | `clientdll` `hidden` `clientcmd_can_execute` | Show the news panel and hide blog |
| `cl_mainmenu_show_blog` | `clientdll` `hidden` `clientcmd_can_execute` | Show the blog and hide news panel |
| `cl_matchstats_print_own_data` | `developmentonly` `clientdll` `defensive` | cl_matchstats_print_own_data RANGENAME |
| `cl_particles_dump_effects` | `developmentonly` `clientdll` `defensive` |  |
| `cl_particles_dumplist` | `linked_concommand` `developmentonly` `clientdll` `defensive` | Dump all new particles, optional name substring. |
| `cl_particles_dumpsimlist` | `linked_concommand` `developmentonly` `clientdll` `defensive` | Dump all simulating particles, optional name substring. |
| `cl_phys_create_test_character_proxy` | `developmentonly` `clientdll` | Create test character proxy |
| `cl_phys_dump_intersection_controller` | `developmentonly` `clientdll` | Dump intersection controller status |
| `cl_phys_dump_main_world` | `developmentonly` `clientdll` | Dump physics main world to file |
| `cl_phys_dump_memory` | `developmentonly` `clientdll` | Dump memory usage |
| `cl_phys_list` | `developmentonly` `clientdll` | List all physics component contents of every entity in the game;
    -stream [1\|0]         initiate\|terminate streaming to physics debugger
    -allents              include non-physical entities
    -classes              print class names
    -sdk                  Rubikon-wide memory short status
    -sdk -struct          Rubikon-wide memory use per struct
    -sdk -rebuildsvms     Rubikon-wide SVM force rebuild and status
    -world                current state of the world
    -world -touch         list body pairs (bodies in contact)
    -world -save <name>   save world to a file
    -world -mem           memory dump (separately per game dll)
    -world -snapshots     Start/Stop dumping snapshots of the world into the current directory
    -world -agg           current aggregate data registry (loaded resources)
 |
| `cl_phys_sleep` | `developmentonly` `clientdll` | Put all physics in all the worlds to sleep |
| `cl_phys_wakeup` | `developmentonly` `clientdll` | Wake all physics objects in the Main physics up |
| `cl_physics_add_test` | `developmentonly` `clientdll` | add test object |
| `cl_physics_highlight_active` | `developmentonly` `clientdll` | Turns on the absbox for all active physics objects.
  0 : un-highlight.
 |
| `cl_physics_remove_test` | `developmentonly` `clientdll` | remove test object |
| `cl_physics_report_active` | `developmentonly` `clientdll` | Lists all active physics objects
  -more : extra info
 |
| `cl_pred_track` | `developmentonly` `clientdll` `defensive` | <entindex> <fieldname>:  Track changes to entity index entindex, for field fieldname. |
| `cl_pred_track_off` | `developmentonly` `clientdll` `defensive` | clear field track changes. |
| `cl_predictioncopy_describe` | `developmentonly` `clientdll` `defensive` | Describe PredictionMap_t for entindex |
| `cl_predictioncopy_print` | `developmentonly` `clientdll` `defensive` | Print simple description of prediction copy fields for entindex |
| `cl_printfps` | `developmentonly` `clientdll` `defensive` | Print information from cl_showfps. |
| `cl_prop_debug` | `clientdll` `cheat` | Toggle prop debug mode. If on, props will show colorcoded bounding boxes. Red means ignore all damage. White means respond physically to damage but never break. Green maps health in the range of 100 down to 1. |
| `cl_querycache_stats` | `clientdll` `cheat` | Display status of the query cache (client only) |
| `cl_reload_hud` | `developmentonly` `clientdll` `defensive` | Reloads the hud scale and resets scale and borders |
| `cl_removedecals` | `clientdll` `cheat` | Remove the decals from the entity under the crosshair. |
| `cl_report_entities` | `developmentonly` `clientdll` `cheat` | Lists all entities |
| `cl_report_predcopy_overrides` | `developmentonly` `clientdll` `defensive` | Report prediction copy overrides |
| `cl_report_simthinklist` | `developmentonly` `clientdll` | Lists all simulating/thinking entities |
| `cl_report_soundpatch` | `developmentonly` `clientdll` `defensive` | reports client-side sound patch count |
| `cl_resetfps` | `developmentonly` `clientdll` `defensive` | Reset information from cl_showfps. |
| `cl_rr_dump_rules` | `clientdll` `cheat` | Print all response rules |
| `cl_script_add_debug_filter` | `clientdll` `cheat` | Add a filter to the game debug overlay |
| `cl_script_add_watch` | `clientdll` `cheat` | Add a watch to the game debug overlay |
| `cl_script_add_watch_pattern` | `clientdll` `cheat` | Add a watch to the game debug overlay |
| `cl_script_attach_debugger` | `clientdll` `cheat` | Connect the vscript VM to the script debugger |
| `cl_script_clear_watches` | `clientdll` `cheat` | Clear all watches from the game debug overlay |
| `cl_script_debug` | `clientdll` `cheat` | Toggle the in-game script debug features |
| `cl_script_dump_all` | `clientdll` `cheat` | Dump the state of the VM to the console |
| `cl_script_find` | `clientdll` `cheat` | Find a key in the VM  |
| `cl_script_help` | `clientdll` `cheat` | Output help for script functions |
| `cl_script_help2` | `developmentonly` `clientdll` `defensive` | Output help for script functions suitable for auto-completion |
| `cl_script_reload` | `clientdll` `cheat` | Reload scripts |
| `cl_script_reload_code` | `clientdll` `cheat` | Execute a vscript file, replacing existing functions with the functions in the run script |
| `cl_script_reload_entity_code` | `clientdll` `cheat` | Execute all of this entity's VScripts, replacing existing functions with the functions in the run scripts |
| `cl_script_remove_debug_filter` | `clientdll` `cheat` | Remove a filter from the game debug overlay |
| `cl_script_remove_watch` | `clientdll` `cheat` | Remove a watch from the game debug overlay |
| `cl_script_remove_watch_pattern` | `clientdll` `cheat` | Remove a watch from the game debug overlay |
| `cl_script_resurrect_unreachable` | `clientdll` `cheat` | Use the garbage collector to track down reference cycles |
| `cl_script_trace_disable` | `clientdll` `cheat` | Turn off a particular trace output by file or function name |
| `cl_script_trace_disable_all` | `clientdll` `cheat` | Turn off all trace output |
| `cl_script_trace_disable_key` | `clientdll` `cheat` | Turn off a particular trace output by table/instance |
| `cl_script_trace_enable` | `clientdll` `cheat` | Turn on a particular trace output by file or function name |
| `cl_script_trace_enable_all` | `clientdll` `cheat` | Turn on all trace output |
| `cl_script_trace_enable_key` | `clientdll` `cheat` | Turn on a particular trace output by table/instance |
| `cl_showents` | `clientdll` `cheat` | Dump entity list to console. |
| `cl_sim_grenade_trajectory` | `clientdll` `cheat` | Draw trajectory of the deployed grenade if thrown from this position. Takes an optional parameter for how long the drawn trajectory will last. |
| `cl_sos_test_get_opvar` | `clientdll` `cheat` |  |
| `cl_sos_test_set_opvar` | `clientdll` `cheat` |  |
| `cl_soundscape_flush` | `clientdll` `cheat` `server_can_execute` | Flushes the client side soundscapes |
| `cl_soundscape_printdebuginfo` | `developmentonly` `clientdll` `defensive` | print soundscapes |
| `cl_ss_origin` | `developmentonly` `clientdll` `defensive` | print origin in script format |
| `cl_test_list_entities` | `clientdll` `cheat` | test-list entities |
| `cl_updatevisibility` | `developmentonly` `clientdll` `defensive` | Updates visibility bits. |
| `clear_bombs` | `gamedll` `cheat` |  |
| `cli_ent_attachments` | `clientdll` `cheat` | Displays the interpolated attachment points on an entity.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cli_ent_hitbox` | `clientdll` `cheat` | Displays the skeleton for the given entity(ies).
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cli_ent_pivot` | `clientdll` `cheat` | Displays the interpolated pivot for the given entity(ies).
	(y=up=green, z=forward=blue, x=left=red). 
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cli_ent_skeleton` | `clientdll` `cheat` | Displays the skeleton for the given entity(ies).
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `cli_ent_vcollide_wireframe` | `clientdll` `cheat` | Displays the interpolated vcollide wireframe pm am entity.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `clutch_mode_toggle` | `clientdll` `release` | Toggle clutch mode convar |
| `collect_entity_model_name` | `gamedll` `cheat` | Collect model names of the entities you're pointing at |
| `commentary_cvarsnotchanging` | `developmentonly` `gamedll` `defensive` |  |
| `commentary_finishnode` | `gamedll` `client_can_execute` |  |
| `confirm_abandon_match` | `clientdll` `hidden` `clientcmd_can_execute` | Confirm that we wish to abandon match |
| `confirm_activate_itemid_now` | `clientdll` `hidden` `clientcmd_can_execute` | Confirm item activation by item id |
| `confirm_join_friend_session_exit_current` | `clientdll` `hidden` `clientcmd_can_execute` | Confirm that we wish to join a friend session, destroying a previous session |
| `confirm_join_new_session_exit_current` | `clientdll` `hidden` `clientcmd_can_execute` | Confirm that we wish to join a new session, destroying a previous session |
| `confirm_join_party_session_exit_current` | `clientdll` `hidden` `clientcmd_can_execute` | Confirm that we wish to join a party session, destroying a previous session |
| `confirm_watch_friend_session_exit_current` | `clientdll` `hidden` `clientcmd_can_execute` | Confirm that we wish to watch a friend session, destroying a previous session |
| `convert_steamid` | `developmentonly` `clientdll` `defensive` | Convert SteamID into multiple formats |
| `create_radius_damage` | `gamedll` `cheat` | Causes radius damage where you're looking, at the passed in radius. |
| `creditsdone` | `developmentonly` `gamedll` `defensive` |  |
| `cs_quit_prompt` | `clientdll` `release` | Quit the game |
| `csgo_download_match` | `clientdll` `dontrecord` `clientcmd_can_execute` | Downloads a match via serial code and starts playback |
| `csgo_econ_action_preview` | `clientdll` `hidden` `dontrecord` `clientcmd_can_execute` | Preview an economy item |
| `csgo_watch_friend_session_exit_current` | `clientdll` `hidden` `clientcmd_can_execute` |  |
| `cvarlist` | `release` | Show the list of convars/concommands. |
| `dbghist_addline` | `developmentonly` `gamedll` `defensive` | Add a line to the debug history. Format: <category id> <line> |
| `dbghist_dump` | `developmentonly` `gamedll` `defensive` | Dump the debug history to the console. Format: <category id>
    Categories:
     0: Entity I/O
     1: AI Decisions
     2: Scene Print
     3: Alyx Blind
     4: Log of damage done to player
	 5: Player Teleport
	 6: Blind Zombie Sounds
	 7: Player Continuous
 |
| `debug_purchase_defidx` | `clientdll` `release` `clientcmd_can_execute` | Purchase an item by defindex |
| `debugoverlay_cycle_domain` | `gamedll` `cheat` | Toggles visibility of the debug overlay system. |
| `debugoverlay_cycle_state` | `gamedll` `cheat` | Toggles visibility of the debug overlay system. |
| `debugoverlay_dashboard` | `gamedll` `cheat` | Makes the debug overlay dashboard visible. |
| `debugoverlay_hide_imgui` | `gamedll` `cheat` | Hides the overlay. |
| `debugoverlay_toggle` | `gamedll` `cheat` | Toggles visibility of the debug overlay system. |
| `demoui` | `clientdll` `release` | Show/hide demo playback ui |
| `dev_send_gc_message` | `developmentonly` `clientdll` `defensive` | <msgid> Send a blank body message with a given ID to gc for routing tests |
| `dev_send_gc_message_server` | `developmentonly` `gamedll` `defensive` | <msgid> Send a blank body message with a given ID to gc for routing tests |
| `dev_simulate_gcdown` | `developmentonly` `clientdll` `defensive` | <state> Turn on/off simulated GC communications failure (GC is down in a way that we know it is down) |
| `differences` | `release` | Show all convars which are not at their default values (optional restricted to specific flags). |
| `dlight_debug` | `clientdll` `cheat` | Creates a dlight in front of the player |
| `dm_reset_spawns` | `developmentonly` `gamedll` `defensive` |  |
| `dm_togglerandomweapons` | `clientdll` `server_can_execute` `clientcmd_can_execute` | Turns random weapons in deathmatch on/off |
| `drawcross` | `gamedll` `cheat` | Draws a cross at the given location
	Arguments: x y z |
| `drawline` | `gamedll` `cheat` | Draws line between two 3D Points.
	Green if no collision
	Red is collides with something
	Arguments: x1 y1 z1 x2 y2 z2 |
| `drawoverviewmap` | `developmentonly` `clientdll` `defensive` | Draws the overview map |
| `drawradar` | `developmentonly` `clientdll` `defensive` | Draws HUD radar |
| `drop_hostage` | `developmentonly` `gamedll` `cheat` | drop held hostage |
| `ds_workshop_changelevel` | `gamedll` `release` | Changelevel to an available workshop map by name |
| `ds_workshop_listmaps` | `gamedll` `release` | Dump workshop maps available on this server |
| `dump_entity_report` | `clientdll` `cheat` | List all client-side entities in the scene |
| `dump_globals` | `developmentonly` `gamedll` `defensive` | Dump all global entities/states |
| `dump_portrait_world_info_with_debug_name_containing` | `developmentonly` `clientdll` |  |
| `dump_response_symbols` | `developmentonly` `gamedll` `defensive` | print all response symbols to the console |
| `dump_secondary_scene_worlds` | `developmentonly` `clientdll` `defensive` | Lists secondary scene worlds and ref counts |
| `dumpparticlelist` | `cheat` | Print out information on existing particle systems |
| `econ_build_pinboard_images_from_collection_name` | `developmentonly` `clientdll` `defensive` | Renders and saves images for all models in a collection. |
| `econ_clear_inventory_images` | `developmentonly` `clientdll` `defensive` | clear the local inventory images (they will regenerate) |
| `econ_show_items_with_tag` | `developmentonly` `clientdll` `defensive` | Lists the item definitions that have a specified tag. |
| `endmatch_votenextmap` | `clientdll` `clientcmd_can_execute` | Votes for the next map at the end of the match |
| `endround` | `gamedll` `cheat` | End the current round. |
| `ent_absbox` | `gamedll` `cheat` | Displays the total bounding box for the given entity(s) in green.  Some entites will also display entity specific overlays.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_actornames` | `gamedll` `cheat` | Displays the entity name for all entities that have ShouldDisplayInActorNames true in code |
| `ent_animgraph2_open_graph` | `gamedll` `cheat` | Opens the graph and starts live debugging the AG2 graph for a given entity
	Arguments: entityName
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_animgraph2_record` | `gamedll` `cheat` | Starts live debugging & recording the AG2 graph for a given entity
	Arguments: entityName
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_animgraph_debug` | `gamedll` `cheat` | Displays debug draws about the given entity(ies) animgraph
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_attachments` | `gamedll` `cheat` | Displays the attachment points on an entity.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_autoaim` | `gamedll` `cheat` | Displays the entity's autoaim radius.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_bbox` | `gamedll` `cheat` | Displays the movement bounding box for the given entity(ies) in orange.  Some entites will also display entity specific overlays.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_bonemergeplayer` | `gamedll` `cheat` | Bonemerge the player onto the entity under the crosshairs |
| `ent_call` | `gamedll` `cheat` | ent_call <funcname> <option:entname> calls function on current look target or filtername, checks on ent, then root, then mode, then map scope |
| `ent_cancelpendingentfires` | `developmentonly` `gamedll` `defensive` | Cancels all ent_fire created outputs that are currently waiting for their delay to expire. |
| `ent_characterize` | `developmentonly` `gamedll` `defensive` | Spew PVS debug info for entity |
| `ent_clear_debug_overlays` | `gamedll` `cheat` | Clears all debug overlays |
| `ent_create` | `gamedll` `cheat` `vconsole_fuzzy_matching` | Creates an entity of the given designer or subclass name where the player is looking. |
| `ent_debug_anim` | `developmentonly` `clientdll` `defensive` | Use the specified entity for animation debugging. |
| `ent_debug_origin_changes` | `developmentonly` `gamedll` | turn on, off, or toggle origin changes on server for entity by index |
| `ent_find` | `gamedll` `cheat` | Find and list all entities with classnames or targetnames that contain the specified substrings.
Format: find_ent <substring>
 |
| `ent_find_index` | `gamedll` `cheat` | Display data for entity matching specified index.
Format: find_ent_index <index>
 |
| `ent_fire` | `gamedll` `cheat` `vconsole_fuzzy_matching` | Usage:
   ent_fire <target> [action] [value] [delay]
 |
| `ent_fire_output` | `gamedll` `cheat` `vconsole_fuzzy_matching` | Usage:
   ent_fire_output <target> [output name] [value] [delay]
 |
| `ent_gib` | `gamedll` `cheat` | Gibs the given entity(s)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_grab` | `gamedll` `cheat` | grabs the object in front of the player. Options: -loose -multiple -toggle |
| `ent_hierarchy` | `gamedll` `cheat` | Prints the entity hierarchy tree rooted at the specified ent(s) |
| `ent_hitbox` | `gamedll` `cheat` | Displays the hitboxes for the given entity(ies).
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_info` | `gamedll` `cheat` | Usage:
   ent_info <class name>
 |
| `ent_joints` | `gamedll` `cheat` | Displays the joint names + axes an entity.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_kill` | `gamedll` `cheat` | Kills the given entity(s)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_list_report` | `developmentonly` `gamedll` `defensive` | Reports all list of all entities in a map, one by one |
| `ent_messages` | `gamedll` `cheat` | Toggles input/output message display for the selected entity(ies).  The name of the entity will be displayed as well as any messages that it sends or receives.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_name` | `gamedll` `cheat` | Displays the entity name |
| `ent_orient` | `gamedll` `cheat` | Orient the specified entity to match the player's angles. By default, only orients target entity's YAW. Use the 'allangles' option to orient on all axis.
	Format: ent_orient <entity name> <optional: allangles> |
| `ent_picker` | `gamedll` `cheat` | Toggles 'picker' mode.  When picker is on, the bounding box, pivot and debugging text is displayed for whatever entity the player is looking at.
	Arguments:	full - enables all debug information |
| `ent_pivot` | `gamedll` `cheat` | Displays the pivot for the given entity(ies).
	(y=up=green, z=forward=blue, x=left=red). 
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_rbox` | `clientdll` `cheat` | Displays the total bounding box for the given entity(s) in green.  Some entites will also display entity specific overlays.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_remove` | `gamedll` `cheat` | Removes the given entity(s)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_remove_all` | `gamedll` `cheat` | Removes all entities of the specified type
	Arguments:   	{entity_name} / {class_name}  |
| `ent_reveal_in_hammer` | `developmentonly` `gamedll` | Given a mapname and hammer uniqueid, reveal it in Hammer |
| `ent_rotate` | `gamedll` `cheat` | Rotates an entity by a specified # of degrees |
| `ent_scale` | `gamedll` `cheat` | Scales entities.	Arguments: <scale factor> <{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at}> |
| `ent_scenehierarchy` | `gamedll` `cheat` | Prints the entity scenenode hierarchy tree rooted at the specified ent(s) |
| `ent_script_dump` | `gamedll` `cheat` | Dumps the names and values of this entity's script scope to the console
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_select` | `gamedll` `cheat` | Select or deselects the given entities(s) for later manipulation
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_setang` | `gamedll` `cheat` `client_can_execute` | Set entity angles |
| `ent_setname` | `gamedll` `cheat` | Sets the targetname of the given entity(s)
	Arguments:   	<new entity name> <{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at}> |
| `ent_setpos` | `gamedll` `cheat` `client_can_execute` | Move entity to position |
| `ent_show_damage` | `gamedll` `cheat` | Sets damage display mode.  When on, you will see the amount of damage dealt over the target's head. |
| `ent_show_response_criteria` | `gamedll` `cheat` | Print, to the console, an entity's current criteria set used to select responses.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_skeleton` | `gamedll` `cheat` | Displays the skeleton for the given entity(ies).
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_spew_derived_classes` | `developmentonly` `gamedll` | Prints out all entity classes which inherit from a specified base class |
| `ent_teleport` | `gamedll` `cheat` | Teleport the specified entity to where the player is looking.
	Format: ent_teleport <entity name> |
| `ent_text` | `gamedll` `cheat` `vconsole_fuzzy_matching` | Displays text debugging information about the given entity(ies) on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_text256` | `gamedll` `cheat` | Displays text debugging information about the given entity(ies) [within 256 units of the player] on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_text_clear` | `gamedll` `cheat` | Hide text debugging information about the given entity(ies) on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_text_filter` | `gamedll` `cheat` | Set which ent_text filters you want:  |
| `ent_text_radius` | `gamedll` `cheat` | Displays text debugging information about the given entity(ies) [near the player] on top of the entity (See Overlay Text)
	2 Arguments:   	<Radius> <{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at}> |
| `ent_text_sticky_add` | `gamedll` `cheat` | Adds to list of names to display text debugging information about the given entity(ies) on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_text_sticky_clear` | `gamedll` `cheat` | Clears the list of names to display text debugging information about the given entity(ies) on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_text_sticky_dump` | `gamedll` `cheat` | Spews the list of names to display text debugging information about the given entity(ies) on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_text_sticky_remove` | `gamedll` `cheat` | Removes from the list of names to display text debugging information about the given entity(ies) on top of the entity (See Overlay Text)
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_ungrab` | `gamedll` `cheat` | un-grabs all objects |
| `ent_vcollide_wireframe` | `gamedll` `cheat` | Displays the interpolated vcollide wireframe pm am entity.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_viewentity` | `developmentonly` `gamedll` | Selects the picked entity as the view entity |
| `ent_viewoffset` | `gamedll` `cheat` | Displays the eye position for the given entity(ies) in red.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ent_viewpunch` | `developmentonly` `gamedll` | Used to debug ViewPunch |
| `ent_visibility_traces` | `gamedll` `cheat` `vconsole_fuzzy_matching` | Displays visibility traces for the given entity
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `ents` | `developmentonly` `gamedll` `defensive` | List server entities, sorted by spawn group |
| `error_message_explain_pure` | `clientdll` `hidden` `clientcmd_can_execute` | Take user to Steam support article |
| `error_message_explain_unsigned` | `clientdll` `hidden` `clientcmd_can_execute` | Take user to Steam support article |
| `error_message_explain_vac` | `clientdll` `hidden` `clientcmd_can_execute` | Take user to Steam support article |
| `explode` | `gamedll` `cheat` `client_can_execute` | Kills the player with explosive damage |
| `explodevector` | `gamedll` `cheat` `client_can_execute` | Kills a player applying an explosive force. Usage: explodevector <player> <x value> <y value> <z value> |
| `fadein` | `gamedll` `cheat` | fadein {time r g b}: Fades the screen in from black or from the specified color over the given number of seconds. |
| `fadeout` | `gamedll` `cheat` | fadeout {time r g b}: Fades the screen to black or to the specified color over the given number of seconds. |
| `find` | `release` | Find concommands with the specified string in their name/help text. |
| `findflags` | `release` | Find concommands by flags. |
| `firetarget` | `gamedll` `cheat` |  |
| `firstperson` | `clientdll` `release` `execute_per_tick` | Switch to firstperson camera. |
| `func_mover_count` | `gamedll` `cheat` |  |
| `func_mover_enable_debug_all` | `gamedll` `cheat` |  |
| `game_particle_manager_dump_requeue` | `developmentonly` `clientdll` | Dump contents of particle manager requeue |
| `game_particle_manager_list_active` | `developmentonly` `clientdll` | Dump counts of active particles |
| `gameevents_analyze` | `developmentonly` `gamedll` | compare game events across all mods |
| `gameevents_dumptofile` | `developmentonly` `gamedll` | write gameevents keyvalues (sorted by name) to gameevents_<modname>.txt |
| `gameinstructor_dump_open_lessons` | `clientdll` `cheat` | Gives a list of all currently open lessons. |
| `gameinstructor_dump_run_lesson_counts` | `clientdll` `cheat` | Gives a list of lessons that been completed or shown |
| `gameinstructor_reload_lessons` | `developmentonly` `clientdll` `defensive` | Shuts down all open lessons and reloads them from the script file. |
| `gameinstructor_reset_counts` | `developmentonly` `clientdll` | Resets all display and success counts to zero. |
| `gameinstructor_teach_lesson` | `developmentonly` `clientdll` `defensive` | Force a specific lesson to be triggered |
| `gcmd` | `clientdll` `hidden` `clientcmd_can_execute` | Generate a command |
| `generate_null_container` | `linked_concommand` `developmentonly` `defensive` | Generated a nulled out container. |
| `generate_trash_synth` | `linked_concommand` `developmentonly` `defensive` | Args: [Asset directory Path] |
| `getpos` | `clientdll` `cheat` | dump position and angles to the console |
| `getpos_exact` | `clientdll` `cheat` | dump origin and angles to the console |
| `getposcopy` | `clientdll` `cheat` | dump position and angles to the console and clipboard |
| `getposcopy_exact` | `clientdll` `cheat` | dump origin and angles to the console and clipboard |
| `give` | `gamedll` `vconsole_fuzzy_matching` `client_can_execute` | Give item to player.
	Arguments: <item_name> |
| `give_oriented` | `gamedll` `vconsole_fuzzy_matching` `client_can_execute` | Give item oriented to player angles.
	Arguments: <item_name> |
| `givecurrentammo` | `gamedll` `cheat` | Give a supply of ammo for current weapon..
 |
| `global_set` | `gamedll` `cheat` | global_set <globalname> <state>: Sets the state of the given env_global (0 = OFF, 1 = ON, 2 = DEAD). |
| `god` | `gamedll` `cheat` `client_can_execute` | Toggle by default, or 0 to disable and 1 to enable. Player becomes invulnerable. |
| `graphcontroller_dumpparams` | `developmentonly` `gamedll` | Print all anim graph parameters for the specified entity.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `groundlist` | `developmentonly` `gamedll` `cheat` | Display ground entity list <index> |
| `healme` | `gamedll` `cheat` `client_can_execute` | Heals the player.
	Arguments: <health to gain> |
| `help` | `release` | Find help about a convar/concommand. |
| `hideoverviewmap` | `developmentonly` `clientdll` `defensive` | Hides the overview map |
| `hideradar` | `developmentonly` `clientdll` `defensive` | Hides HUD radar |
| `host_workshop_collection` | `gamedll` `release` | Host a workshop map collection as a mapgroup |
| `host_workshop_map` | `gamedll` `release` | Get the latest version of the map and host it on this server. |
| `host_writeconfig_with_prompt` | `clientdll` `release` `server_can_execute` | Write settings if user agrees |
| `hud_reloadscheme` | `developmentonly` `clientdll` `defensive` | Reloads hud layout and animation scripts. |
| `hurtme` | `gamedll` `cheat` `client_can_execute` | Hurts the player.
	Arguments: <health to lose> |
| `hurtthem` | `gamedll` `cheat` `client_can_execute` | Hurts the enemy in front of you.
	Arguments: <health to lose> |
| `ic` | `developmentonly` `clientdll` `defensive` | interp entity count
 |
| `ik_debug_fabrik_backwards_iteration_toggle` | `linked_concommand` `developmentonly` `defensive` |  |
| `ik_debug_fabrik_forwards_iteration_toggle` | `linked_concommand` `developmentonly` `defensive` |  |
| `imgui_cycle_undocked_window_focus` | `developmentonly` `defensive` | Cycles focus between the game window and undocked imgui windows |
| `imgui_debug_entity` | `gamedll` `cheat` | Shows the entity browser, focused on the entity you specify.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `imgui_set_selection` | `gamedll` `cheat` | Sets ImGui selection |
| `imgui_set_status_text` | `gamedll` `cheat` | Sets ImGui header status text |
| `import_csgo_config` | `developmentonly` `clientdll` `defensive` | Imports an existing CS:GO configuration file into CS2 |
| `impulse` | `clientdll` `release` | Triggers impulse command |
| `in_forcebuttonstate` | `developmentonly` `gamedll` `vconsole_fuzzy_matching` | Forces a button to be a particular state - WHEN PROCESSING USERCOMMANDS |
| `in_forceinput` | `developmentonly` `clientdll` `vconsole_fuzzy_matching` | Forces a button to be a particular state -- WHEN SAMPLING INPUT |
| `invnext` | `clientdll` `server_can_execute` |  |
| `invnextselect` | `clientdll` `server_can_execute` |  |
| `invprev` | `clientdll` `server_can_execute` |  |
| `invprevselect` | `clientdll` `server_can_execute` |  |
| `iv_debug` | `developmentonly` `clientdll` `defensive` | Spew interpolated var info for entity. |
| `iv_interp` | `developmentonly` `clientdll` `defensive` | Spew interpolated var info for entity. |
| `iv_off` | `developmentonly` `clientdll` `defensive` | Turn off all interpolation variable spew. |
| `iv_on` | `developmentonly` `clientdll` `defensive` | Spew both interpolated var debug info and history for entity. |
| `kill` | `gamedll` `cheat` `client_can_execute` | Kills the player with generic damage |
| `killvector` | `gamedll` `cheat` `client_can_execute` | Kills a player applying force. Usage: killvector <player> <x value> <y value> <z value> |
| `lastinv` | `clientdll` `server_can_execute` |  |
| `launch_training_map` | `developmentonly` `clientdll` `defensive` |  |
| `launch_warmup_map` | `clientdll` `dontrecord` `clientcmd_can_execute` | Launches warmup map |
| `lightbinner_precompute` | `developmentonly` `defensive` |  |
| `lightbinner_test_computespheresilhouette` | `developmentonly` `defensive` |  |
| `lightbinner_test_computesumsilhouette` | `developmentonly` `defensive` |  |
| `listRecentNPCSpeech` | `developmentonly` `gamedll` `dontrecord` `defensive` | Displays a list of the last 5 lines of speech from NPCs. |
| `listissues` | `gamedll` `client_can_execute` | List all the issues that can be voted on. |
| `localization_quest_item_string_printout` | `developmentonly` `clientdll` `defensive` | localization_quest_item_string_printout |
| `log_color` | `dontrecord` `release` | Set the color of a logging channel. |
| `log_dumpchannels` | `dontrecord` `release` | Dumps information about all logging channels. |
| `log_flags` | `dontrecord` `release` | Set the flags on a logging channel. |
| `log_level` | `dontrecord` `release` | Set the spew level of a logging channel. |
| `log_verbosity` | `dontrecord` `release` | Set the verbosity of a logging channel. |
| `logaddress_add_http` | `gamedll` `unlogged` `release` | Set URI of a listener to receive logs via http post. Wrap URI in double quotes. |
| `logaddress_add_http_delayed` | `gamedll` `unlogged` `release` | Set a delay and URI of a listener to receive logs via http post. Wrap URI in double quotes. |
| `logaddress_del_http` | `gamedll` `unlogged` `release` | Remove http listener by URI. Wrap URI in double quotes. |
| `logaddress_delall_http` | `gamedll` `unlogged` `release` | Remove all http listeners from the dispatch list. |
| `logaddress_list_http` | `gamedll` `unlogged` `release` | List all URIs currently receiving server logs |
| `lrucache_flush` | `developmentonly` `defensive` | Flushes the specified cache |
| `lrucache_reset_stats` | `developmentonly` `defensive` | Resets stats for the specified CUtlLRUCaches (or all if none specified) |
| `lrucache_set_size` | `developmentonly` `defensive` | Sets the specified cache to the specified size |
| `lrucache_stats` | `developmentonly` `defensive` | Spews information about all CUtlLRUCaches |
| `map_enable_portrait_worlds` | `clientdll` `cheat` | Enables/disables portrait worlds |
| `map_setbombradius` | `gamedll` `cheat` | Sets the bomb radius for the map. |
| `map_showbombradius` | `gamedll` `cheat` | Shows bomb radius from the center of each bomb site and planted bomb. |
| `map_showspawnpoints` | `developmentonly` `gamedll` `defensive` | Shows player spawn points (red=invalid). Optionally pass in the duration. |
| `map_workshop` | `clientdll` `release` `vconsole_fuzzy_matching` `vconsole_set_focus` | Launch a workshop map |
| `mapgroup` | `gamedll` `dontrecord` `release` | Specify a map group |
| `markup_group_ent_bbox` | `gamedll` `cheat` | markup_group_ent_bbox <markup_group name> -> toggle ent_bbox for all members of the named markup group |
| `markup_group_ent_text` | `gamedll` `cheat` | markup_group_ent_text <markup_group name> -> toggle ent_text for all members of the named markup group |
| `markup_group_spew` | `gamedll` `cheat` | Spew all current markup groups and their members |
| `mat_debug` | `developmentonly` `clientdll` `defensive` | Sets a mat_fullbright debug visualization mode |
| `matchdraft_debug_sendlog` | `clientdll` `hidden` `dontrecord` `release` `clientcmd_can_execute` | Print debug draft into HTTP log |
| `menuselect` | `clientdll` `clientcmd_can_execute` | menuselect |
| `minimap_create` | `clientdll` `cheat` | Does a bunch of work to create a minimap |
| `mm_queue_draft_show` | `clientdll` `hidden` `clientcmd_can_execute` | Display current draft |
| `mm_queue_show_stats` | `clientdll` `clientcmd_can_execute` | Display global server stats |
| `model_dump_convert_info` | `linked_concommand` `developmentonly` `gamedll` `clientdll` `defensive` | Print model load-time conversion info |
| `movie_fixwave` | `developmentonly` `defensive` | Fixup corrupted .wav file if engine crashed during startmovie/endmovie, etc. |
| `mp_backup_restore_list_files` | `gamedll` `release` | Lists recent backup round files matching the prefix, most recent files first, accepts a numeric parameter to limit the number of files displayed |
| `mp_backup_restore_load_file` | `gamedll` `release` | Loads player cash, KDA, scores and team scores; resets to the next round after the backup |
| `mp_bot_ai_bt_clear_cache` | `gamedll` `release` | Clears the cache for behavior tree files. |
| `mp_debug_timeouts` | `developmentonly` `gamedll` `defensive` | Prints time outs to the console for debugging |
| `mp_disable_autokick` | `gamedll` `release` | Prevents a userid from being auto-kicked |
| `mp_dump_timers` | `developmentonly` `gamedll` `defensive` | Prints round timers to the console for debugging |
| `mp_modify_timeouts` | `gamedll` `release` | mp_modify_timeouts <CT\|T> <N>, e.g., mp_modify ct -1 |
| `mp_pause_match` | `gamedll` `release` | Pause the match in the next freeze time |
| `mp_scrambleteams` | `gamedll` `release` | Scramble the teams and restart the game |
| `mp_swapteams` | `gamedll` `release` | Swap the teams and restart the game |
| `mp_unpause_match` | `gamedll` `release` | Resume the match |
| `mp_warmup_end` | `gamedll` `release` | End warmup immediately. |
| `mp_warmup_start` | `gamedll` `release` | Start warmup. |
| `nav_add_to_selected_set` | `gamedll` `cheat` | Add current area to the selected set. |
| `nav_add_to_selected_set_by_id` | `gamedll` `cheat` | Add specified area id to the selected set. |
| `nav_begin_deselecting` | `gamedll` `cheat` | Start continuously removing from the selected set. |
| `nav_begin_drag_deselecting` | `gamedll` `cheat` | Start dragging a selection area. |
| `nav_begin_drag_selecting` | `gamedll` `cheat` | Start dragging a selection area. |
| `nav_begin_selecting` | `gamedll` `cheat` | Start continuously adding to the selected set. |
| `nav_check_connectivity` | `gamedll` `cheat` | Checks to be sure every (or just the marked) nav area can get to every goal area for the map (hostages or bomb site). |
| `nav_clear_attribute` | `gamedll` `cheat` | Remove given nav attribute from all areas in the selected set. |
| `nav_clear_attributes` | `gamedll` `cheat` | Clear all nav attributes of selected area. |
| `nav_clear_selected_set` | `gamedll` `cheat` | Clear the selected set. |
| `nav_create_indirect_connection` | `gamedll` `cheat` | Create a connection between the selected area and the area pointed at by the crosshair. |
| `nav_create_indirect_connection_from_to` | `gamedll` `cheat` | Create a connection between the current 'from' and 'to' locations. |
| `nav_create_indirect_connection_set_from_using_editpos` | `gamedll` `cheat` | Set the 'from' location of an indirect connection to be the current edit pos of nav_edit. |
| `nav_create_indirect_connection_set_to_using_editpos` | `gamedll` `cheat` | Set the 'to' location of an indirect connection to be the current edit pos of nav_edit. |
| `nav_delete` | `gamedll` `cheat` | Deletes the currently highlighted Area. |
| `nav_end_deselecting` | `gamedll` `cheat` | Stop continuously removing from the selected set. |
| `nav_end_drag_deselecting` | `gamedll` `cheat` | Stop dragging a selection area. |
| `nav_end_drag_selecting` | `gamedll` `cheat` | Stop dragging a selection area. |
| `nav_end_selecting` | `gamedll` `cheat` | Stop continuously adding to the selected set. |
| `nav_list_movable_meshes` | `gamedll` `cheat` | List the movable meshes registered with the movable meshes manager. |
| `nav_lower_drag_volume_max` | `gamedll` `cheat` | Lower the top of the drag select volume. |
| `nav_lower_drag_volume_min` | `gamedll` `cheat` | Lower the bottom of the drag select volume. |
| `nav_mark` | `gamedll` `cheat` | Marks the Area or Ladder under the cursor for manipulation by subsequent editing commands. |
| `nav_mark_attribute` | `gamedll` `cheat` | Set nav attribute for all areas in the selected set. |
| `nav_raise_drag_volume_max` | `gamedll` `cheat` | Raise the top of the drag select volume. |
| `nav_raise_drag_volume_min` | `gamedll` `cheat` | Raise the bottom of the drag select volume. |
| `nav_recall_selected_set` | `gamedll` `cheat` | Re-selects the stored selected set. |
| `nav_remove_from_selected_set` | `gamedll` `cheat` | Remove current area from the selected set. |
| `nav_select_radius` | `gamedll` `cheat` | Adds all areas in a radius to the selection set |
| `nav_select_with_attribute` | `gamedll` `cheat` | Selects areas with the given attribute. |
| `nav_set_movable_mesh_dormant_flag` | `gamedll` `cheat` | Set the movable mesh dormant flag (0=active, 1=dormant) |
| `nav_split` | `gamedll` `cheat` | To split an Area into two, align the split line using your cursor and invoke the split command. |
| `nav_store_selected_set` | `gamedll` `cheat` | Stores the current selected set for later retrieval. |
| `nav_switch` | `developmentonly` `gamedll` `defensive` | Switches to navmesh for the specified spawngroup |
| `nav_test_level_hull` | `gamedll` `cheat` | Find entities that intrude into the nav mesh.  List those entities in console output, and display bounding boxes around them for a while. |
| `nav_test_level_hull_move` | `gamedll` `cheat` |  |
| `nav_toggle_deselecting` | `gamedll` `cheat` | Start or stop continuously removing from the selected set. |
| `nav_toggle_in_selected_set` | `gamedll` `cheat` | Remove current area from the selected set. |
| `nav_toggle_selected_set` | `gamedll` `cheat` | Toggles all areas into/out of the selected set. |
| `nav_toggle_selecting` | `gamedll` `cheat` | Start or stop continuously adding to the selected set. |
| `nav_unmark` | `gamedll` `cheat` | Clears the marked Area or Ladder. |
| `net_reloadgameevents` | `developmentonly` `gamedll` | Reload the game events |
| `noclip` | `gamedll` `cheat` `client_can_execute` | Toggle. Player becomes non-solid and flies.  Optional argument of 0 or 1 to force enable/disable |
| `notarget` | `gamedll` `cheat` `client_can_execute` | Toggle. Player becomes hidden to NPCs. |
| `p2p_ping` | `developmentonly` `clientdll` `defensive` | Ping a peer. |
| `panorama_console_reset_size_and_position` | `linked_concommand` `developmentonly` `clientdll` `hidden` `defensive` | Resets the panorama console to its default size and position |
| `particle_profile` | `developmentonly` `defensive` | Profile particle |
| `particle_profile_spike` | `developmentonly` `defensive` | Profile particle spike |
| `particle_reset_assertions` | `developmentonly` | Causes all single-fire particle assertions to trigger once more. |
| `particle_stop_all` | `developmentonly` `clientdll` `cheat` | Stops all particle systems currently playing |
| `particle_stop_specified` | `developmentonly` `clientdll` `cheat` | Stops all particle systems that match specified name |
| `particle_stop_unspecified` | `developmentonly` `clientdll` `cheat` | Stops all particle systems that don't match specified name |
| `particle_test_create` | `gamedll` `cheat` | Creates the named particle system where the player is looking.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `particle_test_destroy` | `gamedll` `cheat` | Destroys all particle systems matching the specified name.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `particle_test_start` | `gamedll` `cheat` | Dispatches the test particle system with the parameters specified in particle_test_file,
 particle_test_attach_mode and particle_test_attach_param on the entity the player is looking at.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `particle_test_stop` | `gamedll` `cheat` | Stops all particle systems on the selected entities.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `perfectworld_replenish_funds` | `clientdll` `hidden` `clientcmd_can_execute` | Opens Perfect World funds replenishment page for account. |
| `phys_create_test_character_proxy` | `developmentonly` `gamedll` | Create test character proxy |
| `phys_debug_draw` | `developmentonly` `defensive` | Set up debug-draw of physics internal state |
| `phys_dump_intersection_controller` | `developmentonly` `gamedll` | Dump intersection controller status |
| `phys_dump_main_world` | `developmentonly` `gamedll` | Dump physics main world to file |
| `phys_dump_memory` | `developmentonly` `gamedll` | Dump memory usage |
| `phys_list` | `developmentonly` `gamedll` | List all physics component contents of every entity in the game;
    -stream [1\|0]         initiate\|terminate streaming to physics debugger
    -allents              include non-physical entities
    -classes              print class names
    -sdk                  Rubikon-wide memory short status
    -sdk -struct          Rubikon-wide memory use per struct
    -sdk -rebuildsvms     Rubikon-wide SVM force rebuild and status
    -world                current state of the world
    -world -touch         list body pairs (bodies in contact)
    -world -save <name>   save world to a file
    -world -mem           memory dump (separately per game dll)
    -world -snapshots     Start/Stop dumping snapshots of the world into the current directory
    -world -agg           current aggregate data registry (loaded resources)
 |
| `phys_shoot` | `gamedll` `cheat` | Shoots a phys object. |
| `phys_sleep` | `developmentonly` `gamedll` | Put all physics in all the worlds to sleep |
| `phys_wakeup` | `developmentonly` `gamedll` | Wake all physics objects in the Main physics up |
| `physics_add_test` | `developmentonly` `gamedll` | add test object |
| `physics_debug_entity` | `developmentonly` `gamedll` `defensive` | Dumps debug info for an entity |
| `physics_highlight_active` | `developmentonly` `gamedll` | Turns on the absbox for all active physics objects.
  0 : un-highlight.
 |
| `physics_remove_test` | `developmentonly` `gamedll` | remove test object |
| `physics_report_active` | `developmentonly` `gamedll` | Lists all active physics objects
  -more : extra info
 |
| `pixelvis_debug` | `cheat` | Dump debug info |
| `plant_bomb` | `gamedll` `cheat` | Plant a bomb where the player is looking. |
| `play` | `server_can_execute` | Play a sound. |
| `player_ping` | `gamedll` `client_can_execute` | Creates a ping notification where the player is looking. |
| `playsoundscape` | `clientdll` `cheat` | Forces a soundscape to play |
| `playvol` | `developmentonly` `defensive` | Play a sound at a specified volume. |
| `print_mapgroup` | `clientdll` `release` | Prints the current mapgroup and the contained maps |
| `print_mapgroup_sv` | `gamedll` `release` | Prints the current mapgroup and the contained maps |
| `prop_debug` | `gamedll` `cheat` | Toggle prop debug mode. If on, props will show colorcoded bounding boxes. Red means ignore all damage. White means respond physically to damage but never break. Green maps health in the range of 100 down to 1. |
| `prop_dynamic_create` | `gamedll` `cheat` | Creates a dynamic prop with a specific .vmdl aimed away from where the player is looking.
	Arguments: {.vmdl name} |
| `prop_physics_create` | `gamedll` `cheat` | Creates a physics prop with a specific .vmdl aimed away from where the player is looking.
	Arguments: {.vmdl name} |
| `pulse_debug_entity` | `gamedll` `cheat` `vconsole_fuzzy_matching` | Opens a graph referencing the selected entity. If it is referenced by more than 1 graph, list all the active pulse graph instances referring to that entity so you can pick which one you want. |
| `pulse_list_game_blackboards` | `gamedll` `cheat` | List all the active pulse graph instances |
| `radio` | `clientdll` `release` | Opens a radio menu |
| `radio1` | `clientdll` `release` | Opens a radio menu |
| `radio2` | `clientdll` `release` | Opens a radio menu |
| `radio3` | `clientdll` `release` | Opens a radio menu |
| `ragdoll_cleanup_all` | `linked_concommand` `gamedll` `clientdll` `cheat` | Cleans up all ragdolls. |
| `rangefinder` | `gamedll` `cheat` | Measures distance along a ray |
| `rangefinder2d` | `gamedll` `cheat` | Measures distance along a ray, only measuring along XY plane. |
| `ray_bench` | `developmentonly` `gamedll` `defensive` | Load the rays and run the benchmark |
| `rebuy` | `clientdll` `clientcmd_can_execute` | Attempt to repurchase items with the order listed in cl_rebuy |
| `regenerate_weapon_skins` | `clientdll` `cheat` |  |
| `reload_store_config` | `developmentonly` `clientdll` `defensive` |  |
| `remove_weapon` | `gamedll` `cheat` `client_can_execute` | Remove a weapon held by the player.
	Arguments: <weapon subclass name> |
| `replant_bomb` | `gamedll` `cheat` |  |
| `replay_death` | `gamedll` `cheat` | start hltv replay of last death |
| `replay_start` | `gamedll` `cheat` `client_can_execute` | Start Source2 TV replay: replay_start <delay>\|stash [<player name or index>] |
| `replay_stop` | `gamedll` `client_can_execute` | stop hltv replay |
| `report_entities` | `developmentonly` `gamedll` `cheat` | Lists all entities |
| `report_simthinklist` | `developmentonly` `gamedll` | Lists all simulating/thinking entities |
| `report_soundpatch` | `developmentonly` `gamedll` `defensive` | reports sound patch count |
| `respawn_player` | `gamedll` `cheat` | Respawns the player from death!
 |
| `restart_in_insecure` | `clientdll` `hidden` `clientcmd_can_execute` | Restart in insecure mode |
| `restart_in_trusted` | `clientdll` `hidden` `clientcmd_can_execute` | Restart in trusted mode |
| `restart_in_untrusted` | `clientdll` `hidden` `clientcmd_can_execute` | Restart in untrusted mode |
| `restart_normal` | `clientdll` `hidden` `clientcmd_can_execute` | Restart |
| `retake_barrier_clear` | `gamedll` `cheat` |  |
| `retake_barrier_point` | `gamedll` `cheat` |  |
| `retake_barrier_spawn` | `gamedll` `cheat` |  |
| `rr_dump_rules` | `gamedll` `cheat` | Print all response rules |
| `rr_forceconcept` | `gamedll` `cheat` | fire a response concept directly at a given character.
USAGE: rr_forceconcept <target name or index> <concept> "criteria1:value1,criteria2:value2,..."
criteria values are optional.
 |
| `save` | `developmentonly` `gamedll` `dontrecord` `defensive` | Save Game |
| `save_clear_subdirectory` | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `save_finish_async` | `developmentonly` `gamedll` `defensive` |  |
| `save_set_subdirectory` | `developmentonly` `gamedll` `replicated` `defensive` |  |
| `save_showelapsedtime` | `developmentonly` `gamedll` `defensive` | display up-to-date elapsed play time |
| `save_watchclass` | `developmentonly` `gamedll` `defensive` | Restrict spew to entities with matching classname |
| `save_watchentity` | `developmentonly` `gamedll` `defensive` | Restrict spew to entity index |
| `say` | `gamedll` `client_can_execute` | Display player message |
| `say_team` | `gamedll` `client_can_execute` | Display player message to team |
| `sc_dumpworld` | `cheat` | Dump a list of the objects in a sceneworld (Usage: sc_dumpworld <world_index>) |
| `sc_dumpworld3d` | `cheat` | Dump the objects in a sceneworld into a 3d geoview buffer (Usage: sc_dumpworld3d <world_index>) |
| `sc_list_extradata_allocations` | `developmentonly` `defensive` | Prints out the overall extra data allocation counts |
| `sc_listworlds` | `cheat` | List all the active sceneworlds |
| `sc_setclassflags` | `cheat` | Low level command to set the flags byte associated with an object class. sc_SetClassFlags <classname> <value>
 |
| `sc_showclasses` | `cheat` | List the object class names known by scenesystem
 |
| `scene_playvcd` | `gamedll` `cheat` | Play the given VCD as an instanced scripted scene. |
| `script_add_debug_filter` | `gamedll` `cheat` | Add a filter to the game debug overlay |
| `script_add_watch` | `gamedll` `cheat` | Add a watch to the game debug overlay |
| `script_add_watch_pattern` | `gamedll` `cheat` | Add a watch to the game debug overlay |
| `script_attach_debugger` | `gamedll` `cheat` | Connect the vscript VM to the script debugger |
| `script_clear_watches` | `gamedll` `cheat` | Clear all watches from the game debug overlay |
| `script_debug` | `gamedll` `cheat` | Toggle the in-game script debug features |
| `script_dump_all` | `gamedll` `cheat` | Dump the state of the VM to the console |
| `script_find` | `gamedll` `cheat` | Find a key in the VM  |
| `script_help` | `gamedll` `cheat` | Output help for script functions |
| `script_help2` | `developmentonly` `gamedll` `defensive` | Output help for script functions suitable for auto-completion |
| `script_reload` | `gamedll` `cheat` | Reload scripts |
| `script_reload_code` | `gamedll` `cheat` | Execute a vscript file, replacing existing functions with the functions in the run script |
| `script_reload_entity_code` | `gamedll` `cheat` | Execute all of this entity's VScripts, replacing existing functions with the functions in the run scripts |
| `script_remove_debug_filter` | `gamedll` `cheat` | Remove a filter from the game debug overlay |
| `script_remove_watch` | `gamedll` `cheat` | Remove a watch from the game debug overlay |
| `script_remove_watch_pattern` | `gamedll` `cheat` | Remove a watch from the game debug overlay |
| `script_resurrect_unreachable` | `gamedll` `cheat` | Use the garbage collector to track down reference cycles |
| `script_trace_disable` | `gamedll` `cheat` | Turn off a particular trace output by file or function name |
| `script_trace_disable_all` | `gamedll` `cheat` | Turn off all trace output |
| `script_trace_disable_key` | `gamedll` `cheat` | Turn off a particular trace output by table/instance |
| `script_trace_enable` | `gamedll` `cheat` | Turn on a particular trace output by file or function name |
| `script_trace_enable_all` | `gamedll` `cheat` | Turn on all trace output |
| `script_trace_enable_key` | `gamedll` `cheat` | Turn on a particular trace output by table/instance |
| `scrubber` | `developmentonly` `defensive` | Scrub system off - not a dev build |
| `sellbackall` | `clientdll` `clientcmd_can_execute` | Attempt to refund all equipment |
| `send_round_backup_file_list` | `gamedll` `hidden` `release` |  |
| `server_game_time` | `developmentonly` `gamedll` `defensive` | Gives the game time in seconds (server's curtime) |
| `server_snd_cast` | `gamedll` `cheat` | Casts a ray and starts a sound event where the ray hits. The sound event will retrigger periodically. Usage: server_snd_cast <eventname> [<retrigger time>] [<max distance>]. Arguments that are specified will become defaults for the remainder of the session. |
| `server_snd_pos` | `gamedll` `cheat` | Starts a sound event at a given position. The sound event will retrigger periodically. Usage: server_snd_pos <eventname> <retrigger time> <x> <y> <z>. |
| `servervoice_clear` | `developmentonly` `clientdll` `defensive` | servervoice_clear |
| `servervoice_dump` | `developmentonly` `clientdll` `defensive` | servervoice_dump |
| `setang` | `gamedll` `cheat` `client_can_execute` | Snap player eyes to specified pitch yaw <roll:optional> (must have sv_cheats). |
| `setang_exact` | `gamedll` `cheat` `client_can_execute` | Snap player eyes and orientation to specified pitch yaw <roll:optional> (must have sv_cheats). |
| `setmodel` | `gamedll` `cheat` | Changes's player's model |
| `setpos` | `gamedll` `cheat` `client_can_execute` | Move player to specified origin (must have sv_cheats). |
| `setpos_exact` | `gamedll` `cheat` `client_can_execute` | Move player to an exact specified origin (must have sv_cheats). |
| `setpos_player` | `gamedll` `cheat` `client_can_execute` | Move specified player to specified origin (must have sv_cheats). |
| `shake` | `gamedll` `cheat` | Shake the screen. |
| `shake_stop` | `clientdll` `cheat` | Stops all active screen shakes.
 |
| `shake_testpunch` | `clientdll` `cheat` | Test a punch-style screen shake.
 |
| `shatterglass_break` | `gamedll` `cheat` |  |
| `shatterglass_restore` | `gamedll` `cheat` |  |
| `show_loadout_toggle` | `clientdll` `clientcmd_can_execute` | Toggles loadout display |
| `show_untrusted_warning_again` | `clientdll` `hidden` `clientcmd_can_execute` | Show untrusted warning again |
| `showents` | `gamedll` `cheat` | Dump entity list to console. |
| `showtriggers` | `gamedll` `cheat` | Enable or Disable showing trigger entities |
| `showtriggers_toggle` | `gamedll` `cheat` | Displays the movement bounding box for the triggers in orange.  Some entites will also display entity specific overlays.
	Arguments:   	{entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `slot0` | `clientdll` `server_can_execute` |  |
| `slot1` | `clientdll` `server_can_execute` |  |
| `slot10` | `clientdll` `server_can_execute` |  |
| `slot11` | `clientdll` `server_can_execute` |  |
| `slot12` | `clientdll` `server_can_execute` |  |
| `slot13` | `clientdll` `server_can_execute` |  |
| `slot2` | `clientdll` `server_can_execute` |  |
| `slot3` | `clientdll` `server_can_execute` |  |
| `slot4` | `clientdll` `server_can_execute` |  |
| `slot5` | `clientdll` `server_can_execute` |  |
| `slot6` | `clientdll` `server_can_execute` |  |
| `slot7` | `clientdll` `server_can_execute` |  |
| `slot8` | `clientdll` `server_can_execute` |  |
| `slot9` | `clientdll` `server_can_execute` |  |
| `snapto` | `developmentonly` `clientdll` `defensive` |  |
| `snd__beatpattern_stop_track` | `cheat` | Stops the specified track |
| `snd_async_flush` | `developmentonly` `defensive` | Flush all unlocked async audio data |
| `snd_async_showmem` | `developmentonly` `defensive` | Show async memory stats |
| `snd_async_showmem_music` | `developmentonly` `defensive` | Show async memory stats for just non-streamed music |
| `snd_async_showmem_summary` | `developmentonly` `defensive` | Show brief async memory stats |
| `snd_beatpattern_flush` | `cheat` | Purge and reload all beat pattern data and files. |
| `snd_beatpattern_print_activetracks` | `cheat` | List all active tracks |
| `snd_beatpattern_print_patterns` | `cheat` | List all available beat patterns |
| `snd_beatpattern_set_track_bpm` | `cheat` | Sets the tempo of the specified track |
| `snd_beatpattern_set_track_transpose` | `cheat` | Sets the transposition of the specified track |
| `snd_beatpattern_stop_all_tracks` | `cheat` | Stops all currently playing patterns |
| `snd_cast` | `cheat` | Casts a ray and starts a sound event where the ray hits. The sound event will retrigger periodically if cl_snd_cast_retrigger is set. The sound event will clear previous snd_cast events if cl_snd_cast_clear is set. Usage: snd_cast <eventname> [<retrigger time>] [<max distance>]. Arguments that are specified will become defaults for the remainder of the session. |
| `snd_compare_soundevents` | `developmentonly` `cheat` | Compare the compiled and loaded contents of 2 soundevents. |
| `snd_cs_duck_reverb` | `developmentonly` `clientdll` `defensive` | One shot trigger to duck reverb for a few seconds. |
| `snd_front_headphone_position` | `developmentonly` `defensive` | Specifies the position (in degrees) of the virtual front left/right headphones. |
| `snd_front_stereo_speaker_position` | `developmentonly` `defensive` | Specifies the position (in degrees) of the virtual front left/right speakers. |
| `snd_front_surround_speaker_position` | `developmentonly` `defensive` | Specifies the position (in degrees) of the virtual front left/right speakers. |
| `snd_get_physics_surface_properties` | `cheat` | Get physics surface properties for all the materials. |
| `snd_headphone_pan_exponent` | `developmentonly` `defensive` | Specifies the exponent for the pan xfade from phone to phone if the "exp" pan law is being used. |
| `snd_headphone_pan_radial_weight` | `developmentonly` `defensive` | Apply cos(angle) * weight before pan law |
| `snd_list_deferred_soundevents` | `developmentonly` `cheat` | List all current deferred load soundevents |
| `snd_list_soundevents` | `developmentonly` `cheat` | List all available soundevents |
| `snd_list_soundevents_by_stack` | `developmentonly` `cheat` | List all available soundevents using specified stack name |
| `snd_print_current_mixer_mixgroup` | `developmentonly` `defensive` | Get data related to mix group matching string |
| `snd_print_samplers` | `cheat` | List all available samplers |
| `snd_print_soundevent` | `developmentonly` `vconsole_fuzzy_matching` `vconsole_set_focus` | Print the data associated with the specified soundevent. |
| `snd_print_soundevent_default_public_properties` | `developmentonly` `vconsole_fuzzy_matching` `vconsole_set_focus` | Print the default public properties of a specified soundevent. Values do not reflect values set on the soundevent. For that see "snd_print_soundevent" |
| `snd_purge_vsnd_table` | `developmentonly` | Purges the VSnd table |
| `snd_rear_headphone_position` | `developmentonly` `defensive` | Specifies the position  (in degrees) of the virtual rear left/right headphones. |
| `snd_rear_stereo_speaker_position` | `developmentonly` `defensive` | Specifies the position (in degrees) of the virtual rear left/right speakers. |
| `snd_rear_surround_speaker_position` | `developmentonly` `defensive` | Specifies the position (in degrees) of the virtual rear left/right speakers. |
| `snd_refresh_ui_audio_state` | `clientdll` `cheat` | Restores audio DSP state for the UI. |
| `snd_remove_all_soundevents` | `developmentonly` `cheat` | Remove all soundevents |
| `snd_remove_soundevent` | `developmentonly` `cheat` | Remove the specified soundevent |
| `snd_samplers_play_note` | `cheat` | Play a note from a specified sampler |
| `snd_samplers_stop_note` | `cheat` | Stop a note from a specified sampler |
| `snd_set_physics_surface_properties` | `cheat` | Set physics surface properties for materials. Usage: <heuristic #> <commit> |
| `snd_setmixer` | `developmentonly` | Set named Mixgroup of current mixer to mix vol, mute, solo. |
| `snd_setmixlayer` | `developmentonly` | Set named Mixgroup of named mix layer to mix vol, mute, solo. |
| `snd_side_surround_speaker_position` | `developmentonly` `defensive` | Specifies the position (in degrees) of the virtual rear left/right speakers. |
| `snd_sos_cl_soundevent_pause_last` | `developmentonly` `clientdll` `defensive` | Test |
| `snd_sos_cl_soundevent_start` | `developmentonly` `clientdll` `defensive` | Test |
| `snd_sos_cl_soundevent_stop_last` | `developmentonly` `clientdll` `defensive` | Test |
| `snd_sos_cl_soundevent_unpause_last` | `developmentonly` `clientdll` `defensive` | Test |
| `snd_sos_compare_operator_stacks` | `cheat` | Compares 2 operator stacks and spews any errors |
| `snd_sos_flush_operators` | `cheat` | Flush and re-parse the sound operator system |
| `snd_sos_get_operator_field_info` | `cheat` | Currently gets info for a single operator field |
| `snd_sos_pause_soundevent` | `cheat` | Pause the specified soundevent in the list |
| `snd_sos_print_class_sizes` | `cheat` | Prints the sizes of relevant sos classes. |
| `snd_sos_print_field_name_strings` | `cheat` | Prints a list of currently cached field name strings |
| `snd_sos_print_groups` | `cheat` | Prints the current state of the groups system |
| `snd_sos_print_operator_stack` | `cheat` | Prints a master list of currently exposed variables |
| `snd_sos_print_operator_stack_operator` | `cheat` | Prints an operator from a stack |
| `snd_sos_print_operator_stacks` | `cheat` | Prints a list of currently available stacks |
| `snd_sos_print_operators` | `cheat` | Prints a list of currently available operators |
| `snd_sos_print_stack_exec_list` | `cheat` | Prints the current stack execution list |
| `snd_sos_print_strings` | `cheat` | Prints a list of currently cached strings |
| `snd_sos_print_tool_properties` | `cheat` | Prints the current state of tool properties. |
| `snd_sos_resolve_execute_operator` | `cheat` | Resolve the inputs and execute one specified operator from a specified stack |
| `snd_sos_set_operator_field` | `cheat` | Currently sets a single float operator field |
| `snd_sos_set_operator_field_by_guid` | `cheat` | Currently sets a single float operator field |
| `snd_sos_soundevent_profile` | `cheat` | Dump a record of current soundevents and profile data |
| `snd_sos_start_soundevent` | `cheat` | Starts a specified soundevent |
| `snd_sos_start_soundevent_at_pos` | `cheat` | Starts a specified soundevent at the given position |
| `snd_sos_start_stack` | `cheat` | Starts a specified stack via an empty soundevent |
| `snd_sos_stop_all_soundevents` | `cheat` | Stops all soundevents currently on the execution list |
| `snd_sos_stop_soundevent_guid` | `cheat` | Stops a specified soundevent |
| `snd_sos_stop_soundevent_index` | `cheat` | Stops a specified soundevent |
| `snd_sos_stop_track` | `cheat` | Stop the specified track and it's queue. |
| `snd_sos_sv_soundevent_pause_last` | `developmentonly` `gamedll` `defensive` | Test |
| `snd_sos_sv_soundevent_start` | `developmentonly` `gamedll` `defensive` | Test |
| `snd_sos_sv_soundevent_stop_last` | `developmentonly` `gamedll` `defensive` | Test |
| `snd_sos_sv_soundevent_unpause_last` | `developmentonly` `gamedll` `defensive` | Test |
| `snd_sos_sv_test_gender` | `developmentonly` `gamedll` `defensive` | Test |
| `snd_sos_test_soundmessage` | `cheat` | test |
| `snd_sos_unpause_soundevent` | `cheat` | UnPause the first soundevent in the list |
| `snd_soundevent_clear_deferred` | `developmentonly` `cheat` | Clear the list of deferred soundevents for loading. |
| `snd_soundmixer_flush` | `developmentonly` `defensive` | Reload soundmixers.txt file. |
| `snd_soundmixer_list_mix_groups` | `developmentonly` `defensive` | List all mix groups to dev console. |
| `snd_soundmixer_list_mix_layers` | `developmentonly` `defensive` | List all mix layers to dev console. |
| `snd_soundmixer_list_mixers` | `developmentonly` `defensive` | List all mixers to dev console. |
| `snd_soundmixer_set_trigger_factor` | `developmentonly` | Set named mix layer / mix group, trigger amount. |
| `snd_soundmixer_setmixlayer_amount` | `developmentonly` | Set named mix layer mix amount. |
| `snd_steamaudio_display_probes` | `developmentonly` `defensive` | Load all the probes from a file and display probes based on the passed on arguments. |
| `snd_stereo_speaker_pan_exponent` | `developmentonly` `defensive` | Specifies the exponent for the pan xfade from speaker to speaker if the "exp" pan law is being used. |
| `snd_stereo_speaker_pan_radial_weight` | `developmentonly` `defensive` | Apply cos(angle) * weight before pan law |
| `snd_surround_speaker_pan_exponent` | `developmentonly` `defensive` | Specifies the exponent for the pan xfade from speaker to speaker if the "exp" pan law is being used. |
| `snd_surround_speaker_pan_radial_weight` | `developmentonly` `defensive` | Apply cos(angle) * weight before pan law |
| `sndplaydelay` | `developmentonly` `defensive` |  |
| `soundinfo` | `release` | Describe the current sound device with an active voice list. |
| `soundlist` | `developmentonly` `defensive` | List all known sounds. |
| `soundscape_dumpclient` | `clientdll` `cheat` | Dumps the client's soundscape data.
 |
| `soundscape_flush` | `developmentonly` `gamedll` `defensive` | Flushes the server & client side soundscapes |
| `soundsysteminfo` | `developmentonly` `defensive` | Describe the current sound device without an active voice list. |
| `spawnCashStack` | `developmentonly` `gamedll` `cheat` |  |
| `spec_goto` | `clientdll` `clientcmd_can_execute` | Move the spectator camera to a specific location. `spec_goto x y z pitch yaw` |
| `spec_lock_to_current_player` | `developmentonly` `clientdll` | As an observer, lock the spectator target to the currently observed target |
| `spec_mode` | `clientdll` `clientcmd_can_execute` | Set spectator mode |
| `spec_next` | `clientdll` `clientcmd_can_execute` | Spectate next player |
| `spec_player` | `clientdll` `clientcmd_can_execute` | Spectate a player by name or slot |
| `spec_pos` | `clientdll` `cheat` | dump position and angles to the console |
| `spec_prev` | `clientdll` `clientcmd_can_execute` | Spectate previous player |
| `ss_teleport` | `developmentonly` `clientdll` `cheat` | Teleport other splitscreen player to my location. |
| `start_rec_mic` | `linked_concommand` `developmentonly` `defensive` | Start recording to a desired wav. |
| `steamvrevent_quit` | `developmentonly` `gamedll` `hidden` `defensive` | steamvrevent_quit |
| `stop_rec_mic` | `linked_concommand` `developmentonly` `defensive` | Stop recording to a desired wav. |
| `stop_rec_mic_all` | `linked_concommand` `developmentonly` `defensive` | Stop recording all mic streams. |
| `stopsound` | `cheat` |  |
| `stopsoundscape` | `clientdll` `cheat` | Stops all soundscape processing and fades current looping sounds |
| `stopwatch` | `developmentonly` `clientdll` `defensive` | General purpose timer. use 'stopwatch' to toggle or explicitly call 'stopwatch start' and/or 'stopwatch stop'. |
| `subclass_change` | `gamedll` `cheat` `vconsole_fuzzy_matching` | Changes the subclass of the given entity.
	Arguments:   	<new_subclass> {entity_name} / {class_name} / {entity_index} / {no argument = pick what player is looking at} |
| `subclass_create` | `gamedll` `cheat` `vconsole_fuzzy_matching` | Creates an entity of the given subclass where the player is looking. |
| `surfaceprop` | `gamedll` `cheat` | Reports the surface properties at the cursor |
| `sv_annotation_give_weapon` | `gamedll` `hidden` `release` | Give weapon required by annotation |
| `sv_annotation_remove_weapon` | `gamedll` `hidden` `release` | Remove weapon given by annotation |
| `sv_cs_dump_econ_item_stringtable` | `developmentonly` `gamedll` `defensive` | sv_cs_dump_econ_item_stringtable |
| `sv_dev_simulate_gcdown` | `developmentonly` `gamedll` `defensive` | <state> Turn on/off simulated GC communications failure (GC is down in a way that we know it is down) |
| `sv_explode_inferno_at_crosshair` | `developmentonly` `gamedll` `cheat` | explodes molotov(0) or Incendiary (1) at crosshair location with single param |
| `sv_explode_smokegrenade_at_crosshair` | `developmentonly` `gamedll` `cheat` | explodes smoke grenade at crosshair location |
| `sv_game_mode_convars` | `developmentonly` `gamedll` `defensive` | Display the values of the convars for the current game_mode. |
| `sv_kill_smokegrenade` | `developmentonly` `gamedll` `cheat` | kill all smoke grenades |
| `sv_load_forced_client_names_file` | `gamedll` `release` | Loads a file containing SteamID64 names for clients |
| `sv_load_random_client_names_file` | `gamedll` `release` | Loads a file containing random name words for clients |
| `sv_querycache_stats` | `developmentonly` `gamedll` `defensive` | Display status of the query cache (client only) |
| `sv_rethrow_last_grenade` | `gamedll` `cheat` | Emit the last grenade thrown on the server. |
| `sv_soundscape_printdebuginfo` | `gamedll` `cheat` | print soundscapes |
| `sv_throw_decoygrenade` | `developmentonly` `gamedll` `cheat` | throw decoy grenade with parmas. |
| `sv_throw_flashgrenade` | `developmentonly` `gamedll` `cheat` | throw flash grenade with parmas. |
| `sv_throw_hegrenade` | `developmentonly` `gamedll` `cheat` | throw HEgrenade with parmas. |
| `sv_throw_molotov` | `developmentonly` `gamedll` `cheat` | throw molotov grenade with parmas. |
| `sv_throw_smokegrenade` | `developmentonly` `gamedll` `cheat` | throw smoke grenade with parmas. |
| `switchhands` | `clientdll` `release` |  |
| `switchhandsleft` | `clientdll` `release` |  |
| `switchhandsright` | `clientdll` `release` |  |
| `teammenu` | `clientdll` `server_can_execute` | Show team selection window |
| `telemetry_message` | `gamedll` `cheat` | Place a message in the telemetry timeline |
| `telemetry_toggle_timespan` | `gamedll` `cheat` | Starts/stops a timespan with an ever increasing name. |
| `test_dispatcheffect` | `gamedll` `cheat` | Test a clientside dispatch effect.
	Usage: test_dispatcheffect <effect name> <distance away> <flags> <magnitude> <scale>
	Defaults are: <distance 1024> <flags 0> <magnitude 0> <scale 0>
 |
| `test_entity_blocker` | `gamedll` `cheat` | Test command that drops an entity blocker out in front of the player. |
| `test_list_entities` | `gamedll` `cheat` | test-list entities |
| `test_voice_container_nesting` | `linked_concommand` `developmentonly` `defensive` | Test nesting voice containers. |
| `test_voice_containers` | `linked_concommand` `developmentonly` `defensive` | Quick example for how we'd derive traits from voice containers. |
| `thirdperson` | `clientdll` `cheat` `execute_per_tick` | Switch to thirdperson camera. |
| `thirdperson_mayamode` | `clientdll` `cheat` | Switch to thirdperson Maya-like camera controls. |
| `thirdpersonshoulder` | `developmentonly` `clientdll` `defensive` | Switch to thirdperson-shoulder camera. |
| `timeleft` | `gamedll` `client_can_execute` | prints the time remaining in the match |
| `timeout_ct_start` | `gamedll` `release` |  |
| `timeout_terrorist_start` | `gamedll` `release` |  |
| `toggleRdrOpt` | `developmentonly` `clientdll` |  |
| `toggleradarscale` | `clientdll` `release` | Toggles the radar scale |
| `traceattack` | `developmentonly` `gamedll` `defensive` | traceattack damage hitgroup |
| `tv_msg` | `developmentonly` `gamedll` `defensive` | Send a screen message to all clients. |
| `url_execute` | `developmentonly` `clientdll` `defensive` | Executes url-based commands, used for incoming commands from url-based launches when the game's already running. |
| `vmix_debug_list` | `developmentonly` `defensive` | Debug dump the list of available vmix graphs |
| `vmix_input` | `cheat` | Set an input mix value |
| `vmix_output` | `cheat` | Dump main graph control output values |
| `voice_containers_get_instance_args` | `linked_concommand` `developmentonly` `defensive` | Args: [Voice Container Path] |
| `voice_containers_get_instance_params` | `linked_concommand` `developmentonly` `defensive` | Args: [Voice Container Path] |
| `voice_modenable_toggle` | `clientdll` `release` | Toggle the voice_modenable convar. |
| `voice_status_test_toggle` | `developmentonly` `clientdll` | Test voice and status notices |
| `voice_toggle_open_mic` | `clientdll` `release` | Toggles between open-mic and push-to-talk |
| `weapon_switch` | `developmentonly` `gamedll` | Use a particular weapon	
Arguments: <weapon_name> |
| `workshop_annotation_submit` | `clientdll` `release` | Submit annotation to workshop. To update an existing submission add its ID number from the workshop URL as a second argument. |
| `workshop_clear_cloud_save` | `developmentonly` `gamedll` `defensive` | Remove a workshop save from steam cloud. Pass the published file id to delete or 0 to delete the non-workshop addon save. |
| `workshop_dump_cloud_contents` | `developmentonly` `gamedll` `defensive` | Spew contents of steam cloud. |
| `workshop_item_submit` | `clientdll` `hidden` `release` |  |
| `workshop_tournament_item_submit` | `clientdll` `hidden` `release` |  |
