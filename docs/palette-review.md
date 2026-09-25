# Palette notes · 0.11.0

GreenTree has four variants. Day Vivid is light; Day AAA, Night AAA and Midnight AAA are dark.

- **Day Vivid:** warm ivory `#F3EFE5`, vivid green keywords `#00A84A`, blue-cyan fields `#00758F`, sky-blue functions/cursor `#006AC4`, violet types `#7C3AED`, bold pink numbers `#BD2B77`. The green uses regular weight and deliberately falls below AA.
- **Day AAA:** indigo `#1C2135` makes brighter green, blue, violet and pink possible at the audited 7:1 text target.
- **Night AAA:** `#050505`, soft-white text and filenames `#D8E1EC`, regular green keywords, orange cursor.
- **Midnight AAA:** `#000000`, pure-white filenames, bold green keywords, blue functions and rose-pink special variables such as TypeScript `this`.

Night and Midnight use violet `#D99CFF` for types and warmer pink `#FF9FB8` for special variables. Filenames follow `text` and `text.muted`; Git status colors remain separate.

## Verification

Run `python3 scripts/check_contrast.py` to audit **45,460 color pairs**. See the [full report](contrast-report.md) for thresholds and exclusions. The six Day Vivid green captures have a custom 2.5:1 floor; this is not a WCAG text threshold. Other Day Vivid text is checked at 4.5:1, the three AAA variants at 7:1, and key non-text indicators at 3:1.

The 0.11.0 theme from commit `f0c745e93e52aea44c92d0528b366f4cd7c52708` was installed through **Install Dev Extension** in Zed 1.21.0 on macOS. All four variants were selected and visually checked using [tree.ts](../examples/tree.ts). The [screenshots](screenshots/) are the original 1922 × 1944 JPEG captures, without recoloring, resizing or recompression. File icons come from the user's Zed setup and are not bundled with this color theme.

The family and file were renamed from GreenTree Contrast to GreenTree. Remove an older local `green-tree-contrast.json` copy and restart Zed if old names remain cached. Previous palette experiments and retired preview images remain available in Git history.
