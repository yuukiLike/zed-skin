# GreenTree · Contrast audit

Dark primary text: AAA 7:1. Comments: AA 4.5:1. Day Vivid uses 4.5:1, except green syntax at a custom 2.5:1 (below AA). Search and selected text have no contrast target.
UI indicators use 3:1 on their surfaces. Selection checks measure background visibility and search overlap; selected text appearance is reviewed in Zed.
Visibility guards are custom: 0.06 Oklab distance (ΔEOK) for search, selection, symbols, changed words and conflict sides; 1.25:1 luminance for Markdown selections and active search on dark editor surfaces. They are not WCAG criteria or proof of visual acceptance.
ANSI black/white retain their terminal roles: paired normal, bright and dim colors target 4.5:1; black on a dark default surface and white on a light one are exempt. Other program-chosen combinations need an in-app check.
Pass/fail uses unrounded values. See [checks, sources and limits](theme-testing.md).

Reproduce: `python3 scripts/check_contrast.py --report docs/contrast-report.md`.

## GreenTree Day Vivid

Checked pairs: 11139.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2346 | 4.5105:1 | 4.5:1 | PASS |
| Editor / syntax | 3657 | 3.2783:1 | 2.5:1 / 4.5:1 | PASS (custom) |
| Comments | 138 | 5.3061:1 | 4.5:1 | PASS |
| Terminal text | 6 | 4.9292:1 | 4.5:1 | PASS |
| Terminal ANSI | 45 | 4.5158:1 | 4.5:1 | PASS |
| UI indicators | 3105 | 3.6919:1 | 3:1 | PASS |
| Scrollbar | 3 | 3.6962:1 | 3:1 | PASS |
| Cursors | 1552 | 3.3145:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 6.3362:1 | 4.5:1 | PASS |
| Vim / Helix badges | 8 | 4.5559:1 | 4.5:1 | PASS |
| Markdown selection visibility | 18 | 1.4350:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 36 | 0.0648 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.0945 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 100 | 0.1027 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 60 | 0.0671 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| List selection visibility | 12 | 0.0632 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor highlight visibility | 6 | 0.0675 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Debugger row visibility | 2 | 0.0668 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Debugger frame visibility | 1 | 0.0864 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Conflict distinction | 3 | 0.0652 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search distinction | 12 | 0.0607 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff word visibility | 4 | 0.0635 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search visibility | 16 | 0.0912 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`syntax.keyword` / `renamed.background`: 3.2783:1.

## GreenTree Day AAA

Checked pairs: 11145.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2346 | 7.0734:1 | 7:1 | PASS |
| Editor / syntax | 3657 | 7.0734:1 | 7:1 | PASS |
| Comments | 138 | 6.8885:1 | 4.5:1 | PASS |
| Terminal text | 6 | 9.4944:1 | 7:1 | PASS |
| Terminal ANSI | 45 | 5.4304:1 | 4.5:1 / 7:1 | PASS |
| UI indicators | 3105 | 4.2772:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.9861:1 | 3:1 | PASS |
| Cursors | 1552 | 3.1134:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 9.1080:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 7.8429:1 | 7:1 | PASS |
| Markdown selection visibility | 18 | 1.6809:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 36 | 0.0674 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.1161 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 100 | 0.1078 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 60 | 0.0693 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Active search visibility | 6 | 2.1876:1 | 1.25:1 | PASS (custom) |
| List selection visibility | 12 | 0.0700 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor highlight visibility | 6 | 0.0815 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Debugger row visibility | 2 | 0.0697 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Debugger frame visibility | 1 | 0.0672 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Conflict distinction | 3 | 0.0823 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search distinction | 12 | 0.0663 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff word visibility | 4 | 0.0778 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search visibility | 16 | 0.1050 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`terminal.ansi.bright_black` / `terminal.ansi.bright_white`: 5.4304:1.

## GreenTree Night AAA

Checked pairs: 11145.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2346 | 7.1414:1 | 7:1 | PASS |
| Editor / syntax | 3657 | 7.0316:1 | 7:1 | PASS |
| Comments | 138 | 6.7598:1 | 4.5:1 | PASS |
| Terminal text | 6 | 10.5586:1 | 7:1 | PASS |
| Terminal ANSI | 45 | 4.5234:1 | 4.5:1 / 7:1 | PASS |
| UI indicators | 3105 | 3.3340:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.6351:1 | 3:1 | PASS |
| Cursors | 1552 | 3.0476:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 11.0848:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.0515:1 | 7:1 | PASS |
| Markdown selection visibility | 18 | 1.8055:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 36 | 0.0787 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.1684 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 100 | 0.1288 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 60 | 0.0817 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Active search visibility | 6 | 2.2730:1 | 1.25:1 | PASS (custom) |
| List selection visibility | 12 | 0.0804 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor highlight visibility | 6 | 0.1368 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Debugger row visibility | 2 | 0.0965 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Debugger frame visibility | 1 | 0.1331 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Conflict distinction | 3 | 0.1255 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search distinction | 12 | 0.0737 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff word visibility | 4 | 0.0896 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search visibility | 16 | 0.1168 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`terminal.ansi.bright_black` / `terminal.ansi.bright_white`: 4.5234:1.

## GreenTree Midnight AAA

Checked pairs: 11145.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2346 | 7.1414:1 | 7:1 | PASS |
| Editor / syntax | 3657 | 7.0316:1 | 7:1 | PASS |
| Comments | 138 | 6.7598:1 | 4.5:1 | PASS |
| Terminal text | 6 | 10.8791:1 | 7:1 | PASS |
| Terminal ANSI | 45 | 5.4060:1 | 4.5:1 / 7:1 | PASS |
| UI indicators | 3105 | 3.3340:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.7758:1 | 3:1 | PASS |
| Cursors | 1552 | 3.0476:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 11.4213:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.7633:1 | 7:1 | PASS |
| Markdown selection visibility | 18 | 1.8004:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 36 | 0.0843 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.2646 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 100 | 0.1411 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 60 | 0.0881 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Active search visibility | 6 | 2.2565:1 | 1.25:1 | PASS (custom) |
| List selection visibility | 12 | 0.0804 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor highlight visibility | 6 | 0.1774 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Debugger row visibility | 2 | 0.1453 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Debugger frame visibility | 1 | 0.2791 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Conflict distinction | 3 | 0.1255 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search distinction | 12 | 0.0806 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff word visibility | 4 | 0.0946 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search visibility | 16 | 0.1280 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`terminal.ansi.bright_black` / `terminal.ansi.bright_white`: 5.4060:1.


This audit covers explicit palette colors and modeled selections. Runtime fading, user overrides, terminal program colors and Zed's rendering behavior require in-app checks.
