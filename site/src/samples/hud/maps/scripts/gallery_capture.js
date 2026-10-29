import { CSPlayerPawn, CustomHudLayout, Instance } from "cs_script/point_script";

// custom_hud_layout named "gallery_capture_layout", layout = panorama/layout/custom_game/gallery_capture.vxml
// info_target named "gallery_capture_point" marks the centre of the zone.
const LAYOUT_NAME = "gallery_capture_layout";
const POINT_NAME = "gallery_capture_point";
const RADIUS = 160;
const SECONDS_TO_CAPTURE = 10;
const SEGMENTS = 10;
const TICK = 0.25;

let progress = 0; // 0..1
let shownSegments = -1;
let shownState = "";
let shownLabel = "";

function getLayout() {
    const found = Instance.FindEntityByName(LAYOUT_NAME);
    return found instanceof CustomHudLayout ? found : undefined;
}

/** Counts living pawns per team inside the zone. */
function occupants() {
    const point = Instance.FindEntityByName(POINT_NAME);
    const counts = { t: 0, ct: 0 };
    if (!point) return counts;
    const c = point.GetAbsOrigin();
    for (const pawn of Instance.FindEntitiesByClass("player")) {
        if (!(pawn instanceof CSPlayerPawn) || !pawn.IsAlive()) continue;
        const p = pawn.GetAbsOrigin();
        const dx = p.x - c.x, dy = p.y - c.y, dz = p.z - c.z;
        if (dx * dx + dy * dy + dz * dz > RADIUS * RADIUS) continue;
        if (pawn.GetTeamNumber() === 2) counts.t++;
        else if (pawn.GetTeamNumber() === 3) counts.ct++;
    }
    return counts;
}

Instance.SetThink(() => {
    const hud = getLayout();
    const now = Instance.GetGameTime();
    if (hud) {
        const { t, ct } = occupants();
        const contested = t > 0 && ct > 0;
        if (t > 0 && !contested) progress = Math.min(1, progress + TICK / SECONDS_TO_CAPTURE);

        const state = contested ? "Contested" : t > 0 ? "Capturing" : progress > 0 ? "Held" : "Idle";
        const segments = Math.round(progress * SEGMENTS);

        // Ten fixed segments instead of an animated width: a width transition
        // restarts whenever a dialog variable in the same subtree changes.
        if (segments !== shownSegments) {
            for (let i = 0; i < SEGMENTS; i++) hud.SetHasClass(`seg${i}`, "On", i < segments);
            shownSegments = segments;
        }
        if (state !== shownState) {
            hud.SetHasClass("capture", "Hidden", state === "Idle");
            hud.SetHasClass("capture", "Contested", contested);
            shownState = state;
        }
        const label = contested ? "Contested!" : `Captured ${Math.round(progress * 100)}%`;
        if (label !== shownLabel) {
            hud.SetDialogVariableString("capture_label", "text", label);
            shownLabel = label;
        }
    }
    Instance.SetNextThink(now + TICK);
});

Instance.OnRoundStart(() => {
    progress = 0;
    shownSegments = -1;
    shownState = "";
    shownLabel = "";
    Instance.SetNextThink(Instance.GetGameTime());
});

Instance.OnActivate(() => {
    Instance.SetNextThink(Instance.GetGameTime());
});
