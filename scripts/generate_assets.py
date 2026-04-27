# yaml_frontmatter:
#   id: 'generate_assets'
#   title: 'Orquestador masivo de generacion de graficos SVG'
#   tags: ['graphics', 'automation']

import subprocess
import sys
from pathlib import Path

# Configuracion de entorno para imports locales
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.logging import log_error, log_info, log_warn


def run_graphic_script(script_path: Path) -> bool:
    """Ejecuta un script individual de generacion de graficos."""
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)], capture_output=True, text=True, check=False
        )

        if result.returncode == 0:
            return True
        else:
            print(f"\n[ERROR] Fallo en {script_path.name}:")
            print(result.stderr)
            return False
    except Exception as e:
        log_error(f"Excepcion ejecutando {script_path.name}: {e}")
        return False


def orchestrate_assets():
    """Recorre la carpeta scripts/grafics y ejecuta todos los generadores."""
    project_root = Path(__file__).resolve().parents[1]
    grafics_dir = project_root / "scripts" / "grafics"

    if not grafics_dir.exists():
        log_error(f"No se encontro el directorio de graficos: {grafics_dir}")
        return

    log_info("Iniciando generacion masiva de activos graficos...")

    scripts = sorted(list(grafics_dir.rglob("*.py")))
    total = len(scripts)
    success_count = 0

    for i, script in enumerate(scripts, 1):
        rel_path = script.relative_to(grafics_dir)
        print(f"[{i}/{total}] Procesando: {rel_path}", end="\r")

        if run_graphic_script(script):
            success_count += 1

    print("\n" + "=" * 40)
    log_info(f"Proceso completado: {success_count}/{total} graficos generados con exito.")

    if success_count < total:
        log_warn(f"Hubo {total - success_count} fallos. Revisa los logs de error arriba.")


if __name__ == "__main__":
    orchestrate_assets()
