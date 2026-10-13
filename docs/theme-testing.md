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
- Markdown: selection visibility on prose, links, inline code, fenced code and
  diffs, including search overlap.
- Lists: selected rows versus the surrounding surface and hover; symbols and
  brackets versus normal/active lines; changed words versus solid/hollow diff
  rows and overlapping search; conflict sides versus each other and the editor.
- Terminal: default text and ANSI colors on the default surface; normal, bright
  and dim black/white pairs. Black must stay darker than white.
- Regressions: the old faint/brown highlights, selection hiding a match, invisible
  overlays, incorrect alpha/paint order, missing fields and duplicate JSON keys.
- Independent color-math references, unrounded thresholds and failing CLI status.

Dark primary text targets 7:1; comments target 4.5:1.
Day Vivid targets 4.5:1 except green syntax at a custom 2.5:1.
Search and selected text have no contrast target; tests retain visibility and overlap checks.
ANSI black on a dark default surface and white on a light one are exempt;
black/white pairs target 4.5:1. Arbitrary program-chosen pairs are not guaranteed.
Visibility uses custom guards: 0.06 Oklab distance for color separation, and 1.25:1
luminance for Markdown selections and active matches on dark editor backgrounds.
These guards catch known regressions; they do not guarantee visual acceptance.

## Rendering and references

[Zed 1.23.2 paints search before editor selections](https://github.com/zed-industries/zed/blob/v1.23.2/crates/editor/src/element.rs).
It multiplies the selection's theme alpha by 0.5 while search has focus. An opaque
selection can therefore replace the active search color when focus returns to the
editor. All variants use translucent selections to preserve it. The theme API
exposes two search backgrounds; adding outlines would require an editor change.
Search uses the Markdown selection blue at 40% for the current match and 20% for
others. Checks composite search over each actual surface, including inline chips
and diff rows, before applying word highlights or selections.
Markdown selections remain translucent for older Zed versions that paint over
glyphs. Their appearance needs a visual check, rather than a text contrast gate.
Lists also use `ghost_element.selected`, not just `element.selected`. Diff word
fills are painted after hunk fills and search: equal row/word colors hide changes,
while opaque word fills erase search. Translucent fills preserve both, including
when the player selection is painted last. ANSI slots can be foregrounds or
backgrounds; testing every slot only as text on the default surface previously
inverted their intended roles.

- [Catppuccin](https://github.com/catppuccin/zed/blob/4314cb05c74d141b7962290a41d6087e8c0ad02f/.github/workflows/check.yml): CI checks generated-theme consistency. We apply that idea to the audit report.
- [Rosé Pine](https://github.com/rose-pine/zed/blob/1446d31a2eec6bee627883d523ec63ef5c78ec9b/src/template.json): search states use different alpha values. This is a palette reference, not a borrowed test suite.
- Zed's [search tests](https://github.com/zed-industries/zed/blob/v1.23.2/crates/search/src/project_search.rs#L3725) and [Markdown tests](https://github.com/zed-industries/zed/blob/v1.23.2/crates/markdown/src/markdown.rs#L7941): distinct active colors, navigation, aligned inline code, Unicode and search/selection overlap inform our cases.
- Color math: [WCAG contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [Oklab](https://bottosson.github.io/posts/oklab/#converting-from-linear-srgb-to-oklab).

## In-app checks

Use [human-todo.md](../human-todo.md) for the release checklist, pass criteria and
result recording. It includes [the Markdown sample](../examples/theme-checks.md),
common editor/terminal states and the remaining visual coverage gaps.

## Local check · 2026-10-13

Zed 1.23.2 on macOS: blue Markdown selections were checked in Night AAA and Day
Vivid across prose, links, inline code and fenced code. Night AAA also covered
search overlap in code blocks and partial inline-code selection. Screenshots were
recorded under `.local/color-review/markdown-selection/`. The original
Night AAA theme and workspace were restored afterward.

Before search was unified with the Markdown selection blue, the review checked
Git word diffs, search inside changed words, conflicts
and project search in all four variants; command lists in Day AAA and Day Vivid;
brackets/references and ANSI black/white, black-on-green and reverse video in
Night AAA and Day Vivid. Night AAA also covered whole/partial symbol search and
navigation between files in project search. The terminal checks used Zed's
existing contrast adjustment; Day Vivid's black-on-green text was lightened by
Zed. Raw screenshots were recorded under `.local/color-review/final-review/`.
Night AAA and the original workspace were restored. No editor patch or rendering
override was installed.

That round passed 51 tests and the four-palette audit. After unifying search with
the selection blue, 56 tests and the updated audit pass, including transparent
search over inline chips, solid/hollow diff rows and focus-dependent selections.
The blue search palette was checked in Markdown previews in all four variants,
and in source views in Night AAA and Day Vivid. The latter two also covered
inline-code search/selection overlap. Day Vivid's source view showed cyan
document-reference highlights after selecting a whole word; the current search
match remained blue. Check that combination separately during manual acceptance.
New captures are in the locally ignored `.local/search-blue/` folder. Night AAA
and the original workspace/search query were restored.
CI commands were checked locally, not yet on GitHub. Older Zed binaries were not exercised.
Python tests do not execute GPUI or cover clipping, runtime fading, user overrides
or terminal programs' own colors. Repeat the manual checks after Zed updates.
