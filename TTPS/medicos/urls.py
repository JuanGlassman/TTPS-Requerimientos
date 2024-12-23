from django.contrib import admin
from django.urls import path, include
from . import views
from medicos import views as medico_view

app_name = 'medicos'

urlpatterns = [
    path("pacientes/", medico_view.pacientes, name="listar_pacientes"),
    path("iniciar_estudio/", medico_view.iniciar_estudio, name="iniciar_estudio"),
    path("iniciar_estudio/<int:paciente_id>/", medico_view.iniciar_estudio_paciente, name="iniciar_estudio_paciente"),
    path("estudios_paciente/<int:paciente_id>/", medico_view.estudios_paciente, name="estudios_paciente"),
    path("crear_paciente/", views.crear_paciente, name="crear_paciente"),
    path('editar_paciente/<int:id_paciente>/', views.editar_paciente, name='editar_paciente')
]