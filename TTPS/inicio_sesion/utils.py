PERMISOS = [
    "lista_usuarios", "lista_medicos", "medico_create", "medico_update", "medico_destroy",
    "lista_lab_admin", "lab_admin_create", "lab_admin_update", "lab_admin_destroy",
    "lista_pacientes", "paciente_create", "paciente_update", "paciente_destroy", "paciente_show",
    "iniciar_estudio", "historial_estudios_paciente", "estudio_show", "elegir_turno", "dar_concentimiento"
    "gestionar_muestras", "actualizar_estado_muestra", "cambiar_estado", 
    "cargar_muestra", "lista_sample_set", "enviar_sample_set", 
    "lista_estudios_set", "eliminar_estudios_set", "agregar_estudios_set", 
    "lista_centros", "centro_create", "centro_update", "centro_destroy",
    "lista_usuarios", "usuario_create", "usuario_update", "usuario_destroy", 
    "transportista", "pedido_create", "ruta_create", "pedido_update", "ruta_update"
]


PERMISOS_POR_ROL = {
    "system_admin": [
        "lista_usuarios", "lista_medicos", "medico_create", "medico_update", "medico_destroy",
        "lista_lab_admin", "lab_admin_create", "lab_admin_update", "lab_admin_destroy",
        "lista_pacientes", "paciente_create", "paciente_update", "paciente_destroy", "paciente_show",
        "iniciar_estudio", "historial_estudios_paciente", "estudio_show"
        "gestionar_muestras", "actualizar_estado_muestra", "cambiar_estado", 
        "cargar_muestra", "lista_sample_set", "enviar_sample_set", 
        "lista_estudios_set", "eliminar_estudios_set", "agregar_estudios_set",
        "lista_centros", "centro_create", "centro_update", "centro_destroy",
        "lista_usuarios", "usuario_create", "usuario_update", "usuario_destroy",
        "pedido_create", "ruta_create", "pedido_update", "ruta_update",
    ],
    "lab_admin": [
        "lista_medicos", "medico_create", "medico_update", "medico_destroy",
        "gestionar_muestras", "actualizar_estado_muestra", "cambiar_estado", 
        "cargar_muestra", "lista_sample_set", "enviar_sample_set", 
        "lista_estudios_set", "eliminar_estudios_set", "agregar_estudios_set", 
        "pedido_create", "ruta_create", "pedido_update", "ruta_update",
        "presupuestar", "pagar_estudio", "cancelar_estudio", "cargar_resultado"
    ],
    "medico": [
        "lista_pacientes", "paciente_create", "paciente_update", "paciente_destroy", "paciente_show",
        "iniciar_estudio", "historial_estudios_paciente", "estudio_show", "usuario_create"
    ],
    "paciente": [
        "historial_estudios_paciente", "elegir_turno", "estudio_show", "dar_concentimiento", "nav_bar_mis_estudios"
    ],
    "transportista": [
        "transportista"
    ]
}