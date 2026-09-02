import { join } from 'node:path';
import { readJsonFile, siteDataDir } from '../paths';

export interface SurfaceProperty {
	name: string;
	value: string;
}

export interface SurfaceRow {
	scope: string;
	source_file: string;
	properties: SurfaceProperty[];
}

export interface SurfaceMaterial {
	name: string;
	rows: SurfaceRow[];
}

interface RawSurfacesData {
	materials: SurfaceMaterial[];
}

let cache: SurfaceMaterial[] | undefined;

export function loadSurfaceMaterials(): SurfaceMaterial[] {
	if (cache) return cache;
	const raw = readJsonFile<RawSurfacesData>(join(siteDataDir(), 'surfaces.json'));
	cache = raw.materials;
	return cache;
}
