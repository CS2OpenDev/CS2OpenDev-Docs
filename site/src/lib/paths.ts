import { existsSync, readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';

const ARTIFACT_DIR = join('docs', 'generated', 'downstream-codegen-schemas');

/**
 * Walk up from the working directory looking for the generator's output tree.
 * import.meta.url resolves inside dist/.prerender during a build, so it cannot
 * be used to anchor this.
 */
function findRepoRoot(): string {
	const override = process.env.CS2_DOCS_ROOT;
	if (override) return resolve(override);
	let dir = process.cwd();
	for (let i = 0; i < 8; i++) {
		if (existsSync(join(dir, ARTIFACT_DIR))) return dir;
		const up = dirname(dir);
		if (up === dir) break;
		dir = up;
	}
	throw new Error(
		`Could not find ${ARTIFACT_DIR} above ${process.cwd()}. Set CS2_DOCS_ROOT to the repository root.`
	);
}

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
