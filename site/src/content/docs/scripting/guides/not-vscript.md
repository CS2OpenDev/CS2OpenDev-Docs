---
title: cs_script vs VScript and Panorama
description: Why CS2 map scripting is neither CS:GO's VScript nor Panorama UI JavaScript, with a migration table from CS:GO.
---

Searches for "CS2 scripting" turn up three different systems. Only one of them is how you script a CS2 map.

| System | Where it runs | Used for in CS2 |
|---|---|---|
| **cs_script** | A server entity, `point_script` ([`CCSPointScriptEntity`](../../../schemas/server/CCSPointScriptEntity/)), running JavaScript that imports `cs_script/point_script` | Map logic. This is the system Valve documents and supports for CS2 maps. |
| **VScript** | CS:GO ran Squirrel scripts through the `vscripts` keyvalue; other Source 2 games use Lua | Nothing that Valve documents for CS2. |
| **Panorama** | The game client's UI framework (XML layouts, CSS, client JavaScript) | The game's own UI. Maps can show layouts through `custom_hud_layout`, but without client-side scripting. |

## About the leftover VScript keys

CS2's entity definitions are layered on Source 2's shared `game/core/base.fgd`. That shared file still gives entities a `vscripts` keyvalue and `RunScriptCode` / `CallScriptFunction` inputs, and it still defines `logic_script`. Hammer shows them, but they come from the shared engine base. Valve's CS2 scripting documentation and `point_script.d.ts` say nothing about a bridge between them and cs_script. To call into a script from map I/O, use `point_script`'s own `RunScriptInput`.

## About Panorama

`custom_hud_layout` takes a Panorama layout (`.vxml`) with its stylesheet (`.vcss`), and the server script changes it through `CustomHudLayout` methods. Valve's declaration file is explicit: "Events and client side scripting are not supported." Your Panorama files are markup and styles only; all the logic stays in cs_script. See [Custom HUD layouts](../custom-hud/).

## Migrating from CS:GO

The left-hand column is what a CS:GO map used. The right-hand column is the closest equivalent in CS2's declaration file. Where the right-hand side says "none", the current API has no equivalent.

| CS:GO (VScript / entities) | CS2 cs_script |
|---|---|
| `vscripts` keyvalue on an entity | A `point_script` entity with its `cs_script` keyvalue |
| `RunScriptCode` / `CallScriptFunction` inputs | `RunScriptInput` with a string parameter, handled by `Instance.OnScriptInput(name, cb)` |
| `EntFire(target, input, value, delay)` | `Instance.EntFireAtName({ name, input, value, delay })`, or `EntFireAtTarget({ target, … })` |
| `Entities.FindByName` / `Entities.FindByClassname` | `Instance.FindEntityByName` / `FindEntitiesByName` / `FindEntityByClass` / `FindEntitiesByClass` |
| `thinkfunction` keyvalue | `Instance.SetThink` + `Instance.SetNextThink`, or `await Instance.Delay(s)` |
| `logic_eventlistener` entity | Typed hooks on `Instance` (`OnRoundStart`, `OnPlayerKill`, …). There is no generic listener, so events without a hook can't be reached. |
| `game_ui` for player input | `CSPlayerPawn.IsInputPressed` / `WasInputJustPressed` / `WasInputJustReleased` with `CSInputs` flags. `game_ui` isn't in the entity definitions Hammer loads for CS2; it survives only in the CS:GO map-import scripts. |
| Cursor-driven UI | `CustomHudLayout.SetInputCaptureEnabled(slot, true)` + `Instance.OnCustomHudClicked` |
| `SendToConsole` / `SendToConsoleServer` | `Console.ClientCommand(playerSlot, cmd)` / `Console.ServerCommand(cmd)` |
| `ScriptGetGameMode` / `ScriptGetGameType` | `Instance.GetGameMode()` / `Instance.GetGameType()`; the numbers are listed on [Game Modes](../../../game-modes/) |
| `ScriptPrintMessageChatAll` | None. `Instance.DebugScreenText` works in dev environments only; use a `custom_hud_layout` for player-facing text |
| Squirrel tables and classes | Standard JavaScript (Valve's `tsconfig.json` targets ES2022), ES modules, `async`/`await` |
