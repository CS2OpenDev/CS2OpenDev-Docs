// Walks a built Astro site and checks every internal href/src resolves to a
// real file, and every fragment resolves to an id on its target page.
//
// Usage: node scripts/check-links.mjs [distDir] [--allow-missing-prefix <path-prefix>]...
//
// distDir defaults to "dist". --allow-missing-prefix is repeatable: a broken
// link whose resolved site-absolute path starts with one of these prefixes is
// reported as "skipped by prefix" instead of broken. That is for subset
// builds (SITE_SUBSET=n), which omit most entity pages on purpose.

import { readFileSync, readdirSync } from 'node:fs';
import { join, posix, resolve } from 'node:path';

// Must match the `BASE` constant in astro.config.mjs.
const BASE = '/CS2OpenDev-Docs';

const MAX_BROKEN_PRINTED = 50;

function parseArgs(argv) {
	let distDir = 'dist';
	let distDirSet = false;
	const allowMissingPrefixes = [];
	for (let i = 0; i < argv.length; i++) {
		const arg = argv[i];
		if (arg === '--allow-missing-prefix') {
			allowMissingPrefixes.push(argv[++i]);
		} else if (arg.startsWith('--allow-missing-prefix=')) {
			allowMissingPrefixes.push(arg.slice('--allow-missing-prefix='.length));
		} else if (!distDirSet) {
			distDir = arg;
			distDirSet = true;
		}
	}
	return { distDir, allowMissingPrefixes };
}

/** One readdir pass, relative POSIX paths for every file under root. */
function walkFiles(root) {
	const files = [];
	function recur(dir) {
		for (const entry of readdirSync(dir, { withFileTypes: true })) {
			const full = join(dir, entry.name);
			if (entry.isDirectory()) {
				recur(full);
			} else if (entry.isFile()) {
				files.push(posix.relative(root.replace(/\\/g, '/'), full.replace(/\\/g, '/')));
			}
		}
	}
	recur(root);
	return files;
}

/** dist-relative path (e.g. "schemas/foo/index.html") to its site URL, base included. */
function fileToUrl(rel) {
	if (rel === 'index.html') return `${BASE}/`;
	if (rel.endsWith('/index.html')) return `${BASE}/${rel.slice(0, -'index.html'.length)}`;
	return `${BASE}/${rel}`;
}

/** Site-absolute pathname (base already stripped) to a dist-relative file, or null. */
function resolveToFile(diskPath, allFiles) {
	const clean = diskPath === '' ? '/' : diskPath;
	const rel = clean.replace(/^\/+/, '');
	let candidates;
	if (clean.endsWith('/')) {
		candidates = [rel === '' ? 'index.html' : `${rel}index.html`];
	} else {
		const lastSegment = rel.slice(rel.lastIndexOf('/') + 1);
		if (lastSegment.includes('.')) {
			candidates = [rel];
		} else {
			candidates = [rel, `${rel}/index.html`, `${rel}.html`];
		}
	}
	for (const candidate of candidates) {
		if (allFiles.has(candidate)) return candidate;
	}
	return null;
}

function stripBase(pathname) {
	if (pathname === BASE) return '/';
	if (pathname.startsWith(`${BASE}/`)) return pathname.slice(BASE.length);
	return pathname;
}

const HREF_SRC_RE = /\s(?:href|src)=["']([^"']*)["']/g;
const ID_RE = /\sid=["']([^"']+)["']/g;
const REFRESH_STUB_RE = /http-equiv=["']refresh["']/i;

function classify(href) {
	if (href === '') return 'ignore';
	if (href.startsWith('#')) return 'fragment';
	if (href.startsWith('//')) return 'ignore'; // protocol-relative external
	if (/^[a-zA-Z][a-zA-Z0-9+.-]*:/.test(href)) return 'ignore'; // has a scheme: http(s), mailto, data, javascript, tel...
	return 'internal';
}

function main() {
	const { distDir, allowMissingPrefixes } = parseArgs(process.argv.slice(2));
	const root = resolve(distDir);

	const allFilesList = walkFiles(root);
	const allFiles = new Set(allFilesList);
	const htmlFiles = allFilesList.filter((f) => f.endsWith('.html'));

	// Phase 1: read every HTML file once. Record its URL, whether it's a
	// redirect stub, its id set, and its raw href/src values.
	const pages = new Map(); // rel path -> { url, isStub, ids, links }
	for (const rel of htmlFiles) {
		const content = readFileSync(join(root, rel), 'utf8');
		const isStub = REFRESH_STUB_RE.test(content);
		const ids = new Set();
		for (const m of content.matchAll(ID_RE)) ids.add(m[1]);
		const links = [];
		if (!isStub) {
			for (const m of content.matchAll(HREF_SRC_RE)) links.push(m[1]);
		}
		pages.set(rel, { url: fileToUrl(rel), isStub, ids, links });
	}

	// Phase 2: resolve every link against the in-memory data. No further I/O.
	let linkCount = 0;
	let internalCount = 0;
	let anchorCount = 0;
	let skippedByPrefixCount = 0;
	const broken = [];

	for (const [rel, page] of pages) {
		for (const href of page.links) {
			linkCount++;
			const kind = classify(href);
			if (kind === 'ignore') continue;

			if (kind === 'fragment') {
				anchorCount++;
				const id = href.slice(1);
				if (id !== '' && !page.ids.has(id)) {
					broken.push({ file: rel, href, reason: `missing anchor #${id} on self` });
				}
				continue;
			}

			internalCount++;
			const resolved = new URL(href, `http://x${page.url}`);
			const diskPath = stripBase(resolved.pathname);
			const target = resolveToFile(diskPath, allFiles);

			if (target === null) {
				if (allowMissingPrefixes.some((p) => resolved.pathname.startsWith(p))) {
					skippedByPrefixCount++;
				} else {
					broken.push({ file: rel, href, reason: `no such page or asset: ${resolved.pathname}` });
				}
				continue;
			}

			if (resolved.hash && resolved.hash.length > 1 && target.endsWith('.html') && !target.startsWith('pagefind/')) {
				anchorCount++;
				const targetPage = pages.get(target);
				const id = resolved.hash.slice(1);
				if (targetPage && !targetPage.ids.has(id)) {
					broken.push({ file: rel, href, reason: `missing anchor #${id} on ${target}` });
				}
			}
		}
	}

	const stubCount = [...pages.values()].filter((p) => p.isStub).length;

	console.log(`pages scanned: ${pages.size} (${stubCount} redirect stubs skipped as link sources)`);
	console.log(`links found: ${linkCount} (${internalCount} internal, checked)`);
	console.log(`anchors checked: ${anchorCount}`);
	console.log(`skipped by prefix: ${skippedByPrefixCount}`);
	console.log(`broken: ${broken.length}`);

	if (broken.length > 0) {
		console.log('');
		for (const entry of broken.slice(0, MAX_BROKEN_PRINTED)) {
			console.log(`  ${entry.file}: ${entry.href}  (${entry.reason})`);
		}
		if (broken.length > MAX_BROKEN_PRINTED) {
			console.log(`  ... and ${broken.length - MAX_BROKEN_PRINTED} more`);
		}
		process.exit(1);
	}
}

main();
