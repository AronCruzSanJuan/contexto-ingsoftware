# Práctica 4 — Diagrama de contexto

**Equipo:**
**Sistema:**
**Integrantes:**

---

## Parte A — Entidades externas y flujos

## Parte A – Entidades externas y flujos

Antes de dibujar, llenen esta tabla. Una fila por entidad externa. Tomen como punto de partida los participantes que identificaron en E1 y la especificación funcional del lunes.

| Entidad externa | Datos que le entrega al sistema | Datos que recibe del sistema |
| --- | --- | --- |
| Alumnos y docentes | Datos de la incidencia/falla (descripción, ubicación, evidencia/detalles) | Confirmación de reporte, estado y seguimiento de la incidencia |
| Personal de mantenimiento | Actualización del estado del reporte (en proceso, resuelto, etc.), observaciones | Consulta de reportes pendientes, detalles de las incidencias asignadas |
| Administradores del sistema | Configuraciones, gestión de usuarios, asignación de permisos/reportes | Reportes consolidados, métricas/estadísticas de operación, estado general del sistema |

***¿Qué quedó fuera del sistema y por qué?*** 
Se descartó al módulo o encargado de la **compra de refacciones/insumos para mantenimiento** como entidad externa. Aunque el personal de mantenimiento repara las fallas, el proceso de adquisición y pago de insumos es gestionado por un sistema administrativo/financiero independiente de la institución y no intercambia datos directamente con este sistema de reportes.

> 

---

## Parte C — Declaración de propósito

En 2 o 3 líneas: ¿para qué existe el sistema, a quién sirve y qué beneficio produce? No describan pantallas ni tecnología.

Se descartó al módulo o encargado de la compra de refacciones/insumos para mantenimiento como entidad externa. Aunque el personal de mantenimiento repara las fallas, el proceso de adquisición y pago de insumos es gestionado por un sistema administrativo/financiero independiente de la institución y no intercambia datos directamente con este sistema de reportes.
> 

---

## Parte D — Contenido de los flujos

Una fila por cada flecha de su diagrama. En "Datos que contiene" listen los datos concretos que viajan en ese flujo.

| Flujo | Origen -> Destino | Datos que contiene |
| --- | --- | --- |
| Datos de Incidencia | Alumnos Y Docentes -> Sistema De Reportes De Mantenimiento | Título del reporte, descripción de la falla, ubicación/edificio, categoría (eléctrica, mobiliario, etc.) y fecha de reporte |
| Confirmación y seguimiento | Sistema De Reportes De Mantenimiento -> Alumnos Y Docentes | Número de folio asignado, estado actual del reporte. |
| Consulta de reportes pendientes | Sistema De Reportes De Mantenimiento -> Personal de mantenimiento | Lista de incidencias abiertas, ubicación del problema, descripción detallada, datos de contacto del usuario |
| Estado del Reporte | Personal de mantenimiento -> Sistema De Reportes De Mantenimiento | Folio del reporte, nuevo estado (En proceso, Resuelto, Cancelado), observaciones del técnico, diagnóstico realizado |
| Configuraciones y asignaciones | Administradores del sistema -> Sistema De Reportes De Mantenimiento | Asignación de reportes a personal técnico específico, alta/baja de usuarios, cambio de roles y permisos del sistema |
| Reportes consolidados y métricas | Sistema De Reportes De Mantenimiento -> Administradores del sistema | Número de incidencias por categoría/edificio, índice de resolución, reportes pendientes |

---

## Declaración de uso de IA

Si no usaron IA, escriban «No usamos IA» en la primera fila.

| Herramienta | Para qué la usaron | Qué verificaron |
|---|---|---|
|  |  |  |
