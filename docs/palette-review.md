# Palette notes

- **Day Vivid:** warm ivory `#F3EFE5` with green `#009843`, blue, violet and pink.
  Green was slightly darkened to keep selected Markdown above the custom 2.5:1 floor.
- **Day AAA:** deep indigo `#1C2135` with bright syntax colors.
- **Night AAA:** near black `#050505`, soft white and regular green keywords.
- **Midnight AAA:** pure black `#000000`, bright white and bold green keywords.

Dark search results use blue for the current match and violet for other matches;
Day Vivid uses cyan and yellow. Translucent blue editor selections preserve the
search color underneath. Dark Markdown selections use a warm neutral overlay to
remain readable with both old and current paint order. Comments are italic gray,
lightened where necessary for search and selection stacking.

Dark primary text targets AAA 7:1; comments, search and selected text use AA 4.5:1.
Day Vivid's green syntax and selected Markdown use a custom 2.5:1 floor, below AA.
See the generated [contrast report](contrast-report.md) and [checks](theme-testing.md).

[Screenshots](screenshots/) show version 0.11.0 (`f0c745e`) in Zed 1.21.0 on macOS,
using [tree.ts](../examples/tree.ts). They predate the search/selection changes and
are original 1922 × 1944 captures. File icons belong to the user's Zed setup.
