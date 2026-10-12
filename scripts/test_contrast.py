"""Regressions for theme validation and common editor, Markdown and terminal states.

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
    COLOR_DISTANCE_GROUPS, MARKDOWN_SELECTION, ROOT, TEXT_GROUPS,
    audit, color_distance, composite, contrast, contrast_rgb, interaction_checks, markdown_selection_checks,
    oklab, read_object, rgb, search_highlight_checks, selection_color,
    word_diff_backgrounds, word_diff_checks,
)


class MarkdownSelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.themes = json.loads((ROOT / "themes/green-tree.json").read_text())["themes"]

    def test_prose_links_inline_code_and_fenced_code_are_covered(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                rows = markdown_selection_checks(theme["style"])
                backgrounds = {row[2] for row in rows}
                for background in ("editor.background", "editor.background / link",
                                   "editor.background / inline code", "editor.background / code block"):
                    self.assertIn(background, backgrounds)
                for capture in ("diff.plus", "diff.minus"):
                    self.assertIn(f"syntax.{capture}.background_color / code block", backgrounds)

    def test_search_overlap_covers_inline_and_fenced_code(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                rows = markdown_selection_checks(theme["style"])
                overlap = [row for row in rows if row[0] == "Markdown search selection visibility"]
                self.assertEqual({row[2] for row in overlap}, {
                    f"{key} / {label}" for key in ("search.match_background", "search.active_match_background")
                    for label in ("inline code", "code block")
                })
                self.assertFalse([row for row in overlap if row[3] < row[4]])

    def test_faint_selection_over_a_search_match_fails(self):
        style = copy.deepcopy(self.themes[-1]["style"])
        style[MARKDOWN_SELECTION] = "#408CFF06"
        rows = markdown_selection_checks(style)
        self.assertTrue(any(row[0] == "Markdown search selection visibility" and row[3] < row[4] for row in rows))

    def test_all_four_selections_stand_out_from_their_surfaces(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                rows = markdown_selection_checks(theme["style"])
                visibility = [row for row in rows if row[0] == "Markdown selection visibility"]
                self.assertTrue(any("inline code" in row[2] for row in visibility))
                self.assertTrue(any("syntax.diff.minus.background_color" in row[2] for row in visibility))
                self.assertFalse([row for row in visibility if row[3] < row[4]])

    def test_faint_selection_is_still_rejected(self):
        style = copy.deepcopy(self.themes[1]["style"])
        style[MARKDOWN_SELECTION] = "#408CFF06"
        rows = markdown_selection_checks(style)
        self.assertTrue(any(row[3] < row[4] for row in rows if row[0] == "Markdown selection visibility"))

    def test_selected_text_below_aa_is_allowed(self):
        theme = copy.deepcopy(self.themes[-1])
        style = theme["style"]
        style[MARKDOWN_SELECTION] = "#408CFF80"
        background = composite(style[MARKDOWN_SELECTION], rgb(style["search.active_match_background"]))
        foreground = rgb(style["syntax"]["comment"]["color"])
        for painted in (foreground, composite(style[MARKDOWN_SELECTION], foreground)):
            self.assertLess(contrast_rgb(painted, background), 4.5)
        self.assertFalse([row for row in audit(theme) if row[3] < row[4]])

    def test_selection_exception_preserves_primary_and_search_targets(self):
        for theme in self.themes[1:]:
            with self.subTest(theme=theme["name"]):
                rows = audit(theme)
                self.assertEqual({row[4] for row in rows if row[0] == "Comments"}, {4.5})
                for group in ("Editor / syntax", "UI text", "Terminal text"):
                    primary = [row for row in rows if row[0] == group and not row[2].startswith("search.")]
                    self.assertTrue(primary)
                    self.assertEqual({row[4] for row in primary}, {7})
                for group in ("Editor / syntax", "UI text"):
                    search = [row for row in rows if row[0] == group and row[2].startswith("search.")]
                    self.assertTrue(search)
                    self.assertEqual({row[4] for row in search}, {4.5})

    def test_opaque_or_invisible_selections_are_rejected(self):
        for theme in self.themes:
            style = copy.deepcopy(theme["style"])
            for color in ("#0C1A2D", "#0C1A2DFF", "#0C1A2D00", "#ZZZZZZ80", None):
                with self.subTest(theme=theme["name"], color=color):
                    style[MARKDOWN_SELECTION] = color
                    with self.assertRaises(ValueError):
                        markdown_selection_checks(style)

    def test_source_over_composites_colors(self):
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
                # Text contrast alone did not catch the old faint backgrounds.
                old_scope = [row for row in rows if row[0] not in COLOR_DISTANCE_GROUPS | {"Active search visibility"}]
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

    def test_editor_and_terminal_selections_have_no_text_contrast_target(self):
        for theme in self.themes:
            with self.subTest(theme=theme["name"]):
                rows = audit(theme)
                self.assertFalse([row for row in rows if row[0] in TEXT_GROUPS and ".selection" in row[2]])
                self.assertTrue(any(row[0] == "Editor selection visibility" for row in rows))
                for state in ("search focused", "editor focused"):
                    self.assertTrue(any(row[0] == "Search state distinction"
                                        and row[1] == f"active match / {state}" for row in rows))

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


class InteractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.themes = json.loads((ROOT / "themes/green-tree.json").read_text())["themes"]

    def test_changed_words_cannot_blend_into_either_diff_row_style(self):
        for theme in self.themes:
            for kind in ("added", "deleted"):
                for surface in ("background", "hollow_background"):
                    with self.subTest(theme=theme["name"], kind=kind, surface=surface):
                        style = copy.deepcopy(theme["style"])
                        word, row = f"version_control.word_{kind}", f"editor.diff_hunk.{kind}.{surface}"
                        style[word] = style[row]
                        self.assertTrue(any(r[0] == "Diff word visibility" and r[1:3] == (word, row)
                                            and r[3] < r[4] for r in word_diff_checks(style)[0]))

    def test_opaque_word_fills_cannot_hide_search_results(self):
        for theme in self.themes:
            for word in ("version_control.word_added", "version_control.word_deleted"):
                for opacity in ("", "FF", "FE"):
                    with self.subTest(theme=theme["name"], word=word, opacity=opacity):
                        style = copy.deepcopy(theme["style"])
                        style[word] = "#00245E" + opacity
                        rows, _ = word_diff_checks(style)
                        self.assertTrue(any(r[0] == "Diff search distinction" and r[3] < r[4] for r in rows))

    def test_transparent_word_fills_cannot_erase_the_diff_emphasis(self):
        style = copy.deepcopy(self.themes[-1]["style"])
        style["version_control.word_deleted"] = "#0000FF00"
        rows, _ = word_diff_checks(style)
        self.assertTrue(any(r[0] == "Diff word visibility" and r[3] == 0 for r in rows))

    def test_word_fills_are_composited_on_solid_and_hollow_rows(self):
        style = copy.deepcopy(self.themes[-1]["style"])
        style["version_control.word_deleted"] = "#0000FF33"
        for surface in ("background", "hollow_background"):
            style[f"editor.diff_hunk.deleted.{surface}"] = "#000000"
        rows = [(name, color) for name, color in word_diff_backgrounds(style) if "word_deleted" in name]
        self.assertEqual(len(rows), 2)
        for _, color in rows:
            self.assertEqual(color, (0, 0, 0.2))

    def test_word_diff_search_text_retains_aa_without_weakening_plain_code(self):
        for theme in self.themes[1:]:
            rows = [r for r in audit(theme) if r[0] == "Editor / syntax" and "version_control.word_" in r[2]]
            self.assertEqual({r[4] for r in rows if r[2].startswith("search.")}, {4.5})
            self.assertEqual({r[4] for r in rows if not r[2].startswith("search.")}, {7})

    def test_conflict_sides_cannot_be_equal_or_almost_equal(self):
        for color in ("#00245E", "#00245F"):
            style = copy.deepcopy(self.themes[-1]["style"])
            style["version_control.conflict_marker.ours"] = "#00245E"
            style["version_control.conflict_marker.theirs"] = color
            self.assertTrue(any(r[0] == "Conflict distinction" and r[2].endswith(".theirs")
                                and r[3] < r[4] for r in interaction_checks(style)))

    def test_each_conflict_side_must_be_visible_on_the_editor(self):
        for theme in self.themes:
            for side in ("ours", "theirs"):
                style = copy.deepcopy(theme["style"])
                style[f"version_control.conflict_marker.{side}"] = style["editor.background"]
                self.assertTrue(any(r[0] == "Conflict distinction" and r[2] == "editor.background"
                                    and r[3] < r[4] for r in interaction_checks(style)))

    def test_previous_faint_list_selections_are_rejected(self):
        for theme, old_color in zip(self.themes[:2], ("#EAF1F8", "#242D43")):
            for kind in ("element", "ghost_element"):
                with self.subTest(theme=theme["name"], kind=kind):
                    style = copy.deepcopy(theme["style"])
                    style[f"{kind}.selected"] = old_color
                    self.assertTrue(any(r[0] == "List selection visibility" and r[1] == f"{kind}.selected"
                                        and r[3] < r[4] for r in interaction_checks(style)))

    def test_list_selection_must_differ_from_hover_as_well_as_the_surface(self):
        for kind in ("element", "ghost_element"):
            style = copy.deepcopy(self.themes[-1]["style"])
            style[f"{kind}.hover"] = style[f"{kind}.selected"]
            self.assertTrue(any(r[0] == "List selection visibility" and r[2] == f"{kind}.hover"
                                and r[3] < r[4] for r in interaction_checks(style)))

    def test_symbol_and_bracket_highlights_cover_normal_and_active_lines(self):
        for kind in ("read", "write", "bracket"):
            for background in ("editor.background", "editor.active_line.background"):
                style = copy.deepcopy(self.themes[-1]["style"])
                key = f"editor.document_highlight.{kind}_background"
                style[key] = style[background]
                self.assertTrue(any(r[0] == "Editor highlight visibility" and r[1:3] == (key, background)
                                    and r[3] < r[4] for r in interaction_checks(style)))

    def test_old_light_ansi_black_fails_despite_readable_default_terminal_text(self):
        theme = copy.deepcopy(self.themes[2])
        theme["style"]["terminal.ansi.black"] = "#B5BBC5"
        rows = audit(theme)
        self.assertFalse([r for r in rows if r[0] == "Terminal text" and r[3] < r[4]])
        self.assertTrue(any(r[0] == "Terminal ANSI" and r[1] == "terminal.ansi.black"
                            and r[2] == "terminal.ansi.white" and r[3] < r[4] for r in rows))

    def test_ansi_black_white_pairs_include_bright_and_dim_variants(self):
        for variant in ("", "bright_", "dim_"):
            theme = copy.deepcopy(self.themes[2])
            black = f"terminal.ansi.{variant}black"
            theme["style"][black] = "#A0A0A0"
            self.assertTrue(any(r[0] == "Terminal ANSI" and r[1] == black and r[3] < r[4]
                                for r in audit(theme)))

    def test_inverted_ansi_names_are_rejected_even_with_high_contrast(self):
        theme = copy.deepcopy(self.themes[0])
        theme["style"]["terminal.ansi.black"] = "#FFFFFF"
        theme["style"]["terminal.ansi.white"] = "#000000"
        with self.assertRaisesRegex(ValueError, "must be darker"):
            audit(theme)

    def test_unreadable_default_terminal_text_is_still_rejected(self):
        for theme in self.themes:
            bad = copy.deepcopy(theme)
            bad["style"]["terminal.foreground"] = bad["style"]["terminal.background"]
            self.assertTrue(any(r[0] == "Terminal text" and r[3] < r[4] for r in audit(bad)))


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
