import { join } from 'node:path';
import type { Row } from '../../components/islands/DataTable';
import { siteDataDir, readJsonFile, requireKeys, requireRows } from '../paths';
import { inlineCodeHtml } from '../html';

export interface GameEventField {
	name: string;
	type: string;
	description: string;
}

export interface GameEvent {
	name: string;
	source: string;
	anchor: string;
	description: string;
	notes: string;
	warning: string;
	properties: Record<string, string>;
	fields: GameEventField[];
}

export interface TypeLegendEntry {
	type: string;
	description: string;
	key_t_type_code: number | null;
	note: string;
}

interface RawGameEventsData {
	events: GameEvent[];
	/** event name -> sources it is defined in, for every name that appears more than once. */
	duplicates: Record<string, string[]>;
	sources: string[];
	type_legend: TypeLegendEntry[];
}

let cache: RawGameEventsData | undefined;

export function loadGameEventsData(): RawGameEventsData {
	if (cache) return cache;
	const file = join(siteDataDir(), 'gameevents.json');
	const raw = readJsonFile<RawGameEventsData>(file);
	requireKeys(file, raw, ['events', 'duplicates', 'sources', 'type_legend']);
	requireRows(file, raw.events, 'events', [
		'name',
		'source',
		'anchor',
		'description',
		'notes',
		'warning',
		'properties',
		'fields',
	]);
	requireRows(file, raw.type_legend, 'type_legend', ['type', 'description', 'key_t_type_code', 'note']);
	cache = raw;
	return cache;
}

export function loadGameEvents(): GameEvent[] {
	return loadGameEventsData().events;
}

/** Source file stem with the `.gameevents` suffix stripped, matching the anchor rule. */
export function sourceStem(source: string): string {
	return source.replace(/\.gameevents$/, '');
}

/** Heading text: bare name, unless this name has a same-named sibling in another source. */
export function eventHeading(ev: GameEvent, duplicates: Record<string, string[]>): string {
	return duplicates[ev.name] ? `${ev.name} (${sourceStem(ev.source)})` : ev.name;
}

export function typeLegendAnchor(type: string): string {
	return `type-${type}`;
}

/**
 * Index rows, shared by the page and rows.json. `href` is the event's own section;
 * `description` is HTML (overlay code spans) and `search` its plain text for the filter.
 */
export function gameEventRows(): Row[] {
	const { events, duplicates } = loadGameEventsData();
	return events.map((ev) => ({
		name: eventHeading(ev, duplicates),
		href: `#${ev.anchor}`,
		source: sourceStem(ev.source),
		fields: ev.fields.length,
		description: inlineCodeHtml(ev.description),
		search: ev.description,
	}));
}
