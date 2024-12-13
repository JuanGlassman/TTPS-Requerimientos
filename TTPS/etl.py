from enum import Enum
import sqlite3
from datetime import datetime

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
                    fecha_id INTEGER PRIMARY KEY,
                    anio TEXT,
                    mes TEXT,
                    dia TEXT
                )    
            """)

            # Crear dimensión lugar
            conn.execute("""
                CREATE TABLE IF NOT EXISTS DIM_LUGAR (
                    lugar_id INTEGER PRIMARY KEY,
                    ciudad TEXT,
                    localidad TEXT,
                    provincia TEXT
                )
            """)
            
            # Crear dimensión estado
            conn.execute("""
                CREATE TABLE IF NOT EXISTS DIM_ESTADO (
                    estado_id INTEGER PRIMARY KEY,
                    estado TEXT
                )
            """)

            # Crear dimensión estado
            conn.execute("""
                CREATE TABLE IF NOT EXISTS DIM_PATOLOGIA (
                    patologia_id INTEGER PRIMARY KEY,
                    patologia TEXT,
                    gen TEXT
                )
            """)
            
            # Crear tabla de hechos
            # conn.execute("""
            #     CREATE TABLE IF NOT EXISTS HECHO_DEMORA_ESTUDIO (
            #         id_hecho_demora INTEGER PRIMARY KEY,
            #         estudio_id INTEGER,
            #         fecha_id INTEGER,
            #         lugar_id INTEGER,
            #         estado_id INTEGER,
            #         duracion_estado_dias INTEGER,
            #         fecha_inicio_estado DATE,
            #         fecha_fin_estado DATE,
            #         FOREIGN KEY (fecha_id) REFERENCES DIM_FECHA (fecha_id),
            #         FOREIGN KEY (lugar_id) REFERENCES DIM_LUGAR (lugar_id),
            #         FOREIGN KEY (estado_id) REFERENCES DIM_ESTADO (estado_id)
            #     )
            # """)

            # Crear hecho estudios
            conn.execute("""
                CREATE TABLE IF NOT EXISTS HECHO_ESTUDIOS (
                    id_hecho_estudio INTEGER PRIMARY KEY,
                    lugar_id INTEGER,
                    fecha_id INTEGER,
                    estado_id INTEGER,
                    patologia_id INTEGER,
                    resultado TEXT
                )
            """)

    def obtener_fechas(self):
        cursor = self.origen_conn.cursor()
        cursor.execute("""
            SELECT DISTINCT fecha_inicio fecha FROM estudios_historialestudio
            UNION
            SELECT DISTINCT fecha_fin FROM estudios_historialestudio 
            WHERE fecha_fin IS NOT NULL
        """)
        return cursor.fetchall()

    def transform_tiempo(self):
        """Transformar y cargar dimensión de tiempo"""
        cursor_target = self.destino_conn.cursor()
        
        # Obtener fechas únicas
        fechas = self.obtener_fechas()
        
        # Insertar cada fecha con sus atributos calculados
        for fecha_id, (fecha,) in enumerate(fechas, 1):
            date_obj = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S.%f')
            mes_nombres = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
                        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
            
            cursor_target.execute("""
                INSERT INTO DIM_FECHA (
                    fecha_id, fecha, anio, mes, dia, nombre_mes
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                fecha_id,
                fecha,
                date_obj.year,
                date_obj.month,
                date_obj.day,
                mes_nombres[date_obj.month - 1]
            ))
        
        self.destino_conn.commit()

    def transform_lugar(self):
    #     """Transformar y cargar dimensión de lugar"""
    #     cursor_source = self.origen_conn.cursor()
    #     cursor_target = self.destino_conn.cursor()
        
    #     cursor_source.execute("SELECT * FROM lugares")
    #     lugares = cursor_source.fetchall()
        
    #     for lugar in lugares:
    #         cursor_target.execute("""
    #             INSERT INTO DIM_LUGAR (lugar_id, ciudad, localidad, pais, region)
    #             VALUES (?, ?, ?, ?, ?)
    #         """, lugar)
        
    #     self.destino_conn.commit()
        pass

    def transform_estado(self):
        """Transformar y cargar dimensión de estado"""
        cursor_source = self.origen_conn.cursor()
        cursor_target = self.destino_conn.cursor()           
        
        for estado in EstadoEstudio:
            cursor_target.execute("""
                INSERT INTO DIM_ESTADO (
                    estado_id, estado
                ) VALUES (?, ?)
            """, (
                estado.id,          # El valor del enum
                estado.nombre            # El nombre del estado                
            ))
        
        self.destino_conn.commit()

    def calculate_duration_days(self, fecha_inicio, fecha_fin):
        """Calcular duración en días entre dos fechas"""
        if not fecha_fin:
            return None
        
        inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        return (fin - inicio).days

    def transform_hechos_demora(self):
        """Transformar y cargar tabla de hechos"""
        cursor_source = self.origen_conn.cursor()
        cursor_target = self.destino_conn.cursor()
        
        # Obtener los datos necesarios de las tablas fuente
        cursor_source.execute("""
            SELECT 
                e.id_estudio as estudio_id,
                e.lugar_id,
                he.estado_id,
                he.fecha_inicio,
                he.fecha_fin
            FROM estudios e
            JOIN estudios_historialestudio he ON e.id = he.estudio_id
        """)
        estudios_data = cursor_source.fetchall()
        
        # Procesar cada registro
        for estudio in estudios_data:
            estudio_id, lugar_id, estado_id, fecha_inicio, fecha_fin = estudio
            
            # Obtener tiempo_id
            cursor_target.execute(
                "SELECT fecha_id FROM DIM_FECHA WHERE fecha = ?",
                (fecha_inicio,)
            )
            fecha_id = cursor_target.fetchone()[0]
            
            # Calcular duración
            duracion = self.calculate_duration_days(fecha_inicio, fecha_fin)            
            
            # Insertar en tabla de hechos
            cursor_target.execute("""
                INSERT INTO HECHO_DEMORA_ESTUDIO (
                    estudio_id, tiempo_id, lugar_id, estado_id,
                    duracion_estado_dias, fecha_inicio_estado, fecha_fin_estado
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                estudio_id, fecha_id, lugar_id, estado_id,
                duracion, fecha_inicio, fecha_fin
            ))
        
        self.target_conn.commit()

    def procesar_hecho_estudios(self):
        cursor_source = self.origen_conn.cursor()
        cursor_target = self.destino_conn.cursor()
        
        # Obtener los datos necesarios de las tablas fuente
        cursor_source.execute("""
            SELECT
                e.fecha,
                e.estado,
                e.patologia,
                e.resultado
            FROM estudios e
        """)
        estudios_data = cursor_source.fetchall()

        # Procesar cada registro
        for estudio in estudios_data:
            fecha, estado, patologia, resultado = estudio

            # Insertar en tabla de hechos
            cursor_target.execute("""
                INSERT INTO HECHO_DEMORA_ESTUDIO (
                    estudio_id, tiempo_id, lugar_id, estado_id,
                    duracion_estado_dias, fecha_inicio_estado, fecha_fin_estado
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                fecha_id, lugar_id, estado_id,
                duracion, fecha_inicio, fecha_fin
            ))
        
        self.target_conn.commit()



    def run_etl(self):
        """Ejecutar proceso ETL completo"""
        print("Iniciando proceso ETL...")
        
        print("Creando esquema estrella...")
        self.crear_modelo_estrella()
        
        print("Transformando y cargando dimensión tiempo...")
        self.transform_tiempo()
        
        # print("Transformando y cargando dimensión lugar...")
        # self.transform_lugar()
        
        print("Transformando y cargando dimensión estado...")
        self.transform_estado()
        
        print("Transformando y cargando tabla de hechos...")
        self.transform_hechos()
        
        print("Proceso ETL completado exitosamente!")
    
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