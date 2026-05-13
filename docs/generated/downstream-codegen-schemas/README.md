# Downstream codegen schemas

Machine-readable schemas for CS2 entity classes, structs, enums, and game
events — kept in shapes that mirror upstream sources so any tooling that
already targets those sources works unchanged.

## Files

- **`cs2_schema.json`** — community-enriched mirror of
  [DumpSource2's `cs2.json.gz`](https://github.com/ValveResourceFormat/SchemaExplorer/blob/main/schemas/cs2.json.gz).
  Top-level: `generator`, `revision`, `version_date`, `version_time`,
  `classes`, `enums` — exactly upstream's shape.  Optional
  `annotations` blocks layer in community-curated descriptions / notes
  / warnings.  Cross-module twins (e.g. `CCSPlayerController` in both
  `client` and `server`) emit one record per `(module, name)`.

- **`gameevents_schema.json`** — community-enriched mirror of the
  parsed `.gameevents` KV1 registry.  Top-level: `events` list; each
  record preserves its parsed `name` / `comment` / `source` /
  `properties` / `fields` from the upstream KV1 source.  Same
  `annotations` enrichment pattern as `cs2_schema.json`.

## Why this shape (and not JSON Schema 2020-12)

Both files used to be JSON Schema 2020-12 documents.  Standard codegens
(quicktype, NJsonSchema, json-schema-to-typescript) couldn't handle the
layered `allOf` / `$ref` inheritance and the synthetic defs needed to
model native CS2 types (`CHandle<X>`, `CUtlVector<T>`, `Vector`, …).
Mirroring the upstream structured shape lets each consumer apply its
own type-mapping policy without fighting JSON Schema's vocabulary.

## Format reference

Full per-key documentation lives in
[`AGENTS.md`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/AGENTS.md#cs2_schemajson-format)
at the repository root.

## Auto-generated — do not hand-edit

These files are regenerated every 4 hours from upstream by
[`.github/workflows/generate-docs.yml`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/.github/workflows/generate-docs.yml).
To change the generated output, edit the generator
(`docs/generate_docs.py`) or the community overlays under
`docs/overlays/` instead.

_Last regenerated against CS2 build `10641237` (May 07 2026)._
