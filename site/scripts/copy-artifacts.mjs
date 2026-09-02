import { cpSync, mkdirSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { ARTIFACT_DIR, findRepoRoot } from './repo-root.mjs';

const TARGET = join('public', 'generated', 'downstream-codegen-schemas');

const from = join(findRepoRoot(), ARTIFACT_DIR);
const to = join(process.cwd(), TARGET);

rmSync(to, { recursive: true, force: true });
mkdirSync(dirname(to), { recursive: true });
cpSync(from, to, { recursive: true });
console.log(`copied ${from} -> ${to}`);
