# yaml_frontmatter:
#   id: 'test_validators'
#   title: 'Pruebas unitarias para validadores de codificacion, matematicas, metadatos y estilo semantico'
#   tags: ['tests', 'validators', 'encoding', 'jsonschema', 'semantic-breaks']

import json

import jsonschema
import pytest
from jsonschema.exceptions import ValidationError

from scripts.core import encoding_validator, formula_validator
from scripts.io.metadata_agent import MetadataAgent
from utils.markdown import check_semantic_line_breaks


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
    text = r"Fórmula: $x+y = z$ y bloque $$\int dx$$"
    assert formula_validator.scan_unbalanced_math(text) is False


def test_math_syntax_unbalanced():
    """Prueba detección de fórmulas LaTeX desbalanceadas."""
    text = "Error: $x+y = z (falta cierre)"
    assert formula_validator.scan_unbalanced_math(text) is True


def test_metadata_agent_synchronization(sandbox_project):
    """Verifica que MetadataAgent sincronice correctamente los metadatos YAML a JSON adyacentes."""
    agent = MetadataAgent(sandbox_project)
    agent.synchronize()

    # Comprobar que se creo el archivo JSON adyacente para el tema de prueba
    json_path = sandbox_project / "src" / "01_fundamentos_logica" / "test_tema.json"
    assert json_path.exists(), "No se creo el archivo JSON adyacente de metadatos"

    with open(json_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
    
    assert meta["id"] == "msc01_test_tema"
    assert meta["pilar"] == "01_fundamentos_logica"
    assert meta["msc_code"] == "01-01"


def test_metadata_schema_validation(sandbox_project):
    """Verifica que la validacion contra el esquema JSON funcione correctamente con metadatos validos e invalidos."""
    schema_path = sandbox_project / "metadata" / "schemas" / "content.schema.json"
    assert schema_path.exists()

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    # Caso valido
    valid_meta = {
        "id": "msc01_demostracion",
        "title": "Metodos de Demostracion",
        "pilar": "01_fundamentos_logica",
        "msc_code": "03-01",
        "status": "stable"
    }
    # No deberia lanzar ninguna excepcion
    jsonschema.validate(instance=valid_meta, schema=schema)

    # Caso invalido (falta 'status')
    invalid_meta = {
        "id": "msc01_demostracion",
        "title": "Metodos de Demostracion",
        "pilar": "01_fundamentos_logica",
        "msc_code": "03-01"
    }
    with pytest.raises(ValidationError):
        jsonschema.validate(instance=invalid_meta, schema=schema)


def test_semantic_line_breaks_validator():
    """Valida la regla de 'Salto de línea semántico' (Semantic Line Breaks) mediante utils.markdown."""
    # Prosa correcta (un punto final de linea, o punto y salto de linea)
    prosa_valida = (
        "Esta es una linea de texto.\n"
        "Esta es otra linea diferente que empieza aqui.\n"
        "Una formula inline $x = y$ no deberia molestar."
    )
    warnings_valida = check_semantic_line_breaks(prosa_valida)
    assert len(warnings_valida) == 0, f"Se detectaron advertencias falsas: {warnings_valida}"

    # Prosa invalida (punto y seguido en la misma linea)
    prosa_invalida = "Esta es una frase. Y esta es otra en la misma linea."
    warnings_invalida = check_semantic_line_breaks(prosa_invalida)
    assert len(warnings_invalida) == 1
    assert "Se detectó punto y seguido" in warnings_invalida[0]


