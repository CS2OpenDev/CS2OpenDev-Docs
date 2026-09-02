import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import '../../styles/datatable.css';

export interface Column {
	key: string;
	label: string;
	numeric?: boolean;
	mono?: boolean;
	html?: boolean;
	sortable?: boolean;
	width?: string;
	facet?: boolean;
}

export type Row = Record<string, string | number | boolean | null | string[]>;

export interface DataTableProps {
	id: string;
	columns: Column[];
	rows: Row[];
	anchorKey?: string;
	searchKeys?: string[];
	pageSize?: number;
	initialSort?: { key: string; dir: 'asc' | 'desc' };
	caption?: string;
	emptyText?: string;
	/** When set, `rows` is only the server-rendered first page. The full set
	 * (a JSON array of Row) is fetched from this URL on first interaction. */
	src?: string;
}

type SortDir = 'asc' | 'desc' | null;
type FacetState = Record<string, string[]>;

/** Pure, module-scope so the row loop never allocates a closure per cell. */
function renderCellContent(col: Column, value: Row[string]) {
	if (col.html) {
		const html = value === null || value === undefined ? '' : String(value);
		return <span dangerouslySetInnerHTML={{ __html: html }} />;
	}
	if (col.facet) {
		const arr = Array.isArray(value) ? value : [];
		if (arr.length === 0) return null;
		return (
			<span className="dtbl-chips">
				{arr.map((v) => (
					<span className="dtbl-chip" key={v}>
						{v}
					</span>
				))}
			</span>
		);
	}
	if (value === null || value === undefined) return '';
	return String(value);
}

function cellClassName(col: Column): string | undefined {
	const classes: string[] = [];
	if (col.numeric) classes.push('dtbl-num');
	if (col.mono) classes.push('dtbl-mono');
	return classes.length ? classes.join(' ') : undefined;
}

function rowMatchesText(row: Row, needle: string, keys: string[]): boolean {
	if (!needle) return true;
	for (const k of keys) {
		const v = row[k];
		if (v === null || v === undefined) continue;
		const s = Array.isArray(v) ? v.join(' ') : String(v);
		if (s.toLowerCase().includes(needle)) return true;
	}
	return false;
}

/** Every active chip is required: AND within a facet column and across columns. */
function rowMatchesFacets(row: Row, active: FacetState): boolean {
	for (const key in active) {
		const required = active[key];
		if (!required || required.length === 0) continue;
		const val = row[key];
		const arr = Array.isArray(val) ? val : [];
		for (const req of required) {
			if (!arr.includes(req)) return false;
		}
	}
	return true;
}

function compareRows(a: Row, b: Row, key: string, numeric: boolean): number {
	const av = a[key];
	const bv = b[key];
	if (numeric) {
		const an = av === null || av === undefined ? -Infinity : Number(av);
		const bn = bv === null || bv === undefined ? -Infinity : Number(bv);
		return an - bn;
	}
	const as = av === null || av === undefined ? '' : Array.isArray(av) ? av.join(', ') : String(av);
	const bs = bv === null || bv === undefined ? '' : Array.isArray(bv) ? bv.join(', ') : String(bv);
	return as.localeCompare(bs, undefined, { numeric: true, sensitivity: 'base' });
}

function parseSortParam(raw: string | null): { key: string; dir: SortDir } | null {
	if (!raw) return null;
	const idx = raw.lastIndexOf(':');
	if (idx <= 0) return null;
	const key = raw.slice(0, idx);
	const dir = raw.slice(idx + 1);
	if (dir !== 'asc' && dir !== 'desc') return null;
	return { key, dir };
}

export default function DataTable({
	id,
	columns,
	rows,
	anchorKey,
	searchKeys,
	pageSize: pageSizeProp = 250,
	initialSort,
	caption,
	emptyText = 'No matching rows.',
	src,
}: DataTableProps) {
	const [filterText, setFilterText] = useState('');
	const [activeFacets, setActiveFacets] = useState<FacetState>({});
	const [sortKey, setSortKey] = useState<string | null>(initialSort?.key ?? null);
	const [sortDir, setSortDir] = useState<SortDir>(initialSort?.dir ?? null);
	const [page, setPage] = useState(1);
	const [pageSize, setPageSize] = useState(pageSizeProp);
	const [revealId, setRevealId] = useState<string | null>(null);
	const [fullRows, setFullRows] = useState<Row[] | null>(null);
	const [srcLoading, setSrcLoading] = useState(false);

	const didWriteUrlRef = useRef(false);
	const srcFetchStartedRef = useRef(false);
	const pendingHashRef = useRef<string | null>(null);

	// Live mirrors of state that effects and callbacks need without joining
	// their dependency arrays (would otherwise re-run on every keystroke or
	// force stale closures). Updated unconditionally every render.
	const sortKeyRef = useRef(sortKey);
	const sortDirRef = useRef(sortDir);
	const filterTextRef = useRef(filterText);
	const activeFacetsRef = useRef(activeFacets);
	sortKeyRef.current = sortKey;
	sortDirRef.current = sortDir;
	filterTextRef.current = filterText;
	activeFacetsRef.current = activeFacets;

	// The dataset actually rendered: the full set once `src` has resolved,
	// otherwise whatever `rows` the server sent (the whole set, or just the
	// first page when `src` is in play).
	const effectiveRows = fullRows ?? rows;

	const columnByKey = useMemo(() => new Map(columns.map((c) => [c.key, c])), [columns]);
	const facetColumns = useMemo(() => columns.filter((c) => c.facet), [columns]);

	const effectiveSearchKeys = useMemo(
		() => searchKeys ?? columns.filter((c) => !c.html && !c.facet).map((c) => c.key),
		[searchKeys, columns]
	);

	const facetValues = useMemo(() => {
		const map: Record<string, string[]> = {};
		for (const col of facetColumns) {
			const set = new Set<string>();
			for (const row of effectiveRows) {
				const v = row[col.key];
				if (Array.isArray(v)) for (const item of v) set.add(item);
			}
			map[col.key] = Array.from(set).sort((a, b) => a.localeCompare(b));
		}
		return map;
	}, [effectiveRows, facetColumns]);

	const filtered = useMemo(() => {
		const needle = filterText.trim().toLowerCase();
		const hasFacetFilter = Object.values(activeFacets).some((v) => v.length > 0);
		if (!needle && !hasFacetFilter) return effectiveRows;
		return effectiveRows.filter(
			(r) => rowMatchesText(r, needle, effectiveSearchKeys) && rowMatchesFacets(r, activeFacets)
		);
	}, [effectiveRows, filterText, activeFacets, effectiveSearchKeys]);

	const sorted = useMemo(() => {
		if (!sortKey || !sortDir) return filtered;
		const col = columnByKey.get(sortKey);
		if (!col) return filtered;
		const dir = sortDir === 'desc' ? -1 : 1;
		return [...filtered].sort((a, b) => compareRows(a, b, sortKey, !!col.numeric) * dir);
	}, [filtered, sortKey, sortDir, columnByKey]);

	const totalPages = pageSize > 0 ? Math.max(1, Math.ceil(sorted.length / pageSize)) : 1;
	const clampedPage = Math.min(Math.max(1, page), totalPages);

	const pageRows = useMemo(() => {
		if (pageSize <= 0) return sorted;
		const start = (clampedPage - 1) * pageSize;
		return sorted.slice(start, start + pageSize);
	}, [sorted, clampedPage, pageSize]);

	// Fetches the full row set exactly once. Safe to call from multiple
	// handlers (focus, sort, facet, page, hash reveal, idle prefetch): the ref
	// guard makes every call after the first a no-op.
	const ensureFullRows = useCallback(() => {
		if (!src || srcFetchStartedRef.current) return;
		srcFetchStartedRef.current = true;
		setSrcLoading(true);
		fetch(src)
			.then((res) => {
				if (!res.ok) throw new Error(`${res.status}`);
				return res.json() as Promise<Row[]>;
			})
			.then((data) => {
				setFullRows(data);
				setSrcLoading(false);
			})
			.catch(() => {
				// Leave fullRows null; the server-rendered first page stays usable.
				setSrcLoading(false);
			});
	}, [src]);

	// Prefetch once the main thread is idle, so most viewers never see the
	// loading note at all. Safari has no requestIdleCallback, hence the timer.
	useEffect(() => {
		if (!src || typeof window === 'undefined') return;
		const w = window as typeof window & { requestIdleCallback?: (cb: () => void) => number };
		if (typeof w.requestIdleCallback === 'function') {
			const handle = w.requestIdleCallback(() => ensureFullRows());
			return () => {
				(window as typeof window & { cancelIdleCallback?: (h: number) => void }).cancelIdleCallback?.(handle);
			};
		}
		const timer = setTimeout(() => ensureFullRows(), 200);
		return () => clearTimeout(timer);
	}, [src, ensureFullRows]);

	// Shared by the mount-time hash check and the deferred retry once the full
	// set arrives. Returns whether hashId was found in candidateRows.
	const attemptReveal = useCallback(
		(
			candidateRows: Row[],
			hashId: string,
			curFilter: string,
			curFacets: FacetState,
			curSortKey: string | null,
			curSortDir: SortDir,
			curPageSize: number
		): boolean => {
			if (!anchorKey) return false;
			const match = candidateRows.find((r) => String(r[anchorKey]) === hashId);
			if (!match) return false;

			let filter = curFilter;
			let facets = curFacets;
			const passesFilter =
				rowMatchesText(match, filter.trim().toLowerCase(), effectiveSearchKeys) && rowMatchesFacets(match, facets);
			if (!passesFilter) {
				filter = '';
				facets = {};
			}

			let revealSet = candidateRows.filter(
				(r) => rowMatchesText(r, filter.trim().toLowerCase(), effectiveSearchKeys) && rowMatchesFacets(r, facets)
			);
			if (curSortKey && curSortDir) {
				const col = columnByKey.get(curSortKey);
				if (col) {
					const dir = curSortDir === 'desc' ? -1 : 1;
					revealSet = [...revealSet].sort((a, b) => compareRows(a, b, curSortKey, !!col.numeric) * dir);
				}
			}
			const idx = revealSet.findIndex((r) => String(r[anchorKey]) === hashId);
			if (idx < 0) return false;

			if (filter !== curFilter) setFilterText(filter);
			if (facets !== curFacets) setActiveFacets(facets);
			setPage(curPageSize > 0 ? Math.floor(idx / curPageSize) + 1 : 1);
			setRevealId(hashId);
			return true;
		},
		[anchorKey, effectiveSearchKeys, columnByKey]
	);

	// Read URL state and resolve a #hash anchor once, on mount. Runs client-only:
	// the SSR pass and first hydration render must match, so nothing here can
	// run before the effect phase.
	useEffect(() => {
		if (typeof window === 'undefined') return;
		const params = new URLSearchParams(window.location.search);
		const prefix = `${id}.`;

		let nextFilter = params.get(`${prefix}q`) ?? '';
		let nextSortKey = initialSort?.key ?? null;
		let nextSortDir: SortDir = initialSort?.dir ?? null;
		const parsedSort = parseSortParam(params.get(`${prefix}sort`));
		if (parsedSort) {
			nextSortKey = parsedSort.key;
			nextSortDir = parsedSort.dir;
		}
		let nextPage = Number(params.get(`${prefix}page`)) || 1;

		const nextFacets: FacetState = {};
		for (const col of facetColumns) {
			const v = params.get(`${prefix}${col.key}`);
			if (v) nextFacets[col.key] = v.split(',').filter(Boolean);
		}

		let nextPageSize = pageSizeProp;
		try {
			if (pageSizeProp !== 0 && window.sessionStorage.getItem(`dtbl:${id}:showAll`) === '1') {
				nextPageSize = 0;
			}
		} catch {
			/* sessionStorage unavailable (private mode); keep the prop default. */
		}

		setFilterText(nextFilter);
		setActiveFacets(nextFacets);
		setSortKey(nextSortKey);
		setSortDir(nextSortDir);
		setPage(nextPage);
		setPageSize(nextPageSize);

		// attemptReveal's own setState calls (filter/facets/page/revealId) run
		// after the baseline ones above in the same batch, so they win when a
		// reveal is found.
		const rawHash = window.location.hash;
		if (rawHash && anchorKey) {
			const hashId = decodeURIComponent(rawHash.slice(1));
			const found = attemptReveal(rows, hashId, nextFilter, nextFacets, nextSortKey, nextSortDir, nextPageSize);
			if (!found && src) {
				// Not on the server-rendered first page: fetch the rest and retry.
				pendingHashRef.current = hashId;
				ensureFullRows();
			}
		}
		// Mount-only: reads location once. Later user interaction owns state after this.
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, []);

	// Retry a hash reveal that wasn't on the initial page, once the full set
	// arrives. Uses live refs for filter/sort so a reveal found later still
	// respects anything the viewer changed in the meantime.
	useEffect(() => {
		if (!fullRows || !pendingHashRef.current) return;
		const hashId = pendingHashRef.current;
		pendingHashRef.current = null;
		attemptReveal(
			fullRows,
			hashId,
			filterTextRef.current,
			activeFacetsRef.current,
			sortKeyRef.current,
			sortDirRef.current,
			pageSize
		);
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, [fullRows]);

	// Write current state back to the URL. The very first effect run (mount,
	// still holding defaults) is skipped so it never clobbers an incoming URL
	// before the mount-read effect above has applied it.
	useEffect(() => {
		if (typeof window === 'undefined') return;
		if (!didWriteUrlRef.current) {
			didWriteUrlRef.current = true;
			return;
		}
		const params = new URLSearchParams(window.location.search);
		const prefix = `${id}.`;
		for (const key of Array.from(params.keys())) {
			if (key.startsWith(prefix)) params.delete(key);
		}
		if (filterText) params.set(`${prefix}q`, filterText);
		// The initial sort is the page default, so it never goes into the URL.
		const isDefaultSort = sortKey === (initialSort?.key ?? null) && sortDir === (initialSort?.dir ?? null);
		if (sortKey && sortDir && !isDefaultSort) params.set(`${prefix}sort`, `${sortKey}:${sortDir}`);
		if (clampedPage > 1) params.set(`${prefix}page`, String(clampedPage));
		for (const [k, vals] of Object.entries(activeFacets)) {
			if (vals.length) params.set(`${prefix}${k}`, vals.join(','));
		}
		const qs = params.toString();
		const newUrl = `${window.location.pathname}${qs ? `?${qs}` : ''}${window.location.hash}`;
		const current = `${window.location.pathname}${window.location.search}${window.location.hash}`;
		if (newUrl !== current) window.history.replaceState(window.history.state, '', newUrl);
	}, [id, filterText, activeFacets, sortKey, sortDir, clampedPage, initialSort]);

	// Scroll a revealed row into view once its page has actually rendered.
	useEffect(() => {
		if (!revealId) return;
		const el = document.getElementById(revealId);
		if (!el) return;
		el.scrollIntoView({ block: 'center' });
		el.classList.add('dtbl-row-highlight');
		const timer = setTimeout(() => {
			el.classList.remove('dtbl-row-highlight');
		}, 2000);
		setRevealId(null);
		return () => clearTimeout(timer);
	}, [revealId, pageRows]);

	// The three-way cycle (asc -> desc -> clear) needs both the previous key
	// and dir together, so read them off the refs above rather than stale
	// closures.
	const onHeaderClick = useCallback((key: string) => {
		ensureFullRows();
		setPage(1);
		if (sortKeyRef.current !== key) {
			setSortKey(key);
			setSortDir('asc');
			return;
		}
		if (sortDirRef.current === 'asc') {
			setSortDir('desc');
			return;
		}
		if (sortDirRef.current === 'desc') {
			setSortKey(null);
			setSortDir(null);
			return;
		}
		setSortDir('asc');
	}, [ensureFullRows]);

	const toggleFacet = useCallback(
		(colKey: string, value: string) => {
			ensureFullRows();
			setActiveFacets((prev) => {
				const current = prev[colKey] ?? [];
				const next = current.includes(value) ? current.filter((v) => v !== value) : [...current, value];
				const copy = { ...prev };
				if (next.length === 0) delete copy[colKey];
				else copy[colKey] = next;
				return copy;
			});
			setPage(1);
		},
		[ensureFullRows]
	);

	const handleClearAll = useCallback(() => {
		setFilterText('');
		setActiveFacets({});
		setPage(1);
	}, []);

	const handleShowAll = useCallback(() => {
		ensureFullRows();
		setPageSize(0);
		setPage(1);
		try {
			window.sessionStorage.setItem(`dtbl:${id}:showAll`, '1');
		} catch {
			/* ignore */
		}
	}, [id, ensureFullRows]);

	const goToPage = useCallback(
		(next: number) => {
			ensureFullRows();
			setPage(next);
		},
		[ensureFullRows]
	);

	const hasActiveFacets = Object.values(activeFacets).some((v) => v.length > 0);

	return (
		<div className="dtbl-root">
			<div className="dtbl-controls">
				<div className="dtbl-search">
					<label htmlFor={`${id}-filter`}>Filter</label>
					<input
						id={`${id}-filter`}
						type="text"
						value={filterText}
						onFocus={ensureFullRows}
						onChange={(e) => {
							setFilterText(e.target.value);
							setPage(1);
						}}
						placeholder="Type to filter"
						autoComplete="off"
					/>
				</div>

				{facetColumns.length > 0 && (
					<div className="dtbl-facets">
						{facetColumns.map((col) => (
							<fieldset className="dtbl-facet-group" key={col.key}>
								<legend>{col.label}</legend>
								<div className="dtbl-chip-row">
									{(facetValues[col.key] ?? []).map((val) => {
										const active = (activeFacets[col.key] ?? []).includes(val);
										return (
											<button
												type="button"
												key={val}
												className={active ? 'dtbl-chip-btn dtbl-chip-btn-active' : 'dtbl-chip-btn'}
												aria-pressed={active}
												onClick={() => toggleFacet(col.key, val)}
											>
												{val}
											</button>
										);
									})}
								</div>
							</fieldset>
						))}
					</div>
				)}

				{(filterText || hasActiveFacets) && (
					<button type="button" className="dtbl-clear-btn" onClick={handleClearAll}>
						Clear filters
					</button>
				)}

				<p className="dtbl-count" aria-live="polite">
					{srcLoading && <span className="dtbl-loading">Loading full list… </span>}
					Showing {sorted.length.toLocaleString()} of {effectiveRows.length.toLocaleString()}
				</p>
			</div>

			<div className="dtbl-wrap">
				<table aria-label={caption}>
					{caption && <caption>{caption}</caption>}
					<colgroup>
						{columns.map((col) => (
							<col key={col.key} style={col.width ? { width: col.width } : undefined} />
						))}
					</colgroup>
					<thead>
						<tr>
							{columns.map((col) => {
								const isSortable = col.sortable !== false;
								const isActive = sortKey === col.key && !!sortDir;
								const ariaSort = !isSortable ? undefined : isActive ? (sortDir === 'asc' ? 'ascending' : 'descending') : 'none';
								return (
									<th
										key={col.key}
										scope="col"
										aria-sort={ariaSort}
										className={col.numeric ? 'dtbl-num' : undefined}
									>
										{isSortable ? (
											<button type="button" className="dtbl-sort-btn" onClick={() => onHeaderClick(col.key)}>
												<span>{col.label}</span>
												<span className="dtbl-sort-indicator" aria-hidden="true">
													{isActive ? (sortDir === 'asc' ? '▲' : '▼') : ''}
												</span>
											</button>
										) : (
											col.label
										)}
									</th>
								);
							})}
						</tr>
					</thead>
					<tbody>
						{pageRows.length === 0 ? (
							<tr>
								<td className="dtbl-empty" colSpan={columns.length}>
									{emptyText}
								</td>
							</tr>
						) : (
							pageRows.map((row, idx) => {
								const rowId = anchorKey ? String(row[anchorKey]) : undefined;
								return (
									<tr key={rowId ?? `${clampedPage}-${idx}`} id={rowId}>
										{columns.map((col) => (
											<td key={col.key} className={cellClassName(col)}>
												{renderCellContent(col, row[col.key])}
											</td>
										))}
									</tr>
								);
							})
						)}
					</tbody>
				</table>
			</div>

			{pageSize > 0 && (
				<div className="dtbl-pager">
					<button type="button" onClick={() => goToPage(Math.max(1, clampedPage - 1))} disabled={clampedPage <= 1}>
						Previous
					</button>
					<span className="dtbl-pager-status">
						Page {clampedPage} of {totalPages}
					</span>
					<button
						type="button"
						onClick={() => goToPage(Math.min(totalPages, clampedPage + 1))}
						disabled={clampedPage >= totalPages}
					>
						Next
					</button>
					<button type="button" onClick={handleShowAll}>
						Show all
					</button>
				</div>
			)}
		</div>
	);
}
