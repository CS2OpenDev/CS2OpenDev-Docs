import { escapeHtml } from './html';
import { entityHref } from './urls';
import type { ClassEntity, SchemaIndex } from './data/schema';
import { childrenOf, resolveClass, spineOf } from './data/schema';

export interface TreeNode {
	ent: ClassEntity;
	children: TreeNode[];
	/** Rendered as <details open>: the node sits on the path to the current page. */
	open: boolean;
	current: boolean;
	/** Children omitted under a cap. */
	truncated: number;
}

export interface TreeLimits {
	/** Levels of descendants below the current node. */
	depth?: number;
	/** Children listed per node before truncating. */
	breadth?: number;
}

function node(ent: ClassEntity, overrides: Partial<TreeNode> = {}): TreeNode {
	return { ent, children: [], open: false, current: false, truncated: 0, ...overrides };
}

function descendants(
	idx: SchemaIndex,
	ent: ClassEntity,
	depth: number,
	breadth: number,
	seen: Set<string>
): { children: TreeNode[]; truncated: number } {
	if (depth <= 0) return { children: [], truncated: 0 };
	const all = childrenOf(idx, ent).filter((c) => !seen.has(c.key));
	const kept = all.slice(0, breadth);
	const children = kept.map((c) => {
		seen.add(c.key);
		const sub = descendants(idx, c, depth - 1, breadth, seen);
		return node(c, sub);
	});
	return { children, truncated: all.length - kept.length };
}

/**
 * Root ancestor down to `ent`, expanded along that path, with `ent`'s own
 * descendants collapsed underneath it.
 */
export function buildEntityTree(idx: SchemaIndex, ent: ClassEntity, limits: TreeLimits = {}): TreeNode {
	const depth = limits.depth ?? 2;
	const breadth = limits.breadth ?? 120;
	const seen = new Set<string>([ent.key]);
	const sub = descendants(idx, ent, depth, breadth, seen);
	let current = node(ent, { open: true, current: true, ...sub });

	for (const ancestor of spineOf(idx, ent)) {
		current = node(ancestor, { open: true, children: [current] });
	}
	return current;
}

/** Every root class in a module with its in-module subclasses nested underneath. */
export function buildModuleForest(idx: SchemaIndex, module: string, limits: TreeLimits = {}): TreeNode[] {
	const breadth = limits.breadth ?? Number.POSITIVE_INFINITY;
	const classes = (idx.byModule.get(module) ?? []).filter((e): e is ClassEntity => e.kind === 'class');
	const local = new Set(classes.map((c) => c.key));
	const seen = new Set<string>();

	const build = (ent: ClassEntity): TreeNode => {
		seen.add(ent.key);
		const all = childrenOf(idx, ent).filter((c) => local.has(c.key) && !seen.has(c.key));
		const kept = all.slice(0, breadth);
		return node(ent, {
			children: kept.map(build),
			truncated: all.length - kept.length,
		});
	};

	const roots = classes.filter((c) => {
		const p = c.raw.parents[0];
		if (!p) return true;
		const pe = resolveClass(idx, p.name, [c.module], p.module);
		return !pe || !local.has(pe.key);
	});
	return roots.map(build);
}

export function countTreeNodes(nodes: TreeNode[]): number {
	let n = 0;
	for (const node of nodes) n += 1 + countTreeNodes(node.children);
	return n;
}

export interface RenderOptions {
	/** Suppress the module tag on nodes from this module, which is most of them. */
	homeModule?: string;
}

function renderNode(n: TreeNode, opts: RenderOptions): string {
	const label = n.current
		? `<strong aria-current="page">${escapeHtml(n.ent.name)}</strong>`
		: `<a href="${entityHref(n.ent.module, n.ent.name)}">${escapeHtml(n.ent.name)}</a>`;
	const suffix =
		n.ent.module === opts.homeModule ? '' : ` <span class="cs2-count">${escapeHtml(n.ent.module)}</span>`;
	const listed = n.children.length + n.truncated;
	if (n.children.length === 0) {
		return `<li>${label}${suffix}</li>`;
	}
	const more = n.truncated > 0 ? `<li><span class="cs2-count">and ${n.truncated} more</span></li>` : '';
	const count = listed > 1 ? ` <span class="cs2-count">(${listed})</span>` : '';
	return (
		`<li><details${n.open ? ' open' : ''}><summary>${label}${suffix}${count}</summary>` +
		`<ul>${n.children.map((c) => renderNode(c, opts)).join('')}${more}</ul></details></li>`
	);
}

export function renderTreeHtml(nodes: TreeNode[], opts: RenderOptions = {}): string {
	return `<ul class="cs2-tree">${nodes.map((n) => renderNode(n, opts)).join('')}</ul>`;
}
