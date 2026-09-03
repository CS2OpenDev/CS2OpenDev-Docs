import { join } from 'node:path';
import type { Row } from '../../components/islands/DataTable';
import { siteDataDir, readJsonFile, requireKeys, requireRows } from '../paths';

export interface ConVarFlagLegendEntry {
	name: string;
	convar_count: number;
	command_count: number;
	description: string;
}

export interface ConVarRaw {
	name: string;
	default: string;
	value_type: string;
	min: number | null;
	max: number | null;
	flags: string[];
	help: string;
	prefix: string;
}

interface RawConVarsData {
	convars: ConVarRaw[];
	flags: ConVarFlagLegendEntry[];
}

let cache: RawConVarsData | undefined;

export function loadConVarsData(): RawConVarsData {
	if (cache) return cache;
	const file = join(siteDataDir(), 'convars.json');
	const raw = readJsonFile<RawConVarsData>(file);
	requireKeys(file, raw, ['convars', 'flags']);
	requireRows(file, raw.convars, 'convars', ['name', 'default', 'value_type', 'min', 'max', 'flags', 'help', 'prefix']);
	requireRows(file, raw.flags, 'flags', ['name', 'convar_count', 'command_count', 'description']);
	cache = raw;
	return cache;
}

export function loadConVars(): ConVarRaw[] {
	return loadConVarsData().convars;
}

/** Same legend array is duplicated onto commands.json; either file's copy is authoritative. */
export function flagLegend(): ConVarFlagLegendEntry[] {
	return loadConVarsData().flags;
}

export function flagAnchor(name: string): string {
	return `flag-${name}`;
}

/**
 * `min`/`max` bound only one side on 49 convars in this build (upstream gives a floor
 * with no ceiling, or vice versa); render those with an inequality rather than a blank
 * half of a range that implies the other side is unbounded by omission.
 */
export function rangeText(min: number | null, max: number | null): string {
	if (min !== null && max !== null) return `${min} to ${max}`;
	if (min !== null) return `≥ ${min}`;
	if (max !== null) return `≤ ${max}`;
	return '';
}

/** Every convar as a DataTable row. The page's first page and rows.json both
 * come from here, so a hash reveal lands on the same row either way. */
export function convarRows(): Row[] {
	return loadConVars().map((c) => ({
		name: c.name,
		default: c.default,
		value_type: c.value_type,
		range: rangeText(c.min, c.max),
		flags: c.flags,
		description: c.help,
	}));
}
