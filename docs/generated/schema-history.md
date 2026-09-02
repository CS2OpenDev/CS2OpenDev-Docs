---
layout: default
title: Schema History
nav_order: 15
---

# Schema History

> Source: **Build 25000182** · 2026-08-28 · `windows-x86_64` · schema `0.10.0`

Field-precise, build-to-build evolution of the CS2 C++ entity schema, derived by diffing every committed `entity_schema.json` snapshot (SchemaTracker's cumulative `schema_evolution.json`, Layer A).  Unlike the coarse [Changelog](changelog.md) — which only reports *that* a class changed — this reports *which field* was added, removed, retyped, or moved.

- **Platform:** `windows-x86_64` (the canonical render; windows is a strict **superset** in class coverage — historical Windows-only tool binaries such as `hammer.dll` / `sfm.dll` have no Linux counterparts — while shared classes differ in offsets/sizes per platform)
- **Baseline build:** `10832117` · **Latest build:** `25000182`
- **Artifact schema version:** `0.10.0` (SchemaTracker's `schemas/schema_evolution.proto` family)
- **Transitions:** 386 total, **143 with structural changes** (243 no-op builds)
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
| `24934554` → `24957633` | 2026-08-26 | 0 / 0 / 6 | 0 / 0 / 0 | 10 |
| `24828357` → `24916958` | 2026-08-24 | 10 / 0 / 3 | 1 / 0 / 1 | 0 |
| `24701871` → `24828357` | 2026-08-19 | 0 / 0 / 2 | 0 / 0 / 0 | 0 |
| `24662694` → `24701871` | 2026-08-12 | 0 / 0 / 2 | 0 / 0 / 0 | 0 |
| `24442510` → `24537688` | 2026-08-03 | 0 / 0 / 6 | 0 / 0 / 0 | 99 |
| `24304127` → `24442510` | 2026-07-29 | 0 / 0 / 0 | 0 / 0 / 1 | 0 |
| `24248951` → `24304127` | 2026-07-20 | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `24074625` → `24116939` | 2026-07-08 | 232 / 59 / 1097 | 96 / 15 / 62 | 4792 |
| `23773332` → `23994866` | 2026-07-01 | 0 / 0 / 1 | 0 / 0 / 0 | 5 |
| `23333587` → `23354238` | 2026-05-22 | 0 / 0 / 1 | 0 / 0 / 0 | 11 |
| `23296257` → `23333587` | 2026-05-20 | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `23241720` → `23296257` | 2026-05-18 | 0 / 0 / 6 | 0 / 0 / 0 | 30 |
| `23187627` → `23241720` | 2026-05-14 | 0 / 0 / 2 | 0 / 0 / 0 | 122 |
| `23118419` → `23135875` | 2026-05-07 | 0 / 0 / 10 | 0 / 0 / 0 | 294 |
| `23018732` → `23038025` | 2026-04-30 | 0 / 0 / 6 | 0 / 0 / 0 | 161 |
| `22948967` → `23000122` | 2026-04-28 | 0 / 2 / 12 | 0 / 1 / 0 | 174 |
| `22880072` → `22894272` | 2026-04-21 | 2 / 0 / 5 | 0 / 0 / 0 | 216 |
| `22877907` → `22880072` | 2026-04-21 | 775 / 0 / 0 | 49 / 0 / 0 | 0 |
| `22876476` → `22877907` | 2026-04-21 | 0 / 775 / 2 | 0 / 49 / 0 | 118 |
| `22627914` → `22876476` | 2026-04-20 | 164 / 28 / 4630 | 36 / 3 / 16 | 11112 |
| `22370414` → `22405124` | 2026-03-18 | 0 / 0 / 3 | 0 / 0 / 0 | 13 |
| `22336282` → `22368164` | 2026-03-16 | 0 / 0 / 1 | 0 / 0 / 0 | 9 |
| `22266770` → `22303696` | 2026-03-11 | 0 / 0 / 1 | 0 / 0 / 0 | 120 |
| `21868850` → `22063930` | 2026-02-23 | 0 / 0 / 1 | 0 / 0 / 0 | 120 |
| `21708006` → `21789745` | 2026-02-04 | 0 / 0 / 5 | 0 / 0 / 0 | 195 |
| `21626952` → `21657141` | 2026-01-26 | 0 / 0 / 1 | 0 / 0 / 0 | 1 |
| `21609678` → `21626952` | 2026-01-24 | 0 / 0 / 1 | 0 / 0 / 0 | 4 |
| `21595680` → `21609678` | 2026-01-22 | 0 / 0 / 9 | 0 / 0 / 0 | 52 |
| `21529689` → `21593048` | 2026-01-21 | 437 / 16 / 1087 | 32 / 3 / 18 | 7627 |
| `20670159` → `20775075` | 2025-11-12 | 0 / 0 / 10 | 0 / 0 / 1 | 35 |
| `20596740` → `20670159` | 2025-11-04 | 0 / 0 / 4 | 0 / 0 / 0 | 6 |
| `20535897` → `20596740` | 2025-10-29 | 2 / 2 / 32 | 0 / 0 / 0 | 95 |
| `20442176` → `20503857` | 2025-10-22 | 2 / 0 / 7 | 0 / 0 / 0 | 155 |
| `20392228` → `20410358` | 2025-10-15 | 0 / 0 / 3 | 0 / 0 / 0 | 44 |
| `20278147` → `20392228` | 2025-10-14 | 90 / 15 / 1373 | 9 / 1 / 13 | 5927 |
| `20215164` → `20230584` | 2025-10-02 | 2 / 0 / 6 | 0 / 0 / 0 | 0 |
| `20116868` → `20134212` | 2025-09-26 | 0 / 0 / 8 | 0 / 0 / 0 | 109 |
| `20101391` → `20116868` | 2025-09-24 | 0 / 0 / 3 | 0 / 0 / 0 | 0 |
| `20084900` → `20101391` | 2025-09-24 | 0 / 0 / 2 | 0 / 0 / 0 | 18 |
| `20024151` → `20040136` | 2025-09-19 | 2 / 2 / 3 | 0 / 0 / 0 | 14 |
| `20022951` → `20024151` | 2025-09-18 | 0 / 0 / 2 | 0 / 0 / 0 | 2 |
| `20011206` → `20022951` | 2025-09-17 | 0 / 0 / 2 | 0 / 0 / 0 | 16 |
| `19932965` → `20007038` | 2025-09-16 | 20 / 49 / 1634 | 11 / 5 / 8 | 2941 |
| `19903381` → `19916932` | 2025-09-09 | 0 / 0 / 1 | 0 / 0 / 0 | 71 |
| `19762064` → `19847200` | 2025-09-03 | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `19657793` → `19747060` | 2025-08-26 | 0 / 0 / 20 | 1 / 0 / 0 | 216 |
| `19605004` → `19644975` | 2025-08-18 | 0 / 0 / 9 | 0 / 0 / 0 | 290 |
| `19450283` → `19602992` | 2025-08-14 | 57 / 301 / 249 | 15 / 14 / 19 | 985 |
| `19421827` → `19450283` | 2025-08-01 | 0 / 0 / 2 | 0 / 0 / 0 | 8 |
| `19406478` → `19421827` | 2025-07-31 | 0 / 0 / 48 | 0 / 0 / 0 | 41 |
| `19391961` → `19406478` | 2025-07-30 | 0 / 0 / 50 | 0 / 0 / 0 | 75 |
| `19251152` → `19388062` | 2025-07-28 | 1442 / 204 / 2638 | 99 / 16 / 58 | 8194 |
| `19222571` → `19236816` | 2025-07-15 | 0 / 0 / 1 | 0 / 0 / 0 | 89 |
| `18816418` → `19083876` | 2025-07-02 | 0 / 1 / 5 | 0 / 0 / 1 | 7 |
| `18382650` → `18394927` | 2025-05-08 | 0 / 0 / 2 | 0 / 0 / 0 | 4 |
| `18185360` → `18380903` | 2025-05-07 | 1 / 0 / 5 | 0 / 0 / 0 | 320 |
| `17800215` → `17931128` | 2025-03-31 | 0 / 27 / 48 | 0 / 0 / 3 | 87 |
| `17732524` → `17800215` | 2025-03-20 | 0 / 0 / 8 | 0 / 0 / 0 | 248 |
| `17230622` → `17272995` | 2025-02-06 | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `17148705` → `17162095` | 2025-01-28 | 0 / 0 / 1 | 0 / 0 / 0 | 2 |
| `17032840` → `17084099` | 2025-01-21 | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `16958277` → `17006600` | 2025-01-15 | 0 / 0 / 1 | 0 / 0 / 0 | 3 |
| `16806987` → `16933364` | 2025-01-07 | 0 / 0 / 2 | 0 / 0 / 0 | 45 |
| `16687167` → `16794210` | 2024-12-19 | 0 / 0 / 10 | 0 / 0 / 0 | 11 |
| `16382602` → `16398395` | 2024-11-13 | 1 / 0 / 16 | 1 / 0 / 1 | 203 |
| `16243257` → `16320304` | 2024-11-06 | 6 / 0 / 8 | 0 / 0 / 0 | 66 |
| `16213816` → `16228412` | 2024-10-29 | 0 / 0 / 2 | 0 / 0 / 0 | 5 |
| `16184206` → `16213816` | 2024-10-29 | 0 / 0 / 65 | 0 / 0 / 0 | 207 |
| `16087659` → `16156846` | 2024-10-23 | 0 / 0 / 114 | 0 / 0 / 0 | 90 |
| `16071819` → `16087659` | 2024-10-17 | 0 / 0 / 4 | 0 / 0 / 0 | 3 |
| `16015437` → `16057663` | 2024-10-15 | 7 / 1 / 474 | 1 / 0 / 0 | 3002 |
| `15923186` → `15936283` | 2024-10-05 | 0 / 0 / 2 | 1 / 0 / 0 | 14 |
| `15656858` → `15908369` | 2024-10-02 | 251 / 10 / 1417 | 38 / 1 / 20 | 8801 |
| `15582507` → `15644071` | 2024-09-09 | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `15372392` → `15424813` | 2024-08-19 | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `15324295` → `15372392` | 2024-08-14 | 2 / 0 / 13 | 0 / 0 / 0 | 368 |
| `15309899` → `15312306` | 2024-08-09 | 0 / 0 / 1 | 0 / 0 / 0 | 1 |
| `15155775` → `15309899` | 2024-08-08 | 0 / 0 / 2 | 0 / 0 / 0 | 28 |
| `14851576` → `14864281` | 2024-06-27 | 42 / 0 / 0 | 14 / 0 / 0 | 0 |
| `14850494` → `14851576` | 2024-06-26 | 0 / 42 / 0 | 0 / 14 / 0 | 0 |
| `14787627` → `14836768` | 2024-06-25 | 0 / 0 / 69 | 0 / 0 / 1 | 314 |
| `14684351` → `14711932` | 2024-06-13 | 0 / 0 / 1 | 0 / 0 / 0 | 1 |
| `14672345` → `14684351` | 2024-06-11 | 0 / 0 / 5 | 0 / 0 / 0 | 125 |
| `14553911` → `14602005` | 2024-06-04 | 0 / 20 / 9 | 0 / 0 / 1 | 12 |
| `14487420` → `14536966` | 2024-05-29 | 0 / 0 / 59 | 0 / 0 / 0 | 66 |
| `14446408` → `14470938` | 2024-05-23 | 224 / 41 / 1049 | 40 / 2 / 26 | 6767 |
| `14249031` → `14296060` | 2024-05-07 | 0 / 1 / 0 | 0 / 0 / 0 | 0 |
| `14191516` → `14225153` | 2024-04-30 | 0 / 0 / 1 | 0 / 0 / 0 | 1 |
| `14139085` → `14178987` | 2024-04-25 | 0 / 1 / 134 | 0 / 0 / 1 | 680 |
| `14075664` → `14139085` | 2024-04-23 | 0 / 0 / 9 | 0 / 0 / 0 | 136 |
| `13804656` → `13829089` | 2024-03-23 | 0 / 0 / 1 | 0 / 0 / 0 | 1 |
| `13735017` → `13758187` | 2024-03-15 | 0 / 0 / 2 | 0 / 0 / 0 | 1 |
| `13687128` → `13735017` | 2024-03-14 | 0 / 0 / 1 | 0 / 0 / 0 | 7 |
| `13481434` → `13593156` | 2024-02-28 | 0 / 0 / 10 | 0 / 0 / 1 | 113 |
| `13460160` → `13470915` | 2024-02-16 | 0 / 0 / 3 | 0 / 0 / 0 | 8 |
| `13439412` → `13460160` | 2024-02-15 | 41 / 0 / 0 | 3 / 0 / 0 | 0 |
| `13438770` → `13439412` | 2024-02-13 | 0 / 41 / 0 | 0 / 3 / 0 | 0 |
| `13240071` → `13385739` | 2024-02-06 | 129 / 32 / 2674 | 355 / 0 / 0 | 13991 |
| `12957241` → `12995320` | 2023-12-18 | 0 / 0 / 1 | 0 / 0 / 0 | 2 |
| `12934552` → `12956327` | 2023-12-14 | 0 / 0 / 64 | 0 / 0 / 0 | 232 |
| `12895370` → `12905434` | 2023-12-07 | 0 / 0 / 10 | 0 / 0 / 0 | 12 |
| `12873276` → `12895370` | 2023-12-07 | 0 / 0 / 73 | 0 / 0 / 0 | 179 |
| `12854667` → `12873276` | 2023-12-04 | 0 / 0 / 12 | 0 / 0 / 0 | 92 |
| `12756335` → `12843950` | 2023-11-30 | 0 / 19 / 119 | 0 / 0 / 0 | 213 |
| `12736853` → `12756335` | 2023-11-21 | 1 / 0 / 0 | 0 / 0 / 0 | 0 |
| `12725887` → `12726829` | 2023-11-17 | 0 / 0 / 2 | 0 / 0 / 0 | 0 |
| `12693482` → `12725887` | 2023-11-17 | 2 / 0 / 86 | 0 / 0 / 0 | 230 |
| `12666450` → `12693482` | 2023-11-13 | 0 / 0 / 7 | 0 / 0 / 0 | 307 |
| `12656218` → `12666450` | 2023-11-10 | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `12617548` → `12656218` | 2023-11-09 | 0 / 0 / 119 | 0 / 0 / 0 | 172 |
| `12616847` → `12617548` | 2023-11-04 | 60 / 0 / 0 | 0 / 0 / 0 | 0 |
| `12616521` → `12616847` | 2023-11-04 | 0 / 60 / 0 | 0 / 0 / 0 | 0 |
| `12607859` → `12616521` | 2023-11-03 | 0 / 0 / 17 | 0 / 0 / 0 | 369 |
| `12547359` → `12606072` | 2023-11-02 | 11 / 0 / 149 | 0 / 0 / 0 | 951 |
| `12494887` → `12535846` | 2023-10-25 | 1 / 0 / 2 | 0 / 0 / 0 | 8 |
| `12465841` → `12485612` | 2023-10-19 | 1 / 0 / 56 | 0 / 0 / 0 | 95 |
| `12438553` → `12465841` | 2023-10-17 | 1 / 0 / 10 | 0 / 0 / 0 | 238 |
| `12416747` → `12427908` | 2023-10-12 | 2 / 0 / 33 | 0 / 0 / 0 | 113 |
| `12377892` → `12398121` | 2023-10-09 | 0 / 0 / 5 | 0 / 0 / 0 | 7 |
| `12349504` → `12358457` | 2023-10-04 | 0 / 0 / 6 | 0 / 0 / 0 | 156 |
| `12328020` → `12338824` | 2023-10-02 | 0 / 0 / 54 | 0 / 0 / 0 | 53 |
| `12312218` → `12321656` | 2023-09-29 | 0 / 0 / 2 | 0 / 0 / 0 | 2 |
| `12192623` → `12299470` | 2023-09-27 | 45 / 94 / 297 | 0 / 0 / 0 | 2088 |
| `12184506` → `12192623` | 2023-09-14 | 0 / 0 / 9 | 0 / 0 / 0 | 10 |
| `12147839` → `12182426` | 2023-09-13 | 0 / 1 / 308 | 0 / 0 / 0 | 2056 |
| `12136709` → `12146510` | 2023-09-08 | 0 / 0 / 5 | 0 / 0 / 0 | 126 |
| `12085105` → `12093437` | 2023-09-02 | 0 / 0 / 7 | 0 / 0 / 0 | 70 |
| `11979365` → `12083517` | 2023-08-31 | 20 / 6 / 95 | 0 / 0 / 0 | 745 |
| `11887584` → `11949605` | 2023-08-15 | 2 / 0 / 86 | 0 / 0 / 0 | 298 |
| `11852153` → `11862226` | 2023-08-03 | 1 / 1 / 4 | 0 / 0 / 0 | 20 |
| `11785765` → `11852153` | 2023-08-02 | 10 / 3 / 184 | 0 / 0 / 0 | 1092 |
| `11732520` → `11743491` | 2023-07-19 | 0 / 0 / 1 | 0 / 0 / 0 | 0 |
| `11724280` → `11732520` | 2023-07-18 | 0 / 0 / 54 | 0 / 0 / 0 | 106 |
| `11602641` → `11723163` | 2023-07-17 | 13 / 10 / 23 | 0 / 0 / 0 | 421 |
| `11593506` → `11602641` | 2023-06-30 | 0 / 0 / 1 | 0 / 0 / 0 | 108 |
| `11519750` → `11593506` | 2023-06-29 | 16 / 131 / 358 | 0 / 0 / 0 | 2801 |
| `11473523` → `11483104` | 2023-06-15 | 0 / 0 / 4 | 0 / 0 / 0 | 6 |
| `11437123` → `11472786` | 2023-06-14 | 4 / 1 / 24 | 0 / 0 / 0 | 99 |
| `11428378` → `11437123` | 2023-06-09 | 0 / 0 / 2 | 0 / 0 / 0 | 4 |
| `11408339` → `11418830` | 2023-06-07 | 0 / 0 / 2 | 0 / 0 / 0 | 4 |
| `11081546` → `11408339` | 2023-06-06 | 173 / 135 / 1334 | 0 / 0 / 0 | 8789 |
| `10894923` → `10898038` | 2023-03-31 | 4 / 0 / 2 | 0 / 0 / 0 | 8 |
| `10853092` → `10894923` | 2023-03-30 | 50 / 11 / 503 | 0 / 0 / 0 | 3133 |

## Most recent structural changes

### `24934554` → `24957633`

*Steam manifests created `2026-08-25T18:35:52Z` → `2026-08-26T20:58:46Z`*

**Classes changed (6):**

| Class | Field ops | Layout |
|-------|-----------|--------|
| `!GlobalTypes/dynpitchvol_base_t` | meta×1 | — |
| `!GlobalTypes/dynpitchvol_t` | meta×1 | — |
| `client.dll/CCSCustomHudLayout` | ~offset×3 | resize 2096→2088 |
| `client.dll/CCSCustomHudLayoutState` | ~offset×2 | resize 272→264 |
| `server.dll/CCSCustomHudLayout` | ~offset×3 | resize 2032→2024 |
| `server.dll/CCSCustomHudLayoutState` | ~offset×2 | resize 416→408 |

### `24828357` → `24916958`

*Steam manifests created `2026-08-19T23:16:48Z` → `2026-08-24T23:15:06Z`*

**Classes added (10):** `!GlobalTypes/HUDPanelDialogVariableString_t`, `!GlobalTypes/HUDPanelHasClass_t`, `client.dll/CCSCustomHudLayout`, `client.dll/CCSCustomHudLayoutState`, `client.dll/CCSCustomHudLayout_API`, `client.dll/CCSPlayerCamera`, `server.dll/CCSCustomHudLayout`, `server.dll/CCSCustomHudLayoutState`, `server.dll/CCSCustomHudLayout_API`, `server.dll/CCSPlayerCamera`

**Classes changed (3):**

| Class | Field ops | Layout |
|-------|-----------|--------|
| `!GlobalTypes/dynpitchvol_base_t` | meta×1 | — |
| `!GlobalTypes/dynpitchvol_t` | meta×1 | — |
| `server.dll/CCSPointScriptEntity` | — | resize 1552→1576 |

### `24701871` → `24828357`

*Steam manifests created `2026-08-12T22:20:36Z` → `2026-08-19T23:16:48Z`*

**Classes changed (2):**

| Class | Field ops | Layout |
|-------|-----------|--------|
| `!GlobalTypes/dynpitchvol_base_t` | meta×1 | — |
| `!GlobalTypes/dynpitchvol_t` | meta×1 | — |
