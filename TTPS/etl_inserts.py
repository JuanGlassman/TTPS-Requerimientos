import sqlite3
from datetime import datetime

def insert_fecha(cursor_target, fecha_str):
    date_obj = datetime.strptime(fecha_str, '%Y-%m-%d')

    dia_formateado = date_obj.strftime('%d-%m-%Y')
    mes_formateado = date_obj.strftime('%m-%Y')
    anio_formateado = date_obj.strftime('%Y')

    cursor_target.execute("""
        INSERT OR IGNORE INTO DIM_FECHA (
            anio, mes, dia
        ) VALUES (?, ?, ?)
    """, (
        anio_formateado,
        mes_formateado,
        dia_formateado
    ))

    return cursor_target.lastrowid

def insert_lugar(cursor_target, lugar):
    cursor_target.execute("""
        INSERT INTO DIM_LUGAR (ciudad, provincia, pais)
        VALUES (?, ?, ?)
    """, (
        lugar[1],
        lugar[2],
        lugar[3]
    ))

def insert_hecho_facturacion(cursor_target, facturacion, fecha_id):
    cursor_target.execute("""
        INSERT INTO HECHO_FACTURACION (monto, fecha_id, lugar_id)
        VALUES (?, ?, ?)
    """, (
        facturacion[0],
        fecha_id,
        facturacion[1]       
    ))