import { join } from 'node:path';
import { siteDataDir, readJsonFile, requireKeys, requireRows } from '../paths';
import { escapeHtml } from '../html';
import { entityHref, protoEnumHref, protoMessageHref } from '../urls';
import { resolveEntity, type SchemaIndex } from './schema';

export type ProtoTypeKind = 'scalar' | 'message' | 'enum' | 'unknown';
export type ProtoLabel = 'optional' | 'repeated' | 'required';

export interface ProtoField {
	name: string;
	number: number;
	label: ProtoLabel;
	type: string;
	type_kind: ProtoTypeKind;
	/** The file the type is declared in, with its `.proto` suffix; null for scalars. */
	type_file: string | null;
	default: string;
	description: string;
	notes: string;
}

export interface ProtoOneof {
	name: string;
	fields: string[];
}

export interface ProtoWireId {
	enum: string;
	constant: string;
	value: number;
}

export interface ProtoMessage {
	name: string;
	/** Dotted `Parent.Nested` path; equal to `name` for a top-level message. */
	qualified: string;
	parent: string | null;
	description: string;
	notes: string;
	fields: ProtoField[];
	/** Direct children only, by qualified name. */
	nested_messages: string[];
	nested_enums: string[];
	oneofs: ProtoOneof[];
	wire_ids: ProtoWireId[];
}

export interface ProtoEnumValue {
	name: string;
	number: number;
}

export interface ProtoEnum {
	name: string;
	qualified: string;
	parent: string | null;
	values: ProtoEnumValue[];
}

export interface ProtoFile {
	name: string;
	stem: string;
	package: string | null;
	imports: string[];
	description: string;
	notes: string;
	messages: ProtoMessage[];
	enums: ProtoEnum[];
}

interface RawProtoData {
	files: ProtoFile[];
	/** qualified type name (message or enum) -> defining file, with `.proto` suffix. */
	types: Record<string, string>;
	/** qualified type name -> sorted qualified names of messages with a field of that type. */
	referenced_by: Record<string, string[]>;
}

export type ProtoGroup = 'CS2 wire format' | 'Demo' | 'Game events' | 'User messages' | 'GC and Steam SDK' | 'Other';

export const PROTO_GROUP_ORDER: ProtoGroup[] = [
	'CS2 wire format',
	'Demo',
	'Game events',
	'User messages',
	'GC and Steam SDK',
	'Other',
];

/** The core game-networking protocol files: connection, channel and entity-delta framing. */
const CS2_WIRE_STEMS = new Set([
	'netmessages',
	'networkbasetypes',
	'network_connection',
	'connectionless_netmessages',
	'clientmessages',
	'usercmd',
	'cs_usercmd',
	'cs_prediction_events',
	'te',
	'c_peer2peer_netmessages',
	'networksystem_protomessages',
]);

/**
 * Every file in this build carries `package: null`, so the group has to come from the
 * file name rather than the descriptor. `demo.proto` is Demo; a stem ending in
 * `gameevents` or `usermessages` is that family; `CS2_WIRE_STEMS` is the core
 * connection/channel protocol; a stem naming a GC channel, Steam message set, or Steam
 * Datagram Relay is GC and Steam SDK; anything left over is Other.
 */
export function fileGroup(stem: string): ProtoGroup {
	if (stem === 'demo') return 'Demo';
	if (stem.endsWith('gameevents')) return 'Game events';
	if (stem.endsWith('usermessages')) return 'User messages';
	if (
		stem.endsWith('_gcmessages') ||
		stem === 'gcsystemmsgs' ||
		stem.startsWith('steammessages') ||
		stem.endsWith('.steamworkssdk') ||
		stem.startsWith('steamnetworkingsockets') ||
		stem.startsWith('steamdatagram')
	) {
		return 'GC and Steam SDK';
	}
	if (CS2_WIRE_STEMS.has(stem)) return 'CS2 wire format';
	return 'Other';
}

export interface ProtoIndex {
	files: ProtoFile[];
	filesByStem: Map<string, ProtoFile>;
	types: Record<string, string>;
	referencedBy: Record<string, string[]>;
	messageByQualified: Map<string, { file: ProtoFile; message: ProtoMessage }>;
	enumByQualified: Map<string, { file: ProtoFile; enm: ProtoEnum }>;
	/** `${enum}\0${constant}` -> the message that constant maps to, by the wire-id join rule. */
	wireIdToMessage: Map<string, { file: ProtoFile; message: ProtoMessage }>;
}

let cache: ProtoIndex | undefined;

export function loadProtoIndex(): ProtoIndex {
	if (cache) return cache;
	const file = join(siteDataDir(), 'protobufs.json');
	const raw = readJsonFile<RawProtoData>(file);
	requireKeys(file, raw, ['files', 'types', 'referenced_by']);
	requireRows(file, raw.files, 'files', ['name', 'stem', 'package', 'imports', 'description', 'notes', 'messages', 'enums']);
	// The first file may declare no messages or no enums; check the first of each that exists.
	const withMessages = raw.files.find((f) => f.messages.length > 0);
	requireRows(file, withMessages?.messages, 'files[].messages', [
		'name',
		'qualified',
		'parent',
		'description',
		'notes',
		'fields',
		'nested_messages',
		'nested_enums',
		'oneofs',
		'wire_ids',
	]);
	const withFields = raw.files.flatMap((f) => f.messages).find((m) => m.fields.length > 0);
	requireRows(file, withFields?.fields, 'files[].messages[].fields', [
		'name',
		'number',
		'label',
		'type',
		'type_kind',
		'type_file',
		'default',
		'description',
		'notes',
	]);
	const withEnums = raw.files.find((f) => f.enums.length > 0);
	requireRows(file, withEnums?.enums, 'files[].enums', ['name', 'qualified', 'parent', 'values']);
	requireRows(file, withEnums?.enums[0]?.values, 'files[].enums[].values', ['name', 'number']);

	const filesByStem = new Map<string, ProtoFile>();
	const messageByQualified = new Map<string, { file: ProtoFile; message: ProtoMessage }>();
	const enumByQualified = new Map<string, { file: ProtoFile; enm: ProtoEnum }>();
	const wireIdToMessage = new Map<string, { file: ProtoFile; message: ProtoMessage }>();

	for (const file of raw.files) {
		filesByStem.set(file.stem, file);
		for (const message of file.messages) {
			messageByQualified.set(message.qualified, { file, message });
			for (const w of message.wire_ids) {
				wireIdToMessage.set(`${w.enum}\0${w.constant}`, { file, message });
			}
		}
		for (const enm of file.enums) {
			enumByQualified.set(enm.qualified, { file, enm });
		}
	}

	cache = {
		files: raw.files,
		filesByStem,
		types: raw.types,
		referencedBy: raw.referenced_by,
		messageByQualified,
		enumByQualified,
		wireIdToMessage,
	};
	return cache;
}

export function filesByGroup(idx: ProtoIndex): Map<ProtoGroup, ProtoFile[]> {
	const out = new Map<ProtoGroup, ProtoFile[]>();
	for (const g of PROTO_GROUP_ORDER) out.set(g, []);
	for (const file of idx.files) out.get(fileGroup(file.stem))!.push(file);
	return out;
}

/** File stem a qualified type name is declared in, or undefined outside the descriptor set. */
export function fileForType(idx: ProtoIndex, qualified: string): string | undefined {
	const f = idx.types[qualified];
	return f ? f.replace(/\.proto$/, '') : undefined;
}

export function topLevelMessages(file: ProtoFile): ProtoMessage[] {
	return file.messages.filter((m) => m.parent === null);
}

export function topLevelEnums(file: ProtoFile): ProtoEnum[] {
	return file.enums.filter((e) => e.parent === null);
}

/** Every message in the file (top-level and nested) that carries at least one wire id. */
export function fileWireIds(file: ProtoFile): { message: ProtoMessage; wireId: ProtoWireId }[] {
	const out: { message: ProtoMessage; wireId: ProtoWireId }[] = [];
	for (const message of file.messages) {
		for (const wireId of message.wire_ids) out.push({ message, wireId });
	}
	return out;
}

/** Messages elsewhere in the descriptor with a field typed as this qualified name, resolved to a file. */
export function messagesReferencing(idx: ProtoIndex, qualified: string): { qualified: string; file: string }[] {
	const names = idx.referencedBy[qualified] ?? [];
	const out: { qualified: string; file: string }[] = [];
	for (const name of names) {
		const file = fileForType(idx, name);
		if (file) out.push({ qualified: name, file });
	}
	return out;
}

/**
 * The schema entity page for a wire-id enum, when SchemaTracker walked an enum of the
 * same name (all nine join-rule enums live under the server module on this build).
 */
export function schemaEnumHref(schemaIdx: SchemaIndex, enumName: string): string | undefined {
	const ent = resolveEntity(schemaIdx, enumName, []);
	return ent && ent.kind === 'enum' ? entityHref(ent.module, ent.name) : undefined;
}

/** The message that an enum constant maps to under the wire-id join rule, if any. */
export function messageForConstant(
	idx: ProtoIndex,
	enumName: string,
	constant: string
): { qualified: string; file: string } | undefined {
	const hit = idx.wireIdToMessage.get(`${enumName}\0${constant}`);
	return hit ? { qualified: hit.message.qualified, file: hit.file.stem } : undefined;
}

/**
 * A field's type as HTML: scalars are plain escaped text, message/enum types anchor
 * into the declaring file's page (same file or across files).
 */
export function linkFieldType(field: ProtoField): string {
	if ((field.type_kind !== 'message' && field.type_kind !== 'enum') || !field.type_file) {
		return escapeHtml(field.type);
	}
	const stem = field.type_file.replace(/\.proto$/, '');
	const href = field.type_kind === 'enum' ? protoEnumHref(stem, field.type) : protoMessageHref(stem, field.type);
	return `<a href="${href}">${escapeHtml(field.type)}</a>`;
}

/** Total message count in a file, top-level plus nested, used for the diagram-eligibility cap. */
export function messageCount(file: ProtoFile): number {
	return file.messages.length;
}

export interface ReferenceEdge {
	from: string;
	to: string;
}

/** Message-to-message field references inside one file, deduplicated, self-references dropped. */
export function referenceEdges(file: ProtoFile): ReferenceEdge[] {
	const seen = new Set<string>();
	const edges: ReferenceEdge[] = [];
	for (const m of file.messages) {
		for (const f of m.fields) {
			if (f.type_kind !== 'message' || f.type === m.qualified) continue;
			const key = `${m.qualified}\0${f.type}`;
			if (seen.has(key)) continue;
			seen.add(key);
			edges.push({ from: m.qualified, to: f.type });
		}
	}
	return edges;
}

/**
 * A flowchart of message reference edges, one labelled node per message and no field
 * boxes. Node ids are synthetic so dotted qualified names never have to be quoted.
 */
export function referenceDiagram(file: ProtoFile): string[] {
	const edges = referenceEdges(file);
	if (edges.length === 0) return [];
	const ids = new Map<string, string>();
	const declared = new Set<string>();
	const lines: string[] = [];
	let n = 0;
	const nodeId = (name: string): string => {
		let id = ids.get(name);
		if (!id) {
			id = `n${n++}`;
			ids.set(name, id);
		}
		if (!declared.has(id)) {
			declared.add(id);
			lines.push(`    ${id}["${name}"]`);
		}
		return id;
	};
	for (const e of edges) {
		const a = nodeId(e.from);
		const b = nodeId(e.to);
		lines.push(`    ${a} --> ${b}`);
	}
	return lines;
}

/**
 * Message boxes with no fields, for a file whose messages don't reference each other (so
 * `referenceDiagram` would be empty) but that still deserves a diagram. Synthetic ids and
 * bracket labels for the same reason as `referenceDiagram`: qualified names carry dots
 * that are fine inside a quoted label but not as a bare mermaid identifier.
 */
export function messageBoxDiagram(file: ProtoFile, cap: number): string[] {
	const lines: string[] = [];
	let n = 0;
	for (const m of file.messages.slice(0, cap)) {
		const id = `n${n++}`;
		const label = m.qualified.replace(/"/g, "'");
		lines.push(`    class ${id}["${label}"]`);
	}
	return lines;
}

export interface HeadingEntry {
	depth: number;
	slug: string;
	text: string;
}

/**
 * Headings for one top-level message and everything nested inside it, in the same
 * depth-first order the message is rendered in: nested messages then nested enums,
 * each a flat h4 regardless of how many levels deep it actually sits.
 */
export function messageHeadings(idx: ProtoIndex, message: ProtoMessage, depth: number): HeadingEntry[] {
	const out: HeadingEntry[] = [{ depth, slug: message.qualified, text: message.qualified }];
	for (const childName of message.nested_messages) {
		const child = idx.messageByQualified.get(childName);
		if (child) out.push(...messageHeadings(idx, child.message, 4));
	}
	for (const enumName of message.nested_enums) {
		if (idx.enumByQualified.has(enumName)) out.push({ depth: 4, slug: enumName, text: enumName });
	}
	return out;
}
