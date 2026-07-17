# TestingBackend — Contrato

## INPUT
```yaml
task_id: <string>
detail_level: terse|technical
objetivos:
  modulo: <string>                     # ej: companies, auth
  descripcion: <string>                # 1-2 frases
  capa: unit|integration|repository    # capa enum (C.1)
scenarios:
  - id: <string>
    type: positive|negative|edge|boundary|error   # type enum
    input:
      data: <objeto json>
      setup: <string>                  # preparación previa, ej: "truncar tabla X"
    expected:
      status: <code|int>                # EXACTO, no range — determinismo
      shape: <json-schema-ish>          # estructura esperada
      invariant: <string>               # propiedad que debe cumplirse
    purpose: <string>                   # qué se intenta demostrar
detener_si_falla:
  nivel: continuar|stop_and_suite|stop_module|stop_all
  umbral_porcentaje: <int>              # default 30
framework: autodetect|<nombre>           # autodetect default
```

## OUTPUT
```yaml
status: ok|partial|failed|blocked       # blocked = prereq roto, no se pudo testear
task_id: <string>
confidence: high|medium|low            # transversal — Exp-Testing re-delega si low Y bugs>0
ejecucion:
  framework_detectado: <string>
  comando: <string>                    # ej: "pytest -x --tb=short"
  duracion_ms: <int>
  exit_code: <int>
cobertura:                              # si el framework lo reporta
  lineas: <float>
  ramas: <float>
  funciones: <float>
resultados:
  - scenario_id: <string>
    status: pass|fail|skip
    asserts:
      pasados: <int>
      fallidos: <int>
    error: <string>                    # si falló, mensaje literal
bugs:
  - scenario_id: <string>
    severidad: CRITICAL|HIGH|MEDIUM|LOW
    hipotesis: <string>                # NO descripcion — el tester SUPORE (no afirma)
    reproducible: <bool>
    categoria: LOGIC|ASSERTION|SETUP|ENV|DATA
resumen:
  total_scenarios: <int>
  pasados: <int>
  fallidos: <int>
  skip: <int>
  cobertura_alcanzada: <bool>
  stop_aplicado: <bool>                # si detener_si_falla disparó
  razon_stop: <string>                 # si stop_aplicado=true
```

### Determinism rules
- Asserts exactos OBLIGATORIOS. `expect([200,403,404]).toContain(...)` PROHIBIDO.
- Si prereq roto (setup falla, DB no levanta, fixture missing) → `status: blocked`, NO swallow test con asserts tolerantes.
- No hardcodear IDs mágicos para dodgear bugs que sí existen.
- 30% failure threshold → stop suite/module/all y reportar.
