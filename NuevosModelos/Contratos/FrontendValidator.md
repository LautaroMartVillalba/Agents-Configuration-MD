# FrontendValidator — Contrato

## INPUT
```yaml
task_id: <string>
detail_level: terse|technical          # NO soporta semantic
url: <string>                          # OBLIGATORIO, sin esto aborta status:failed
viewports:
  - {width: 1920, height: 1080, label: desktop}
  - {width: 768, height: 1024, label: tablet}
  - {width: 375, height: 667, label: mobile}
archivos:                              # estructura anidada created/edited por componente
  - archivo: CompanyCard.tsx
    created: [render(), handleClick()]
    edited: [componentDidUpdate()]
interacciones:
  - accion: hover|click|type|fill_form|navigate
    target: <string>
    valor: <string>                    # solo si type/fill
    label: <string>                    # nombre del screenshot
    resultado_esperado: <string>       # 1-2 frases: animación/redirect/info esperada
criterios:                             # 7 criterios frontend
  rotura_visual: {required: boolean}
  desalineacion: {required: boolean}
  textos: {required: boolean}
  colores: {required: boolean}
  responsive: {required: boolean}
  estados: {required: boolean}
screenshots_dir: {$PATH_RAIZ_DEL_PROYECTO}/screenshots/{task_id}
```

## OUTPUT
```yaml
status: ok|warnings|rejected
veredicto: APROBADO|APROBADO_CON_ALERTAS|REPROBADO
task_id: <string>
capturas:
  - viewport: <label>
    archivo: <path>
    estado: ok|issues
  - viewport: <label>
    archivo: <path>
    estado: ok|issues
    despues_interaccion: <string>      # label interaccion que originó la captura
hallazgos:
  - severidad: CRITICAL|HIGH|MEDIUM|LOW
    viewport: <label>
    archivo: <path>                    # CSS/TSX responsable
    linea: <int>                       # opcional
    categoria: ROTURA_VISUAL|DESALINEACION|TEXTOS|COLORES|RESPONSIVE|ESTADOS
    confianza: high|medium|low
    root_cause: <string>
    recomendacion: <string>            # NO implementa, solo indica
    evidence: {archivo, lineas, snippet}
    captura: <path>
resumen:
  por_viewport: [{viewport, issues}]
  total_issues: <int>
  comprobado:                          # flags true/false
    cache: <bool>
    animations: <bool>
    transactions: <bool>               # state atomic updates
    concurrency: <bool>
    logic: <bool>
    transitions: <bool>
    responsive: <bool>
    accessibility: <bool>
```
