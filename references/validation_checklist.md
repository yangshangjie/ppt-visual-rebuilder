# Validation Checklist

Use this checklist before asking the user to approve each gate. If an item fails, fix the artifact before moving forward.

## 1. PPT Outline Acceptance

- Slide count matches the source PPT or user expectation.
- Page order is correct.
- Each slide has a title, core point, body points, and visual suggestion.
- Chapter structure is clear.
- Key product names, business terms, numbers, and customer-specific terms are preserved exactly.
- Unknown or unreadable content is marked as `需用户确认`.
- The outline does not add unconfirmed customer names, amounts, KPI values, service promises, or dates.
- The user has explicitly approved the outline before mosaic generation.

## 2. Mosaic Acceptance

- The mosaic contains every slide in the deck.
- Slide order is correct.
- Every thumbnail is a 16:9 landscape PPT page.
- The whole mosaic uses one coherent visual system.
- Main titles, key numbers, chart structure, and page rhythm are visible.
- The design direction fits the audience and content density.
- Different mosaic versions vary by visual language, not only color.
- No final single-page image is produced by cropping the mosaic.
- The user has selected or approved one mosaic direction before page expansion.

## 3. Single-Page Visual Acceptance

- Each output is one complete independent 16:9 slide image.
- The page is not a crop of the mosaic.
- The page follows the selected mosaic's layout and visual system.
- Main title, core point, key numbers, chart labels, footer, and page number are readable.
- Page content is based on the confirmed outline and source material.
- No extra unsupported data, people, customer names, metrics, or promises are introduced.
- Critical pages are shown to the user before continuing.
- Files are saved under `outputs/slides/` using names such as `slide-01.png`.

## 4. Chinese Text Acceptance

- Chinese titles use correct standard characters.
- Fragile words such as `销售` are checked visually.
- Product names and brand terms are exact.
- Key numbers and KPI labels match source or confirmed outline.
- Page numbers and footer text are correct.
- There is no mojibake, fake glyph, hallucinated Chinese, random English, or broken punctuation.
- If generated text is wrong but the image is otherwise good, use deterministic repair such as `scripts/overlay_text.py`.
- Corrected files are saved under `outputs/corrected/`.

## 5. Dashboard / Screenshot Restoration Acceptance

- Module count matches the user screenshot.
- Module zones and relative proportions match the screenshot.
- Card hierarchy and chart hierarchy match the screenshot.
- Labels and numbers are copied only when visible or confirmed.
- Chart types match the screenshot: bar, line, donut, KPI cards, etc.
- No invented names, dates, amounts, rankings, or precise KPI values are added.
- If details are unreadable, use abstract placeholders or mark `需用户确认`.
- The visual style may be re-skinned, but information architecture must remain faithful.

## 6. Final PPTX Acceptance

- Final file is saved under `outputs/pptx/final-deck.pptx` or another user-approved name.
- Slide count and order match the approved visual drafts.
- Page size is 16:9.
- Text is editable where practical.
- Shapes, charts, tables, icons, and images are editable where practical.
- The deck does not rely on full-slide raster images unless the user explicitly approved image-only reconstruction.
- Typography, color system, page footer, page number, cards, diagrams, and dashboard modules are consistent.
- No text overlaps, clipping, broken layout, or unreadable page numbers remain.
- Rendered previews are visually checked before delivery.
- The user has approved the final PPTX or requested specific revisions.
