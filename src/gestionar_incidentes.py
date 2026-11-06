"""
Módulo principal para gestionar incidentes de mantenimiento universitario.
"""

# RAMA AFRENTE (Entrada)


def leer_datos_usuario():
    """Obtiene el reporte inicial y el número de folio proporcionado por el usuario."""
    reporte_incidente = "Fuga de agua en edifici B"
    numero_folio = 1042
    return reporte_incidente, numero_folio

def leer_datos_tecnico():
    """Obtiene los datos de actualización proporcionados por el técnico."""
    datos_actualizacion = "Revisión completada CAMBIO RELIZADO."
    return datos_actualizacion

def validar_entradas(reporte_incidente, numero_folio, datos_actualizacion):
    """Valida y estructura las entradas antes de procesarlas"""
    datos_validados = {
        "folio": numero_folio,
        "reporte": reporte_incidente,
        "actualizacion": datos_actualizacion,
        "valido": True
    }
    return datos_validados

# RAMA CENTRAL (Transformación)
def procesar_logica_incidente(datos_validados):
    """Procesa la lógica de negocio del incidente de mantenimiento"""
    incidente_procesado = datos_validados.copy()
    incidente_procesado["estado_calculado"] = "En proceso de resolución"
    return incidente_procesado

def actualizar_estado_incidente(incidente_procesado):
    """Gestiona el cambio de estado del incidente (Integrando lógica de estados si aplica)."""
    estado_actual = incidente_procesado["estado_calculado"]
    return estado_actual

# RAMA EFERENTE (Salida)

def formatear_salida_reporte(incidente_procesado, estado_actual):
    """Prepara las cuplas de salida para el reporte y el historial."""
    datos_incidencia = f"Folio: {incidente_procesado['folio']} - {incidente_procesado['reporte']}"
    actualizacion_historial = f"Estado: {estado_actual} | Nota: {incidente_procesado['actualizacion']}"
    return datos_incidencia, actualizacion_historial

def almacenar_o_mostrar_resultados(datos_incidencia, actualizacion_historial):
    """Envía los datos procesados a su destino final (Reportes/Historial)."""
    print("[SALIDA SISTEMA]")
    print(f"-> Datos de Incidencia: {datos_incidencia}")
    print(f"-> Actualización / Historial: {actualizacion_historial}")

# MÓDULO PRINCIPAL (Coordinador)

def gestionar_incidentes():
    """Módulo principal que solo coordina: llama a sus tres ramas y nada más."""
    # 1. Llamada a Rama Aferente
    reporte_incidente, numero_folio = leer_datos_usuario()
    datos_actualizacion = leer_datos_tecnico()
    datos_validados = validar_entradas(reporte_incidente, numero_folio, datos_actualizacion)
    
    # 2. Llamada a Rama Central
    incidente_procesado = procesar_logica_incidente(datos_validados)
    estado_actual = actualizar_estado_incidente(incidente_procesado)
    
    # 3. Llamada a Rama Eferente
    datos_incidencia, actualizacion_historial = formatear_salida_reporte(incidente_procesado, estado_actual)
    almacenar_o_mostrar_resultados(datos_incidencia, actualizacion_historial)

if __name__ == "__main__":
    gestionar_incidentes()