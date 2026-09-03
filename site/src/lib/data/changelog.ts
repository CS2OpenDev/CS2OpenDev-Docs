import { join } from 'node:path';
import { readJsonFile, requireKeys, requireRows, siteDataDir } from '../paths';

export interface ChangelogFieldChange {
	field: string;
	old_value: string;
	new_value: string;
}

export interface ChangelogChangedEntry {
	name: string;
	field_changes: ChangelogFieldChange[];
}

export interface ChangelogFamily {
	family: string;
	added_count: number;
	removed_count: number;
	changed_count: number;
	added: string[];
	removed: string[];
	changed: ChangelogChangedEntry[];
	truncated: boolean;
}

export interface Changelog {
	from_build: string;
	to_build: string;
	platform: string;
	families: ChangelogFamily[];
	no_changes: boolean;
	schema_history_anchor: string;
}

let cache: Changelog | undefined;

export function loadChangelog(): Changelog {
	if (cache) return cache;
	const file = join(siteDataDir(), 'changelog.json');
	const raw = readJsonFile<Changelog>(file);
	requireKeys(file, raw, ['from_build', 'to_build', 'platform', 'families', 'no_changes', 'schema_history_anchor']);
	requireRows(file, raw.families, 'families', [
		'family',
		'added_count',
		'removed_count',
		'changed_count',
		'added',
		'removed',
		'changed',
		'truncated',
	]);
	cache = raw;
	return cache;
}
