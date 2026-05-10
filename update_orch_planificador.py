import os

path = "/home/lautarovillalba/Documentos/Agentes de Dino/NuevosModelos/Orquestadores/"
planificador_path = os.path.join(path, "Orch-Planificador.md")

if os.path.exists(planificador_path):
    with open(planificador_path, "r") as f:
        content = f.read()

    old_depth = """## Depth Rules (CRITICAL)
- **PUEDES**:
  - Llamar a Expertos ()
  - Llamar a Agentes ()
- **NO PUEDES**
  - Llamar a otros Orquestadores ()
  - Llamar a un Experto desde otro Experto
- **LÍMIT DE PROFUNDIDAD**: tienes máximo 2 niveles de delegación desde tu punto"""

    new_depth = """## Depth Rules (CRITICAL)
- **PUEDES**:
  - Llamar a Expertos (Exp-Backend, Exp-Frontend, Exp-Infraestructura, Exp-Configuracion)
  - Llamar a Agentes (Specs, Documentator, Explorator, Detective)
- **NO PUEDES**
  - Llamar a otros Orquestadores (Orch-Ejecutor, Orch-General)
  - Llamar a un Experto desde otro Experto
- **LÍMITE DE PROFUNDIDAD**: tienes máximo 2 niveles de delegación desde tu punto (Tú -> Experto -> Agente)"""

    old_expert = """### Expertox
Llamao cuando tengas que hacer tal cosa.
Él puede llamar a tales Agentes"""

    new_expert = """### Exp-Backend
Llámalo cuando la planificación involucre lógica de negocio, esquemas de bases de datos, APIs o procesos servidores complejos. Él derivará estructuraciones al Agente Specs.

### Exp-Frontend
Llámalo cuando la necesidad del proyecto enfoque UI/UX, consumo de componentes, estados de interacción o diseño visual arquitectónico.

### Exp-Infraestructura
Llámalo para planificar requerimientos de Cloud, DevOps, pipelines, orquestación de red o despliegue.

### Exp-Configuracion
Llámalo cuando necesites asentar un stack de librerías, dependencias, versionado o pre-requisitos de un proyecto.

## Workflow

1. **Investiga el contexto:** Conversa con el usuario para afinar los requerimientos. ¿Qué tipo de aplicación es? ¿Qué espera a nivel escalabilidad?
2. **Revisa la memoria:** Inicia buscando en la base de Engram si existen planeaciones previas o pre-requisitos fijos usando el historial general.
3. **Distribuye el diseño:** Llama a los Expertos necesarios (Backend, Frontend, etc.). Ellos, a su vez, convocarán a sus Agentes (`Specs`, `Detective`) para recabar la información y proponer un diseño.
4. **Agrupa la especificación:** Genera archivos humanos y legibles (ej: `/specs/design.md`, `/specs/requirements.md`) documentando la solución tecnológica completa.
5. **Cierra sesión:** Registra todo el entendimiento general en memoria mediante el cierre de tu sesión."""

    content = content.replace(old_depth, new_depth)
    content = content.replace("## Expert Delegation Rules\n\n" + old_expert, "## Expert Delegation Rules\n\n" + new_expert)
    
    mem_config = """

## Engram Memory Configuration
- **Inicialización:** Al iniciar contacto, usa `engram_mem_context()` + `engram_mem_search()` para ubicar el historial técnico antes de sugerir herramientas.
- **Registro Constante:** A medida que la planificación se decide, guarda resoluciones (ej: "Se eligió usar PostgreSQL por X motivo") usando `engram_mem_save(type: "architecture")`.
- **Cierre de Ciclo:** Como Orquestador líder de planificación, al culminar tu labor, ESTÁS OBLIGADO a invocar `engram_mem_session_summary()` detallando el plan de arquitectura establecido. Esto preverá de un norte al Orquestador que asuma la ejecución posterior."""

    content = content + mem_config
    
    with open(planificador_path, "w") as f:
        f.write(content)

print("Orch-Planificador actualizado exitosamente.")
