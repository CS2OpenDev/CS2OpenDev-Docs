// Totals a built Astro site's output size and flags any page grown out of
// proportion to its content.
//
// Usage: node scripts/check-size.mjs [distDir]
//
// distDir defaults to "dist".

import { readdirSync, statSync } from 'node:fs';
import { join, posix, resolve } from 'node:path';

// GitHub Pages caps a published site at 1 GB; 400 MB leaves headroom for the
// image/font assets other page families will add later. schemas/ alone is
// 221 MB today and a second platform roughly doubles it, so that platform
// needs a per-page diet or its own site before it fits under the cap.
const MAX_TOTAL_BYTES = 400 * 1024 * 1024;

// Entity pages are printed in bulk from one schema; a sidebar bug once made
// every one of them carry the full 4,400-entry nav and pushed the site to
// 4.1 GB, with pages near 1 MB. The largest entity page is 156 KB today and
// grows with every upstream build; 512 KB still catches the sidebar case by
// a factor of two without tripping on an ordinary data change.
const MAX_ENTITY_PAGE_BYTES = 512 * 1024;

// Module indexes and hierarchy pages list every class in a module (server
// has 1,143), so they get the same ceiling as the other big tables.
const MAX_SCHEMA_INDEX_PAGE_BYTES = 1024 * 1024;

// ConVars, commands and items are legitimately large single-page tables;
// 3 MB is the ceiling for any other page family.
const MAX_OTHER_PAGE_BYTES = 3 * 1024 * 1024;

const TOP_N = 10;

function parseArgs(argv) {
	return argv[0] ?? 'dist';
}

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

function formatBytes(bytes) {
	if (bytes >= 1024 * 1024) return `${(bytes / (1024 * 1024)).toFixed(2)} MB`;
	if (bytes >= 1024) return `${(bytes / 1024).toFixed(1)} KB`;
	return `${bytes} B`;
}

// schemas/<module>/<Entity>/index.html is an entity page; schemas/index.html,
// schemas/<module>/index.html and the hierarchy pages are indexes.
function limitFor(rel) {
	if (!rel.startsWith('schemas/')) return MAX_OTHER_PAGE_BYTES;
	const parts = rel.split('/');
	const isEntity = parts.length === 4 && parts[3] === 'index.html' && parts[2] !== 'hierarchy';
	return isEntity ? MAX_ENTITY_PAGE_BYTES : MAX_SCHEMA_INDEX_PAGE_BYTES;
}

function main() {
	const distDir = parseArgs(process.argv.slice(2));
	const root = resolve(distDir);

	const allFiles = walkFiles(root);
	const sized = allFiles.map((rel) => ({ rel, bytes: statSync(join(root, rel)).size }));

	const totalBytes = sized.reduce((sum, f) => sum + f.bytes, 0);
	const pages = sized.filter((f) => f.rel.endsWith('.html'));

	const oversized = [];
	for (const page of pages) {
		const limit = limitFor(page.rel);
		if (page.bytes > limit) {
			oversized.push({ ...page, limit });
		}
	}

	const largest = [...pages].sort((a, b) => b.bytes - a.bytes).slice(0, TOP_N);

	console.log(`total size: ${formatBytes(totalBytes)} (limit ${formatBytes(MAX_TOTAL_BYTES)})`);
	console.log(`files: ${sized.length}, pages: ${pages.length}`);
	console.log('');
	console.log(`largest ${TOP_N} pages:`);
	for (const page of largest) {
		console.log(`  ${formatBytes(page.bytes).padStart(10)}  ${page.rel}`);
	}

	let failed = false;

	if (totalBytes > MAX_TOTAL_BYTES) {
		console.log('');
		console.log(`FAIL: total size ${formatBytes(totalBytes)} exceeds ${formatBytes(MAX_TOTAL_BYTES)}`);
		failed = true;
	}

	if (oversized.length > 0) {
		console.log('');
		console.log(`FAIL: ${oversized.length} page(s) exceed their size limit:`);
		for (const page of oversized) {
			console.log(`  ${page.rel}: ${formatBytes(page.bytes)} > ${formatBytes(page.limit)}`);
		}
		failed = true;
	}

	if (failed) process.exit(1);
}

main();
