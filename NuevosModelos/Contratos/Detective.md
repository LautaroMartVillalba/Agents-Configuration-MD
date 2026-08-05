# Detective — Contrato

## INPUT
```yaml
task_id: <string>
detail_level: terse|technical|semantic
restricciones_respuesta:
  max_resumen_frases: 3
  narrar_razonamiento: false
  no_secciones_extra: true
operation:
  type: buscar_endpoints|trazar_flujo|inventariar_modulo|buscar_referencias|comparar_patrones|identificar_dead_code|mapear_dependencias|ubicar_slot|extraer_contrato
  module:
    directorios: [<path>, ...]
    archivos: [<path>, ...]
    indeterminado: <bool>
capability:
  - locate|trace|inventory|compare|map|extract|identify
profundidad: <int>
consultas:
  - termino: <string>                   # NO urls_probables (ELIMINADO)
requerimientos_implicitos:              # opcional
  - <string>
```

## OUTPUT
```yaml
status: ok|partial|failed
task_id: <string>
fuentes:
  - url: <string>
    tipo: docs|repo|blog|spec|cookbook|so|github|other
    acceso: public|auth_required|paywall|rate_limited
    relevancia: alta|media|baja
opciones:                               # min 2
  A:
    titulo: <string>
    pros: [<string>, ...]
    contras: [<string>, ...]
    certainty: exact|likely|partial
  B:
    titulo: <string>
    pros: [...]
    contras: [...]
    certainty: exact|likely|partial
summary: <string>                       # SOLO si detail_level=semantic
```

### Notas
- `opciones` letras A-Z libre — mínimo 2. El experto llamante define cuántas según necesidad.
- `certainty` enum: exact (matches docs/API oficial), likely (deducido de fuentes sólidas), partial (incompleto).
- `fuentes.acceso` ayuda al orquestador a decidir si vale re-buscar o conformarse.
- Default `detail_level: terse`. Usar `semantic` solo si el llamante necesita explicación humana.
- Evidencia breve y representativa: fuentes primarias primero; no narrar razonamiento ni repetir el contrato.
