---
title: Getting started with cs_script
description: How CS2 map scripts are attached, loaded and wired to the map, from Valve's shipped point_script.d.ts and the cs_script_demo addon.
---

Counter-Strike 2 map scripts are JavaScript files run by a `point_script` entity. Valve calls the system **cs_script**. Everything on this page comes from files Valve ships with the CS2 Workshop Tools: the declaration file `point_script.d.ts`, its `tsconfig.json`, the `cs_script_demo` example addon, and the entity definitions in `game/csgo/csgo.fgd`. Where the community knows more than those files say, the page links out instead of guessing.

## The pieces

| Piece | What it is |
|---|---|
| `point_script` entity | The map entity that runs a script. It has two keyvalues, `targetname` and `cs_script` (a `resource:vjs` asset reference), and one input, `RunScriptInput(string)`. On the server it is [`CCSPointScriptEntity`](../../../schemas/server/CCSPointScriptEntity/). |
| Your `.js` file | An ES module that imports from `"cs_script/point_script"`. The resource compiler turns it into a `.vjs_c` that loads with the map. |
| `cs_script/point_script` | The module the game provides. It exports three objects: `Instance` (events, entities, traces, timing), `Console` (logging, ConVars, console commands) and `GameRules` (warmup, rounds, score, team money), plus the entity classes and enums. |
| `point_script.d.ts` + `tsconfig.json` | The API as a TypeScript declaration file, shipped at `content/csgo_addons/cs_script_demo/maps/scripts/` in your CS2 install. Valve says it will keep both files current as the API changes. |

## Minimal script

```js
import { Instance, Console } from "cs_script/point_script";

Console.Log("Hello cs_script!");

Instance.OnPlayerJump(({ player }) => {
    Console.Log(`${player.GetPlayerController()?.GetPlayerName()} jumped`);
});
```

1. Put the file in your addon. The demo addon keeps its scripts under `maps/scripts/`.
2. Add a `point_script` entity to the map in Hammer and give it a name.
3. Point its `cs_script` property at your script as a vjs asset.

## How a script runs

- The compiled script loads during map load.
- When the `point_script` entity spawns, the top-level code of the script runs once.
- Everything after that happens through callbacks you register on `Instance`, such as `Instance.OnActivate`, `Instance.OnRoundStart` and `Instance.OnPlayerKill`.
- A map can contain several `point_script` entities. Each runs its own script with its own `Instance`, its own globals and its own entity objects.

The [runtime semantics](../runtime-semantics/) guide covers timing, reloads and the other rules in detail.

## Editor support

Copy `point_script.d.ts` and `tsconfig.json` from the demo addon into the folder that holds your scripts. Editors that understand TypeScript projects, such as VS Code, then give you completion and type checking on plain JavaScript without any further setup. Valve's `tsconfig.json` is:

```json
{
    "compilerOptions": {
        "strict": true,
        "target": "es2022",
        "checkJs": true,
        "noEmit": true
    }
}
```

`target: es2022` is the JavaScript version Valve says CS2 currently runs. `checkJs` means JSDoc annotations are type-checked, which is how the demo scripts narrow types:

```js
/** @type {CSPlayerPawn | undefined} */
let tracked = undefined;
```

Copy the declaration file again after each game update. It changes often, and an old copy will happily autocomplete methods that have been removed. The [changelog](../../../changelog/) lists per-build API changes once SchemaTracker publishes them.

If you'd rather write TypeScript and compile it to JavaScript, the community maintains templates and tooling for that; see [Community resources](#community-resources).

## Talking to the map

Scripts and map logic drive each other through entity I/O.

**Map to script.** Fire `RunScriptInput` at the `point_script` with a string parameter, and register a handler for that string:

```js
// Hammer output on a trigger: OnStartTouch → my_script → RunScriptInput → ResetAndCleanUp
Instance.OnScriptInput("ResetAndCleanUp", ({ caller, activator }) => {
    // caller and activator are the entities from the I/O event, when present
});
```

**Script to map.** Fire inputs on named entities or on an entity you already hold. Valve's demo map passes wildcard names such as `"cover.*"`:

```js
Instance.EntFireAtName({ name: "relay.start_countdown", input: "Trigger", delay: 3 });
Instance.EntFireAtName({ name: "cover.*", input: "Enable" });
```

**Listening to map outputs.** Connect a callback to any entity output:

```js
const button = Instance.FindEntityByName("my_button");
if (button) {
    const id = Instance.ConnectOutput(button, "OnPressed", ({ activator }) => { /* … */ });
    // later: Instance.DisconnectOutput(id)
}
```

Input and output names are plain strings in the declaration file, so a typo fails silently at runtime. The valid inputs and outputs for each entity class come from the game's FGD files; this site will publish them as a typed reference.

## Community resources

These are community projects, not Valve's, and we don't control what they publish:

- [Source2Wiki cs_script section](https://www.source2.wiki/Scripting/Counter-Strike%202/cs_script/introduction): prose docs and examples, regenerated when the game updates.
- [Source2ZE/cs_script](https://github.com/Source2ZE/cs_script): the `@s2ze/*` npm packages (repackaged types, a scheduler, maths helpers) and the `create-cs-script` scaffolder.
- [Source2ZE/cs_script_boilerplate](https://github.com/Source2ZE/cs_script_boilerplate): a TypeScript and Rollup starter project.

Valve asks for feedback at `CSGOTeamFeedback@valvesoftware.com` with "cs_script Feedback" in the subject line.
