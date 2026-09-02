import { join } from 'node:path';
import { readJsonFile, siteDataDir } from '../paths';

export interface CollisionGroup {
	name: string;
	type: string;
	description: string;
	interact_as: string[];
	interact_with: string[];
	interact_exclude: string[];
}

interface RawPropsData {
	breakable_models: unknown[];
	collision_groups: CollisionGroup[];
	prop_classes: unknown[];
}

let cache: CollisionGroup[] | undefined;

export function loadCollisionGroups(): CollisionGroup[] {
	if (cache) return cache;
	const raw = readJsonFile<RawPropsData>(join(siteDataDir(), 'props.json'));
	cache = raw.collision_groups;
	return cache;
}
