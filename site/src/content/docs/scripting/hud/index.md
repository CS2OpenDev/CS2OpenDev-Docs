---
title: Scripting HUD
description: Showing custom Panorama UI from a CS2 map script with custom_hud_layout, its supported panels, CSS hooks and the CustomHudLayout API.
---

`custom_hud_layout` is how a scripted map shows its own UI. The entity loads a Panorama layout, and the server script toggles CSS classes, sets text and captures the cursor. Valve marks the feature `@experimental`, so expect breaking changes.

## Setup

1. Add a Panorama layout `.xml` under `panorama/layout/custom_game/` in your addon. Its stylesheet goes under `panorama/styles/custom_game/`. The layout includes the stylesheet by its `.css` source path, and the compiled file is `.vcss_c`.
2. Add a `custom_hud_layout` point entity to the map, give it a name, and set its `layout` property to the layout's `.vxml` asset.
3. Optionally set `observable`. When it's on, whoever is spectating a player sees that player's version of the UI.
4. In your script, find the entity, which comes back as a `CustomHudLayout`, and drive it.

## What a layout may contain

| Element | Supported attributes |
|---|---|
| `<Panel>` | `id`, `class`, `hittest` |
| `<Label>` | `id`, `class`, `hittest`, `text` |
| `<Image>` | `id`, `class`, `hittest`, `src` |
| `<Button>` | `id`, `class` |

CSS styling works. Events and client-side scripting don't: a layout is markup and styles only.

A layout pulls in its stylesheet with `<styles><include src="file://{resources}/styles/custom_game/<name>.css" /></styles>` at the top of `<root>`, as Valve's demo does. Community projects show a dialog variable in a Label with `text="{s:<variable>}"` and set it from the script with the Label's `id` and the variable name. Valve's demo doesn't use this syntax. [HUD gotchas](./gotchas/) lists what else Panorama accepts and rejects, and [HUD examples](./examples/) points to complete layouts in community projects.

While the matching game UI is showing, the game sets these classes on an ancestor panel, so your CSS can hide or move things out of the way:

`HUD_TEAMINTRO_VISIBLE`, `HUD_BUYMENU_VISIBLE`, `HUD_SCOREBOARD_VISIBLE`, `HUD_WINPANEL_VISIBLE`, `HUD_ENDOFMATCH_VISIBLE`, `HUD_TEAMMENU_VISIBLE`, `HUD_CHAT_VISIBLE`

## Driving it from script

| Method | Effect |
|---|---|
| `SetHasClass(panelId, className, hasClass?)` | Adds or removes a class for every player. Omit `hasClass` to revert to the layout's original value. |
| `SetHasClassForPlayer(slot, panelId, className, hasClass?)` | Overrides the class for one player. Omit `hasClass` to fall back to the all-player value. |
| `SetDialogVariableString(panelId, name, value)` | Sets a Panorama dialog variable for everyone. |
| `SetDialogVariableStringForPlayer(slot, panelId, name, value?)` | Overrides it for one player. Omit `value` to fall back to the all-player value. |
| `SetInputCaptureEnabled(slot, enabled)` / `IsInputCaptureEnabled(slot)` | Puts a player in cursor mode so clicks register, and takes away movement until every layout has released capture. |
| `Reset()` / `ResetForPlayer(slot)` | Restores the original state. |

Clicks arrive through `Instance.OnCustomHudClicked(({ player, layout, buttonId }) => …)`, where `buttonId` is the clicked button's `id`.

Valve's `cs_script_demo` addon shows the whole pattern. The layout starts with a `Dismissed` class on `#dialog` that sets `opacity: 0`. When a player activates, the script removes the class for that player and captures input. A click on `dismiss_button` adds the class back and releases capture:

```js
Instance.OnCustomHudClicked(({ player, layout, buttonId }) => {
    if (layout === welcome && buttonId === "dismiss_button") {
        welcome.SetHasClassForPlayer(player.GetPlayerSlot(), "dialog", "Dismissed", true);
        welcome.SetInputCaptureEnabled(player.GetPlayerSlot(), false);
    }
});
```

## Related map entities

`csgo.fgd` defines two more entities in the same family. Each matches a class in the declaration file:

- `radar_element`: an icon on the radar and the overview map. Its script class is `CSRadarPoint`, with `SetIcon`, `SetColor` and `SetVisibleToTeam`.
- `observable_element`: a model players can spectate once no teammates are alive. Its script class is `CSObservablePoint`, with `SetObservableModelEntity` and `SetObservableForTeam`.
