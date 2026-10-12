# Theme checks

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/check_contrast.py --report docs/contrast-report.md
git diff --check
```

Only Python's standard library is needed. CI runs the tests and audit, then fails
if the generated report differs from the committed copy.

## Coverage

- All four palettes: text contrast, visible search/selection backgrounds, and
  distinct current/other matches with either the search field or editor focused.
- Markdown: prose, links, inline code, fenced syntax, comments and diffs; search
  plus selection with both legacy over-glyph and current under-glyph painting.
- Regressions: the old faint/brown highlights, selection hiding a match, invisible
  overlays, unreadable stacked highlights, missing fields and duplicate JSON keys.
- Independent color-math references, unrounded thresholds and failing CLI status.

Dark primary text targets 7:1; comments, search and selected text target 4.5:1.
Day Vivid targets 4.5:1 except green syntax and selected Markdown at a custom 2.5:1.
Visibility uses custom guards: 0.06 Oklab distance for color separation, and 1.25:1
luminance for Markdown selections and active matches on dark editor backgrounds.
These guards catch known regressions; they do not guarantee visual acceptance.

## Rendering and references

[Zed 1.23.2 paints search before editor selections](https://github.com/zed-industries/zed/blob/v1.23.2/crates/editor/src/element.rs).
It multiplies the selection's theme alpha by 0.5 while search has focus. An opaque
selection can therefore replace the active search color when focus returns to the
editor. Dark variants use translucent selections to preserve it. The theme API
exposes two search backgrounds; adding outlines would require an editor change.

- [Catppuccin](https://github.com/catppuccin/zed/blob/4314cb05c74d141b7962290a41d6087e8c0ad02f/.github/workflows/check.yml): CI checks generated-theme consistency. We apply that idea to the audit report.
- [Rosé Pine](https://github.com/rose-pine/zed/blob/1446d31a2eec6bee627883d523ec63ef5c78ec9b/src/template.json): search states use different alpha values. This is a palette reference, not a borrowed test suite.
- Zed's [search tests](https://github.com/zed-industries/zed/blob/v1.23.2/crates/search/src/project_search.rs#L3725) and [Markdown tests](https://github.com/zed-industries/zed/blob/v1.23.2/crates/markdown/src/markdown.rs#L7941): distinct active colors, navigation, aligned inline code, Unicode and search/selection overlap inform our cases.
- Color math: [WCAG contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [Oklab](https://bottosson.github.io/posts/oklab/#converting-from-linear-srgb-to-oklab).

## In-app checklist

Open [the sample](../examples/theme-checks.md) as source and Markdown preview in each variant:

1. Search `iPhone` (one result), then `任务` (multiple); move forward/back and wrap.
2. Switch focus between search and editor; the current result must remain visible.
3. Search `test`, partial `tes`, and `é中🙂` in inline code and aligned tables.
4. Select prose, links, partial inline code and fenced code, with search on and off.
5. Check an absent query, clear the query, then dismiss search.
6. Check project search and confirm the installed JSON matches the repository.

## Local check · 2026-10-13

Zed 1.23.2 on macOS: all four variants were checked for source `iPhone` and preview
`test` matches. Night AAA also covered match navigation, focus changes and partial
selection over searched inline code. Day Vivid covered focus changes and selected
green code. The original Night AAA theme was restored afterward.

All 42 tests and the four-palette audit passed; report regeneration was identical.
CI commands were checked locally, not yet on GitHub. Project search and older Zed
binaries were not exercised; the legacy paint order has color-model coverage only.
Python tests do not execute GPUI or cover clipping, runtime fading, user overrides
or terminal programs' own colors. Repeat the in-app checklist after Zed updates.
