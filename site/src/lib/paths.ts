import { readFileSync } from 'node:fs';
import { join } from 'node:path';
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
