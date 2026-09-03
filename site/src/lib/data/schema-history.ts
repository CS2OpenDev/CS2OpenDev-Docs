import { existsSync } from 'node:fs';
import { join } from 'node:path';
import { readJsonFile, requireKeys, requireRows, siteDataDir } from '../paths';

export interface HistoryTransition {
	from_build: string;
	to_build: string;
	from_date: string;
	to_date: string;
	anchor: string;
	counts: {
		class_added: number;
		class_changed: number;
		class_removed: number;
		enum_added: number;
		enum_changed: number;
		enum_removed: number;
		field_ops: number;
	};
	is_empty: boolean;
}

export interface HistoryClassChange {
	name: string;
	field_ops: Record<string, number>;
	metadata_only: boolean;
	static_field_ops: number;
	meta_ops: number;
	paired_evidence: number;
	pair_candidates: number;
	resize: { from: string; to: string } | null;
	realign: boolean;
	reparent: boolean;
	flags_changed: boolean;
	confirmed_rename_count: number;
}

export interface HistoryDetail {
	from_build: string;
	to_build: string;
	anchor: string;
	from_date: string;
	to_date: string;
	classes_added: string[];
	classes_removed: string[];
	classes_changed: HistoryClassChange[];
	classes_changed_total: number;
	classes_changed_truncated: boolean;
	class_pair_candidates_count: number;
	field_move_candidates_count: number;
	/** Present on some historical entries; absent on others depending on the evolution artifact's shape. */
	enums_added?: string[];
	enums_removed?: string[];
	enums_changed?: unknown[];
}

/** docs/overlays/schema-lens.yml's `breaking:` list, passed through unmodified. */
export interface BreakingEntry {
	class?: string;
	field?: string;
	build?: string;
	note?: string;
	guard?: string;
	[key: string]: unknown;
}

export interface SchemaHistory {
	baseline_build: string;
	latest_build: string;
	platform: string;
	schema_version: string;
	transitions: HistoryTransition[];
	detail: HistoryDetail[];
	breaking: BreakingEntry[];
}

let cache: SchemaHistory | null | undefined;

/** null when the generator had no schema_evolution data for this platform and wrote no file. */
export function loadSchemaHistory(): SchemaHistory | null {
	if (cache !== undefined) return cache;
	const file = join(siteDataDir(), 'schema-history.json');
	if (!existsSync(file)) {
		cache = null;
		return cache;
	}
	const raw = readJsonFile<SchemaHistory>(file);
	requireKeys(file, raw, ['baseline_build', 'latest_build', 'platform', 'schema_version', 'transitions', 'detail', 'breaking']);
	requireRows(file, raw.transitions, 'transitions', ['from_build', 'to_build', 'from_date', 'to_date', 'anchor', 'counts', 'is_empty']);
	if (raw.detail.length > 0) {
		requireKeys(file, raw.detail[0], [
			'from_build',
			'to_build',
			'anchor',
			'from_date',
			'to_date',
			'classes_added',
			'classes_removed',
			'classes_changed',
			'classes_changed_total',
			'classes_changed_truncated',
			'class_pair_candidates_count',
			'field_move_candidates_count',
		], 'detail[0]');
	}
	for (const d of raw.detail) {
		d.enums_added ??= [];
		d.enums_removed ??= [];
		d.enums_changed ??= [];
	}
	cache = raw;
	return cache;
}
