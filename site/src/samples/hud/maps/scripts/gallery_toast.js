import { CustomHudLayout, Instance } from "cs_script/point_script";

// custom_hud_layout named "gallery_toast_layout", layout = panorama/layout/custom_game/gallery_toast.vxml
const LAYOUT_NAME = "gallery_toast_layout";
const SHOW_SECONDS = 3;
const STYLES = ["Danger", "Success"];

let generation = 0;

function getLayout() {
    const found = Instance.FindEntityByName(LAYOUT_NAME);
    return found instanceof CustomHudLayout ? found : undefined;
}

/**
 * Shows a toast to everyone. `style` is "Danger", "Success" or undefined for the default accent.
 * @param {string} title @param {string} body @param {string} [style]
 */
async function toast(title, body, style) {
    const hud = getLayout();
    if (!hud) return;
    const mine = ++generation;

    // Removing and re-adding a class in the same tick sends nothing, so a toast that
    // replaces a visible one hides it first and slides back in on a later tick.
    hud.SetHasClass("toast", "Show", false);
    await Instance.Delay(0.3);
    if (mine !== generation) return;

    hud.SetDialogVariableString("toast_title", "text", title);
    hud.SetDialogVariableString("toast_body", "text", body);
    for (const s of STYLES) hud.SetHasClass("toast", s, s === style);
    hud.SetHasClass("toast", "Show", true);

    await Instance.Delay(SHOW_SECONDS);
    if (mine === generation) hud.SetHasClass("toast", "Show", false);
}

Instance.OnBombPlant(() => {
    toast("Bomb planted", "Defuse it before it explodes", "Danger");
});

Instance.OnBombDefuse(() => {
    toast("Bomb defused", "Counter-Terrorists saved the site", "Success");
});

Instance.OnRoundStart(() => {
    toast("Round started", "Capture the point to win");
});
