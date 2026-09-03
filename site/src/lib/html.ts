export function escapeHtml(s: string): string {
	return s
		.replace(/&/g, '&amp;')
		.replace(/</g, '&lt;')
		.replace(/>/g, '&gt;')
		.replace(/"/g, '&quot;');
}

const CODE_SPAN = /`([^`]+)`/g;

/** Overlay prose as HTML: escaped text with `code spans` set in <code>, the only markup the overlays use. */
export function inlineCodeHtml(s: string): string {
	return escapeHtml(s).replace(CODE_SPAN, '<code>$1</code>');
}

/** Overlay prose for plain-text slots such as a meta description. */
export function stripInlineCode(s: string): string {
	return s.replace(CODE_SPAN, '$1');
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
