# GreenTree · Contrast audit

Uses the WCAG 2.x sRGB relative luminance formula. Day Vivid's green syntax has a custom 2.5:1 floor and does not meet AA text contrast.
Other base-palette Day Vivid text is checked at 4.5:1. Day AAA, Night and Midnight primary text is checked at 7:1; comments use 4.5:1.
Markdown selections are composited over both glyphs and backgrounds: dark variants use AA 4.5:1; Day Vivid uses a custom 2.5:1 floor (not AA).
Selected/unselected Markdown backgrounds must differ by a custom 1.25:1 luminance ratio. This visibility guard is not a WCAG criterion or a substitute for visual review.
Key non-text indicators are checked at 3:1. Unknown theme names are rejected, not given a weaker target.
Pass/fail uses unrounded ratios; tables display four decimal places.

Reproduce: `python3 scripts/check_contrast.py --report docs/contrast-report.md`.

## GreenTree Day Vivid

Checked pairs: 11315.

| Scope | Pairs | Minimum contrast | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2618 | 4.5105:1 | 4.5:1 | PASS |
| Editor / syntax | 4081 | 2.7265:1 | 2.5:1 / 4.5:1 | PASS (custom) |
| Comments | 154 | 5.3061:1 | 4.5:1 | PASS |
| Terminal text | 270 | 4.5105:1 | 4.5:1 | PASS |
| UI indicators | 3465 | 3.6919:1 | 3:1 | PASS |
| Scrollbar | 3 | 3.6962:1 | 3:1 | PASS |
| Cursors | 616 | 4.5534:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 4.5587:1 | 4.5:1 | PASS |
| Vim / Helix badges | 8 | 4.5559:1 | 4.5:1 | PASS |
| Markdown selection | 74 | 2.5212:1 | 2.5:1 | PASS (custom) |
| Markdown selection visibility | 18 | 1.2676:1 | 1.25:1 | PASS (custom) |

Lowest text contrast pair:

`syntax.keyword` / `editor.background / code block`: 2.5212:1.

## GreenTree Day AAA

Checked pairs: 11315.

| Scope | Pairs | Minimum contrast | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2618 | 7.0984:1 | 7:1 | PASS |
| Editor / syntax | 4081 | 7.0984:1 | 7:1 | PASS |
| Comments | 154 | 5.7668:1 | 4.5:1 | PASS |
| Terminal text | 270 | 7.0721:1 | 7:1 | PASS |
| UI indicators | 3465 | 4.2923:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.9861:1 | 3:1 | PASS |
| Cursors | 616 | 7.0984:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 8.2458:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 7.8429:1 | 7:1 | PASS |
| Markdown selection | 74 | 4.7196:1 | 4.5:1 | PASS |
| Markdown selection visibility | 18 | 1.2698:1 | 1.25:1 | PASS (custom) |

Lowest text contrast pair:

`syntax.comment` / `editor.background / code block`: 4.7196:1.

## GreenTree Night AAA

Checked pairs: 11315.

| Scope | Pairs | Minimum contrast | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2618 | 7.4199:1 | 7:1 | PASS |
| Editor / syntax | 4081 | 7.3059:1 | 7:1 | PASS |
| Comments | 154 | 5.2146:1 | 4.5:1 | PASS |
| Terminal text | 270 | 7.3925:1 | 7:1 | PASS |
| UI indicators | 3465 | 3.4640:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.6351:1 | 3:1 | PASS |
| Cursors | 616 | 7.4199:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 9.9285:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.0515:1 | 7:1 | PASS |
| Markdown selection | 74 | 4.7090:1 | 4.5:1 | PASS |
| Markdown selection visibility | 18 | 1.3596:1 | 1.25:1 | PASS (custom) |

Lowest text contrast pair:

`syntax.diff.minus` / `syntax.diff.minus.background_color / code block`: 4.7090:1.

## GreenTree Midnight AAA

Checked pairs: 11315.

| Scope | Pairs | Minimum contrast | Target | Result |
| --- | ---: | ---: | ---: | --- |
| UI text | 2618 | 8.4232:1 | 7:1 | PASS |
| Editor / syntax | 4081 | 8.2937:1 | 7:1 | PASS |
| Comments | 154 | 5.9197:1 | 4.5:1 | PASS |
| Terminal text | 270 | 8.3920:1 | 7:1 | PASS |
| UI indicators | 3465 | 3.9324:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.7758:1 | 3:1 | PASS |
| Cursors | 616 | 8.4232:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 10.2298:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.7633:1 | 7:1 | PASS |
| Markdown selection | 74 | 4.5985:1 | 4.5:1 | PASS |
| Markdown selection visibility | 18 | 1.4706:1 | 1.25:1 | PASS (custom) |

Lowest text contrast pair:

`syntax.comment` / `editor.background / code block`: 4.5985:1.


## Scope

Checks explicit UI text, syntax including comments, line numbers, status text, default ANSI terminal foregrounds,
cursors and borders against selection, search, diff, bracket-match and popup backgrounds. Transparent placeholder borders are excluded.

Markdown selection checks cover prose, links, inline code and syntax-highlighted code blocks, including the overlay on the glyphs themselves.
They model the sRGB source-over blend used by Zed; fully opaque and invisible selection overlays are rejected.

The AAA theme names describe the primary-text target, not every state: comments and selected Markdown intentionally target AA 4.5:1.
Markdown selection visibility uses a custom 1.25:1 floor, not the WCAG 3:1 non-text target. Editor selection/background separation is not checked.

This is a palette audit, not WCAG certification of Zed. It does not verify focus area, keyboard or screen-reader behavior,
language-server fading, plugin colors, or terminal application backgrounds, 256 colors and true color.
Runtime color/opacity adjustments and user overrides require evaluation of the actual rendered result.

References: [WCAG AAA text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html),
[non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).
