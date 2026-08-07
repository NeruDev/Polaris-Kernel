import os
import re
from pathlib import Path

def audit_formulas():
    src_dir = Path("src")
    qmd_files = list(src_dir.rglob("*.qmd"))
    
    doubtful_formulas = []
    
    # Common DLMF specific macros that break standard MathJax/KaTeX
    suspicious_patterns = [
        r'\\ifrac', r'\\NVar', r'\\cfracstyle', r'\\cc\b', r'\\cst\b', r'\\op\b',
        r'\\pv\b', r'\\real\b', r'\\imag\b', r'\\ph\b', r'\\mod\b', r'&[a-zA-Z]+;',
        r'\\left\s*$', r'\\right\s*$',  # Unmatched left/right at end of strings
    ]
    
    for qmd in qmd_files:
        content = qmd.read_text(encoding='utf-8')
        
        # Extract all $$ ... $$ blocks
        formulas = re.findall(r'\$\$(.*?)\$\$', content, re.DOTALL)
        
        for idx, formula in enumerate(formulas):
            formula_clean = formula.strip()
            
            # Check for unbalanced braces
            if formula_clean.count('{') != formula_clean.count('}'):
                doubtful_formulas.append({
                    "file": str(qmd),
                    "formula": formula_clean,
                    "reason": "Unbalanced braces { }"
                })
                continue
                
            # Check for suspicious macros
            for pat in suspicious_patterns:
                if re.search(pat, formula_clean):
                    doubtful_formulas.append({
                        "file": str(qmd),
                        "formula": formula_clean,
                        "reason": f"Suspicious pattern found: {pat}"
                    })
                    break
                    
    # Write report
    report_path = Path("temp_audit.md")
    if not doubtful_formulas:
        report_path.write_text("# Auditoría de Fórmulas\n\nNo se encontraron fórmulas dudosas.", encoding='utf-8')
    else:
        report = "# Auditoría de Fórmulas Dudosas\n\n"
        for i, df in enumerate(doubtful_formulas, 1):
            report += f"## {i}. Archivo: `{df['file']}`\n"
            report += f"**Motivo:** {df['reason']}\n\n"
            report += f"**Fórmula:**\n```latex\n{df['formula']}\n```\n\n"
            
        report_path.write_text(report, encoding='utf-8')
        
    print(f"Auditoría completada. {len(doubtful_formulas)} fórmulas dudosas encontradas. Reporte guardado en temp_audit.md")

if __name__ == "__main__":
    audit_formulas()
