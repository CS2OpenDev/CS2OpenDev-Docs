// @ts-check
import { readdirSync } from 'node:fs';
import { join } from 'node:path';
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import starlight from '@astrojs/starlight';
import starlightBlog from 'starlight-blog';
import starlightSidebarTopics from 'starlight-sidebar-topics';
import { codegenDir } from './src/lib/paths';
import { loadSchemaIndex, pagedEntities } from './src/lib/data/schema';
import { entitySlug } from './src/lib/urls';
import { enumerateLegacyRedirects } from './src/lib/legacy-paths';

const BASE = '/CS2OpenDev-Docs';

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
 * Old Jekyll paths. Astro cannot enumerate params for a dynamic redirect in a static
 * build and does not prefix `base` on a redirect destination, so every stub is listed
 * with the base baked in. Entity and module stubs come from the live schema index;
 * everything else comes from src/lib/legacy-paths.ts, the same rules the 404 page
 * falls back to for `.html` requests this table does not cover.
 */
const redirects = {
	'/generated/schemas': `${BASE}/schemas/`,
};
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
	'(function(){function go(){var h=decodeURIComponent(location.hash.slice(1));',
	'if(!h||document.getElementById(h))return;',
	'var t=document.querySelector(\'[data-legacy-anchor="\'+h.replace(/"/g,\'\')+\'"]\');',
	'var l=h.toLowerCase(),all=document.querySelectorAll(\'[id]\'),i;',
	'if(!t){for(i=0;i<all.length;i++){if(all[i].id.toLowerCase()===l){t=all[i];break;}}}',
	'if(!t){for(i=0;i<all.length;i++){if(all[i].id.toLowerCase().indexOf(l+\'-\')===0){t=all[i];break;}}}',
	'if(!t)return;',
	'history.replaceState(history.state,\'\',location.pathname+location.search+\'#\'+t.id);',
	't.scrollIntoView();}',
	'if(document.readyState===\'loading\'){document.addEventListener(\'DOMContentLoaded\',go);}else{go();}',
	'window.addEventListener(\'hashchange\',go);})();',
].join('');

export default defineConfig({
	site: 'https://cs2opendev.github.io',
	base: BASE,
	// Parallel subset builds each need their own content cache.
	cacheDir: process.env.ASTRO_CACHE_DIR ?? './node_modules/.astro',
	redirects,
	integrations: [
		react(),
		starlight({
			title: 'CS2 Reference',
			// src/pages/404.astro carries the legacy-path redirect script.
			disable404Route: true,
			description: `CS2 entity schema, protobuf and console reference for build ${idx.provenance.buildId} (${idx.provenance.platform}).`,
			customCss: ['./src/styles/custom.css'],
			favicon: '/favicon.svg',
			head: [
				{ tag: 'meta', attrs: { name: 'theme-color', content: '#0b0e14' } },
				// Old Jekyll anchors were lowercased and duplicates got numeric suffixes;
				// the new ids keep case and use a source suffix. Resolve a missing hash by
				// data-legacy-anchor, then case-insensitive id, then id prefix.
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
				starlightSidebarTopics(
					[
						{
							// No icon: the topic switcher's icon wrapper alone is ~2 KB of inline
							// SVG path data repeated on every page, and there is only one topic.
							id: 'reference',
							label: 'Reference',
							link: '/',
							items: referenceSidebar,
						},
					],
					{
						// Entity, module and protobuf pages are src/pages routes, so the plugin
						// cannot infer their topic from the sidebar.
						topics: {
							reference: [
								'/schemas/**',
								'/protobufs/**',
								'/generated/**',
								'/convars/**',
								'/commands/**',
								'/game-events/**',
								'/network-messages/**',
								'/items/**',
								'/maps/**',
								'/game-modes/**',
								'/props/**',
								'/surfaces/**',
								'/modules/**',
								'/changelog/**',
								'/schema-history/**',
								'/codegen-schemas/**',
							],
						},
						exclude: ['/blog', '/blog/**', '/404'],
					}
				),
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
