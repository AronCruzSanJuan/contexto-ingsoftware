# Minispecs - Práctica 7

## Minispec 1
- **Proceso:** 1.1 Validar ubicación del incidente
- **Entradas:** `Reporte de incidente` (proveniente del Usuario), `Ubicaciones` (proveniente del almacén de ubicaciones)
- **Salidas:** `Solicitud validada`
- **Almacenes:** `[Ubicaciones]` (Solo Lectura - R)
- **Lógica (Español estructurado):**
  SI (se recibe "Reporte de incidente") ENTONCES
      Leer el campo de ubicación del reporte.
      Consultar el almacén [Ubicaciones] para verificar si la ubicación existe.
      SI (la ubicación es válida y se encuentra en el área de cobertura) ENTONCES
          Generar y emitir la "Solicitud validada" hacia el proceso 1.2.
      SINO
          Mostrar mensaje de error: "Ubicación no válida".
          Rechazar el reporte y solicitar corrección al usuario.
      FIN_SI
  FIN_SI

---

## Minispec 2
- **Proceso:** 1.2 Registrar incidente
- **Entradas:** `Solicitud validada`
- **Salidas:** `Datos de incidente`
- **Almacenes:** `[Reportes]` (Lectura y Escritura - R/W)
- **Lógica (Español estructurado):**
  SI (se recibe "Solicitud validada") ENTONCES
      Extraer la información completa del incidente.
      Asignar un estatus inicial al reporte (por ejemplo: "Registrado").
      Guardar el registro completo en el almacén de datos [Reportes].
      Enviar los "Datos de incidente" hacia el proceso 1.3 para su procesamiento.
  FIN_SI

---

## Minispec 3
- **Proceso:** 1.3 Generar folio
- **Entradas:** `Datos de incidente`
- **Salidas:** `Número de folio` (hacia el Usuario)
- **Almacenes:** `[Reportes]` (Lectura y Escritura - R/W)
- **Lógica (Español estructurado):**
  SI (se reciben "Datos de incidente") ENTONCES
      Generar un código o número de folio único secuencial para el reporte.
      Vincular el "Número de folio" generado con el registro correspondiente en el almacén [Reportes].
      Enviar el "Número de folio" de regreso al Usuario para su consulta y seguimiento.
  FIN_SI

---

## Minispec 4
- **Proceso:** 1.4 Actualizar estado de incidente
- **Entradas:** `Datos de actualización`
- **Salidas:** `Actualización / Historial`
- **Almacenes:** `[Reportes]` (Lectura y Escritura - R/W)
- **Lógica (Tabla de Decisión):**

Proceso 1.4 Actualizar estado de incidente. Tres condiciones dan $2^3 = 8$ reglas; con «–» (no importa) quedan 4.

| Condiciones / Reglas | R1 | R2 | R3 | R4 |
| :--- | :---: | :---: | :---: | :---: |
| **C1** ¿Folio existente? | N | S | S | S |
| **C2** ¿Técnico autorizado? | – | N | S | S |
| **C3** ¿Nuevo estado válido? | – | – | N | S |
| **Acciones** | | | | |
| **A1** Mostrar error de folio inexistente | X | | | |
| **A2** Mostrar error por falta de permisos | | X | | |
| **A3** Mostrar error de estado inválido | | | X | |
| **A4** Actualizar estado en almacén `[Reportes]` y generar historial | | | | X |