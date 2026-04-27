# yaml_frontmatter:
#   id: 'encoding_validator'
#   title: 'Validador estricto de codificación UTF-8'
#   tags: ['core', 'validation']

from pathlib import Path
from typing import List, Set, Optional

DEFAULT_TEXT_EXTENSIONS = {".md", ".json", ".py", ".html", ".css", ".js", ".yml", ".yaml"}
IGNORED_DIRS = {".git", ".venv", "venv", "__pycache__", "site"}

def is_ignored(path: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.parts)

def validate_utf8_file(path: Path) -> Optional[str]:
    """Verifica si un archivo es UTF-8 puro."""
    try:
        path.read_bytes().decode("utf-8")
        return None
    except UnicodeDecodeError as e:
        return f"Error UTF-8 en {path.name}: {e.reason} en pos {e.start}"
    except Exception as e:
        return f"Error leyendo {path.name}: {e}"

def validate_paths(targets: List[Path]) -> List[str]:
    """Valida múltiples rutas recursivamente."""
    errors = []
    for target in targets:
        if not target.exists(): continue
        files = target.rglob("*") if target.is_dir() else [target]
        for f in files:
            if f.is_file() and f.suffix.lower() in DEFAULT_TEXT_EXTENSIONS and not is_ignored(f):
                err = validate_utf8_file(f)
                if err: errors.append(err)
    return errors
