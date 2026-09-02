import { gameEventRows } from '../../lib/data/gameevents';

export const prerender = true;

export function GET() {
	return new Response(JSON.stringify(gameEventRows()), {
		headers: { 'Content-Type': 'application/json' },
	});
}
