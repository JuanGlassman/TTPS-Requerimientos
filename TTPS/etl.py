from enum import Enum
import sqlite3
from datetime import datetime

import etl_inserts, etl_dimensiones

class EstadoEstudio(Enum):
    INICIADO = (1, 'Iniciado')
    PRESUPUESTADO = (2, 'Presupuestado')
    PAGADO = (3, 'Pagado')
    AUTORIZADO = (4, 'Autorizado')
    TURNO_CONFIRMADO = (5, 'Turno Confirmado')
    REALIZADA = (6, 'Realizada')
    CENTRALIZADA = (7, 'Centralizada')
    ENVIADA_EXTERIOR = (8, 'Enviada al Exterior')
    FINALIZADO = (9, 'Finalizado')
    CANCELADO = (10, 'Cancelado')

    @property
    def id(self):
        return self.value[0]

    @property
    def nombre(self):
        return self.value[1]

class ETL:
    def __init__(self, db_origen, db_destino):
    
        self.origen_conn = sqlite3.connect(db_origen)
        self.destino_conn = sqlite3.connect(db_destino)

        self.origen_conn.execute("PRAGMA foreign_keys = ON")
        self.destino_conn.execute("PRAGMA foreign_keys = ON")

    def crear_modelo_estrella(self):
        with self.destino_conn as conn:
            #Creo tabla DIM_FECHA
            conn.execute("""
                CREATE TABLE IF NOT EXISTS DIM_FECHA (
                    fecha_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    anio TEXT,
                    mes TEXT,
                    dia TEXT
                )    
            """)

            # Crear dimensión lugar
            conn.execute("""
                CREATE TABLE IF NOT EXISTS DIM_LUGAR (
                    lugar_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ciudad TEXT,
                    provincia TEXT,
                    pais TEXT
                )
            """)
            
            # Crear dimensión estado
            conn.execute("""
                CREATE TABLE IF NOT EXISTS DIM_ESTADO (
                    estado_id INTEGER PRIMARY KEY,
                    estado TEXT
                )
            """)

            # Crear dimensión patologia
            conn.execute("""
                CREATE TABLE IF NOT EXISTS DIM_PATOLOGIA (
                    patologia_id INTEGER PRIMARY KEY,
                    patologia TEXT,
                    gen TEXT
                )
            """)

            # Crear dimensión sospecha
            conn.execute("""
                CREATE TABLE IF NOT EXISTS DIM_SOSPECHA (
                    sospecha_id INTEGER PRIMARY KEY,
                    sospecha TEXT
                )
            """)
            
            # Crear tabla de hechos demora
            conn.execute("""
                CREATE TABLE IF NOT EXISTS HECHO_DEMORA_ESTUDIO (
                    id_hecho_demora INTEGER PRIMARY KEY AUTOINCREMENT,
                    lugar_id INTEGER,
                    patologia_id INTEGER,
                    tipo_sospecha INTEGER,
                    estado_id INTEGER,
                    duracion_dias INTEGER,
                    FOREIGN KEY (lugar_id) REFERENCES DIM_LUGAR (lugar_id),
                    FOREIGN KEY (estado_id) REFERENCES DIM_ESTADO (estado_id)
                )
            """)

            # Crear hecho estudios
            conn.execute("""
                CREATE TABLE IF NOT EXISTS HECHO_ESTUDIOS (
                    id_hecho_estudio INTEGER PRIMARY KEY AUTOINCREMENT,
                    lugar_id INTEGER,
                    fecha_id INTEGER,
                    estado_id INTEGER,
                    tipo_sospecha_id INTEGER,
                    patologia_id INTEGER,
                    resultado TEXT
                )
            """)

            # Crear hecho facturacion
            conn.execute("""
                CREATE TABLE IF NOT EXISTS HECHO_FACTURACION (
                    id_facturacion INTEGER PRIMARY KEY AUTOINCREMENT,
                    monto FLOAT,
                    fecha_id INTEGER,
                    lugar_id INTEGER
                )
            """)

    def transform_tiempo(self):
        """Transformar y cargar dimensión de tiempo"""
        cursor_target = self.destino_conn.cursor()
        
        # Obtener fechas únicas
        fechas = etl_dimensiones.obtener_fechas(self.origen_conn.cursor())

        # Insertar cada fecha con sus atributos calculados
        for i, fecha_tupla in enumerate(sorted(fechas)):  # Eliminar duplicados y ordenar
            fecha_str = fecha_tupla[0]
            
            etl_inserts.insert_fecha(cursor_target, fecha_str)
        
        self.destino_conn.commit()

    def transform_lugar(self):
        """Transformar y cargar dimensión de lugar"""
        cursor_source = self.origen_conn.cursor()
        cursor_target = self.destino_conn.cursor()
       
        cursor_source.execute("SELECT * FROM lugares")
        lugares = cursor_source.fetchall()

        for lugar in lugares:
            etl_inserts.insert_lugar(cursor_target, lugar)
    
        self.destino_conn.commit()
        pass
    
    def transform_estado(self):
        """Transformar y cargar dimensión de estado"""
        cursor_source = self.origen_conn.cursor()
        cursor_target = self.destino_conn.cursor()           
        
        for estado in EstadoEstudio:
            # Se inserta de una con el id porque son enums
            cursor_target.execute("""
                INSERT INTO DIM_ESTADO (
                    estado_id, estado
                ) VALUES (?, ?)
            """, (
                estado.id,          # El valor del enum
                estado.nombre            # El nombre del estado                
            ))
        
        self.destino_conn.commit()
        
    def transform_sospecha(self):
        """Transformar y cargar dimensión de sospecha"""
        #cursor_source = self.origen_conn.cursor()
        cursor_target = self.destino_conn.cursor()

        # Se inserta de una con el id porque son enums
        cursor_target.execute("""
            INSERT INTO DIM_SOSPECHA (
                sospecha_id, sospecha
            ) VALUES (?, ?)
        """, (
            0,
            "Puntual"
        ))
        
        cursor_target.execute("""
            INSERT INTO DIM_SOSPECHA (
                sospecha_id, sospecha
            ) VALUES (?, ?)
        """, (
            1,
            "Familiar"
        ))
        self.destino_conn.commit()

    def transform_patologia(self):
        cursor_source = self.origen_conn.cursor()
        cursor_target = self.destino_conn.cursor()

        cursor_source.execute("SELECT * FROM enfermedad")
        patologias = cursor_source.fetchall()

        for patologia in patologias:
            cursor_target.execute("""
                INSERT INTO DIM_PATOLOGIA (patologia_id, patologia, gen)
                VALUES (?, ?, ?)
            """, (
                patologia[0],
                patologia[1],
                patologia[2]
            ))
        
        self.destino_conn.commit()

    def calcular_duracion_dias(self, fecha_inicio, fecha_fin):
        """Calcular duración en días entre dos fechas"""
        if not fecha_fin:
            return None
        
        inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        return (fin - inicio).days

    def procesar_hechos_demora(self):
        """Transformar y cargar tabla de hechos"""
        cursor_source = self.origen_conn.cursor()
        cursor_target = self.destino_conn.cursor()
        
        # Obtener los datos necesarios de las tablas fuente
        cursor_source.execute("""
            SELECT 
                e.fecha,
                e.patologia_id,
                e.tipo_sospecha,
                l.lugar_id,
                he.estado,
                DATE(he.fecha_inicio),
                DATE(he.fecha_fin)
            FROM estudios e
            JOIN lugares l ON e.lugar_id = l.lugar_id
            JOIN estudios_historialestudio he ON e.id_estudio = he.estudio_id                     
        """)
        # GROUP BY l.lugar_id, he.estado

        estudios_data = cursor_source.fetchall()
        
        # Procesar cada registro
        for estudio in estudios_data:
            fecha_estudio, patologia_id, tipo_sospecha, lugar_id, estado, fecha_inicio, fecha_fin = estudio       

            estado_id = etl_dimensiones.obtener_id_estado(cursor_target, estado)

            # Calcular duración
            duracion = self.calcular_duracion_dias(fecha_inicio, fecha_fin)            
            
            # Insertar en tabla de hechos
            cursor_target.execute("""
                INSERT INTO HECHO_DEMORA_ESTUDIO (
                    patologia_id, tipo_sospecha, lugar_id, estado_id, duracion_dias
                ) VALUES (?, ?, ?, ?, ?)
            """, (
                patologia_id, tipo_sospecha, lugar_id, estado_id, duracion
            ))
        
        self.destino_conn.commit()

    def procesar_hecho_estudios(self):
        cursor_source = self.origen_conn.cursor()
        cursor_target = self.destino_conn.cursor()
        
        # Obtener los datos necesarios de las tablas fuente
        cursor_source.execute("""
            SELECT
                e.lugar_id,
                e.fecha,
                e.estado,
                e.tipo_sospecha,
                e.resultado,
                p.nombre
            FROM estudios e
            JOIN enfermedad p ON e.patologia_id = p.id_enfermedad
        """)
        estudios_data = cursor_source.fetchall()

        # Procesar cada registro
        for estudio in estudios_data:
            lugar_id, fecha, estado, tipo_sospecha, resultado, patologia = estudio

            fecha_id = etl_dimensiones.obtener_id_fecha(cursor_target, fecha)
            estado_id = etl_dimensiones.obtener_id_estado(cursor_target, estado)
            patologia_id = etl_dimensiones.obtener_id_patologia(cursor_target, patologia)

            # Insertar en tabla de hechos
            cursor_target.execute("""
                INSERT INTO HECHO_ESTUDIOS (
                    lugar_id, fecha_id,
                    estado_id, patologia_id, tipo_sospecha_id, resultado
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                lugar_id, fecha_id, estado_id,
                patologia_id, tipo_sospecha, resultado
            ))
        
        self.destino_conn.commit()

    def procesar_hecho_facturacion(self):
        cursor_source = self.origen_conn.cursor()
        cursor_target = self.destino_conn.cursor()
        
        cursor_target.execute("""
            SELECT 
                l.lugar_id,
                f.fecha_id,
                f.dia
            FROM DIM_LUGAR l
            JOIN DIM_FECHA f
            GROUP BY l.lugar_id, f.fecha_id                      
        """)
        
        for items in cursor_target.fetchall():
            lugar_id, fecha_id, fecha = items

            fecha_partes = fecha.split('-')
            fecha_formateada = f"{fecha_partes[0]}-{fecha_partes[1]}-{fecha_partes[2]}"

            # Obtener los datos necesarios de las tablas fuente
            cursor_source.execute("""
                SELECT 
                    COALESCE(SUM(p.total), 0) as total_suma,
                    ? as lugar_id,
                    ? as fecha
                FROM estudios e
                JOIN lugares l ON l.lugar_id = e.lugar_id 
                JOIN presupuestos p ON p.estudio_id = e.id_estudio
                WHERE e.lugar_id = ? AND e.fecha = ?
            """, (
                lugar_id,
                fecha_formateada,
                lugar_id,
                fecha_formateada
            ))

            facturacion = cursor_source.fetchone()
            fecha_id = etl_dimensiones.obtener_id_fecha(cursor_target, facturacion[2])
            etl_inserts.insert_hecho_facturacion(cursor_target, facturacion, fecha_id)
        
        self.destino_conn.commit()

    def run_etl(self):
        """Ejecutar proceso ETL completo"""
        print("Iniciando proceso ETL ")
        
        print("Creando esquema estrella 🛠")
        self.crear_modelo_estrella()
        
        print("Cargando dimensión tiempo ⏳")
        self.transform_tiempo()
        
        print("Cargando dimensión lugar ⏳")
        self.transform_lugar()
        
        print("Cargando dimensión estado ⏳")
        self.transform_estado()

        print("Cargando dimensión estado ⏳")
        self.transform_sospecha()

        print("Cargando dimensión patologia ⏳")
        self.transform_patologia()
        
        print("Cargando Hechos Estudios ⚡")
        self.procesar_hecho_estudios()

        print("Cargando Hechos Facturación ⚡")
        self.procesar_hecho_facturacion()

        print("Cargando Hechos Demora Estudios ⚡")
        self.procesar_hechos_demora()
        
        print("Proceso ETL completado exitosamente ✔")
    
    def close_connections(self):
        """Cerrar conexiones a las bases de datos"""
        self.origen_conn.close()
        self.destino_conn.close()


if __name__ == "__main__":
    source_db = "db.sqlite3"
    target_db = "estrella.sqlite3"
    
    etl = ETL(source_db, target_db)
    try:
        etl.run_etl()
    finally:
        etl.close_connections()