# GreenTree

绿系高对比度 Zed 主题，提供一款浅色和三款深色外观。

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![Zed 中的 GreenTree Midnight AAA](docs/screenshots/midnight.jpg)](docs/screenshots/midnight.jpg)

| 主题 | 外观 |
| --- | --- |
| **Day Vivid** | 暖白、鲜绿、紫色与粉色 |
| **Day AAA** | 深靛蓝背景，鲜亮语法颜色 |
| **Night AAA** | 深黑、柔和白色、常规绿色关键字 |
| **Midnight AAA** | 纯黑、亮白、加粗绿色关键字 |

更多截图：[Day Vivid](docs/screenshots/day-vivid.jpg) · [Day AAA](docs/screenshots/day-aaa.jpg) · [Night AAA](docs/screenshots/night.jpg)。

## 安装

在 Zed 的 **Extensions** 中搜索并安装 **[GreenTree](https://zed.dev/extensions/green-tree-theme)**，运行 **`theme selector: toggle`** 选择外观。

手动安装可将 [green-tree.json](themes/green-tree.json) 下载到：

| 平台 | 目录 |
| --- | --- |
| macOS / Linux | `~/.config/zed/themes/` |
| Windows | `%USERPROFILE%\AppData\Roaming\Zed\themes\` |

目录不存在时先创建，再打开主题选择器。[Zed 官方指南](https://zed.dev/docs/themes)。

深色主题以 AAA 7:1 为主要文字目标，注释、搜索采用 AA 4.5:1。选区优先考虑观感与辨识度，不设文字对比度门槛。Day Vivid 的绿色采用自定义 2.5:1 下限，低于 AA。这些是配色目标，不代表整个编辑器获得认证。

无需额外依赖的[检查](docs/theme-testing.md)覆盖搜索、选区、列表、Git 差异与冲突、符号引用、括号和 ANSI 黑白配对。

[人工验收](human-todo.md) · [对比度报告](docs/contrast-report.md) · [配色说明](docs/palette-review.md) · [MIT 许可证](LICENSE)
