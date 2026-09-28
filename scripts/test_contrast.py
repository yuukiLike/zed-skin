"""Regression coverage for Markdown selections painted on top of text.

Run: python3 -m unittest discover -s scripts -p 'test_*.py'
"""

import copy
import json
import unittest

from check_contrast import (
    MARKDOWN_SELECTION, ROOT, audit, composite, markdown_selection_checks, rgb,
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
                for group in ("Comments", "Markdown selection"):
                    self.assertEqual({row[4] for row in rows if row[0] == group}, {4.5})
                for group in ("Editor / syntax", "UI text", "Terminal text"):
                    self.assertEqual({row[4] for row in rows if row[0] == group}, {7})

    def test_opaque_or_invisible_selections_are_rejected(self):
        style = copy.deepcopy(self.themes[-1]["style"])
        for color in ("#0C1A2D", "#0C1A2DFF", "#0C1A2D00"):
            with self.subTest(color=color):
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


if __name__ == "__main__":
    unittest.main()
