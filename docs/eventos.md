## Lista de eventos

## Lista de eventos

| # | Evento | Tipo | Flujo de entrada | Respuesta del sistema |
|---|---|---|---|---|
| 1 | Usuario reporta un incidente | Flujo | Reporte de incidente | Valida los datos del incidente, registra el reporte en estado pendiente y entrega un número de folio al usuario. |
| 2 | Técnico concluye o avanza en la atención del incidente | Flujo | Datos de actualización | Registra el avance o cambio de estado del reporte (ej. En proceso, Resuelto) y actualiza el historial del mantenimiento. |
| 3 | Nueva área o ubicación requiere ser incorporada | Flujo | Datos de ubicación | Registra la nueva ubicación o edificio en el sistema para que esté disponible en los reportes. |