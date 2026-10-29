import { CustomHudLayout, Instance } from "cs_script/point_script";

// custom_hud_layout named "gallery_timer_layout", layout = panorama/layout/custom_game/gallery_timer.vxml
const LAYOUT_NAME = "gallery_timer_layout";
const COUNTDOWN_SECONDS = 60;
const URGENT_SECONDS = 10;

let endsAt = 0;
let shownSeconds = -1;
let running = false;

function getLayout() {
    const found = Instance.FindEntityByName(LAYOUT_NAME);
    return found instanceof CustomHudLayout ? found : undefined;
}

/** @param {number} seconds */
function format(seconds) {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m}:${s.toString().padStart(2, "0")}`;
}

Instance.SetThink(() => {
    if (!running) return;
    const hud = getLayout();
    const now = Instance.GetGameTime();
    const left = Math.max(0, Math.ceil(endsAt - now));

    // Only touch the layout when the displayed second changes.
    if (hud && left !== shownSeconds) {
        shownSeconds = left;
        hud.SetDialogVariableString("timer_value", "time", format(left));
        hud.SetHasClass("timer", "Urgent", left <= URGENT_SECONDS);
    }

    if (left === 0) {
        running = false;
        hud?.SetHasClass("timer", "Hidden", true);
        return;
    }
    Instance.SetNextThink(now + 0.1);
});

Instance.OnRoundStart(() => {
    const hud = getLayout();
    if (!hud) return;
    endsAt = Instance.GetGameTime() + COUNTDOWN_SECONDS;
    shownSeconds = -1;
    running = true;
    hud.SetHasClass("timer", "Hidden", false);
    Instance.SetNextThink(Instance.GetGameTime());
});

Instance.OnRoundEnd(() => {
    running = false;
    getLayout()?.SetHasClass("timer", "Hidden", true);
});
