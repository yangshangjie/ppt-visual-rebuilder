# Publishing Guidelines

Use these guidelines when sharing, maintaining, or accepting contributions to PPT Visual Rebuilder.

## How To Cite This Skill

Recommended citation:

```text
PPT Visual Rebuilder by Yang Shangjie (杨上杰), v1.0.0, 2026.
Licensed under CC BY-NC 4.0.
```

When referencing the workflow in articles, repositories, presentations, training material, or internal documentation, keep the skill name, author, version, and license visible.

## Preserve Author Information

Keep the following files and fields intact unless the maintainer explicitly approves a change:

- `SKILL.md` project metadata
- `AUTHORS.md`
- `CHANGELOG.md`
- `LICENSE`
- `agents/openai.yaml` metadata

Do not remove, hide, overwrite, or replace original attribution when publishing modified versions.

## Submit Issues

Issue reports should include:

- Skill version
- Codex environment or operating system
- Source material type, such as PPTX, screenshot, PDF, or hand-made prototype
- Workflow stage where the issue occurred
- Expected behavior
- Actual behavior
- Example prompt or sanitized screenshot, if safe to share

For generated PPT problems, specify whether the issue is about outline extraction, mosaic generation, single-page expansion, Chinese text repair, dashboard fidelity, or editable PPTX reconstruction.

## Submit Pull Requests

Pull requests should:

- Preserve the existing five approval gates.
- Keep the reverse-engineering to mosaic to single-page visual to PPTX workflow intact.
- Avoid adding unconfirmed business claims, KPI values, customer names, dates, or amounts to examples.
- Update `CHANGELOG.md`.
- Update `Version` and `Last Updated` in `SKILL.md` when the change is released.
- Keep backward compatibility unless the change is intentionally released as `v2.x.x`.

## Contribute Examples

Example files should:

- Be placed under `examples/`.
- Avoid private customer data or confidential business numbers.
- Use realistic but generic PPT scenarios.
- Mark uncertain content as requiring user confirmation.
- Demonstrate approval gates instead of bypassing them.

Recommended naming:

```text
examples/<stage>_<scenario>_example.md
```

## Add Scripts

New scripts should:

- Be placed under `scripts/`.
- Provide command-line help.
- Use explicit input and output paths.
- Write user-visible outputs into `outputs/` during real tasks.
- Avoid destructive filesystem behavior.
- Fail with clear error messages.
- Include a short usage example in the relevant reference file.

For text or image correction scripts, prefer deterministic behavior and avoid changing unrelated image areas.

## Upgrade Version Numbers

Use semantic versioning adapted to this workflow:

- `v1.0.x` for bug fixes, prompt wording corrections, script fixes, and documentation corrections.
- `v1.x.x` for backward-compatible feature additions, new examples, new validation steps, or new helper scripts.
- `v2.x.x` for breaking workflow changes, changed approval behavior, changed output structure, or incompatible prompt contracts.

When releasing a version:

1. Update `Version` in `SKILL.md`.
2. Update `Last Updated` in `SKILL.md`.
3. Update `agents/openai.yaml` metadata.
4. Add a new entry to `CHANGELOG.md`.
5. Check that `AUTHORS.md` and `LICENSE` are still present.

## Maintain CHANGELOG

Each changelog entry should include:

- Version number
- Release date
- Short summary
- Added, changed, fixed, or removed items
- Author or maintainer

Use newest entries first.

## Publication Checklist

Before public sharing:

- Confirm `SKILL.md` still includes project metadata.
- Confirm `AUTHORS.md`, `CHANGELOG.md`, and `LICENSE` are included.
- Confirm `references/validation_checklist.md` and `references/prompts.md` are included.
- Confirm no private PPT, screenshot, customer data, API keys, or generated client assets are bundled.
- Confirm examples are sanitized.
- Confirm scripts are safe to run and do not perform bulk deletion.
- Confirm the five human approval gates remain mandatory.
