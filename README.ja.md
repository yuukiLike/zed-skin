# GreenTree

Zed 向けの高コントラストテーマ集です。3 つのダークテーマは[配色監査](docs/contrast-report.md)で **WCAG AAA の文字コントラスト目標 7:1** を満たしています。明るい色を優先した、暖かな白背景の Day Vivid も用意しました。

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![Zed 上の GreenTree Midnight AAA](docs/screenshots/midnight.jpg)](docs/screenshots/midnight.jpg)

*Midnight AAA — 黒い背景、白いファイル名、太字の緑のキーワードとスカイブルーの関数。*

## 4 つのテーマ

| テーマ | 特徴 | 監査した文字の最低コントラスト比 |
| --- | --- | ---: |
| **Day Vivid** | 暖かなアイボリー · 鮮やかな緑 · 紫 · ピンク | 2.73:1 |
| **Day AAA** | 深いインディゴ · 鮮やかな配色 | 7.07:1 |
| **Night AAA** | 深い黒 · 柔らかな白 · 標準の太さの緑 | 7.31:1 |
| **Midnight AAA** | 純黒 · 明るい白 · 太字のアクセント | 8.29:1 |

Day Vivid は明るい背景で鮮やかな緑を優先するため、緑の文字は **AA・AAA を満たしません**。その他の監査対象の文字は 4.5:1 以上です。AAA 表記は検証済みの色の組み合わせを示し、エディタ全体のアクセシビリティ認証ではありません。

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
