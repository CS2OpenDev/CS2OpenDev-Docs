---
layout: default
title: DebugOverlayBits_t
nav_exclude: true
---

[Schemas](../../schemas.md) / [server](../server.md) / DebugOverlayBits_t

# DebugOverlayBits_t

**Kind:** enum · **Underlying:** `uint64_t` · **Module:** server

## Values

| Name | Value | Description |
|------|-------|-------------|
| `OVERLAY_TEXT_BIT` | 1 | Ent Text — show text debug overlay for this entity |
| `OVERLAY_NAME_BIT` | 2 | Name — show name debug overlay for this entity |
| `OVERLAY_BBOX_BIT` | 4 | Bounding Box — show bounding box overlay for this entity |
| `OVERLAY_PIVOT_BIT` | 8 | Pivot — show pivot for this entity |
| `OVERLAY_MESSAGE_BIT` | 16 | Message — TODO show messages for this entity |
| `OVERLAY_ABSBOX_BIT` | 32 | ABS BBox — show abs bounding box overlay |
| `OVERLAY_RBOX_BIT` | 64 | RBox — show the rbox overlay |
| `OVERLAY_SHOW_BLOCKSLOS` | 128 | Entities That Block LOS — TODO show entities that block NPC LOS |
| `OVERLAY_ATTACHMENTS_BIT` | 256 | Attachment Points — show attachment points |
| `OVERLAY_INTERPOLATED_ATTACHMENTS_BIT` | 512 | Interpolated Attachment Points — show interpolated attachment points |
| `OVERLAY_INTERPOLATED_PIVOT_BIT` | 1024 | Interpolated Pivot — show interpolated pivot for this entity |
| `OVERLAY_SKELETON_BIT` | 2048 | Skeleton — show skeleton for this entity |
| `OVERLAY_INTERPOLATED_SKELETON_BIT` | 4096 | Interpolated Skeleton — show interpolated skeleton |
| `OVERLAY_TRIGGER_BOUNDS_BIT` | 8192 | Trigger Bounds — show trigger bounds |
| `OVERLAY_HITBOX_BIT` | 16384 | Hitboxes — show hitboxes for this entity |
| `OVERLAY_INTERPOLATED_HITBOX_BIT` | 32768 | Interpolated Hitboxes — show interpolated hitboxes |
| `OVERLAY_AUTOAIM_BIT` | 65536 | Autoaim Radius — TODO Display autoaim radius |
| `OVERLAY_NPC_SELECTED_BIT` | 131072 | NPC Selected — TODO the npc is current selected SOURCE2_UNSUPPORTED? |
| `OVERLAY_JOINT_INFO_BIT` | 262144 | Joint Info — hows joint info for this entity |
| `OVERLAY_NPC_ROUTE_BIT` | 524288 | NPC Route — draw the route for this npc |
| `OVERLAY_VISIBILITY_TRACES_BIT` | 1048576 |  |
| `OVERLAY_NPC_ENEMIES_BIT` | 4194304 | NPC Enemies — show npc's enemies |
| `OVERLAY_NPC_CONDITIONS_BIT` | 8388608 | NPC Conditions — show NPC's current conditions |
| `OVERLAY_NPC_COMBAT_BIT` | 16777216 | NPC Combat — show npc combat related information (squads/slots/etc) |
| `OVERLAY_NPC_TASK_BIT` | 33554432 | NPC Schedule Tasks — show npc schedule task details |
| `OVERLAY_NPC_BODYLOCATIONS` | 67108864 | NPC Body Locations — show npc body locations |
| `OVERLAY_NPC_VIEWCONE_BIT` | 134217728 | NPC View Cone — show npc's viewcone |
| `OVERLAY_NPC_KILL_BIT` | 268435456 | NPC Kill — kill the NPC, running all appropriate AI. |
| `OVERLAY_BUDDHA_MODE` | 1073741824 | Buddha Mode — TODO take damage but don't die |
| `OVERLAY_NPC_STEERING_REGULATIONS` | 2147483648 | NPC Steering — Show the steering regulations associated with the NPC |
| `OVERLAY_NPC_TASK_TEXT_BIT` | 4294967296 | NPC Task Console Text — show task and schedule names when they start |
| `OVERLAY_PROP_DEBUG` | 8589934592 | Prop Debug — Show prop health and bounds |
| `OVERLAY_NPC_RELATION_BIT` | 17179869184 | NPC Relationships — show relationships between target and all children |
| `OVERLAY_VIEWOFFSET` | 34359738368 | View Offset — TODO show view offset |
| `OVERLAY_VCOLLIDE_WIREFRAME_BIT` | 68719476736 | Collision Wireframe — show collision wireframe |
| `OVERLAY_NPC_SCRIPTED_COMMANDS_BIT` | 137438953472 | NPC Scripted Commands — show the state of scripted commands |
| `OVERLAY_ACTORNAME_BIT` | 274877906944 | Actor Name — show fancy actor name over head of actors (entities which return ShouldDisplayInActorNames() == true) |
| `OVERLAY_NPC_CONDITIONS_TEXT_BIT` | 549755813888 | NPC Gather Conditions — show condition gathering text info |
| `OVERLAY_NPC_ABILITY_RANGE_DEBUG_BIT` | 1099511627776 | NPC Ability Ranges — draw range indicators for all abilities on the NPC |
| `OVERLAY_MINIMAL_TEXT` | 2199023255552 | Minimal Text — Only draw the base name and subclass, but no other text data |
| `OVERLAY_NPC_GOD_MODE` | 4398046511104 | NPC God Mode — This NPC will take no damage or react to it |
| `OVERLAY_NPC_ANIM_AI_HANDSHAKES_BIT` | 8796093022208 | NPC Anim AI Handshakes — show handshaking between AI and Animgraphs |
| `OVERLAY_NPC_PATH_QUERIES_BIT` | 17592186044416 | NPC Path Queries — show path query processing |
