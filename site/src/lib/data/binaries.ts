import { join } from 'node:path';
import { readJsonFile, siteDataDir } from '../paths';

export interface BinaryModule {
	path: string;
	stem: string;
	file_size: string;
	sha256: string;
	export_count: number;
	resolved_interfaces: string[];
	schema_module: string | null;
	schema_registration_count: number;
}

interface RawModulesData {
	modules: BinaryModule[];
}

let cache: BinaryModule[] | undefined;

export function loadBinaries(): BinaryModule[] {
	if (cache) return cache;
	const raw = readJsonFile<RawModulesData>(join(siteDataDir(), 'modules.json'));
	cache = raw.modules;
	return cache;
}

export function formatFileSize(raw: string): string {
	const n = Number.parseInt(raw, 10);
	if (!Number.isFinite(n)) return raw;
	if (n < 1024) return `${n} B`;
	if (n < 1024 * 1024) return `${(n / 1024).toFixed(1)} KB`;
	return `${(n / (1024 * 1024)).toFixed(1)} MB`;
}
