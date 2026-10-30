---
title: HUD examples
description: Community CS2 projects with working custom_hud_layout layouts and script-driven HUD entities, grouped by the kind of UI they show.
---

This site doesn't keep its own HUD samples. These community projects already have working layouts. They are grouped by the kind of UI each one shows, and each link goes to the file to read first.

Most of them are server plugins, but the layout files work the same from a map script; only the code that calls `SetHasClass` and `SetDialogVariableString` differs. Check a project's license before copying from it. Projects with no license can be read but not reused.

## Starting point

Valve's own example ships with the Workshop Tools: the `cs_script_demo` addon under `content/csgo_addons/cs_script_demo/`. Its `welcome.xml`, `welcome.css` and `maps/scripts/setup.js` show a dismissable dialog with a button and input capture. That is the smallest complete setup, and the one the [overview](../) describes.

- [scriptedeuch `panorama/test.xml`](https://github.com/Orb-Workshop/scriptedeuch/blob/master/panorama/test.xml) (MIT): the same dialog inside a TypeScript map-script setup.

## Menus

- [cs2-ui-kit `hud/layout/example_menu.xml`](https://github.com/nvmxre/cs2-ui-kit/blob/master/hud/layout/example_menu.xml) (MIT): a menu of Buttons over a dimmed backdrop. Its comments explain why the root has no id and why the backdrop takes hittest.
- [CustomHudProbeSW2 `hud/layout/swift_menu_custom_hud.xml`](https://github.com/nicedayzhu/CustomHudProbeSW2/blob/main/hud/layout/swift_menu_custom_hud.xml) (MIT): a menu layout with a matching stylesheet in `hud/styles/`.
- [cs2kz-metamod `cs2kz/menu.xml`](https://github.com/KZGlobalTeam/cs2kz-metamod/blob/master/workshop/panorama/layout/custom_game/cs2kz/menu.xml) (AGPL-3.0): the menu of a large, actively used plugin.

## Notifications and cards

- [cs2-ui-kit `kit/layout/cs2uikit_toasts.xml`](https://github.com/nvmxre/cs2-ui-kit/blob/master/kit/layout/cs2uikit_toasts.xml) (MIT): four stacked toasts per player, placed and animated with transform classes. The stylesheet's header comment is a short course in what Panorama will and won't animate.
- [cs2-ui-kit `kit/layout/cs2uikit_votes.xml`](https://github.com/nvmxre/cs2-ui-kit/blob/master/kit/layout/cs2uikit_votes.xml) (MIT): a vote card.
- [CustomHudProbeSW2 `hud/layout/cyber_card_custom_hud.xml`](https://github.com/nicedayzhu/CustomHudProbeSW2/blob/main/hud/layout/cyber_card_custom_hud.xml) (MIT): showcase cards. The repository also has flip-card and 3D-hover variants, plus in-game screenshots.

## Timers, trackers and status bars

- [cs2kz-metamod `cs2kz/mhud.xml`](https://github.com/KZGlobalTeam/cs2kz-metamod/blob/master/workshop/panorama/layout/custom_game/cs2kz/mhud.xml) (AGPL-3.0): a timer and speed HUD that players can drag and resize.
- [cs2-challenges `challenges/tracker_v5.xml`](https://github.com/Kandru/cs2-challenges/blob/main/workshop/content/panorama/layout/custom_game/challenges/tracker_v5.xml) (GPL-3.0): an on-screen challenge tracker.
- [csQuake `quake_hud.xml`](https://github.com/girlglock/csQuake/blob/main/panorama/layout/custom_game/quake_hud.xml) (GPL-2.0): a Quake status bar driven from a map script. Its digits are empty panels whose sprite is switched by class, which works around the server being unable to change an `<Image>`'s `src`.

## Driving a layout from a map script

- [cs2-map-mcp `mechanics/hud.js`](https://github.com/Rmgs123/cs2-map-mcp/blob/main/src/cs2map/data/mechanics/hud.js) (MIT): a small reusable wrapper around one `custom_hud_layout`, with show and hide per player, per-player text and a throttle so the script doesn't resend every tick.
- [fyscs `ze_diablo/hud.js`](https://github.com/fyscs/cs_script/blob/master/2001/ze_diablo/hud.js) (no license): a zombie-escape map's HUD script that switches colour classes on a label.

## Without a layout

- **`point_worldtext`:** Source2Wiki's walkthrough of Valve's [grenade training demo](https://github.com/Source2Wiki/Source2Wiki/blob/master/docs/Scripting/Counter-Strike%202/cs_script/examples/3-grenadetraining.mdx) (MIT) updates world text with `EntFireAtName({ name, input: "SetMessage", value })` and toggles it with `Enable` and `Disable`.
- **`env_hudhint`:** [fyscs `ze_alien_shooter/bosshud.js`](https://github.com/fyscs/cs_script/blob/master/2001/ze_alien_shooter/bosshud.js) (no license) shows a boss health readout through a hint entity.
- **`radar_element` and `observable_element`:** no public community example yet. The script classes are `CSRadarPoint` (`SetIcon`, `SetColor`, `SetVisibleToTeam`) and `CSObservablePoint`; see the [overview](../#related-map-entities).

Know of a better example, or one for something missing here? A one-line addition to this page is welcome.
