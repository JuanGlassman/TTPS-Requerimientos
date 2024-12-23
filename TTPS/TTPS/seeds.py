from estudios.models import Estudio, EstadoEstudio, Enfermedad, HistorialEstudio, Lugar
from estudios import views as estudios_estado
from inicio_sesion.models import Rol, Usuario
from pacientes.models import Paciente
from medicos.models import Medico
from lab_admin.models import Presupuesto
from lab_admin.models import LabAdmin
from transportista.models import Transportista, HojaDeRuta, Pedido
from transportista import views as transportista_view
from lab_admin.models import Centro, Turno
from datetime import date, time, timedelta, datetime
import random

## Este seed si bien tiene estudios realizados, centralizados, enviados al exterior
## y finalizados, no se crearon Sample Sets ni Hoja de Ruta con sus Pedidos.

def generar_fecha_aleatoria(fecha_inicio_str, fecha_fin_str):
    # Convertir las cadenas de fecha a objetos datetime
    fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d")
    
    # Calcular el rango de días entre las dos fechas
    delta = fecha_fin - fecha_inicio
    
    # Generar un número aleatorio de días dentro del rango
    dias_aleatorios = random.randint(0, delta.days)
    
    # Sumar los días aleatorios a la fecha de inicio
    fecha_aleatoria = fecha_inicio + timedelta(days=dias_aleatorios)
    
    return fecha_aleatoria

def generar_fecha_aleatoria_datetime(fecha_inicio_str, fecha_fin_str):
    # Convertir las cadenas de fecha a objetos datetime
    fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d")
    
    # Calcular el rango de días entre las dos fechas
    delta = fecha_fin - fecha_inicio
    
    # Generar un número aleatorio de días dentro del rango
    dias_aleatorios = random.randint(0, delta.days)
    
    # Sumar los días aleatorios a la fecha de inicio
    fecha_aleatoria = fecha_inicio + timedelta(days=dias_aleatorios)
    
    # Devolver el objeto datetime
    return fecha_aleatoria

def run_seeds():
    
    lugar1 = Lugar.objects.create(
        ciudad = "La Plata",
        provincia = "Buenos Aires",
        pais = "Argentina"
    )

    lugar2 = Lugar.objects.create(
        ciudad="Tandil",
        provincia="Buenos Aires",
        pais="Argentina"
    )

    lugar3 = Lugar.objects.create(
        ciudad="San Nicolás",
        provincia="Buenos Aires",
        pais="Argentina"
    )

    # Ciudades de Entre Ríos (3)
    lugar4 = Lugar.objects.create(
        ciudad="Colón",
        provincia="Entre Ríos",
        pais="Argentina"
    )

    lugar5 = Lugar.objects.create(
        ciudad="Concepción del Uruguay",
        provincia="Entre Ríos",
        pais="Argentina"
    )

    lugar6 = Lugar.objects.create(
        ciudad="Victoria",
        provincia="Entre Ríos",
        pais="Argentina"
    )

    # Ciudades de Córdoba (3)
    lugar7 = Lugar.objects.create(
        ciudad="Río Cuarto",
        provincia="Córdoba",
        pais="Argentina"
    )

    lugar8 = Lugar.objects.create(
        ciudad="Villa Carlos Paz",
        provincia="Córdoba",
        pais="Argentina"
    )

    lugar9 = Lugar.objects.create(
        ciudad="Jesús María",
        provincia="Córdoba",
        pais="Argentina"
    )

    # Ciudades de La Pampa (3)
    lugar10 = Lugar.objects.create(
        ciudad="General Acha",
        provincia="La Pampa",
        pais="Argentina"
    )

    lugar11 = Lugar.objects.create(
        ciudad="Guatraché",
        provincia="La Pampa",
        pais="Argentina"
    )

    lugar12 = Lugar.objects.create(
        ciudad="Toay",
        provincia="La Pampa",
        pais="Argentina"
    )

    # Ciudades de Brasil (2)
    lugar13 = Lugar.objects.create(
        ciudad="Florianópolis",
        provincia="Santa Catarina",
        pais="Brasil"
    )

    lugar14 = Lugar.objects.create(
        ciudad="Porto Alegre",
        provincia="Rio Grande do Sul",
        pais="Brasil"
    )

    # Ciudad de Uruguay (1)
    lugar15 = Lugar.objects.create(
        ciudad="Punta del Este",
        provincia="Maldonado",
        pais="Uruguay"
    )

    centro1 = Centro.objects.create(
        nombre = "Diagnosticos Cipriano",
        direccion = "Calle 9 777",
        longitud = -57.953714, 
        latitud = -34.915258,
        telefono = "221-123456",
        email = "diagnoslp@email.com",
        lugar = lugar1
    )

    centro2 = Centro.objects.create(
        nombre = "Laboratorio de Analisis",
        direccion = "Calle 71 301",
        longitud = -57.923714,
        latitud = -34.925258,
        telefono = "221-123456",
        email = "laboratorio_analisis@email.com",
        lugar = lugar1
    )

    centro3 = Centro.objects.create(
        nombre = "Extraccion de sangre",
        direccion = "Avenida 13 1486",
        longitud = -57.944586953543435,
        latitud = -34.92836420212585,
        telefono = "221-123456",
        email = "extracsang@email.com",
        lugar = lugar1
    )

    centro4 = Centro.objects.create(
        nombre = "Centro de Entre Rios",
        direccion = "Calle 123",
        longitud = -58.523714,
        latitud = -34.625258,
        telefono = "3442-123456",
        email = "centro_entrerios@email.com",
        lugar = lugar4
    )

    centro5 = Centro.objects.create(
        nombre = "Centro de Villa Carlos Paz",
        direccion = "Calle 404",
        longitud = -64.513714,
        latitud = -31.425258,
        telefono = "3541-123456",
        email = "centro_villacarlospaz@email.com",
        lugar = lugar8
    )

    centro6 = Centro.objects.create(
        nombre = "Centro de Toay",
        direccion = "Calle 808",
        longitud = -64.213714,
        latitud = -36.685258,
        telefono = "2954-123456",
        email = "centro_toay@email.com",
        lugar = lugar12
    )

    centro7 = Centro.objects.create(
        nombre = "Centro de Porto Alegre",
        direccion = "Calle 1010",
        longitud = -51.213714,
        latitud = -30.035258,
        telefono = "51-123456",
        email = "centro_portoalegre@email.com",
        lugar = lugar14
    )

    centro8 = Centro.objects.create(
        nombre = "Centro de Punta del Este",
        direccion = "Calle 1111",
        longitud = -54.953714,
        latitud = -34.915258,
        telefono = "42-123456",
        email = "centro_puntadeleste@email.com",
        lugar = lugar15
    )

    #Crear Roles
    rol_system_admin = Rol.objects.create(
        nombre = "system_admin"
    )

    rol_lab_admin = Rol.objects.create(
        nombre = "lab_admin"
    )
    
    rol_paciente = Rol.objects.create(
        nombre = "paciente"
    )

    rol_medico = Rol.objects.create(
        nombre = "medico"
    )

    rol_transportista = Rol.objects.create(
        nombre = "transportista"
    )

    #Patologias
    patologia1 = Enfermedad.objects.create(
        nombre= "ASMD",
        gen = "SMPD1"
    )

    patologia2 = Enfermedad.objects.create(
        nombre= "GAUCHER",
        gen = "GBA"
    )

    patologia3 = Enfermedad.objects.create(
        nombre= "MPSI",
        gen = "IDUA"
    )

    patologia4 = Enfermedad.objects.create(
        nombre= "FABRY",
        gen = "GLA"
    )

    patologia5 = Enfermedad.objects.create(
        nombre= "POMPE",
        gen = "GAA"
    )

    #Crear usuario Administrador de sistema
    superuser = Usuario.objects.create(
        username="admin",
        email="admin@email.com",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        dni = 1,
        is_superuser = 1,
        first_name = "Juan",
        last_name = "Admin",
        fecha_nacimiento = "1985-05-05",
        genero = "M",
        rol_id = rol_system_admin.id_rol
    )

    #Crear usuario Administrador de laboratorio
    usuario_admin_lab = Usuario.objects.create(
        username="fidel_alvarez",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        email="fidel@email.com",
        dni = 2,
        first_name = "Fidel",
        last_name = "Alvarez",
        fecha_nacimiento = "1999-11-05",
        genero = "M",
        rol_id = rol_lab_admin.id_rol
    )

    admin_lab = LabAdmin.objects.create(
        usuario=usuario_admin_lab
    )


    #Crear usuario Medico
    usuarioMedico = Usuario.objects.create(
        username="medico_osvaldo",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        email="medico_osvaldo@email.com",
        dni = 3,
        first_name = "Osvaldo",
        last_name = "Dario",
        fecha_nacimiento = "1985-05-05",
        genero = "M",
        rol_id = rol_medico.id_rol
    )

    medico = Medico.objects.create(
        usuario_id = usuarioMedico.id_usuario,
        especialidad = "Cardiologo",
        matricula = "113/1234"
    )

    usuarioTransportista = Usuario.objects.create(
        username="lucas_garcia",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        email="lukitas@email.com",
        dni = 13,
        first_name = "Lucas",
        last_name = "Garcia",
        fecha_nacimiento = "1999-11-05",
        genero = "M",
        rol_id = rol_transportista.id_rol
    )

    transportista = Transportista.objects.create(
        usuario_id = usuarioTransportista.id_usuario
    )

    #Crear usuarios Pacientes
    usuario1 = Usuario.objects.create(
        username="rodri_lira",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        email="rodri@email.com",
        dni = 4,
        first_name = "Rodrigo",
        last_name = "Lira",
        fecha_nacimiento = "2002-05-05",
        genero = "M",
        rol_id = rol_paciente.id_rol
    )

    usuario2 = Usuario.objects.create(
        username = "sofi_vera",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        email="sofi@email.com",
        dni = 5,
        first_name = "Sofia",
        last_name = "Vera",
        fecha_nacimiento = "2002-05-05",
        genero = "F",
        rol_id = rol_paciente.id_rol
    )

    usuario3 = Usuario.objects.create(        
        username = "valeria_reyes",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        email="valeria@email.com",
        dni = 6,
        first_name = "Valeria",
        last_name = "Reyes",
        fecha_nacimiento = "1998-05-05",
        genero = "F",
        rol_id = rol_paciente.id_rol
    )

    usuario4 = Usuario.objects.create(        
        username="ruben_centurion",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        email="ruben@email.com",
        dni = 7,
        first_name = "Ruben",
        last_name = "Centurión",
        fecha_nacimiento = "1995-05-05",
        genero = "M",
        rol_id = rol_paciente.id_rol
    )

    usuario5 = Usuario.objects.create(
        username="juan_lira",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        email="valentin@email.com",
        dni = 8,
        first_name = "Valentin",
        last_name = "Lira",
        fecha_nacimiento = "1995-05-05",
        genero = "M",
        rol_id = rol_paciente.id_rol
    )

    usuario6 = Usuario.objects.create(
        username="pedro_lira",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        email="valerio@email.com",
        dni = 9,
        first_name = "Valerio",
        last_name = "Lira",
        fecha_nacimiento = "1995-05-05",
        genero = "M",
        rol_id = rol_paciente.id_rol
    )

    usuario7 = Usuario.objects.create(
        username="jorge_liriarte",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        email="valentina@email.com",
        dni = 10,
        first_name = "Valentina",
        last_name = "Liriarte",
        fecha_nacimiento = "1995-05-05",
        genero = "F",
        rol_id = rol_paciente.id_rol
    )

    usuario8 = Usuario.objects.create(
        username="rodolfo_humme",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        email="rodolfo@email.com",
        dni = 11,
        first_name = "Rodolfo",
        last_name = "Humme",
        fecha_nacimiento = "1995-05-05",
        genero = "M",
        rol_id = rol_paciente.id_rol
    )

    usuario9 = Usuario.objects.create(
        username="joaquien_garcia",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=", # el numero 1 hasheado
        email="fidel@email.com",
        dni = 12,
        first_name = "Joaquin",
        last_name = "Garcia",
        fecha_nacimiento = "1999-11-05",
        genero = "M",
        rol_id = rol_paciente.id_rol
    )

    paciente1 = Paciente.objects.create(
        usuario_id = usuario1.id_usuario,
        antecedentes = "No posee",
        historial_medico = "Nunca vino"
    )
    paciente2 = Paciente.objects.create(
        usuario_id = usuario2.id_usuario,
        antecedentes = "Alergia al paracetamol",
        historial_medico = "Operacion de apéndice"
    )
    paciente3 = Paciente.objects.create(
        usuario_id = usuario3.id_usuario,
        antecedentes = "Todas las vacunas contra el covid",
        historial_medico = "Fisura abdominal"
    )
    paciente4 = Paciente.objects.create(
        usuario_id = usuario4.id_usuario,
        antecedentes = "Antitetánica, vacuna contra la gripe",
        historial_medico = "Nunca vino"
    )
    paciente5 = Paciente.objects.create(
        usuario_id = usuario5.id_usuario,
        antecedentes = "Higado graso",
        historial_medico = "Operacion de peritonitis"
    )
    paciente6 = Paciente.objects.create(
        usuario_id = usuario6.id_usuario,
        antecedentes = "Clamidia",
        historial_medico = "Nunca vino"
    )
    paciente7 = Paciente.objects.create(
        usuario_id = usuario7.id_usuario,
        antecedentes = "HPV",
        historial_medico = "Operacion de berrugas de HPV"
    )
    paciente8 = Paciente.objects.create(
        usuario_id = usuario8.id_usuario,
        antecedentes = "No posee",
        historial_medico = "Nunca vino"
    )
    paciente9 = Paciente.objects.create(
        usuario_id = usuario9.id_usuario,
        antecedentes = "Convulsiones",
        historial_medico = "Operación de corneas"
    )
    # Crear 10 pacientes adicionales
    usuario10 = Usuario.objects.create(
        username="matias_fernandez",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=",  # el número 1 hasheado
        email="matias@email.com",
        dni=14,
        first_name="Matías",
        last_name="Fernández",
        fecha_nacimiento="1990-03-12",
        genero="M",
        rol_id=rol_paciente.id_rol
    )
    paciente10 = Paciente.objects.create(
        usuario_id=usuario10.id_usuario,
        antecedentes="Hipertensión arterial",
        historial_medico="Chequeos regulares"
    )

    usuario11 = Usuario.objects.create(
        username="lucia_gomez",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=",  # el número 1 hasheado
        email="lucia@email.com",
        dni=15,
        first_name="Lucía",
        last_name="Gómez",
        fecha_nacimiento="1987-07-25",
        genero="F",
        rol_id=rol_paciente.id_rol
    )
    paciente11 = Paciente.objects.create(
        usuario_id=usuario11.id_usuario,
        antecedentes="Asma leve",
        historial_medico="Tratamiento con inhaladores"
    )

    usuario12 = Usuario.objects.create(
        username="andrea_lopez",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=",  # el número 1 hasheado
        email="andrea@email.com",
        dni=16,
        first_name="Andrea",
        last_name="López",
        fecha_nacimiento="1995-01-08",
        genero="F",
        rol_id=rol_paciente.id_rol
    )
    paciente12 = Paciente.objects.create(
        usuario_id=usuario12.id_usuario,
        antecedentes="Alergia al polen",
        historial_medico="Sin intervenciones mayores"
    )

    usuario13 = Usuario.objects.create(
        username="juan_perez",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=",  # el número 1 hasheado
        email="juan@email.com",
        dni=17,
        first_name="Juan",
        last_name="Pérez",
        fecha_nacimiento="1980-09-15",
        genero="M",
        rol_id=rol_paciente.id_rol
    )
    paciente13 = Paciente.objects.create(
        usuario_id=usuario13.id_usuario,
        antecedentes="Colesterol alto",
        historial_medico="Controlado con medicación"
    )

    usuario14 = Usuario.objects.create(
        username="mariana_rios",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=",  # el número 1 hasheado
        email="mariana@email.com",
        dni=18,
        first_name="Mariana",
        last_name="Ríos",
        fecha_nacimiento="1983-06-18",
        genero="F",
        rol_id=rol_paciente.id_rol
    )
    paciente14 = Paciente.objects.create(
        usuario_id=usuario14.id_usuario,
        antecedentes="Diabetes tipo 2",
        historial_medico="En tratamiento con insulina"
    )
    
    usuario15 = Usuario.objects.create(
        username="carlos_martin",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=",  # el número 1 hasheado
        email="carlos@email.com",
        dni=19,
        first_name="Carlos",
        last_name="Martín",
        fecha_nacimiento="1986-11-05",
        genero="M",
        rol_id=rol_paciente.id_rol
    )
    paciente15 = Paciente.objects.create(
        usuario_id=usuario15.id_usuario,
        antecedentes="No posee antecedentes relevantes",
        historial_medico="En perfectas condiciones"
    )
    
    usuario16 = Usuario.objects.create(
        username="paula_fernandez",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=",  # el número 1 hasheado
        email="paula@email.com",
        dni=20,
        first_name="Paula",
        last_name="Fernández",
        fecha_nacimiento="1992-02-15",
        genero="F",
        rol_id=rol_paciente.id_rol
    )
    paciente16 = Paciente.objects.create(
        usuario_id=usuario16.id_usuario,
        antecedentes="Migrañas frecuentes",
        historial_medico="Tratamiento con analgésicos"
    )
    
    usuario17 = Usuario.objects.create(
        username="martin_garcia",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=",  # el número 1 hasheado
        email="martin@email.com",
        dni=21,
        first_name="Martín",
        last_name="García",
        fecha_nacimiento="1997-08-23",
        genero="M",
        rol_id=rol_paciente.id_rol
    )
    paciente17 = Paciente.objects.create(
        usuario_id=usuario17.id_usuario,
        antecedentes="Artritis en las rodillas",
        historial_medico="Fisioterapia en curso"
    )
    
    usuario18 = Usuario.objects.create(
        username="juanita_luna",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=",  # el número 1 hasheado
        email="juanita@email.com",
        dni=22,
        first_name="Juanita",
        last_name="Luna",
        fecha_nacimiento="1993-09-30",
        genero="F",
        rol_id=rol_paciente.id_rol
    )
    paciente18 = Paciente.objects.create(
        usuario_id=usuario18.id_usuario,
        antecedentes="Problemas gastrointestinales",
        historial_medico="En tratamiento con probióticos"
    )
    
    usuario19 = Usuario.objects.create(
        username="gustavo_mora",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=",  # el número 1 hasheado
        email="gustavo@email.com",
        dni=23,
        first_name="Gustavo",
        last_name="Mora",
        fecha_nacimiento="1989-10-10",
        genero="M",
        rol_id=rol_paciente.id_rol
    )
    paciente19 = Paciente.objects.create(
        usuario_id=usuario19.id_usuario,
        antecedentes="Hipotiroidismo",
        historial_medico="Tratamiento con levotiroxina"
    )
    
    usuario20 = Usuario.objects.create(
        username="marta_vega",
        password="pbkdf2_sha256$870000$yigOCtPVQV2hyOAfg4Jvbu$vJg5/v0OGKH7JgXF0b9prmNou9m4dhUZ02qAGH2Yjkg=",  # el número 1 hasheado
        email="marta@email.com",
        dni=24,
        first_name="Marta",
        last_name="Vega",
        fecha_nacimiento="1984-12-20",
        genero="F",
        rol_id=rol_paciente.id_rol
    )
    paciente20 = Paciente.objects.create(
        usuario_id=usuario20.id_usuario,
        antecedentes="Fibromialgia",
        historial_medico="Bajo tratamiento sintomático"
    )    

    ## ESTUDIOS

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio1 = Estudio.objects.create( 
        id_interno="1234_LIR_ROD",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia1.id_enfermedad,
        paciente_id = paciente1.id_paciente,
        medico_id = medico.id_medico, 
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar1.lugar_id
    )
    
    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio1.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto1 = Presupuesto.objects.create(
        estudio_id = estudio1.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio1.estado = EstadoEstudio.PRESUPUESTADO
    estudio1.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio1.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio1.estado = EstadoEstudio.PAGADO
    estudio1.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio1.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio1.estado = EstadoEstudio.AUTORIZADO
    estudio1.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio1.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio1 = Turno.objects.create(
        usuario_id = usuario1.id_usuario,
        estudio_id = estudio1.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio1.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio1.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio1.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio2 = Estudio.objects.create( 
        id_interno="1235_LIR_ROD",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia2.id_enfermedad,
        paciente_id = paciente1.id_paciente,
        medico_id = medico.id_medico, 
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar1.lugar_id
    )
    
    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio2.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto2 = Presupuesto.objects.create(
        estudio_id = estudio2.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio2.estado = EstadoEstudio.PRESUPUESTADO
    estudio2.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio2.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio3 = Estudio.objects.create( 
        id_interno="1236_LIR_ROD",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia1.id_enfermedad,
        paciente_id = paciente1.id_paciente,
        medico_id = medico.id_medico, 
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar2.lugar_id
    )
    
    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio3.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto3 = Presupuesto.objects.create(
        estudio_id = estudio3.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio3.estado = EstadoEstudio.PRESUPUESTADO
    estudio3.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio3.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio3.estado = EstadoEstudio.PAGADO
    estudio3.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio3.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio3.estado = EstadoEstudio.AUTORIZADO
    estudio3.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio3.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio3 = Turno.objects.create(
        usuario_id = usuario1.id_usuario,
        estudio_id = estudio3.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio3.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio3.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio3.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio4 = Estudio.objects.create(
        id_interno="1237_VER_SOF",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia1.id_enfermedad,
        paciente_id = paciente2.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar2.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio4.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto4 = Presupuesto.objects.create(
        estudio_id = estudio4.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio4.estado = EstadoEstudio.PRESUPUESTADO
    estudio4.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio4.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio5 = Estudio.objects.create(
        id_interno="1238_VER_SOF",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia1.id_enfermedad,
        paciente_id = paciente2.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar3.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio5.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto5 = Presupuesto.objects.create(
        estudio_id = estudio5.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio5.estado = EstadoEstudio.PRESUPUESTADO
    estudio5.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio5.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio5.estado = EstadoEstudio.PAGADO
    estudio5.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio5.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio5.estado = EstadoEstudio.AUTORIZADO
    estudio5.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio5.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio5 = Turno.objects.create(
        usuario_id = usuario2.id_usuario,
        estudio_id = estudio5.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro2.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio5.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio5.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio5.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio5.estado = EstadoEstudio.REALIZADA
    estudio5.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio5.id_estudio,
        estado = EstadoEstudio.REALIZADA,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )
    transportista_view.agregar_estudio_a_pedido(estudio5.id_estudio)

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio5.estado = EstadoEstudio.CENTRALIZADA
    estudio5.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio5.id_estudio,
        estado = EstadoEstudio.CENTRALIZADA,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )
    estudios_estado.asignar_a_sample_set(estudio5)

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=15)
    estudio5.estado = EstadoEstudio.ENVIADA_EXTERIOR
    estudio5.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio5.id_estudio,
        estado = EstadoEstudio.ENVIADA_EXTERIOR,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio5.estado = EstadoEstudio.FINALIZADO
    estudio5.resultado = "positivo"
    estudio5.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio5.id_estudio,
        estado = EstadoEstudio.FINALIZADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio6 = Estudio.objects.create(
        id_interno="1239_VER_SOF",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia4.id_enfermedad,
        paciente_id = paciente2.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar4.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio6.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto6 = Presupuesto.objects.create(
        estudio_id = estudio6.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio6.estado = EstadoEstudio.CANCELADO
    estudio6.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio6.id_estudio,
        estado = EstadoEstudio.CANCELADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio7 = Estudio.objects.create(
        id_interno="1240_REY_VAL",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia4.id_enfermedad,
        paciente_id = paciente3.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar1.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio7.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto7 = Presupuesto.objects.create(
        estudio_id = estudio7.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio7.estado = EstadoEstudio.PRESUPUESTADO
    estudio7.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio7.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio7.estado = EstadoEstudio.PAGADO
    estudio7.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio7.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio7.estado = EstadoEstudio.AUTORIZADO
    estudio7.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio7.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio7 = Turno.objects.create(
        usuario_id = usuario3.id_usuario,
        estudio_id = estudio7.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio7.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio7.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio7.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio7.estado = EstadoEstudio.REALIZADA
    estudio7.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio7.id_estudio,
        estado = EstadoEstudio.REALIZADA,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )
    transportista_view.agregar_estudio_a_pedido(estudio7.id_estudio)

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio7.estado = EstadoEstudio.CENTRALIZADA
    estudio7.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio7.id_estudio,
        estado = EstadoEstudio.CENTRALIZADA,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )
    estudios_estado.asignar_a_sample_set(estudio7)

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=12)
    estudio7.estado = EstadoEstudio.ENVIADA_EXTERIOR
    estudio7.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio7.id_estudio,
        estado = EstadoEstudio.ENVIADA_EXTERIOR,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio7.estado = EstadoEstudio.FINALIZADO
    estudio7.resultado = "negativo"
    estudio7.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio7.id_estudio,
        estado = EstadoEstudio.FINALIZADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio8 = Estudio.objects.create(
        id_interno="1241_CEN_RUB",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia4.id_enfermedad,
        paciente_id = paciente4.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar4.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio8.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto8 = Presupuesto.objects.create(
        estudio_id = estudio8.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio8.estado = EstadoEstudio.PRESUPUESTADO
    estudio8.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio8.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio9 = Estudio.objects.create(
        id_interno="1242_CEN_RUB",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia3.id_enfermedad,
        paciente_id = paciente4.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar5.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio9.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto9 = Presupuesto.objects.create(
        estudio_id = estudio9.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio9.estado = EstadoEstudio.PRESUPUESTADO
    estudio9.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio9.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio9.estado = EstadoEstudio.PAGADO
    estudio9.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio9.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio10 = Estudio.objects.create(
        id_interno="1243_CEN_RUB",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia2.id_enfermedad,
        paciente_id = paciente4.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar5.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio10.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto10 = Presupuesto.objects.create(
        estudio_id = estudio10.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio10.estado = EstadoEstudio.PRESUPUESTADO
    estudio10.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio10.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio10.estado = EstadoEstudio.PAGADO
    estudio10.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio10.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio10.estado = EstadoEstudio.AUTORIZADO
    estudio10.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio10.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio11 = Estudio.objects.create(
        id_interno="1244_CEN_RUB",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia5.id_enfermedad,
        paciente_id = paciente4.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar6.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio11.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto11 = Presupuesto.objects.create(
        estudio_id = estudio11.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio11.estado = EstadoEstudio.PRESUPUESTADO
    estudio11.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio11.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio11.estado = EstadoEstudio.PAGADO
    estudio11.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio11.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio11.estado = EstadoEstudio.AUTORIZADO
    estudio11.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio11.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio11 = Turno.objects.create(
        usuario_id = usuario4.id_usuario,
        estudio_id = estudio11.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio11.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio11.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio11.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio12 = Estudio.objects.create(
        id_interno="1245_LIR_JUA",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia2.id_enfermedad,
        paciente_id = paciente5.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar6.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio12.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto12 = Presupuesto.objects.create(
        estudio_id = estudio12.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio12.estado = EstadoEstudio.PRESUPUESTADO
    estudio12.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio12.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio12.estado = EstadoEstudio.PAGADO
    estudio12.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio12.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio13 = Estudio.objects.create(
        id_interno="1246_LIR_JUA",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia5.id_enfermedad,
        paciente_id = paciente5.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar7.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio13.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto13 = Presupuesto.objects.create(
        estudio_id = estudio13.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio13.estado = EstadoEstudio.PRESUPUESTADO
    estudio13.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio13.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio13.estado = EstadoEstudio.CANCELADO
    estudio13.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio13.id_estudio,
        estado = EstadoEstudio.CANCELADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio14 = Estudio.objects.create(
        id_interno="1247_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia3.id_enfermedad,
        paciente_id = paciente6.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar14.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio14.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto14 = Presupuesto.objects.create(
        estudio_id = estudio14.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio14.estado = EstadoEstudio.PRESUPUESTADO
    estudio14.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio14.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio15 = Estudio.objects.create(
        id_interno="1248_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia5.id_enfermedad,
        paciente_id = paciente6.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar14.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio15.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto15 = Presupuesto.objects.create(
        estudio_id = estudio15.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio15.estado = EstadoEstudio.PRESUPUESTADO
    estudio15.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio15.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio15.estado = EstadoEstudio.PAGADO
    estudio15.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio15.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio15.estado = EstadoEstudio.AUTORIZADO
    estudio15.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio15.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio15 = Turno.objects.create(
        usuario_id = usuario5.id_usuario,
        estudio_id = estudio15.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio15.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio15.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio15.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio15.estado = EstadoEstudio.REALIZADA
    estudio15.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio15.id_estudio,
        estado = EstadoEstudio.REALIZADA,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )
    transportista_view.agregar_estudio_a_pedido(estudio15.id_estudio)

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio15.estado = EstadoEstudio.CENTRALIZADA
    estudio15.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio15.id_estudio,
        estado = EstadoEstudio.CENTRALIZADA,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )
    estudios_estado.asignar_a_sample_set(estudio15)

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=15)
    estudio15.estado = EstadoEstudio.ENVIADA_EXTERIOR
    estudio15.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio15.id_estudio,
        estado = EstadoEstudio.ENVIADA_EXTERIOR,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio15.estado = EstadoEstudio.FINALIZADO
    estudio15.resultado = "positivo"
    estudio15.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio15.id_estudio,
        estado = EstadoEstudio.FINALIZADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio16 = Estudio.objects.create(
        id_interno="1249_LIR_JOR",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia2.id_enfermedad,
        paciente_id = paciente7.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar14.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio16.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto16 = Presupuesto.objects.create(
        estudio_id = estudio16.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio16.estado = EstadoEstudio.PRESUPUESTADO
    estudio16.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio16.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio16.estado = EstadoEstudio.CANCELADO
    estudio16.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio16.id_estudio,
        estado = EstadoEstudio.CANCELADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio17 = Estudio.objects.create(
        id_interno="1250_HUM_ROD",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia4.id_enfermedad,
        paciente_id = paciente8.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar9.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio17.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto17 = Presupuesto.objects.create(
        estudio_id = estudio17.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio17.estado = EstadoEstudio.PRESUPUESTADO
    estudio17.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio17.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio17.estado = EstadoEstudio.CANCELADO
    estudio17.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio17.id_estudio,
        estado = EstadoEstudio.CANCELADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio18 = Estudio.objects.create(
        id_interno="1251_HUM_ROD",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia3.id_enfermedad,
        paciente_id = paciente8.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar10.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)

    HistorialEstudio.objects.create(
        estudio_id = estudio18.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto18 = Presupuesto.objects.create(
        estudio_id = estudio18.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio18.estado = EstadoEstudio.PRESUPUESTADO
    estudio18.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio18.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio18.estado = EstadoEstudio.PAGADO
    estudio18.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio18.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio18.estado = EstadoEstudio.AUTORIZADO
    estudio18.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio18.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio18 = Turno.objects.create(
        usuario_id = usuario6.id_usuario,
        estudio_id = estudio18.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro2.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio18.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio18.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio18.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=num_random)
    estudio18.estado = EstadoEstudio.REALIZADA
    estudio18.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio18.id_estudio,
        estado = EstadoEstudio.REALIZADA,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )
    transportista_view.agregar_estudio_a_pedido(estudio18.id_estudio)

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(days=num_random)
    estudio18.estado = EstadoEstudio.CENTRALIZADA
    estudio18.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio18.id_estudio,
        estado = EstadoEstudio.CENTRALIZADA,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )
    estudios_estado.asignar_a_sample_set(estudio18)

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(days=20)
    estudio18.estado = EstadoEstudio.ENVIADA_EXTERIOR
    estudio18.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio18.id_estudio,
        estado = EstadoEstudio.ENVIADA_EXTERIOR,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio18.estado = EstadoEstudio.FINALIZADO
    estudio18.resultado = "positivo"
    estudio18.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio18.id_estudio,
        estado = EstadoEstudio.FINALIZADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio19 = Estudio.objects.create(
        id_interno="1252_GAR_JOA",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia2.id_enfermedad,
        paciente_id = paciente9.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar9.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(days=num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio19.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto19 = Presupuesto.objects.create(
        estudio_id = estudio19.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio19.estado = EstadoEstudio.PRESUPUESTADO
    estudio19.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio19.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio19.estado = EstadoEstudio.PAGADO
    estudio19.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio19.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio19.estado = EstadoEstudio.AUTORIZADO
    estudio19.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio19.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio19 = Turno.objects.create(
        usuario_id = usuario7.id_usuario,
        estudio_id = estudio19.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro2.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio19.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio19.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio19.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio19.estado = EstadoEstudio.REALIZADA
    estudio19.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio19.id_estudio,
        estado = EstadoEstudio.REALIZADA,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )
    transportista_view.agregar_estudio_a_pedido(estudio19.id_estudio)

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio19.estado = EstadoEstudio.CENTRALIZADA
    estudio19.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio19.id_estudio,
        estado = EstadoEstudio.CENTRALIZADA,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )
    estudios_estado.asignar_a_sample_set(estudio19)

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio19.estado = EstadoEstudio.ENVIADA_EXTERIOR
    estudio19.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio19.id_estudio,
        estado = EstadoEstudio.ENVIADA_EXTERIOR,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio19.estado = EstadoEstudio.FINALIZADO
    estudio19.resultado = "negativo"
    estudio19.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio19.id_estudio,
        estado = EstadoEstudio.FINALIZADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio20 = Estudio.objects.create(
        id_interno="1253_GAR_JOA",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia3.id_enfermedad,
        paciente_id = paciente10.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar11.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio20.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto20 = Presupuesto.objects.create(
        estudio_id = estudio20.id_estudio,
        costo_exoma = 500,
        costo_genes_extra = 200,
        total = 700.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio20.estado = EstadoEstudio.PRESUPUESTADO
    estudio20.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio20.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio20.estado = EstadoEstudio.PAGADO
    estudio20.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio20.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio20.estado = EstadoEstudio.AUTORIZADO
    estudio20.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio20.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio21 = Estudio.objects.create(
        id_interno="1254_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia5.id_enfermedad,
        paciente_id = paciente6.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar7.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio21.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto21 = Presupuesto.objects.create(
        estudio_id = estudio21.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio21.estado = EstadoEstudio.PRESUPUESTADO
    estudio21.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio21.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio21.estado = EstadoEstudio.PAGADO
    estudio21.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio21.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio21.estado = EstadoEstudio.AUTORIZADO
    estudio21.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio21.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio21 = Turno.objects.create(
        usuario_id = usuario6.id_usuario,
        estudio_id = estudio21.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro2.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio21.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio21.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio21.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio21.estado = EstadoEstudio.REALIZADA
    estudio21.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio21.id_estudio,
        estado = EstadoEstudio.REALIZADA,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )
    transportista_view.agregar_estudio_a_pedido(estudio21.id_estudio)

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio21.estado = EstadoEstudio.CENTRALIZADA
    estudio21.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio21.id_estudio,
        estado = EstadoEstudio.CENTRALIZADA,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )
    estudios_estado.asignar_a_sample_set(estudio21)

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio21.estado = EstadoEstudio.ENVIADA_EXTERIOR
    estudio21.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio21.id_estudio,
        estado = EstadoEstudio.ENVIADA_EXTERIOR,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio22 = Estudio.objects.create(
        id_interno="1255_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia2.id_enfermedad,
        paciente_id = paciente5.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar8.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio22.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto22 = Presupuesto.objects.create(
        estudio_id = estudio22.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio22.estado = EstadoEstudio.PRESUPUESTADO
    estudio22.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio22.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio22.estado = EstadoEstudio.PAGADO
    estudio22.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio22.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio22.estado = EstadoEstudio.AUTORIZADO
    estudio22.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio22.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio22 = Turno.objects.create(
        usuario_id = usuario5.id_usuario,
        estudio_id = estudio22.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)

    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio22.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio22.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio22.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio23 = Estudio.objects.create(
        id_interno="1256_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia5.id_enfermedad,
        paciente_id = paciente5.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar7.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio23.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio23.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio24 = Estudio.objects.create(
        id_interno="1257_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia3.id_enfermedad,
        paciente_id = paciente6.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar14.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio24.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )
    
    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio24.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio25 = Estudio.objects.create(
        id_interno="1258_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia5.id_enfermedad,
        paciente_id = paciente8.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar14.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio25.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio25.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio26 = Estudio.objects.create(
        id_interno="1259_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia2.id_enfermedad,
        paciente_id = paciente9.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar9.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio26.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio26.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio26.estado = EstadoEstudio.PRESUPUESTADO
    estudio26.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio26.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")  
    #Crear Estudios y Presupuestos
    estudio27 = Estudio.objects.create(
        id_interno="1260_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia4.id_enfermedad,
        paciente_id = paciente10.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar9.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio27.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio27.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio27.estado = EstadoEstudio.PRESUPUESTADO
    estudio27.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio27.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio28 = Estudio.objects.create(
        id_interno="1261_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia5.id_enfermedad,
        paciente_id = paciente9.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar2.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio28.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio28.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio28.estado = EstadoEstudio.PRESUPUESTADO
    estudio28.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio28.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio29 = Estudio.objects.create(
        id_interno="1262_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia2.id_enfermedad,
        paciente_id = paciente10.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar1.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio29.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio29.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio29.estado = EstadoEstudio.PRESUPUESTADO
    estudio29.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio29.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio29.estado = EstadoEstudio.CANCELADO
    estudio29.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio29.id_estudio,
        estado = EstadoEstudio.CANCELADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio30 = Estudio.objects.create(
        id_interno="1263_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia3.id_enfermedad,
        paciente_id = paciente7.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar1.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio30.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio30.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio30.estado = EstadoEstudio.PRESUPUESTADO
    estudio30.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio30.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio30.estado = EstadoEstudio.PAGADO
    estudio30.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio30.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio30.estado = EstadoEstudio.AUTORIZADO
    estudio30.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio30.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio30 = Turno.objects.create(
        usuario_id = usuario7.id_usuario,
        estudio_id = estudio30.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro2.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio30.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio30.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio30.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio30.estado = EstadoEstudio.REALIZADA
    estudio30.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio30.id_estudio,
        estado = EstadoEstudio.REALIZADA,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )
    transportista_view.agregar_estudio_a_pedido(estudio30.id_estudio)

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio31 = Estudio.objects.create(
        id_interno="1264_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia4.id_enfermedad,
        paciente_id = paciente8.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar2.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio31.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio31.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio31.estado = EstadoEstudio.PRESUPUESTADO
    estudio31.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio31.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio31.estado = EstadoEstudio.PAGADO
    estudio31.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio31.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio32 = Estudio.objects.create(
        id_interno="1265_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia5.id_enfermedad,
        paciente_id = paciente7.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar3.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio32.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio32.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio32.estado = EstadoEstudio.PRESUPUESTADO
    estudio32.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio32.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio32.estado = EstadoEstudio.PAGADO
    estudio32.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio32.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio32.estado = EstadoEstudio.AUTORIZADO
    estudio32.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio32.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio32 = Turno.objects.create(
        usuario_id = usuario6.id_usuario,
        estudio_id = estudio32.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro2.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio32.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio32.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio32.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio33 = Estudio.objects.create(
        id_interno="1266_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia2.id_enfermedad,
        paciente_id = paciente6.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 1,
        lugar_id = lugar3.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio33.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio33.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio33.estado = EstadoEstudio.PRESUPUESTADO
    estudio33.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio33.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio33.estado = EstadoEstudio.PAGADO
    estudio33.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio33.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio33.estado = EstadoEstudio.AUTORIZADO
    estudio33.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio33.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio33 = Turno.objects.create(
        usuario_id = usuario5.id_usuario,
        estudio_id = estudio33.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio33.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio33.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio33.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio33.estado = EstadoEstudio.REALIZADA
    estudio33.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio33.id_estudio,
        estado = EstadoEstudio.REALIZADA,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )
    transportista_view.agregar_estudio_a_pedido(estudio33.id_estudio)

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio33.estado = EstadoEstudio.CENTRALIZADA
    estudio33.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio33.id_estudio,
        estado = EstadoEstudio.CENTRALIZADA,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )
    estudios_estado.asignar_a_sample_set(estudio33)

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio34 = Estudio.objects.create(
        id_interno="1267_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia5.id_enfermedad,
        paciente_id = paciente5.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar4.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio34.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio34.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio34.estado = EstadoEstudio.PRESUPUESTADO
    estudio34.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio34.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio34.estado = EstadoEstudio.PAGADO
    estudio34.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio34.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio34.estado = EstadoEstudio.AUTORIZADO
    estudio34.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio34.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio34 = Turno.objects.create(
        usuario_id = usuario5.id_usuario,
        estudio_id = estudio34.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio34.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio34.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio34.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio35 = Estudio.objects.create(
        id_interno="1268_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia2.id_enfermedad,
        paciente_id = paciente6.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar5.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio35.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio35.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio35.estado = EstadoEstudio.PRESUPUESTADO
    estudio35.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio35.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio35.estado = EstadoEstudio.CANCELADO
    estudio35.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio35.id_estudio,
        estado = EstadoEstudio.CANCELADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio36 = Estudio.objects.create(
        id_interno="1269_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia3.id_enfermedad,
        paciente_id = paciente9.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar6.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio36.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio36.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio36.estado = EstadoEstudio.PRESUPUESTADO
    estudio36.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio36.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio36.estado = EstadoEstudio.PAGADO
    estudio36.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio36.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio36.estado = EstadoEstudio.AUTORIZADO
    estudio36.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio36.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio36 = Turno.objects.create(
        usuario_id = usuario9.id_usuario,
        estudio_id = estudio36.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio36.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio36.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio36.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio36.estado = EstadoEstudio.REALIZADA
    estudio36.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio36.id_estudio,
        estado = EstadoEstudio.REALIZADA,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )
    transportista_view.agregar_estudio_a_pedido(estudio36.id_estudio)

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio36.estado = EstadoEstudio.CENTRALIZADA
    estudio36.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio36.id_estudio,
        estado = EstadoEstudio.CENTRALIZADA,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )
    estudios_estado.asignar_a_sample_set(estudio36)

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio37 = Estudio.objects.create(
        id_interno="1270_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia4.id_enfermedad,
        paciente_id = paciente7.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar7.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio37.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio37.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio37.estado = EstadoEstudio.PRESUPUESTADO
    estudio37.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio37.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio37.estado = EstadoEstudio.PAGADO
    estudio37.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio37.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio37.estado = EstadoEstudio.AUTORIZADO
    estudio37.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio37.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio37 = Turno.objects.create(
        usuario_id = usuario7.id_usuario,
        estudio_id = estudio37.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro2.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio37.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio37.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio37.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio37.estado = EstadoEstudio.REALIZADA
    estudio37.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio37.id_estudio,
        estado = EstadoEstudio.REALIZADA,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )
    transportista_view.agregar_estudio_a_pedido(estudio37.id_estudio)

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio37.estado = EstadoEstudio.CENTRALIZADA
    estudio37.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio37.id_estudio,
        estado = EstadoEstudio.CENTRALIZADA,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )
    estudios_estado.asignar_a_sample_set(estudio37)

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio37.estado = EstadoEstudio.ENVIADA_EXTERIOR
    estudio37.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio37.id_estudio,
        estado = EstadoEstudio.ENVIADA_EXTERIOR,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio37.resultado = "positivo"
    estudio37.estado = EstadoEstudio.FINALIZADO
    estudio37.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio37.id_estudio,
        estado = EstadoEstudio.FINALIZADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio38 = Estudio.objects.create(
        id_interno="1271_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia5.id_enfermedad,
        paciente_id = paciente8.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar8.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio38.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio38.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio38.estado = EstadoEstudio.PRESUPUESTADO
    estudio38.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio38.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio38.estado = EstadoEstudio.PAGADO
    estudio38.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio38.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio38.estado = EstadoEstudio.AUTORIZADO
    estudio38.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio38.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio38 = Turno.objects.create(
        usuario_id = usuario8.id_usuario,
        estudio_id = estudio38.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro2.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio38.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio38.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio38.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio38.estado = EstadoEstudio.REALIZADA
    estudio38.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio38.id_estudio,
        estado = EstadoEstudio.REALIZADA,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )
    transportista_view.agregar_estudio_a_pedido(estudio38.id_estudio)

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio38.estado = EstadoEstudio.CENTRALIZADA
    estudio38.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio38.id_estudio,
        estado = EstadoEstudio.CENTRALIZADA,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )
    estudios_estado.asignar_a_sample_set(estudio38)

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio38.estado = EstadoEstudio.ENVIADA_EXTERIOR
    estudio38.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio38.id_estudio,
        estado = EstadoEstudio.ENVIADA_EXTERIOR,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio39 = Estudio.objects.create(
        id_interno="1272_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia2.id_enfermedad,
        paciente_id = paciente5.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar9.lugar_id
    )
    

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio39.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )

    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio39.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio39.estado = EstadoEstudio.PRESUPUESTADO
    estudio39.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio39.id_estudio,
        estado = EstadoEstudio.PRESUPUESTADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio39.estado = EstadoEstudio.PAGADO
    estudio39.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio39.id_estudio,
        estado = EstadoEstudio.PAGADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio39.estado = EstadoEstudio.AUTORIZADO
    estudio39.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio39.id_estudio,
        estado = EstadoEstudio.AUTORIZADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random_ex
    )

    turno_estudio39 = Turno.objects.create(
        usuario_id = usuario5.id_usuario,
        estudio_id = estudio39.id_estudio,
        fecha = fecha_fin_random_ex + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0),
        consentimiento = "consentimientos/Consentimiento_Informado.pdf"
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio39.estado = EstadoEstudio.TURNO_CONFIRMADO
    estudio39.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio39.id_estudio,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio39.estado = EstadoEstudio.REALIZADA
    estudio39.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio39.id_estudio,
        estado = EstadoEstudio.REALIZADA,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )
    transportista_view.agregar_estudio_a_pedido(estudio39.id_estudio)

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_fin_random_ex + timedelta(num_random)
    estudio39.estado = EstadoEstudio.CENTRALIZADA
    estudio39.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio39.id_estudio,
        estado = EstadoEstudio.CENTRALIZADA,
        fecha_inicio = fecha_fin_random_ex,
        fecha_fin = fecha_fin_random
    )
    estudios_estado.asignar_a_sample_set(estudio39)

    num_random = random.randint(0, 10)
    fecha_fin_random_ex = fecha_fin_random + timedelta(num_random)
    estudio39.estado = EstadoEstudio.ENVIADA_EXTERIOR
    estudio39.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio39.id_estudio,
        estado = EstadoEstudio.ENVIADA_EXTERIOR,
        fecha_inicio = fecha_fin_random,
        fecha_fin = fecha_fin_random_ex
    )

    fecha_random = generar_fecha_aleatoria("2024-05-01", "2024-12-31")
    fecha_aleatoria = fecha_random.strftime("%Y-%m-%d")
    #Crear Estudios y Presupuestos
    estudio40 = Estudio.objects.create(
        id_interno="1273_LIR_PED",
        fecha=fecha_aleatoria,
        tipo_estudio="Exoma",
        patologia_id = patologia3.id_enfermedad,
        paciente_id = paciente6.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0,
        lugar_id = lugar10.lugar_id
    )
    
    presupuesto = Presupuesto.objects.create(
        estudio_id = estudio40.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    num_random = random.randint(0, 10)
    fecha_fin_random = fecha_random + timedelta(num_random)
    HistorialEstudio.objects.create(
        estudio_id = estudio40.id_estudio,
        estado = EstadoEstudio.INICIADO,
        fecha_inicio = fecha_random,
        fecha_fin = fecha_fin_random
    )