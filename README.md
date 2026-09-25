# GreenTree

A high contrast theme collection for Zed. **Day AAA, Night AAA and Midnight AAA meet the WCAG AAA text contrast target of 7:1 in the included palette audit.** Warm-white Day Vivid prioritizes brighter colors; its vivid green syntax does not meet AA or AAA.

Green keywords, sky-blue functions, violet types and warm accents help distinguish code without tinting the whole interface green.

| Theme | Appearance | Minimum audited text contrast |
| --- | --- | ---: |
| **GreenTree Day Vivid** | Warm ivory, vivid green, blue-cyan fields, pink numbers | 2.7265:1; other text ≥ 4.5:1 |
| **GreenTree Day AAA** | Indigo with vivid green, sky blue and violet | 7.0721:1 |
| **GreenTree Night AAA** | Deep black, soft white, regular green, orange cursor | 7.3059:1 |
| **GreenTree Midnight AAA** | Pure black, white filenames, bold green, blue functions and rose-pink `this` | 8.2937:1 |

Day Vivid is the light theme. Day AAA, Night and Midnight are dark themes. The AAA label describes audited color pairs, not certification of the whole editor.

## Install locally

Clone the repository and copy the theme file:

```sh
git clone https://github.com/yuukiLike/zed-skin.git
cd zed-skin
mkdir -p ~/.config/zed/themes
cp -i themes/green-tree.json ~/.config/zed/themes/
```

On Windows, copy the JSON file to `%USERPROFILE%\AppData\Roaming\Zed\themes\`.

In Zed, run `theme selector: toggle` and search for **GreenTree**. On macOS, the shortcut is `⌘K`, then `⌘T`; on Linux and Windows, use `Ctrl+K`, then `Ctrl+T`.

To follow your system appearance, merge this field into your existing Zed settings:

```json
{
  "theme": {
    "mode": "system",
    "light": "GreenTree Day Vivid",
    "dark": "GreenTree Night AAA"
  }
}
```

The extension manifest is included for local development. Marketplace publication is being prepared; the theme is not listed there yet. See the official [theme installation guide](https://zed.dev/docs/themes).

## Verify the palette

```sh
python3 scripts/check_contrast.py
python3 scripts/check_contrast.py --report docs/contrast-report.md
```

The dependency-free audit checks **45,460 foreground/background pairs** across all four themes, including syntax, UI text, selections, search, diff, terminal foregrounds and cursors. It uses unrounded WCAG sRGB contrast ratios. Day Vivid's six green syntax captures use an explicit custom 2.5:1 floor; this is **not a WCAG text threshold**. All other Day Vivid text is checked at 4.5:1, the three AAA variants at 7:1, and key non-text indicators at 3:1.

See the [contrast report](docs/contrast-report.md), [palette history](docs/palette-review.md) and [TypeScript example](examples/tree.ts). Runtime fading, user overrides, plugins and terminal applications can change the rendered result. A color audit does not establish keyboard accessibility, screen-reader support or reading comfort.

## License

[MIT](LICENSE) © 2026 yuukiLike.
