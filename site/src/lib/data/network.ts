import { join } from 'node:path';
import { siteDataDir, readJsonFile, requireKeys, requireRows } from '../paths';
import { fileForType, loadProtoIndex } from './protobufs';

export type NetworkBinding = 'rtti' | 'enum' | 'both';

export interface NetworkRow {
	id: number;
	name: string;
	group: string;
	enum: string | null;
	constant: string | null;
	direction: string | null;
	binding: NetworkBinding;
	type_exists: boolean;
	description: string;
}

interface RawNetworkData {
	rows: NetworkRow[];
}

let cache: NetworkRow[] | undefined;

export function loadNetworkRows(): NetworkRow[] {
	if (cache) return cache;
	const file = join(siteDataDir(), 'network.json');
	const raw = readJsonFile<RawNetworkData>(file);
	requireKeys(file, raw, ['rows']);
	requireRows(file, raw.rows, 'rows', [
		'id',
		'name',
		'group',
		'enum',
		'constant',
		'direction',
		'binding',
		'type_exists',
		'description',
	]);
	cache = raw.rows;
	return cache;
}

/** Reading order: connection/channel messages first, then the id-table families, demo last. */
const GROUP_ORDER = [
	'Bidirectional',
	'NetMessages',
	'ClcMessages',
	'SvcMessages',
	'ClientMessages',
	'PeerToPeer',
	'UserMessages',
	'TempEntities',
	'Decals',
	'Sounds',
	'Source1Legacy',
	'GameEvents',
	'Demo stream',
];

export interface NetworkGroup {
	group: string;
	/** Stable heading id: the group name lowercased with runs of non-alphanumerics collapsed to '-'. */
	slug: string;
	rows: NetworkRow[];
}

export function slugifyGroup(group: string): string {
	return group
		.toLowerCase()
		.replace(/[^a-z0-9]+/g, '-')
		.replace(/^-+|-+$/g, '');
}

/** Rows keyed by (group, id, name): an id is only unique within its group, and one id can bind more than one message. */
export function groupedRows(): NetworkGroup[] {
	const rows = loadNetworkRows();
	const byGroup = new Map<string, NetworkRow[]>();
	for (const r of rows) {
		const list = byGroup.get(r.group);
		if (list) list.push(r);
		else byGroup.set(r.group, [r]);
	}
	for (const list of byGroup.values()) {
		list.sort((a, b) => a.id - b.id || a.name.localeCompare(b.name));
	}
	const known = GROUP_ORDER.filter((g) => byGroup.has(g));
	const rest = [...byGroup.keys()].filter((g) => !GROUP_ORDER.includes(g)).sort();
	return [...known, ...rest].map((group) => ({ group, slug: slugifyGroup(group), rows: byGroup.get(group)! }));
}

/** The proto file a row's message lives in, when the message exists in this build's descriptor set. */
export function rowMessageFile(row: NetworkRow): string | undefined {
	if (!row.type_exists) return undefined;
	return fileForType(loadProtoIndex(), row.name);
}
