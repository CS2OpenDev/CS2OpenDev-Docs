import { CustomHudLayout, Instance } from "cs_script/point_script";

// custom_hud_layout named "gallery_menu_layout", layout = panorama/layout/custom_game/gallery_menu.vxml
const LAYOUT_NAME = "gallery_menu_layout";

/** Button id -> label shown back to the player. */
const OPTIONS = new Map([
    ["opt_rifle", "Rifle"],
    ["opt_smg", "SMG"],
    ["opt_pistol", "Pistol only"],
]);

function getLayout() {
    const found = Instance.FindEntityByName(LAYOUT_NAME);
    return found instanceof CustomHudLayout ? found : undefined;
}

/** @param {number} slot @param {boolean} open */
function setOpen(slot, open) {
    const hud = getLayout();
    if (!hud) return;
    hud.SetHasClassForPlayer(slot, "menu", "Closed", !open);
    // While capture is on the player has a cursor and can't move.
    hud.SetInputCaptureEnabled(slot, open);
}

Instance.OnPlayerChat(({ player, text }) => {
    if (player && text.trim().toLowerCase() === "!menu") {
        setOpen(player.GetPlayerSlot(), true);
    }
});

Instance.OnCustomHudClicked(({ player, layout, buttonId }) => {
    const hud = getLayout();
    if (!hud || layout !== hud) return;
    const slot = player.GetPlayerSlot();

    if (buttonId === "opt_close") {
        setOpen(slot, false);
        return;
    }
    const label = OPTIONS.get(buttonId);
    if (label === undefined) return;

    for (const id of OPTIONS.keys()) {
        hud.SetHasClassForPlayer(slot, id, "Selected", id === buttonId);
    }
    hud.SetDialogVariableStringForPlayer(slot, "menu_choice", "choice", `Next round: ${label}`);
});

Instance.OnPlayerDisconnect(({ playerSlot }) => {
    getLayout()?.ResetForPlayer(playerSlot);
});
