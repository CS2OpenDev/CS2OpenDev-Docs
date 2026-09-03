import type { ClassEntity, SchemaIndex } from '../../lib/data/schema';
import { childrenOf, resolveClass } from '../../lib/data/schema';
import { countTreeNodes, type TreeNode } from '../../lib/tree';

/**
 * Same construction as tree.ts's buildModuleForest, generalized to an arbitrary set of
 * classes rather than one projectName, for the combined server+client hierarchy page.
 */
export function buildForest(idx: SchemaIndex, classes: ClassEntity[]): TreeNode[] {
	const local = new Set(classes.map((c) => c.key));
	const seen = new Set<string>();

	const build = (ent: ClassEntity): TreeNode => {
		seen.add(ent.key);
		const all = childrenOf(idx, ent).filter((c) => local.has(c.key) && !seen.has(c.key));
		return { ent, children: all.map(build), open: false, current: false, truncated: 0 };
	};

	const roots = classes.filter((c) => {
		const p = c.raw.parents[0];
		if (!p) return true;
		const pe = resolveClass(idx, p.name, [c.module], p.module);
		return !pe || !local.has(pe.key);
	});
	return roots.map(build);
}

/** Roots ordered by subtree size, largest first. */
export function sortRootsBySize(roots: TreeNode[]): TreeNode[] {
	return roots
		.map((root) => ({ root, size: countTreeNodes([root]) }))
		.sort((a, b) => b.size - a.size)
		.map((r) => r.root);
}
