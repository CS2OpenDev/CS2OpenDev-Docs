import { musicKitRows } from '../../../lib/data/items';

export const prerender = true;

export function GET() {
	return new Response(JSON.stringify(musicKitRows()), {
		headers: { 'Content-Type': 'application/json' },
	});
}
