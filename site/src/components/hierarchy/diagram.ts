import type { TreeNode } from '../../lib/tree';

/**
 * Same quoting rule as lib/diagram.ts's relationshipDiagram: mermaid rejects
 * double-quoted names containing '::', backticks parse.
 */
function safeName(name: string): string {
	return /^[A-Za-z_]\w*$/.test(name) ? name : `\`${name}\``;
}

/** Every parent-to-child edge in a forest, in the same `<|--` convention as lib/diagram.ts. */
export function forestInheritanceDiagram(roots: TreeNode[]): string[] {
	const lines: string[] = [];
	const walk = (n: TreeNode) => {
		for (const child of n.children) {
			lines.push(`    ${safeName(n.ent.name)} <|-- ${safeName(child.ent.name)}`);
			walk(child);
		}
	};
	for (const root of roots) walk(root);
	return lines;
}
