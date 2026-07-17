# TestingFrontend — Contrato

## INPUT
```yaml
task_id: <string>
detail_level: terse|technical
objetivos:
  modulo: <string>
  descripcion: <string>
  tipo: unit|visual|functional|responsive|e2e   # tipo enum C.2
url: <string>                                    # OBLIGATORIO, aborta si vacío
viewports:
  - {width: 1920, height: 1080, label: desktop}
  - {width: 768, height: 1024, label: tablet}
  - {width: 375, height: 667, label: mobile}
scenarios:
  - id: <string>
    type: positive|negative|edge
    input:
      data: <objeto>
      setup: <string>
    expected:
      status: <code|int>
      shape: <json-schema-ish>
      invariant: <string>
    purpose: <string>
interacciones:
  - accion: hover|click|type|fill_form|navigate
    target: <string>
    valor: <string>                    # solo si type/fill
    esperado:
      tipo: renderizado|redirect|modal_open|modal_close|state_change|api_called|animation|error_display|no_change
      detalle: <string>                # 1-2 frases
    resultado_esperado: <string>       # prosa: animación/redirect/info esperada
criterios:                             # 7 criterios
  rotura_visual: {required: boolean}
  desalineacion: {required: boolean}
  textos: {required: boolean}
  colores: {required: boolean}
  responsive: {required: boolean}
  estados: {required: boolean}
  accessibility: {required: boolean}
screenshots_dir: {$PATH_RAIZ_DEL_PROYECTO}/screenshots/{task_id}
detener_si_falla:
  nivel: continuar|stop_and_suite|stop_module|stop_all
  umbral_porcentaje: <int>
```

## OUTPUT
```yaml
status: ok|partial|failed|blocked
task_id: <string>
confidence: high|medium|low
capturas:
  - viewport: <label>
    archivo: <path>
    estado: ok|issues
    despues_interaccion: <string>      # label interaccion (heredado de B.2)
resultados:
  - scenario_id: <string>
    status: pass|fail|skip
    asserts:
      pasados: <int>
      fallidos: <int>
    error: <string>
bugs:
  - scenario_id: <string>
    severidad: CRITICAL|HIGH|MEDIUM|LOW
    hipotesis: <string>                # SUPORE, no afirma
    reproducible: <bool>
    categoria: ROTURA_VISUAL|DESALINEACION|TEXTOS|COLORES|RESPONSIVE|ESTADOS|ACCESSIBILITY
resumen:
  total_scenarios: <int>
  pasados: <int>
  fallidos: <int>
  skip: <int>
  total_capturas: <int>
  stop_aplicado: <bool>
  razon_stop: <string>
```

### Determinism adapted (visual/functional)
- asserts exactos sobre estado del DOM / visibilidad — `expect(modal.hidden).toBe(false)` sí; `expect([true,false]).toContain(modal.hidden)` PROHIBIDO.
- Si página no carga / 404 / timeout → `status: blocked`, NO screenshot en blanco aprobado.
- 30% failure threshold → stop y reportar.
