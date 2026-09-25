# GreenTree Contrast · 对比度检查

使用 WCAG 2.x sRGB 相对亮度公式；Day、Night、Midnight 及旧名称的普通文字均 ≥ 7:1（AAA）。
所有主题的关键非文字标识 ≥ 3:1；每个主题名称都有明确阈值，未知名称不自动降级。
判定使用未舍入数值，下表仅为显示而保留四位小数。

## GreenTree Contrast Day AAA

检查组合数：11365。

| 检查范围 | 组合数 | 最低对比度 | 要求 | 结果 |
| --- | ---: | ---: | ---: | --- |
| UI text | 2652 | 7.0984:1 | 7:1 | PASS |
| Editor / syntax | 4290 | 7.0984:1 | 7:1 | PASS |
| Terminal text | 270 | 7.0721:1 | 7:1 | PASS |
| UI indicators | 3510 | 4.2923:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.9861:1 | 3:1 | PASS |
| Cursors | 624 | 7.0984:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 8.2458:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 7.8429:1 | 7:1 | PASS |

最低文字对比度对应的组合：

`terminal.ansi.dim_yellow` / `players[0].selection`：7.0721:1。

## GreenTree Contrast Night AAA

检查组合数：11365。

| 检查范围 | 组合数 | 最低对比度 | 要求 | 结果 |
| --- | ---: | ---: | ---: | --- |
| UI text | 2652 | 7.4199:1 | 7:1 | PASS |
| Editor / syntax | 4290 | 7.3059:1 | 7:1 | PASS |
| Terminal text | 270 | 7.3925:1 | 7:1 | PASS |
| UI indicators | 3510 | 3.4640:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.6351:1 | 3:1 | PASS |
| Cursors | 624 | 7.4199:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 9.9285:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.0515:1 | 7:1 | PASS |

最低文字对比度对应的组合：

`syntax.constructor` / `element.active`：7.3059:1。

## GreenTree Contrast Midnight AAA

检查组合数：11365。

| 检查范围 | 组合数 | 最低对比度 | 要求 | 结果 |
| --- | ---: | ---: | ---: | --- |
| UI text | 2652 | 8.4232:1 | 7:1 | PASS |
| Editor / syntax | 4290 | 8.2937:1 | 7:1 | PASS |
| Terminal text | 270 | 8.3920:1 | 7:1 | PASS |
| UI indicators | 3510 | 3.9324:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.7758:1 | 3:1 | PASS |
| Cursors | 624 | 8.4232:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 10.2298:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.7633:1 | 7:1 | PASS |

最低文字对比度对应的组合：

`syntax.constructor` / `search.active_match_background`：8.2937:1。

## GreenTree Contrast AAA

检查组合数：11365。

| 检查范围 | 组合数 | 最低对比度 | 要求 | 结果 |
| --- | ---: | ---: | ---: | --- |
| UI text | 2652 | 7.4199:1 | 7:1 | PASS |
| Editor / syntax | 4290 | 7.3059:1 | 7:1 | PASS |
| Terminal text | 270 | 7.3925:1 | 7:1 | PASS |
| UI indicators | 3510 | 3.4640:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.6351:1 | 3:1 | PASS |
| Cursors | 624 | 7.4199:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 9.9285:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.0515:1 | 7:1 | PASS |

最低文字对比度对应的组合：

`syntax.constructor` / `element.active`：7.3059:1。


## 范围

覆盖主题显式定义的界面文字、语法（含注释）、行号、状态文字、默认终端 ANSI 前景、
光标及边框；同时检查选区、搜索、diff、括号匹配及弹出层底色。透明占位边框不作为可见标识。
这是颜色组合审计，不是 Zed 应用的完整 WCAG AA / AAA 认证。未验证焦点面积、键盘或读屏行为、
选区与相邻底色之间的区别、语言服务额外淡化、插件自定义颜色，或终端程序指定的背景色、256 色和真彩色。
Zed 运行时若调整颜色或透明度，须按实际渲染重新评估。
