#!/usr/bin/env python3
"""Audit GreenTree's color pairs and Markdown selections using WCAG luminance.

No dependencies. This checks theme colors, not whole-application WCAG conformance.
New color fields must be classified below instead of silently escaping the audit.
"""

import argparse
import json
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
# Vivid deliberately prioritizes a bright green on warm white. Only these
# green syntax captures use a custom floor; 2.5:1 is NOT a WCAG text target.
# Keep other Vivid text at 4.5:1. Dark variants retain 7:1 for primary text;
# dimmed comments and Markdown selections intentionally use AA's 4.5:1.
VIVID_GREEN_CAPTURES = {
    "keyword", "preproc", "punctuation.markup", "tag", "title", "diff.plus",
}
COMMENT_CAPTURES = {"comment", "comment.doc"}
TEXT_GROUPS = {
    "UI text", "Editor / syntax", "Terminal text", "Inverse cursor text",
    "Vim / Helix badges", "Comments", "Markdown selection",
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
search.match_background search.active_match_background
version_control.word_added version_control.word_deleted
version_control.conflict_marker.ours version_control.conflict_marker.theirs
vim.yank.background
""".split()
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


def luminance_rgb(channels):
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def luminance(color):
    return luminance_rgb(rgb(color))


def contrast(foreground, background):
    low, high = sorted((luminance(foreground), luminance(background)))
    return (high + 0.05) / (low + 0.05)


def blend(over, under, alpha):
    return tuple(top * alpha + bottom * (1 - alpha) for top, bottom in zip(over, under))


def composite(overlay, under):
    """Source-over in sRGB, retaining precision until luminance calculation."""
    if not isinstance(overlay, str) or not re.fullmatch(r"#[0-9a-fA-F]{8}", overlay):
        raise ValueError(f"Expected an explicit #RRGGBBAA overlay, got {overlay!r}")
    alpha = int(overlay[7:9], 16) / 255
    return blend(rgb(overlay[:7]), under, alpha)


def markdown_selection_checks(style, text_threshold):
    # Zed paints Markdown selections AFTER glyphs. Auditing the foreground
    # against the selection color alone misses complete occlusion at alpha=1.
    # https://github.com/zed-industries/zed/pull/32388
    overlay = style[MARKDOWN_SELECTION]
    composite(overlay, rgb(style["editor.background"]))  # Validate RGBA first.
    if not 0 < int(overlay[7:9], 16) < 255:
        raise ValueError(f"{MARKDOWN_SELECTION} must be visible and translucent")
    results = []
    checked_backgrounds = set()

    def check(foreground_name, foreground, background_name, background):
        selected_background = composite(overlay, background)
        low, high = sorted((luminance_rgb(composite(overlay, rgb(foreground))),
                            luminance_rgb(selected_background)))
        results.append(("Markdown selection", foreground_name, background_name,
                        (high + 0.05) / (low + 0.05), text_threshold))
        if background_name not in checked_backgrounds:
            checked_backgrounds.add(background_name)
            low, high = sorted((luminance_rgb(background), luminance_rgb(selected_background)))
            results.append(("Markdown selection visibility", MARKDOWN_SELECTION, background_name,
                            (high + 0.05) / (low + 0.05), MARKDOWN_SELECTION_VISIBILITY_TARGET))

    for background_name in MARKDOWN_BACKGROUNDS:
        background = rgb(style[background_name])
        for foreground_name in ("text", "text.muted", "text.accent"):
            check(foreground_name, style[foreground_name], background_name, background)
        # Zed gives inline code an editor.foreground overlay at 8% opacity,
        # and links at 2.5%. Both are painted below the selection overlay.
        for foreground_name, opacity, label in (("text", 0.08, "inline code"),
                                                ("text.accent", 0.025, "link")):
            check(foreground_name, style[foreground_name], f"{background_name} / {label}",
                  blend(rgb(style["editor.foreground"]), background, opacity))
    for capture, highlight in style["syntax"].items():
        background = highlight.get("background_color", style["editor.background"])
        background_name = f"syntax.{capture}.background_color" if "background_color" in highlight else "editor.background"
        check(f"syntax.{capture}", highlight["color"], f"{background_name} / code block", rgb(background))
    return results


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
    required = expected | TRANSPARENT | {"background.appearance", "players", "syntax", "accents", MARKDOWN_SELECTION}
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
    vivid_foregrounds = (
        {f"syntax.{capture}" for capture in VIVID_GREEN_CAPTURES}
        if theme["name"] == "GreenTree Day Vivid" else set()
    )

    def check(group, foregrounds, backgrounds, threshold):
        for foreground_name, foreground in foregrounds:
            target = 2.5 if foreground_name in vivid_foregrounds else threshold
            for background_name, background in backgrounds:
                ratio = contrast(foreground, background)
                results.append((group, foreground_name, background_name, ratio, target))

    def fields(names):
        return [(name, style[name]) for name in names]

    ui_backgrounds = fields(UI_BACKGROUNDS + status_backgrounds)
    editor_backgrounds = fields(EDITOR_BACKGROUNDS)
    for index, player in enumerate(style["players"]):
        if set(player) != {"cursor", "background", "selection"}:
            raise ValueError(f"Incomplete player colors at index {index}")
        for key, value in player.items():
            luminance(value)
        editor_backgrounds.append((f"players[{index}].selection", player["selection"]))
        ui_backgrounds.append((f"players[{index}].background", player["background"]))

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
        target_list.append((f"syntax.{capture}", highlight["color"]))
        if "background_color" in highlight:
            editor_backgrounds.append((f"syntax.{capture}.background_color", highlight["background_color"]))

    # All backgrounds are opaque; stacked highlights resolve to one of these
    # surfaces. Transparent placeholders and minimap fills reveal the base; the
    # minimap's visible boundary is audited through minimap.thumb.border.
    all_backgrounds = ui_backgrounds + editor_backgrounds + fields(TERMINAL_BACKGROUNDS)
    accents = [(f"accents[{i}]", color) for i, color in enumerate(style["accents"])]
    check("UI text", fields(UI_TEXT + STATUSES) + accents, all_backgrounds, text_threshold)
    check("Editor / syntax", fields(EDITOR_TEXT) + syntax_text, all_backgrounds, text_threshold)
    check("Comments", comment_text, all_backgrounds, 4.5)
    # Terminal selections use player colors. ANSI backgrounds chosen by programs
    # and indexed/true-color output are outside the default-background guarantee.
    terminal_backgrounds = fields(TERMINAL_BACKGROUNDS) + [
        (f"players[{i}].selection", p["selection"]) for i, p in enumerate(style["players"])
    ]
    check("Terminal text", fields(TERMINAL_TEXT), terminal_backgrounds, text_threshold)
    check("UI indicators", fields(NON_TEXT + status_borders), all_backgrounds, 3)
    check("Scrollbar", fields(["scrollbar.thumb.background", "scrollbar.thumb.hover_background",
          "scrollbar.thumb.active_background"]), fields(["scrollbar.track.background"]), 3)
    for index, player in enumerate(style["players"]):
        check("Cursors", [(f"players[{index}].cursor", player["cursor"])], all_backgrounds, 3)
        # Zed uses editor.background for text inside block cursors and cursor
        # name labels, with the player's cursor color as the background.
        check("Inverse cursor text", fields(["editor.background"]),
              [(f"players[{index}].cursor", player["cursor"])], text_threshold)
    for mode in MODES:
        check("Vim / Helix badges", fields([f"vim.{mode}.foreground"]), fields([f"vim.{mode}.background"]), text_threshold)
    # Selected Markdown is deliberately AA so its highlight can be visible.
    # Day Vivid retains the custom 2.5:1 floor used by its bright green syntax.
    results.extend(markdown_selection_checks(style, 2.5 if theme["name"] == "GreenTree Day Vivid" else 4.5))
    return results


def text_contrast_target(name):
    if name not in TEXT_CONTRAST_TARGETS:
        raise ValueError(f"No explicit text contrast target for theme: {name!r}")
    return TEXT_CONTRAST_TARGETS[name]


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
                    "Uses the WCAG 2.x sRGB relative luminance formula. Day Vivid's green syntax has a custom 2.5:1 floor and does not meet AA text contrast.",
                    "Other base-palette Day Vivid text is checked at 4.5:1. Day AAA, Night and Midnight primary text is checked at 7:1; comments use 4.5:1.",
                    "Markdown selections are composited over both glyphs and backgrounds: dark variants use AA 4.5:1; Day Vivid uses a custom 2.5:1 floor (not AA).",
                    "Selected/unselected Markdown backgrounds must differ by a custom 1.25:1 luminance ratio. This visibility guard is not a WCAG criterion or a substitute for visual review.",
                    "Key non-text indicators are checked at 3:1. Unknown theme names are rejected, not given a weaker target.",
                    "Pass/fail uses unrounded ratios; tables display four decimal places.", "",
                    "Reproduce: `python3 scripts/check_contrast.py --report docs/contrast-report.md`.", ""]
        names = [theme["name"] for theme in family["themes"]]
        if len(names) != len(set(names)):
            raise ValueError("Theme names must be unique")
        failed = []
        for theme in family["themes"]:
            print(f"\n{theme['name']}")
            results = audit(theme)
            failed.extend((theme["name"], *row) for row in results if row[3] < row[4])
            sections += [f"## {theme['name']}", "", f"Checked pairs: {len(results)}.", "",
                         "| Scope | Pairs | Minimum contrast | Target | Result |",
                         "| --- | ---: | ---: | ---: | --- |"]
            for group in dict.fromkeys(row[0] for row in results):
                rows = [row for row in results if row[0] == group]
                worst = min(rows, key=lambda row: row[3])
                result = "PASS" if all(row[3] >= row[4] for row in rows) else "FAIL"
                targets = " / ".join(f"{value:g}:1" for value in sorted({row[4] for row in rows}))
                if group == "Markdown selection visibility" or (theme["name"] == "GreenTree Day Vivid" and group in ("Editor / syntax", "Markdown selection")):
                    result += " (custom)"
                sections.append(f"| {group} | {len(rows)} | {worst[3]:.4f}:1 | {targets} | {result} |")
                print(f"{result:4} {group:22} {len(rows):5} pairs; min {worst[3]:.4f}:1 ({worst[1]} / {worst[2]})")
            sections += ["", "Lowest text contrast pair:", ""]
            worst_text = min((row for row in results if row[0] in TEXT_GROUPS), key=lambda row: row[3])
            sections += [f"`{worst_text[1]}` / `{worst_text[2]}`: {worst_text[3]:.4f}:1.", ""]
        if failed:
            sections += ["## Failed pairs", ""]
            for name, group, foreground, background, ratio, threshold in failed:
                message = f"{name} / {group}: {foreground} / {background} = {ratio:.4f}:1 < {threshold}:1"
                print(message, file=sys.stderr)
                sections.append(f"- {message}")
        sections += ["", "## Scope", "",
                     "Checks explicit UI text, syntax including comments, line numbers, status text, default ANSI terminal foregrounds,",
                     "cursors and borders against selection, search, diff, bracket-match and popup backgrounds. Transparent placeholder borders are excluded.", "",
                     "Markdown selection checks cover prose, links, inline code and syntax-highlighted code blocks, including the overlay on the glyphs themselves.",
                     "They model the sRGB source-over blend used by Zed; fully opaque and invisible selection overlays are rejected.", "",
                     "The AAA theme names describe the primary-text target, not every state: comments and selected Markdown intentionally target AA 4.5:1.",
                     "Markdown selection visibility uses a custom 1.25:1 floor, not the WCAG 3:1 non-text target. Editor selection/background separation is not checked.", "",
                     "This is a palette audit, not WCAG certification of Zed. It does not verify focus area, keyboard or screen-reader behavior,",
                     "language-server fading, plugin colors, or terminal application backgrounds, 256 colors and true color.",
                     "Runtime color/opacity adjustments and user overrides require evaluation of the actual rendered result.", "",
                     "References: [WCAG AAA text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html),",
                     "[non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).", ""]
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text("\n".join(sections))
        return 1 if failed else 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Contrast audit failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
