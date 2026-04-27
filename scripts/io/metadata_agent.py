import json
import re
from pathlib import Path

import yaml


class MetadataAgent:
    """Garantiza la presencia de archivos JSON descriptivos junto a cada fuente."""

    def __init__(self, root_dir):
        self.root = Path(root_dir)

    def extract_yaml(self, file_path):
        content = file_path.read_text(encoding="utf-8")
        # Soporte para MD (---) y Python (# yaml_frontmatter:)
        if file_path.suffix == ".md" and content.startswith("---"):
            parts = content.split("---", 2)
            return yaml.safe_load(parts[1]) if len(parts) >= 3 else None

        if file_path.suffix == ".py":
            match = re.search(r"# yaml_frontmatter:\n((?:#.*\n)+)", content)
            if match:
                yaml_str = match.group(1).replace("# ", "").replace("#", "")
                return yaml.safe_load(yaml_str)
        return None

    def synchronize(self):
        targets = ["src", "scripts", "utils", "tests"]
        for target in targets:
            dir_path = self.root / target
            if not dir_path.exists():
                continue

            for f in dir_path.rglob("*"):
                if f.suffix in [".md", ".py"] and f.name != "__init__.py":
                    metadata = self.extract_yaml(f)
                    if metadata:
                        json_path = f.with_suffix(".json")
                        with open(json_path, "w", encoding="utf-8") as jf:
                            json.dump(metadata, jf, indent=4, ensure_ascii=False)
                        print(f"Sync: {f.name} -> {json_path.name}")


if __name__ == "__main__":
    agent = MetadataAgent(Path(__file__).resolve().parents[2])
    agent.synchronize()
