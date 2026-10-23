# GreenTree · Contrast audit

Day Vivid targets AA 4.5:1 on normal surfaces. The three dark variants match their session-start palettes: primary text targets AAA 7:1 and comments AA 4.5:1. Dark Git highlights retain 7:1 for primary text and 4.5:1 for colored text. Expanded search/selection and rendered-Markdown text measurements are advisory: below-target pairs are marked REVIEW, not claimed as passing their contrast targets.
UI indicators use 3:1 on their surfaces. Selection checks cover both text readability and background visibility, including search overlap in source, Markdown previews and terminal selections.
Visibility guards are custom: 0.06 Oklab distance (ΔEOK) for search, selection, symbols, added/deleted rows, changed words and conflict sides; 1.25:1 luminance for Markdown selections and active search on dark editor surfaces. They are not WCAG criteria or proof of visual acceptance.
ANSI black/white retain their terminal roles: paired normal, bright and dim colors target 4.5:1; black on a dark default surface and white on a light one are exempt. Other program-chosen combinations need an in-app check.
Pass/fail uses unrounded values. See [checks, sources and limits](theme-testing.md).

Reproduce: `python3 scripts/check_contrast.py --report docs/contrast-report.md`.

## GreenTree Day Vivid

Checked pairs: 32556.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 10268 | 2.2192:1 | 4.5:1 | REVIEW (4859 advisory) |
| Editor / syntax | 16006 | 2.2192:1 | 4.5:1 | REVIEW (7884 advisory) |
| Comments | 604 | 2.2427:1 | 4.5:1 | REVIEW (410 advisory) |
| Terminal text | 12 | 4.0000:1 | 4.5:1 | REVIEW (2 advisory) |
| Terminal ANSI | 87 | 3.4832:1 | 4.5:1 | REVIEW (38 advisory) |
| UI indicators | 3735 | 3.1180:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.0216:1 | 3:1 | PASS |
| Cursors | 1552 | 3.0251:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 6.9783:1 | 4.5:1 | PASS |
| Vim / Helix badges | 8 | 4.5091:1 | 4.5:1 | PASS |
| Markdown selection visibility | 18 | 1.6154:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 36 | 0.0609 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.0887 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 100 | 0.0865 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 60 | 0.0848 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| List selection visibility | 12 | 0.0625 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor highlight visibility | 6 | 0.0685 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Debugger row visibility | 2 | 0.0707 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Debugger frame visibility | 1 | 0.0609 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff row distinction | 2 | 0.0626 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Conflict distinction | 3 | 0.0604 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search distinction | 12 | 0.0607 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff word visibility | 4 | 0.0642 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search visibility | 16 | 0.0609 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`version_control.deleted` / `search.active_match_background / element.selection_background / surface.background / inline code`: 2.2192:1.

## GreenTree Day AAA

Checked pairs: 32562.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 10268 | 2.3615:1 | 4.5:1 / 7:1 | REVIEW (4687 advisory) |
| Editor / syntax | 16006 | 2.3615:1 | 4.5:1 / 7:1 | REVIEW (6799 advisory) |
| Comments | 604 | 2.2998:1 | 4.5:1 | REVIEW (338 advisory) |
| Terminal text | 12 | 6.5165:1 | 4.5:1 / 7:1 | PASS |
| Terminal ANSI | 87 | 5.4304:1 | 4.5:1 / 7:1 | PASS |
| UI indicators | 3735 | 3.6363:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.9861:1 | 3:1 | PASS |
| Cursors | 1552 | 3.0273:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 10.5705:1 | 7:1 | PASS |
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
| Diff row distinction | 2 | 0.0673 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Conflict distinction | 3 | 0.0823 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search distinction | 12 | 0.0640 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff word visibility | 4 | 0.0713 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search visibility | 16 | 0.0977 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`syntax.comment` / `search.active / editor focused / players[0].selection / version_control.word_added / editor.diff_hunk.added.background`: 2.2998:1.

## GreenTree Night AAA

Checked pairs: 32562.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 10268 | 2.2810:1 | 4.5:1 / 7:1 | REVIEW (4266 advisory) |
| Editor / syntax | 16006 | 2.2459:1 | 4.5:1 / 7:1 | REVIEW (6313 advisory) |
| Comments | 604 | 2.1590:1 | 4.5:1 | REVIEW (324 advisory) |
| Terminal text | 12 | 7.7660:1 | 4.5:1 / 7:1 | PASS |
| Terminal ANSI | 87 | 4.5234:1 | 4.5:1 / 7:1 | PASS |
| UI indicators | 3735 | 3.0230:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.6351:1 | 3:1 | PASS |
| Cursors | 1552 | 3.0000:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 13.0583:1 | 7:1 | PASS |
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
| Diff row distinction | 2 | 0.0607 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Conflict distinction | 3 | 0.1255 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search distinction | 12 | 0.0674 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff word visibility | 4 | 0.0781 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search visibility | 16 | 0.1022 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`syntax.comment` / `search.active / editor focused / players[0].selection / version_control.word_added / editor.diff_hunk.added.background`: 2.1590:1.

## GreenTree Midnight AAA

Checked pairs: 32562.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 10268 | 2.2923:1 | 4.5:1 / 7:1 | REVIEW (3845 advisory) |
| Editor / syntax | 16006 | 2.2571:1 | 4.5:1 / 7:1 | REVIEW (5543 advisory) |
| Comments | 604 | 2.1698:1 | 4.5:1 | REVIEW (294 advisory) |
| Terminal text | 12 | 8.1296:1 | 4.5:1 / 7:1 | PASS |
| Terminal ANSI | 87 | 5.4060:1 | 4.5:1 / 7:1 | PASS |
| UI indicators | 3735 | 3.2384:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.7758:1 | 3:1 | PASS |
| Cursors | 1552 | 3.0063:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 13.4161:1 | 7:1 | PASS |
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
| Diff row distinction | 2 | 0.0614 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Conflict distinction | 3 | 0.1255 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search distinction | 12 | 0.0687 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff word visibility | 4 | 0.0911 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Diff search visibility | 16 | 0.1048 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`syntax.comment` / `search.active / editor focused / players[0].selection / version_control.word_added / editor.diff_hunk.added.background`: 2.1698:1.


This audit covers explicit palette colors and modeled selections. Runtime fading, user overrides, terminal program colors and Zed's rendering behavior require in-app checks.
