---
topic: testing-domain-exclusivity
expert: Exp-Configuracion
date: 2026-08-02
scope: agent-governance
source: decision
status: active
---

## Regla 1: Testing es dominio exclusivo de agentes Testing
**Contexto**: Los agentes Designers (Backend/Frontend) y Validators (Backend/Frontend) no deben realizar testing. Cada tipo de agente tiene una responsabilidad bien delimitada en el pipeline.
**Decisión**: Prohibir terminantemente a BackendDesigner, FrontendDesigner, BackendValidator y FrontendValidator escribir, ejecutar o revisar tests. El testing es responsabilidad exclusiva de TestingBackend, TestingAPI, TestingFrontend y Exp-Testing.
**Motivo**: Separación de responsabilidades. Los Designers implementan, los Validators auditan código/capturas, los Testing agents verifican comportamiento. Mezclar roles genera duplicación, conflictos de interés y dilución de responsabilidad.
**Ámbito**: Agentes BackendDesigner.md, FrontendDesigner.md, BackendValidator.md, FrontendValidator.md — sección `## Reglas críticas`.
**Alternativas**: Permitir que Validators ejecuten tests como parte de su auditoría — rechazado porque la validación de runtime es un rol distinto al análisis estático/visual.
**Ejemplo**: Si BackendDesigner termina una implementación y se requiere testing, Exp-Backend o el Orquestador delegan a TestingBackend/TestingAPI. BackendDesigner nunca escribe `*.test.*` ni ejecuta `pytest`/`jest`.
