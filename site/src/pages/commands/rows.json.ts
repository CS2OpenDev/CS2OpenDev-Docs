import { commandRows } from '../../lib/data/commands';

export const prerender = true;

export function GET() {
	return new Response(JSON.stringify(commandRows()), {
		headers: { 'Content-Type': 'application/json' },
	});
}
