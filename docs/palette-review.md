# Palette notes · 0.11.0

GreenTree has four variants. Day Vivid is light; Day AAA, Night AAA and Midnight AAA are dark.

- **Day Vivid:** warm ivory `#F3EFE5`, vivid green keywords `#00A84A`, blue-cyan fields `#00758F`, sky-blue functions/cursor `#006AC4`, violet types `#7C3AED`, bold pink numbers `#BD2B77`. The green uses regular weight and deliberately falls below AA.
- **Day AAA:** indigo `#1C2135` makes brighter green, blue, violet and pink possible at the audited 7:1 primary-text target.
- **Night AAA:** `#050505`, soft-white text and filenames `#D8E1EC`, regular green keywords, orange cursor.
- **Midnight AAA:** `#000000`, pure-white filenames, bold green keywords, blue functions and rose-pink special variables such as TypeScript `this`.

Night and Midnight use violet `#D99CFF` for types and warmer pink `#FF9FB8` for special variables. Filenames follow `text` and `text.muted`; Git status colors remain separate.

Comments are italic neutral gray: Day Vivid `#626262`, Day AAA `#A8A8A8`, Night and Midnight `#979797`. They target AA 4.5:1 so they can recede from active code.

Markdown selections use translucent blue overlays painted above the glyphs. Their text targets AA 4.5:1 in the dark variants; Day Vivid retains a custom 2.5:1 floor. The audit also checks a custom 1.25:1 selected/unselected background difference, which is a visibility guard rather than a WCAG criterion.

Unused code is separate: Zed fades language-server diagnostics with `unnecessary_code_fade` (default `0.3`; larger values fade more). A theme cannot make only unused code italic or replace its syntax colors with uniform gray. This runtime fading is outside the palette audit.

## Verification

Run `python3 scripts/check_contrast.py` for the [full report](contrast-report.md), including thresholds and exclusions. The six Day Vivid green captures have a custom 2.5:1 floor; this is not a WCAG text threshold. Other base-palette Day Vivid text is checked at 4.5:1. Dark primary text retains 7:1, comments and selected Markdown use 4.5:1, and key non-text indicators use 3:1. Run `python3 -m unittest discover -s scripts -p 'test_*.py'` for selection regression checks.

The current comment and selection adjustments were checked numerically. The screenshots below predate these changes.

The 0.11.0 theme from commit `f0c745e93e52aea44c92d0528b366f4cd7c52708` was installed through **Install Dev Extension** in Zed 1.21.0 on macOS. All four variants were selected and visually checked using [tree.ts](../examples/tree.ts). The [screenshots](screenshots/) are the original 1922 × 1944 JPEG captures, without recoloring, resizing or recompression. File icons come from the user's Zed setup and are not bundled with this color theme.

The family and file were renamed from GreenTree Contrast to GreenTree. Remove an older local `green-tree-contrast.json` copy and restart Zed if old names remain cached. Previous palette experiments and retired preview images remain available in Git history.
