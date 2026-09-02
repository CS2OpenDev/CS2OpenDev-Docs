import type { Row } from '../../../components/islands/DataTable';
import { loadStickerKits } from '../../../lib/data/items';

// Prerendered at build time (this site's default output mode is static, so
// this is already the default; explicit for documentation).
export const prerender = true;

export function GET() {
	const rows: Row[] = loadStickerKits().map((k) => ({
		def_index: k.def_index,
		name: k.name,
		item_name_token: k.item_name_token,
		description: k.description,
	}));
	return new Response(JSON.stringify(rows), {
		headers: { 'Content-Type': 'application/json' },
	});
}
