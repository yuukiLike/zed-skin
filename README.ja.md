# GreenTree

Zed 向けの高コントラストテーマ集です。3 つのダークテーマは[配色監査](docs/contrast-report.md)で、**主要な文字は WCAG AAA の 7:1**、**コメントと Markdown の選択文字は AA の 4.5:1** を目標にしています。暖かな白背景の Day Vivid は鮮やかさを優先しています。

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![Zed 上の GreenTree Midnight AAA](docs/screenshots/midnight.jpg)](docs/screenshots/midnight.jpg)

*Midnight AAA — 黒い背景、白いファイル名、太字の緑のキーワードとスカイブルーの関数。*

## 4 つのテーマ

| テーマ | 特徴 | 監査した文字の最低コントラスト比 |
| --- | --- | ---: |
| **Day Vivid** | 暖かなアイボリー · 鮮やかな緑 · 紫 · ピンク | 2.52:1 |
| **Day AAA** | 深いインディゴ · 鮮やかな配色 | 4.72:1 |
| **Night AAA** | 深い黒 · 柔らかな白 · 標準の太さの緑 | 4.71:1 |
| **Midnight AAA** | 純黒 · 明るい白 · 太字のアクセント | 4.60:1 |

最低値にはコメントと Markdown の選択文字を含みます。名称の AAA は主要な文字の目標を示し、すべての状態への適合やエディタ全体の認証ではありません。Day Vivid の鮮やかな緑と一部の選択表示は **AA・AAA を満たしません**。言語サーバーによる未使用コードの淡色化は監査対象外です。

<details>
<summary>Day Vivid — 暖かな白と鮮やかな色</summary>

[![Zed 上の GreenTree Day Vivid](docs/screenshots/day-vivid.jpg)](docs/screenshots/day-vivid.jpg)

</details>

<details>
<summary>Day AAA — インディゴと高コントラスト</summary>

[![Zed 上の GreenTree Day AAA](docs/screenshots/day-aaa.jpg)](docs/screenshots/day-aaa.jpg)

</details>

<details>
<summary>Night AAA — 柔らかな夜の配色</summary>

[![Zed 上の GreenTree Night AAA](docs/screenshots/night.jpg)](docs/screenshots/night.jpg)

</details>

*Zed の実際のスクリーンショットです。画像をクリックすると元の解像度で表示できます。*

## インストール

[green-tree.json](https://raw.githubusercontent.com/yuukiLike/zed-skin/main/themes/green-tree.json) をダウンロードし、次のフォルダにコピーします。

| OS | フォルダ |
| --- | --- |
| macOS / Linux | `~/.config/zed/themes/` |
| Windows | `%USERPROFILE%\AppData\Roaming\Zed\themes\` |

フォルダがなければ作成してください。Zed で **`theme selector: toggle`** を実行し、**GreenTree** を検索します。新しい名前が表示されない場合は Zed を再起動してください。[公式ガイド](https://zed.dev/docs/themes)。

マーケットプレイスへの掲載は準備中です。現在はローカルでインストールしてください。

[コントラストレポート](docs/contrast-report.md) · [配色メモ](docs/palette-review.md) · [MIT ライセンス](LICENSE)
