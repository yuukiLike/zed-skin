# 人工验收

macOS / VS Code 键位（含本机自定义）；`⌘` = Command，`⇧` = Shift，`→` = 依次按。

**通用入口：`Command + Shift + P` 打开命令面板，输入下表的 `命令`；面板也会显示实际快捷键。**

四款主题逐一检查并截图，图片存至 `.local/human-qa/`。修改开发扩展后，在命令面板运行 `zed: rebuild dev extension`。

[Markdown 样例](examples/theme-checks.md) · [检查记录与限制](docs/theme-testing.md)

已确认：本次 Markdown 预览搜索高亮（2026-10-20）。

## 截图与跨电脑色差

截图文件相近不代表两块实体屏幕观感相同。[截图来源与测量结果](docs/screenshots/README.md#color-across-computers)。

- [x] 2026-10-25：将 LG 与本机 Color LCD 的 Vivid 截图按 ICC 转为 sRGB，在同一屏上比较。
  用户认为两者接近，更喜欢本机版本，并选择本机代码截图发布。
- [ ] MacBook Air 与 LG：使用相同主题和样例，记录版本、字体/字号、缩放及 ICC，复测绿色关键字与近黑变量。

1. 比较同一文件时先核对 SHA-256；分别截图时保留原图与 ICC，优先无损 PNG，转为 sRGB 后再同屏比较。避免聊天软件重压缩。
2. 实屏对比时暂停 True Tone、Night Shift、自动亮度和色彩滤镜，尽量匹配实际亮度与环境光；相同亮度百分比不代表相同亮度。
   这些显示效果不能仅凭截图验收。[Apple 显示工作流说明](https://support.apple.com/en-ca/guide/mac-help/mhlp275mr4b19/mac)。
3. 先看纯背景，再看字形内部与长期使用的可辨性、舒适度，避免将文字边缘抗锯齿当作主题色差。

记录：`电脑 / 显示器｜Zed 与主题哈希｜ICC / 亮度 / 环境｜同图观感｜同屏双图差异｜原图路径`。

## 功能验收

| 场景 | 入口 / 最短操作 | 看什么 |
| --- | --- | --- |
| 切主题 | `⌘K → ⌘T`，或命令 `theme selector: toggle` | 四款逐一检查 |
| 搜索与选区 | `⌘F`；搜索框中 `Enter` / `⇧Enter` 切结果；拖选文字；`⌘⇧F` 跨文件搜索 | 源码、预览的当前 / 其他匹配、焦点切换及选区叠加清楚；零结果、清空无残留 |
| Markdown | `⌘P` 打开样例 → 命令 `markdown: open preview`；本机也可 `⌘K → ⌘V` | 正文、链接、行内代码、表格、引用、代码块及 diff |
| Git | 改一个词并保存 → 命令 `git: diff` | 增删、变化词、搜索叠加可辨；冲突用临时仓库检查 |
| 列表与代码辅助 | `⌘P` 后按 `↑↓`；`⌘⇧M` 看诊断；悬停变量看类型；命令 `editor: show completions` 打开补全 | 选中 / 悬停、引用、括号、诊断、补全及提示清楚 |
| 调试器 | 可运行项目中：`F9` 设断点 → `F5` 选任务启动 → `F10` 单步；点 Frames 切栈帧、Variables 看变量；工具栏重启，`⇧F5` 停止 | 绿色执行行、变量、断点清楚；停止后旧高亮消失 |
| 终端 | `Ctrl + 反引号` 打开终端，运行 `git diff --color=always` | ANSI 前景 / 背景、反色及选区可读 |
| 日常使用 | 连续使用 20 分钟，再退出并重开 Zed | 搜索与 Markdown 选区仍正常 |

F 键触发系统功能时，加按 `fn`。首次调试没有可选任务时，先[配置调试](https://zed.dev/docs/debugger)。

键位参考：[Zed macOS](https://github.com/zed-industries/zed/blob/v1.24.3/assets/keymaps/default-macos.json) · [VS Code 覆盖](https://github.com/zed-industries/zed/blob/v1.24.3/assets/keymaps/macos/vscode.json)。Markdown 预览快捷键为本机自定义。

检查通过后勾选；未启用的功能注明“未测”。

- [ ] Day Vivid
- [ ] Day AAA
- [ ] Night AAA
- [ ] Midnight AAA
- [ ] 我认可观感，可以发布。验收人 / 日期：________

问题记录：`主题｜最短步骤｜实际 / 期望｜截图路径`。修复后复测再勾选。
