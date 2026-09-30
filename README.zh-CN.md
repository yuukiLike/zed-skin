# GreenTree

一组为 Zed 设计的高对比度主题。三款深色主题在[配色审计](docs/contrast-report.md)中以 **WCAG AAA 7:1 为主要文字目标**，**注释与 Markdown 选中文字采用 AA 4.5:1**。另有优先鲜亮感的暖白 Day Vivid。

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![Zed 中的 GreenTree Midnight AAA](docs/screenshots/midnight.jpg)](docs/screenshots/midnight.jpg)

*Midnight AAA — 纯黑背景、亮白文件名、加粗绿色关键字与天蓝函数。*

## 四种外观

| 主题 | 风格 | 审计最低文字对比度 |
| --- | --- | ---: |
| **Day Vivid** | 暖白 · 鲜绿 · 紫色 · 粉色 | 2.52:1 |
| **Day AAA** | 深靛蓝 · 鲜亮语法 | 4.72:1 |
| **Night AAA** | 深黑 · 柔和白色 · 常规绿色字重 | 4.71:1 |
| **Midnight AAA** | 纯黑 · 亮白 · 加粗重点语法 | 4.60:1 |

最低值包含注释和 Markdown 选中状态。名称中的 AAA 指主要文字目标，不代表所有状态或整个编辑器获得认证。Day Vivid 的鲜绿及部分选中状态**不满足 AA 或 AAA**。语言服务器对未使用代码的淡化不在审计范围内。

<details>
<summary>Day Vivid — 暖白与鲜亮色彩</summary>

[![Zed 中的 GreenTree Day Vivid](docs/screenshots/day-vivid.jpg)](docs/screenshots/day-vivid.jpg)

</details>

<details>
<summary>Day AAA — 深靛蓝与高对比</summary>

[![Zed 中的 GreenTree Day AAA](docs/screenshots/day-aaa.jpg)](docs/screenshots/day-aaa.jpg)

</details>

<details>
<summary>Night AAA — 柔和的夜间配色</summary>

[![Zed 中的 GreenTree Night AAA](docs/screenshots/night.jpg)](docs/screenshots/night.jpg)

</details>

*以上均为 Zed 实际截图，点击图片可查看原始分辨率。*

## 安装

在 Zed 中打开 **Extensions**（macOS：`Cmd+Shift+X`；Linux / Windows：`Ctrl+Shift+X`），搜索 **GreenTree** 并安装。运行 **`theme selector: toggle`**，选择四款 GreenTree 主题之一。[扩展市场页面](https://zed.dev/extensions/green-tree-theme)。

### 手动安装

下载 [green-tree.json](https://raw.githubusercontent.com/yuukiLike/zed-skin/main/themes/green-tree.json)，复制到：

| 平台 | 目录 |
| --- | --- |
| macOS / Linux | `~/.config/zed/themes/` |
| Windows | `%USERPROFILE%\AppData\Roaming\Zed\themes\` |

目录不存在时先创建。在 Zed 中运行 **`theme selector: toggle`**，搜索 **GreenTree**。新名称未出现时重启 Zed。[官方指南](https://zed.dev/docs/themes)。

[对比度报告](docs/contrast-report.md) · [配色说明](docs/palette-review.md) · [MIT 许可证](LICENSE)
