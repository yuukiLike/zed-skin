# Theme checks

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/check_contrast.py --report docs/contrast-report.md
git diff --check
```

Only Python's standard library is needed. CI runs the tests and audit, then fails
if the generated report differs from the committed copy.

## Coverage

- All four palettes: text contrast, visible search/selection backgrounds, and
  distinct current/other matches with either the search field or editor focused.
- Markdown: text contrast and selection visibility on prose, links, inline code,
  fenced code and diffs, including search overlap beneath the glyphs.
- Lists: selected rows versus the surrounding surface and hover; symbols and
  brackets versus normal/active lines; added versus deleted rows; changed words
  versus solid/hollow diff rows and overlapping search; conflict sides versus
  each other and the editor.
- Terminal: default text and ANSI colors on the default and selected surfaces;
  normal, bright and dim black/white pairs. Black must stay darker than white.
- Debugger: execution row versus normal/active lines; selected stack frame versus
  the actual panel background. Missing or invisible debugger colors fail the CLI.
- Regressions: the old faint/brown highlights, selection hiding a match, invisible
  overlays, incorrect alpha/paint order, missing fields and duplicate JSON keys.
- Independent color-math references, unrounded thresholds and failing CLI status.

Day Vivid targets AA 4.5:1 on normal surfaces. The original dark variants
retain 7:1 for primary text and 4.5:1 for comments. Dark primary text retains
7:1 on Git highlights; colored text uses 4.5:1 there. Expanded search/selection
and rendered-Markdown text measurements are advisory, with below-target pairs
marked REVIEW rather than PASS. Baseline normal-surface and highlight-visibility
requirements remain enforced. A successful CLI exit does not make REVIEW rows
meet their text-contrast targets.
ANSI black on a dark default surface and white on a light one are exempt;
black/white pairs target 4.5:1. Arbitrary program-chosen pairs are not guaranteed.
Visibility uses custom guards: 0.06 Oklab distance for color separation, and 1.25:1
luminance for Markdown selections and active matches on dark editor backgrounds.
These guards catch known regressions; they do not guarantee visual acceptance.

## Rendering and references

[Zed 1.23.2 paints search before editor selections](https://github.com/zed-industries/zed/blob/v1.23.2/crates/editor/src/element.rs).
It multiplies the selection's theme alpha by 0.5 while search has focus. An opaque
selection can therefore replace the active search color when focus returns to the
editor. All variants use translucent selections to preserve it. The theme API
exposes two search backgrounds; adding outlines would require an editor change.
Day Vivid search and Markdown selections use green at about 60% for the current
match, 30% for others and 55% for Markdown selections. The original dark variants
use blue at 50%, 30% and 40%. Checks composite search over
each actual surface, including inline chips and diff rows, before applying word
highlights or selections. [Markdown previews in Zed 1.25.2](https://github.com/zed-industries/zed/blob/v1.25.2/crates/markdown/src/markdown.rs#L2600)
read the same two search fields as the source editor, so both views inherit these fills.
[The renderer paints chips, search and selection before glyphs](https://github.com/zed-industries/zed/blob/v1.25.2/crates/markdown/src/markdown.rs#L8042).
The text audit therefore composites these backgrounds while retaining the glyph
color. Older versions that paint selection over glyphs need a separate runtime
check; passing this model does not validate those versions. Rendered previews
have selections but no editor caret, so their fills are excluded from caret
contrast checks; source-editor search and selection still check the cursor.
Lists also use `ghost_element.selected`, not just `element.selected`. Diff word
fills are painted after hunk fills and search: equal row/word colors hide changes,
while opaque word fills erase search. Translucent fills preserve both, including
when the editor selection is painted last. ANSI slots can be foregrounds or
backgrounds; testing every slot only as text on the default surface previously
inverted their intended roles.

- [Catppuccin](https://github.com/catppuccin/zed/blob/4314cb05c74d141b7962290a41d6087e8c0ad02f/.github/workflows/check.yml): CI checks generated-theme consistency. We apply that idea to the audit report.
- [Rosé Pine](https://github.com/rose-pine/zed/blob/1446d31a2eec6bee627883d523ec63ef5c78ec9b/src/template.json): search states use different alpha values. This is a palette reference, not a borrowed test suite.
- Zed's [search tests](https://github.com/zed-industries/zed/blob/v1.23.2/crates/search/src/project_search.rs#L3725) and [Markdown tests](https://github.com/zed-industries/zed/blob/v1.23.2/crates/markdown/src/markdown.rs#L7941): distinct active colors, navigation, aligned inline code, Unicode and search/selection overlap inform our cases.
- Color math: [WCAG contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [Oklab](https://bottosson.github.io/posts/oklab/#converting-from-linear-srgb-to-oklab).

## In-app checks

Use [human-todo.md](../human-todo.md) for the release checklist, pass criteria and
result recording. It includes [the Markdown sample](../examples/theme-checks.md),
common editor/terminal states and the remaining visual coverage gaps.

## Debugger palette

The paused execution row uses green in all four variants: `#B6DBA6` for Day
Vivid, `#06342D` for Day AAA, and `#032E2B` for Night AAA and Midnight AAA.
An earlier gray-green candidate failed the existing 0.06 Oklab visibility guard
in Day Vivid and Day AAA. These fills restore separation from normal/active
lines while preserving the existing primary-text contrast targets.
In Zed 1.24.2, [the editor reads
`editor.debugger_active_line.background`](https://github.com/zed-industries/zed/blob/v1.24.2/crates/editor/src/editor.rs#L6770).
[Frames uses `element.hover` for both the selected frame and hovered frames](https://github.com/zed-industries/zed/blob/v1.24.2/crates/debugger_ui/src/session/running/stack_frame_list.rs#L603),
so the original dark variants use blue-cyan for that shared fill (`#003044` in
Day AAA and `#002D38` in Night AAA and Midnight AAA).
Day Vivid uses pale leaf green (`#D3E9AD`)
for Frames. Other controls using `element.hover` inherit these colors. A theme
cannot give selected and hovered stack frames different fills in this Zed version.

## Vivid tab-close hover · 2026-10-24

The user reported that the hovered tab-close button was hard to distinguish.
[Zed 1.25.3 builds it as a default subtle IconButton with `Color::Muted`](https://github.com/zed-industries/zed/blob/v1.25.3/crates/workspace/src/pane.rs#L3020).
[Muted resolves to `text.muted`](https://github.com/zed-industries/zed/blob/v1.25.3/crates/ui/src/styles/color.rs#L93),
while [the hover fill uses `ghost_element.hover`](https://github.com/zed-industries/zed/blob/v1.25.3/crates/ui/src/components/button/button_like.rs#L298).
The old glyph contrast was already 8.22:1; the pale hover fill was nearly the
same color as the tab backgrounds.

Only Vivid's `ghost_element.hover` changes in this step, from `#D8E2CE` to
soft rose `#E8C8D5`. Oklab distances from active/inactive tab backgrounds
increase from 0.0167/0.0173 to 0.0813/0.0637; the distance from the selected
green row is 0.1108. The unchanged dark close glyph has 7.15:1 contrast on the
new fill. These are focused palette calculations, not an in-app visual pass
or a new CLI gate.

Other subtle/outlined buttons and selectable list rows using the same hover
field inherit the rose fill. Selected-row fills, filled-control hover,
debugger highlights, tab backgrounds, typography, syntax and the other three
theme objects remain unchanged from the preceding step. Global Zed settings
are unchanged. The existing 62 regression tests and enforced contrast checks
pass; extended interaction text measurements remain advisory. No computer-use
testing was performed. On 2026-10-24 the user approved the final appearance,
including the hover fill, and requested a commit.

## Vivid comments and Markdown · 2026-10-24

The user distinguished rendered Markdown Preview from the Markdown source:
the preview felt dull, while the source only needed a more elegant heading green.
Comments had not lost highlighting; both comment captures used low-chroma
blue-gray `#4E5262`. The orange-property commit did not alter them.
The first rose-plum revision (`#7D3C62`) felt too prominent to the user. The
follow-up uses muted plum `#674A5F`, reducing Oklab chroma from 0.1021 to 0.0503
while preserving the existing font style, weight and contrast requirements.

| Surface | Theme field | New color |
| --- | --- | --- |
| Source comments and doc comments | `syntax.comment`, `syntax.comment.doc` | Muted plum `#674A5F` |
| Markdown source headings | `syntax.title` | Emerald `#005F46` |
| Preview links and other UI accent text | `text.accent` | Royal blue `#1234BF` |
| Preview tables, quotes, rules and other UI borders | `border` | Forest green `#39704C` |
| Preview heading rules, code frames and other secondary borders | `border.variant` | Fern green `#3F7654` |

[Zed 1.25.3's Markdown style](https://github.com/zed-industries/zed/blob/v1.25.3/crates/markdown/src/markdown.rs#L186)
uses these shared fields. Its preview overrides use `text` for prose, H1-H5
headings and inline-code text; H6 uses `text.muted`. Inline-code chips use `editor.foreground` at 8% opacity,
and fenced blocks share `editor.background`. Changing `syntax.title` therefore
affects source headings and Markdown highlighted inside a fence, not rendered
heading colors. The theme does not expose separate controls for these preview
surfaces. This pass changes the available accents and borders, not the layout
or the shared foreground/background to simulate unsupported controls.

The supplied preview's large example is a fence labeled `md`, so its contents
are highlighted as Markdown, not as a standalone JavaScript file. Its source
document was inspected but not changed.

Comments measure 5.92:1 on the editor and at least 4.56:1 across enforced
surfaces; source headings measure 5.91:1 and at least 4.55:1, respectively.
The comment/Markdown step changed six Day Vivid color fields. Other syntax colors, token weights,
focus/selection fills and borders, debugger colors, file-list text, backgrounds,
the other three theme objects and global Zed settings remain unchanged.
The existing 62 tests and contrast audit pass; advisory interaction states
remain REVIEW. No computer-use testing or new screenshots were performed.
The user later reported that this appearance looked good. A possible change
to the comment font style was discussed but not applied.

## Green highlights and softer daylight · 2026-10-23

Day Vivid retains the accepted sage editor background (`#DCE4D6`) and green
lists, references, brackets, focus indicators, cursors, search and selections.
After reloading Zed, the user found the accumulated foreground darkening and
heavy typography too strong. Earlier feedback had described a cached palette.
The latest instruction limits the rollback to Day Vivid; its colors and token
weights now come from the saved version before the broad readability revision.
The first scope check compared only the latest rollback, missing dark-theme
changes from earlier in the session. That error is now corrected: Day AAA,
Night AAA and Midnight AAA match the original session-start snapshot and HEAD
exactly. Day Vivid is the only theme object with a net change.

The restored checkpoint used variables `#202820`, keywords `#185C28`, functions
`#174299`, numbers `#8A1F58`, strings `#744000` and italic comments `#3E4A39`. Regular tokens use
explicit weight 400;
keywords/functions retain 500 and other tokens their earlier weights. On the
sage background, calculated contrast is 11.63:1 for variables, 7.18:1 for
comments, 6.20:1 for green, 7.08:1 for blue, 6.66:1 for pink and 6.51:1 for orange.

The normal-text target returns to Vivid's earlier AA 4.5:1. Its restored
search/selection text can fall below AA on stacked fills: those ratios remain
in the report as REVIEW. The original dark palettes also retain their baseline
contrast requirements; expanded Markdown/interaction measurements are advisory.
The regression suite checks that Vivid's low interaction ratios are reported,
while unreadable normal text and invisible highlights still fail the CLI.

Global settings were a second source of cross-theme changes. The session's
`ui_font_family`, `ui_font_weight`, `buffer_font_weight` and
`unnecessary_code_fade` overrides have been removed; the complete settings file
matches the original snapshot. Font sizes and theme selection are preserved.
Vivid's token weights remain in its theme object rather than global settings.

The 62 regression tests pass. Direct comparisons verify that only Vivid differs
from the original theme family, all three dark objects match HEAD exactly, and
Vivid was untouched during this scope repair. At the user's request, validation
uses source review and static checks, with no new computer-use checks or
screenshots. Reload the development extension before comparing colors. At that
rollback checkpoint, visual acceptance was still pending.

After checkpoint commit `5382f74` was pushed, the first Vivid adjustment changed
green syntax from `#185C28` to `#145024` and comments from `#3E4A39` to `#354331`.
That step changed eight syntax foregrounds and retained blue and purple.

The next user screenshot requested stronger green keywords, orange strings,
blue calls, purple types and file-list greens. That adjustment changed
25 syntax foregrounds, 22 shared UI/status foregrounds and three accent entries:

| Text | Before that adjustment | After that adjustment | Contrast on editor background |
| --- | --- | --- | --- |
| Green keywords | `#145024` | `#0B4722` | 7.31:1 → 8.31:1 |
| Orange strings | `#744000` | `#6B3000` | 6.51:1 → 7.87:1 |
| Blue calls | `#174299` | `#1234A6` | 7.08:1 → 7.79:1 |
| Purple types | `#5A28A3` | `#5319A5` | 7.11:1 → 7.86:1 |

Secondary UI/file-list text changes from `#3E4A39` to `#2D412F` (6.63:1 to
7.79:1 on the panel; 5.95:1 to 6.99:1 when selected). Added-file/green accent
text changes from `#17602B` to `#0B4722` (5.42:1 to 7.67:1 on the panel;
4.86:1 to 6.88:1 when selected). Shared UI keys also affect menus, status labels
and debugger text within Vivid.

The user approved the current-file highlight and the broader Vivid palette in
commit `7652d97`, then requested orange property names such as `length`. This
follow-up changed only `syntax.property.color`; that checkpoint's palette was:

| Role | Checkpoint color | Contrast on editor background |
| --- | --- | --- |
| Keywords (`import`, `from`) | `#00551C` | 6.96:1 |
| Calls (`expect`, `equal`) | `#1234BF` | 7.10:1 |
| Types (`Array`) | `#8500A9` | 6.27:1 |
| Properties (`length`, `prototype`, `hasOwnProperty`) | `#943000` | 6.01:1 |
| Strings | `#803B00` | 6.33:1 |
| Numbers / booleans | `#A00052` | 6.16:1 |
| Comments | `#4E5262` | 5.95:1 |
| Variables (`copy`, `input`) | `#090D12` | 14.95:1 |

The accepted palette's Oklab distances remain 0.2843 for comments/variables,
0.2066 for comments/types, 0.1936 for functions/types, and 0.1453 for
strings/numbers. Properties and strings intentionally share a warm color family
after the orange request. The property contrast is 4.98:1 on the selected row
and at least 4.63:1 across the enforced normal/diff surfaces. Color distances
describe the palette, not a perceptual pass/fail.

Leaf green is adjusted from `#006127` to `#00551C`, improving its editor contrast
from 5.88:1 to 6.96:1 and selected-row contrast from 4.87:1 to 5.76:1. Its green
hue is retained, with substantially more lightness and chroma than the rejected
near-black green `#003D1A`. All normal/diff text gates remain at their existing
targets; search/selection and rendered-Markdown pairs retain their reported
advisory status. Punctuation and predictive syntax keep their neutral slate;
numbers, booleans and special strings retain raspberry.

The accepted current-file highlight, other syntax colors, all UI/file-list
colors, font weights/styles, backgrounds, selection fills, the three dark themes
and global settings are unchanged in this step. Validation uses the existing
contrast/compositing audit, regression suite and source comparisons. All 62
regression tests pass. On 2026-10-23 the user confirmed the orange properties
felt more comfortable and authorized delivery. No new agent computer-use
testing was performed, and extended runtime scenarios were not visually rechecked.

## Git diff palette check · 2026-10-21

Zed 1.24.4 on macOS loaded the rebuilt development extension. All four variants
were reviewed with `git: diff` in an isolated local Git repository: whole added
and removed lines, changed identifiers, a changed number, and partial `Number`
search matches in the working side. Each variant has one plain diff and one
search-overlap capture. The eight final original JPEGs, fixture and review index
are Git-ignored under `.local/git-diff-2026-10-21/`; earlier file-comparison setup
captures are kept separately from that final review set.

The revised palette uses soft mint/coral accents and translucent word fills.
Primary text retains 7:1 on dark diff highlights, while colored syntax/status
text uses 4.5:1 there; normal surfaces retain their existing targets. Cursors were
lightened on the dark variants and affected Day Vivid text colors were slightly
darkened. The audit now checks added/deleted row separation, and excludes word
fills from border/icon backgrounds because they only cover glyph ranges.

The 61 Python tests, four-palette audit and whitespace check pass. Original Zed
settings, including theme and font size, were restored after capture. This focused
check does not repeat conflict, debugger, terminal or other-platform runtime QA;
their existing modeled checks still run. Final aesthetic acceptance remains with
the user.

## Markdown search check · 2026-10-20

Zed 1.24.3 on macOS loaded the linked development extension with the stronger
search fills. All four variants were inspected in an isolated Markdown sample:
one preview and one source screenshot per variant. The preview includes CJK
prose, bold/italic text, links, inline code, a table, a quote, TypeScript and diff
fences. Navigation from the first to the second of 19 matches was checked in
Night AAA; the second match remains visibly stronger in all four variants.
Source captures include the active match's editor selection with search focused.
Midnight AAA also covered a preview selection across current/other matches,
zero results and clearing the query.

The 11 final captures plus the Night AAA baseline are Git-ignored under
`.local/markdown-search-2026-10-20/`. The 59 Python tests, four-palette audit and
whitespace check pass. Text-contrast and visibility thresholds were retained;
affected cursor colors were adjusted to preserve 3:1 over the stronger overlays.
This is a focused Markdown/search check; it does not repeat the broader debugger,
terminal, collaboration or platform coverage below.

## Local check · 2026-10-17

The final JSON was loaded through the installed development-extension symlink
using `zed: rebuild dev extension` in Zed 1.24.2 on macOS. All four variants were
checked in a separate fixture workspace. Each of 35 scenes has one original
3840 × 1938 JPEG per variant: 140 reviewed captures, excluding setup attempts.

| Area | Scenes | Reviewed in all four variants |
| --- | --- | --- |
| Markdown preview | 01–10 | Prose/CJK, links, inline code, tables, quotes, TypeScript/diff fences; whole/partial/multiline selections; search overlap, Unicode, zero results and clearing |
| Source and code assistance | 11–18 | Real TypeScript errors, diagnostic/type hover and project diagnostics; reference changes, refreshed bracket pairs; source search/reference overlap; completion selection and keyboard movement |
| Lists | 19–20 | File finder names/paths and selected command, descriptions and shortcuts |
| Git | 21–24 | Real word/number changes, partial search inside changed words, selection overlap and a temporary merge conflict |
| Terminal | 25–27 | Normal/bright/dim ANSI slots, black/white backgrounds, reverse video, bold/underline, real `git diff` output and multiline selection |
| Debugger | 28–33 | Live Node pause, expanded variables, caller-frame selection, F10, restart, enabled/disabled breakpoints and execution-highlight cleanup after stop |
| Project search | 34 | Cross-file results with current/other matches after navigation to a different file |
| Markdown source | 35 | Partial `tes` matches within plain/inline/bold/italic/struck text and table source |

Debugger transitions were performed in one local dependency-free Node session;
each resulting state was inspected in all four variants. Selecting the caller
moved the green band and selected frame together and updated its scope. F10
moved the band from line 5 to 6; restart returned it to line 5. Stop removed the
execution band and inline values; Zed retained dimmed last-known variables.
ANSI black on a dark default background remains an intentional audit exemption.
Zed adjusted Day Vivid's black-on-green foreground during the terminal check.

Raw evidence is Git-ignored under `.local/final-qa-2026-10-17/`: `index.md` links
the 140 scene captures; `observations.json` records the visual checks;
`review.json` identifies the tested theme SHA-256, environment and limitations.
The QA session was stopped and its window closed. The original `algorithm-box`
window/session and theme configuration were restored: dark mode, Night AAA,
with Day Vivid retained as the light theme. Those 140 QA captures are not used as
release previews, and this check does not fill in the user's acceptance boxes.

The 59 Python tests, four-palette audit and whitespace check pass without
relaxing primary-text targets. CI commands were run locally; this is not a
claim that a new GitHub Actions run has completed.

Two runtime caveats remain. Editing the linked JSON or rebuilding the extension
index did not reliably refresh the active palette; `zed: rebuild dev extension`
did. Switching from dark to light can leave the current bracket pair with the
previous dark fill; moving to another pair and back refreshes it (scene 14).
Neither behavior is fixed or exercised by the Python audit. The Frames
hover/selection limitation described above also remains.

Edit predictions were disabled and were not enabled for this check. Dedicated
parameter-help UI and warning diagnostics were not deliberately exercised;
type hovers and real error diagnostics were. Other debugger adapters, Vim/Helix,
collaborative selections, older Zed binaries and other displays/platforms were
not tested. Final aesthetic acceptance, including the latest green, remains
with the user. Repeat the relevant visual checks after editor or theme changes.

## README showcase · 2026-10-17

A separate English demonstration workspace supplied [24 public screenshots](screenshots/README.md):
code, Markdown preview, source search with selection, paused Node.js debugging,
real Git diffs and terminal/ANSI output, each inspected in all four variants.
The READMEs share the same assets, with 360-pixel clickable previews, a visible
debugger comparison and four collapsible galleries. The original overview URLs
now point to the 0.11.2 captures.

The published JPEGs are byte-for-byte copies of the locally retained originals.
Raw captures, the demonstration workspace and a capture manifest remain ignored
under `.local/readme-showcase-2026-10-17/`. The demonstration debug session was
stopped, its window closed, and the original Night AAA / Day Vivid theme
preferences restored. These presentation scenes supplement the 35-scene QA
matrix above; they do not expand its platform or adapter coverage.

## Local check · 2026-10-13

Zed 1.23.2 on macOS: blue Markdown selections were checked in Night AAA and Day
Vivid across prose, links, inline code and fenced code. Night AAA also covered
search overlap in code blocks and partial inline-code selection. Screenshots were
recorded under `.local/color-review/markdown-selection/`. The original
Night AAA theme and workspace were restored afterward.

Before search was unified with the Markdown selection blue, the review checked
Git word diffs, search inside changed words, conflicts
and project search in all four variants; command lists in Day AAA and Day Vivid;
brackets/references and ANSI black/white, black-on-green and reverse video in
Night AAA and Day Vivid. Night AAA also covered whole/partial symbol search and
navigation between files in project search. The terminal checks used Zed's
existing contrast adjustment; Day Vivid's black-on-green text was lightened by
Zed. Raw screenshots were recorded under `.local/color-review/final-review/`.
Night AAA and the original workspace were restored. No editor patch or rendering
override was installed.

That round passed 51 tests and the four-palette audit. After unifying search with
the selection blue, 56 tests and the updated audit pass, including transparent
search over inline chips, solid/hollow diff rows and focus-dependent selections.
The blue search palette was checked in Markdown previews in all four variants,
and in source views in Night AAA and Day Vivid. The latter two also covered
inline-code search/selection overlap. Day Vivid's source view showed cyan
document-reference highlights after selecting a whole word; the current search
match remained blue. Check that combination separately during manual acceptance.
New captures are in the locally ignored `.local/search-blue/` folder. Night AAA
and the original workspace/search query were restored.
CI commands were checked locally, not yet on GitHub. Older Zed binaries were not exercised.
Python tests do not execute GPUI or cover clipping, runtime fading, user overrides
or terminal programs' own colors. Repeat the manual checks after Zed updates.
