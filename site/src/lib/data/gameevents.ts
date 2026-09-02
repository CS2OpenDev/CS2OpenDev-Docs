import { join } from 'node:path';
import { siteDataDir, readJsonFile } from '../paths';

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
	cache = readJsonFile<RawGameEventsData>(join(siteDataDir(), 'gameevents.json'));
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
