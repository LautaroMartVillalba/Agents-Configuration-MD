# BackendDesigner — Contrato

## INPUT
```yaml
task_id: <string>
detail_level: terse|technical          # NO soporta semantic
goal:
  action: CREATE|EDIT|REFACTOR|DELETE|MIGRATE|INTEGRATE   # verbo explícito
  target: <path o símbolo>             # ej: /src/modules/companies/, XService
  reason: <string>                     # 1 línea
archivos:
  crear: [<path>, ...]
  editar: [<path>, ...]
  referencia: [<path>, ...]           # patrones a imitar
  readonly: [<path>, ...]             # SOLO lectura para contexto
restricciones:
  inmutable:                          # NO tocar bajo ningún motivo
    - <path o símbolo>                # ej: XService.class, YService.class/yMethod()
    - <path o símbolo>
  comportamiento:                      # reglas OBLIGATORIAS en archivos donde SÍ se edita
    - archivo: <path>
      regla: <string>                 # ej: "preservar firma pública del método"
    - archivo: <path>
      regla: <string>
stack:
  lenguaje: <string>
  framework: <string>
  orm: <string>
patrones: [<string>, ...]
contexto: <string>                     # opcional
```

## OUTPUT
```yaml
status: ok|partial|failed
task_id: <string>
cambios:
  - archivo: <path>
    accion: created|edited|deleted
    lineas: [start, end]
    descripcion: <string>             # 1 línea
    documentacion_inline: full|partial|missing
  - archivo: <path>
    accion: ...
    lineas: ...
    descripcion: ...
    documentacion_inline: ...
impacto:                              # áreas afectadas — 5 fijos
  api: <bool>
  database: <bool>
  service: <bool>
  config: <bool>
  security: <bool>
dependencias:
  agregadas: [<paquete>, ...]
  removidas: [<paquete>, ...]
  config_modificada:                  # application.yml, .env, docker-compose.yml
    - archivo: <path>
      clave: <string>                 # ej: spring.datasource.url
      valor_anterior: <string>
      valor_nuevo: <string>
      requiere_restart: <bool>
pendientes:
  - tarea: <string>
    severidad: CRITICA|ALTA|MEDIA|BAJA
    bloqueante: <bool>
    razon: <string>                   # 1-2 frases
    archivo: <path>
    accion: CREATE|EDIT|REFACTOR|DELETE|MIGRATE|INTEGRATE   # MISMO enum que goal.action
```

### Notas
- `pendientes[].accion` usa MISMO enum que `goal.action` para que el orquestador arme directamente el próximo goal.
- Áreas de `impacto` cerradas: api, database, service, config, security (5 fijos, NO extendibles). Si no hay impacto de ningún tipo -> 'null'
- `restricciones` dividida en `inmutable` (intocables) + `comportamiento` (reglas en editables).
- `archivos.readonly` añadido para contexto sin permiso de edición.
