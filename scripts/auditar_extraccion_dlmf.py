import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
METADATA_DIR = os.path.join(BASE_DIR, "metadata", "DLMF_data")
INDEX_PATH = os.path.join(METADATA_DIR, "DLMF_indice_completo.json")
AUDIT_REPORT_PATH = os.path.join(METADATA_DIR, "AUDITORIA_EXTRACCION.json")

def main():
    print("Iniciando Auditoría de Extracción de Metadatos DLMF...")

    if not os.path.exists(INDEX_PATH):
        print(f"[ERROR CRÍTICO] No se encontró el índice principal: {INDEX_PATH}")
        sys.exit(1)

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        index_data = json.load(f)

    total_capitulos_esperados = len(index_data["capitulos"])
    capitulos_auditados = 0
    total_secciones_esperadas = 0
    total_secciones_completadas = 0
    total_formulas = 0
    total_palabras_clave = 0
    total_referencias_cruzadas = 0
    total_tablas = 0

    errores = []
    detalles_por_capitulo = []

    for cap in index_data["capitulos"]:
        num = cap["capitulo"]
        title = cap["titulo"]
        json_file_rel = cap["archivo_metadata"]
        json_path = os.path.join(BASE_DIR, json_file_rel)

        if not os.path.exists(json_path):
            errores.append(f"Capítulo {num}: No existe el archivo JSON {json_file_rel}")
            continue

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                sec_data = json.load(f)
        except Exception as e:
            errores.append(f"Capítulo {num}: Error al deserializar JSON: {str(e)}")
            continue

        capitulos_auditados += 1
        cap_secciones = 0
        cap_secciones_ok = 0
        cap_formulas = 0
        cap_keywords = 0
        cap_refs = 0
        cap_tablas = 0

        for cat in sec_data.get("categorias", []):
            for sec in cat.get("secciones", []):
                total_secciones_esperadas += 1
                cap_secciones += 1

                contenido = sec.get("contenido")
                if not contenido:
                    errores.append(f"Capítulo {num} Sección {sec.get('seccion_id')}: Falta el objeto 'contenido'")
                    continue

                estado = contenido.get("estado")
                if estado == "completado":
                    cap_secciones_ok += 1
                    total_secciones_completadas += 1
                else:
                    errores.append(f"Capítulo {num} Sección {sec.get('seccion_id')}: Estado no completado ({estado})")

                # Verify data types
                prosa = contenido.get("prosa_teorica")
                formulas = contenido.get("formulas_clave")
                ecuaciones = contenido.get("ecuaciones_latex")
                tablas = contenido.get("tablas")
                refs = contenido.get("referencias_cruzadas")
                meta = contenido.get("metadatos")

                if not isinstance(prosa, str):
                    errores.append(f"Capítulo {num} Sección {sec.get('seccion_id')}: 'prosa_teorica' no es string")
                if not isinstance(formulas, list):
                    errores.append(f"Capítulo {num} Sección {sec.get('seccion_id')}: 'formulas_clave' no es list")
                if not isinstance(ecuaciones, list):
                    errores.append(f"Capítulo {num} Sección {sec.get('seccion_id')}: 'ecuaciones_latex' no es list")
                if not isinstance(tablas, list):
                    errores.append(f"Capítulo {num} Sección {sec.get('seccion_id')}: 'tablas' no es list")
                if not isinstance(refs, list):
                    errores.append(f"Capítulo {num} Sección {sec.get('seccion_id')}: 'referencias_cruzadas' no es list")
                if not isinstance(meta, dict):
                    errores.append(f"Capítulo {num} Sección {sec.get('seccion_id')}: 'metadatos' no es dict")

                num_f = len(formulas) if isinstance(formulas, list) else 0
                num_kw = len(meta.get("palabras_clave", [])) if isinstance(meta, dict) else 0
                num_r = len(refs) if isinstance(refs, list) else 0
                num_t = len(tablas) if isinstance(tablas, list) else 0

                cap_formulas += num_f
                cap_keywords += num_kw
                cap_refs += num_r
                cap_tablas += num_t

        total_formulas += cap_formulas
        total_palabras_clave += cap_keywords
        total_referencias_cruzadas += cap_refs
        total_tablas += cap_tablas

        detalles_por_capitulo.append({
            "capitulo": num,
            "titulo": title,
            "secciones_totales": cap_secciones,
            "secciones_completadas": cap_secciones_ok,
            "formulas_extraidas": cap_formulas,
            "palabras_clave": cap_keywords,
            "referencias_cruzadas": cap_refs,
            "tablas": cap_tablas,
            "estado": "OK" if cap_secciones == cap_secciones_ok else "ERROR"
        })

    reporte_audit = {
        "titulo": "Informe de Auditoría de Extracción de Metadatos DLMF",
        "resumen_ejecutivo": {
            "total_capitulos_esperados": total_capitulos_esperados,
            "total_capitulos_auditados": capitulos_auditados,
            "total_secciones_esperadas": total_secciones_esperadas,
            "total_secciones_completadas": total_secciones_completadas,
            "porcentaje_exito_secciones": f"{(total_secciones_completadas / total_secciones_esperadas * 100):.2f}%" if total_secciones_esperadas else "0%",
            "total_formulas_extraidas": total_formulas,
            "total_palabras_clave_extraidas": total_palabras_clave,
            "total_referencias_cruzadas": total_referencias_cruzadas,
            "total_tablas_extraidas": total_tablas,
            "total_errores_detectados": len(errores)
        },
        "errores": errores,
        "detalles_por_capitulo": detalles_por_capitulo
    }

    with open(AUDIT_REPORT_PATH, 'w', encoding='utf-8') as f:
        json.dump(reporte_audit, f, ensure_ascii=False, indent=2)

    print("\n" + "="*70)
    print("                RESULTADOS DE LA AUDITORÍA DLMF                 ")
    print("="*70)
    print(f" Capítulos procesados:             {capitulos_auditados}/{total_capitulos_esperados}")
    print(f" Subsecciones verificadas:         {total_secciones_completadas}/{total_secciones_esperadas} ({reporte_audit['resumen_ejecutivo']['porcentaje_exito_secciones']})")
    print(f" Fórmulas LaTeX extraídas:         {total_formulas}")
    print(f" Palabras clave indexadas:          {total_palabras_clave}")
    print(f" Referencias cruzadas:             {total_referencias_cruzadas}")
    print(f" Tablas de datos extraídas:        {total_tablas}")
    print(f" Errores detectados:               {len(errores)}")
    print("="*70)

    if errores:
        print("\n[ALERT] Se detectaron errores durante la auditoría:")
        for err in errores[:10]:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("\n[ÉXITO TOTAL] ¡Todos los datos cumplen con la especificación de tipo y completitud!")

if __name__ == "__main__":
    main()
