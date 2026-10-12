# Palette notes

- **Day Vivid:** warm ivory `#F3EFE5` with green `#009843`, blue, violet and pink.
- **Day AAA:** deep indigo `#1C2135` with bright syntax colors.
- **Night AAA:** near black `#050505`, soft white and regular green keywords.
- **Midnight AAA:** pure black `#000000`, bright white and bold green keywords.

Dark search results use blue for the current match and violet for other matches;
Day Vivid uses cyan and yellow. Translucent blue editor selections preserve the
search color underneath. Markdown selections use a clearer blue overlay
(`#408CFF66`, 40% opacity). Comments are italic gray.

Lists and symbol/bracket highlights use blue/cyan. Changed words use translucent
blue (dark) or yellow (light), preserving search underneath. Diff gutters and row
backgrounds identify additions/deletions. Conflict sides use blue/green in dark
themes and cyan/yellow in Day Vivid. Read/write references share one color; they
identify occurrences without distinguishing access type.

Terminal ANSI black and white retain their dark/light roles, including when used
as backgrounds. They are separate from the terminal's default text colors.

Dark primary text targets AAA 7:1; comments and search use AA 4.5:1.
Selections prioritize appearance and visibility, with no text contrast target.
Day Vivid's green syntax uses a custom 2.5:1 floor, below AA.
See the generated [contrast report](contrast-report.md) and [checks](theme-testing.md).

[Screenshots](screenshots/) show version 0.11.0 (`f0c745e`) in Zed 1.21.0 on macOS,
using [tree.ts](../examples/tree.ts). They predate the interaction changes and
are original 1922 × 1944 captures. File icons belong to the user's Zed setup.
