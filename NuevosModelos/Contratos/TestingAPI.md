# TestingAPI — Contrato

## INPUT
```yaml
task_id: <string>
detail_level: terse|technical
objetivos:
  modulo: <string>
  descripcion: <string>
  tipo: contract|smoke|edge_cases|auth_flow|negative   # tipo enum C.3
  proposito: <string>                 # ej: "evitar duplicados", "verificar auth"
scenarios:
  - id: <string>
    type: contract|smoke|edge_cases|auth_flow|negative
    input:
      data: <objeto>
      setup: <string>
    expected:
      status: <code|int>               # EXACTO, no range
      shape: <json-schema-ish>
      invariant: <string>
    purpose: <string>
depends_on:                             # reemplaza dependencias
  - escenario: <string>
    requerido: <bool>                  # false = skip permitido pero no recomendado
detener_si_falla:
  nivel: continuar|stop_and_suite|stop_module|stop_all
  umbral_porcentaje: <int>
base_url: <string>
auth:                                   # opcional
  type: bearer|basic|api_key|cookie
  token_env: <env-var-name>            # NUNCA inline
```

## OUTPUT
```yaml
status: ok|partial|failed|blocked
task_id: <string>
confidence: high|medium|low
resultados:
  - scenario_id: <string>
    status: pass|fail|skip
    asserts:
      pasados: <int>
      fallidos: <int>
    request:                           # trazabilidad exacta
      method: GET|POST|PUT|PATCH|DELETE
      path: <string>
      headers: <objeto>                # sanitizado (sin tokens)
      body: <objeto>
      query: <objeto>
    respuesta_obtenida:                 #
      estado: <code|int>
      headers: <objeto>
      body: <objeto>
      time_ms: <int>
    error: <string>
bugs:
  - scenario_id: <string>
    severidad: CRITICAL|HIGH|MEDIUM|LOW
    hipotesis: <string>
    reproducible: <bool>
    categoria: CONTRACT|AUTH|VALIDATION|STATUS|SHAPE|PERFORMANCE|SECURITY
resumen:
  total_scenarios: <int>
  pasados: <int>
  fallidos: <int>
  skip: <int>
  dependencias_rotas: <int>
  stop_aplicado: <bool>
  razon_stop: <string>
```

### Determinism adapted (API contract)
- asserts exactos sobre HTTP status. `expect([200,403,404]).toContain(res.status())` PROHIBIDO.
- Si endpoint retorna 500 o no responde → `status: blocked`, declare bug en lugar de aprobar con rango amplio.
- `requerido: false` en depends_on = skip permitido pero buscar máxima cobertura primero.
- 30% failure threshold → stop y reportar.
