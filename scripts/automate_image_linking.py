import os
import re
from pathlib import Path

def parse_assets_record(record_path):
    """Parsea el archivo GENERATED_ASSETS.md para obtener la lista de activos."""
    assets = []
    if not record_path.exists():
        return assets
    
    content = record_path.read_text(encoding='utf-8')
    # Regex para capturar filas de la tabla Markdown
    # | ID | Pilar | Subtema | Desc | Ruta |
    pattern = re.compile(r'\|\s*`([^`]+)`\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*`([^`]+)`\s*\|')
    matches = pattern.findall(content)
    
    for m in matches:
        assets.append({
            "id": m[0].strip(),
            "pilar": m[1].strip(),
            "subtema": m[2].strip(),
            "desc": m[3].strip(),
            "path": m[4].strip()
        })
    return assets

def get_md_files(src_dir):
    """Obtiene metadatos de todos los archivos MD en src."""
    md_data = []
    for path in src_dir.rglob("*.md"):
        content = path.read_text(encoding='utf-8')
        # Extraer ID del frontmatter
        id_match = re.search(r'id:\s*([^\n]+)', content)
        tags_match = re.search(r'tags:\s*\[([^\]]+)\]', content)
        
        md_data.append({
            "path": path,
            "id": id_match.group(1).strip() if id_match else "",
            "tags": [t.strip() for t in tags_match.group(1).split(',')] if tags_match else [],
            "content": content
        })
    return md_data

def link_assets():
    project_root = Path(__file__).resolve().parents[1]
    record_path = project_root / "docs" / "GENERATED_ASSETS.md"
    src_dir = project_root / "src"
    
    assets = parse_assets_record(record_path)
    md_files = get_md_files(src_dir)
    
    print("Iniciando vinculacion automatica de imagenes...")
    
    for asset in assets:
        target_file = None
        
        # Estrategia 1: Coincidencia exacta de ID
        target_file = next((f for f in md_files if f["id"] == asset["id"]), None)
        
        # Estrategia 2: Heuristica por nombre y pilar (si no hay ID exacto)
        if not target_file:
            # Buscar en el mismo pilar archivos que compartan tags o subtemas
            for f in md_files:
                pilar_in_path = asset["pilar"] in str(f["path"]).replace("\\", "/")
                if pilar_in_path:
                    # Si el subtema esta en el nombre del archivo o en los tags
                    if asset["subtema"] in f["path"].name or asset["subtema"] in f["tags"]:
                        target_file = f
                        break
        
        if target_file:
            # Preparar link (ruta relativa al archivo MD)
            # Como estan en el mismo directorio, es solo el nombre del archivo
            img_filename = Path(asset["path"]).name
            img_markdown = f"\n![{asset['desc']}]({img_filename})\n"
            
            if img_filename not in target_file["content"]:
                # Inyectar tras el primer titulo #
                lines = target_file["content"].splitlines()
                new_lines = []
                injected = False
                for line in lines:
                    new_lines.append(line)
                    if not injected and line.startswith("# "):
                        new_lines.append(img_markdown)
                        injected = True
                
                target_file["path"].write_text("\n".join(new_lines), encoding='utf-8')
                print(f"Vinculado: {img_filename} -> {target_file['path'].name}")
            else:
                print(f"Omitido (ya existe): {img_filename} en {target_file['path'].name}")

if __name__ == "__main__":
    link_assets()
