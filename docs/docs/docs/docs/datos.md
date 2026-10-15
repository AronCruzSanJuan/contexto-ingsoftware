## De almacenes a entidades

| Almacén del DFD | Qué guarda (una oración) | Entidad candidata | Identificador |
|---|---|---|---|
| D1 Incidencias | Cada incidencia reportada en el sistema, su estado actual y detalles de seguimiento. | Incidencia | @folio |
| D2 Ubicaciones | Las ubicaciones válidas de las instalaciones universitarias para registrar los incidentes. | Ubicacion | @id_ubicacion |

**Decisión:** 
¿Hay algún almacén que une a otros dos y además tiene datos propios?
Sí, el sistema gestiona la relación entre el usuario/técnico, la incidencia y la ubicación a través del registro de incidentes, donde se asocian la ubicación válida y el folio asignado.

## Diccionario de datos

### Almacenes

* **Reportes** = @folio + datos_ubicacion + descripcion_incidente + estado_incidente + (fecha_reporte) + (historial_actualizaciones)
* **Ubicaciones** = @id_ubicacion + nombre_area + edificio + piso + (observaciones)

### Flujos de frontera

* **Reporte de incidente** = datos_ubicacion + descripcion_incidente  *Flujo que entra desde el Usuario*
* **Número de folio** = @folio + fecha_reporte  *Flujo que sale hacia el Usuario*

### Estados / Categorías

* **estado_incidente** = ["pendiente" | "en proceso" | "atendido" | "cancelado"]

