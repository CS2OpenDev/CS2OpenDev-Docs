import { join } from 'node:path';
import { readJsonFile, requireKeys, requireRows, siteDataDir } from '../paths';

export interface MetaModule {
	module: string;
	classes: number;
	enums: number;
}

export interface MetaCounts {
	classes: number;
	commands: number;
	convars: number;
	enums: number;
	events: number;
	fields: number;
	game_modes: number;
	items: number;
	maps: number;
	messages: number;
	modules: number;
	music_kits: number;
	paint_kits: number;
	proto_files: number;
	sticker_kits: number;
	surfaces: number;
}

export interface Meta {
	build_id: string;
	steam_date: string;
	/** The Steam depot manifest timestamp from the build's provenance.json. */
	steam_manifest_utc: string;
	platform: string;
	schema_version: string;
	tool_version: string;
	tool_commit: string;
	counts: MetaCounts;
	modules: MetaModule[];
	note: string;
}

let cache: Meta | undefined;

/** meta.json: build identity and per-family counts, read once and cached. */
export function loadMeta(): Meta {
	if (cache) return cache;
	const file = join(siteDataDir(), 'meta.json');
	const raw = readJsonFile<Meta>(file);
	requireKeys(file, raw, [
		'build_id',
		'steam_date',
		'steam_manifest_utc',
		'platform',
		'schema_version',
		'tool_version',
		'tool_commit',
		'counts',
		'modules',
		'note',
	]);
	requireKeys(file, raw.counts, [
		'classes',
		'commands',
		'convars',
		'enums',
		'events',
		'fields',
		'game_modes',
		'items',
		'maps',
		'messages',
		'modules',
		'music_kits',
		'paint_kits',
		'proto_files',
		'sticker_kits',
		'surfaces',
	], 'counts');
	requireRows(file, raw.modules, 'modules', ['module', 'classes', 'enums']);
	cache = raw;
	return cache;
}
