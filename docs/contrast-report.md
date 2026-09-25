# GreenTree Contrast · 对比度检查

使用 WCAG 2.x sRGB 相对亮度公式；普通文字 ≥ 7:1，关键非文字标识 ≥ 3:1。
判定使用未舍入数值，下表仅为显示而保留四位小数。

## GreenTree Contrast Day AAA

检查组合数：11365。

| 检查范围 | 组合数 | 最低对比度 | 要求 | 结果 |
| --- | ---: | ---: | ---: | --- |
| UI text | 2652 | 7.1108:1 | 7:1 | PASS |
| Editor / syntax | 4290 | 7.1108:1 | 7:1 | PASS |
| Terminal text | 270 | 7.1108:1 | 7:1 | PASS |
| UI indicators | 3510 | 3.3344:1 | 3:1 | PASS |
| Scrollbar | 3 | 3.9944:1 | 3:1 | PASS |
| Cursors | 624 | 7.1423:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 8.5560:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 7.9313:1 | 7:1 | PASS |

最低文字对比度对应的组合：

`text.muted` / `element.active`：7.1108:1。

## GreenTree Contrast Night AAA

检查组合数：11365。

| 检查范围 | 组合数 | 最低对比度 | 要求 | 结果 |
| --- | ---: | ---: | ---: | --- |
| UI text | 2652 | 7.3872:1 | 7:1 | PASS |
| Editor / syntax | 4290 | 7.3872:1 | 7:1 | PASS |
| Terminal text | 270 | 7.3872:1 | 7:1 | PASS |
| UI indicators | 3510 | 3.4640:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.6351:1 | 3:1 | PASS |
| Cursors | 624 | 7.4199:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 9.9285:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.0515:1 | 7:1 | PASS |

最低文字对比度对应的组合：

`text.muted` / `element.active`：7.3872:1。

## GreenTree Contrast AAA

检查组合数：11365。

| 检查范围 | 组合数 | 最低对比度 | 要求 | 结果 |
| --- | ---: | ---: | ---: | --- |
| UI text | 2652 | 7.3872:1 | 7:1 | PASS |
| Editor / syntax | 4290 | 7.3872:1 | 7:1 | PASS |
| Terminal text | 270 | 7.3872:1 | 7:1 | PASS |
| UI indicators | 3510 | 3.4640:1 | 3:1 | PASS |
| Scrollbar | 3 | 4.6351:1 | 3:1 | PASS |
| Cursors | 624 | 7.4199:1 | 3:1 | PASS |
| Inverse cursor text | 8 | 9.9285:1 | 7:1 | PASS |
| Vim / Helix badges | 8 | 9.0515:1 | 7:1 | PASS |

最低文字对比度对应的组合：

`text.muted` / `element.active`：7.3872:1。


## 范围

覆盖主题显式定义的界面文字、语法（含注释）、行号、状态文字、默认终端 ANSI 前景、
光标及边框；同时检查选区、搜索、diff、括号匹配及弹出层底色。透明占位边框不作为可见标识。
这是颜色组合审计，不是 Zed 应用的完整 WCAG AAA 认证。未验证焦点面积、键盘或读屏行为、
选区与相邻底色之间的区别、语言服务额外淡化、插件自定义颜色，或终端程序指定的背景色、256 色和真彩色。
Zed 运行时若调整颜色或透明度，须按实际渲染重新评估。
