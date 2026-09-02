import { join } from 'node:path';
import { readJsonFile, siteDataDir } from '../paths';

export interface GameMode {
	id: string;
	game_type: number;
	game_mode: number;
	name_token: string;
	description_token: string;
	display_name: string;
	max_players: number;
	map_groups: string[];
	type_flags: number;
	exhibit_game_type: string;
	convars: unknown[];
	has_convar_overrides: boolean;
}

export interface GameType {
	id: string;
	index: number;
	modes: GameMode[];
}

export interface MapGroup {
	id: string;
	maps: string[];
}

interface RawGameModesData {
	note: string;
	game_types: GameType[];
	map_groups: MapGroup[];
}

export interface GameModesIndex {
	note: string;
	gameTypes: GameType[];
	mapGroupsById: Map<string, MapGroup>;
}

let cache: GameModesIndex | undefined;

export function loadGameModes(): GameModesIndex {
	if (cache) return cache;
	const raw = readJsonFile<RawGameModesData>(join(siteDataDir(), 'game_modes.json'));
	cache = {
		note: raw.note,
		gameTypes: raw.game_types,
		mapGroupsById: new Map(raw.map_groups.map((g) => [g.id, g])),
	};
	return cache;
}
