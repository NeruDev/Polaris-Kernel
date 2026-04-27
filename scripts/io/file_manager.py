# yaml_frontmatter:
#   id: 'file_manager'
#   title: 'Abstraccion de operaciones de I/O para Markdown y JSON'
#   tags: ['io', 'filesystem']

import json
import shutil
import yaml
import os
from pathlib import Path
from typing import Dict, Any, Tuple, Optional
from scripts.core.error_handling import FileOperationError

class FileManager:
    """Maneja de forma segura las lecturas y escrituras del proyecto."""
    
    def read_text(self, path: Path) -> str:
        try:
            return path.read_text(encoding='utf-8')
        except Exception as e:
            raise FileOperationError(f"Error de lectura en {path.name}: {e}")

    def write_text(self, path: Path, content: str):
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8', newline='\n')
        except Exception as e:
            raise FileOperationError(f"Error de escritura en {path.name}: {e}")

    def read_json(self, path: Path) -> Dict[str, Any]:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise FileOperationError(f"Error de parsing JSON en {path.name}: {e}")

    def write_json(self, data: Dict[str, Any], path: Path):
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            raise FileOperationError(f"Error guardando JSON en {path.name}: {e}")

    def read_markdown_with_frontmatter(self, path: Path) -> Tuple[Dict[str, Any], str]:
        """Extrae el frontmatter YAML y el cuerpo del Markdown."""
        content = self.read_text(path)
        if content.startswith('---'):
            try:
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    metadata = yaml.safe_load(parts[1]) or {}
                    return metadata, parts[2].strip()
            except Exception as e:
                raise FileOperationError(f"Error en Frontmatter YAML de {path.name}: {e}")
        return {}, content.strip()

    def ensure_dir(self, path: Path):
        """Asegura que un directorio exista."""
        path.mkdir(parents=True, exist_ok=True)

    def remove_dir(self, path: Path):
        """Elimina un directorio y su contenido."""
        if path.exists() and path.is_dir():
            shutil.rmtree(path)

    def copy_dir(self, src: Path, dst: Path, merge: bool = True):
        """Copia un directorio completo."""
        try:
            if not merge and dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst, dirs_exist_ok=True)
        except Exception as e:
            raise FileOperationError(f"Error copiando {src.name} -> {dst.name}: {e}")
