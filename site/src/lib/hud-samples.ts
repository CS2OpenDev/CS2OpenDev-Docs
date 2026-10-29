/**
 * The HUD gallery's samples. Each one is a set of real files under src/samples/hud/,
 * laid out the way an addon expects them, and every page renders those files as-is.
 * `screenshot` is the basename of a capture under src/samples/hud/screenshots/;
 * until one exists, the page shows a placeholder instead.
 */
export interface HudSample {
	slug: string;
	title: string;
	summary: string;
	/** What the sample is built from, shown on its gallery card. */
	uses: string[];
	/** Paths relative to src/samples/hud/. */
	files: string[];
}

const layout = (name: string) => [
	`panorama/layout/custom_game/gallery_${name}.xml`,
	`panorama/styles/custom_game/gallery_${name}.css`,
	`maps/scripts/gallery_${name}.js`,
];

export const HUD_SAMPLES: HudSample[] = [
	{
		slug: 'dialog',
		title: 'Welcome dialog',
		summary: 'A dismissable dialog that greets each player by name and captures the cursor until they click.',
		uses: ['custom_hud_layout', 'input capture', 'per-player dialog variable'],
		files: layout('dialog'),
	},
	{
		slug: 'timer',
		title: 'Countdown timer',
		summary: 'A round countdown at the top of the screen that turns red near zero and hides under the scoreboard.',
		uses: ['custom_hud_layout', 'SetThink', 'HUD_SCOREBOARD_VISIBLE'],
		files: layout('timer'),
	},
	{
		slug: 'status',
		title: 'Player stat card',
		summary: "A per-player card with that player's kills and current streak.",
		uses: ['custom_hud_layout', 'per-player state', 'OnPlayerKill'],
		files: layout('status'),
	},
	{
		slug: 'menu',
		title: 'Clickable menu',
		summary: 'A loadout menu opened from chat, with a selected state and a close button.',
		uses: ['custom_hud_layout', 'OnCustomHudClicked', 'OnPlayerChat'],
		files: layout('menu'),
	},
	{
		slug: 'toast',
		title: 'Notification toast',
		summary: 'A toast that slides in for bomb plants, defuses and round starts, and replaces itself cleanly.',
		uses: ['custom_hud_layout', 'Instance.Delay', 'transitions'],
		files: layout('toast'),
	},
	{
		slug: 'capture',
		title: 'Capture progress bar',
		summary: 'A segmented progress bar for a capture zone that shows when the zone is contested.',
		uses: ['custom_hud_layout', 'FindEntitiesByClass', 'segmented bar'],
		files: layout('capture'),
	},
	{
		slug: 'text',
		title: 'World and screen text',
		summary: 'A point_worldtext scoreboard in the map and a game_text message for the player who got a kill.',
		uses: ['point_worldtext', 'game_text', 'EntFireAtName'],
		files: ['maps/scripts/gallery_text.js'],
	},
	{
		slug: 'radar',
		title: 'Radar markers',
		summary: 'radar_element markers that change icon, colour and team visibility as objectives change hands.',
		uses: ['radar_element', 'CSRadarPoint', 'OnScriptInput'],
		files: ['maps/scripts/gallery_radar.js'],
	},
];

export function hudSample(slug: string): HudSample {
	const sample = HUD_SAMPLES.find((s) => s.slug === slug);
	if (!sample) throw new Error(`hud-samples: no sample "${slug}"`);
	return sample;
}

const SOURCES = import.meta.glob<string>('../samples/hud/**/*.{xml,css,js}', {
	query: '?raw',
	import: 'default',
	eager: true,
});

/** A sample file's text. Throws on a path that is listed but missing, so a rename fails the build. */
export function hudSource(path: string): string {
	const text = SOURCES[`../samples/hud/${path}`];
	if (text === undefined) throw new Error(`hud-samples: no file src/samples/hud/${path}`);
	return text;
}

const SHOTS = import.meta.glob<{ default: ImageMetadata }>('../samples/hud/screenshots/*.{png,jpg,webp}', {
	eager: true,
});

/** The sample's screenshot, or undefined until one is captured. */
export function hudScreenshot(slug: string): ImageMetadata | undefined {
	for (const [path, mod] of Object.entries(SHOTS)) {
		if (path.replace(/^.*\//, '').replace(/\.[^.]+$/, '') === slug) return mod.default;
	}
	return undefined;
}
