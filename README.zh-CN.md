# GreenTree

一组为 Zed 设计的高对比度主题。三款深色主题在[配色审计](docs/contrast-report.md)中达到 **WCAG AAA 7:1 文字对比度目标**，另有优先鲜亮感的暖白 Day Vivid。

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![Zed 中的 GreenTree Midnight AAA](docs/screenshots/midnight.jpg)](docs/screenshots/midnight.jpg)

*Midnight AAA — 纯黑背景、亮白文件名、加粗绿色关键字与天蓝函数。*

## 四种外观

| 主题 | 风格 | 审计最低文字对比度 |
| --- | --- | ---: |
| **Day Vivid** | 暖白 · 鲜绿 · 紫色 · 粉色 | 2.73:1 |
| **Day AAA** | 深靛蓝 · 鲜亮语法 | 7.07:1 |
| **Night AAA** | 深黑 · 柔和白色 · 常规绿色字重 | 7.31:1 |
| **Midnight AAA** | 纯黑 · 亮白 · 加粗重点语法 | 8.29:1 |

Day Vivid 为了保留浅底鲜绿，绿色文字**不满足 AA 或 AAA**；其余已审计文字达到 4.5:1。AAA 标记描述已检查的颜色组合，不表示整个编辑器获得无障碍认证。

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

下载 [green-tree.json](https://raw.githubusercontent.com/yuukiLike/zed-skin/main/themes/green-tree.json)，复制到：

| 平台 | 目录 |
| --- | --- |
| macOS / Linux | `~/.config/zed/themes/` |
| Windows | `%USERPROFILE%\AppData\Roaming\Zed\themes\` |

目录不存在时先创建。在 Zed 中运行 **`theme selector: toggle`**，搜索 **GreenTree**。新名称未出现时重启 Zed。[官方指南](https://zed.dev/docs/themes)。

扩展市场上架正在准备中，目前请使用本地安装。

[对比度报告](docs/contrast-report.md) · [配色说明](docs/palette-review.md) · [MIT 许可证](LICENSE)
