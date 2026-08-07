import os
import re
from pathlib import Path

def main():
    root = Path(__file__).resolve().parents[1]
    src_dir = root / "src"
    typst_dir = root / "scripts" / "grafics" / "typst_src"
    
    pillars = [d for d in src_dir.iterdir() if d.is_dir() and re.match(r'^\d{2}_', d.name)]
    
    for pillar in pillars:
        print(f"--- Revisando pilar: {pillar.name} ---")
        
        # Encontrar SVGs sueltos en la raiz del pilar
        loose_svgs = list(pillar.glob("*.svg"))
        
        # Encontrar todos los QMDs en las subcarpetas de este pilar
        qmd_files = list(pillar.rglob("*.qmd"))
        
        for svg in loose_svgs:
            svg_name = svg.name
            print(f"  Encontrado SVG suelto: {svg_name}")
            
            # Buscar que QMD lo referencia
            target_qmd = None
            target_nivel = None
            
            for qmd in qmd_files:
                try:
                    content = qmd.read_text(encoding="utf-8")
                    if f"({svg_name})" in content or f"/{svg_name})" in content:
                        target_qmd = qmd
                        target_nivel = qmd.parent.name
                        break
                except Exception as e:
                    pass
            
            if target_qmd:
                print(f"    Referenciado en: {target_qmd.name} (Nivel: {target_nivel})")
                new_svg_path = target_qmd.parent / svg_name
                
                # Mover SVG
                print(f"    Moviendo SVG a: {new_svg_path.relative_to(root)}")
                svg.rename(new_svg_path)
                
                # Buscar archivo Typst y renombrarlo
                old_typ_name = f"{pillar.name}___{svg.stem}.typ"
                new_typ_name = f"{pillar.name}___{target_nivel}___{svg.stem}.typ"
                
                old_typ_path = typst_dir / old_typ_name
                new_typ_path = typst_dir / new_typ_name
                
                if old_typ_path.exists():
                    print(f"    Renombrando script Typst a: {new_typ_name}")
                    old_typ_path.rename(new_typ_path)
                else:
                    # Puede que ya tenga algún prefijo?
                    print(f"    [!] Script Typst no encontrado en ruta esperada: {old_typ_name}")
            else:
                print(f"    [!] No se encontro QMD que referencie a {svg_name}")
                
        # Verificar referencias rotas en los QMD (ej. si algun QMD apunta a '../img.svg')
        for qmd in qmd_files:
            try:
                content = qmd.read_text(encoding="utf-8")
                new_content = content
                modified = False
                
                # Buscar imagenes markdown ![alt](ruta)
                # que tengan un path con carpetas, ej. src/01_fundamentos/img.svg o ../img.svg
                # y dejarlos solo con el nombre del archivo, asumiendo que el archivo esta en su misma carpeta.
                pattern = r'!\[([^\]]*)\]\((?:[./a-zA-Z0-9_]+?/)+([a-zA-Z0-9_]+\.svg)\)'
                def repl(match):
                    alt_text = match.group(1)
                    filename = match.group(2)
                    return f"![{alt_text}]({filename})"
                
                new_content, count = re.subn(pattern, repl, new_content)
                if count > 0:
                    print(f"  [FIX] Corrigiendo {count} rutas en {qmd.name}")
                    qmd.write_text(new_content, encoding="utf-8")
                    
            except Exception as e:
                pass

if __name__ == '__main__':
    main()
