import sqlite3
from datetime import datetime
import etl_inserts

def obtener_fechas(cursor):
    cursor.execute("""
        SELECT DISTINCT DATE(fecha_inicio) as fecha FROM estudios_historialestudio
        UNION
        SELECT DISTINCT DATE(fecha_fin) as fecha FROM estudios_historialestudio
        WHERE fecha_fin IS NOT NULL
    """)
    return cursor.fetchall()

def obtener_id_fecha(cursor, fecha):
    date_obj = datetime.strptime(fecha, '%Y-%m-%d')
    fecha_formateada = date_obj.strftime('%d-%m-%Y')

    cursor.execute("""
        SELECT f.fecha_id FROM DIM_FECHA f
        WHERE f.dia = ?
    """, [fecha_formateada])

    resultado = cursor.fetchone()
    fecha_id = resultado[0] if resultado else None

    #Insertar si no existe!!! 
    #if fecha_id is not None:
        #etl_inserts.insert_fecha(cursor, fecha)
        #cursor.execute("INSERT INTO ... (fecha_id, ...) VALUES (?, ...)", [fecha_id, ...])

    return fecha_id

def obtener_id_estado(cursor, estado):
    cursor.execute("""
        SELECT e.estado_id FROM DIM_ESTADO e
        WHERE e.estado = ?
    """, [estado] )

    resultado = cursor.fetchone()
    estado_id = resultado[0] if resultado else None

    return estado_id

def obtener_id_patologia(cursor, patologia):
    cursor.execute("""
        SELECT e.patologia_id FROM DIM_PATOLOGIA e
        WHERE e.patologia = ?
    """, [patologia] )

    resultado = cursor.fetchone()
    patologia_id = resultado[0] if resultado else None

    return patologia_id