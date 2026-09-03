import { join } from 'node:path';
import { readJsonFile, requireKeys, requireRows, siteDataDir } from '../paths';

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
	const file = join(siteDataDir(), 'game_modes.json');
	const raw = readJsonFile<RawGameModesData>(file);
	requireKeys(file, raw, ['note', 'game_types', 'map_groups']);
	requireRows(file, raw.game_types, 'game_types', ['id', 'index', 'modes']);
	requireRows(file, raw.game_types[0]!.modes, 'game_types[0].modes', [
		'id',
		'game_type',
		'game_mode',
		'name_token',
		'description_token',
		'display_name',
		'max_players',
		'map_groups',
		'type_flags',
		'exhibit_game_type',
		'convars',
		'has_convar_overrides',
	]);
	requireRows(file, raw.map_groups, 'map_groups', ['id', 'maps']);
	cache = {
		note: raw.note,
		gameTypes: raw.game_types,
		mapGroupsById: new Map(raw.map_groups.map((g) => [g.id, g])),
	};
	return cache;
}
