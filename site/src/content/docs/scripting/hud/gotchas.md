---
title: HUD gotchas
description: What breaks in CS2 custom_hud_layout files and why, from Valve's declaration file and from the community authors who found it out.
---

Panorama looks like HTML and CSS, but it's its own engine, and `custom_hud_layout` allows only a small part of it. Most of what goes wrong fails without an error: the layout doesn't appear, or a property does nothing.

Each item is marked by where it comes from:

- **Valve:** stated in `point_script.d.ts` or shown in Valve's `cs_script_demo` addon.
- **Reported:** written up by community authors from their own testing, and not yet confirmed here. The sources are [cs2-ui-kit's GOTCHAS.md](https://github.com/nvmxre/cs2-ui-kit/blob/f145a39ce2769e0fee78b8af92e77c822c38fcf5/docs/GOTCHAS.md), [PanoramaHUD-Skills' runtime notes](https://github.com/Next-il/PanoramaHUD-Skills/blob/c6c90c02ccded876c536502bf31d7c1202ae3d52/cs2-panorama-hud/references/runtime-behaviour.md) and [cs2-challenges' Panorama CSS notes](https://github.com/Kandru/cs2-challenges/blob/bd4c33842bfb147cc3b3c937bfbfddf0eef995e1/workshop/panorama-css.md). If you've confirmed or disproved one, a change to this page is welcome.

## Markup

- **Valve:** the allowed elements and attributes are listed under [What a layout may contain](../#what-a-layout-may-contain).
- **Reported:** one disallowed panel type or attribute stops the whole layout from loading. `style`, `hittestchildren` and `scaling` are all rejected.
- **Reported:** the root panel may not have an `id`; the resource compiler refuses the file. Put the id on a panel inside it. Valve's demo root has only a `class`.
- **Reported:** because the root is always visible, hide and show a panel inside it, never the root itself.
- **Reported:** `hittest="false"` on every panel that isn't meant to be clicked keeps clicks from landing on decoration. While input capture is on, clicks on empty space can reach the stock HUD underneath, such as the buy menu.

## CSS

- **Valve:** styling with CSS is supported. Valve's demo stylesheet uses `flow-children`, `horizontal-align`, `&.Class` nesting, `&:hover`, `transition-property` and `transition-duration`, and eight-digit hex colours such as `#000000ee`.
- **Reported:** web layout and value syntax are dropped without a warning: `display`, flexbox, `rgba()`, `calc()`, `var()`, `@media`, `::before` and `::after`. Lay out with `flow-children: down | right` and `horizontal-align`/`vertical-align`, and write colours as hex.
- **Reported:** `background-size: contain` is spelled `contains` in Panorama.
- **Reported:** `box-shadow` takes the colour first.
- **Reported:** panels never wrap, and a `width: 100%` child of a parent with no size renders as nothing. Give containers a size.
- **Reported:** `background-blur` does nothing; `world-blur` blurs the game behind a panel.
- **Reported:** transitions on `opacity` and `transform` work. Animating height or anything that reflows the layout doesn't.

## Classes and dialog variables

- **Valve:** how the `ForPlayer` methods override the all-player value and fall back to it is under [Driving it from script](../#driving-it-from-script).
- **Valve:** the seven `HUD_*_VISIBLE` classes the game sets while stock UI is open are listed under [What a layout may contain](../#what-a-layout-may-contain). A selector such as `.HUD_SCOREBOARD_VISIBLE #mine` reacts to one.
- **Reported:** the dialog-variable syntax for a Label's `text` is under [What a layout may contain](../#what-a-layout-may-contain).
- **Reported:** class changes reach clients as a difference from the last state, so removing and re-adding a class in the same tick sends nothing. To replay an animation, remove the class and add it back on a later tick, or alternate between two class names.
- **Reported:** setting a dialog variable restarts any `width` transition in the same part of the layout. Build bars from fixed segments, or with `clip: rect()`.
- **Reported:** each `custom_hud_layout` can intern at most 1024 distinct ids, class names and variable names.

## Images

- **Reported:** the server can't change an `<Image>`'s `src` at run time. To switch images, put each as a `background-image` on a class and toggle the class.
- **Reported:** game assets resolve through `s2r://`, for example `url("s2r://panorama/images/icons/ui/expand.vsvg")`. An addon's own images go under `panorama/images/custom_game/`.
- **Reported:** a stock `.vsvg` used directly as an `<Image src>` has broken layouts; using it as a background works.

## Layering and players

- **Reported:** only `z-index: 99999` on the outermost panel puts a layout above the stock HUD.
- **Valve:** input capture freezes the player until every layout has released it. Release it wherever you close the UI.
- **Reported:** state is kept per slot, and a slot is reused by the next player to connect. Clear a slot on disconnect with `ResetForPlayer`, or hide per-player panels on spawn.
- **Reported:** the `custom_hud_layout` entity outlives a server plugin reload, along with the classes and variables already set on it. Whether a map script's hot reload in Tools mode behaves the same hasn't been checked; resetting what the script owns on load is safe either way.
