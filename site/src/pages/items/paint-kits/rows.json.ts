import { paintKitRows } from '../../../lib/data/items';

export const prerender = true;

export function GET() {
	return new Response(JSON.stringify(paintKitRows()), {
		headers: { 'Content-Type': 'application/json' },
	});
}
