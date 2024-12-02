from django.urls import path
from pacientes import views as paciente_view

app_name = 'pacientes'

urlpatterns = [
    path("ver_detalle/<int:paciente_id>/", paciente_view.paciente_detalle, name="paciente_detalle"),
    path("mis_estudios/", paciente_view.mis_estudios, name="historial_estudios_paciente"),
    path("turnos/sacar_turno/<int:id_estudio>/", paciente_view.sacar_turno, name="sacar_turno"),
    path("turnos/confirmacion_turno/<int:turno_id>/", paciente_view.confirmacion_turno, name="confirmacion_turno"),
    path('turnos/obtener_horarios_disponibles/', paciente_view.obtener_horarios_disponibles, name='obtener_horarios_disponibles'),
    path('turnos/descargar_consentimiento/', paciente_view.descargar_consentimiento, name='descargar_consentimiento'),
]