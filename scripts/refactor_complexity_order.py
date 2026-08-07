import json
import re
from pathlib import Path


def get_level_index(level):
    levels = {"intro": 0, "intermedio": 1, "avanzado": 2, "abstracto": 3}
    return levels.get(level.lower(), 99)

def main():
    root = Path(__file__).resolve().parents[1]
    src_dir = root / "src"
    typst_dir = root / "scripts" / "grafics" / "typst_src"
    
    pillars = [d for d in src_dir.iterdir() if d.is_dir() and re.match(r'^\d{2}_', d.name)]
    
    for pillar in pillars:
        print(f"--- Processando pilar: {pillar.name} ---")
        
        # Encontrar jsons en el pilar (directos o ya en subcarpetas)
        json_files = list(pillar.rglob("*.json"))
        
        # 1. Parse metadatos y agrupar por nivel
        levels_map = {"intro": [], "intermedio": [], "avanzado": [], "abstracto": []}
        
        for jf in json_files:
            try:
                with open(jf, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                continue
                
            nivel = data.get("nivel", "intro").lower()
            if nivel not in levels_map:
                levels_map["intro"].append(jf)
                nivel = "intro"
            else:
                levels_map[nivel].append(jf)
        
        # 2. Renombrar y mover por nivel
        renames = []
        for nivel, files in levels_map.items():
            if not files:
                continue
            
            # Crear subcarpeta
            nivel_dir = pillar / nivel
            nivel_dir.mkdir(exist_ok=True)
            
            # Ordenar archivos alfabeticamente por nombre base (quitando prefijo numérico si existe)
            def get_base(p):
                return re.sub(r'^\d{2}_', '', p.stem)
                
            files.sort(key=get_base)
            
            for i, jf in enumerate(files, 1):
                base = get_base(jf)
                old_name = jf.stem
                new_prefix = f"{i:02d}_"
                new_name = f"{new_prefix}{base}"
                
                renames.append({
                    "old_path": jf.parent,
                    "old_name": old_name,
                    "new_name": new_name,
                    "nivel": nivel,
                    "base": base
                })
        
        # 3. Ejecutar los movimientos y renombramientos
        for item in renames:
            old_name = item["old_name"]
            new_name = item["new_name"]
            nivel = item["nivel"]
            base = item["base"]
            old_path = item["old_path"]
            nivel_dir = pillar / nivel
            
            # Mover y renombrar JSON
            old_json = old_path / f"{old_name}.json"
            new_json = nivel_dir / f"{new_name}.json"
            if old_json.exists():
                old_json.rename(new_json)
                
            # Mover y renombrar QMD
            old_qmd = old_path / f"{old_name}.qmd"
            new_qmd = nivel_dir / f"{new_name}.qmd"
            if old_qmd.exists():
                old_qmd.rename(new_qmd)
                
            # Mover y renombrar SVG
            svg_candidates = [old_path / f"{old_name}.svg", old_path / f"{base}.svg"]
            for cand in svg_candidates:
                if cand.exists():
                    new_svg = nivel_dir / f"{new_name}.svg"
                    cand.rename(new_svg)
                    break
                    
            # Renombrar Typst (el Typst file original puede estar con prefijos 01_ o sin ellos)
            typst_candidates = [
                typst_dir / f"{pillar.name}___{old_name}.typ",
                typst_dir / f"{pillar.name}___{base}.typ",
                typst_dir / f"{pillar.name}___{nivel}___{old_name}.typ",
                typst_dir / f"{pillar.name}___{nivel}___{base}.typ"
            ]
            for cand in typst_candidates:
                if cand.exists():
                    new_typ = typst_dir / f"{pillar.name}___{nivel}___{new_name}.typ"
                    if cand != new_typ:
                        cand.rename(new_typ)
                    break
        
        # 4. Actualizar referencias SVG dentro de los QMD
        # Los QMD ahora están en subcarpetas. Las referencias a sus propias imágenes SVG 
        # en la misma carpeta son simplemente "01_imagen.svg".
        qmd_files = list(pillar.rglob("*.qmd"))
        for qmd in qmd_files:
            try:
                with open(qmd, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                content_modified = False
                for item in renames:
                    old_name = item["old_name"]
                    new_name = item["new_name"]
                    base = item["base"]
                    
                    replace_pairs = [
                        (f"({old_name}.svg)", f"({new_name}.svg)"),
                        (f"({base}.svg)", f"({new_name}.svg)"),
                    ]
                    
                    for old_str, new_str in replace_pairs:
                        if old_str in content:
                            content = content.replace(old_str, new_str)
                            content_modified = True
                            
                if content_modified:
                    with open(qmd, "w", encoding="utf-8") as f:
                        f.write(content)
            except Exception as e:
                print(f"Error updating references in {qmd}: {e}")

if __name__ == '__main__':
    main()
