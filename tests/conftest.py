# yaml_frontmatter:
#   id: 'conftest'
#   title: 'Configuracion global de fixtures para Pytest'
#   tags: ['tests', 'infrastructure']

from pathlib import Path

import pytest


@pytest.fixture
def repo_root():
    """Retorna la raiz del repositorio real."""
    return Path(__file__).resolve().parents[1]


@pytest.fixture
def sandbox_project(tmp_path):
    """
    Crea un mini-repositorio temporal para pruebas seguras.
    Sigue la arquitectura completa de Polaris Kernel (6 Pilares).
    """
    pilares = [
        "01_fundamentos_logica",
        "02_estructuras_algebraicas",
        "03_analisis_continuidad",
        "04_espacio_forma",
        "05_discrecion_computacion",
        "06_estocastica_incertidumbre",
    ]
    src_dir = tmp_path / "src"
    src_dir.mkdir()

    for pilar in pilares:
        (src_dir / pilar).mkdir()

    (tmp_path / "scripts").mkdir()
    (tmp_path / "utils").mkdir()
    (tmp_path / "metadata").mkdir()
    (tmp_path / "metadata" / "schemas").mkdir()

    # Escribir un esquema simplificado para pruebas en el sandbox
    schema_path = tmp_path / "metadata" / "schemas" / "content.schema.json"
    schema_path.write_text(
        """{
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "required": ["id", "title", "pilar", "msc_code", "status"],
            "properties": {
                "id": { "type": "string" },
                "title": { "type": "string" },
                "pilar": { "type": "string" },
                "msc_code": { "type": "string" },
                "status": { "type": "string" }
            }
        }""",
        encoding="utf-8",
    )

    # Crear archivo de ejemplo con frontmatter completo bajo el nuevo paradigma
    tema_path = src_dir / "01_fundamentos_logica" / "test_tema.md"
    tema_path.write_text(
        "---\nid: msc01_test_tema\ntitle: 'Tema de Prueba'\npilar: '01_fundamentos_logica'\nmsc_code: '01-01'\nstatus: 'stable'\n---\n\n## 1.1 Seccion\nContenido del tema de prueba con frase unica.",
        encoding="utf-8",
    )

    return tmp_path
