# GreenTree

緑を基調とした Zed 向けの高コントラストテーマ。ライト 1 種とダーク 3 種を用意しています。

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![Zed 上の GreenTree Midnight AAA](docs/screenshots/midnight.jpg)](docs/screenshots/midnight.jpg)

| テーマ | 配色 |
| --- | --- |
| **Day Vivid** | 暖かな白、鮮やかな緑、紫とピンク |
| **Day AAA** | 深いインディゴと明るい構文色 |
| **Night AAA** | 黒に近い背景、柔らかな白、標準の太さの緑 |
| **Midnight AAA** | 純黒、明るい白、太字の緑のキーワード |

その他の画像：[Day Vivid](docs/screenshots/day-vivid.jpg) · [Day AAA](docs/screenshots/day-aaa.jpg) · [Night AAA](docs/screenshots/night.jpg)。

## インストール

Zed の **Extensions** で **[GreenTree](https://zed.dev/extensions/green-tree-theme)** を検索してインストールし、**`theme selector: toggle`** でテーマを選びます。

手動の場合は [green-tree.json](themes/green-tree.json) を次のフォルダに保存してください。

| OS | フォルダ |
| --- | --- |
| macOS / Linux | `~/.config/zed/themes/` |
| Windows | `%USERPROFILE%\AppData\Roaming\Zed\themes\` |

フォルダがなければ作成し、テーマ選択画面を開き直します。[Zed 公式ガイド](https://zed.dev/docs/themes)。

ダークテーマは主要な文字に AAA 7:1、コメントに AA 4.5:1 を目標とします。検索と選択範囲は青で統一し、見た目と識別しやすさを優先して、文字のコントラスト基準は設けません。Day Vivid の緑は独自の下限 2.5:1 で、AA を満たしません。配色の目標であり、エディタ全体の認証ではありません。

追加依存なしの[検証](docs/theme-testing.md)は、検索・選択範囲・リスト・Git 差分と競合・シンボル参照・括弧・ANSI の黒と白の組み合わせを対象にします。

[手動検証](human-todo.md) · [コントラストレポート](docs/contrast-report.md) · [配色メモ](docs/palette-review.md) · [MIT ライセンス](LICENSE)
