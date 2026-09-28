# Zed marketplace handoff

**已准备，尚未提交。** 上架入口是向 [zed-industries/extensions](https://github.com/zed-industries/extensions) 提交 PR，合并后由官方打包发布。[发布指南](https://zed.dev/docs/extensions/publishing/publishing-guide)

| 项目 | 已确认内容 |
| --- | --- |
| 名称 / ID | GreenTree / `green-tree-theme` |
| 版本 / 许可证 | 0.11.0 / MIT |
| 公开仓库 | [yuukiLike/zed-skin](https://github.com/yuukiLike/zed-skin) |
| 主题提交 | [`f0c745e`](https://github.com/yuukiLike/zed-skin/commit/f0c745e93e52aea44c92d0528b366f4cd7c52708)，已推送且在 `main` 历史中 |
| 实机验证 | Zed 1.21.0 / macOS，开发扩展安装成功，四款主题逐一切换并截图 |
| 颜色验证 | 当前[配色审计](../contrast-report.md)：三款深色主题主要文字达到 7:1；注释和 Markdown 选中文字按 4.5:1 校验；Day Vivid 鲜绿不满足 AA |

[zed-registry.patch](zed-registry.patch) 已在上游 `fac8916` 的注册文件上通过 `git apply --check --index`，只新增 `.gitmodules` 条目、`extensions.toml` 条目和指向上述主题提交的 gitlink。ID 在该上游版本未被占用。

## 人工提交

官方 [AI policy](https://github.com/zed-industries/extensions/blob/main/AI_POLICY.md) 明确规定：

> Autonomous agents are not allowed to be used for contributing to this project.

因此这里提供可审查的补丁和验证事实；最终 PR 正文、提交操作及维护者沟通需要作者本人完成。

Fork 并克隆官方仓库后，假设 `extensions` 和 `zed-skin` 位于同级目录，在 `extensions` 中执行：

```sh
git switch -c add-green-tree-theme
git apply --check --index ../zed-skin/docs/promotion/zed-registry.patch
git apply --index ../zed-skin/docs/promotion/zed-registry.patch
git submodule update --init extensions/green-tree-theme
pnpm install --frozen-lockfile
pnpm sort-extensions
git add .gitmodules extensions.toml extensions/green-tree-theme
git diff --cached
```

确认只涉及 GreenTree 后，提交并推送自己的分支，用自己的话填写 PR。若上游变化导致补丁冲突，按[官方指南](https://zed.dev/docs/extensions/publishing/publishing-guide)重新添加同一扩展，保留 0.11.0 和上述提交。合并并实际出现在[主题目录](https://zed.dev/extensions?filter=themes)后，再更新三语 README 的安装说明和宣发状态。
