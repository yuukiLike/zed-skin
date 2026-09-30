# GreenTree

A high contrast theme collection for Zed. Three dark variants target **WCAG AAA 7:1 for primary text**, with **AA 4.5:1 for comments and Markdown selections** in the [palette audit](docs/contrast-report.md). Warm-white Day Vivid favors brighter colors.

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![GreenTree Midnight AAA in Zed](docs/screenshots/midnight.jpg)](docs/screenshots/midnight.jpg)

*Midnight AAA — pure black, white filenames, bold green keywords and sky-blue functions.*

## Four themes

| Theme | Feel | Minimum audited text contrast |
| --- | --- | ---: |
| **Day Vivid** | Warm ivory · vivid green · violet · pink | 2.52:1 |
| **Day AAA** | Deep indigo · vivid colors | 4.72:1 |
| **Night AAA** | Deep black · soft white · regular green | 4.71:1 |
| **Midnight AAA** | Pure black · bright white · bold accents | 4.60:1 |

Minimums include comments and Markdown selections. The AAA names refer to primary text, not every state or certification of the editor. Day Vivid's bright green and some selections do **not** meet AA or AAA. Language-server fading is outside the audit.

<details>
<summary>Day Vivid — warm and colorful</summary>

[![GreenTree Day Vivid in Zed](docs/screenshots/day-vivid.jpg)](docs/screenshots/day-vivid.jpg)

</details>

<details>
<summary>Day AAA — indigo and vivid</summary>

[![GreenTree Day AAA in Zed](docs/screenshots/day-aaa.jpg)](docs/screenshots/day-aaa.jpg)

</details>

<details>
<summary>Night AAA — softer after dark</summary>

[![GreenTree Night AAA in Zed](docs/screenshots/night.jpg)](docs/screenshots/night.jpg)

</details>

*Actual Zed screenshots. Click any image for its original resolution.*

## Install

Open **Extensions** in Zed (`Cmd+Shift+X` on macOS or `Ctrl+Shift+X` on Linux/Windows), search **GreenTree**, and install it. Run **`theme selector: toggle`** and choose one of the four GreenTree themes. [Marketplace listing](https://zed.dev/extensions/green-tree-theme).

### Manual install

Download [green-tree.json](https://raw.githubusercontent.com/yuukiLike/zed-skin/main/themes/green-tree.json) and copy it into:

| Platform | Folder |
| --- | --- |
| macOS / Linux | `~/.config/zed/themes/` |
| Windows | `%USERPROFILE%\AppData\Roaming\Zed\themes\` |

Create the folder if needed. Run **`theme selector: toggle`** in Zed and search **GreenTree**. Restart Zed if the new names do not appear. [Official guide](https://zed.dev/docs/themes).

[Contrast report](docs/contrast-report.md) · [Palette notes](docs/palette-review.md) · [MIT License](LICENSE)
