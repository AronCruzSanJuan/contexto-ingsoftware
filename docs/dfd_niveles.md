## Agrupación del nivel 1

| Proceso de nivel 1 | Agrupa (procesos preliminares) | Criterio |
|---|---|---|
| 1 Gestionar incidentes | 1 Registrar incidente + 2 Actualizar estado de incidente | Mismo almacén (`[Reportes]`) y misma área de negocio (Atención y seguimiento de incidentes) |
| 2 Gestionar catálogo de ubicaciones | 3 Registrar ubicación | Única operación de administración sobre el almacén `[Ubicaciones]` por el Administrador |

## Balanceo del nivel 1

- **Reporte de incidente:** Entrada desde la entidad `Usuario` hacia el proceso `1 Gestionar incidentes`
- **Número de folio:** Salida del proceso `1 Gestionar incidentes` hacia la entidad `Usuario`
- **Datos de actualización:** Entrada desde la entidad `Técnico` hacia el proceso `1 Gestionar incidentes`
- **Datos de ubicación:** Entrada desde la entidad `Administrador` hacia el proceso `2 Gestionar catálogo de ubicaciones`

## Nivel 2 del proceso 1: Gestionar incidentes

| Subproceso | Entra | Sale |
|---|---|---|
| **1.1 Validar ubicación del incidente** | `Reporte de incidente` (de Usuario); `Ubicación válida` (de Almacén `[Ubicaciones]`) | `Solicitud validada` (a 1.2) |
| **1.2 Registrar incidente** | `Solicitud validada` (de 1.1) | `Datos de incidente` (a Almacén `[Reportes]`); `Datos de folio` (a 1.3) |
| **1.3 Generar folio** | `Datos de folio` (de 1.2) | `Número de folio` (a entidad Usuario) |
| **1.4 Actualizar estado de incidente** | `Datos de actualización` (de entidad Técnico); `Estado actual` (de Almacén `[Reportes]`) | `Actualización / Historial` (a Almacén `[Reportes]`) |

## Balanceo del level 2 - proceso 1

- **Reporte de incidente:** Llega desde la entidad `Usuario` e ingresa al subproceso `1.1 Validar ubicación del incidente`.
- **Número de folio:** Sale del subproceso `1.3 Generar folio` hacia la entidad `Usuario`.
- **Datos de actualización:** Llega desde la entidad `Técnico` e ingresa al subproceso `1.4 Actualizar estado de incidente`.
- **Ubicación válida:** Proviene del almacén `[Ubicaciones]` e ingresa al subproceso `1.1 Validar ubicación del incidente`.
- **Datos de incidente:** Sale del subproceso `1.2 Registrar incidente` hacia el almacén `[Reportes]`.
- **Actualización / Historial:** Sale del subproceso `1.4 Actualizar estado de incidente` hacia el almacén `[Reportes]`.

## Uso de IA

Usamos Google Gemini para apoyar en la estructuración de las tablas de balanceo del nivel 1 y nivel 2, así como en la generación del código XML para los diagramas en Draw.io (`dfd_nivel1.drawio` y `dfd_nivel2_proceso_1.drawio`). Verificamos que todos los flujos e interacciones estuvieran balanceados contra el diagrama de contexto.