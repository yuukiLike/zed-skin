# Palette notes

- **Day Vivid:** soft sage `#DCE4D6` with near-black variables `#090D12`, leaf
  green keywords `#00551C`, royal-blue calls `#1234BF`, orchid types `#8500A9`,
  raspberry values `#A00052` and burnt-orange strings `#803B00`. Properties use
  deep teal `#003642`, italic comments use slate blue-gray `#4E5262`, and
  punctuation uses neutral slate `#41464D`. Color categories differ in both hue
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

On the sage editor background, keyword contrast increases from 5.88:1 to
6.96:1 while retaining the leaf-green hue; comments reach 5.95:1. The existing
4.5:1 requirements remain enforced on normal and diff surfaces. The closest
pair among eight primary syntax roles increases from 0.1046 to 0.1339 Oklab
distance. Properties separate from green keywords, and comments separate from
violet types and near-black variables. This is a relative palette measurement,
not a guarantee of visual acceptance.

Day Vivid's lists and symbol/bracket highlights use leaf green, with matching
focus borders, active indent guides and line numbers. Its selected row is
`#B4D8AA`, distinct from its `#D3E9AD` hover. The user approved the current-file
highlight; these UI colors remain unchanged in the syntax-category adjustment.
Git diffs use soft mint green
for additions and coral/rose for deletions, with matching gutters and hollow
borders. Changed words use brighter translucent green/red fills over lightly
tinted rows, preserving search underneath. The dark palettes retain their
original blue/cyan lists, symbol highlights, word fills and cursor colors.
Vivid's secondary UI/file-list text uses forest green `#2D412F`; added-file
labels and green UI accents use `#0B4722`. These shared UI colors also apply to
menus, status labels and debugger text. File lists retain their existing weight.
Secondary text reaches 7.79:1 on the panel and 6.99:1 on the selected row;
added-file text reaches 7.67:1 and 6.88:1, respectively. Conflict
sides use blue/green in dark themes and muted blue/yellow in Day Vivid.
Read/write references share one color;
they identify occurrences without distinguishing access type.

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

[Screenshots](screenshots/README.md) show version 0.11.2 in Zed 1.24.2 on macOS:
24 original English captures covering code, Markdown, search/selection, a live
debugger, Git diffs and terminal colors in all four variants. The READMEs use
small clickable previews and collapsible galleries. File icons belong to the
user's Zed setup.

The 2026-10-23 palette has code review and automated color checks. The user
confirmed the sage background and selected text from their own screenshots.
The user then clarified that earlier feedback described a cached, unreloaded
theme and requested another rollback, scoped to Day Vivid only. That rollback
restored the earlier colors and lighter typography. Follow-up adjustments affect
only Vivid's colored syntax and UI/file-list foregrounds. Its sage surfaces and
green selection fills are retained. An initial
scope check compared only the latest rollback and missed earlier dark-theme
edits. The three dark variants have now been restored exactly to the original
session snapshot, also verified against HEAD. The user approved the final Vivid
appearance on 2026-10-23 and requested a commit. No final computer-use testing
was performed at the user's request. Published screenshots
show the previous palette. The four global overrides introduced during this
work (UI family/weight, editor weight and unnecessary-code fading) were removed.
The settings file matches the session-start snapshot; font sizes and theme
selection are preserved. Only Day Vivid differs from the original theme family.
