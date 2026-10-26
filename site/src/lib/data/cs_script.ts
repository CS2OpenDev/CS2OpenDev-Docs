import { existsSync } from 'node:fs';
import { join } from 'node:path';
import { escapeHtml, inlineCodeHtml } from '../html';
import { readJsonFile, requireKeys, requireRows, siteDataDir } from '../paths';
import {
	commandsHref,
	convarAnchorHref,
	convarsHref,
	entityIoHref,
	gameEventsHref,
	gameModesHref,
	itemsHref,
	scriptAnchorHref,
	scriptTypeHref,
} from '../urls';

export type SeeTarget = 'entities' | 'game_modes' | 'items' | 'convars' | 'commands' | 'game_events';

export interface SchemaRef {
	name: string;
	module: string;
}

interface DocFields {
	doc: string;
	deprecated: boolean;
	deprecation_note: string;
	experimental: boolean;
	experimental_note: string;
}

export interface ScriptParam {
	name: string;
	type: string;
	optional: boolean;
	rest: boolean;
}

export interface ScriptMember extends DocFields {
	name: string;
	kind: string;
	overload_index: number;
	signature: string;
	optional: boolean;
	modifiers: string[];
	type_params: string[];
	params: ScriptParam[];
	param_docs: Record<string, string>;
	return_type: string;
	returns_doc: string;
	type: string;
	default_value: string;
	examples: string[];
	referenced_types: string[];
	convars: string[];
	see: SeeTarget[];
}

export interface ScriptType extends DocFields {
	name: string;
	kind: string;
	exported: boolean;
	extends: string[];
	implements: string[];
	subclasses: string[];
	type_params: string[];
	type: string;
	examples: string[];
	referenced_types: string[];
	schema: SchemaRef | null;
	classnames: string[];
	/** Classnames with no FGD entry (`player`); they have no /entities/ page. */
	runtime_classnames: string[];
	convars: string[];
	members: ScriptMember[];
}

export interface ScriptEnumMember {
	name: string;
	value: number;
	initializer: string;
	doc: string;
	deprecated: boolean;
	deprecation_note: string;
	convars: string[];
	engine_name: string;
	engine_value: string;
	engine_match: boolean;
}

export interface ScriptEnum extends DocFields {
	name: string;
	exported: boolean;
	schema: SchemaRef | null;
	values_agree: boolean | null;
	members: ScriptEnumMember[];
}

export interface ScriptHook extends DocFields {
	name: string;
	signature: string;
	mapped: boolean;
	events: { name: string; anchor: string }[];
	verified: boolean;
	notes: string;
}

export interface CsScript {
	build_id: string;
	module: string;
	module_doc: string;
	file_doc: string;
	es_target: string;
	source_path: string;
	source_sha256: string;
	tsconfig_path: string;
	exports: { name: string; type: string; doc: string }[];
	types: ScriptType[];
	enums: ScriptEnum[];
	hooks: ScriptHook[];
}

let cache: CsScript | null | undefined;

/** null when the build carries no cs_script_api.json (Linux, or an older extract). */
export function loadCsScript(): CsScript | null {
	if (cache !== undefined) return cache;
	const file = join(siteDataDir(), 'cs_script.json');
	if (!existsSync(file)) {
		cache = null;
		return cache;
	}
	const raw = readJsonFile<CsScript>(file);
	requireKeys(file, raw, [
		'build_id',
		'module',
		'module_doc',
		'file_doc',
		'es_target',
		'source_path',
		'source_sha256',
		'tsconfig_path',
		'exports',
		'types',
		'enums',
		'hooks',
	]);
	requireRows(file, raw.exports, 'exports', ['name', 'type', 'doc']);
	requireRows(file, raw.types, 'types', [
		'name',
		'kind',
		'exported',
		'extends',
		'subclasses',
		'type',
		'schema',
		'classnames',
		'runtime_classnames',
		'convars',
		'members',
		'doc',
		'deprecated',
		'experimental',
	]);
	requireRows(file, raw.enums, 'enums', ['name', 'schema', 'values_agree', 'members', 'doc', 'deprecated']);
	requireRows(file, raw.hooks, 'hooks', ['name', 'signature', 'mapped', 'events', 'verified', 'notes', 'doc']);
	cache = raw;
	return cache;
}

/** Interfaces and classes get a page each; type aliases are listed on the index. */
export function pagedTypes(api: CsScript): ScriptType[] {
	return api.types.filter((t) => t.kind !== 'type_alias');
}

export function typeByName(api: CsScript): Map<string, ScriptType> {
	return new Map(api.types.map((t) => [t.name, t]));
}

export function enumByName(api: CsScript): Map<string, ScriptEnum> {
	return new Map(api.enums.map((e) => [e.name, e]));
}

/** Members grouped by name, overloads together, in declaration order. */
export function memberGroups(t: ScriptType): { name: string; overloads: ScriptMember[] }[] {
	const out: { name: string; overloads: ScriptMember[] }[] = [];
	const at = new Map<string, number>();
	for (const m of t.members) {
		const i = at.get(m.name);
		if (i === undefined) {
			at.set(m.name, out.length);
			out.push({ name: m.name, overloads: [m] });
		} else {
			out[i].overloads.push(m);
		}
	}
	return out;
}

const IDENT = /[A-Za-z_][A-Za-z0-9_]*/g;

/** Page or index anchor for a script type or enum name, if this build declares it. */
export function scriptNameHref(api: CsScript, name: string): string | undefined {
	const t = typeByName(api).get(name);
	if (t) return t.kind === 'type_alias' ? scriptAnchorHref(name) : scriptTypeHref(name);
	return enumByName(api).has(name) ? scriptAnchorHref(name) : undefined;
}

/** A type or signature text as HTML, with every declared type name linked. */
export function linkTypesHtml(api: CsScript, text: string, self?: string): string {
	let out = '';
	let last = 0;
	for (const m of text.matchAll(IDENT)) {
		const at = m.index ?? 0;
		out += escapeHtml(text.slice(last, at));
		const href = m[0] === self ? undefined : scriptNameHref(api, m[0]);
		out += href ? `<a href="${href}">${m[0]}</a>` : escapeHtml(m[0]);
		last = at + m[0].length;
	}
	return out + escapeHtml(text.slice(last));
}

/**
 * d.ts doc text as HTML: `code spans`, paragraph breaks kept, and each convar
 * name the generator found in the text linked to its row on /convars/.
 */
export function docHtml(text: string, convars: string[] = []): string {
	let html = inlineCodeHtml(text).replace(/\n/g, '<br />');
	for (const name of convars) {
		const re = new RegExp(`(?<![\w/#])${name}(?![\w])`, 'g');
		html = html.replace(re, `<a href="${convarAnchorHref(name)}"><code>${name}</code></a>`);
	}
	return html;
}

export const SEE_LABEL: Record<SeeTarget, string> = {
	entities: 'Entity I/O',
	game_modes: 'Game modes',
	items: 'Items',
	convars: 'ConVars',
	commands: 'Commands',
	game_events: 'Game events',
};

export function seeHref(target: SeeTarget): string {
	return {
		entities: entityIoHref(),
		game_modes: gameModesHref(),
		items: itemsHref(),
		convars: convarsHref(),
		commands: commandsHref(),
		game_events: gameEventsHref(),
	}[target];
}
