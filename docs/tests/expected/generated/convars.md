---
title: ConVars
---

# ConVar Reference

> Source: **Build 9000001** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

All console variables extracted from CS2, with the value type and the bounds the engine enforces where it declares them.

| Name | Type | Default | Range | Flags | Description |
|------|------|---------|-------|-------|-------------|
| `bot_prefix` | `String` |  |  | `gamedll` `release` | This string is prefixed to the name of all bots that join the game.<br>&lt;difficulty&gt; will be replaced with the bot's difficulty.<br>&lt;weaponclass&gt; will be replaced with the bot's desired weapon class.<br>&lt;skill&gt; will be replaced with a 0-100 representation of the bot's skill. |
| `mp_roundtime` | `Float32` | `5.000000` | `0.100000 .. 60.000000` | `gamedll` `notify` `replicated` `release` `commandline_enforced` | How many minutes each round takes. |
| `sv_cheats` | `Bool` | `false` |  | `notify` `replicated` `release` | Allow cheats on server |
| `mp_friendlyfire` | `Bool` | `false` |  | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | Allows team members to injure other members of their team |
| `cl_showfps` | `Int32` | `0` |  | `clientdll` `release` | Draw fps meter at top of screen (1 = fps, 2 = smooth fps, 3 = server MS, 4 = Show FPS and Log to file ) |
| `mp_maxrounds` | `Int32` | `0` | `>= 0` | `gamedll` `clientdll` `notify` `replicated` `release` `commandline_enforced` | max number of rounds to play before server changes maps |
| `host_timescale` | `Float32` | `1.000000` |  | `replicated` `cheat` | Prescale the clock by this amount. |
| `sv_gravity` | `Float32` | `800.000000` |  | `gamedll` `clientdll` `notify` `replicated` `release` | World gravity. |
| `mp_retake_ct_loadout_default_pistol_round` | `String` | `1&#124;3;#GameUI_Retake_Card_4v3,1,0,secondary0&#124;1;#GameUI_Retake_Card_FlashOut,0,0,secondary0,grenade0;#GameUI_Retake_Card_HideAndPeek,0,0,secondary0,grenade1` |  | `gamedll` `clientdll` `replicated` `release` `commandline_enforced` | CT Loadouts for default pistol round when playing bomb site retake. |
