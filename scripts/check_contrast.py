#!/usr/bin/env python3
"""Audit GreenTree's text contrast and common interaction states.

No dependencies. This checks theme colors, not whole-application WCAG conformance.
New color fields must be classified below instead of silently escaping the audit.
"""

import argparse
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Explicit targets prevent a light appearance or an accidental rename from
# silently weakening the Night / Midnight AAA requirement.
TEXT_CONTRAST_TARGETS = {
    "GreenTree Day Vivid": 4.5,
    "GreenTree Day AAA": 7,
    "GreenTree Night AAA": 7,
    "GreenTree Midnight AAA": 7,
}
# Vivid targets AA on normal surfaces. The original dark palettes retain AAA
# for primary text and AA for comments. Expanded interaction/Markdown text
# measurements remain visible as advisory results, not new palette requirements.
COMMENT_CAPTURES = {"comment", "comment.doc"}
TEXT_GROUPS = {
    "UI text", "Editor / syntax", "Terminal text", "Terminal ANSI", "Inverse cursor text",
    "Vim / Helix badges", "Comments",
}
UI_BACKGROUNDS = """
background surface.background elevated_surface.background
element.background element.hover element.active element.selected
element.disabled drop_target.background
ghost_element.hover ghost_element.active ghost_element.selected ghost_element.disabled
status_bar.background title_bar.background title_bar.inactive_background
toolbar.background tab_bar.background tab.inactive_background tab.active_background
panel.background panel.overlay_background panel.overlay_hover
""".split()
EDITOR_BACKGROUNDS = """
editor.background editor.gutter.background editor.subheader.background
editor.active_line.background editor.highlighted_line.background
editor.debugger_active_line.background
editor.document_highlight.read_background editor.document_highlight.write_background
editor.document_highlight.bracket_background
editor.diff_hunk.added.background editor.diff_hunk.added.hollow_background
editor.diff_hunk.deleted.background editor.diff_hunk.deleted.hollow_background
version_control.conflict_marker.ours version_control.conflict_marker.theirs
vim.yank.background
""".split()
SEARCH_BACKGROUNDS = ("search.match_background", "search.active_match_background")
WORD_DIFF_BACKGROUNDS = {
    f"version_control.word_{kind}": [f"editor.diff_hunk.{kind}.{part}" for part in ("background", "hollow_background")]
    for kind in ("added", "deleted")
}
UI_TEXT = """
text text.muted text.placeholder text.disabled text.accent link_text.hover
version_control.added version_control.deleted version_control.modified
version_control.renamed version_control.conflict version_control.ignored
""".split()
EDITOR_TEXT = """
editor.foreground editor.code_lens.foreground editor.line_number
editor.active_line_number editor.hover_line_number vim.helix_jump_label.foreground
""".split()
NON_TEXT = """
border border.variant border.focused border.selected border.disabled
drop_target.border icon icon.muted icon.disabled icon.placeholder icon.accent
debugger.accent panel.focused_border panel.indent_guide panel.indent_guide_hover
panel.indent_guide_active pane.focused_border pane_group.border
scrollbar.thumb.background scrollbar.thumb.hover_background
scrollbar.thumb.active_background scrollbar.thumb.border scrollbar.track.border
minimap.thumb.border editor.invisible editor.wrap_guide editor.active_wrap_guide
editor.indent_guide editor.indent_guide_active
editor.diff_hunk.added.hollow_border editor.diff_hunk.deleted.hollow_border
""".split()
STATUSES = """
conflict created deleted error hidden hint ignored info modified predictive
renamed success unreachable warning
""".split()
MODES = "normal insert replace visual visual_line visual_block helix_normal helix_select".split()
ANSI_COLORS = "black red green yellow blue magenta cyan white".split()
TERMINAL_TEXT = ["terminal.foreground", "terminal.bright_foreground", "terminal.dim_foreground"] + [
    f"terminal.ansi.{variant}{color}"
    for variant in ("", "bright_", "dim_") for color in ANSI_COLORS
]
TERMINAL_BACKGROUNDS = ["terminal.background", "terminal.ansi.background"]
TRANSPARENT = {
    "border.transparent", "ghost_element.background", "minimap.thumb.background",
    "minimap.thumb.hover_background", "minimap.thumb.active_background",
}
REQUIRED_SYNTAX = """
attribute boolean comment comment.doc constant constructor embedded emphasis
emphasis.strong enum function hint keyword label link_text link_uri namespace
number operator predictive preproc primary property punctuation punctuation.bracket
punctuation.delimiter punctuation.list_marker punctuation.markup punctuation.special
selector selector.pseudo string string.escape string.regex string.special
string.special.symbol tag text.literal title type variable variable.parameter
variable.special variant diff.plus diff.minus
""".split()
MARKDOWN_SELECTION = "element.selection_background"
# A project-specific visibility guard, NOT the WCAG non-text 3:1 threshold.
# Text contrast alone accepts an almost invisible selection (e.g. alpha 0x06).
MARKDOWN_SELECTION_VISIBILITY_TARGET = 1.25
MARKDOWN_BACKGROUNDS = """
background surface.background elevated_surface.background panel.background editor.background
""".split()
# Custom regression guards, NOT WCAG thresholds. Equal-luminance hues can be
# distinct while pale, nearly identical backgrounds can pass text contrast.
SEARCH_VISIBILITY_TARGET = 0.06
SEARCH_DISTINCTION_TARGET = 0.06
STATE_VISIBILITY_TARGET = 0.06
COLOR_DISTANCE_GROUPS = {
    "Search visibility", "Search state distinction", "Editor selection visibility",
    "Markdown search selection visibility", "List selection visibility",
    "Editor highlight visibility", "Diff row distinction", "Diff word visibility", "Conflict distinction",
    "Diff search visibility", "Diff search distinction",
    "Debugger row visibility", "Debugger frame visibility",
}


def read_object(pairs):
    """JSON's default duplicate-key behavior can hide a bad color override."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def rgb(color):
    if not isinstance(color, str) or not re.fullmatch(r"#[0-9a-fA-F]{6}", color):
        raise ValueError(f"Expected an opaque #RRGGBB color, got {color!r}")
    return tuple(int(color[i:i + 2], 16) / 255 for i in (1, 3, 5))


def linear_rgb(channels):
    return tuple(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels)


def luminance_rgb(channels):
    return sum(c * weight for c, weight in zip(linear_rgb(channels), (0.2126, 0.7152, 0.0722)))


def luminance(color):
    return luminance_rgb(rgb(color))


def contrast(foreground, background):
    return contrast_rgb(rgb(foreground), rgb(background))


def contrast_rgb(foreground, background):
    low, high = sorted((luminance_rgb(foreground), luminance_rgb(background)))
    return (high + 0.05) / (low + 0.05)


def oklab(channels):
    """sRGB -> Oklab; matrices from https://bottosson.github.io/posts/oklab/."""
    r, g, b = linear_rgb(channels)
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    return (
        0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
        1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
        0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s,
    )


def color_distance(first, second):
    return math.dist(oklab(first), oklab(second))


def blend(over, under, alpha):
    return tuple(top * alpha + bottom * (1 - alpha) for top, bottom in zip(over, under))


def composite(overlay, under):
    """Source-over in sRGB, retaining precision until luminance calculation."""
    if not isinstance(overlay, str) or not re.fullmatch(r"#[0-9a-fA-F]{8}", overlay):
        raise ValueError(f"Expected an explicit #RRGGBBAA overlay, got {overlay!r}")
    alpha = int(overlay[7:9], 16) / 255
    return blend(rgb(overlay[:7]), under, alpha)


def selection_color(color, background, opacity=1):
    """Zed multiplies the theme alpha by 0.5 when the editor loses focus."""
    if isinstance(color, str) and re.fullmatch(r"#[0-9a-fA-F]{8}", color):
        return blend(rgb(color[:7]), background, int(color[7:9], 16) / 255 * opacity)
    return blend(rgb(color), background, opacity)


def markdown_surfaces(style):
    surfaces = {}
    for name in MARKDOWN_BACKGROUNDS:
        background = rgb(style[name])
        surfaces[name] = background
        # Zed paints inline chips and link backgrounds below search/selection.
        for label, opacity in (("inline code", 0.08), ("link", 0.025)):
            surfaces[f"{name} / {label}"] = blend(rgb(style["editor.foreground"]), background, opacity)
    for capture, highlight in style["syntax"].items():
        name = f"syntax.{capture}.background_color" if "background_color" in highlight else "editor.background"
        surfaces[f"{name} / code block"] = rgb(highlight.get("background_color", style["editor.background"]))
    return list(surfaces.items())


def search_highlight_checks(style):
    """Check ordinary/active matches and the editor's selection over a match.

    Zed v1.23.2: editor/src/items.rs selects the two search colors;
    editor/src/element.rs paints the player selection over the match, at 50%
    of its theme alpha while search has focus, and its full alpha with editor focus.
    """
    surfaces = markdown_surfaces(style) + [(name, rgb(style[name])) for name in
                                         ("editor.active_line.background", "editor.highlighted_line.background")]
    selection = style["players"][0]["selection"]
    editor_background = rgb(style["editor.background"])
    results = [("Editor selection visibility", "players[0].selection", "editor.background",
                color_distance(selection_color(selection, editor_background), editor_background),
                SEARCH_VISIBILITY_TARGET)]
    for surface_name, surface in surfaces:
        ordinary, active = [selection_color(style[key], surface) for key in SEARCH_BACKGROUNDS]
        for key, color in zip(SEARCH_BACKGROUNDS, (ordinary, active)):
            results.append(("Search visibility", key, surface_name,
                            color_distance(color, surface), SEARCH_VISIBILITY_TARGET))
        for name, color in (
            ("active match", active),
            ("active match / search focused", selection_color(selection, active, 0.5)),
            ("active match / editor focused", selection_color(selection, active)),
        ):
            results.append(("Search state distinction", name, f"ordinary match / {surface_name}",
                            color_distance(color, ordinary), SEARCH_DISTINCTION_TARGET))
            results.append(("Search visibility", name, surface_name,
                            color_distance(color, surface), SEARCH_VISIBILITY_TARGET))
            # A distinct hue can still disappear on a dark editor surface.
            if surface_name in ("editor.background", "editor.active_line.background") and luminance_rgb(surface) < 0.1:
                results.append(("Active search visibility", name, surface_name,
                                contrast_rgb(color, surface), 1.25))
    return results


def markdown_selection_checks(style):
    # Keep selections visible on each rendered surface. audit() separately
    # checks text against the composited fill beneath glyphs in Zed 1.25.2.
    overlay = style[MARKDOWN_SELECTION]
    composite(overlay, rgb(style["editor.background"]))  # Validate RGBA first.
    if not 0 < int(overlay[7:9], 16) < 255:
        raise ValueError(f"{MARKDOWN_SELECTION} must be visible and translucent")
    results = []
    def check(background_name, background, search_match=False):
        selected_background = composite(overlay, background)
        if search_match:
            results.append(("Markdown search selection visibility", MARKDOWN_SELECTION, background_name,
                            color_distance(background, selected_background), SEARCH_VISIBILITY_TARGET))
        else:
            results.append(("Markdown selection visibility", MARKDOWN_SELECTION, background_name,
                            contrast_rgb(background, selected_background), MARKDOWN_SELECTION_VISIBILITY_TARGET))

    for name, background in markdown_surfaces(style):
        check(name, background)
        for key in SEARCH_BACKGROUNDS:
            check(f"{key} / {name}", selection_color(style[key], background), search_match=True)
    return results


def interaction_checks(style):
    """Compare actual neighboring states, not only text against each fill."""
    pairs = []
    for kind in ("element", "ghost_element"):
        for background in ("background", "surface.background", "elevated_surface.background",
                           "panel.background", "element.background", f"{kind}.hover"):
            pairs.append(("List selection visibility", f"{kind}.selected", background))
    for kind in ("read", "write", "bracket"):
        for background in ("editor.background", "editor.active_line.background"):
            pairs.append(("Editor highlight visibility", f"editor.document_highlight.{kind}_background", background))
    for background in ("editor.background", "editor.active_line.background"):
        pairs.append(("Debugger row visibility", "editor.debugger_active_line.background", background))
    # Zed 1.24.2 paints both selected and hovered stack frames with element.hover.
    pairs.append(("Debugger frame visibility", "element.hover", "panel.background"))
    for surface in ("background", "hollow_background"):
        pairs.append(("Diff row distinction", f"editor.diff_hunk.added.{surface}",
                      f"editor.diff_hunk.deleted.{surface}"))
    for side in ("ours", "theirs"):
        pairs.append(("Conflict distinction", f"version_control.conflict_marker.{side}", "editor.background"))
    pairs.append(("Conflict distinction", "version_control.conflict_marker.ours", "version_control.conflict_marker.theirs"))
    return [(group, first, second, color_distance(rgb(style[first]), rgb(style[second])), STATE_VISIBILITY_TARGET)
            for group, first, second in pairs]


def word_diff_backgrounds(style):
    return [(f"{word} / {surface}", selection_color(style[word], rgb(style[surface])))
            for word, surfaces in WORD_DIFF_BACKGROUNDS.items() for surface in surfaces]


def word_diff_checks(style):
    # Zed appends word highlights after search, then paints player selections.
    # Audit that order; an opaque word fill erases both search states.
    results = []
    search_backgrounds = []
    for word, surfaces in WORD_DIFF_BACKGROUNDS.items():
        for surface in surfaces:
            base = rgb(style[surface])
            ordinary, active = [selection_color(style[word], selection_color(style[key], base))
                                for key in SEARCH_BACKGROUNDS]
            states = [("ordinary", ordinary), ("active", active)] + [
                (f"active / {focus} / players[0].selection", selection_color(style["players"][0]["selection"], active, opacity))
                for focus, opacity in (("search focused", 0.5), ("editor focused", 1))
            ]
            search_backgrounds.extend((f"search.{state} / {word} / {surface}", color) for state, color in states)
            for state, color in states[1:]:
                results.append(("Diff search distinction", f"{word} / {state}", f"{surface} / ordinary",
                                color_distance(color, ordinary), SEARCH_DISTINCTION_TARGET))
            plain = selection_color(style[word], base)
            results.append(("Diff word visibility", word, surface, color_distance(plain, base), STATE_VISIBILITY_TARGET))
            for state, color in states:
                results.append(("Diff search visibility", f"{word} / {state}", surface,
                                color_distance(color, plain), SEARCH_VISIBILITY_TARGET))
    return results, search_backgrounds


def audit(theme):
    style = theme["style"]
    text_threshold = text_contrast_target(theme["name"])
    if theme["appearance"] not in ("dark", "light") or style["background.appearance"] != "opaque":
        raise ValueError("This audit requires a light or dark theme with an opaque window background")

    status_backgrounds = [f"{name}.background" for name in STATUSES]
    status_borders = [f"{name}.border" for name in STATUSES]
    mode_colors = [f"vim.{mode}.{part}" for mode in MODES for part in ("foreground", "background")]
    expected = set(
        UI_BACKGROUNDS + EDITOR_BACKGROUNDS + UI_TEXT + EDITOR_TEXT + NON_TEXT
        + STATUSES + status_backgrounds + status_borders + mode_colors
        + TERMINAL_TEXT + TERMINAL_BACKGROUNDS + ["scrollbar.track.background"]
    )
    required = expected | TRANSPARENT | set(WORD_DIFF_BACKGROUNDS) | set(SEARCH_BACKGROUNDS) | {
        "background.appearance", "players", "syntax", "accents", MARKDOWN_SELECTION,
    }
    if required != set(style):
        raise ValueError(f"Missing fields: {sorted(required - set(style))}; unclassified fields: {sorted(set(style) - required)}")
    for key in expected:
        luminance(style[key])
    for key in TRANSPARENT:
        if style[key] != "#00000000":
            raise ValueError(f"{key} must remain a transparent placeholder")

    syntax = style["syntax"]
    missing = set(REQUIRED_SYNTAX) - set(syntax)
    if missing:
        raise ValueError(f"Missing syntax captures: {sorted(missing)}")
    if len(style["players"]) < 2 or not style["accents"]:
        raise ValueError("Provide local/remote player colors and at least one accent")

    results = []
    def check(group, foregrounds, backgrounds, threshold):
        for foreground_name, foreground in foregrounds:
            for background_name, background in backgrounds:
                target = threshold
                if group in TEXT_GROUPS and (".selection" in background_name or background_name.startswith("search.")):
                    target = min(target, 4.5)
                # Brighter Git highlights keep primary text at AAA and colored
                # syntax/status text at AA, as documented in the palette targets.
                if (group in {"UI text", "Editor / syntax", "Comments"}
                        and (background_name.startswith("version_control.word_")
                             or background_name.startswith("editor.diff_hunk."))
                        and foreground_name not in {"text", "editor.foreground"}):
                    target = min(target, 4.5)
                ratio = contrast_rgb(foreground, background)
                results.append((group, foreground_name, background_name, ratio, target))

    def fields(names):
        return [(name, rgb(style[name])) for name in names]

    ui_backgrounds = fields(UI_BACKGROUNDS + status_backgrounds)
    word_backgrounds = word_diff_backgrounds(style)
    word_results, word_search_backgrounds = word_diff_checks(style)
    search_backgrounds = [(f"{key} / {name}", selection_color(style[key], color))
                          for key in SEARCH_BACKGROUNDS for name, color in fields(EDITOR_BACKGROUNDS)]
    editor_backgrounds = fields(EDITOR_BACKGROUNDS) + word_backgrounds + search_backgrounds + word_search_backgrounds
    # Markdown previews share the search colors but have their own selection
    # overlay. Audit the text on that final fill, including selection over search.
    for name, background in markdown_surfaces(style):
        editor_backgrounds.append((f"markdown / {name}", background))
        editor_backgrounds.append((f"{MARKDOWN_SELECTION} / {name}",
                                   selection_color(style[MARKDOWN_SELECTION], background)))
        for key in SEARCH_BACKGROUNDS:
            searched = selection_color(style[key], background)
            editor_backgrounds.append((f"{key} / markdown / {name}", searched))
            editor_backgrounds.append((f"{key} / {MARKDOWN_SELECTION} / {name}",
                                       selection_color(style[MARKDOWN_SELECTION], searched)))
    for index, player in enumerate(style["players"]):
        if set(player) != {"cursor", "background", "selection"}:
            raise ValueError(f"Incomplete player colors at index {index}")
        luminance(player["cursor"])
        ui_backgrounds.append((f"players[{index}].background", rgb(player["background"])))
        if len(player["selection"]) == 9:
            for name, background in fields(EDITOR_BACKGROUNDS) + word_backgrounds + search_backgrounds:
                label = f"{name} / players[{index}].selection"
                editor_backgrounds.append((label, selection_color(player["selection"], background)))
                if name.startswith("search.active_match_background"):
                    editor_backgrounds.append((f"{label} / search focused", selection_color(player["selection"], background, 0.5)))
        else:
            editor_backgrounds.append((f"players[{index}].selection", rgb(player["selection"])))

    syntax_text = []
    comment_text = []
    for capture, highlight in syntax.items():
        if set(highlight) - {"color", "background_color", "font_style", "font_weight"}:
            raise ValueError(f"Unsupported syntax properties: {capture}")
        luminance(highlight["color"])
        if highlight.get("font_style", "normal") not in ("normal", "italic", "oblique"):
            raise ValueError(f"Invalid font style: {capture}")
        if highlight.get("font_weight", 400) not in range(100, 1000, 100):
            raise ValueError(f"Invalid font weight: {capture}")
        target_list = comment_text if capture in COMMENT_CAPTURES else syntax_text
        target_list.append((f"syntax.{capture}", rgb(highlight["color"])))
        if "background_color" in highlight:
            editor_backgrounds.append((f"syntax.{capture}.background_color", rgb(highlight["background_color"])))
            for index, player in enumerate(style["players"]):
                if len(player["selection"]) == 9:
                    editor_backgrounds.append((f"syntax.{capture}.background_color / players[{index}].selection",
                                               selection_color(player["selection"], rgb(highlight["background_color"]))))

    # Transparent player selections are composited over the actual surface.
    # Transparent placeholders and minimap fills reveal the base; the
    # minimap's visible boundary is audited through minimap.thumb.border.
    all_backgrounds = ui_backgrounds + editor_backgrounds + fields(TERMINAL_BACKGROUNDS)
    accents = [(f"accents[{i}]", rgb(color)) for i, color in enumerate(style["accents"])]
    check("UI text", fields(UI_TEXT + STATUSES) + accents, all_backgrounds, text_threshold)
    check("Editor / syntax", fields(EDITOR_TEXT) + syntax_text, all_backgrounds, text_threshold)
    check("Comments", comment_text, all_backgrounds, 4.5)
    terminal_backgrounds = fields(TERMINAL_BACKGROUNDS) + [
        (f"{name} / players[0].selection", selection_color(style["players"][0]["selection"], color))
        for name, color in fields(TERMINAL_BACKGROUNDS)
    ]
    check("Terminal text", fields(TERMINAL_TEXT[:3]), terminal_backgrounds, text_threshold)
    # ANSI names can be foregrounds OR backgrounds. Do not turn black into
    # white (or white into black) just to pass the default-background check.
    low_contrast_name = "black" if theme["appearance"] == "dark" else "white"
    ansi_on_default = [key for key in TERMINAL_TEXT[3:] if not key.endswith(low_contrast_name)]
    check("Terminal ANSI", fields(ansi_on_default), terminal_backgrounds, text_threshold)
    for variant in ("", "bright_", "dim_"):
        black, white = (f"terminal.ansi.{variant}{name}" for name in ("black", "white"))
        if luminance(style[black]) >= luminance(style[white]):
            raise ValueError(f"{black} must be darker than {white}")
        check("Terminal ANSI", fields([black]), fields([white]), 4.5)
    # Search, word diffs and selections cover glyphs, not UI borders or icons.
    indicator_backgrounds = [(name, color) for name, color in all_backgrounds
                             if not name.startswith(("search.", "version_control.word_"))
                             and ".selection" not in name]
    check("UI indicators", fields(NON_TEXT + status_borders), indicator_backgrounds, 3)
    check("Scrollbar", fields(["scrollbar.thumb.background", "scrollbar.thumb.hover_background",
          "scrollbar.thumb.active_background"]), fields(["scrollbar.track.background"]), 3)
    # Rendered Markdown previews have text selections but no editor caret.
    cursor_backgrounds = [(name, color) for name, color in all_backgrounds
                          if not name.startswith("markdown / ")
                          and " / markdown / " not in name
                          and MARKDOWN_SELECTION not in name]
    for index, player in enumerate(style["players"]):
        check("Cursors", [(f"players[{index}].cursor", rgb(player["cursor"]))], cursor_backgrounds, 3)
        # Zed uses editor.background for text inside block cursors and cursor
        # name labels, with the player's cursor color as the background.
        check("Inverse cursor text", fields(["editor.background"]),
              [(f"players[{index}].cursor", rgb(player["cursor"]))], text_threshold)
    for mode in MODES:
        check("Vim / Helix badges", fields([f"vim.{mode}.foreground"]), fields([f"vim.{mode}.background"]), text_threshold)
    results.extend(markdown_selection_checks(style))
    results.extend(search_highlight_checks(style))
    results.extend(interaction_checks(style))
    results.extend(word_results)
    return results


def advisory_text_check(theme, row):
    """Retain expanded measurements without recoloring restored palettes.

    Search/selection text and rendered Markdown surfaces were outside the
    original enforced scope. Report their deficits honestly while preserving
    the user's requested palettes and the baseline normal-surface requirements.
    """
    return (theme["name"] in TEXT_CONTRAST_TARGETS and row[0] in TEXT_GROUPS
            and (".selection" in row[2] or row[2].startswith(("search.", "markdown / "))))


def text_contrast_target(name):
    if name not in TEXT_CONTRAST_TARGETS:
        raise ValueError(f"No explicit text contrast target for theme: {name!r}")
    return TEXT_CONTRAST_TARGETS[name]


def measurement(group, value):
    return f"{value:.4f} ΔEOK" if group in COLOR_DISTANCE_GROUPS else f"{value:.4f}:1"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("theme", nargs="?", type=Path, default=ROOT / "themes/green-tree.json")
    parser.add_argument("--report", type=Path, help="Write a Markdown report, including every failed pair")
    args = parser.parse_args()
    try:
        family = json.loads(args.theme.read_text(), object_pairs_hook=read_object)
        if not family["name"] or not family["author"] or not family["themes"]:
            raise ValueError("Theme family metadata and themes must not be empty")
        sections = ["# GreenTree · Contrast audit", "",
                    "Day Vivid targets AA 4.5:1 on normal surfaces. The three dark variants match their session-start palettes: primary text targets AAA 7:1 and comments AA 4.5:1. Dark Git highlights retain 7:1 for primary text and 4.5:1 for colored text. Expanded search/selection and rendered-Markdown text measurements are advisory: below-target pairs are marked REVIEW, not claimed as passing their contrast targets.",
                    "UI indicators use 3:1 on their surfaces. Selection checks cover both text readability and background visibility, including search overlap in source, Markdown previews and terminal selections.",
                    "Visibility guards are custom: 0.06 Oklab distance (ΔEOK) for search, selection, symbols, added/deleted rows, changed words and conflict sides; 1.25:1 luminance for Markdown selections and active search on dark editor surfaces. They are not WCAG criteria or proof of visual acceptance.",
                    "ANSI black/white retain their terminal roles: paired normal, bright and dim colors target 4.5:1; black on a dark default surface and white on a light one are exempt. Other program-chosen combinations need an in-app check.",
                    "Pass/fail uses unrounded values. See [checks, sources and limits](theme-testing.md).", "",
                    "Reproduce: `python3 scripts/check_contrast.py --report docs/contrast-report.md`.", ""]
        names = [theme["name"] for theme in family["themes"]]
        if len(names) != len(set(names)):
            raise ValueError("Theme names must be unique")
        failed = []
        for theme in family["themes"]:
            print(f"\n{theme['name']}")
            results = audit(theme)
            failed.extend((theme["name"], *row) for row in results
                          if row[3] < row[4] and not advisory_text_check(theme, row))
            sections += [f"## {theme['name']}", "", f"Checked pairs: {len(results)}.", "",
                         "| Scope | Pairs | Minimum | Target | Result |",
                         "| --- | ---: | ---: | ---: | --- |"]
            for group in dict.fromkeys(row[0] for row in results):
                rows = [row for row in results if row[0] == group]
                worst = min(rows, key=lambda row: row[3])
                below_target = [row for row in rows if row[3] < row[4]]
                failures = [row for row in below_target if not advisory_text_check(theme, row)]
                result = "FAIL" if failures else f"REVIEW ({len(below_target)} advisory)" if below_target else "PASS"
                unit = " ΔEOK" if group in COLOR_DISTANCE_GROUPS else ":1"
                targets = " / ".join(f"{value:g}{unit}" for value in sorted({row[4] for row in rows}))
                if group in COLOR_DISTANCE_GROUPS | {"Markdown selection visibility", "Active search visibility"}:
                    result += " (custom)"
                sections.append(f"| {group} | {len(rows)} | {measurement(group, worst[3])} | {targets} | {result} |")
                print(f"{result:4} {group:22} {len(rows):5} pairs; min {measurement(group, worst[3])} ({worst[1]} / {worst[2]})")
            sections += ["", "Lowest text contrast pair:", ""]
            worst_text = min((row for row in results if row[0] in TEXT_GROUPS), key=lambda row: row[3])
            sections += [f"`{worst_text[1]}` / `{worst_text[2]}`: {worst_text[3]:.4f}:1.", ""]
        if failed:
            sections += ["## Failed pairs", ""]
            for name, group, foreground, background, ratio, threshold in failed:
                message = f"{name} / {group}: {foreground} / {background} = {measurement(group, ratio)} < {measurement(group, threshold)}"
                print(message, file=sys.stderr)
                sections.append(f"- {message}")
        sections += ["", "This audit covers explicit palette colors and modeled selections. Runtime fading, user overrides, terminal program colors and Zed's rendering behavior require in-app checks.", ""]
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text("\n".join(sections))
        return 1 if failed else 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Contrast audit failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
