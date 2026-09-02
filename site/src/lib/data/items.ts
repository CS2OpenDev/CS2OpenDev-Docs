import { join } from 'node:path';
import type { Row } from '../../components/islands/DataTable';
import { readJsonFile, siteDataDir } from '../paths';

export interface ItemResolution {
	classname: string;
	descriptionToken: string;
	itemSlot: string;
	itemTypeName: string;
	nameToken: string;
}

export interface Item {
	def_index: number;
	name: string;
	classname: string;
	name_token: string;
	item_type_name: string;
	item_slot: string;
	description_token: string;
	is_default: boolean;
	prefab_id: string;
	quality: string | null;
	rarity: string | null;
	resolution: ItemResolution;
}

export interface Prefab {
	id: string;
	classname: string;
	item_slot: string;
	item_type_name: string;
	name_token: string;
	parent_prefab: string;
}

export interface Rarity {
	id: string;
	loc_key: string;
	loc_key_weapon: string;
	value: number;
}

export interface Quality {
	id: string;
	value: number;
}

interface RawItems {
	items: Item[];
	prefabs: Prefab[];
	rarities: Rarity[];
	qualities: Quality[];
	note: string;
}

export interface PaintKit {
	def_index: number;
	name: string;
	description_tag: string;
}

export interface StickerKit {
	def_index: number;
	name: string;
	description: string;
	item_name_token: string;
}

export interface MusicKit {
	def_index: number;
	name: string;
	loc_name: string;
}

let itemsCache: RawItems | undefined;
let paintKitsCache: PaintKit[] | undefined;
let stickerKitsCache: StickerKit[] | undefined;
let musicKitsCache: MusicKit[] | undefined;

export function loadItems(): RawItems {
	itemsCache ??= readJsonFile<RawItems>(join(siteDataDir(), 'items.json'));
	return itemsCache;
}

export function loadPaintKits(): PaintKit[] {
	paintKitsCache ??= readJsonFile<{ paint_kits: PaintKit[] }>(join(siteDataDir(), 'paint_kits.json')).paint_kits;
	return paintKitsCache;
}

export function loadStickerKits(): StickerKit[] {
	stickerKitsCache ??= readJsonFile<{ sticker_kits: StickerKit[] }>(
		join(siteDataDir(), 'sticker_kits.json')
	).sticker_kits;
	return stickerKitsCache;
}

export function loadMusicKits(): MusicKit[] {
	musicKitsCache ??= readJsonFile<{ music_kits: MusicKit[] }>(join(siteDataDir(), 'music_kits.json')).music_kits;
	return musicKitsCache;
}

// DataTable rows for the four tables. Each page slices its first page from the
// same array its rows.json serves, so the two agree row for row.

export function itemRows(): Row[] {
	return loadItems().items.map((it) => ({
		def_index: it.def_index,
		name: it.name,
		prefab_id: it.prefab_id,
		item_type_name: it.item_type_name ? [it.item_type_name] : [],
		classname: it.classname,
		name_token: it.name_token,
	}));
}

export function paintKitRows(): Row[] {
	return loadPaintKits().map((k) => ({
		def_index: k.def_index,
		name: k.name,
		description_tag: k.description_tag,
	}));
}

export function stickerKitRows(): Row[] {
	return loadStickerKits().map((k) => ({
		def_index: k.def_index,
		name: k.name,
		item_name_token: k.item_name_token,
		description: k.description,
	}));
}

export function musicKitRows(): Row[] {
	return loadMusicKits().map((k) => ({
		def_index: k.def_index,
		name: k.name,
		loc_name: k.loc_name,
	}));
}
