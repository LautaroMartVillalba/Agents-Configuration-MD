# BackendValidator — Contrato

## INPUT
```yaml
task_id: <string>
detail_level: terse|technical          # NO soporta semantic
archivos:                               # focaliza atención del validador
  - archivo: EjemploService             # nombre o path
      created:
        - xMethod()
        - yMethod()
      edited:
        - aMethod()
  - archivo: OtroEjemploController
      created: [...]
      edited: [...]
criterios:                              # cada criterio SIEMPRE item con required
  performance: {required: true}
  business_logic: {required: true}
  security: {required: true}
  logic: {required: true}
  edge_cases: {required: false}
  convention: {required: false}
  bucle: {required: false}
  transactionality: {required: false}  # manejo de transacciones DB
```

Criterio `required: true` no verificable → se reporta como hallazgo CRITICAL, confianza low, root_cause "criterio requerido no verificable".

## OUTPUT
```yaml
status: ok|warnings|rejected
veredicto: APROBADO|APROBADO_CON_ALERTAS|REPROBADO   # enum final
task_id: <string>
hallazgos:
  - severidad: CRITICAL|HIGH|MEDIUM|LOW
    archivo: <path>
    linea_inicio: <int>
    linea_fin: <int>
    categoria: PERFORMANCE|BUSINESS_LOGIC|SECURITY|BUCLE|LOGIC|CONVENTION|TRANSACTIONALITY
    confianza: high|medium|low
    root_cause: <string>              # POR QUÉ de la alerta, 1-2 frases
    recomendacion: <string>           # CÓMO solucionar, 1-2 frases, sin implementar
    evidence:
      archivo: <path>
      lineas: [start, end]
      snippet: <string>               # extracto LITERAL del código, breve
resumen:
  total_hallazgos: <int>
  por_severidad: {CRITICAL, HIGH, MEDIUM, LOW}
  archivos_afectados: <int>
  criterios_verificados: <int>
  criterios_no_verificables: <int>
```

**Mapeo status↔veredicto**: ok→APROBADO (sin CRIT ni HIGH) · warnings→APROBADO_CON_ALERTAS (0 CRIT) · rejected→REPROBADO (>0 CRIT o required:true no verificable).
