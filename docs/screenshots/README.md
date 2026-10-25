# Screenshot gallery

The English, Chinese and Japanese READMEs share these 24 English screenshots:
six scenes in each of GreenTree's four variants. The editor overviews are visible
immediately. The other five scenes each have a collapsible two-column comparison,
ordered Midnight AAA, Night AAA, Day AAA, Day Vivid. The comparison images fill
their columns without a fixed pixel width. Every preview links to its original.
Theme links above the overview provide quick navigation between the four variants.

All 24 images were refreshed on **2026-10-25** in **Zed 1.25.3 on macOS
27.0.1**, using the repository palette at
[`7caf432`](https://github.com/yuukiLike/zed-skin/commit/7caf43209904ce663f0f2e9fbe0f154a0b85bfc1).
This includes the latest Day Vivid keywords, orange properties, muted plum
comments and Markdown accents. The extension metadata is still **0.11.2**; the
existing image URLs, including the `v0.11.2/` folder, are retained.

Each scene uses the same English sample and layout across all four variants.
All images are **3840 × 1938**. Native JPEG originals carry the capture display's
**LG ULTRAFINE** ICC profile. The published JPEGs are converted from that profile
to **sRGB IEC61966-2.1**, with the sRGB ICC profile embedded and JPEG quality 95
without chroma subsampling. There is no manual recoloring, compositing or resizing.
The originals remain untouched in the ignored local evidence folder. File icons,
pointer/input indicators and window decorations belong to the capture environment,
not the theme extension.

The capture session uses a separate Zed user-data directory and a small local Git
repository. Editor/UI font sizes are 17/18; terminal font size is 16. The theme
file is an exact copy of `themes/green-tree.json`, SHA-256
`5413a3e9f66776768c2b0b73a741fd2aad5d14194c12deb39485dba7cc6fa838`.
The regular Zed configuration and display settings were not changed.

| Scene | Midnight AAA | Night AAA | Day AAA | Day Vivid |
| --- | --- | --- | --- | --- |
| TypeScript editor | [View](midnight.jpg) | [View](night.jpg) | [View](day-aaa.jpg) | [View](day-vivid.jpg) |
| Paused debugger | [View](v0.11.2/midnight-debugger.jpg) | [View](v0.11.2/night-debugger.jpg) | [View](v0.11.2/day-aaa-debugger.jpg) | [View](v0.11.2/day-vivid-debugger.jpg) |
| Markdown preview | [View](v0.11.2/midnight-markdown.jpg) | [View](v0.11.2/night-markdown.jpg) | [View](v0.11.2/day-aaa-markdown.jpg) | [View](v0.11.2/day-vivid-markdown.jpg) |
| Search and selection | [View](v0.11.2/midnight-search-selection.jpg) | [View](v0.11.2/night-search-selection.jpg) | [View](v0.11.2/day-aaa-search-selection.jpg) | [View](v0.11.2/day-vivid-search-selection.jpg) |
| Git diff | [View](v0.11.2/midnight-git-diff.jpg) | [View](v0.11.2/night-git-diff.jpg) | [View](v0.11.2/day-aaa-git-diff.jpg) | [View](v0.11.2/day-vivid-git-diff.jpg) |
| Terminal and ANSI colors | [View](v0.11.2/midnight-terminal.jpg) | [View](v0.11.2/night-terminal.jpg) | [View](v0.11.2/day-aaa-terminal.jpg) | [View](v0.11.2/day-vivid-terminal.jpg) |

The debugger shows a live Node.js session paused at `debugger;`, with an enabled
breakpoint, inline values, the selected stack frame and local variables. The Git
view shows actual uncommitted changes. The terminal shows real normal, bright
and dim ANSI output, black/white backgrounds, reverse video, Node.js output and
`git diff` output. Zed's terminal contrast adjustment remains enabled; the image
therefore includes the editor's adjustment of Day Vivid's black-on-green text.

These previews illustrate everyday appearance; the broader regression coverage
and its limitations are documented in [Theme checks](../theme-testing.md).
The original 24 captures, setup attempts, isolated demonstration workspace,
conversion script and per-image hashes/profile measurements remain Git-ignored
under `.local/readme-refresh-2026-10-25/`. The debug session was stopped and the
isolated editor instance closed after capture.

## Color across computers

Embedding sRGB makes the published images easier to interpret consistently,
but it cannot guarantee identical appearance on every physical display.
The original LG-profile Vivid screenshot's flat editor background is
approximately RGB `(216, 224, 209)`; after conversion to sRGB it is
`(220, 228, 213)`, close to the theme's `#DCE4D6` / `(220, 228, 214)`.
The one-level difference is consistent with the JPEG capture/export precision;
this is a file-pixel check, not a measurement of the physical display.
RGB numbers from different ICC spaces should not be compared directly.
[Apple's color-management explanation](https://developer.apple.com/library/archive/technotes/tn2313/_index.html)
describes why the profile is part of the color's meaning.

For future captures, retain the original file and its ICC profile, preferably
as lossless PNG, then convert pixels to sRGB before embedding the target profile.
Assigning a new profile without conversion changes the interpretation of the
existing pixels. Avoid chat-app recompression for color comparisons.
The [cross-computer checklist](../../human-todo.md#截图与跨电脑色差) separates
file differences from display differences. Only this Mac/LG setup was exercised;
a second computer and calibrated side-by-side display measurements remain pending.
