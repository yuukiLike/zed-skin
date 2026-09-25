# GreenTree · Contrast audit

Uses the WCAG 2.x sRGB relative luminance formula. Day Vivid's green syntax has a custom 2.5:1 floor and does not meet AA text contrast.
Other Day Vivid text is checked at 4.5:1; Day AAA, Night and Midnight text at 7:1.
Key non-text indicators are checked at 3:1. Unknown theme names are rejected, not given a weaker target.
Pass/fail uses unrounded ratios; tables display four decimal places.

Reproduce: `python3 scripts/check_contrast.py --report docs/contrast-report.md`.

## GreenTree Day Vivid

Checked pairs: 11365.

| Scope | Pairs | Minimum contrast | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2652 | 4.5105:1 | 4.5:1 | PASS |
| Editor / syntax | 4290 | 2.7265:1 | 2.5:1 / 4.5:1 | PASS (custom) |
| Terminal text | 270 | 4.5105:1 | 4.5:1 | PASS |
| UI indicators | 3510 | 3.6919:1 | 3:1 | PASS |
| Scrollbar | 3 | 3.6962:1 | 3:1 | PASS |
| Cursors | 624 | 4.5534:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 4.5587:1 | 4.5:1 | PASS |
| Vim / Helix badges | 8 | 4.5559:1 | 4.5:1 | PASS |

Lowest text contrast pair:

`syntax.keyword` / `renamed.background`: 2.7265:1.

## GreenTree Day AAA

Checked pairs: 11365.

| Scope | Pairs | Minimum contrast | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2652 | 7.0984:1 | 7:1 | PASS |
| Editor / syntax | 4290 | 7.0984:1 | 7:1 | PASS |
| Terminal text | 270 | 7.0721:1 | 7:1 | PASS |
| UI indicators | 3510 | 4.2923:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.9861:1 | 3:1 | PASS |
| Cursors | 624 | 7.0984:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 8.2458:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 7.8429:1 | 7:1 | PASS |

Lowest text contrast pair:

`terminal.ansi.dim_yellow` / `players[0].selection`: 7.0721:1.

## GreenTree Night AAA

Checked pairs: 11365.

| Scope | Pairs | Minimum contrast | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2652 | 7.4199:1 | 7:1 | PASS |
| Editor / syntax | 4290 | 7.3059:1 | 7:1 | PASS |
| Terminal text | 270 | 7.3925:1 | 7:1 | PASS |
| UI indicators | 3510 | 3.4640:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.6351:1 | 3:1 | PASS |
| Cursors | 624 | 7.4199:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 9.9285:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.0515:1 | 7:1 | PASS |

Lowest text contrast pair:

`syntax.constructor` / `element.active`: 7.3059:1.

## GreenTree Midnight AAA

Checked pairs: 11365.

| Scope | Pairs | Minimum contrast | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2652 | 8.4232:1 | 7:1 | PASS |
| Editor / syntax | 4290 | 8.2937:1 | 7:1 | PASS |
| Terminal text | 270 | 8.3920:1 | 7:1 | PASS |
| UI indicators | 3510 | 3.9324:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.7758:1 | 3:1 | PASS |
| Cursors | 624 | 8.4232:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 10.2298:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.7633:1 | 7:1 | PASS |

Lowest text contrast pair:

`syntax.constructor` / `search.active_match_background`: 8.2937:1.


## Scope

Checks explicit UI text, syntax including comments, line numbers, status text, default ANSI terminal foregrounds,
cursors and borders against selection, search, diff, bracket-match and popup backgrounds. Transparent placeholder borders are excluded.

This is a palette audit, not WCAG certification of Zed. It does not verify focus area, keyboard or screen-reader behavior,
selection/background separation, language-server fading, plugin colors, or terminal application backgrounds, 256 colors and true color.
Runtime color/opacity adjustments and user overrides require evaluation of the actual rendered result.

References: [WCAG AAA text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html),
[non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).
