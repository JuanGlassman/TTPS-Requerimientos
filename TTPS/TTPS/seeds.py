from estudios.models import Estudio, EstadoEstudio, Enfermedad
from inicio_sesion.models import Rol, Usuario
from pacientes.models import Paciente
from medicos.models import Medico
from lab_admin.models import Presupuesto
from lab_admin.models import LabAdmin
from transportista.models import Transportista, HojaDeRuta, Pedido
from lab_admin.models import Centro, Turno
from datetime import date, time, timedelta

def run_seeds():
    centro1 = Centro.objects.create(
        nombre = "Diagnosticos Cipriano",
        direccion = "Calle 9 777",
        longitud = -57.953714, 
        latitud = -34.915258,
        telefono = "221-123456",
        email = "diagnoslp@email.com"
    )

    centro2 = Centro.objects.create(
        nombre = "Laboratorio de Analisis",
        direccion = "Calle 71 301",
        longitud = -57.923714,
        latitud = -34.925258,
        telefono = "221-123456",
        email = "labanal@email.com"
    )

    centro3 = Centro.objects.create(
        nombre = "Extraccion de sangre",
        direccion = "Avenida 13 1486",
        longitud = -57.944586953543435,
        latitud = -34.92836420212585,
        telefono = "221-123456",
        email = "extracsang@email.com"
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

    #Crear Estudios y Presupuestos
    estudio1 = Estudio.objects.create(
        id_interno="1234_LIR_ROD",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id = patologia1.id_enfermedad,
        paciente_id = paciente1.id_paciente,
        medico_id = medico.id_medico, 
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0
    )

    presupuesto1 = Presupuesto.objects.create(
        estudio_id = estudio1.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    estudio2 = Estudio.objects.create(
        id_interno="1245_LIR_ROD",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia1.id_enfermedad,
        paciente_id = paciente1.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.FINALIZADO,
        tipo_sospecha = 0
    )

    turno_estudio2 = Turno.objects.create(
        usuario_id = usuario1.id_usuario,
        estudio_id = estudio2.id_estudio,
        fecha = date.today() + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0)
    )

    presupuesto2 = Presupuesto.objects.create(
        estudio_id = estudio2.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    estudio3 = Estudio.objects.create(
        id_interno="1245_LIR_ROD",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id = patologia3.id_enfermedad,
        paciente_id = paciente1.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.CANCELADO,
        tipo_sospecha = 0
    )

    presupuesto3 = Presupuesto.objects.create(
        estudio_id = estudio3.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    estudio4 = Estudio.objects.create(
        id_interno="5965_VER_SOF",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia4.id_enfermedad,
        paciente_id = paciente2.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.PRESUPUESTADO,
        tipo_sospecha = 0
    )

    presupuesto4 = Presupuesto.objects.create(
        estudio_id = estudio4.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    estudio5 = Estudio.objects.create(
        id_interno="1275_REY_VAL",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia2.id_enfermedad,
        paciente_id = paciente3.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.PAGADO,
        tipo_sospecha = 0
    )

    presupuesto5 = Presupuesto.objects.create(
        estudio_id = estudio5.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    estudio6 = Estudio.objects.create(
        id_interno="1275_CEN_RUB",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia1.id_enfermedad,
        paciente_id = paciente4.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.AUTORIZADO,
        tipo_sospecha = 0
    )

    turno_estudio6 = Turno.objects.create(
        usuario_id = usuario4.id_usuario,
        estudio_id = estudio6.id_estudio,
        fecha = date.today() + timedelta(days=5),
        centro_id = centro2.id_centro,
        horario = time(hour=14, minute=30, second=0)
    )

    presupuesto6 = Presupuesto.objects.create(
        estudio_id = estudio6.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    estudio7 = Estudio.objects.create(
        id_interno="1275_LIR_VAL",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia5.id_enfermedad,
        paciente_id = paciente5.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        tipo_sospecha = 0
    )

    turno_estudio7 = Turno.objects.create(
        usuario_id = usuario5.id_usuario,
        estudio_id = estudio7.id_estudio,
        fecha = date.today() + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0)
    )

    presupuesto7 = Presupuesto.objects.create(
        estudio_id = estudio7.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    estudio8 = Estudio.objects.create(
        id_interno="1275_LIR_ROD",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia2.id_enfermedad,
        paciente_id = paciente6.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.REALIZADA,
        tipo_sospecha = 0
    )

    turno_estudio8 = Turno.objects.create(
        usuario_id = usuario6.id_usuario,
        estudio_id = estudio8.id_estudio,
        fecha = date.today() + timedelta(days=5),
        centro_id = centro2.id_centro,
        horario = time(hour=14, minute=30, second=0)
    )

    presupuesto8 = Presupuesto.objects.create(
        estudio_id = estudio8.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    estudio9 = Estudio.objects.create(
        id_interno="1275_HUM_ROD",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia1.id_enfermedad,
        paciente_id = paciente8.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.CENTRALIZADA,
        tipo_sospecha = 0
    )

    turno_estudio9 = Turno.objects.create(
        usuario_id = usuario8.id_usuario,
        estudio_id = estudio9.id_estudio,
        fecha = date.today() + timedelta(days=5),
        centro_id = centro2.id_centro,
        horario = time(hour=14, minute=30, second=0)
    )

    presupuesto9 = Presupuesto.objects.create(
        estudio_id = estudio9.id_estudio,
        costo_exoma = 500,
        total = 500.0
    )

    estudio10 = Estudio.objects.create(
        id_interno="1275_LIR_ROD",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id = patologia1.id_enfermedad,
        paciente_id = paciente7.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.ENVIADA_EXTERIOR,
        tipo_sospecha = 0
    )

    turno_estudio10 = Turno.objects.create(
        usuario_id = usuario7.id_usuario,
        estudio_id = estudio10.id_estudio,
        fecha = date.today() + timedelta(days=5),
        centro_id = centro1.id_centro,
        horario = time(hour=14, minute=30, second=0)
    )

    presupuesto10 = Presupuesto.objects.create(
        estudio_id = estudio10.id_estudio,
        costo_exoma = 500,
        total = 500.0
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

    # Crear estudios en estado PAGADO
    estudio_pagado1 = Estudio.objects.create(
        id_interno="2345_FER_MAT",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id= patologia2.id_enfermedad,
        paciente_id=paciente10.id_paciente,
        medico_id=medico.id_medico,
        estado=EstadoEstudio.PAGADO,
        tipo_sospecha=0
    )
    presupuesto_pagado1 = Presupuesto.objects.create(
        estudio_id=estudio_pagado1.id_estudio,
        costo_exoma=500,
        total = 500.0
    )

    estudio_pagado2 = Estudio.objects.create(
        id_interno="2346_GOM_LUC",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id= patologia3.id_enfermedad,
        paciente_id=paciente11.id_paciente,
        medico_id=medico.id_medico,
        estado=EstadoEstudio.PAGADO,
        tipo_sospecha=0
    )
    presupuesto_pagado2 = Presupuesto.objects.create(
        estudio_id=estudio_pagado2.id_estudio,
        costo_exoma=500,
        total = 500.0
    )

    estudio_pagado3 = Estudio.objects.create(
        id_interno="2348_RIO_MAR",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia4.id_enfermedad,
        paciente_id=paciente14.id_paciente,
        medico_id=medico.id_medico,
        estado=EstadoEstudio.PAGADO,
        tipo_sospecha=0
    )
    presupuesto_pagado3 = Presupuesto.objects.create(
        estudio_id=estudio_pagado3.id_estudio,
        costo_exoma=500,
        total = 500.0
    )

    # Crear estudios en estado REALIZADA y sus turnos
    estudio_realizado1 = Estudio.objects.create(
        id_interno="2347_LOP_AND",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id = patologia4.id_enfermedad,
        paciente_id=paciente12.id_paciente,
        medico_id=medico.id_medico,
        estado=EstadoEstudio.REALIZADA,
        tipo_sospecha=0
    )
    turno_realizado1 = Turno.objects.create(
        usuario_id=paciente12.usuario.id_usuario,
        estudio_id=estudio_realizado1.id_estudio,
        fecha=date.today() - timedelta(days=2),
        centro_id=centro1.id_centro,
        horario=time(hour=9, minute=30)
    )

    estudio_realizado2 = Estudio.objects.create(
        id_interno="2348_PER_JUA",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia5.id_enfermedad,
        paciente_id=paciente13.id_paciente,
        medico_id=medico.id_medico,
        estado=EstadoEstudio.REALIZADA,
        tipo_sospecha=0
    )
    turno_realizado2 = Turno.objects.create(
        usuario_id=paciente13.usuario.id_usuario,
        estudio_id=estudio_realizado2.id_estudio,
        fecha=date.today() - timedelta(days=2),
        centro_id=centro2.id_centro,
        horario=time(hour=10, minute=45)
    )

    estudio_realizado3 = Estudio.objects.create(
        id_interno="2349_MAR_CAR",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia1.id_enfermedad,
        paciente_id=paciente15.id_paciente,
        medico_id=medico.id_medico,
        estado=EstadoEstudio.REALIZADA,
        tipo_sospecha=0
    )
    turno_realizado3 = Turno.objects.create(
        usuario_id=paciente13.usuario.id_usuario,
        estudio_id=estudio_realizado3.id_estudio,
        fecha=date.today() - timedelta(days=2),
        centro_id=centro2.id_centro,
        horario=time(hour=11, minute=00)
    )

    estudio_realizado4 = Estudio.objects.create(
        id_interno="2350_FER_PAU",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia3.id_enfermedad,
        paciente_id=paciente16.id_paciente,
        medico_id=medico.id_medico,
        estado=EstadoEstudio.REALIZADA,
        tipo_sospecha=0
    )
    turno_realizado4 = Turno.objects.create(
        usuario_id=paciente13.usuario.id_usuario,
        estudio_id=estudio_realizado4.id_estudio,
        fecha=date.today() - timedelta(days=2),
        centro_id=centro2.id_centro,
        horario=time(hour=11, minute=15)
    )

    estudio_realizado5 = Estudio.objects.create(
        id_interno="2351_GAR_MAR",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia3.id_enfermedad,
        paciente_id=paciente17.id_paciente,
        medico_id=medico.id_medico,
        estado=EstadoEstudio.REALIZADA,
        tipo_sospecha=0
    )
    turno_realizado5 = Turno.objects.create(
        usuario_id=paciente13.usuario.id_usuario,
        estudio_id=estudio_realizado5.id_estudio,
        fecha=date.today() - timedelta(days=2),
        centro_id=centro2.id_centro,
        horario=time(hour=11, minute=15)
    )

    estudio_realizado6 = Estudio.objects.create(
        id_interno="2352_LUN_JUA",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia5.id_enfermedad,
        paciente_id=paciente18.id_paciente,
        medico_id=medico.id_medico,
        estado=EstadoEstudio.REALIZADA,
        tipo_sospecha=0
    )
    turno_realizado6 = Turno.objects.create(
        usuario_id=paciente13.usuario.id_usuario,
        estudio_id=estudio_realizado6.id_estudio,
        fecha=date.today() - timedelta(days=2),
        centro_id=centro2.id_centro,
        horario=time(hour=11, minute=15)
    )

    estudio_realizado7 = Estudio.objects.create(
        id_interno="2353_MOR_GUS",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia1.id_enfermedad,
        paciente_id=paciente19.id_paciente,
        medico_id=medico.id_medico,
        estado=EstadoEstudio.REALIZADA,
        tipo_sospecha=0
    )
    turno_realizado7 = Turno.objects.create(
        usuario_id=paciente13.usuario.id_usuario,
        estudio_id=estudio_realizado7.id_estudio,
        fecha=date.today() - timedelta(days=2),
        centro_id=centro2.id_centro,
        horario=time(hour=11, minute=15)
    )

    estudio_realizado8 = Estudio.objects.create(
        id_interno="2354_VEG_MAR",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia_id=patologia2.id_enfermedad,
        paciente_id=paciente20.id_paciente,
        medico_id=medico.id_medico,
        estado=EstadoEstudio.REALIZADA,
        tipo_sospecha=0
    )
    turno_realizado8 = Turno.objects.create(
        usuario_id=paciente13.usuario.id_usuario,
        estudio_id=estudio_realizado8.id_estudio,
        fecha=date.today() - timedelta(days=2),
        centro_id=centro2.id_centro,
        horario=time(hour=11, minute=15)
    )

    # Crear pedidos manualmente
    pedido1 = Pedido.objects.create(
        centro_id=centro1.id_centro,
        estado="pendiente"
    )
    pedido1.estudios.add(estudio_realizado1, estudio_realizado3, estudio_realizado5)

    pedido2 = Pedido.objects.create(
        centro_id=centro2.id_centro,
        estado="pendiente"
    )
    pedido2.estudios.add(estudio_realizado2, estudio_realizado4, estudio_realizado6)

    pedido3 = Pedido.objects.create(
        centro_id=centro3.id_centro,
        estado="pendiente"
    )
    pedido3.estudios.add(estudio_realizado8, estudio_realizado7)

    # Crear hoja de ruta manualmente
    hoja_de_ruta = HojaDeRuta.objects.create(
        fecha=date.today(),
        transportista_id=transportista.id_transportista,
        estado="pendiente"
    )
    hoja_de_ruta.pedidos.add(pedido1, pedido2, pedido3)