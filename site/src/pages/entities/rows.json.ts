import { entityIoRows } from '../../lib/data/entity_io';

export const prerender = true;

export function GET() {
	return new Response(JSON.stringify(entityIoRows()), {
		headers: { 'Content-Type': 'application/json' },
	});
}
