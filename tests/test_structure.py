# yaml_frontmatter:
#   id: 'test_structure'
#   title: 'Pruebas de integridad estructural, nomenclatura y adyacencia de metadatos'
#   tags: ['tests', 'structure', 'naming-hygiene', 'metadata-adjacency']


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
    required = ["scripts", "utils", "metadata", "tests"]
    for folder in required:
        assert (repo_root / folder).is_dir(), f"Falta carpeta de sistema: {folder}"


def test_naming_hygiene_and_no_accents(repo_root):
    """Verifica que todos los archivos y carpetas en src/ sigan snake_case y no tengan acentos."""
    import re

    # Permitir letras minusculas, numeros, guiones bajos y extensiones permitidas
    # Tambien permite carpetas de assets
    snake_case_pattern = re.compile(r"^[a-z0-9_]+(?:\.[a-z0-9]+)?$")
    accent_chars = "áéíóúáéíóúüñÁÉÍÓÚÑ"

    src_dir = repo_root / "src"
    assert src_dir.exists()

    for path in src_dir.rglob("*"):
        # Ignorar archivos temporales o carpetas ocultas si las hay
        if path.name.startswith("."):
            continue

        # Verificar que no contenga caracteres con acento o especiales
        has_accents = any(char in accent_chars for char in path.name)
        assert not has_accents, f"El archivo o carpeta contiene acentos o caracteres especiales no permitidos: {path.relative_to(repo_root)}"

        # Verificar snake_case en archivos y directorios
        # Los pilares empiezan con numeros ej: 01_fundamentos_logica (es compatible con el patron)
        is_valid_name = snake_case_pattern.match(path.name)
        assert is_valid_name, f"El nombre no cumple con snake_case estricto: {path.relative_to(repo_root)}"


def test_metadata_adjacency_exists(repo_root):
    """Verifica que cada archivo de teoria (.qmd o .md) en src/ tenga su .json adyacente según ADR-002."""
    src_dir = repo_root / "src"
    assert src_dir.exists()

    for path in src_dir.rglob("*"):
        if path.is_file() and path.suffix in [".qmd", ".md"]:
            # Omitir archivos README globales de los pilares si los hay o indice general
            if path.name in ["README.md", "index.qmd"]:
                continue
            
            json_path = path.with_suffix(".json")
            assert json_path.exists(), f"Falta el archivo descriptivo JSON adyacente para: {path.relative_to(repo_root)} (Requerido por ADR-002)"

