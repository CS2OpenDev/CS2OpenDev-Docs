import { CSPlayerPawn, CustomHudLayout, Instance } from "cs_script/point_script";

// custom_hud_layout named "gallery_status_layout", layout = panorama/layout/custom_game/gallery_status.vxml
const LAYOUT_NAME = "gallery_status_layout";
const STREAK_HIGHLIGHT = 3;

/** @type {Map<number, { kills: number, streak: number }>} keyed by player slot */
const stats = new Map();

function getLayout() {
    const found = Instance.FindEntityByName(LAYOUT_NAME);
    return found instanceof CustomHudLayout ? found : undefined;
}

/** @param {number} slot */
function render(slot) {
    const hud = getLayout();
    const s = stats.get(slot);
    if (!hud || !s) return;
    hud.SetDialogVariableStringForPlayer(slot, "status_kills", "value", String(s.kills));
    hud.SetDialogVariableStringForPlayer(slot, "status_streak", "value", String(s.streak));
    hud.SetHasClassForPlayer(slot, "status", "OnStreak", s.streak >= STREAK_HIGHLIGHT);
    hud.SetHasClassForPlayer(slot, "status", "Hidden", false);
}

/** @param {import("cs_script/point_script").Entity | undefined} entity */
function slotOf(entity) {
    if (!(entity instanceof CSPlayerPawn)) return undefined;
    return entity.GetPlayerController()?.GetPlayerSlot();
}

Instance.OnPlayerActivate(({ player }) => {
    const slot = player.GetPlayerSlot();
    stats.set(slot, { kills: 0, streak: 0 });
    render(slot);
});

Instance.OnPlayerKill(({ player, attacker }) => {
    const victim = slotOf(player);
    const killer = slotOf(attacker);
    if (killer !== undefined && killer !== victim) {
        const s = stats.get(killer);
        if (s) {
            s.kills += 1;
            s.streak += 1;
            render(killer);
        }
    }
    if (victim !== undefined) {
        const s = stats.get(victim);
        if (s) {
            s.streak = 0;
            render(victim);
        }
    }
});

// Slots are reused, so clear everything a leaving player had set.
Instance.OnPlayerDisconnect(({ playerSlot }) => {
    stats.delete(playerSlot);
    getLayout()?.ResetForPlayer(playerSlot);
});
