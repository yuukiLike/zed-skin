#!/usr/bin/env python3
"""Audit GreenTree's explicit, opaque color pairs using WCAG relative luminance.

No dependencies. This checks theme colors, not whole-application WCAG conformance.
New color fields must be classified below instead of silently escaping the audit.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UI_BACKGROUNDS = """
background surface.background elevated_surface.background
element.background element.hover element.active element.selected
element.selection_background element.disabled drop_target.background
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


def read_object(pairs):
    """JSON's default duplicate-key behavior can hide a bad color override."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def luminance(color):
    if not isinstance(color, str) or not re.fullmatch(r"#[0-9a-fA-F]{6}", color):
        raise ValueError(f"Expected an opaque #RRGGBB color, got {color!r}")
    channels = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(foreground, background):
    low, high = sorted((luminance(foreground), luminance(background)))
    return (high + 0.05) / (low + 0.05)


def audit(theme):
    style = theme["style"]
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
    required = expected | TRANSPARENT | {"background.appearance", "players", "syntax", "accents"}
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
                ratio = contrast(foreground, background)
                results.append((group, foreground_name, background_name, ratio, threshold))

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
    for capture, highlight in syntax.items():
        if set(highlight) - {"color", "background_color", "font_style", "font_weight"}:
            raise ValueError(f"Unsupported syntax properties: {capture}")
        luminance(highlight["color"])
        if highlight.get("font_style", "normal") not in ("normal", "italic", "oblique"):
            raise ValueError(f"Invalid font style: {capture}")
        if highlight.get("font_weight", 400) not in range(100, 1000, 100):
            raise ValueError(f"Invalid font weight: {capture}")
        syntax_text.append((f"syntax.{capture}", highlight["color"]))
        if "background_color" in highlight:
            editor_backgrounds.append((f"syntax.{capture}.background_color", highlight["background_color"]))

    # All backgrounds are opaque; stacked highlights resolve to one of these
    # surfaces. Transparent placeholders and minimap fills reveal the base; the
    # minimap's visible boundary is audited through minimap.thumb.border.
    all_backgrounds = ui_backgrounds + editor_backgrounds + fields(TERMINAL_BACKGROUNDS)
    accents = [(f"accents[{i}]", color) for i, color in enumerate(style["accents"])]
    check("UI text", fields(UI_TEXT + STATUSES) + accents, all_backgrounds, 7)
    check("Editor / syntax", fields(EDITOR_TEXT) + syntax_text, all_backgrounds, 7)
    # Terminal selections use player colors. ANSI backgrounds chosen by programs
    # and indexed/true-color output are outside the default-background guarantee.
    terminal_backgrounds = fields(TERMINAL_BACKGROUNDS) + [
        (f"players[{i}].selection", p["selection"]) for i, p in enumerate(style["players"])
    ]
    check("Terminal text", fields(TERMINAL_TEXT), terminal_backgrounds, 7)
    check("UI indicators", fields(NON_TEXT + status_borders), all_backgrounds, 3)
    check("Scrollbar", fields(["scrollbar.thumb.background", "scrollbar.thumb.hover_background",
          "scrollbar.thumb.active_background"]), fields(["scrollbar.track.background"]), 3)
    for index, player in enumerate(style["players"]):
        check("Cursors", [(f"players[{index}].cursor", player["cursor"])], all_backgrounds, 3)
        # Zed uses editor.background for text inside block cursors and cursor
        # name labels, with the player's cursor color as the background.
        check("Inverse cursor text", fields(["editor.background"]),
              [(f"players[{index}].cursor", player["cursor"])], 7)
    for mode in MODES:
        check("Vim / Helix badges", fields([f"vim.{mode}.foreground"]), fields([f"vim.{mode}.background"]), 7)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("theme", nargs="?", type=Path, default=ROOT / "themes/green-tree-contrast.json")
    parser.add_argument("--report", type=Path, help="Write a Markdown report, including every failed pair")
    args = parser.parse_args()
    try:
        family = json.loads(args.theme.read_text(), object_pairs_hook=read_object)
        if not family["name"] or not family["author"] or not family["themes"]:
            raise ValueError("Theme family metadata and themes must not be empty")
        sections = ["# GreenTree Contrast · 对比度检查", "",
                    "使用 WCAG 2.x sRGB 相对亮度公式；普通文字 ≥ 7:1，关键非文字标识 ≥ 3:1。",
                    "判定使用未舍入数值，下表仅为显示而保留四位小数。", ""]
        names = [theme["name"] for theme in family["themes"]]
        if len(names) != len(set(names)):
            raise ValueError("Theme names must be unique")
        failed = []
        for theme in family["themes"]:
            print(f"\n{theme['name']}")
            results = audit(theme)
            failed.extend((theme["name"], *row) for row in results if row[3] < row[4])
            sections += [f"## {theme['name']}", "", f"检查组合数：{len(results)}。", "",
                         "| 检查范围 | 组合数 | 最低对比度 | 要求 | 结果 |",
                         "| --- | ---: | ---: | ---: | --- |"]
            for group in dict.fromkeys(row[0] for row in results):
                rows = [row for row in results if row[0] == group]
                worst = min(rows, key=lambda row: row[3])
                result = "PASS" if all(row[3] >= row[4] for row in rows) else "FAIL"
                sections.append(f"| {group} | {len(rows)} | {worst[3]:.4f}:1 | {worst[4]}:1 | {result} |")
                print(f"{result:4} {group:22} {len(rows):5} pairs; min {worst[3]:.4f}:1 ({worst[1]} / {worst[2]})")
            sections += ["", "最低文字对比度对应的组合：", ""]
            worst_text = min((row for row in results if row[4] == 7), key=lambda row: row[3])
            sections += [f"`{worst_text[1]}` / `{worst_text[2]}`：{worst_text[3]:.4f}:1。", ""]
        if failed:
            sections += ["## 未通过的组合", ""]
            for name, group, foreground, background, ratio, threshold in failed:
                message = f"{name} / {group}: {foreground} / {background} = {ratio:.4f}:1 < {threshold}:1"
                print(message, file=sys.stderr)
                sections.append(f"- {message}")
        sections += ["", "## 范围", "",
                     "覆盖主题显式定义的界面文字、语法（含注释）、行号、状态文字、默认终端 ANSI 前景、",
                     "光标及边框；同时检查选区、搜索、diff、括号匹配及弹出层底色。透明占位边框不作为可见标识。",
                     "这是颜色组合审计，不是 Zed 应用的完整 WCAG AAA 认证。未验证焦点面积、键盘或读屏行为、",
                     "选区与相邻底色之间的区别、语言服务额外淡化、插件自定义颜色，或终端程序指定的背景色、256 色和真彩色。",
                     "Zed 运行时若调整颜色或透明度，须按实际渲染重新评估。", ""]
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text("\n".join(sections))
        return 1 if failed else 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Contrast audit failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
