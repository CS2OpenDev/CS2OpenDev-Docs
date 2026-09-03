import type { ClassEntity, Entity, SchemaIndex } from './data/schema';
import { childrenOf, resolveClass, resolveEntity, typeRefNames } from './data/schema';

const PARENT_LEVELS = 5;
const CHILD_CAP = 20;
const COMPOSITION_CAP = 10;

/** Mermaid rejects double-quoted names containing '::'; backticks parse. */
function safeName(name: string): string {
	return /^[A-Za-z_]\w*$/.test(name) ? name : `\`${name}\``;
}

/**
 * Parent spine, capped child fan-out and a few composition edges. Kept small on
 * purpose: the inheritance tree carries the full picture.
 */
export function relationshipDiagram(idx: SchemaIndex, ent: Entity): string[] {
	if (ent.kind !== 'class') return [];
	const lines: string[] = [];
	const seen = new Set<string>();

	const edge = (from: string, to: string, arrow: string) => {
		const key = `${from}${arrow}${to}`;
		if (seen.has(key)) return;
		seen.add(key);
		lines.push(`    ${safeName(from)} ${arrow} ${safeName(to)}`);
	};

	const chain: ClassEntity[] = [ent];
	let cur: ClassEntity | undefined = ent;
	for (let i = 0; i < PARENT_LEVELS && cur; i++) {
		const p = cur.raw.parents[0];
		if (!p) break;
		const next: ClassEntity | undefined = resolveClass(idx, p.name, [ent.module, cur.module], p.module);
		if (!next || chain.some((c) => c.key === next.key)) break;
		chain.push(next);
		cur = next;
	}
	for (let i = chain.length - 1; i > 0; i--) {
		edge(chain[i]!.name, chain[i - 1]!.name, '<|--');
	}

	for (const child of childrenOf(idx, ent).slice(0, CHILD_CAP)) {
		if (child.key === ent.key) continue;
		edge(ent.name, child.name, '<|--');
	}

	let comp = 0;
	for (const f of ent.raw.fields) {
		if (comp >= COMPOSITION_CAP) break;
		for (const refName of typeRefNames(f.type.name)) {
			if (comp >= COMPOSITION_CAP) break;
			const target = resolveEntity(idx, refName, [ent.module], f.typeModule);
			if (!target || target.key === ent.key || target.kind !== 'class') continue;
			const before = seen.size;
			edge(ent.name, target.name, f.type.name.includes('*') || f.type.name.includes('CHandle') ? '-->' : '*--');
			if (seen.size > before) comp++;
		}
	}
	return lines;
}
