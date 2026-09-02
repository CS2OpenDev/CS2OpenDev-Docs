import { readFileSync } from 'node:fs';
import { basename, join } from 'node:path';
import { ARTIFACT_DIR, findRepoRoot } from '../../scripts/repo-root.mjs';

let repoRootCache: string | undefined;

export function repoRoot(): string {
	repoRootCache ??= findRepoRoot();
	return repoRootCache;
}

/** docs/generated/downstream-codegen-schemas, the codegen artifact tree. */
export function codegenDir(): string {
	return join(repoRoot(), ARTIFACT_DIR);
}

/** docs/generated/data, the per-family site bundle produced alongside the codegen tree. */
export function siteDataDir(): string {
	return join(repoRoot(), 'docs', 'generated', 'data');
}

export function readJsonFile<T>(path: string): T {
	return JSON.parse(readFileSync(path, 'utf8')) as T;
}

/**
 * The bundle's interfaces are hand-written, so a renamed or dropped key would
 * render as a blank cell. These fail the build naming the file and the key.
 */
export function requireKeys(file: string, obj: unknown, keys: readonly string[], label = 'top level'): void {
	if (obj === null || typeof obj !== 'object') {
		throw new Error(`${basename(file)}: ${label} is not an object`);
	}
	for (const key of keys) {
		if (!(key in obj)) throw new Error(`${basename(file)}: ${label} has no key "${key}"`);
	}
}

/** A main array must be non-empty, and its first record must carry the keys the reader uses. */
export function requireRows(file: string, rows: unknown, label: string, keys: readonly string[]): void {
	if (!Array.isArray(rows) || rows.length === 0) {
		throw new Error(`${basename(file)}: ${label} is empty or not an array`);
	}
	requireKeys(file, rows[0], keys, `${label}[0]`);
}
