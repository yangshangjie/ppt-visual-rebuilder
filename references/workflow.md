# PPT Visual Rebuilder Workflow

## Workflow Summary

Run this workflow in this exact order:

1. Source analysis.
2. Page-by-page outline.
3. Human outline approval.
4. Full-deck visual mosaics.
5. Human mosaic approval.
6. Single-page 16:9 visual drafts.
7. Human critical-page approval.
8. Text/module repair.
9. Human final visual approval.
10. Editable PPTX reconstruction.

Do not skip approval gates.

## Source PPT Analysis

For `.pptx` inputs:

1. Copy the source into the working project when needed.
2. Extract slide text, slide count, layout names, image counts, and object positions.
3. Print page-by-page visible text.
4. Render or inspect screenshots/contact sheets when possible.
5. Build a structured outline with title, core point, body points, and visual suggestion.

Prefer structured APIs such as `python-pptx`, unzip/XML inspection, or presentation tooling over guessing from screenshots alone.

Unknown content must be marked `需用户确认`.

## Approval Behavior

At every gate:

- Show the artifact.
- Summarize what was produced.
- Ask a concise confirmation question.
- Do not continue until the user approves.

If the user is dissatisfied, revise the current stage rather than moving forward.

## Full-Deck Mosaic Generation

Generate mosaics only after the outline is approved.

Mosaic requirements:

- One complete image per visual direction.
- All slides included.
- Correct page order.
- 16:9 slide thumbnails.
- Unified visual system inside each mosaic.
- Main titles, key numbers, major diagrams, and page rhythm visible.
- No PPTX generation.
- No single-page visual draft generation.

Style directions should differ by visual language, not only palette:

- premium AI technology
- product operations
- executive command center
- consulting solution
- brand launch

After delivering mosaics, ask the user to choose or request regeneration.

## Single-Page Expansion

Start only after mosaic approval.

Rules:

- Generate one independent 16:9 slide image per page.
- Never crop the mosaic to produce a final single-page visual.
- The mosaic is only a style/layout reference.
- Preserve the selected mosaic's visual system, page hierarchy, footer, and page number style.
- Use the confirmed outline to restore unreadable small text.
- Do not invent data.

Save outputs to `outputs/slides/`.

## Dashboard And Screenshot Matching

When the user provides a dashboard or UI screenshot:

- Count cards, modules, and charts.
- Preserve zones, proportions, and hierarchy.
- Re-skin into the chosen deck style only after preserving structure.
- Copy labels and numbers only when visible or confirmed.
- If details are unreadable, use placeholders or mark `需用户确认`.

If generation changes the module structure, regenerate.

## Chinese Text Repair

Generated Chinese text is high risk. Inspect:

- titles
- product names
- key metrics
- chart labels
- page numbers
- footers

For exact corrections, use `scripts/overlay_text.py`.

Example:

```bash
python scripts/overlay_text.py \
  --input outputs/slides/slide-15.png \
  --output outputs/corrected/slide-15-corrected.png \
  --box 520,70,1800,220 \
  --text "让AI赋能销售，让数据驱动增长" \
  --font-size 72 \
  --text-color 246,250,255,255 \
  --box-color 0,0,0,255
```

Do not remove third-party trial/license watermarks. Ask for an authorized source or regenerate from allowed materials.

## Output Paths

Use these locations:

- `outputs/mosaics/mosaic-v1.png`
- `outputs/mosaics/mosaic-v2.png`
- `outputs/mosaics/mosaic-v3.png`
- `outputs/slides/slide-01.png`
- `outputs/slides/slide-02.png`
- `outputs/corrected/slide-10-corrected.png`
- `outputs/pptx/final-deck.pptx`

## Final PPTX Reconstruction

Start only after all visual drafts are approved.

Use editable text, shapes, charts, and images where practical. Avoid image-only decks unless the user explicitly asks.

Render and inspect the final deck before delivery.

Use `references/validation_checklist.md` before each approval gate.
