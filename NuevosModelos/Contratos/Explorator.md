# Explorator — Contrato

## INPUT
```yaml
task_id: <string>
detail_level: terse|technical|semantic       # ÚNICO que soporta semantic (junto Detective)
operation:
  type: buscar_endpoints|trazar_flujo|inventariar_modulo|buscar_referencias|comparar_patrones|identificar_dead_code|mapear_dependencias|ubicar_slot|extraer_contrato
  module:
    directorios: [<path>, ...]
    archivos: [<path>, ...]
    indeterminado: <bool>               # true = buscar en todo el proyecto
capability:                              # reemplaza tipo_resultado
  - locate|trace|inventory|compare|map|extract|identify
profundidad: <int>                       # 0=directo, -1=todo, default 1
```

## OUTPUT
```yaml
status: ok|partial|failed
task_id: <string>
snippets:
  - archivo: <path>
    lineas: [start, end]
    relevancia: <string>                # 1 línea
flujo:                                  # si capability incluye trace
  nodes: [<string>, ...]                # símbolos involucrados
  edges:
    - from: <string>
      to: <string>
      edge_types:                       # enum
        - calls|creates|reads|writes|publishes|subscribes|imports|extends|implements|throws|returns
mapa:                                   # si capability incluye inventory/map
  <modulo>:
    controllers: [<string>, ...]
    services: [<string>, ...]
    repositories: [<string>, ...]
    models: [<string>, ...]
    config: [<string>, ...]
    routers: [<string>, ...]
    handlers: [<string>, ...]
    hooks: [<string>, ...]
    utils: [<string>, ...]
    types: [<string>, ...]
    puntos_interes: [<string>, ...]     # fusionado
summary: <string>                       # SOLO si detail_level=semantic — prosa
```

### Notas
- `operation.type` es enum ABIERTO a agregaciones nuevas (no cerrado).
- `detail_level: semantic` añade `summary` en prosa al final del output.
- `mapa` sub-llaves: enum cerrado `controllers|services|repositories|models|config|routers|handlers|hooks|utils|types|otros`.
