---
topic: agent-output-efficiency
expert: Exp-Configuracion
date: 2026-08-04
scope: agents
source: governance
status: active
supersedes: null
---

## Regla 1: Presupuestar salida por capa
**Contexto**: Varios modelos tienden a producir razonamientos y respuestas innecesariamente largas.
**Decisión**: Orquestadores responden como capa humana breve; Expertos procesan en profundidad pero reportan compacto; Hojas reciben qué hacer, ejecutan y reportan.
**Motivo**: Reducir inferencia, ruido y consumo de contexto sin cambiar modelos.
**Ámbito**: Todos los Orquestadores, Expertos y Agentes hoja del ecosistema.
**Ejemplo**: Orquestador máximo 6 frases, Experto máximo 8 frases, Hoja máximo 3 frases salvo contrato explícito.

## Regla 2: No narrar razonamiento
**Contexto**: La explicación paso a paso del razonamiento alarga respuestas y no mejora la ejecución del contrato.
**Decisión**: Los agentes no deben narrar cadena de pensamiento ni proceso interno; comunican resultado, estado, evidencia mínima, bloqueadores y próximos pasos.
**Motivo**: Mantener foco operativo y evitar que el Orquestador o usuario tengan que filtrar razonamiento innecesario.
**Ámbito**: Todos los agentes.
**Ejemplo**: Decir "Delegué a TestingAPI y reportó 2 fallos HIGH" en vez de explicar cómo se decidió cada escenario.

## Regla 3: Usar detail_level de forma conservadora
**Contexto**: Los contratos ya soportan `detail_level`, pero sin default operativo fuerte.
**Decisión**: `detail_level: terse` es el default. `technical` se usa solo si se necesita evidencia ampliada. `semantic` queda reservado para Explorator/Detective cuando el llamante necesita explicación humana.
**Motivo**: Controlar verbosidad desde el contrato sin cambiar modelos.
**Ámbito**: Delegaciones Experto -> Hoja y contratos hoja.
**Ejemplo**: Exp-Backend delega a BackendValidator con `detail_level: terse` y solo pide `technical` si necesita evidencia detallada de un hallazgo.

## Regla 4: Acotar evidencia
**Contexto**: Validators, Testing, Explorator y Detective necesitan evidencia, pero los logs/snippets largos saturan contexto.
**Decisión**: Reportar evidencia breve y representativa: snippets mínimos, errores literales relevantes, fuentes primarias y conteos; agrupar MEDIUM/LOW si hay volumen.
**Motivo**: Mantener precisión sin convertir reportes en dumps.
**Ámbito**: Hojas de validación, testing, exploración e investigación.
**Ejemplo**: Un fallo repetido en 12 endpoints se resume con conteo y 1-2 ejemplos representativos.

## Regla 5: Prohibir comandos no terminantes en hojas
**Contexto**: Comandos como `bun run dev` o watchers pueden dejar al agente en bucles sin resultado positivo.
**Decisión**: Las hojas no ejecutan servidores persistentes, watchers, prompts interactivos ni comandos que requieran interacción de consola.
**Motivo**: Evitar bloqueos operativos y reportes incompletos.
**Ámbito**: Agentes hoja con `bash: allow`, especialmente TestingBackend, TestingAPI y TestingFrontend.
**Ejemplo**: Usar `npm test -- --run` o `vitest run`; no usar `npm run dev`, `next dev` ni `vite --host`.

## Regla 6: No repetir contratos
**Contexto**: Algunos agentes explican el contrato en vez de cumplirlo.
**Decisión**: El agente cumple su contrato y no lo reexplica; tampoco agrega secciones extra si `restricciones_respuesta.no_secciones_extra: true`.
**Motivo**: Reducir ruido y asegurar salidas parseables.
**Ámbito**: Todos los contratos y prompts.
**Ejemplo**: Terminar con el bloque YAML requerido, sin una sección adicional de "Notas sobre el contrato".
