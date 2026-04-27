import json
import os
from pathlib import Path


def get_directory_tree(root_path, ignore_list):
    tree = {}
    root_path = Path(root_path)

    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if d not in ignore_list and not d.startswith(".")]

        rel_path = Path(root).relative_to(root_path)
        if rel_path == Path("."):
            node = tree
        else:
            node = tree
            for part in rel_path.parts:
                if part not in node:
                    node[part] = {}
                node = node[part]

        for f in files:
            f_path = Path(f)
            if f.startswith("."):
                continue
            if f_path.suffix in [
                ".md",
                ".py",
                ".svg",
                ".html",
                ".css",
                ".js",
                ".json",
                ".txt",
                ".toml",
                ".yml",
                ".yaml",
            ]:
                node[f] = "file"

    return tree


def run():
    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    ignore = [
        "venv",
        ".venv",
        "__pycache__",
        "site",
        ".git",
        ".pytest_cache",
        ".ruff_cache",
        ".mypy_cache",
        "dist",
        "build",
    ]

    tree = get_directory_tree(PROJECT_ROOT, ignore)

    out_json = PROJECT_ROOT / "docs" / "project_structure.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(tree, f, indent=4, ensure_ascii=False)

    print(f"Generado: {out_json.name}")


if __name__ == "__main__":
    run()
