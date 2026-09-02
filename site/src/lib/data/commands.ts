import { join } from 'node:path';
import { siteDataDir, readJsonFile } from '../paths';
import { flagLegend as convarFlagLegend, type ConVarFlagLegendEntry } from './convars';

export type { ConVarFlagLegendEntry };
export { helpTextHtml, flagAnchor } from './convars';

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
	cache = readJsonFile<RawCommandsData>(join(siteDataDir(), 'commands.json'));
	return cache;
}

export function loadCommands(): CommandRaw[] {
	return loadCommandsData().commands;
}

/** commands.json carries its own copy of the same legend array as convars.json. */
export function flagLegend(): ConVarFlagLegendEntry[] {
	return loadCommandsData().flags ?? convarFlagLegend();
}
