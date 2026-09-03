import { loadSchemaIndex } from './data/schema';

/** One line naming the artifact every page on the site is projected from. */
export function provenanceLine(): string {
	const p = loadSchemaIndex().provenance;
	return `CS2 build ${p.buildId} · Steam date ${p.versionDate} · platform ${p.platform} · schema format ${p.schemaFormatVersion}`;
}
