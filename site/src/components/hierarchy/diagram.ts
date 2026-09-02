import type { TreeNode } from '../../lib/tree';

/**
 * Same quoting rule as lib/diagram.ts's relationshipDiagram: mermaid rejects
 * double-quoted names containing '::', backticks parse.
 */
function safeName(name: string): string {
	return /^[A-Za-z_]\w*$/.test(name) ? name : `\`${name}\``;
}

export interface CappedDiagram {
	/** classDiagram body lines, ready to join under a `classDiagram` header. */
	lines: string[];
	/** Edges actually included, at most `cap`. */
	edgeCount: number;
	/** Edges in the full forest, before the cap. */
	total: number;
}

/**
 * Every parent-to-child edge in a forest, in the same `<|--` convention as lib/diagram.ts,
 * breadth first within each root (roots in the given order) so a cap keeps the top of
 * each hierarchy rather than exhausting itself on one deep branch.
 */
export function forestInheritanceDiagram(roots: TreeNode[], cap: number): CappedDiagram {
	const lines: string[] = [];
	let edgeCount = 0;
	let total = 0;
	for (const root of roots) {
		const queue: TreeNode[] = [root];
		while (queue.length > 0) {
			const n = queue.shift()!;
			for (const child of n.children) {
				if (edgeCount < cap) {
					lines.push(`    ${safeName(n.ent.name)} <|-- ${safeName(child.ent.name)}`);
					edgeCount++;
				}
				total++;
				queue.push(child);
			}
		}
	}
	return { lines, edgeCount, total };
}

/**
 * Same edges, but every node gets a synthetic id and a "Name (module)" label instead of
 * being addressed by its raw name. The combined server+client tree has 189 identically
 * named classes; without this they would collapse into one node in the diagram.
 */
export function forestInheritanceDiagramTagged(roots: TreeNode[], cap: number): CappedDiagram {
	const lines: string[] = [];
	let edgeCount = 0;
	let total = 0;
	const ids = new Map<string, string>();
	const declared = new Set<string>();
	let next = 0;

	const idFor = (key: string, name: string, module: string): string => {
		let id = ids.get(key);
		if (!id) {
			id = `n${next++}`;
			ids.set(key, id);
		}
		if (!declared.has(id)) {
			declared.add(id);
			const label = `${name} (${module})`.replace(/"/g, "'");
			lines.push(`    class ${id}["${label}"]`);
		}
		return id;
	};

	for (const root of roots) {
		const queue: TreeNode[] = [root];
		while (queue.length > 0) {
			const n = queue.shift()!;
			for (const child of n.children) {
				if (edgeCount < cap) {
					const a = idFor(n.ent.key, n.ent.name, n.ent.module);
					const b = idFor(child.ent.key, child.ent.name, child.ent.module);
					lines.push(`    ${a} <|-- ${b}`);
					edgeCount++;
				}
				total++;
				queue.push(child);
			}
		}
	}
	return { lines, edgeCount, total };
}
