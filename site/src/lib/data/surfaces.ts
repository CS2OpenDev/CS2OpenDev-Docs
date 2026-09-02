import { join } from 'node:path';
import { readJsonFile, requireKeys, requireRows, siteDataDir } from '../paths';

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
	const file = join(siteDataDir(), 'surfaces.json');
	const raw = readJsonFile<RawSurfacesData>(file);
	requireKeys(file, raw, ['materials']);
	requireRows(file, raw.materials, 'materials', ['name', 'rows']);
	requireRows(file, raw.materials[0]!.rows, 'materials[0].rows', ['scope', 'source_file', 'properties']);
	cache = raw.materials;
	return cache;
}
