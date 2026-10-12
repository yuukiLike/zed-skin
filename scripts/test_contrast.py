"""Regression coverage for theme validation, search highlights and Markdown selections.

Run: python3 -m unittest discover -s scripts -p 'test_*.py'
"""

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from check_contrast import (
    COLOR_DISTANCE_GROUPS, MARKDOWN_SELECTION, ROOT, VIVID_GREEN_CAPTURES,
    audit, color_distance, composite, contrast, markdown_selection_checks,
    oklab, read_object, rgb, search_highlight_checks, selection_color,
)


class MarkdownSelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.themes = json.loads((ROOT / "themes/green-tree.json").read_text())["themes"]

    def test_all_four_themes_keep_selected_text_readable(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                target = 2.5 if theme["name"] == "GreenTree Day Vivid" else 4.5
                rows = markdown_selection_checks(theme["style"], target)
                self.assertTrue(any("inline code" in row[2] for row in rows))
                self.assertTrue(any(row[1] == "syntax.comment" for row in rows))
                self.assertFalse([row for row in rows if row[0] == "Markdown selection" and row[3] < row[4]])

    def test_current_zed_selection_below_glyphs_keeps_text_readable(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                target = 2.5 if theme["name"] == "GreenTree Day Vivid" else 4.5
                rows = markdown_selection_checks(theme["style"], target)
                current = [row for row in rows if row[0] == "Markdown selection (under text)"]
                self.assertTrue(current)
                self.assertFalse([row for row in current if row[3] < row[4]])

    def test_old_vivid_green_fails_current_paint_order(self):
        style = copy.deepcopy(self.themes[0]["style"])
        for capture in VIVID_GREEN_CAPTURES:
            style["syntax"][capture]["color"] = "#00A84A"
        rows = markdown_selection_checks(style, 2.5)
        self.assertTrue(all(row[3] >= row[4] for row in rows if row[0] == "Markdown selection"))
        self.assertTrue(any(row[3] < row[4] for row in rows if row[0] == "Markdown selection (under text)"))

    def test_prose_links_inline_code_and_fenced_code_are_covered(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                rows = markdown_selection_checks(theme["style"], 2.5)
                for group in ("Markdown selection", "Markdown selection (under text)"):
                    cases = [(row[1], row[2]) for row in rows if row[0] == group]
                    self.assertIn(("text", "editor.background"), cases)
                    self.assertIn(("text.accent", "editor.background / link"), cases)
                    self.assertIn(("text", "editor.background / inline code"), cases)
                    self.assertIn(("syntax.comment", "editor.background / code block"), cases)
                    for capture in ("diff.plus", "diff.minus"):
                        self.assertIn((f"syntax.{capture}", f"syntax.{capture}.background_color / code block"), cases)

    def test_inline_code_search_and_selection_overlap_is_covered(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                rows = markdown_selection_checks(theme["style"], 2.5 if theme["appearance"] == "light" else 4.5)
                overlap = [row for row in rows if row[2].startswith("search.")]
                for key in ("search.match_background", "search.active_match_background"):
                    for foreground in ("text", "text.accent"):
                        self.assertTrue(any(row[1] == foreground and row[2] == f"{key} / inline code" for row in overlap))
                self.assertTrue(any(row[0] == "Markdown search selection visibility" for row in overlap))
                self.assertFalse([row for row in overlap if row[3] < row[4]])

    def test_faint_selection_over_a_search_match_fails(self):
        style = copy.deepcopy(self.themes[-1]["style"])
        style[MARKDOWN_SELECTION] = "#408CFF06"
        rows = markdown_selection_checks(style, 4.5)
        self.assertTrue(any(row[0] == "Markdown search selection visibility" and row[3] < row[4] for row in rows))

    def test_fenced_code_search_and_selection_overlap_is_covered(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                rows = markdown_selection_checks(theme["style"], 2.5 if theme["appearance"] == "light" else 4.5)
                overlap = [row for row in rows if row[2].startswith("search.") and row[2].endswith(" / code block")]
                cases = {(row[0], row[1], row[2]) for row in overlap}
                for group in ("Markdown selection", "Markdown selection (under text)"):
                    for key in ("search.match_background", "search.active_match_background"):
                        for capture in theme["style"]["syntax"]:
                            self.assertIn((group, f"syntax.{capture}", f"{key} / code block"), cases)
                self.assertFalse([row for row in overlap if row[3] < row[4]])

    def test_previous_dark_palettes_fail_when_search_and_selection_stack(self):
        for theme in self.themes[1:]:
            with self.subTest(theme=theme["name"]):
                style = copy.deepcopy(theme["style"])
                old_comment = "#A8A8A8" if theme["name"] == "GreenTree Day AAA" else "#979797"
                for capture in ("comment", "comment.doc"):
                    style["syntax"][capture]["color"] = old_comment
                if theme["name"] == "GreenTree Midnight AAA":
                    style[MARKDOWN_SELECTION] = "#408CFF4D"
                rows = markdown_selection_checks(style, 4.5)
                failed = [row for row in rows if row[3] < row[4]]
                self.assertTrue(failed)
                self.assertTrue(any(row[1] == "syntax.comment" and row[2].startswith("search.")
                                    and row[2].endswith(" / code block") for row in failed))

    def test_all_four_selections_stand_out_from_their_surfaces(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                rows = markdown_selection_checks(theme["style"], 4.5)
                visibility = [row for row in rows if row[0] == "Markdown selection visibility"]
                self.assertTrue(any("inline code" in row[2] for row in visibility))
                self.assertTrue(any("syntax.diff.minus.background_color" in row[2] for row in visibility))
                self.assertFalse([row for row in visibility if row[3] < row[4]])

    def test_faint_selection_fails_even_when_text_contrast_passes(self):
        style = copy.deepcopy(self.themes[1]["style"])
        style[MARKDOWN_SELECTION] = "#408CFF06"
        rows = markdown_selection_checks(style, 4.5)
        self.assertTrue(all(row[3] >= row[4] for row in rows if row[0] == "Markdown selection"))
        self.assertTrue(any(row[3] < row[4] for row in rows if row[0] == "Markdown selection visibility"))

    def test_aa_exceptions_do_not_weaken_primary_text_targets(self):
        for theme in self.themes[1:]:
            with self.subTest(theme=theme["name"]):
                rows = audit(theme)
                for group in ("Comments", "Markdown selection", "Markdown selection (under text)"):
                    self.assertEqual({row[4] for row in rows if row[0] == group}, {4.5})
                for group in ("Editor / syntax", "UI text", "Terminal text"):
                    primary = [row for row in rows if row[0] == group
                               and not row[2].startswith("search.") and ".selection" not in row[2]]
                    self.assertTrue(primary)
                    self.assertEqual({row[4] for row in primary}, {7})
                    interaction = [row for row in rows if row[0] == group
                                   and (row[2].startswith("search.") or ".selection" in row[2])]
                    self.assertTrue(interaction)
                    self.assertEqual({row[4] for row in interaction}, {4.5})

    def test_opaque_or_invisible_selections_are_rejected(self):
        for theme in self.themes:
            style = copy.deepcopy(theme["style"])
            for color in ("#0C1A2D", "#0C1A2DFF", "#0C1A2D00", "#ZZZZZZ80", None):
                with self.subTest(theme=theme["name"], color=color):
                    style[MARKDOWN_SELECTION] = color
                    with self.assertRaises(ValueError):
                        markdown_selection_checks(style, 7)

    def test_high_opacity_reduces_glyph_contrast(self):
        style = copy.deepcopy(self.themes[-1]["style"])
        style[MARKDOWN_SELECTION] = "#408CFFEE"
        rows = markdown_selection_checks(style, 7)
        # Merely requiring alpha < 1 would still allow almost invisible text.
        self.assertTrue(all(row[3] < row[4] for row in rows if row[0] == "Markdown selection"))

    def test_source_over_composites_foreground_as_well_as_background(self):
        self.assertEqual(composite("#408CFF00", rgb("#FFFFFF")), rgb("#FFFFFF"))
        for under in ("#FFFFFF", "#000000"):
            self.assertEqual(composite("#408CFFFF", rgb(under)), rgb("#408CFF"))
        self.assertAlmostEqual(composite("#FFFFFF80", rgb("#000000"))[0], 128 / 255)


class SearchHighlightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.themes = json.loads((ROOT / "themes/green-tree.json").read_text())["themes"]

    def test_all_variants_have_visible_and_distinct_matches(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                rows = search_highlight_checks(theme["style"])
                self.assertFalse([row for row in rows if row[3] < row[4]])

    def test_search_covers_active_lines_and_rendered_markdown(self):
        rows = search_highlight_checks(self.themes[0]["style"])
        cases = {(row[1], row[2]) for row in rows}
        for match in ("search.match_background", "search.active_match_background"):
            for surface in ("editor.background", "editor.active_line.background",
                            "editor.highlighted_line.background", "surface.background",
                            "editor.background / inline code", "editor.background / link"):
                self.assertIn((match, surface), cases)
        for state in ("active match", "active match / search focused", "active match / editor focused"):
            self.assertIn((state, "ordinary match"), cases)

    def test_previous_search_palette_is_rejected_in_every_variant(self):
        old_colors = [
            ("#FFF5DD", "#FFF1CC"), ("#292820", "#302C20"),
            ("#252117", "#292416"), ("#17140B", "#201A0C"),
        ]
        for theme, (ordinary, active) in zip(self.themes, old_colors):
            with self.subTest(theme=theme["name"]):
                old = copy.deepcopy(theme)
                old["style"]["search.match_background"] = ordinary
                old["style"]["search.active_match_background"] = active
                rows = audit(old)
                # The old text-only audit did not check search/selection stacking.
                old_scope = [row for row in rows if row[0] not in COLOR_DISTANCE_GROUPS | {"Active search visibility"}
                             and not (row[0].startswith("Markdown selection") and row[2].startswith("search."))]
                self.assertFalse([row for row in old_scope if row[3] < row[4]])
                self.assertTrue(any(row[3] < row[4] for row in rows if row[0] == "Search state distinction"))

    def test_brown_active_match_hidden_by_selection_is_rejected(self):
        for theme, selection in zip(self.themes[1:], ("#242D43", "#15263E", "#0C1A2D")):
            with self.subTest(theme=theme["name"]):
                style = copy.deepcopy(theme["style"])
                style["search.match_background"] = "#380867"
                style["search.active_match_background"] = "#441B00"
                style["players"][0]["selection"] = selection
                rows = search_highlight_checks(style)
                self.assertTrue(all(row[3] >= row[4] for row in rows
                                    if row[0] == "Search state distinction"))
                self.assertTrue(any(row[0] == "Active search visibility" and row[3] < row[4] for row in rows))

    def test_focused_match_cannot_disappear_into_the_surface(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                style = copy.deepcopy(theme["style"])
                style["players"][0]["selection"] = style["editor.background"]
                rows = search_highlight_checks(style)
                self.assertTrue(any(row[0] == "Search visibility" and row[1] == "active match / editor focused"
                                    and row[3] == 0 for row in rows))

    def test_invisible_local_selection_fails(self):
        style = copy.deepcopy(self.themes[-1]["style"])
        style["players"][0]["selection"] = "#408CFF00"
        rows = search_highlight_checks(style)
        self.assertTrue(any(row[0] == "Editor selection visibility" and row[3] == 0 for row in rows))

    def test_search_text_covers_both_editor_focus_states(self):
        for theme in self.themes[1:]:
            with self.subTest(theme=theme["name"]):
                rows = audit(theme)
                for suffix in ("players[0].selection", "players[0].selection / search focused"):
                    selected = [row for row in rows if row[0] in ("Editor / syntax", "Comments")
                                and row[2] == f"search.active_match_background / {suffix}"]
                    self.assertTrue(selected)
                    self.assertTrue(all(row[3] >= row[4] == 4.5 for row in selected))

    def test_transparent_selection_preserves_the_active_search_fill(self):
        for theme in self.themes[1:]:
            with self.subTest(theme=theme["name"]):
                style = theme["style"]
                selection = style["players"][0]["selection"]
                active = selection_color(selection, rgb(style["search.active_match_background"]))
                plain = selection_color(selection, rgb(style["editor.background"]))
                self.assertGreater(color_distance(active, plain), 0.1)

    def test_invisible_match_fails_despite_readable_text(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                bad = copy.deepcopy(theme)
                bad["style"]["search.match_background"] = bad["style"]["editor.background"]
                rows = audit(bad)
                self.assertTrue(any(row[0] == "Search visibility" and row[3] == 0 for row in rows))
                self.assertFalse([row for row in rows if row[0] == "Editor / syntax" and row[3] < row[4]])

    def test_same_active_and_ordinary_colors_fail(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                style = copy.deepcopy(theme["style"])
                style["search.active_match_background"] = style["search.match_background"]
                rows = search_highlight_checks(style)
                self.assertTrue(any(row[0] == "Search state distinction" and row[3] == 0 for row in rows))

    def test_almost_identical_colors_fail_not_only_exact_duplicates(self):
        style = copy.deepcopy(self.themes[-1]["style"])
        style["search.match_background"] = "#380867"
        style["search.active_match_background"] = "#380868"
        rows = search_highlight_checks(style)
        self.assertTrue(any(0 < row[3] < row[4] for row in rows if row[0] == "Search state distinction"))

    def test_selection_can_hide_active_match_distinction(self):
        style = copy.deepcopy(self.themes[-1]["style"])
        style["players"][0]["selection"] = style["search.match_background"]
        rows = search_highlight_checks(style)
        self.assertTrue(any(row[1] == "active match / editor focused" and row[3] == 0 for row in rows))
        self.assertTrue(all(row[3] >= row[4] for row in rows if row[1] == "active match"))

    def test_bright_search_background_cannot_sacrifice_text(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                bad = copy.deepcopy(theme)
                bad["style"]["search.match_background"] = bad["style"]["editor.foreground"]
                rows = audit(bad)
                self.assertTrue(any(row[0] == "Editor / syntax" and row[3] < row[4] for row in rows))

    def test_search_transparency_is_rejected_instead_of_miscomputed(self):
        style = copy.deepcopy(self.themes[-1]["style"])
        for key in ("search.match_background", "search.active_match_background"):
            for color in ("#00000000", "#38086780", None):
                with self.subTest(key=key, color=color):
                    bad = copy.deepcopy(style)
                    bad[key] = color
                    with self.assertRaises(ValueError):
                        search_highlight_checks(bad)


class ThemeValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.family = json.loads((ROOT / "themes/green-tree.json").read_text(), object_pairs_hook=read_object)

    def test_entire_palette_passes_for_all_four_variants(self):
        self.assertEqual(len(self.family["themes"]), 4)
        for theme in self.family["themes"]:
            with self.subTest(theme=theme["name"]):
                self.assertFalse([row for row in audit(theme) if row[3] < row[4]])

    def test_missing_interaction_keys_are_rejected(self):
        for key in ("search.match_background", "search.active_match_background", MARKDOWN_SELECTION):
            with self.subTest(key=key):
                theme = copy.deepcopy(self.family["themes"][-1])
                del theme["style"][key]
                with self.assertRaisesRegex(ValueError, "Missing fields"):
                    audit(theme)

    def test_unknown_keys_cannot_silently_fall_back(self):
        theme = copy.deepcopy(self.family["themes"][-1])
        theme["style"]["search.match_backgound"] = "#FFFF00"
        with self.assertRaisesRegex(ValueError, "unclassified fields"):
            audit(theme)

    def test_duplicate_json_keys_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate JSON key"):
            json.loads('{"style":{"search.match_background":"#123456","search.match_background":"#000000"}}',
                       object_pairs_hook=read_object)

    def test_unknown_theme_cannot_weaken_contrast_target(self):
        theme = copy.deepcopy(self.family["themes"][-1])
        theme["name"] = "Renamed theme"
        with self.assertRaisesRegex(ValueError, "No explicit text contrast target"):
            audit(theme)

    def test_missing_syntax_capture_is_rejected(self):
        theme = copy.deepcopy(self.family["themes"][-1])
        del theme["style"]["syntax"]["text.literal"]
        with self.assertRaisesRegex(ValueError, "Missing syntax captures"):
            audit(theme)

    def test_cli_returns_failure_for_invisible_search(self):
        family = copy.deepcopy(self.family)
        style = family["themes"][-1]["style"]
        style["search.match_background"] = style["editor.background"]
        with tempfile.TemporaryDirectory() as directory:
            theme_path = Path(directory) / "bad-theme.json"
            theme_path.write_text(json.dumps(family))
            result = subprocess.run([sys.executable, str(ROOT / "scripts/check_contrast.py"), str(theme_path)],
                                    capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Search visibility", result.stderr)
        self.assertIn("ΔEOK", result.stderr)

    def test_cli_rejects_duplicate_theme_names(self):
        family = copy.deepcopy(self.family)
        family["themes"].append(copy.deepcopy(family["themes"][0]))
        with tempfile.TemporaryDirectory() as directory:
            theme_path = Path(directory) / "bad-theme.json"
            theme_path.write_text(json.dumps(family))
            result = subprocess.run([sys.executable, str(ROOT / "scripts/check_contrast.py"), str(theme_path)],
                                    capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Theme names must be unique", result.stderr)


class ColorMathTests(unittest.TestCase):
    def test_selection_alpha_is_multiplied_by_focus_opacity(self):
        black = rgb("#000000")
        self.assertAlmostEqual(selection_color("#FFFFFF80", black)[0], 128 / 255)
        self.assertAlmostEqual(selection_color("#FFFFFF80", black, 0.5)[0], 64 / 255)
        self.assertEqual(selection_color("#FFFFFF", black, 0.5), (0.5, 0.5, 0.5))

    def test_black_white_contrast_and_symmetry(self):
        self.assertEqual(contrast("#000000", "#FFFFFF"), 21)
        self.assertEqual(contrast("#FFFFFF", "#000000"), 21)
        self.assertEqual(contrast("#123456", "#123456"), 1)

    def test_unrounded_contrast_does_not_pass_at_a_rounded_boundary(self):
        ratio = contrast("#777777", "#FFFFFF")
        self.assertEqual(round(ratio, 1), 4.5)
        self.assertLess(ratio, 4.5)

    def test_oklab_reference_colors(self):
        for color, expected in (
            ("#000000", (0, 0, 0)), ("#FFFFFF", (1, 0, 0)),
            ("#FF0000", (0.6279554, 0.2248631, 0.1258463)),
            ("#00FF00", (0.8664396, -0.2338876, 0.1794985)),
            ("#0000FF", (0.4520137, -0.0324570, -0.3115281)),
        ):
            with self.subTest(color=color):
                for actual, reference in zip(oklab(rgb(color)), expected):
                    self.assertAlmostEqual(actual, reference, places=6)

    def test_color_distance_is_symmetric_and_zero_only_for_same_color(self):
        red, blue = rgb("#FF0000"), rgb("#0000FF")
        self.assertEqual(color_distance(red, red), 0)
        self.assertAlmostEqual(color_distance(red, blue), color_distance(blue, red))
        self.assertGreater(color_distance(red, blue), 0.5)

    def test_invalid_or_nonopaque_palette_colors_are_rejected(self):
        for color in ("red", "#fff", "#12345600", "#XYZXYZ", "123456", None, 123456):
            with self.subTest(color=color):
                with self.assertRaises(ValueError):
                    rgb(color)


if __name__ == "__main__":
    unittest.main()
