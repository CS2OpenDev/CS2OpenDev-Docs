import { stickerKitRows } from '../../../lib/data/items';

export const prerender = true;

export function GET() {
	return new Response(JSON.stringify(stickerKitRows()), {
		headers: { 'Content-Type': 'application/json' },
	});
}
