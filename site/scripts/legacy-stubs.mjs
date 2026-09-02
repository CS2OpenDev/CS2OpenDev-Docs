// @ts-check
// Astro writes each `redirects` entry as dist/<path>/index.html with a meta refresh.
// The old Jekyll site served every page as <path>.html, and GitHub Pages answers a
// missing file with a 404 status, so each stub gets a sibling <path>.html as well.
// Both carry a script that forwards the fragment, which a meta refresh drops.

import { existsSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const REFRESH_RE = /http-equiv=["']refresh["'][^>]*?content=["']\d+;\s*url=([^"']+)["']/i;
const CANONICAL_RE = /<link[^>]*?rel=["']canonical["'][^>]*?href=["']([^"']+)["']/i;

/** @param {string} s */
function escapeHtml(s) {
	return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

/**
 * @param {string} to site-absolute destination
 * @param {string} canonical
 */
function stubHtml(to, canonical) {
	// `<` keeps a `</script>` in the destination from ending the script.
	const js = JSON.stringify(to).replace(/</g, '\\u003c');
	return [
		'<!doctype html>',
		'<html lang="en">',
		'<head>',
		'<meta charset="utf-8">',
		`<title>Redirecting to ${escapeHtml(to)}</title>`,
		`<script>location.replace(${js}+location.hash)</script>`,
		`<meta http-equiv="refresh" content="0;url=${escapeHtml(to)}">`,
		'<meta name="robots" content="noindex">',
		`<link rel="canonical" href="${escapeHtml(canonical)}">`,
		'</head>',
		'<body>',
		`<a href="${escapeHtml(to)}">Redirecting to ${escapeHtml(to)}</a>`,
		'</body>',
		'</html>',
		'',
	].join('\n');
}

/**
 * @param {string} dir
 * @param {string[]} out
 */
function collectIndexFiles(dir, out) {
	for (const entry of readdirSync(dir, { withFileTypes: true })) {
		const full = join(dir, entry.name);
		if (entry.isDirectory()) collectIndexFiles(full, out);
		else if (entry.name === 'index.html') out.push(full);
	}
}

/** @returns {import('astro').AstroIntegration} */
export function legacyHtmlStubs() {
	return {
		name: 'legacy-html-stubs',
		hooks: {
			'astro:build:done': ({ dir, logger }) => {
				const root = join(fileURLToPath(dir), 'generated');
				if (!existsSync(root)) return;
				/** @type {string[]} */
				const files = [];
				collectIndexFiles(root, files);
				let count = 0;
				for (const file of files) {
					const html = readFileSync(file, 'utf8');
					const refresh = REFRESH_RE.exec(html);
					if (!refresh) continue;
					const to = refresh[1];
					const canonical = CANONICAL_RE.exec(html)?.[1] ?? to;
					const stub = stubHtml(to, canonical);
					writeFileSync(file, stub);
					writeFileSync(`${dirname(file)}.html`, stub);
					count++;
				}
				logger.info(`wrote ${count} legacy .html stubs under generated/`);
			},
		},
	};
}
