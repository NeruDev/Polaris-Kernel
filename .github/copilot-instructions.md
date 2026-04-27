# GitHub Copilot Rules for Polaris Kernel

## Project Context
- **Name:** Polaris Kernel (MathKernel)
- **Architecture:** Bourbaki-based modular system with 6 pillars in `src/`.
- **Primary Tech:** Python 3.11, Matplotlib (SVG), Sympy, Markdown (MathJax).
- **Core Standard:** Always respect `AGENTS.md` and `ARQUITECTURE.md`.

## Execution Style
- **Narrate Before Act:** Briefly explain the technical rationale before modifying files.
- **Incrementalism:** Apply surgical, minimal changes. Avoid broad refactorings across multiple pillars.
- **No Emojis:** Do NOT use emojis in code, scripts, or log messages to prevent encoding/parsing errors.

## Validation & Quality
- **Integrity:** Every `.md` file must maintain its YAML frontmatter with correct `id` and `pilar`.
- **Scripts:** Ensure any new script in `scripts/` is compatible with the `build.py` orchestrator.
- **Assets:** Verify that SVG assets exist in the same directory as the `.md` files before referencing them.
- **Testing:** Add or update tests in `tests/` for any new logic in `scripts/core/`.

## Code Generation Standards
- **Simplicity:** Prefer readable Python over complex abstractions.
- **Path Handling:** Always use `pathlib.Path` for filesystem operations.
- **Markdown Hygiene:** Follow semantic rules in `ARQUITECTURE.md`:
  - **One Sentence per Line:** Use semantic line breaks in prosa.
  - **Unbounded LaTeX:** Do not limit line length in math blocks.
  - **Semantic Paragraphs:** Group by logical units, not line count.
- **Word Count:** 300-500 words per file (Excluding Frontmatter and Glossary).
- **Formatting:** Adhere to `pyproject.toml` (Ruff/Mypy).

## Safety & Intent
- **Non-Destructive:** Never delete theory files in `src/` or assets in `metadata/` without explicit confirmation.
- **Inquiry vs Directive:** If a request is vague, ask for clarification instead of assuming architectural changes.
