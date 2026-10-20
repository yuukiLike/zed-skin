# Palette notes

- **Day Vivid:** warm ivory `#F3EFE5` with green `#009843`, blue, violet and pink.
- **Day AAA:** deep indigo `#1C2135` with bright syntax colors.
- **Night AAA:** near black `#050505`, soft white and regular green keywords.
- **Midnight AAA:** pure black `#000000`, bright white and bold green keywords.

All variants use a stronger version of the Markdown selection blue for search:
`#408CFF80` (about 50%) for the current match and `#408CFF4D` (about 30%) for other
matches. Markdown selections retain `#408CFF66` (40%); local editor selections use
`#408CFF40` (about 25%), preserving search underneath. Affected cursors are darker
in Day Vivid and lighter in the dark variants to stay visible over the stronger
combined overlays. Comments are italic gray.

Lists and symbol/bracket highlights use blue/cyan. Git diffs use soft mint green
for additions and coral/rose for deletions, with matching gutters and hollow
borders. Changed words use brighter translucent green/red fills over lightly
tinted rows, preserving search underneath. Dark variants brighten their cursors
to remain visible over these overlays. Day Vivid slightly deepens affected text
colors to retain its existing contrast targets. Conflict sides use blue/green in
dark themes and cyan/yellow in Day Vivid. Read/write references share one color;
they identify occurrences without distinguishing access type.

Terminal ANSI black and white retain their dark/light roles, including when used
as backgrounds. They are separate from the terminal's default text colors.

Debugger execution rows use mint/green fills. Selected stack frames use pale mint
in Day Vivid and blue-cyan in the dark variants; Zed 1.24.2 shares that fill with
hovered frames and other controls using `element.hover`.

Dark primary text targets AAA 7:1, including Git highlights. Colored syntax/status
text targets 7:1 on normal surfaces and AA 4.5:1 on diff rows and changed words;
this lets those overlays use brighter colors. Comments use AA 4.5:1.
Search and selections prioritize appearance and visibility, with no text contrast target.
Day Vivid's green syntax uses a custom 2.5:1 floor, below AA.
See the generated [contrast report](contrast-report.md) and [checks](theme-testing.md).

[Screenshots](screenshots/README.md) show version 0.11.2 in Zed 1.24.2 on macOS:
24 original English captures covering code, Markdown, search/selection, a live
debugger, Git diffs and terminal colors in all four variants. The READMEs use
small clickable previews and collapsible galleries. File icons belong to the
user's Zed setup.
