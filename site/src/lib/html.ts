export function escapeHtml(s: string): string {
	return s
		.replace(/&/g, '&amp;')
		.replace(/</g, '&lt;')
		.replace(/>/g, '&gt;')
		.replace(/"/g, '&quot;');
}

export function hex(n: number): string {
	return n < 0 ? `-0x${Math.abs(n).toString(16)}` : `0x${n.toString(16)}`;
}

/** Parse the string-encoded integers the schema artifact uses for size and offset. */
export function toInt(v: string | number | undefined): number | null {
	if (v === undefined || v === null) return null;
	const n = typeof v === 'number' ? v : Number.parseInt(v, 10);
	return Number.isFinite(n) ? n : null;
}
