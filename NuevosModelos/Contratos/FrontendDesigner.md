# FrontendDesigner — Contrato

## INPUT
```yaml
task_id: <string>
detail_level: terse|technical          # NO soporta semantic
goal:
  action: CREATE|EDIT|REFACTOR|DELETE|MIGRATE|INTEGRATE
  target: <path o componente>          # ej: /src/components/companies/, CompanyCard.tsx
  reason: <string>
archivos:
  crear: [<path>, ...]
  editar: [<path>, ...]
  referencia: [<path>, ...]           # componentes/patrones a imitar (lectura para copia de estilo)
  readonly: [<path>, ...]             # contexto sin permiso de edición
restricciones:
  inmutable:                           # NO tocar bajo ningún motivo
    - <path o componente>              # ej: Button.tsx, ThemeProvider
    - <path o componente>
  comportamiento:                      # reglas OBLIGATORIAS en archivos editables
    - archivo: <path>
      regla: <string>                  # ej: "preservar firma de props pública"
    - archivo: <path>
      regla: <string>                  # ej: "mantener estado del form entre unmounts"
stack:
  lenguaje: <string>                   # ej: TypeScript
  framework: <string>                  # ej: React 18, Vue 3
  libreria_ui: <string>                # ej: MUI, Tailwind, shadcn/ui
  estado: <string>                     # ej: Zustand, Redux Toolkit, Context API
  design_tokens:                       # diseño visual — source of truth
    fuente: archivo|url
    path: <path o URL>                 # ej: /src/styles/tokens.css, https://figma.com/...
patrones: [<string>, ...]              # ej: "compound components", "HOC", "hooks custom"
componentes_relacionados:               # array — acoplamiento explícito cualitativo
  - fuente:
      path: <path>
      relacion: <string>                # relación breve: "consume su hook useCompany", "renderiza su children"
  - fuente:
      path: <path>
      relacion: <string>
```

## OUTPUT
```yaml
status: ok|partial|failed
task_id: <string>
cambios:
  - archivo: <path>
    accion: created|edited|deleted
    lineas: [start, end]
    descripcion: <string>              # 1 línea: qué se hizo
    props_nuevos:                       # SIEMPRE presente, incluso en edits internos
      - nombre: <string>
        tipo: <string>                 # ej: "string", "ReactNode", "(e: Event) => void"
        requerido: <bool>
        default: <string>              # opcional, si tiene default
        descripcion: <string>          # 1 línea
    comportamiento:                    # OPCIONAL por cambio — solo si aplica (componente stateful o con handlers)
      estado:                          # mutaciones de state (Zustand/Redux/Context)
        - slice: <string>              # ej: "companies", "ui.modal"
          accion: <string>              # ej: "added selector", "removed reducer"
      eventos:                         # handlers vinculados
        - tipo: <string>                # defaults sugeridos: onClick|onChange|onSubmit|onHover|onFocus|onBlur|onKeyDown — ABIERTO si ninguno encaja
          target: <string>             # ej: "submit-button", "search-input"
          descripcion: <string>        # 1 línea: qué dispara
  - archivo: <path>
    accion: ...
    lineas: ...
    descripcion: ...
    props_nuevos: [...]
  impacto:                             # áreas afectadas — 7 (extends A.1 con ui_ux + state)
    api: <bool>                        # contrato con backend (REST/GraphQL) cambió
    database: <bool>                   # false casi siempre en frontend puro
    service: <bool>                    # hooks/services de fetching
    config: <bool>                     # vite.config, tailwind.config, etc.
    security: <bool>                   # XSS, sanitización, JWT storage
    ui_ux: <bool>                      # layout, estilo, tokens visuales
    state: <bool>                      # store/context/selectors
dependencias:
  agregadas: [<paquete>, ...]          # ej: "@mui/x-data-grid"
  removidas: [<paquete>, ...]
  config_modificada:                    # vite.config.ts, tailwind.config.js, etc.
    - archivo: <path>
      clave: <string>
      valor_anterior: <string>
      valor_nuevo: <string>
      requiere_restart: <bool>
pendientes:
  - tarea: <string>
    severidad: CRITICA|ALTA|MEDIA|BAJA
    bloqueante: <bool>
    razon: <string>
    archivo: <path>
    accion: CREATE|EDIT|REFACTOR|DELETE|MIGRATE|INTEGRATE   # mismo enum que goal.action
```

## Notas
- `props_nuevos` SIEMPRE presente (inclusive en edits internos).
- `comportamiento.estado`/`comportamiento.eventos` OPCIONALES por cambio, solo si aplica.
- `design_tokens.fuente` enum `archivo|url` — sin `inline`.
- `eventos.tipo` default enum onClick|onChange|onSubmit|onHover|onFocus|onBlur|onKeyDown, ABIERTO si ninguno encaja.
- `componentes_relacionados` array de objetos `{fuente: {path, relacion}}` — relación cualitativa breve.
