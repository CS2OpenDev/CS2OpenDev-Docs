import { CustomHudLayout, Instance } from "cs_script/point_script";

// custom_hud_layout named "gallery_dialog_layout", layout = panorama/layout/custom_game/gallery_dialog.vxml
const LAYOUT_NAME = "gallery_dialog_layout";

/** @type {CustomHudLayout | undefined} */
let layout;

function getLayout() {
    if (!layout || !layout.IsValid()) {
        const found = Instance.FindEntityByName(LAYOUT_NAME);
        layout = found instanceof CustomHudLayout ? found : undefined;
    }
    return layout;
}

/** @param {number} slot */
function show(slot) {
    const hud = getLayout();
    if (!hud) return;
    hud.SetHasClassForPlayer(slot, "dialog", "Dismissed", false);
    hud.SetInputCaptureEnabled(slot, true);
}

/** @param {number} slot */
function hide(slot) {
    const hud = getLayout();
    if (!hud) return;
    hud.SetHasClassForPlayer(slot, "dialog", "Dismissed", true);
    hud.SetInputCaptureEnabled(slot, false);
}

Instance.OnPlayerActivate(({ player }) => {
    if (player.IsBot()) return;
    const slot = player.GetPlayerSlot();
    // Each player sees their own name; the variable lives on the Label that shows it.
    getLayout()?.SetDialogVariableStringForPlayer(slot, "dialog_title", "name", player.GetPlayerName());
    show(slot);
});

Instance.OnCustomHudClicked(({ player, layout: clicked, buttonId }) => {
    if (clicked === getLayout() && buttonId === "dismiss_button") {
        hide(player.GetPlayerSlot());
    }
});

// A reused slot must not inherit the previous player's dialog state.
Instance.OnPlayerDisconnect(({ playerSlot }) => {
    getLayout()?.ResetForPlayer(playerSlot);
});
