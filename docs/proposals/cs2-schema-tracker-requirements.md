---
title: "Proposal: CS2-Schema-Tracker requirements"
parent: Proposals
nav_exclude: true
---

## Context

The `CS2OpenDev-Docs` repo currently depends on three external upstreams for every piece of structured CS2 data it republishes: `SteamDatabase/GameTracking-CS2` (protobufs, `.gameevents`, convars/commands as text), `ValveResourceFormat/DumpSource2` (the actual binary-walking tool that produces the structured schema dump), and `ValveResourceFormat/SchemaExplorer` (the gzipped `cs2.json.gz` distribution of those dumps). Those upstreams ship at their own cadence, mix CS2 data with unrelated assets, expose different data shapes for different artifacts, gate the historical depth and per-architecture granularity available to downstream consumers (today: 17 entity-schema snapshots over 10 weeks, no per-architecture differentiation), and offer no provenance back to the binary bytes the data was extracted from.

This document specifies `CS2OpenDev/CS2-Schema-Tracker` — a new, independent extraction system that produces a single internally consistent set of artifacts directly from CS2 game binaries. It eliminates the three upstream dependencies, supports four per-(OS, architecture, target) tuples, records verifiable provenance for every artifact, and commits one artifact set per CS2 build to a dedicated public git repository with build-ID-tagged history walked from the earliest reachable Source 2 CS2 build (CS2 Limited Test, Steam build 1555, 2023-03-22) forward.

Once every requirement in this document is satisfied, the system is operational: it produces deterministic per-build artifacts without manual intervention, with full provenance and schema-validated output, replacing the GameTracking-CS2 / DumpSource2 / SchemaExplorer dependencies in `CS2OpenDev-Docs` and any future downstream consumer.

---

## Goals (in priority order)

1. **Highest possible artifact quality** — every output traceable to a specific byte range in a specific binary with a recorded SHA-256.
2. **Determinism** — same tool version + same input binaries ⇒ byte-identical output.
3. **Independence** — zero runtime dependency on GameTracking-CS2, DumpSource2, SchemaExplorer, or any other third-party CS2-data-extracting project.
4. **Per-(OS, arch, target) granularity** — Linux+Windows × server+client, four tuples, separate artifact sets per tuple.
5. **Long-term low maintenance, subject to goals 1–4** — within the quality/determinism/independence/granularity constraints, choose technologies that minimize ongoing cost; prefer batch tooling that survives Valve format changes via localized patches. The hybrid C++/C# split (see "Technology choices") accepts a two-toolchain cost in exchange for goals 1 and 2.

## Non-goals

- Attaching to a running CS2 game process (no `ReadProcessMemory` / debugger attach). The tool loads CS2 binaries into its **own** process via `dlopen` / `LoadLibrary` and walks them there; the game itself is never running. See "Extraction approach" below for why pure static binary analysis is not viable for the schema system specifically.
- Asset extraction beyond the schema/document scope (no maps, models, sounds, localizations).
- Replacing the Jekyll docs site itself — `CS2OpenDev-Docs` continues to render markdown; only its *data inputs* change.
- Supporting Source 1 CS:GO (pre-2023-03-22). Out of physical reach: no comparable schema reflection system exists.
- Mac client binaries (Valve ships them irregularly; excluded from v1 scope).
- Heuristic / probabilistic schema reconstruction. The system records only what is directly extractable from binaries.
- Steam `prerelease` / non-public branches for v1 (public branch only; prerelease coverage is a v1.1 candidate).

---

## Output artifacts (catalog — these filenames are part of the public consumer contract)

Every output is emitted **once per (Steam build, OS, architecture, target) tuple** where target ∈ {server, client}. `server` means the dedicated-server binaries (`server.dll`/`.so`, `tier0`, `schemasystem`, dedicated-server-only modules). `client` means the game-client binaries (`client.dll`/`.so` plus the larger client-side module set). Server and client are separate Steam depots with distinct binary content; per-tuple artifact sets reflect that. The four targeted tuples for v1:

- `linux-x86_64.server`
- `windows-x86_64.server`
- `linux-x86_64.client`
- `windows-x86_64.client`

For each tuple, the system produces:

| Artifact | Filename | What it carries | Primary source |
|---|---|---|---|
| Entity schema | `entity_schema.json` | Classes, structs, enums, fields with offsets/sizes/types/metadata, parent chains, KV3 defaults | Schema system in binary |
| Protobuf descriptors | `protos/<file>.proto` (per descriptor file) + `protos.descriptorset` | Network message definitions, round-tripped to `.proto` text + a `FileDescriptorSet` binary | Embedded `FileDescriptorProto`s in binary |
| Game events | `gameevents.json` | KV1 game-event registry, structurally parsed | `.gameevents` files inside `pak01_dir.vpk` |
| ConVars | `convars.json` | Every console variable: name, default, flags, description | ConCommandBase registry in binary |
| Commands | `commands.json` | Every console command: name, flags, description | ConCommandBase registry in binary |
| Network message ID table | `network_messages.json` | Integer message-ID → protobuf message-type mapping, per network channel | NetMessages registry in binary |
| Engine constants | `engine_constants.json` | Auto-discoverable named integer/string constants reachable via the schema system or named-constant pools | Schema metadata + named-constant pools |
| String pools | `string_pools.json` | Static string pools tagged as reflection-reachable at module load (e.g. `CUtlSymbolLarge` interned strings), deduplicated per pool | Symbol pools in binary |
| Registry audit | `registry_audit.json` | Enumeration of every named registry symbol present in the binary, each marked `extracted` (with the artifact filename) or `omitted` (with rationale) | Tool's audit pass over binary symbols |
| Module manifest | `modules.json` | Every binary file read: path, SHA-256, file size, export count, schema-system registration count | Binary file headers + tool measurements |
| Provenance record | `provenance.json` | See **NFR-1** | Generated by tool |

A single tuple's artifact set lives at:

```text
artifacts/<build_id>/
  omissions.json                  # build-level — records any tuples not dumped (see NFR-12)
  <tuple>/
    entity_schema.json
    gameevents.json
    ...
    protos/
      cs_gameevents.proto
      ...
```

Per-tuple directories are siblings under a single `<build_id>` directory so a consumer can compare across tuples for the same build trivially. A build-level `omissions.json` sits alongside the tuple directories and lists any tuples that were not dumped, with rationale (see NFR-12); the file always exists (an empty `omissions: []` for builds where all four tuples succeeded). The proto3 schemas that define every JSON artifact's shape live at the repo root under `schemas/*.proto` — single source of truth, the same files compile to typed bindings for any consumer language via `protoc`.

> **Note on naming vs. status quo.** The current `CS2OpenDev-Docs` ships a hand-curated `well_known_constants.json` (e.g., team numbers, `m_gamePhase` meanings) that is NOT a binary extraction — it is a curated overlay. That artifact stays with `CS2OpenDev-Docs`. The new system's `engine_constants.json` is the auto-extracted equivalent: only what the binary itself exposes by name. The two are distinct and intentionally so.

---

## Input sources

The system reads **only** (extraction-time inputs):

- CS2 game binaries fetched directly from Steam (`server.dll`/`.so`, `client.dll`/`.so`, `tier0`, `schemasystem`, equivalent modules per tuple, and `pak01_dir.vpk` for `.gameevents`).
- Steam manifest metadata for build identification (`appid`, `depotid`, `manifestid`, `built_from_cl.txt`, `steam.inf`, Steam build ID).
- Its own source code and per-build configuration (e.g., schema-system version probes).

The system **shall NOT depend on** (build-time or runtime):

- `SteamDatabase/GameTracking-CS2` (data or tooling).
- `ValveResourceFormat/SchemaExplorer`.
- `ValveResourceFormat/DumpSource2` upstream as a *dependency*. A vendored fork of DumpSource2 inside `walker/` is explicitly permitted per FR-15 and is **not** a dependency on the upstream — once forked, the upstream may be deleted, archived, or diverge without affecting our build.
- Any other third-party CS2-data-extracting project.

The system **does depend on** (build-time, declared and pinned):

- `alliedmodders/hl2sdk` (cs2 branch) — the engine SDK headers, used by the C++ walker kernel for Source 2 C++ struct layouts. Pinned as a git submodule at `walker/third_party/hl2sdk`. HL2SDK is the engine SDK that the walker fundamentally requires (see "Extraction approach"); it is not a CS2-data-extracting project, and NFR-6 carves it out from the independence rule. Bumped deliberately per CS2 ABI shift.

---

## Extraction approach (the load-bearing technical decision)

**Pure static binary analysis is not viable for the schema system.** Source 2's schema metadata (`CSchemaSystem`, `CSchemaClassInfo`, field offsets, metadata payloads) is constructed by C++ static initializers running on the heap — it is not laid out flat in any binary section. To enumerate classes, the schema system's init code must actually execute.

Every successful Source 2 schema dumper does one of two things:

1. **In-process dynamic loading.** `dlopen` / `LoadLibrary` the Source 2 DLLs into the dumper's own process, call the C export `CreateInterface("SchemaSystem_001", ...)` to obtain a live `CSchemaSystem*`, run `InstallSchemaBindings` on each per-module library to force schema registration, then walk Valve's C++ object graph using the engine SDK's type definitions. Used by `ValveResourceFormat/DumpSource2` (C++), `neverlosecc/source2gen` (C++), `praydog/Source2Gen` (C++).
2. **External RPM against a running game.** Attach to a live `cs2.exe`, `OpenProcess` + `ReadProcessMemory`, pattern-scan to find the schema singleton, walk the same object graph from another process. Used by `a2x/cs2-dumper` (Rust), `sneakyevil/CS2-SchemaDumper` (C++), `GAMMACASE/Source2SchemaDumper` (C++ Metamod plugin).

For an offline tool with no running game, only approach (1) is available.

The walker — regardless of language — needs the C++ struct layouts of `CSchemaSystem`, `CSchemaClassInfo`, `CSchemaSystemTypeScope`, `CSchemaEnumInfo`, `SchemaClassFieldData_t`, `SchemaMetadataEntryData_t`, `ICvar`, `ConVarRefAbstract`. DumpSource2 imports these directly from `alliedmodders/hl2sdk`; non-C++ ports (e.g., `a2x/cs2-dumper`) must re-declare every layout in the target language and keep it in sync with HL2SDK by hand. Layout drift between the replica and the shipped DLL produces silent corruption — the worst failure mode for a dumper whose purpose is verifiable output.

## Technology choices (decisions, not deferred)

### Implementation: **hybrid — C++ schema-walker kernel + C# host**

The two-language split puts each language where its prior art is strongest and avoids both the "everything in C++" maintenance cost and the "replicate Valve C++ structs in C# unsafe code" silent-corruption risk.

**C++ schema-walker kernel** (a small subproject under `walker/`)

- Scope: only the work that strictly requires HL2SDK and live C++ type access. Loads the Source 2 DLLs into its own process, invokes `CreateInterface` / `InstallSchemaBindings`, walks `CSchemaSystem`, `ICvar`, and the NetMessages registry. Emits a single intermediate file (JSON or protobuf binary) per invocation.
- Built on `alliedmodders/hl2sdk` (cs2 branch), pinned as a git submodule. Modeled directly on DumpSource2's technique (which we may fork outright rather than reimplement — see FR-15).
- Built per-(OS, arch) and shipped as a native binary the C# host invokes via subprocess. No P/Invoke; no ABI risk between the kernel and the host.
- Target size: low-thousands of lines, dominated by Valve struct member access. The hard reverse-engineering work is already done in DumpSource2 / `praydog`'s 2015 schema-system writeup.

**C# host** (the rest of the project, under `host/`)

- Scope: Steam depot acquisition (`SteamKit2` or `DepotDownloader`), VPK 1/2 container parsing (the existing C# `ValveResourceFormat` library is proven prior art for this — same for KV1 / KV3), `.proto` descriptor extraction + round-trip (`Google.Protobuf`), JSON serialization (`System.Text.Json` with deterministic options), schema validation (round-trip through generated proto3 message classes), registry-audit aggregation, git commit/tag orchestration, CI driver.
- `.NET 8`+ via the `dotnet` CLI — works identically on Linux/Windows/macOS for the host-side work; the walker subprocess is the only architecture-constrained piece.
- Produces single-file self-contained executables via `dotnet publish`; the host travels with its target-tuple's compiled walker binary.

**Inter-process contract:** host invokes walker as a subprocess with command-line arguments naming the tuple and the binary directory; walker writes one intermediate file (format defined under `schemas/walker_output.proto`) to a path the host specifies; walker exits with a status code. Host reads the file, merges with its own-extracted artifacts (protos, gameevents, etc.), and emits the per-artifact files defined in the catalog. The walker's output schema is part of the public versioning contract.

**Why hybrid over the alternatives**

| Approach | Schema-walker work | Steam / VPK / KV3 / JSON / CI work | Silent-corruption risk | Rejected because |
|---|---|---|---|---|
| Pure C++ | Trivial (HL2SDK + DumpSource2 pattern) | Painful — no equivalent of `SteamKit2` / `ValveResourceFormat` in C++; protobuf descriptor round-trip via `libprotobuf` is workable but more friction than `Google.Protobuf`. | Lowest | High ongoing maintenance cost for the non-walker majority of the codebase. |
| Pure C# | Hard — must replicate Valve C++ struct layouts (private members, vtables, padding, alignment) as `unsafe` C# with manual `[FieldOffset]`. No existing C# project has walked the CS2 schema system this way (`CounterStrikeSharp` *consumes* GAMMACASE's pre-dumped JSON, it does not dump). Layout drift = silent corruption. | Easy | Highest | Silent-corruption risk on the load-bearing artifact (`entity_schema.json`) is unacceptable given the "highest possible artifact quality" goal. |
| Pure Rust | Hard for the same reason as C#. `a2x/cs2-dumper` proves the technique works in Rust — but only for the external-RPM variant, against a running game. No proven Rust in-process loader for Source 2. | Mixed — `goblin` and `libloading` exist; no VPK/KV1/KV3 library comparable to ValveResourceFormat; Steam crates less mature. | Same as C# | Same as C#, plus weaker ecosystem for the non-walker work, plus diverges from team language preference. |
| **Hybrid (selected)** | Trivial in the kernel; the kernel is small enough to vendor and maintain. | Easy in the C# host (proven C# libraries for every part). | Lowest — kernel uses HL2SDK like DumpSource2. | — |

**Cost the hybrid accepts**

- Two language toolchains in CI: `dotnet` SDK + C++ toolchain (g++ on Linux, MSVC on Windows). Both are first-class on GitHub Actions hosted runners; the build matrix becomes (host-OS × {linux-server, linux-client, windows-server, windows-client}) ≈ two CI runners.
- HL2SDK as a pinned git submodule. AlliedModders updates it on every Source 2 ABI shift; we pin per CS2 revision and bump deliberately. Cost is small relative to the alternative of vendoring our own struct definitions.

### Canonical output format: **Proto3 schemas, JSON as primary distribution, protobuf binary as secondary**

Rationale:

- One source of truth for every artifact's shape: a `.proto3` definition committed under `schemas/`.
- JSON output uses the proto3 JSON mapping (deterministic via canonical-form options) — preserves the current consumer experience (no codegen needed for casual readers).
- Binary protobuf output available for the same data via the same `.proto` definitions — small, fast random access, for high-volume consumers.
- Consumers in every major language get typed bindings for free by running `protoc` against the shipped schemas.
- Test infrastructure: every produced artifact is validated by deserializing it against the schema's generated message class (TR-1).

Alternatives rejected:

- **Plain JSON + JSON Schema 2020-12**: tried and abandoned in `CS2OpenDev-Docs` per its `CLAUDE.md` — standard codegens couldn't handle recursive type definitions. Documented-but-typeless JSON works for humans but offers no validation story.
- **Cap'n Proto / FlatBuffers**: marginal performance wins, materially smaller ecosystem, harder consumer story. Rejected.

### Output schema versioning: **Semantic versioning**, single shared version across the artifact family

- `MAJOR` bumps on backwards-incompatible removal/rename of any field in any output.
- `MINOR` bumps on additive changes (new field, new artifact type).
- `PATCH` bumps on docstring/comment-only changes within `.proto` schemas.
- Every artifact carries the schema version it conforms to.

### Repository

The system lives at **`CS2OpenDev/CS2-Schema-Tracker`** — public, MIT-licensed. Repository layout, commit, and tag scheme are specified in the "Repository structure" section below.

---

## Functional requirements

Every requirement has a **Done when** clause defining objective completion.

### FR-1: Entity schema extraction

The system extracts every class, struct, and enum registered with the CS2 schema system, with fields (name, offset, size, type), parent chains, and reflection metadata. Extraction is performed by the C++ walker kernel via in-process dynamic loading of the target tuple's Source 2 DLLs (per "Extraction approach" above), then handed to the C# host for serialization into `entity_schema.json`.

**Done when (recent builds, ≥ 2026-03-16):** `entity_schema.json` contains 100% of the class/enum names present in `ValveResourceFormat/SchemaExplorer`'s same-build `cs2.json.gz` (cross-check used only during development verification; no runtime dep), OR any name omission is listed in `registry_audit.json` with a written rationale.

**Done when (older builds, < 2026-03-16):** no parallel SchemaExplorer snapshot exists; completeness is established by (a) the cross-tuple consistency check (TR-3) — Linux and Windows tuples for the same build must agree on the union of class names, enum names, and enum member names (offsets and sizes legitimately differ), (b) the registry audit (FR-8) — every named schema symbol present in the loaded binaries appears as `extracted` or `omitted`-with-rationale, and (c) determinism + schema validation (NFR-2 + TR-1).

**In both cases:** every emitted field record carries non-default values for `name`, `offset`, `type`, and `module`.

### FR-2: Protobuf descriptor extraction

The system extracts embedded `FileDescriptorProto`s from CS2 binaries and emits both `.proto` text files (round-tripped) and a combined `protos.descriptorset` binary.

**Done when:** every emitted `.proto` file compiles cleanly via `protoc` with no warnings, AND every message defined in the emitted set deserializes the corresponding-typed packets in the test fixture corpus (TR-4) without error.

### FR-3: Game-event extraction

The system extracts `.gameevents` KV1 content from `pak01_dir.vpk` (which itself requires the system to parse the VPK1/VPK2 container format) and emits a structured `gameevents.json`.

**Done when:** every event present in the source `.gameevents` files appears in the output with its name, source filename, properties (`local`, `reliable`), and field list (name, type, comment) preserved verbatim. VPK extraction tested per TR-7.

### FR-4: ConVars + commands extraction

The system extracts every entry in the CS2 ConCommandBase registry.

**Done when:** `convars.json` and `commands.json` together contain 100% of the entries present in `GameTracking-CS2`'s same-build `DumpSource2/convars.txt` and `commands.txt` (cross-check used only during development verification), OR any omission is listed in `registry_audit.json` with a written rationale.

### FR-5: Network message ID table extraction

The system extracts the integer-ID → protobuf-message-type mapping for every registered network channel.

**Done when:** `network_messages.json` lists every numeric ID registered in the binary's NetMessages registry, mapped to its corresponding `.proto` message type name from the FR-2 output for the same tuple.

### FR-6: Engine constants extraction

The system extracts named integer/string constants exposed via the schema system or named-constant pools.

**Done when:** `engine_constants.json` carries every constant whose name and value are recoverable through the audited registry surface (FR-10); each constant ties back to the symbol pool / registry it was extracted from. The system never emits a constant whose name is inferred — only constants the binary itself names.

### FR-7: String pool extraction

The system extracts static string pools tagged as reflection-reachable at module load.

**Done when:** `string_pools.json` contains every interned string the schema system registers, deduplicated by pool, with the pool name (e.g., `CUtlSymbolLarge`) preserved.

### FR-8: Registry audit

The system enumerates every named registry symbol present in the loaded binaries and labels each as either `extracted` (paired with the output artifact filename that received it) or `omitted` (paired with a rationale string).

**Done when:** `registry_audit.json` exists per tuple per build; an audit-script in the tool repo regenerates it deterministically from the same inputs; every entry in every other artifact is reachable from an `extracted` row, and every `omitted` row carries a non-empty rationale.

### FR-9: Module manifest

The system emits `modules.json` listing every binary file read for this tuple, with SHA-256, file size, export count, and the count of schema-system registrations attributed to it.

**Done when:** every binary the tool opened during extraction appears in the manifest with a SHA-256 that can be independently reproduced by `sha256sum` over the same file.

### FR-10: Auto-discovery completeness audit

The system surfaces every clean per-(build, tuple) consistent output the schema/reflection systems expose — beyond the explicit FR-1 through FR-7 list — by way of the FR-8 registry audit.

**Done when:** `registry_audit.json` enumerates every named registry symbol present in the binary; the tool's CI fails if any symbol is present but neither `extracted` nor `omitted`-with-rationale, preventing silent drops.

### FR-11: Steam acquisition

The system downloads the CS2 binaries it needs directly from Steam without manual intervention, given a target Steam build ID (or `latest` for the current public-branch build).

**Done when:** `tool acquire --build <N> --tuple linux-x86_64.server` (or equivalent invocation) fetches every binary required for the tuple, verifies the bytes against the Steam manifest's content hashes, supports resume after interruption, handles depot-key rotation, and exits non-zero on any verification failure. Anonymous depot access is used (CS2 is free-to-play); no Steam account credentials are required.

### FR-12: VPK container parsing

The system parses VPK1 and VPK2 archive formats to extract loose files (specifically `.gameevents`) needed for FR-3.

**Done when:** the tool can list and extract files from `pak01_dir.vpk` shipped with any v1-scoped build, without depending on any third-party VPK tool at runtime.

### FR-13: KV3 default-value extraction

The system extracts KV3-encoded class default values (the `MGetKV3ClassDefaults` metadata payload) and emits them in a structured form embedded under the corresponding class in `entity_schema.json`.

**Done when:** every class for which the binary carries KV3 default data has both the raw KV3 string and a structurally-parsed representation in `entity_schema.json`; classes whose KV3 string fails parsing carry the raw string only, with a parse-failure note (matches the parity behavior of `CS2OpenDev-Docs`'s existing `value_parsed` sidecar).

### FR-14: Downstream-consumer contract stability

The system's public contract — everything a downstream consumer pins against — is collected in a single `CONTRACT.md` at the repo root and bound by the semver discipline of the output schema family. Any change to anything listed in `CONTRACT.md` is gated by the same MAJOR/MINOR/PATCH rules that apply to `.proto` schemas.

**Done when:** `CONTRACT.md` exists at the repo root and documents at minimum:

- **Artifact filenames** — every file in the catalog above, with its directory-relative path.
- **Per-tuple directory layout** — the `artifacts/<build_id>/{omissions.json, <tuple>/...}` shape.
- **Tuple names** — the exact set `linux-x86_64.server`, `windows-x86_64.server`, `linux-x86_64.client`, `windows-x86_64.client`.
- **Tag scheme** — `build/<id>`, `rev/<N>`, `build/<id>+r<n>` per "Commit + tag scheme".
- **Schema-version negotiation rules** — how a consumer reads the schema version from any artifact and decides whether their bindings are compatible.
- **CLI surface** — the full host subcommand set (e.g., `extract`, `acquire`, `fetch-cached-binaries`) with stable argument names; covers the commands cited in FR-4 / FR-11 / FR-16 / NFR-4.
- **Cache retention policy** — per FR-16, cache entries are immutable; deletion is a public-contract break.
- **Schema-version range** — the `schemas/*.proto` family version this commit's artifacts conform to.

### FR-15: Walker kernel + host architecture

The schema-walker work is implemented as a small C++ kernel that uses `alliedmodders/hl2sdk` (cs2 branch, pinned as a git submodule) for Source 2 struct layouts. The host (C#) invokes the kernel as a subprocess per tuple, passes a directory of loaded binaries plus an output path, reads the kernel's intermediate output file, and merges it into the per-tuple artifact set. The kernel and host are versioned together; the intermediate format is defined under `schemas/walker_output.proto` and follows the same semver discipline as the public output schemas.

The kernel's technique (in-process `dlopen` + `CreateInterface` + `InstallSchemaBindings` + walk Valve C++ types via HL2SDK) MAY be implemented by forking `ValveResourceFormat/DumpSource2` outright, with the fork pinned to a specific commit and any local modifications recorded in `walker/PATCHES.md`. Forking is permitted because DumpSource2 is the proven reference; reimplementing its loader logic would be net cost with no quality gain.

**Done when:** `walker/` contains a CMake-built C++ project that produces a native binary per (OS, arch) host; `host/` contains a `dotnet` project that invokes the walker binary as a subprocess and consumes its output; `schemas/walker_output.proto` defines the intermediate format; `walker/PATCHES.md` documents any DumpSource2-fork deltas (or notes "vendored re-implementation, no upstream parent"); CI builds both languages cleanly on every PR.

### FR-16: Binary cache for reproducibility

The system maintains a content-addressed binary cache that stores every input binary referenced by any committed artifact set, keyed by SHA-256. The cache is the mechanism that gives NFR-3 (reproducibility) and TR-5 (reproducibility smoke) operational teeth — without it, "any third party can reproduce a historical artifact set" is aspirational, because Steam manifests for old builds may become unreachable or change content over time.

**Done when:**

- A binary cache exists at a stable, documented URL (e.g., a public S3 bucket, GitHub Release attachments, a public-read object store, or equivalent). The specific backend is an implementation detail.
- Every commit to `artifacts/` includes a CI step that uploads any not-yet-cached input binary (referenced by SHA-256 in its `provenance.json`) to the cache before the commit is pushed. CI fails the workflow if any `provenance.json`-referenced binary cannot be fetched from the cache after upload.
- A documented host command (e.g., `dotnet run --project host -- fetch-cached-binaries --build <N> --tuple <T> --out <dir>`) downloads every cached binary for that build/tuple by SHA-256 to a local directory, with no Steam access required.
- Retention policy is documented in `CONTRACT.md`: cache entries are immutable; deletion of any cached SHA-256 is out of scope for v1 and would constitute a public-contract break.

---

## Non-functional requirements

### NFR-1: Provenance

Every artifact set ships a `provenance.json` recording:

- Tool version (semver + git commit SHA of the dumper).
- For every input binary read: file path, SHA-256, file size, file mtime from the Steam manifest.
- Steam identity: `appid`, `depotid`, `manifestid` per depot read, Steam build ID, manifest creation time (UTC).
- CS2 build identity: schema `revision` (from schema system), `build_id` (from Steam), `built_from_cl` (from `built_from_cl.txt`).
- Target tuple: `(os, arch, target)`.
- Schema version emitted: the proto3 schema family version every output conforms to.

**Done when:** every artifact set contains a `provenance.json` validating against `schemas/provenance.proto` and carrying all fields above.

### NFR-2: Determinism

Re-running the tool against the same input binaries with the same tool version produces byte-identical output across all artifact files.

**Done when:** TR-2 (determinism test) passes in CI on every PR.

### NFR-3: Reproducibility

Any third party with the input binaries (verified by SHA-256 from `provenance.json`) and the tool source (at the recorded commit SHA) can regenerate any committed artifact set byte-identically. This is verified by TR-5.

### NFR-4: Local-runnable, with documented host-OS constraint

The tool's host (the C# layer) runs end-to-end on Linux x86_64, Windows x86_64, and macOS arm64/x86_64 developer workstations with no infrastructure beyond a C++ toolchain (CMake + g++/clang on Linux/macOS, MSVC Build Tools on Windows) and the `dotnet` SDK installed. The walker kernel, because it dynamically loads target-tuple binaries into its own process, must run on a host whose OS+arch matches the target tuple's: a Linux x86_64 host can extract `linux-x86_64.{server,client}`; a Windows x86_64 host can extract `windows-x86_64.{server,client}`. A macOS developer can build the host, edit the kernel, and run host-only tests, but cannot natively dump Linux or Windows tuples — they must use a Linux/Windows VM or remote build.

**Done when:** on Linux x86_64, `dotnet run -- extract --build <N> --tuple linux-x86_64.server` (and `.client`) on a clean clone produces a complete artifact set; on Windows x86_64, the same for the `windows-x86_64.*` tuples; on macOS, host-only tests pass and a documented "use a Linux/Windows runner for extraction" message is emitted if the user attempts a cross-OS extraction.

### NFR-5: Format-documented

Every output artifact's structure is fully documented by its proto3 schema under `schemas/`. No undocumented fields.

**Done when:** every `.json` artifact's top-level structure validates against a corresponding `schemas/*.proto` definition, and the schemas are themselves committed to the tool repo as the single source of truth.

### NFR-6: No third-party CS2-data-extracting project runtime dependencies

The tool builds and runs without any of `SteamDatabase/GameTracking-CS2`, `ValveResourceFormat/SchemaExplorer`, or any other third-party project whose purpose is to *re-publish* extracted CS2 data. The tool MAY depend on `alliedmodders/hl2sdk` (cs2 branch) as a pinned git submodule for C++ struct layouts in the walker kernel — HL2SDK is the engine SDK, not a data-extracting project, and the walker fundamentally requires its type definitions (see "Extraction approach"). The tool MAY depend on or fork `ValveResourceFormat/DumpSource2` (see FR-15); forking transfers ownership and removes the runtime/build dependency on the upstream repo.

**Done when:** the tool repo's `host/*.csproj` and `walker/CMakeLists.txt` declare zero dependencies (NuGet, git submodule, system-installed, or otherwise) on GameTracking-CS2, SchemaExplorer, or upstream DumpSource2 (a vendored fork inside `walker/` is permitted and is *not* a dependency on the upstream); CI runs on a base runner image with none of those upstreams present. HL2SDK appears as a pinned `walker/third_party/hl2sdk` git submodule and is the only third-party CS2-domain build input.

### NFR-7: Schema-system version handling

When Valve changes the CS2 schema-system memory layout, the tool detects the change before extraction begins. If the layout is known, the tool dispatches to the matching extractor. If unknown, the tool exits non-zero with an error naming the unknown layout signature. Silent fallback to a guessed extractor is forbidden.

**Done when:** the tool carries a schema-system-version probe; TR-6 (probe test) passes for every layout the tool claims to support; the probe's "unknown" path exits non-zero and emits the layout signature to stderr.

### NFR-8: Repository structure & tagging compliance

**Done when:** every commit under `artifacts/` carries a `build/<steam_build_id>` annotated tag; the first commit at each new schema revision additionally carries a `rev/<schema_revision>` tag; `git log --oneline artifacts/` shows a strictly chronological-by-Steam-publication-time history (no manual reorderings); any republished build (same build ID, different bytes — rare but observed historically) results in a *new* commit tagged `build/<id>+r<n>` where `<n>` is a monotonically incrementing republish index.

### NFR-9: CI cadence

**Done when:** automated CI checks for new Steam manifests at least once per 24h and produces a new artifact set within 6h of detection. The 6h figure is an initial target — after the first three successful automated runs (per Definition-of-done item 4), the operator records the measured median+p95 duration in the workflow file's comments and tightens or loosens the 6h target accordingly. Subsequent revisions follow the same record-and-update process.

### NFR-10: CI runner strategy

- **Primary:** GitHub Actions hosted runners.
- **Fallback:** self-hosted runner, only where measurement shows hosted runners cannot meet a tuple's disk/bandwidth needs (client tuples in particular may not fit).

**Done when:** CI workflows declare runner type per job; hosted runner is the default for any job that fits a current GitHub-hosted runner's free disk and standard bandwidth; self-hosted is used only where measurement has shown hosted to be infeasible, with the measurement and reason documented in the workflow file's comments.

### NFR-11: Fail-loud, never-partial

On any input failure (corrupt binary, missing module, depot acquisition failure, schema-system-probe unknown, VPK extraction error), the tool exits non-zero before writing any artifact bytes. Partial artifact sets are forbidden.

**Done when:** TR-8 covers every documented failure mode and asserts: zero artifact files on disk after a failed run, non-zero exit code, error message identifies the failed stage.

### NFR-12: All-or-nothing per-(build, tuple) commit

A single commit to `artifacts/` contains either the complete artifact set for one (build, tuple), or one complete artifact set across all four tuples for one build. Partial commits across tuples (e.g., three tuples succeeded, one failed) are forbidden; CI either succeeds across all four and commits, or commits none and surfaces the failure for operator action.

**Done when:** CI workflow logic enforces this; a documented exception process exists for tuples that are permanently unreachable for a historical build (e.g., a tuple whose Steam depot was unavailable at extraction time, or a historical build for which the walker's schema-system probe rejects the binary's layout per NFR-7). Per-tuple omissions are recorded in a build-level `artifacts/<build_id>/omissions.json` that validates against `schemas/omissions.proto`; the file is always present (with `omissions: []` for clean builds), enumerates each omitted tuple with a `reason` string drawn from a fixed enum (`depot_unavailable`, `walker_layout_unknown`, `binary_corrupt`, `other`), and includes a free-text `notes` field for context.

### NFR-13: Storage observability + soft threshold

The `artifacts/` history is tracked in-repo without Git LFS for v1. CI reports the total `artifacts/` size and per-commit growth on every push, so the team has the data needed to decide when storage strategy should change (LFS adoption, artifact-repo split, release-attached binaries). A *soft* threshold (single shallow clone > 5 GB OR annual growth > 10 GB) emits a clearly-labeled `STORAGE THRESHOLD BREACHED` log line and opens a GitHub issue (via `actions/github-script` or equivalent) in the same repo, but does not block CI; if the team accepts the breach, the acceptance is recorded in `docs/storage-decisions.md` with a date and rationale, and the issue is closed referencing that record.

**Done when:** CI emits the size + per-commit growth report on every push; the soft-threshold check is wired up; crossing the threshold opens an issue (labeled `storage-threshold`) and emits the labeled log line; `docs/storage-decisions.md` exists (even if empty at v1) ready to accept acceptance entries.

---

## Repository structure

Single repo (`CS2OpenDev/CS2-Schema-Tracker`) holds tool source (both languages), artifacts, history, schemas, and CI. Layout:

```text
walker/                     # C++ schema-walker kernel (FR-15)
  CMakeLists.txt
  src/
  third_party/
    hl2sdk/                 # pinned git submodule (alliedmodders/hl2sdk, cs2 branch)
  PATCHES.md                # any deltas from a forked DumpSource2 base
host/                       # C# host (.NET 8+)
  Cs2SchemaTracker.sln
  src/
  tests/
schemas/                    # proto3 schemas (single source of truth)
  entity_schema.proto
  gameevents.proto
  convars.proto
  commands.proto
  network_messages.proto
  engine_constants.proto
  string_pools.proto
  registry_audit.proto
  modules.proto
  omissions.proto           # build-level per-tuple omission records (NFR-12)
  provenance.proto
  walker_output.proto       # intermediate format the kernel writes for the host
artifacts/
  <build_id>/
    linux-x86_64.server/
      entity_schema.json
      gameevents.json
      ... (full artifact set)
    linux-x86_64.client/
    windows-x86_64.server/
    windows-x86_64.client/
docs/                       # operator + consumer documentation
CONTRACT.md                 # public consumer contract (FR-14)
LICENSE                     # MIT
README.md
.github/workflows/          # CI/CD
```

### Commit + tag scheme

The user's directive: use the highest-resolution identifier that changes every push; supplement with a timestamp only if no such identifier exists. Steam build ID changes per push and is therefore primary.

- **One commit per (build, all-four-tuples) artifact update.** Per NFR-12, the four tuples ship together.
- **Primary tag:** `build/<steam_build_id>` — annotated, mandatory, unique per commit.
- **Secondary tag:** `rev/<schema_revision>` — annotated, only on the first commit at a given schema revision (subsequent same-rev commits don't re-tag — consumers asking "what was at rev N?" get the earliest-known commit at that rev).
- **Republish tag suffix:** `build/<id>+r<n>` where `<n>` is a monotonically incrementing republish index, used only when Valve republishes a build ID with different bytes (rare but observed historically).
- **Tag messages** carry the provenance summary (build ID, schema rev, manifest IDs per depot, manifest creation time).
- `main` is the only long-lived branch.
- Commit subject normative prefixes: `tool: <message>` for tool-source commits, `dump: build <id>` for artifact commits. CI enforces.

---

## Workflow requirements

### WR-1: Tool-first development

The tool repo's commit history shows tool-source completion (all FRs and NFRs satisfied, validated by tests) **before** any `artifacts/` commits land. No backfill begins until tooling is ready.

**Done when:** the first `artifacts/` commit's parent contains complete `walker/` and `host/` trees that together pass every test in TR-1 through TR-8, AND that parent commit's subject begins with `tool:`. CI enforces.

### WR-2: Historical backfill

Once the tool is verified, an operator walks every CS2 Steam build from the earliest reachable (CS2 Limited Test, build 1555, ~2023-03-22) on the public branch to the current head, downloading each manifest, running the tool, and committing one (build, all-four-tuples) artifact set per build.

Backfill proceeds in **segments bounded by known schema-system layout coverage**: per NFR-7 the walker fails loud on any unknown layout. When the operator encounters a build whose layout is unknown, backfill halts; a walker-side patch adds support for that layout (with a fixture added under TR-6), the walker is re-released, and backfill resumes. Builds for which a tuple cannot be dumped — because the layout is too divergent to support, the depot is unavailable, or the binary itself is missing — are recorded per NFR-12 (per-tuple omission with rationale) rather than skipping the entire build.

**Done when:** `artifacts/` contains a directory for every CS2 Steam build reachable from public-branch manifest history; every build directory contains an `omissions.json` (empty list for clean builds, populated for builds with any omitted tuple) plus one subdirectory per dumped tuple; a tracking file under `docs/backfill-status.md` records any historical builds where every tuple was unreachable, with the date the operator confirmed the absence.

### WR-3: Ongoing automated extraction

CI detects new public-branch Steam manifests, downloads, extracts, validates, commits + tags, and pushes without operator action.

**Done when:** a scheduled CI workflow (hosted GitHub Actions runners by default per NFR-10; self-hosted fallback only where required) detects a new manifest, runs the full extraction for every tuple, validates output, commits + tags, and pushes — all within a single workflow run, on a `cron` schedule honoring NFR-9.

---

## Test requirements

### TR-1: Schema validation

Every emitted JSON artifact validates by round-tripping through the proto3 message generated from its `schemas/*.proto` definition.

**Done when:** a test suite loads every produced artifact, parses it into its proto message, re-serializes with canonical-form options, and asserts the re-serialization equals the input. Runs in CI on every PR.

### TR-2: Determinism

Two consecutive extractions against the same fixture binaries produce byte-identical output.

**Done when:** CI runs the determinism test on a pinned fixture build and asserts `diff -r` produces no output.

### TR-3: Cross-tuple consistency

For data that should agree across tuples (class names, enum members, proto message names) **within modules that were loaded by more than one tuple**, the per-tuple outputs do agree. Server-only modules (loaded only in server tuples) and client-only modules (loaded only in client tuples) are legitimately tuple-exclusive and excluded from the comparison.

**Shared modules** for a given build are defined as the intersection of the per-tuple `modules.json` files: a module appears in the shared set if and only if every dumped tuple's `modules.json` lists it.

**Done when:** a test loads every dumped tuple's artifact set for the build under test (consulting `omissions.json` so absent tuples don't trigger a missing-file failure — the test runs against whatever tuples are present and skips with a pass if fewer than two are present), computes the shared-module set, and asserts that for classes/enums/proto messages *within shared modules*: (a) the union of class names is identical across tuples, (b) the union of enum names and enum-member names is identical, (c) the union of proto message names is identical. Offsets and sizes legitimately differ across tuples; names do not. The test logs both the shared-module set and any tuple-exclusive modules so consumers can audit the boundary.

### TR-4: Protobuf round-trip

Every emitted `.proto` file compiles via `protoc`, and the descriptor set deserializes a captured-real-network-packet corpus committed under `host/tests/fixtures/network/`.

**Done when:** the fixture corpus deserializes without error using the latest emitted descriptor set; CI fails if any packet type fails to deserialize.

### TR-5: Reproducibility smoke

A scripted reproduction of one randomly-selected historical artifact set, starting from `provenance.json` alone, produces byte-identical output.

**Done when:** a CI job picks a random committed historical artifact set, fetches the input binaries by SHA-256 from the binary cache (FR-16), runs the tool at the recorded tool commit, and asserts byte-identical output to the committed set. CI fails the job if any referenced binary is missing from the cache (a missing binary is treated as an FR-16 violation, not a TR-5 skip). Satisfies NFR-3.

### TR-6: Schema-system version probe

The tool's schema-system-version probe correctly identifies every layout the team claims to support.

**Done when:** a test suite carries one fixture per supported schema-system layout, runs the probe against each, and asserts the correct layout identifier is returned; an "unknown" fixture is included and the probe correctly reports it as unknown without crashing.

### TR-7: VPK extraction round-trip

The tool's VPK parser extracts `.gameevents` from `pak01_dir.vpk` for every v1-scoped tuple.

**Done when:** a test suite loads a fixture `pak01_dir.vpk` for each v1-scoped tuple, asserts the expected `.gameevents` files are extractable, and asserts the byte content matches a pinned expected SHA-256.

### TR-8: Fail-loud coverage

Every documented failure mode (corrupt binary, missing module, depot acquisition failure, schema-system probe unknown, VPK extraction error, KV3 parse failure) is exercised by a test that asserts: zero artifact files on disk, non-zero exit code, error message names the failed stage.

**Done when:** the test suite covers every failure mode listed under NFR-11; CI fails if a new failure mode is added without a corresponding test.

---

## Definition of "done" (v1 operational)

The system is operational when **all** of the following hold:

1. Every FR (1–16) and NFR (1–13) has its **Done when** clause satisfied.
2. Every TR (1–8) is implemented and passing in CI.
3. The historical backfill (WR-2) has populated `artifacts/` for every reachable Steam build from 2023-03-22 forward on the public branch.
4. The ongoing CI workflow (WR-3) has produced at least three consecutive automated artifact updates without operator intervention.
5. `CS2OpenDev-Docs` has been switched to consume from `CS2OpenDev/CS2-Schema-Tracker`. Concretely: the `upstream/data` and `upstream/schema-explorer` submodules are removed, replaced by either a `CS2-Schema-Tracker` submodule or a CI-time fetch of pinned artifacts; `docs/generate_docs.py` is updated to read the new artifact layout (`artifacts/<build_id>/<tuple>/*`) instead of the legacy upstream paths. The migration is complete when `python3 docs/generate_docs.py` produces a `docs/generated/` tree whose diff against the pre-migration version is limited to additive enrichment (no fields lost, no entity counts dropped, no regressions in the Jekyll site).

---

## Deferred to implementation (only within-requirement details)

Per the user's directive, only implementation details *within* a requirement are deferred. The following are not blocking for this requirements doc but will be decided during tool construction:

- Whether the C++ walker kernel forks DumpSource2 outright or vendors an equivalent re-implementation — decision recorded in `walker/PATCHES.md`; either is permitted under FR-15.
- The host-side PE/ELF parsing library (`PeNet`, `ELFSharp`, or alternatives), used for module-manifest SHA-256 computation, section inspection, and export enumeration — within FR-9 scope; the walker kernel does not need these because it operates on loaded modules.
- Specific binary-cache backend (S3, GitHub Release attachments, public-read object store, IPFS, ...) — implementation detail of FR-16. Constraint is "stable URL, immutable contents, fetchable by SHA-256."
- The C# library for VPK / KV1 / KV3 parsing (`ValveKeyValue`, a slice of `ValveResourceFormat`, or our own) — within FR-3 / FR-12 / FR-13 scope.
- Specific Steam-depot download library (`SteamKit2` library vs `DepotDownloader` subprocess) — implementation detail of FR-11.
- Specific `.proto` text-form emission technique (use protobuf reflection vs walk the descriptor manually) — implementation detail of FR-2.
- The exact set of schema-system layouts the walker probe distinguishes — discovered empirically during WR-2 backfill; the requirement (NFR-7, TR-6) stands regardless. Each new layout encountered is a new walker-side patch landed before that backfill segment proceeds.
- The exact technique used to identify "named registry symbols" for FR-8/FR-10 — likely a combination of HL2SDK type enumeration and walk-time discovery within the kernel; specific approach is a kernel-implementation detail.

---

## Verification end-to-end (how to test the resulting system)

For a reviewer or operator validating "is v1 done":

1. **Build the walker** on a clean Linux x86_64 box: `cmake -S walker -B walker/build && cmake --build walker/build` succeeds; HL2SDK submodule fetched.
2. **Build the host:** `dotnet build host/` succeeds.
3. **Run all tests:** `dotnet test host/` — every test in TR-1 through TR-8 passes; the walker's own tests (in `walker/tests/`) pass via CTest.
4. **Run a fresh extraction:** `dotnet run --project host -- extract --build <latest> --tuple linux-x86_64.server` invokes the walker as a subprocess, consumes its output, and produces a complete artifact set in `artifacts/<latest>/linux-x86_64.server/`.
5. **Validate the produced artifacts** against their schemas: every JSON parses into the corresponding proto message.
6. **Inspect `provenance.json`** for the artifact set: all NFR-1 fields populated; every binary SHA-256 reproducible via `sha256sum`.
7. **Inspect `registry_audit.json`:** zero entries with neither `extracted` nor `omitted` status.
8. **Verify the git history:** `git tag -l 'build/*' | wc -l` matches the number of `artifacts/` build directories.
9. **Verify the binary cache (FR-16):** for the build extracted in step 4, run `dotnet run --project host -- fetch-cached-binaries --build <latest> --tuple linux-x86_64.server --out /tmp/cached` and confirm every binary listed in `provenance.json` arrives with its recorded SHA-256. Then attempt the same fetch for a randomly-selected historical build's tuple — should also succeed.
10. **Verify storage observability (NFR-13):** push a no-op commit; confirm CI emits the size + per-commit growth report; manually trigger a synthetic over-threshold scenario (e.g., temporarily lower the threshold) and confirm the `STORAGE THRESHOLD BREACHED` log line + GitHub issue appear; revert.
11. **Verify the consumer contract:** clone `CS2OpenDev-Docs`, apply the migration from Definition-of-done item 5, run `python3 docs/generate_docs.py`, confirm output diff against today's generated docs is limited to additive enrichment (no regressions).
12. **Cross-OS sanity:** on a Windows x86_64 runner, repeat steps 1–5 for `windows-x86_64.server`; confirm tuple-isolation per FR-9 (the Linux-host extraction did not need to read Windows binaries and vice versa).
