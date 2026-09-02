import { join } from 'node:path';
import { readJsonFile, requireKeys, requireRows, siteDataDir } from '../paths';

export interface MapEntry {
	name: string;
	material: string;
	blockName: string;
	bombAX: string;
	bombAY: string;
	bombBX: string;
	bombBY: string;
	ctSpawnX: string;
	ctSpawnY: string;
	tSpawnX: string;
	tSpawnY: string;
	posX: string;
	posY: string;
	rotate: string;
	scale: string;
	zoom: string;
	properties: unknown[];
}

interface RawMapsData {
	map_names: string[];
	note: string;
	maps: MapEntry[];
}

export interface MapsIndex {
	maps: MapEntry[];
	note: string;
}

let cache: MapsIndex | undefined;

export function loadMaps(): MapsIndex {
	if (cache) return cache;
	const file = join(siteDataDir(), 'maps.json');
	const raw = readJsonFile<RawMapsData>(file);
	requireKeys(file, raw, ['map_names', 'note', 'maps']);
	requireRows(file, raw.maps, 'maps', [
		'name',
		'material',
		'blockName',
		'bombAX',
		'bombAY',
		'bombBX',
		'bombBY',
		'ctSpawnX',
		'ctSpawnY',
		'tSpawnX',
		'tSpawnY',
		'posX',
		'posY',
		'rotate',
		'scale',
		'zoom',
		'properties',
	]);
	cache = { maps: raw.maps, note: raw.note };
	return cache;
}
