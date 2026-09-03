import { join } from 'node:path';
import type { Row } from '../../components/islands/DataTable';
import { siteDataDir, readJsonFile, requireKeys, requireRows } from '../paths';
import { flagLegend as convarFlagLegend, type ConVarFlagLegendEntry } from './convars';

export type { ConVarFlagLegendEntry };
export { flagAnchor } from './convars';

export interface CommandRaw {
	name: string;
	flags: string[];
	help: string;
	prefix: string;
	has_completion_callback: boolean;
}

interface RawCommandsData {
	commands: CommandRaw[];
	flags: ConVarFlagLegendEntry[];
}

let cache: RawCommandsData | undefined;

export function loadCommandsData(): RawCommandsData {
	if (cache) return cache;
	const file = join(siteDataDir(), 'commands.json');
	const raw = readJsonFile<RawCommandsData>(file);
	requireKeys(file, raw, ['commands', 'flags']);
	requireRows(file, raw.commands, 'commands', ['name', 'flags', 'help', 'prefix', 'has_completion_callback']);
	requireRows(file, raw.flags, 'flags', ['name', 'convar_count', 'command_count', 'description']);
	cache = raw;
	return cache;
}

export function loadCommands(): CommandRaw[] {
	return loadCommandsData().commands;
}

/** commands.json carries its own copy of the same legend array as convars.json. */
export function flagLegend(): ConVarFlagLegendEntry[] {
	return loadCommandsData().flags ?? convarFlagLegend();
}

/** Every command as a DataTable row; shared by the page and rows.json. */
export function commandRows(): Row[] {
	return loadCommands().map((c) => ({
		name: c.name,
		completion: c.has_completion_callback ? 'Yes' : '',
		flags: c.flags,
		description: c.help,
	}));
}
