# yaml_frontmatter:
#   id: 'test_validators'
#   title: 'Pruebas unitarias para validadores avanzados'
#   tags: ['tests', 'validators']

from scripts.core import encoding_validator, formula_validator


def test_utf8_validation_positive(tmp_path):
    """Prueba que detecte correctamente un archivo UTF-8."""
    f = tmp_path / "valid.md"
    f.write_text("Texto con eñe y matemáticas: $x^2$", encoding="utf-8")
    assert encoding_validator.validate_utf8_file(f) is None


def test_utf8_validation_negative(tmp_path):
    """Prueba que detecte un archivo con codificación errónea."""
    f = tmp_path / "invalid.md"
    # Escribir con codificación diferente (latin-1) para forzar error
    f.write_bytes("Texto con eñe: ñ".encode("latin-1"))
    assert encoding_validator.validate_utf8_file(f) is not None


def test_math_syntax_balanced():
    """Prueba detección de fórmulas LaTeX balanceadas."""
    text = "Fórmula: $x+y = z$ y bloque $$\int dx$$"
    assert formula_validator.scan_unbalanced_math(text) is False


def test_math_syntax_unbalanced():
    """Prueba detección de fórmulas LaTeX desbalanceadas."""
    text = "Error: $x+y = z (falta cierre)"
    assert formula_validator.scan_unbalanced_math(text) is True
