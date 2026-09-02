"""End-to-end golden-file test: run the generator on the committed fixture
and compare every byte of the output to docs/tests/expected/.

Regenerate the goldens with:

    python3 docs/tests/update_expected.py
"""

from __future__ import annotations

import io
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

from _gen import EXPECTED, FIXTURE, gd


def run_generator(
    out_dir: Path, extra: list[str] | None = None, fixture: Path = FIXTURE
) -> tuple[int, str]:
    """Render *fixture* into *out_dir*; returns ``(exit code, combined log)``."""
    argv = [
        "--repo-root", str(fixture),
        "--artifacts-root", str(fixture / "artifacts"),
        "--build", "9000001",
        "--platform", "windows-x86_64",
        "--output", str(out_dir),
    ] + (extra or [])
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = gd.main(argv)
    return code, out.getvalue() + err.getvalue()


class GoldenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.mkdtemp(prefix="cs2docs-golden-")
        cls.out = Path(cls._tmp)
        cls.code, cls.log = run_generator(cls.out)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls._tmp, ignore_errors=True)

    def test_generator_succeeds(self):
        self.assertEqual(self.code, 0, self.log)

    def test_expected_tree_exists(self):
        self.assertTrue(
            EXPECTED.is_dir(),
            "docs/tests/expected/ is missing; run docs/tests/update_expected.py",
        )

    def test_output_matches_the_goldens(self):
        produced = {
            p.relative_to(self.out).as_posix()
            for p in self.out.rglob("*") if p.is_file()
        }
        expected = {
            p.relative_to(EXPECTED).as_posix()
            for p in EXPECTED.rglob("*") if p.is_file()
        }
        self.assertEqual(
            sorted(produced - expected), [], "files produced but not in expected/"
        )
        self.assertEqual(
            sorted(expected - produced), [], "files in expected/ but not produced"
        )
        differing = [
            rel for rel in sorted(expected)
            if (EXPECTED / rel).read_bytes() != (self.out / rel).read_bytes()
        ]
        self.assertEqual(differing, [], "content differs from expected/")

    def test_run_is_deterministic(self):
        with tempfile.TemporaryDirectory() as d:
            second = Path(d)
            code, log = run_generator(second)
            self.assertEqual(code, 0, log)
            differing = [
                p.relative_to(second).as_posix()
                for p in second.rglob("*") if p.is_file()
                and p.read_bytes() != (self.out / p.relative_to(second)).read_bytes()
            ]
            self.assertEqual(differing, [])

    def test_self_checks_report_clean(self):
        self.assertIn("0 cross-module inherited row(s)", self.log)
        self.assertIn("0 broken table row(s)", self.log)

    def test_strict_fails_on_the_stale_overlay_key(self):
        with tempfile.TemporaryDirectory() as d:
            code, log = run_generator(Path(d), ["--strict"])
        self.assertNotEqual(code, 0)
        self.assertIn("CClassThatWasRemoved", log)

    def test_strict_fails_on_an_unknown_overlay_stem(self):
        with tempfile.TemporaryDirectory() as d:
            fixture = _fixture_copy(Path(d))
            (fixture / "docs" / "overlays" / "nonsense.yml").write_text(
                "CCSPlayerPawnTypo:\n  description: Annotates nothing.\n",
                encoding="utf-8",
            )
            code, log = run_generator(Path(d) / "out", ["--strict"], fixture)
        self.assertNotEqual(code, 0)
        self.assertIn("UNRESOLVED nonsense: no such module or overlay file", log)

    def test_strict_fails_on_a_module_mismatch(self):
        with tempfile.TemporaryDirectory() as d:
            fixture = _fixture_copy(Path(d))
            _drop_stale_overlay_keys(fixture)
            code, log = run_generator(Path(d) / "clean", ["--strict"], fixture)
            self.assertEqual(code, 0, log)
            with (fixture / "docs" / "overlays" / "entity2.yml").open("a", encoding="utf-8") as fh:
                fh.write("CCSPlayerPawn:\n  description: Filed under the wrong module.\n")
            code, log = run_generator(Path(d) / "out", ["--strict"], fixture)
        self.assertNotEqual(code, 0)
        self.assertIn("MODULE     entity2/CCSPlayerPawn: CCSPlayerPawn lives in server", log)
        self.assertNotIn("UNRESOLVED", log)


def _fixture_copy(root: Path) -> Path:
    dst = root / "fixture"
    shutil.copytree(FIXTURE, dst)
    return dst


def _drop_stale_overlay_keys(fixture: Path) -> None:
    """Remove the two deliberately stale keys so a copy passes ``--strict``."""
    import yaml

    overlays = fixture / "docs" / "overlays"
    server = yaml.safe_load((overlays / "server.yml").read_text(encoding="utf-8"))
    del server["CClassThatWasRemoved"]
    (overlays / "server.yml").write_text(yaml.safe_dump(server), encoding="utf-8")
    demo = yaml.safe_load((overlays / "protobufs" / "demo.yml").read_text(encoding="utf-8"))
    del demo["messages"]["CDemoClassInfo"]["fields"]["no_such_field"]
    (overlays / "protobufs" / "demo.yml").write_text(yaml.safe_dump(demo), encoding="utf-8")


class ContentTests(unittest.TestCase):
    """Assertions on the golden text, so a regression names itself."""

    def _read(self, rel: str) -> str:
        return (EXPECTED / rel).read_text(encoding="utf-8")

    def test_server_pawn_uses_the_server_base_offset(self):
        page = self._read("generated/schemas/server/CCSPlayerPawn.md")
        self.assertIn(
            "| `0x2d0` | `m_iHealth` | int32 | [CBaseEntity](../server/CBaseEntity.md)",
            page,
        )
        self.assertNotIn("../client/", page)

    def test_client_pawn_uses_the_client_base_offset(self):
        page = self._read("generated/schemas/client/C_CSPlayerPawn.md")
        self.assertIn("[C_BaseEntity](../client/C_BaseEntity.md)", page)
        self.assertNotIn("| [CBaseEntity](../server/", page)

    def test_twin_pages_carry_the_module_in_the_title(self):
        self.assertIn(
            "title: CBaseAnimGraph (server)",
            self._read("generated/schemas/server/CBaseAnimGraph.md"),
        )
        self.assertIn(
            "**Twin:** [CBaseAnimGraph (client)](../client/CBaseAnimGraph.md)",
            self._read("generated/schemas/server/CBaseAnimGraph.md"),
        )

    def test_schema_pages_carry_provenance(self):
        self.assertIn("> Source: **Build 9000001**",
                      self._read("generated/schemas/server/CBaseEntity.md"))
        self.assertIn("> Source: **Build 9000001**", self._read("generated/schemas.md"))
        self.assertIn("> Source: **Build 9000001**", self._read("generated/convars.md"))

    def test_no_kramdown_attribute_lists_remain(self):
        for rel in ("generated/items.md", "generated/network.md", "index.md",
                    "generated/schema-history.md"):
            self.assertNotIn("{: .", self._read(rel), rel)

    def test_inherited_row_shows_the_base_class_annotation(self):
        page = self._read("generated/schemas/server/CCSPlayerPawn.md")
        health = [ln for ln in page.splitlines() if "| `m_iHealth` |" in ln][0]
        self.assertIn("Current health points", health)

    def test_enum_member_annotations_render(self):
        page = self._read("generated/schemas/server/SolidType_t.md")
        self.assertIn("| `SOLID_NONE` | 0 | No collision. |", page)

    def test_negative_enum_value_under_unsigned_shows_the_wrap(self):
        self.assertIn("| `None` | -1 (`0xffffffff`) |",
                      self._read("generated/schemas/server/BloodType.md"))

    def test_bitfield_rows_carry_a_bit_index(self):
        page = self._read("generated/schemas/client/CGameSceneNode.md")
        self.assertIn("`0x0` bit 0 |", page)
        self.assertIn("`0x0` bit 1 |", page)

    def test_unspecified_alignment_is_not_printed_as_255(self):
        for path in (EXPECTED / "generated" / "schemas").rglob("*.md"):
            self.assertNotIn("**Align:** 255", path.read_text(encoding="utf-8"),
                             str(path))

    def test_convars_table_has_one_row_per_convar(self):
        page = self._read("generated/convars.md")
        rows = [ln for ln in page.splitlines() if ln.startswith("|")]
        # header + separator + one row per convar
        self.assertEqual(len(rows) - 2, self._convar_count())
        self.assertIn("| Name | Type | Default | Range | Flags | Description |", page)

    def _convar_count(self) -> int:
        import json
        data = json.loads(
            (FIXTURE / "artifacts" / "9000001" / "windows-x86_64" / "convars.json")
            .read_text(encoding="utf-8")
        )
        return len(data["convars"])

    def test_placeholders_are_escaped_not_emitted_as_html(self):
        page = self._read("generated/convars.md")
        self.assertIn("&lt;difficulty&gt;", page)
        self.assertNotIn("<difficulty>", page)

    def test_multiline_description_folds_to_br(self):
        line = [ln for ln in self._read("generated/convars.md").splitlines()
                if ln.startswith("| `bot_prefix`")][0]
        self.assertIn("<br>", line)

    def test_convar_range_column_is_populated(self):
        line = [ln for ln in self._read("generated/convars.md").splitlines()
                if ln.startswith("| `mp_roundtime`")][0]
        self.assertIn("`Float32`", line)
        self.assertIn("..", line)

    def test_convars_schema_carries_the_new_keys(self):
        import json
        data = json.loads(self._read("generated/downstream-codegen-schemas/convars_schema.json"))
        rt = [c for c in data["convars"] if c["name"] == "mp_roundtime"][0]
        self.assertEqual(rt["value_type"], "Float32")
        self.assertEqual(rt["min"], 0.1)
        self.assertEqual(rt["max"], 60)
        self.assertIsInstance(rt["max"], int)
        unbounded = [c for c in data["convars"] if c["name"] == "sv_cheats"][0]
        self.assertIsNone(unbounded["min"])
        self.assertIsNone(unbounded["max"])

    def test_site_convars_agree_with_the_codegen_bounds(self):
        import json
        codegen = json.loads(self._read("generated/downstream-codegen-schemas/convars_schema.json"))
        site = json.loads(self._read("generated/data/convars.json"))
        by_name = {c["name"]: c for c in site["convars"]}
        for c in codegen["convars"]:
            self.assertEqual((c["min"], c["max"]), (by_name[c["name"]]["min"], by_name[c["name"]]["max"]), c["name"])

    def test_nested_proto_overlay_key_reaches_both_outputs(self):
        import json
        data = json.loads(self._read("generated/data/protobufs.json"))
        demo = [f for f in data["files"] if f["stem"] == "demo"][0]
        nested = [m for m in demo["messages"] if m["qualified"] == "CDemoClassInfo.class_t"][0]
        self.assertEqual(nested["description"], "One class id to network-class-name row.")
        field = [f for f in nested["fields"] if f["name"] == "network_name"][0]
        self.assertEqual(field["description"], "The network class name the id maps to.")
        self.assertIn("One class id to network-class-name row.", self._read("generated/proto/demo.md"))

    def test_proto_enum_values_carry_name_and_number_only(self):
        import json
        data = json.loads(self._read("generated/data/protobufs.json"))
        for f in data["files"]:
            for e in f["enums"]:
                for v in e["values"]:
                    self.assertEqual(set(v), {"name", "number"}, e["qualified"])

    def test_items_carry_no_rarity_or_quality_field(self):
        import json
        data = json.loads(self._read("generated/data/items.json"))
        for it in data["items"]:
            self.assertNotIn("rarity", it)
            self.assertNotIn("quality", it)

    def test_meta_dates_come_from_the_build_provenance(self):
        import json
        meta = json.loads(self._read("generated/data/meta.json"))
        self.assertEqual(meta["steam_manifest_utc"], "2026-08-28T00:00:00Z")
        self.assertNotIn("generated_utc", meta)

    def test_commands_schema_carries_the_completion_flag(self):
        import json
        data = json.loads(self._read("generated/downstream-codegen-schemas/commands_schema.json"))
        self.assertTrue(all("has_completion_callback" in c for c in data["commands"]))

    def test_nested_proto_types_get_a_section_and_a_link(self):
        page = self._read("generated/proto/demo.md")
        self.assertIn("#### `CDemoClassInfo.class_t`", page)
        self.assertIn("[CDemoClassInfo.class_t](#cdemoclassinfoclass_t)", page)

    def test_proto_diagram_uses_qualified_node_ids(self):
        page = self._read("generated/proto/demo.md")
        self.assertIn('class CDemoClassInfo_class_t["CDemoClassInfo.class_t"]', page)

    def test_cross_file_proto_type_links_to_its_page(self):
        # gameevents.proto's key_t carries a networkbasetypes type.
        page = self._read("generated/proto/gameevents.md")
        self.assertIn("networkbasetypes.md#", page)

    def test_duplicate_event_names_get_unique_headings_and_anchors(self):
        page = self._read("generated/gameevents.md")
        self.assertIn("### player_death (core.gameevents)", page)
        self.assertIn("### player_death (mod.gameevents)", page)
        self.assertIn("(#player_death-modgameevents)", page)

    def test_network_page_links_message_anchors(self):
        self.assertRegex(self._read("generated/network.md"), r"\]\(proto/\w+\.md#\w+\)")

    def test_changelog_says_there_were_no_changes(self):
        page = self._read("generated/changelog.md")
        self.assertIn("No changes in", page)
        self.assertIn("Families diffed:", page)

    def test_empty_values_do_not_render_as_empty_code_spans(self):
        for rel in ("generated/items.md", "generated/maps.md", "generated/props.md"):
            self.assertNotIn("``", self._read(rel), rel)

    def test_heading_ids_do_not_embed_counts(self):
        self.assertIn("## Items\n", self._read("generated/items.md"))
        self.assertIn("## Prop classes\n", self._read("generated/props.md"))

    def test_mermaid_names_are_backticked_never_double_quoted(self):
        page = self._read("generated/schemas/modellib/CBoneConstraintPoseSpaceBone.md")
        self.assertIn(
            "CBoneConstraintPoseSpaceBone *-- `CBoneConstraintPoseSpaceBone::Input_t`",
            page,
        )
        body = page.split("---\n", 2)[-1]
        self.assertNotIn('"CBoneConstraintPoseSpaceBone::Input_t"', body)

    def test_nested_type_gets_its_own_page_and_link(self):
        page = self._read("generated/schemas/modellib/CBoneConstraintPoseSpaceBone.md")
        self.assertIn(
            "[CBoneConstraintPoseSpaceBone::Input_t]"
            "(../modellib/CBoneConstraintPoseSpaceBone.Input_t.md)",
            page,
        )

    def test_zero_field_class_says_so(self):
        pages = [p for p in (EXPECTED / "generated" / "schemas").rglob("*.md")
                 if "No schema-visible fields" in p.read_text(encoding="utf-8")]
        self.assertTrue(pages, "expected at least one class page with no fields")


if __name__ == "__main__":
    unittest.main()
