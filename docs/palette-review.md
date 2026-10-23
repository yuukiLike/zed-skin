# Palette notes

- **Day Vivid:** soft sage `#DCE4D6` with dark gray-green text `#202820`, leaf
  green `#185C28`, blue `#174299`, pink `#8A1F58`, orange `#744000` and violet.
  Comments use gray-green `#3E4A39`. This restores the palette before the broad
  foreground darkening and heavier typography.
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

Day Vivid's lists and symbol/bracket highlights use leaf green, with matching
focus borders, active indent guides and line numbers. Its selected row is
`#B4D8AA`, distinct from its `#D3E9AD` hover. Git diffs use soft mint green
for additions and coral/rose for deletions, with matching gutters and hollow
borders. Changed words use brighter translucent green/red fills over lightly
tinted rows, preserving search underneath. The dark palettes retain their
original blue/cyan lists, symbol highlights, word fills and cursor colors.
Day Vivid keeps its earlier foregrounds on sage base surfaces. Conflict
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
theme and requested another rollback, scoped to Day Vivid only. Vivid now uses
the saved colors and lighter typography from before the broad readability
revision. Its sage surfaces and green selection fills are retained. An initial
scope check compared only the latest rollback and missed earlier dark-theme
edits. The three dark variants have now been restored exactly to the original
session snapshot, also verified against HEAD. Overall visual acceptance is still
pending. No final
computer-use testing was performed at the user's request. Published screenshots
show the previous palette. The four global overrides introduced during this
work (UI family/weight, editor weight and unnecessary-code fading) were removed.
The settings file matches the session-start snapshot; font sizes and theme
selection are preserved. Only Day Vivid differs from the original theme family.
