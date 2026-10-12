# Zed marketplace handoff

历史记录：以下仅描述 0.11.1，不是当前工作区的发布清单。当前检查与配色目标见[测试说明](../theme-testing.md)。

首次上架 [PR #7749](https://github.com/zed-industries/extensions/pull/7749) 已合并，扩展市场已收录 [GreenTree](https://zed.dev/extensions/green-tree-theme)。本文件记录 **0.11.1 更新**的范围与验证事实，最终 PR 由作者本人提交。[官方更新说明](https://zed.dev/docs/extensions/publishing/updating-and-maintenance)

| 项目 | 已确认内容 |
| --- | --- |
| 名称 / ID | GreenTree / `green-tree-theme` |
| 待提交版本 / 许可证 | 0.11.1 / MIT |
| 公开仓库 | [yuukiLike/zed-skin](https://github.com/yuukiLike/zed-skin) |
| 主题优化 | [`4c53138`](https://github.com/yuukiLike/zed-skin/commit/4c53138e73372c19416dffce090345e9b2bebcdf)：改善注释与 Markdown 选中效果的可读性 |
| 实机验证 | 2026-09-30，作者确认已在 Zed 中切换四款主题并检查实际效果，效果正常；这项结论来自作者确认 |
| 自动验证 | 2026-09-30，`python3 scripts/check_contrast.py` 与 `python3 scripts/test_contrast.py` 均通过，后者包含 7 项回归测试 |
| 颜色目标 | 三款深色主题主要文字按 7:1 校验，注释和 Markdown 选中文字按 4.5:1 校验；Day Vivid 鲜绿及部分选中状态使用自定义阈值，不代表满足 AA |

本次官方仓库的更新只涉及两处：`extensions.toml` 中 GreenTree 的版本从 `0.11.0` 升至 `0.11.1`，以及 `extensions/green-tree-theme` 指向新的发布提交。

三语 README 已更新为扩展市场安装说明，同时保留手动安装方式。具体配色和阈值见[配色审计](../contrast-report.md)。

## 人工提交

官方 [AI policy](https://github.com/zed-industries/extensions/blob/main/AI_POLICY.md) 明确规定：

> Autonomous agents are not allowed to be used for contributing to this project.

作者需要理解更新内容，用自己的话写 PR 正文，并亲自回复维护者。此文件提供验证事实，供作者审阅。

准备分支：`yuukiLike/extensions` 的 `update-green-tree-theme-0.11.1`。

打开[更新比较页面](https://github.com/zed-industries/extensions/compare/main...yuukiLike:update-green-tree-theme-0.11.1?expand=1)，确认目标是 `zed-industries/extensions:main`，来源是上述准备分支，改动只涉及 GreenTree。审阅后，作者自行填写正文、确认贡献指南并创建 PR。

[zed-registry.patch](zed-registry.patch) 仅保留首次上架时的补丁记录；更新已有扩展时请使用上述更新分支。
