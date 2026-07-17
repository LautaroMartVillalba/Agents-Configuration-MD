# Orchestrator-Experto — Contrato (interfaz Orquestador↔Experto)

## INPUT Orquestador → Experto
```yaml
task_id: <string>                     # generado por Orquestador, propagado por Experto a cada hoja
descripcion: <string>                 # TAREA del usuario en lenguaje natural, preservando intent + alcance
ambito: [<string>, ...]               # sub-dominios semánticos (ej: "módulo companies") — opcional
prioridad: CRITICA|ALTA|MEDIA|BAJA     # para que el Experto decida triage interno
```

## OUTPUT Experto → Orquestador
```yaml
status: ok|partial|failed
task_id: <string>
resumen_ejecutivo: <string>            # prosa 2-4 frases — para que el Orquestador responda al humano naturalmente
delegaciones_realizadas:               # contador por agente hoja invocado
  BackendDesigner: <int>
  FrontendDesigner: <int>
  BackendValidator: <int>
  FrontendValidator: <int>
  TestingBackend: <int>
  TestingFrontend: <int>
  TestingAPI: <int>
  Explorator: <int>
  Detective: <int>
pendientes_usuario:                    # lo que el humano necesita saber/decidir
  - severidad: CRITICA|ALTA|MEDIA|BAJA
    descripcion: <string>              # ej: "Falta spec de UI para módulo X"
    requiere_accion_usuario: <bool>    # true = el humano debe responder
    bloqueante: <bool>                  # true = el flujo NO continúa sin resolver esto
rules_emitidas:                         # transparencia — capability Rules persistida a .github/rules/**
  - topic: <string>
    archivo: <path>
    accion: created|updated|superseded|deprecated
proximos_pasos:                         # continuidad sugerida al Orquestador
  - descripcion: <string>
    razon: <string>
```

## Workflow del Orquestador
1. Recibir mensaje usuario.
2. (Opcional) Si falta contexto para decidir routing → delegar a `Explorator` con contrato D.1.
3. Seleccionar `experto` + packear `descripcion` (casi verbatim del usuario) + `ambito?` + `prioridad`.
4. Lanzar `task()` con YAML INPUT del contrato. Recibir YAML OUTPUT del Experto.
5. Mostrar `resumen_ejecutivo` al usuario.
6. Iterar `pendientes_usuario[]`:
   - si `bloqueante: true` → suspender ejecución y subir el pendiente al humano
   - si solo `requiere_accion_usuario: true` (no bloqueante) → avisar y seguir
7. Si `proximos_pasos[]` no vacío → sugerir continuidad al usuario (sin forzar — la decisión de invocar otro Experto es del Orquestador, no del Experto que respondió).

## Variantes por Orquestador
- **Orch-Ejecutor**: ante `status: failed` del Experto → decide reintento con `descripcion` aumentada, o sube al humano. Libre de planificar.
- **Orch-Planificador**: puebla Engram + ayuda al humano a articular `descripcion` y entender el problema o lo que está buscando hacer. No implementa.
- **Orch-General**: conversaciones generales sin agenda fija.

## Trazabilidad
`task_id` único generado por el Orquestador. El Experto lo incluye en su OUTPUT y lo propaga a cada `task()` a las hojas (cada hoja recibe su propio `task_id` internamente, pero el `task_id` raíz queda en el hilo). Permite al Orquestador correlacionar todo el flujo.

## Learned
- **`bloqueante` vs `requiere_accion_usuario`** son ortogonales: puede haber pendiente que requiere input pero el Experto puede seguir trabajando en otra tarea no dependiente, o pendiente que detiene todos los hilos.
