import { itemRows } from '../../lib/data/items';

export const prerender = true;

export function GET() {
	return new Response(JSON.stringify(itemRows()), {
		headers: { 'Content-Type': 'application/json' },
	});
}
