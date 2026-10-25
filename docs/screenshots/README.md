# Screenshot gallery

The three READMEs share 24 English screenshots: six scenes in each of GreenTree's
four variants. They were refreshed on **2026-10-25** in **Zed 1.25.3 on macOS
27.0.1**, using the palette at
[`7caf432`](https://github.com/yuukiLike/zed-skin/commit/7caf43209904ce663f0f2e9fbe0f154a0b85bfc1).
The extension remains **0.11.2**; existing image URLs, including `v0.11.2/`, are retained.
The captured theme matches `themes/green-tree.json`, SHA-256
`5413a3e9f66776768c2b0b73a741fd2aad5d14194c12deb39485dba7cc6fa838`.

## Capture sources

| Images | Display | Dimensions | Native ICC |
| --- | --- | --- | --- |
| Day Vivid editor overview | Built-in Color LCD | 2880 × 1678 | Display |
| Other 23 images | LG ULTRAFINE | 3840 × 1938 | LG ULTRAFINE |

The Day Vivid overview uses the local capture selected by the user after a
same-screen comparison. It shows the same code sample in a separate window with
the regular Zed profile (editor/UI sizes 15/20). The LG session used isolated
user data and a small Git fixture (editor/UI sizes 17/18; terminal size 16).
No theme fields, regular Zed settings or display settings were changed.

Published JPEGs are converted from each source ICC to embedded sRGB, at quality
95 without chroma subsampling. There is no resizing, compositing or manual
recoloring. File icons, pointer indicators and window decorations belong to the
capture environment.

| Scene | Midnight AAA | Night AAA | Day AAA | Day Vivid |
| --- | --- | --- | --- | --- |
| TypeScript editor | [View](midnight.jpg) | [View](night.jpg) | [View](day-aaa.jpg) | [View](day-vivid.jpg) |
| Paused debugger | [View](v0.11.2/midnight-debugger.jpg) | [View](v0.11.2/night-debugger.jpg) | [View](v0.11.2/day-aaa-debugger.jpg) | [View](v0.11.2/day-vivid-debugger.jpg) |
| Markdown preview | [View](v0.11.2/midnight-markdown.jpg) | [View](v0.11.2/night-markdown.jpg) | [View](v0.11.2/day-aaa-markdown.jpg) | [View](v0.11.2/day-vivid-markdown.jpg) |
| Search and selection | [View](v0.11.2/midnight-search-selection.jpg) | [View](v0.11.2/night-search-selection.jpg) | [View](v0.11.2/day-aaa-search-selection.jpg) | [View](v0.11.2/day-vivid-search-selection.jpg) |
| Git diff | [View](v0.11.2/midnight-git-diff.jpg) | [View](v0.11.2/night-git-diff.jpg) | [View](v0.11.2/day-aaa-git-diff.jpg) | [View](v0.11.2/day-vivid-git-diff.jpg) |
| Terminal and ANSI colors | [View](v0.11.2/midnight-terminal.jpg) | [View](v0.11.2/night-terminal.jpg) | [View](v0.11.2/day-aaa-terminal.jpg) | [View](v0.11.2/day-vivid-terminal.jpg) |

The debugger shows a live Node.js pause at `debugger;`, with a green execution
row, breakpoint, inline values, selected frame and locals. Git views show actual
uncommitted changes. Terminal captures include normal/bright/dim ANSI, reverse
video and Zed's enabled contrast adjustment. These scenes do not replace the
broader [regression checks](../theme-testing.md).

Originals and capture evidence stay Git-ignored under
`.local/readme-refresh-2026-10-25/` (LG session, on the capture computer) and
`.local/display-comparison-2026-10-25/` (local capture and comparison).

## Color across computers

The LG Vivid overview and local capture were compared after ICC conversion to
sRGB. A 120,000-pixel flat-background sample measured `(220, 228, 213)` for LG
and `(221, 228, 215)` for the local lossless conversion. The local published JPEG
measures `(221, 227, 215)` after encoding; the theme specifies `(220, 228, 214)`.
Nine syntax samples differed by at most 5/255 per-channel median before that
final export. These are sampled file pixels, including antialiasing and JPEG
effects; they do not establish whole-image equality or physical-display accuracy.

Retain original ICC profiles, then convert pixels to sRGB rather than replacing
the profile label. Identical files can still look different across physical
displays. See [Apple's color-management explanation](https://developer.apple.com/library/archive/technotes/tn2313/_index.html)
and the [physical-display checklist](../../human-todo.md#截图与跨电脑色差).
