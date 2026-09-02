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

**Total events:** 8

| Source | Events | Description |
|--------|--------|-------------|
| `core.gameevents` | 2 | Core Engine Events |
| `game.gameevents` | 1 | Game Events |
| `mod.gameevents` | 5 | CS2 (Counter-Strike) Events |

## Event Index

| Event | Source | Fields | Description |
|-------|--------|--------|-------------|
| [player_death](#player_death-coregameevents) | `core.gameevents` | 2 | Fired when a player dies.  Carries `userid` (the victim) and `attacker`.  Detailed kill information (weapon, headshot, assister, penetration count, no-scope flag, distance) lives on the legacy `cs_gameevents.proto` user-message `CMsgSource1LegacyGameEvent` payload — extract those keys when parsing demos. |
| [round_end](#round_end-coregameevents) | `core.gameevents` | 4 | Fired when a round concludes.  Carries the winning team (`winner`), the reason for the win (`reason`, see RoundEndReason table below), and a human-readable `message` string. |
| [round_end](#round_end-gamegameevents) | `game.gameevents` | 4 | Fired when a round concludes.  Carries the winning team (`winner`), the reason for the win (`reason`, see RoundEndReason table below), and a human-readable `message` string. |
| [bomb_planted](#bomb_planted) | `mod.gameevents` | 3 | Fired when the C4 is successfully armed.  `site` is the bombsite index (0=A, 1=B).  At this point a `CPlantedC4` entity exists and the 40-second countdown begins. |
| [player_death](#player_death-modgameevents) | `mod.gameevents` | 22 | Fired when a player dies.  Carries `userid` (the victim) and `attacker`.  Detailed kill information (weapon, headshot, assister, penetration count, no-scope flag, distance) lives on the legacy `cs_gameevents.proto` user-message `CMsgSource1LegacyGameEvent` payload — extract those keys when parsing demos. |
| [player_jump](#player_jump) | `mod.gameevents` | 1 |  |
| [round_end](#round_end-modgameevents) | `mod.gameevents` | 6 | Fired when a round concludes.  Carries the winning team (`winner`), the reason for the win (`reason`, see RoundEndReason table below), and a human-readable `message` string. |
| [weapon_fire](#weapon_fire) | `mod.gameevents` | 3 | Fired each time a player pulls the trigger and a shot is taken. `weapon` is the lowercase classname (`ak47`, `awp`, `knife`, `hegrenade`, …).  Use `bullet_damage` for the *hit* event counterpart. |

---

## Core Engine Events

*Source: `core.gameevents`*

### player_death (core.gameevents)

Fired when a player dies.  Carries `userid` (the victim) and `attacker`.  Detailed kill information (weapon, headshot, assister, penetration count, no-scope flag, distance) lives on the legacy `cs_gameevents.proto` user-message `CMsgSource1LegacyGameEvent` payload — extract those keys when parsing demos.

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | user ID who died |
| `attacker` | `player_controller_and_pawn` | user ID who killed |

### round_end (core.gameevents)

Fired when a round concludes.  Carries the winning team (`winner`), the reason for the win (`reason`, see RoundEndReason table below), and a human-readable `message` string.

> 📝 The `winner` value uses the same team-number scheme as the `Team` constant in `well_known_constants.json` (2=T, 3=CT, 0/1 for draw / unassigned).  The `reason` byte enumerates win conditions: bomb detonation, defusal, time expiry, eliminations, surrender, etc. — full mapping is in `public/cstrike15_gameconstants.h` upstream.

| Field | Type | Description |
|-------|------|-------------|
| `winner` | `byte` | winner team/user i |
| `reason` | `byte` | reson why team won |
| `message` | `string` | end round message |
| `time` | `float` |  |

## Game Events

*Source: `game.gameevents`*

### round_end (game.gameevents)

Fired when a round concludes.  Carries the winning team (`winner`), the reason for the win (`reason`, see RoundEndReason table below), and a human-readable `message` string.

> 📝 The `winner` value uses the same team-number scheme as the `Team` constant in `well_known_constants.json` (2=T, 3=CT, 0/1 for draw / unassigned).  The `reason` byte enumerates win conditions: bomb detonation, defusal, time expiry, eliminations, surrender, etc. — full mapping is in `public/cstrike15_gameconstants.h` upstream.

| Field | Type | Description |
|-------|------|-------------|
| `winner` | `byte` | winner team/user i |
| `reason` | `byte` | reson why team won |
| `message` | `string` | end round message |
| `legacy` | `byte` | server-generated legacy value |

## CS2 (Counter-Strike) Events

*Source: `mod.gameevents`*

### bomb_planted

Fired when the C4 is successfully armed.  `site` is the bombsite index (0=A, 1=B).  At this point a `CPlantedC4` entity exists and the 40-second countdown begins.

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` | player who planted the bomb |
| `site` | `short` | bombsite index |
| `c4` | `short` |  |

### player_death (mod.gameevents)

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

### player_jump

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller` |  |

### round_end (mod.gameevents)

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

### weapon_fire

Fired each time a player pulls the trigger and a shot is taken. `weapon` is the lowercase classname (`ak47`, `awp`, `knife`, `hegrenade`, …).  Use `bullet_damage` for the *hit* event counterpart.

| Field | Type | Description |
|-------|------|-------------|
| `userid` | `player_controller_and_pawn` |  |
| `weapon` | `string` | weapon name used |
| `silenced` | `bool` | is weapon silenced |
