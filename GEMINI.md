# Gemini Instructions for Polaris Kernel

## Context Priority
- **Source of Truth:** Refer to `metadata/` for system structure and IA-ready records.
- **Content Exploration:** Use `src/` exclusively for conceptual understanding and theory management.
- **Global Standards:** Foundation mandates are in `AGENTS.md` and `ARQUITECTURE.md`.

## Navigation & Naming
- **Strict Naming:** Use exact `snake_case` for all files and directories.
- **No Inferences:** Do not assume alternative names; if a file is not found via exact match, list the directory to verify.
- **Path Hygiene:** Never use accents or special characters in file paths or names.

## Content Handling
- **Language:** All theoretical material, comments, and agent outputs must be in **Spanish (es-ES or es-MX)**.
- **No Translation:** Do not translate content unless explicitly requested by the user.
- **Semantic Formatting:** Priority is pedagogical flow. 
  - Use **Semantic Line Breaks** (one sentence per line).
  - **LaTeX Immunity:** Block formulas (`$$...$$`) have no line length limits.
  - **Logical Paragraphs:** Group by logical units, not line count.
- **Size Target:** 300-500 words per file (Excluding Frontmatter and Glossary).

## Task Behavior & Linking
- **The Trinity Rule:** When generating or modifying assets, always preserve the link:
  `scripts/grafics/` (Generator) → `src/` (SVG Asset) → `GENERATED_ASSETS.md` (Registry).
- **Metadata Integrity:** Ensure every `.md` file has a valid YAML frontmatter including `id` (MSC standard), `title`, and `pilar`.
- **Build First:** Before declaring a task finished, ensure `scripts/build.py` runs without critical errors.
