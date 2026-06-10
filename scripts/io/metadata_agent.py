# yaml_frontmatter:
#   id: 'metadata_agent'
#   title: 'Agente de sincronizacion de metadatos'
#   tags: ['scripts', 'io', 'metadata']

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
        # Soporte para MD/QMD (---) y Python (# yaml_frontmatter:)
        if file_path.suffix in [".md", ".qmd"] and content.startswith("---"):
            match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", content, re.DOTALL)
            if match:
                return yaml.safe_load(match.group(1))
            return None

        if file_path.suffix == ".py":
            match = re.search(r"# yaml_frontmatter:\n((?:#.*\n)+)", content)
            if match:
                yaml_str = match.group(1).replace("# ", "").replace("#", "")
                return yaml.safe_load(yaml_str)
        return None

    def inject_quarto_metadata(self, file_path, quarto_meta, custom_meta):
        """
        Futuro: Genera e inyecta los metadatos YAML en dos secciones estructuradas.
        Sección 1: Quarto (title, date, author, description, categories)
        Sección 2: Polaris (id, pilar, status, etc.)
        """
        # TODO: Implementar lógica de sobreescritura estructurada con comentarios.
        pass

    def synchronize(self):
        targets = ["src", "scripts", "utils", "tests"]
        for target in targets:
            dir_path = self.root / target
            if not dir_path.exists():
                continue

            for f in dir_path.rglob("*"):
                if f.suffix in [".md", ".qmd", ".py"] and f.name != "__init__.py":
                    metadata = self.extract_yaml(f)
                    if metadata:
                        json_path = f.with_suffix(".json")
                        with open(json_path, "w", encoding="utf-8") as jf:
                            json.dump(metadata, jf, indent=4, ensure_ascii=False)
                        print(f"Sync: {f.name} -> {json_path.name}")


if __name__ == "__main__":
    agent = MetadataAgent(Path(__file__).resolve().parents[2])
    agent.synchronize()
