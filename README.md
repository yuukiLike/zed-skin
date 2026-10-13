# GreenTree

Green-focused, high contrast themes for Zed: one light and three dark variants.

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![GreenTree Midnight AAA in Zed](docs/screenshots/midnight.jpg)](docs/screenshots/midnight.jpg)

| Theme | Appearance |
| --- | --- |
| **Day Vivid** | Warm ivory, vivid green, violet and pink |
| **Day AAA** | Deep indigo with bright syntax colors |
| **Night AAA** | Near black, soft white and regular green keywords |
| **Midnight AAA** | Pure black, bright white and bold green keywords |

More screenshots: [Day Vivid](docs/screenshots/day-vivid.jpg) · [Day AAA](docs/screenshots/day-aaa.jpg) · [Night AAA](docs/screenshots/night.jpg).

## Install

In Zed's **Extensions**, search for **[GreenTree](https://zed.dev/extensions/green-tree-theme)** and install it. Run **`theme selector: toggle`** and choose a variant.

For manual installation, download [green-tree.json](themes/green-tree.json) into:

| Platform | Folder |
| --- | --- |
| macOS / Linux | `~/.config/zed/themes/` |
| Windows | `%USERPROFILE%\AppData\Roaming\Zed\themes\` |

Create the folder if needed, then reopen the theme selector. [Zed's theme guide](https://zed.dev/docs/themes).

Dark variants target AAA 7:1 for primary text and AA 4.5:1 for comments. Search and selections share a blue hue and prioritize appearance and visibility, with no text contrast target. Day Vivid's green uses a custom 2.5:1 floor, below AA. These are palette targets, not whole-editor certification.

Dependency-free [checks](docs/theme-testing.md) cover search, selections, lists, Git diffs/conflicts, symbols, brackets and ANSI black/white pairs.

[Manual QA](human-todo.md) · [Contrast report](docs/contrast-report.md) · [Palette notes](docs/palette-review.md) · [MIT License](LICENSE)
