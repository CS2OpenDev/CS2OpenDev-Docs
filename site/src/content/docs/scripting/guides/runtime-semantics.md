---
title: cs_script runtime semantics
description: Lifecycle, timing, tools-mode reloads, damage hooks, save data and the other behaviour Valve documents in point_script.d.ts.
---

This page collects the runtime rules that are easy to miss in the declaration file. Unless a point is marked as community-reported, it is stated in Valve's `point_script.d.ts` for the current build.

## Lifecycle

- The top-level code of a script runs once, when its `point_script` entity spawns.
- `Instance.OnActivate` runs when the entity activates.
- Each `point_script` in the map runs in isolation, with its own `Instance`, its own globals and its own set of entity objects. Two scripts don't share state just because they're in the same map.

## Entity objects

- Entity objects are stable. Two variables that refer to the same entity are `===`, and properties you attach to an entity object are still there the next time you fetch it.
- An entity can be deleted while you hold it. Check `IsValid()` before using a reference you've kept across ticks.
- Lookups return typed subclasses where the API has one. Narrow with `instanceof`:

```js
const ent = Instance.FindEntityByName("prop");
if (ent instanceof BaseModelEntity) ent.Glow({ r: 255, g: 0, b: 0 });
```

The typed classes are `Entity`, `BaseModelEntity`, `CSWeaponBase`, `C4`, `CSGrenadeProjectileBase`, `CSPlantedC4`, `CSHostage`, `CSRadarPoint`, `CSObservablePoint`, `CSPlayerController`, `CSObserverPawn`, `CSPlayerPawn`, `CustomHudLayout`, `PointTemplate` and `CustomPlayerCamera`. Every other entity is a plain `Entity`, and you reach its behaviour through I/O.

## Timing

| API | Behaviour |
|---|---|
| `Instance.SetThink(cb)` + `Instance.SetNextThink(time)` | Sets the script's think callback. `SetNextThink` takes an absolute game time (`Instance.GetGameTime()` plus a delay), and the callback runs on the tick nearest that time, which can be early or late. Re-arm it from inside the callback to keep it running. |
| `await Instance.Delay(seconds)` | A promise that resolves on the tick nearest the delay. |
| `Instance.QueueAfterThinks(cb)` | Runs once, after every entity has thought this tick (player input handled, projectiles moved). Use it when the world needs to be in a consistent state. Valve's demo applies a velocity change from a damage callback this way. Callbacks queued from inside one still run in the same tick. |

Nothing is exact to the millisecond. Everything snaps to ticks.

## Events

- Events are typed hooks on `Instance`, such as `OnRoundStart`, `OnPlayerKill`, `OnBombPlant`, `OnGunFire` and `OnCustomHudClicked`. There is **no generic game-event listener**. An earlier `Instance.OnGameEvent` was removed, so any event without a hook can't be reached from script.
- `OnModifyPlayerDamage` runs before armour and health are applied, after hitgroup multipliers. Return `{ damage }` to change the amount, `{ damageFlags: event.damageFlags | CSDamageFlags.IGNORE_ARMOR }` to pierce armour, or `{ abort: true }` to cancel. It doesn't fire when the player would take no damage at all (frozen, invulnerable, or friendly fire off). `OnPlayerDamage` fires afterwards, with the health actually lost.
- `OnBulletImpact` fires for every impact of a bullet, penetrations included, before any player damage event for that bullet. `OnGunFire` fires once per shot, even when a shotgun fires several pellets.
- In damage events, `weapon` is absent for grenades, because the weapon entity is often gone by the time the projectile explodes.
- **Community-reported:** each hook and `SetThink` appear to hold a single callback, so libraries that need several listeners multiplex behind one. The declaration file doesn't say either way; see [typestrikelib's notes](https://github.com/marKEYfrfx/typestrikelib).

## Tools-mode reload

In tools mode, saving the script recompiles it, clears every registered callback and re-runs the top-level code. **Globals and entity objects survive the reload.** That makes iteration fast, but it also means an old closure stored on a global or on an entity can keep running code from the previous version of your script. This only matters in tools mode.

`Instance.OnScriptReload({ before, after })` handles the edge cases. `before` runs before teardown, and whatever it returns is passed to `after` once the new code has been evaluated:

```js
let mode = "idle";

Instance.OnScriptReload({
    before: () => ({ mode }),
    after: (memory) => { mode = memory.mode; Instance.SetNextThink(Instance.GetGameTime()); },
});
```

## Save data

`Instance.SetSaveData(string)` and `Instance.GetSaveData()` store one string per **workshop addon**. Writes go to disk synchronously on every call, and the first read is a synchronous disk read, so batch writes rather than calling it every tick.

## Console and ConVars

- `Console.Log` writes to the console. It replaces the deprecated `Instance.Msg`.
- `Console.GetConvarBoolean/Number/String/Vector/QAngle/Color` return `undefined` if the convar doesn't exist. Use the getter that matches the convar's value type; the [ConVars reference](../../../convars/) lists every convar's type.
- `Console.RegisterCheatCommand(name, cb)` adds a console command that only works while `sv_cheats` is on.
- `Console.ServerCommand` and `Console.ClientCommand(playerSlot, cmd)` issue commands.

## Dev-only and experimental

- `Instance.DebugScreenText`, `DebugLine`, `DebugSphere` and `DebugBox` only work in development environments, so don't build gameplay on them.
- `Instance.Precache`, `CustomHudLayout` and `CustomPlayerCamera` are marked `@experimental` and may change in breaking ways.
- Several methods are `@deprecated`, including `Instance.Msg`, `ServerCommand`, `IsWarmupPeriod` and `AddTeamMoney` on `Instance`; their replacements are now on `Console` and `GameRules`. Older positional overloads of `EntFireAtName`, `Teleport` and the `Debug*` methods are deprecated too, in favour of the config-object forms.

## Precaching

Models, particles, materials and sounds referenced at runtime can hitch the first time they load. `Instance.Precache({ resources: [...] })` (supporting `.vmdl`, `.vpcf`, `.vmat` and `.vsnd`) loads them on the server and clients ahead of time, and returns a handle you can poll:

```js
const handle = Instance.Precache({ resources: [model] });
while (handle && !handle.IsLoadedForAll()) await Instance.Delay(0);
```
