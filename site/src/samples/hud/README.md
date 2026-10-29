# HUD gallery samples

The files behind `/scripting/hud/`. Each page renders these files as they are, so
editing one here changes the page. They are laid out like an addon:

```
panorama/layout/custom_game/gallery_<name>.xml   layouts (compile to .vxml)
panorama/styles/custom_game/gallery_<name>.css   stylesheets (compile to .vcss)
maps/scripts/gallery_<name>.js                   point_script scripts (compile to .vjs)
maps/scripts/tsconfig.json                       Valve's compiler options
screenshots/<name>.png                           in-game captures
```

`src/lib/hud-samples.ts` lists the samples, their titles and their files. A file
listed there that doesn't exist fails the build.

## Typechecking the scripts

Valve's `point_script.d.ts` isn't committed (it's gitignored at that path). Copy it
in from the Workshop Tools, then run `tsc` in the scripts folder:

```bash
cp "<CS2>/content/csgo_addons/cs_script_demo/maps/scripts/point_script.d.ts" maps/scripts/
cd maps/scripts && ../../../../../node_modules/.bin/tsc -p .
```

Do this after any script change. It's not in CI, because CI has no copy of the file.

## Screenshots

A sample page shows a "Screenshot needed" placeholder until
`screenshots/<slug>.png` (or `.jpg`/`.webp`) exists, where `<slug>` is the sample's
slug in `hud-samples.ts`. The page's status line switches to "taken in game" at the
same time, so only add a capture made from the files in this folder, unedited.

To capture one:

1. Copy the sample's files into a test addon and place the entities from its page's
   **Map setup** table. One `point_script` per sample.
2. Run the map at 1920×1080 with the stock HUD visible, and get the sample into the
   state its page describes (for the menu, open it and pick an option; for the toast,
   catch it fully slid in).
3. Take the screenshot in game (F12 in Steam), crop nothing, and save it as
   `screenshots/<slug>.png`. Keep files under about 500 KB; convert to `.webp` or
   `.jpg` if needed.
4. In the commit message, note the game build the capture was taken on.

If a sample doesn't render as its CSS intends, fix the sample in the same change
rather than capturing it broken, and note what was wrong on the
[HUD gotchas](../../content/docs/scripting/hud/gotchas.md) page.
