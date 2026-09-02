import { existsSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';

/** docs/generated/downstream-codegen-schemas, relative to the repository root. */
export const ARTIFACT_DIR = join('docs', 'generated', 'downstream-codegen-schemas');

/**
 * Walk up from the working directory looking for the generator's output tree.
 * import.meta.url resolves inside dist/.prerender during a build, so it cannot
 * be used to anchor this.
 * @returns {string}
 */
export function findRepoRoot() {
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
