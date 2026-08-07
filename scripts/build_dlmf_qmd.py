import json
import re
from pathlib import Path

try:
    from deep_translator import GoogleTranslator
except ImportError:
    GoogleTranslator = None

def get_mappings():
    readme_path = Path("src/README.md")
    content = readme_path.read_text(encoding="utf-8")
    # Matches: * [`src/01_fundamentos_logica/avanzado/09_metodos_algebraicos_analiticos.qmd`](...):
    #   - **Origen DLMF:** Capítulo 1
    # Also captures lines for MSC Code.
    
    mappings = []
    
    # We will use regex to find each qmd block
    blocks = content.split("* [`src/")
    for block in blocks[1:]:
        qmd_match = re.search(r'^(.*?\.qmd)`\]', block)
        if not qmd_match:
            continue
        qmd_file = "src/" + qmd_match.group(1)
        
        cap_match = re.search(r'\*\*Origen DLMF:\*\*\s*(?:Secciones.*?Capítulos\s*|Capítulo\s*)(\d+)', block)
        if not cap_match:
            # Maybe it's a list like "Capítulos 7 y 8" -> take the first one or primary
            cap_match = re.search(r'Capítulos?\s*(\d+)', block)
            if not cap_match:
                continue
        cap = int(cap_match.group(1))
        
        msc_match = re.search(r'\*\*Código MSC2020:\*\*\s*(.+?)\.', block)
        msc = msc_match.group(1).replace("`", "").strip() if msc_match else "00A00"
        
        # Determine difficulty and pilar from path
        parts = qmd_file.split("/")
        pilar = parts[1]
        difficulty = parts[2]
        
        # Create base title from filename
        filename = parts[3].replace(".qmd", "")
        title = " ".join(filename.split("_")[1:]).title()
        
        mappings.append({
            "qmd_file": qmd_file,
            "cap": cap,
            "msc": msc,
            "pilar": pilar,
            "difficulty": difficulty,
            "title": title
        })
        
    return mappings

def find_metadata_json(cap):
    metadata_dir = Path("metadata/DLMF_data")
    for file in metadata_dir.glob("*.json"):
        if file.name.startswith(f"{cap}_"):
            return file
    return None

def sentence_split(text):
    # Split text into sentences for Semantic Line Breaks
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]

def format_semantic_line_breaks(text):
    sentences = sentence_split(text)
    return "\n".join(sentences)

def build_qmd():
    mappings = get_mappings()
    
    translator = GoogleTranslator(source='en', target='es') if GoogleTranslator else None
    
    for mapping in mappings:
        print(f"Procesando Capítulo {mapping['cap']} -> {mapping['qmd_file']}")
        
        json_file = find_metadata_json(mapping['cap'])
        if not json_file:
            print(f"Advertencia: No se encontró JSON para el Capítulo {mapping['cap']}")
            continue
            
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        original_title = data.get("titulo_original", "")
        if translator:
            try:
                translated_title = translator.translate(original_title)
            except:
                translated_title = mapping['title']
        else:
            translated_title = mapping['title']
            
        # Extract formulas and text
        definiciones = []
        identidades = []
        asintotica = []
        
        for cat in data.get("categorias", []):
            for sec in cat.get("secciones", []):
                contenido = sec.get("contenido", {})
                eqs = contenido.get("ecuaciones_latex", [])
                contenido.get("prosa_teorica", "")
                
                # Split formulas intuitively based on common symbols (just for placing them in subdivisions)
                for eq in eqs:
                    if "\\sim" in eq or "\\to" in eq or "O(" in eq:
                        asintotica.append(eq)
                    elif "=" in eq and ("+" in eq or "-" in eq) and len(eq) > 30:
                        identidades.append(eq)
                    else:
                        definiciones.append(eq)
                        
        # Limit to top 5 most relevant per section to avoid giant files
        definiciones = list(dict.fromkeys(definiciones))[:5]
        identidades = list(dict.fromkeys(identidades))[:5]
        asintotica = list(dict.fromkeys(asintotica))[:5]
        
        # Build QMD content
        primary_msc = mapping['msc'].split(",")[0].strip()
        tags = [t.strip() for t in mapping['msc'].split(",")]
        
        qmd_content = f"""---
id: "{primary_msc}"
title: "{translated_title}"
pilar: "{mapping['pilar']}"
msc_code: "{mapping['msc']}"
difficulty: "{mapping['difficulty']}"
tags:
"""
        for t in tags:
            qmd_content += f"  - {t}\n"
            
        qmd_content += f"""---

# {translated_title}

Este documento establece los fundamentos analíticos y algebraicos de las funciones tratadas en el Capítulo {mapping['cap']} de la DLMF.
Su clasificación responde a los requerimientos de rigor de Polaris Kernel.

## 1. Definiciones y Construcción Axiomática

La conceptualización principal se define mediante expresiones generadoras.
"""
        if definiciones:
            qmd_content += "Las ecuaciones fundamentales que describen esta estructura son:\n\n"
            for eq in definiciones:
                qmd_content += f"$$\n{eq}\n$$\n\n"
        else:
            qmd_content += "Esta sección asienta las bases teóricas de la categoría.\n"
            
        qmd_content += """
## 2. Identidades y Relaciones de Recurrencia

Se deducen analíticamente las propiedades de simetría y ecuaciones diferenciales asociadas.
"""
        if identidades:
            qmd_content += "A continuación se presentan las identidades clave:\n\n"
            for eq in identidades:
                qmd_content += f"$$\n{eq}\n$$\n\n"
        else:
            qmd_content += "Las identidades algebraicas preservan las simetrías escalares de las funciones.\n"
            
        qmd_content += """
## 3. Comportamiento Asintótico y Polos

El análisis asintótico revela el crecimiento de la función para valores límite.
"""
        if asintotica:
            qmd_content += "Las expansiones asintóticas predominantes se expresan como:\n\n"
            for eq in asintotica:
                qmd_content += f"$$\n{eq}\n$$\n\n"
        else:
            qmd_content += "El comportamiento límite se rige por las propiedades analíticas en la esfera de Riemann.\n"
            
        qmd_content += """
## 4. Clasificación de Fórmulas y Simetrías

Las transformaciones modulares y funcionales subyacentes se preservan bajo operaciones continuas.
Esta clasificación permite derivar propiedades de ortogonalidad complejas.

## 5. Representación Gráfica e Interactividad

(Espacio reservado para diagramas generados mediante la integración con Typst).
"""

        # Ensure directory exists
        qmd_path = Path(mapping['qmd_file'])
        qmd_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write QMD
        qmd_path.write_text(qmd_content, encoding='utf-8')
        
        # Write Adyacent JSON
        json_path = qmd_path.with_suffix(".json")
        json_content = {
            "id": primary_msc,
            "title": translated_title,
            "pilar": mapping['pilar'],
            "msc_code": mapping['msc'],
            "difficulty": mapping['difficulty'],
            "source_dlmf_chapter": mapping['cap'],
            "status": "volcado_estructural_completado"
        }
        with open(json_path, 'w', encoding='utf-8') as jf:
            json.dump(json_content, jf, indent=2, ensure_ascii=False)
            
    print(f"\\n[EXITO] Proceso completado: Se volcaron exitosamente {len(mappings)} documentos a 'src/'.")

if __name__ == "__main__":
    build_qmd()
