# Generator tests

Tests for `docs/generate_docs.py`.  No new runtime dependencies: `pyyaml` and
`protobuf` are the same two packages the generator already needs.

## Running them

From the repository root:

```bash
python3 -m unittest discover -s docs/tests -t docs/tests
```

or, if pytest is installed:

```bash
python3 -m pytest docs/tests
```

Both take a few seconds; the golden test runs the whole generator over the
fixture twice (once for the comparison, once to prove the run is
deterministic).

## What is here

| File | What it does |
|---|---|
| `test_units.py` | The pure helpers: variant resolution, layout flattening, cell escaping, mermaid quoting, the type-reference regex, overlay lookup and validation, proto flattening and anchors, bitfield bit indices, the table self-check. Builds its own five-record entity dict, so it does not read the fixture. |
| `test_golden.py` | Runs `main()` over the fixture into a temporary directory and compares every byte against `expected/`, then asserts named facts about the golden text so a failure says which rendering rule broke. |
| `fixture/` | A trimmed SchemaTracker artifact set plus the overlays that apply to it. Committed. |
| `expected/` | The generator's output for that fixture. Committed. |
| `make_fixture.py` | Rebuilds `fixture/` from a real artifact set. |
| `update_expected.py` | Rebuilds `expected/` from `fixture/`. |
| `_gen.py` | Loads `docs/generate_docs.py` by path as the module `gd`. |

Nothing under `docs/generated/` or `docs/index.md` is touched: the golden test
writes to a temporary directory and `update_expected.py` writes only to
`expected/`.

## When output changes on purpose

```bash
python3 docs/tests/update_expected.py
git diff docs/tests/expected
```

The diff is the review surface.  Read it before committing: every rendering
change to the real site shows up there first, at a size you can actually read.

## When the fixture needs to change

`make_fixture.py` cuts the fixture out of a real artifact set:

```bash
python3 docs/tests/make_fixture.py \
  --artifacts-root ./upstream/schema-tracker/artifacts \
  --build 25000182 --platform windows-x86_64 --repo-root .
python3 docs/tests/update_expected.py
```

The build id is rewritten to `9000001` and the Steam manifest date is pinned,
so a fixture rebuild against a newer artifact set does not churn every
provenance line.  Bumping the source build will still churn offsets and field
lists, which is the point: the fixture is a snapshot, not a live view.

## What the fixture deliberately covers

- Both variants of every class on the `CCSPlayerPawn` and `C_CSPlayerPawn`
  primary-parent spines down to `CEntityInstance`.  The client record
  registers first, so a server page that resolves its bases by bare name picks
  up client offsets: that is the bug the resolver tests pin.
- `CBoneConstraintPoseSpaceBone::Input_t`, a nested `A::B` name, for the
  filename mapping, the link regex and mermaid quoting.
- `CGameSceneNode`, a run of bitfields sharing one offset.
- `SolidType_t` with overlay member annotations, and `BloodType`, which has a
  negative member value under an unsigned underlying type.
- `demo.proto` (nested messages several levels deep), `gameevents.proto` (two
  different nested types named `key_t`, and a cross-file type reference) and
  `networkbasetypes.proto`.  `demo.proto` also imports a file that is not in
  the set, so the unresolvable-import path is exercised.
- Eight game events, two of which are both named `player_death` from different
  sources.
- Convars and commands whose descriptions carry newlines, pipes and
  `<placeholder>` tokens, plus `mp_roundtime` for the type and range columns.
- A `changelog.json` whose families are all empty, so the "no changes"
  sentence is covered.
- Two overlay keys that resolve to nothing, so `--strict` has something to
  fail on.
- The site data bundle under `generated/data/`, written by `docs/site_data.py`
  from the same fixture, so its JSON shapes are pinned by the goldens too.

Not covered: the Linux artifact set (upstream's `latest` branch carries only
one platform), and the large-transition branches of the schema-history page
(the fixture's `schema_evolution` artifact is synthetic and small).
