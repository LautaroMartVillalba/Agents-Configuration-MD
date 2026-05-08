import os

path = "/home/lautarovillalba/Documentos/Agentes de Dino/NuevosModelos/Agentes/"

code_reviewer_path = os.path.join(path, "CodeReviewer.md")
backend_val_path = os.path.join(path, "BackendValidator.md")
frontend_val_path = os.path.join(path, "FrontendValidator.md")

# BackendValidator update
with open(backend_val_path, "r") as f:
    backend_content = f.read()

backend_role_addition = """- Detección de huecos de seguridad (Vulnerabilidades, Injections).
- Verificación exhaustiva de performancia (consultas lentas, complejidad algorítmica).
- Identificación de bucles infinitos, inconsistencias lógicas y faltas a la lógica de negocio."""

backend_response_addition = """- Tipo de problema identificado (PERFORMANCE, BUSINESS_LOGIC, SECURITY, BUCLE, LOGIC, CONVENTION).
- Desglose de hallazgos por archivo/línea y descripción concisa."""

backend_content = backend_content.replace(
    "- Verificación del flujo de la lógica de negocio.",
    "- Verificación del flujo de la lógica de negocio.\n" + backend_role_addition
)
backend_content = backend_content.replace(
    "- Desglose de hallazgos por archivo/línea (Errores, Mejoras recomendadas, Buenas prácticas omitidas).",
    backend_response_addition
)

with open(backend_val_path, "w") as f:
    f.write(backend_content)

# FrontendValidator update
with open(frontend_val_path, "r") as f:
    frontend_content = f.read()

frontend_role_addition = """- Prevención de huecos de seguridad en el cliente (XSS, manejo inseguro de estado/tokens).
- Auditoría de performancia y renderizado (re-renders innecesarios, bucles infinitos en hooks).
- Detección de inconsistencias lógicas en el flujo de usuario."""

frontend_response_addition = """- Categorización del problema detectado (PERFORMANCE, UI_LOGIC, SECURITY, ACCESSIBILITY, UX).
- Detalles sobre fallos responsivos (mobile/tablet/desktop) y visuales."""

frontend_content = frontend_content.replace(
    "- Revisión de ortografía, tono y correcta escritura en \"textos expuestos\" o de la interfaz.",
    "- Revisión de ortografía, tono y correcta escritura en \"textos expuestos\" o de la interfaz.\n" + frontend_role_addition
)

frontend_content = frontend_content.replace(
    "- Detalles sobre fallos responsivos (mobile/tablet/desktop).",
    frontend_response_addition
)

with open(frontend_val_path, "w") as f:
    f.write(frontend_content)

# Delete CodeReviewer
if os.path.exists(code_reviewer_path):
    os.remove(code_reviewer_path)
    print("CodeReviewer.md eliminado exitosamente.")

print("Validators actualizados exitosamente integrando las responsabilidades de CodeReviewer.")
