from estudios.models import Estudio, EstadoEstudio, HistorialEstudio
from inicio_sesion.models import Rol, Usuario
from pacientes.models import Paciente
from medicos.models import Medico
from lab_admin.models import Presupuesto
from datetime import date
def run_seeds():

    rolPaciente = Rol.objects.create(
        nombre = "Paciente"
    )

    rolMedico = Rol.objects.create(
        nombre = "Medico"
    )

    #region Usuarios
    usuarioMedico = Usuario.objects.create(
        dni = 25652587,
        first_name = "Osvaldo",
        last_name = "Dario",
        fecha_nacimiento = "1985-05-05",
        genero = "M",
        rol_id = rolMedico.id_rol
    )

    medico = Medico.objects.create(
        usuario_id = usuarioMedico.id_usuario
    )

    usuario1 = Usuario.objects.create(
        username="rodri",
        password="1234",
        email="rodri@email.com",
        dni = 25489631,
        first_name = "Rodrigo",
        last_name = "Lira",
        fecha_nacimiento = "2002-05-05",
        genero = "M",
        rol_id = rolPaciente.id_rol
    )

    usuario2 = Usuario.objects.create(
        username = "sofi",
        password="1234",
        email="sofi@email.com",
        dni = 33742169,
        first_name = "Sofia",
        last_name = "Vera",
        fecha_nacimiento = "2002-05-05",
        genero = "F",
        rol_id = rolPaciente.id_rol
    )

    usuario3 = Usuario.objects.create(        
        username = "valeria",
        password="1234",
        email="valeria@email.com",
        dni = 40158923,
        first_name = "Valeria",
        last_name = "Reyes",
        fecha_nacimiento = "1998-05-05",
        genero = "F",
        rol_id = rolPaciente.id_rol
    )

    usuario4 = Usuario.objects.create(        
        username="ruben",
        password="1234",
        email="ruben@email.com",
        dni = 28967435,
        first_name = "Ruben",
        last_name = "Centurión",
        fecha_nacimiento = "1995-05-05",
        genero = "M",
        rol_id = rolPaciente.id_rol
    )

    usuario5 = Usuario.objects.create(
        username="valentin",
        password="1234",
        email="valentin@email.com",
        dni = 35714982,
        first_name = "Valentin",
        last_name = "Lira",
        fecha_nacimiento = "1995-05-05",
        genero = "M",
        rol_id = rolPaciente.id_rol
    )

    usuario6 = Usuario.objects.create(
        username="valerio",
        password="1234",
        email="valerio@email.com",
        dni = 31598746,
        first_name = "Valerio",
        last_name = "Lira",
        fecha_nacimiento = "1995-05-05",
        genero = "M",
        rol_id = rolPaciente.id_rol
    )

    usuario7 = Usuario.objects.create(
        username="valentina",
        password="1234",
        email="valentina@email.com",
        dni = 38245917,
        first_name = "Valentina",
        last_name = "Lira",
        fecha_nacimiento = "1995-05-05",
        genero = "F",
        rol_id = rolPaciente.id_rol
    )

    usuario8 = Usuario.objects.create(
        username="rodolfo",
        password="1234",
        email="rodolfo@email.com",
        dni = 38288917,
        first_name = "Rodolfo",
        last_name = "Humme",
        fecha_nacimiento = "1995-05-05",
        genero = "M",
        rol_id = rolPaciente.id_rol
    )

    usuario9 = Usuario.objects.create(
        username="fidel",
        password="1234",
        email="fidel@email.com",
        dni = 38282827,
        first_name = "Fidel",
        last_name = "Alvarez",
        fecha_nacimiento = "1999-11-05",
        genero = "M",
        rol_id = rolPaciente.id_rol
    )
    #endregion

    #region Pacientes
    paciente1 = Paciente.objects.create(
        usuario_id = usuario1.id_usuario
    )
    paciente2 = Paciente.objects.create(
        usuario_id = usuario2.id_usuario
    )
    paciente3 = Paciente.objects.create(
        usuario_id = usuario3.id_usuario
    )
    paciente4 = Paciente.objects.create(
        usuario_id = usuario4.id_usuario
    )
    paciente5 = Paciente.objects.create(
        usuario_id = usuario5.id_usuario
    )
    paciente6 = Paciente.objects.create(
        usuario_id = usuario6.id_usuario
    )
    paciente7 = Paciente.objects.create(
        usuario_id = usuario7.id_usuario
    )
    paciente8 = Paciente.objects.create(
        usuario_id = usuario8.id_usuario
    )
    paciente9 = Paciente.objects.create(
        usuario_id = usuario9.id_usuario
    )
    #endregion

    #region Estudios y Presupuestos
    estudio1 = Estudio.objects.create(
        id_interno="1234_LIR_ROD",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia="patologia1",
        paciente_id = paciente1.id_paciente,
        medico_id = medico.id_medico, 
        estado = EstadoEstudio.INICIADO,
        tipo_sospecha = 0
    )

    presupuesto1 = Presupuesto.objects.create(
        estudio_id = estudio1.id_estudio,
        costo_exoma = 500
    )

    estudio2 = Estudio.objects.create(
        id_interno="1245_LIR_ROD",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia="patologia1",
        paciente_id = paciente1.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.FINALIZADO,
        tipo_sospecha = 0
    )

    presupuesto2 = Presupuesto.objects.create(
        estudio_id = estudio2.id_estudio,
        costo_exoma = 500
    )

    estudio3 = Estudio.objects.create(
        id_interno="1245_LIR_ROD",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia="patologia3",
        paciente_id = paciente1.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.CANCELADO,
        tipo_sospecha = 0
    )

    presupuesto3 = Presupuesto.objects.create(
        estudio_id = estudio3.id_estudio,
        costo_exoma = 500
    )

    estudio4 = Estudio.objects.create(
        id_interno="5965_VER_SOF",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia="patologia4",
        paciente_id = paciente2.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.PRESUPUESTADO,
        tipo_sospecha = 0
    )

    presupuesto4 = Presupuesto.objects.create(
        estudio_id = estudio4.id_estudio,
        costo_exoma = 500
    )

    estudio5 = Estudio.objects.create(
        id_interno="1275_REY_VAL",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia="patologia1",
        paciente_id = paciente3.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.PAGADO,
        tipo_sospecha = 0
    )

    presupuesto5 = Presupuesto.objects.create(
        estudio_id = estudio5.id_estudio,
        costo_exoma = 500
    )

    estudio6 = Estudio.objects.create(
        id_interno="1275_CEN_RUB",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia="patologia1",
        paciente_id = paciente4.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.AUTORIZADO,
        tipo_sospecha = 0
    )

    presupuesto6 = Presupuesto.objects.create(
        estudio_id = estudio6.id_estudio,
        costo_exoma = 500
    )

    estudio7 = Estudio.objects.create(
        id_interno="1275_LIR_VAL",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia="patologia1",
        paciente_id = paciente5.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.TURNO_CONFIRMADO,
        tipo_sospecha = 0
    )

    presupuesto7 = Presupuesto.objects.create(
        estudio_id = estudio7.id_estudio,
        costo_exoma = 500
    )

    estudio8 = Estudio.objects.create(
        id_interno="1275_LIR_ROD",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia="patologia1",
        paciente_id = paciente6.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.REALIZADA,
        tipo_sospecha = 0
    )

    presupuesto8 = Presupuesto.objects.create(
        estudio_id = estudio8.id_estudio,
        costo_exoma = 500
    )

    estudio9 = Estudio.objects.create(
        id_interno="1275_HUM_ROD",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia="patologia8",
        paciente_id = paciente8.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.CENTRALIZADA,
        tipo_sospecha = 0
    )

    presupuesto9 = Presupuesto.objects.create(
        estudio_id = estudio9.id_estudio,
        costo_exoma = 500
    )

    estudio10 = Estudio.objects.create(
        id_interno="1275_LIR_ROD",
        fecha=date.today(),
        tipo_estudio="Exoma",
        patologia="patologia1",
        paciente_id = paciente7.id_paciente,
        medico_id = medico.id_medico,
        estado = EstadoEstudio.ENVIADA_EXTERIOR,
        tipo_sospecha = 0
    )

    presupuesto10 = Presupuesto.objects.create(
        estudio_id = estudio10.id_estudio,
        costo_exoma = 500
    )

    #endregion