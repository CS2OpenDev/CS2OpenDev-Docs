import { cpSync, existsSync, mkdirSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';

const SOURCE = join('docs', 'generated', 'downstream-codegen-schemas');
const TARGET = join('public', 'generated', 'downstream-codegen-schemas');

function findRepoRoot() {
	if (process.env.CS2_DOCS_ROOT) return process.env.CS2_DOCS_ROOT;
	let dir = process.cwd();
	for (let i = 0; i < 8; i++) {
		if (existsSync(join(dir, SOURCE))) return dir;
		const up = dirname(dir);
		if (up === dir) break;
		dir = up;
	}
	throw new Error(`Could not find ${SOURCE} above ${process.cwd()}. Set CS2_DOCS_ROOT.`);
}

const from = join(findRepoRoot(), SOURCE);
const to = join(process.cwd(), TARGET);

rmSync(to, { recursive: true, force: true });
mkdirSync(dirname(to), { recursive: true });
cpSync(from, to, { recursive: true });
console.log(`copied ${from} -> ${to}`);
