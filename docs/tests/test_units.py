"""Unit tests for the pure helpers in docs/generate_docs.py.

Run with pytest or `python3 -m unittest`; see docs/tests/README.md.
"""

from __future__ import annotations

import unittest

from _gen import gd, sd


def _cls(name, module, binary, bases=(), base_modules=(), fields=(), **extra):
    rec = {
        "name": name,
        "kind": "class",
        "module": module,
        "binary_module": binary,
        "bases": list(bases),
        "base_modules": list(base_modules),
        "fields": [dict(f) for f in fields],
        "metadata": [],
        "enum_underlying": None,
        "size": 64,
        "alignment": 8,
        "flags": 0,
        "cpp_name": name,
        "raw": {"name": name},
    }
    rec.update(extra)
    return rec


def twin_entities():
    """Two client/server twins plus a shared base, keyed the way the loader keys them."""
    entities: dict[str, dict] = {}
    for rec in (
        # The client record registers first, as it does in the real artifact.
        _cls("CBaseEntity", "client", "client.dll",
             fields=[{"name": "m_iHealth", "type": "int32", "offset": 0x34C,
                      "annotations": []}]),
        _cls("CBaseEntity", "server", "server.dll",
             fields=[{"name": "m_iHealth", "type": "int32", "offset": 0x2D0,
                      "annotations": []}]),
        _cls("CPawn", "client", "client.dll",
             bases=["CBaseEntity"], base_modules=["client.dll"],
             fields=[{"name": "m_flClient", "type": "float32", "offset": 0x400,
                      "annotations": []}]),
        _cls("CPawn", "server", "server.dll",
             bases=["CBaseEntity"], base_modules=["server.dll"],
             fields=[{"name": "m_flServer", "type": "float32", "offset": 0x400,
                      "annotations": []}]),
        _cls("COnlyOnServer", "server", "server.dll",
             bases=["CBaseEntity"], base_modules=["server.dll"]),
    ):
        gd._add_entity(entities, rec)
    return entities


class ResolverTests(unittest.TestCase):
    def setUp(self):
        self.entities = twin_entities()

    def test_client_record_is_primary(self):
        self.assertEqual(self.entities["CBaseEntity"]["module"], "client")

    def test_prefers_same_project_name(self):
        v = gd._resolve_variant("CBaseEntity", self.entities, "server")
        self.assertEqual(v["module"], "server")

    def test_falls_back_to_binary_module(self):
        v = gd._resolve_variant("CBaseEntity", self.entities, "", "server.dll")
        self.assertEqual(v["module"], "server")

    def test_falls_back_to_primary(self):
        v = gd._resolve_variant("CBaseEntity", self.entities, "particles")
        self.assertEqual(v["module"], "client")

    def test_unknown_name_is_none(self):
        self.assertIsNone(gd._resolve_variant("CNope", self.entities, "server"))

    def test_base_variant_uses_the_childs_module(self):
        server_pawn = gd._resolve_variant("CPawn", self.entities, "server")
        base = gd._base_variant_for(server_pawn, "CBaseEntity", self.entities)
        self.assertEqual(base["module"], "server")

    def test_server_layout_takes_the_server_offset(self):
        server_pawn = gd._resolve_variant("CPawn", self.entities, "server")
        rows, _ = gd._flatten_layout(server_pawn, self.entities)
        health = [r for r in rows if r["field"]["name"] == "m_iHealth"][0]
        self.assertEqual(health["field"]["offset"], 0x2D0)
        self.assertEqual(len(rows), 2)

    def test_client_layout_takes_the_client_offset(self):
        client_pawn = gd._resolve_variant("CPawn", self.entities, "client")
        rows, _ = gd._flatten_layout(client_pawn, self.entities)
        health = [r for r in rows if r["field"]["name"] == "m_iHealth"][0]
        self.assertEqual(health["field"]["offset"], 0x34C)

    def test_derived_by_is_module_scoped(self):
        children = gd._build_children_index(self.entities)
        server_base = gd._resolve_variant("CBaseEntity", self.entities, "server")
        names = sorted(c["name"] for c in
                       gd._own_children(server_base, self.entities, children))
        self.assertEqual(names, ["COnlyOnServer", "CPawn"])
        client_base = gd._resolve_variant("CBaseEntity", self.entities, "client")
        self.assertEqual(
            [c["name"] for c in gd._own_children(client_base, self.entities, children)],
            ["CPawn"],
        )

    def test_consistency_check_passes_on_resolved_layouts(self):
        violations, exempt = gd.check_module_layout_consistency(self.entities)
        self.assertEqual(violations, [])
        self.assertEqual(exempt, 0)

    def test_consistency_check_catches_the_bare_name_regression(self):
        # Reinstate the old behaviour: resolve a base by bare name, first
        # registration wins.  The server pawn then inherits the client layout,
        # which is exactly what the check exists to refuse.
        original = gd._base_variant_for
        gd._base_variant_for = lambda child, base, entities: entities.get(base)
        try:
            violations, _ = gd.check_module_layout_consistency(self.entities)
        finally:
            gd._base_variant_for = original
        self.assertTrue(any("CPawn" in v for v in violations), violations)
        self.assertTrue(any("client/CBaseEntity" in v for v in violations), violations)

    def test_layout_rows_record_the_declaring_module(self):
        server_pawn = gd._resolve_variant("CPawn", self.entities, "server")
        rows, _ = gd._flatten_layout(server_pawn, self.entities)
        health = [r for r in rows if r["field"]["name"] == "m_iHealth"][0]
        self.assertEqual(health["declaring_module"], "server")


class CellEscapingTests(unittest.TestCase):
    def test_free_text_escapes_html(self):
        self.assertEqual(
            gd._md_cell("bot_stop <difficulty>"),
            "bot_stop &lt;difficulty&gt;",
        )

    def test_free_text_escapes_ampersand_first(self):
        self.assertEqual(gd._md_cell("a & <b>"), "a &amp; &lt;b&gt;")

    def test_free_text_escapes_pipe(self):
        self.assertEqual(gd._md_cell("a | b"), "a \\| b")

    def test_free_text_folds_newlines(self):
        self.assertEqual(gd._md_cell("one\ntwo\r\nthree"), "one<br>two<br>three")

    def test_free_text_strips_block_scalar_tail(self):
        self.assertEqual(gd._md_cell("text\n"), "text")

    def test_free_text_empty(self):
        self.assertEqual(gd._md_cell(None), "")
        self.assertEqual(gd._md_cell("   \n "), "")

    def test_prose_keeps_markdown(self):
        self.assertEqual(
            gd._md_prose("see [the page](x.md) <not a tag>\n"),
            "see [the page](x.md) <not a tag>",
        )
        self.assertEqual(gd._md_prose("a | b"), "a \\| b")

    def test_code_cell_uses_the_entity_for_pipes(self):
        self.assertEqual(gd._md_code_cell("a || b"), "a &#124;&#124; b")

    def test_code_cell_does_not_html_escape(self):
        self.assertEqual(gd._md_code_cell("CUtlVector< int32 >"),
                         "CUtlVector< int32 >")

    def test_code_helper_returns_empty_for_empty(self):
        self.assertEqual(gd._code(""), "")
        self.assertEqual(gd._code(None), "")
        self.assertEqual(gd._code("x"), "`x`")

    def test_defuse_tags_leaves_templates_alone(self):
        self.assertEqual(gd._defuse_tags("CUtlVector< int32 >"),
                         "CUtlVector< int32 >")
        self.assertEqual(gd._defuse_tags("<b>bold"), "&lt;b>bold")

    def test_enum_value_wraps_negative_under_unsigned(self):
        self.assertEqual(gd._enum_value_cell("-1", "uint32_t"), "-1 (`0xffffffff`)")
        self.assertEqual(gd._enum_value_cell("-1", "int32_t"), "-1")
        self.assertEqual(gd._enum_value_cell("3", "uint32_t"), "3")
        self.assertEqual(gd._enum_value_cell("", "uint32_t"), "")


class MermaidTests(unittest.TestCase):
    def test_plain_identifier_is_unquoted(self):
        self.assertEqual(gd._mermaid_safe("CBaseEntity"), "CBaseEntity")

    def test_nested_name_uses_backticks(self):
        # Mermaid 10.9's classDiagram grammar rejects the double-quoted form.
        self.assertEqual(gd._mermaid_safe("A::B"), "`A::B`")

    def test_dotted_name_uses_backticks(self):
        self.assertEqual(gd._mermaid_safe("CDemo.class_t"), "`CDemo.class_t`")

    def test_no_double_quotes_are_emitted(self):
        for name in ("A::B", "CDemo.class_t", "a b", "x<y>"):
            self.assertNotIn('"', gd._mermaid_safe(name))

    def test_mermaid_id_is_a_plain_identifier(self):
        self.assertEqual(gd._mermaid_id("CMsgSource1LegacyGameEvent.key_t"),
                         "CMsgSource1LegacyGameEvent_key_t")


class TypeLinkTests(unittest.TestCase):
    def setUp(self):
        self.entities = {}
        for rec in (
            _cls("CBaseEntity", "server", "server.dll"),
            _cls("CNmBlend1DNode", "animlib", "animationsystem.dll"),
            _cls("CNmBlend1DNode::CDefinition", "animlib", "animationsystem.dll"),
        ):
            gd._add_entity(self.entities, rec)

    def test_nested_name_is_matched_whole(self):
        self.assertEqual(
            gd._extract_type_refs("CNmBlend1DNode::CDefinition", self.entities),
            ["CNmBlend1DNode::CDefinition"],
        )

    def test_unknown_nested_falls_back_to_the_outer_class(self):
        self.assertEqual(
            gd._extract_type_refs("CNmBlend1DNode::CNope", self.entities),
            ["CNmBlend1DNode"],
        )

    def test_link_targets_the_nested_page(self):
        out = gd._md_link_type("CNmBlend1DNode::CDefinition", self.entities, "animlib")
        self.assertEqual(
            out,
            "[CNmBlend1DNode::CDefinition](../animlib/CNmBlend1DNode.CDefinition.md)",
        )

    def test_link_leaves_the_unknown_tail_as_text(self):
        out = gd._md_link_type("CNmBlend1DNode::CNope", self.entities, "animlib")
        self.assertEqual(out, "[CNmBlend1DNode](../animlib/CNmBlend1DNode.md)::CNope")

    def test_template_type_links_the_inner_class(self):
        out = gd._md_link_type("CHandle< CBaseEntity >", self.entities, "server")
        self.assertEqual(out, "CHandle< [CBaseEntity](../server/CBaseEntity.md) >")

    def test_type_filename_maps_nested_names(self):
        self.assertEqual(gd._type_filename("A::B"), "A.B")


class OverlayTests(unittest.TestCase):
    def test_lookup_prefers_the_module_key(self):
        overlays = {
            "server/CFoo": {"description": "server text"},
            "client/CFoo": {"description": "client text"},
        }
        self.assertEqual(
            gd.get_overlay(overlays, "client", "CFoo")["description"], "client text"
        )

    def test_lookup_falls_back_to_the_name(self):
        overlays = {"server/CFoo": {"description": "server text"}}
        self.assertEqual(
            gd.get_overlay(overlays, "particles", "CFoo")["description"], "server text"
        )

    def test_lookup_misses_return_empty(self):
        self.assertEqual(gd.get_overlay({}, "server", "CFoo"), {})

    def test_block_scalar_tails_are_stripped_at_load(self):
        stripped = gd._strip_overlay_strings(
            {"a": "text\n", "b": {"c": "more\n"}, "d": ["x\n"]}
        )
        self.assertEqual(stripped, {"a": "text", "b": {"c": "more"}, "d": ["x"]})

    def test_unresolved_keys_are_reported_with_a_suggestion(self):
        entities = twin_entities()
        overlays = {
            "server/CPawn": {"fields": {"m_flServer": {}, "m_flServerTypo": {}}},
            "server/CGone": {"description": "x"},
        }
        unresolved, mismatched = gd.check_overlay_keys(overlays, entities, [], [])
        joined = "\n".join(unresolved)
        self.assertIn("server/CGone", joined)
        self.assertIn("m_flServerTypo", joined)
        self.assertIn("nearest: m_flServer", joined)
        self.assertNotIn("m_flServer:", joined)
        self.assertEqual(mismatched, [])

    def test_module_mismatch_is_separate_from_unresolved(self):
        entities = twin_entities()
        overlays = {"client/COnlyOnServer": {"description": "x"}}
        unresolved, mismatched = gd.check_overlay_keys(overlays, entities, [], [])
        self.assertEqual(unresolved, [])
        self.assertEqual(len(mismatched), 1)
        self.assertIn("client/COnlyOnServer", mismatched[0])

    def test_unknown_overlay_stem_is_unresolved(self):
        entities = twin_entities()
        overlays = {
            "nonsense": {"CPawnTypo": {"description": "x"}},
            "nonsense/CPawnTypo": {"description": "x"},
            "sever": {"CPawn": {"description": "x"}},
            "sever/CPawn": {"description": "x"},
        }
        unresolved, mismatched = gd.check_overlay_keys(overlays, entities, [], [])
        joined = "\n".join(unresolved)
        self.assertIn("nonsense: no such module or overlay file", joined)
        self.assertIn("sever: no such module or overlay file (nearest: server)", joined)
        self.assertEqual(mismatched, [])

    def test_wrapper_overlay_stems_are_known(self):
        overlays = {
            "gameevents": {"events": {}},
            "gameevents/events": {},
            "convar_flags": {"flags": {}},
            "convar_flags/flags": {},
        }
        unresolved, _ = gd.check_overlay_keys(overlays, twin_entities(), [], [])
        self.assertEqual(unresolved, [])

    def test_game_event_keys_are_checked(self):
        overlays = {"gameevents": {"events": {
            "player_death": {"fields": {"userid": {}, "nope": {}}},
            "no_such_event": {},
        }}}
        events = [{"name": "player_death", "source": "core.gameevents",
                   "fields": [{"name": "userid"}]}]
        unresolved, _ = gd.check_overlay_keys(overlays, {}, [], events)
        joined = "\n".join(unresolved)
        self.assertIn("no_such_event", joined)
        self.assertIn("player_death.nope", joined)


class ProtoTests(unittest.TestCase):
    def setUp(self):
        self.proto = {
            "filename": "demo.proto",
            "messages": [
                {
                    "name": "CDemoClassInfo",
                    "fields": [{"name": "classes", "number": "1",
                                "type": "CDemoClassInfo.class_t",
                                "label": "repeated"}],
                    "nested": [{"name": "class_t", "fields": [], "nested": [],
                                "enums": [], "oneofs": []}],
                    "enums": [{"name": "mode_t", "values": [{"name": "M", "number": "0"}]}],
                    "oneofs": [],
                },
                {
                    "name": "CDemoOther",
                    "fields": [],
                    "nested": [{"name": "class_t", "fields": [], "nested": [],
                                "enums": [], "oneofs": []}],
                    "enums": [],
                    "oneofs": [],
                },
            ],
            "enums": [],
        }

    def test_nested_messages_are_flattened_with_qualified_names(self):
        names = [q for q, _ in gd._proto_flatten_messages(self.proto["messages"])]
        self.assertEqual(
            names,
            ["CDemoClassInfo", "CDemoClassInfo.class_t", "CDemoOther",
             "CDemoOther.class_t"],
        )

    def test_nested_enums_are_flattened(self):
        self.assertIn("CDemoClassInfo.mode_t",
                      [q for q, _ in gd._proto_flatten_enums(self.proto)])

    def test_ambiguous_simple_names_get_no_alias(self):
        index = gd._proto_name_index(self.proto)
        self.assertNotIn("class_t", index)
        self.assertEqual(index["CDemoClassInfo.class_t"], "CDemoClassInfo.class_t")

    def test_link_uses_the_qualified_anchor(self):
        index = gd._proto_name_index(self.proto)
        self.assertEqual(
            gd._proto_link_type("CDemoClassInfo.class_t", index),
            "[CDemoClassInfo.class_t](#cdemoclassinfoclass_t)",
        )

    def test_anchor_matches_the_heading_slug(self):
        self.assertEqual(gd._proto_anchor("CDemoClassInfo.class_t"),
                         "cdemoclassinfoclass_t")
        self.assertEqual(gd._proto_anchor("player_death (mod.gameevents)"),
                         "player_death-modgameevents")

    def test_cross_file_type_links_to_the_other_page(self):
        other = {"filename": "networkbasetypes.proto",
                 "messages": [{"name": "CMsgVector", "fields": [], "nested": [],
                               "enums": [], "oneofs": []}],
                 "enums": []}
        glob = gd._proto_global_index([self.proto, other])
        self.assertEqual(
            gd._proto_link_type("CMsgVector", gd._proto_name_index(self.proto), glob),
            "[CMsgVector](networkbasetypes.md#cmsgvector)",
        )

    def test_primitives_are_not_linked(self):
        index = gd._proto_name_index(self.proto)
        self.assertEqual(gd._proto_link_type("uint32", index), "uint32")

    def test_diagram_gives_same_named_nested_types_distinct_nodes(self):
        lines = "\n".join(gd._build_proto_mermaid(self.proto))
        self.assertIn('class CDemoClassInfo_class_t["CDemoClassInfo.class_t"]', lines)
        self.assertIn('class CDemoOther_class_t["CDemoOther.class_t"]', lines)


class ConVarBoundTests(unittest.TestCase):
    def test_integral_bound_is_an_int(self):
        self.assertEqual(gd._bound_number("-20.000000"), -20)
        self.assertIsInstance(gd._bound_number("-20.000000"), int)
        self.assertEqual(gd._bound_number("0"), 0)

    def test_fractional_bound_is_a_float(self):
        self.assertEqual(gd._bound_number("0.100000"), 0.1)

    def test_blank_and_non_finite_are_none(self):
        self.assertIsNone(gd._bound_number(""))
        self.assertIsNone(gd._bound_number(None))
        self.assertIsNone(gd._bound_number("inf"))
        self.assertIsNone(gd._bound_number("not a number"))


class FlagLegendTests(unittest.TestCase):
    def setUp(self):
        sd.WARNINGS.clear()
        sd.INFOS.clear()

    def test_new_upstream_flag_is_informational(self):
        overlays = {"convar_flags": {"flags": {"cheat": {"description": "Needs sv_cheats."}}}}
        convars = [{"flags": ["cheat", "brand_new"]}]
        commands = [{"flags": ["brand_new"]}]
        legend = sd._build_flags_legend(overlays, convars, commands)
        self.assertEqual(sd.WARNINGS, [])
        self.assertEqual(len(sd.INFOS), 1)
        self.assertIn("brand_new", sd.INFOS[0])
        new = [f for f in legend if f["name"] == "brand_new"][0]
        self.assertEqual(new["description"], "")
        self.assertEqual(new["convar_count"], 1)
        self.assertEqual(new["command_count"], 1)

    def test_missing_overlay_file_is_still_a_warning(self):
        sd._build_flags_legend({}, [{"flags": ["cheat"]}], [])
        self.assertEqual(len(sd.WARNINGS), 1)


class BitfieldTests(unittest.TestCase):
    def test_bit_index_accumulates_within_one_offset(self):
        rows = [
            {"field": {"name": "a", "type": "bitfield:1", "offset": 0}},
            {"field": {"name": "b", "type": "bitfield:1", "offset": 0}},
            {"field": {"name": "c", "type": "bitfield:2", "offset": 0}},
            {"field": {"name": "d", "type": "bitfield:1", "offset": 4}},
            {"field": {"name": "e", "type": "int32", "offset": 8}},
        ]
        gd._annotate_bitfields(rows)
        self.assertEqual([r.get("bits") for r in rows],
                         [(0, 0), (1, 1), (2, 3), (0, 0), None])


class TableCheckTests(unittest.TestCase):
    def _write(self, tmp, text):
        (tmp / "page.md").write_text(text, encoding="utf-8")
        return gd.check_markdown_tables(tmp)

    def test_accepts_a_well_formed_table(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(
                self._write(Path(d), "| A | B |\n|---|---|\n| 1 | 2 |\n\ntext\n"), []
            )

    def test_flags_a_row_broken_by_a_newline(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as d:
            problems = self._write(Path(d), "| A | B |\n|---|---|\n| 1 | two\nlines |\n")
            self.assertEqual(len(problems), 1)
            self.assertIn("lines |", problems[0])

    def test_ignores_fenced_blocks(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(
                self._write(Path(d), "```mermaid\nclassDiagram\n  A <|-- B\n```\n"), []
            )


if __name__ == "__main__":
    unittest.main()
