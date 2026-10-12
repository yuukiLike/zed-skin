# GreenTree · Contrast audit

Dark primary text: AAA 7:1. Comments, search and selected text: AA 4.5:1. Day Vivid uses 4.5:1, except green syntax and selected Markdown at a custom 2.5:1 (below AA).
UI indicators use 3:1 on their surfaces. Text selections are composited before measurement; Markdown checks cover both legacy over-glyph and current under-glyph paint order.
Visibility guards are custom: 0.06 Oklab distance (ΔEOK) for color separation; 1.25:1 luminance for Markdown selections and active search on dark editor surfaces. They are not WCAG criteria or proof of visual acceptance.
Pass/fail uses unrounded values. See [checks, sources and limits](theme-testing.md).

Reproduce: `python3 scripts/check_contrast.py --report docs/contrast-report.md`.

## GreenTree Day Vivid

Checked pairs: 11191.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2618 | 4.5105:1 | 4.5:1 | PASS |
| Editor / syntax | 4081 | 3.2783:1 | 2.5:1 / 4.5:1 | PASS (custom) |
| Comments | 154 | 5.3061:1 | 4.5:1 | PASS |
| Terminal text | 270 | 4.5105:1 | 4.5:1 | PASS |
| UI indicators | 3015 | 3.6919:1 | 3:1 | PASS |
| Scrollbar | 3 | 3.6962:1 | 3:1 | PASS |
| Cursors | 616 | 4.5534:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 4.5587:1 | 4.5:1 | PASS |
| Vim / Helix badges | 8 | 4.5559:1 | 4.5:1 | PASS |
| Markdown selection | 176 | 2.9641:1 | 2.5:1 | PASS (custom) |
| Markdown selection (under text) | 176 | 2.5612:1 | 2.5:1 | PASS (custom) |
| Markdown selection visibility | 18 | 1.2676:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 4 | 0.0878 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 40 | 0.0633 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.0753 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 3 | 0.1500 ΔEOK | 0.06 ΔEOK | PASS (custom) |

Lowest text contrast pair:

`syntax.keyword` / `editor.background / code block`: 2.5612:1.

## GreenTree Day AAA

Checked pairs: 13331.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 3366 | 4.9012:1 | 4.5:1 / 7:1 | PASS |
| Editor / syntax | 5247 | 4.9012:1 | 4.5:1 / 7:1 | PASS |
| Comments | 198 | 4.7730:1 | 4.5:1 | PASS |
| Terminal text | 270 | 5.6385:1 | 4.5:1 / 7:1 | PASS |
| UI indicators | 3015 | 4.2923:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.9861:1 | 3:1 | PASS |
| Cursors | 792 | 4.9012:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 8.2458:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 7.8429:1 | 7:1 | PASS |
| Markdown selection | 176 | 4.5333:1 | 4.5:1 | PASS |
| Markdown selection (under text) | 176 | 4.9647:1 | 4.5:1 | PASS |
| Markdown selection visibility | 18 | 1.4455:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 4 | 0.0621 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 40 | 0.1646 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.1161 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 3 | 0.1081 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Active search visibility | 6 | 1.3098:1 | 1.25:1 | PASS (custom) |

Lowest text contrast pair:

`text.accent` / `elevated_surface.background / link`: 4.5333:1.

## GreenTree Night AAA

Checked pairs: 13331.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 3366 | 4.8361:1 | 4.5:1 / 7:1 | PASS |
| Editor / syntax | 5247 | 4.7617:1 | 4.5:1 / 7:1 | PASS |
| Comments | 198 | 4.5776:1 | 4.5:1 | PASS |
| Terminal text | 270 | 7.2755:1 | 4.5:1 / 7:1 | PASS |
| UI indicators | 3015 | 3.4640:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.6351:1 | 3:1 | PASS |
| Cursors | 792 | 4.8361:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 9.9285:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.0515:1 | 7:1 | PASS |
| Markdown selection | 176 | 4.5085:1 | 4.5:1 | PASS |
| Markdown selection (under text) | 176 | 4.6291:1 | 4.5:1 | PASS |
| Markdown selection visibility | 18 | 1.3906:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 4 | 0.0648 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 40 | 0.1782 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.1684 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 3 | 0.0961 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Active search visibility | 6 | 1.4972:1 | 1.25:1 | PASS (custom) |

Lowest text contrast pair:

`syntax.comment` / `search.match_background / code block`: 4.5085:1.

## GreenTree Midnight AAA

Checked pairs: 13331.

| Scope | Pairs | Minimum | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 3366 | 4.8361:1 | 4.5:1 / 7:1 | PASS |
| Editor / syntax | 5247 | 4.7617:1 | 4.5:1 / 7:1 | PASS |
| Comments | 198 | 4.5776:1 | 4.5:1 | PASS |
| Terminal text | 270 | 7.6161:1 | 4.5:1 / 7:1 | PASS |
| UI indicators | 3015 | 3.9756:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.7758:1 | 3:1 | PASS |
| Cursors | 792 | 4.8361:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 10.2298:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.7633:1 | 7:1 | PASS |
| Markdown selection | 176 | 4.5085:1 | 4.5:1 | PASS |
| Markdown selection (under text) | 176 | 4.6291:1 | 4.5:1 | PASS |
| Markdown selection visibility | 18 | 1.3625:1 | 1.25:1 | PASS (custom) |
| Markdown search selection visibility | 4 | 0.0648 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search visibility | 40 | 0.2098 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Editor selection visibility | 1 | 0.2646 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Search state distinction | 3 | 0.0961 ΔEOK | 0.06 ΔEOK | PASS (custom) |
| Active search visibility | 6 | 1.6150:1 | 1.25:1 | PASS (custom) |

Lowest text contrast pair:

`syntax.comment` / `search.match_background / code block`: 4.5085:1.


This audit covers explicit palette colors and modeled selections. Runtime fading, user overrides, terminal program colors and Zed's rendering behavior require in-app checks.
