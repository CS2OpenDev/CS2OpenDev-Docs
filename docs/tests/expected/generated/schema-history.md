---
title: Schema History
---

# Schema History

> Source: **Build 9000001** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Fixture schema-lens overlay.

> Two lines, so the blockquote continuation is covered.
> Second line.

- **Platform:** `windows-x86_64` (the canonical render; windows is a strict **superset** in class coverage — historical Windows-only tool binaries such as `hammer.dll` / `sfm.dll` have no Linux counterparts — while shared classes differ in offsets/sizes per platform)
- **Baseline build:** `8999999` · **Latest build:** `9000001`
- **Artifact schema version:** `0.8.0` (SchemaTracker's `schemas/schema_evolution.proto` family)
- **Transitions:** 2 total, **1 with structural changes** (1 no-op builds)
- **Full per-field history:** the portable [`field_history.json`](downstream-codegen-schemas/field_history.json) carries first/last-seen and the type history for every `(class, field)` across all builds.  Its `[firstSeenBuild, lastSeenBuild]` interval is a presence **hull**, not continuous presence — a field can be absent for intermediate builds with no trace there; exact presence replays from the transitions below.

To bring an instance captured under build *X* forward to build *Y*, apply each transition in `[X, Y)` in order.  Every op carries both endpoints, so the same chain replays backward.

## Evidence surfaces

The artifact is **facts-only**: it never asserts a rename, a move, or a safety verdict.  Alongside the raw add/remove ops it emits neutral *evidence* lists, each signal independently provable from the two snapshots being diffed.  Promotion to a confirmed rename happens downstream, in [`docs/overlays/schema-lens.yml`](https://github.com/CS2OpenDev/CS2OpenDev-Docs/blob/main/docs/overlays/schema-lens.yml).

| Surface | Scope | Signals | Since |
|---------|-------|---------|-------|
| `classChanged[].pairedEvidence` | removed+added field pairs within one class, greedy 1:1, pre-filtered to same offset **and** same rendered type | always exactly `offsetExact`, `typeMatch` | frozen (pre-0.6.0) |
| `classChanged[].pairCandidates` | **every** removed/added field pair within one class whose rendered types are equal **or** whose offsets are equal — N:M, deliberately unselected | `typeMatch`, `offsetExact`, `sizeMatch` (never alone) | 0.6.0 |
| `classPairCandidates` | removed/added **class** pairs sharing a bare (module-stripped) name — the cross-module move the qualified key cannot see | `bareNameMatch` (floor), `sizeMatch`, `fieldSetMatch` | 0.6.0 |
| `fieldMoveCandidates` | a same-named, same-typed field removed from one **surviving** class and added to another (hoist / push-down / sideways move) | `fieldNameMatch` + `typeMatch` (floor), `parentChainUp`, `parentChainDown` | 0.6.0 |

The candidate lists are **complete on their own** — every `pairedEvidence` pair reappears in `pairCandidates`, so consumers never need to union the two surfaces.  A 1:1 pick among tied candidates would be an inference, which is why the wider surfaces stay unselected; `offsetAdjacent` is never emitted (any adjacency threshold is consumer policy, not a fact).  `pairedEvidence` itself is frozen for compatibility.

Later artifact revisions add further facts: **0.7.0** covers class-attribute changes (`staticFieldOps`, `cppName`, `projectName`, inheritance depths, `flags2`) and a calendar axis — each transition carries `fromManifestCreatedUtc` / `toManifestCreatedUtc`, verbatim from the two builds' Steam provenance records; **0.8.0** adds structured per-key metadata ops (`metaOps` on classes, fields, and enum members; values over 256 UTF-8 bytes are carried as a SHA-256 hash + byte count instead of inline).

## Transitions with structural changes

| Transition | Date | Classes +/−/~ | Enums +/−/~ | Field ops |
|------------|------|---------------|-------------|-----------|
| `8999999` → `9000000` | 2026-08-14 | 1 / 0 / 1 | 0 / 0 / 0 | 2 |

## Most recent structural changes

### `8999999` → `9000000`

*Steam manifests created `2026-08-01T00:00:00Z` → `2026-08-14T00:00:00Z`*

**Classes added (1):** `CBaseAnimGraph`

**Classes changed (1):**

| Class | Field ops | Layout |
|-------|-----------|--------|
| `CBaseCombatCharacter` | ＋field×1, ~offset×1 | resize 1000→1008 |
