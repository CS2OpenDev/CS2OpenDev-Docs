import { join } from 'node:path';
import { readJsonFile, siteDataDir } from '../paths';

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
	const raw = readJsonFile<RawMapsData>(join(siteDataDir(), 'maps.json'));
	cache = { maps: raw.maps, note: raw.note };
	return cache;
}
