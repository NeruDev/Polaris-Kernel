import os
from typing import List, Dict, Any

class ContentValidator:
    REQUIRED_FIELDS = ['id', 'title', 'pilar', 'msc_code']

    @staticmethod
    def validate_utf8(file_path: str) -> bool:
        """Verifica que el archivo tenga codificación UTF-8 pura."""
        try:
            with open(file_path, 'rb') as f:
                f.read().decode('utf-8')
            return True
        except UnicodeDecodeError:
            return False

    @staticmethod
    def validate_metadata(metadata: Dict[str, Any]) -> List[str]:
        """Valida que los metadatos contengan los campos obligatorios."""
        errors = []
        for field in ContentValidator.REQUIRED_FIELDS:
            if field not in metadata or not metadata[field]:
                errors.append(f"Campo faltante o vacío: {field}")
        return errors
