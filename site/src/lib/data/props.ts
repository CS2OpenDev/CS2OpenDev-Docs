import { join } from 'node:path';
import { readJsonFile, requireKeys, requireRows, siteDataDir } from '../paths';

export interface CollisionGroup {
	name: string;
	type: string;
	description: string;
	interact_as: string[];
	interact_with: string[];
	interact_exclude: string[];
}

export interface PropProperty {
	name: string;
	value: string;
}

export interface PropClass {
	id: string;
	properties: PropProperty[];
}

export interface BreakableModelGroup {
	id: string;
	models: string[];
}

interface RawPropsData {
	breakable_models: BreakableModelGroup[];
	collision_groups: CollisionGroup[];
	prop_classes: PropClass[];
}

export interface PropsIndex {
	collisionGroups: CollisionGroup[];
	propClasses: PropClass[];
	breakableModels: BreakableModelGroup[];
}

let cache: PropsIndex | undefined;

export function loadProps(): PropsIndex {
	if (cache) return cache;
	const file = join(siteDataDir(), 'props.json');
	const raw = readJsonFile<RawPropsData>(file);
	requireKeys(file, raw, ['breakable_models', 'collision_groups', 'prop_classes']);
	requireRows(file, raw.collision_groups, 'collision_groups', [
		'name',
		'type',
		'description',
		'interact_as',
		'interact_with',
		'interact_exclude',
	]);
	requireRows(file, raw.prop_classes, 'prop_classes', ['id', 'properties']);
	requireRows(file, raw.breakable_models, 'breakable_models', ['id', 'models']);
	cache = {
		collisionGroups: raw.collision_groups,
		propClasses: raw.prop_classes,
		breakableModels: raw.breakable_models,
	};
	return cache;
}
