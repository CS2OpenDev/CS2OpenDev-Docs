// import.meta.env is absent when this module is loaded outside Vite (config-time scripts).
const base = (import.meta.env?.BASE_URL ?? '/').replace(/\/$/, '');

export function withBase(path: string): string {
	return `${base}/${path.replace(/^\//, '')}`;
}

/** '::' is the only character in a type name that a URL path cannot carry. */
export function entitySlug(name: string): string {
	return name.replace(/::/g, '.');
}

export function schemasHref(): string {
	return withBase('/schemas/');
}

export function moduleHref(module: string): string {
	return withBase(`/schemas/${module}/`);
}

export function moduleHierarchyHref(module: string): string {
	return withBase(`/schemas/${module}/hierarchy/`);
}

/** The combined server + client inheritance tree, replacing the old server_hierarchy diagram. */
export function hierarchyHref(): string {
	return withBase('/schemas/hierarchy/');
}

export function entityHref(module: string, name: string): string {
	return withBase(`/schemas/${module}/${entitySlug(name)}/`);
}

export function codegenArtifactHref(file: string): string {
	return withBase(`/generated/downstream-codegen-schemas/${file}`);
}

/** Proto files are keyed by stem; strip a `.proto` suffix so callers can pass either form. */
function protoStem(file: string): string {
	return file.replace(/\.proto$/, '');
}

export function protoFileHref(stem: string): string {
	return withBase(`/protobufs/${protoStem(stem)}/`);
}

export function protoMessageHref(file: string, qualified: string): string {
	return withBase(`/protobufs/${protoStem(file)}/#${qualified}`);
}

export function protoEnumHref(file: string, qualified: string): string {
	return withBase(`/protobufs/${protoStem(file)}/#${qualified}`);
}

export function networkHref(): string {
	return withBase('/network-messages/');
}

export function itemsHref(): string {
	return withBase('/items/');
}

export function itemAnchorHref(name: string): string {
	return withBase(`/items/#${encodeURIComponent(name)}`);
}

export function paintKitsHref(): string {
	return withBase('/items/paint-kits/');
}

export function stickerKitsHref(): string {
	return withBase('/items/sticker-kits/');
}

export function musicKitsHref(): string {
	return withBase('/items/music-kits/');
}

export function mapsHref(): string {
	return withBase('/maps/');
}

export function gameModesHref(): string {
	return withBase('/game-modes/');
}

export function gameModeAnchorHref(modeId: string): string {
	return withBase(`/game-modes/#${modeId}`);
}

export function propsHref(): string {
	return withBase('/props/');
}

export function surfacesHref(): string {
	return withBase('/surfaces/');
}

export function surfaceMaterialSlug(name: string): string {
	return name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
}

export function surfaceMaterialAnchorHref(name: string): string {
	return withBase(`/surfaces/#${surfaceMaterialSlug(name)}`);
}

export function modulesHref(): string {
	return withBase('/modules/');
}

export function changelogHref(): string {
	return withBase('/changelog/');
}

export function schemaHistoryHref(): string {
	return withBase('/schema-history/');
}

/** `changelog.json`'s `schema_history_anchor` and a transition's own `anchor` are both
 * bare `<from>-<to>`; both pages prefix it with `t-` so the id is a valid CSS selector. */
export function schemaHistoryTransitionAnchorHref(anchor: string): string {
	return withBase(`/schema-history/#t-${anchor}`);
}

export function codegenSchemasHref(): string {
	return withBase('/codegen-schemas/');
}

export function convarsHref(): string {
	return withBase('/convars/');
}

export function convarAnchorHref(name: string): string {
	return withBase(`/convars/#${encodeURIComponent(name)}`);
}

export function commandsHref(): string {
	return withBase('/commands/');
}

export function commandAnchorHref(name: string): string {
	return withBase(`/commands/#${encodeURIComponent(name)}`);
}

export function gameEventsHref(): string {
	return withBase('/game-events/');
}

export function gameEventAnchorHref(anchor: string): string {
	return withBase(`/game-events/#${anchor}`);
}
