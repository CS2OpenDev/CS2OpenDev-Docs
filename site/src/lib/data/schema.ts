import { join } from 'node:path';
import { codegenDir, readJsonFile } from '../paths';
import { escapeHtml, toInt } from '../html';
import { entityHref, entitySlug } from '../urls';

export interface RawType {
	category: string;
	name: string;
	module?: string;
	count?: string;
	atomicCategory?: string;
	inner?: RawType;
}
export interface RawMeta {
	name: string;
	value?: string;
}
export interface Annotations {
	description?: string;
	notes?: string;
	warning?: string;
}
export interface RawField {
	name: string;
	offset: string;
	type: RawType;
	metadata: RawMeta[];
	typeModule?: string;
	annotations?: Annotations;
}
export interface RawParent {
	name: string;
	module: string;
	offset: number;
}
export interface RawClass {
	name: string;
	module: string;
	projectName: string;
	cppName?: string;
	size: string;
	alignment: number;
	flags: number;
	flags2?: number;
	parents: RawParent[];
	fields: RawField[];
	metadata: RawMeta[];
	staticFields?: unknown[];
	singleInheritanceDepth?: number;
	multipleInheritanceDepth?: number;
	annotations?: Annotations;
	diagram_url?: string;
}
export interface RawEnumMember {
	name: string;
	value: string;
	metadata: RawMeta[];
	annotations?: Annotations;
}
export interface RawEnum {
	name: string;
	module: string;
	projectName: string;
	/** Underlying integer type, for example uint32_t. */
	alignment: string;
	size: number;
	flags: number;
	members: RawEnumMember[];
	annotations?: Annotations;
}
export interface RawSchema {
	schema_format_version: string;
	generator: string;
	build_id: number;
	platform: string;
	revision: string;
	version_date: string;
	version_time: string;
	classes: RawClass[];
	enums: RawEnum[];
}

export interface Provenance {
	buildId: number;
	platform: string;
	versionDate: string;
	versionTime: string;
	revision: string;
	schemaFormatVersion: string;
}

interface EntityCommon {
	/** `${module}/${name}`, unique across the artifact. */
	key: string;
	name: string;
	/** projectName: the coarse project axis (server, client, entity2, ...). */
	module: string;
	/** The binary the type was walked out of, for example server.dll. */
	binaryModule: string;
	slug: string;
	annotations?: Annotations;
}
export interface ClassEntity extends EntityCommon {
	kind: 'class';
	raw: RawClass;
}
export interface EnumEntity extends EntityCommon {
	kind: 'enum';
	raw: RawEnum;
}
export type Entity = ClassEntity | EnumEntity;

export interface LayoutRow {
	field: RawField;
	declaring: ClassEntity;
	inherited: boolean;
	offset: number | null;
	/** Bit index within the offset, for consecutive BITFIELD rows sharing an offset. */
	bit: number | null;
	bitWidth: number | null;
}

export interface Layout {
	rows: LayoutRow[];
	/** Non-primary bases, whose fields the artifact does not place. */
	secondary: ClassEntity[];
	/** Declaring classes in spine order, root last. */
	spine: ClassEntity[];
	ownCount: number;
}

export interface SchemaIndex {
	provenance: Provenance;
	all: Entity[];
	classes: ClassEntity[];
	enums: EnumEntity[];
	byKey: Map<string, Entity>;
	byName: Map<string, Entity[]>;
	byModule: Map<string, Entity[]>;
	/** Direct subclasses, keyed by the resolved parent's entity key. */
	children: Map<string, ClassEntity[]>;
	/** Classes that reference a type in a field, keyed by the resolved target's key. */
	usedBy: Map<string, ClassEntity[]>;
	modules: string[];
	/** Bases that resolve outside the referring module because no local variant exists. */
	crossModuleBases: number;
}

const TYPE_REF = /[A-Z_]\w+(?:::\w+)*/g;

let cache: SchemaIndex | undefined;

export function loadSchemaIndex(): SchemaIndex {
	if (cache) return cache;
	const raw = readJsonFile<RawSchema>(join(codegenDir(), 'cs2_schema.json'));

	const classes: ClassEntity[] = raw.classes.map((c) => ({
		kind: 'class',
		key: `${c.projectName}/${c.name}`,
		name: c.name,
		module: c.projectName,
		binaryModule: c.module,
		slug: entitySlug(c.name),
		annotations: c.annotations,
		raw: c,
	}));
	const enums: EnumEntity[] = raw.enums.map((e) => ({
		kind: 'enum',
		key: `${e.projectName}/${e.name}`,
		name: e.name,
		module: e.projectName,
		binaryModule: e.module,
		slug: entitySlug(e.name),
		annotations: e.annotations,
		raw: e,
	}));
	const all: Entity[] = [...classes, ...enums];

	const byKey = new Map<string, Entity>();
	const byName = new Map<string, Entity[]>();
	const byModule = new Map<string, Entity[]>();
	for (const ent of all) {
		byKey.set(ent.key, ent);
		push(byName, ent.name, ent);
		push(byModule, ent.module, ent);
	}
	for (const list of byModule.values()) list.sort(byNameThenKind);
	const modules = [...byModule.keys()].sort();

	const idx: SchemaIndex = {
		provenance: {
			buildId: raw.build_id,
			platform: raw.platform,
			versionDate: raw.version_date,
			versionTime: raw.version_time,
			revision: raw.revision,
			schemaFormatVersion: raw.schema_format_version,
		},
		all,
		classes,
		enums,
		byKey,
		byName,
		byModule,
		children: new Map(),
		usedBy: new Map(),
		modules,
		crossModuleBases: 0,
	};

	for (const c of classes) {
		for (const p of c.raw.parents) {
			const pe = resolveClass(idx, p.name, [c.module], p.module);
			if (!pe) continue;
			if (pe.module !== c.module) idx.crossModuleBases++;
			push(idx.children, pe.key, c);
		}
	}
	for (const list of idx.children.values()) list.sort(byNameThenKind);

	buildUsedBy(idx);
	assertNoCrossProjectSpine(idx);

	cache = idx;
	return idx;
}

function push<T>(map: Map<string, T[]>, key: string, value: T): void {
	const list = map.get(key);
	if (list) list.push(value);
	else map.set(key, [value]);
}

function byNameThenKind(a: Entity, b: Entity): number {
	return a.name.localeCompare(b.name) || a.kind.localeCompare(b.kind);
}

/**
 * Same projectName wins, then the binary module recorded on the reference, then
 * the first variant. Preferring projectName is what keeps a server class from
 * walking into the client hierarchy for the 189 twinned names.
 */
export function resolveEntity(
	idx: SchemaIndex,
	name: string,
	prefer: readonly string[],
	binaryModule?: string
): Entity | undefined {
	const variants = idx.byName.get(name);
	if (!variants) return undefined;
	if (variants.length === 1) return variants[0];
	for (const module of prefer) {
		if (!module) continue;
		const hit = variants.find((v) => v.module === module);
		if (hit) return hit;
	}
	if (binaryModule) {
		const hit = variants.find((v) => v.binaryModule === binaryModule);
		if (hit) return hit;
	}
	return variants[0];
}

export function resolveClass(
	idx: SchemaIndex,
	name: string,
	prefer: readonly string[],
	binaryModule?: string
): ClassEntity | undefined {
	const ent = resolveEntity(idx, name, prefer, binaryModule);
	return ent && ent.kind === 'class' ? ent : undefined;
}

export function typeRefNames(typeName: string): string[] {
	const out: string[] = [];
	for (const m of typeName.matchAll(TYPE_REF)) {
		if (!out.includes(m[0])) out.push(m[0]);
	}
	return out;
}

function buildUsedBy(idx: SchemaIndex): void {
	const seen = new Map<string, Set<string>>();
	for (const c of idx.classes) {
		for (const f of c.raw.fields) {
			for (const refName of typeRefNames(f.type.name)) {
				const target = resolveEntity(idx, refName, [c.module], f.typeModule);
				if (!target || target.key === c.key) continue;
				let users = seen.get(target.key);
				if (!users) {
					users = new Set();
					seen.set(target.key, users);
				}
				if (users.has(c.key)) continue;
				users.add(c.key);
				push(idx.usedBy, target.key, c);
			}
		}
	}
	for (const list of idx.usedBy.values()) list.sort(byNameThenKind);
}

/**
 * The client and server binaries declare 189 identically named twins. Attributing
 * a server row to a client declaring class (the defect this site replaces) is a
 * hard error; a base that only exists in the other project is an upstream gap and
 * is only counted.
 */
function assertNoCrossProjectSpine(idx: SchemaIndex): void {
	const pair: Record<string, string> = { server: 'client', client: 'server' };
	const violations: string[] = [];
	for (const c of idx.classes) {
		const twin = pair[c.module];
		if (!twin) continue;
		for (const ancestor of spineOf(idx, c)) {
			if (ancestor.module !== twin) continue;
			const local = idx.byName.get(ancestor.name)?.some((v) => v.module === c.module);
			if (local) violations.push(`${c.key} -> ${ancestor.key}`);
		}
	}
	if (violations.length > 0) {
		throw new Error(
			`Cross-project base resolution: ${violations.length} class(es) attribute layout rows to the ` +
				`opposite project while a same-project variant exists. First: ${violations.slice(0, 5).join(', ')}`
		);
	}
}

/** Primary-parent chain above `ent`, nearest first. */
export function spineOf(idx: SchemaIndex, ent: ClassEntity): ClassEntity[] {
	const out: ClassEntity[] = [];
	const visited = new Set<string>([ent.key]);
	let cur: ClassEntity | undefined = ent;
	while (cur) {
		const p: RawParent | undefined = cur.raw.parents[0];
		if (!p) break;
		const next: ClassEntity | undefined = resolveClass(idx, p.name, [ent.module, cur.module], p.module);
		if (!next || visited.has(next.key)) break;
		visited.add(next.key);
		out.push(next);
		cur = next;
	}
	return out;
}

export function directParents(idx: SchemaIndex, ent: ClassEntity): { name: string; ent?: ClassEntity }[] {
	return ent.raw.parents.map((p) => ({
		name: p.name,
		ent: resolveClass(idx, p.name, [ent.module], p.module),
	}));
}

export function childrenOf(idx: SchemaIndex, ent: Entity): ClassEntity[] {
	return idx.children.get(ent.key) ?? [];
}

/** The same name under a different projectName, for example the client twin of a server class. */
export function twinsOf(idx: SchemaIndex, ent: Entity): Entity[] {
	return (idx.byName.get(ent.name) ?? []).filter((v) => v.key !== ent.key);
}

export function usersOf(idx: SchemaIndex, ent: Entity): ClassEntity[] {
	return idx.usedBy.get(ent.key) ?? [];
}

/** Own fields plus fields inherited along the primary-parent spine, ordered by absolute offset. */
export function flattenLayout(idx: SchemaIndex, ent: ClassEntity): Layout {
	const spine = spineOf(idx, ent);
	const rows: LayoutRow[] = [];
	const seenFields = new Set<string>();
	const secondary: ClassEntity[] = [];

	const add = (declaring: ClassEntity, inherited: boolean) => {
		for (const f of declaring.raw.fields) {
			if (seenFields.has(f.name)) continue;
			seenFields.add(f.name);
			rows.push({ field: f, declaring, inherited, offset: toInt(f.offset), bit: null, bitWidth: null });
		}
	};
	add(ent, false);
	const ownCount = rows.length;
	for (const anc of spine) add(anc, true);

	for (const cls of [ent, ...spine]) {
		for (const p of cls.raw.parents.slice(1)) {
			const se = resolveClass(idx, p.name, [ent.module, cls.module], p.module);
			if (se && !secondary.some((s) => s.key === se.key)) secondary.push(se);
		}
	}

	rows.sort((a, b) => {
		if (a.offset === null) return b.offset === null ? 0 : 1;
		if (b.offset === null) return -1;
		return a.offset - b.offset || a.field.name.localeCompare(b.field.name);
	});
	assignBitIndices(rows);
	return { rows, secondary, spine, ownCount };
}

/** Bit position accumulates across consecutive bitfield rows that share an offset. */
function assignBitIndices(rows: LayoutRow[]): void {
	let cursorOffset: number | null = null;
	let cursor = 0;
	for (const r of rows) {
		if (r.field.type.category !== 'BITFIELD' || r.offset === null) {
			cursorOffset = null;
			cursor = 0;
			continue;
		}
		const width = Number.parseInt(r.field.type.name.split(':')[1] ?? '1', 10) || 1;
		if (r.offset !== cursorOffset) {
			cursorOffset = r.offset;
			cursor = 0;
		}
		r.bit = cursor;
		r.bitWidth = width;
		cursor += width;
	}
}

/** Declared and inherited field counts without allocating rows, for index tables. */
export function layoutCounts(idx: SchemaIndex, ent: ClassEntity): { own: number; total: number } {
	const names = new Set<string>();
	for (const f of ent.raw.fields) names.add(f.name);
	const own = names.size;
	for (const anc of spineOf(idx, ent)) {
		for (const f of anc.raw.fields) names.add(f.name);
	}
	return { own, total: names.size };
}

/**
 * The annotation shown on a row: the field's own prose, or the declaring class's
 * prose for an inherited row, which is where 87% of rows live.
 */
export function rowAnnotation(row: LayoutRow): string {
	return row.field.annotations?.description?.trim() ?? '';
}

export function metaLabel(m: RawMeta): string {
	const v = (m.value ?? '').trim();
	return v ? `${m.name} ${v}` : m.name;
}

export function friendlyText(metas: RawMeta[] | undefined): string {
	if (!metas) return '';
	let friendly = '';
	let desc = '';
	for (const m of metas) {
		const v = (m.value ?? '').trim().replace(/^"|"$/g, '');
		if (m.name === 'MPropertyFriendlyName' && !friendly) friendly = v;
		else if (m.name === 'MPropertyDescription' && !desc) desc = v;
	}
	if (friendly && desc && friendly !== desc) return `${friendly}: ${desc}`;
	return friendly || desc;
}

export function kv3Defaults(ent: ClassEntity): string | undefined {
	const v = ent.raw.metadata.find((m) => m.name === 'MGetKV3ClassDefaults')?.value;
	return v && v.trim() ? v : undefined;
}

export function displayMetadata(ent: ClassEntity): string[] {
	return ent.raw.metadata
		.filter((m) => m.name && m.name !== 'MGetKV3ClassDefaults' && !m.name.startsWith('MNetworkVarNames'))
		.map(metaLabel);
}

/** Link every known type name inside a rendered type string. */
export function linkTypeHtml(idx: SchemaIndex, typeName: string, fromModule: string, binaryModule?: string): string {
	return escapeHtml(typeName).replace(TYPE_REF, (word) => {
		const target = resolveEntity(idx, word, [fromModule], binaryModule);
		if (!target) return word;
		return `<a href="${entityHref(target.module, target.name)}">${word}</a>`;
	});
}

/** Enum members are printed signed; unsigned underlying types also get the wrapped hex. */
export function enumValueDisplay(e: RawEnum, value: string): { value: string; hex?: string } {
	const unsigned = String(e.alignment).startsWith('uint');
	let n: bigint;
	try {
		n = BigInt(value);
	} catch {
		return { value };
	}
	if (!unsigned || n >= 0n) return { value };
	const bits = BigInt((e.size || 4) * 8);
	const wrapped = (n + (1n << bits)) % (1n << bits);
	return { value, hex: `0x${wrapped.toString(16).toUpperCase()}` };
}

/**
 * Search aliases: the identifier split on underscores and CamelCase boundaries so a
 * query for `PlayerPawn` reaches `C_CSPlayerPawn`.
 */
export function identifierAliases(name: string): string[] {
	const parts = new Set<string>();
	for (const chunk of name.split(/[_:]+/)) {
		if (!chunk) continue;
		if (chunk.length > 1) parts.add(chunk);
		const words = chunk
			.replace(/([a-z0-9])([A-Z])/g, '$1 $2')
			.replace(/([A-Z]+)([A-Z][a-z])/g, '$1 $2')
			.split(' ')
			.filter((w) => w.length > 1);
		for (const word of words) parts.add(word);
		// Adjacent pairs: search tokenises on whitespace, so PlayerPawn only reaches
		// CCSPlayerPawn if the pair is emitted as its own token.
		for (let i = 0; i + 1 < words.length; i++) parts.add(words[i]! + words[i + 1]!);
	}
	parts.delete(name);
	return [...parts];
}

export function subsetLimit(): number {
	const n = Number.parseInt(process.env.SITE_SUBSET ?? '', 10);
	return Number.isFinite(n) && n > 0 ? n : 0;
}

/** Entities that get a page, honouring SITE_SUBSET (first n per module). */
export function pagedEntities(idx: SchemaIndex): Entity[] {
	const limit = subsetLimit();
	if (!limit) return idx.all;
	const keys = new Set<string>();
	const out: Entity[] = [];
	for (const module of idx.modules) {
		for (const ent of (idx.byModule.get(module) ?? []).slice(0, limit)) {
			keys.add(ent.key);
			out.push(ent);
		}
	}
	// SITE_INCLUDE pins named pages into a subset build, for example server/CCSPlayerPawn.
	for (const key of (process.env.SITE_INCLUDE ?? '').split(',')) {
		const ent = idx.byKey.get(key.trim());
		if (ent && !keys.has(ent.key)) {
			keys.add(ent.key);
			out.push(ent);
		}
	}
	return out;
}

const COUNTERPART: Record<string, { module: string; map: (n: string) => string }[]> = {
	client: [{ module: 'server', map: (n) => (n.startsWith('C_') ? `C${n.slice(2)}` : n) }],
	server: [{ module: 'client', map: (n) => (n.startsWith('C') && !n.startsWith('C_') ? `C_${n.slice(1)}` : n) }],
};

/**
 * The client and server builds name the same concept `C_Foo` and `CFoo`. That is a
 * naming convention, not something the artifact records, so it is offered as a
 * separate link from the same-name twin.
 */
export function counterpartOf(idx: SchemaIndex, ent: Entity): Entity | undefined {
	for (const rule of COUNTERPART[ent.module] ?? []) {
		const name = rule.map(ent.name);
		if (name === ent.name) continue;
		const hit = idx.byName.get(name)?.find((v) => v.module === rule.module && v.kind === ent.kind);
		if (hit) return hit;
	}
	return undefined;
}

export interface StripSegment {
	offset: number;
	span: number;
	label: string;
	declaring?: ClassEntity;
	gap: boolean;
}

/**
 * One segment per distinct offset, sized by the distance to the next offset. Per-field
 * byte size is not in the artifact, so a segment covers the field plus any padding
 * that follows it.
 */
export function stripSegments(layout: Layout, size: number | null): StripSegment[] {
	if (!size || size <= 0) return [];
	const placed = layout.rows.filter((r) => r.offset !== null && r.offset < size);
	if (placed.length === 0) return [];

	const groups: { offset: number; rows: LayoutRow[] }[] = [];
	for (const r of placed) {
		const last = groups[groups.length - 1];
		if (last && last.offset === r.offset) last.rows.push(r);
		else groups.push({ offset: r.offset!, rows: [r] });
	}

	const segments: StripSegment[] = [];
	if (groups[0]!.offset > 0) {
		segments.push({
			offset: 0,
			span: groups[0]!.offset,
			label: `0x0 to 0x${groups[0]!.offset.toString(16)} not described by the schema`,
			gap: true,
		});
	}
	for (let i = 0; i < groups.length; i++) {
		const g = groups[i]!;
		const end = i + 1 < groups.length ? groups[i + 1]!.offset : size;
		const names = g.rows.map((r) => r.field.name);
		const shown = names.length > 2 ? `${names.slice(0, 2).join(' ')} +${names.length - 2}` : names.join(' ');
		segments.push({
			offset: g.offset,
			span: Math.max(1, end - g.offset),
			label: `0x${g.offset.toString(16)} ${shown}`,
			declaring: g.rows[0]!.declaring,
			gap: false,
		});
	}
	return segments;
}

/** Stable, mid-lightness hues so the same declaring class reads in both themes. */
export function segmentColor(index: number): string {
	return `hsl(${(index * 137.508) % 360} 52% 52%)`;
}
