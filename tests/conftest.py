# yaml_frontmatter:
#   id: 'conftest'
#   title: 'Configuracion global de fixtures para Pytest'
#   tags: ['tests', 'infrastructure']

import pytest
import shutil
from pathlib import Path

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
        "06_estocastica_incertidumbre"
    ]
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    
    for pilar in pilares:
        (src_dir / pilar).mkdir()

    (tmp_path / "scripts").mkdir()
    (tmp_path / "utils").mkdir()
    (tmp_path / "site_src").mkdir()
    (tmp_path / "metadata").mkdir()
    
    # Crear archivo de ejemplo
    tema_path = src_dir / "01_fundamentos_logica" / "test_tema.md"
    tema_path.write_text(
        "---\nid: msc00_test\ntitle: 'Tema de Prueba'\npilar: '01_fundamentos_logica'\n---\n\n## 1.1 Seccion\nContenido.",
        encoding="utf-8"
    )

    # Template base
    (tmp_path / "site_src" / "template_page.html").write_text(
        "<html><body><h1>Explorador de Conocimiento</h1><!-- El contenido Markdown se inyectará aquí --></body></html>",
        encoding="utf-8"
    )

    return tmp_path
