# PPT Visual Rebuilder

Production-grade workflow for:

- PPT reverse engineering
- Human approval gates
- Full-deck mosaic generation
- Single-page visual expansion
- Chinese text repair
- Editable PPTX reconstruction

## Features

- Five-stage approval workflow
- Anti-hallucination constraints
- Dashboard structure preservation
- Chinese typography repair
- Standardized output directories

## Documentation

- [User Guide](docs/usage.md)
- [Workflow Reference](references/workflow.md)
- [Prompt Library](references/prompts.md)
- [Validation Checklist](references/validation_checklist.md)

These documents describe the complete human-in-the-loop workflow, validation requirements, prompt references, and operational guidelines for production-grade PPT generation.

## Project Structure

```text
agents/
docs/
examples/
references/
scripts/

AUTHORS.md
CHANGELOG.md
LICENSE
README.md
SKILL.md
```

## Roadmap

### v1.0.x - Documentation and reliability

- Refine public documentation and onboarding materials.
- Expand sanitized examples for common PPT reconstruction scenarios.
- Improve deterministic Chinese typography and small-text repair workflows.

### v1.1.x - Workflow coverage and template depth

- Add guidance for Gamma, Pitch, and adjacent presentation workflows.
- Introduce consulting-style presentation templates and reusable structure patterns.
- Improve compatibility guidance for GPT, Gemini, DeepSeek, and other multimodal models.

### v2.0.x - Automation and extensibility

- Explore more automated editable PPTX reconstruction while preserving human approval gates.
- Introduce plugin-oriented workflow extension points.
- Add configurable visual-production pipelines for different presentation scenarios.

## License

CC BY-NC 4.0

## Author

Yang Shangjie (杨上杰)
