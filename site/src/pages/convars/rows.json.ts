import { convarRows } from '../../lib/data/convars';

export const prerender = true;

export function GET() {
	return new Response(JSON.stringify(convarRows()), {
		headers: { 'Content-Type': 'application/json' },
	});
}
