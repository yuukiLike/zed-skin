# GreenTree · Contrast audit

Dark primary text: AAA 7:1. Comments and search: AA 4.5:1. Day Vivid uses 4.5:1, except green syntax at a custom 2.5:1 (below AA). Selected text has no contrast target.
UI indicators use 3:1 on their surfaces. Selection checks measure background visibility and search overlap; selected text appearance is reviewed in Zed.
Visibility guards are custom: 0.06 Oklab distance (ΔEOK) for search, selection, symbols, changed words and conflict sides; 1.25:1 luminance for Markdown selections and active search on dark editor surfaces. They are not WCAG criteria or proof of visual acceptance.
ANSI black/white retain their terminal roles: paired normal, bright and dim colors target 4.5:1; black on a dark default surface and white on a light one are exempt. Other program-chosen combinations need an in-app check.
Pass/fail uses unrounded values. See [checks, sources and limits](theme-testing.md).

Reproduce: `python3 scripts/check_contrast.py --report docs/contrast-report.md`.

## GreenTree Day Vivid

Checked pairs: 10659.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2550 | 4.5105:1 | 4.5:1 | PASS |
| Editor / syntax | 3975 | 3.2783:1 | 2.5:1 / 4.5:1 | PASS (custom) |
| Comments | 150 | 5.3061:1 | 4.5:1 | PASS |
| Terminal text | 6 | 4.9292:1 | 4.5:1 | PASS |
| Terminal ANSI | 45 | 4.5158:1 | 4.5:1 | PASS |
| UI indicators | 3105 | 3.6919:1 | 3:1 | PASS |
| Scrollbar | 3 | 3.6962:1 | 3:1 | PASS |
| Cursors | 696 | 4.5534:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 4.5587:1 | 4.5:1 | PASS |
| Vim / Helix badges | 8 | 4.5559:1 | 4.5:1 | PASS |
| Markdown selection visibility | 18 | 1.4350:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 4 | 0.1396 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 40 | 0.0633 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.0753 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 3 | 0.1500 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| List selection visibility | 12 | 0.0653 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor highlight visibility | 6 | 0.0675 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Conflict distinction | 3 | 0.0652 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search distinction | 6 | 0.1095 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff word visibility | 4 | 0.0635 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search visibility | 16 | 0.0600 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`syntax.keyword` / `renamed.background`: 3.2783:1.

## GreenTree Day AAA

Checked pairs: 10857.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2550 | 5.6481:1 | 4.5:1 / 7:1 | PASS |
| Editor / syntax | 3975 | 5.6481:1 | 4.5:1 / 7:1 | PASS |
| Comments | 150 | 5.5004:1 | 4.5:1 | PASS |
| Terminal text | 6 | 9.4944:1 | 7:1 | PASS |
| Terminal ANSI | 45 | 5.4304:1 | 4.5:1 / 7:1 | PASS |
| UI indicators | 3105 | 4.2923:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.9861:1 | 3:1 | PASS |
| Cursors | 888 | 4.7128:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 8.2458:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 7.8429:1 | 7:1 | PASS |
| Markdown selection visibility | 18 | 1.6809:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 4 | 0.0844 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 40 | 0.1646 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.1161 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 3 | 0.1081 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Active search visibility | 6 | 1.3098:1 | 1.25:1 | PASS (custom) |
| List selection visibility | 12 | 0.0783 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor highlight visibility | 6 | 0.0815 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Conflict distinction | 3 | 0.0823 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search distinction | 6 | 0.0768 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff word visibility | 4 | 0.0778 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search visibility | 16 | 0.1328 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`terminal.ansi.bright_black` / `terminal.ansi.bright_white`: 5.4304:1.

## GreenTree Night AAA

Checked pairs: 10857.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2550 | 5.6292:1 | 4.5:1 / 7:1 | PASS |
| Editor / syntax | 3975 | 5.5426:1 | 4.5:1 / 7:1 | PASS |
| Comments | 150 | 5.3283:1 | 4.5:1 | PASS |
| Terminal text | 6 | 10.5586:1 | 7:1 | PASS |
| Terminal ANSI | 45 | 4.5234:1 | 4.5:1 / 7:1 | PASS |
| UI indicators | 3105 | 3.3775:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.6351:1 | 3:1 | PASS |
| Cursors | 888 | 4.6091:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 9.9285:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.0515:1 | 7:1 | PASS |
| Markdown selection visibility | 18 | 1.8055:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 4 | 0.0945 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 40 | 0.1782 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.1684 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 3 | 0.0961 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Active search visibility | 6 | 1.4972:1 | 1.25:1 | PASS (custom) |
| List selection visibility | 12 | 0.0999 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor highlight visibility | 6 | 0.1368 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Conflict distinction | 3 | 0.1255 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search distinction | 6 | 0.0652 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff word visibility | 4 | 0.0896 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search visibility | 16 | 0.1664 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`terminal.ansi.bright_black` / `terminal.ansi.bright_white`: 4.5234:1.

## GreenTree Midnight AAA

Checked pairs: 10857.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2550 | 5.6292:1 | 4.5:1 / 7:1 | PASS |
| Editor / syntax | 3975 | 5.5426:1 | 4.5:1 / 7:1 | PASS |
| Comments | 150 | 5.3283:1 | 4.5:1 | PASS |
| Terminal text | 6 | 10.8791:1 | 7:1 | PASS |
| Terminal ANSI | 45 | 5.4060:1 | 4.5:1 / 7:1 | PASS |
| UI indicators | 3105 | 3.3775:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.7758:1 | 3:1 | PASS |
| Cursors | 888 | 4.6091:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 10.2298:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.7633:1 | 7:1 | PASS |
| Markdown selection visibility | 18 | 1.8004:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 4 | 0.0945 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 40 | 0.2098 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.2646 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 3 | 0.0961 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Active search visibility | 6 | 1.6150:1 | 1.25:1 | PASS (custom) |
| List selection visibility | 12 | 0.1197 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor highlight visibility | 6 | 0.1774 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Conflict distinction | 3 | 0.1255 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search distinction | 6 | 0.0652 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff word visibility | 4 | 0.0946 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search visibility | 16 | 0.1916 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`syntax.comment` / `search.active / version_control.word_added`: 5.3283:1.


This audit covers explicit palette colors and modeled selections. Runtime fading, user overrides, terminal program colors and Zed's rendering behavior require in-app checks.
