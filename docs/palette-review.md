# Palette notes

- **Day Vivid:** soft sage `#DCE4D6` with near-black variables `#090D12`, leaf
  green keywords `#00610C`, royal-blue calls `#1234BF`, orchid types `#8500A9`,
  raspberry values `#A00052` and burnt-orange strings `#803B00`. Properties use
  orange `#943000`, italic comments use muted plum `#674A5F`, and
  punctuation uses neutral slate `#41464D`. Markdown source headings use emerald
  `#005F46`, separately from code keywords. Color categories differ in both hue
  and lightness. Font weights and backgrounds are unchanged.
- **Day AAA:** deep indigo `#1C2135` with bright syntax colors.
- **Night AAA:** near black `#050505`, soft white and regular green keywords.
- **Midnight AAA:** pure black `#000000`, bright white and bold green keywords.

Day Vivid uses green `#438D3D` at 60% for the current search match, 30% for
others and 55% for Markdown selections. The original dark palettes use blue
`#408CFF` at 50%, 30% and 40%, respectively. Local editor selections remain at
25%, preserving search underneath. Vivid uses regular variables and italic
comments (400), with keywords/functions at 500; other tokens retain their
earlier weights. Dark variants retain their original token weights and italic
gray comments. No global font-family, weight or fading overrides are installed.

For the dimmer-display adjustment, keyword contrast against near-black variables
increases from 2.15:1 to 2.52:1. The brighter, more saturated leaf green retains
5.93:1 against the sage editor and at least 4.57:1 across enforced surfaces;
comments reach 5.92:1 on the editor. The existing 4.5:1 requirements remain
enforced on normal and diff surfaces. At the user's
request, property names such as `length` use orange: 6.01:1 on the editor and
4.98:1 on the selected row. Properties and strings now share a warm color
family; other approved syntax colors are retained. Palette measurements do not
guarantee visual acceptance.

Day Vivid's lists and symbol/bracket highlights use leaf green, with matching
focus borders, active indent guides and line numbers. Its selected row is
`#B4D8AA`, distinct from its `#D3E9AD` hover. The user approved the current-file
highlight; these UI colors remain unchanged in the syntax-category adjustment.
Subtle buttons (including the tab close button) and list rows using
`ghost_element.hover` now use soft rose `#E8C8D5` on hover, distinct from green
selected rows. Filled controls and debugger frames retain their leaf-green
`element.hover`. Tab backgrounds and the dark close glyph remain unchanged.
Git diffs use soft mint green
for additions and coral/rose for deletions, with matching gutters and hollow
borders. Changed words use brighter translucent green/red fills over lightly
tinted rows, preserving search underneath. The dark palettes retain their
original blue/cyan lists, symbol highlights, word fills and cursor colors.
Vivid's secondary UI/file-list text uses forest green `#2D412F`; added-file
labels and green status colors use `#0B4722`. These shared UI colors also apply to
menus, status labels and debugger text. File lists retain their existing weight.
Secondary text reaches 7.79:1 on the panel and 6.99:1 on the selected row;
added-file text reaches 7.67:1 and 6.88:1, respectively. Conflict
sides use blue/green in dark themes and muted blue/yellow in Day Vivid.
Read/write references share one color;
they identify occurrences without distinguishing access type.

Markdown preview links use royal blue `#1234BF` through the shared `text.accent`
field. Forest borders `#39704C` and `#3F7654` color tables, quotes, dividers and
code frames; other Vivid controls using `border` or `border.variant` inherit
these colors too. Focus/selection borders, file-list text, selected rows and
backgrounds are unchanged. In Zed 1.25.3, preview H1-H5 headings, prose and inline-code
text all use `text`; H6 uses `text.muted`. The source-heading capture does not recolor rendered
headings. Code blocks also share the editor background. These are renderer
limits, not additional theme controls. See the [source mapping](theme-testing.md#vivid-comments-and-markdown--2026-10-24).

Terminal ANSI black and white retain their dark/light roles, including when used
as backgrounds. They are separate from the terminal's default text colors.

Debugger execution rows use green fills. Selected stack frames use pale leaf
green in Day Vivid and the original blue-cyan in dark variants; Zed shares that fill with
hovered frames and other controls using `element.hover`.

Day Vivid uses AA 4.5:1 on normal surfaces. The original dark variants target
AAA 7:1 for primary text and AA 4.5:1 for comments; colored text uses 4.5:1 on
diff rows while primary text retains 7:1. Expanded search/selection and rendered
Markdown measurements are advisory, with below-target pairs marked REVIEW.
Normal-surface and highlight-visibility requirements remain enforced; REVIEW
does not claim that every rendered or stacked state meets its text target.
See the generated [contrast report](contrast-report.md) and [checks](theme-testing.md).

[Screenshots](screenshots/README.md) show the current palette in Zed 1.25.3 on
macOS 27.0.1: 24 English captures across six scenes and all four variants,
refreshed on 2026-10-25 with embedded sRGB profiles. The Day Vivid editor overview
uses the user's preferred local Color LCD capture; the other images are from LG.
File icons belong to the capture setup. Physical-display acceptance remains
separate from the [screenshot comparison](../human-todo.md#截图与跨电脑色差).

The 2026-10-23 palette has code review and automated color checks. The user
confirmed the sage background and selected text from their own screenshots.
The user then clarified that earlier feedback described a cached, unreloaded
theme and requested another rollback, scoped to Day Vivid only. That rollback
restored the earlier colors and lighter typography. Follow-up adjustments affect
only Vivid's colored syntax and UI/file-list foregrounds. Its sage surfaces and
green selection fills are retained. An initial
scope check compared only the latest rollback and missed earlier dark-theme
edits. The three dark variants have now been restored exactly to the original
session snapshot, also verified against HEAD. The user approved the Vivid
appearance committed as `7652d97` on 2026-10-23, then requested the orange
property follow-up. The user confirmed the orange properties felt more
comfortable and authorized delivery on 2026-10-23. At that stage, no final computer-use
testing was performed at the user's request. The 2026-10-25 screenshot refresh
now illustrates the current palette. The four global overrides introduced during this
work (UI family/weight, editor weight and unnecessary-code fading) were removed.
The settings file matches the session-start snapshot; font sizes and theme
selection are preserved. Only Day Vivid differs from the original theme family.
The user reported that the 2026-10-24 comment/Markdown appearance looked good.
The user also approved the final rose hover-fill adjustment and requested a
commit on 2026-10-24. That step used no computer-use checks or global settings changes.
The subsequent keyword color-only adjustment is now shown in the 2026-10-25
LG-display captures as well as the static audit. A controlled comparison on the
MacBook Air and dimmer LG display is still pending.
