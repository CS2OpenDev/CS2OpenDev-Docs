import { existsSync } from 'node:fs';
import { join } from 'node:path';
import type { Row } from '../../components/islands/DataTable';
import { readJsonFile, requireKeys, requireRows, siteDataDir } from '../paths';
import { entityIoClassHref } from '../urls';
import type { SchemaRef } from './cs_script';

export interface EntityPort {
	name: string;
	param_type: string;
	description: string;
	declared_in: string;
}

export interface EntityKeyvalue {
	name: string;
	type: string;
	display_name: string;
	default_value: string;
	description: string;
	declared_in: string;
	choices: { value: string; label: string }[];
	flags: { value: number; label: string; default: boolean }[];
}

export interface EntityClass {
	name: string;
	class_type: string;
	description: string;
	bases: string[];
	helpers: string[];
	source_file: string;
	schema: SchemaRef | null;
	script_type: string | null;
	keyvalues: EntityKeyvalue[];
	inputs: EntityPort[];
	outputs: EntityPort[];
}

export interface EntityIo {
	build_id: string;
	root: string;
	sources: string[];
	base_class_count: number;
	excluded: string[];
	classes: EntityClass[];
}

let cache: EntityIo | null | undefined;

/** null when the build carries no entity_io.json (Linux, or an older extract). */
export function loadEntityIo(): EntityIo | null {
	if (cache !== undefined) return cache;
	const file = join(siteDataDir(), 'entity_io.json');
	if (!existsSync(file)) {
		cache = null;
		return cache;
	}
	const raw = readJsonFile<EntityIo>(file);
	requireKeys(file, raw, ['build_id', 'root', 'sources', 'base_class_count', 'excluded', 'classes']);
	requireRows(file, raw.classes, 'classes', [
		'name',
		'class_type',
		'description',
		'bases',
		'source_file',
		'schema',
		'script_type',
		'keyvalues',
		'inputs',
		'outputs',
	]);
	cache = raw;
	return cache;
}

/** Index rows, shared by the page and rows.json. */
export function entityIoRows(): Row[] {
	const io = loadEntityIo();
	if (!io) return [];
	return io.classes.map((c) => ({
		name: c.name,
		href: entityIoClassHref(c.name),
		class_type: c.class_type.replace(/Class$/, ''),
		keyvalues: c.keyvalues.length,
		inputs: c.inputs.length,
		outputs: c.outputs.length,
		script_type: c.script_type ?? '',
		description: c.description,
	}));
}
