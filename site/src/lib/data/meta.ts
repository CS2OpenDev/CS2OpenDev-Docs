import { join } from 'node:path';
import { readJsonFile, siteDataDir } from '../paths';

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
	platform: string;
	generated_utc: string;
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
	cache = readJsonFile<Meta>(join(siteDataDir(), 'meta.json'));
	return cache;
}
