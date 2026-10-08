# Actividad del 7 de octubre: Del análisis al diseño

## Módulos y cohesión

| Proceso de nivel 1 | En una oración | Cohesión | Decisión de diseño |
|---|---|---|---|
| **1 Gestionar incidentes** | Registra el reporte de un usuario, valida su ubicación, genera un folio y actualiza el seguimiento del técnico. | Comunicacional | Se divide en los submódulos de su Nivel 2 (`1.1 Validar ubicación del incidente`, `1.2 Registrar incidente`, `1.3 Generar folio` y `1.4 Actualizar estado de incidente`), los cuales poseen cohesión funcional. |
| **2 Gestionar catálogo de ubicaciones** | Da de alta y mantiene las ubicaciones válidas del sistema para el reporte de incidentes. | Funcional | Se queda como está. Además, será el único módulo responsable de escribir y actualizar el almacén `[Ubicaciones]`. |

## Acoplamiento

| Entre | Qué comparten | Acoplamiento | Decisión de diseño |
|---|---|---|---|
| **1.1 Validar ubicación del incidente $\rightarrow$ 1.2 Registrar incidente** | `Solicitud validada` (objeto de datos con los datos mínimos del reporte) | De datos | Adecuado. Pasar únicamente el identificador de ubicación y la descripción necesaria para el registro. |
| **1.2 Registrar incidente $\rightarrow$ 1.3 Generar folio** | `Datos de folio` (identificador y marca de tiempo) | De datos | Adecuado. Se transfieren solo los datos indispensables para emitir el folio. |
| **Proceso 1 (`Gestionar incidentes`) y Proceso 2 (`Gestionar catálogo de ubicaciones`)** | Ambos acceden al almacén `[Ubicaciones]` | Común | Reducir acoplamiento asignando a `2 Gestionar catálogo de ubicaciones` la propiedad exclusiva de escritura en `[Ubicaciones]`. El Proceso 1 solo realiza consultas de validación. |

## Uso de IA

Verificamos que cada módulo y flujo respetara las definiciones de diseño arquitectónico.