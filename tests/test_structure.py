# yaml_frontmatter:
#   id: 'test_structure'
#   title: 'Pruebas de integridad de la estructura de pilares'
#   tags: ['tests', 'structure']


def test_six_pillars_exist(repo_root):
    """Verifica que los 6 pilares de la arquitectura Bourbaki existan en src/."""
    expected_pillars = [
        "01_fundamentos_logica",
        "02_estructuras_algebraicas",
        "03_analisis_continuidad",
        "04_espacio_forma",
        "05_discrecion_computacion",
        "06_estocastica_incertidumbre",
    ]

    src_dir = repo_root / "src"
    assert src_dir.exists(), "Directorio src/ no encontrado"

    for pillar in expected_pillars:
        pillar_path = src_dir / pillar
        assert pillar_path.is_dir(), f"Falta el pilar obligatorio: {pillar}"


def test_root_directories_exist(repo_root):
    """Verifica que las carpetas de sistema existan en la raiz."""
    required = ["scripts", "utils", "metadata", "site_src", "tests"]
    for folder in required:
        assert (repo_root / folder).is_dir(), f"Falta carpeta de sistema: {folder}"
