import { CSPlayerPawn, GameRules, Instance } from "cs_script/point_script";

// point_worldtext named "gallery_score_text": world text above the spawn.
// game_text named "gallery_kill_text": "All Players" flag off, so it shows only to the activator.
const WORLD_TEXT = "gallery_score_text";
const SCREEN_TEXT = "gallery_kill_text";

function showScore() {
    const ct = GameRules.GetTeamScore(3);
    const t = GameRules.GetTeamScore(2);
    Instance.EntFireAtName({ name: WORLD_TEXT, input: "SetMessage", value: `CT ${ct}  :  ${t} T` });
}

Instance.OnRoundStart(() => {
    Instance.EntFireAtName({ name: WORLD_TEXT, input: "SetTextColor", value: "255 255 255" });
    showScore();
});
Instance.OnActivate(showScore);

Instance.OnRoundEnd(({ winningTeam }) => {
    const tWon = winningTeam === 2;
    Instance.EntFireAtName({ name: WORLD_TEXT, input: "SetTextColor", value: tWon ? "255 90 79" : "63 140 255" });
    Instance.EntFireAtName({ name: WORLD_TEXT, input: "SetMessage", value: tWon ? "Terrorists win" : "Counter-Terrorists win" });
});

Instance.OnPlayerKill(({ player, attacker }) => {
    if (!(attacker instanceof CSPlayerPawn) || attacker === player) return;
    const victim = player.GetPlayerController()?.GetPlayerName() ?? "someone";
    // game_text shows to the activator, so pass the killer's pawn.
    Instance.EntFireAtName({ name: SCREEN_TEXT, input: "SetText", value: `You eliminated ${victim}` });
    Instance.EntFireAtName({ name: SCREEN_TEXT, input: "Display", activator: attacker });
});
