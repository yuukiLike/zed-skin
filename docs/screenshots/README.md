# Screenshot gallery

The English, Chinese and Japanese READMEs share these 24 English screenshots:
six scenes in each of GreenTree's four variants. The editor overviews are visible
immediately. The other five scenes each have a collapsible two-column comparison,
ordered Midnight AAA, Night AAA, Day AAA, Day Vivid. The comparison images fill
their columns without a fixed pixel width. Every preview links to its original.
Theme links above the overview provide quick navigation between the four variants.

Captured on 2026-10-17 with GreenTree **0.11.2** in **Zed 1.24.2 on macOS**.
Each scene uses the same English sample and layout across all four variants.
These are original native JPEG captures, with no recoloring or compositing.
Code, Markdown, search and debugger images are 3800 × 1902; Git and terminal
images are 3840 × 1938. File icons and the window's screen-sharing indicator
belong to the capture environment, not the theme extension.

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

These previews replace the 0.11.0 overview images while retaining their existing
URLs. They illustrate everyday appearance; the broader regression coverage and
its limitations are documented in [Theme checks](../theme-testing.md). Full QA
evidence, capture attempts and the isolated demonstration workspace remain in
the Git-ignored local `.local/` directory.
