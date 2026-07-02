---
name: ppt-visual-rebuilder
description: Reverse-engineer an existing PowerPoint deck or hand-made PPT prototype into a confirmed page-by-page outline, generate full-deck visual style mosaics, wait for human approval, expand an approved mosaic into independent high-resolution 16:9 slide visual drafts, repair generated Chinese text or screenshot/dashboard mismatches, and only after final approval rebuild an editable PPTX. Use when the user asks to analyze PPT/PPTX content, create or compare PPT style mosaics, expand a selected mosaic into single-page visuals, fix generated slide image details, preserve screenshot module layouts, or reconstruct a final editable PowerPoint from approved visual drafts. This skill must enforce approval gates and must not auto-advance between outline, mosaic, page visuals, critical-page review, and PPTX generation.
---

# PPT Visual Rebuilder

> Author: 杨上杰 (Yang Shangjie)
> Version: v1.0.0
> Last Updated: 2026-07-02
> Maintainer: 杨上杰
>
> PPT Visual Rebuilder is a production-grade workflow for reverse-engineering PPT structures, generating style mosaics, expanding high-fidelity page visuals, repairing Chinese text, and rebuilding editable PPTX files.
>
> Copyright (c) 2026 Yang Shangjie.

## Project Metadata Rules

- Preserve the author, maintainer, copyright, version, and license information when sharing, copying, modifying, or republishing this skill.
- Update `Version` and `Last Updated` in this file whenever the skill is released or materially changed.
- Keep author and maintainer information consistent across `SKILL.md`, `AUTHORS.md`, `CHANGELOG.md`, `LICENSE`, `agents/openai.yaml`, and public release materials.
- Use `CHANGELOG.md` for release notes and version history.
- Use `references/publishing_guidelines.md` before publishing, accepting contributions, or preparing a public copy.
- Do not automatically remove author attribution from generated documentation or packaged skill files.

## Purpose

Use this skill for the controlled PPT visual-production workflow:

1. Reverse-engineer PPT content structure.
2. Generate full-deck style mosaics.
3. Pause for human confirmation.
4. Expand the approved mosaic into separate high-resolution 16:9 slide visuals.
5. Repair Chinese text, numbers, page labels, and screenshot/dashboard modules.
6. After final approval, rebuild an editable PPTX.

The core goal is not "make a PPT from nothing". The user usually first uses GPT to organize requirements, hand-builds a rough PPT to lock each page's structure, iterates that rough PPT, and only then asks Codex to run this skill.

## Trigger Scenarios

Use this skill when the user asks for any of the following:

- Read a PPT/PPTX and reverse-engineer its outline and per-slide content.
- Turn a hand-made PPT prototype into a polished visual direction.
- Generate 2-3 or more full-deck PPT visual mosaics for style selection.
- Expand a selected PPT mosaic into individual high-resolution 16:9 page visuals.
- Keep a selected mosaic as the visual/layout mother reference.
- Rebuild a page using a user-provided screenshot as the strict module reference.
- Fix Chinese glyph errors, wrong KPI labels, wrong page numbers, or wrong module structures.
- Prepare approved slide visual drafts for editable PPTX reconstruction.

Do not use this skill for unrelated image editing, generic graphic design, or direct PPTX creation without the outline/mosaic/approval workflow.

## Companion Skills

- Use `$imagegen` for raster image generation and image edits.
- Use the presentations skill for reading `.pptx` files and for final editable PPTX creation.
- If the user explicitly names `$imagegen`, read its `SKILL.md` before generating or editing images.

## Mandatory Approval Gates

This workflow is gate-controlled. Never auto-advance past a gate. Continue only when the user explicitly approves with language such as "确认", "可以", "继续", "按这个方向做", "这版可以", or equivalent.

If the user gives criticism, asks for changes, says "不够", "不对", "重做", or provides a new screenshot/material, revise the current stage and ask for approval again.

Required gates:

1. **Outline approval**: After producing the page-by-page outline, stop. Do not generate mosaics before the user confirms the outline.
2. **Mosaic approval**: After generating visual mosaics, stop. Do not expand single-page visuals before the user chooses or approves one direction.
3. **Single-page generation approval**: Before expanding pages, ask whether to proceed from the approved mosaic and whether to generate page-by-page or batch.
4. **Critical-page approval**: Stop for review after high-risk pages: cover, solution architecture, dashboard/cockpit, value/KPI, implementation roadmap, closing page, and any page based on a user screenshot.
5. **PPTX build approval**: After all visual drafts are accepted, ask whether to start editable PPTX reconstruction. Do not create/export a PPTX before this approval.

Useful Chinese gate questions:

```text
这版大纲是否确认？确认后我再生成拼图。
这几版拼图你选哪一版？是否需要重做或补充素材？
是否确认按这版拼图扩展逐页高清 16:9 单页视觉稿？
这页是否通过？如果有错字、数字或模块问题，我先修。
所有视觉稿是否确认？确认后我再开始重建可编辑 PPTX。
```

## Output Rules

All user-visible deliverables must be saved under the current project `outputs/` folder.

Use these subfolders:

- `outputs/mosaics/` for full-deck style mosaics.
- `outputs/slides/` for independent single-page visual drafts.
- `outputs/corrected/` for repaired/revised slide images.
- `outputs/pptx/` for final editable decks.

Use stable names:

```text
outputs/mosaics/mosaic-v1.png
outputs/mosaics/mosaic-v2.png
outputs/mosaics/mosaic-v3.png
outputs/slides/slide-01.png
outputs/slides/slide-02.png
outputs/corrected/slide-10-corrected.png
outputs/pptx/final-deck.pptx
```

Do not leave final project assets only under image-generation default folders. Copy final user-visible images into `outputs/`.

## Workflow

### 1. Ingest Source Material

Collect:

- Source `.pptx`, screenshots, PDFs, documents, or pasted images.
- The user's hand-made PPT, if available.
- Product photos, brand assets, dashboard screenshots, or page references.
- User requirements and correction history.

For `.pptx`, use structured extraction where possible. Record:

- slide count and page order
- visible text
- image/object counts
- page titles
- key numbers and terms
- suspected diagrams, dashboards, screenshots, and product visuals

### 2. Reverse-Engineer The PPT Outline

Produce a page-by-page outline before any visual generation. Each page should include:

- title
- core point
- body points
- visual suggestion
- exact words, numbers, product names, and screenshots that must be preserved
- items that are unclear and need user confirmation

Stop at **Outline approval**.

### 3. Generate Full-Deck Style Mosaics

After outline approval, use `$imagegen` to generate complete PPT mosaics.

Each mosaic must:

- contain all pages in correct order
- show each thumbnail as a 16:9 landscape PPT page
- use one unified visual system
- make titles, key numbers, major charts, and page structure readable
- represent a complete, formal, usable business PPT direction
- differ meaningfully from other versions, not only by color

Do not generate single-page visuals in this stage.

Stop at **Mosaic approval**.

### 4. Expand An Approved Mosaic Into Single Pages

After explicit approval, generate independent slide visuals.

Rules:

- Generate one complete 16:9 slide image per page.
- Do not generate a multi-page composite.
- Do not crop the mosaic and call it a final page.
- Treat the mosaic as style/layout reference only.
- Preserve the corresponding page's composition, hierarchy, visual system, footer, and page number.
- Fill unreadable small text only from the confirmed outline or user-provided source, not by invention.

Stop for **Critical-page approval** on high-risk pages.

### 5. Repair Generated Images

Use deterministic repair when an image is visually good but contains small factual/text errors.

Common repairs:

- Chinese glyph errors such as `销售`.
- Wrong key numbers.
- Wrong or missing page numbers.
- Dashboard modules that do not match the user's screenshot.
- Extra unsupported claims.

Use `scripts/overlay_text.py` to repair exact text when possible.

Do not remove third-party trial/license watermarks. Ask for an authorized source image or regenerate from allowed materials.

### 6. Rebuild Editable PPTX

Only after final visual approval, use the presentations skill to create an editable PowerPoint.

The approved slide visuals are the design reference, but the final PPTX should use editable text, shapes, charts, and images where practical. Do not simply paste full-slide screenshots unless the user explicitly requests an image-only deck.

## Anti-Hallucination Rules

- Do not add business data, customer names, amounts, KPI values, percentages, dates, service promises, or rankings that were not confirmed by the user or visible in source material.
- If text or chart details cannot be read, mark them as `需用户确认`.
- For screenshot-based pages, preserve module count, region proportions, information hierarchy, and chart/card placement.
- For Chinese titles, key metrics, product names, page numbers, and footers, prioritize correctness over visual flourish.
- If a page looks beautiful but the text is wrong, treat the page as failed.
- If image generation invents details, regenerate with stricter constraints or repair deterministically.

## Prompt And Validation References

Read these as needed:

- `references/workflow.md`: detailed workflow and approval behavior.
- `references/prompts.md`: copy-ready stage prompts.
- `references/validation_checklist.md`: acceptance criteria for outlines, mosaics, single-page visuals, text, dashboards, and final PPTX.
- `references/publishing_guidelines.md`: public sharing, attribution, issue, PR, example, script, versioning, and changelog maintenance rules.

Use `examples/` when the user wants examples or when constructing a new prompt from scratch.
