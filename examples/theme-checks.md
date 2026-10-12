# Search and selection sample

同一两千首夹具在 iPhone 上查看。此行用于单个匹配的回归检查。

完整任务三轮；完整任务中的数据；另一项任务。

Search for **needle**. Move forward and backward through the results; compare the
active match with every other match. Repeat with **音源** and **é中🙂**.

needle in prose; another needle, and `needle` in inline code.

音源 in prose; another 音源, and `音源` in inline code.

`test` beside plain test; **bold `test`**; *italic `test`*; ~~struck `test`~~.

[needle in a link](https://zed.dev) and [`needle` in a code link](https://zed.dev).

Select across prose, `inline code`, and a [link](https://zed.dev). Then select only
part of `inline code`. Check that text remains readable and selection remains visible.

| Left | Center | Right |
| :--- | :---: | ---: |
| `needle` | `needle` | `needle` |
| ~~`test`~~ | ~~`test`~~ | ~~`test`~~ |
| `é中🙂` | `é中🙂` | `é中🙂` |

> A quote with needle, `needle`, and **needle**.

```typescript
// needle 音源 é中🙂 in a comment
const needle = "needle";
function findNeedle(value: string): string {
  return value.includes(needle) ? needle : "missing";
}
```

```diff
- needle removed
+ needle added
```

For no results, search for a value absent from this document. Clear the query and
confirm match highlighting goes away.
