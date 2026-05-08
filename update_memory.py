import os

path = "/home/lautarovillalba/Documentos/Agentes de Dino/NuevosModelos/Agentes/"

group1 = ["Specs.md", "FrontendDesigner.md", "BackendDesigner.md", "Documentator.md"]
group2 = ["CodeReviewer.md", "FrontendValidator.md", "BackendValidator.md", "Tester.md"]
group3 = ["Explorator.md", "Detective.md"]

mem1 = """## Engram Memory Configuration
- **Contexto Previo:** Usa `engram_mem_search` antes de diseñar para no contradecir decisiones previas.
- **Guardado Evolutivo:** Para arquitecturas, reglas o patrones, usa SIEMPRE `engram_mem_suggest_topic_key` para obtener una llave, y guárdalo pasándola en `engram_mem_save()`. Esto actualiza la información en vez de duplicarla.
- **Resolución de conflictos:** Si el guardado devuelve `judgment_required`, usa obligatoriamente `engram_mem_compare` para dictaminar si tu archivo reemplaza (supersedes) o complementa (compatible) a las memorias viejas.
- **Tipos de guardado:** `architecture`, `decision`, `pattern`.
"""

mem2 = """## Engram Memory Configuration
- **Registro de Hallazgos:** Registra bugs complejos o reiterativos con `engram_mem_save()` usando el formato estructurado (What/Why/Where/Learned).
- **Tipos de guardado:** `bugfix`, `discovery`.
- **Mantenimiento Base de Conocimiento:** Si al registrar un problema salta una alerta de conflicto (`judgment_required`), resuélvela con `engram_mem_compare`.
"""

mem3 = """## Engram Memory Configuration
- **Búsqueda exhaustiva:** Tu herramienta principal es `engram_mem_search`. Para encontrar el porqué de una configuración, usa `engram_mem_timeline` sobre el ID encontrado.
- **Registro de Inteligencia:** Si encuentras un link vital, documentación externa clave o un patrón global en la estructura del proyecto que debe ser recordado, usa `engram_mem_save(type: "learning")`.
"""

for file in os.listdir(path):
    if not file.endswith(".md"): continue
    
    filepath = os.path.join(path, file)
    with open(filepath, "r") as f:
        content = f.read()
    
    # Split content on '## Engram Memory'
    parts = content.split("## Engram Memory")
    if len(parts) == 2:
        base = parts[0]
        
        replacement = ""
        if file in group1:
            replacement = mem1
        elif file in group2:
            replacement = mem2
        elif file in group3:
            replacement = mem3
            
        new_content = base + replacement
        with open(filepath, "w") as f:
            f.write(new_content)

print("Archivos actualizados con la nueva configuracion de Engram Memory.")
