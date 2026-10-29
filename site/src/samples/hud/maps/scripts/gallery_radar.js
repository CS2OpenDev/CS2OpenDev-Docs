import { CSRadarColor, CSRadarIcon, CSRadarPoint, Instance } from "cs_script/point_script";

// radar_element entities named "gallery_radar_a" and "gallery_radar_b", one per objective.
const MARKERS = ["gallery_radar_a", "gallery_radar_b"];
const TEAM_T = 2;
const TEAM_CT = 3;

/** @param {string} name */
function marker(name) {
    const found = Instance.FindEntityByName(name);
    return found instanceof CSRadarPoint ? found : undefined;
}

// Round start: both objectives are neutral towers that everyone sees.
Instance.OnRoundStart(() => {
    for (const name of MARKERS) {
        const m = marker(name);
        if (!m) continue;
        m.SetIcon(CSRadarIcon.TOWER);
        m.SetColor(CSRadarColor.WHITE);
        m.SetVisibleToTeam(TEAM_T, true);
        m.SetVisibleToTeam(TEAM_CT, true);
    }
});

// A trigger_multiple's OnStartTouch can fire RunScriptInput with "claim_a" or "claim_b"
// on the point_script; the activator is the player who touched it.
for (const [input, name] of [["claim_a", "gallery_radar_a"], ["claim_b", "gallery_radar_b"]]) {
    Instance.OnScriptInput(input, ({ activator }) => {
        const m = marker(name);
        if (!m || !activator) return;
        const team = activator.GetTeamNumber();
        m.SetColor(team === TEAM_T ? CSRadarColor.T : CSRadarColor.CT);
    });
}

// Once the bomb is planted, marker A becomes a red C4 icon that only the Counter-Terrorists see.
Instance.OnBombPlant(() => {
    const m = marker("gallery_radar_a");
    if (!m) return;
    m.SetIcon(CSRadarIcon.C4);
    m.SetColor(CSRadarColor.RED);
    m.SetVisibleToTeam(TEAM_T, false);
});
