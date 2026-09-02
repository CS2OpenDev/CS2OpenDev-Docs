import { join } from 'node:path';
import { siteDataDir, readJsonFile } from '../paths';
import { escapeHtml } from '../html';

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
	cache = readJsonFile<RawConVarsData>(join(siteDataDir(), 'convars.json'));
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

/**
 * Raw upstream help text to trusted HTML: escape first, then turn `<token>` placeholders
 * into `<code>` and newlines into `<br>` so multi-line descriptions (bot_prefix, and 15
 * more convars) render as one readable table cell instead of breaking the table.
 */
export function helpTextHtml(help: string): string {
	const escaped = escapeHtml(help);
	const withPlaceholders = escaped.replace(/&lt;(.+?)&gt;/g, '<code>&lt;$1&gt;</code>');
	return withPlaceholders.replace(/\n/g, '<br>');
}
