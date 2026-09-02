/**
 * Maps old Jekyll `/generated/...` URLs to their new Astro paths. No Node or DOM
 * imports here: astro.config.mjs calls this at build time to enumerate the static
 * redirect table, and 404.astro imports the same function into the client bundle
 * to route arbitrary `.html` requests that a static redirect table cannot list.
 */

/** Old top-level slug under /generated/ to the new top-level path. */
export const LEGACY_FLAT_PAGES: Record<string, string> = {
	convars: '/convars/',
	commands: '/commands/',
	gameevents: '/game-events/',
	network: '/network-messages/',
	items: '/items/',
	maps: '/maps/',
	gamemodes: '/game-modes/',
	props: '/props/',
	surfaces: '/surfaces/',
	modules: '/modules/',
	changelog: '/changelog/',
	'schema-history': '/schema-history/',
	protobufs: '/protobufs/',
	'downstream-codegen-schemas': '/codegen-schemas/',
};

export interface LegacyPathParams {
	/** Schema module names (projectName), for /generated/diagrams/<module>. */
	modules: readonly string[];
	/** Proto file stems without the .proto extension, for /generated/proto/<stem>. */
	protoStems: readonly string[];
}

/**
 * Maps one old path (no site base, `.html` optional) to its new path (also no base).
 * Returns null when nothing on the new site covers it. Entity and module pages under
 * /generated/schemas/... are handled by an exhaustive per-entity redirect table built
 * elsewhere, but the generic two- and three-segment shape below still matches them so
 * the 404 fallback can route deep links that predate that table too.
 */
export function mapLegacyPath(pathname: string, params: LegacyPathParams): string | null {
	const path = pathname.replace(/\.html$/i, '').replace(/\/+$/, '');
	const parts = path.split('/').filter(Boolean);
	if (parts[0] !== 'generated') return null;
	const rest = parts.slice(1);

	if (rest.length === 0) return '/schemas/';

	if (rest[0] === 'schemas') {
		if (rest.length === 1) return '/schemas/';
		if (rest.length === 2) return `/schemas/${rest[1]}/`;
		if (rest.length === 3) return `/schemas/${rest[1]}/${rest[2]}/`;
		return null;
	}

	if (rest[0] === 'proto' && rest.length === 2) {
		return params.protoStems.includes(rest[1]!) ? `/protobufs/${rest[1]}/` : null;
	}

	if (rest[0] === 'diagrams' && rest.length === 2) {
		if (rest[1] === 'server_hierarchy') return '/schemas/hierarchy/';
		return params.modules.includes(rest[1]!) ? `/schemas/${rest[1]}/hierarchy/` : null;
	}

	// downstream-codegen-schemas is deliberately not matched past one segment: the JSON
	// artifacts under it are mirrored to the same path by copy-artifacts.mjs and must
	// keep resolving directly rather than bouncing through /codegen-schemas/.
	if (rest.length === 1) {
		const target = LEGACY_FLAT_PAGES[rest[0]!];
		if (target) return target;
	}

	return null;
}

/**
 * Every statically enumerable old path this function maps, for astro.config.mjs to
 * turn into literal redirect entries (Astro cannot expand a dynamic redirect pattern
 * and prefix `base` on the destination at the same time).
 */
export function enumerateLegacyRedirects(params: LegacyPathParams): Array<{ from: string; to: string }> {
	const from = [
		...Object.keys(LEGACY_FLAT_PAGES).map((slug) => `/generated/${slug}`),
		...params.protoStems.map((stem) => `/generated/proto/${stem}`),
		...params.modules.map((module) => `/generated/diagrams/${module}`),
		'/generated/diagrams/server_hierarchy',
	];
	return from.map((path) => {
		const to = mapLegacyPath(path, params);
		if (!to) throw new Error(`legacy-paths: no mapping produced for ${path}`);
		return { from: path, to };
	});
}
