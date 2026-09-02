// @ts-check
import { readdirSync } from 'node:fs';
import { join } from 'node:path';
import { defineConfig, passthroughImageService } from 'astro/config';
import preact from '@astrojs/preact';
import starlight from '@astrojs/starlight';
import starlightBlog from 'starlight-blog';
import { codegenDir } from './src/lib/paths';
import { loadSchemaIndex, pagedEntities } from './src/lib/data/schema';
import { entitySlug } from './src/lib/urls';
import { enumerateLegacyRedirects } from './src/lib/legacy-paths';
import { BASE } from './scripts/site-base.mjs';
import { legacyHtmlStubs } from './scripts/legacy-stubs.mjs';

const idx = loadSchemaIndex();

const protoFiles = readdirSync(join(codegenDir(), 'proto'))
	.filter((f) => f.endsWith('.proto'))
	.sort();
const protoStems = protoFiles.map((f) => f.replace(/\.proto$/, ''));

/**
 * A hand-written sidebar with one link per module or proto file renders 927 KB of
 * identical markup on every one of 4,440 pages. The six largest modules and ten
 * proto files parsers actually reach for get a direct link; everything else is one
 * click away on the index page for its group.
 */
const topModules = [...idx.modules]
	.sort((a, b) => (idx.byModule.get(b)?.length ?? 0) - (idx.byModule.get(a)?.length ?? 0))
	.slice(0, 6)
	.sort();

const coreProtoStems = [
	'demo',
	'netmessages',
	'networkbasetypes',
	'network_connection',
	'usermessages',
	'cstrike15_usermessages',
	'cs_usercmd',
	'usercmd',
	'gameevents',
	'cs_gameevents',
].filter((stem) => protoStems.includes(stem));

/** Flat pages owned by other page families. Order is the reading order, not alphabetical. */
const flatPages = [
	['ConVars', '/convars/'],
	['Commands', '/commands/'],
	['Game Events', '/game-events/'],
	['Network Messages', '/network-messages/'],
	['Items', '/items/'],
	['Maps', '/maps/'],
	['Game Modes', '/game-modes/'],
	['Props', '/props/'],
	['Surfaces', '/surfaces/'],
	['Modules', '/modules/'],
	['Changelog', '/changelog/'],
	['Schema History', '/schema-history/'],
	['Codegen Schemas', '/codegen-schemas/'],
];

const referenceSidebar = [
	{ label: 'Home', link: '/' },
	{
		label: 'Schemas',
		collapsed: true,
		items: [
			{ label: 'All modules', link: '/schemas/' },
			...topModules.map((m) => ({ label: m, link: `/schemas/${m}/` })),
			{ label: 'Hierarchy', link: '/schemas/hierarchy/' },
		],
	},
	{
		label: 'Protobufs',
		collapsed: true,
		items: [
			{ label: 'All files', link: '/protobufs/' },
			...coreProtoStems.map((stem) => ({ label: `${stem}.proto`, link: `/protobufs/${stem}/` })),
		],
	},
	...flatPages.map(([label, link]) => ({ label, link })),
];

/**
 * Old Jekyll paths. Astro does not prefix `base` on a redirect destination, so a
 * dynamic `[module]/[entity]` rule would point at the unprefixed path; every stub is
 * listed literally with the base baked in. Entity and module stubs come from the live
 * schema index; everything else comes from src/lib/legacy-paths.ts, the same rules
 * the 404 page falls back to for `.html` requests this table does not cover.
 */
const redirects = /** @type {Record<string, string>} */ ({
	'/generated/schemas': `${BASE}/schemas/`,
});
for (const module of idx.modules) {
	redirects[`/generated/schemas/${module}`] = `${BASE}/schemas/${module}/`;
}
for (const ent of pagedEntities(idx)) {
	const slug = entitySlug(ent.name);
	redirects[`/generated/schemas/${ent.module}/${slug}`] = `${BASE}/schemas/${ent.module}/${slug}/`;
}
for (const { from, to } of enumerateLegacyRedirects({ modules: idx.modules, protoStems })) {
	redirects[from] = `${BASE}${to}`;
}

const LEGACY_ANCHOR_SCRIPT = [
	'(function(){var all;',
	'function find(h){var t=document.getElementById(h);',
	'if(!t)t=document.querySelector(\'[data-legacy-anchor~="\'+CSS.escape(h)+\'"]\');',
	'if(!t){var l=h.toLowerCase(),i;for(i=0;i<all.length;i++){if(all[i].id.toLowerCase()===l){t=all[i];break;}}}',
	'return t;}',
	'function go(){var r=location.hash.slice(1),h;try{h=decodeURIComponent(r);}catch(e){h=r;}',
	'if(!h||document.getElementById(h))return;',
	'all=document.querySelectorAll(\'[id]\');',
	'var t=find(h),s=h.replace(/-+\\d+$/,\'\');',
	'if(!t&&s!==h)t=find(s);',
	'if(!t){var l=h.toLowerCase(),i;for(i=0;i<all.length;i++){if(all[i].id.toLowerCase().indexOf(l+\'-\')===0){t=all[i];break;}}}',
	'if(!t)return;',
	'history.replaceState(history.state,\'\',location.pathname+location.search+\'#\'+t.id);',
	't.scrollIntoView();}',
	'if(document.readyState===\'loading\'){document.addEventListener(\'DOMContentLoaded\',go);}else{go();}',
	'window.addEventListener(\'hashchange\',go);})();',
].join('');

export default defineConfig({
	site: 'https://cs2opendev.github.io',
	base: BASE,
	trailingSlash: 'always',
	redirects,
	// Astro inlines any stylesheet under 4 KB into every page that imports it;
	// on 4,390 entity pages that is about 18 MB of repeated CSS.
	build: { inlineStylesheets: 'never' },
	// Nothing on the site goes through astro:assets, so the build never needs sharp.
	image: { service: passthroughImageService() },
	integrations: [
		preact({ compat: true }),
		legacyHtmlStubs(),
		starlight({
			title: 'CS2 Reference',
			// src/pages/404.astro carries the legacy-path redirect script.
			disable404Route: true,
			description: `CS2 entity schema, protobuf and console reference for build ${idx.provenance.buildId} (${idx.provenance.platform}).`,
			customCss: ['./src/styles/custom.css'],
			sidebar: referenceSidebar,
			favicon: '/favicon.svg',
			head: [
				// Starlight's page grounds: white in light mode, hsl(224, 10%, 10%) in dark.
				{ tag: 'meta', attrs: { name: 'theme-color', media: '(prefers-color-scheme: light)', content: '#ffffff' } },
				{ tag: 'meta', attrs: { name: 'theme-color', media: '(prefers-color-scheme: dark)', content: '#17181c' } },
				// No og:image exists, so the large-image card would render an empty frame.
				{ tag: 'meta', attrs: { name: 'twitter:card', content: 'summary' } },
				// Old Jekyll anchors were lowercased, and a repeated or count-bearing
				// heading got a numeric suffix. Resolve a missing hash by data-legacy-anchor
				// (a space-separated list), then case-insensitive id, then the same three
				// with the trailing -N stripped, then id prefix.
				{ tag: 'script', content: LEGACY_ANCHOR_SCRIPT },
			],
			social: [
				{
					icon: 'github',
					label: 'GitHub',
					href: 'https://github.com/CS2OpenDev/CS2OpenDev-Docs',
				},
			],
			pagefind: {
				ranking: {
					// The corpus is mostly big memory-layout tables; a page that happens to
					// repeat a term in its rows should not outrank the page whose title is
					// that term. metaWeights.title does the real work; the other three keep a
					// long table from winning purely on raw term count.
					pageLength: 0.15,
					termFrequency: 0.05,
					termSaturation: 1,
					metaWeights: { title: 10 },
				},
			},
			plugins: [
				starlightBlog({
					title: 'Blog',
					prefix: 'blog',
					authors: {
						cs2opendev: { name: 'CS2OpenDev' },
					},
				}),
			],
		}),
	],
});
